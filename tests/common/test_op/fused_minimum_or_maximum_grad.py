# Copyright 2019 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""fused_minimum_or_maximum_grad"""
import akg
import akg.lang.cce.te_compute.util as akg_compute_util
from akg import topi, tvm
from akg.ops.math import sum
from akg.ops.math.cast import cast
from akg.utils import kernel_exec as utils
from akg.utils import validation_check as vc_util
from akg.utils.dsl_create import zero_const
from akg.utils.format_transform import get_shape


def get_default_attrs():
    """get default attrs."""
    default_attrs = {
        "enable_post_poly_loop_partition": False,  # speed up compilation
    }
    return default_attrs


@vc_util.check_input_type(tvm.tensor.Tensor, tvm.tensor.Tensor, tvm.tensor.Tensor, bool, bool, str)
def fused_minimum_or_maximum_grad(dz, x, y, grad_x, grad_y, op_type):
    """
    Gradient for minimum or maximum operation between two input tensors `x` and `y`.

    Args:
        dz (tvm.tensor.Tensor): Type float16, float32, int32.
        x (tvm.tensor.Tensor): Type float16, float32, int32.
        y (tvm.tensor.Tensor): Type float16, float32, int32.
        grad_x (bool): Whether calculate dx.
        grad_y (bool): Whether calculate dy.
        op_type (str): The type of the op, "GE" for MaximumGrad or "LE" for MinimumGrad.

    Note:
        At least one of grad_x and grad_y is True.

    Returns:
        dx, tvm.tensor.Tensor of the same type as inputs, it will be returned if grad_x is True.
        dy, tvm.tensor.Tensor of the same type as inputs, it will be returned if grad_y is True.
    """
    vc_util.check_shape(x)
    vc_util.check_shape(y)
    vc_util.check_shape(dz)
    vc_util.ops_dtype_check([x.dtype, y.dtype, dz.dtype],
                            [vc_util.DtypeForDavinci.ALL_FLOAT, vc_util.DtypeForDavinci.INT32])

    vc_util.broadcast_check(x, dz)
    vc_util.broadcast_check(y, dz)

    # check op types
    check_list = ["GE", "LE"]
    if op_type not in check_list:
        raise ValueError("FusedMinimumOrMaximumGrad only support %s while op type is %s" %
                         (",".join(check_list), op_type))

    if not grad_x and not grad_y:
        raise ValueError("At least one of grad_x and grad_y is True.")

    x_shape = get_shape(x)
    y_shape = get_shape(y)
    dz_shape = get_shape(dz)
    ori_dtype = dz.dtype

    # get greater compute
    x = akg.lang.cce.broadcast(x, dz_shape)
    y = akg.lang.cce.broadcast(y, dz_shape)

    if utils.product_is_mini() and ori_dtype != "float16":
        x = cast(x, "float16")
        y = cast(y, "float16")
        dz = cast(dz, "float16")
    elif ori_dtype == "int32":
        x = cast(x, "float32")
        y = cast(y, "float32")
        dz = cast(dz, "float32")
    zero = zero_const(dz.dtype)

    if op_type == "LE":
        dx = tvm.compute(dz_shape, lambda *i: tvm.expr.Select((x(*i) <= y(*i)), dz(*i), zero), name='dx')
        dy = topi.subtract(dz, dx)
    elif op_type == "GE":
        dx = tvm.compute(dz_shape, lambda *i: tvm.expr.Select((x(*i) >= y(*i)), dz(*i), zero), name='dx')
        dy = topi.subtract(dz, dx)

    if dx.dtype == "float16":
        # cast to fp32 for higher precision of reduce_sum.
        if get_shape(dx) != x_shape:
            dx = cast(dx, "float32")
        if get_shape(dy) != y_shape:
            dy = cast(dy, "float32")

    dx = sum.sum_by_shape(dx, x_shape)
    dy = sum.sum_by_shape(dy, y_shape)

    if ori_dtype != dx.dtype:
        dx = cast(dx, ori_dtype)
    if ori_dtype != dy.dtype:
        dy = cast(dy, ori_dtype)

    attrs = get_default_attrs()
    if grad_x and grad_y:
        return dx, dy, attrs
    if grad_x:
        return dx, attrs
    return dy, attrs
