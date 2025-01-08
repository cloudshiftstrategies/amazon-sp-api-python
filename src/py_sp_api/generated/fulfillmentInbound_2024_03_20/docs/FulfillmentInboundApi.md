# py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi

All URIs are relative to *https://sellingpartnerapi-na.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_inbound_plan**](FulfillmentInboundApi.md#cancel_inbound_plan) | **PUT** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/cancellation | cancelInboundPlan
[**cancel_self_ship_appointment**](FulfillmentInboundApi.md#cancel_self_ship_appointment) | **PUT** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/selfShipAppointmentCancellation | cancelSelfShipAppointment
[**confirm_delivery_window_options**](FulfillmentInboundApi.md#confirm_delivery_window_options) | **POST** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/deliveryWindowOptions/{deliveryWindowOptionId}/confirmation | confirmDeliveryWindowOptions
[**confirm_packing_option**](FulfillmentInboundApi.md#confirm_packing_option) | **POST** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/packingOptions/{packingOptionId}/confirmation | confirmPackingOption
[**confirm_placement_option**](FulfillmentInboundApi.md#confirm_placement_option) | **POST** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/placementOptions/{placementOptionId}/confirmation | confirmPlacementOption
[**confirm_shipment_content_update_preview**](FulfillmentInboundApi.md#confirm_shipment_content_update_preview) | **POST** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/contentUpdatePreviews/{contentUpdatePreviewId}/confirmation | confirmShipmentContentUpdatePreview
[**confirm_transportation_options**](FulfillmentInboundApi.md#confirm_transportation_options) | **POST** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/transportationOptions/confirmation | confirmTransportationOptions
[**create_inbound_plan**](FulfillmentInboundApi.md#create_inbound_plan) | **POST** /inbound/fba/2024-03-20/inboundPlans | createInboundPlan
[**create_marketplace_item_labels**](FulfillmentInboundApi.md#create_marketplace_item_labels) | **POST** /inbound/fba/2024-03-20/items/labels | createMarketplaceItemLabels
[**generate_delivery_window_options**](FulfillmentInboundApi.md#generate_delivery_window_options) | **POST** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/deliveryWindowOptions | generateDeliveryWindowOptions
[**generate_packing_options**](FulfillmentInboundApi.md#generate_packing_options) | **POST** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/packingOptions | generatePackingOptions
[**generate_placement_options**](FulfillmentInboundApi.md#generate_placement_options) | **POST** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/placementOptions | generatePlacementOptions
[**generate_self_ship_appointment_slots**](FulfillmentInboundApi.md#generate_self_ship_appointment_slots) | **POST** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/selfShipAppointmentSlots | generateSelfShipAppointmentSlots
[**generate_shipment_content_update_previews**](FulfillmentInboundApi.md#generate_shipment_content_update_previews) | **POST** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/contentUpdatePreviews | generateShipmentContentUpdatePreviews
[**generate_transportation_options**](FulfillmentInboundApi.md#generate_transportation_options) | **POST** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/transportationOptions | generateTransportationOptions
[**get_delivery_challan_document**](FulfillmentInboundApi.md#get_delivery_challan_document) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/deliveryChallanDocument | getDeliveryChallanDocument
[**get_inbound_operation_status**](FulfillmentInboundApi.md#get_inbound_operation_status) | **GET** /inbound/fba/2024-03-20/operations/{operationId} | getInboundOperationStatus
[**get_inbound_plan**](FulfillmentInboundApi.md#get_inbound_plan) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId} | getInboundPlan
[**get_self_ship_appointment_slots**](FulfillmentInboundApi.md#get_self_ship_appointment_slots) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/selfShipAppointmentSlots | getSelfShipAppointmentSlots
[**get_shipment**](FulfillmentInboundApi.md#get_shipment) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId} | getShipment
[**get_shipment_content_update_preview**](FulfillmentInboundApi.md#get_shipment_content_update_preview) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/contentUpdatePreviews/{contentUpdatePreviewId} | getShipmentContentUpdatePreview
[**list_delivery_window_options**](FulfillmentInboundApi.md#list_delivery_window_options) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/deliveryWindowOptions | listDeliveryWindowOptions
[**list_inbound_plan_boxes**](FulfillmentInboundApi.md#list_inbound_plan_boxes) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/boxes | listInboundPlanBoxes
[**list_inbound_plan_items**](FulfillmentInboundApi.md#list_inbound_plan_items) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/items | listInboundPlanItems
[**list_inbound_plan_pallets**](FulfillmentInboundApi.md#list_inbound_plan_pallets) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/pallets | listInboundPlanPallets
[**list_inbound_plans**](FulfillmentInboundApi.md#list_inbound_plans) | **GET** /inbound/fba/2024-03-20/inboundPlans | listInboundPlans
[**list_item_compliance_details**](FulfillmentInboundApi.md#list_item_compliance_details) | **GET** /inbound/fba/2024-03-20/items/compliance | listItemComplianceDetails
[**list_packing_group_boxes**](FulfillmentInboundApi.md#list_packing_group_boxes) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/packingGroups/{packingGroupId}/boxes | listPackingGroupBoxes
[**list_packing_group_items**](FulfillmentInboundApi.md#list_packing_group_items) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/packingGroups/{packingGroupId}/items | listPackingGroupItems
[**list_packing_options**](FulfillmentInboundApi.md#list_packing_options) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/packingOptions | listPackingOptions
[**list_placement_options**](FulfillmentInboundApi.md#list_placement_options) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/placementOptions | listPlacementOptions
[**list_prep_details**](FulfillmentInboundApi.md#list_prep_details) | **GET** /inbound/fba/2024-03-20/items/prepDetails | listPrepDetails
[**list_shipment_boxes**](FulfillmentInboundApi.md#list_shipment_boxes) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/boxes | listShipmentBoxes
[**list_shipment_content_update_previews**](FulfillmentInboundApi.md#list_shipment_content_update_previews) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/contentUpdatePreviews | listShipmentContentUpdatePreviews
[**list_shipment_items**](FulfillmentInboundApi.md#list_shipment_items) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/items | listShipmentItems
[**list_shipment_pallets**](FulfillmentInboundApi.md#list_shipment_pallets) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/pallets | listShipmentPallets
[**list_transportation_options**](FulfillmentInboundApi.md#list_transportation_options) | **GET** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/transportationOptions | listTransportationOptions
[**schedule_self_ship_appointment**](FulfillmentInboundApi.md#schedule_self_ship_appointment) | **POST** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/selfShipAppointmentSlots/{slotId}/schedule | scheduleSelfShipAppointment
[**set_packing_information**](FulfillmentInboundApi.md#set_packing_information) | **POST** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/packingInformation | setPackingInformation
[**set_prep_details**](FulfillmentInboundApi.md#set_prep_details) | **POST** /inbound/fba/2024-03-20/items/prepDetails | setPrepDetails
[**update_inbound_plan_name**](FulfillmentInboundApi.md#update_inbound_plan_name) | **PUT** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/name | updateInboundPlanName
[**update_item_compliance_details**](FulfillmentInboundApi.md#update_item_compliance_details) | **PUT** /inbound/fba/2024-03-20/items/compliance | updateItemComplianceDetails
[**update_shipment_name**](FulfillmentInboundApi.md#update_shipment_name) | **PUT** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/name | updateShipmentName
[**update_shipment_source_address**](FulfillmentInboundApi.md#update_shipment_source_address) | **PUT** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/sourceAddress | updateShipmentSourceAddress
[**update_shipment_tracking_details**](FulfillmentInboundApi.md#update_shipment_tracking_details) | **PUT** /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/trackingDetails | updateShipmentTrackingDetails


# **cancel_inbound_plan**
> CancelInboundPlanResponse cancel_inbound_plan(inbound_plan_id)

cancelInboundPlan

Cancels an Inbound Plan. Charges may apply if the cancellation is performed outside of a void window. The window for Amazon Partnered Carriers is 24 hours for Small Parcel Delivery (SPD) and one hour for Less-Than-Truckload (LTL) carrier shipments.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 2 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.cancel_inbound_plan_response import CancelInboundPlanResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.

    try:
        # cancelInboundPlan
        api_response = api_instance.cancel_inbound_plan(inbound_plan_id)
        print("The response of FulfillmentInboundApi->cancel_inbound_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->cancel_inbound_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 

### Return type

[**CancelInboundPlanResponse**](CancelInboundPlanResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | CancelInboundPlan 202 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_self_ship_appointment**
> CancelSelfShipAppointmentResponse cancel_self_ship_appointment(inbound_plan_id, shipment_id, body)

cancelSelfShipAppointment

Cancels a self-ship appointment slot against a shipment.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.cancel_self_ship_appointment_request import CancelSelfShipAppointmentRequest
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.cancel_self_ship_appointment_response import CancelSelfShipAppointmentResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.
    body = py_sp_api.generated.fulfillmentInbound_2024_03_20.CancelSelfShipAppointmentRequest() # CancelSelfShipAppointmentRequest | The body of the request to `cancelSelfShipAppointment`.

    try:
        # cancelSelfShipAppointment
        api_response = api_instance.cancel_self_ship_appointment(inbound_plan_id, shipment_id, body)
        print("The response of FulfillmentInboundApi->cancel_self_ship_appointment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->cancel_self_ship_appointment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 
 **body** | [**CancelSelfShipAppointmentRequest**](CancelSelfShipAppointmentRequest.md)| The body of the request to &#x60;cancelSelfShipAppointment&#x60;. | 

### Return type

[**CancelSelfShipAppointmentResponse**](CancelSelfShipAppointmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | CancelSelfShipAppointment 202 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_delivery_window_options**
> ConfirmDeliveryWindowOptionsResponse confirm_delivery_window_options(inbound_plan_id, shipment_id, delivery_window_option_id)

confirmDeliveryWindowOptions

Confirms the delivery window option for chosen shipment within an inbound plan. A placement option must be confirmed prior to use of this API. Once confirmed, new delivery window options cannot be generated, but the chosen delivery window option can be updated before shipment closure. The window is used to provide the expected time when a shipment will arrive at the warehouse. All transportation options which have the program `CONFIRMED_DELIVERY_WINDOW` require a delivery window to be confirmed prior to transportation option confirmation.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.confirm_delivery_window_options_response import ConfirmDeliveryWindowOptionsResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    shipment_id = 'shipment_id_example' # str | The shipment to confirm the delivery window option for.
    delivery_window_option_id = 'delivery_window_option_id_example' # str | The id of the delivery window option to be confirmed.

    try:
        # confirmDeliveryWindowOptions
        api_response = api_instance.confirm_delivery_window_options(inbound_plan_id, shipment_id, delivery_window_option_id)
        print("The response of FulfillmentInboundApi->confirm_delivery_window_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->confirm_delivery_window_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| The shipment to confirm the delivery window option for. | 
 **delivery_window_option_id** | **str**| The id of the delivery window option to be confirmed. | 

### Return type

[**ConfirmDeliveryWindowOptionsResponse**](ConfirmDeliveryWindowOptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | ConfirmDeliveryWindowOptions 202 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_packing_option**
> ConfirmPackingOptionResponse confirm_packing_option(inbound_plan_id, packing_option_id)

confirmPackingOption

Confirms the packing option for an inbound plan.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 2 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.confirm_packing_option_response import ConfirmPackingOptionResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    packing_option_id = 'packing_option_id_example' # str | Identifier of a packing option.

    try:
        # confirmPackingOption
        api_response = api_instance.confirm_packing_option(inbound_plan_id, packing_option_id)
        print("The response of FulfillmentInboundApi->confirm_packing_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->confirm_packing_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **packing_option_id** | **str**| Identifier of a packing option. | 

### Return type

[**ConfirmPackingOptionResponse**](ConfirmPackingOptionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | ConfirmPackingOption 202 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_placement_option**
> ConfirmPlacementOptionResponse confirm_placement_option(inbound_plan_id, placement_option_id)

confirmPlacementOption

Confirms the placement option for an inbound plan. Once confirmed, it cannot be changed for the Inbound Plan.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 2 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.confirm_placement_option_response import ConfirmPlacementOptionResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    placement_option_id = 'placement_option_id_example' # str | The identifier of a placement option. A placement option represents the shipment splits and destinations of SKUs.

    try:
        # confirmPlacementOption
        api_response = api_instance.confirm_placement_option(inbound_plan_id, placement_option_id)
        print("The response of FulfillmentInboundApi->confirm_placement_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->confirm_placement_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **placement_option_id** | **str**| The identifier of a placement option. A placement option represents the shipment splits and destinations of SKUs. | 

### Return type

[**ConfirmPlacementOptionResponse**](ConfirmPlacementOptionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | ConfirmPlacementOption 202 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_shipment_content_update_preview**
> ConfirmShipmentContentUpdatePreviewResponse confirm_shipment_content_update_preview(inbound_plan_id, shipment_id, content_update_preview_id)

confirmShipmentContentUpdatePreview

Confirm a shipment content update preview and accept the changes in transportation cost.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.confirm_shipment_content_update_preview_response import ConfirmShipmentContentUpdatePreviewResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.
    content_update_preview_id = 'content_update_preview_id_example' # str | Identifier of a content update preview.

    try:
        # confirmShipmentContentUpdatePreview
        api_response = api_instance.confirm_shipment_content_update_preview(inbound_plan_id, shipment_id, content_update_preview_id)
        print("The response of FulfillmentInboundApi->confirm_shipment_content_update_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->confirm_shipment_content_update_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 
 **content_update_preview_id** | **str**| Identifier of a content update preview. | 

### Return type

[**ConfirmShipmentContentUpdatePreviewResponse**](ConfirmShipmentContentUpdatePreviewResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | ConfirmShipmentContentUpdatePreview 202 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_transportation_options**
> ConfirmTransportationOptionsResponse confirm_transportation_options(inbound_plan_id, body)

confirmTransportationOptions

Confirms all the transportation options for an inbound plan. A placement option must be confirmed prior to use of this API. Once confirmed, new transportation options can not be generated or confirmed for the Inbound Plan.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 2 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.confirm_transportation_options_request import ConfirmTransportationOptionsRequest
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.confirm_transportation_options_response import ConfirmTransportationOptionsResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    body = py_sp_api.generated.fulfillmentInbound_2024_03_20.ConfirmTransportationOptionsRequest() # ConfirmTransportationOptionsRequest | The body of the request to `confirmTransportationOptions`.

    try:
        # confirmTransportationOptions
        api_response = api_instance.confirm_transportation_options(inbound_plan_id, body)
        print("The response of FulfillmentInboundApi->confirm_transportation_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->confirm_transportation_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **body** | [**ConfirmTransportationOptionsRequest**](ConfirmTransportationOptionsRequest.md)| The body of the request to &#x60;confirmTransportationOptions&#x60;. | 

### Return type

[**ConfirmTransportationOptionsResponse**](ConfirmTransportationOptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | ConfirmTransportationOptions 202 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_inbound_plan**
> CreateInboundPlanResponse create_inbound_plan(body)

createInboundPlan

Creates an inbound plan. An inbound plan contains all the necessary information to send shipments into Amazon's fufillment network.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 2 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.create_inbound_plan_request import CreateInboundPlanRequest
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.create_inbound_plan_response import CreateInboundPlanResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    body = py_sp_api.generated.fulfillmentInbound_2024_03_20.CreateInboundPlanRequest() # CreateInboundPlanRequest | The body of the request to `createInboundPlan`.

    try:
        # createInboundPlan
        api_response = api_instance.create_inbound_plan(body)
        print("The response of FulfillmentInboundApi->create_inbound_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->create_inbound_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateInboundPlanRequest**](CreateInboundPlanRequest.md)| The body of the request to &#x60;createInboundPlan&#x60;. | 

### Return type

[**CreateInboundPlanResponse**](CreateInboundPlanResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | CreateInboundPlan 202 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_marketplace_item_labels**
> CreateMarketplaceItemLabelsResponse create_marketplace_item_labels(body)

createMarketplaceItemLabels

For a given marketplace - creates labels for a list of MSKUs.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.create_marketplace_item_labels_request import CreateMarketplaceItemLabelsRequest
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.create_marketplace_item_labels_response import CreateMarketplaceItemLabelsResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    body = py_sp_api.generated.fulfillmentInbound_2024_03_20.CreateMarketplaceItemLabelsRequest() # CreateMarketplaceItemLabelsRequest | The body of the request to `createMarketplaceItemLabels`.

    try:
        # createMarketplaceItemLabels
        api_response = api_instance.create_marketplace_item_labels(body)
        print("The response of FulfillmentInboundApi->create_marketplace_item_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->create_marketplace_item_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateMarketplaceItemLabelsRequest**](CreateMarketplaceItemLabelsRequest.md)| The body of the request to &#x60;createMarketplaceItemLabels&#x60;. | 

### Return type

[**CreateMarketplaceItemLabelsResponse**](CreateMarketplaceItemLabelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CreateMarketplaceItemLabels 200 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_delivery_window_options**
> GenerateDeliveryWindowOptionsResponse generate_delivery_window_options(inbound_plan_id, shipment_id)

generateDeliveryWindowOptions

Generates available delivery window options for a given shipment.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.generate_delivery_window_options_response import GenerateDeliveryWindowOptionsResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    shipment_id = 'shipment_id_example' # str | The shipment to generate delivery window options for.

    try:
        # generateDeliveryWindowOptions
        api_response = api_instance.generate_delivery_window_options(inbound_plan_id, shipment_id)
        print("The response of FulfillmentInboundApi->generate_delivery_window_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->generate_delivery_window_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| The shipment to generate delivery window options for. | 

### Return type

[**GenerateDeliveryWindowOptionsResponse**](GenerateDeliveryWindowOptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | GenerateDeliveryWindowOptions 202 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_packing_options**
> GeneratePackingOptionsResponse generate_packing_options(inbound_plan_id)

generatePackingOptions

Generates available packing options for the inbound plan.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 2 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.generate_packing_options_response import GeneratePackingOptionsResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.

    try:
        # generatePackingOptions
        api_response = api_instance.generate_packing_options(inbound_plan_id)
        print("The response of FulfillmentInboundApi->generate_packing_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->generate_packing_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 

### Return type

[**GeneratePackingOptionsResponse**](GeneratePackingOptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | GeneratePackingOptions 202 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_placement_options**
> GeneratePlacementOptionsResponse generate_placement_options(inbound_plan_id, body)

generatePlacementOptions

Generates placement options for the inbound plan.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 2 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.generate_placement_options_request import GeneratePlacementOptionsRequest
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.generate_placement_options_response import GeneratePlacementOptionsResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    body = py_sp_api.generated.fulfillmentInbound_2024_03_20.GeneratePlacementOptionsRequest() # GeneratePlacementOptionsRequest | The body of the request to `generatePlacementOptions`.

    try:
        # generatePlacementOptions
        api_response = api_instance.generate_placement_options(inbound_plan_id, body)
        print("The response of FulfillmentInboundApi->generate_placement_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->generate_placement_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **body** | [**GeneratePlacementOptionsRequest**](GeneratePlacementOptionsRequest.md)| The body of the request to &#x60;generatePlacementOptions&#x60;. | 

### Return type

[**GeneratePlacementOptionsResponse**](GeneratePlacementOptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | GeneratePlacementOptions 202 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_self_ship_appointment_slots**
> GenerateSelfShipAppointmentSlotsResponse generate_self_ship_appointment_slots(inbound_plan_id, shipment_id, body)

generateSelfShipAppointmentSlots

Initiates the process of generating the appointment slots list.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 2 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.generate_self_ship_appointment_slots_request import GenerateSelfShipAppointmentSlotsRequest
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.generate_self_ship_appointment_slots_response import GenerateSelfShipAppointmentSlotsResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.
    body = py_sp_api.generated.fulfillmentInbound_2024_03_20.GenerateSelfShipAppointmentSlotsRequest() # GenerateSelfShipAppointmentSlotsRequest | The body of the request to `generateSelfShipAppointmentSlots`.

    try:
        # generateSelfShipAppointmentSlots
        api_response = api_instance.generate_self_ship_appointment_slots(inbound_plan_id, shipment_id, body)
        print("The response of FulfillmentInboundApi->generate_self_ship_appointment_slots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->generate_self_ship_appointment_slots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 
 **body** | [**GenerateSelfShipAppointmentSlotsRequest**](GenerateSelfShipAppointmentSlotsRequest.md)| The body of the request to &#x60;generateSelfShipAppointmentSlots&#x60;. | 

### Return type

[**GenerateSelfShipAppointmentSlotsResponse**](GenerateSelfShipAppointmentSlotsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | GenerateSelfShipAppointmentSlots 201 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_shipment_content_update_previews**
> GenerateShipmentContentUpdatePreviewsResponse generate_shipment_content_update_previews(inbound_plan_id, shipment_id, body)

generateShipmentContentUpdatePreviews

Generate a shipment content update preview given a set of intended boxes and/or items for a shipment with a confirmed carrier. The shipment content update preview will be viewable with the updated costs and contents prior to confirmation.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.generate_shipment_content_update_previews_request import GenerateShipmentContentUpdatePreviewsRequest
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.generate_shipment_content_update_previews_response import GenerateShipmentContentUpdatePreviewsResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.
    body = py_sp_api.generated.fulfillmentInbound_2024_03_20.GenerateShipmentContentUpdatePreviewsRequest() # GenerateShipmentContentUpdatePreviewsRequest | The body of the request to `generateShipmentContentUpdatePreviews`.

    try:
        # generateShipmentContentUpdatePreviews
        api_response = api_instance.generate_shipment_content_update_previews(inbound_plan_id, shipment_id, body)
        print("The response of FulfillmentInboundApi->generate_shipment_content_update_previews:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->generate_shipment_content_update_previews: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 
 **body** | [**GenerateShipmentContentUpdatePreviewsRequest**](GenerateShipmentContentUpdatePreviewsRequest.md)| The body of the request to &#x60;generateShipmentContentUpdatePreviews&#x60;. | 

### Return type

[**GenerateShipmentContentUpdatePreviewsResponse**](GenerateShipmentContentUpdatePreviewsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | GenerateShipmentContentUpdatePreviews 202 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_transportation_options**
> GenerateTransportationOptionsResponse generate_transportation_options(inbound_plan_id, body)

generateTransportationOptions

Generates available transportation options for a given placement option.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 2 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.generate_transportation_options_request import GenerateTransportationOptionsRequest
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.generate_transportation_options_response import GenerateTransportationOptionsResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    body = py_sp_api.generated.fulfillmentInbound_2024_03_20.GenerateTransportationOptionsRequest() # GenerateTransportationOptionsRequest | The body of the request to `generateTransportationOptions`.

    try:
        # generateTransportationOptions
        api_response = api_instance.generate_transportation_options(inbound_plan_id, body)
        print("The response of FulfillmentInboundApi->generate_transportation_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->generate_transportation_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **body** | [**GenerateTransportationOptionsRequest**](GenerateTransportationOptionsRequest.md)| The body of the request to &#x60;generateTransportationOptions&#x60;. | 

### Return type

[**GenerateTransportationOptionsResponse**](GenerateTransportationOptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | GenerateTransportationOptions 202 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delivery_challan_document**
> GetDeliveryChallanDocumentResponse get_delivery_challan_document(inbound_plan_id, shipment_id)

getDeliveryChallanDocument

Provide delivery challan document for PCP transportation in IN marketplace.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 6 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.get_delivery_challan_document_response import GetDeliveryChallanDocumentResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.

    try:
        # getDeliveryChallanDocument
        api_response = api_instance.get_delivery_challan_document(inbound_plan_id, shipment_id)
        print("The response of FulfillmentInboundApi->get_delivery_challan_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->get_delivery_challan_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 

### Return type

[**GetDeliveryChallanDocumentResponse**](GetDeliveryChallanDocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GetDeliveryChallanDocument 200 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbound_operation_status**
> InboundOperationStatus get_inbound_operation_status(operation_id)

getInboundOperationStatus

Gets the status of the processing of an asynchronous API call.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 6 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.inbound_operation_status import InboundOperationStatus
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    operation_id = 'operation_id_example' # str | Identifier of an asynchronous operation.

    try:
        # getInboundOperationStatus
        api_response = api_instance.get_inbound_operation_status(operation_id)
        print("The response of FulfillmentInboundApi->get_inbound_operation_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->get_inbound_operation_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_id** | **str**| Identifier of an asynchronous operation. | 

### Return type

[**InboundOperationStatus**](InboundOperationStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GetInboundOperationStatus 200 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbound_plan**
> InboundPlan get_inbound_plan(inbound_plan_id)

getInboundPlan

Fetches the top level information about an inbound plan.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 6 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.inbound_plan import InboundPlan
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.

    try:
        # getInboundPlan
        api_response = api_instance.get_inbound_plan(inbound_plan_id)
        print("The response of FulfillmentInboundApi->get_inbound_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->get_inbound_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 

### Return type

[**InboundPlan**](InboundPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GetInboundPlan 200 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_ship_appointment_slots**
> GetSelfShipAppointmentSlotsResponse get_self_ship_appointment_slots(inbound_plan_id, shipment_id, page_size=page_size, pagination_token=pagination_token)

getSelfShipAppointmentSlots

Retrieves a list of available self-ship appointment slots used to drop off a shipment at a warehouse.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 6 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.get_self_ship_appointment_slots_response import GetSelfShipAppointmentSlotsResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.
    page_size = 10 # int | The number of self ship appointment slots to return in the response matching the given query. (optional) (default to 10)
    pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)

    try:
        # getSelfShipAppointmentSlots
        api_response = api_instance.get_self_ship_appointment_slots(inbound_plan_id, shipment_id, page_size=page_size, pagination_token=pagination_token)
        print("The response of FulfillmentInboundApi->get_self_ship_appointment_slots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->get_self_ship_appointment_slots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 
 **page_size** | **int**| The number of self ship appointment slots to return in the response matching the given query. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 

### Return type

[**GetSelfShipAppointmentSlotsResponse**](GetSelfShipAppointmentSlotsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GetSelfShipAppointmentSlots 200 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipment**
> Shipment get_shipment(inbound_plan_id, shipment_id)

getShipment

Provides the full details for a specific shipment within an inbound plan. The `transportationOptionId` inside `acceptedTransportationSelection` can be used to retrieve the transportation details for the shipment.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 6 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.shipment import Shipment
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.

    try:
        # getShipment
        api_response = api_instance.get_shipment(inbound_plan_id, shipment_id)
        print("The response of FulfillmentInboundApi->get_shipment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->get_shipment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 

### Return type

[**Shipment**](Shipment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GetShipment 200 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipment_content_update_preview**
> ContentUpdatePreview get_shipment_content_update_preview(inbound_plan_id, shipment_id, content_update_preview_id)

getShipmentContentUpdatePreview

Retrieve a shipment content update preview which provides a summary of the requested shipment content changes along with the transportation cost implications of the change that can only be confirmed prior to the expiry date specified.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.content_update_preview import ContentUpdatePreview
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.
    content_update_preview_id = 'content_update_preview_id_example' # str | Identifier of a content update preview.

    try:
        # getShipmentContentUpdatePreview
        api_response = api_instance.get_shipment_content_update_preview(inbound_plan_id, shipment_id, content_update_preview_id)
        print("The response of FulfillmentInboundApi->get_shipment_content_update_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->get_shipment_content_update_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 
 **content_update_preview_id** | **str**| Identifier of a content update preview. | 

### Return type

[**ContentUpdatePreview**](ContentUpdatePreview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GetShipmentContentUpdatePreview 200 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_delivery_window_options**
> ListDeliveryWindowOptionsResponse list_delivery_window_options(inbound_plan_id, shipment_id, page_size=page_size, pagination_token=pagination_token)

listDeliveryWindowOptions

Retrieves all delivery window options for a shipment. Delivery window options must first be generated by the `generateDeliveryWindowOptions` operation before becoming available.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.list_delivery_window_options_response import ListDeliveryWindowOptionsResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    shipment_id = 'shipment_id_example' # str | The shipment to get delivery window options for.
    page_size = 10 # int | The number of delivery window options to return in the response matching the given query. (optional) (default to 10)
    pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)

    try:
        # listDeliveryWindowOptions
        api_response = api_instance.list_delivery_window_options(inbound_plan_id, shipment_id, page_size=page_size, pagination_token=pagination_token)
        print("The response of FulfillmentInboundApi->list_delivery_window_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->list_delivery_window_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| The shipment to get delivery window options for. | 
 **page_size** | **int**| The number of delivery window options to return in the response matching the given query. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 

### Return type

[**ListDeliveryWindowOptionsResponse**](ListDeliveryWindowOptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListDeliveryWindowOptions 200 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inbound_plan_boxes**
> ListInboundPlanBoxesResponse list_inbound_plan_boxes(inbound_plan_id, page_size=page_size, pagination_token=pagination_token)

listInboundPlanBoxes

Provides a paginated list of box packages in an inbound plan.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 6 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.list_inbound_plan_boxes_response import ListInboundPlanBoxesResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    page_size = 10 # int | The number of boxes to return in the response matching the given query. (optional) (default to 10)
    pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)

    try:
        # listInboundPlanBoxes
        api_response = api_instance.list_inbound_plan_boxes(inbound_plan_id, page_size=page_size, pagination_token=pagination_token)
        print("The response of FulfillmentInboundApi->list_inbound_plan_boxes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->list_inbound_plan_boxes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **page_size** | **int**| The number of boxes to return in the response matching the given query. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 

### Return type

[**ListInboundPlanBoxesResponse**](ListInboundPlanBoxesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListInboundPlanBoxes 200 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inbound_plan_items**
> ListInboundPlanItemsResponse list_inbound_plan_items(inbound_plan_id, page_size=page_size, pagination_token=pagination_token)

listInboundPlanItems

Provides a paginated list of item packages in an inbound plan.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 6 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.list_inbound_plan_items_response import ListInboundPlanItemsResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    page_size = 10 # int | The number of items to return in the response matching the given query. (optional) (default to 10)
    pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)

    try:
        # listInboundPlanItems
        api_response = api_instance.list_inbound_plan_items(inbound_plan_id, page_size=page_size, pagination_token=pagination_token)
        print("The response of FulfillmentInboundApi->list_inbound_plan_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->list_inbound_plan_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **page_size** | **int**| The number of items to return in the response matching the given query. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 

### Return type

[**ListInboundPlanItemsResponse**](ListInboundPlanItemsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListInboundPlanItems 200 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inbound_plan_pallets**
> ListInboundPlanPalletsResponse list_inbound_plan_pallets(inbound_plan_id, page_size=page_size, pagination_token=pagination_token)

listInboundPlanPallets

Provides a paginated list of pallet packages in an inbound plan. An inbound plan will have pallets when the related details are provided after generating Less-Than-Truckload (LTL) carrier shipments.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 6 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.list_inbound_plan_pallets_response import ListInboundPlanPalletsResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    page_size = 10 # int | The number of pallets to return in the response matching the given query. (optional) (default to 10)
    pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)

    try:
        # listInboundPlanPallets
        api_response = api_instance.list_inbound_plan_pallets(inbound_plan_id, page_size=page_size, pagination_token=pagination_token)
        print("The response of FulfillmentInboundApi->list_inbound_plan_pallets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->list_inbound_plan_pallets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **page_size** | **int**| The number of pallets to return in the response matching the given query. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 

### Return type

[**ListInboundPlanPalletsResponse**](ListInboundPlanPalletsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListInboundPlanPallets 200 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inbound_plans**
> ListInboundPlansResponse list_inbound_plans(page_size=page_size, pagination_token=pagination_token, status=status, sort_by=sort_by, sort_order=sort_order)

listInboundPlans

Provides a list of inbound plans with minimal information.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 6 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.list_inbound_plans_response import ListInboundPlansResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    page_size = 10 # int | The number of inbound plans to return in the response matching the given query. (optional) (default to 10)
    pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)
    status = 'status_example' # str | The status of an inbound plan. (optional)
    sort_by = 'sort_by_example' # str | Sort by field. (optional)
    sort_order = 'sort_order_example' # str | The sort order. (optional)

    try:
        # listInboundPlans
        api_response = api_instance.list_inbound_plans(page_size=page_size, pagination_token=pagination_token, status=status, sort_by=sort_by, sort_order=sort_order)
        print("The response of FulfillmentInboundApi->list_inbound_plans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->list_inbound_plans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of inbound plans to return in the response matching the given query. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 
 **status** | **str**| The status of an inbound plan. | [optional] 
 **sort_by** | **str**| Sort by field. | [optional] 
 **sort_order** | **str**| The sort order. | [optional] 

### Return type

[**ListInboundPlansResponse**](ListInboundPlansResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListInboundPlans 200 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_item_compliance_details**
> ListItemComplianceDetailsResponse list_item_compliance_details(mskus, marketplace_id)

listItemComplianceDetails

List the inbound compliance details for MSKUs in a given marketplace.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 6 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.list_item_compliance_details_response import ListItemComplianceDetailsResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    mskus = ['mskus_example'] # List[str] | A list of merchant SKUs, a merchant-supplied identifier of a specific SKU.
    marketplace_id = 'marketplace_id_example' # str | The Marketplace ID. For a list of possible values, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).

    try:
        # listItemComplianceDetails
        api_response = api_instance.list_item_compliance_details(mskus, marketplace_id)
        print("The response of FulfillmentInboundApi->list_item_compliance_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->list_item_compliance_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mskus** | [**List[str]**](str.md)| A list of merchant SKUs, a merchant-supplied identifier of a specific SKU. | 
 **marketplace_id** | **str**| The Marketplace ID. For a list of possible values, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids). | 

### Return type

[**ListItemComplianceDetailsResponse**](ListItemComplianceDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListItemComplianceDetails 200 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_packing_group_boxes**
> ListPackingGroupBoxesResponse list_packing_group_boxes(inbound_plan_id, packing_group_id, page_size=page_size, pagination_token=pagination_token)

listPackingGroupBoxes

Retrieves a page of boxes from a given packing group. These boxes were previously provided through the `setPackingInformation` operation. This API is used for workflows where boxes are packed before Amazon determines shipment splits.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.list_packing_group_boxes_response import ListPackingGroupBoxesResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    packing_group_id = 'packing_group_id_example' # str | Identifier of a packing group.
    page_size = 10 # int | The number of packing group boxes to return in the response matching the given query. (optional) (default to 10)
    pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)

    try:
        # listPackingGroupBoxes
        api_response = api_instance.list_packing_group_boxes(inbound_plan_id, packing_group_id, page_size=page_size, pagination_token=pagination_token)
        print("The response of FulfillmentInboundApi->list_packing_group_boxes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->list_packing_group_boxes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **packing_group_id** | **str**| Identifier of a packing group. | 
 **page_size** | **int**| The number of packing group boxes to return in the response matching the given query. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 

### Return type

[**ListPackingGroupBoxesResponse**](ListPackingGroupBoxesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListPackingGroupBoxes 200 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_packing_group_items**
> ListPackingGroupItemsResponse list_packing_group_items(inbound_plan_id, packing_group_id, page_size=page_size, pagination_token=pagination_token)

listPackingGroupItems

Retrieves a page of items in a given packing group. Packing options must first be generated by the corresponding operation before packing group items can be listed.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.list_packing_group_items_response import ListPackingGroupItemsResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    packing_group_id = 'packing_group_id_example' # str | Identifier of a packing group.
    page_size = 10 # int | The number of packing group items to return in the response matching the given query. (optional) (default to 10)
    pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)

    try:
        # listPackingGroupItems
        api_response = api_instance.list_packing_group_items(inbound_plan_id, packing_group_id, page_size=page_size, pagination_token=pagination_token)
        print("The response of FulfillmentInboundApi->list_packing_group_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->list_packing_group_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **packing_group_id** | **str**| Identifier of a packing group. | 
 **page_size** | **int**| The number of packing group items to return in the response matching the given query. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 

### Return type

[**ListPackingGroupItemsResponse**](ListPackingGroupItemsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListPackingGroupItems 200 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_packing_options**
> ListPackingOptionsResponse list_packing_options(inbound_plan_id, page_size=page_size, pagination_token=pagination_token)

listPackingOptions

Retrieves a list of all packing options for an inbound plan. Packing options must first be generated by the corresponding operation before becoming available.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 6 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.list_packing_options_response import ListPackingOptionsResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    page_size = 10 # int | The number of packing options to return in the response matching the given query. (optional) (default to 10)
    pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)

    try:
        # listPackingOptions
        api_response = api_instance.list_packing_options(inbound_plan_id, page_size=page_size, pagination_token=pagination_token)
        print("The response of FulfillmentInboundApi->list_packing_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->list_packing_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **page_size** | **int**| The number of packing options to return in the response matching the given query. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 

### Return type

[**ListPackingOptionsResponse**](ListPackingOptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListPackingOptions 200 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_placement_options**
> ListPlacementOptionsResponse list_placement_options(inbound_plan_id, page_size=page_size, pagination_token=pagination_token)

listPlacementOptions

Provides a list of all placement options for an inbound plan. Placement options must first be generated by the corresponding operation before becoming available.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 6 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.list_placement_options_response import ListPlacementOptionsResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    page_size = 10 # int | The number of placement options to return in the response matching the given query. (optional) (default to 10)
    pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)

    try:
        # listPlacementOptions
        api_response = api_instance.list_placement_options(inbound_plan_id, page_size=page_size, pagination_token=pagination_token)
        print("The response of FulfillmentInboundApi->list_placement_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->list_placement_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **page_size** | **int**| The number of placement options to return in the response matching the given query. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 

### Return type

[**ListPlacementOptionsResponse**](ListPlacementOptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListPlacementOptions 200 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_prep_details**
> ListPrepDetailsResponse list_prep_details(marketplace_id, mskus)

listPrepDetails

Get preparation details for a list of MSKUs in a specified marketplace.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.list_prep_details_response import ListPrepDetailsResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    marketplace_id = 'marketplace_id_example' # str | The marketplace ID. For a list of possible values, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
    mskus = ['mskus_example'] # List[str] | A list of merchant SKUs, a merchant-supplied identifier of a specific SKU.

    try:
        # listPrepDetails
        api_response = api_instance.list_prep_details(marketplace_id, mskus)
        print("The response of FulfillmentInboundApi->list_prep_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->list_prep_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| The marketplace ID. For a list of possible values, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids). | 
 **mskus** | [**List[str]**](str.md)| A list of merchant SKUs, a merchant-supplied identifier of a specific SKU. | 

### Return type

[**ListPrepDetailsResponse**](ListPrepDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListPrepDetails 200 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_shipment_boxes**
> ListShipmentBoxesResponse list_shipment_boxes(inbound_plan_id, shipment_id, page_size=page_size, pagination_token=pagination_token)

listShipmentBoxes

Provides a paginated list of box packages in a shipment.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.list_shipment_boxes_response import ListShipmentBoxesResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.
    page_size = 10 # int | The number of boxes to return in the response matching the given query. (optional) (default to 10)
    pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)

    try:
        # listShipmentBoxes
        api_response = api_instance.list_shipment_boxes(inbound_plan_id, shipment_id, page_size=page_size, pagination_token=pagination_token)
        print("The response of FulfillmentInboundApi->list_shipment_boxes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->list_shipment_boxes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 
 **page_size** | **int**| The number of boxes to return in the response matching the given query. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 

### Return type

[**ListShipmentBoxesResponse**](ListShipmentBoxesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListShipmentBoxes 200 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_shipment_content_update_previews**
> ListShipmentContentUpdatePreviewsResponse list_shipment_content_update_previews(inbound_plan_id, shipment_id, page_size=page_size, pagination_token=pagination_token)

listShipmentContentUpdatePreviews

Retrieve a paginated list of shipment content update previews for a given shipment. The shipment content update preview is a summary of the requested shipment content changes along with the transportation cost implications of the change that can only be confirmed prior to the expiry date specified.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.list_shipment_content_update_previews_response import ListShipmentContentUpdatePreviewsResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.
    page_size = 10 # int | The number of content update previews to return. (optional) (default to 10)
    pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)

    try:
        # listShipmentContentUpdatePreviews
        api_response = api_instance.list_shipment_content_update_previews(inbound_plan_id, shipment_id, page_size=page_size, pagination_token=pagination_token)
        print("The response of FulfillmentInboundApi->list_shipment_content_update_previews:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->list_shipment_content_update_previews: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 
 **page_size** | **int**| The number of content update previews to return. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 

### Return type

[**ListShipmentContentUpdatePreviewsResponse**](ListShipmentContentUpdatePreviewsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListShipmentContentUpdatePreviews 200 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_shipment_items**
> ListShipmentItemsResponse list_shipment_items(inbound_plan_id, shipment_id, page_size=page_size, pagination_token=pagination_token)

listShipmentItems

Provides a paginated list of item packages in a shipment.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.list_shipment_items_response import ListShipmentItemsResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.
    page_size = 10 # int | The number of items to return in the response matching the given query. (optional) (default to 10)
    pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)

    try:
        # listShipmentItems
        api_response = api_instance.list_shipment_items(inbound_plan_id, shipment_id, page_size=page_size, pagination_token=pagination_token)
        print("The response of FulfillmentInboundApi->list_shipment_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->list_shipment_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 
 **page_size** | **int**| The number of items to return in the response matching the given query. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 

### Return type

[**ListShipmentItemsResponse**](ListShipmentItemsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListShipmentItems 200 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_shipment_pallets**
> ListShipmentPalletsResponse list_shipment_pallets(inbound_plan_id, shipment_id, page_size=page_size, pagination_token=pagination_token)

listShipmentPallets

Provides a paginated list of pallet packages in a shipment. A palletized shipment will have pallets when the related details are provided after generating Less-Than-Truckload (LTL) carrier shipments.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.list_shipment_pallets_response import ListShipmentPalletsResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.
    page_size = 10 # int | The number of pallets to return in the response matching the given query. (optional) (default to 10)
    pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)

    try:
        # listShipmentPallets
        api_response = api_instance.list_shipment_pallets(inbound_plan_id, shipment_id, page_size=page_size, pagination_token=pagination_token)
        print("The response of FulfillmentInboundApi->list_shipment_pallets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->list_shipment_pallets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 
 **page_size** | **int**| The number of pallets to return in the response matching the given query. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 

### Return type

[**ListShipmentPalletsResponse**](ListShipmentPalletsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListShipmentPallets 200 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transportation_options**
> ListTransportationOptionsResponse list_transportation_options(inbound_plan_id, page_size=page_size, pagination_token=pagination_token, placement_option_id=placement_option_id, shipment_id=shipment_id)

listTransportationOptions

Retrieves all transportation options for a shipment. Transportation options must first be generated by the `generateTransportationOptions` operation before becoming available.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 6 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.list_transportation_options_response import ListTransportationOptionsResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    page_size = 10 # int | The number of transportation options to return in the response matching the given query. (optional) (default to 10)
    pagination_token = 'pagination_token_example' # str | A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. (optional)
    placement_option_id = 'placement_option_id_example' # str | The placement option to get transportation options for. Either `placementOptionId` or `shipmentId` must be specified. (optional)
    shipment_id = 'shipment_id_example' # str | The shipment to get transportation options for. Either `placementOptionId` or `shipmentId` must be specified. (optional)

    try:
        # listTransportationOptions
        api_response = api_instance.list_transportation_options(inbound_plan_id, page_size=page_size, pagination_token=pagination_token, placement_option_id=placement_option_id, shipment_id=shipment_id)
        print("The response of FulfillmentInboundApi->list_transportation_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->list_transportation_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **page_size** | **int**| The number of transportation options to return in the response matching the given query. | [optional] [default to 10]
 **pagination_token** | **str**| A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the &#x60;pagination&#x60; returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result. | [optional] 
 **placement_option_id** | **str**| The placement option to get transportation options for. Either &#x60;placementOptionId&#x60; or &#x60;shipmentId&#x60; must be specified. | [optional] 
 **shipment_id** | **str**| The shipment to get transportation options for. Either &#x60;placementOptionId&#x60; or &#x60;shipmentId&#x60; must be specified. | [optional] 

### Return type

[**ListTransportationOptionsResponse**](ListTransportationOptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListTransportationOptions 200 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_self_ship_appointment**
> ScheduleSelfShipAppointmentResponse schedule_self_ship_appointment(inbound_plan_id, shipment_id, slot_id, body)

scheduleSelfShipAppointment

Confirms or reschedules a self-ship appointment slot against a shipment.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 2 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.schedule_self_ship_appointment_request import ScheduleSelfShipAppointmentRequest
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.schedule_self_ship_appointment_response import ScheduleSelfShipAppointmentResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.
    slot_id = 'slot_id_example' # str | An identifier to a self-ship appointment slot.
    body = py_sp_api.generated.fulfillmentInbound_2024_03_20.ScheduleSelfShipAppointmentRequest() # ScheduleSelfShipAppointmentRequest | The body of the request to `scheduleSelfShipAppointment`.

    try:
        # scheduleSelfShipAppointment
        api_response = api_instance.schedule_self_ship_appointment(inbound_plan_id, shipment_id, slot_id, body)
        print("The response of FulfillmentInboundApi->schedule_self_ship_appointment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->schedule_self_ship_appointment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 
 **slot_id** | **str**| An identifier to a self-ship appointment slot. | 
 **body** | [**ScheduleSelfShipAppointmentRequest**](ScheduleSelfShipAppointmentRequest.md)| The body of the request to &#x60;scheduleSelfShipAppointment&#x60;. | 

### Return type

[**ScheduleSelfShipAppointmentResponse**](ScheduleSelfShipAppointmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ScheduleSelfShipAppointment 200 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_packing_information**
> SetPackingInformationResponse set_packing_information(inbound_plan_id, body)

setPackingInformation

Sets packing information for an inbound plan. This should be called after an inbound plan is created to populate the box level information required for planning and transportation estimates.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 2 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.set_packing_information_request import SetPackingInformationRequest
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.set_packing_information_response import SetPackingInformationResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    body = py_sp_api.generated.fulfillmentInbound_2024_03_20.SetPackingInformationRequest() # SetPackingInformationRequest | The body of the request to `setPackingInformation`.

    try:
        # setPackingInformation
        api_response = api_instance.set_packing_information(inbound_plan_id, body)
        print("The response of FulfillmentInboundApi->set_packing_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->set_packing_information: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **body** | [**SetPackingInformationRequest**](SetPackingInformationRequest.md)| The body of the request to &#x60;setPackingInformation&#x60;. | 

### Return type

[**SetPackingInformationResponse**](SetPackingInformationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | SetPackingInformation 202 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_prep_details**
> SetPrepDetailsResponse set_prep_details(body)

setPrepDetails

Set the preparation details for a list of MSKUs in a specified marketplace.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.set_prep_details_request import SetPrepDetailsRequest
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.set_prep_details_response import SetPrepDetailsResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    body = py_sp_api.generated.fulfillmentInbound_2024_03_20.SetPrepDetailsRequest() # SetPrepDetailsRequest | The body of the request to `setPrepDetails`.

    try:
        # setPrepDetails
        api_response = api_instance.set_prep_details(body)
        print("The response of FulfillmentInboundApi->set_prep_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->set_prep_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetPrepDetailsRequest**](SetPrepDetailsRequest.md)| The body of the request to &#x60;setPrepDetails&#x60;. | 

### Return type

[**SetPrepDetailsResponse**](SetPrepDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | SetPrepDetails 202 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inbound_plan_name**
> update_inbound_plan_name(inbound_plan_id, body)

updateInboundPlanName

Updates the name of an existing inbound plan.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.update_inbound_plan_name_request import UpdateInboundPlanNameRequest
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    body = py_sp_api.generated.fulfillmentInbound_2024_03_20.UpdateInboundPlanNameRequest() # UpdateInboundPlanNameRequest | The body of the request to `updateInboundPlanName`.

    try:
        # updateInboundPlanName
        api_instance.update_inbound_plan_name(inbound_plan_id, body)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->update_inbound_plan_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **body** | [**UpdateInboundPlanNameRequest**](UpdateInboundPlanNameRequest.md)| The body of the request to &#x60;updateInboundPlanName&#x60;. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | UpdateInboundPlanName 204 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_compliance_details**
> UpdateItemComplianceDetailsResponse update_item_compliance_details(marketplace_id, body)

updateItemComplianceDetails

Update compliance details for a list of MSKUs. The details provided here are only used for the India (IN - A21TJRUUN4KGV) marketplace compliance validation.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 6 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.update_item_compliance_details_request import UpdateItemComplianceDetailsRequest
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.update_item_compliance_details_response import UpdateItemComplianceDetailsResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    marketplace_id = 'marketplace_id_example' # str | The Marketplace ID. For a list of possible values, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
    body = py_sp_api.generated.fulfillmentInbound_2024_03_20.UpdateItemComplianceDetailsRequest() # UpdateItemComplianceDetailsRequest | The body of the request to `updateItemComplianceDetails`.

    try:
        # updateItemComplianceDetails
        api_response = api_instance.update_item_compliance_details(marketplace_id, body)
        print("The response of FulfillmentInboundApi->update_item_compliance_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->update_item_compliance_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**| The Marketplace ID. For a list of possible values, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids). | 
 **body** | [**UpdateItemComplianceDetailsRequest**](UpdateItemComplianceDetailsRequest.md)| The body of the request to &#x60;updateItemComplianceDetails&#x60;. | 

### Return type

[**UpdateItemComplianceDetailsResponse**](UpdateItemComplianceDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | UpdateItemComplianceDetails 202 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shipment_name**
> update_shipment_name(inbound_plan_id, shipment_id, body)

updateShipmentName

Updates the name of an existing shipment.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.update_shipment_name_request import UpdateShipmentNameRequest
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.
    body = py_sp_api.generated.fulfillmentInbound_2024_03_20.UpdateShipmentNameRequest() # UpdateShipmentNameRequest | The body of the request to `updateShipmentName`.

    try:
        # updateShipmentName
        api_instance.update_shipment_name(inbound_plan_id, shipment_id, body)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->update_shipment_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 
 **body** | [**UpdateShipmentNameRequest**](UpdateShipmentNameRequest.md)| The body of the request to &#x60;updateShipmentName&#x60;. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | UpdateShipmentName 204 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shipment_source_address**
> UpdateShipmentSourceAddressResponse update_shipment_source_address(inbound_plan_id, shipment_id, body)

updateShipmentSourceAddress

Updates the source address of an existing shipment. The shipment source address can only be updated prior to the confirmation of the shipment carriers. As a result of the updated source address, existing transportation options will be invalidated and will need to be regenerated to capture the potential difference in transportation options and quotes due to the new source address.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.update_shipment_source_address_request import UpdateShipmentSourceAddressRequest
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.update_shipment_source_address_response import UpdateShipmentSourceAddressResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.
    body = py_sp_api.generated.fulfillmentInbound_2024_03_20.UpdateShipmentSourceAddressRequest() # UpdateShipmentSourceAddressRequest | The body of the request to `updateShipmentSourceAddress`.

    try:
        # updateShipmentSourceAddress
        api_response = api_instance.update_shipment_source_address(inbound_plan_id, shipment_id, body)
        print("The response of FulfillmentInboundApi->update_shipment_source_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->update_shipment_source_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 
 **body** | [**UpdateShipmentSourceAddressRequest**](UpdateShipmentSourceAddressRequest.md)| The body of the request to &#x60;updateShipmentSourceAddress&#x60;. | 

### Return type

[**UpdateShipmentSourceAddressResponse**](UpdateShipmentSourceAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | UpdateShipmentSourceAddress 202 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shipment_tracking_details**
> UpdateShipmentTrackingDetailsResponse update_shipment_tracking_details(inbound_plan_id, shipment_id, body)

updateShipmentTrackingDetails

Updates a shipment's tracking details.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 2 |  The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

### Example


```python
import py_sp_api.generated.fulfillmentInbound_2024_03_20
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.update_shipment_tracking_details_request import UpdateShipmentTrackingDetailsRequest
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.update_shipment_tracking_details_response import UpdateShipmentTrackingDetailsResponse
from py_sp_api.generated.fulfillmentInbound_2024_03_20.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sellingpartnerapi-na.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = py_sp_api.generated.fulfillmentInbound_2024_03_20.Configuration(
    host = "https://sellingpartnerapi-na.amazon.com"
)


# Enter a context with an instance of the API client
with py_sp_api.generated.fulfillmentInbound_2024_03_20.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_sp_api.generated.fulfillmentInbound_2024_03_20.FulfillmentInboundApi(api_client)
    inbound_plan_id = 'inbound_plan_id_example' # str | Identifier of an inbound plan.
    shipment_id = 'shipment_id_example' # str | Identifier of a shipment. A shipment contains the boxes and units being inbounded.
    body = py_sp_api.generated.fulfillmentInbound_2024_03_20.UpdateShipmentTrackingDetailsRequest() # UpdateShipmentTrackingDetailsRequest | The body of the request to `updateShipmentTrackingDetails`.

    try:
        # updateShipmentTrackingDetails
        api_response = api_instance.update_shipment_tracking_details(inbound_plan_id, shipment_id, body)
        print("The response of FulfillmentInboundApi->update_shipment_tracking_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentInboundApi->update_shipment_tracking_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_plan_id** | **str**| Identifier of an inbound plan. | 
 **shipment_id** | **str**| Identifier of a shipment. A shipment contains the boxes and units being inbounded. | 
 **body** | [**UpdateShipmentTrackingDetailsRequest**](UpdateShipmentTrackingDetailsRequest.md)| The body of the request to &#x60;updateShipmentTrackingDetails&#x60;. | 

### Return type

[**UpdateShipmentTrackingDetailsResponse**](UpdateShipmentTrackingDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | UpdateShipmentTrackingDetails 202 response |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**400** | Request has missing or invalid parameters and cannot be parsed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**403** | Indicates that access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**404** | The resource specified does not exist. |  * x-amzn-RequestId - Unique request reference identifier. <br>  * x-amzn-RateLimit-Limit - Your rate limit (requests per second) for this operation. <br>  |
**413** | The request size exceeded the maximum accepted size. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**415** | The request payload is in an unsupported format. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**429** | The frequency of requests was greater than allowed. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**500** | An unexpected condition occurred that prevented the server from fulfilling the request. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |
**503** | Temporary overloading or maintenance of the server. |  * x-amzn-RequestId - Unique request reference identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

