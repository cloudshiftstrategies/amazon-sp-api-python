# coding: utf-8

"""
    Selling Partner API for Replenishment

    The Selling Partner API for Replenishment (Replenishment API) provides programmatic access to replenishment program metrics and offers. These programs provide recurring delivery of any replenishable item at a frequency chosen by the customer.  The Replenishment API is available worldwide wherever Amazon Subscribe & Save is available or is supported. The API is available to vendors and FBA selling partners.

    The version of the OpenAPI document: 2022-11-07
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from py_sp_api.generated.replenishment_2022_11_07.models.time_interval import TimeInterval
from typing import Optional, Set
from typing_extensions import Self

class ListOfferMetricsResponseOffer(BaseModel):
    """
    An object which contains offer metrics.
    """ # noqa: E501
    asin: Optional[StrictStr] = Field(default=None, description="The Amazon Standard Identification Number (ASIN).")
    not_delivered_due_to_oos: Optional[Union[Annotated[float, Field(le=1E+2, strict=True, ge=0)], Annotated[int, Field(le=100, strict=True, ge=0)]]] = Field(default=None, description="The percentage of items that were not shipped out of the total shipped units over a period of time due to being out of stock. Applicable to PERFORMANCE timePeriodType.", alias="notDeliveredDueToOOS")
    total_subscriptions_revenue: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="The revenue generated from subscriptions over a period of time. Applicable to PERFORMANCE timePeriodType.", alias="totalSubscriptionsRevenue")
    shipped_subscription_units: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="The number of units shipped to the subscribers over a period of time. Applicable to PERFORMANCE timePeriodType.", alias="shippedSubscriptionUnits")
    active_subscriptions: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="The number of active subscriptions present at the end of the period. Applicable to PERFORMANCE timePeriodType.", alias="activeSubscriptions")
    revenue_penetration: Optional[Union[Annotated[float, Field(le=1E+2, strict=True, ge=0)], Annotated[int, Field(le=100, strict=True, ge=0)]]] = Field(default=None, description="The percentage of total program revenue out of total product revenue. Applicable to PERFORMANCE timePeriodType.", alias="revenuePenetration")
    lost_revenue_due_to_oos: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="The revenue that would have been generated had there not been out of stock. Applicable to PERFORMANCE timePeriodType.", alias="lostRevenueDueToOOS")
    coupons_revenue_penetration: Optional[Union[Annotated[float, Field(le=1E+2, strict=True, ge=0)], Annotated[int, Field(le=100, strict=True, ge=0)]]] = Field(default=None, description="The percentage of revenue from ASINs with coupons out of total revenue from all ASINs. Applicable to PERFORMANCE timePeriodType.", alias="couponsRevenuePenetration")
    share_of_coupon_subscriptions: Optional[Union[Annotated[float, Field(le=1E+2, strict=True, ge=0)], Annotated[int, Field(le=100, strict=True, ge=0)]]] = Field(default=None, description="The percentage of new subscriptions acquired through coupons. Applicable to PERFORMANCE timePeriodType.", alias="shareOfCouponSubscriptions")
    next30_day_total_subscriptions_revenue: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="The forecasted total subscription revenue for the next 30 days. Applicable to FORECAST timePeriodType.", alias="next30DayTotalSubscriptionsRevenue")
    next60_day_total_subscriptions_revenue: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="The forecasted total subscription revenue for the next 60 days. Applicable to FORECAST timePeriodType.", alias="next60DayTotalSubscriptionsRevenue")
    next90_day_total_subscriptions_revenue: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="The forecasted total subscription revenue for the next 90 days. Applicable to FORECAST timePeriodType.", alias="next90DayTotalSubscriptionsRevenue")
    next30_day_shipped_subscription_units: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="The forecasted shipped subscription units for the next 30 days. Applicable to FORECAST timePeriodType.", alias="next30DayShippedSubscriptionUnits")
    next60_day_shipped_subscription_units: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="The forecasted shipped subscription units for the next 60 days. Applicable to FORECAST timePeriodType.", alias="next60DayShippedSubscriptionUnits")
    next90_day_shipped_subscription_units: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="The forecasted shipped subscription units for the next 90 days. Applicable to FORECAST timePeriodType.", alias="next90DayShippedSubscriptionUnits")
    time_interval: Optional[TimeInterval] = Field(default=None, alias="timeInterval")
    currency_code: Optional[StrictStr] = Field(default=None, description="The currency code in ISO 4217 format.", alias="currencyCode")
    __properties: ClassVar[List[str]] = ["asin", "notDeliveredDueToOOS", "totalSubscriptionsRevenue", "shippedSubscriptionUnits", "activeSubscriptions", "revenuePenetration", "lostRevenueDueToOOS", "couponsRevenuePenetration", "shareOfCouponSubscriptions", "next30DayTotalSubscriptionsRevenue", "next60DayTotalSubscriptionsRevenue", "next90DayTotalSubscriptionsRevenue", "next30DayShippedSubscriptionUnits", "next60DayShippedSubscriptionUnits", "next90DayShippedSubscriptionUnits", "timeInterval", "currencyCode"]

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
        """Create an instance of ListOfferMetricsResponseOffer from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of time_interval
        if self.time_interval:
            _dict['timeInterval'] = self.time_interval.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListOfferMetricsResponseOffer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "asin": obj.get("asin"),
            "notDeliveredDueToOOS": obj.get("notDeliveredDueToOOS"),
            "totalSubscriptionsRevenue": obj.get("totalSubscriptionsRevenue"),
            "shippedSubscriptionUnits": obj.get("shippedSubscriptionUnits"),
            "activeSubscriptions": obj.get("activeSubscriptions"),
            "revenuePenetration": obj.get("revenuePenetration"),
            "lostRevenueDueToOOS": obj.get("lostRevenueDueToOOS"),
            "couponsRevenuePenetration": obj.get("couponsRevenuePenetration"),
            "shareOfCouponSubscriptions": obj.get("shareOfCouponSubscriptions"),
            "next30DayTotalSubscriptionsRevenue": obj.get("next30DayTotalSubscriptionsRevenue"),
            "next60DayTotalSubscriptionsRevenue": obj.get("next60DayTotalSubscriptionsRevenue"),
            "next90DayTotalSubscriptionsRevenue": obj.get("next90DayTotalSubscriptionsRevenue"),
            "next30DayShippedSubscriptionUnits": obj.get("next30DayShippedSubscriptionUnits"),
            "next60DayShippedSubscriptionUnits": obj.get("next60DayShippedSubscriptionUnits"),
            "next90DayShippedSubscriptionUnits": obj.get("next90DayShippedSubscriptionUnits"),
            "timeInterval": TimeInterval.from_dict(obj["timeInterval"]) if obj.get("timeInterval") is not None else None,
            "currencyCode": obj.get("currencyCode")
        })
        return _obj


