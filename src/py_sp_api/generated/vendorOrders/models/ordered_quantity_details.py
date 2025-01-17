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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.vendorOrders.models.item_quantity import ItemQuantity
from typing import Optional, Set
from typing_extensions import Self

class OrderedQuantityDetails(BaseModel):
    """
    Details of item quantity ordered.
    """ # noqa: E501
    updated_date: Optional[datetime] = Field(default=None, description="The date when the line item quantity was updated by buyer. Must be in ISO-8601 date/time format.", alias="updatedDate")
    ordered_quantity: Optional[ItemQuantity] = Field(default=None, alias="orderedQuantity")
    cancelled_quantity: Optional[ItemQuantity] = Field(default=None, alias="cancelledQuantity")
    __properties: ClassVar[List[str]] = ["updatedDate", "orderedQuantity", "cancelledQuantity"]

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
        """Create an instance of OrderedQuantityDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cancelled_quantity
        if self.cancelled_quantity:
            _dict['cancelledQuantity'] = self.cancelled_quantity.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderedQuantityDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "updatedDate": obj.get("updatedDate"),
            "orderedQuantity": ItemQuantity.from_dict(obj["orderedQuantity"]) if obj.get("orderedQuantity") is not None else None,
            "cancelledQuantity": ItemQuantity.from_dict(obj["cancelledQuantity"]) if obj.get("cancelledQuantity") is not None else None
        })
        return _obj


