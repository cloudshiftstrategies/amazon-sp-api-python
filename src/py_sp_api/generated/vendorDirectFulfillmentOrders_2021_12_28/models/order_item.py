# coding: utf-8

"""
    Selling Partner API for Direct Fulfillment Orders

    The Selling Partner API for Direct Fulfillment Orders provides programmatic access to a direct fulfillment vendor's order data.

    The version of the OpenAPI document: 2021-12-28
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.vendorDirectFulfillmentOrders_2021_12_28.models.buyer_customized_info_detail import BuyerCustomizedInfoDetail
from py_sp_api.generated.vendorDirectFulfillmentOrders_2021_12_28.models.gift_details import GiftDetails
from py_sp_api.generated.vendorDirectFulfillmentOrders_2021_12_28.models.item_quantity import ItemQuantity
from py_sp_api.generated.vendorDirectFulfillmentOrders_2021_12_28.models.money import Money
from py_sp_api.generated.vendorDirectFulfillmentOrders_2021_12_28.models.scheduled_delivery_shipment import ScheduledDeliveryShipment
from py_sp_api.generated.vendorDirectFulfillmentOrders_2021_12_28.models.tax_item_details import TaxItemDetails
from typing import Optional, Set
from typing_extensions import Self

class OrderItem(BaseModel):
    """
    An item within an order
    """ # noqa: E501
    item_sequence_number: StrictStr = Field(description="Numbering of the item on the purchase order. The first item will be 1, the second 2, and so on.", alias="itemSequenceNumber")
    buyer_product_identifier: Optional[StrictStr] = Field(default=None, description="Buyer's standard identification number (ASIN) of an item.", alias="buyerProductIdentifier")
    vendor_product_identifier: Optional[StrictStr] = Field(default=None, description="The vendor selected product identification of the item.", alias="vendorProductIdentifier")
    title: Optional[StrictStr] = Field(default=None, description="Title for the item.")
    ordered_quantity: ItemQuantity = Field(alias="orderedQuantity")
    scheduled_delivery_shipment: Optional[ScheduledDeliveryShipment] = Field(default=None, alias="scheduledDeliveryShipment")
    gift_details: Optional[GiftDetails] = Field(default=None, alias="giftDetails")
    net_price: Money = Field(alias="netPrice")
    tax_details: Optional[TaxItemDetails] = Field(default=None, alias="taxDetails")
    total_price: Optional[Money] = Field(default=None, alias="totalPrice")
    buyer_customized_info: Optional[BuyerCustomizedInfoDetail] = Field(default=None, alias="buyerCustomizedInfo")
    __properties: ClassVar[List[str]] = ["itemSequenceNumber", "buyerProductIdentifier", "vendorProductIdentifier", "title", "orderedQuantity", "scheduledDeliveryShipment", "giftDetails", "netPrice", "taxDetails", "totalPrice", "buyerCustomizedInfo"]

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
        """Create an instance of OrderItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ordered_quantity
        if self.ordered_quantity:
            _dict['orderedQuantity'] = self.ordered_quantity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of scheduled_delivery_shipment
        if self.scheduled_delivery_shipment:
            _dict['scheduledDeliveryShipment'] = self.scheduled_delivery_shipment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gift_details
        if self.gift_details:
            _dict['giftDetails'] = self.gift_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of net_price
        if self.net_price:
            _dict['netPrice'] = self.net_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tax_details
        if self.tax_details:
            _dict['taxDetails'] = self.tax_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total_price
        if self.total_price:
            _dict['totalPrice'] = self.total_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of buyer_customized_info
        if self.buyer_customized_info:
            _dict['buyerCustomizedInfo'] = self.buyer_customized_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "itemSequenceNumber": obj.get("itemSequenceNumber"),
            "buyerProductIdentifier": obj.get("buyerProductIdentifier"),
            "vendorProductIdentifier": obj.get("vendorProductIdentifier"),
            "title": obj.get("title"),
            "orderedQuantity": ItemQuantity.from_dict(obj["orderedQuantity"]) if obj.get("orderedQuantity") is not None else None,
            "scheduledDeliveryShipment": ScheduledDeliveryShipment.from_dict(obj["scheduledDeliveryShipment"]) if obj.get("scheduledDeliveryShipment") is not None else None,
            "giftDetails": GiftDetails.from_dict(obj["giftDetails"]) if obj.get("giftDetails") is not None else None,
            "netPrice": Money.from_dict(obj["netPrice"]) if obj.get("netPrice") is not None else None,
            "taxDetails": TaxItemDetails.from_dict(obj["taxDetails"]) if obj.get("taxDetails") is not None else None,
            "totalPrice": Money.from_dict(obj["totalPrice"]) if obj.get("totalPrice") is not None else None,
            "buyerCustomizedInfo": BuyerCustomizedInfoDetail.from_dict(obj["buyerCustomizedInfo"]) if obj.get("buyerCustomizedInfo") is not None else None
        })
        return _obj


