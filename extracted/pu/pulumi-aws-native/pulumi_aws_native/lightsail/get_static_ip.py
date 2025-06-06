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
    'GetStaticIpResult',
    'AwaitableGetStaticIpResult',
    'get_static_ip',
    'get_static_ip_output',
]

@pulumi.output_type
class GetStaticIpResult:
    def __init__(__self__, attached_to=None, ip_address=None, is_attached=None, static_ip_arn=None):
        if attached_to and not isinstance(attached_to, str):
            raise TypeError("Expected argument 'attached_to' to be a str")
        pulumi.set(__self__, "attached_to", attached_to)
        if ip_address and not isinstance(ip_address, str):
            raise TypeError("Expected argument 'ip_address' to be a str")
        pulumi.set(__self__, "ip_address", ip_address)
        if is_attached and not isinstance(is_attached, bool):
            raise TypeError("Expected argument 'is_attached' to be a bool")
        pulumi.set(__self__, "is_attached", is_attached)
        if static_ip_arn and not isinstance(static_ip_arn, str):
            raise TypeError("Expected argument 'static_ip_arn' to be a str")
        pulumi.set(__self__, "static_ip_arn", static_ip_arn)

    @property
    @pulumi.getter(name="attachedTo")
    def attached_to(self) -> Optional[builtins.str]:
        """
        The instance where the static IP is attached.
        """
        return pulumi.get(self, "attached_to")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[builtins.str]:
        """
        The static IP address.
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter(name="isAttached")
    def is_attached(self) -> Optional[builtins.bool]:
        """
        A Boolean value indicating whether the static IP is attached.
        """
        return pulumi.get(self, "is_attached")

    @property
    @pulumi.getter(name="staticIpArn")
    def static_ip_arn(self) -> Optional[builtins.str]:
        """
        The Amazon Resource Name (ARN) of the static IP (for example, `arn:aws:lightsail:us-east-2:123456789101:StaticIp/244ad76f-8aad-4741-809f-12345EXAMPLE` ).
        """
        return pulumi.get(self, "static_ip_arn")


class AwaitableGetStaticIpResult(GetStaticIpResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStaticIpResult(
            attached_to=self.attached_to,
            ip_address=self.ip_address,
            is_attached=self.is_attached,
            static_ip_arn=self.static_ip_arn)


def get_static_ip(static_ip_name: Optional[builtins.str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStaticIpResult:
    """
    Resource Type definition for AWS::Lightsail::StaticIp


    :param builtins.str static_ip_name: The name of the static IP address.
    """
    __args__ = dict()
    __args__['staticIpName'] = static_ip_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:lightsail:getStaticIp', __args__, opts=opts, typ=GetStaticIpResult).value

    return AwaitableGetStaticIpResult(
        attached_to=pulumi.get(__ret__, 'attached_to'),
        ip_address=pulumi.get(__ret__, 'ip_address'),
        is_attached=pulumi.get(__ret__, 'is_attached'),
        static_ip_arn=pulumi.get(__ret__, 'static_ip_arn'))
def get_static_ip_output(static_ip_name: Optional[pulumi.Input[builtins.str]] = None,
                         opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetStaticIpResult]:
    """
    Resource Type definition for AWS::Lightsail::StaticIp


    :param builtins.str static_ip_name: The name of the static IP address.
    """
    __args__ = dict()
    __args__['staticIpName'] = static_ip_name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:lightsail:getStaticIp', __args__, opts=opts, typ=GetStaticIpResult)
    return __ret__.apply(lambda __response__: GetStaticIpResult(
        attached_to=pulumi.get(__response__, 'attached_to'),
        ip_address=pulumi.get(__response__, 'ip_address'),
        is_attached=pulumi.get(__response__, 'is_attached'),
        static_ip_arn=pulumi.get(__response__, 'static_ip_arn')))
