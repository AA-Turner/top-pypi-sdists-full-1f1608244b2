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
    'GetSubscriptionTargetResult',
    'AwaitableGetSubscriptionTargetResult',
    'get_subscription_target',
    'get_subscription_target_output',
]

@pulumi.output_type
class GetSubscriptionTargetResult:
    def __init__(__self__, applicable_asset_types=None, authorized_principals=None, created_at=None, created_by=None, domain_id=None, environment_id=None, id=None, manage_access_role=None, name=None, project_id=None, provider=None, subscription_target_config=None, updated_at=None, updated_by=None):
        if applicable_asset_types and not isinstance(applicable_asset_types, list):
            raise TypeError("Expected argument 'applicable_asset_types' to be a list")
        pulumi.set(__self__, "applicable_asset_types", applicable_asset_types)
        if authorized_principals and not isinstance(authorized_principals, list):
            raise TypeError("Expected argument 'authorized_principals' to be a list")
        pulumi.set(__self__, "authorized_principals", authorized_principals)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if created_by and not isinstance(created_by, str):
            raise TypeError("Expected argument 'created_by' to be a str")
        pulumi.set(__self__, "created_by", created_by)
        if domain_id and not isinstance(domain_id, str):
            raise TypeError("Expected argument 'domain_id' to be a str")
        pulumi.set(__self__, "domain_id", domain_id)
        if environment_id and not isinstance(environment_id, str):
            raise TypeError("Expected argument 'environment_id' to be a str")
        pulumi.set(__self__, "environment_id", environment_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if manage_access_role and not isinstance(manage_access_role, str):
            raise TypeError("Expected argument 'manage_access_role' to be a str")
        pulumi.set(__self__, "manage_access_role", manage_access_role)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if provider and not isinstance(provider, str):
            raise TypeError("Expected argument 'provider' to be a str")
        pulumi.set(__self__, "provider", provider)
        if subscription_target_config and not isinstance(subscription_target_config, list):
            raise TypeError("Expected argument 'subscription_target_config' to be a list")
        pulumi.set(__self__, "subscription_target_config", subscription_target_config)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)
        if updated_by and not isinstance(updated_by, str):
            raise TypeError("Expected argument 'updated_by' to be a str")
        pulumi.set(__self__, "updated_by", updated_by)

    @property
    @pulumi.getter(name="applicableAssetTypes")
    def applicable_asset_types(self) -> Optional[Sequence[builtins.str]]:
        """
        The asset types that can be included in the subscription target.
        """
        return pulumi.get(self, "applicable_asset_types")

    @property
    @pulumi.getter(name="authorizedPrincipals")
    def authorized_principals(self) -> Optional[Sequence[builtins.str]]:
        """
        The authorized principals of the subscription target.
        """
        return pulumi.get(self, "authorized_principals")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[builtins.str]:
        """
        The timestamp of when the subscription target was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[builtins.str]:
        """
        The Amazon DataZone user who created the subscription target.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> Optional[builtins.str]:
        """
        The ID of the Amazon DataZone domain in which subscription target is created.
        """
        return pulumi.get(self, "domain_id")

    @property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[builtins.str]:
        """
        The ID of the environment in which subscription target is created.
        """
        return pulumi.get(self, "environment_id")

    @property
    @pulumi.getter
    def id(self) -> Optional[builtins.str]:
        """
        The ID of the subscription target.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="manageAccessRole")
    def manage_access_role(self) -> Optional[builtins.str]:
        """
        The manage access role that is used to create the subscription target.
        """
        return pulumi.get(self, "manage_access_role")

    @property
    @pulumi.getter
    def name(self) -> Optional[builtins.str]:
        """
        The name of the subscription target.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[builtins.str]:
        """
        The identifier of the project specified in the subscription target.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def provider(self) -> Optional[builtins.str]:
        """
        The provider of the subscription target.
        """
        return pulumi.get(self, "provider")

    @property
    @pulumi.getter(name="subscriptionTargetConfig")
    def subscription_target_config(self) -> Optional[Sequence['outputs.SubscriptionTargetForm']]:
        """
        The configuration of the subscription target.
        """
        return pulumi.get(self, "subscription_target_config")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[builtins.str]:
        """
        The timestamp of when the subscription target was updated.
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> Optional[builtins.str]:
        """
        The Amazon DataZone user who updated the subscription target.
        """
        return pulumi.get(self, "updated_by")


class AwaitableGetSubscriptionTargetResult(GetSubscriptionTargetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSubscriptionTargetResult(
            applicable_asset_types=self.applicable_asset_types,
            authorized_principals=self.authorized_principals,
            created_at=self.created_at,
            created_by=self.created_by,
            domain_id=self.domain_id,
            environment_id=self.environment_id,
            id=self.id,
            manage_access_role=self.manage_access_role,
            name=self.name,
            project_id=self.project_id,
            provider=self.provider,
            subscription_target_config=self.subscription_target_config,
            updated_at=self.updated_at,
            updated_by=self.updated_by)


def get_subscription_target(domain_id: Optional[builtins.str] = None,
                            environment_id: Optional[builtins.str] = None,
                            id: Optional[builtins.str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSubscriptionTargetResult:
    """
    Subscription targets enables one to access the data to which you have subscribed in your projects.


    :param builtins.str domain_id: The ID of the Amazon DataZone domain in which subscription target is created.
    :param builtins.str environment_id: The ID of the environment in which subscription target is created.
    :param builtins.str id: The ID of the subscription target.
    """
    __args__ = dict()
    __args__['domainId'] = domain_id
    __args__['environmentId'] = environment_id
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:datazone:getSubscriptionTarget', __args__, opts=opts, typ=GetSubscriptionTargetResult).value

    return AwaitableGetSubscriptionTargetResult(
        applicable_asset_types=pulumi.get(__ret__, 'applicable_asset_types'),
        authorized_principals=pulumi.get(__ret__, 'authorized_principals'),
        created_at=pulumi.get(__ret__, 'created_at'),
        created_by=pulumi.get(__ret__, 'created_by'),
        domain_id=pulumi.get(__ret__, 'domain_id'),
        environment_id=pulumi.get(__ret__, 'environment_id'),
        id=pulumi.get(__ret__, 'id'),
        manage_access_role=pulumi.get(__ret__, 'manage_access_role'),
        name=pulumi.get(__ret__, 'name'),
        project_id=pulumi.get(__ret__, 'project_id'),
        provider=pulumi.get(__ret__, 'provider'),
        subscription_target_config=pulumi.get(__ret__, 'subscription_target_config'),
        updated_at=pulumi.get(__ret__, 'updated_at'),
        updated_by=pulumi.get(__ret__, 'updated_by'))
def get_subscription_target_output(domain_id: Optional[pulumi.Input[builtins.str]] = None,
                                   environment_id: Optional[pulumi.Input[builtins.str]] = None,
                                   id: Optional[pulumi.Input[builtins.str]] = None,
                                   opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetSubscriptionTargetResult]:
    """
    Subscription targets enables one to access the data to which you have subscribed in your projects.


    :param builtins.str domain_id: The ID of the Amazon DataZone domain in which subscription target is created.
    :param builtins.str environment_id: The ID of the environment in which subscription target is created.
    :param builtins.str id: The ID of the subscription target.
    """
    __args__ = dict()
    __args__['domainId'] = domain_id
    __args__['environmentId'] = environment_id
    __args__['id'] = id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:datazone:getSubscriptionTarget', __args__, opts=opts, typ=GetSubscriptionTargetResult)
    return __ret__.apply(lambda __response__: GetSubscriptionTargetResult(
        applicable_asset_types=pulumi.get(__response__, 'applicable_asset_types'),
        authorized_principals=pulumi.get(__response__, 'authorized_principals'),
        created_at=pulumi.get(__response__, 'created_at'),
        created_by=pulumi.get(__response__, 'created_by'),
        domain_id=pulumi.get(__response__, 'domain_id'),
        environment_id=pulumi.get(__response__, 'environment_id'),
        id=pulumi.get(__response__, 'id'),
        manage_access_role=pulumi.get(__response__, 'manage_access_role'),
        name=pulumi.get(__response__, 'name'),
        project_id=pulumi.get(__response__, 'project_id'),
        provider=pulumi.get(__response__, 'provider'),
        subscription_target_config=pulumi.get(__response__, 'subscription_target_config'),
        updated_at=pulumi.get(__response__, 'updated_at'),
        updated_by=pulumi.get(__response__, 'updated_by')))
