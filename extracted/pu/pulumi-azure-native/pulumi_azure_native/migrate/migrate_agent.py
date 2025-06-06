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

__all__ = ['MigrateAgentArgs', 'MigrateAgent']

@pulumi.input_type
class MigrateAgentArgs:
    def __init__(__self__, *,
                 modernize_project_name: pulumi.Input[builtins.str],
                 resource_group_name: pulumi.Input[builtins.str],
                 agent_name: Optional[pulumi.Input[builtins.str]] = None,
                 properties: Optional[pulumi.Input['MigrateAgentModelPropertiesArgs']] = None,
                 subscription_id: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None):
        """
        The set of arguments for constructing a MigrateAgent resource.
        :param pulumi.Input[builtins.str] modernize_project_name: ModernizeProject name.
        :param pulumi.Input[builtins.str] resource_group_name: Name of the Azure Resource Group that project is part of.
        :param pulumi.Input[builtins.str] agent_name: MigrateAgent name.
        :param pulumi.Input['MigrateAgentModelPropertiesArgs'] properties: MigrateAgent model properties.
        :param pulumi.Input[builtins.str] subscription_id: Azure Subscription Id in which project was created.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] tags: Gets or sets the resource tags.
        """
        pulumi.set(__self__, "modernize_project_name", modernize_project_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if agent_name is not None:
            pulumi.set(__self__, "agent_name", agent_name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if subscription_id is not None:
            pulumi.set(__self__, "subscription_id", subscription_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="modernizeProjectName")
    def modernize_project_name(self) -> pulumi.Input[builtins.str]:
        """
        ModernizeProject name.
        """
        return pulumi.get(self, "modernize_project_name")

    @modernize_project_name.setter
    def modernize_project_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "modernize_project_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[builtins.str]:
        """
        Name of the Azure Resource Group that project is part of.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="agentName")
    def agent_name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        MigrateAgent name.
        """
        return pulumi.get(self, "agent_name")

    @agent_name.setter
    def agent_name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "agent_name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['MigrateAgentModelPropertiesArgs']]:
        """
        MigrateAgent model properties.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['MigrateAgentModelPropertiesArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Azure Subscription Id in which project was created.
        """
        return pulumi.get(self, "subscription_id")

    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "subscription_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]:
        """
        Gets or sets the resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.type_token("azure-native:migrate:MigrateAgent")
class MigrateAgent(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_name: Optional[pulumi.Input[builtins.str]] = None,
                 modernize_project_name: Optional[pulumi.Input[builtins.str]] = None,
                 properties: Optional[pulumi.Input[Union['MigrateAgentModelPropertiesArgs', 'MigrateAgentModelPropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 subscription_id: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        """
        MigrateAgent model.

        Uses Azure REST API version 2022-05-01-preview. In version 2.x of the Azure Native provider, it used API version 2022-05-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] agent_name: MigrateAgent name.
        :param pulumi.Input[builtins.str] modernize_project_name: ModernizeProject name.
        :param pulumi.Input[Union['MigrateAgentModelPropertiesArgs', 'MigrateAgentModelPropertiesArgsDict']] properties: MigrateAgent model properties.
        :param pulumi.Input[builtins.str] resource_group_name: Name of the Azure Resource Group that project is part of.
        :param pulumi.Input[builtins.str] subscription_id: Azure Subscription Id in which project was created.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] tags: Gets or sets the resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MigrateAgentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        MigrateAgent model.

        Uses Azure REST API version 2022-05-01-preview. In version 2.x of the Azure Native provider, it used API version 2022-05-01-preview.

        :param str resource_name: The name of the resource.
        :param MigrateAgentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MigrateAgentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_name: Optional[pulumi.Input[builtins.str]] = None,
                 modernize_project_name: Optional[pulumi.Input[builtins.str]] = None,
                 properties: Optional[pulumi.Input[Union['MigrateAgentModelPropertiesArgs', 'MigrateAgentModelPropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 subscription_id: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MigrateAgentArgs.__new__(MigrateAgentArgs)

            __props__.__dict__["agent_name"] = agent_name
            if modernize_project_name is None and not opts.urn:
                raise TypeError("Missing required property 'modernize_project_name'")
            __props__.__dict__["modernize_project_name"] = modernize_project_name
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["subscription_id"] = subscription_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["azure_api_version"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:migrate/v20220501preview:MigrateAgent")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(MigrateAgent, __self__).__init__(
            'azure-native:migrate:MigrateAgent',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'MigrateAgent':
        """
        Get an existing MigrateAgent resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MigrateAgentArgs.__new__(MigrateAgentArgs)

        __props__.__dict__["azure_api_version"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return MigrateAgent(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[builtins.str]:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        Gets or sets the name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.MigrateAgentModelPropertiesResponse']:
        """
        MigrateAgent model properties.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.MigrateAgentModelResponseSystemData']:
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, builtins.str]]]:
        """
        Gets or sets the resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[builtins.str]:
        """
        Gets or sets the type of the resource.
        """
        return pulumi.get(self, "type")

