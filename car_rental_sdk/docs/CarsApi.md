# openapi_client.CarsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_car_cars_post**](CarsApi.md#create_car_cars_post) | **POST** /cars/ | Create Car
[**get_car_cars_car_id_get**](CarsApi.md#get_car_cars_car_id_get) | **GET** /cars/{car_id} | Get Car
[**list_cars_cars_get**](CarsApi.md#list_cars_cars_get) | **GET** /cars/ | List Cars


# **create_car_cars_post**
> CarResponse create_car_cars_post(car_create)

Create Car

### Example


```python
import openapi_client
from openapi_client.models.car_create import CarCreate
from openapi_client.models.car_response import CarResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CarsApi(api_client)
    car_create = openapi_client.CarCreate() # CarCreate | 

    try:
        # Create Car
        api_response = api_instance.create_car_cars_post(car_create)
        print("The response of CarsApi->create_car_cars_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarsApi->create_car_cars_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_create** | [**CarCreate**](CarCreate.md)|  | 

### Return type

[**CarResponse**](CarResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_car_cars_car_id_get**
> CarResponse get_car_cars_car_id_get(car_id)

Get Car

### Example


```python
import openapi_client
from openapi_client.models.car_response import CarResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CarsApi(api_client)
    car_id = 56 # int | 

    try:
        # Get Car
        api_response = api_instance.get_car_cars_car_id_get(car_id)
        print("The response of CarsApi->get_car_cars_car_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarsApi->get_car_cars_car_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_id** | **int**|  | 

### Return type

[**CarResponse**](CarResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cars_cars_get**
> List[CarResponse] list_cars_cars_get()

List Cars

### Example


```python
import openapi_client
from openapi_client.models.car_response import CarResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CarsApi(api_client)

    try:
        # List Cars
        api_response = api_instance.list_cars_cars_get()
        print("The response of CarsApi->list_cars_cars_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarsApi->list_cars_cars_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CarResponse]**](CarResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

