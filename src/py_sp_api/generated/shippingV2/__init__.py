# coding: utf-8

# flake8: noqa

"""
    Amazon Shipping API

    The Amazon Shipping API is designed to support outbound shipping use cases both for orders originating on Amazon-owned marketplaces as well as external channels/marketplaces. With these APIs, you can request shipping rates, create shipments, cancel shipments, and track shipments.

    The version of the OpenAPI document: v2
    Contact: swa-api-core@amazon.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from py_sp_api.generated.shippingV2.api.shipping_api import ShippingApi

# import ApiClient
from py_sp_api.generated.shippingV2.api_response import ApiResponse
from py_sp_api.generated.shippingV2.api_client import ApiClient
from py_sp_api.generated.shippingV2.configuration import Configuration
from py_sp_api.generated.shippingV2.exceptions import OpenApiException
from py_sp_api.generated.shippingV2.exceptions import ApiTypeError
from py_sp_api.generated.shippingV2.exceptions import ApiValueError
from py_sp_api.generated.shippingV2.exceptions import ApiKeyError
from py_sp_api.generated.shippingV2.exceptions import ApiAttributeError
from py_sp_api.generated.shippingV2.exceptions import ApiException

# import models into sdk package
from py_sp_api.generated.shippingV2.models.access_point import AccessPoint
from py_sp_api.generated.shippingV2.models.access_point_details import AccessPointDetails
from py_sp_api.generated.shippingV2.models.access_point_type import AccessPointType
from py_sp_api.generated.shippingV2.models.accessibility_attributes import AccessibilityAttributes
from py_sp_api.generated.shippingV2.models.account_status import AccountStatus
from py_sp_api.generated.shippingV2.models.account_type import AccountType
from py_sp_api.generated.shippingV2.models.active_account import ActiveAccount
from py_sp_api.generated.shippingV2.models.address import Address
from py_sp_api.generated.shippingV2.models.amazon_order_details import AmazonOrderDetails
from py_sp_api.generated.shippingV2.models.amazon_shipment_details import AmazonShipmentDetails
from py_sp_api.generated.shippingV2.models.available_value_added_service_group import AvailableValueAddedServiceGroup
from py_sp_api.generated.shippingV2.models.benefits import Benefits
from py_sp_api.generated.shippingV2.models.cancel_shipment_response import CancelShipmentResponse
from py_sp_api.generated.shippingV2.models.carrier import Carrier
from py_sp_api.generated.shippingV2.models.carrier_account_attribute import CarrierAccountAttribute
from py_sp_api.generated.shippingV2.models.carrier_account_input import CarrierAccountInput
from py_sp_api.generated.shippingV2.models.channel_details import ChannelDetails
from py_sp_api.generated.shippingV2.models.channel_type import ChannelType
from py_sp_api.generated.shippingV2.models.charge_component import ChargeComponent
from py_sp_api.generated.shippingV2.models.client_reference_detail import ClientReferenceDetail
from py_sp_api.generated.shippingV2.models.collect_on_delivery import CollectOnDelivery
from py_sp_api.generated.shippingV2.models.collection_forms_history_record import CollectionFormsHistoryRecord
from py_sp_api.generated.shippingV2.models.collections_form_document import CollectionsFormDocument
from py_sp_api.generated.shippingV2.models.currency import Currency
from py_sp_api.generated.shippingV2.models.dangerous_goods_details import DangerousGoodsDetails
from py_sp_api.generated.shippingV2.models.date_range import DateRange
from py_sp_api.generated.shippingV2.models.dimensions import Dimensions
from py_sp_api.generated.shippingV2.models.direct_fulfillment_item_identifiers import DirectFulfillmentItemIdentifiers
from py_sp_api.generated.shippingV2.models.direct_purchase_request import DirectPurchaseRequest
from py_sp_api.generated.shippingV2.models.direct_purchase_response import DirectPurchaseResponse
from py_sp_api.generated.shippingV2.models.direct_purchase_result import DirectPurchaseResult
from py_sp_api.generated.shippingV2.models.document_format import DocumentFormat
from py_sp_api.generated.shippingV2.models.document_size import DocumentSize
from py_sp_api.generated.shippingV2.models.document_type import DocumentType
from py_sp_api.generated.shippingV2.models.error import Error
from py_sp_api.generated.shippingV2.models.error_list import ErrorList
from py_sp_api.generated.shippingV2.models.event import Event
from py_sp_api.generated.shippingV2.models.event_code import EventCode
from py_sp_api.generated.shippingV2.models.exception_operating_hours import ExceptionOperatingHours
from py_sp_api.generated.shippingV2.models.excluded_benefit import ExcludedBenefit
from py_sp_api.generated.shippingV2.models.generate_collection_form_request import GenerateCollectionFormRequest
from py_sp_api.generated.shippingV2.models.generate_collection_form_response import GenerateCollectionFormResponse
from py_sp_api.generated.shippingV2.models.generation_status import GenerationStatus
from py_sp_api.generated.shippingV2.models.geocode import Geocode
from py_sp_api.generated.shippingV2.models.get_access_points_response import GetAccessPointsResponse
from py_sp_api.generated.shippingV2.models.get_access_points_result import GetAccessPointsResult
from py_sp_api.generated.shippingV2.models.get_additional_inputs_response import GetAdditionalInputsResponse
from py_sp_api.generated.shippingV2.models.get_carrier_account_form_inputs_response import GetCarrierAccountFormInputsResponse
from py_sp_api.generated.shippingV2.models.get_carrier_accounts_request import GetCarrierAccountsRequest
from py_sp_api.generated.shippingV2.models.get_carrier_accounts_response import GetCarrierAccountsResponse
from py_sp_api.generated.shippingV2.models.get_collection_form_history_request import GetCollectionFormHistoryRequest
from py_sp_api.generated.shippingV2.models.get_collection_form_history_response import GetCollectionFormHistoryResponse
from py_sp_api.generated.shippingV2.models.get_collection_form_response import GetCollectionFormResponse
from py_sp_api.generated.shippingV2.models.get_rates_request import GetRatesRequest
from py_sp_api.generated.shippingV2.models.get_rates_response import GetRatesResponse
from py_sp_api.generated.shippingV2.models.get_rates_result import GetRatesResult
from py_sp_api.generated.shippingV2.models.get_shipment_documents_response import GetShipmentDocumentsResponse
from py_sp_api.generated.shippingV2.models.get_shipment_documents_result import GetShipmentDocumentsResult
from py_sp_api.generated.shippingV2.models.get_tracking_response import GetTrackingResponse
from py_sp_api.generated.shippingV2.models.get_tracking_result import GetTrackingResult
from py_sp_api.generated.shippingV2.models.get_unmanifested_shipments_request import GetUnmanifestedShipmentsRequest
from py_sp_api.generated.shippingV2.models.get_unmanifested_shipments_response import GetUnmanifestedShipmentsResponse
from py_sp_api.generated.shippingV2.models.ineligibility_reason import IneligibilityReason
from py_sp_api.generated.shippingV2.models.ineligibility_reason_code import IneligibilityReasonCode
from py_sp_api.generated.shippingV2.models.ineligible_rate import IneligibleRate
from py_sp_api.generated.shippingV2.models.input_type import InputType
from py_sp_api.generated.shippingV2.models.invoice_details import InvoiceDetails
from py_sp_api.generated.shippingV2.models.item import Item
from py_sp_api.generated.shippingV2.models.link_carrier_account_request import LinkCarrierAccountRequest
from py_sp_api.generated.shippingV2.models.link_carrier_account_response import LinkCarrierAccountResponse
from py_sp_api.generated.shippingV2.models.linkable_account_type import LinkableAccountType
from py_sp_api.generated.shippingV2.models.linkable_carrier import LinkableCarrier
from py_sp_api.generated.shippingV2.models.liquid_volume import LiquidVolume
from py_sp_api.generated.shippingV2.models.location import Location
from py_sp_api.generated.shippingV2.models.one_click_shipment_request import OneClickShipmentRequest
from py_sp_api.generated.shippingV2.models.one_click_shipment_response import OneClickShipmentResponse
from py_sp_api.generated.shippingV2.models.one_click_shipment_result import OneClickShipmentResult
from py_sp_api.generated.shippingV2.models.one_click_shipment_value_added_service import OneClickShipmentValueAddedService
from py_sp_api.generated.shippingV2.models.operating_hours import OperatingHours
from py_sp_api.generated.shippingV2.models.package import Package
from py_sp_api.generated.shippingV2.models.package_document import PackageDocument
from py_sp_api.generated.shippingV2.models.package_document_detail import PackageDocumentDetail
from py_sp_api.generated.shippingV2.models.payment_type import PaymentType
from py_sp_api.generated.shippingV2.models.print_option import PrintOption
from py_sp_api.generated.shippingV2.models.promise import Promise
from py_sp_api.generated.shippingV2.models.purchase_shipment_request import PurchaseShipmentRequest
from py_sp_api.generated.shippingV2.models.purchase_shipment_response import PurchaseShipmentResponse
from py_sp_api.generated.shippingV2.models.purchase_shipment_result import PurchaseShipmentResult
from py_sp_api.generated.shippingV2.models.rate import Rate
from py_sp_api.generated.shippingV2.models.rate_item import RateItem
from py_sp_api.generated.shippingV2.models.rate_item_id import RateItemID
from py_sp_api.generated.shippingV2.models.rate_item_type import RateItemType
from py_sp_api.generated.shippingV2.models.requested_document_specification import RequestedDocumentSpecification
from py_sp_api.generated.shippingV2.models.requested_value_added_service import RequestedValueAddedService
from py_sp_api.generated.shippingV2.models.service import Service
from py_sp_api.generated.shippingV2.models.service_selection import ServiceSelection
from py_sp_api.generated.shippingV2.models.shipment_type import ShipmentType
from py_sp_api.generated.shippingV2.models.shipper_instruction import ShipperInstruction
from py_sp_api.generated.shippingV2.models.status import Status
from py_sp_api.generated.shippingV2.models.supported_document_detail import SupportedDocumentDetail
from py_sp_api.generated.shippingV2.models.supported_document_specification import SupportedDocumentSpecification
from py_sp_api.generated.shippingV2.models.tax_detail import TaxDetail
from py_sp_api.generated.shippingV2.models.tax_type import TaxType
from py_sp_api.generated.shippingV2.models.time_of_day import TimeOfDay
from py_sp_api.generated.shippingV2.models.time_window import TimeWindow
from py_sp_api.generated.shippingV2.models.tracking_summary import TrackingSummary
from py_sp_api.generated.shippingV2.models.unlink_carrier_account_request import UnlinkCarrierAccountRequest
from py_sp_api.generated.shippingV2.models.unlink_carrier_account_response import UnlinkCarrierAccountResponse
from py_sp_api.generated.shippingV2.models.unmanifested_carrier_information import UnmanifestedCarrierInformation
from py_sp_api.generated.shippingV2.models.unmanifested_shipment_location import UnmanifestedShipmentLocation
from py_sp_api.generated.shippingV2.models.validation_metadata import ValidationMetadata
from py_sp_api.generated.shippingV2.models.value_added_service import ValueAddedService
from py_sp_api.generated.shippingV2.models.value_added_service_details import ValueAddedServiceDetails
from py_sp_api.generated.shippingV2.models.weight import Weight

from .base_client import SPAPIClient
