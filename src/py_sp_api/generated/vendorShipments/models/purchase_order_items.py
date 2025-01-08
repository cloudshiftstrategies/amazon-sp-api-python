# coding: utf-8

"""
    Selling Partner API for Retail Procurement Shipments

    The Selling Partner API for Retail Procurement Shipments provides programmatic access to retail shipping data for vendors.

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
from py_sp_api.generated.vendorShipments.models.item_quantity import ItemQuantity
from py_sp_api.generated.vendorShipments.models.money import Money
from typing import Optional, Set
from typing_extensions import Self

class PurchaseOrderItems(BaseModel):
    """
    Details of the item being shipped.
    """ # noqa: E501
    item_sequence_number: StrictStr = Field(description="Item sequence number for the item. The first item will be 001, the second 002, and so on. This number is used as a reference to refer to this item from the carton or pallet level.", alias="itemSequenceNumber")
    buyer_product_identifier: Optional[StrictStr] = Field(default=None, description="Amazon Standard Identification Number (ASIN) for a SKU", alias="buyerProductIdentifier")
    vendor_product_identifier: Optional[StrictStr] = Field(default=None, description="The vendor selected product identification of the item. Should be the same as was sent in the purchase order.", alias="vendorProductIdentifier")
    shipped_quantity: ItemQuantity = Field(alias="shippedQuantity")
    maximum_retail_price: Optional[Money] = Field(default=None, alias="maximumRetailPrice")
    __properties: ClassVar[List[str]] = ["itemSequenceNumber", "buyerProductIdentifier", "vendorProductIdentifier", "shippedQuantity", "maximumRetailPrice"]

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
        """Create an instance of PurchaseOrderItems from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of shipped_quantity
        if self.shipped_quantity:
            _dict['shippedQuantity'] = self.shipped_quantity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of maximum_retail_price
        if self.maximum_retail_price:
            _dict['maximumRetailPrice'] = self.maximum_retail_price.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PurchaseOrderItems from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "itemSequenceNumber": obj.get("itemSequenceNumber"),
            "buyerProductIdentifier": obj.get("buyerProductIdentifier"),
            "vendorProductIdentifier": obj.get("vendorProductIdentifier"),
            "shippedQuantity": ItemQuantity.from_dict(obj["shippedQuantity"]) if obj.get("shippedQuantity") is not None else None,
            "maximumRetailPrice": Money.from_dict(obj["maximumRetailPrice"]) if obj.get("maximumRetailPrice") is not None else None
        })
        return _obj


