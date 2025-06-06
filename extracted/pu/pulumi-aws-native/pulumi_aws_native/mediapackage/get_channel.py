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

__all__ = [
    'GetChannelResult',
    'AwaitableGetChannelResult',
    'get_channel',
    'get_channel_output',
]

@pulumi.output_type
class GetChannelResult:
    def __init__(__self__, arn=None, description=None, egress_access_logs=None, hls_ingest=None, ingress_access_logs=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if egress_access_logs and not isinstance(egress_access_logs, dict):
            raise TypeError("Expected argument 'egress_access_logs' to be a dict")
        pulumi.set(__self__, "egress_access_logs", egress_access_logs)
        if hls_ingest and not isinstance(hls_ingest, dict):
            raise TypeError("Expected argument 'hls_ingest' to be a dict")
        pulumi.set(__self__, "hls_ingest", hls_ingest)
        if ingress_access_logs and not isinstance(ingress_access_logs, dict):
            raise TypeError("Expected argument 'ingress_access_logs' to be a dict")
        pulumi.set(__self__, "ingress_access_logs", ingress_access_logs)

    @property
    @pulumi.getter
    def arn(self) -> Optional[builtins.str]:
        """
        The Amazon Resource Name (ARN) assigned to the Channel.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> Optional[builtins.str]:
        """
        A short text description of the Channel.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="egressAccessLogs")
    def egress_access_logs(self) -> Optional['outputs.ChannelLogConfiguration']:
        """
        The configuration parameters for egress access logging.
        """
        return pulumi.get(self, "egress_access_logs")

    @property
    @pulumi.getter(name="hlsIngest")
    def hls_ingest(self) -> Optional['outputs.ChannelHlsIngest']:
        """
        An HTTP Live Streaming (HLS) ingest resource configuration.
        """
        return pulumi.get(self, "hls_ingest")

    @property
    @pulumi.getter(name="ingressAccessLogs")
    def ingress_access_logs(self) -> Optional['outputs.ChannelLogConfiguration']:
        """
        The configuration parameters for egress access logging.
        """
        return pulumi.get(self, "ingress_access_logs")


class AwaitableGetChannelResult(GetChannelResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetChannelResult(
            arn=self.arn,
            description=self.description,
            egress_access_logs=self.egress_access_logs,
            hls_ingest=self.hls_ingest,
            ingress_access_logs=self.ingress_access_logs)


def get_channel(id: Optional[builtins.str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetChannelResult:
    """
    Resource schema for AWS::MediaPackage::Channel


    :param builtins.str id: The ID of the Channel.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:mediapackage:getChannel', __args__, opts=opts, typ=GetChannelResult).value

    return AwaitableGetChannelResult(
        arn=pulumi.get(__ret__, 'arn'),
        description=pulumi.get(__ret__, 'description'),
        egress_access_logs=pulumi.get(__ret__, 'egress_access_logs'),
        hls_ingest=pulumi.get(__ret__, 'hls_ingest'),
        ingress_access_logs=pulumi.get(__ret__, 'ingress_access_logs'))
def get_channel_output(id: Optional[pulumi.Input[builtins.str]] = None,
                       opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetChannelResult]:
    """
    Resource schema for AWS::MediaPackage::Channel


    :param builtins.str id: The ID of the Channel.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:mediapackage:getChannel', __args__, opts=opts, typ=GetChannelResult)
    return __ret__.apply(lambda __response__: GetChannelResult(
        arn=pulumi.get(__response__, 'arn'),
        description=pulumi.get(__response__, 'description'),
        egress_access_logs=pulumi.get(__response__, 'egress_access_logs'),
        hls_ingest=pulumi.get(__response__, 'hls_ingest'),
        ingress_access_logs=pulumi.get(__response__, 'ingress_access_logs')))
