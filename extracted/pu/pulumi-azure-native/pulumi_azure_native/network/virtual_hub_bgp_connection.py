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

__all__ = ['VirtualHubBgpConnectionArgs', 'VirtualHubBgpConnection']

@pulumi.input_type
class VirtualHubBgpConnectionArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[builtins.str],
                 virtual_hub_name: pulumi.Input[builtins.str],
                 connection_name: Optional[pulumi.Input[builtins.str]] = None,
                 hub_virtual_network_connection: Optional[pulumi.Input['SubResourceArgs']] = None,
                 id: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 peer_asn: Optional[pulumi.Input[builtins.float]] = None,
                 peer_ip: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a VirtualHubBgpConnection resource.
        :param pulumi.Input[builtins.str] resource_group_name: The resource group name of the VirtualHub.
        :param pulumi.Input[builtins.str] virtual_hub_name: The name of the VirtualHub.
        :param pulumi.Input[builtins.str] connection_name: The name of the connection.
        :param pulumi.Input['SubResourceArgs'] hub_virtual_network_connection: The reference to the HubVirtualNetworkConnection resource.
        :param pulumi.Input[builtins.str] id: Resource ID.
        :param pulumi.Input[builtins.str] name: Name of the connection.
        :param pulumi.Input[builtins.float] peer_asn: Peer ASN.
        :param pulumi.Input[builtins.str] peer_ip: Peer IP.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "virtual_hub_name", virtual_hub_name)
        if connection_name is not None:
            pulumi.set(__self__, "connection_name", connection_name)
        if hub_virtual_network_connection is not None:
            pulumi.set(__self__, "hub_virtual_network_connection", hub_virtual_network_connection)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if peer_asn is not None:
            pulumi.set(__self__, "peer_asn", peer_asn)
        if peer_ip is not None:
            pulumi.set(__self__, "peer_ip", peer_ip)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[builtins.str]:
        """
        The resource group name of the VirtualHub.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="virtualHubName")
    def virtual_hub_name(self) -> pulumi.Input[builtins.str]:
        """
        The name of the VirtualHub.
        """
        return pulumi.get(self, "virtual_hub_name")

    @virtual_hub_name.setter
    def virtual_hub_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "virtual_hub_name", value)

    @property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the connection.
        """
        return pulumi.get(self, "connection_name")

    @connection_name.setter
    def connection_name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "connection_name", value)

    @property
    @pulumi.getter(name="hubVirtualNetworkConnection")
    def hub_virtual_network_connection(self) -> Optional[pulumi.Input['SubResourceArgs']]:
        """
        The reference to the HubVirtualNetworkConnection resource.
        """
        return pulumi.get(self, "hub_virtual_network_connection")

    @hub_virtual_network_connection.setter
    def hub_virtual_network_connection(self, value: Optional[pulumi.Input['SubResourceArgs']]):
        pulumi.set(self, "hub_virtual_network_connection", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Name of the connection.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="peerAsn")
    def peer_asn(self) -> Optional[pulumi.Input[builtins.float]]:
        """
        Peer ASN.
        """
        return pulumi.get(self, "peer_asn")

    @peer_asn.setter
    def peer_asn(self, value: Optional[pulumi.Input[builtins.float]]):
        pulumi.set(self, "peer_asn", value)

    @property
    @pulumi.getter(name="peerIp")
    def peer_ip(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Peer IP.
        """
        return pulumi.get(self, "peer_ip")

    @peer_ip.setter
    def peer_ip(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "peer_ip", value)


@pulumi.type_token("azure-native:network:VirtualHubBgpConnection")
class VirtualHubBgpConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection_name: Optional[pulumi.Input[builtins.str]] = None,
                 hub_virtual_network_connection: Optional[pulumi.Input[Union['SubResourceArgs', 'SubResourceArgsDict']]] = None,
                 id: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 peer_asn: Optional[pulumi.Input[builtins.float]] = None,
                 peer_ip: Optional[pulumi.Input[builtins.str]] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 virtual_hub_name: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        Virtual Appliance Site resource.

        Uses Azure REST API version 2024-05-01. In version 2.x of the Azure Native provider, it used API version 2023-02-01.

        Other available API versions: 2020-05-01, 2020-06-01, 2020-07-01, 2020-08-01, 2020-11-01, 2021-02-01, 2021-03-01, 2021-05-01, 2021-08-01, 2022-01-01, 2022-05-01, 2022-07-01, 2022-09-01, 2022-11-01, 2023-02-01, 2023-04-01, 2023-05-01, 2023-06-01, 2023-09-01, 2023-11-01, 2024-01-01, 2024-03-01, 2024-07-01. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native network [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] connection_name: The name of the connection.
        :param pulumi.Input[Union['SubResourceArgs', 'SubResourceArgsDict']] hub_virtual_network_connection: The reference to the HubVirtualNetworkConnection resource.
        :param pulumi.Input[builtins.str] id: Resource ID.
        :param pulumi.Input[builtins.str] name: Name of the connection.
        :param pulumi.Input[builtins.float] peer_asn: Peer ASN.
        :param pulumi.Input[builtins.str] peer_ip: Peer IP.
        :param pulumi.Input[builtins.str] resource_group_name: The resource group name of the VirtualHub.
        :param pulumi.Input[builtins.str] virtual_hub_name: The name of the VirtualHub.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualHubBgpConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Virtual Appliance Site resource.

        Uses Azure REST API version 2024-05-01. In version 2.x of the Azure Native provider, it used API version 2023-02-01.

        Other available API versions: 2020-05-01, 2020-06-01, 2020-07-01, 2020-08-01, 2020-11-01, 2021-02-01, 2021-03-01, 2021-05-01, 2021-08-01, 2022-01-01, 2022-05-01, 2022-07-01, 2022-09-01, 2022-11-01, 2023-02-01, 2023-04-01, 2023-05-01, 2023-06-01, 2023-09-01, 2023-11-01, 2024-01-01, 2024-03-01, 2024-07-01. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native network [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.

        :param str resource_name: The name of the resource.
        :param VirtualHubBgpConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualHubBgpConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection_name: Optional[pulumi.Input[builtins.str]] = None,
                 hub_virtual_network_connection: Optional[pulumi.Input[Union['SubResourceArgs', 'SubResourceArgsDict']]] = None,
                 id: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 peer_asn: Optional[pulumi.Input[builtins.float]] = None,
                 peer_ip: Optional[pulumi.Input[builtins.str]] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 virtual_hub_name: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VirtualHubBgpConnectionArgs.__new__(VirtualHubBgpConnectionArgs)

            __props__.__dict__["connection_name"] = connection_name
            __props__.__dict__["hub_virtual_network_connection"] = hub_virtual_network_connection
            __props__.__dict__["id"] = id
            __props__.__dict__["name"] = name
            __props__.__dict__["peer_asn"] = peer_asn
            __props__.__dict__["peer_ip"] = peer_ip
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if virtual_hub_name is None and not opts.urn:
                raise TypeError("Missing required property 'virtual_hub_name'")
            __props__.__dict__["virtual_hub_name"] = virtual_hub_name
            __props__.__dict__["azure_api_version"] = None
            __props__.__dict__["connection_state"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network/v20200501:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network/v20200601:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network/v20200701:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network/v20200801:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network/v20201101:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network/v20210201:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network/v20210301:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network/v20210501:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network/v20210801:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network/v20220101:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network/v20220501:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network/v20220701:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network/v20220901:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network/v20221101:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network/v20230201:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network/v20230401:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network/v20230501:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network/v20230601:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network/v20230901:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network/v20231101:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network/v20240101:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network/v20240301:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network/v20240501:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network/v20240701:VirtualHubBgpConnection")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VirtualHubBgpConnection, __self__).__init__(
            'azure-native:network:VirtualHubBgpConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VirtualHubBgpConnection':
        """
        Get an existing VirtualHubBgpConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VirtualHubBgpConnectionArgs.__new__(VirtualHubBgpConnectionArgs)

        __props__.__dict__["azure_api_version"] = None
        __props__.__dict__["connection_state"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["hub_virtual_network_connection"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["peer_asn"] = None
        __props__.__dict__["peer_ip"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["type"] = None
        return VirtualHubBgpConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[builtins.str]:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter(name="connectionState")
    def connection_state(self) -> pulumi.Output[builtins.str]:
        """
        The current state of the VirtualHub to Peer.
        """
        return pulumi.get(self, "connection_state")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[builtins.str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="hubVirtualNetworkConnection")
    def hub_virtual_network_connection(self) -> pulumi.Output[Optional['outputs.SubResourceResponse']]:
        """
        The reference to the HubVirtualNetworkConnection resource.
        """
        return pulumi.get(self, "hub_virtual_network_connection")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        Name of the connection.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="peerAsn")
    def peer_asn(self) -> pulumi.Output[Optional[builtins.float]]:
        """
        Peer ASN.
        """
        return pulumi.get(self, "peer_asn")

    @property
    @pulumi.getter(name="peerIp")
    def peer_ip(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        Peer IP.
        """
        return pulumi.get(self, "peer_ip")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[builtins.str]:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[builtins.str]:
        """
        Connection type.
        """
        return pulumi.get(self, "type")

