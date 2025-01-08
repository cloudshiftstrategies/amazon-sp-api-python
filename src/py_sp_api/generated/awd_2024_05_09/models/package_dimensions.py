# coding: utf-8

"""
    The Selling Partner API for Amazon Warehousing and Distribution

    The Selling Partner API for Amazon Warehousing and Distribution (AWD) provides programmatic access to information about AWD shipments and inventory. 

    The version of the OpenAPI document: 2024-05-09
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Union
from py_sp_api.generated.awd_2024_05_09.models.dimension_unit_of_measurement import DimensionUnitOfMeasurement
from typing import Optional, Set
from typing_extensions import Self

class PackageDimensions(BaseModel):
    """
    Dimensions of the package.
    """ # noqa: E501
    height: Union[StrictFloat, StrictInt] = Field(description="Height of the package.")
    length: Union[StrictFloat, StrictInt] = Field(description="Length of the package.")
    unit_of_measurement: DimensionUnitOfMeasurement = Field(alias="unitOfMeasurement")
    width: Union[StrictFloat, StrictInt] = Field(description="Width of the package.")
    __properties: ClassVar[List[str]] = ["height", "length", "unitOfMeasurement", "width"]

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
        """Create an instance of PackageDimensions from a JSON string"""
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
        """Create an instance of PackageDimensions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "height": obj.get("height"),
            "length": obj.get("length"),
            "unitOfMeasurement": obj.get("unitOfMeasurement"),
            "width": obj.get("width")
        })
        return _obj


