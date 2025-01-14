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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from py_sp_api.generated.awd_2024_05_09.models.address import Address
from py_sp_api.generated.awd_2024_05_09.models.distribution_package_quantity import DistributionPackageQuantity
from py_sp_api.generated.awd_2024_05_09.models.inbound_preferences import InboundPreferences
from py_sp_api.generated.awd_2024_05_09.models.inbound_shipment import InboundShipment
from py_sp_api.generated.awd_2024_05_09.models.inbound_status import InboundStatus
from typing import Optional, Set
from typing_extensions import Self

class InboundOrder(BaseModel):
    """
    Represents an AWD inbound order.
    """ # noqa: E501
    channel_placed_inbound_shipments: Annotated[List[InboundShipment], Field(min_length=1)] = Field(description="List of inbound shipments part of this order.", alias="channelPlacedInboundShipments")
    created_at: datetime = Field(description="Date when this order was created.", alias="createdAt")
    external_reference_id: Optional[StrictStr] = Field(default=None, description="Reference ID that can be used to correlate the order with partner resources.", alias="externalReferenceId")
    order_id: StrictStr = Field(description="Inbound order ID.", alias="orderId")
    order_status: InboundStatus = Field(alias="orderStatus")
    order_version: StrictStr = Field(description="Inbound order version.", alias="orderVersion")
    origin_address: Address = Field(alias="originAddress")
    packages_to_inbound: Annotated[List[DistributionPackageQuantity], Field(min_length=1)] = Field(description="List of packages to be inbounded.", alias="packagesToInbound")
    preferences: Optional[InboundPreferences] = None
    ship_by: Optional[datetime] = Field(default=None, description="Date by which this order will be shipped.", alias="shipBy")
    updated_at: Optional[datetime] = Field(default=None, description="Date when this order was last updated.", alias="updatedAt")
    __properties: ClassVar[List[str]] = ["channelPlacedInboundShipments", "createdAt", "externalReferenceId", "orderId", "orderStatus", "orderVersion", "originAddress", "packagesToInbound", "preferences", "shipBy", "updatedAt"]

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
        """Create an instance of InboundOrder from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in channel_placed_inbound_shipments (list)
        _items = []
        if self.channel_placed_inbound_shipments:
            for _item_channel_placed_inbound_shipments in self.channel_placed_inbound_shipments:
                if _item_channel_placed_inbound_shipments:
                    _items.append(_item_channel_placed_inbound_shipments.to_dict())
            _dict['channelPlacedInboundShipments'] = _items
        # override the default output from pydantic by calling `to_dict()` of origin_address
        if self.origin_address:
            _dict['originAddress'] = self.origin_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in packages_to_inbound (list)
        _items = []
        if self.packages_to_inbound:
            for _item_packages_to_inbound in self.packages_to_inbound:
                if _item_packages_to_inbound:
                    _items.append(_item_packages_to_inbound.to_dict())
            _dict['packagesToInbound'] = _items
        # override the default output from pydantic by calling `to_dict()` of preferences
        if self.preferences:
            _dict['preferences'] = self.preferences.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InboundOrder from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "channelPlacedInboundShipments": [InboundShipment.from_dict(_item) for _item in obj["channelPlacedInboundShipments"]] if obj.get("channelPlacedInboundShipments") is not None else None,
            "createdAt": obj.get("createdAt"),
            "externalReferenceId": obj.get("externalReferenceId"),
            "orderId": obj.get("orderId"),
            "orderStatus": obj.get("orderStatus"),
            "orderVersion": obj.get("orderVersion"),
            "originAddress": Address.from_dict(obj["originAddress"]) if obj.get("originAddress") is not None else None,
            "packagesToInbound": [DistributionPackageQuantity.from_dict(_item) for _item in obj["packagesToInbound"]] if obj.get("packagesToInbound") is not None else None,
            "preferences": InboundPreferences.from_dict(obj["preferences"]) if obj.get("preferences") is not None else None,
            "shipBy": obj.get("shipBy"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj


