# coding: utf-8

"""
    Selling Partner API for Fulfillment Inbound

    The Selling Partner API for Fulfillment Inbound lets you create applications that create and update inbound shipments of inventory to Amazon's fulfillment network.

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ShipmentStatus(str, Enum):
    """
    Indicates the status of the inbound shipment. When used with the createInboundShipment operation, WORKING is the only valid value. When used with the updateInboundShipment operation, possible values are WORKING, SHIPPED or CANCELLED.
    """

    """
    allowed enum values
    """
    WORKING = 'WORKING'
    SHIPPED = 'SHIPPED'
    RECEIVING = 'RECEIVING'
    CANCELLED = 'CANCELLED'
    DELETED = 'DELETED'
    CLOSED = 'CLOSED'
    ERROR = 'ERROR'
    IN_TRANSIT = 'IN_TRANSIT'
    DELIVERED = 'DELIVERED'
    CHECKED_IN = 'CHECKED_IN'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ShipmentStatus from a JSON string"""
        return cls(json.loads(json_str))


