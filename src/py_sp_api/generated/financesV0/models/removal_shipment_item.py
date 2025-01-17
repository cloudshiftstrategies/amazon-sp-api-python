# coding: utf-8

"""
    Selling Partner API for Finances

    The Selling Partner API for Finances helps you obtain financial information relevant to a seller's business. You can obtain financial events for a given order, financial event group, or date range without having to wait until a statement period closes. You can also obtain financial event groups for a given date range.

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.financesV0.models.currency import Currency
from typing import Optional, Set
from typing_extensions import Self

class RemovalShipmentItem(BaseModel):
    """
    Item-level information for a removal shipment.
    """ # noqa: E501
    removal_shipment_item_id: Optional[StrictStr] = Field(default=None, description="An identifier for an item in a removal shipment.", alias="RemovalShipmentItemId")
    tax_collection_model: Optional[StrictStr] = Field(default=None, description="The tax collection model applied to the item.  Possible values:  * MarketplaceFacilitator - Tax is withheld and remitted to the taxing authority by Amazon on behalf of the seller.  * Standard - Tax is paid to the seller and not remitted to the taxing authority by Amazon.", alias="TaxCollectionModel")
    fulfillment_network_sku: Optional[StrictStr] = Field(default=None, description="The Amazon fulfillment network SKU for the item.", alias="FulfillmentNetworkSKU")
    quantity: Optional[StrictInt] = Field(default=None, description="The quantity of the item.", alias="Quantity")
    revenue: Optional[Currency] = Field(default=None, alias="Revenue")
    fee_amount: Optional[Currency] = Field(default=None, alias="FeeAmount")
    tax_amount: Optional[Currency] = Field(default=None, alias="TaxAmount")
    tax_withheld: Optional[Currency] = Field(default=None, alias="TaxWithheld")
    __properties: ClassVar[List[str]] = ["RemovalShipmentItemId", "TaxCollectionModel", "FulfillmentNetworkSKU", "Quantity", "Revenue", "FeeAmount", "TaxAmount", "TaxWithheld"]

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
        """Create an instance of RemovalShipmentItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of revenue
        if self.revenue:
            _dict['Revenue'] = self.revenue.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fee_amount
        if self.fee_amount:
            _dict['FeeAmount'] = self.fee_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tax_amount
        if self.tax_amount:
            _dict['TaxAmount'] = self.tax_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tax_withheld
        if self.tax_withheld:
            _dict['TaxWithheld'] = self.tax_withheld.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RemovalShipmentItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "RemovalShipmentItemId": obj.get("RemovalShipmentItemId"),
            "TaxCollectionModel": obj.get("TaxCollectionModel"),
            "FulfillmentNetworkSKU": obj.get("FulfillmentNetworkSKU"),
            "Quantity": obj.get("Quantity"),
            "Revenue": Currency.from_dict(obj["Revenue"]) if obj.get("Revenue") is not None else None,
            "FeeAmount": Currency.from_dict(obj["FeeAmount"]) if obj.get("FeeAmount") is not None else None,
            "TaxAmount": Currency.from_dict(obj["TaxAmount"]) if obj.get("TaxAmount") is not None else None,
            "TaxWithheld": Currency.from_dict(obj["TaxWithheld"]) if obj.get("TaxWithheld") is not None else None
        })
        return _obj


