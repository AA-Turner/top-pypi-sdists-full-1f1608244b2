"""
    Argo Workflows API

    Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. For more information, please see https://argo-workflows.readthedocs.io/en/latest/  # noqa: E501

    The version of the OpenAPI document: VERSION
    Generated by: https://openapi-generator.tech
"""


import unittest

import argo_workflows
from argo_workflows.api.info_service_api import InfoServiceApi  # noqa: E501


class TestInfoServiceApi(unittest.TestCase):
    """InfoServiceApi unit test stubs"""

    def setUp(self):
        self.api = InfoServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_collect_event(self):
        """Test case for collect_event

        """
        pass

    def test_get_info(self):
        """Test case for get_info

        """
        pass

    def test_get_user_info(self):
        """Test case for get_user_info

        """
        pass

    def test_get_version(self):
        """Test case for get_version

        """
        pass


if __name__ == '__main__':
    unittest.main()
