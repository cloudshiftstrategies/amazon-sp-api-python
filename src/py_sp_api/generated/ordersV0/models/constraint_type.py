# coding: utf-8

"""
    Orders v0

    Use the Orders Selling Partner API to programmatically retrieve order information. With this API, you can develop fast, flexible, and custom applications to manage order synchronization, perform order research, and create demand-based decision support tools.   _Note:_ For the JP, AU, and SG marketplaces, the Orders API supports orders from 2016 onward. For all other marketplaces, the Orders API supports orders for the last two years (orders older than this don't show up in the response).

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ConstraintType(str, Enum):
    """
    Details the importance of the constraint present on the item
    """

    """
    allowed enum values
    """
    MANDATORY = 'MANDATORY'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ConstraintType from a JSON string"""
        return cls(json.loads(json_str))


