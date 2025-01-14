# coding: utf-8

"""
    Selling Partner API for Direct Fulfillment Payments

    The Selling Partner API for Direct Fulfillment Payments provides programmatic access to a direct fulfillment vendor's invoice data.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.vendorDirectFulfillmentPaymentsV1.models.charge_details import ChargeDetails
from py_sp_api.generated.vendorDirectFulfillmentPaymentsV1.models.item_quantity import ItemQuantity
from py_sp_api.generated.vendorDirectFulfillmentPaymentsV1.models.money import Money
from py_sp_api.generated.vendorDirectFulfillmentPaymentsV1.models.tax_detail import TaxDetail
from typing import Optional, Set
from typing_extensions import Self

class InvoiceItem(BaseModel):
    """
    Provides the details of the items in this invoice.
    """ # noqa: E501
    item_sequence_number: StrictStr = Field(description="Numbering of the item on the purchase order. The first item will be 1, the second 2, and so on.", alias="itemSequenceNumber")
    buyer_product_identifier: Optional[StrictStr] = Field(default=None, description="Buyer's standard identification number (ASIN) of an item.", alias="buyerProductIdentifier")
    vendor_product_identifier: Optional[StrictStr] = Field(default=None, description="The vendor selected product identification of the item.", alias="vendorProductIdentifier")
    invoiced_quantity: ItemQuantity = Field(alias="invoicedQuantity")
    net_cost: Money = Field(alias="netCost")
    purchase_order_number: StrictStr = Field(description="The purchase order number for this order. Formatting Notes: 8-character alpha-numeric code.", alias="purchaseOrderNumber")
    vendor_order_number: Optional[StrictStr] = Field(default=None, description="The vendor's order number for this order.", alias="vendorOrderNumber")
    hsn_code: Optional[StrictStr] = Field(default=None, description="Harmonized System of Nomenclature (HSN) tax code. The HSN number cannot contain alphabets.", alias="hsnCode")
    tax_details: Optional[List[TaxDetail]] = Field(default=None, description="Individual tax details per line item.", alias="taxDetails")
    charge_details: Optional[List[ChargeDetails]] = Field(default=None, description="Individual charge details per line item.", alias="chargeDetails")
    __properties: ClassVar[List[str]] = ["itemSequenceNumber", "buyerProductIdentifier", "vendorProductIdentifier", "invoicedQuantity", "netCost", "purchaseOrderNumber", "vendorOrderNumber", "hsnCode", "taxDetails", "chargeDetails"]

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
        """Create an instance of InvoiceItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of invoiced_quantity
        if self.invoiced_quantity:
            _dict['invoicedQuantity'] = self.invoiced_quantity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of net_cost
        if self.net_cost:
            _dict['netCost'] = self.net_cost.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in tax_details (list)
        _items = []
        if self.tax_details:
            for _item_tax_details in self.tax_details:
                if _item_tax_details:
                    _items.append(_item_tax_details.to_dict())
            _dict['taxDetails'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in charge_details (list)
        _items = []
        if self.charge_details:
            for _item_charge_details in self.charge_details:
                if _item_charge_details:
                    _items.append(_item_charge_details.to_dict())
            _dict['chargeDetails'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InvoiceItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "itemSequenceNumber": obj.get("itemSequenceNumber"),
            "buyerProductIdentifier": obj.get("buyerProductIdentifier"),
            "vendorProductIdentifier": obj.get("vendorProductIdentifier"),
            "invoicedQuantity": ItemQuantity.from_dict(obj["invoicedQuantity"]) if obj.get("invoicedQuantity") is not None else None,
            "netCost": Money.from_dict(obj["netCost"]) if obj.get("netCost") is not None else None,
            "purchaseOrderNumber": obj.get("purchaseOrderNumber"),
            "vendorOrderNumber": obj.get("vendorOrderNumber"),
            "hsnCode": obj.get("hsnCode"),
            "taxDetails": [TaxDetail.from_dict(_item) for _item in obj["taxDetails"]] if obj.get("taxDetails") is not None else None,
            "chargeDetails": [ChargeDetails.from_dict(_item) for _item in obj["chargeDetails"]] if obj.get("chargeDetails") is not None else None
        })
        return _obj


