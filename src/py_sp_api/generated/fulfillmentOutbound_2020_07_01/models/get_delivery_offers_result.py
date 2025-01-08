# coding: utf-8

"""
    Selling Partner APIs for Fulfillment Outbound

    The Selling Partner API for Fulfillment Outbound lets you create applications that help a seller fulfill Multi-Channel Fulfillment orders using their inventory in Amazon's fulfillment network. You can get information on both potential and existing fulfillment orders.

    The version of the OpenAPI document: 2020-07-01
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.fulfillmentOutbound_2020_07_01.models.delivery_offer import DeliveryOffer
from typing import Optional, Set
from typing_extensions import Self

class GetDeliveryOffersResult(BaseModel):
    """
    A list of delivery offers, including offer expiration, earliest and latest date and time range, and the delivery offer policy.
    """ # noqa: E501
    delivery_offers: Optional[List[DeliveryOffer]] = Field(default=None, description="An array of delivery offer information.", alias="deliveryOffers")
    __properties: ClassVar[List[str]] = ["deliveryOffers"]

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
        """Create an instance of GetDeliveryOffersResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in delivery_offers (list)
        _items = []
        if self.delivery_offers:
            for _item_delivery_offers in self.delivery_offers:
                if _item_delivery_offers:
                    _items.append(_item_delivery_offers.to_dict())
            _dict['deliveryOffers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetDeliveryOffersResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "deliveryOffers": [DeliveryOffer.from_dict(_item) for _item in obj["deliveryOffers"]] if obj.get("deliveryOffers") is not None else None
        })
        return _obj


