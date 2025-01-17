# coding: utf-8

"""
    Selling Partner API for Pricing

    The Selling Partner API for Pricing helps you programmatically retrieve product pricing and offer pricing information for Amazon Marketplace products.  For more information, refer to the [Product Pricing v2022-05-01 Use Case Guide](https://developer-docs.amazon.com/sp-api/docs/product-pricing-api-v2022-05-01-use-case-guide).

    The version of the OpenAPI document: 2022-05-01
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class FulfillmentType(str, Enum):
    """
    Indicates whether the item is fulfilled by Amazon or by the seller (merchant).
    """

    """
    allowed enum values
    """
    AFN = 'AFN'
    MFN = 'MFN'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FulfillmentType from a JSON string"""
        return cls(json.loads(json_str))


