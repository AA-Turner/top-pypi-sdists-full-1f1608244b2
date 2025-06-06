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
from ._inputs import *

__all__ = ['DeploymentArgs', 'Deployment']

@pulumi.input_type
class DeploymentArgs:
    def __init__(__self__, *,
                 catalog_name: pulumi.Input[builtins.str],
                 device_group_name: pulumi.Input[builtins.str],
                 product_name: pulumi.Input[builtins.str],
                 resource_group_name: pulumi.Input[builtins.str],
                 deployed_images: Optional[pulumi.Input[Sequence[pulumi.Input['ImageArgs']]]] = None,
                 deployment_id: Optional[pulumi.Input[builtins.str]] = None,
                 deployment_name: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a Deployment resource.
        :param pulumi.Input[builtins.str] catalog_name: Name of catalog
        :param pulumi.Input[builtins.str] device_group_name: Name of device group.
        :param pulumi.Input[builtins.str] product_name: Name of product.
        :param pulumi.Input[builtins.str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input['ImageArgs']]] deployed_images: Images deployed
        :param pulumi.Input[builtins.str] deployment_id: Deployment ID
        :param pulumi.Input[builtins.str] deployment_name: Deployment name. Use .default for deployment creation and to get the current deployment for the associated device group.
        """
        pulumi.set(__self__, "catalog_name", catalog_name)
        pulumi.set(__self__, "device_group_name", device_group_name)
        pulumi.set(__self__, "product_name", product_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if deployed_images is not None:
            pulumi.set(__self__, "deployed_images", deployed_images)
        if deployment_id is not None:
            pulumi.set(__self__, "deployment_id", deployment_id)
        if deployment_name is not None:
            pulumi.set(__self__, "deployment_name", deployment_name)

    @property
    @pulumi.getter(name="catalogName")
    def catalog_name(self) -> pulumi.Input[builtins.str]:
        """
        Name of catalog
        """
        return pulumi.get(self, "catalog_name")

    @catalog_name.setter
    def catalog_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "catalog_name", value)

    @property
    @pulumi.getter(name="deviceGroupName")
    def device_group_name(self) -> pulumi.Input[builtins.str]:
        """
        Name of device group.
        """
        return pulumi.get(self, "device_group_name")

    @device_group_name.setter
    def device_group_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "device_group_name", value)

    @property
    @pulumi.getter(name="productName")
    def product_name(self) -> pulumi.Input[builtins.str]:
        """
        Name of product.
        """
        return pulumi.get(self, "product_name")

    @product_name.setter
    def product_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "product_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[builtins.str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="deployedImages")
    def deployed_images(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ImageArgs']]]]:
        """
        Images deployed
        """
        return pulumi.get(self, "deployed_images")

    @deployed_images.setter
    def deployed_images(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ImageArgs']]]]):
        pulumi.set(self, "deployed_images", value)

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Deployment ID
        """
        return pulumi.get(self, "deployment_id")

    @deployment_id.setter
    def deployment_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "deployment_id", value)

    @property
    @pulumi.getter(name="deploymentName")
    def deployment_name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Deployment name. Use .default for deployment creation and to get the current deployment for the associated device group.
        """
        return pulumi.get(self, "deployment_name")

    @deployment_name.setter
    def deployment_name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "deployment_name", value)


@pulumi.type_token("azure-native:azuresphere:Deployment")
class Deployment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 catalog_name: Optional[pulumi.Input[builtins.str]] = None,
                 deployed_images: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ImageArgs', 'ImageArgsDict']]]]] = None,
                 deployment_id: Optional[pulumi.Input[builtins.str]] = None,
                 deployment_name: Optional[pulumi.Input[builtins.str]] = None,
                 device_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 product_name: Optional[pulumi.Input[builtins.str]] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        An deployment resource belonging to a device group resource.

        Uses Azure REST API version 2024-04-01. In version 2.x of the Azure Native provider, it used API version 2022-09-01-preview.

        Other available API versions: 2022-09-01-preview. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native azuresphere [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] catalog_name: Name of catalog
        :param pulumi.Input[Sequence[pulumi.Input[Union['ImageArgs', 'ImageArgsDict']]]] deployed_images: Images deployed
        :param pulumi.Input[builtins.str] deployment_id: Deployment ID
        :param pulumi.Input[builtins.str] deployment_name: Deployment name. Use .default for deployment creation and to get the current deployment for the associated device group.
        :param pulumi.Input[builtins.str] device_group_name: Name of device group.
        :param pulumi.Input[builtins.str] product_name: Name of product.
        :param pulumi.Input[builtins.str] resource_group_name: The name of the resource group. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DeploymentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An deployment resource belonging to a device group resource.

        Uses Azure REST API version 2024-04-01. In version 2.x of the Azure Native provider, it used API version 2022-09-01-preview.

        Other available API versions: 2022-09-01-preview. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native azuresphere [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.

        :param str resource_name: The name of the resource.
        :param DeploymentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DeploymentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 catalog_name: Optional[pulumi.Input[builtins.str]] = None,
                 deployed_images: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ImageArgs', 'ImageArgsDict']]]]] = None,
                 deployment_id: Optional[pulumi.Input[builtins.str]] = None,
                 deployment_name: Optional[pulumi.Input[builtins.str]] = None,
                 device_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 product_name: Optional[pulumi.Input[builtins.str]] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DeploymentArgs.__new__(DeploymentArgs)

            if catalog_name is None and not opts.urn:
                raise TypeError("Missing required property 'catalog_name'")
            __props__.__dict__["catalog_name"] = catalog_name
            __props__.__dict__["deployed_images"] = deployed_images
            __props__.__dict__["deployment_id"] = deployment_id
            __props__.__dict__["deployment_name"] = deployment_name
            if device_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'device_group_name'")
            __props__.__dict__["device_group_name"] = device_group_name
            if product_name is None and not opts.urn:
                raise TypeError("Missing required property 'product_name'")
            __props__.__dict__["product_name"] = product_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["azure_api_version"] = None
            __props__.__dict__["deployment_date_utc"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:azuresphere/v20220901preview:Deployment"), pulumi.Alias(type_="azure-native:azuresphere/v20240401:Deployment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Deployment, __self__).__init__(
            'azure-native:azuresphere:Deployment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Deployment':
        """
        Get an existing Deployment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DeploymentArgs.__new__(DeploymentArgs)

        __props__.__dict__["azure_api_version"] = None
        __props__.__dict__["deployed_images"] = None
        __props__.__dict__["deployment_date_utc"] = None
        __props__.__dict__["deployment_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return Deployment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[builtins.str]:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter(name="deployedImages")
    def deployed_images(self) -> pulumi.Output[Optional[Sequence['outputs.ImageResponse']]]:
        """
        Images deployed
        """
        return pulumi.get(self, "deployed_images")

    @property
    @pulumi.getter(name="deploymentDateUtc")
    def deployment_date_utc(self) -> pulumi.Output[builtins.str]:
        """
        Deployment date UTC
        """
        return pulumi.get(self, "deployment_date_utc")

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        Deployment ID
        """
        return pulumi.get(self, "deployment_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[builtins.str]:
        """
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[builtins.str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

