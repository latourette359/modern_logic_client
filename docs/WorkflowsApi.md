# modern_logic_client.WorkflowsApi

All URIs are relative to *https://{company}.usemodernlogic.com/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workflow_get**](WorkflowsApi.md#workflow_get) | **GET** /workflow | List Available Workflows
[**workflow_workflow_id_execute_post**](WorkflowsApi.md#workflow_workflow_id_execute_post) | **POST** /workflow/{workflowID}/execute | Execute Workflow
[**workflow_workflow_id_executions_get**](WorkflowsApi.md#workflow_workflow_id_executions_get) | **GET** /workflow/{workflowID}/executions | List Workflow Executions
[**workflow_workflow_id_get**](WorkflowsApi.md#workflow_workflow_id_get) | **GET** /workflow/{workflowID} | Get Workflow Details
[**workflow_workflow_id_versions_get**](WorkflowsApi.md#workflow_workflow_id_versions_get) | **GET** /workflow/{workflowID}/versions | List Workflow Versions
[**workflow_workflow_id_webhooks_get**](WorkflowsApi.md#workflow_workflow_id_webhooks_get) | **GET** /workflow/{workflowID}/webhooks | List Active Callbacks

# **workflow_get**
> InlineResponse2001 workflow_get(page_size=page_size, page_number=page_number)

List Available Workflows

### Example
```python
from __future__ import print_function
import time
import modern_logic_client
from modern_logic_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = modern_logic_client.WorkflowsApi(modern_logic_client.ApiClient(configuration))
page_size = 56 # int | Number of elements to return (default is 10) (optional)
page_number = 56 # int | Lists are ordered by creation date ascending. To return the first page, set pageNumber to zero (optional)

try:
    # List Available Workflows
    api_response = api_instance.workflow_get(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowsApi->workflow_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Number of elements to return (default is 10) | [optional] 
 **page_number** | **int**| Lists are ordered by creation date ascending. To return the first page, set pageNumber to zero | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_workflow_id_execute_post**
> WorkflowExecutionResult workflow_workflow_id_execute_post(body, workflow_id, v=v)

Execute Workflow

### Example
```python
from __future__ import print_function
import time
import modern_logic_client
from modern_logic_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = modern_logic_client.WorkflowsApi(modern_logic_client.ApiClient(configuration))
body = NULL # dict(str, object) | Execution Information
workflow_id = 56 # int | Workflow id
v = 56 # int | If you want to run a version other then the current production version, you can supply the version number to run. (optional)

try:
    # Execute Workflow
    api_response = api_instance.workflow_workflow_id_execute_post(body, workflow_id, v=v)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowsApi->workflow_workflow_id_execute_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)| Execution Information | 
 **workflow_id** | **int**| Workflow id | 
 **v** | **int**| If you want to run a version other then the current production version, you can supply the version number to run. | [optional] 

### Return type

[**WorkflowExecutionResult**](WorkflowExecutionResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_workflow_id_executions_get**
> InlineResponse200 workflow_workflow_id_executions_get(workflow_id, v=v, page_size=page_size, page_number=page_number)

List Workflow Executions

### Example
```python
from __future__ import print_function
import time
import modern_logic_client
from modern_logic_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = modern_logic_client.WorkflowsApi(modern_logic_client.ApiClient(configuration))
workflow_id = 56 # int | Workflow Id
v = 56 # int | If you want to return the executions of a particular workflow version instead of all workflows (optional)
page_size = 56 # int | Number of elements to return (default is 10) (optional)
page_number = 56 # int | Lists are ordered by creation date ascending. To return the first page, set pageNumber to zero (optional)

try:
    # List Workflow Executions
    api_response = api_instance.workflow_workflow_id_executions_get(workflow_id, v=v, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowsApi->workflow_workflow_id_executions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **int**| Workflow Id | 
 **v** | **int**| If you want to return the executions of a particular workflow version instead of all workflows | [optional] 
 **page_size** | **int**| Number of elements to return (default is 10) | [optional] 
 **page_number** | **int**| Lists are ordered by creation date ascending. To return the first page, set pageNumber to zero | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_workflow_id_get**
> Workflow workflow_workflow_id_get(workflow_id)

Get Workflow Details

### Example
```python
from __future__ import print_function
import time
import modern_logic_client
from modern_logic_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = modern_logic_client.WorkflowsApi(modern_logic_client.ApiClient(configuration))
workflow_id = 56 # int | Workflow id

try:
    # Get Workflow Details
    api_response = api_instance.workflow_workflow_id_get(workflow_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowsApi->workflow_workflow_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **int**| Workflow id | 

### Return type

[**Workflow**](Workflow.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_workflow_id_versions_get**
> InlineResponse2002 workflow_workflow_id_versions_get(workflow_id, page_size=page_size, page_number=page_number)

List Workflow Versions

### Example
```python
from __future__ import print_function
import time
import modern_logic_client
from modern_logic_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = modern_logic_client.WorkflowsApi(modern_logic_client.ApiClient(configuration))
workflow_id = 56 # int | Workflow id
page_size = 56 # int | Number of elements to return (default is 10) (optional)
page_number = 56 # int | Lists are ordered by creation date ascending. To return the first page, set pageNumber to zero (optional)

try:
    # List Workflow Versions
    api_response = api_instance.workflow_workflow_id_versions_get(workflow_id, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowsApi->workflow_workflow_id_versions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **int**| Workflow id | 
 **page_size** | **int**| Number of elements to return (default is 10) | [optional] 
 **page_number** | **int**| Lists are ordered by creation date ascending. To return the first page, set pageNumber to zero | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_workflow_id_webhooks_get**
> InlineResponse2003 workflow_workflow_id_webhooks_get(workflow_id, page_size=page_size, page_number=page_number)

List Active Callbacks

### Example
```python
from __future__ import print_function
import time
import modern_logic_client
from modern_logic_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = modern_logic_client.WorkflowsApi(modern_logic_client.ApiClient(configuration))
workflow_id = 56 # int | Workflow ID
page_size = 56 # int | Number of elements to return (default is 10) (optional)
page_number = 56 # int | Lists are ordered by creation date ascending. To return the first page, set pageNumber to zero (optional)

try:
    # List Active Callbacks
    api_response = api_instance.workflow_workflow_id_webhooks_get(workflow_id, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowsApi->workflow_workflow_id_webhooks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **int**| Workflow ID | 
 **page_size** | **int**| Number of elements to return (default is 10) | [optional] 
 **page_number** | **int**| Lists are ordered by creation date ascending. To return the first page, set pageNumber to zero | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

