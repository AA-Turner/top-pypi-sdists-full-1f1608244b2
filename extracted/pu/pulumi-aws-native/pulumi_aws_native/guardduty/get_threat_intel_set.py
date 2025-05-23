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
from .. import outputs as _root_outputs

__all__ = [
    'GetThreatIntelSetResult',
    'AwaitableGetThreatIntelSetResult',
    'get_threat_intel_set',
    'get_threat_intel_set_output',
]

@pulumi.output_type
class GetThreatIntelSetResult:
    def __init__(__self__, id=None, location=None, name=None, tags=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def id(self) -> Optional[builtins.str]:
        """
        The unique ID of the `threatIntelSet` .
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[builtins.str]:
        """
        The URI of the file that contains the ThreatIntelSet.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> Optional[builtins.str]:
        """
        A user-friendly ThreatIntelSet name displayed in all findings that are generated by activity that involves IP addresses included in this ThreatIntelSet.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        The tags to be added to a new threat list resource. Each tag consists of a key and an optional value, both of which you define.

        For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html) .
        """
        return pulumi.get(self, "tags")


class AwaitableGetThreatIntelSetResult(GetThreatIntelSetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetThreatIntelSetResult(
            id=self.id,
            location=self.location,
            name=self.name,
            tags=self.tags)


def get_threat_intel_set(detector_id: Optional[builtins.str] = None,
                         id: Optional[builtins.str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetThreatIntelSetResult:
    """
    Resource Type definition for AWS::GuardDuty::ThreatIntelSet


    :param builtins.str detector_id: The unique ID of the detector of the GuardDuty account for which you want to create a `ThreatIntelSet` .
           
           To find the `detectorId` in the current Region, see the
           Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
    :param builtins.str id: The unique ID of the `threatIntelSet` .
    """
    __args__ = dict()
    __args__['detectorId'] = detector_id
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:guardduty:getThreatIntelSet', __args__, opts=opts, typ=GetThreatIntelSetResult).value

    return AwaitableGetThreatIntelSetResult(
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        tags=pulumi.get(__ret__, 'tags'))
def get_threat_intel_set_output(detector_id: Optional[pulumi.Input[builtins.str]] = None,
                                id: Optional[pulumi.Input[builtins.str]] = None,
                                opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetThreatIntelSetResult]:
    """
    Resource Type definition for AWS::GuardDuty::ThreatIntelSet


    :param builtins.str detector_id: The unique ID of the detector of the GuardDuty account for which you want to create a `ThreatIntelSet` .
           
           To find the `detectorId` in the current Region, see the
           Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
    :param builtins.str id: The unique ID of the `threatIntelSet` .
    """
    __args__ = dict()
    __args__['detectorId'] = detector_id
    __args__['id'] = id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:guardduty:getThreatIntelSet', __args__, opts=opts, typ=GetThreatIntelSetResult)
    return __ret__.apply(lambda __response__: GetThreatIntelSetResult(
        id=pulumi.get(__response__, 'id'),
        location=pulumi.get(__response__, 'location'),
        name=pulumi.get(__response__, 'name'),
        tags=pulumi.get(__response__, 'tags')))
