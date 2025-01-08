# coding: utf-8

"""
    Selling Partner API for Shipping

    Provides programmatic access to Amazon Shipping APIs.   **Note:** If you are new to the Amazon Shipping API, refer to the latest version of <a href=\"https://developer-docs.amazon.com/amazon-shipping/docs/shipping-api-v2-reference\">Amazon Shipping API (v2)</a> on the <a href=\"https://developer-docs.amazon.com/amazon-shipping/\">Amazon Shipping Developer Documentation</a> site.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from py_sp_api.generated.shipping.models.address import Address
from py_sp_api.generated.shipping.models.container import Container
from py_sp_api.generated.shipping.models.label_specification import LabelSpecification
from py_sp_api.generated.shipping.models.service_type import ServiceType
from typing import Optional, Set
from typing_extensions import Self

class PurchaseShipmentRequest(BaseModel):
    """
    The payload schema for the purchaseShipment operation.
    """ # noqa: E501
    client_reference_id: Annotated[str, Field(strict=True, max_length=40)] = Field(description="Client reference id.", alias="clientReferenceId")
    ship_to: Address = Field(alias="shipTo")
    ship_from: Address = Field(alias="shipFrom")
    ship_date: Optional[datetime] = Field(default=None, description="The start date and time. This defaults to the current date and time.", alias="shipDate")
    service_type: ServiceType = Field(alias="serviceType")
    containers: List[Container] = Field(description="A list of container.")
    label_specification: LabelSpecification = Field(alias="labelSpecification")
    __properties: ClassVar[List[str]] = ["clientReferenceId", "shipTo", "shipFrom", "shipDate", "serviceType", "containers", "labelSpecification"]

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
        """Create an instance of PurchaseShipmentRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ship_to
        if self.ship_to:
            _dict['shipTo'] = self.ship_to.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ship_from
        if self.ship_from:
            _dict['shipFrom'] = self.ship_from.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in containers (list)
        _items = []
        if self.containers:
            for _item_containers in self.containers:
                if _item_containers:
                    _items.append(_item_containers.to_dict())
            _dict['containers'] = _items
        # override the default output from pydantic by calling `to_dict()` of label_specification
        if self.label_specification:
            _dict['labelSpecification'] = self.label_specification.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PurchaseShipmentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clientReferenceId": obj.get("clientReferenceId"),
            "shipTo": Address.from_dict(obj["shipTo"]) if obj.get("shipTo") is not None else None,
            "shipFrom": Address.from_dict(obj["shipFrom"]) if obj.get("shipFrom") is not None else None,
            "shipDate": obj.get("shipDate"),
            "serviceType": obj.get("serviceType"),
            "containers": [Container.from_dict(_item) for _item in obj["containers"]] if obj.get("containers") is not None else None,
            "labelSpecification": LabelSpecification.from_dict(obj["labelSpecification"]) if obj.get("labelSpecification") is not None else None
        })
        return _obj


