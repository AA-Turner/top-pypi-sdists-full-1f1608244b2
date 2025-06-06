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
    'GetIpExtendedCommunityResult',
    'AwaitableGetIpExtendedCommunityResult',
    'get_ip_extended_community',
    'get_ip_extended_community_output',
]

@pulumi.output_type
class GetIpExtendedCommunityResult:
    """
    The IP Extended Community resource definition.
    """
    def __init__(__self__, administrative_state=None, annotation=None, azure_api_version=None, configuration_state=None, id=None, ip_extended_community_rules=None, location=None, name=None, provisioning_state=None, system_data=None, tags=None, type=None):
        if administrative_state and not isinstance(administrative_state, str):
            raise TypeError("Expected argument 'administrative_state' to be a str")
        pulumi.set(__self__, "administrative_state", administrative_state)
        if annotation and not isinstance(annotation, str):
            raise TypeError("Expected argument 'annotation' to be a str")
        pulumi.set(__self__, "annotation", annotation)
        if azure_api_version and not isinstance(azure_api_version, str):
            raise TypeError("Expected argument 'azure_api_version' to be a str")
        pulumi.set(__self__, "azure_api_version", azure_api_version)
        if configuration_state and not isinstance(configuration_state, str):
            raise TypeError("Expected argument 'configuration_state' to be a str")
        pulumi.set(__self__, "configuration_state", configuration_state)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip_extended_community_rules and not isinstance(ip_extended_community_rules, list):
            raise TypeError("Expected argument 'ip_extended_community_rules' to be a list")
        pulumi.set(__self__, "ip_extended_community_rules", ip_extended_community_rules)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="administrativeState")
    def administrative_state(self) -> builtins.str:
        """
        Administrative state of the resource.
        """
        return pulumi.get(self, "administrative_state")

    @property
    @pulumi.getter
    def annotation(self) -> Optional[builtins.str]:
        """
        Switch configuration description.
        """
        return pulumi.get(self, "annotation")

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> builtins.str:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter(name="configurationState")
    def configuration_state(self) -> builtins.str:
        """
        Configuration state of the resource.
        """
        return pulumi.get(self, "configuration_state")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipExtendedCommunityRules")
    def ip_extended_community_rules(self) -> Sequence['outputs.IpExtendedCommunityRuleResponse']:
        """
        List of IP Extended Community Rules.
        """
        return pulumi.get(self, "ip_extended_community_rules")

    @property
    @pulumi.getter
    def location(self) -> builtins.str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> builtins.str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> builtins.str:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, builtins.str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> builtins.str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetIpExtendedCommunityResult(GetIpExtendedCommunityResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIpExtendedCommunityResult(
            administrative_state=self.administrative_state,
            annotation=self.annotation,
            azure_api_version=self.azure_api_version,
            configuration_state=self.configuration_state,
            id=self.id,
            ip_extended_community_rules=self.ip_extended_community_rules,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_ip_extended_community(ip_extended_community_name: Optional[builtins.str] = None,
                              resource_group_name: Optional[builtins.str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIpExtendedCommunityResult:
    """
    Implements IP Extended Community GET method.

    Uses Azure REST API version 2023-06-15.

    Other available API versions: 2023-02-01-preview. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native managednetworkfabric [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param builtins.str ip_extended_community_name: Name of the IP Extended Community.
    :param builtins.str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['ipExtendedCommunityName'] = ip_extended_community_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:managednetworkfabric:getIpExtendedCommunity', __args__, opts=opts, typ=GetIpExtendedCommunityResult).value

    return AwaitableGetIpExtendedCommunityResult(
        administrative_state=pulumi.get(__ret__, 'administrative_state'),
        annotation=pulumi.get(__ret__, 'annotation'),
        azure_api_version=pulumi.get(__ret__, 'azure_api_version'),
        configuration_state=pulumi.get(__ret__, 'configuration_state'),
        id=pulumi.get(__ret__, 'id'),
        ip_extended_community_rules=pulumi.get(__ret__, 'ip_extended_community_rules'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))
def get_ip_extended_community_output(ip_extended_community_name: Optional[pulumi.Input[builtins.str]] = None,
                                     resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                                     opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetIpExtendedCommunityResult]:
    """
    Implements IP Extended Community GET method.

    Uses Azure REST API version 2023-06-15.

    Other available API versions: 2023-02-01-preview. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native managednetworkfabric [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param builtins.str ip_extended_community_name: Name of the IP Extended Community.
    :param builtins.str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['ipExtendedCommunityName'] = ip_extended_community_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('azure-native:managednetworkfabric:getIpExtendedCommunity', __args__, opts=opts, typ=GetIpExtendedCommunityResult)
    return __ret__.apply(lambda __response__: GetIpExtendedCommunityResult(
        administrative_state=pulumi.get(__response__, 'administrative_state'),
        annotation=pulumi.get(__response__, 'annotation'),
        azure_api_version=pulumi.get(__response__, 'azure_api_version'),
        configuration_state=pulumi.get(__response__, 'configuration_state'),
        id=pulumi.get(__response__, 'id'),
        ip_extended_community_rules=pulumi.get(__response__, 'ip_extended_community_rules'),
        location=pulumi.get(__response__, 'location'),
        name=pulumi.get(__response__, 'name'),
        provisioning_state=pulumi.get(__response__, 'provisioning_state'),
        system_data=pulumi.get(__response__, 'system_data'),
        tags=pulumi.get(__response__, 'tags'),
        type=pulumi.get(__response__, 'type')))
