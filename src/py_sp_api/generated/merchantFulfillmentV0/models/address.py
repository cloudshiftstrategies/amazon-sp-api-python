# coding: utf-8

"""
    Selling Partner API for Merchant Fulfillment

    With the Selling Partner API for Merchant Fulfillment, you can build applications that sellers can use to purchase shipping for non-Prime and Prime orders using Amazon's Buy Shipping Services.

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Address(BaseModel):
    """
    The postal address information.
    """ # noqa: E501
    name: Annotated[str, Field(strict=True, max_length=30)] = Field(description="The name of the addressee, or business name.", alias="Name")
    address_line1: Annotated[str, Field(strict=True, max_length=180)] = Field(description="The street address information.", alias="AddressLine1")
    address_line2: Optional[Annotated[str, Field(strict=True, max_length=60)]] = Field(default=None, description="Additional street address information.", alias="AddressLine2")
    address_line3: Optional[Annotated[str, Field(strict=True, max_length=60)]] = Field(default=None, description="Additional street address information.", alias="AddressLine3")
    district_or_county: Optional[StrictStr] = Field(default=None, description="The district or county.", alias="DistrictOrCounty")
    email: StrictStr = Field(description="The email address.", alias="Email")
    city: Annotated[str, Field(strict=True, max_length=30)] = Field(description="The city.", alias="City")
    state_or_province_code: Optional[Annotated[str, Field(strict=True, max_length=30)]] = Field(default=None, description="The state or province code. This is a required field in Canada, US, and UK marketplaces, and for shipments that originate in China.", alias="StateOrProvinceCode")
    postal_code: Annotated[str, Field(strict=True, max_length=30)] = Field(description="The zip code or postal code.", alias="PostalCode")
    country_code: StrictStr = Field(description="The two-letter country code in [ISO 3166-1 alpha-2](https://www.iban.com/country-codes) format.", alias="CountryCode")
    phone: Annotated[str, Field(strict=True, max_length=30)] = Field(description="The phone number.", alias="Phone")
    __properties: ClassVar[List[str]] = ["Name", "AddressLine1", "AddressLine2", "AddressLine3", "DistrictOrCounty", "Email", "City", "StateOrProvinceCode", "PostalCode", "CountryCode", "Phone"]

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
        """Create an instance of Address from a JSON string"""
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
        """Create an instance of Address from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Name": obj.get("Name"),
            "AddressLine1": obj.get("AddressLine1"),
            "AddressLine2": obj.get("AddressLine2"),
            "AddressLine3": obj.get("AddressLine3"),
            "DistrictOrCounty": obj.get("DistrictOrCounty"),
            "Email": obj.get("Email"),
            "City": obj.get("City"),
            "StateOrProvinceCode": obj.get("StateOrProvinceCode"),
            "PostalCode": obj.get("PostalCode"),
            "CountryCode": obj.get("CountryCode"),
            "Phone": obj.get("Phone")
        })
        return _obj


