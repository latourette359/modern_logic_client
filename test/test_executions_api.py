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
from modern_logic_client.api.executions_api import ExecutionsApi  # noqa: E501
from modern_logic_client.rest import ApiException


class TestExecutionsApi(unittest.TestCase):
    """ExecutionsApi unit test stubs"""

    def setUp(self):
        self.api = ExecutionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_customer_customer_id_executions_get(self):
        """Test case for customer_customer_id_executions_get

        List Customer Executions  # noqa: E501
        """
        pass

    def test_execution_execution_id_get(self):
        """Test case for execution_execution_id_get

        Get Execution Details  # noqa: E501
        """
        pass

    def test_execution_execution_id_resume_post(self):
        """Test case for execution_execution_id_resume_post

        Resume Execution  # noqa: E501
        """
        pass

    def test_execution_get(self):
        """Test case for execution_get

        List executions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
