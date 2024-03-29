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
from modern_logic_client.api.data_sources_api import DataSourcesApi  # noqa: E501
from modern_logic_client.rest import ApiException


class TestDataSourcesApi(unittest.TestCase):
    """DataSourcesApi unit test stubs"""

    def setUp(self):
        self.api = DataSourcesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_datasource_calls_datasource_call_id_get(self):
        """Test case for datasource_calls_datasource_call_id_get

        Get Data Source Call Details  # noqa: E501
        """
        pass

    def test_datasource_datasource_id_calls_get(self):
        """Test case for datasource_datasource_id_calls_get

        List Data Source Calls  # noqa: E501
        """
        pass

    def test_datasource_datasource_id_get(self):
        """Test case for datasource_datasource_id_get

        Get Data Source Details  # noqa: E501
        """
        pass

    def test_datasource_get(self):
        """Test case for datasource_get

        List Data Sources  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
