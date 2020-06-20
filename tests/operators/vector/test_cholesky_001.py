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

import os
import pytest
from base import TestBase
from nose.plugins.attrib import attr
from test_run.cholesky_run import cholesky_run

############################################################
# TestCase= class: put to tests/*/
############################################################


class TestCase(TestBase):

    def setup(self):
        case_name = "test_cholesky_001"
        case_path = os.getcwd()
        self.params_init(case_name, case_path)
        self.caseresult = True
        self._log.info("============= {0} Setup case============".format(self.casename))
        self.testarg = [
            # testflag,opfuncname,testRunArgs, setdimArgs
            #("cholesky_001",cholesky_run,((64, 64), "float32")),
        ]
        self.testarg_rpc_cloud = [
            # # testflag,opfuncname,testRunArgs, setdimArgs
            #     ("clip_004",clip_run,((8,), -9, 2, "float16")),
            #     ("clip_005",clip_run,((8, 16), -9, 2, "float16")),
            #     ("clip_006",clip_run,((8, 16, 16), -9, 2, "float32")),
        ]
        return

    @pytest.mark.rpc_mini
    @pytest.mark.level0
    @pytest.mark.env_onecard
    @pytest.mark.platform_x86_ascend_training
    def test_run(self):
        """
        run case.#
        :return:
        """
        self.common_run(self.testarg)

    @pytest.mark.rpc_cloud
    @pytest.mark.env_onecard
    @pytest.mark.platform_x86_ascend_training
    def test_run_rpc_cloud(self):
        """
        run case.#
        :return:
        """
        self.common_run(self.testarg_rpc_cloud)

    def teardown(self):
        """
        clean environment
        :return:
        """
        self._log.info("============= {0} Teardown============".format(self.casename))
        return
