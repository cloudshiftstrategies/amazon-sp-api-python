# coding: utf-8

"""
    Selling Partner API for Retail Procurement Shipments

    The Selling Partner API for Retail Procurement Shipments provides programmatic access to retail shipping data for vendors.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.vendorShipments.models.volume import Volume
from py_sp_api.generated.vendorShipments.models.weight import Weight
from typing import Optional, Set
from typing_extensions import Self

class TransportShipmentMeasurements(BaseModel):
    """
    Shipment measurement details.
    """ # noqa: E501
    total_carton_count: Optional[StrictInt] = Field(default=None, description="Total number of cartons present in the shipment. Provide the cartonCount only for non-palletized shipments.", alias="totalCartonCount")
    total_pallet_stackable: Optional[StrictInt] = Field(default=None, description="Total number of Stackable Pallets present in the shipment.", alias="totalPalletStackable")
    total_pallet_non_stackable: Optional[StrictInt] = Field(default=None, description="Total number of Non Stackable Pallets present in the shipment.", alias="totalPalletNonStackable")
    shipment_weight: Optional[Weight] = Field(default=None, alias="shipmentWeight")
    shipment_volume: Optional[Volume] = Field(default=None, alias="shipmentVolume")
    __properties: ClassVar[List[str]] = ["totalCartonCount", "totalPalletStackable", "totalPalletNonStackable", "shipmentWeight", "shipmentVolume"]

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
        """Create an instance of TransportShipmentMeasurements from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of shipment_weight
        if self.shipment_weight:
            _dict['shipmentWeight'] = self.shipment_weight.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipment_volume
        if self.shipment_volume:
            _dict['shipmentVolume'] = self.shipment_volume.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransportShipmentMeasurements from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "totalCartonCount": obj.get("totalCartonCount"),
            "totalPalletStackable": obj.get("totalPalletStackable"),
            "totalPalletNonStackable": obj.get("totalPalletNonStackable"),
            "shipmentWeight": Weight.from_dict(obj["shipmentWeight"]) if obj.get("shipmentWeight") is not None else None,
            "shipmentVolume": Volume.from_dict(obj["shipmentVolume"]) if obj.get("shipmentVolume") is not None else None
        })
        return _obj


