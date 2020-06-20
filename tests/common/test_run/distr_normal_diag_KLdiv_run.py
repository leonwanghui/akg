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

import numpy as np
from tensorio import compare_tensor
from akg.utils import kernel_exec as utils
from test_op.prob_program.distribution import normal_diag
from gen_random import random_gaussian


def KLdiv_op(mean, scale):
  return normal_diag.normal_diag(mean, scale).KL_divergence()

def KLdiv_run(shape, dtype, kernelname="", attrs = None):
  expect, mean, scale, output = gen_data(dtype, shape)

  mod = utils.op_build_test(KLdiv_op, [mean.shape, scale.shape],
                            [dtype, dtype], kernel_name=kernelname,
                            op_attrs=[], attrs=None, log_cce=True, dump_cce=True, polyhedral=True)
  output = utils.mod_launch(mod, [mean, scale, output], expect = expect)
  return (mean, scale), output, expect, compare_tensor(output, expect, rtol=5e-03, equal_nan=True)


def gen_data(dtype, shape):
  support_list = {"float16": np.float16, "float32": np.float32}
  m, k = shape
  mean  = random_gaussian((m, k), miu=1, sigma=0.1).astype(support_list[dtype])
  scale = random_gaussian((m, k), miu=1, sigma=0.1).astype(support_list[dtype])
  cov = scale * scale
  expect = -0.5 * np.sum(1 + np.log(cov) - mean * mean - cov, -1)
  output = np.full((m, ), 0.0).astype(support_list[dtype])

  return expect, mean, scale, output
