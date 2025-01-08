# coding: utf-8

"""
    Report v2021-06-30

    The Selling Partner API for Reports lets you retrieve and manage a variety of reports that can help selling partners manage their businesses.

    The version of the OpenAPI document: 2021-06-30
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.reports_2021_06_30.models.report import Report
from typing import Optional, Set
from typing_extensions import Self

class GetReportsResponse(BaseModel):
    """
    The response for the `getReports` operation.
    """ # noqa: E501
    reports: List[Report] = Field(description="A list of reports.")
    next_token: Optional[StrictStr] = Field(default=None, description="Returned when the number of results exceeds `pageSize`. To get the next page of results, call `getReports` with this token as the only parameter.", alias="nextToken")
    __properties: ClassVar[List[str]] = ["reports", "nextToken"]

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
        """Create an instance of GetReportsResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in reports (list)
        _items = []
        if self.reports:
            for _item_reports in self.reports:
                if _item_reports:
                    _items.append(_item_reports.to_dict())
            _dict['reports'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetReportsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "reports": [Report.from_dict(_item) for _item in obj["reports"]] if obj.get("reports") is not None else None,
            "nextToken": obj.get("nextToken")
        })
        return _obj


