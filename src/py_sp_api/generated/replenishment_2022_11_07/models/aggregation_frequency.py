# coding: utf-8

"""
    Selling Partner API for Replenishment

    The Selling Partner API for Replenishment (Replenishment API) provides programmatic access to replenishment program metrics and offers. These programs provide recurring delivery of any replenishable item at a frequency chosen by the customer.  The Replenishment API is available worldwide wherever Amazon Subscribe & Save is available or is supported. The API is available to vendors and FBA selling partners.

    The version of the OpenAPI document: 2022-11-07
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AggregationFrequency(str, Enum):
    """
    The time period used to group data in the response. Note that this is only valid for the `PERFORMANCE` time period type.
    """

    """
    allowed enum values
    """
    WEEK = 'WEEK'
    MONTH = 'MONTH'
    QUARTER = 'QUARTER'
    YEAR = 'YEAR'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AggregationFrequency from a JSON string"""
        return cls(json.loads(json_str))


