# coding: utf-8

"""
    Selling Partner API for Services

    With the Services API, you can build applications that help service providers get and modify their service orders and manage their resources.

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
from typing_extensions import Annotated
from py_sp_api.generated.services.models.recurrence import Recurrence
from typing import Optional, Set
from typing_extensions import Self

class AvailabilityRecord(BaseModel):
    """
    `AvailabilityRecord` to represent the capacity of a resource over a time range.
    """ # noqa: E501
    start_time: datetime = Field(description="Denotes the time from when the resource is available in a day in ISO-8601 format.", alias="startTime")
    end_time: datetime = Field(description="Denotes the time till when the resource is available in a day in ISO-8601 format.", alias="endTime")
    recurrence: Optional[Recurrence] = None
    capacity: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="Signifies the capacity of a resource which is available.")
    __properties: ClassVar[List[str]] = ["startTime", "endTime", "recurrence", "capacity"]

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
        """Create an instance of AvailabilityRecord from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of recurrence
        if self.recurrence:
            _dict['recurrence'] = self.recurrence.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AvailabilityRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "startTime": obj.get("startTime"),
            "endTime": obj.get("endTime"),
            "recurrence": Recurrence.from_dict(obj["recurrence"]) if obj.get("recurrence") is not None else None,
            "capacity": obj.get("capacity")
        })
        return _obj


