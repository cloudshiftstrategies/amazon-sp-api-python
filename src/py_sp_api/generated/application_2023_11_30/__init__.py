# coding: utf-8

# flake8: noqa

"""
    Selling Partner API for Application Management

    The Selling Partner API for Application Management lets you programmatically update the client secret on registered applications.

    The version of the OpenAPI document: 2023-11-30
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from py_sp_api.generated.application_2023_11_30.api.applications_api import ApplicationsApi

# import ApiClient
from py_sp_api.generated.application_2023_11_30.api_response import ApiResponse
from py_sp_api.generated.application_2023_11_30.api_client import ApiClient
from py_sp_api.generated.application_2023_11_30.configuration import Configuration
from py_sp_api.generated.application_2023_11_30.exceptions import OpenApiException
from py_sp_api.generated.application_2023_11_30.exceptions import ApiTypeError
from py_sp_api.generated.application_2023_11_30.exceptions import ApiValueError
from py_sp_api.generated.application_2023_11_30.exceptions import ApiKeyError
from py_sp_api.generated.application_2023_11_30.exceptions import ApiAttributeError
from py_sp_api.generated.application_2023_11_30.exceptions import ApiException

# import models into sdk package
from py_sp_api.generated.application_2023_11_30.models.error import Error
from py_sp_api.generated.application_2023_11_30.models.error_list import ErrorList

from .base_client import SPAPIClient
