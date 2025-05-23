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
from . import outputs
from ._enums import *

__all__ = [
    'GetMonitoringSubscriptionResult',
    'AwaitableGetMonitoringSubscriptionResult',
    'get_monitoring_subscription',
    'get_monitoring_subscription_output',
]

@pulumi.output_type
class GetMonitoringSubscriptionResult:
    def __init__(__self__, monitoring_subscription=None):
        if monitoring_subscription and not isinstance(monitoring_subscription, dict):
            raise TypeError("Expected argument 'monitoring_subscription' to be a dict")
        pulumi.set(__self__, "monitoring_subscription", monitoring_subscription)

    @property
    @pulumi.getter(name="monitoringSubscription")
    def monitoring_subscription(self) -> Optional['outputs.MonitoringSubscription']:
        """
        A subscription configuration for additional CloudWatch metrics.
        """
        return pulumi.get(self, "monitoring_subscription")


class AwaitableGetMonitoringSubscriptionResult(GetMonitoringSubscriptionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMonitoringSubscriptionResult(
            monitoring_subscription=self.monitoring_subscription)


def get_monitoring_subscription(distribution_id: Optional[builtins.str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMonitoringSubscriptionResult:
    """
    A monitoring subscription. This structure contains information about whether additional CloudWatch metrics are enabled for a given CloudFront distribution.


    :param builtins.str distribution_id: The ID of the distribution that you are enabling metrics for.
    """
    __args__ = dict()
    __args__['distributionId'] = distribution_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:cloudfront:getMonitoringSubscription', __args__, opts=opts, typ=GetMonitoringSubscriptionResult).value

    return AwaitableGetMonitoringSubscriptionResult(
        monitoring_subscription=pulumi.get(__ret__, 'monitoring_subscription'))
def get_monitoring_subscription_output(distribution_id: Optional[pulumi.Input[builtins.str]] = None,
                                       opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetMonitoringSubscriptionResult]:
    """
    A monitoring subscription. This structure contains information about whether additional CloudWatch metrics are enabled for a given CloudFront distribution.


    :param builtins.str distribution_id: The ID of the distribution that you are enabling metrics for.
    """
    __args__ = dict()
    __args__['distributionId'] = distribution_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:cloudfront:getMonitoringSubscription', __args__, opts=opts, typ=GetMonitoringSubscriptionResult)
    return __ret__.apply(lambda __response__: GetMonitoringSubscriptionResult(
        monitoring_subscription=pulumi.get(__response__, 'monitoring_subscription')))
