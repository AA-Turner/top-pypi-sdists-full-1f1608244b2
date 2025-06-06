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
    'GetCustomizedAcceleratorResult',
    'AwaitableGetCustomizedAcceleratorResult',
    'get_customized_accelerator',
    'get_customized_accelerator_output',
]

@pulumi.output_type
class GetCustomizedAcceleratorResult:
    """
    Customized accelerator resource
    """
    def __init__(__self__, azure_api_version=None, id=None, name=None, properties=None, sku=None, system_data=None, type=None):
        if azure_api_version and not isinstance(azure_api_version, str):
            raise TypeError("Expected argument 'azure_api_version' to be a str")
        pulumi.set(__self__, "azure_api_version", azure_api_version)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

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
        Fully qualified resource Id for the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> builtins.str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.CustomizedAcceleratorPropertiesResponse':
        """
        Customized accelerator properties payload
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.SkuResponse']:
        """
        Sku of the customized accelerator resource
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> builtins.str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetCustomizedAcceleratorResult(GetCustomizedAcceleratorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCustomizedAcceleratorResult(
            azure_api_version=self.azure_api_version,
            id=self.id,
            name=self.name,
            properties=self.properties,
            sku=self.sku,
            system_data=self.system_data,
            type=self.type)


def get_customized_accelerator(application_accelerator_name: Optional[builtins.str] = None,
                               customized_accelerator_name: Optional[builtins.str] = None,
                               resource_group_name: Optional[builtins.str] = None,
                               service_name: Optional[builtins.str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCustomizedAcceleratorResult:
    """
    Get the customized accelerator.

    Uses Azure REST API version 2024-01-01-preview.

    Other available API versions: 2023-05-01-preview, 2023-07-01-preview, 2023-09-01-preview, 2023-11-01-preview, 2023-12-01, 2024-05-01-preview. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native appplatform [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param builtins.str application_accelerator_name: The name of the application accelerator.
    :param builtins.str customized_accelerator_name: The name of the customized accelerator.
    :param builtins.str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param builtins.str service_name: The name of the Service resource.
    """
    __args__ = dict()
    __args__['applicationAcceleratorName'] = application_accelerator_name
    __args__['customizedAcceleratorName'] = customized_accelerator_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:appplatform:getCustomizedAccelerator', __args__, opts=opts, typ=GetCustomizedAcceleratorResult).value

    return AwaitableGetCustomizedAcceleratorResult(
        azure_api_version=pulumi.get(__ret__, 'azure_api_version'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        sku=pulumi.get(__ret__, 'sku'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))
def get_customized_accelerator_output(application_accelerator_name: Optional[pulumi.Input[builtins.str]] = None,
                                      customized_accelerator_name: Optional[pulumi.Input[builtins.str]] = None,
                                      resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                                      service_name: Optional[pulumi.Input[builtins.str]] = None,
                                      opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetCustomizedAcceleratorResult]:
    """
    Get the customized accelerator.

    Uses Azure REST API version 2024-01-01-preview.

    Other available API versions: 2023-05-01-preview, 2023-07-01-preview, 2023-09-01-preview, 2023-11-01-preview, 2023-12-01, 2024-05-01-preview. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native appplatform [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param builtins.str application_accelerator_name: The name of the application accelerator.
    :param builtins.str customized_accelerator_name: The name of the customized accelerator.
    :param builtins.str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param builtins.str service_name: The name of the Service resource.
    """
    __args__ = dict()
    __args__['applicationAcceleratorName'] = application_accelerator_name
    __args__['customizedAcceleratorName'] = customized_accelerator_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('azure-native:appplatform:getCustomizedAccelerator', __args__, opts=opts, typ=GetCustomizedAcceleratorResult)
    return __ret__.apply(lambda __response__: GetCustomizedAcceleratorResult(
        azure_api_version=pulumi.get(__response__, 'azure_api_version'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        properties=pulumi.get(__response__, 'properties'),
        sku=pulumi.get(__response__, 'sku'),
        system_data=pulumi.get(__response__, 'system_data'),
        type=pulumi.get(__response__, 'type')))
