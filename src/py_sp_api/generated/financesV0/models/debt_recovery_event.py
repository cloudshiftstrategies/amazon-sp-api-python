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
from py_sp_api.generated.financesV0.models.charge_instrument import ChargeInstrument
from py_sp_api.generated.financesV0.models.currency import Currency
from py_sp_api.generated.financesV0.models.debt_recovery_item import DebtRecoveryItem
from typing import Optional, Set
from typing_extensions import Self

class DebtRecoveryEvent(BaseModel):
    """
    A debt payment or debt adjustment.
    """ # noqa: E501
    debt_recovery_type: Optional[StrictStr] = Field(default=None, description="The debt recovery type.  Possible values:  * DebtPayment  * DebtPaymentFailure  * DebtAdjustment", alias="DebtRecoveryType")
    recovery_amount: Optional[Currency] = Field(default=None, alias="RecoveryAmount")
    over_payment_credit: Optional[Currency] = Field(default=None, alias="OverPaymentCredit")
    debt_recovery_item_list: Optional[List[DebtRecoveryItem]] = Field(default=None, description="A list of debt recovery item information.", alias="DebtRecoveryItemList")
    charge_instrument_list: Optional[List[ChargeInstrument]] = Field(default=None, description="A list of payment instruments.", alias="ChargeInstrumentList")
    __properties: ClassVar[List[str]] = ["DebtRecoveryType", "RecoveryAmount", "OverPaymentCredit", "DebtRecoveryItemList", "ChargeInstrumentList"]

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
        """Create an instance of DebtRecoveryEvent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of recovery_amount
        if self.recovery_amount:
            _dict['RecoveryAmount'] = self.recovery_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of over_payment_credit
        if self.over_payment_credit:
            _dict['OverPaymentCredit'] = self.over_payment_credit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in debt_recovery_item_list (list)
        _items = []
        if self.debt_recovery_item_list:
            for _item_debt_recovery_item_list in self.debt_recovery_item_list:
                if _item_debt_recovery_item_list:
                    _items.append(_item_debt_recovery_item_list.to_dict())
            _dict['DebtRecoveryItemList'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in charge_instrument_list (list)
        _items = []
        if self.charge_instrument_list:
            for _item_charge_instrument_list in self.charge_instrument_list:
                if _item_charge_instrument_list:
                    _items.append(_item_charge_instrument_list.to_dict())
            _dict['ChargeInstrumentList'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DebtRecoveryEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "DebtRecoveryType": obj.get("DebtRecoveryType"),
            "RecoveryAmount": Currency.from_dict(obj["RecoveryAmount"]) if obj.get("RecoveryAmount") is not None else None,
            "OverPaymentCredit": Currency.from_dict(obj["OverPaymentCredit"]) if obj.get("OverPaymentCredit") is not None else None,
            "DebtRecoveryItemList": [DebtRecoveryItem.from_dict(_item) for _item in obj["DebtRecoveryItemList"]] if obj.get("DebtRecoveryItemList") is not None else None,
            "ChargeInstrumentList": [ChargeInstrument.from_dict(_item) for _item in obj["ChargeInstrumentList"]] if obj.get("ChargeInstrumentList") is not None else None
        })
        return _obj


