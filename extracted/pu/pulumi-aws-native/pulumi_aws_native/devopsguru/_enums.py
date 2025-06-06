# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
import pulumi
from enum import Enum

__all__ = [
    'NotificationChannelInsightSeverity',
    'NotificationChannelNotificationMessageType',
    'ResourceCollectionType',
]


@pulumi.type_token("aws-native:devopsguru:NotificationChannelInsightSeverity")
class NotificationChannelInsightSeverity(builtins.str, Enum):
    """
    DevOps Guru Insight Severity Enum
    """
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


@pulumi.type_token("aws-native:devopsguru:NotificationChannelNotificationMessageType")
class NotificationChannelNotificationMessageType(builtins.str, Enum):
    """
    DevOps Guru NotificationMessageType Enum
    """
    NEW_INSIGHT = "NEW_INSIGHT"
    CLOSED_INSIGHT = "CLOSED_INSIGHT"
    NEW_ASSOCIATION = "NEW_ASSOCIATION"
    SEVERITY_UPGRADED = "SEVERITY_UPGRADED"
    NEW_RECOMMENDATION = "NEW_RECOMMENDATION"


@pulumi.type_token("aws-native:devopsguru:ResourceCollectionType")
class ResourceCollectionType(builtins.str, Enum):
    """
    The type of ResourceCollection
    """
    AWS_CLOUD_FORMATION = "AWS_CLOUD_FORMATION"
    AWS_TAGS = "AWS_TAGS"
