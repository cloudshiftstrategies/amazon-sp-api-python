# coding: utf-8

"""
    Selling Partner API for Finances

    The Selling Partner API for Finances helps you obtain financial information relevant to a seller's business. You can obtain financial events for a given order, financial event group, or date range without having to wait until a statement period closes. You can also obtain financial event groups for a given date range.

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.financesV0.models.currency import Currency
from py_sp_api.generated.financesV0.models.tax_withheld_component import TaxWithheldComponent
from typing import Optional, Set
from typing_extensions import Self

class RetrochargeEvent(BaseModel):
    """
    A retrocharge or retrocharge reversal.
    """ # noqa: E501
    retrocharge_event_type: Optional[StrictStr] = Field(default=None, description="The type of event.  Possible values:  * Retrocharge  * RetrochargeReversal", alias="RetrochargeEventType")
    amazon_order_id: Optional[StrictStr] = Field(default=None, description="An Amazon-defined identifier for an order.", alias="AmazonOrderId")
    posted_date: Optional[datetime] = Field(default=None, description="Fields with a schema type of date are in ISO 8601 date time format (for example GroupBeginDate).", alias="PostedDate")
    base_tax: Optional[Currency] = Field(default=None, alias="BaseTax")
    shipping_tax: Optional[Currency] = Field(default=None, alias="ShippingTax")
    marketplace_name: Optional[StrictStr] = Field(default=None, description="The name of the marketplace where the retrocharge event occurred.", alias="MarketplaceName")
    retrocharge_tax_withheld_list: Optional[List[TaxWithheldComponent]] = Field(default=None, description="A list of information about taxes withheld.", alias="RetrochargeTaxWithheldList")
    __properties: ClassVar[List[str]] = ["RetrochargeEventType", "AmazonOrderId", "PostedDate", "BaseTax", "ShippingTax", "MarketplaceName", "RetrochargeTaxWithheldList"]

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
        """Create an instance of RetrochargeEvent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of base_tax
        if self.base_tax:
            _dict['BaseTax'] = self.base_tax.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipping_tax
        if self.shipping_tax:
            _dict['ShippingTax'] = self.shipping_tax.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in retrocharge_tax_withheld_list (list)
        _items = []
        if self.retrocharge_tax_withheld_list:
            for _item_retrocharge_tax_withheld_list in self.retrocharge_tax_withheld_list:
                if _item_retrocharge_tax_withheld_list:
                    _items.append(_item_retrocharge_tax_withheld_list.to_dict())
            _dict['RetrochargeTaxWithheldList'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RetrochargeEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "RetrochargeEventType": obj.get("RetrochargeEventType"),
            "AmazonOrderId": obj.get("AmazonOrderId"),
            "PostedDate": obj.get("PostedDate"),
            "BaseTax": Currency.from_dict(obj["BaseTax"]) if obj.get("BaseTax") is not None else None,
            "ShippingTax": Currency.from_dict(obj["ShippingTax"]) if obj.get("ShippingTax") is not None else None,
            "MarketplaceName": obj.get("MarketplaceName"),
            "RetrochargeTaxWithheldList": [TaxWithheldComponent.from_dict(_item) for _item in obj["RetrochargeTaxWithheldList"]] if obj.get("RetrochargeTaxWithheldList") is not None else None
        })
        return _obj


