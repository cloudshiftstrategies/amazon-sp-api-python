# coding: utf-8

"""
    Selling Partner API for Finances

    The Selling Partner API for Finances helps you obtain financial information relevant to a seller's business. You can obtain financial events for a given order, financial event group, or date range without having to wait until a statement period closes. You can also obtain financial event groups for a given date range.

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.financesV0.models.currency import Currency
from typing import Optional, Set
from typing_extensions import Self

class CapacityReservationBillingEvent(BaseModel):
    """
    An event related to a capacity reservation billing charge.
    """ # noqa: E501
    transaction_type: Optional[StrictStr] = Field(default=None, description="Indicates the type of transaction. For example, FBA Inventory Fee", alias="TransactionType")
    posted_date: Optional[datetime] = Field(default=None, description="Fields with a schema type of date are in ISO 8601 date time format (for example GroupBeginDate).", alias="PostedDate")
    description: Optional[StrictStr] = Field(default=None, description="A short description of the capacity reservation billing event.", alias="Description")
    transaction_amount: Optional[Currency] = Field(default=None, alias="TransactionAmount")
    __properties: ClassVar[List[str]] = ["TransactionType", "PostedDate", "Description", "TransactionAmount"]

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
        """Create an instance of CapacityReservationBillingEvent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of transaction_amount
        if self.transaction_amount:
            _dict['TransactionAmount'] = self.transaction_amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CapacityReservationBillingEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "TransactionType": obj.get("TransactionType"),
            "PostedDate": obj.get("PostedDate"),
            "Description": obj.get("Description"),
            "TransactionAmount": Currency.from_dict(obj["TransactionAmount"]) if obj.get("TransactionAmount") is not None else None
        })
        return _obj


