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
    'GetUserResult',
    'AwaitableGetUserResult',
    'get_user',
    'get_user_output',
]

@pulumi.output_type
class GetUserResult:
    """
    A collection of values returned by getUser.
    """
    def __init__(__self__, arn=None, id=None, path=None, permissions_boundary=None, tags=None, user_id=None, user_name=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if path and not isinstance(path, str):
            raise TypeError("Expected argument 'path' to be a str")
        pulumi.set(__self__, "path", path)
        if permissions_boundary and not isinstance(permissions_boundary, str):
            raise TypeError("Expected argument 'permissions_boundary' to be a str")
        pulumi.set(__self__, "permissions_boundary", permissions_boundary)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if user_id and not isinstance(user_id, str):
            raise TypeError("Expected argument 'user_id' to be a str")
        pulumi.set(__self__, "user_id", user_id)
        if user_name and not isinstance(user_name, str):
            raise TypeError("Expected argument 'user_name' to be a str")
        pulumi.set(__self__, "user_name", user_name)

    @property
    @pulumi.getter
    def arn(self) -> builtins.str:
        """
        ARN assigned by AWS for this user.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def path(self) -> builtins.str:
        """
        Path in which this user was created.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter(name="permissionsBoundary")
    def permissions_boundary(self) -> builtins.str:
        """
        The ARN of the policy that is used to set the permissions boundary for the user.
        """
        return pulumi.get(self, "permissions_boundary")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, builtins.str]:
        """
        Map of key-value pairs associated with the user.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> builtins.str:
        """
        Unique ID assigned by AWS for this user.
        """
        return pulumi.get(self, "user_id")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> builtins.str:
        """
        Name associated to this User
        """
        return pulumi.get(self, "user_name")


class AwaitableGetUserResult(GetUserResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUserResult(
            arn=self.arn,
            id=self.id,
            path=self.path,
            permissions_boundary=self.permissions_boundary,
            tags=self.tags,
            user_id=self.user_id,
            user_name=self.user_name)


def get_user(tags: Optional[Mapping[str, builtins.str]] = None,
             user_name: Optional[builtins.str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUserResult:
    """
    This data source can be used to fetch information about a specific
    IAM user. By using this data source, you can reference IAM user
    properties without having to hard code ARNs or unique IDs as input.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.iam.get_user(user_name="an_example_user_name")
    ```


    :param Mapping[str, builtins.str] tags: Map of key-value pairs associated with the user.
    :param builtins.str user_name: Friendly IAM user name to match.
    """
    __args__ = dict()
    __args__['tags'] = tags
    __args__['userName'] = user_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:iam/getUser:getUser', __args__, opts=opts, typ=GetUserResult).value

    return AwaitableGetUserResult(
        arn=pulumi.get(__ret__, 'arn'),
        id=pulumi.get(__ret__, 'id'),
        path=pulumi.get(__ret__, 'path'),
        permissions_boundary=pulumi.get(__ret__, 'permissions_boundary'),
        tags=pulumi.get(__ret__, 'tags'),
        user_id=pulumi.get(__ret__, 'user_id'),
        user_name=pulumi.get(__ret__, 'user_name'))
def get_user_output(tags: Optional[pulumi.Input[Optional[Mapping[str, builtins.str]]]] = None,
                    user_name: Optional[pulumi.Input[builtins.str]] = None,
                    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetUserResult]:
    """
    This data source can be used to fetch information about a specific
    IAM user. By using this data source, you can reference IAM user
    properties without having to hard code ARNs or unique IDs as input.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.iam.get_user(user_name="an_example_user_name")
    ```


    :param Mapping[str, builtins.str] tags: Map of key-value pairs associated with the user.
    :param builtins.str user_name: Friendly IAM user name to match.
    """
    __args__ = dict()
    __args__['tags'] = tags
    __args__['userName'] = user_name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:iam/getUser:getUser', __args__, opts=opts, typ=GetUserResult)
    return __ret__.apply(lambda __response__: GetUserResult(
        arn=pulumi.get(__response__, 'arn'),
        id=pulumi.get(__response__, 'id'),
        path=pulumi.get(__response__, 'path'),
        permissions_boundary=pulumi.get(__response__, 'permissions_boundary'),
        tags=pulumi.get(__response__, 'tags'),
        user_id=pulumi.get(__response__, 'user_id'),
        user_name=pulumi.get(__response__, 'user_name')))
