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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class BuyerCustomizedInfoDetail(BaseModel):
    """
    The details of the products the vendor has configured as customizable.
    """ # noqa: E501
    customized_url: Optional[StrictStr] = Field(default=None, description="A [Base 64](https://datatracker.ietf.org/doc/html/rfc4648#section-4) encoded URL using the UTF-8 character set. The URL provides the location of the zip file that specifies the types of customizations or configurations allowed by the vendor, along with types and ranges for the attributes of their products.", alias="customizedUrl")
    __properties: ClassVar[List[str]] = ["customizedUrl"]

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
        """Create an instance of BuyerCustomizedInfoDetail from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BuyerCustomizedInfoDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "customizedUrl": obj.get("customizedUrl")
        })
        return _obj


