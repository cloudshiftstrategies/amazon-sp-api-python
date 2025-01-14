# coding: utf-8

"""
    Selling Partner API for Retail Procurement Orders

    The Selling Partner API for Retail Procurement Orders provides programmatic access to vendor orders data.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.vendorOrders.models.money import Money
from py_sp_api.generated.vendorOrders.models.order_item_status_acknowledgement_status import OrderItemStatusAcknowledgementStatus
from py_sp_api.generated.vendorOrders.models.order_item_status_ordered_quantity import OrderItemStatusOrderedQuantity
from py_sp_api.generated.vendorOrders.models.order_item_status_receiving_status import OrderItemStatusReceivingStatus
from typing import Optional, Set
from typing_extensions import Self

class OrderItemStatus(BaseModel):
    """
    Represents the current status of an order item, including acknowledgement and receiving details.
    """ # noqa: E501
    item_sequence_number: StrictStr = Field(description="Numbering of the item on the purchase order. The first item will be 1, the second 2, and so on.", alias="itemSequenceNumber")
    buyer_product_identifier: Optional[StrictStr] = Field(default=None, description="Buyer's Standard Identification Number (ASIN) of an item.", alias="buyerProductIdentifier")
    vendor_product_identifier: Optional[StrictStr] = Field(default=None, description="The vendor selected product identification of the item.", alias="vendorProductIdentifier")
    net_cost: Optional[Money] = Field(default=None, alias="netCost")
    list_price: Optional[Money] = Field(default=None, alias="listPrice")
    ordered_quantity: Optional[OrderItemStatusOrderedQuantity] = Field(default=None, alias="orderedQuantity")
    acknowledgement_status: Optional[OrderItemStatusAcknowledgementStatus] = Field(default=None, alias="acknowledgementStatus")
    receiving_status: Optional[OrderItemStatusReceivingStatus] = Field(default=None, alias="receivingStatus")
    __properties: ClassVar[List[str]] = ["itemSequenceNumber", "buyerProductIdentifier", "vendorProductIdentifier", "netCost", "listPrice", "orderedQuantity", "acknowledgementStatus", "receivingStatus"]

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
        """Create an instance of OrderItemStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of net_cost
        if self.net_cost:
            _dict['netCost'] = self.net_cost.to_dict()
        # override the default output from pydantic by calling `to_dict()` of list_price
        if self.list_price:
            _dict['listPrice'] = self.list_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ordered_quantity
        if self.ordered_quantity:
            _dict['orderedQuantity'] = self.ordered_quantity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of acknowledgement_status
        if self.acknowledgement_status:
            _dict['acknowledgementStatus'] = self.acknowledgement_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of receiving_status
        if self.receiving_status:
            _dict['receivingStatus'] = self.receiving_status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderItemStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "itemSequenceNumber": obj.get("itemSequenceNumber"),
            "buyerProductIdentifier": obj.get("buyerProductIdentifier"),
            "vendorProductIdentifier": obj.get("vendorProductIdentifier"),
            "netCost": Money.from_dict(obj["netCost"]) if obj.get("netCost") is not None else None,
            "listPrice": Money.from_dict(obj["listPrice"]) if obj.get("listPrice") is not None else None,
            "orderedQuantity": OrderItemStatusOrderedQuantity.from_dict(obj["orderedQuantity"]) if obj.get("orderedQuantity") is not None else None,
            "acknowledgementStatus": OrderItemStatusAcknowledgementStatus.from_dict(obj["acknowledgementStatus"]) if obj.get("acknowledgementStatus") is not None else None,
            "receivingStatus": OrderItemStatusReceivingStatus.from_dict(obj["receivingStatus"]) if obj.get("receivingStatus") is not None else None
        })
        return _obj


