# coding: utf-8

"""
    Selling Partner API for Merchant Fulfillment

    With the Selling Partner API for Merchant Fulfillment, you can build applications that sellers can use to purchase shipping for non-Prime and Prime orders using Amazon's Buy Shipping Services.

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class UnitOfWeight(str, Enum):
    """
    The unit of weight.
    """

    """
    allowed enum values
    """
    OZ = 'oz'
    G = 'g'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UnitOfWeight from a JSON string"""
        return cls(json.loads(json_str))


