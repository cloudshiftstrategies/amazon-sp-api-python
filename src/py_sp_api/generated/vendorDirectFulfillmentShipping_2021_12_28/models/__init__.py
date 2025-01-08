# coding: utf-8

# flake8: noqa
"""
    Selling Partner API for Direct Fulfillment Shipping

    Use the Selling Partner API for Direct Fulfillment Shipping to access a direct fulfillment vendor's shipping data.

    The version of the OpenAPI document: 2021-12-28
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.address import Address
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.carrier_id import CarrierId
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.container import Container
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.container_label import ContainerLabel
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.container_label_format import ContainerLabelFormat
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.create_container_label_request import CreateContainerLabelRequest
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.create_container_label_response import CreateContainerLabelResponse
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.create_shipping_labels_request import CreateShippingLabelsRequest
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.customer_invoice import CustomerInvoice
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.customer_invoice_list import CustomerInvoiceList
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.dimensions import Dimensions
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.error import Error
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.error_list import ErrorList
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.item import Item
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.item_quantity import ItemQuantity
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.label_data import LabelData
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.package import Package
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.packed_item import PackedItem
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.packing_slip import PackingSlip
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.packing_slip_list import PackingSlipList
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.pagination import Pagination
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.party_identification import PartyIdentification
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.shipment_confirmation import ShipmentConfirmation
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.shipment_details import ShipmentDetails
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.shipment_schedule import ShipmentSchedule
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.shipment_status_update import ShipmentStatusUpdate
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.shipping_label import ShippingLabel
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.shipping_label_list import ShippingLabelList
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.shipping_label_request import ShippingLabelRequest
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.status_update_details import StatusUpdateDetails
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.submit_shipment_confirmations_request import SubmitShipmentConfirmationsRequest
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.submit_shipment_status_updates_request import SubmitShipmentStatusUpdatesRequest
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.submit_shipping_labels_request import SubmitShippingLabelsRequest
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.tax_registration_details import TaxRegistrationDetails
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.transaction_reference import TransactionReference
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.weight import Weight
