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

class SolutionProviderCreditEvent(BaseModel):
    """
    A credit given to a solution provider.
    """ # noqa: E501
    provider_transaction_type: Optional[StrictStr] = Field(default=None, description="The transaction type.", alias="ProviderTransactionType")
    seller_order_id: Optional[StrictStr] = Field(default=None, description="A seller-defined identifier for an order.", alias="SellerOrderId")
    marketplace_id: Optional[StrictStr] = Field(default=None, description="The identifier of the marketplace where the order was placed.", alias="MarketplaceId")
    marketplace_country_code: Optional[StrictStr] = Field(default=None, description="The two-letter country code of the country associated with the marketplace where the order was placed.", alias="MarketplaceCountryCode")
    seller_id: Optional[StrictStr] = Field(default=None, description="The Amazon-defined identifier of the seller.", alias="SellerId")
    seller_store_name: Optional[StrictStr] = Field(default=None, description="The store name where the payment event occurred.", alias="SellerStoreName")
    provider_id: Optional[StrictStr] = Field(default=None, description="The Amazon-defined identifier of the solution provider.", alias="ProviderId")
    provider_store_name: Optional[StrictStr] = Field(default=None, description="The store name where the payment event occurred.", alias="ProviderStoreName")
    transaction_amount: Optional[Currency] = Field(default=None, alias="TransactionAmount")
    transaction_creation_date: Optional[datetime] = Field(default=None, description="Fields with a schema type of date are in ISO 8601 date time format (for example GroupBeginDate).", alias="TransactionCreationDate")
    __properties: ClassVar[List[str]] = ["ProviderTransactionType", "SellerOrderId", "MarketplaceId", "MarketplaceCountryCode", "SellerId", "SellerStoreName", "ProviderId", "ProviderStoreName", "TransactionAmount", "TransactionCreationDate"]

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
        """Create an instance of SolutionProviderCreditEvent from a JSON string"""
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
        """Create an instance of SolutionProviderCreditEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ProviderTransactionType": obj.get("ProviderTransactionType"),
            "SellerOrderId": obj.get("SellerOrderId"),
            "MarketplaceId": obj.get("MarketplaceId"),
            "MarketplaceCountryCode": obj.get("MarketplaceCountryCode"),
            "SellerId": obj.get("SellerId"),
            "SellerStoreName": obj.get("SellerStoreName"),
            "ProviderId": obj.get("ProviderId"),
            "ProviderStoreName": obj.get("ProviderStoreName"),
            "TransactionAmount": Currency.from_dict(obj["TransactionAmount"]) if obj.get("TransactionAmount") is not None else None,
            "TransactionCreationDate": obj.get("TransactionCreationDate")
        })
        return _obj


