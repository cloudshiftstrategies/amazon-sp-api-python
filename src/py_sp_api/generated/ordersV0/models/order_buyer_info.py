# coding: utf-8

"""
    Orders v0

    Use the Orders Selling Partner API to programmatically retrieve order information. With this API, you can develop fast, flexible, and custom applications to manage order synchronization, perform order research, and create demand-based decision support tools.   _Note:_ For the JP, AU, and SG marketplaces, the Orders API supports orders from 2016 onward. For all other marketplaces, the Orders API supports orders for the last two years (orders older than this don't show up in the response).

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.ordersV0.models.buyer_tax_info import BuyerTaxInfo
from typing import Optional, Set
from typing_extensions import Self

class OrderBuyerInfo(BaseModel):
    """
    Buyer information for an order.
    """ # noqa: E501
    amazon_order_id: StrictStr = Field(description="An Amazon-defined order identifier, in 3-7-7 format.", alias="AmazonOrderId")
    buyer_email: Optional[StrictStr] = Field(default=None, description="The anonymized email address of the buyer.", alias="BuyerEmail")
    buyer_name: Optional[StrictStr] = Field(default=None, description="The buyer name or the recipient name.", alias="BuyerName")
    buyer_county: Optional[StrictStr] = Field(default=None, description="The county of the buyer.  **Note**: This attribute is only available in the Brazil marketplace.", alias="BuyerCounty")
    buyer_tax_info: Optional[BuyerTaxInfo] = Field(default=None, alias="BuyerTaxInfo")
    purchase_order_number: Optional[StrictStr] = Field(default=None, description="The purchase order (PO) number entered by the buyer at checkout. Only returned for orders where the buyer entered a PO number at checkout.", alias="PurchaseOrderNumber")
    __properties: ClassVar[List[str]] = ["AmazonOrderId", "BuyerEmail", "BuyerName", "BuyerCounty", "BuyerTaxInfo", "PurchaseOrderNumber"]

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
        """Create an instance of OrderBuyerInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of buyer_tax_info
        if self.buyer_tax_info:
            _dict['BuyerTaxInfo'] = self.buyer_tax_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderBuyerInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "AmazonOrderId": obj.get("AmazonOrderId"),
            "BuyerEmail": obj.get("BuyerEmail"),
            "BuyerName": obj.get("BuyerName"),
            "BuyerCounty": obj.get("BuyerCounty"),
            "BuyerTaxInfo": BuyerTaxInfo.from_dict(obj["BuyerTaxInfo"]) if obj.get("BuyerTaxInfo") is not None else None,
            "PurchaseOrderNumber": obj.get("PurchaseOrderNumber")
        })
        return _obj


