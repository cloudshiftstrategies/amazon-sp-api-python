# coding: utf-8

"""
    The Selling Partner API for Finances

    The Selling Partner API for Finances provides financial information relevant to a seller's business. You can obtain financial events for a given order or date range without having to wait until a statement period closes.

    The version of the OpenAPI document: 2024-06-19
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.finances_2024_06_19.models.breakdown import Breakdown
from py_sp_api.generated.finances_2024_06_19.models.context import Context
from py_sp_api.generated.finances_2024_06_19.models.currency import Currency
from py_sp_api.generated.finances_2024_06_19.models.item import Item
from py_sp_api.generated.finances_2024_06_19.models.marketplace_details import MarketplaceDetails
from py_sp_api.generated.finances_2024_06_19.models.related_identifier import RelatedIdentifier
from py_sp_api.generated.finances_2024_06_19.models.selling_partner_metadata import SellingPartnerMetadata
from typing import Optional, Set
from typing_extensions import Self

class Transaction(BaseModel):
    """
    All the information related to a transaction.
    """ # noqa: E501
    selling_partner_metadata: Optional[SellingPartnerMetadata] = Field(default=None, alias="sellingPartnerMetadata")
    related_identifiers: Optional[List[RelatedIdentifier]] = Field(default=None, description="Related business identifiers of the transaction.", alias="relatedIdentifiers")
    transaction_type: Optional[StrictStr] = Field(default=None, description="The type of transaction.  **Possible value:** `Shipment`", alias="transactionType")
    transaction_id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the transaction.", alias="transactionId")
    transaction_status: Optional[StrictStr] = Field(default=None, description="The status of the transaction.   **Possible values:**  * `Deferred` * `Released`", alias="transactionStatus")
    description: Optional[StrictStr] = Field(default=None, description="Describes the reasons for the transaction.  **Example:** 'Order Payment', 'Refund Order'")
    posted_date: Optional[datetime] = Field(default=None, description="A date in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format.", alias="postedDate")
    total_amount: Optional[Currency] = Field(default=None, alias="totalAmount")
    marketplace_details: Optional[MarketplaceDetails] = Field(default=None, alias="marketplaceDetails")
    items: Optional[List[Item]] = Field(default=None, description="A list of items in the transaction.")
    contexts: Optional[List[Context]] = Field(default=None, description="A list of additional information about the item.")
    breakdowns: Optional[List[Breakdown]] = Field(default=None, description="A list of breakdowns that provide details on how the total amount is calculated for the transaction.")
    __properties: ClassVar[List[str]] = ["sellingPartnerMetadata", "relatedIdentifiers", "transactionType", "transactionId", "transactionStatus", "description", "postedDate", "totalAmount", "marketplaceDetails", "items", "contexts", "breakdowns"]

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
        """Create an instance of Transaction from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of selling_partner_metadata
        if self.selling_partner_metadata:
            _dict['sellingPartnerMetadata'] = self.selling_partner_metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in related_identifiers (list)
        _items = []
        if self.related_identifiers:
            for _item_related_identifiers in self.related_identifiers:
                if _item_related_identifiers:
                    _items.append(_item_related_identifiers.to_dict())
            _dict['relatedIdentifiers'] = _items
        # override the default output from pydantic by calling `to_dict()` of total_amount
        if self.total_amount:
            _dict['totalAmount'] = self.total_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of marketplace_details
        if self.marketplace_details:
            _dict['marketplaceDetails'] = self.marketplace_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item_items in self.items:
                if _item_items:
                    _items.append(_item_items.to_dict())
            _dict['items'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in contexts (list)
        _items = []
        if self.contexts:
            for _item_contexts in self.contexts:
                if _item_contexts:
                    _items.append(_item_contexts.to_dict())
            _dict['contexts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in breakdowns (list)
        _items = []
        if self.breakdowns:
            for _item_breakdowns in self.breakdowns:
                if _item_breakdowns:
                    _items.append(_item_breakdowns.to_dict())
            _dict['breakdowns'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Transaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sellingPartnerMetadata": SellingPartnerMetadata.from_dict(obj["sellingPartnerMetadata"]) if obj.get("sellingPartnerMetadata") is not None else None,
            "relatedIdentifiers": [RelatedIdentifier.from_dict(_item) for _item in obj["relatedIdentifiers"]] if obj.get("relatedIdentifiers") is not None else None,
            "transactionType": obj.get("transactionType"),
            "transactionId": obj.get("transactionId"),
            "transactionStatus": obj.get("transactionStatus"),
            "description": obj.get("description"),
            "postedDate": obj.get("postedDate"),
            "totalAmount": Currency.from_dict(obj["totalAmount"]) if obj.get("totalAmount") is not None else None,
            "marketplaceDetails": MarketplaceDetails.from_dict(obj["marketplaceDetails"]) if obj.get("marketplaceDetails") is not None else None,
            "items": [Item.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
            "contexts": [Context.from_dict(_item) for _item in obj["contexts"]] if obj.get("contexts") is not None else None,
            "breakdowns": [Breakdown.from_dict(_item) for _item in obj["breakdowns"]] if obj.get("breakdowns") is not None else None
        })
        return _obj


