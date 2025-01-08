# coding: utf-8

"""
    Fulfillment Inbound v2024-03-20

    The Selling Partner API for Fulfillment By Amazon (FBA) Inbound. The FBA Inbound API enables building inbound workflows to create, manage, and send shipments into Amazon's fulfillment network. The API has interoperability with the Send-to-Amazon user interface.

    The version of the OpenAPI document: 2024-03-20
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.tax_details import TaxDetails
from typing import Optional, Set
from typing_extensions import Self

class ComplianceDetail(BaseModel):
    """
    Contains item identifiers and related tax information.
    """ # noqa: E501
    asin: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=10)]] = Field(default=None, description="The Amazon Standard Identification Number, which identifies the detail page identifier.")
    fnsku: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=10)]] = Field(default=None, description="The Fulfillment Network SKU, which identifies a real fulfillable item with catalog data and condition.")
    msku: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=40)]] = Field(default=None, description="The merchant SKU, a merchant-supplied identifier for a specific SKU.")
    tax_details: Optional[TaxDetails] = Field(default=None, alias="taxDetails")
    __properties: ClassVar[List[str]] = ["asin", "fnsku", "msku", "taxDetails"]

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
        """Create an instance of ComplianceDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of tax_details
        if self.tax_details:
            _dict['taxDetails'] = self.tax_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ComplianceDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "asin": obj.get("asin"),
            "fnsku": obj.get("fnsku"),
            "msku": obj.get("msku"),
            "taxDetails": TaxDetails.from_dict(obj["taxDetails"]) if obj.get("taxDetails") is not None else None
        })
        return _obj


