# coding: utf-8

"""
    Orders v0

    Use the Orders Selling Partner API to programmatically retrieve order information. With this API, you can develop fast, flexible, and custom applications to manage order synchronization, perform order research, and create demand-based decision support tools.   _Note:_ For the JP, AU, and SG marketplaces, the Orders API supports orders from 2016 onward. For all other marketplaces, the Orders API supports orders for the last two years (orders older than this don't show up in the response).

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.ordersV0.models.open_interval import OpenInterval
from typing import Optional, Set
from typing_extensions import Self

class BusinessHours(BaseModel):
    """
    Business days and hours when the destination is open for deliveries.
    """ # noqa: E501
    day_of_week: Optional[StrictStr] = Field(default=None, description="Day of the week.", alias="DayOfWeek")
    open_intervals: Optional[List[OpenInterval]] = Field(default=None, description="Time window during the day when the business is open.", alias="OpenIntervals")
    __properties: ClassVar[List[str]] = ["DayOfWeek", "OpenIntervals"]

    @field_validator('day_of_week')
    def day_of_week_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']):
            raise ValueError("must be one of enum values ('SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT')")
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
        """Create an instance of BusinessHours from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in open_intervals (list)
        _items = []
        if self.open_intervals:
            for _item_open_intervals in self.open_intervals:
                if _item_open_intervals:
                    _items.append(_item_open_intervals.to_dict())
            _dict['OpenIntervals'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BusinessHours from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "DayOfWeek": obj.get("DayOfWeek"),
            "OpenIntervals": [OpenInterval.from_dict(_item) for _item in obj["OpenIntervals"]] if obj.get("OpenIntervals") is not None else None
        })
        return _obj


