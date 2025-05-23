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
    'GetDisasterRecoveryConfigurationResult',
    'AwaitableGetDisasterRecoveryConfigurationResult',
    'get_disaster_recovery_configuration',
    'get_disaster_recovery_configuration_output',
]

@pulumi.output_type
class GetDisasterRecoveryConfigurationResult:
    """
    Represents a disaster recovery configuration.
    """
    def __init__(__self__, auto_failover=None, azure_api_version=None, failover_policy=None, id=None, location=None, logical_server_name=None, name=None, partner_logical_server_name=None, partner_server_id=None, role=None, status=None, type=None):
        if auto_failover and not isinstance(auto_failover, str):
            raise TypeError("Expected argument 'auto_failover' to be a str")
        pulumi.set(__self__, "auto_failover", auto_failover)
        if azure_api_version and not isinstance(azure_api_version, str):
            raise TypeError("Expected argument 'azure_api_version' to be a str")
        pulumi.set(__self__, "azure_api_version", azure_api_version)
        if failover_policy and not isinstance(failover_policy, str):
            raise TypeError("Expected argument 'failover_policy' to be a str")
        pulumi.set(__self__, "failover_policy", failover_policy)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if logical_server_name and not isinstance(logical_server_name, str):
            raise TypeError("Expected argument 'logical_server_name' to be a str")
        pulumi.set(__self__, "logical_server_name", logical_server_name)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if partner_logical_server_name and not isinstance(partner_logical_server_name, str):
            raise TypeError("Expected argument 'partner_logical_server_name' to be a str")
        pulumi.set(__self__, "partner_logical_server_name", partner_logical_server_name)
        if partner_server_id and not isinstance(partner_server_id, str):
            raise TypeError("Expected argument 'partner_server_id' to be a str")
        pulumi.set(__self__, "partner_server_id", partner_server_id)
        if role and not isinstance(role, str):
            raise TypeError("Expected argument 'role' to be a str")
        pulumi.set(__self__, "role", role)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="autoFailover")
    def auto_failover(self) -> builtins.str:
        """
        Whether or not failover can be done automatically.
        """
        return pulumi.get(self, "auto_failover")

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> builtins.str:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter(name="failoverPolicy")
    def failover_policy(self) -> builtins.str:
        """
        How aggressive the automatic failover should be.
        """
        return pulumi.get(self, "failover_policy")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> builtins.str:
        """
        Location of the server that contains this disaster recovery configuration.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="logicalServerName")
    def logical_server_name(self) -> builtins.str:
        """
        Logical name of the server.
        """
        return pulumi.get(self, "logical_server_name")

    @property
    @pulumi.getter
    def name(self) -> builtins.str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partnerLogicalServerName")
    def partner_logical_server_name(self) -> builtins.str:
        """
        Logical name of the partner server.
        """
        return pulumi.get(self, "partner_logical_server_name")

    @property
    @pulumi.getter(name="partnerServerId")
    def partner_server_id(self) -> builtins.str:
        """
        Id of the partner server.
        """
        return pulumi.get(self, "partner_server_id")

    @property
    @pulumi.getter
    def role(self) -> builtins.str:
        """
        The role of the current server in the disaster recovery configuration.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter
    def status(self) -> builtins.str:
        """
        The status of the disaster recovery configuration.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> builtins.str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetDisasterRecoveryConfigurationResult(GetDisasterRecoveryConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDisasterRecoveryConfigurationResult(
            auto_failover=self.auto_failover,
            azure_api_version=self.azure_api_version,
            failover_policy=self.failover_policy,
            id=self.id,
            location=self.location,
            logical_server_name=self.logical_server_name,
            name=self.name,
            partner_logical_server_name=self.partner_logical_server_name,
            partner_server_id=self.partner_server_id,
            role=self.role,
            status=self.status,
            type=self.type)


def get_disaster_recovery_configuration(disaster_recovery_configuration_name: Optional[builtins.str] = None,
                                        resource_group_name: Optional[builtins.str] = None,
                                        server_name: Optional[builtins.str] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDisasterRecoveryConfigurationResult:
    """
    Gets a disaster recovery configuration.

    Uses Azure REST API version 2014-04-01.


    :param builtins.str disaster_recovery_configuration_name: The name of the disaster recovery configuration.
    :param builtins.str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param builtins.str server_name: The name of the server.
    """
    __args__ = dict()
    __args__['disasterRecoveryConfigurationName'] = disaster_recovery_configuration_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:sql:getDisasterRecoveryConfiguration', __args__, opts=opts, typ=GetDisasterRecoveryConfigurationResult).value

    return AwaitableGetDisasterRecoveryConfigurationResult(
        auto_failover=pulumi.get(__ret__, 'auto_failover'),
        azure_api_version=pulumi.get(__ret__, 'azure_api_version'),
        failover_policy=pulumi.get(__ret__, 'failover_policy'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        logical_server_name=pulumi.get(__ret__, 'logical_server_name'),
        name=pulumi.get(__ret__, 'name'),
        partner_logical_server_name=pulumi.get(__ret__, 'partner_logical_server_name'),
        partner_server_id=pulumi.get(__ret__, 'partner_server_id'),
        role=pulumi.get(__ret__, 'role'),
        status=pulumi.get(__ret__, 'status'),
        type=pulumi.get(__ret__, 'type'))
def get_disaster_recovery_configuration_output(disaster_recovery_configuration_name: Optional[pulumi.Input[builtins.str]] = None,
                                               resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                                               server_name: Optional[pulumi.Input[builtins.str]] = None,
                                               opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetDisasterRecoveryConfigurationResult]:
    """
    Gets a disaster recovery configuration.

    Uses Azure REST API version 2014-04-01.


    :param builtins.str disaster_recovery_configuration_name: The name of the disaster recovery configuration.
    :param builtins.str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param builtins.str server_name: The name of the server.
    """
    __args__ = dict()
    __args__['disasterRecoveryConfigurationName'] = disaster_recovery_configuration_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('azure-native:sql:getDisasterRecoveryConfiguration', __args__, opts=opts, typ=GetDisasterRecoveryConfigurationResult)
    return __ret__.apply(lambda __response__: GetDisasterRecoveryConfigurationResult(
        auto_failover=pulumi.get(__response__, 'auto_failover'),
        azure_api_version=pulumi.get(__response__, 'azure_api_version'),
        failover_policy=pulumi.get(__response__, 'failover_policy'),
        id=pulumi.get(__response__, 'id'),
        location=pulumi.get(__response__, 'location'),
        logical_server_name=pulumi.get(__response__, 'logical_server_name'),
        name=pulumi.get(__response__, 'name'),
        partner_logical_server_name=pulumi.get(__response__, 'partner_logical_server_name'),
        partner_server_id=pulumi.get(__response__, 'partner_server_id'),
        role=pulumi.get(__response__, 'role'),
        status=pulumi.get(__response__, 'status'),
        type=pulumi.get(__response__, 'type')))
