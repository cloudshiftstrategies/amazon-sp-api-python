# coding: utf-8

"""
    Amazon Shipping API

    The Amazon Shipping API is designed to support outbound shipping use cases both for orders originating on Amazon-owned marketplaces as well as external channels/marketplaces. With these APIs, you can request shipping rates, create shipments, cancel shipments, and track shipments.

    The version of the OpenAPI document: v2
    Contact: swa-api-core@amazon.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.shippingV2.models.date_range import DateRange
from py_sp_api.generated.shippingV2.models.operating_hours import OperatingHours
from typing import Optional, Set
from typing_extensions import Self

class ExceptionOperatingHours(BaseModel):
    """
    Defines exceptions to standard operating hours for certain date ranges.
    """ # noqa: E501
    date_range: Optional[DateRange] = Field(default=None, alias="dateRange")
    operating_hours: Optional[OperatingHours] = Field(default=None, alias="operatingHours")
    __properties: ClassVar[List[str]] = ["dateRange", "operatingHours"]

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
        """Create an instance of ExceptionOperatingHours from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of date_range
        if self.date_range:
            _dict['dateRange'] = self.date_range.to_dict()
        # override the default output from pydantic by calling `to_dict()` of operating_hours
        if self.operating_hours:
            _dict['operatingHours'] = self.operating_hours.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExceptionOperatingHours from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dateRange": DateRange.from_dict(obj["dateRange"]) if obj.get("dateRange") is not None else None,
            "operatingHours": OperatingHours.from_dict(obj["operatingHours"]) if obj.get("operatingHours") is not None else None
        })
        return _obj


