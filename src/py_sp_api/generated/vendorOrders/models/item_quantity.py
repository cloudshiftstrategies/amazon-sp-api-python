# coding: utf-8

"""
    Selling Partner API for Retail Procurement Orders

    The Selling Partner API for Retail Procurement Orders provides programmatic access to vendor orders data.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ItemQuantity(BaseModel):
    """
    Details of quantity ordered.
    """ # noqa: E501
    amount: Optional[StrictInt] = Field(default=None, description="Acknowledged quantity. This value should not be zero.")
    unit_of_measure: Optional[StrictStr] = Field(default=None, description="Unit of measure for the acknowledged quantity.", alias="unitOfMeasure")
    unit_size: Optional[StrictInt] = Field(default=None, description="The case size, in the event that we ordered using cases.", alias="unitSize")
    __properties: ClassVar[List[str]] = ["amount", "unitOfMeasure", "unitSize"]

    @field_validator('unit_of_measure')
    def unit_of_measure_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Cases', 'Eaches']):
            raise ValueError("must be one of enum values ('Cases', 'Eaches')")
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
        """Create an instance of ItemQuantity from a JSON string"""
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
        """Create an instance of ItemQuantity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": obj.get("amount"),
            "unitOfMeasure": obj.get("unitOfMeasure"),
            "unitSize": obj.get("unitSize")
        })
        return _obj


