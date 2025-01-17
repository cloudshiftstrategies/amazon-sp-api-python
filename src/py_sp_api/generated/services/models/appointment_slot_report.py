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
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.services.models.appointment_slot import AppointmentSlot
from typing import Optional, Set
from typing_extensions import Self

class AppointmentSlotReport(BaseModel):
    """
    Availability information as per the service context queried.
    """ # noqa: E501
    scheduling_type: Optional[StrictStr] = Field(default=None, description="Defines the type of slots.", alias="schedulingType")
    start_time: Optional[datetime] = Field(default=None, description="Start Time from which the appointment slots are generated in ISO 8601 format.", alias="startTime")
    end_time: Optional[datetime] = Field(default=None, description="End Time up to which the appointment slots are generated in ISO 8601 format.", alias="endTime")
    appointment_slots: Optional[List[AppointmentSlot]] = Field(default=None, description="A list of time windows along with associated capacity in which the service can be performed.", alias="appointmentSlots")
    __properties: ClassVar[List[str]] = ["schedulingType", "startTime", "endTime", "appointmentSlots"]

    @field_validator('scheduling_type')
    def scheduling_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['REAL_TIME_SCHEDULING', 'NON_REAL_TIME_SCHEDULING']):
            raise ValueError("must be one of enum values ('REAL_TIME_SCHEDULING', 'NON_REAL_TIME_SCHEDULING')")
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
        """Create an instance of AppointmentSlotReport from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in appointment_slots (list)
        _items = []
        if self.appointment_slots:
            for _item_appointment_slots in self.appointment_slots:
                if _item_appointment_slots:
                    _items.append(_item_appointment_slots.to_dict())
            _dict['appointmentSlots'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AppointmentSlotReport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schedulingType": obj.get("schedulingType"),
            "startTime": obj.get("startTime"),
            "endTime": obj.get("endTime"),
            "appointmentSlots": [AppointmentSlot.from_dict(_item) for _item in obj["appointmentSlots"]] if obj.get("appointmentSlots") is not None else None
        })
        return _obj


