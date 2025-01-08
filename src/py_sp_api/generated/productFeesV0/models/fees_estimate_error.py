# coding: utf-8

"""
    Selling Partner API for Product Fees

    The Selling Partner API for Product Fees lets you programmatically retrieve estimated fees for a product. You can then account for those fees in your pricing.

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class FeesEstimateError(BaseModel):
    """
    An unexpected error occurred during this operation.
    """ # noqa: E501
    type: StrictStr = Field(description="An error type, identifying either the receiver or the sender as the originator of the error.", alias="Type")
    code: StrictStr = Field(description="An error code that identifies the type of error that occurred.", alias="Code")
    message: StrictStr = Field(description="A message that describes the error condition.", alias="Message")
    detail: List[Dict[str, Any]] = Field(description="Additional information that can help the caller understand or fix the issue.", alias="Detail")
    __properties: ClassVar[List[str]] = ["Type", "Code", "Message", "Detail"]

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
        """Create an instance of FeesEstimateError from a JSON string"""
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
        """Create an instance of FeesEstimateError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Type": obj.get("Type"),
            "Code": obj.get("Code"),
            "Message": obj.get("Message"),
            "Detail": obj.get("Detail")
        })
        return _obj


