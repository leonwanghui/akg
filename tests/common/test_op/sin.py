# Copyright 2020 Huawei Technologies Co., Ltd
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

"""operator dsl function: sin"""
import akg
from akg import tvm
from akg.utils.format_transform import get_shape
from akg.utils import validation_check as vc_util

# define a string name of "float16"
FLOAT_16 = "float16"
# define a string name of "float32"
FLOAT_32 = "float32"

PI = 3.14159265358979

# the first factor to use Taylor series in circle
FIRST_ORDER = 5
# the last factor to use Taylor series in circle
LAST_ORDER = 13
# the first factor of Taylor series
FIRST_FACTOR = -1.0 / 6.0

def _sin(x):
    """implement of Taylor's formula for sine"""
    input_x_power = akg.lang.cce.vmul(x, x)
    iter_value = akg.lang.cce.vmul(
        akg.lang.cce.vmuls(input_x_power, FIRST_FACTOR), x)
    res = akg.lang.cce.vadd(x, iter_value)

    i = FIRST_ORDER
    while i < LAST_ORDER:
        iter_value = akg.lang.cce.vmuls(
            akg.lang.cce.vmul(input_x_power, iter_value),
                              -1.0 / (i*(i - 1)))
        res = akg.lang.cce.vadd(res, iter_value)
        # add 2 to get the next order
        i = i + 2

    return res


def sin_compute(x):
    """compute for sine"""
    dtype = x.dtype
    shape = get_shape(x)

    # cast to type float32 when type is float16
    if dtype == FLOAT_16:
        x = akg.lang.cce.cast_to(x, FLOAT_32)

    pai_multiple = akg.lang.cce.vmuls(x, 1 / PI)
    round_float = akg.lang.cce.cast_to(
        akg.lang.cce.round(pai_multiple), FLOAT_32)
    # to adjust x to [-pai/2,pai/2]
    x = akg.lang.cce.vsub(x, akg.lang.cce.vmuls(round_float, PI))

    res = _sin(x)

    # if round is odd, the final result need to mutiply -1.
    # Need to multipy 1/2 to get the ceil value
    ceil_value = akg.lang.cce.ceil(akg.lang.cce.vmuls(round_float, 1 / 2))
    # if odd, ceil*2-round is 1,if even, the value is 0
    sub_value = akg.lang.cce.vsub(
        akg.lang.cce.vmuls(ceil_value, tvm.const(2, dtype)), round_float)
    tensor_one = akg.lang.cce.broadcast(tvm.const(1, FLOAT_32), shape)
    odd_tensor = akg.lang.cce.vsub(tensor_one, sub_value)
    even_tensor = akg.lang.cce.vsub(odd_tensor, tensor_one)
    odd_even_tensor = akg.lang.cce.vadd(odd_tensor, even_tensor)
    res = akg.lang.cce.vmul(res, odd_even_tensor)

    # cast the dtype to float16
    if dtype == FLOAT_16:
        res = akg.lang.cce.cast_to(res, FLOAT_16)

    return res

def get_attrs():
    """get attrs."""
    attrs = {
        "enable_feature_library": True
    }
    return attrs

def sin_call(x):
    """compute for sine"""
    dtype = x.dtype
    shape = get_shape(x)

    optimize = False

    # cast to type float32 when type is float16
    if dtype == FLOAT_16:
        x = akg.lang.cce.cast_to(x, FLOAT_32)

    if optimize:
        pai_multiple = akg.lang.cce.vmuls(x, 1 / PI)
        round_float = akg.lang.cce.cast_to(
            akg.lang.cce.round(pai_multiple), FLOAT_32)
        # to adjust x to [-pai/2,pai/2]
        x = akg.lang.cce.vsub(x, akg.lang.cce.vmuls(round_float, PI))

    res = akg.tvm.compute(shape, lambda *indice: akg.lang.cce.sin(x(*indice)), name="res")

    if optimize:
        # if round is odd, the final result need to mutiply -1.
        # Need to multipy 1/2 to get the ceil value
        ceil_value = akg.lang.cce.ceil(akg.lang.cce.vmuls(round_float, 1 / 2))
        # if odd, ceil*2-round is 1,if even, the value is 0
        sub_value = akg.lang.cce.vsub(
            akg.lang.cce.vmuls(ceil_value, tvm.const(2, dtype)), round_float)
        tensor_one = akg.lang.cce.broadcast(tvm.const(1, FLOAT_32), shape)
        odd_tensor = akg.lang.cce.vsub(tensor_one, sub_value)
        even_tensor = akg.lang.cce.vsub(odd_tensor, tensor_one)
        odd_even_tensor = akg.lang.cce.vadd(odd_tensor, even_tensor)
        res = akg.lang.cce.vmul(res, odd_even_tensor)

    # cast the dtype to float16
    if dtype == FLOAT_16:
        res = akg.lang.cce.cast_to(res, FLOAT_16)

    return res, get_attrs()

@vc_util.check_input_type(akg.tvm.tensor.Tensor)
def sin(x):
    """
    Computes sine value of a tensor with Taylor's theorem.

    .. math::
        \\begin{array}{ll} \\\\
            sin(x) = x - \\frac{x^3}{3!} + \\frac{x^5}{5!} + ... +
                (-1)^k \\cdot \\frac{x^{2(k+1)}}{(2(k+1))!}
        \\end{array}

    Args:
        x (tvm.tensor.Tensor): Tensor of type float16, float32.

    Rerurns:
        tvm.tensor.Tensor of same type and shape as in_data.
    """
    vc_util.ops_dtype_check(x.dtype, vc_util.DtypeForDavinci.ALL_FLOAT)
    vc_util.check_shape(x.shape)

    use_call = True
    if use_call:
        return sin_call(x)
    return sin_compute(x)
