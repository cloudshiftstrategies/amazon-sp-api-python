# coding: utf-8

"""
    Selling Partner API for Merchant Fulfillment

    With the Selling Partner API for Merchant Fulfillment, you can build applications that sellers can use to purchase shipping for non-Prime and Prime orders using Amazon's Buy Shipping Services.

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.merchantFulfillmentV0.models.additional_seller_inputs import AdditionalSellerInputs
from py_sp_api.generated.merchantFulfillmentV0.models.dangerous_goods_details import DangerousGoodsDetails
from py_sp_api.generated.merchantFulfillmentV0.models.liquid_volume import LiquidVolume
from py_sp_api.generated.merchantFulfillmentV0.models.weight import Weight
from typing import Optional, Set
from typing_extensions import Self

class Item(BaseModel):
    """
    An Amazon order item identifier and a quantity.
    """ # noqa: E501
    order_item_id: StrictStr = Field(description="An Amazon-defined identifier for an individual item in an order.", alias="OrderItemId")
    quantity: StrictInt = Field(description="The number of items.", alias="Quantity")
    item_weight: Optional[Weight] = Field(default=None, alias="ItemWeight")
    item_description: Optional[StrictStr] = Field(default=None, description="The description of the item.", alias="ItemDescription")
    transparency_code_list: Optional[List[StrictStr]] = Field(default=None, description="A list of transparency codes.", alias="TransparencyCodeList")
    item_level_seller_inputs_list: Optional[List[AdditionalSellerInputs]] = Field(default=None, description="A list of additional seller input pairs required to purchase shipping.", alias="ItemLevelSellerInputsList")
    liquid_volume: Optional[LiquidVolume] = Field(default=None, alias="LiquidVolume")
    is_hazmat: Optional[StrictBool] = Field(default=None, description="When true, the item qualifies as hazardous materials (hazmat). Defaults to false.", alias="IsHazmat")
    dangerous_goods_details: Optional[DangerousGoodsDetails] = Field(default=None, alias="DangerousGoodsDetails")
    __properties: ClassVar[List[str]] = ["OrderItemId", "Quantity", "ItemWeight", "ItemDescription", "TransparencyCodeList", "ItemLevelSellerInputsList", "LiquidVolume", "IsHazmat", "DangerousGoodsDetails"]

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
        """Create an instance of Item from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of item_weight
        if self.item_weight:
            _dict['ItemWeight'] = self.item_weight.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in item_level_seller_inputs_list (list)
        _items = []
        if self.item_level_seller_inputs_list:
            for _item_item_level_seller_inputs_list in self.item_level_seller_inputs_list:
                if _item_item_level_seller_inputs_list:
                    _items.append(_item_item_level_seller_inputs_list.to_dict())
            _dict['ItemLevelSellerInputsList'] = _items
        # override the default output from pydantic by calling `to_dict()` of liquid_volume
        if self.liquid_volume:
            _dict['LiquidVolume'] = self.liquid_volume.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dangerous_goods_details
        if self.dangerous_goods_details:
            _dict['DangerousGoodsDetails'] = self.dangerous_goods_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Item from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "OrderItemId": obj.get("OrderItemId"),
            "Quantity": obj.get("Quantity"),
            "ItemWeight": Weight.from_dict(obj["ItemWeight"]) if obj.get("ItemWeight") is not None else None,
            "ItemDescription": obj.get("ItemDescription"),
            "TransparencyCodeList": obj.get("TransparencyCodeList"),
            "ItemLevelSellerInputsList": [AdditionalSellerInputs.from_dict(_item) for _item in obj["ItemLevelSellerInputsList"]] if obj.get("ItemLevelSellerInputsList") is not None else None,
            "LiquidVolume": LiquidVolume.from_dict(obj["LiquidVolume"]) if obj.get("LiquidVolume") is not None else None,
            "IsHazmat": obj.get("IsHazmat"),
            "DangerousGoodsDetails": DangerousGoodsDetails.from_dict(obj["DangerousGoodsDetails"]) if obj.get("DangerousGoodsDetails") is not None else None
        })
        return _obj


