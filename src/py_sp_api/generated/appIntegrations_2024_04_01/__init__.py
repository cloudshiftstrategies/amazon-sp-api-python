# coding: utf-8

# flake8: noqa

"""
    The Selling Partner API for third party application integrations.

    With the AppIntegrations API v2024-04-01, you can send notifications to Amazon Selling Partners and display the notifications in Seller Central.

    The version of the OpenAPI document: 2024-04-01
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from py_sp_api.generated.appIntegrations_2024_04_01.api.app_integrations_api import AppIntegrationsApi

# import ApiClient
from py_sp_api.generated.appIntegrations_2024_04_01.api_response import ApiResponse
from py_sp_api.generated.appIntegrations_2024_04_01.api_client import ApiClient
from py_sp_api.generated.appIntegrations_2024_04_01.configuration import Configuration
from py_sp_api.generated.appIntegrations_2024_04_01.exceptions import OpenApiException
from py_sp_api.generated.appIntegrations_2024_04_01.exceptions import ApiTypeError
from py_sp_api.generated.appIntegrations_2024_04_01.exceptions import ApiValueError
from py_sp_api.generated.appIntegrations_2024_04_01.exceptions import ApiKeyError
from py_sp_api.generated.appIntegrations_2024_04_01.exceptions import ApiAttributeError
from py_sp_api.generated.appIntegrations_2024_04_01.exceptions import ApiException

# import models into sdk package
from py_sp_api.generated.appIntegrations_2024_04_01.models.create_notification_request import CreateNotificationRequest
from py_sp_api.generated.appIntegrations_2024_04_01.models.create_notification_response import CreateNotificationResponse
from py_sp_api.generated.appIntegrations_2024_04_01.models.delete_notifications_request import DeleteNotificationsRequest
from py_sp_api.generated.appIntegrations_2024_04_01.models.error import Error
from py_sp_api.generated.appIntegrations_2024_04_01.models.error_list import ErrorList
from py_sp_api.generated.appIntegrations_2024_04_01.models.record_action_feedback_request import RecordActionFeedbackRequest

from .base_client import SPAPIClient
