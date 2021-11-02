# modern_logic_client.CustomersApi

All URIs are relative to *https://{company}.usemodernlogic.com/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customer_customer_id_delete**](CustomersApi.md#customer_customer_id_delete) | **DELETE** /customer/{customerId} | Delete Customer
[**customer_customer_id_get**](CustomersApi.md#customer_customer_id_get) | **GET** /customer/{customerId} | Get Customer Details
[**customer_customer_id_put**](CustomersApi.md#customer_customer_id_put) | **PUT** /customer/{customerId} | Update Customer Details
[**customer_get**](CustomersApi.md#customer_get) | **GET** /customer | List Customers
[**customer_post**](CustomersApi.md#customer_post) | **POST** /customer | Create Customer

# **customer_customer_id_delete**
> Customer customer_customer_id_delete(customer_id)

Delete Customer

### Example
```python
from __future__ import print_function
import time
import modern_logic_client
from modern_logic_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = modern_logic_client.CustomersApi(modern_logic_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | Customer id that the client supplied

try:
    # Delete Customer
    api_response = api_instance.customer_customer_id_delete(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->customer_customer_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Customer id that the client supplied | 

### Return type

[**Customer**](Customer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_customer_id_get**
> Customer customer_customer_id_get(customer_id)

Get Customer Details

### Example
```python
from __future__ import print_function
import time
import modern_logic_client
from modern_logic_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = modern_logic_client.CustomersApi(modern_logic_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | Customer id that the client supplied

try:
    # Get Customer Details
    api_response = api_instance.customer_customer_id_get(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->customer_customer_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Customer id that the client supplied | 

### Return type

[**Customer**](Customer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_customer_id_put**
> Customer customer_customer_id_put(body, customer_id)

Update Customer Details

### Example
```python
from __future__ import print_function
import time
import modern_logic_client
from modern_logic_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = modern_logic_client.CustomersApi(modern_logic_client.ApiClient(configuration))
body = modern_logic_client.Customer() # Customer | Customer Information
customer_id = 'customer_id_example' # str | Customer id that the client supplied

try:
    # Update Customer Details
    api_response = api_instance.customer_customer_id_put(body, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->customer_customer_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Customer**](Customer.md)| Customer Information | 
 **customer_id** | **str**| Customer id that the client supplied | 

### Return type

[**Customer**](Customer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_get**
> InlineResponse2008 customer_get(page_size=page_size, page_number=page_number)

List Customers

### Example
```python
from __future__ import print_function
import time
import modern_logic_client
from modern_logic_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = modern_logic_client.CustomersApi(modern_logic_client.ApiClient(configuration))
page_size = 56 # int | Number of elements to return (default is 10) (optional)
page_number = 56 # int | Lists are ordered by creation date ascending. To return the first page, set pageNumber to zero (optional)

try:
    # List Customers
    api_response = api_instance.customer_get(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->customer_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Number of elements to return (default is 10) | [optional] 
 **page_number** | **int**| Lists are ordered by creation date ascending. To return the first page, set pageNumber to zero | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_post**
> Customer customer_post(body)

Create Customer

### Example
```python
from __future__ import print_function
import time
import modern_logic_client
from modern_logic_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = modern_logic_client.CustomersApi(modern_logic_client.ApiClient(configuration))
body = modern_logic_client.Customer() # Customer | Customer Information

try:
    # Create Customer
    api_response = api_instance.customer_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->customer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Customer**](Customer.md)| Customer Information | 

### Return type

[**Customer**](Customer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

