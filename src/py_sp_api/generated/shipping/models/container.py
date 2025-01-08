# coding: utf-8

"""
    Selling Partner API for Shipping

    Provides programmatic access to Amazon Shipping APIs.   **Note:** If you are new to the Amazon Shipping API, refer to the latest version of <a href=\"https://developer-docs.amazon.com/amazon-shipping/docs/shipping-api-v2-reference\">Amazon Shipping API (v2)</a> on the <a href=\"https://developer-docs.amazon.com/amazon-shipping/\">Amazon Shipping Developer Documentation</a> site.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from py_sp_api.generated.shipping.models.container_item import ContainerItem
from py_sp_api.generated.shipping.models.currency import Currency
from py_sp_api.generated.shipping.models.dimensions import Dimensions
from py_sp_api.generated.shipping.models.weight import Weight
from typing import Optional, Set
from typing_extensions import Self

class Container(BaseModel):
    """
    Container in the shipment.
    """ # noqa: E501
    container_type: Optional[StrictStr] = Field(default=None, description="The type of physical container being used. (always 'PACKAGE')", alias="containerType")
    container_reference_id: Annotated[str, Field(strict=True, max_length=40)] = Field(description="An identifier for the container. This must be unique within all the containers in the same shipment.", alias="containerReferenceId")
    value: Currency
    dimensions: Dimensions
    items: List[ContainerItem] = Field(description="A list of the items in the container.")
    weight: Weight
    __properties: ClassVar[List[str]] = ["containerType", "containerReferenceId", "value", "dimensions", "items", "weight"]

    @field_validator('container_type')
    def container_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PACKAGE']):
            raise ValueError("must be one of enum values ('PACKAGE')")
        return value

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
        """Create an instance of Container from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of value
        if self.value:
            _dict['value'] = self.value.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dimensions
        if self.dimensions:
            _dict['dimensions'] = self.dimensions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item_items in self.items:
                if _item_items:
                    _items.append(_item_items.to_dict())
            _dict['items'] = _items
        # override the default output from pydantic by calling `to_dict()` of weight
        if self.weight:
            _dict['weight'] = self.weight.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Container from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "containerType": obj.get("containerType"),
            "containerReferenceId": obj.get("containerReferenceId"),
            "value": Currency.from_dict(obj["value"]) if obj.get("value") is not None else None,
            "dimensions": Dimensions.from_dict(obj["dimensions"]) if obj.get("dimensions") is not None else None,
            "items": [ContainerItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
            "weight": Weight.from_dict(obj["weight"]) if obj.get("weight") is not None else None
        })
        return _obj


