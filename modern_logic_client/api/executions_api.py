# coding: utf-8

"""
    Modern Logic Api

    Manage and version your customer decision logic outside of your codebase  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: info@usemodernlogic.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from modern_logic_client.api_client import ApiClient


class ExecutionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def customer_customer_id_executions_get(self, customer_id, **kwargs):  # noqa: E501
        """List Customer Executions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.customer_customer_id_executions_get(customer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customer_id: Customer id that the client supplied (required)
        :param int page_size: Number of elements to return (default is 10)
        :param int page_number: Lists are ordered by creation date ascending. To return the first page, set pageNumber to zero
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.customer_customer_id_executions_get_with_http_info(customer_id, **kwargs)  # noqa: E501
        else:
            (data) = self.customer_customer_id_executions_get_with_http_info(customer_id, **kwargs)  # noqa: E501
            return data

    def customer_customer_id_executions_get_with_http_info(self, customer_id, **kwargs):  # noqa: E501
        """List Customer Executions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.customer_customer_id_executions_get_with_http_info(customer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customer_id: Customer id that the client supplied (required)
        :param int page_size: Number of elements to return (default is 10)
        :param int page_number: Lists are ordered by creation date ascending. To return the first page, set pageNumber to zero
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id', 'page_size', 'page_number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method customer_customer_id_executions_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params or
                params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `customer_customer_id_executions_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'customer_id' in params:
            path_params['customerId'] = params['customer_id']  # noqa: E501

        query_params = []
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page_number' in params:
            query_params.append(('pageNumber', params['page_number']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/customer/{customerId}/executions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2004',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def execution_execution_id_get(self, execution_id, **kwargs):  # noqa: E501
        """Get Execution Details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.execution_execution_id_get(execution_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int execution_id: Execution id (required)
        :return: Execution
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.execution_execution_id_get_with_http_info(execution_id, **kwargs)  # noqa: E501
        else:
            (data) = self.execution_execution_id_get_with_http_info(execution_id, **kwargs)  # noqa: E501
            return data

    def execution_execution_id_get_with_http_info(self, execution_id, **kwargs):  # noqa: E501
        """Get Execution Details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.execution_execution_id_get_with_http_info(execution_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int execution_id: Execution id (required)
        :return: Execution
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['execution_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method execution_execution_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'execution_id' is set
        if ('execution_id' not in params or
                params['execution_id'] is None):
            raise ValueError("Missing the required parameter `execution_id` when calling `execution_execution_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'execution_id' in params:
            path_params['executionId'] = params['execution_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/execution/{executionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Execution',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def execution_execution_id_resume_post(self, body, execution_id, **kwargs):  # noqa: E501
        """Resume Execution  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.execution_execution_id_resume_post(body, execution_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param dict(str, object) body: Execution Information (required)
        :param int execution_id: execution id (required)
        :return: WorkflowExecutionResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.execution_execution_id_resume_post_with_http_info(body, execution_id, **kwargs)  # noqa: E501
        else:
            (data) = self.execution_execution_id_resume_post_with_http_info(body, execution_id, **kwargs)  # noqa: E501
            return data

    def execution_execution_id_resume_post_with_http_info(self, body, execution_id, **kwargs):  # noqa: E501
        """Resume Execution  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.execution_execution_id_resume_post_with_http_info(body, execution_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param dict(str, object) body: Execution Information (required)
        :param int execution_id: execution id (required)
        :return: WorkflowExecutionResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'execution_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method execution_execution_id_resume_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `execution_execution_id_resume_post`")  # noqa: E501
        # verify the required parameter 'execution_id' is set
        if ('execution_id' not in params or
                params['execution_id'] is None):
            raise ValueError("Missing the required parameter `execution_id` when calling `execution_execution_id_resume_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'execution_id' in params:
            path_params['executionId'] = params['execution_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/execution/{executionId}/resume', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkflowExecutionResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def execution_get(self, **kwargs):  # noqa: E501
        """List executions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.execution_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: Number of elements to return (default is 10)
        :param int page_number: Lists are ordered by creation date ascending. To return the first page, set pageNumber to zero
        :param str alert_type: The type of the alert associated with the execution.
        :param date before: Filter executions to those that occurred before the given date.
        :param date after: Filter executions to those that occurred after the given date.
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.execution_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.execution_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def execution_get_with_http_info(self, **kwargs):  # noqa: E501
        """List executions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.execution_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: Number of elements to return (default is 10)
        :param int page_number: Lists are ordered by creation date ascending. To return the first page, set pageNumber to zero
        :param str alert_type: The type of the alert associated with the execution.
        :param date before: Filter executions to those that occurred before the given date.
        :param date after: Filter executions to those that occurred after the given date.
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page_number', 'alert_type', 'before', 'after']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method execution_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page_number' in params:
            query_params.append(('pageNumber', params['page_number']))  # noqa: E501
        if 'alert_type' in params:
            query_params.append(('alertType', params['alert_type']))  # noqa: E501
        if 'before' in params:
            query_params.append(('before', params['before']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/execution', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2004',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
