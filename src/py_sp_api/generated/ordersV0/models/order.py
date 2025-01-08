# coding: utf-8

"""
    Orders v0

    Use the Orders Selling Partner API to programmatically retrieve order information. With this API, you can develop fast, flexible, and custom applications to manage order synchronization, perform order research, and create demand-based decision support tools.   _Note:_ For the JP, AU, and SG marketplaces, the Orders API supports orders from 2016 onward. For all other marketplaces, the Orders API supports orders for the last two years (orders older than this don't show up in the response).

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.ordersV0.models.address import Address
from py_sp_api.generated.ordersV0.models.automated_shipping_settings import AutomatedShippingSettings
from py_sp_api.generated.ordersV0.models.buyer_info import BuyerInfo
from py_sp_api.generated.ordersV0.models.buyer_tax_information import BuyerTaxInformation
from py_sp_api.generated.ordersV0.models.easy_ship_shipment_status import EasyShipShipmentStatus
from py_sp_api.generated.ordersV0.models.electronic_invoice_status import ElectronicInvoiceStatus
from py_sp_api.generated.ordersV0.models.fulfillment_instruction import FulfillmentInstruction
from py_sp_api.generated.ordersV0.models.marketplace_tax_info import MarketplaceTaxInfo
from py_sp_api.generated.ordersV0.models.money import Money
from py_sp_api.generated.ordersV0.models.payment_execution_detail_item import PaymentExecutionDetailItem
from typing import Optional, Set
from typing_extensions import Self

class Order(BaseModel):
    """
    Order information.
    """ # noqa: E501
    amazon_order_id: StrictStr = Field(description="An Amazon-defined order identifier, in 3-7-7 format.", alias="AmazonOrderId")
    seller_order_id: Optional[StrictStr] = Field(default=None, description="A seller-defined order identifier.", alias="SellerOrderId")
    purchase_date: StrictStr = Field(description="The date when the order was created.", alias="PurchaseDate")
    last_update_date: StrictStr = Field(description="The date when the order was last updated.  __Note__: `LastUpdateDate` is returned with an incorrect date for orders that were last updated before 2009-04-01.", alias="LastUpdateDate")
    order_status: StrictStr = Field(description="The current order status.", alias="OrderStatus")
    fulfillment_channel: Optional[StrictStr] = Field(default=None, description="Whether the order was fulfilled by Amazon (`AFN`) or by the seller (`MFN`).", alias="FulfillmentChannel")
    sales_channel: Optional[StrictStr] = Field(default=None, description="The sales channel for the first item in the order.", alias="SalesChannel")
    order_channel: Optional[StrictStr] = Field(default=None, description="The order channel for the first item in the order.", alias="OrderChannel")
    ship_service_level: Optional[StrictStr] = Field(default=None, description="The order's shipment service level.", alias="ShipServiceLevel")
    order_total: Optional[Money] = Field(default=None, alias="OrderTotal")
    number_of_items_shipped: Optional[StrictInt] = Field(default=None, description="The number of items shipped.", alias="NumberOfItemsShipped")
    number_of_items_unshipped: Optional[StrictInt] = Field(default=None, description="The number of items unshipped.", alias="NumberOfItemsUnshipped")
    payment_execution_detail: Optional[List[PaymentExecutionDetailItem]] = Field(default=None, description="A list of payment execution detail items.", alias="PaymentExecutionDetail")
    payment_method: Optional[StrictStr] = Field(default=None, description="The payment method for the order. This property is limited to COD and CVS payment methods. Unless you need the specific COD payment information provided by the `PaymentExecutionDetailItem` object, we recommend using the `PaymentMethodDetails` property to get payment method information.", alias="PaymentMethod")
    payment_method_details: Optional[List[StrictStr]] = Field(default=None, description="A list of payment method detail items.", alias="PaymentMethodDetails")
    marketplace_id: Optional[StrictStr] = Field(default=None, description="The identifier for the marketplace where the order was placed.", alias="MarketplaceId")
    shipment_service_level_category: Optional[StrictStr] = Field(default=None, description="The shipment service level category for the order.  **Possible values**: `Expedited`, `FreeEconomy`, `NextDay`, `Priority`, `SameDay`, `SecondDay`, `Scheduled`, and `Standard`.", alias="ShipmentServiceLevelCategory")
    easy_ship_shipment_status: Optional[EasyShipShipmentStatus] = Field(default=None, alias="EasyShipShipmentStatus")
    cba_displayable_shipping_label: Optional[StrictStr] = Field(default=None, description="Custom ship label for Checkout by Amazon (CBA).", alias="CbaDisplayableShippingLabel")
    order_type: Optional[StrictStr] = Field(default=None, description="The order's type.", alias="OrderType")
    earliest_ship_date: Optional[StrictStr] = Field(default=None, description="The start of the time period within which you have committed to ship the order. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date time format. Only returned for seller-fulfilled orders.  __Note__: `EarliestShipDate` might not be returned for orders placed before February 1, 2013.", alias="EarliestShipDate")
    latest_ship_date: Optional[StrictStr] = Field(default=None, description="The end of the time period within which you have committed to ship the order. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date time format. Only returned for seller-fulfilled orders.  __Note__: `LatestShipDate` might not be returned for orders placed before February 1, 2013.", alias="LatestShipDate")
    earliest_delivery_date: Optional[StrictStr] = Field(default=None, description="The start of the time period within which you have committed to fulfill the order. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date time format. Only returned for seller-fulfilled orders.", alias="EarliestDeliveryDate")
    latest_delivery_date: Optional[StrictStr] = Field(default=None, description="The end of the time period within which you have committed to fulfill the order. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date time format. Only returned for seller-fulfilled orders that do not have a `PendingAvailability`, `Pending`, or `Canceled` status.", alias="LatestDeliveryDate")
    is_business_order: Optional[StrictBool] = Field(default=None, description="When true, the order is an Amazon Business order. An Amazon Business order is an order where the buyer is a Verified Business Buyer.", alias="IsBusinessOrder")
    is_prime: Optional[StrictBool] = Field(default=None, description="When true, the order is a seller-fulfilled Amazon Prime order.", alias="IsPrime")
    is_premium_order: Optional[StrictBool] = Field(default=None, description="When true, the order has a Premium Shipping Service Level Agreement. For more information about Premium Shipping orders, refer to \"Premium Shipping Options\" in the Seller Central Help for your marketplace.", alias="IsPremiumOrder")
    is_global_express_enabled: Optional[StrictBool] = Field(default=None, description="When true, the order is a `GlobalExpress` order.", alias="IsGlobalExpressEnabled")
    replaced_order_id: Optional[StrictStr] = Field(default=None, description="The order ID value for the order that is being replaced. Returned only if IsReplacementOrder = true.", alias="ReplacedOrderId")
    is_replacement_order: Optional[StrictBool] = Field(default=None, description="When true, this is a replacement order.", alias="IsReplacementOrder")
    promise_response_due_date: Optional[StrictStr] = Field(default=None, description="Indicates the date by which the seller must respond to the buyer with an estimated ship date. Only returned for Sourcing on Demand orders.", alias="PromiseResponseDueDate")
    is_estimated_ship_date_set: Optional[StrictBool] = Field(default=None, description="When true, the estimated ship date is set for the order. Only returned for Sourcing on Demand orders.", alias="IsEstimatedShipDateSet")
    is_sold_by_ab: Optional[StrictBool] = Field(default=None, description="When true, the item within this order was bought and re-sold by Amazon Business EU SARL (ABEU). By buying and instantly re-selling your items, ABEU becomes the seller of record, making your inventory available for sale to customers who would not otherwise purchase from a third-party seller.", alias="IsSoldByAB")
    is_iba: Optional[StrictBool] = Field(default=None, description="When true, the item within this order was bought and re-sold by Amazon Business EU SARL (ABEU). By buying and instantly re-selling your items, ABEU becomes the seller of record, making your inventory available for sale to customers who would not otherwise purchase from a third-party seller.", alias="IsIBA")
    default_ship_from_location_address: Optional[Address] = Field(default=None, alias="DefaultShipFromLocationAddress")
    buyer_invoice_preference: Optional[StrictStr] = Field(default=None, description="The buyer's invoicing preference. Sellers can use this data to issue electronic invoices for orders in Turkey.  **Note**: This attribute is only available in the Turkey marketplace.", alias="BuyerInvoicePreference")
    buyer_tax_information: Optional[BuyerTaxInformation] = Field(default=None, alias="BuyerTaxInformation")
    fulfillment_instruction: Optional[FulfillmentInstruction] = Field(default=None, alias="FulfillmentInstruction")
    is_ispu: Optional[StrictBool] = Field(default=None, description="When true, this order is marked to be picked up from a store rather than delivered.", alias="IsISPU")
    is_access_point_order: Optional[StrictBool] = Field(default=None, description="When true, this order is marked to be delivered to an Access Point. The access location is chosen by the customer. Access Points include Amazon Hub Lockers, Amazon Hub Counters, and pickup points operated by carriers.", alias="IsAccessPointOrder")
    marketplace_tax_info: Optional[MarketplaceTaxInfo] = Field(default=None, alias="MarketplaceTaxInfo")
    seller_display_name: Optional[StrictStr] = Field(default=None, description="The seller’s friendly name registered in the marketplace where the sale took place. Sellers can use this data to issue electronic invoices for orders in Brazil.  **Note**: This attribute is only available in the Brazil marketplace for the orders with `Pending` or `Unshipped` status.", alias="SellerDisplayName")
    shipping_address: Optional[Address] = Field(default=None, alias="ShippingAddress")
    buyer_info: Optional[BuyerInfo] = Field(default=None, alias="BuyerInfo")
    automated_shipping_settings: Optional[AutomatedShippingSettings] = Field(default=None, alias="AutomatedShippingSettings")
    has_regulated_items: Optional[StrictBool] = Field(default=None, description="Whether the order contains regulated items which may require additional approval steps before being fulfilled.", alias="HasRegulatedItems")
    electronic_invoice_status: Optional[ElectronicInvoiceStatus] = Field(default=None, alias="ElectronicInvoiceStatus")
    __properties: ClassVar[List[str]] = ["AmazonOrderId", "SellerOrderId", "PurchaseDate", "LastUpdateDate", "OrderStatus", "FulfillmentChannel", "SalesChannel", "OrderChannel", "ShipServiceLevel", "OrderTotal", "NumberOfItemsShipped", "NumberOfItemsUnshipped", "PaymentExecutionDetail", "PaymentMethod", "PaymentMethodDetails", "MarketplaceId", "ShipmentServiceLevelCategory", "EasyShipShipmentStatus", "CbaDisplayableShippingLabel", "OrderType", "EarliestShipDate", "LatestShipDate", "EarliestDeliveryDate", "LatestDeliveryDate", "IsBusinessOrder", "IsPrime", "IsPremiumOrder", "IsGlobalExpressEnabled", "ReplacedOrderId", "IsReplacementOrder", "PromiseResponseDueDate", "IsEstimatedShipDateSet", "IsSoldByAB", "IsIBA", "DefaultShipFromLocationAddress", "BuyerInvoicePreference", "BuyerTaxInformation", "FulfillmentInstruction", "IsISPU", "IsAccessPointOrder", "MarketplaceTaxInfo", "SellerDisplayName", "ShippingAddress", "BuyerInfo", "AutomatedShippingSettings", "HasRegulatedItems", "ElectronicInvoiceStatus"]

    @field_validator('order_status')
    def order_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Pending', 'Unshipped', 'PartiallyShipped', 'Shipped', 'Canceled', 'Unfulfillable', 'InvoiceUnconfirmed', 'PendingAvailability']):
            raise ValueError("must be one of enum values ('Pending', 'Unshipped', 'PartiallyShipped', 'Shipped', 'Canceled', 'Unfulfillable', 'InvoiceUnconfirmed', 'PendingAvailability')")
        return value

    @field_validator('fulfillment_channel')
    def fulfillment_channel_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['MFN', 'AFN']):
            raise ValueError("must be one of enum values ('MFN', 'AFN')")
        return value

    @field_validator('payment_method')
    def payment_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['COD', 'CVS', 'Other']):
            raise ValueError("must be one of enum values ('COD', 'CVS', 'Other')")
        return value

    @field_validator('order_type')
    def order_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['StandardOrder', 'LongLeadTimeOrder', 'Preorder', 'BackOrder', 'SourcingOnDemandOrder']):
            raise ValueError("must be one of enum values ('StandardOrder', 'LongLeadTimeOrder', 'Preorder', 'BackOrder', 'SourcingOnDemandOrder')")
        return value

    @field_validator('buyer_invoice_preference')
    def buyer_invoice_preference_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['INDIVIDUAL', 'BUSINESS']):
            raise ValueError("must be one of enum values ('INDIVIDUAL', 'BUSINESS')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Order from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of order_total
        if self.order_total:
            _dict['OrderTotal'] = self.order_total.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in payment_execution_detail (list)
        _items = []
        if self.payment_execution_detail:
            for _item_payment_execution_detail in self.payment_execution_detail:
                if _item_payment_execution_detail:
                    _items.append(_item_payment_execution_detail.to_dict())
            _dict['PaymentExecutionDetail'] = _items
        # override the default output from pydantic by calling `to_dict()` of default_ship_from_location_address
        if self.default_ship_from_location_address:
            _dict['DefaultShipFromLocationAddress'] = self.default_ship_from_location_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of buyer_tax_information
        if self.buyer_tax_information:
            _dict['BuyerTaxInformation'] = self.buyer_tax_information.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fulfillment_instruction
        if self.fulfillment_instruction:
            _dict['FulfillmentInstruction'] = self.fulfillment_instruction.to_dict()
        # override the default output from pydantic by calling `to_dict()` of marketplace_tax_info
        if self.marketplace_tax_info:
            _dict['MarketplaceTaxInfo'] = self.marketplace_tax_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipping_address
        if self.shipping_address:
            _dict['ShippingAddress'] = self.shipping_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of buyer_info
        if self.buyer_info:
            _dict['BuyerInfo'] = self.buyer_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of automated_shipping_settings
        if self.automated_shipping_settings:
            _dict['AutomatedShippingSettings'] = self.automated_shipping_settings.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Order from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "AmazonOrderId": obj.get("AmazonOrderId"),
            "SellerOrderId": obj.get("SellerOrderId"),
            "PurchaseDate": obj.get("PurchaseDate"),
            "LastUpdateDate": obj.get("LastUpdateDate"),
            "OrderStatus": obj.get("OrderStatus"),
            "FulfillmentChannel": obj.get("FulfillmentChannel"),
            "SalesChannel": obj.get("SalesChannel"),
            "OrderChannel": obj.get("OrderChannel"),
            "ShipServiceLevel": obj.get("ShipServiceLevel"),
            "OrderTotal": Money.from_dict(obj["OrderTotal"]) if obj.get("OrderTotal") is not None else None,
            "NumberOfItemsShipped": obj.get("NumberOfItemsShipped"),
            "NumberOfItemsUnshipped": obj.get("NumberOfItemsUnshipped"),
            "PaymentExecutionDetail": [PaymentExecutionDetailItem.from_dict(_item) for _item in obj["PaymentExecutionDetail"]] if obj.get("PaymentExecutionDetail") is not None else None,
            "PaymentMethod": obj.get("PaymentMethod"),
            "PaymentMethodDetails": obj.get("PaymentMethodDetails"),
            "MarketplaceId": obj.get("MarketplaceId"),
            "ShipmentServiceLevelCategory": obj.get("ShipmentServiceLevelCategory"),
            "EasyShipShipmentStatus": obj.get("EasyShipShipmentStatus"),
            "CbaDisplayableShippingLabel": obj.get("CbaDisplayableShippingLabel"),
            "OrderType": obj.get("OrderType"),
            "EarliestShipDate": obj.get("EarliestShipDate"),
            "LatestShipDate": obj.get("LatestShipDate"),
            "EarliestDeliveryDate": obj.get("EarliestDeliveryDate"),
            "LatestDeliveryDate": obj.get("LatestDeliveryDate"),
            "IsBusinessOrder": obj.get("IsBusinessOrder"),
            "IsPrime": obj.get("IsPrime"),
            "IsPremiumOrder": obj.get("IsPremiumOrder"),
            "IsGlobalExpressEnabled": obj.get("IsGlobalExpressEnabled"),
            "ReplacedOrderId": obj.get("ReplacedOrderId"),
            "IsReplacementOrder": obj.get("IsReplacementOrder"),
            "PromiseResponseDueDate": obj.get("PromiseResponseDueDate"),
            "IsEstimatedShipDateSet": obj.get("IsEstimatedShipDateSet"),
            "IsSoldByAB": obj.get("IsSoldByAB"),
            "IsIBA": obj.get("IsIBA"),
            "DefaultShipFromLocationAddress": Address.from_dict(obj["DefaultShipFromLocationAddress"]) if obj.get("DefaultShipFromLocationAddress") is not None else None,
            "BuyerInvoicePreference": obj.get("BuyerInvoicePreference"),
            "BuyerTaxInformation": BuyerTaxInformation.from_dict(obj["BuyerTaxInformation"]) if obj.get("BuyerTaxInformation") is not None else None,
            "FulfillmentInstruction": FulfillmentInstruction.from_dict(obj["FulfillmentInstruction"]) if obj.get("FulfillmentInstruction") is not None else None,
            "IsISPU": obj.get("IsISPU"),
            "IsAccessPointOrder": obj.get("IsAccessPointOrder"),
            "MarketplaceTaxInfo": MarketplaceTaxInfo.from_dict(obj["MarketplaceTaxInfo"]) if obj.get("MarketplaceTaxInfo") is not None else None,
            "SellerDisplayName": obj.get("SellerDisplayName"),
            "ShippingAddress": Address.from_dict(obj["ShippingAddress"]) if obj.get("ShippingAddress") is not None else None,
            "BuyerInfo": BuyerInfo.from_dict(obj["BuyerInfo"]) if obj.get("BuyerInfo") is not None else None,
            "AutomatedShippingSettings": AutomatedShippingSettings.from_dict(obj["AutomatedShippingSettings"]) if obj.get("AutomatedShippingSettings") is not None else None,
            "HasRegulatedItems": obj.get("HasRegulatedItems"),
            "ElectronicInvoiceStatus": obj.get("ElectronicInvoiceStatus")
        })
        return _obj


