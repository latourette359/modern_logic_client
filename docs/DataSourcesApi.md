# modern_logic_client.DataSourcesApi

All URIs are relative to *https://{company}.usemodernlogic.com/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**datasource_calls_datasource_call_id_get**](DataSourcesApi.md#datasource_calls_datasource_call_id_get) | **GET** /datasource_calls/{datasourceCallId} | Get Data Source Call Details
[**datasource_datasource_id_calls_get**](DataSourcesApi.md#datasource_datasource_id_calls_get) | **GET** /datasource/{datasourceId}/calls | List Data Source Calls
[**datasource_datasource_id_get**](DataSourcesApi.md#datasource_datasource_id_get) | **GET** /datasource/{datasourceId} | Get Data Source Details
[**datasource_get**](DataSourcesApi.md#datasource_get) | **GET** /datasource | List Data Sources

# **datasource_calls_datasource_call_id_get**
> DataSourceCall datasource_calls_datasource_call_id_get(datasource_call_id)

Get Data Source Call Details

A datasource call is a single instance of when a datasource was queried by a workflow

### Example
```python
from __future__ import print_function
import time
import modern_logic_client
from modern_logic_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = modern_logic_client.DataSourcesApi(modern_logic_client.ApiClient(configuration))
datasource_call_id = 56 # int | Data source call id

try:
    # Get Data Source Call Details
    api_response = api_instance.datasource_calls_datasource_call_id_get(datasource_call_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->datasource_calls_datasource_call_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource_call_id** | **int**| Data source call id | 

### Return type

[**DataSourceCall**](DataSourceCall.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasource_datasource_id_calls_get**
> InlineResponse2006 datasource_datasource_id_calls_get(datasource_id, page_size=page_size, page_number=page_number)

List Data Source Calls

### Example
```python
from __future__ import print_function
import time
import modern_logic_client
from modern_logic_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = modern_logic_client.DataSourcesApi(modern_logic_client.ApiClient(configuration))
datasource_id = 56 # int | Specified workflow to run, to evaluate the target user.
page_size = 56 # int | Number of elements to return (default is 10) (optional)
page_number = 56 # int | Lists are ordered by creation date ascending. To return the first page, set pageNumber to zero (optional)

try:
    # List Data Source Calls
    api_response = api_instance.datasource_datasource_id_calls_get(datasource_id, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->datasource_datasource_id_calls_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource_id** | **int**| Specified workflow to run, to evaluate the target user. | 
 **page_size** | **int**| Number of elements to return (default is 10) | [optional] 
 **page_number** | **int**| Lists are ordered by creation date ascending. To return the first page, set pageNumber to zero | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasource_datasource_id_get**
> DataSource datasource_datasource_id_get(datasource_id)

Get Data Source Details

Evaluates a new user using the specificed workflow and user details. Typically called during onboarding.

### Example
```python
from __future__ import print_function
import time
import modern_logic_client
from modern_logic_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = modern_logic_client.DataSourcesApi(modern_logic_client.ApiClient(configuration))
datasource_id = 56 # int | Data Source id

try:
    # Get Data Source Details
    api_response = api_instance.datasource_datasource_id_get(datasource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->datasource_datasource_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource_id** | **int**| Data Source id | 

### Return type

[**DataSource**](DataSource.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasource_get**
> InlineResponse2005 datasource_get(page_size=page_size, page_number=page_number)

List Data Sources

### Example
```python
from __future__ import print_function
import time
import modern_logic_client
from modern_logic_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = modern_logic_client.DataSourcesApi(modern_logic_client.ApiClient(configuration))
page_size = 56 # int | Number of elements to return (default is 10) (optional)
page_number = 56 # int | Lists are ordered by creation date ascending. To return the first page, set pageNumber to zero (optional)

try:
    # List Data Sources
    api_response = api_instance.datasource_get(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->datasource_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Number of elements to return (default is 10) | [optional] 
 **page_number** | **int**| Lists are ordered by creation date ascending. To return the first page, set pageNumber to zero | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

