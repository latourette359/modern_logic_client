# modern_logic_client.AlertsApi

All URIs are relative to *https://{company}.usemodernlogic.com/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alert_alert_id_get**](AlertsApi.md#alert_alert_id_get) | **GET** /alert/{alertId} | Get Alert Details
[**alert_get**](AlertsApi.md#alert_get) | **GET** /alert | List Alerts

# **alert_alert_id_get**
> Alert alert_alert_id_get(alert_id)

Get Alert Details

### Example
```python
from __future__ import print_function
import time
import modern_logic_client
from modern_logic_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = modern_logic_client.AlertsApi(modern_logic_client.ApiClient(configuration))
alert_id = 56 # int | Alert id

try:
    # Get Alert Details
    api_response = api_instance.alert_alert_id_get(alert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->alert_alert_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| Alert id | 

### Return type

[**Alert**](Alert.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_get**
> InlineResponse2007 alert_get(page_size=page_size, page_number=page_number, assigned_to=assigned_to, assigned_to_team=assigned_to_team, workflow=workflow, before=before, after=after)

List Alerts

### Example
```python
from __future__ import print_function
import time
import modern_logic_client
from modern_logic_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = modern_logic_client.AlertsApi(modern_logic_client.ApiClient(configuration))
page_size = 56 # int | Number of elements to return (default is 10) (optional)
page_number = 56 # int | Lists are ordered by creation date ascending. To return the first page, set pageNumber to zero (optional)
assigned_to = 'assigned_to_example' # str | The username of the user the alert is assigned to (optional)
assigned_to_team = 'assigned_to_team_example' # str | The name of the team the alert is assigned to (optional)
workflow = 'workflow_example' # str | The name of the workflow associated to the alert (optional)
before = '2013-10-20' # date | Filter alerts to those that occurred before the given date. (optional)
after = '2013-10-20' # date | Filter alerts to those that occurred after the given date. (optional)

try:
    # List Alerts
    api_response = api_instance.alert_get(page_size=page_size, page_number=page_number, assigned_to=assigned_to, assigned_to_team=assigned_to_team, workflow=workflow, before=before, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->alert_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Number of elements to return (default is 10) | [optional] 
 **page_number** | **int**| Lists are ordered by creation date ascending. To return the first page, set pageNumber to zero | [optional] 
 **assigned_to** | **str**| The username of the user the alert is assigned to | [optional] 
 **assigned_to_team** | **str**| The name of the team the alert is assigned to | [optional] 
 **workflow** | **str**| The name of the workflow associated to the alert | [optional] 
 **before** | **date**| Filter alerts to those that occurred before the given date. | [optional] 
 **after** | **date**| Filter alerts to those that occurred after the given date. | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

