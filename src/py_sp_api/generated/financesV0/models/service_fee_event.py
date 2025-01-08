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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.financesV0.models.fee_component import FeeComponent
from typing import Optional, Set
from typing_extensions import Self

class ServiceFeeEvent(BaseModel):
    """
    A service fee on the seller's account.
    """ # noqa: E501
    amazon_order_id: Optional[StrictStr] = Field(default=None, description="An Amazon-defined identifier for an order.", alias="AmazonOrderId")
    fee_reason: Optional[StrictStr] = Field(default=None, description="A short description of the service fee reason.", alias="FeeReason")
    fee_list: Optional[List[FeeComponent]] = Field(default=None, description="A list of fee component information.", alias="FeeList")
    seller_sku: Optional[StrictStr] = Field(default=None, description="The seller SKU of the item. The seller SKU is qualified by the seller's seller ID, which is included with every call to the Selling Partner API.", alias="SellerSKU")
    fn_sku: Optional[StrictStr] = Field(default=None, description="A unique identifier assigned by Amazon to products stored in and fulfilled from an Amazon fulfillment center.", alias="FnSKU")
    fee_description: Optional[StrictStr] = Field(default=None, description="A short description of the service fee event.", alias="FeeDescription")
    asin: Optional[StrictStr] = Field(default=None, description="The Amazon Standard Identification Number (ASIN) of the item.", alias="ASIN")
    store_name: Optional[StrictStr] = Field(default=None, description="The name of the store where the event occurred.", alias="StoreName")
    __properties: ClassVar[List[str]] = ["AmazonOrderId", "FeeReason", "FeeList", "SellerSKU", "FnSKU", "FeeDescription", "ASIN", "StoreName"]

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
        """Create an instance of ServiceFeeEvent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in fee_list (list)
        _items = []
        if self.fee_list:
            for _item_fee_list in self.fee_list:
                if _item_fee_list:
                    _items.append(_item_fee_list.to_dict())
            _dict['FeeList'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServiceFeeEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "AmazonOrderId": obj.get("AmazonOrderId"),
            "FeeReason": obj.get("FeeReason"),
            "FeeList": [FeeComponent.from_dict(_item) for _item in obj["FeeList"]] if obj.get("FeeList") is not None else None,
            "SellerSKU": obj.get("SellerSKU"),
            "FnSKU": obj.get("FnSKU"),
            "FeeDescription": obj.get("FeeDescription"),
            "ASIN": obj.get("ASIN"),
            "StoreName": obj.get("StoreName")
        })
        return _obj


