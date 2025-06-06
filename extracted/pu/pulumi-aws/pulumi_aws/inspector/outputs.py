# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities

__all__ = [
    'AssessmentTemplateEventSubscription',
]

@pulumi.output_type
class AssessmentTemplateEventSubscription(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "topicArn":
            suggest = "topic_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AssessmentTemplateEventSubscription. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AssessmentTemplateEventSubscription.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AssessmentTemplateEventSubscription.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 event: builtins.str,
                 topic_arn: builtins.str):
        """
        :param builtins.str event: The event for which you want to receive SNS notifications. Valid values are `ASSESSMENT_RUN_STARTED`, `ASSESSMENT_RUN_COMPLETED`, `ASSESSMENT_RUN_STATE_CHANGED`, and `FINDING_REPORTED`.
        :param builtins.str topic_arn: The ARN of the SNS topic to which notifications are sent.
        """
        pulumi.set(__self__, "event", event)
        pulumi.set(__self__, "topic_arn", topic_arn)

    @property
    @pulumi.getter
    def event(self) -> builtins.str:
        """
        The event for which you want to receive SNS notifications. Valid values are `ASSESSMENT_RUN_STARTED`, `ASSESSMENT_RUN_COMPLETED`, `ASSESSMENT_RUN_STATE_CHANGED`, and `FINDING_REPORTED`.
        """
        return pulumi.get(self, "event")

    @property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> builtins.str:
        """
        The ARN of the SNS topic to which notifications are sent.
        """
        return pulumi.get(self, "topic_arn")


