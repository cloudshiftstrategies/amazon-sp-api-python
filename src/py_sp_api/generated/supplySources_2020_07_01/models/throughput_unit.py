# coding: utf-8

"""
    Selling Partner API for Supply Sources

    Manage configurations and capabilities of seller supply sources.

    The version of the OpenAPI document: 2020-07-01
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ThroughputUnit(str, Enum):
    """
    The throughput unit
    """

    """
    allowed enum values
    """
    ORDER = 'Order'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ThroughputUnit from a JSON string"""
        return cls(json.loads(json_str))


