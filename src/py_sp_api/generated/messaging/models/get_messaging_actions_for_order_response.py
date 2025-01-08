# coding: utf-8

"""
    Selling Partner API for Messaging

    With the Messaging API you can build applications that send messages to buyers. You can get a list of message types that are available for an order that you specify, then call an operation that sends a message to the buyer for that order. The Messaging API returns responses that are formed according to the <a href=https://tools.ietf.org/html/draft-kelly-json-hal-08>JSON Hypertext Application Language</a> (HAL) standard.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.messaging.models.error import Error
from py_sp_api.generated.messaging.models.get_messaging_actions_for_order_response_embedded import GetMessagingActionsForOrderResponseEmbedded
from py_sp_api.generated.messaging.models.get_messaging_actions_for_order_response_links import GetMessagingActionsForOrderResponseLinks
from typing import Optional, Set
from typing_extensions import Self

class GetMessagingActionsForOrderResponse(BaseModel):
    """
    The response schema for the `getMessagingActionsForOrder` operation.
    """ # noqa: E501
    links: Optional[GetMessagingActionsForOrderResponseLinks] = Field(default=None, alias="_links")
    embedded: Optional[GetMessagingActionsForOrderResponseEmbedded] = Field(default=None, alias="_embedded")
    errors: Optional[List[Error]] = Field(default=None, description="A list of error responses returned when a request is unsuccessful.")
    __properties: ClassVar[List[str]] = ["_links", "_embedded", "errors"]

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
        """Create an instance of GetMessagingActionsForOrderResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of embedded
        if self.embedded:
            _dict['_embedded'] = self.embedded.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item_errors in self.errors:
                if _item_errors:
                    _items.append(_item_errors.to_dict())
            _dict['errors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetMessagingActionsForOrderResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_links": GetMessagingActionsForOrderResponseLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "_embedded": GetMessagingActionsForOrderResponseEmbedded.from_dict(obj["_embedded"]) if obj.get("_embedded") is not None else None,
            "errors": [Error.from_dict(_item) for _item in obj["errors"]] if obj.get("errors") is not None else None
        })
        return _obj


