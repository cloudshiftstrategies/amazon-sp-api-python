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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.financesV0.models.currency import Currency
from typing import Optional, Set
from typing_extensions import Self

class ChargeComponent(BaseModel):
    """
    A charge on the seller's account.  Possible values:  * Principal - The selling price of the order item, equal to the selling price of the item multiplied by the quantity ordered.  * Tax - The tax collected by the seller on the Principal.  * MarketplaceFacilitatorTax-Principal - The tax withheld on the Principal.  * MarketplaceFacilitatorTax-Shipping - The tax withheld on the ShippingCharge.  * MarketplaceFacilitatorTax-Giftwrap - The tax withheld on the Giftwrap charge.  * MarketplaceFacilitatorTax-Other - The tax withheld on other miscellaneous charges.  * Discount - The promotional discount for an order item.  * TaxDiscount - The tax amount deducted for promotional rebates.  * CODItemCharge - The COD charge for an order item.  * CODItemTaxCharge - The tax collected by the seller on a CODItemCharge.  * CODOrderCharge - The COD charge for an order.  * CODOrderTaxCharge - The tax collected by the seller on a CODOrderCharge.  * CODShippingCharge - Shipping charges for a COD order.  * CODShippingTaxCharge - The tax collected by the seller on a CODShippingCharge.  * ShippingCharge - The shipping charge.  * ShippingTax - The tax collected by the seller on a ShippingCharge.  * Goodwill - The amount given to a buyer as a gesture of goodwill or to compensate for pain and suffering in the buying experience.  * Giftwrap - The gift wrap charge.  * GiftwrapTax - The tax collected by the seller on a Giftwrap charge.  * RestockingFee - The charge applied to the buyer when returning a product in certain categories.  * ReturnShipping - The amount given to the buyer to compensate for shipping the item back in the event we are at fault.  * PointsFee - The value of Amazon Points deducted from the refund if the buyer does not have enough Amazon Points to cover the deduction.  * GenericDeduction - A generic bad debt deduction.  * FreeReplacementReturnShipping - The compensation for return shipping when a buyer receives the wrong item, requests a free replacement, and returns the incorrect item.  * PaymentMethodFee - The fee collected for certain payment methods in certain marketplaces.  * ExportCharge - The export duty that is charged when an item is shipped to an international destination as part of the Amazon Global program.  * SAFE-TReimbursement - The SAFE-T claim amount for the item.  * TCS-CGST - Tax Collected at Source (TCS) for Central Goods and Services Tax (CGST).  * TCS-SGST - Tax Collected at Source for State Goods and Services Tax (SGST).  * TCS-IGST - Tax Collected at Source for Integrated Goods and Services Tax (IGST).  * TCS-UTGST - Tax Collected at Source for Union Territories Goods and Services Tax (UTGST).
    """ # noqa: E501
    charge_type: Optional[StrictStr] = Field(default=None, description="The type of charge.", alias="ChargeType")
    charge_amount: Optional[Currency] = Field(default=None, alias="ChargeAmount")
    __properties: ClassVar[List[str]] = ["ChargeType", "ChargeAmount"]

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
        """Create an instance of ChargeComponent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of charge_amount
        if self.charge_amount:
            _dict['ChargeAmount'] = self.charge_amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ChargeComponent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ChargeType": obj.get("ChargeType"),
            "ChargeAmount": Currency.from_dict(obj["ChargeAmount"]) if obj.get("ChargeAmount") is not None else None
        })
        return _obj


