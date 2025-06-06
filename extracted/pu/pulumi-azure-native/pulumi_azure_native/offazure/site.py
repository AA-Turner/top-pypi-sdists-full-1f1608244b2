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
from ._inputs import *

__all__ = ['SiteArgs', 'Site']

@pulumi.input_type
class SiteArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[builtins.str],
                 e_tag: Optional[pulumi.Input[builtins.str]] = None,
                 location: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 properties: Optional[pulumi.Input['SitePropertiesArgs']] = None,
                 site_name: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None):
        """
        The set of arguments for constructing a Site resource.
        :param pulumi.Input[builtins.str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[builtins.str] e_tag: eTag for concurrency control.
        :param pulumi.Input[builtins.str] location: Azure location in which Sites is created.
        :param pulumi.Input[builtins.str] name: Name of the VMware site.
        :param pulumi.Input['SitePropertiesArgs'] properties: Nested properties of VMWare site.
        :param pulumi.Input[builtins.str] site_name: Site name.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if e_tag is not None:
            pulumi.set(__self__, "e_tag", e_tag)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if site_name is not None:
            pulumi.set(__self__, "site_name", site_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        eTag for concurrency control.
        """
        return pulumi.get(self, "e_tag")

    @e_tag.setter
    def e_tag(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "e_tag", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Azure location in which Sites is created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Name of the VMware site.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['SitePropertiesArgs']]:
        """
        Nested properties of VMWare site.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['SitePropertiesArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="siteName")
    def site_name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Site name.
        """
        return pulumi.get(self, "site_name")

    @site_name.setter
    def site_name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "site_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.type_token("azure-native:offazure:Site")
class Site(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 e_tag: Optional[pulumi.Input[builtins.str]] = None,
                 location: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 properties: Optional[pulumi.Input[Union['SitePropertiesArgs', 'SitePropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 site_name: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        """
        Site REST Resource.

        Uses Azure REST API version 2020-07-07. In version 2.x of the Azure Native provider, it used API version 2020-07-07.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] e_tag: eTag for concurrency control.
        :param pulumi.Input[builtins.str] location: Azure location in which Sites is created.
        :param pulumi.Input[builtins.str] name: Name of the VMware site.
        :param pulumi.Input[Union['SitePropertiesArgs', 'SitePropertiesArgsDict']] properties: Nested properties of VMWare site.
        :param pulumi.Input[builtins.str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[builtins.str] site_name: Site name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SiteArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Site REST Resource.

        Uses Azure REST API version 2020-07-07. In version 2.x of the Azure Native provider, it used API version 2020-07-07.

        :param str resource_name: The name of the resource.
        :param SiteArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SiteArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 e_tag: Optional[pulumi.Input[builtins.str]] = None,
                 location: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 properties: Optional[pulumi.Input[Union['SitePropertiesArgs', 'SitePropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 site_name: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SiteArgs.__new__(SiteArgs)

            __props__.__dict__["e_tag"] = e_tag
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["site_name"] = site_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["azure_api_version"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:offazure/v20200101:Site"), pulumi.Alias(type_="azure-native:offazure/v20200707:Site"), pulumi.Alias(type_="azure-native:offazure/v20230606:Site"), pulumi.Alias(type_="azure-native:offazure/v20230606:SitesController"), pulumi.Alias(type_="azure-native:offazure/v20231001preview:Site"), pulumi.Alias(type_="azure-native:offazure/v20231001preview:SitesController"), pulumi.Alias(type_="azure-native:offazure/v20240501preview:Site"), pulumi.Alias(type_="azure-native:offazure/v20240501preview:SitesController"), pulumi.Alias(type_="azure-native:offazure:SitesController")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Site, __self__).__init__(
            'azure-native:offazure:Site',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Site':
        """
        Get an existing Site resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SiteArgs.__new__(SiteArgs)

        __props__.__dict__["azure_api_version"] = None
        __props__.__dict__["e_tag"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Site(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[builtins.str]:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        eTag for concurrency control.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        Azure location in which Sites is created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        Name of the VMware site.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.SitePropertiesResponse']:
        """
        Nested properties of VMWare site.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, builtins.str]]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[builtins.str]:
        """
        Type of resource. Type = Microsoft.OffAzure/VMWareSites.
        """
        return pulumi.get(self, "type")

