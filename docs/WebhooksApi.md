# modern_logic_client.WebhooksApi

All URIs are relative to *https://{company}.usemodernlogic.com/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhook_get**](WebhooksApi.md#webhook_get) | **GET** /webhook | List Webhooks
[**webhook_webhook_id_get**](WebhooksApi.md#webhook_webhook_id_get) | **GET** /webhook/{webhookId} | Get Webhook Details

# **webhook_get**
> InlineResponse2003 webhook_get(page_size=page_size, page_number=page_number)

List Webhooks

### Example
```python
from __future__ import print_function
import time
import modern_logic_client
from modern_logic_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = modern_logic_client.WebhooksApi(modern_logic_client.ApiClient(configuration))
page_size = 56 # int | Number of elements to return (default is 10) (optional)
page_number = 56 # int | Lists are ordered by creation date ascending. To return the first page, set pageNumber to zero (optional)

try:
    # List Webhooks
    api_response = api_instance.webhook_get(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhook_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **webhook_webhook_id_get**
> Webhook webhook_webhook_id_get(webhook_id)

Get Webhook Details

### Example
```python
from __future__ import print_function
import time
import modern_logic_client
from modern_logic_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = modern_logic_client.WebhooksApi(modern_logic_client.ApiClient(configuration))
webhook_id = 56 # int | Webhook Id

try:
    # Get Webhook Details
    api_response = api_instance.webhook_webhook_id_get(webhook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhook_webhook_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **int**| Webhook Id | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

