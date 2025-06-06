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
from ._enums import *

__all__ = [
    'GetControlPanelResult',
    'AwaitableGetControlPanelResult',
    'get_control_panel',
    'get_control_panel_output',
]

@pulumi.output_type
class GetControlPanelResult:
    def __init__(__self__, control_panel_arn=None, default_control_panel=None, name=None, routing_control_count=None, status=None):
        if control_panel_arn and not isinstance(control_panel_arn, str):
            raise TypeError("Expected argument 'control_panel_arn' to be a str")
        pulumi.set(__self__, "control_panel_arn", control_panel_arn)
        if default_control_panel and not isinstance(default_control_panel, bool):
            raise TypeError("Expected argument 'default_control_panel' to be a bool")
        pulumi.set(__self__, "default_control_panel", default_control_panel)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if routing_control_count and not isinstance(routing_control_count, int):
            raise TypeError("Expected argument 'routing_control_count' to be a int")
        pulumi.set(__self__, "routing_control_count", routing_control_count)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="controlPanelArn")
    def control_panel_arn(self) -> Optional[builtins.str]:
        """
        The Amazon Resource Name (ARN) of the cluster.
        """
        return pulumi.get(self, "control_panel_arn")

    @property
    @pulumi.getter(name="defaultControlPanel")
    def default_control_panel(self) -> Optional[builtins.bool]:
        """
        A flag that Amazon Route 53 Application Recovery Controller sets to true to designate the default control panel for a cluster. When you create a cluster, Amazon Route 53 Application Recovery Controller creates a control panel, and sets this flag for that control panel. If you create a control panel yourself, this flag is set to false.
        """
        return pulumi.get(self, "default_control_panel")

    @property
    @pulumi.getter
    def name(self) -> Optional[builtins.str]:
        """
        The name of the control panel. You can use any non-white space character in the name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="routingControlCount")
    def routing_control_count(self) -> Optional[builtins.int]:
        """
        Count of associated routing controls
        """
        return pulumi.get(self, "routing_control_count")

    @property
    @pulumi.getter
    def status(self) -> Optional['ControlPanelStatus']:
        """
        The deployment status of control panel. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.
        """
        return pulumi.get(self, "status")


class AwaitableGetControlPanelResult(GetControlPanelResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetControlPanelResult(
            control_panel_arn=self.control_panel_arn,
            default_control_panel=self.default_control_panel,
            name=self.name,
            routing_control_count=self.routing_control_count,
            status=self.status)


def get_control_panel(control_panel_arn: Optional[builtins.str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetControlPanelResult:
    """
    AWS Route53 Recovery Control Control Panel resource schema .


    :param builtins.str control_panel_arn: The Amazon Resource Name (ARN) of the cluster.
    """
    __args__ = dict()
    __args__['controlPanelArn'] = control_panel_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:route53recoverycontrol:getControlPanel', __args__, opts=opts, typ=GetControlPanelResult).value

    return AwaitableGetControlPanelResult(
        control_panel_arn=pulumi.get(__ret__, 'control_panel_arn'),
        default_control_panel=pulumi.get(__ret__, 'default_control_panel'),
        name=pulumi.get(__ret__, 'name'),
        routing_control_count=pulumi.get(__ret__, 'routing_control_count'),
        status=pulumi.get(__ret__, 'status'))
def get_control_panel_output(control_panel_arn: Optional[pulumi.Input[builtins.str]] = None,
                             opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetControlPanelResult]:
    """
    AWS Route53 Recovery Control Control Panel resource schema .


    :param builtins.str control_panel_arn: The Amazon Resource Name (ARN) of the cluster.
    """
    __args__ = dict()
    __args__['controlPanelArn'] = control_panel_arn
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:route53recoverycontrol:getControlPanel', __args__, opts=opts, typ=GetControlPanelResult)
    return __ret__.apply(lambda __response__: GetControlPanelResult(
        control_panel_arn=pulumi.get(__response__, 'control_panel_arn'),
        default_control_panel=pulumi.get(__response__, 'default_control_panel'),
        name=pulumi.get(__response__, 'name'),
        routing_control_count=pulumi.get(__response__, 'routing_control_count'),
        status=pulumi.get(__response__, 'status')))
