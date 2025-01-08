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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List
from py_sp_api.generated.catalogItems_2020_12_01.models.item import Item
from py_sp_api.generated.catalogItems_2020_12_01.models.pagination import Pagination
from py_sp_api.generated.catalogItems_2020_12_01.models.refinements import Refinements
from typing import Optional, Set
from typing_extensions import Self

class ItemSearchResults(BaseModel):
    """
    Items in the Amazon catalog and search related metadata.
    """ # noqa: E501
    number_of_results: StrictInt = Field(description="The estimated total number of products matched by the search query (only results up to the page count limit will be returned per request regardless of the number found).  Note: The maximum number of items (ASINs) that can be returned and paged through is 1000.", alias="numberOfResults")
    pagination: Pagination
    refinements: Refinements
    items: List[Item] = Field(description="A list of items from the Amazon catalog.")
    __properties: ClassVar[List[str]] = ["numberOfResults", "pagination", "refinements", "items"]

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
        """Create an instance of ItemSearchResults from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of pagination
        if self.pagination:
            _dict['pagination'] = self.pagination.to_dict()
        # override the default output from pydantic by calling `to_dict()` of refinements
        if self.refinements:
            _dict['refinements'] = self.refinements.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item_items in self.items:
                if _item_items:
                    _items.append(_item_items.to_dict())
            _dict['items'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ItemSearchResults from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "numberOfResults": obj.get("numberOfResults"),
            "pagination": Pagination.from_dict(obj["pagination"]) if obj.get("pagination") is not None else None,
            "refinements": Refinements.from_dict(obj["refinements"]) if obj.get("refinements") is not None else None,
            "items": [Item.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None
        })
        return _obj


