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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.vendorOrders.models.item_quantity import ItemQuantity
from typing import Optional, Set
from typing_extensions import Self

class OrderItemAcknowledgement(BaseModel):
    """
    Represents the acknowledgement details for an individual order item, including the acknowledgement code, acknowledged quantity, scheduled ship and delivery dates, and rejection reason (if applicable).
    """ # noqa: E501
    acknowledgement_code: StrictStr = Field(description="This indicates the acknowledgement code.", alias="acknowledgementCode")
    acknowledged_quantity: ItemQuantity = Field(alias="acknowledgedQuantity")
    scheduled_ship_date: Optional[datetime] = Field(default=None, description="Estimated ship date per line item. Must be in ISO-8601 date/time format.", alias="scheduledShipDate")
    scheduled_delivery_date: Optional[datetime] = Field(default=None, description="Estimated delivery date per line item. Must be in ISO-8601 date/time format.", alias="scheduledDeliveryDate")
    rejection_reason: Optional[StrictStr] = Field(default=None, description="Indicates the reason for rejection.", alias="rejectionReason")
    __properties: ClassVar[List[str]] = ["acknowledgementCode", "acknowledgedQuantity", "scheduledShipDate", "scheduledDeliveryDate", "rejectionReason"]

    @field_validator('acknowledgement_code')
    def acknowledgement_code_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Accepted', 'Backordered', 'Rejected']):
            raise ValueError("must be one of enum values ('Accepted', 'Backordered', 'Rejected')")
        return value

    @field_validator('rejection_reason')
    def rejection_reason_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['TemporarilyUnavailable', 'InvalidProductIdentifier', 'ObsoleteProduct']):
            raise ValueError("must be one of enum values ('TemporarilyUnavailable', 'InvalidProductIdentifier', 'ObsoleteProduct')")
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
        """Create an instance of OrderItemAcknowledgement from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of acknowledged_quantity
        if self.acknowledged_quantity:
            _dict['acknowledgedQuantity'] = self.acknowledged_quantity.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderItemAcknowledgement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "acknowledgementCode": obj.get("acknowledgementCode"),
            "acknowledgedQuantity": ItemQuantity.from_dict(obj["acknowledgedQuantity"]) if obj.get("acknowledgedQuantity") is not None else None,
            "scheduledShipDate": obj.get("scheduledShipDate"),
            "scheduledDeliveryDate": obj.get("scheduledDeliveryDate"),
            "rejectionReason": obj.get("rejectionReason")
        })
        return _obj


