# coding: utf-8

"""
    Selling Partner API for Merchant Fulfillment

    With the Selling Partner API for Merchant Fulfillment, you can build applications that sellers can use to purchase shipping for non-Prime and Prime orders using Amazon's Buy Shipping Services.

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.merchantFulfillmentV0.models.additional_seller_input import AdditionalSellerInput
from py_sp_api.generated.merchantFulfillmentV0.models.constraint import Constraint
from py_sp_api.generated.merchantFulfillmentV0.models.input_target_type import InputTargetType
from typing import Optional, Set
from typing_extensions import Self

class SellerInputDefinition(BaseModel):
    """
    Specifies characteristics that apply to a seller input.
    """ # noqa: E501
    is_required: StrictBool = Field(description="When true, the additional input field is required.", alias="IsRequired")
    data_type: StrictStr = Field(description="The data type of the additional input field.", alias="DataType")
    constraints: List[Constraint] = Field(description="List of constraints.", alias="Constraints")
    input_display_text: StrictStr = Field(description="The display text for the additional input field.", alias="InputDisplayText")
    input_target: Optional[InputTargetType] = Field(default=None, alias="InputTarget")
    stored_value: AdditionalSellerInput = Field(alias="StoredValue")
    restricted_set_values: Optional[List[StrictStr]] = Field(default=None, description="The set of fixed values in an additional seller input.", alias="RestrictedSetValues")
    __properties: ClassVar[List[str]] = ["IsRequired", "DataType", "Constraints", "InputDisplayText", "InputTarget", "StoredValue", "RestrictedSetValues"]

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
        """Create an instance of SellerInputDefinition from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in constraints (list)
        _items = []
        if self.constraints:
            for _item_constraints in self.constraints:
                if _item_constraints:
                    _items.append(_item_constraints.to_dict())
            _dict['Constraints'] = _items
        # override the default output from pydantic by calling `to_dict()` of stored_value
        if self.stored_value:
            _dict['StoredValue'] = self.stored_value.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SellerInputDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "IsRequired": obj.get("IsRequired"),
            "DataType": obj.get("DataType"),
            "Constraints": [Constraint.from_dict(_item) for _item in obj["Constraints"]] if obj.get("Constraints") is not None else None,
            "InputDisplayText": obj.get("InputDisplayText"),
            "InputTarget": obj.get("InputTarget"),
            "StoredValue": AdditionalSellerInput.from_dict(obj["StoredValue"]) if obj.get("StoredValue") is not None else None,
            "RestrictedSetValues": obj.get("RestrictedSetValues")
        })
        return _obj


