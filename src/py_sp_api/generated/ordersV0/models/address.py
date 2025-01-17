# coding: utf-8

"""
    Orders v0

    Use the Orders Selling Partner API to programmatically retrieve order information. With this API, you can develop fast, flexible, and custom applications to manage order synchronization, perform order research, and create demand-based decision support tools.   _Note:_ For the JP, AU, and SG marketplaces, the Orders API supports orders from 2016 onward. For all other marketplaces, the Orders API supports orders for the last two years (orders older than this don't show up in the response).

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.ordersV0.models.address_extended_fields import AddressExtendedFields
from typing import Optional, Set
from typing_extensions import Self

class Address(BaseModel):
    """
    The shipping address for the order.
    """ # noqa: E501
    name: StrictStr = Field(description="The name.", alias="Name")
    company_name: Optional[StrictStr] = Field(default=None, description="The company name of the recipient.  **Note**: This attribute is only available for shipping address.", alias="CompanyName")
    address_line1: Optional[StrictStr] = Field(default=None, description="The street address.", alias="AddressLine1")
    address_line2: Optional[StrictStr] = Field(default=None, description="Additional street address information, if required.", alias="AddressLine2")
    address_line3: Optional[StrictStr] = Field(default=None, description="Additional street address information, if required.", alias="AddressLine3")
    city: Optional[StrictStr] = Field(default=None, description="The city.", alias="City")
    county: Optional[StrictStr] = Field(default=None, description="The county.", alias="County")
    district: Optional[StrictStr] = Field(default=None, description="The district.", alias="District")
    state_or_region: Optional[StrictStr] = Field(default=None, description="The state or region.", alias="StateOrRegion")
    municipality: Optional[StrictStr] = Field(default=None, description="The municipality.", alias="Municipality")
    postal_code: Optional[StrictStr] = Field(default=None, description="The postal code.", alias="PostalCode")
    country_code: Optional[StrictStr] = Field(default=None, description="The country code. A two-character country code, in ISO 3166-1 alpha-2 format.", alias="CountryCode")
    phone: Optional[StrictStr] = Field(default=None, description="The phone number of the buyer.  **Note**:  1. This attribute is only available for shipping address. 2. In some cases, the buyer phone number is suppressed:  a. Phone is suppressed for all `AFN` (fulfilled by Amazon) orders. b. Phone is suppressed for the shipped `MFN` (fulfilled by seller) order when the current date is past the Latest Delivery Date.", alias="Phone")
    extended_fields: Optional[AddressExtendedFields] = Field(default=None, alias="ExtendedFields")
    address_type: Optional[StrictStr] = Field(default=None, description="The address type of the shipping address.", alias="AddressType")
    __properties: ClassVar[List[str]] = ["Name", "CompanyName", "AddressLine1", "AddressLine2", "AddressLine3", "City", "County", "District", "StateOrRegion", "Municipality", "PostalCode", "CountryCode", "Phone", "ExtendedFields", "AddressType"]

    @field_validator('address_type')
    def address_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Residential', 'Commercial']):
            raise ValueError("must be one of enum values ('Residential', 'Commercial')")
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
        # override the default output from pydantic by calling `to_dict()` of extended_fields
        if self.extended_fields:
            _dict['ExtendedFields'] = self.extended_fields.to_dict()
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
            "CompanyName": obj.get("CompanyName"),
            "AddressLine1": obj.get("AddressLine1"),
            "AddressLine2": obj.get("AddressLine2"),
            "AddressLine3": obj.get("AddressLine3"),
            "City": obj.get("City"),
            "County": obj.get("County"),
            "District": obj.get("District"),
            "StateOrRegion": obj.get("StateOrRegion"),
            "Municipality": obj.get("Municipality"),
            "PostalCode": obj.get("PostalCode"),
            "CountryCode": obj.get("CountryCode"),
            "Phone": obj.get("Phone"),
            "ExtendedFields": AddressExtendedFields.from_dict(obj["ExtendedFields"]) if obj.get("ExtendedFields") is not None else None,
            "AddressType": obj.get("AddressType")
        })
        return _obj


