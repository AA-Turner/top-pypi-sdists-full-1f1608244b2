"""
    Argo Workflows API

    Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. For more information, please see https://argo-workflows.readthedocs.io/en/latest/  # noqa: E501

    The version of the OpenAPI document: VERSION
    Generated by: https://openapi-generator.tech
"""


import unittest

import argo_workflows
from argo_workflows.api.workflow_template_service_api import WorkflowTemplateServiceApi  # noqa: E501


class TestWorkflowTemplateServiceApi(unittest.TestCase):
    """WorkflowTemplateServiceApi unit test stubs"""

    def setUp(self):
        self.api = WorkflowTemplateServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_workflow_template(self):
        """Test case for create_workflow_template

        """
        pass

    def test_delete_workflow_template(self):
        """Test case for delete_workflow_template

        """
        pass

    def test_get_workflow_template(self):
        """Test case for get_workflow_template

        """
        pass

    def test_lint_workflow_template(self):
        """Test case for lint_workflow_template

        """
        pass

    def test_list_workflow_templates(self):
        """Test case for list_workflow_templates

        """
        pass

    def test_update_workflow_template(self):
        """Test case for update_workflow_template

        """
        pass


if __name__ == '__main__':
    unittest.main()
