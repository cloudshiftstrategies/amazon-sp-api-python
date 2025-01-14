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
from typing_extensions import Annotated
from py_sp_api.generated.services.models.appointment import Appointment
from py_sp_api.generated.services.models.appointment_time import AppointmentTime
from py_sp_api.generated.services.models.associated_item import AssociatedItem
from py_sp_api.generated.services.models.buyer import Buyer
from py_sp_api.generated.services.models.scope_of_work import ScopeOfWork
from py_sp_api.generated.services.models.seller import Seller
from py_sp_api.generated.services.models.service_job_provider import ServiceJobProvider
from py_sp_api.generated.services.models.service_location import ServiceLocation
from typing import Optional, Set
from typing_extensions import Self

class ServiceJob(BaseModel):
    """
    The job details of a service.
    """ # noqa: E501
    create_time: Optional[datetime] = Field(default=None, description="The date and time of the creation of the job in ISO 8601 format.", alias="createTime")
    service_job_id: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=100)]] = Field(default=None, description="Amazon identifier for the service job.", alias="serviceJobId")
    service_job_status: Optional[StrictStr] = Field(default=None, description="The status of the service job.", alias="serviceJobStatus")
    scope_of_work: Optional[ScopeOfWork] = Field(default=None, alias="scopeOfWork")
    seller: Optional[Seller] = None
    service_job_provider: Optional[ServiceJobProvider] = Field(default=None, alias="serviceJobProvider")
    preferred_appointment_times: Optional[List[AppointmentTime]] = Field(default=None, description="A list of appointment windows preferred by the buyer. Included only if the buyer selected appointment windows when creating the order.", alias="preferredAppointmentTimes")
    appointments: Optional[List[Appointment]] = Field(default=None, description="A list of appointments.")
    service_order_id: Optional[Annotated[str, Field(min_length=5, strict=True, max_length=20)]] = Field(default=None, description="The Amazon-defined identifier for an order placed by the buyer, in 3-7-7 format.", alias="serviceOrderId")
    marketplace_id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The marketplace identifier.", alias="marketplaceId")
    store_id: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=100)]] = Field(default=None, description="The Amazon-defined identifier for the region scope.", alias="storeId")
    buyer: Optional[Buyer] = None
    associated_items: Optional[List[AssociatedItem]] = Field(default=None, description="A list of items associated with the service job.", alias="associatedItems")
    service_location: Optional[ServiceLocation] = Field(default=None, alias="serviceLocation")
    __properties: ClassVar[List[str]] = ["createTime", "serviceJobId", "serviceJobStatus", "scopeOfWork", "seller", "serviceJobProvider", "preferredAppointmentTimes", "appointments", "serviceOrderId", "marketplaceId", "storeId", "buyer", "associatedItems", "serviceLocation"]

    @field_validator('service_job_status')
    def service_job_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['NOT_SERVICED', 'CANCELLED', 'COMPLETED', 'PENDING_SCHEDULE', 'NOT_FULFILLABLE', 'HOLD', 'PAYMENT_DECLINED']):
            raise ValueError("must be one of enum values ('NOT_SERVICED', 'CANCELLED', 'COMPLETED', 'PENDING_SCHEDULE', 'NOT_FULFILLABLE', 'HOLD', 'PAYMENT_DECLINED')")
        return value

    @field_validator('marketplace_id')
    def marketplace_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[A-Z0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[A-Z0-9]*$/")
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
        """Create an instance of ServiceJob from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of scope_of_work
        if self.scope_of_work:
            _dict['scopeOfWork'] = self.scope_of_work.to_dict()
        # override the default output from pydantic by calling `to_dict()` of seller
        if self.seller:
            _dict['seller'] = self.seller.to_dict()
        # override the default output from pydantic by calling `to_dict()` of service_job_provider
        if self.service_job_provider:
            _dict['serviceJobProvider'] = self.service_job_provider.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in preferred_appointment_times (list)
        _items = []
        if self.preferred_appointment_times:
            for _item_preferred_appointment_times in self.preferred_appointment_times:
                if _item_preferred_appointment_times:
                    _items.append(_item_preferred_appointment_times.to_dict())
            _dict['preferredAppointmentTimes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in appointments (list)
        _items = []
        if self.appointments:
            for _item_appointments in self.appointments:
                if _item_appointments:
                    _items.append(_item_appointments.to_dict())
            _dict['appointments'] = _items
        # override the default output from pydantic by calling `to_dict()` of buyer
        if self.buyer:
            _dict['buyer'] = self.buyer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in associated_items (list)
        _items = []
        if self.associated_items:
            for _item_associated_items in self.associated_items:
                if _item_associated_items:
                    _items.append(_item_associated_items.to_dict())
            _dict['associatedItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of service_location
        if self.service_location:
            _dict['serviceLocation'] = self.service_location.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServiceJob from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "createTime": obj.get("createTime"),
            "serviceJobId": obj.get("serviceJobId"),
            "serviceJobStatus": obj.get("serviceJobStatus"),
            "scopeOfWork": ScopeOfWork.from_dict(obj["scopeOfWork"]) if obj.get("scopeOfWork") is not None else None,
            "seller": Seller.from_dict(obj["seller"]) if obj.get("seller") is not None else None,
            "serviceJobProvider": ServiceJobProvider.from_dict(obj["serviceJobProvider"]) if obj.get("serviceJobProvider") is not None else None,
            "preferredAppointmentTimes": [AppointmentTime.from_dict(_item) for _item in obj["preferredAppointmentTimes"]] if obj.get("preferredAppointmentTimes") is not None else None,
            "appointments": [Appointment.from_dict(_item) for _item in obj["appointments"]] if obj.get("appointments") is not None else None,
            "serviceOrderId": obj.get("serviceOrderId"),
            "marketplaceId": obj.get("marketplaceId"),
            "storeId": obj.get("storeId"),
            "buyer": Buyer.from_dict(obj["buyer"]) if obj.get("buyer") is not None else None,
            "associatedItems": [AssociatedItem.from_dict(_item) for _item in obj["associatedItems"]] if obj.get("associatedItems") is not None else None,
            "serviceLocation": ServiceLocation.from_dict(obj["serviceLocation"]) if obj.get("serviceLocation") is not None else None
        })
        return _obj


