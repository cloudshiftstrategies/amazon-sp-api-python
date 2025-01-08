# coding: utf-8

"""
    Selling Partner API for Catalog Items

    The Selling Partner API for Catalog Items helps you programmatically retrieve item details for items in the catalog.

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
from py_sp_api.generated.catalogItemsV0.models.decimal_with_units import DecimalWithUnits
from typing import Optional, Set
from typing_extensions import Self

class Image(BaseModel):
    """
    The image attribute of the item.
    """ # noqa: E501
    url: Optional[StrictStr] = Field(default=None, description="The image URL attribute of the item.", alias="URL")
    height: Optional[DecimalWithUnits] = Field(default=None, alias="Height")
    width: Optional[DecimalWithUnits] = Field(default=None, alias="Width")
    __properties: ClassVar[List[str]] = ["URL", "Height", "Width"]

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
        """Create an instance of Image from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of height
        if self.height:
            _dict['Height'] = self.height.to_dict()
        # override the default output from pydantic by calling `to_dict()` of width
        if self.width:
            _dict['Width'] = self.width.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Image from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "URL": obj.get("URL"),
            "Height": DecimalWithUnits.from_dict(obj["Height"]) if obj.get("Height") is not None else None,
            "Width": DecimalWithUnits.from_dict(obj["Width"]) if obj.get("Width") is not None else None
        })
        return _obj


