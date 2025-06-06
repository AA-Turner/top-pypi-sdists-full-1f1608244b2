# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
import pulumi
from enum import Enum

__all__ = [
    'NotificationRuleDetailType',
    'NotificationRuleStatus',
]


@pulumi.type_token("aws-native:codestarnotifications:NotificationRuleDetailType")
class NotificationRuleDetailType(builtins.str, Enum):
    """
    The level of detail to include in the notifications for this resource. `BASIC` will include only the contents of the event as it would appear in Amazon CloudWatch. `FULL` will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created.
    """
    BASIC = "BASIC"
    FULL = "FULL"


@pulumi.type_token("aws-native:codestarnotifications:NotificationRuleStatus")
class NotificationRuleStatus(builtins.str, Enum):
    """
    The status of the notification rule. The default value is `ENABLED` . If the status is set to `DISABLED` , notifications aren't sent for the notification rule.
    """
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
