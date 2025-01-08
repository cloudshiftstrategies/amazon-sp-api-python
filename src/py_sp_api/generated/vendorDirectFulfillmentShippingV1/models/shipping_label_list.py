# coding: utf-8

"""
    Selling Partner API for Direct Fulfillment Shipping

    The Selling Partner API for Direct Fulfillment Shipping provides programmatic access to a direct fulfillment vendor's shipping data.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.vendorDirectFulfillmentShippingV1.models.pagination import Pagination
from py_sp_api.generated.vendorDirectFulfillmentShippingV1.models.shipping_label import ShippingLabel
from typing import Optional, Set
from typing_extensions import Self

class ShippingLabelList(BaseModel):
    """
    Response payload with the list of shipping labels
    """ # noqa: E501
    pagination: Optional[Pagination] = None
    shipping_labels: Optional[List[ShippingLabel]] = Field(default=None, description="An array containing the details of the generated shipping labels.", alias="shippingLabels")
    __properties: ClassVar[List[str]] = ["pagination", "shippingLabels"]

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
        """Create an instance of ShippingLabelList from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of pagination
        if self.pagination:
            _dict['pagination'] = self.pagination.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in shipping_labels (list)
        _items = []
        if self.shipping_labels:
            for _item_shipping_labels in self.shipping_labels:
                if _item_shipping_labels:
                    _items.append(_item_shipping_labels.to_dict())
            _dict['shippingLabels'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ShippingLabelList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pagination": Pagination.from_dict(obj["pagination"]) if obj.get("pagination") is not None else None,
            "shippingLabels": [ShippingLabel.from_dict(_item) for _item in obj["shippingLabels"]] if obj.get("shippingLabels") is not None else None
        })
        return _obj


