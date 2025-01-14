# coding: utf-8

"""
    Selling Partner API for Pricing

    The Selling Partner API for Pricing helps you programmatically retrieve product pricing and offer pricing information for Amazon Marketplace products.  For more information, refer to the [Product Pricing v2022-05-01 Use Case Guide](https://developer-docs.amazon.com/sp-api/docs/product-pricing-api-v2022-05-01-use-case-guide).

    The version of the OpenAPI document: 2022-05-01
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
from py_sp_api.generated.productPricing_2022_05_01.models.competitive_summary_included_data import CompetitiveSummaryIncludedData
from py_sp_api.generated.productPricing_2022_05_01.models.http_method import HttpMethod
from py_sp_api.generated.productPricing_2022_05_01.models.lowest_priced_offers_input import LowestPricedOffersInput
from typing import Optional, Set
from typing_extensions import Self

class CompetitiveSummaryRequest(BaseModel):
    """
    An individual `competitiveSummary` request for an ASIN and `marketplaceId`.
    """ # noqa: E501
    asin: StrictStr = Field(description="The ASIN of the item.")
    marketplace_id: StrictStr = Field(description="A marketplace identifier. Specifies the marketplace for which data is returned.", alias="marketplaceId")
    included_data: Annotated[List[CompetitiveSummaryIncludedData], Field(min_length=1)] = Field(description="The list of requested competitive pricing data for the product.", alias="includedData")
    lowest_priced_offers_inputs: Optional[Annotated[List[LowestPricedOffersInput], Field(min_length=0, max_length=5)]] = Field(default=None, description="The list of `lowestPricedOffersInput` parameters that are used to build `lowestPricedOffers` in the response. This attribute is only valid if `lowestPricedOffers` is requested in `includedData`", alias="lowestPricedOffersInputs")
    method: HttpMethod
    uri: Annotated[str, Field(min_length=6, strict=True, max_length=512)] = Field(description="The URI associated with the individual APIs that are called as part of the batch request.")
    __properties: ClassVar[List[str]] = ["asin", "marketplaceId", "includedData", "lowestPricedOffersInputs", "method", "uri"]

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
        """Create an instance of CompetitiveSummaryRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in lowest_priced_offers_inputs (list)
        _items = []
        if self.lowest_priced_offers_inputs:
            for _item_lowest_priced_offers_inputs in self.lowest_priced_offers_inputs:
                if _item_lowest_priced_offers_inputs:
                    _items.append(_item_lowest_priced_offers_inputs.to_dict())
            _dict['lowestPricedOffersInputs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CompetitiveSummaryRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "asin": obj.get("asin"),
            "marketplaceId": obj.get("marketplaceId"),
            "includedData": obj.get("includedData"),
            "lowestPricedOffersInputs": [LowestPricedOffersInput.from_dict(_item) for _item in obj["lowestPricedOffersInputs"]] if obj.get("lowestPricedOffersInputs") is not None else None,
            "method": obj.get("method"),
            "uri": obj.get("uri")
        })
        return _obj


