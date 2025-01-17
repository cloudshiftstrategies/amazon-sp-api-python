# coding: utf-8

"""
    Fulfillment Inbound v2024-03-20

    The Selling Partner API for Fulfillment By Amazon (FBA) Inbound. The FBA Inbound API enables building inbound workflows to create, manage, and send shipments into Amazon's fulfillment network. The API has interoperability with the Send-to-Amazon user interface.

    The version of the OpenAPI document: 2024-03-20
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.contact_information import ContactInformation
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.dates import Dates
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.freight_information import FreightInformation
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.selected_delivery_window import SelectedDeliveryWindow
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.self_ship_appointment_details import SelfShipAppointmentDetails
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.shipment_destination import ShipmentDestination
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.shipment_source import ShipmentSource
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.tracking_details import TrackingDetails
from typing import Optional, Set
from typing_extensions import Self

class Shipment(BaseModel):
    """
    Contains information pertaining to a shipment in an inbound plan.
    """ # noqa: E501
    amazon_reference_id: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=1024)]] = Field(default=None, description="A unique identifier created by Amazon that identifies this Amazon-partnered, Less Than Truckload/Full Truckload (LTL/FTL) shipment.", alias="amazonReferenceId")
    contact_information: Optional[ContactInformation] = Field(default=None, alias="contactInformation")
    dates: Optional[Dates] = None
    destination: ShipmentDestination
    freight_information: Optional[FreightInformation] = Field(default=None, alias="freightInformation")
    name: Optional[StrictStr] = Field(default=None, description="The name of the shipment.")
    placement_option_id: Annotated[str, Field(min_length=38, strict=True, max_length=38)] = Field(description="The identifier of a placement option. A placement option represents the shipment splits and destinations of SKUs.", alias="placementOptionId")
    selected_delivery_window: Optional[SelectedDeliveryWindow] = Field(default=None, alias="selectedDeliveryWindow")
    selected_transportation_option_id: Optional[Annotated[str, Field(min_length=38, strict=True, max_length=38)]] = Field(default=None, description="Identifier of a transportation option. A transportation option represent one option for how to send a shipment.", alias="selectedTransportationOptionId")
    self_ship_appointment_details: Optional[List[SelfShipAppointmentDetails]] = Field(default=None, description="List of self ship appointment details.", alias="selfShipAppointmentDetails")
    shipment_confirmation_id: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=1024)]] = Field(default=None, description="The confirmed shipment ID which shows up on labels (for example, `FBA1234ABCD`).", alias="shipmentConfirmationId")
    shipment_id: Annotated[str, Field(min_length=38, strict=True, max_length=38)] = Field(description="Identifier of a shipment. A shipment contains the boxes and units being inbounded.", alias="shipmentId")
    source: ShipmentSource
    status: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=1024)]] = Field(default=None, description="The status of a shipment. The state of the shipment will typically start as `UNCONFIRMED`, then transition to `WORKING` after a placement option has been confirmed, and then to `READY_TO_SHIP` once labels are generated.  Possible values: `ABANDONED`, `CANCELLED`, `CHECKED_IN`, `CLOSED`, `DELETED`, `DELIVERED`, `IN_TRANSIT`, `MIXED`, `READY_TO_SHIP`, `RECEIVING`, `SHIPPED`, `UNCONFIRMED`, `WORKING`")
    tracking_details: Optional[TrackingDetails] = Field(default=None, alias="trackingDetails")
    __properties: ClassVar[List[str]] = ["amazonReferenceId", "contactInformation", "dates", "destination", "freightInformation", "name", "placementOptionId", "selectedDeliveryWindow", "selectedTransportationOptionId", "selfShipAppointmentDetails", "shipmentConfirmationId", "shipmentId", "source", "status", "trackingDetails"]

    @field_validator('placement_option_id')
    def placement_option_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9-]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9-]*$/")
        return value

    @field_validator('selected_transportation_option_id')
    def selected_transportation_option_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9-]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9-]*$/")
        return value

    @field_validator('shipment_id')
    def shipment_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9-]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9-]*$/")
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
        """Create an instance of Shipment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of contact_information
        if self.contact_information:
            _dict['contactInformation'] = self.contact_information.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dates
        if self.dates:
            _dict['dates'] = self.dates.to_dict()
        # override the default output from pydantic by calling `to_dict()` of destination
        if self.destination:
            _dict['destination'] = self.destination.to_dict()
        # override the default output from pydantic by calling `to_dict()` of freight_information
        if self.freight_information:
            _dict['freightInformation'] = self.freight_information.to_dict()
        # override the default output from pydantic by calling `to_dict()` of selected_delivery_window
        if self.selected_delivery_window:
            _dict['selectedDeliveryWindow'] = self.selected_delivery_window.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in self_ship_appointment_details (list)
        _items = []
        if self.self_ship_appointment_details:
            for _item_self_ship_appointment_details in self.self_ship_appointment_details:
                if _item_self_ship_appointment_details:
                    _items.append(_item_self_ship_appointment_details.to_dict())
            _dict['selfShipAppointmentDetails'] = _items
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tracking_details
        if self.tracking_details:
            _dict['trackingDetails'] = self.tracking_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Shipment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amazonReferenceId": obj.get("amazonReferenceId"),
            "contactInformation": ContactInformation.from_dict(obj["contactInformation"]) if obj.get("contactInformation") is not None else None,
            "dates": Dates.from_dict(obj["dates"]) if obj.get("dates") is not None else None,
            "destination": ShipmentDestination.from_dict(obj["destination"]) if obj.get("destination") is not None else None,
            "freightInformation": FreightInformation.from_dict(obj["freightInformation"]) if obj.get("freightInformation") is not None else None,
            "name": obj.get("name"),
            "placementOptionId": obj.get("placementOptionId"),
            "selectedDeliveryWindow": SelectedDeliveryWindow.from_dict(obj["selectedDeliveryWindow"]) if obj.get("selectedDeliveryWindow") is not None else None,
            "selectedTransportationOptionId": obj.get("selectedTransportationOptionId"),
            "selfShipAppointmentDetails": [SelfShipAppointmentDetails.from_dict(_item) for _item in obj["selfShipAppointmentDetails"]] if obj.get("selfShipAppointmentDetails") is not None else None,
            "shipmentConfirmationId": obj.get("shipmentConfirmationId"),
            "shipmentId": obj.get("shipmentId"),
            "source": ShipmentSource.from_dict(obj["source"]) if obj.get("source") is not None else None,
            "status": obj.get("status"),
            "trackingDetails": TrackingDetails.from_dict(obj["trackingDetails"]) if obj.get("trackingDetails") is not None else None
        })
        return _obj


