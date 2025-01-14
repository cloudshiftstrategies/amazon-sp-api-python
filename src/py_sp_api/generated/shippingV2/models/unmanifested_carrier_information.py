# coding: utf-8

"""
    Amazon Shipping API

    The Amazon Shipping API is designed to support outbound shipping use cases both for orders originating on Amazon-owned marketplaces as well as external channels/marketplaces. With these APIs, you can request shipping rates, create shipments, cancel shipments, and track shipments.

    The version of the OpenAPI document: v2
    Contact: swa-api-core@amazon.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.shippingV2.models.unmanifested_shipment_location import UnmanifestedShipmentLocation
from typing import Optional, Set
from typing_extensions import Self

class UnmanifestedCarrierInformation(BaseModel):
    """
    UnmanifestedCarrierInformation like carrierId CarrierName and Location
    """ # noqa: E501
    carrier_id: Optional[StrictStr] = Field(default=None, description="The carrier identifier for the offering, provided by the carrier.", alias="carrierId")
    carrier_name: Optional[StrictStr] = Field(default=None, description="The carrier name for the offering.", alias="carrierName")
    unmanifested_shipment_location_list: Optional[List[UnmanifestedShipmentLocation]] = Field(default=None, description="A list of UnmanifestedShipmentLocation", alias="unmanifestedShipmentLocationList")
    __properties: ClassVar[List[str]] = ["carrierId", "carrierName", "unmanifestedShipmentLocationList"]

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
        """Create an instance of UnmanifestedCarrierInformation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in unmanifested_shipment_location_list (list)
        _items = []
        if self.unmanifested_shipment_location_list:
            for _item_unmanifested_shipment_location_list in self.unmanifested_shipment_location_list:
                if _item_unmanifested_shipment_location_list:
                    _items.append(_item_unmanifested_shipment_location_list.to_dict())
            _dict['unmanifestedShipmentLocationList'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UnmanifestedCarrierInformation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "carrierId": obj.get("carrierId"),
            "carrierName": obj.get("carrierName"),
            "unmanifestedShipmentLocationList": [UnmanifestedShipmentLocation.from_dict(_item) for _item in obj["unmanifestedShipmentLocationList"]] if obj.get("unmanifestedShipmentLocationList") is not None else None
        })
        return _obj


