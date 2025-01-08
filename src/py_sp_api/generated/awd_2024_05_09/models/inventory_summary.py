# coding: utf-8

"""
    The Selling Partner API for Amazon Warehousing and Distribution

    The Selling Partner API for Amazon Warehousing and Distribution (AWD) provides programmatic access to information about AWD shipments and inventory. 

    The version of the OpenAPI document: 2024-05-09
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.awd_2024_05_09.models.expiration_details import ExpirationDetails
from py_sp_api.generated.awd_2024_05_09.models.inventory_details import InventoryDetails
from typing import Optional, Set
from typing_extensions import Self

class InventorySummary(BaseModel):
    """
    Summary of inventory per SKU.
    """ # noqa: E501
    expiration_details: Optional[List[ExpirationDetails]] = Field(default=None, description="The expiration details of the inventory. This object will only appear if the `details` parameter in the request is set to `SHOW`.", alias="expirationDetails")
    inventory_details: Optional[InventoryDetails] = Field(default=None, alias="inventoryDetails")
    sku: StrictStr = Field(description="The seller or merchant SKU.")
    total_inbound_quantity: Optional[StrictInt] = Field(default=None, description="Total quantity that is in-transit from the seller and has not yet been received at an AWD Distribution Center", alias="totalInboundQuantity")
    total_onhand_quantity: Optional[StrictInt] = Field(default=None, description="Total quantity that is present in AWD distribution centers.", alias="totalOnhandQuantity")
    __properties: ClassVar[List[str]] = ["expirationDetails", "inventoryDetails", "sku", "totalInboundQuantity", "totalOnhandQuantity"]

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
        """Create an instance of InventorySummary from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in expiration_details (list)
        _items = []
        if self.expiration_details:
            for _item_expiration_details in self.expiration_details:
                if _item_expiration_details:
                    _items.append(_item_expiration_details.to_dict())
            _dict['expirationDetails'] = _items
        # override the default output from pydantic by calling `to_dict()` of inventory_details
        if self.inventory_details:
            _dict['inventoryDetails'] = self.inventory_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InventorySummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "expirationDetails": [ExpirationDetails.from_dict(_item) for _item in obj["expirationDetails"]] if obj.get("expirationDetails") is not None else None,
            "inventoryDetails": InventoryDetails.from_dict(obj["inventoryDetails"]) if obj.get("inventoryDetails") is not None else None,
            "sku": obj.get("sku"),
            "totalInboundQuantity": obj.get("totalInboundQuantity"),
            "totalOnhandQuantity": obj.get("totalOnhandQuantity")
        })
        return _obj


