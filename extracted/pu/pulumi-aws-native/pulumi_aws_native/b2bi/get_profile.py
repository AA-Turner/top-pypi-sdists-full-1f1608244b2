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
    'GetProfileResult',
    'AwaitableGetProfileResult',
    'get_profile',
    'get_profile_output',
]

@pulumi.output_type
class GetProfileResult:
    def __init__(__self__, business_name=None, created_at=None, email=None, log_group_name=None, modified_at=None, name=None, phone=None, profile_arn=None, profile_id=None, tags=None):
        if business_name and not isinstance(business_name, str):
            raise TypeError("Expected argument 'business_name' to be a str")
        pulumi.set(__self__, "business_name", business_name)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if email and not isinstance(email, str):
            raise TypeError("Expected argument 'email' to be a str")
        pulumi.set(__self__, "email", email)
        if log_group_name and not isinstance(log_group_name, str):
            raise TypeError("Expected argument 'log_group_name' to be a str")
        pulumi.set(__self__, "log_group_name", log_group_name)
        if modified_at and not isinstance(modified_at, str):
            raise TypeError("Expected argument 'modified_at' to be a str")
        pulumi.set(__self__, "modified_at", modified_at)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if phone and not isinstance(phone, str):
            raise TypeError("Expected argument 'phone' to be a str")
        pulumi.set(__self__, "phone", phone)
        if profile_arn and not isinstance(profile_arn, str):
            raise TypeError("Expected argument 'profile_arn' to be a str")
        pulumi.set(__self__, "profile_arn", profile_arn)
        if profile_id and not isinstance(profile_id, str):
            raise TypeError("Expected argument 'profile_id' to be a str")
        pulumi.set(__self__, "profile_id", profile_id)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="businessName")
    def business_name(self) -> Optional[builtins.str]:
        """
        Returns the name for the business associated with this profile.
        """
        return pulumi.get(self, "business_name")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[builtins.str]:
        """
        Returns the timestamp for creation date and time of the profile.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def email(self) -> Optional[builtins.str]:
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[builtins.str]:
        """
        Returns the name of the logging group.
        """
        return pulumi.get(self, "log_group_name")

    @property
    @pulumi.getter(name="modifiedAt")
    def modified_at(self) -> Optional[builtins.str]:
        """
        Returns the timestamp that identifies the most recent date and time that the profile was modified.
        """
        return pulumi.get(self, "modified_at")

    @property
    @pulumi.getter
    def name(self) -> Optional[builtins.str]:
        """
        Returns the display name for profile.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def phone(self) -> Optional[builtins.str]:
        return pulumi.get(self, "phone")

    @property
    @pulumi.getter(name="profileArn")
    def profile_arn(self) -> Optional[builtins.str]:
        """
        Returns an Amazon Resource Name (ARN) for the profile.
        """
        return pulumi.get(self, "profile_arn")

    @property
    @pulumi.getter(name="profileId")
    def profile_id(self) -> Optional[builtins.str]:
        return pulumi.get(self, "profile_id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        A key-value pair for a specific profile. Tags are metadata that you can use to search for and group capabilities for various purposes.
        """
        return pulumi.get(self, "tags")


class AwaitableGetProfileResult(GetProfileResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProfileResult(
            business_name=self.business_name,
            created_at=self.created_at,
            email=self.email,
            log_group_name=self.log_group_name,
            modified_at=self.modified_at,
            name=self.name,
            phone=self.phone,
            profile_arn=self.profile_arn,
            profile_id=self.profile_id,
            tags=self.tags)


def get_profile(profile_id: Optional[builtins.str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProfileResult:
    """
    Definition of AWS::B2BI::Profile Resource Type
    """
    __args__ = dict()
    __args__['profileId'] = profile_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:b2bi:getProfile', __args__, opts=opts, typ=GetProfileResult).value

    return AwaitableGetProfileResult(
        business_name=pulumi.get(__ret__, 'business_name'),
        created_at=pulumi.get(__ret__, 'created_at'),
        email=pulumi.get(__ret__, 'email'),
        log_group_name=pulumi.get(__ret__, 'log_group_name'),
        modified_at=pulumi.get(__ret__, 'modified_at'),
        name=pulumi.get(__ret__, 'name'),
        phone=pulumi.get(__ret__, 'phone'),
        profile_arn=pulumi.get(__ret__, 'profile_arn'),
        profile_id=pulumi.get(__ret__, 'profile_id'),
        tags=pulumi.get(__ret__, 'tags'))
def get_profile_output(profile_id: Optional[pulumi.Input[builtins.str]] = None,
                       opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetProfileResult]:
    """
    Definition of AWS::B2BI::Profile Resource Type
    """
    __args__ = dict()
    __args__['profileId'] = profile_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:b2bi:getProfile', __args__, opts=opts, typ=GetProfileResult)
    return __ret__.apply(lambda __response__: GetProfileResult(
        business_name=pulumi.get(__response__, 'business_name'),
        created_at=pulumi.get(__response__, 'created_at'),
        email=pulumi.get(__response__, 'email'),
        log_group_name=pulumi.get(__response__, 'log_group_name'),
        modified_at=pulumi.get(__response__, 'modified_at'),
        name=pulumi.get(__response__, 'name'),
        phone=pulumi.get(__response__, 'phone'),
        profile_arn=pulumi.get(__response__, 'profile_arn'),
        profile_id=pulumi.get(__response__, 'profile_id'),
        tags=pulumi.get(__response__, 'tags')))
