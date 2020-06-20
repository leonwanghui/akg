#!/usr/bin/env python3
# coding: utf-8
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

"""operator dsl function: batch_norm_ad"""
import akg
from akg.ops.nn import fused_batch_norm
from akg.utils import custom_tiling as ct_util, validation_check as vc_util

DIM_MAP = {
    str(((32, 128, 7, 7, 16), "float16")):
    ((0, 0, 1, 1), (0, 1, 16, 1), (0, 2, 16, 1), (0, 3, 7, 1), (0, 4, 7, 1),
     (1, 0, 1, 1), (1, 1, 16, 1), (1, 2, 4, 1), (1, 3, 7, 1), (1, 4, 7, 1),
     (2, 0, 1, 1), (2, 1, 16, 1), (2, 2, 1, 1), (2, 3, 7, 1), (2, 4, 7, 1)),

    str(((32, 16, 14, 14, 16), "float16")):
    ((0, 0, 1, 1), (0, 1, 16, 1), (0, 2, 8, 1), (0, 3, 2, 1), (0, 4, 7, 1),
     (1, 0, 1, 1), (1, 1, 16, 1), (1, 2, 16, 1), (1, 3, 1, 1), (1, 4, 14, 1)),

    str(((32, 16, 28, 28, 16), "float16")):
    ((0, 0, 1, 1), (0, 1, 16, 1), (0, 2, 1, 1), (0, 3, 7, 1), (0, 4, 28, 1),
     (1, 0, 1, 1), (1, 1, 16, 1), (1, 2, 1, 1), (1, 3, 2, 1), (1, 4, 28, 1),
     (2, 0, 1, 1), (2, 1, 16, 1), (2, 2, 1, 1), (2, 3, 28, 1), (2, 4, 28, 1)),

    str(((32, 16, 56, 56, 16), "float16")):
    ((0, 0, 1, 1), (0, 1, 16, 1), (0, 2, 16, 1), (0, 3, 7, 1), (0, 4, 7, 1),
     (1, 0, 1, 1), (1, 1, 16, 1), (1, 2, 4, 1), (1, 3, 7, 1), (1, 4, 14, 1),
     (2, 0, 1, 1), (2, 1, 16, 1), (2, 2, 1, 1), (2, 3, 7, 1), (2, 4, 7, 1)),

    str(((32, 32, 14, 14, 16), "float16")):
    ((0, 0, 1, 1), (0, 1, 16, 1), (0, 2, 4, 1), (0, 3, 14, 1), (0, 4, 14, 1),
     (1, 0, 1, 1), (1, 1, 16, 1), (1, 2, 1, 1), (1, 3, 14, 1), (1, 4, 14, 1),
     (2, 0, 1, 1), (2, 1, 16, 1), (2, 2, 1, 1), (2, 3, 2, 1), (2, 4, 14, 1)),

    str(((32, 32, 28, 28, 16), "float16")):
    ((0, 0, 1, 1), (0, 1, 16, 1), (0, 2, 1, 1), (0, 3, 7, 1), (0, 4, 28, 1),
     (1, 0, 1, 1), (1, 1, 16, 1), (1, 2, 1, 1), (1, 3, 2, 1), (1, 4, 28, 1),
     (2, 0, 1, 1), (2, 1, 16, 1), (2, 2, 1, 1), (2, 3, 28, 1), (2, 4, 28, 1)),

    str(((32, 32, 7, 7, 16), "float16")):
    ((0, 0, 1, 1), (0, 1, 16, 1), (0, 2, 16, 1), (0, 3, 1, 1), (0, 4, 14, 1),
     (1, 0, 1, 1), (1, 1, 16, 1), (1, 2, 32, 1), (1, 3, 1, 1), (1, 4, 7, 1)),

    str(((32, 4, 112, 112, 16), "float16")):
    ((0, 0, 1, 1), (0, 1, 16, 1), (0, 2, 2, 1), (0, 3, 16, 1), (0, 4, 4, 1),
     (1, 0, 1, 1), (1, 1, 16, 1), (1, 2, 4, 1), (1, 3, 56, 1), (1, 4, 1, 1)),

    str(((32, 4, 56, 56, 16), "float16")):
    ((0, 0, 1, 1), (0, 1, 16, 1), (0, 2, 2, 1), (0, 3, 16, 1), (0, 4, 4, 1),
     (1, 0, 1, 1), (1, 1, 16, 1), (1, 2, 4, 1), (1, 3, 56, 1), (1, 4, 1, 1)),

    str(((32, 64, 14, 14, 16), "float16")):
    ((0, 0, 1, 1), (0, 1, 16, 1), (0, 2, 1, 1), (0, 3, 14, 1), (0, 4, 14, 1),
     (1, 0, 1, 1), (1, 1, 16, 1), (1, 2, 1, 1), (1, 3, 2, 1), (1, 4, 4, 1),
     (2, 0, 1, 1), (2, 1, 16, 1), (2, 2, 4, 1), (2, 3, 14, 1), (2, 4, 14, 1)),

    str(((32, 8, 28, 28, 16), "float16")):
    ((0, 0, 1, 1), (0, 1, 16, 1), (0, 2, 1, 1), (0, 3, 7, 1), (0, 4, 28, 1),
     (1, 0, 1, 1), (1, 1, 16, 1), (1, 2, 1, 1), (1, 3, 2, 1), (1, 4, 28, 1),
     (2, 0, 1, 1), (2, 1, 16, 1), (2, 2, 1, 1), (2, 3, 28, 1), (2, 4, 28, 1)),

    str(((32, 8, 56, 56, 16), "float16")):
    ((0, 0, 1, 1), (0, 1, 16, 1), (0, 2, 1, 1), (0, 3, 14, 1), (0, 4, 56, 1),
     (1, 0, 1, 1), (1, 1, 16, 1), (1, 1, 1, 1), (1, 3, 4, 1), (1, 4, 56, 1),
     (2, 0, 1, 1), (2, 1, 16, 1), (2, 1, 1, 1), (2, 3, 1, 1), (2, 4, 56, 1)),
}

def set_dim_func(data):
    """dim func."""
    shape = [x.value for x in data.shape]

    hash_key = str((tuple(shape), data.dtype))
    if hash_key in DIM_MAP.keys():
        diminfo = ct_util.set_dims(DIM_MAP[hash_key])
    else:
        diminfo = ""

    return diminfo, hash_key

def get_attrs():
    """get attrs."""
    attrs = {
        "pragma_reschedule": 1,
        "pragma_modshift": 1,
        "disable_cse": 1,
        "enable_bisect_optimize": 1,
        "merge_outer_loop_for_multicore": 2,
    }
    return attrs

@vc_util.check_input_type(akg.tvm.tensor.Tensor, akg.tvm.tensor.Tensor,
                          akg.tvm.tensor.Tensor, akg.tvm.tensor.Tensor,
                          akg.tvm.tensor.Tensor, (str, type(None)),
                          (int, type(None)), (float, type(None)))
def batch_norm_ad(head, data, mean, var, gamma, data_format="DefaultFormat", axis=1, eps=1e-3):
    """
    Compute gradient for batch normalization operator using automatic differentiate.

    Args:
        head (tvm.tensor.Tensor): Input tensor.
        data (tvm.tensor.Tensor): Input tensor.
        mean (tvm.tensor.Tensor): Input tensor.
        var (tvm.tensor.Tensor): Input tensor.
        gamma (tvm.tensor.Tensor): Input tensor.
        data_format (str): Data format of input tensors.
        axis (int): specify the channel axis when data_format is "DefaultFormat".
        eps (float): small float added to variance to avoid dividing by zero.

    Returns:
        tvm.tensor.Tensor of same shape and type as head.
    """
    supported_format = ["NCHW", "NHWC", "NC1HWC0", "DefaultFormat"]
    if data_format not in supported_format:
        raise RuntimeError("{} format is not supported by batch norm ad now.".format(data_format))
    beta = akg.tvm.placeholder(gamma.shape, gamma.dtype, name="beta")
    outputs = fused_batch_norm.fused_batch_norm(data, gamma, beta, mean, var, eps=eps,
                                                is_training=True, data_format=data_format,
                                                axis=axis, single_sum=True)
    output = outputs[0]
    AD_attrs = {"keep_dims": 1, "tensor_optimize": 1, "export_DOT": 1, "separate_output": 1}
    grads = list(akg.differentiate(output, [data, gamma, beta], head, AD_attrs, [outputs[3], mean, outputs[4], var]))
    auto_diff_outs = [grads[0], grads[1], grads[2]]

    attrs = get_attrs()
    dim_info, _ = set_dim_func(data)
    if dim_info != "":
        attrs["dim"] = dim_info
    attrs["custom_tiling"] = fused_batch_norm.batch_norm_tiling_strategy(auto_diff_outs, data_format)

    return auto_diff_outs, attrs
