# coding: utf-8

"""
    Selling Partner API for Reports

    Effective **June 27, 2024**, the Selling Partner API for Reports v2020-09-04 will no longer be available and all calls to it will fail. Integrations that rely on the Reports API must migrate to [Reports v2021-06-30](https://developer-docs.amazon.com/sp-api/docs/reports-api-v2021-06-30-reference) to avoid service disruption.

    The version of the OpenAPI document: 2020-09-04
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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class CreateReportSpecification(BaseModel):
    """
    CreateReportSpecification
    """ # noqa: E501
    report_options: Optional[Dict[str, StrictStr]] = Field(default=None, description="Additional information passed to reports. This varies by report type.", alias="reportOptions")
    report_type: StrictStr = Field(description="The report type.", alias="reportType")
    data_start_time: Optional[datetime] = Field(default=None, description="The start of a date and time range, in ISO 8601 date time format, used for selecting the data to report. The default is now. The value must be prior to or equal to the current date and time. Not all report types make use of this.", alias="dataStartTime")
    data_end_time: Optional[datetime] = Field(default=None, description="The end of a date and time range, in ISO 8601 date time format, used for selecting the data to report. The default is now. The value must be prior to or equal to the current date and time. Not all report types make use of this.", alias="dataEndTime")
    marketplace_ids: Annotated[List[StrictStr], Field(min_length=1, max_length=25)] = Field(description="A list of marketplace identifiers. The report document's contents will contain data for all of the specified marketplaces, unless the report type indicates otherwise.", alias="marketplaceIds")
    __properties: ClassVar[List[str]] = ["reportOptions", "reportType", "dataStartTime", "dataEndTime", "marketplaceIds"]

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
        """Create an instance of CreateReportSpecification from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateReportSpecification from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "reportOptions": obj.get("reportOptions"),
            "reportType": obj.get("reportType"),
            "dataStartTime": obj.get("dataStartTime"),
            "dataEndTime": obj.get("dataEndTime"),
            "marketplaceIds": obj.get("marketplaceIds")
        })
        return _obj


