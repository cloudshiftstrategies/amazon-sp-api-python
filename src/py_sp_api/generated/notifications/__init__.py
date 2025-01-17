# coding: utf-8

# flake8: noqa

"""
    Selling Partner API for Notifications

    The Selling Partner API for Notifications lets you subscribe to notifications that are relevant to a selling partner's business. Using this API you can create a destination to receive notifications, subscribe to notifications, delete notification subscriptions, and more.  For more information, refer to the [Notifications Use Case Guide](https://developer-docs.amazon.com/sp-api/docs/notifications-api-v1-use-case-guide).

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from py_sp_api.generated.notifications.api.notifications_api import NotificationsApi

# import ApiClient
from py_sp_api.generated.notifications.api_response import ApiResponse
from py_sp_api.generated.notifications.api_client import ApiClient
from py_sp_api.generated.notifications.configuration import Configuration
from py_sp_api.generated.notifications.exceptions import OpenApiException
from py_sp_api.generated.notifications.exceptions import ApiTypeError
from py_sp_api.generated.notifications.exceptions import ApiValueError
from py_sp_api.generated.notifications.exceptions import ApiKeyError
from py_sp_api.generated.notifications.exceptions import ApiAttributeError
from py_sp_api.generated.notifications.exceptions import ApiException

# import models into sdk package
from py_sp_api.generated.notifications.models.aggregation_filter import AggregationFilter
from py_sp_api.generated.notifications.models.aggregation_settings import AggregationSettings
from py_sp_api.generated.notifications.models.aggregation_time_period import AggregationTimePeriod
from py_sp_api.generated.notifications.models.create_destination_request import CreateDestinationRequest
from py_sp_api.generated.notifications.models.create_destination_response import CreateDestinationResponse
from py_sp_api.generated.notifications.models.create_subscription_request import CreateSubscriptionRequest
from py_sp_api.generated.notifications.models.create_subscription_response import CreateSubscriptionResponse
from py_sp_api.generated.notifications.models.delete_destination_response import DeleteDestinationResponse
from py_sp_api.generated.notifications.models.delete_subscription_by_id_response import DeleteSubscriptionByIdResponse
from py_sp_api.generated.notifications.models.destination import Destination
from py_sp_api.generated.notifications.models.destination_resource import DestinationResource
from py_sp_api.generated.notifications.models.destination_resource_specification import DestinationResourceSpecification
from py_sp_api.generated.notifications.models.error import Error
from py_sp_api.generated.notifications.models.event_bridge_resource import EventBridgeResource
from py_sp_api.generated.notifications.models.event_bridge_resource_specification import EventBridgeResourceSpecification
from py_sp_api.generated.notifications.models.event_filter import EventFilter
from py_sp_api.generated.notifications.models.get_destination_response import GetDestinationResponse
from py_sp_api.generated.notifications.models.get_destinations_response import GetDestinationsResponse
from py_sp_api.generated.notifications.models.get_subscription_by_id_response import GetSubscriptionByIdResponse
from py_sp_api.generated.notifications.models.get_subscription_response import GetSubscriptionResponse
from py_sp_api.generated.notifications.models.marketplace_filter import MarketplaceFilter
from py_sp_api.generated.notifications.models.order_change_type_enum import OrderChangeTypeEnum
from py_sp_api.generated.notifications.models.order_change_type_filter import OrderChangeTypeFilter
from py_sp_api.generated.notifications.models.processing_directive import ProcessingDirective
from py_sp_api.generated.notifications.models.sqs_resource import SqsResource
from py_sp_api.generated.notifications.models.subscription import Subscription

from .base_client import SPAPIClient
