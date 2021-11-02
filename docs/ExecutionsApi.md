# modern_logic_client.ExecutionsApi

All URIs are relative to *https://{company}.usemodernlogic.com/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customer_customer_id_executions_get**](ExecutionsApi.md#customer_customer_id_executions_get) | **GET** /customer/{customerId}/executions | List Customer Executions
[**execution_execution_id_get**](ExecutionsApi.md#execution_execution_id_get) | **GET** /execution/{executionId} | Get Execution Details
[**execution_execution_id_resume_post**](ExecutionsApi.md#execution_execution_id_resume_post) | **POST** /execution/{executionId}/resume | Resume Execution
[**execution_get**](ExecutionsApi.md#execution_get) | **GET** /execution | List executions

# **customer_customer_id_executions_get**
> InlineResponse2004 customer_customer_id_executions_get(customer_id, page_size=page_size, page_number=page_number)

List Customer Executions

### Example
```python
from __future__ import print_function
import time
import modern_logic_client
from modern_logic_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = modern_logic_client.ExecutionsApi(modern_logic_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | Customer id that the client supplied
page_size = 56 # int | Number of elements to return (default is 10) (optional)
page_number = 56 # int | Lists are ordered by creation date ascending. To return the first page, set pageNumber to zero (optional)

try:
    # List Customer Executions
    api_response = api_instance.customer_customer_id_executions_get(customer_id, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExecutionsApi->customer_customer_id_executions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Customer id that the client supplied | 
 **page_size** | **int**| Number of elements to return (default is 10) | [optional] 
 **page_number** | **int**| Lists are ordered by creation date ascending. To return the first page, set pageNumber to zero | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execution_execution_id_get**
> Execution execution_execution_id_get(execution_id)

Get Execution Details

### Example
```python
from __future__ import print_function
import time
import modern_logic_client
from modern_logic_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = modern_logic_client.ExecutionsApi(modern_logic_client.ApiClient(configuration))
execution_id = 56 # int | Execution id

try:
    # Get Execution Details
    api_response = api_instance.execution_execution_id_get(execution_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExecutionsApi->execution_execution_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **int**| Execution id | 

### Return type

[**Execution**](Execution.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execution_execution_id_resume_post**
> WorkflowExecutionResult execution_execution_id_resume_post(body, execution_id)

Resume Execution

### Example
```python
from __future__ import print_function
import time
import modern_logic_client
from modern_logic_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = modern_logic_client.ExecutionsApi(modern_logic_client.ApiClient(configuration))
body = NULL # dict(str, object) | Execution Information
execution_id = 56 # int | execution id

try:
    # Resume Execution
    api_response = api_instance.execution_execution_id_resume_post(body, execution_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExecutionsApi->execution_execution_id_resume_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)| Execution Information | 
 **execution_id** | **int**| execution id | 

### Return type

[**WorkflowExecutionResult**](WorkflowExecutionResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execution_get**
> InlineResponse2004 execution_get(page_size=page_size, page_number=page_number, alert_type=alert_type, before=before, after=after)

List executions

### Example
```python
from __future__ import print_function
import time
import modern_logic_client
from modern_logic_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = modern_logic_client.ExecutionsApi(modern_logic_client.ApiClient(configuration))
page_size = 56 # int | Number of elements to return (default is 10) (optional)
page_number = 56 # int | Lists are ordered by creation date ascending. To return the first page, set pageNumber to zero (optional)
alert_type = 'alert_type_example' # str | The alert status of this execution (optional)
before = '2013-10-20' # date | Filter executions to those that occurred before the given date. (optional)
after = '2013-10-20' # date | Filter executions to those that occurred after the given date. (optional)

try:
    # List executions
    api_response = api_instance.execution_get(page_size=page_size, page_number=page_number, alert_type=alert_type, before=before, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExecutionsApi->execution_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Number of elements to return (default is 10) | [optional] 
 **page_number** | **int**| Lists are ordered by creation date ascending. To return the first page, set pageNumber to zero | [optional] 
 **alert_type** | **str**| The alert status of this execution | [optional] 
 **before** | **date**| Filter executions to those that occurred before the given date. | [optional] 
 **after** | **date**| Filter executions to those that occurred after the given date. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

