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

__all__ = ['ExpressRouteConnectionInitArgs', 'ExpressRouteConnection']

@pulumi.input_type
class ExpressRouteConnectionInitArgs:
    def __init__(__self__, *,
                 express_route_circuit_peering: pulumi.Input['ExpressRouteCircuitPeeringIdArgs'],
                 express_route_gateway_name: pulumi.Input[builtins.str],
                 name: pulumi.Input[builtins.str],
                 resource_group_name: pulumi.Input[builtins.str],
                 authorization_key: Optional[pulumi.Input[builtins.str]] = None,
                 connection_name: Optional[pulumi.Input[builtins.str]] = None,
                 enable_internet_security: Optional[pulumi.Input[builtins.bool]] = None,
                 enable_private_link_fast_path: Optional[pulumi.Input[builtins.bool]] = None,
                 express_route_gateway_bypass: Optional[pulumi.Input[builtins.bool]] = None,
                 id: Optional[pulumi.Input[builtins.str]] = None,
                 routing_configuration: Optional[pulumi.Input['RoutingConfigurationArgs']] = None,
                 routing_weight: Optional[pulumi.Input[builtins.int]] = None):
        """
        The set of arguments for constructing a ExpressRouteConnection resource.
        :param pulumi.Input['ExpressRouteCircuitPeeringIdArgs'] express_route_circuit_peering: The ExpressRoute circuit peering.
        :param pulumi.Input[builtins.str] express_route_gateway_name: The name of the ExpressRoute gateway.
        :param pulumi.Input[builtins.str] name: The name of the resource.
        :param pulumi.Input[builtins.str] resource_group_name: The name of the resource group.
        :param pulumi.Input[builtins.str] authorization_key: Authorization key to establish the connection.
        :param pulumi.Input[builtins.str] connection_name: The name of the connection subresource.
        :param pulumi.Input[builtins.bool] enable_internet_security: Enable internet security.
        :param pulumi.Input[builtins.bool] enable_private_link_fast_path: Bypass the ExpressRoute gateway when accessing private-links. ExpressRoute FastPath (expressRouteGatewayBypass) must be enabled.
        :param pulumi.Input[builtins.bool] express_route_gateway_bypass: Enable FastPath to vWan Firewall hub.
        :param pulumi.Input[builtins.str] id: Resource ID.
        :param pulumi.Input['RoutingConfigurationArgs'] routing_configuration: The Routing Configuration indicating the associated and propagated route tables on this connection.
        :param pulumi.Input[builtins.int] routing_weight: The routing weight associated to the connection.
        """
        pulumi.set(__self__, "express_route_circuit_peering", express_route_circuit_peering)
        pulumi.set(__self__, "express_route_gateway_name", express_route_gateway_name)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if authorization_key is not None:
            pulumi.set(__self__, "authorization_key", authorization_key)
        if connection_name is not None:
            pulumi.set(__self__, "connection_name", connection_name)
        if enable_internet_security is not None:
            pulumi.set(__self__, "enable_internet_security", enable_internet_security)
        if enable_private_link_fast_path is not None:
            pulumi.set(__self__, "enable_private_link_fast_path", enable_private_link_fast_path)
        if express_route_gateway_bypass is not None:
            pulumi.set(__self__, "express_route_gateway_bypass", express_route_gateway_bypass)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if routing_configuration is not None:
            pulumi.set(__self__, "routing_configuration", routing_configuration)
        if routing_weight is not None:
            pulumi.set(__self__, "routing_weight", routing_weight)

    @property
    @pulumi.getter(name="expressRouteCircuitPeering")
    def express_route_circuit_peering(self) -> pulumi.Input['ExpressRouteCircuitPeeringIdArgs']:
        """
        The ExpressRoute circuit peering.
        """
        return pulumi.get(self, "express_route_circuit_peering")

    @express_route_circuit_peering.setter
    def express_route_circuit_peering(self, value: pulumi.Input['ExpressRouteCircuitPeeringIdArgs']):
        pulumi.set(self, "express_route_circuit_peering", value)

    @property
    @pulumi.getter(name="expressRouteGatewayName")
    def express_route_gateway_name(self) -> pulumi.Input[builtins.str]:
        """
        The name of the ExpressRoute gateway.
        """
        return pulumi.get(self, "express_route_gateway_name")

    @express_route_gateway_name.setter
    def express_route_gateway_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "express_route_gateway_name", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[builtins.str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "name", value)

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
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Authorization key to establish the connection.
        """
        return pulumi.get(self, "authorization_key")

    @authorization_key.setter
    def authorization_key(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "authorization_key", value)

    @property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the connection subresource.
        """
        return pulumi.get(self, "connection_name")

    @connection_name.setter
    def connection_name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "connection_name", value)

    @property
    @pulumi.getter(name="enableInternetSecurity")
    def enable_internet_security(self) -> Optional[pulumi.Input[builtins.bool]]:
        """
        Enable internet security.
        """
        return pulumi.get(self, "enable_internet_security")

    @enable_internet_security.setter
    def enable_internet_security(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "enable_internet_security", value)

    @property
    @pulumi.getter(name="enablePrivateLinkFastPath")
    def enable_private_link_fast_path(self) -> Optional[pulumi.Input[builtins.bool]]:
        """
        Bypass the ExpressRoute gateway when accessing private-links. ExpressRoute FastPath (expressRouteGatewayBypass) must be enabled.
        """
        return pulumi.get(self, "enable_private_link_fast_path")

    @enable_private_link_fast_path.setter
    def enable_private_link_fast_path(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "enable_private_link_fast_path", value)

    @property
    @pulumi.getter(name="expressRouteGatewayBypass")
    def express_route_gateway_bypass(self) -> Optional[pulumi.Input[builtins.bool]]:
        """
        Enable FastPath to vWan Firewall hub.
        """
        return pulumi.get(self, "express_route_gateway_bypass")

    @express_route_gateway_bypass.setter
    def express_route_gateway_bypass(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "express_route_gateway_bypass", value)

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
    @pulumi.getter(name="routingConfiguration")
    def routing_configuration(self) -> Optional[pulumi.Input['RoutingConfigurationArgs']]:
        """
        The Routing Configuration indicating the associated and propagated route tables on this connection.
        """
        return pulumi.get(self, "routing_configuration")

    @routing_configuration.setter
    def routing_configuration(self, value: Optional[pulumi.Input['RoutingConfigurationArgs']]):
        pulumi.set(self, "routing_configuration", value)

    @property
    @pulumi.getter(name="routingWeight")
    def routing_weight(self) -> Optional[pulumi.Input[builtins.int]]:
        """
        The routing weight associated to the connection.
        """
        return pulumi.get(self, "routing_weight")

    @routing_weight.setter
    def routing_weight(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "routing_weight", value)


@pulumi.type_token("azure-native:network:ExpressRouteConnection")
class ExpressRouteConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorization_key: Optional[pulumi.Input[builtins.str]] = None,
                 connection_name: Optional[pulumi.Input[builtins.str]] = None,
                 enable_internet_security: Optional[pulumi.Input[builtins.bool]] = None,
                 enable_private_link_fast_path: Optional[pulumi.Input[builtins.bool]] = None,
                 express_route_circuit_peering: Optional[pulumi.Input[Union['ExpressRouteCircuitPeeringIdArgs', 'ExpressRouteCircuitPeeringIdArgsDict']]] = None,
                 express_route_gateway_bypass: Optional[pulumi.Input[builtins.bool]] = None,
                 express_route_gateway_name: Optional[pulumi.Input[builtins.str]] = None,
                 id: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 routing_configuration: Optional[pulumi.Input[Union['RoutingConfigurationArgs', 'RoutingConfigurationArgsDict']]] = None,
                 routing_weight: Optional[pulumi.Input[builtins.int]] = None,
                 __props__=None):
        """
        ExpressRouteConnection resource.

        Uses Azure REST API version 2024-05-01. In version 2.x of the Azure Native provider, it used API version 2023-02-01.

        Other available API versions: 2018-08-01, 2018-10-01, 2018-11-01, 2018-12-01, 2019-02-01, 2019-04-01, 2019-06-01, 2019-07-01, 2019-08-01, 2019-09-01, 2019-11-01, 2019-12-01, 2020-03-01, 2020-04-01, 2020-05-01, 2020-06-01, 2020-07-01, 2020-08-01, 2020-11-01, 2021-02-01, 2021-03-01, 2021-05-01, 2021-08-01, 2022-01-01, 2022-05-01, 2022-07-01, 2022-09-01, 2022-11-01, 2023-02-01, 2023-04-01, 2023-05-01, 2023-06-01, 2023-09-01, 2023-11-01, 2024-01-01, 2024-03-01, 2024-07-01. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native network [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] authorization_key: Authorization key to establish the connection.
        :param pulumi.Input[builtins.str] connection_name: The name of the connection subresource.
        :param pulumi.Input[builtins.bool] enable_internet_security: Enable internet security.
        :param pulumi.Input[builtins.bool] enable_private_link_fast_path: Bypass the ExpressRoute gateway when accessing private-links. ExpressRoute FastPath (expressRouteGatewayBypass) must be enabled.
        :param pulumi.Input[Union['ExpressRouteCircuitPeeringIdArgs', 'ExpressRouteCircuitPeeringIdArgsDict']] express_route_circuit_peering: The ExpressRoute circuit peering.
        :param pulumi.Input[builtins.bool] express_route_gateway_bypass: Enable FastPath to vWan Firewall hub.
        :param pulumi.Input[builtins.str] express_route_gateway_name: The name of the ExpressRoute gateway.
        :param pulumi.Input[builtins.str] id: Resource ID.
        :param pulumi.Input[builtins.str] name: The name of the resource.
        :param pulumi.Input[builtins.str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Union['RoutingConfigurationArgs', 'RoutingConfigurationArgsDict']] routing_configuration: The Routing Configuration indicating the associated and propagated route tables on this connection.
        :param pulumi.Input[builtins.int] routing_weight: The routing weight associated to the connection.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExpressRouteConnectionInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ExpressRouteConnection resource.

        Uses Azure REST API version 2024-05-01. In version 2.x of the Azure Native provider, it used API version 2023-02-01.

        Other available API versions: 2018-08-01, 2018-10-01, 2018-11-01, 2018-12-01, 2019-02-01, 2019-04-01, 2019-06-01, 2019-07-01, 2019-08-01, 2019-09-01, 2019-11-01, 2019-12-01, 2020-03-01, 2020-04-01, 2020-05-01, 2020-06-01, 2020-07-01, 2020-08-01, 2020-11-01, 2021-02-01, 2021-03-01, 2021-05-01, 2021-08-01, 2022-01-01, 2022-05-01, 2022-07-01, 2022-09-01, 2022-11-01, 2023-02-01, 2023-04-01, 2023-05-01, 2023-06-01, 2023-09-01, 2023-11-01, 2024-01-01, 2024-03-01, 2024-07-01. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native network [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.

        :param str resource_name: The name of the resource.
        :param ExpressRouteConnectionInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExpressRouteConnectionInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorization_key: Optional[pulumi.Input[builtins.str]] = None,
                 connection_name: Optional[pulumi.Input[builtins.str]] = None,
                 enable_internet_security: Optional[pulumi.Input[builtins.bool]] = None,
                 enable_private_link_fast_path: Optional[pulumi.Input[builtins.bool]] = None,
                 express_route_circuit_peering: Optional[pulumi.Input[Union['ExpressRouteCircuitPeeringIdArgs', 'ExpressRouteCircuitPeeringIdArgsDict']]] = None,
                 express_route_gateway_bypass: Optional[pulumi.Input[builtins.bool]] = None,
                 express_route_gateway_name: Optional[pulumi.Input[builtins.str]] = None,
                 id: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 routing_configuration: Optional[pulumi.Input[Union['RoutingConfigurationArgs', 'RoutingConfigurationArgsDict']]] = None,
                 routing_weight: Optional[pulumi.Input[builtins.int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ExpressRouteConnectionInitArgs.__new__(ExpressRouteConnectionInitArgs)

            __props__.__dict__["authorization_key"] = authorization_key
            __props__.__dict__["connection_name"] = connection_name
            __props__.__dict__["enable_internet_security"] = enable_internet_security
            __props__.__dict__["enable_private_link_fast_path"] = enable_private_link_fast_path
            if express_route_circuit_peering is None and not opts.urn:
                raise TypeError("Missing required property 'express_route_circuit_peering'")
            __props__.__dict__["express_route_circuit_peering"] = express_route_circuit_peering
            __props__.__dict__["express_route_gateway_bypass"] = express_route_gateway_bypass
            if express_route_gateway_name is None and not opts.urn:
                raise TypeError("Missing required property 'express_route_gateway_name'")
            __props__.__dict__["express_route_gateway_name"] = express_route_gateway_name
            __props__.__dict__["id"] = id
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["routing_configuration"] = routing_configuration
            __props__.__dict__["routing_weight"] = routing_weight
            __props__.__dict__["azure_api_version"] = None
            __props__.__dict__["provisioning_state"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network/v20180801:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20181001:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20181101:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20181201:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20190201:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20190401:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20190601:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20190701:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20190801:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20190901:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20191101:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20191201:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20200301:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20200401:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20200501:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20200601:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20200701:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20200801:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20201101:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20210201:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20210301:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20210501:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20210801:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20220101:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20220501:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20220701:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20220901:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20221101:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20230201:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20230401:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20230501:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20230601:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20230901:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20231101:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20240101:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20240301:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20240501:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20240701:ExpressRouteConnection")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ExpressRouteConnection, __self__).__init__(
            'azure-native:network:ExpressRouteConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ExpressRouteConnection':
        """
        Get an existing ExpressRouteConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ExpressRouteConnectionInitArgs.__new__(ExpressRouteConnectionInitArgs)

        __props__.__dict__["authorization_key"] = None
        __props__.__dict__["azure_api_version"] = None
        __props__.__dict__["enable_internet_security"] = None
        __props__.__dict__["enable_private_link_fast_path"] = None
        __props__.__dict__["express_route_circuit_peering"] = None
        __props__.__dict__["express_route_gateway_bypass"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["routing_configuration"] = None
        __props__.__dict__["routing_weight"] = None
        return ExpressRouteConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        Authorization key to establish the connection.
        """
        return pulumi.get(self, "authorization_key")

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[builtins.str]:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter(name="enableInternetSecurity")
    def enable_internet_security(self) -> pulumi.Output[Optional[builtins.bool]]:
        """
        Enable internet security.
        """
        return pulumi.get(self, "enable_internet_security")

    @property
    @pulumi.getter(name="enablePrivateLinkFastPath")
    def enable_private_link_fast_path(self) -> pulumi.Output[Optional[builtins.bool]]:
        """
        Bypass the ExpressRoute gateway when accessing private-links. ExpressRoute FastPath (expressRouteGatewayBypass) must be enabled.
        """
        return pulumi.get(self, "enable_private_link_fast_path")

    @property
    @pulumi.getter(name="expressRouteCircuitPeering")
    def express_route_circuit_peering(self) -> pulumi.Output['outputs.ExpressRouteCircuitPeeringIdResponse']:
        """
        The ExpressRoute circuit peering.
        """
        return pulumi.get(self, "express_route_circuit_peering")

    @property
    @pulumi.getter(name="expressRouteGatewayBypass")
    def express_route_gateway_bypass(self) -> pulumi.Output[Optional[builtins.bool]]:
        """
        Enable FastPath to vWan Firewall hub.
        """
        return pulumi.get(self, "express_route_gateway_bypass")

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
        The provisioning state of the express route connection resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="routingConfiguration")
    def routing_configuration(self) -> pulumi.Output[Optional['outputs.RoutingConfigurationResponse']]:
        """
        The Routing Configuration indicating the associated and propagated route tables on this connection.
        """
        return pulumi.get(self, "routing_configuration")

    @property
    @pulumi.getter(name="routingWeight")
    def routing_weight(self) -> pulumi.Output[Optional[builtins.int]]:
        """
        The routing weight associated to the connection.
        """
        return pulumi.get(self, "routing_weight")

