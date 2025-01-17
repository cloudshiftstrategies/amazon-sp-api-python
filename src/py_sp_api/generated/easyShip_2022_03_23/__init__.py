# coding: utf-8

# flake8: noqa

"""
    Selling Partner API for Easy Ship

    The Selling Partner API for Easy Ship helps you build applications that help sellers manage and ship Amazon Easy Ship orders.  Your Easy Ship applications can:  * Get available time slots for packages to be scheduled for delivery.  * Schedule, reschedule, and cancel Easy Ship orders.  * Print labels, invoices, and warranties.  See the [Marketplace Support Table](doc:easyship-api-v2022-03-23-use-case-guide#marketplace-support-table) for the differences in Easy Ship operations by marketplace.

    The version of the OpenAPI document: 2022-03-23
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from py_sp_api.generated.easyShip_2022_03_23.api.easy_ship_api import EasyShipApi

# import ApiClient
from py_sp_api.generated.easyShip_2022_03_23.api_response import ApiResponse
from py_sp_api.generated.easyShip_2022_03_23.api_client import ApiClient
from py_sp_api.generated.easyShip_2022_03_23.configuration import Configuration
from py_sp_api.generated.easyShip_2022_03_23.exceptions import OpenApiException
from py_sp_api.generated.easyShip_2022_03_23.exceptions import ApiTypeError
from py_sp_api.generated.easyShip_2022_03_23.exceptions import ApiValueError
from py_sp_api.generated.easyShip_2022_03_23.exceptions import ApiKeyError
from py_sp_api.generated.easyShip_2022_03_23.exceptions import ApiAttributeError
from py_sp_api.generated.easyShip_2022_03_23.exceptions import ApiException

# import models into sdk package
from py_sp_api.generated.easyShip_2022_03_23.models.code import Code
from py_sp_api.generated.easyShip_2022_03_23.models.create_scheduled_package_request import CreateScheduledPackageRequest
from py_sp_api.generated.easyShip_2022_03_23.models.create_scheduled_packages_request import CreateScheduledPackagesRequest
from py_sp_api.generated.easyShip_2022_03_23.models.create_scheduled_packages_response import CreateScheduledPackagesResponse
from py_sp_api.generated.easyShip_2022_03_23.models.dimensions import Dimensions
from py_sp_api.generated.easyShip_2022_03_23.models.error import Error
from py_sp_api.generated.easyShip_2022_03_23.models.error_list import ErrorList
from py_sp_api.generated.easyShip_2022_03_23.models.handover_method import HandoverMethod
from py_sp_api.generated.easyShip_2022_03_23.models.invoice_data import InvoiceData
from py_sp_api.generated.easyShip_2022_03_23.models.item import Item
from py_sp_api.generated.easyShip_2022_03_23.models.label_format import LabelFormat
from py_sp_api.generated.easyShip_2022_03_23.models.list_handover_slots_request import ListHandoverSlotsRequest
from py_sp_api.generated.easyShip_2022_03_23.models.list_handover_slots_response import ListHandoverSlotsResponse
from py_sp_api.generated.easyShip_2022_03_23.models.order_schedule_details import OrderScheduleDetails
from py_sp_api.generated.easyShip_2022_03_23.models.package import Package
from py_sp_api.generated.easyShip_2022_03_23.models.package_details import PackageDetails
from py_sp_api.generated.easyShip_2022_03_23.models.package_status import PackageStatus
from py_sp_api.generated.easyShip_2022_03_23.models.packages import Packages
from py_sp_api.generated.easyShip_2022_03_23.models.rejected_order import RejectedOrder
from py_sp_api.generated.easyShip_2022_03_23.models.scheduled_package_id import ScheduledPackageId
from py_sp_api.generated.easyShip_2022_03_23.models.time_slot import TimeSlot
from py_sp_api.generated.easyShip_2022_03_23.models.tracking_details import TrackingDetails
from py_sp_api.generated.easyShip_2022_03_23.models.unit_of_length import UnitOfLength
from py_sp_api.generated.easyShip_2022_03_23.models.unit_of_weight import UnitOfWeight
from py_sp_api.generated.easyShip_2022_03_23.models.update_package_details import UpdatePackageDetails
from py_sp_api.generated.easyShip_2022_03_23.models.update_scheduled_packages_request import UpdateScheduledPackagesRequest
from py_sp_api.generated.easyShip_2022_03_23.models.weight import Weight

from .base_client import SPAPIClient
