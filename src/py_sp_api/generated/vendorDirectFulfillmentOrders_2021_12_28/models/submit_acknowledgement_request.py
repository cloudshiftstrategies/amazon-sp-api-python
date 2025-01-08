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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.vendorDirectFulfillmentOrders_2021_12_28.models.order_acknowledgement_item import OrderAcknowledgementItem
from typing import Optional, Set
from typing_extensions import Self

class SubmitAcknowledgementRequest(BaseModel):
    """
    The request schema for the submitAcknowledgement operation.
    """ # noqa: E501
    order_acknowledgements: Optional[List[OrderAcknowledgementItem]] = Field(default=None, description="A list of one or more purchase orders.", alias="orderAcknowledgements")
    __properties: ClassVar[List[str]] = ["orderAcknowledgements"]

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
        """Create an instance of SubmitAcknowledgementRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in order_acknowledgements (list)
        _items = []
        if self.order_acknowledgements:
            for _item_order_acknowledgements in self.order_acknowledgements:
                if _item_order_acknowledgements:
                    _items.append(_item_order_acknowledgements.to_dict())
            _dict['orderAcknowledgements'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubmitAcknowledgementRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "orderAcknowledgements": [OrderAcknowledgementItem.from_dict(_item) for _item in obj["orderAcknowledgements"]] if obj.get("orderAcknowledgements") is not None else None
        })
        return _obj


