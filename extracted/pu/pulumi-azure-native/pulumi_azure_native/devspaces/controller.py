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

__all__ = ['ControllerArgs', 'Controller']

@pulumi.input_type
class ControllerArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[builtins.str],
                 sku: pulumi.Input['SkuArgs'],
                 target_container_host_credentials_base64: pulumi.Input[builtins.str],
                 target_container_host_resource_id: pulumi.Input[builtins.str],
                 location: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None):
        """
        The set of arguments for constructing a Controller resource.
        :param pulumi.Input[builtins.str] resource_group_name: Resource group to which the resource belongs.
        :param pulumi.Input['SkuArgs'] sku: Model representing SKU for Azure Dev Spaces Controller.
        :param pulumi.Input[builtins.str] target_container_host_credentials_base64: Credentials of the target container host (base64).
        :param pulumi.Input[builtins.str] target_container_host_resource_id: Resource ID of the target container host
        :param pulumi.Input[builtins.str] location: Region where the Azure resource is located.
        :param pulumi.Input[builtins.str] name: Name of the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] tags: Tags for the Azure resource.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sku", sku)
        pulumi.set(__self__, "target_container_host_credentials_base64", target_container_host_credentials_base64)
        pulumi.set(__self__, "target_container_host_resource_id", target_container_host_resource_id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[builtins.str]:
        """
        Resource group to which the resource belongs.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Input['SkuArgs']:
        """
        Model representing SKU for Azure Dev Spaces Controller.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: pulumi.Input['SkuArgs']):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter(name="targetContainerHostCredentialsBase64")
    def target_container_host_credentials_base64(self) -> pulumi.Input[builtins.str]:
        """
        Credentials of the target container host (base64).
        """
        return pulumi.get(self, "target_container_host_credentials_base64")

    @target_container_host_credentials_base64.setter
    def target_container_host_credentials_base64(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "target_container_host_credentials_base64", value)

    @property
    @pulumi.getter(name="targetContainerHostResourceId")
    def target_container_host_resource_id(self) -> pulumi.Input[builtins.str]:
        """
        Resource ID of the target container host
        """
        return pulumi.get(self, "target_container_host_resource_id")

    @target_container_host_resource_id.setter
    def target_container_host_resource_id(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "target_container_host_resource_id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Region where the Azure resource is located.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]:
        """
        Tags for the Azure resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.type_token("azure-native:devspaces:Controller")
class Controller(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 sku: Optional[pulumi.Input[Union['SkuArgs', 'SkuArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 target_container_host_credentials_base64: Optional[pulumi.Input[builtins.str]] = None,
                 target_container_host_resource_id: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        Uses Azure REST API version 2019-04-01. In version 2.x of the Azure Native provider, it used API version 2019-04-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] location: Region where the Azure resource is located.
        :param pulumi.Input[builtins.str] name: Name of the resource.
        :param pulumi.Input[builtins.str] resource_group_name: Resource group to which the resource belongs.
        :param pulumi.Input[Union['SkuArgs', 'SkuArgsDict']] sku: Model representing SKU for Azure Dev Spaces Controller.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] tags: Tags for the Azure resource.
        :param pulumi.Input[builtins.str] target_container_host_credentials_base64: Credentials of the target container host (base64).
        :param pulumi.Input[builtins.str] target_container_host_resource_id: Resource ID of the target container host
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ControllerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Uses Azure REST API version 2019-04-01. In version 2.x of the Azure Native provider, it used API version 2019-04-01.

        :param str resource_name: The name of the resource.
        :param ControllerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ControllerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 sku: Optional[pulumi.Input[Union['SkuArgs', 'SkuArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 target_container_host_credentials_base64: Optional[pulumi.Input[builtins.str]] = None,
                 target_container_host_resource_id: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ControllerArgs.__new__(ControllerArgs)

            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if sku is None and not opts.urn:
                raise TypeError("Missing required property 'sku'")
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            if target_container_host_credentials_base64 is None and not opts.urn:
                raise TypeError("Missing required property 'target_container_host_credentials_base64'")
            __props__.__dict__["target_container_host_credentials_base64"] = target_container_host_credentials_base64
            if target_container_host_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'target_container_host_resource_id'")
            __props__.__dict__["target_container_host_resource_id"] = target_container_host_resource_id
            __props__.__dict__["azure_api_version"] = None
            __props__.__dict__["data_plane_fqdn"] = None
            __props__.__dict__["host_suffix"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["target_container_host_api_server_fqdn"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:devspaces/v20190401:Controller")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Controller, __self__).__init__(
            'azure-native:devspaces:Controller',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Controller':
        """
        Get an existing Controller resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ControllerArgs.__new__(ControllerArgs)

        __props__.__dict__["azure_api_version"] = None
        __props__.__dict__["data_plane_fqdn"] = None
        __props__.__dict__["host_suffix"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["target_container_host_api_server_fqdn"] = None
        __props__.__dict__["target_container_host_resource_id"] = None
        __props__.__dict__["type"] = None
        return Controller(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[builtins.str]:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter(name="dataPlaneFqdn")
    def data_plane_fqdn(self) -> pulumi.Output[builtins.str]:
        """
        DNS name for accessing DataPlane services
        """
        return pulumi.get(self, "data_plane_fqdn")

    @property
    @pulumi.getter(name="hostSuffix")
    def host_suffix(self) -> pulumi.Output[builtins.str]:
        """
        DNS suffix for public endpoints running in the Azure Dev Spaces Controller.
        """
        return pulumi.get(self, "host_suffix")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[builtins.str]:
        """
        Region where the Azure resource is located.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[builtins.str]:
        """
        Provisioning state of the Azure Dev Spaces Controller.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output['outputs.SkuResponse']:
        """
        Model representing SKU for Azure Dev Spaces Controller.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, builtins.str]]]:
        """
        Tags for the Azure resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetContainerHostApiServerFqdn")
    def target_container_host_api_server_fqdn(self) -> pulumi.Output[builtins.str]:
        """
        DNS of the target container host's API server
        """
        return pulumi.get(self, "target_container_host_api_server_fqdn")

    @property
    @pulumi.getter(name="targetContainerHostResourceId")
    def target_container_host_resource_id(self) -> pulumi.Output[builtins.str]:
        """
        Resource ID of the target container host
        """
        return pulumi.get(self, "target_container_host_resource_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[builtins.str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

