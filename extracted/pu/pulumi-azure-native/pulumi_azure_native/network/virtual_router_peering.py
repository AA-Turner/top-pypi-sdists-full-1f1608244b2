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

__all__ = ['VirtualRouterPeeringArgs', 'VirtualRouterPeering']

@pulumi.input_type
class VirtualRouterPeeringArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[builtins.str],
                 virtual_router_name: pulumi.Input[builtins.str],
                 id: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 peer_asn: Optional[pulumi.Input[builtins.float]] = None,
                 peer_ip: Optional[pulumi.Input[builtins.str]] = None,
                 peering_name: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a VirtualRouterPeering resource.
        :param pulumi.Input[builtins.str] resource_group_name: The name of the resource group.
        :param pulumi.Input[builtins.str] virtual_router_name: The name of the Virtual Router.
        :param pulumi.Input[builtins.str] id: Resource ID.
        :param pulumi.Input[builtins.str] name: Name of the virtual router peering that is unique within a virtual router.
        :param pulumi.Input[builtins.float] peer_asn: Peer ASN.
        :param pulumi.Input[builtins.str] peer_ip: Peer IP.
        :param pulumi.Input[builtins.str] peering_name: The name of the Virtual Router Peering.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "virtual_router_name", virtual_router_name)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if peer_asn is not None:
            pulumi.set(__self__, "peer_asn", peer_asn)
        if peer_ip is not None:
            pulumi.set(__self__, "peer_ip", peer_ip)
        if peering_name is not None:
            pulumi.set(__self__, "peering_name", peering_name)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[builtins.str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="virtualRouterName")
    def virtual_router_name(self) -> pulumi.Input[builtins.str]:
        """
        The name of the Virtual Router.
        """
        return pulumi.get(self, "virtual_router_name")

    @virtual_router_name.setter
    def virtual_router_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "virtual_router_name", value)

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
        Name of the virtual router peering that is unique within a virtual router.
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

    @property
    @pulumi.getter(name="peeringName")
    def peering_name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the Virtual Router Peering.
        """
        return pulumi.get(self, "peering_name")

    @peering_name.setter
    def peering_name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "peering_name", value)


@pulumi.type_token("azure-native:network:VirtualRouterPeering")
class VirtualRouterPeering(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 id: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 peer_asn: Optional[pulumi.Input[builtins.float]] = None,
                 peer_ip: Optional[pulumi.Input[builtins.str]] = None,
                 peering_name: Optional[pulumi.Input[builtins.str]] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 virtual_router_name: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        Virtual Router Peering resource.

        Uses Azure REST API version 2024-05-01. In version 2.x of the Azure Native provider, it used API version 2023-02-01.

        Other available API versions: 2019-07-01, 2019-08-01, 2019-09-01, 2019-11-01, 2019-12-01, 2020-03-01, 2020-04-01, 2020-05-01, 2020-06-01, 2020-07-01, 2020-08-01, 2020-11-01, 2021-02-01, 2021-03-01, 2021-05-01, 2021-08-01, 2022-01-01, 2022-05-01, 2022-07-01, 2022-09-01, 2022-11-01, 2023-02-01, 2023-04-01, 2023-05-01, 2023-06-01, 2023-09-01, 2023-11-01, 2024-01-01, 2024-03-01, 2024-07-01. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native network [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] id: Resource ID.
        :param pulumi.Input[builtins.str] name: Name of the virtual router peering that is unique within a virtual router.
        :param pulumi.Input[builtins.float] peer_asn: Peer ASN.
        :param pulumi.Input[builtins.str] peer_ip: Peer IP.
        :param pulumi.Input[builtins.str] peering_name: The name of the Virtual Router Peering.
        :param pulumi.Input[builtins.str] resource_group_name: The name of the resource group.
        :param pulumi.Input[builtins.str] virtual_router_name: The name of the Virtual Router.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualRouterPeeringArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Virtual Router Peering resource.

        Uses Azure REST API version 2024-05-01. In version 2.x of the Azure Native provider, it used API version 2023-02-01.

        Other available API versions: 2019-07-01, 2019-08-01, 2019-09-01, 2019-11-01, 2019-12-01, 2020-03-01, 2020-04-01, 2020-05-01, 2020-06-01, 2020-07-01, 2020-08-01, 2020-11-01, 2021-02-01, 2021-03-01, 2021-05-01, 2021-08-01, 2022-01-01, 2022-05-01, 2022-07-01, 2022-09-01, 2022-11-01, 2023-02-01, 2023-04-01, 2023-05-01, 2023-06-01, 2023-09-01, 2023-11-01, 2024-01-01, 2024-03-01, 2024-07-01. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native network [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.

        :param str resource_name: The name of the resource.
        :param VirtualRouterPeeringArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualRouterPeeringArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 id: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 peer_asn: Optional[pulumi.Input[builtins.float]] = None,
                 peer_ip: Optional[pulumi.Input[builtins.str]] = None,
                 peering_name: Optional[pulumi.Input[builtins.str]] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 virtual_router_name: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VirtualRouterPeeringArgs.__new__(VirtualRouterPeeringArgs)

            __props__.__dict__["id"] = id
            __props__.__dict__["name"] = name
            __props__.__dict__["peer_asn"] = peer_asn
            __props__.__dict__["peer_ip"] = peer_ip
            __props__.__dict__["peering_name"] = peering_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if virtual_router_name is None and not opts.urn:
                raise TypeError("Missing required property 'virtual_router_name'")
            __props__.__dict__["virtual_router_name"] = virtual_router_name
            __props__.__dict__["azure_api_version"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network/v20190701:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20190801:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20190901:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20191101:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20191201:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20200301:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20200401:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20200501:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20200601:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20200701:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20200801:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20201101:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20210201:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20210301:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20210501:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20210801:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20220101:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20220501:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20220701:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20220901:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20221101:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20230201:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20230401:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20230501:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20230601:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20230901:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20231101:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20240101:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20240301:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20240501:VirtualRouterPeering"), pulumi.Alias(type_="azure-native:network/v20240701:VirtualRouterPeering")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VirtualRouterPeering, __self__).__init__(
            'azure-native:network:VirtualRouterPeering',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VirtualRouterPeering':
        """
        Get an existing VirtualRouterPeering resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VirtualRouterPeeringArgs.__new__(VirtualRouterPeeringArgs)

        __props__.__dict__["azure_api_version"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["peer_asn"] = None
        __props__.__dict__["peer_ip"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["type"] = None
        return VirtualRouterPeering(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[builtins.str]:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[builtins.str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        Name of the virtual router peering that is unique within a virtual router.
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
        Peering type.
        """
        return pulumi.get(self, "type")

