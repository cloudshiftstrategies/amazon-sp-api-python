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
from py_sp_api.generated.catalogItems_2020_12_01.models.item_identifiers_by_marketplace import ItemIdentifiersByMarketplace
from py_sp_api.generated.catalogItems_2020_12_01.models.item_images_by_marketplace import ItemImagesByMarketplace
from py_sp_api.generated.catalogItems_2020_12_01.models.item_product_type_by_marketplace import ItemProductTypeByMarketplace
from py_sp_api.generated.catalogItems_2020_12_01.models.item_sales_ranks_by_marketplace import ItemSalesRanksByMarketplace
from py_sp_api.generated.catalogItems_2020_12_01.models.item_summary_by_marketplace import ItemSummaryByMarketplace
from py_sp_api.generated.catalogItems_2020_12_01.models.item_variations_by_marketplace import ItemVariationsByMarketplace
from py_sp_api.generated.catalogItems_2020_12_01.models.item_vendor_details_by_marketplace import ItemVendorDetailsByMarketplace
from typing import Optional, Set
from typing_extensions import Self

class Item(BaseModel):
    """
    An item in the Amazon catalog.
    """ # noqa: E501
    asin: StrictStr = Field(description="Amazon Standard Identification Number (ASIN) is the unique identifier for an item in the Amazon catalog.")
    attributes: Optional[Dict[str, Any]] = Field(default=None, description="A JSON object that contains structured item attribute data keyed by attribute name. Catalog item attributes are available only to brand owners and conform to the related product type definitions available in the Selling Partner API for Product Type Definitions.")
    identifiers: Optional[List[ItemIdentifiersByMarketplace]] = Field(default=None, description="Identifiers associated with the item in the Amazon catalog, such as UPC and EAN identifiers.")
    images: Optional[List[ItemImagesByMarketplace]] = Field(default=None, description="Images for an item in the Amazon catalog. All image variants are provided to brand owners. Otherwise, a thumbnail of the \"MAIN\" image variant is provided.")
    product_types: Optional[List[ItemProductTypeByMarketplace]] = Field(default=None, description="Product types associated with the Amazon catalog item.", alias="productTypes")
    sales_ranks: Optional[List[ItemSalesRanksByMarketplace]] = Field(default=None, description="Sales ranks of an Amazon catalog item.", alias="salesRanks")
    summaries: Optional[List[ItemSummaryByMarketplace]] = Field(default=None, description="Summary details of an Amazon catalog item.")
    variations: Optional[List[ItemVariationsByMarketplace]] = Field(default=None, description="Variation details by marketplace for an Amazon catalog item (variation relationships).")
    vendor_details: Optional[List[ItemVendorDetailsByMarketplace]] = Field(default=None, description="Vendor details associated with an Amazon catalog item. Vendor details are available to vendors only.", alias="vendorDetails")
    __properties: ClassVar[List[str]] = ["asin", "attributes", "identifiers", "images", "productTypes", "salesRanks", "summaries", "variations", "vendorDetails"]

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
        """Create an instance of Item from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in identifiers (list)
        _items = []
        if self.identifiers:
            for _item_identifiers in self.identifiers:
                if _item_identifiers:
                    _items.append(_item_identifiers.to_dict())
            _dict['identifiers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item_images in self.images:
                if _item_images:
                    _items.append(_item_images.to_dict())
            _dict['images'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in product_types (list)
        _items = []
        if self.product_types:
            for _item_product_types in self.product_types:
                if _item_product_types:
                    _items.append(_item_product_types.to_dict())
            _dict['productTypes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sales_ranks (list)
        _items = []
        if self.sales_ranks:
            for _item_sales_ranks in self.sales_ranks:
                if _item_sales_ranks:
                    _items.append(_item_sales_ranks.to_dict())
            _dict['salesRanks'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in summaries (list)
        _items = []
        if self.summaries:
            for _item_summaries in self.summaries:
                if _item_summaries:
                    _items.append(_item_summaries.to_dict())
            _dict['summaries'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in variations (list)
        _items = []
        if self.variations:
            for _item_variations in self.variations:
                if _item_variations:
                    _items.append(_item_variations.to_dict())
            _dict['variations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in vendor_details (list)
        _items = []
        if self.vendor_details:
            for _item_vendor_details in self.vendor_details:
                if _item_vendor_details:
                    _items.append(_item_vendor_details.to_dict())
            _dict['vendorDetails'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Item from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "asin": obj.get("asin"),
            "attributes": obj.get("attributes"),
            "identifiers": [ItemIdentifiersByMarketplace.from_dict(_item) for _item in obj["identifiers"]] if obj.get("identifiers") is not None else None,
            "images": [ItemImagesByMarketplace.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "productTypes": [ItemProductTypeByMarketplace.from_dict(_item) for _item in obj["productTypes"]] if obj.get("productTypes") is not None else None,
            "salesRanks": [ItemSalesRanksByMarketplace.from_dict(_item) for _item in obj["salesRanks"]] if obj.get("salesRanks") is not None else None,
            "summaries": [ItemSummaryByMarketplace.from_dict(_item) for _item in obj["summaries"]] if obj.get("summaries") is not None else None,
            "variations": [ItemVariationsByMarketplace.from_dict(_item) for _item in obj["variations"]] if obj.get("variations") is not None else None,
            "vendorDetails": [ItemVendorDetailsByMarketplace.from_dict(_item) for _item in obj["vendorDetails"]] if obj.get("vendorDetails") is not None else None
        })
        return _obj


