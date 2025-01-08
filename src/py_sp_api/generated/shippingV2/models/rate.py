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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.shippingV2.models.available_value_added_service_group import AvailableValueAddedServiceGroup
from py_sp_api.generated.shippingV2.models.benefits import Benefits
from py_sp_api.generated.shippingV2.models.currency import Currency
from py_sp_api.generated.shippingV2.models.payment_type import PaymentType
from py_sp_api.generated.shippingV2.models.promise import Promise
from py_sp_api.generated.shippingV2.models.rate_item import RateItem
from py_sp_api.generated.shippingV2.models.supported_document_specification import SupportedDocumentSpecification
from py_sp_api.generated.shippingV2.models.weight import Weight
from typing import Optional, Set
from typing_extensions import Self

class Rate(BaseModel):
    """
    The details of a shipping service offering.
    """ # noqa: E501
    rate_id: StrictStr = Field(description="An identifier for the rate (shipment offering) provided by a shipping service provider.", alias="rateId")
    carrier_id: StrictStr = Field(description="The carrier identifier for the offering, provided by the carrier.", alias="carrierId")
    carrier_name: StrictStr = Field(description="The carrier name for the offering.", alias="carrierName")
    service_id: StrictStr = Field(description="An identifier for the shipping service.", alias="serviceId")
    service_name: StrictStr = Field(description="The name of the shipping service.", alias="serviceName")
    billed_weight: Optional[Weight] = Field(default=None, alias="billedWeight")
    total_charge: Currency = Field(alias="totalCharge")
    promise: Promise
    supported_document_specifications: List[SupportedDocumentSpecification] = Field(description="A list of the document specifications supported for a shipment service offering.", alias="supportedDocumentSpecifications")
    available_value_added_service_groups: Optional[List[AvailableValueAddedServiceGroup]] = Field(default=None, description="A list of value-added services available for a shipping service offering.", alias="availableValueAddedServiceGroups")
    requires_additional_inputs: StrictBool = Field(description="When true, indicates that additional inputs are required to purchase this shipment service. You must then call the getAdditionalInputs operation to return the JSON schema to use when providing the additional inputs to the purchaseShipment operation.", alias="requiresAdditionalInputs")
    rate_item_list: Optional[List[RateItem]] = Field(default=None, description="A list of RateItem", alias="rateItemList")
    payment_type: Optional[PaymentType] = Field(default=None, alias="paymentType")
    benefits: Optional[Benefits] = None
    __properties: ClassVar[List[str]] = ["rateId", "carrierId", "carrierName", "serviceId", "serviceName", "billedWeight", "totalCharge", "promise", "supportedDocumentSpecifications", "availableValueAddedServiceGroups", "requiresAdditionalInputs", "rateItemList", "paymentType", "benefits"]

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
        """Create an instance of Rate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of billed_weight
        if self.billed_weight:
            _dict['billedWeight'] = self.billed_weight.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total_charge
        if self.total_charge:
            _dict['totalCharge'] = self.total_charge.to_dict()
        # override the default output from pydantic by calling `to_dict()` of promise
        if self.promise:
            _dict['promise'] = self.promise.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in supported_document_specifications (list)
        _items = []
        if self.supported_document_specifications:
            for _item_supported_document_specifications in self.supported_document_specifications:
                if _item_supported_document_specifications:
                    _items.append(_item_supported_document_specifications.to_dict())
            _dict['supportedDocumentSpecifications'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in available_value_added_service_groups (list)
        _items = []
        if self.available_value_added_service_groups:
            for _item_available_value_added_service_groups in self.available_value_added_service_groups:
                if _item_available_value_added_service_groups:
                    _items.append(_item_available_value_added_service_groups.to_dict())
            _dict['availableValueAddedServiceGroups'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in rate_item_list (list)
        _items = []
        if self.rate_item_list:
            for _item_rate_item_list in self.rate_item_list:
                if _item_rate_item_list:
                    _items.append(_item_rate_item_list.to_dict())
            _dict['rateItemList'] = _items
        # override the default output from pydantic by calling `to_dict()` of benefits
        if self.benefits:
            _dict['benefits'] = self.benefits.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Rate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "rateId": obj.get("rateId"),
            "carrierId": obj.get("carrierId"),
            "carrierName": obj.get("carrierName"),
            "serviceId": obj.get("serviceId"),
            "serviceName": obj.get("serviceName"),
            "billedWeight": Weight.from_dict(obj["billedWeight"]) if obj.get("billedWeight") is not None else None,
            "totalCharge": Currency.from_dict(obj["totalCharge"]) if obj.get("totalCharge") is not None else None,
            "promise": Promise.from_dict(obj["promise"]) if obj.get("promise") is not None else None,
            "supportedDocumentSpecifications": [SupportedDocumentSpecification.from_dict(_item) for _item in obj["supportedDocumentSpecifications"]] if obj.get("supportedDocumentSpecifications") is not None else None,
            "availableValueAddedServiceGroups": [AvailableValueAddedServiceGroup.from_dict(_item) for _item in obj["availableValueAddedServiceGroups"]] if obj.get("availableValueAddedServiceGroups") is not None else None,
            "requiresAdditionalInputs": obj.get("requiresAdditionalInputs"),
            "rateItemList": [RateItem.from_dict(_item) for _item in obj["rateItemList"]] if obj.get("rateItemList") is not None else None,
            "paymentType": obj.get("paymentType"),
            "benefits": Benefits.from_dict(obj["benefits"]) if obj.get("benefits") is not None else None
        })
        return _obj


