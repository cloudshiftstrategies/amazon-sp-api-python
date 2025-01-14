# coding: utf-8

"""
    Selling Partner API for Supply Sources

    Manage configurations and capabilities of seller supply sources.

    The version of the OpenAPI document: 2020-07-01
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.supplySources_2020_07_01.models.contact_details import ContactDetails
from py_sp_api.generated.supplySources_2020_07_01.models.duration import Duration
from py_sp_api.generated.supplySources_2020_07_01.models.operating_hours_by_day import OperatingHoursByDay
from py_sp_api.generated.supplySources_2020_07_01.models.throughput_config import ThroughputConfig
from typing import Optional, Set
from typing_extensions import Self

class OperationalConfiguration(BaseModel):
    """
    The operational configuration of `supplySources`.
    """ # noqa: E501
    contact_details: Optional[ContactDetails] = Field(default=None, alias="contactDetails")
    throughput_config: Optional[ThroughputConfig] = Field(default=None, alias="throughputConfig")
    operating_hours_by_day: Optional[OperatingHoursByDay] = Field(default=None, alias="operatingHoursByDay")
    handling_time: Optional[Duration] = Field(default=None, alias="handlingTime")
    __properties: ClassVar[List[str]] = ["contactDetails", "throughputConfig", "operatingHoursByDay", "handlingTime"]

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
        """Create an instance of OperationalConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of contact_details
        if self.contact_details:
            _dict['contactDetails'] = self.contact_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of throughput_config
        if self.throughput_config:
            _dict['throughputConfig'] = self.throughput_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of operating_hours_by_day
        if self.operating_hours_by_day:
            _dict['operatingHoursByDay'] = self.operating_hours_by_day.to_dict()
        # override the default output from pydantic by calling `to_dict()` of handling_time
        if self.handling_time:
            _dict['handlingTime'] = self.handling_time.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OperationalConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "contactDetails": ContactDetails.from_dict(obj["contactDetails"]) if obj.get("contactDetails") is not None else None,
            "throughputConfig": ThroughputConfig.from_dict(obj["throughputConfig"]) if obj.get("throughputConfig") is not None else None,
            "operatingHoursByDay": OperatingHoursByDay.from_dict(obj["operatingHoursByDay"]) if obj.get("operatingHoursByDay") is not None else None,
            "handlingTime": Duration.from_dict(obj["handlingTime"]) if obj.get("handlingTime") is not None else None
        })
        return _obj


