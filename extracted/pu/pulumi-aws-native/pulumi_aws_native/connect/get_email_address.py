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
    'GetEmailAddressResult',
    'AwaitableGetEmailAddressResult',
    'get_email_address',
    'get_email_address_output',
]

@pulumi.output_type
class GetEmailAddressResult:
    def __init__(__self__, description=None, display_name=None, email_address_arn=None, instance_arn=None, tags=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if email_address_arn and not isinstance(email_address_arn, str):
            raise TypeError("Expected argument 'email_address_arn' to be a str")
        pulumi.set(__self__, "email_address_arn", email_address_arn)
        if instance_arn and not isinstance(instance_arn, str):
            raise TypeError("Expected argument 'instance_arn' to be a str")
        pulumi.set(__self__, "instance_arn", instance_arn)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def description(self) -> Optional[builtins.str]:
        """
        A description for the email address.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[builtins.str]:
        """
        The display name for the email address.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="emailAddressArn")
    def email_address_arn(self) -> Optional[builtins.str]:
        """
        The identifier of the email address.
        """
        return pulumi.get(self, "email_address_arn")

    @property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> Optional[builtins.str]:
        """
        The identifier of the Amazon Connect instance.
        """
        return pulumi.get(self, "instance_arn")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        One or more tags.
        """
        return pulumi.get(self, "tags")


class AwaitableGetEmailAddressResult(GetEmailAddressResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEmailAddressResult(
            description=self.description,
            display_name=self.display_name,
            email_address_arn=self.email_address_arn,
            instance_arn=self.instance_arn,
            tags=self.tags)


def get_email_address(email_address_arn: Optional[builtins.str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEmailAddressResult:
    """
    Resource Type definition for AWS::Connect::EmailAddress


    :param builtins.str email_address_arn: The identifier of the email address.
    """
    __args__ = dict()
    __args__['emailAddressArn'] = email_address_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:connect:getEmailAddress', __args__, opts=opts, typ=GetEmailAddressResult).value

    return AwaitableGetEmailAddressResult(
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        email_address_arn=pulumi.get(__ret__, 'email_address_arn'),
        instance_arn=pulumi.get(__ret__, 'instance_arn'),
        tags=pulumi.get(__ret__, 'tags'))
def get_email_address_output(email_address_arn: Optional[pulumi.Input[builtins.str]] = None,
                             opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetEmailAddressResult]:
    """
    Resource Type definition for AWS::Connect::EmailAddress


    :param builtins.str email_address_arn: The identifier of the email address.
    """
    __args__ = dict()
    __args__['emailAddressArn'] = email_address_arn
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:connect:getEmailAddress', __args__, opts=opts, typ=GetEmailAddressResult)
    return __ret__.apply(lambda __response__: GetEmailAddressResult(
        description=pulumi.get(__response__, 'description'),
        display_name=pulumi.get(__response__, 'display_name'),
        email_address_arn=pulumi.get(__response__, 'email_address_arn'),
        instance_arn=pulumi.get(__response__, 'instance_arn'),
        tags=pulumi.get(__response__, 'tags')))
