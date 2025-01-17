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
from typing import Any, ClassVar, Dict, List
from py_sp_api.generated.shippingV2.models.carrier import Carrier
from py_sp_api.generated.shippingV2.models.currency import Currency
from py_sp_api.generated.shippingV2.models.package_document_detail import PackageDocumentDetail
from py_sp_api.generated.shippingV2.models.promise import Promise
from py_sp_api.generated.shippingV2.models.service import Service
from typing import Optional, Set
from typing_extensions import Self

class OneClickShipmentResult(BaseModel):
    """
    The payload for the OneClickShipment API.
    """ # noqa: E501
    shipment_id: StrictStr = Field(description="The unique shipment identifier provided by a shipping service.", alias="shipmentId")
    package_document_details: List[PackageDocumentDetail] = Field(description="A list of post-purchase details about a package that will be shipped using a shipping service.", alias="packageDocumentDetails")
    promise: Promise
    carrier: Carrier
    service: Service
    total_charge: Currency = Field(alias="totalCharge")
    __properties: ClassVar[List[str]] = ["shipmentId", "packageDocumentDetails", "promise", "carrier", "service", "totalCharge"]

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
        """Create an instance of OneClickShipmentResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in package_document_details (list)
        _items = []
        if self.package_document_details:
            for _item_package_document_details in self.package_document_details:
                if _item_package_document_details:
                    _items.append(_item_package_document_details.to_dict())
            _dict['packageDocumentDetails'] = _items
        # override the default output from pydantic by calling `to_dict()` of promise
        if self.promise:
            _dict['promise'] = self.promise.to_dict()
        # override the default output from pydantic by calling `to_dict()` of carrier
        if self.carrier:
            _dict['carrier'] = self.carrier.to_dict()
        # override the default output from pydantic by calling `to_dict()` of service
        if self.service:
            _dict['service'] = self.service.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total_charge
        if self.total_charge:
            _dict['totalCharge'] = self.total_charge.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OneClickShipmentResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "shipmentId": obj.get("shipmentId"),
            "packageDocumentDetails": [PackageDocumentDetail.from_dict(_item) for _item in obj["packageDocumentDetails"]] if obj.get("packageDocumentDetails") is not None else None,
            "promise": Promise.from_dict(obj["promise"]) if obj.get("promise") is not None else None,
            "carrier": Carrier.from_dict(obj["carrier"]) if obj.get("carrier") is not None else None,
            "service": Service.from_dict(obj["service"]) if obj.get("service") is not None else None,
            "totalCharge": Currency.from_dict(obj["totalCharge"]) if obj.get("totalCharge") is not None else None
        })
        return _obj


