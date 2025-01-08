# coding: utf-8

"""
    Selling Partner API for Merchant Fulfillment

    With the Selling Partner API for Merchant Fulfillment, you can build applications that sellers can use to purchase shipping for non-Prime and Prime orders using Amazon's Buy Shipping Services.

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.merchantFulfillmentV0.models.shipment_request_details import ShipmentRequestDetails
from py_sp_api.generated.merchantFulfillmentV0.models.shipping_offering_filter import ShippingOfferingFilter
from typing import Optional, Set
from typing_extensions import Self

class GetEligibleShipmentServicesRequest(BaseModel):
    """
    Request schema.
    """ # noqa: E501
    shipment_request_details: ShipmentRequestDetails = Field(alias="ShipmentRequestDetails")
    shipping_offering_filter: Optional[ShippingOfferingFilter] = Field(default=None, alias="ShippingOfferingFilter")
    __properties: ClassVar[List[str]] = ["ShipmentRequestDetails", "ShippingOfferingFilter"]

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
        """Create an instance of GetEligibleShipmentServicesRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of shipment_request_details
        if self.shipment_request_details:
            _dict['ShipmentRequestDetails'] = self.shipment_request_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipping_offering_filter
        if self.shipping_offering_filter:
            _dict['ShippingOfferingFilter'] = self.shipping_offering_filter.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetEligibleShipmentServicesRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ShipmentRequestDetails": ShipmentRequestDetails.from_dict(obj["ShipmentRequestDetails"]) if obj.get("ShipmentRequestDetails") is not None else None,
            "ShippingOfferingFilter": ShippingOfferingFilter.from_dict(obj["ShippingOfferingFilter"]) if obj.get("ShippingOfferingFilter") is not None else None
        })
        return _obj


