# modern-logic-client
Manage and version your customer decision logic outside of your codebase

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

Run 
```sh
pip install modern-logic-client
```

Then import the package:
```python
import modern_logic_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import modern_logic_client
from modern_logic_client.rest import ApiException
from pprint import pprint

# first set your configuration
configuration = modern_logic_client.Configuration()
configuration.api_key['Authorization'] = '<your token>'
configuration.host='https://<your api host>/v1'


# create an instance of the API class
api_instance = modern_logic_client.AlertsApi(modern_logic_client.ApiClient(configuration))
alert_id = 56 # int | Alert id

try:
    # Get Alert Details
    api_response = api_instance.alert_alert_id_get(alert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->alert_alert_id_get: %s\n" % e)


# execute a workflow
api_instance = modern_logic_client.WorkflowsApi(modern_logic_client.ApiClient(configuration))
workflow_id = 199 # int | Alert id
body = {"customerId":"nick123"}
try:
    #  execute a workflow
    api_response = api_instance.workflow_workflow_id_execute_post(body, workflow_id)
    pprint(api_response)
except ApiException as e:
    print("Exception: %s\n" % e)


## Documentation for API Endpoints

All URIs are relative to *https://{company}.usemodernlogic.com/v1/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AlertsApi* | [**alert_alert_id_get**](docs/AlertsApi.md#alert_alert_id_get) | **GET** /alert/{alertId} | Get Alert Details
*AlertsApi* | [**alert_get**](docs/AlertsApi.md#alert_get) | **GET** /alert | List Alerts
*CustomersApi* | [**customer_customer_id_delete**](docs/CustomersApi.md#customer_customer_id_delete) | **DELETE** /customer/{customerId} | Delete Customer
*CustomersApi* | [**customer_customer_id_get**](docs/CustomersApi.md#customer_customer_id_get) | **GET** /customer/{customerId} | Get Customer Details
*CustomersApi* | [**customer_customer_id_put**](docs/CustomersApi.md#customer_customer_id_put) | **PUT** /customer/{customerId} | Update Customer Details
*CustomersApi* | [**customer_get**](docs/CustomersApi.md#customer_get) | **GET** /customer | List Customers
*CustomersApi* | [**customer_post**](docs/CustomersApi.md#customer_post) | **POST** /customer | Create Customer
*DataSourcesApi* | [**datasource_calls_datasource_call_id_get**](docs/DataSourcesApi.md#datasource_calls_datasource_call_id_get) | **GET** /datasource_calls/{datasourceCallId} | Get Data Source Call Details
*DataSourcesApi* | [**datasource_datasource_id_calls_get**](docs/DataSourcesApi.md#datasource_datasource_id_calls_get) | **GET** /datasource/{datasourceId}/calls | List Data Source Calls
*DataSourcesApi* | [**datasource_datasource_id_get**](docs/DataSourcesApi.md#datasource_datasource_id_get) | **GET** /datasource/{datasourceId} | Get Data Source Details
*DataSourcesApi* | [**datasource_get**](docs/DataSourcesApi.md#datasource_get) | **GET** /datasource | List Data Sources
*ExecutionsApi* | [**customer_customer_id_executions_get**](docs/ExecutionsApi.md#customer_customer_id_executions_get) | **GET** /customer/{customerId}/executions | List Customer Executions
*ExecutionsApi* | [**execution_execution_id_get**](docs/ExecutionsApi.md#execution_execution_id_get) | **GET** /execution/{executionId} | Get Execution Details
*ExecutionsApi* | [**execution_execution_id_resume_post**](docs/ExecutionsApi.md#execution_execution_id_resume_post) | **POST** /execution/{executionId}/resume | Resume Execution
*WebhooksApi* | [**webhook_get**](docs/WebhooksApi.md#webhook_get) | **GET** /webhook | List Webhooks
*WebhooksApi* | [**webhook_webhook_id_get**](docs/WebhooksApi.md#webhook_webhook_id_get) | **GET** /webhook/{webhookId} | Get Webhook Details
*WorkflowsApi* | [**workflow_get**](docs/WorkflowsApi.md#workflow_get) | **GET** /workflow | List Available Workflows
*WorkflowsApi* | [**workflow_workflow_id_execute_post**](docs/WorkflowsApi.md#workflow_workflow_id_execute_post) | **POST** /workflow/{workflowID}/execute | Execute Workflow
*WorkflowsApi* | [**workflow_workflow_id_executions_get**](docs/WorkflowsApi.md#workflow_workflow_id_executions_get) | **GET** /workflow/{workflowID}/executions | List Workflow Executions
*WorkflowsApi* | [**workflow_workflow_id_get**](docs/WorkflowsApi.md#workflow_workflow_id_get) | **GET** /workflow/{workflowID} | Get Workflow Details
*WorkflowsApi* | [**workflow_workflow_id_versions_get**](docs/WorkflowsApi.md#workflow_workflow_id_versions_get) | **GET** /workflow/{workflowID}/versions | List Workflow Versions
*WorkflowsApi* | [**workflow_workflow_id_webhooks_get**](docs/WorkflowsApi.md#workflow_workflow_id_webhooks_get) | **GET** /workflow/{workflowID}/webhooks | List Active Callbacks

## Documentation For Models

 - [Alert](docs/Alert.md)
 - [AlertItem](docs/AlertItem.md)
 - [Customer](docs/Customer.md)
 - [CustomerItem](docs/CustomerItem.md)
 - [DataSource](docs/DataSource.md)
 - [DataSourceCall](docs/DataSourceCall.md)
 - [DataSourceCallItem](docs/DataSourceCallItem.md)
 - [DataSourceType](docs/DataSourceType.md)
 - [Execution](docs/Execution.md)
 - [ExecutionInput](docs/ExecutionInput.md)
 - [ExecutionItem](docs/ExecutionItem.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [ListResponse](docs/ListResponse.md)
 - [RuleSetWarning](docs/RuleSetWarning.md)
 - [RuleWarning](docs/RuleWarning.md)
 - [Webhook](docs/Webhook.md)
 - [WebhookResponse](docs/WebhookResponse.md)
 - [Workflow](docs/Workflow.md)
 - [WorkflowExecutionResult](docs/WorkflowExecutionResult.md)
 - [WorkflowVersion](docs/WorkflowVersion.md)

## Documentation For Authorization


## bearerAuth



## Author

info@usemodernlogic.com
