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
    'GetSecretValueResult',
    'AwaitableGetSecretValueResult',
    'get_secret_value',
    'get_secret_value_output',
]

@pulumi.output_type
class GetSecretValueResult:
    """
    This type describes a value of a secret resource. The name of this resource is the version identifier corresponding to this secret value.
    """
    def __init__(__self__, azure_api_version=None, id=None, location=None, name=None, provisioning_state=None, tags=None, type=None, value=None):
        if azure_api_version and not isinstance(azure_api_version, str):
            raise TypeError("Expected argument 'azure_api_version' to be a str")
        pulumi.set(__self__, "azure_api_version", azure_api_version)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if value and not isinstance(value, str):
            raise TypeError("Expected argument 'value' to be a str")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> builtins.str:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        """
        Fully qualified identifier for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

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
        State of the resource.
        """
        return pulumi.get(self, "provisioning_state")

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
        The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> Optional[builtins.str]:
        """
        The actual value of the secret.
        """
        return pulumi.get(self, "value")


class AwaitableGetSecretValueResult(GetSecretValueResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecretValueResult(
            azure_api_version=self.azure_api_version,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            tags=self.tags,
            type=self.type,
            value=self.value)


def get_secret_value(resource_group_name: Optional[builtins.str] = None,
                     secret_resource_name: Optional[builtins.str] = None,
                     secret_value_resource_name: Optional[builtins.str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecretValueResult:
    """
    Get the information about the specified named secret value resources. The information does not include the actual value of the secret.

    Uses Azure REST API version 2018-09-01-preview.


    :param builtins.str resource_group_name: Azure resource group name
    :param builtins.str secret_resource_name: The name of the secret resource.
    :param builtins.str secret_value_resource_name: The name of the secret resource value which is typically the version identifier for the value.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['secretResourceName'] = secret_resource_name
    __args__['secretValueResourceName'] = secret_value_resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:servicefabricmesh:getSecretValue', __args__, opts=opts, typ=GetSecretValueResult).value

    return AwaitableGetSecretValueResult(
        azure_api_version=pulumi.get(__ret__, 'azure_api_version'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        value=pulumi.get(__ret__, 'value'))
def get_secret_value_output(resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                            secret_resource_name: Optional[pulumi.Input[builtins.str]] = None,
                            secret_value_resource_name: Optional[pulumi.Input[builtins.str]] = None,
                            opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetSecretValueResult]:
    """
    Get the information about the specified named secret value resources. The information does not include the actual value of the secret.

    Uses Azure REST API version 2018-09-01-preview.


    :param builtins.str resource_group_name: Azure resource group name
    :param builtins.str secret_resource_name: The name of the secret resource.
    :param builtins.str secret_value_resource_name: The name of the secret resource value which is typically the version identifier for the value.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['secretResourceName'] = secret_resource_name
    __args__['secretValueResourceName'] = secret_value_resource_name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('azure-native:servicefabricmesh:getSecretValue', __args__, opts=opts, typ=GetSecretValueResult)
    return __ret__.apply(lambda __response__: GetSecretValueResult(
        azure_api_version=pulumi.get(__response__, 'azure_api_version'),
        id=pulumi.get(__response__, 'id'),
        location=pulumi.get(__response__, 'location'),
        name=pulumi.get(__response__, 'name'),
        provisioning_state=pulumi.get(__response__, 'provisioning_state'),
        tags=pulumi.get(__response__, 'tags'),
        type=pulumi.get(__response__, 'type'),
        value=pulumi.get(__response__, 'value')))
