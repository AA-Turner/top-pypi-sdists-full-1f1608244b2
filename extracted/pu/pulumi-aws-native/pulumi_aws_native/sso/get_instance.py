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
from ._enums import *

__all__ = [
    'GetInstanceResult',
    'AwaitableGetInstanceResult',
    'get_instance',
    'get_instance_output',
]

@pulumi.output_type
class GetInstanceResult:
    def __init__(__self__, identity_store_id=None, instance_arn=None, name=None, owner_account_id=None, status=None, tags=None):
        if identity_store_id and not isinstance(identity_store_id, str):
            raise TypeError("Expected argument 'identity_store_id' to be a str")
        pulumi.set(__self__, "identity_store_id", identity_store_id)
        if instance_arn and not isinstance(instance_arn, str):
            raise TypeError("Expected argument 'instance_arn' to be a str")
        pulumi.set(__self__, "instance_arn", instance_arn)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if owner_account_id and not isinstance(owner_account_id, str):
            raise TypeError("Expected argument 'owner_account_id' to be a str")
        pulumi.set(__self__, "owner_account_id", owner_account_id)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="identityStoreId")
    def identity_store_id(self) -> Optional[builtins.str]:
        """
        The ID of the identity store associated with the created Identity Center (SSO) Instance
        """
        return pulumi.get(self, "identity_store_id")

    @property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> Optional[builtins.str]:
        """
        The SSO Instance ARN that is returned upon creation of the Identity Center (SSO) Instance
        """
        return pulumi.get(self, "instance_arn")

    @property
    @pulumi.getter
    def name(self) -> Optional[builtins.str]:
        """
        The name you want to assign to this Identity Center (SSO) Instance
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> Optional[builtins.str]:
        """
        The AWS accountId of the owner of the Identity Center (SSO) Instance
        """
        return pulumi.get(self, "owner_account_id")

    @property
    @pulumi.getter
    def status(self) -> Optional['InstanceStatus']:
        """
        The status of the Identity Center (SSO) Instance, create_in_progress/delete_in_progress/active
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        Specifies tags to be attached to the instance of IAM Identity Center.
        """
        return pulumi.get(self, "tags")


class AwaitableGetInstanceResult(GetInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceResult(
            identity_store_id=self.identity_store_id,
            instance_arn=self.instance_arn,
            name=self.name,
            owner_account_id=self.owner_account_id,
            status=self.status,
            tags=self.tags)


def get_instance(instance_arn: Optional[builtins.str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceResult:
    """
    Resource Type definition for Identity Center (SSO) Instance


    :param builtins.str instance_arn: The SSO Instance ARN that is returned upon creation of the Identity Center (SSO) Instance
    """
    __args__ = dict()
    __args__['instanceArn'] = instance_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:sso:getInstance', __args__, opts=opts, typ=GetInstanceResult).value

    return AwaitableGetInstanceResult(
        identity_store_id=pulumi.get(__ret__, 'identity_store_id'),
        instance_arn=pulumi.get(__ret__, 'instance_arn'),
        name=pulumi.get(__ret__, 'name'),
        owner_account_id=pulumi.get(__ret__, 'owner_account_id'),
        status=pulumi.get(__ret__, 'status'),
        tags=pulumi.get(__ret__, 'tags'))
def get_instance_output(instance_arn: Optional[pulumi.Input[builtins.str]] = None,
                        opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetInstanceResult]:
    """
    Resource Type definition for Identity Center (SSO) Instance


    :param builtins.str instance_arn: The SSO Instance ARN that is returned upon creation of the Identity Center (SSO) Instance
    """
    __args__ = dict()
    __args__['instanceArn'] = instance_arn
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:sso:getInstance', __args__, opts=opts, typ=GetInstanceResult)
    return __ret__.apply(lambda __response__: GetInstanceResult(
        identity_store_id=pulumi.get(__response__, 'identity_store_id'),
        instance_arn=pulumi.get(__response__, 'instance_arn'),
        name=pulumi.get(__response__, 'name'),
        owner_account_id=pulumi.get(__response__, 'owner_account_id'),
        status=pulumi.get(__response__, 'status'),
        tags=pulumi.get(__response__, 'tags')))
