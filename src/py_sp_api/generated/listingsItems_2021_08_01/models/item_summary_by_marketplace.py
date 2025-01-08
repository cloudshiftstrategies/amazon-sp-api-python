# coding: utf-8

"""
    Selling Partner API for Listings Items

    The Selling Partner API for Listings Items (Listings Items API) provides programmatic access to selling partner listings on Amazon. Use this API in collaboration with the Selling Partner API for Product Type Definitions, which you use to retrieve the information about Amazon product types needed to use the Listings Items API.  For more information, see the [Listings Items API Use Case Guide](https://developer-docs.amazon.com/sp-api/docs/listings-items-api-v2021-08-01-use-case-guide).

    The version of the OpenAPI document: 2021-08-01
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
from py_sp_api.generated.listingsItems_2021_08_01.models.item_image import ItemImage
from typing import Optional, Set
from typing_extensions import Self

class ItemSummaryByMarketplace(BaseModel):
    """
    Summary details of a listings item for an Amazon marketplace.
    """ # noqa: E501
    marketplace_id: StrictStr = Field(description="A marketplace identifier. Identifies the Amazon marketplace for the listings item.", alias="marketplaceId")
    asin: Optional[StrictStr] = Field(default=None, description="Amazon Standard Identification Number (ASIN) of the listings item.")
    product_type: StrictStr = Field(description="The Amazon product type of the listings item.", alias="productType")
    condition_type: Optional[StrictStr] = Field(default=None, description="Identifies the condition of the listings item.", alias="conditionType")
    status: List[StrictStr] = Field(description="Statuses that apply to the listings item.")
    fn_sku: Optional[StrictStr] = Field(default=None, description="The fulfillment network stock keeping unit is an identifier used by Amazon fulfillment centers to identify each unique item.", alias="fnSku")
    item_name: Optional[StrictStr] = Field(default=None, description="The name or title associated with an Amazon catalog item.", alias="itemName")
    created_date: datetime = Field(description="The date the listings item was created in ISO 8601 format.", alias="createdDate")
    last_updated_date: datetime = Field(description="The date the listings item was last updated in ISO 8601 format.", alias="lastUpdatedDate")
    main_image: Optional[ItemImage] = Field(default=None, alias="mainImage")
    __properties: ClassVar[List[str]] = ["marketplaceId", "asin", "productType", "conditionType", "status", "fnSku", "itemName", "createdDate", "lastUpdatedDate", "mainImage"]

    @field_validator('condition_type')
    def condition_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['new_new', 'new_open_box', 'new_oem', 'refurbished_refurbished', 'used_like_new', 'used_very_good', 'used_good', 'used_acceptable', 'collectible_like_new', 'collectible_very_good', 'collectible_good', 'collectible_acceptable', 'club_club']):
            raise ValueError("must be one of enum values ('new_new', 'new_open_box', 'new_oem', 'refurbished_refurbished', 'used_like_new', 'used_very_good', 'used_good', 'used_acceptable', 'collectible_like_new', 'collectible_very_good', 'collectible_good', 'collectible_acceptable', 'club_club')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in set(['BUYABLE', 'DISCOVERABLE']):
                raise ValueError("each list item must be one of ('BUYABLE', 'DISCOVERABLE')")
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
        # override the default output from pydantic by calling `to_dict()` of main_image
        if self.main_image:
            _dict['mainImage'] = self.main_image.to_dict()
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
            "asin": obj.get("asin"),
            "productType": obj.get("productType"),
            "conditionType": obj.get("conditionType"),
            "status": obj.get("status"),
            "fnSku": obj.get("fnSku"),
            "itemName": obj.get("itemName"),
            "createdDate": obj.get("createdDate"),
            "lastUpdatedDate": obj.get("lastUpdatedDate"),
            "mainImage": ItemImage.from_dict(obj["mainImage"]) if obj.get("mainImage") is not None else None
        })
        return _obj


