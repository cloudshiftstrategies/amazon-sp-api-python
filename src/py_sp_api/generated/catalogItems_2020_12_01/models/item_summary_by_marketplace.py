# coding: utf-8

"""
    Selling Partner API for Catalog Items

    The Selling Partner API for Catalog Items provides programmatic access to information about items in the Amazon catalog.  For more information, see the [Catalog Items API Use Case Guide](doc:catalog-items-api-v2020-12-01-use-case-guide).

    The version of the OpenAPI document: 2020-12-01
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ItemSummaryByMarketplace(BaseModel):
    """
    Summary details of an Amazon catalog item for the indicated Amazon marketplace.
    """ # noqa: E501
    marketplace_id: StrictStr = Field(description="Amazon marketplace identifier.", alias="marketplaceId")
    brand_name: Optional[StrictStr] = Field(default=None, description="Name of the brand associated with an Amazon catalog item.", alias="brandName")
    browse_node: Optional[StrictStr] = Field(default=None, description="Identifier of the browse node associated with an Amazon catalog item.", alias="browseNode")
    color_name: Optional[StrictStr] = Field(default=None, description="Name of the color associated with an Amazon catalog item.", alias="colorName")
    item_name: Optional[StrictStr] = Field(default=None, description="Name, or title, associated with an Amazon catalog item.", alias="itemName")
    manufacturer: Optional[StrictStr] = Field(default=None, description="Name of the manufacturer associated with an Amazon catalog item.")
    model_number: Optional[StrictStr] = Field(default=None, description="Model number associated with an Amazon catalog item.", alias="modelNumber")
    size_name: Optional[StrictStr] = Field(default=None, description="Name of the size associated with an Amazon catalog item.", alias="sizeName")
    style_name: Optional[StrictStr] = Field(default=None, description="Name of the style associated with an Amazon catalog item.", alias="styleName")
    __properties: ClassVar[List[str]] = ["marketplaceId", "brandName", "browseNode", "colorName", "itemName", "manufacturer", "modelNumber", "sizeName", "styleName"]

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
        """Create an instance of ItemSummaryByMarketplace from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ItemSummaryByMarketplace from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "marketplaceId": obj.get("marketplaceId"),
            "brandName": obj.get("brandName"),
            "browseNode": obj.get("browseNode"),
            "colorName": obj.get("colorName"),
            "itemName": obj.get("itemName"),
            "manufacturer": obj.get("manufacturer"),
            "modelNumber": obj.get("modelNumber"),
            "sizeName": obj.get("sizeName"),
            "styleName": obj.get("styleName")
        })
        return _obj


