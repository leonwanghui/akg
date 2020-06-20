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

"""operator dsl fuction: distr_normal_diag_sample_ad"""

import akg
from test_op.prob_program.distribution import bernoulli
from akg.utils import custom_tiling as ct_util

dist_bernoulli_logprob_ad_set_dim_map = {
}


def dist_bernoulli_logprob_ad_set_dim_func(head, x, probs):
    """
    Lookup the dist_bernoulli_ad_set_dim_map and return hash_value and hash_key
    """
    key = []
    key.append(tuple(head.shape))
    key.append(tuple(x.shape))
    key.append(tuple(probs.shape))
    key.append(x.dtype)
    hash_key = str(tuple(key))

    if hash_key in dist_bernoulli_logprob_ad_set_dim_map.keys():
        return ct_util.set_dims(dist_bernoulli_logprob_ad_set_dim_map[hash_key]), hash_key
    return "", hash_key

@ct_util.reg_set_dim_func(dist_bernoulli_logprob_ad_set_dim_func)
def bernoulli_logprob_ad(head, x, probs):
    """
    An example of differentiating bernoulli.logprob in all inputs and paramters

    Args:
        head: The adjoint of the output, in other words, some tensors, by which the Jacobians
            will be multiplied
        x: input, tenosor of 0 or 1
        probs: probabilities of random variables taking values 1

    """
    mod = bernoulli.bernoulli(probs).log_prob(x)
    auto_diff_outs = list(akg.differentiate(mod, [x, probs], head))
    return auto_diff_outs
