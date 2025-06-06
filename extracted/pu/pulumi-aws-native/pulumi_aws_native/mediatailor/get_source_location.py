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
from .. import outputs as _root_outputs
from ._enums import *

__all__ = [
    'GetSourceLocationResult',
    'AwaitableGetSourceLocationResult',
    'get_source_location',
    'get_source_location_output',
]

@pulumi.output_type
class GetSourceLocationResult:
    def __init__(__self__, access_configuration=None, arn=None, default_segment_delivery_configuration=None, http_configuration=None, segment_delivery_configurations=None, tags=None):
        if access_configuration and not isinstance(access_configuration, dict):
            raise TypeError("Expected argument 'access_configuration' to be a dict")
        pulumi.set(__self__, "access_configuration", access_configuration)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if default_segment_delivery_configuration and not isinstance(default_segment_delivery_configuration, dict):
            raise TypeError("Expected argument 'default_segment_delivery_configuration' to be a dict")
        pulumi.set(__self__, "default_segment_delivery_configuration", default_segment_delivery_configuration)
        if http_configuration and not isinstance(http_configuration, dict):
            raise TypeError("Expected argument 'http_configuration' to be a dict")
        pulumi.set(__self__, "http_configuration", http_configuration)
        if segment_delivery_configurations and not isinstance(segment_delivery_configurations, list):
            raise TypeError("Expected argument 'segment_delivery_configurations' to be a list")
        pulumi.set(__self__, "segment_delivery_configurations", segment_delivery_configurations)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="accessConfiguration")
    def access_configuration(self) -> Optional['outputs.SourceLocationAccessConfiguration']:
        """
        The access configuration for the source location.
        """
        return pulumi.get(self, "access_configuration")

    @property
    @pulumi.getter
    def arn(self) -> Optional[builtins.str]:
        """
        <p>The ARN of the source location.</p>
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="defaultSegmentDeliveryConfiguration")
    def default_segment_delivery_configuration(self) -> Optional['outputs.SourceLocationDefaultSegmentDeliveryConfiguration']:
        """
        The default segment delivery configuration.
        """
        return pulumi.get(self, "default_segment_delivery_configuration")

    @property
    @pulumi.getter(name="httpConfiguration")
    def http_configuration(self) -> Optional['outputs.SourceLocationHttpConfiguration']:
        """
        The HTTP configuration for the source location.
        """
        return pulumi.get(self, "http_configuration")

    @property
    @pulumi.getter(name="segmentDeliveryConfigurations")
    def segment_delivery_configurations(self) -> Optional[Sequence['outputs.SourceLocationSegmentDeliveryConfiguration']]:
        """
        <p>A list of the segment delivery configurations associated with this resource.</p>
        """
        return pulumi.get(self, "segment_delivery_configurations")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        The tags to assign to the source location.
        """
        return pulumi.get(self, "tags")


class AwaitableGetSourceLocationResult(GetSourceLocationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSourceLocationResult(
            access_configuration=self.access_configuration,
            arn=self.arn,
            default_segment_delivery_configuration=self.default_segment_delivery_configuration,
            http_configuration=self.http_configuration,
            segment_delivery_configurations=self.segment_delivery_configurations,
            tags=self.tags)


def get_source_location(source_location_name: Optional[builtins.str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSourceLocationResult:
    """
    Definition of AWS::MediaTailor::SourceLocation Resource Type


    :param builtins.str source_location_name: The name of the source location.
    """
    __args__ = dict()
    __args__['sourceLocationName'] = source_location_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:mediatailor:getSourceLocation', __args__, opts=opts, typ=GetSourceLocationResult).value

    return AwaitableGetSourceLocationResult(
        access_configuration=pulumi.get(__ret__, 'access_configuration'),
        arn=pulumi.get(__ret__, 'arn'),
        default_segment_delivery_configuration=pulumi.get(__ret__, 'default_segment_delivery_configuration'),
        http_configuration=pulumi.get(__ret__, 'http_configuration'),
        segment_delivery_configurations=pulumi.get(__ret__, 'segment_delivery_configurations'),
        tags=pulumi.get(__ret__, 'tags'))
def get_source_location_output(source_location_name: Optional[pulumi.Input[builtins.str]] = None,
                               opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetSourceLocationResult]:
    """
    Definition of AWS::MediaTailor::SourceLocation Resource Type


    :param builtins.str source_location_name: The name of the source location.
    """
    __args__ = dict()
    __args__['sourceLocationName'] = source_location_name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:mediatailor:getSourceLocation', __args__, opts=opts, typ=GetSourceLocationResult)
    return __ret__.apply(lambda __response__: GetSourceLocationResult(
        access_configuration=pulumi.get(__response__, 'access_configuration'),
        arn=pulumi.get(__response__, 'arn'),
        default_segment_delivery_configuration=pulumi.get(__response__, 'default_segment_delivery_configuration'),
        http_configuration=pulumi.get(__response__, 'http_configuration'),
        segment_delivery_configurations=pulumi.get(__response__, 'segment_delivery_configurations'),
        tags=pulumi.get(__response__, 'tags')))
