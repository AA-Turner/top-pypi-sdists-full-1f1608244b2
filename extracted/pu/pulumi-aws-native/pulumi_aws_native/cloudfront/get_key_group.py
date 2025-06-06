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
    'GetKeyGroupResult',
    'AwaitableGetKeyGroupResult',
    'get_key_group',
    'get_key_group_output',
]

@pulumi.output_type
class GetKeyGroupResult:
    def __init__(__self__, id=None, key_group_config=None, last_modified_time=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if key_group_config and not isinstance(key_group_config, dict):
            raise TypeError("Expected argument 'key_group_config' to be a dict")
        pulumi.set(__self__, "key_group_config", key_group_config)
        if last_modified_time and not isinstance(last_modified_time, str):
            raise TypeError("Expected argument 'last_modified_time' to be a str")
        pulumi.set(__self__, "last_modified_time", last_modified_time)

    @property
    @pulumi.getter
    def id(self) -> Optional[builtins.str]:
        """
        The identifier for the key group.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="keyGroupConfig")
    def key_group_config(self) -> Optional['outputs.KeyGroupConfig']:
        """
        The key group configuration.
        """
        return pulumi.get(self, "key_group_config")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[builtins.str]:
        """
        The date and time when the key group was last modified.
        """
        return pulumi.get(self, "last_modified_time")


class AwaitableGetKeyGroupResult(GetKeyGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKeyGroupResult(
            id=self.id,
            key_group_config=self.key_group_config,
            last_modified_time=self.last_modified_time)


def get_key_group(id: Optional[builtins.str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKeyGroupResult:
    """
    A key group.
     A key group contains a list of public keys that you can use with [CloudFront signed URLs and signed cookies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html).


    :param builtins.str id: The identifier for the key group.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:cloudfront:getKeyGroup', __args__, opts=opts, typ=GetKeyGroupResult).value

    return AwaitableGetKeyGroupResult(
        id=pulumi.get(__ret__, 'id'),
        key_group_config=pulumi.get(__ret__, 'key_group_config'),
        last_modified_time=pulumi.get(__ret__, 'last_modified_time'))
def get_key_group_output(id: Optional[pulumi.Input[builtins.str]] = None,
                         opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetKeyGroupResult]:
    """
    A key group.
     A key group contains a list of public keys that you can use with [CloudFront signed URLs and signed cookies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html).


    :param builtins.str id: The identifier for the key group.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:cloudfront:getKeyGroup', __args__, opts=opts, typ=GetKeyGroupResult)
    return __ret__.apply(lambda __response__: GetKeyGroupResult(
        id=pulumi.get(__response__, 'id'),
        key_group_config=pulumi.get(__response__, 'key_group_config'),
        last_modified_time=pulumi.get(__response__, 'last_modified_time')))
