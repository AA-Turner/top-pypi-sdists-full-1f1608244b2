# coding: utf-8

# flake8: noqa
"""
    Snowflake Notification Integration API.

    The Snowflake Notification Integration API is a REST API that you can use to access, update, and perform certain actions on Notification Integration resource in a Snowflake database.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: support@snowflake.com
    Generated by: https://openapi-generator.tech

    Do not edit this file manually.
"""

from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from snowflake.core.notification_integration._generated.api.notification_integration_api import NotificationIntegrationApi
# import ApiClient
from snowflake.core.notification_integration._generated.api_client import ApiClient
from snowflake.core.notification_integration._generated.configuration import Configuration
# import models into sdk package
from snowflake.core.notification_integration._generated.models.error_response import ErrorResponse
from snowflake.core.notification_integration._generated.models.notification_email import NotificationEmail
from snowflake.core.notification_integration._generated.models.notification_hook import NotificationHook
from snowflake.core.notification_integration._generated.models.notification_integration import NotificationIntegration
from snowflake.core.notification_integration._generated.models.notification_queue_aws_sns_outbound import NotificationQueueAwsSnsOutbound
from snowflake.core.notification_integration._generated.models.notification_queue_azure_event_grid_inbound import NotificationQueueAzureEventGridInbound
from snowflake.core.notification_integration._generated.models.notification_queue_azure_event_grid_outbound import NotificationQueueAzureEventGridOutbound
from snowflake.core.notification_integration._generated.models.notification_queue_gcp_pubsub_inbound import NotificationQueueGcpPubsubInbound
from snowflake.core.notification_integration._generated.models.notification_queue_gcp_pubsub_outbound import NotificationQueueGcpPubsubOutbound
from snowflake.core.notification_integration._generated.models.notification_webhook import NotificationWebhook
from snowflake.core.notification_integration._generated.models.success_accepted_response import SuccessAcceptedResponse
from snowflake.core.notification_integration._generated.models.success_response import SuccessResponse
from snowflake.core.notification_integration._generated.models.webhook_secret import WebhookSecret
