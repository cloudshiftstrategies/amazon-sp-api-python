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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.address import Address
from typing import Optional, Set
from typing_extensions import Self

class InboundPlanSummary(BaseModel):
    """
    A light-weight inbound plan.
    """ # noqa: E501
    created_at: datetime = Field(description="The time at which the inbound plan was created. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format with pattern `yyyy-MM-ddTHH:mm:ssZ`.", alias="createdAt")
    inbound_plan_id: Annotated[str, Field(min_length=38, strict=True, max_length=38)] = Field(description="Identifier of an inbound plan.", alias="inboundPlanId")
    last_updated_at: datetime = Field(description="The time at which the inbound plan was last updated. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format with pattern `yyyy-MM-ddTHH:mm:ssZ`.", alias="lastUpdatedAt")
    marketplace_ids: List[Annotated[str, Field(min_length=1, strict=True, max_length=20)]] = Field(description="A list of marketplace IDs.", alias="marketplaceIds")
    name: StrictStr = Field(description="Human-readable name of the inbound plan.")
    source_address: Address = Field(alias="sourceAddress")
    status: Annotated[str, Field(min_length=1, strict=True, max_length=1024)] = Field(description="The current status of the inbound plan. Possible values: `ACTIVE`, `VOIDED`, `SHIPPED`, `ERRORED`.")
    __properties: ClassVar[List[str]] = ["createdAt", "inboundPlanId", "lastUpdatedAt", "marketplaceIds", "name", "sourceAddress", "status"]

    @field_validator('inbound_plan_id')
    def inbound_plan_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9-]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9-]*$/")
        return value

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
        """Create an instance of InboundPlanSummary from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of source_address
        if self.source_address:
            _dict['sourceAddress'] = self.source_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InboundPlanSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "createdAt": obj.get("createdAt"),
            "inboundPlanId": obj.get("inboundPlanId"),
            "lastUpdatedAt": obj.get("lastUpdatedAt"),
            "marketplaceIds": obj.get("marketplaceIds"),
            "name": obj.get("name"),
            "sourceAddress": Address.from_dict(obj["sourceAddress"]) if obj.get("sourceAddress") is not None else None,
            "status": obj.get("status")
        })
        return _obj


