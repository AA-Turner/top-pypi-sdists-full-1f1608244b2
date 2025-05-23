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
    'GetVirtualNetworkGatewayConnectionResult',
    'AwaitableGetVirtualNetworkGatewayConnectionResult',
    'get_virtual_network_gateway_connection',
    'get_virtual_network_gateway_connection_output',
]

@pulumi.output_type
class GetVirtualNetworkGatewayConnectionResult:
    """
    A common class for general resource information.
    """
    def __init__(__self__, authorization_key=None, azure_api_version=None, connection_mode=None, connection_protocol=None, connection_status=None, connection_type=None, dpd_timeout_seconds=None, egress_bytes_transferred=None, egress_nat_rules=None, enable_bgp=None, enable_private_link_fast_path=None, etag=None, express_route_gateway_bypass=None, gateway_custom_bgp_ip_addresses=None, id=None, ingress_bytes_transferred=None, ingress_nat_rules=None, ipsec_policies=None, local_network_gateway2=None, location=None, name=None, peer=None, provisioning_state=None, resource_guid=None, routing_weight=None, shared_key=None, tags=None, traffic_selector_policies=None, tunnel_connection_status=None, type=None, use_local_azure_ip_address=None, use_policy_based_traffic_selectors=None, virtual_network_gateway1=None, virtual_network_gateway2=None):
        if authorization_key and not isinstance(authorization_key, str):
            raise TypeError("Expected argument 'authorization_key' to be a str")
        pulumi.set(__self__, "authorization_key", authorization_key)
        if azure_api_version and not isinstance(azure_api_version, str):
            raise TypeError("Expected argument 'azure_api_version' to be a str")
        pulumi.set(__self__, "azure_api_version", azure_api_version)
        if connection_mode and not isinstance(connection_mode, str):
            raise TypeError("Expected argument 'connection_mode' to be a str")
        pulumi.set(__self__, "connection_mode", connection_mode)
        if connection_protocol and not isinstance(connection_protocol, str):
            raise TypeError("Expected argument 'connection_protocol' to be a str")
        pulumi.set(__self__, "connection_protocol", connection_protocol)
        if connection_status and not isinstance(connection_status, str):
            raise TypeError("Expected argument 'connection_status' to be a str")
        pulumi.set(__self__, "connection_status", connection_status)
        if connection_type and not isinstance(connection_type, str):
            raise TypeError("Expected argument 'connection_type' to be a str")
        pulumi.set(__self__, "connection_type", connection_type)
        if dpd_timeout_seconds and not isinstance(dpd_timeout_seconds, int):
            raise TypeError("Expected argument 'dpd_timeout_seconds' to be a int")
        pulumi.set(__self__, "dpd_timeout_seconds", dpd_timeout_seconds)
        if egress_bytes_transferred and not isinstance(egress_bytes_transferred, float):
            raise TypeError("Expected argument 'egress_bytes_transferred' to be a float")
        pulumi.set(__self__, "egress_bytes_transferred", egress_bytes_transferred)
        if egress_nat_rules and not isinstance(egress_nat_rules, list):
            raise TypeError("Expected argument 'egress_nat_rules' to be a list")
        pulumi.set(__self__, "egress_nat_rules", egress_nat_rules)
        if enable_bgp and not isinstance(enable_bgp, bool):
            raise TypeError("Expected argument 'enable_bgp' to be a bool")
        pulumi.set(__self__, "enable_bgp", enable_bgp)
        if enable_private_link_fast_path and not isinstance(enable_private_link_fast_path, bool):
            raise TypeError("Expected argument 'enable_private_link_fast_path' to be a bool")
        pulumi.set(__self__, "enable_private_link_fast_path", enable_private_link_fast_path)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if express_route_gateway_bypass and not isinstance(express_route_gateway_bypass, bool):
            raise TypeError("Expected argument 'express_route_gateway_bypass' to be a bool")
        pulumi.set(__self__, "express_route_gateway_bypass", express_route_gateway_bypass)
        if gateway_custom_bgp_ip_addresses and not isinstance(gateway_custom_bgp_ip_addresses, list):
            raise TypeError("Expected argument 'gateway_custom_bgp_ip_addresses' to be a list")
        pulumi.set(__self__, "gateway_custom_bgp_ip_addresses", gateway_custom_bgp_ip_addresses)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ingress_bytes_transferred and not isinstance(ingress_bytes_transferred, float):
            raise TypeError("Expected argument 'ingress_bytes_transferred' to be a float")
        pulumi.set(__self__, "ingress_bytes_transferred", ingress_bytes_transferred)
        if ingress_nat_rules and not isinstance(ingress_nat_rules, list):
            raise TypeError("Expected argument 'ingress_nat_rules' to be a list")
        pulumi.set(__self__, "ingress_nat_rules", ingress_nat_rules)
        if ipsec_policies and not isinstance(ipsec_policies, list):
            raise TypeError("Expected argument 'ipsec_policies' to be a list")
        pulumi.set(__self__, "ipsec_policies", ipsec_policies)
        if local_network_gateway2 and not isinstance(local_network_gateway2, dict):
            raise TypeError("Expected argument 'local_network_gateway2' to be a dict")
        pulumi.set(__self__, "local_network_gateway2", local_network_gateway2)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if peer and not isinstance(peer, dict):
            raise TypeError("Expected argument 'peer' to be a dict")
        pulumi.set(__self__, "peer", peer)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resource_guid and not isinstance(resource_guid, str):
            raise TypeError("Expected argument 'resource_guid' to be a str")
        pulumi.set(__self__, "resource_guid", resource_guid)
        if routing_weight and not isinstance(routing_weight, int):
            raise TypeError("Expected argument 'routing_weight' to be a int")
        pulumi.set(__self__, "routing_weight", routing_weight)
        if shared_key and not isinstance(shared_key, str):
            raise TypeError("Expected argument 'shared_key' to be a str")
        pulumi.set(__self__, "shared_key", shared_key)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if traffic_selector_policies and not isinstance(traffic_selector_policies, list):
            raise TypeError("Expected argument 'traffic_selector_policies' to be a list")
        pulumi.set(__self__, "traffic_selector_policies", traffic_selector_policies)
        if tunnel_connection_status and not isinstance(tunnel_connection_status, list):
            raise TypeError("Expected argument 'tunnel_connection_status' to be a list")
        pulumi.set(__self__, "tunnel_connection_status", tunnel_connection_status)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if use_local_azure_ip_address and not isinstance(use_local_azure_ip_address, bool):
            raise TypeError("Expected argument 'use_local_azure_ip_address' to be a bool")
        pulumi.set(__self__, "use_local_azure_ip_address", use_local_azure_ip_address)
        if use_policy_based_traffic_selectors and not isinstance(use_policy_based_traffic_selectors, bool):
            raise TypeError("Expected argument 'use_policy_based_traffic_selectors' to be a bool")
        pulumi.set(__self__, "use_policy_based_traffic_selectors", use_policy_based_traffic_selectors)
        if virtual_network_gateway1 and not isinstance(virtual_network_gateway1, dict):
            raise TypeError("Expected argument 'virtual_network_gateway1' to be a dict")
        pulumi.set(__self__, "virtual_network_gateway1", virtual_network_gateway1)
        if virtual_network_gateway2 and not isinstance(virtual_network_gateway2, dict):
            raise TypeError("Expected argument 'virtual_network_gateway2' to be a dict")
        pulumi.set(__self__, "virtual_network_gateway2", virtual_network_gateway2)

    @property
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> Optional[builtins.str]:
        """
        The authorizationKey.
        """
        return pulumi.get(self, "authorization_key")

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> builtins.str:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter(name="connectionMode")
    def connection_mode(self) -> Optional[builtins.str]:
        """
        The connection mode for this connection.
        """
        return pulumi.get(self, "connection_mode")

    @property
    @pulumi.getter(name="connectionProtocol")
    def connection_protocol(self) -> Optional[builtins.str]:
        """
        Connection protocol used for this connection.
        """
        return pulumi.get(self, "connection_protocol")

    @property
    @pulumi.getter(name="connectionStatus")
    def connection_status(self) -> builtins.str:
        """
        Virtual Network Gateway connection status.
        """
        return pulumi.get(self, "connection_status")

    @property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> builtins.str:
        """
        Gateway connection type.
        """
        return pulumi.get(self, "connection_type")

    @property
    @pulumi.getter(name="dpdTimeoutSeconds")
    def dpd_timeout_seconds(self) -> Optional[builtins.int]:
        """
        The dead peer detection timeout of this connection in seconds.
        """
        return pulumi.get(self, "dpd_timeout_seconds")

    @property
    @pulumi.getter(name="egressBytesTransferred")
    def egress_bytes_transferred(self) -> builtins.float:
        """
        The egress bytes transferred in this connection.
        """
        return pulumi.get(self, "egress_bytes_transferred")

    @property
    @pulumi.getter(name="egressNatRules")
    def egress_nat_rules(self) -> Optional[Sequence['outputs.SubResourceResponse']]:
        """
        List of egress NatRules.
        """
        return pulumi.get(self, "egress_nat_rules")

    @property
    @pulumi.getter(name="enableBgp")
    def enable_bgp(self) -> Optional[builtins.bool]:
        """
        EnableBgp flag.
        """
        return pulumi.get(self, "enable_bgp")

    @property
    @pulumi.getter(name="enablePrivateLinkFastPath")
    def enable_private_link_fast_path(self) -> Optional[builtins.bool]:
        """
        Bypass the ExpressRoute gateway when accessing private-links. ExpressRoute FastPath (expressRouteGatewayBypass) must be enabled.
        """
        return pulumi.get(self, "enable_private_link_fast_path")

    @property
    @pulumi.getter
    def etag(self) -> builtins.str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="expressRouteGatewayBypass")
    def express_route_gateway_bypass(self) -> Optional[builtins.bool]:
        """
        Bypass ExpressRoute Gateway for data forwarding.
        """
        return pulumi.get(self, "express_route_gateway_bypass")

    @property
    @pulumi.getter(name="gatewayCustomBgpIpAddresses")
    def gateway_custom_bgp_ip_addresses(self) -> Optional[Sequence['outputs.GatewayCustomBgpIpAddressIpConfigurationResponse']]:
        """
        GatewayCustomBgpIpAddresses to be used for virtual network gateway Connection.
        """
        return pulumi.get(self, "gateway_custom_bgp_ip_addresses")

    @property
    @pulumi.getter
    def id(self) -> Optional[builtins.str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ingressBytesTransferred")
    def ingress_bytes_transferred(self) -> builtins.float:
        """
        The ingress bytes transferred in this connection.
        """
        return pulumi.get(self, "ingress_bytes_transferred")

    @property
    @pulumi.getter(name="ingressNatRules")
    def ingress_nat_rules(self) -> Optional[Sequence['outputs.SubResourceResponse']]:
        """
        List of ingress NatRules.
        """
        return pulumi.get(self, "ingress_nat_rules")

    @property
    @pulumi.getter(name="ipsecPolicies")
    def ipsec_policies(self) -> Optional[Sequence['outputs.IpsecPolicyResponse']]:
        """
        The IPSec Policies to be considered by this connection.
        """
        return pulumi.get(self, "ipsec_policies")

    @property
    @pulumi.getter(name="localNetworkGateway2")
    def local_network_gateway2(self) -> Optional['outputs.LocalNetworkGatewayResponse']:
        """
        The reference to local network gateway resource.
        """
        return pulumi.get(self, "local_network_gateway2")

    @property
    @pulumi.getter
    def location(self) -> Optional[builtins.str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> builtins.str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def peer(self) -> Optional['outputs.SubResourceResponse']:
        """
        The reference to peerings resource.
        """
        return pulumi.get(self, "peer")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> builtins.str:
        """
        The provisioning state of the virtual network gateway connection resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> builtins.str:
        """
        The resource GUID property of the virtual network gateway connection resource.
        """
        return pulumi.get(self, "resource_guid")

    @property
    @pulumi.getter(name="routingWeight")
    def routing_weight(self) -> Optional[builtins.int]:
        """
        The routing weight.
        """
        return pulumi.get(self, "routing_weight")

    @property
    @pulumi.getter(name="sharedKey")
    def shared_key(self) -> Optional[builtins.str]:
        """
        The IPSec shared key.
        """
        return pulumi.get(self, "shared_key")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, builtins.str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="trafficSelectorPolicies")
    def traffic_selector_policies(self) -> Optional[Sequence['outputs.TrafficSelectorPolicyResponse']]:
        """
        The Traffic Selector Policies to be considered by this connection.
        """
        return pulumi.get(self, "traffic_selector_policies")

    @property
    @pulumi.getter(name="tunnelConnectionStatus")
    def tunnel_connection_status(self) -> Sequence['outputs.TunnelConnectionHealthResponse']:
        """
        Collection of all tunnels' connection health status.
        """
        return pulumi.get(self, "tunnel_connection_status")

    @property
    @pulumi.getter
    def type(self) -> builtins.str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="useLocalAzureIpAddress")
    def use_local_azure_ip_address(self) -> Optional[builtins.bool]:
        """
        Use private local Azure IP for the connection.
        """
        return pulumi.get(self, "use_local_azure_ip_address")

    @property
    @pulumi.getter(name="usePolicyBasedTrafficSelectors")
    def use_policy_based_traffic_selectors(self) -> Optional[builtins.bool]:
        """
        Enable policy-based traffic selectors.
        """
        return pulumi.get(self, "use_policy_based_traffic_selectors")

    @property
    @pulumi.getter(name="virtualNetworkGateway1")
    def virtual_network_gateway1(self) -> 'outputs.VirtualNetworkGatewayResponse':
        """
        The reference to virtual network gateway resource.
        """
        return pulumi.get(self, "virtual_network_gateway1")

    @property
    @pulumi.getter(name="virtualNetworkGateway2")
    def virtual_network_gateway2(self) -> Optional['outputs.VirtualNetworkGatewayResponse']:
        """
        The reference to virtual network gateway resource.
        """
        return pulumi.get(self, "virtual_network_gateway2")


class AwaitableGetVirtualNetworkGatewayConnectionResult(GetVirtualNetworkGatewayConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualNetworkGatewayConnectionResult(
            authorization_key=self.authorization_key,
            azure_api_version=self.azure_api_version,
            connection_mode=self.connection_mode,
            connection_protocol=self.connection_protocol,
            connection_status=self.connection_status,
            connection_type=self.connection_type,
            dpd_timeout_seconds=self.dpd_timeout_seconds,
            egress_bytes_transferred=self.egress_bytes_transferred,
            egress_nat_rules=self.egress_nat_rules,
            enable_bgp=self.enable_bgp,
            enable_private_link_fast_path=self.enable_private_link_fast_path,
            etag=self.etag,
            express_route_gateway_bypass=self.express_route_gateway_bypass,
            gateway_custom_bgp_ip_addresses=self.gateway_custom_bgp_ip_addresses,
            id=self.id,
            ingress_bytes_transferred=self.ingress_bytes_transferred,
            ingress_nat_rules=self.ingress_nat_rules,
            ipsec_policies=self.ipsec_policies,
            local_network_gateway2=self.local_network_gateway2,
            location=self.location,
            name=self.name,
            peer=self.peer,
            provisioning_state=self.provisioning_state,
            resource_guid=self.resource_guid,
            routing_weight=self.routing_weight,
            shared_key=self.shared_key,
            tags=self.tags,
            traffic_selector_policies=self.traffic_selector_policies,
            tunnel_connection_status=self.tunnel_connection_status,
            type=self.type,
            use_local_azure_ip_address=self.use_local_azure_ip_address,
            use_policy_based_traffic_selectors=self.use_policy_based_traffic_selectors,
            virtual_network_gateway1=self.virtual_network_gateway1,
            virtual_network_gateway2=self.virtual_network_gateway2)


def get_virtual_network_gateway_connection(resource_group_name: Optional[builtins.str] = None,
                                           virtual_network_gateway_connection_name: Optional[builtins.str] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualNetworkGatewayConnectionResult:
    """
    Gets the specified virtual network gateway connection by resource group.

    Uses Azure REST API version 2024-05-01.

    Other available API versions: 2018-06-01, 2018-07-01, 2018-08-01, 2018-10-01, 2018-11-01, 2018-12-01, 2019-02-01, 2019-04-01, 2019-06-01, 2019-07-01, 2019-08-01, 2019-09-01, 2019-11-01, 2019-12-01, 2020-03-01, 2020-04-01, 2020-05-01, 2020-06-01, 2020-07-01, 2020-08-01, 2020-11-01, 2021-02-01, 2021-03-01, 2021-05-01, 2021-08-01, 2022-01-01, 2022-05-01, 2022-07-01, 2022-09-01, 2022-11-01, 2023-02-01, 2023-04-01, 2023-05-01, 2023-06-01, 2023-09-01, 2023-11-01, 2024-01-01, 2024-03-01, 2024-07-01. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native network [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param builtins.str resource_group_name: The name of the resource group.
    :param builtins.str virtual_network_gateway_connection_name: The name of the virtual network gateway connection.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['virtualNetworkGatewayConnectionName'] = virtual_network_gateway_connection_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network:getVirtualNetworkGatewayConnection', __args__, opts=opts, typ=GetVirtualNetworkGatewayConnectionResult).value

    return AwaitableGetVirtualNetworkGatewayConnectionResult(
        authorization_key=pulumi.get(__ret__, 'authorization_key'),
        azure_api_version=pulumi.get(__ret__, 'azure_api_version'),
        connection_mode=pulumi.get(__ret__, 'connection_mode'),
        connection_protocol=pulumi.get(__ret__, 'connection_protocol'),
        connection_status=pulumi.get(__ret__, 'connection_status'),
        connection_type=pulumi.get(__ret__, 'connection_type'),
        dpd_timeout_seconds=pulumi.get(__ret__, 'dpd_timeout_seconds'),
        egress_bytes_transferred=pulumi.get(__ret__, 'egress_bytes_transferred'),
        egress_nat_rules=pulumi.get(__ret__, 'egress_nat_rules'),
        enable_bgp=pulumi.get(__ret__, 'enable_bgp'),
        enable_private_link_fast_path=pulumi.get(__ret__, 'enable_private_link_fast_path'),
        etag=pulumi.get(__ret__, 'etag'),
        express_route_gateway_bypass=pulumi.get(__ret__, 'express_route_gateway_bypass'),
        gateway_custom_bgp_ip_addresses=pulumi.get(__ret__, 'gateway_custom_bgp_ip_addresses'),
        id=pulumi.get(__ret__, 'id'),
        ingress_bytes_transferred=pulumi.get(__ret__, 'ingress_bytes_transferred'),
        ingress_nat_rules=pulumi.get(__ret__, 'ingress_nat_rules'),
        ipsec_policies=pulumi.get(__ret__, 'ipsec_policies'),
        local_network_gateway2=pulumi.get(__ret__, 'local_network_gateway2'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        peer=pulumi.get(__ret__, 'peer'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        resource_guid=pulumi.get(__ret__, 'resource_guid'),
        routing_weight=pulumi.get(__ret__, 'routing_weight'),
        shared_key=pulumi.get(__ret__, 'shared_key'),
        tags=pulumi.get(__ret__, 'tags'),
        traffic_selector_policies=pulumi.get(__ret__, 'traffic_selector_policies'),
        tunnel_connection_status=pulumi.get(__ret__, 'tunnel_connection_status'),
        type=pulumi.get(__ret__, 'type'),
        use_local_azure_ip_address=pulumi.get(__ret__, 'use_local_azure_ip_address'),
        use_policy_based_traffic_selectors=pulumi.get(__ret__, 'use_policy_based_traffic_selectors'),
        virtual_network_gateway1=pulumi.get(__ret__, 'virtual_network_gateway1'),
        virtual_network_gateway2=pulumi.get(__ret__, 'virtual_network_gateway2'))
def get_virtual_network_gateway_connection_output(resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                                                  virtual_network_gateway_connection_name: Optional[pulumi.Input[builtins.str]] = None,
                                                  opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetVirtualNetworkGatewayConnectionResult]:
    """
    Gets the specified virtual network gateway connection by resource group.

    Uses Azure REST API version 2024-05-01.

    Other available API versions: 2018-06-01, 2018-07-01, 2018-08-01, 2018-10-01, 2018-11-01, 2018-12-01, 2019-02-01, 2019-04-01, 2019-06-01, 2019-07-01, 2019-08-01, 2019-09-01, 2019-11-01, 2019-12-01, 2020-03-01, 2020-04-01, 2020-05-01, 2020-06-01, 2020-07-01, 2020-08-01, 2020-11-01, 2021-02-01, 2021-03-01, 2021-05-01, 2021-08-01, 2022-01-01, 2022-05-01, 2022-07-01, 2022-09-01, 2022-11-01, 2023-02-01, 2023-04-01, 2023-05-01, 2023-06-01, 2023-09-01, 2023-11-01, 2024-01-01, 2024-03-01, 2024-07-01. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native network [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param builtins.str resource_group_name: The name of the resource group.
    :param builtins.str virtual_network_gateway_connection_name: The name of the virtual network gateway connection.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['virtualNetworkGatewayConnectionName'] = virtual_network_gateway_connection_name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('azure-native:network:getVirtualNetworkGatewayConnection', __args__, opts=opts, typ=GetVirtualNetworkGatewayConnectionResult)
    return __ret__.apply(lambda __response__: GetVirtualNetworkGatewayConnectionResult(
        authorization_key=pulumi.get(__response__, 'authorization_key'),
        azure_api_version=pulumi.get(__response__, 'azure_api_version'),
        connection_mode=pulumi.get(__response__, 'connection_mode'),
        connection_protocol=pulumi.get(__response__, 'connection_protocol'),
        connection_status=pulumi.get(__response__, 'connection_status'),
        connection_type=pulumi.get(__response__, 'connection_type'),
        dpd_timeout_seconds=pulumi.get(__response__, 'dpd_timeout_seconds'),
        egress_bytes_transferred=pulumi.get(__response__, 'egress_bytes_transferred'),
        egress_nat_rules=pulumi.get(__response__, 'egress_nat_rules'),
        enable_bgp=pulumi.get(__response__, 'enable_bgp'),
        enable_private_link_fast_path=pulumi.get(__response__, 'enable_private_link_fast_path'),
        etag=pulumi.get(__response__, 'etag'),
        express_route_gateway_bypass=pulumi.get(__response__, 'express_route_gateway_bypass'),
        gateway_custom_bgp_ip_addresses=pulumi.get(__response__, 'gateway_custom_bgp_ip_addresses'),
        id=pulumi.get(__response__, 'id'),
        ingress_bytes_transferred=pulumi.get(__response__, 'ingress_bytes_transferred'),
        ingress_nat_rules=pulumi.get(__response__, 'ingress_nat_rules'),
        ipsec_policies=pulumi.get(__response__, 'ipsec_policies'),
        local_network_gateway2=pulumi.get(__response__, 'local_network_gateway2'),
        location=pulumi.get(__response__, 'location'),
        name=pulumi.get(__response__, 'name'),
        peer=pulumi.get(__response__, 'peer'),
        provisioning_state=pulumi.get(__response__, 'provisioning_state'),
        resource_guid=pulumi.get(__response__, 'resource_guid'),
        routing_weight=pulumi.get(__response__, 'routing_weight'),
        shared_key=pulumi.get(__response__, 'shared_key'),
        tags=pulumi.get(__response__, 'tags'),
        traffic_selector_policies=pulumi.get(__response__, 'traffic_selector_policies'),
        tunnel_connection_status=pulumi.get(__response__, 'tunnel_connection_status'),
        type=pulumi.get(__response__, 'type'),
        use_local_azure_ip_address=pulumi.get(__response__, 'use_local_azure_ip_address'),
        use_policy_based_traffic_selectors=pulumi.get(__response__, 'use_policy_based_traffic_selectors'),
        virtual_network_gateway1=pulumi.get(__response__, 'virtual_network_gateway1'),
        virtual_network_gateway2=pulumi.get(__response__, 'virtual_network_gateway2')))
