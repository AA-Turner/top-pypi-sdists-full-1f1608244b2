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
from ._enums import *

__all__ = [
    'GetConfigurationPolicyResult',
    'AwaitableGetConfigurationPolicyResult',
    'get_configuration_policy',
    'get_configuration_policy_output',
]

@pulumi.output_type
class GetConfigurationPolicyResult:
    def __init__(__self__, arn=None, configuration_policy=None, created_at=None, description=None, id=None, name=None, service_enabled=None, tags=None, updated_at=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if configuration_policy and not isinstance(configuration_policy, dict):
            raise TypeError("Expected argument 'configuration_policy' to be a dict")
        pulumi.set(__self__, "configuration_policy", configuration_policy)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if service_enabled and not isinstance(service_enabled, bool):
            raise TypeError("Expected argument 'service_enabled' to be a bool")
        pulumi.set(__self__, "service_enabled", service_enabled)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter
    def arn(self) -> Optional[builtins.str]:
        """
        The Amazon Resource Name (ARN) of the configuration policy.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="configurationPolicy")
    def configuration_policy(self) -> Optional['outputs.ConfigurationPolicyPolicy']:
        """
        An object that defines how AWS Security Hub is configured. It includes whether Security Hub is enabled or disabled, a list of enabled security standards, a list of enabled or disabled security controls, and a list of custom parameter values for specified controls. If you provide a list of security controls that are enabled in the configuration policy, Security Hub disables all other controls (including newly released controls). If you provide a list of security controls that are disabled in the configuration policy, Security Hub enables all other controls (including newly released controls).
        """
        return pulumi.get(self, "configuration_policy")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[builtins.str]:
        """
        The date and time, in UTC and ISO 8601 format.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> Optional[builtins.str]:
        """
        The description of the configuration policy.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> Optional[builtins.str]:
        """
        The universally unique identifier (UUID) of the configuration policy.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[builtins.str]:
        """
        The name of the configuration policy.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="serviceEnabled")
    def service_enabled(self) -> Optional[builtins.bool]:
        """
        Indicates whether the service that the configuration policy applies to is enabled in the policy.
        """
        return pulumi.get(self, "service_enabled")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, builtins.str]]:
        """
        User-defined tags associated with a configuration policy. For more information, see [Tagging AWS Security Hub resources](https://docs.aws.amazon.com/securityhub/latest/userguide/tagging-resources.html) in the *Security Hub user guide* .
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[builtins.str]:
        """
        The date and time, in UTC and ISO 8601 format.
        """
        return pulumi.get(self, "updated_at")


class AwaitableGetConfigurationPolicyResult(GetConfigurationPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConfigurationPolicyResult(
            arn=self.arn,
            configuration_policy=self.configuration_policy,
            created_at=self.created_at,
            description=self.description,
            id=self.id,
            name=self.name,
            service_enabled=self.service_enabled,
            tags=self.tags,
            updated_at=self.updated_at)


def get_configuration_policy(arn: Optional[builtins.str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConfigurationPolicyResult:
    """
    The AWS::SecurityHub::ConfigurationPolicy resource represents the Central Configuration Policy in your account.


    :param builtins.str arn: The Amazon Resource Name (ARN) of the configuration policy.
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:securityhub:getConfigurationPolicy', __args__, opts=opts, typ=GetConfigurationPolicyResult).value

    return AwaitableGetConfigurationPolicyResult(
        arn=pulumi.get(__ret__, 'arn'),
        configuration_policy=pulumi.get(__ret__, 'configuration_policy'),
        created_at=pulumi.get(__ret__, 'created_at'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        service_enabled=pulumi.get(__ret__, 'service_enabled'),
        tags=pulumi.get(__ret__, 'tags'),
        updated_at=pulumi.get(__ret__, 'updated_at'))
def get_configuration_policy_output(arn: Optional[pulumi.Input[builtins.str]] = None,
                                    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetConfigurationPolicyResult]:
    """
    The AWS::SecurityHub::ConfigurationPolicy resource represents the Central Configuration Policy in your account.


    :param builtins.str arn: The Amazon Resource Name (ARN) of the configuration policy.
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:securityhub:getConfigurationPolicy', __args__, opts=opts, typ=GetConfigurationPolicyResult)
    return __ret__.apply(lambda __response__: GetConfigurationPolicyResult(
        arn=pulumi.get(__response__, 'arn'),
        configuration_policy=pulumi.get(__response__, 'configuration_policy'),
        created_at=pulumi.get(__response__, 'created_at'),
        description=pulumi.get(__response__, 'description'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        service_enabled=pulumi.get(__response__, 'service_enabled'),
        tags=pulumi.get(__response__, 'tags'),
        updated_at=pulumi.get(__response__, 'updated_at')))
