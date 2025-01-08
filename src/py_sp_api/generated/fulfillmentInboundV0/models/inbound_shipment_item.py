# coding: utf-8

"""
    Selling Partner API for Fulfillment Inbound

    The Selling Partner API for Fulfillment Inbound lets you create applications that create and update inbound shipments of inventory to Amazon's fulfillment network.

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.fulfillmentInboundV0.models.prep_details import PrepDetails
from typing import Optional, Set
from typing_extensions import Self

class InboundShipmentItem(BaseModel):
    """
    Item information for an inbound shipment. Submitted with a call to the createInboundShipment or updateInboundShipment operation.
    """ # noqa: E501
    shipment_id: Optional[StrictStr] = Field(default=None, description="A shipment identifier originally returned by the createInboundShipmentPlan operation.", alias="ShipmentId")
    seller_sku: StrictStr = Field(description="The seller SKU of the item.", alias="SellerSKU")
    fulfillment_network_sku: Optional[StrictStr] = Field(default=None, description="Amazon's fulfillment network SKU of the item.", alias="FulfillmentNetworkSKU")
    quantity_shipped: StrictInt = Field(description="The item quantity.", alias="QuantityShipped")
    quantity_received: Optional[StrictInt] = Field(default=None, description="The item quantity.", alias="QuantityReceived")
    quantity_in_case: Optional[StrictInt] = Field(default=None, description="The item quantity.", alias="QuantityInCase")
    release_date: Optional[date] = Field(default=None, description="Type containing date in string format", alias="ReleaseDate")
    prep_details_list: Optional[List[PrepDetails]] = Field(default=None, description="A list of preparation instructions and who is responsible for that preparation.", alias="PrepDetailsList")
    __properties: ClassVar[List[str]] = ["ShipmentId", "SellerSKU", "FulfillmentNetworkSKU", "QuantityShipped", "QuantityReceived", "QuantityInCase", "ReleaseDate", "PrepDetailsList"]

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
        """Create an instance of InboundShipmentItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in prep_details_list (list)
        _items = []
        if self.prep_details_list:
            for _item_prep_details_list in self.prep_details_list:
                if _item_prep_details_list:
                    _items.append(_item_prep_details_list.to_dict())
            _dict['PrepDetailsList'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InboundShipmentItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ShipmentId": obj.get("ShipmentId"),
            "SellerSKU": obj.get("SellerSKU"),
            "FulfillmentNetworkSKU": obj.get("FulfillmentNetworkSKU"),
            "QuantityShipped": obj.get("QuantityShipped"),
            "QuantityReceived": obj.get("QuantityReceived"),
            "QuantityInCase": obj.get("QuantityInCase"),
            "ReleaseDate": obj.get("ReleaseDate"),
            "PrepDetailsList": [PrepDetails.from_dict(_item) for _item in obj["PrepDetailsList"]] if obj.get("PrepDetailsList") is not None else None
        })
        return _obj


