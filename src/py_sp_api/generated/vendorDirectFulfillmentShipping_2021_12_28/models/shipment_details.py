# coding: utf-8

"""
    Selling Partner API for Direct Fulfillment Shipping

    Use the Selling Partner API for Direct Fulfillment Shipping to access a direct fulfillment vendor's shipping data.

    The version of the OpenAPI document: 2021-12-28
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ShipmentDetails(BaseModel):
    """
    Details about a shipment.
    """ # noqa: E501
    shipped_date: datetime = Field(description="The date of the shipment's departure from vendor's location. Vendors send ASNs within 30 minutes of departure from their warehouse/distribution center or six hours prior to the appointment time at the Amazon destination warehouse. The shipped date mentioned in the shipment confirmation cannot be in the future.", alias="shippedDate")
    shipment_status: StrictStr = Field(description="The shipment status.", alias="shipmentStatus")
    is_priority_shipment: Optional[StrictBool] = Field(default=None, description="Provide the priority of the shipment.", alias="isPriorityShipment")
    vendor_order_number: Optional[StrictStr] = Field(default=None, description="The vendor order number is a unique identifier generated by a vendor for their reference.", alias="vendorOrderNumber")
    estimated_delivery_date: Optional[datetime] = Field(default=None, description="The date on which the shipment is expected to reach the buyer's warehouse. The date is estimated based on the average transit time between the ship-from location and the destination. Usually, the exact appointment time is unknown when creating the shipment confirmation and is later provided by the buyer.", alias="estimatedDeliveryDate")
    __properties: ClassVar[List[str]] = ["shippedDate", "shipmentStatus", "isPriorityShipment", "vendorOrderNumber", "estimatedDeliveryDate"]

    @field_validator('shipment_status')
    def shipment_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['SHIPPED', 'FLOOR_DENIAL']):
            raise ValueError("must be one of enum values ('SHIPPED', 'FLOOR_DENIAL')")
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
        """Create an instance of ShipmentDetails from a JSON string"""
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
        """Create an instance of ShipmentDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "shippedDate": obj.get("shippedDate"),
            "shipmentStatus": obj.get("shipmentStatus"),
            "isPriorityShipment": obj.get("isPriorityShipment"),
            "vendorOrderNumber": obj.get("vendorOrderNumber"),
            "estimatedDeliveryDate": obj.get("estimatedDeliveryDate")
        })
        return _obj


