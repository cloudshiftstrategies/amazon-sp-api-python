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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from py_sp_api.generated.awd_2024_05_09.models.carrier_code import CarrierCode
from typing import Optional, Set
from typing_extensions import Self

class TrackingDetails(BaseModel):
    """
    Tracking details for the shipment. If using SPD transportation, this can be for each case. If not using SPD transportation, this is a single tracking entry for the entire shipment.
    """ # noqa: E501
    carrier_code: Optional[CarrierCode] = Field(default=None, alias="carrierCode")
    ship_by: datetime = Field(description="Timestamp denoting when the shipment will be shipped Date should be in ISO 8601 format as defined by date-time.", alias="shipBy")
    booking_id: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="The identifier that is received from transportation to uniquely identify a booking.", alias="bookingId")
    __properties: ClassVar[List[str]] = ["carrierCode", "shipBy", "bookingId"]

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
        """Create an instance of TrackingDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of carrier_code
        if self.carrier_code:
            _dict['carrierCode'] = self.carrier_code.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TrackingDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "carrierCode": CarrierCode.from_dict(obj["carrierCode"]) if obj.get("carrierCode") is not None else None,
            "shipBy": obj.get("shipBy"),
            "bookingId": obj.get("bookingId")
        })
        return _obj


