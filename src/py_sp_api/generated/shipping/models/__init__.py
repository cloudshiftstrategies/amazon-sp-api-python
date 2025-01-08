# coding: utf-8

# flake8: noqa
"""
    Selling Partner API for Shipping

    Provides programmatic access to Amazon Shipping APIs.   **Note:** If you are new to the Amazon Shipping API, refer to the latest version of <a href=\"https://developer-docs.amazon.com/amazon-shipping/docs/shipping-api-v2-reference\">Amazon Shipping API (v2)</a> on the <a href=\"https://developer-docs.amazon.com/amazon-shipping/\">Amazon Shipping Developer Documentation</a> site.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from py_sp_api.generated.shipping.models.accepted_rate import AcceptedRate
from py_sp_api.generated.shipping.models.account import Account
from py_sp_api.generated.shipping.models.address import Address
from py_sp_api.generated.shipping.models.cancel_shipment_response import CancelShipmentResponse
from py_sp_api.generated.shipping.models.container import Container
from py_sp_api.generated.shipping.models.container_item import ContainerItem
from py_sp_api.generated.shipping.models.container_specification import ContainerSpecification
from py_sp_api.generated.shipping.models.create_shipment_request import CreateShipmentRequest
from py_sp_api.generated.shipping.models.create_shipment_response import CreateShipmentResponse
from py_sp_api.generated.shipping.models.create_shipment_result import CreateShipmentResult
from py_sp_api.generated.shipping.models.currency import Currency
from py_sp_api.generated.shipping.models.dimensions import Dimensions
from py_sp_api.generated.shipping.models.error import Error
from py_sp_api.generated.shipping.models.event import Event
from py_sp_api.generated.shipping.models.get_account_response import GetAccountResponse
from py_sp_api.generated.shipping.models.get_rates_request import GetRatesRequest
from py_sp_api.generated.shipping.models.get_rates_response import GetRatesResponse
from py_sp_api.generated.shipping.models.get_rates_result import GetRatesResult
from py_sp_api.generated.shipping.models.get_shipment_response import GetShipmentResponse
from py_sp_api.generated.shipping.models.get_tracking_information_response import GetTrackingInformationResponse
from py_sp_api.generated.shipping.models.label import Label
from py_sp_api.generated.shipping.models.label_result import LabelResult
from py_sp_api.generated.shipping.models.label_specification import LabelSpecification
from py_sp_api.generated.shipping.models.location import Location
from py_sp_api.generated.shipping.models.party import Party
from py_sp_api.generated.shipping.models.purchase_labels_request import PurchaseLabelsRequest
from py_sp_api.generated.shipping.models.purchase_labels_response import PurchaseLabelsResponse
from py_sp_api.generated.shipping.models.purchase_labels_result import PurchaseLabelsResult
from py_sp_api.generated.shipping.models.purchase_shipment_request import PurchaseShipmentRequest
from py_sp_api.generated.shipping.models.purchase_shipment_response import PurchaseShipmentResponse
from py_sp_api.generated.shipping.models.purchase_shipment_result import PurchaseShipmentResult
from py_sp_api.generated.shipping.models.rate import Rate
from py_sp_api.generated.shipping.models.retrieve_shipping_label_request import RetrieveShippingLabelRequest
from py_sp_api.generated.shipping.models.retrieve_shipping_label_response import RetrieveShippingLabelResponse
from py_sp_api.generated.shipping.models.retrieve_shipping_label_result import RetrieveShippingLabelResult
from py_sp_api.generated.shipping.models.service_rate import ServiceRate
from py_sp_api.generated.shipping.models.service_type import ServiceType
from py_sp_api.generated.shipping.models.shipment import Shipment
from py_sp_api.generated.shipping.models.shipping_promise_set import ShippingPromiseSet
from py_sp_api.generated.shipping.models.time_range import TimeRange
from py_sp_api.generated.shipping.models.tracking_information import TrackingInformation
from py_sp_api.generated.shipping.models.tracking_summary import TrackingSummary
from py_sp_api.generated.shipping.models.weight import Weight
