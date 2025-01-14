# coding: utf-8

"""
    Selling Partner API for Easy Ship

    The Selling Partner API for Easy Ship helps you build applications that help sellers manage and ship Amazon Easy Ship orders.  Your Easy Ship applications can:  * Get available time slots for packages to be scheduled for delivery.  * Schedule, reschedule, and cancel Easy Ship orders.  * Print labels, invoices, and warranties.  See the [Marketplace Support Table](doc:easyship-api-v2022-03-23-use-case-guide#marketplace-support-table) for the differences in Easy Ship operations by marketplace.

    The version of the OpenAPI document: 2022-03-23
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from py_sp_api.generated.easyShip_2022_03_23.models.update_package_details import UpdatePackageDetails
from typing import Optional, Set
from typing_extensions import Self

class UpdateScheduledPackagesRequest(BaseModel):
    """
    The request schema for the `updateScheduledPackages` operation.
    """ # noqa: E501
    marketplace_id: Annotated[str, Field(min_length=1, strict=True, max_length=255)] = Field(description="A string of up to 255 characters.", alias="marketplaceId")
    update_package_details_list: Annotated[List[UpdatePackageDetails], Field(min_length=1, max_length=500)] = Field(description="A list of package update details.", alias="updatePackageDetailsList")
    __properties: ClassVar[List[str]] = ["marketplaceId", "updatePackageDetailsList"]

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
        """Create an instance of UpdateScheduledPackagesRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in update_package_details_list (list)
        _items = []
        if self.update_package_details_list:
            for _item_update_package_details_list in self.update_package_details_list:
                if _item_update_package_details_list:
                    _items.append(_item_update_package_details_list.to_dict())
            _dict['updatePackageDetailsList'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateScheduledPackagesRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "marketplaceId": obj.get("marketplaceId"),
            "updatePackageDetailsList": [UpdatePackageDetails.from_dict(_item) for _item in obj["updatePackageDetailsList"]] if obj.get("updatePackageDetailsList") is not None else None
        })
        return _obj


