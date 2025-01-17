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


class Metric(str, Enum):
    """
    The metric name and description.
    """

    """
    allowed enum values
    """
    SHIPPED_SUBSCRIPTION_UNITS = 'SHIPPED_SUBSCRIPTION_UNITS'
    TOTAL_SUBSCRIPTIONS_REVENUE = 'TOTAL_SUBSCRIPTIONS_REVENUE'
    ACTIVE_SUBSCRIPTIONS = 'ACTIVE_SUBSCRIPTIONS'
    NOT_DELIVERED_DUE_TO_OOS = 'NOT_DELIVERED_DUE_TO_OOS'
    SUBSCRIBER_NON_SUBSCRIBER_AVERAGE_REVENUE = 'SUBSCRIBER_NON_SUBSCRIBER_AVERAGE_REVENUE'
    LOST_REVENUE_DUE_TO_OOS = 'LOST_REVENUE_DUE_TO_OOS'
    SUBSCRIBER_NON_SUBSCRIBER_AVERAGE_REORDERS = 'SUBSCRIBER_NON_SUBSCRIBER_AVERAGE_REORDERS'
    COUPONS_REVENUE_PENETRATION = 'COUPONS_REVENUE_PENETRATION'
    REVENUE_BY_DELIVERIES = 'REVENUE_BY_DELIVERIES'
    SUBSCRIBER_RETENTION = 'SUBSCRIBER_RETENTION'
    REVENUE_PENETRATION_BY_SELLER_FUNDING = 'REVENUE_PENETRATION_BY_SELLER_FUNDING'
    SHARE_OF_COUPON_SUBSCRIPTIONS = 'SHARE_OF_COUPON_SUBSCRIPTIONS'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Metric from a JSON string"""
        return cls(json.loads(json_str))


