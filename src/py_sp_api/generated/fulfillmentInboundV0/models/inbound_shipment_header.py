# coding: utf-8

"""
    Selling Partner API for Fulfillment Inbound

    The Selling Partner API for Fulfillment Inbound lets you create applications that create and update inbound shipments of inventory to Amazon's fulfillment network.

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.fulfillmentInboundV0.models.address import Address
from py_sp_api.generated.fulfillmentInboundV0.models.intended_box_contents_source import IntendedBoxContentsSource
from py_sp_api.generated.fulfillmentInboundV0.models.label_prep_preference import LabelPrepPreference
from py_sp_api.generated.fulfillmentInboundV0.models.shipment_status import ShipmentStatus
from typing import Optional, Set
from typing_extensions import Self

class InboundShipmentHeader(BaseModel):
    """
    Inbound shipment information used to create and update inbound shipments.
    """ # noqa: E501
    shipment_name: StrictStr = Field(description="The name for the shipment. Use a naming convention that helps distinguish between shipments over time, such as the date the shipment was created.", alias="ShipmentName")
    ship_from_address: Address = Field(alias="ShipFromAddress")
    destination_fulfillment_center_id: StrictStr = Field(description="The identifier for the fulfillment center to which the shipment will be shipped. Get this value from the InboundShipmentPlan object in the response returned by the createInboundShipmentPlan operation.", alias="DestinationFulfillmentCenterId")
    are_cases_required: Optional[StrictBool] = Field(default=None, description="Indicates whether or not an inbound shipment contains case-packed boxes. Note: A shipment must contain either all case-packed boxes or all individually packed boxes.  Possible values:  true - All boxes in the shipment must be case packed.  false - All boxes in the shipment must be individually packed.  Note: If AreCasesRequired = true for an inbound shipment, then the value of QuantityInCase must be greater than zero for every item in the shipment. Otherwise the service returns an error.", alias="AreCasesRequired")
    shipment_status: ShipmentStatus = Field(alias="ShipmentStatus")
    label_prep_preference: LabelPrepPreference = Field(alias="LabelPrepPreference")
    intended_box_contents_source: Optional[IntendedBoxContentsSource] = Field(default=None, alias="IntendedBoxContentsSource")
    __properties: ClassVar[List[str]] = ["ShipmentName", "ShipFromAddress", "DestinationFulfillmentCenterId", "AreCasesRequired", "ShipmentStatus", "LabelPrepPreference", "IntendedBoxContentsSource"]

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
        """Create an instance of InboundShipmentHeader from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ship_from_address
        if self.ship_from_address:
            _dict['ShipFromAddress'] = self.ship_from_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InboundShipmentHeader from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ShipmentName": obj.get("ShipmentName"),
            "ShipFromAddress": Address.from_dict(obj["ShipFromAddress"]) if obj.get("ShipFromAddress") is not None else None,
            "DestinationFulfillmentCenterId": obj.get("DestinationFulfillmentCenterId"),
            "AreCasesRequired": obj.get("AreCasesRequired"),
            "ShipmentStatus": obj.get("ShipmentStatus"),
            "LabelPrepPreference": obj.get("LabelPrepPreference"),
            "IntendedBoxContentsSource": obj.get("IntendedBoxContentsSource")
        })
        return _obj


