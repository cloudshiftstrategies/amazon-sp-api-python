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
from typing import Any, ClassVar, Dict, List
from py_sp_api.generated.catalogItems_2020_12_01.models.item_identifier import ItemIdentifier
from typing import Optional, Set
from typing_extensions import Self

class ItemIdentifiersByMarketplace(BaseModel):
    """
    Identifiers associated with the item in the Amazon catalog for the indicated Amazon marketplace.
    """ # noqa: E501
    marketplace_id: StrictStr = Field(description="Amazon marketplace identifier.", alias="marketplaceId")
    identifiers: List[ItemIdentifier] = Field(description="Identifiers associated with the item in the Amazon catalog for the indicated Amazon marketplace.")
    __properties: ClassVar[List[str]] = ["marketplaceId", "identifiers"]

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
        """Create an instance of ItemIdentifiersByMarketplace from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ItemIdentifiersByMarketplace from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "marketplaceId": obj.get("marketplaceId"),
            "identifiers": [ItemIdentifier.from_dict(_item) for _item in obj["identifiers"]] if obj.get("identifiers") is not None else None
        })
        return _obj


