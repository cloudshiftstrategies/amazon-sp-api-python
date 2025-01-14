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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from py_sp_api.generated.vendorShipments.models.route import Route
from py_sp_api.generated.vendorShipments.models.weight import Weight
from typing import Optional, Set
from typing_extensions import Self

class ImportDetails(BaseModel):
    """
    Provide these fields only if this shipment is a direct import.
    """ # noqa: E501
    method_of_payment: Optional[StrictStr] = Field(default=None, description="This is used for import purchase orders only. If the recipient requests, this field will contain the shipment method of payment.", alias="methodOfPayment")
    seal_number: Optional[StrictStr] = Field(default=None, description="The container's seal number.", alias="sealNumber")
    route: Optional[Route] = None
    import_containers: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None, description="Types and numbers of container(s) for import purchase orders. Can be a comma-separated list if shipment has multiple containers.", alias="importContainers")
    billable_weight: Optional[Weight] = Field(default=None, alias="billableWeight")
    estimated_ship_by_date: Optional[datetime] = Field(default=None, description="Date on which the shipment is expected to be shipped. This value should not be in the past and not more than 60 days out in the future.", alias="estimatedShipByDate")
    handling_instructions: Optional[StrictStr] = Field(default=None, description="Identification of the instructions on how specified item/carton/pallet should be handled.", alias="handlingInstructions")
    __properties: ClassVar[List[str]] = ["methodOfPayment", "sealNumber", "route", "importContainers", "billableWeight", "estimatedShipByDate", "handlingInstructions"]

    @field_validator('method_of_payment')
    def method_of_payment_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PaidByBuyer', 'CollectOnDelivery', 'DefinedByBuyerAndSeller', 'FOBPortOfCall', 'PrepaidBySeller', 'PaidBySeller']):
            raise ValueError("must be one of enum values ('PaidByBuyer', 'CollectOnDelivery', 'DefinedByBuyerAndSeller', 'FOBPortOfCall', 'PrepaidBySeller', 'PaidBySeller')")
        return value

    @field_validator('handling_instructions')
    def handling_instructions_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Oversized', 'Fragile', 'Food', 'HandleWithCare']):
            raise ValueError("must be one of enum values ('Oversized', 'Fragile', 'Food', 'HandleWithCare')")
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
        """Create an instance of ImportDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of route
        if self.route:
            _dict['route'] = self.route.to_dict()
        # override the default output from pydantic by calling `to_dict()` of billable_weight
        if self.billable_weight:
            _dict['billableWeight'] = self.billable_weight.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ImportDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "methodOfPayment": obj.get("methodOfPayment"),
            "sealNumber": obj.get("sealNumber"),
            "route": Route.from_dict(obj["route"]) if obj.get("route") is not None else None,
            "importContainers": obj.get("importContainers"),
            "billableWeight": Weight.from_dict(obj["billableWeight"]) if obj.get("billableWeight") is not None else None,
            "estimatedShipByDate": obj.get("estimatedShipByDate"),
            "handlingInstructions": obj.get("handlingInstructions")
        })
        return _obj


