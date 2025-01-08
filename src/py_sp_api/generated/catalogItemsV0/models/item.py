# coding: utf-8

"""
    Selling Partner API for Catalog Items

    The Selling Partner API for Catalog Items helps you programmatically retrieve item details for items in the catalog.

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
from py_sp_api.generated.catalogItemsV0.models.attribute_set_list_type import AttributeSetListType
from py_sp_api.generated.catalogItemsV0.models.identifier_type import IdentifierType
from py_sp_api.generated.catalogItemsV0.models.relationship_type import RelationshipType
from py_sp_api.generated.catalogItemsV0.models.sales_rank_type import SalesRankType
from typing import Optional, Set
from typing_extensions import Self

class Item(BaseModel):
    """
    An item in the Amazon catalog.
    """ # noqa: E501
    identifiers: IdentifierType = Field(alias="Identifiers")
    attribute_sets: Optional[List[AttributeSetListType]] = Field(default=None, description="A list of attributes for the item.", alias="AttributeSets")
    relationships: Optional[List[RelationshipType]] = Field(default=None, description="A list of variation relationship information, if applicable for the item.", alias="Relationships")
    sales_rankings: Optional[List[SalesRankType]] = Field(default=None, description="A list of sales rank information for the item by category.", alias="SalesRankings")
    __properties: ClassVar[List[str]] = ["Identifiers", "AttributeSets", "Relationships", "SalesRankings"]

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
        # override the default output from pydantic by calling `to_dict()` of identifiers
        if self.identifiers:
            _dict['Identifiers'] = self.identifiers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in attribute_sets (list)
        _items = []
        if self.attribute_sets:
            for _item_attribute_sets in self.attribute_sets:
                if _item_attribute_sets:
                    _items.append(_item_attribute_sets.to_dict())
            _dict['AttributeSets'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in relationships (list)
        _items = []
        if self.relationships:
            for _item_relationships in self.relationships:
                if _item_relationships:
                    _items.append(_item_relationships.to_dict())
            _dict['Relationships'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sales_rankings (list)
        _items = []
        if self.sales_rankings:
            for _item_sales_rankings in self.sales_rankings:
                if _item_sales_rankings:
                    _items.append(_item_sales_rankings.to_dict())
            _dict['SalesRankings'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Item from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Identifiers": IdentifierType.from_dict(obj["Identifiers"]) if obj.get("Identifiers") is not None else None,
            "AttributeSets": [AttributeSetListType.from_dict(_item) for _item in obj["AttributeSets"]] if obj.get("AttributeSets") is not None else None,
            "Relationships": [RelationshipType.from_dict(_item) for _item in obj["Relationships"]] if obj.get("Relationships") is not None else None,
            "SalesRankings": [SalesRankType.from_dict(_item) for _item in obj["SalesRankings"]] if obj.get("SalesRankings") is not None else None
        })
        return _obj


