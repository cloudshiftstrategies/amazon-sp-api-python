# coding: utf-8

"""
    Selling Partner API for Shipping

    Provides programmatic access to Amazon Shipping APIs.   **Note:** If you are new to the Amazon Shipping API, refer to the latest version of <a href=\"https://developer-docs.amazon.com/amazon-shipping/docs/shipping-api-v2-reference\">Amazon Shipping API (v2)</a> on the <a href=\"https://developer-docs.amazon.com/amazon-shipping/\">Amazon Shipping Developer Documentation</a> site.

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
from typing_extensions import Annotated
from py_sp_api.generated.shipping.models.accepted_rate import AcceptedRate
from py_sp_api.generated.shipping.models.label_result import LabelResult
from typing import Optional, Set
from typing_extensions import Self

class PurchaseLabelsResult(BaseModel):
    """
    The payload schema for the purchaseLabels operation.
    """ # noqa: E501
    shipment_id: StrictStr = Field(description="The unique shipment identifier.", alias="shipmentId")
    client_reference_id: Optional[Annotated[str, Field(strict=True, max_length=40)]] = Field(default=None, description="Client reference id.", alias="clientReferenceId")
    accepted_rate: AcceptedRate = Field(alias="acceptedRate")
    label_results: List[LabelResult] = Field(description="A list of label results", alias="labelResults")
    __properties: ClassVar[List[str]] = ["shipmentId", "clientReferenceId", "acceptedRate", "labelResults"]

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
        """Create an instance of PurchaseLabelsResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of accepted_rate
        if self.accepted_rate:
            _dict['acceptedRate'] = self.accepted_rate.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in label_results (list)
        _items = []
        if self.label_results:
            for _item_label_results in self.label_results:
                if _item_label_results:
                    _items.append(_item_label_results.to_dict())
            _dict['labelResults'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PurchaseLabelsResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "shipmentId": obj.get("shipmentId"),
            "clientReferenceId": obj.get("clientReferenceId"),
            "acceptedRate": AcceptedRate.from_dict(obj["acceptedRate"]) if obj.get("acceptedRate") is not None else None,
            "labelResults": [LabelResult.from_dict(_item) for _item in obj["labelResults"]] if obj.get("labelResults") is not None else None
        })
        return _obj


