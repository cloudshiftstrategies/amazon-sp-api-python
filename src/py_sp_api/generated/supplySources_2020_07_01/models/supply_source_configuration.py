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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.supplySources_2020_07_01.models.operational_configuration import OperationalConfiguration
from typing import Optional, Set
from typing_extensions import Self

class SupplySourceConfiguration(BaseModel):
    """
    Includes configuration and timezone of a supply source.
    """ # noqa: E501
    operational_configuration: Optional[OperationalConfiguration] = Field(default=None, alias="operationalConfiguration")
    timezone: Optional[StrictStr] = Field(default=None, description="Please see RFC 6557, should be a canonical time zone ID as listed here: https://www.joda.org/joda-time/timezones.html.")
    __properties: ClassVar[List[str]] = ["operationalConfiguration", "timezone"]

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
        """Create an instance of SupplySourceConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of operational_configuration
        if self.operational_configuration:
            _dict['operationalConfiguration'] = self.operational_configuration.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SupplySourceConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "operationalConfiguration": OperationalConfiguration.from_dict(obj["operationalConfiguration"]) if obj.get("operationalConfiguration") is not None else None,
            "timezone": obj.get("timezone")
        })
        return _obj


