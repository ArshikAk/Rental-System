# openapi_client.RentalsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**active_rentals_rentals_active_get**](RentalsApi.md#active_rentals_rentals_active_get) | **GET** /rentals/active | Active Rentals
[**cancel_rental_rentals_rental_id_delete**](RentalsApi.md#cancel_rental_rentals_rental_id_delete) | **DELETE** /rentals/{rental_id} | Cancel Rental
[**list_rentals_rentals_get**](RentalsApi.md#list_rentals_rentals_get) | **GET** /rentals/ | List Rentals
[**rent_car_rentals_car_id_rent_post**](RentalsApi.md#rent_car_rentals_car_id_rent_post) | **POST** /rentals/{car_id}/rent | Rent Car


# **active_rentals_rentals_active_get**
> List[RentalResponse] active_rentals_rentals_active_get()

Active Rentals

### Example


```python
import openapi_client
from openapi_client.models.rental_response import RentalResponse
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
    api_instance = openapi_client.RentalsApi(api_client)

    try:
        # Active Rentals
        api_response = api_instance.active_rentals_rentals_active_get()
        print("The response of RentalsApi->active_rentals_rentals_active_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalsApi->active_rentals_rentals_active_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[RentalResponse]**](RentalResponse.md)

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

# **cancel_rental_rentals_rental_id_delete**
> object cancel_rental_rentals_rental_id_delete(rental_id)

Cancel Rental

### Example


```python
import openapi_client
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
    api_instance = openapi_client.RentalsApi(api_client)
    rental_id = 56 # int | 

    try:
        # Cancel Rental
        api_response = api_instance.cancel_rental_rentals_rental_id_delete(rental_id)
        print("The response of RentalsApi->cancel_rental_rentals_rental_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalsApi->cancel_rental_rentals_rental_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rental_id** | **int**|  | 

### Return type

**object**

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

# **list_rentals_rentals_get**
> List[RentalResponse] list_rentals_rentals_get()

List Rentals

### Example


```python
import openapi_client
from openapi_client.models.rental_response import RentalResponse
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
    api_instance = openapi_client.RentalsApi(api_client)

    try:
        # List Rentals
        api_response = api_instance.list_rentals_rentals_get()
        print("The response of RentalsApi->list_rentals_rentals_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalsApi->list_rentals_rentals_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[RentalResponse]**](RentalResponse.md)

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

# **rent_car_rentals_car_id_rent_post**
> RentalResponse rent_car_rentals_car_id_rent_post(car_id, rental_create)

Rent Car

### Example


```python
import openapi_client
from openapi_client.models.rental_create import RentalCreate
from openapi_client.models.rental_response import RentalResponse
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
    api_instance = openapi_client.RentalsApi(api_client)
    car_id = 56 # int | 
    rental_create = openapi_client.RentalCreate() # RentalCreate | 

    try:
        # Rent Car
        api_response = api_instance.rent_car_rentals_car_id_rent_post(car_id, rental_create)
        print("The response of RentalsApi->rent_car_rentals_car_id_rent_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalsApi->rent_car_rentals_car_id_rent_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_id** | **int**|  | 
 **rental_create** | [**RentalCreate**](RentalCreate.md)|  | 

### Return type

[**RentalResponse**](RentalResponse.md)

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

