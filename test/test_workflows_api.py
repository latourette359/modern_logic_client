# coding: utf-8

"""
    Modern Logic Api

    Manage and version your customer decision logic outside of your codebase  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: info@usemodernlogic.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import modern_logic_client
from modern_logic_client.api.workflows_api import WorkflowsApi  # noqa: E501
from modern_logic_client.rest import ApiException


class TestWorkflowsApi(unittest.TestCase):
    """WorkflowsApi unit test stubs"""

    def setUp(self):
        self.api = WorkflowsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_workflow_get(self):
        """Test case for workflow_get

        List Available Workflows  # noqa: E501
        """
        pass

    def test_workflow_workflow_id_execute_post(self):
        """Test case for workflow_workflow_id_execute_post

        Execute Workflow  # noqa: E501
        """
        pass

    def test_workflow_workflow_id_executions_get(self):
        """Test case for workflow_workflow_id_executions_get

        List Workflow Executions  # noqa: E501
        """
        pass

    def test_workflow_workflow_id_get(self):
        """Test case for workflow_workflow_id_get

        Get Workflow Details  # noqa: E501
        """
        pass

    def test_workflow_workflow_id_versions_get(self):
        """Test case for workflow_workflow_id_versions_get

        List Workflow Versions  # noqa: E501
        """
        pass

    def test_workflow_workflow_id_webhooks_get(self):
        """Test case for workflow_workflow_id_webhooks_get

        List Active Callbacks  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()