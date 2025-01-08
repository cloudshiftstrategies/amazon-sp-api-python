# coding: utf-8

"""
    Selling Partner API for Pricing

    The Selling Partner API for Pricing helps you programmatically retrieve product pricing and offer information for Amazon Marketplace products.

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.productPricingV0.models.competitive_price_type import CompetitivePriceType
from py_sp_api.generated.productPricingV0.models.money_type import MoneyType
from py_sp_api.generated.productPricingV0.models.offer_listing_count_type import OfferListingCountType
from typing import Optional, Set
from typing_extensions import Self

class CompetitivePricingType(BaseModel):
    """
    Competitive pricing information for the item.
    """ # noqa: E501
    competitive_prices: List[CompetitivePriceType] = Field(description="A list of competitive pricing information.", alias="CompetitivePrices")
    number_of_offer_listings: List[OfferListingCountType] = Field(description="The number of active offer listings for the item that was submitted. The listing count is returned by condition, one for each listing condition value that is returned.", alias="NumberOfOfferListings")
    trade_in_value: Optional[MoneyType] = Field(default=None, alias="TradeInValue")
    __properties: ClassVar[List[str]] = ["CompetitivePrices", "NumberOfOfferListings", "TradeInValue"]

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
        """Create an instance of CompetitivePricingType from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in competitive_prices (list)
        _items = []
        if self.competitive_prices:
            for _item_competitive_prices in self.competitive_prices:
                if _item_competitive_prices:
                    _items.append(_item_competitive_prices.to_dict())
            _dict['CompetitivePrices'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in number_of_offer_listings (list)
        _items = []
        if self.number_of_offer_listings:
            for _item_number_of_offer_listings in self.number_of_offer_listings:
                if _item_number_of_offer_listings:
                    _items.append(_item_number_of_offer_listings.to_dict())
            _dict['NumberOfOfferListings'] = _items
        # override the default output from pydantic by calling `to_dict()` of trade_in_value
        if self.trade_in_value:
            _dict['TradeInValue'] = self.trade_in_value.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CompetitivePricingType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "CompetitivePrices": [CompetitivePriceType.from_dict(_item) for _item in obj["CompetitivePrices"]] if obj.get("CompetitivePrices") is not None else None,
            "NumberOfOfferListings": [OfferListingCountType.from_dict(_item) for _item in obj["NumberOfOfferListings"]] if obj.get("NumberOfOfferListings") is not None else None,
            "TradeInValue": MoneyType.from_dict(obj["TradeInValue"]) if obj.get("TradeInValue") is not None else None
        })
        return _obj


