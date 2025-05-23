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

__all__ = ['EdgeSiteArgs', 'EdgeSite']

@pulumi.input_type
class EdgeSiteArgs:
    def __init__(__self__, *,
                 global_communications_site: pulumi.Input['EdgeSitesPropertiesGlobalCommunicationsSiteArgs'],
                 resource_group_name: pulumi.Input[builtins.str],
                 edge_site_name: Optional[pulumi.Input[builtins.str]] = None,
                 location: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None):
        """
        The set of arguments for constructing a EdgeSite resource.
        :param pulumi.Input['EdgeSitesPropertiesGlobalCommunicationsSiteArgs'] global_communications_site: A reference to global communications site.
        :param pulumi.Input[builtins.str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[builtins.str] edge_site_name: Edge site name.
        :param pulumi.Input[builtins.str] location: The geo-location where the resource lives
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "global_communications_site", global_communications_site)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if edge_site_name is not None:
            pulumi.set(__self__, "edge_site_name", edge_site_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="globalCommunicationsSite")
    def global_communications_site(self) -> pulumi.Input['EdgeSitesPropertiesGlobalCommunicationsSiteArgs']:
        """
        A reference to global communications site.
        """
        return pulumi.get(self, "global_communications_site")

    @global_communications_site.setter
    def global_communications_site(self, value: pulumi.Input['EdgeSitesPropertiesGlobalCommunicationsSiteArgs']):
        pulumi.set(self, "global_communications_site", value)

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
    @pulumi.getter(name="edgeSiteName")
    def edge_site_name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Edge site name.
        """
        return pulumi.get(self, "edge_site_name")

    @edge_site_name.setter
    def edge_site_name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "edge_site_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.type_token("azure-native:orbital:EdgeSite")
class EdgeSite(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 edge_site_name: Optional[pulumi.Input[builtins.str]] = None,
                 global_communications_site: Optional[pulumi.Input[Union['EdgeSitesPropertiesGlobalCommunicationsSiteArgs', 'EdgeSitesPropertiesGlobalCommunicationsSiteArgsDict']]] = None,
                 location: Optional[pulumi.Input[builtins.str]] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        """
        A customer's reference to a global communications site site.

        Uses Azure REST API version 2024-03-01-preview. In version 2.x of the Azure Native provider, it used API version 2024-03-01-preview.

        Other available API versions: 2024-03-01. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native orbital [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] edge_site_name: Edge site name.
        :param pulumi.Input[Union['EdgeSitesPropertiesGlobalCommunicationsSiteArgs', 'EdgeSitesPropertiesGlobalCommunicationsSiteArgsDict']] global_communications_site: A reference to global communications site.
        :param pulumi.Input[builtins.str] location: The geo-location where the resource lives
        :param pulumi.Input[builtins.str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EdgeSiteArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A customer's reference to a global communications site site.

        Uses Azure REST API version 2024-03-01-preview. In version 2.x of the Azure Native provider, it used API version 2024-03-01-preview.

        Other available API versions: 2024-03-01. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native orbital [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.

        :param str resource_name: The name of the resource.
        :param EdgeSiteArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EdgeSiteArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 edge_site_name: Optional[pulumi.Input[builtins.str]] = None,
                 global_communications_site: Optional[pulumi.Input[Union['EdgeSitesPropertiesGlobalCommunicationsSiteArgs', 'EdgeSitesPropertiesGlobalCommunicationsSiteArgsDict']]] = None,
                 location: Optional[pulumi.Input[builtins.str]] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EdgeSiteArgs.__new__(EdgeSiteArgs)

            __props__.__dict__["edge_site_name"] = edge_site_name
            if global_communications_site is None and not opts.urn:
                raise TypeError("Missing required property 'global_communications_site'")
            __props__.__dict__["global_communications_site"] = global_communications_site
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["azure_api_version"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:orbital/v20240301:EdgeSite"), pulumi.Alias(type_="azure-native:orbital/v20240301preview:EdgeSite")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(EdgeSite, __self__).__init__(
            'azure-native:orbital:EdgeSite',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EdgeSite':
        """
        Get an existing EdgeSite resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EdgeSiteArgs.__new__(EdgeSiteArgs)

        __props__.__dict__["azure_api_version"] = None
        __props__.__dict__["global_communications_site"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return EdgeSite(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[builtins.str]:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter(name="globalCommunicationsSite")
    def global_communications_site(self) -> pulumi.Output['outputs.EdgeSitesPropertiesResponseGlobalCommunicationsSite']:
        """
        A reference to global communications site.
        """
        return pulumi.get(self, "global_communications_site")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[builtins.str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, builtins.str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[builtins.str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

