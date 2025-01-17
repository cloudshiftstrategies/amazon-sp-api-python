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
from py_sp_api.generated.shippingV2.models.value_added_service import ValueAddedService
from typing import Optional, Set
from typing_extensions import Self

class AvailableValueAddedServiceGroup(BaseModel):
    """
    The value-added services available for purchase with a shipping service offering.
    """ # noqa: E501
    group_id: StrictStr = Field(description="The type of the value-added service group.", alias="groupId")
    group_description: StrictStr = Field(description="The name of the value-added service group.", alias="groupDescription")
    is_required: StrictBool = Field(description="When true, one or more of the value-added services listed must be specified.", alias="isRequired")
    value_added_services: Optional[List[ValueAddedService]] = Field(default=None, description="A list of optional value-added services available for purchase with a shipping service offering.", alias="valueAddedServices")
    __properties: ClassVar[List[str]] = ["groupId", "groupDescription", "isRequired", "valueAddedServices"]

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
        """Create an instance of AvailableValueAddedServiceGroup from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in value_added_services (list)
        _items = []
        if self.value_added_services:
            for _item_value_added_services in self.value_added_services:
                if _item_value_added_services:
                    _items.append(_item_value_added_services.to_dict())
            _dict['valueAddedServices'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AvailableValueAddedServiceGroup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "groupId": obj.get("groupId"),
            "groupDescription": obj.get("groupDescription"),
            "isRequired": obj.get("isRequired"),
            "valueAddedServices": [ValueAddedService.from_dict(_item) for _item in obj["valueAddedServices"]] if obj.get("valueAddedServices") is not None else None
        })
        return _obj


