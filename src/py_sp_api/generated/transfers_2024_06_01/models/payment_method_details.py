# coding: utf-8

"""
    The Selling Partner API for Transfers.

    The Selling Partner API for Transfers enables selling partners to retrieve payment methods and initiate payouts for their seller accounts. This API supports the following marketplaces: DE, FR, IT, ES, SE, NL, PL, and BE.

    The version of the OpenAPI document: 2024-06-01
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.transfers_2024_06_01.models.assignment_type import AssignmentType
from py_sp_api.generated.transfers_2024_06_01.models.expiry_date import ExpiryDate
from py_sp_api.generated.transfers_2024_06_01.models.payment_method_type import PaymentMethodType
from typing import Optional, Set
from typing_extensions import Self

class PaymentMethodDetails(BaseModel):
    """
    The details of a payment method.
    """ # noqa: E501
    account_holder_name: Optional[StrictStr] = Field(default=None, description="The name of the account holder who is registered for the payment method.", alias="accountHolderName")
    payment_method_id: Optional[StrictStr] = Field(default=None, description="The payment method identifier.", alias="paymentMethodId")
    tail: Optional[StrictStr] = Field(default=None, description="The last three or four digits of the payment method.")
    expiry_date: Optional[ExpiryDate] = Field(default=None, alias="expiryDate")
    country_code: Optional[StrictStr] = Field(default=None, description="The two-letter country code in ISO 3166-1 alpha-2 format. For payment methods in the `card` category, the code is for the country where the card was issued. For payment methods in the `bank account` category, the code is for the country where the account is located.", alias="countryCode")
    payment_method_type: Optional[PaymentMethodType] = Field(default=None, alias="paymentMethodType")
    assignment_type: Optional[AssignmentType] = Field(default=None, alias="assignmentType")
    __properties: ClassVar[List[str]] = ["accountHolderName", "paymentMethodId", "tail", "expiryDate", "countryCode", "paymentMethodType", "assignmentType"]

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
        """Create an instance of PaymentMethodDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of expiry_date
        if self.expiry_date:
            _dict['expiryDate'] = self.expiry_date.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentMethodDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountHolderName": obj.get("accountHolderName"),
            "paymentMethodId": obj.get("paymentMethodId"),
            "tail": obj.get("tail"),
            "expiryDate": ExpiryDate.from_dict(obj["expiryDate"]) if obj.get("expiryDate") is not None else None,
            "countryCode": obj.get("countryCode"),
            "paymentMethodType": obj.get("paymentMethodType"),
            "assignmentType": obj.get("assignmentType")
        })
        return _obj


