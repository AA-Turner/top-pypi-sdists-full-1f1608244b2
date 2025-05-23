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

__all__ = ['ServerCommunicationLinkArgs', 'ServerCommunicationLink']

@pulumi.input_type
class ServerCommunicationLinkArgs:
    def __init__(__self__, *,
                 partner_server: pulumi.Input[builtins.str],
                 resource_group_name: pulumi.Input[builtins.str],
                 server_name: pulumi.Input[builtins.str],
                 communication_link_name: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a ServerCommunicationLink resource.
        :param pulumi.Input[builtins.str] partner_server: The name of the partner server.
        :param pulumi.Input[builtins.str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[builtins.str] server_name: The name of the server.
        :param pulumi.Input[builtins.str] communication_link_name: The name of the server communication link.
        """
        pulumi.set(__self__, "partner_server", partner_server)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "server_name", server_name)
        if communication_link_name is not None:
            pulumi.set(__self__, "communication_link_name", communication_link_name)

    @property
    @pulumi.getter(name="partnerServer")
    def partner_server(self) -> pulumi.Input[builtins.str]:
        """
        The name of the partner server.
        """
        return pulumi.get(self, "partner_server")

    @partner_server.setter
    def partner_server(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "partner_server", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[builtins.str]:
        """
        The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[builtins.str]:
        """
        The name of the server.
        """
        return pulumi.get(self, "server_name")

    @server_name.setter
    def server_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "server_name", value)

    @property
    @pulumi.getter(name="communicationLinkName")
    def communication_link_name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the server communication link.
        """
        return pulumi.get(self, "communication_link_name")

    @communication_link_name.setter
    def communication_link_name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "communication_link_name", value)


@pulumi.type_token("azure-native:sql:ServerCommunicationLink")
class ServerCommunicationLink(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 communication_link_name: Optional[pulumi.Input[builtins.str]] = None,
                 partner_server: Optional[pulumi.Input[builtins.str]] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 server_name: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        Server communication link.

        Uses Azure REST API version 2014-04-01. In version 2.x of the Azure Native provider, it used API version 2014-04-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] communication_link_name: The name of the server communication link.
        :param pulumi.Input[builtins.str] partner_server: The name of the partner server.
        :param pulumi.Input[builtins.str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[builtins.str] server_name: The name of the server.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServerCommunicationLinkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Server communication link.

        Uses Azure REST API version 2014-04-01. In version 2.x of the Azure Native provider, it used API version 2014-04-01.

        :param str resource_name: The name of the resource.
        :param ServerCommunicationLinkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServerCommunicationLinkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 communication_link_name: Optional[pulumi.Input[builtins.str]] = None,
                 partner_server: Optional[pulumi.Input[builtins.str]] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 server_name: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServerCommunicationLinkArgs.__new__(ServerCommunicationLinkArgs)

            __props__.__dict__["communication_link_name"] = communication_link_name
            if partner_server is None and not opts.urn:
                raise TypeError("Missing required property 'partner_server'")
            __props__.__dict__["partner_server"] = partner_server
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if server_name is None and not opts.urn:
                raise TypeError("Missing required property 'server_name'")
            __props__.__dict__["server_name"] = server_name
            __props__.__dict__["azure_api_version"] = None
            __props__.__dict__["kind"] = None
            __props__.__dict__["location"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:sql/v20140401:ServerCommunicationLink")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ServerCommunicationLink, __self__).__init__(
            'azure-native:sql:ServerCommunicationLink',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ServerCommunicationLink':
        """
        Get an existing ServerCommunicationLink resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServerCommunicationLinkArgs.__new__(ServerCommunicationLinkArgs)

        __props__.__dict__["azure_api_version"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["partner_server"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["type"] = None
        return ServerCommunicationLink(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[builtins.str]:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[builtins.str]:
        """
        Communication link kind.  This property is used for Azure Portal metadata.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[builtins.str]:
        """
        Communication link location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partnerServer")
    def partner_server(self) -> pulumi.Output[builtins.str]:
        """
        The name of the partner server.
        """
        return pulumi.get(self, "partner_server")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[builtins.str]:
        """
        The state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[builtins.str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

