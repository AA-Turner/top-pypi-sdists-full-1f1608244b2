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

__all__ = [
    'ConnectivityCollectionResponse',
    'ManagedNetworkGroupResponse',
    'ManagedNetworkPeeringPolicyPropertiesResponse',
    'ManagedNetworkPeeringPolicyResponse',
    'ResourceIdResponse',
    'ScopeResponse',
]

@pulumi.output_type
class ConnectivityCollectionResponse(dict):
    """
    The collection of Connectivity related groups and policies within the Managed Network
    """
    def __init__(__self__, *,
                 groups: Sequence['outputs.ManagedNetworkGroupResponse'],
                 peerings: Sequence['outputs.ManagedNetworkPeeringPolicyResponse']):
        """
        The collection of Connectivity related groups and policies within the Managed Network
        :param Sequence['ManagedNetworkGroupResponse'] groups: The collection of connectivity related Managed Network Groups within the Managed Network
        :param Sequence['ManagedNetworkPeeringPolicyResponse'] peerings: The collection of Managed Network Peering Policies within the Managed Network
        """
        pulumi.set(__self__, "groups", groups)
        pulumi.set(__self__, "peerings", peerings)

    @property
    @pulumi.getter
    def groups(self) -> Sequence['outputs.ManagedNetworkGroupResponse']:
        """
        The collection of connectivity related Managed Network Groups within the Managed Network
        """
        return pulumi.get(self, "groups")

    @property
    @pulumi.getter
    def peerings(self) -> Sequence['outputs.ManagedNetworkPeeringPolicyResponse']:
        """
        The collection of Managed Network Peering Policies within the Managed Network
        """
        return pulumi.get(self, "peerings")


@pulumi.output_type
class ManagedNetworkGroupResponse(dict):
    """
    The Managed Network Group resource
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "provisioningState":
            suggest = "provisioning_state"
        elif key == "managementGroups":
            suggest = "management_groups"
        elif key == "virtualNetworks":
            suggest = "virtual_networks"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ManagedNetworkGroupResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ManagedNetworkGroupResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ManagedNetworkGroupResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 etag: builtins.str,
                 id: builtins.str,
                 name: builtins.str,
                 provisioning_state: builtins.str,
                 type: builtins.str,
                 kind: Optional[builtins.str] = None,
                 location: Optional[builtins.str] = None,
                 management_groups: Optional[Sequence['outputs.ResourceIdResponse']] = None,
                 subnets: Optional[Sequence['outputs.ResourceIdResponse']] = None,
                 subscriptions: Optional[Sequence['outputs.ResourceIdResponse']] = None,
                 virtual_networks: Optional[Sequence['outputs.ResourceIdResponse']] = None):
        """
        The Managed Network Group resource
        :param builtins.str etag: A unique read-only string that changes whenever the resource is updated.
        :param builtins.str id: Fully qualified resource Id for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        :param builtins.str name: The name of the resource
        :param builtins.str provisioning_state: Provisioning state of the ManagedNetwork resource.
        :param builtins.str type: The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
        :param builtins.str kind: Responsibility role under which this Managed Network Group will be created
        :param builtins.str location: The geo-location where the resource lives
        :param Sequence['ResourceIdResponse'] management_groups: The collection of management groups covered by the Managed Network
        :param Sequence['ResourceIdResponse'] subnets: The collection of  subnets covered by the Managed Network
        :param Sequence['ResourceIdResponse'] subscriptions: The collection of subscriptions covered by the Managed Network
        :param Sequence['ResourceIdResponse'] virtual_networks: The collection of virtual nets covered by the Managed Network
        """
        pulumi.set(__self__, "etag", etag)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        pulumi.set(__self__, "type", type)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if management_groups is not None:
            pulumi.set(__self__, "management_groups", management_groups)
        if subnets is not None:
            pulumi.set(__self__, "subnets", subnets)
        if subscriptions is not None:
            pulumi.set(__self__, "subscriptions", subscriptions)
        if virtual_networks is not None:
            pulumi.set(__self__, "virtual_networks", virtual_networks)

    @property
    @pulumi.getter
    def etag(self) -> builtins.str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        """
        Fully qualified resource Id for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> builtins.str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> builtins.str:
        """
        Provisioning state of the ManagedNetwork resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> builtins.str:
        """
        The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def kind(self) -> Optional[builtins.str]:
        """
        Responsibility role under which this Managed Network Group will be created
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> Optional[builtins.str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managementGroups")
    def management_groups(self) -> Optional[Sequence['outputs.ResourceIdResponse']]:
        """
        The collection of management groups covered by the Managed Network
        """
        return pulumi.get(self, "management_groups")

    @property
    @pulumi.getter
    def subnets(self) -> Optional[Sequence['outputs.ResourceIdResponse']]:
        """
        The collection of  subnets covered by the Managed Network
        """
        return pulumi.get(self, "subnets")

    @property
    @pulumi.getter
    def subscriptions(self) -> Optional[Sequence['outputs.ResourceIdResponse']]:
        """
        The collection of subscriptions covered by the Managed Network
        """
        return pulumi.get(self, "subscriptions")

    @property
    @pulumi.getter(name="virtualNetworks")
    def virtual_networks(self) -> Optional[Sequence['outputs.ResourceIdResponse']]:
        """
        The collection of virtual nets covered by the Managed Network
        """
        return pulumi.get(self, "virtual_networks")


@pulumi.output_type
class ManagedNetworkPeeringPolicyPropertiesResponse(dict):
    """
    Properties of a Managed Network Peering Policy
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "provisioningState":
            suggest = "provisioning_state"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ManagedNetworkPeeringPolicyPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ManagedNetworkPeeringPolicyPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ManagedNetworkPeeringPolicyPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 etag: builtins.str,
                 provisioning_state: builtins.str,
                 type: builtins.str,
                 hub: Optional['outputs.ResourceIdResponse'] = None,
                 mesh: Optional[Sequence['outputs.ResourceIdResponse']] = None,
                 spokes: Optional[Sequence['outputs.ResourceIdResponse']] = None):
        """
        Properties of a Managed Network Peering Policy
        :param builtins.str etag: A unique read-only string that changes whenever the resource is updated.
        :param builtins.str provisioning_state: Provisioning state of the ManagedNetwork resource.
        :param builtins.str type: Gets or sets the connectivity type of a network structure policy
        :param 'ResourceIdResponse' hub: Gets or sets the hub virtual network ID
        :param Sequence['ResourceIdResponse'] mesh: Gets or sets the mesh group IDs
        :param Sequence['ResourceIdResponse'] spokes: Gets or sets the spokes group IDs
        """
        pulumi.set(__self__, "etag", etag)
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        pulumi.set(__self__, "type", type)
        if hub is not None:
            pulumi.set(__self__, "hub", hub)
        if mesh is not None:
            pulumi.set(__self__, "mesh", mesh)
        if spokes is not None:
            pulumi.set(__self__, "spokes", spokes)

    @property
    @pulumi.getter
    def etag(self) -> builtins.str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> builtins.str:
        """
        Provisioning state of the ManagedNetwork resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> builtins.str:
        """
        Gets or sets the connectivity type of a network structure policy
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def hub(self) -> Optional['outputs.ResourceIdResponse']:
        """
        Gets or sets the hub virtual network ID
        """
        return pulumi.get(self, "hub")

    @property
    @pulumi.getter
    def mesh(self) -> Optional[Sequence['outputs.ResourceIdResponse']]:
        """
        Gets or sets the mesh group IDs
        """
        return pulumi.get(self, "mesh")

    @property
    @pulumi.getter
    def spokes(self) -> Optional[Sequence['outputs.ResourceIdResponse']]:
        """
        Gets or sets the spokes group IDs
        """
        return pulumi.get(self, "spokes")


@pulumi.output_type
class ManagedNetworkPeeringPolicyResponse(dict):
    """
    The Managed Network Peering Policy resource
    """
    def __init__(__self__, *,
                 id: builtins.str,
                 name: builtins.str,
                 type: builtins.str,
                 location: Optional[builtins.str] = None,
                 properties: Optional['outputs.ManagedNetworkPeeringPolicyPropertiesResponse'] = None):
        """
        The Managed Network Peering Policy resource
        :param builtins.str id: Fully qualified resource Id for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        :param builtins.str name: The name of the resource
        :param builtins.str type: The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
        :param builtins.str location: The geo-location where the resource lives
        :param 'ManagedNetworkPeeringPolicyPropertiesResponse' properties: Gets or sets the properties of a Managed Network Policy
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", type)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        """
        Fully qualified resource Id for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> builtins.str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> builtins.str:
        """
        The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def location(self) -> Optional[builtins.str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def properties(self) -> Optional['outputs.ManagedNetworkPeeringPolicyPropertiesResponse']:
        """
        Gets or sets the properties of a Managed Network Policy
        """
        return pulumi.get(self, "properties")


@pulumi.output_type
class ResourceIdResponse(dict):
    """
    Generic pointer to a resource
    """
    def __init__(__self__, *,
                 id: Optional[builtins.str] = None):
        """
        Generic pointer to a resource
        :param builtins.str id: Resource Id
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[builtins.str]:
        """
        Resource Id
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class ScopeResponse(dict):
    """
    Scope of a Managed Network
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "managementGroups":
            suggest = "management_groups"
        elif key == "virtualNetworks":
            suggest = "virtual_networks"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScopeResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScopeResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScopeResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 management_groups: Optional[Sequence['outputs.ResourceIdResponse']] = None,
                 subnets: Optional[Sequence['outputs.ResourceIdResponse']] = None,
                 subscriptions: Optional[Sequence['outputs.ResourceIdResponse']] = None,
                 virtual_networks: Optional[Sequence['outputs.ResourceIdResponse']] = None):
        """
        Scope of a Managed Network
        :param Sequence['ResourceIdResponse'] management_groups: The collection of management groups covered by the Managed Network
        :param Sequence['ResourceIdResponse'] subnets: The collection of  subnets covered by the Managed Network
        :param Sequence['ResourceIdResponse'] subscriptions: The collection of subscriptions covered by the Managed Network
        :param Sequence['ResourceIdResponse'] virtual_networks: The collection of virtual nets covered by the Managed Network
        """
        if management_groups is not None:
            pulumi.set(__self__, "management_groups", management_groups)
        if subnets is not None:
            pulumi.set(__self__, "subnets", subnets)
        if subscriptions is not None:
            pulumi.set(__self__, "subscriptions", subscriptions)
        if virtual_networks is not None:
            pulumi.set(__self__, "virtual_networks", virtual_networks)

    @property
    @pulumi.getter(name="managementGroups")
    def management_groups(self) -> Optional[Sequence['outputs.ResourceIdResponse']]:
        """
        The collection of management groups covered by the Managed Network
        """
        return pulumi.get(self, "management_groups")

    @property
    @pulumi.getter
    def subnets(self) -> Optional[Sequence['outputs.ResourceIdResponse']]:
        """
        The collection of  subnets covered by the Managed Network
        """
        return pulumi.get(self, "subnets")

    @property
    @pulumi.getter
    def subscriptions(self) -> Optional[Sequence['outputs.ResourceIdResponse']]:
        """
        The collection of subscriptions covered by the Managed Network
        """
        return pulumi.get(self, "subscriptions")

    @property
    @pulumi.getter(name="virtualNetworks")
    def virtual_networks(self) -> Optional[Sequence['outputs.ResourceIdResponse']]:
        """
        The collection of virtual nets covered by the Managed Network
        """
        return pulumi.get(self, "virtual_networks")


