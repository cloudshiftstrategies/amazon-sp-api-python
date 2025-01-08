# coding: utf-8

"""
    Selling Partner API for Data Kiosk

    The Selling Partner API for Data Kiosk lets you submit GraphQL queries from a variety of schemas to help selling partners manage their businesses.

    The version of the OpenAPI document: 2023-11-15
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.dataKiosk_2023_11_15.models.get_queries_response_pagination import GetQueriesResponsePagination
from py_sp_api.generated.dataKiosk_2023_11_15.models.query import Query
from typing import Optional, Set
from typing_extensions import Self

class GetQueriesResponse(BaseModel):
    """
    The response for the `getQueries` operation.
    """ # noqa: E501
    queries: List[Query] = Field(description="A list of queries.")
    pagination: Optional[GetQueriesResponsePagination] = None
    __properties: ClassVar[List[str]] = ["queries", "pagination"]

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
        """Create an instance of GetQueriesResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in queries (list)
        _items = []
        if self.queries:
            for _item_queries in self.queries:
                if _item_queries:
                    _items.append(_item_queries.to_dict())
            _dict['queries'] = _items
        # override the default output from pydantic by calling `to_dict()` of pagination
        if self.pagination:
            _dict['pagination'] = self.pagination.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetQueriesResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "queries": [Query.from_dict(_item) for _item in obj["queries"]] if obj.get("queries") is not None else None,
            "pagination": GetQueriesResponsePagination.from_dict(obj["pagination"]) if obj.get("pagination") is not None else None
        })
        return _obj


