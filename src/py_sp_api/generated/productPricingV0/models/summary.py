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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.productPricingV0.models.buy_box_price_type import BuyBoxPriceType
from py_sp_api.generated.productPricingV0.models.lowest_price_type import LowestPriceType
from py_sp_api.generated.productPricingV0.models.money_type import MoneyType
from py_sp_api.generated.productPricingV0.models.offer_count_type import OfferCountType
from py_sp_api.generated.productPricingV0.models.sales_rank_type import SalesRankType
from typing import Optional, Set
from typing_extensions import Self

class Summary(BaseModel):
    """
    Contains price information about the product, including the LowestPrices and BuyBoxPrices, the ListPrice, the SuggestedLowerPricePlusShipping, and NumberOfOffers and NumberOfBuyBoxEligibleOffers.
    """ # noqa: E501
    total_offer_count: StrictInt = Field(description="The number of unique offers contained in NumberOfOffers.", alias="TotalOfferCount")
    number_of_offers: Optional[List[OfferCountType]] = Field(default=None, alias="NumberOfOffers")
    lowest_prices: Optional[List[LowestPriceType]] = Field(default=None, alias="LowestPrices")
    buy_box_prices: Optional[List[BuyBoxPriceType]] = Field(default=None, alias="BuyBoxPrices")
    list_price: Optional[MoneyType] = Field(default=None, alias="ListPrice")
    competitive_price_threshold: Optional[MoneyType] = Field(default=None, alias="CompetitivePriceThreshold")
    suggested_lower_price_plus_shipping: Optional[MoneyType] = Field(default=None, alias="SuggestedLowerPricePlusShipping")
    sales_rankings: Optional[List[SalesRankType]] = Field(default=None, description="A list of sales rank information for the item, by category.", alias="SalesRankings")
    buy_box_eligible_offers: Optional[List[OfferCountType]] = Field(default=None, alias="BuyBoxEligibleOffers")
    offers_available_time: Optional[datetime] = Field(default=None, description="When the status is ActiveButTooSoonForProcessing, this is the time when the offers will be available for processing.", alias="OffersAvailableTime")
    __properties: ClassVar[List[str]] = ["TotalOfferCount", "NumberOfOffers", "LowestPrices", "BuyBoxPrices", "ListPrice", "CompetitivePriceThreshold", "SuggestedLowerPricePlusShipping", "SalesRankings", "BuyBoxEligibleOffers", "OffersAvailableTime"]

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
        """Create an instance of Summary from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in number_of_offers (list)
        _items = []
        if self.number_of_offers:
            for _item_number_of_offers in self.number_of_offers:
                if _item_number_of_offers:
                    _items.append(_item_number_of_offers.to_dict())
            _dict['NumberOfOffers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in lowest_prices (list)
        _items = []
        if self.lowest_prices:
            for _item_lowest_prices in self.lowest_prices:
                if _item_lowest_prices:
                    _items.append(_item_lowest_prices.to_dict())
            _dict['LowestPrices'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in buy_box_prices (list)
        _items = []
        if self.buy_box_prices:
            for _item_buy_box_prices in self.buy_box_prices:
                if _item_buy_box_prices:
                    _items.append(_item_buy_box_prices.to_dict())
            _dict['BuyBoxPrices'] = _items
        # override the default output from pydantic by calling `to_dict()` of list_price
        if self.list_price:
            _dict['ListPrice'] = self.list_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of competitive_price_threshold
        if self.competitive_price_threshold:
            _dict['CompetitivePriceThreshold'] = self.competitive_price_threshold.to_dict()
        # override the default output from pydantic by calling `to_dict()` of suggested_lower_price_plus_shipping
        if self.suggested_lower_price_plus_shipping:
            _dict['SuggestedLowerPricePlusShipping'] = self.suggested_lower_price_plus_shipping.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in sales_rankings (list)
        _items = []
        if self.sales_rankings:
            for _item_sales_rankings in self.sales_rankings:
                if _item_sales_rankings:
                    _items.append(_item_sales_rankings.to_dict())
            _dict['SalesRankings'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in buy_box_eligible_offers (list)
        _items = []
        if self.buy_box_eligible_offers:
            for _item_buy_box_eligible_offers in self.buy_box_eligible_offers:
                if _item_buy_box_eligible_offers:
                    _items.append(_item_buy_box_eligible_offers.to_dict())
            _dict['BuyBoxEligibleOffers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Summary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "TotalOfferCount": obj.get("TotalOfferCount"),
            "NumberOfOffers": [OfferCountType.from_dict(_item) for _item in obj["NumberOfOffers"]] if obj.get("NumberOfOffers") is not None else None,
            "LowestPrices": [LowestPriceType.from_dict(_item) for _item in obj["LowestPrices"]] if obj.get("LowestPrices") is not None else None,
            "BuyBoxPrices": [BuyBoxPriceType.from_dict(_item) for _item in obj["BuyBoxPrices"]] if obj.get("BuyBoxPrices") is not None else None,
            "ListPrice": MoneyType.from_dict(obj["ListPrice"]) if obj.get("ListPrice") is not None else None,
            "CompetitivePriceThreshold": MoneyType.from_dict(obj["CompetitivePriceThreshold"]) if obj.get("CompetitivePriceThreshold") is not None else None,
            "SuggestedLowerPricePlusShipping": MoneyType.from_dict(obj["SuggestedLowerPricePlusShipping"]) if obj.get("SuggestedLowerPricePlusShipping") is not None else None,
            "SalesRankings": [SalesRankType.from_dict(_item) for _item in obj["SalesRankings"]] if obj.get("SalesRankings") is not None else None,
            "BuyBoxEligibleOffers": [OfferCountType.from_dict(_item) for _item in obj["BuyBoxEligibleOffers"]] if obj.get("BuyBoxEligibleOffers") is not None else None,
            "OffersAvailableTime": obj.get("OffersAvailableTime")
        })
        return _obj


