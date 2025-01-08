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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ListingsItemPutRequest(BaseModel):
    """
    The request body schema for the `putListingsItem` operation.
    """ # noqa: E501
    product_type: StrictStr = Field(description="The Amazon product type of the listings item.", alias="productType")
    requirements: Optional[StrictStr] = Field(default=None, description="The name of the requirements set for the provided data.")
    attributes: Dict[str, Any] = Field(description="A JSON object containing structured listings item attribute data keyed by attribute name.")
    __properties: ClassVar[List[str]] = ["productType", "requirements", "attributes"]

    @field_validator('requirements')
    def requirements_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['LISTING', 'LISTING_PRODUCT_ONLY', 'LISTING_OFFER_ONLY']):
            raise ValueError("must be one of enum values ('LISTING', 'LISTING_PRODUCT_ONLY', 'LISTING_OFFER_ONLY')")
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
        """Create an instance of ListingsItemPutRequest from a JSON string"""
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
        """Create an instance of ListingsItemPutRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "productType": obj.get("productType"),
            "requirements": obj.get("requirements"),
            "attributes": obj.get("attributes")
        })
        return _obj


