# coding: utf-8

"""
    Catalog Items v2022-04-01

    The Selling Partner API for Catalog Items provides programmatic access to information about items in the Amazon catalog.  For more information, refer to the [Catalog Items API Use Case Guide](doc:catalog-items-api-v2022-04-01-use-case-guide).

    The version of the OpenAPI document: 2022-04-01
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.catalogItems_2022_04_01.models.item_browse_classification import ItemBrowseClassification
from py_sp_api.generated.catalogItems_2022_04_01.models.item_contributor import ItemContributor
from typing import Optional, Set
from typing_extensions import Self

class ItemSummaryByMarketplace(BaseModel):
    """
    Summary details of an Amazon catalog item for the indicated Amazon marketplace.
    """ # noqa: E501
    marketplace_id: StrictStr = Field(description="Amazon marketplace identifier.", alias="marketplaceId")
    adult_product: Optional[StrictBool] = Field(default=None, description="Identifies an Amazon catalog item is intended for an adult audience or is sexual in nature.", alias="adultProduct")
    autographed: Optional[StrictBool] = Field(default=None, description="Identifies an Amazon catalog item is autographed by a player or celebrity.")
    brand: Optional[StrictStr] = Field(default=None, description="Name of the brand associated with an Amazon catalog item.")
    browse_classification: Optional[ItemBrowseClassification] = Field(default=None, alias="browseClassification")
    color: Optional[StrictStr] = Field(default=None, description="Name of the color associated with an Amazon catalog item.")
    contributors: Optional[List[ItemContributor]] = Field(default=None, description="Individual contributors to the creation of an item, such as the authors or actors.")
    item_classification: Optional[StrictStr] = Field(default=None, description="Classification type associated with the Amazon catalog item.", alias="itemClassification")
    item_name: Optional[StrictStr] = Field(default=None, description="Name, or title, associated with an Amazon catalog item.", alias="itemName")
    manufacturer: Optional[StrictStr] = Field(default=None, description="Name of the manufacturer associated with an Amazon catalog item.")
    memorabilia: Optional[StrictBool] = Field(default=None, description="Identifies an Amazon catalog item is memorabilia valued for its connection with historical events, culture, or entertainment.")
    model_number: Optional[StrictStr] = Field(default=None, description="Model number associated with an Amazon catalog item.", alias="modelNumber")
    package_quantity: Optional[StrictInt] = Field(default=None, description="Quantity of an Amazon catalog item in one package.", alias="packageQuantity")
    part_number: Optional[StrictStr] = Field(default=None, description="Part number associated with an Amazon catalog item.", alias="partNumber")
    release_date: Optional[date] = Field(default=None, description="First date on which an Amazon catalog item is shippable to customers.", alias="releaseDate")
    size: Optional[StrictStr] = Field(default=None, description="Name of the size associated with an Amazon catalog item.")
    style: Optional[StrictStr] = Field(default=None, description="Name of the style associated with an Amazon catalog item.")
    trade_in_eligible: Optional[StrictBool] = Field(default=None, description="Identifies an Amazon catalog item is eligible for trade-in.", alias="tradeInEligible")
    website_display_group: Optional[StrictStr] = Field(default=None, description="Identifier of the website display group associated with an Amazon catalog item.", alias="websiteDisplayGroup")
    website_display_group_name: Optional[StrictStr] = Field(default=None, description="Display name of the website display group associated with an Amazon catalog item.", alias="websiteDisplayGroupName")
    __properties: ClassVar[List[str]] = ["marketplaceId", "adultProduct", "autographed", "brand", "browseClassification", "color", "contributors", "itemClassification", "itemName", "manufacturer", "memorabilia", "modelNumber", "packageQuantity", "partNumber", "releaseDate", "size", "style", "tradeInEligible", "websiteDisplayGroup", "websiteDisplayGroupName"]

    @field_validator('item_classification')
    def item_classification_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['BASE_PRODUCT', 'OTHER', 'PRODUCT_BUNDLE', 'VARIATION_PARENT']):
            raise ValueError("must be one of enum values ('BASE_PRODUCT', 'OTHER', 'PRODUCT_BUNDLE', 'VARIATION_PARENT')")
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
        # override the default output from pydantic by calling `to_dict()` of browse_classification
        if self.browse_classification:
            _dict['browseClassification'] = self.browse_classification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in contributors (list)
        _items = []
        if self.contributors:
            for _item_contributors in self.contributors:
                if _item_contributors:
                    _items.append(_item_contributors.to_dict())
            _dict['contributors'] = _items
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
            "adultProduct": obj.get("adultProduct"),
            "autographed": obj.get("autographed"),
            "brand": obj.get("brand"),
            "browseClassification": ItemBrowseClassification.from_dict(obj["browseClassification"]) if obj.get("browseClassification") is not None else None,
            "color": obj.get("color"),
            "contributors": [ItemContributor.from_dict(_item) for _item in obj["contributors"]] if obj.get("contributors") is not None else None,
            "itemClassification": obj.get("itemClassification"),
            "itemName": obj.get("itemName"),
            "manufacturer": obj.get("manufacturer"),
            "memorabilia": obj.get("memorabilia"),
            "modelNumber": obj.get("modelNumber"),
            "packageQuantity": obj.get("packageQuantity"),
            "partNumber": obj.get("partNumber"),
            "releaseDate": obj.get("releaseDate"),
            "size": obj.get("size"),
            "style": obj.get("style"),
            "tradeInEligible": obj.get("tradeInEligible"),
            "websiteDisplayGroup": obj.get("websiteDisplayGroup"),
            "websiteDisplayGroupName": obj.get("websiteDisplayGroupName")
        })
        return _obj


