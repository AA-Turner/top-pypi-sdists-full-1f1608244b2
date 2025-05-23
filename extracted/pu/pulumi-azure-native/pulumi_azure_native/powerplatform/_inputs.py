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
from ._enums import *

__all__ = [
    'EnterprisePolicyIdentityArgs',
    'EnterprisePolicyIdentityArgsDict',
    'KeyPropertiesArgs',
    'KeyPropertiesArgsDict',
    'KeyVaultPropertiesArgs',
    'KeyVaultPropertiesArgsDict',
    'PrivateLinkServiceConnectionStateArgs',
    'PrivateLinkServiceConnectionStateArgsDict',
    'PropertiesEncryptionArgs',
    'PropertiesEncryptionArgsDict',
    'PropertiesLockboxArgs',
    'PropertiesLockboxArgsDict',
    'PropertiesNetworkInjectionArgs',
    'PropertiesNetworkInjectionArgsDict',
    'SubnetPropertiesArgs',
    'SubnetPropertiesArgsDict',
    'VirtualNetworkPropertiesArgs',
    'VirtualNetworkPropertiesArgsDict',
]

MYPY = False

if not MYPY:
    class EnterprisePolicyIdentityArgsDict(TypedDict):
        """
        The identity of the EnterprisePolicy.
        """
        type: NotRequired[pulumi.Input['ResourceIdentityType']]
        """
        The type of identity used for the EnterprisePolicy. Currently, the only supported type is 'SystemAssigned', which implicitly creates an identity.
        """
elif False:
    EnterprisePolicyIdentityArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class EnterprisePolicyIdentityArgs:
    def __init__(__self__, *,
                 type: Optional[pulumi.Input['ResourceIdentityType']] = None):
        """
        The identity of the EnterprisePolicy.
        :param pulumi.Input['ResourceIdentityType'] type: The type of identity used for the EnterprisePolicy. Currently, the only supported type is 'SystemAssigned', which implicitly creates an identity.
        """
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input['ResourceIdentityType']]:
        """
        The type of identity used for the EnterprisePolicy. Currently, the only supported type is 'SystemAssigned', which implicitly creates an identity.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input['ResourceIdentityType']]):
        pulumi.set(self, "type", value)


if not MYPY:
    class KeyPropertiesArgsDict(TypedDict):
        """
        Url and version of the KeyVault Secret
        """
        name: NotRequired[pulumi.Input[builtins.str]]
        """
        The identifier of the key vault key used to encrypt data.
        """
        version: NotRequired[pulumi.Input[builtins.str]]
        """
        The version of the identity which will be used to access key vault.
        """
elif False:
    KeyPropertiesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class KeyPropertiesArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 version: Optional[pulumi.Input[builtins.str]] = None):
        """
        Url and version of the KeyVault Secret
        :param pulumi.Input[builtins.str] name: The identifier of the key vault key used to encrypt data.
        :param pulumi.Input[builtins.str] version: The version of the identity which will be used to access key vault.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The identifier of the key vault key used to encrypt data.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The version of the identity which will be used to access key vault.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "version", value)


if not MYPY:
    class KeyVaultPropertiesArgsDict(TypedDict):
        """
        Settings concerning key vault encryption for a configuration store.
        """
        id: NotRequired[pulumi.Input[builtins.str]]
        """
        Uri of KeyVault
        """
        key: NotRequired[pulumi.Input['KeyPropertiesArgsDict']]
        """
        Identity of the secret that includes name and version.
        """
elif False:
    KeyVaultPropertiesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class KeyVaultPropertiesArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[builtins.str]] = None,
                 key: Optional[pulumi.Input['KeyPropertiesArgs']] = None):
        """
        Settings concerning key vault encryption for a configuration store.
        :param pulumi.Input[builtins.str] id: Uri of KeyVault
        :param pulumi.Input['KeyPropertiesArgs'] key: Identity of the secret that includes name and version.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)
        if key is not None:
            pulumi.set(__self__, "key", key)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Uri of KeyVault
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input['KeyPropertiesArgs']]:
        """
        Identity of the secret that includes name and version.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input['KeyPropertiesArgs']]):
        pulumi.set(self, "key", value)


if not MYPY:
    class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
        """
        A collection of information about the state of the connection between service consumer and provider.
        """
        actions_required: NotRequired[pulumi.Input[builtins.str]]
        """
        A message indicating if changes on the service provider require any updates on the consumer.
        """
        description: NotRequired[pulumi.Input[builtins.str]]
        """
        The reason for approval/rejection of the connection.
        """
        status: NotRequired[pulumi.Input[Union[builtins.str, 'PrivateEndpointServiceConnectionStatus']]]
        """
        Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
elif False:
    PrivateLinkServiceConnectionStateArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(__self__, *,
                 actions_required: Optional[pulumi.Input[builtins.str]] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 status: Optional[pulumi.Input[Union[builtins.str, 'PrivateEndpointServiceConnectionStatus']]] = None):
        """
        A collection of information about the state of the connection between service consumer and provider.
        :param pulumi.Input[builtins.str] actions_required: A message indicating if changes on the service provider require any updates on the consumer.
        :param pulumi.Input[builtins.str] description: The reason for approval/rejection of the connection.
        :param pulumi.Input[Union[builtins.str, 'PrivateEndpointServiceConnectionStatus']] status: Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        if actions_required is not None:
            pulumi.set(__self__, "actions_required", actions_required)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        A message indicating if changes on the service provider require any updates on the consumer.
        """
        return pulumi.get(self, "actions_required")

    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "actions_required", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The reason for approval/rejection of the connection.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[builtins.str, 'PrivateEndpointServiceConnectionStatus']]]:
        """
        Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[builtins.str, 'PrivateEndpointServiceConnectionStatus']]]):
        pulumi.set(self, "status", value)


if not MYPY:
    class PropertiesEncryptionArgsDict(TypedDict):
        """
        The encryption settings for a configuration store.
        """
        key_vault: NotRequired[pulumi.Input['KeyVaultPropertiesArgsDict']]
        """
        Key vault properties.
        """
        state: NotRequired[pulumi.Input[Union[builtins.str, 'State']]]
        """
        The state of onboarding, which only appears in the response.
        """
elif False:
    PropertiesEncryptionArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PropertiesEncryptionArgs:
    def __init__(__self__, *,
                 key_vault: Optional[pulumi.Input['KeyVaultPropertiesArgs']] = None,
                 state: Optional[pulumi.Input[Union[builtins.str, 'State']]] = None):
        """
        The encryption settings for a configuration store.
        :param pulumi.Input['KeyVaultPropertiesArgs'] key_vault: Key vault properties.
        :param pulumi.Input[Union[builtins.str, 'State']] state: The state of onboarding, which only appears in the response.
        """
        if key_vault is not None:
            pulumi.set(__self__, "key_vault", key_vault)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="keyVault")
    def key_vault(self) -> Optional[pulumi.Input['KeyVaultPropertiesArgs']]:
        """
        Key vault properties.
        """
        return pulumi.get(self, "key_vault")

    @key_vault.setter
    def key_vault(self, value: Optional[pulumi.Input['KeyVaultPropertiesArgs']]):
        pulumi.set(self, "key_vault", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[builtins.str, 'State']]]:
        """
        The state of onboarding, which only appears in the response.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[builtins.str, 'State']]]):
        pulumi.set(self, "state", value)


if not MYPY:
    class PropertiesLockboxArgsDict(TypedDict):
        """
        Settings concerning lockbox.
        """
        state: NotRequired[pulumi.Input[Union[builtins.str, 'State']]]
        """
        lockbox configuration
        """
elif False:
    PropertiesLockboxArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PropertiesLockboxArgs:
    def __init__(__self__, *,
                 state: Optional[pulumi.Input[Union[builtins.str, 'State']]] = None):
        """
        Settings concerning lockbox.
        :param pulumi.Input[Union[builtins.str, 'State']] state: lockbox configuration
        """
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[builtins.str, 'State']]]:
        """
        lockbox configuration
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[builtins.str, 'State']]]):
        pulumi.set(self, "state", value)


if not MYPY:
    class PropertiesNetworkInjectionArgsDict(TypedDict):
        """
        Settings concerning network injection.
        """
        virtual_networks: NotRequired[pulumi.Input[Sequence[pulumi.Input['VirtualNetworkPropertiesArgsDict']]]]
        """
        Network injection configuration
        """
elif False:
    PropertiesNetworkInjectionArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PropertiesNetworkInjectionArgs:
    def __init__(__self__, *,
                 virtual_networks: Optional[pulumi.Input[Sequence[pulumi.Input['VirtualNetworkPropertiesArgs']]]] = None):
        """
        Settings concerning network injection.
        :param pulumi.Input[Sequence[pulumi.Input['VirtualNetworkPropertiesArgs']]] virtual_networks: Network injection configuration
        """
        if virtual_networks is not None:
            pulumi.set(__self__, "virtual_networks", virtual_networks)

    @property
    @pulumi.getter(name="virtualNetworks")
    def virtual_networks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VirtualNetworkPropertiesArgs']]]]:
        """
        Network injection configuration
        """
        return pulumi.get(self, "virtual_networks")

    @virtual_networks.setter
    def virtual_networks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VirtualNetworkPropertiesArgs']]]]):
        pulumi.set(self, "virtual_networks", value)


if not MYPY:
    class SubnetPropertiesArgsDict(TypedDict):
        """
        Properties of a subnet.
        """
        name: NotRequired[pulumi.Input[builtins.str]]
        """
        Subnet name.
        """
elif False:
    SubnetPropertiesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SubnetPropertiesArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[builtins.str]] = None):
        """
        Properties of a subnet.
        :param pulumi.Input[builtins.str] name: Subnet name.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Subnet name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)


if not MYPY:
    class VirtualNetworkPropertiesArgsDict(TypedDict):
        """
        Settings concerning the virtual network.
        """
        id: NotRequired[pulumi.Input[builtins.str]]
        """
        Uri of the virtual network.
        """
        subnet: NotRequired[pulumi.Input['SubnetPropertiesArgsDict']]
        """
        Properties of a subnet.
        """
elif False:
    VirtualNetworkPropertiesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class VirtualNetworkPropertiesArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[builtins.str]] = None,
                 subnet: Optional[pulumi.Input['SubnetPropertiesArgs']] = None):
        """
        Settings concerning the virtual network.
        :param pulumi.Input[builtins.str] id: Uri of the virtual network.
        :param pulumi.Input['SubnetPropertiesArgs'] subnet: Properties of a subnet.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)
        if subnet is not None:
            pulumi.set(__self__, "subnet", subnet)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Uri of the virtual network.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input['SubnetPropertiesArgs']]:
        """
        Properties of a subnet.
        """
        return pulumi.get(self, "subnet")

    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input['SubnetPropertiesArgs']]):
        pulumi.set(self, "subnet", value)


