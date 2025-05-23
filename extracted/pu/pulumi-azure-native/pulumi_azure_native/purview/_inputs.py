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
    'AccountSkuArgs',
    'AccountSkuArgsDict',
    'CredentialsArgs',
    'CredentialsArgsDict',
    'IdentityArgs',
    'IdentityArgsDict',
    'IngestionStorageArgs',
    'IngestionStorageArgsDict',
    'PrivateEndpointArgs',
    'PrivateEndpointArgsDict',
    'PrivateLinkServiceConnectionStateArgs',
    'PrivateLinkServiceConnectionStateArgsDict',
]

MYPY = False

if not MYPY:
    class AccountSkuArgsDict(TypedDict):
        """
        Gets or sets the Sku.
        """
        capacity: NotRequired[pulumi.Input[builtins.int]]
        """
        Gets or sets the sku capacity.
        """
        name: NotRequired[pulumi.Input[Union[builtins.str, 'AccountSkuName']]]
        """
        Gets or sets the sku name.
        """
elif False:
    AccountSkuArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class AccountSkuArgs:
    def __init__(__self__, *,
                 capacity: Optional[pulumi.Input[builtins.int]] = None,
                 name: Optional[pulumi.Input[Union[builtins.str, 'AccountSkuName']]] = None):
        """
        Gets or sets the Sku.
        :param pulumi.Input[builtins.int] capacity: Gets or sets the sku capacity.
        :param pulumi.Input[Union[builtins.str, 'AccountSkuName']] name: Gets or sets the sku name.
        """
        if capacity is not None:
            pulumi.set(__self__, "capacity", capacity)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[builtins.int]]:
        """
        Gets or sets the sku capacity.
        """
        return pulumi.get(self, "capacity")

    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "capacity", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[Union[builtins.str, 'AccountSkuName']]]:
        """
        Gets or sets the sku name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[Union[builtins.str, 'AccountSkuName']]]):
        pulumi.set(self, "name", value)


if not MYPY:
    class CredentialsArgsDict(TypedDict):
        """
        Credentials to access the event streaming service attached to the purview account.
        """
        identity_id: NotRequired[pulumi.Input[builtins.str]]
        """
        Identity identifier for UserAssign type.
        """
        type: NotRequired[pulumi.Input[Union[builtins.str, 'KafkaConfigurationIdentityType']]]
        """
        Identity Type.
        """
elif False:
    CredentialsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class CredentialsArgs:
    def __init__(__self__, *,
                 identity_id: Optional[pulumi.Input[builtins.str]] = None,
                 type: Optional[pulumi.Input[Union[builtins.str, 'KafkaConfigurationIdentityType']]] = None):
        """
        Credentials to access the event streaming service attached to the purview account.
        :param pulumi.Input[builtins.str] identity_id: Identity identifier for UserAssign type.
        :param pulumi.Input[Union[builtins.str, 'KafkaConfigurationIdentityType']] type: Identity Type.
        """
        if identity_id is not None:
            pulumi.set(__self__, "identity_id", identity_id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="identityId")
    def identity_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Identity identifier for UserAssign type.
        """
        return pulumi.get(self, "identity_id")

    @identity_id.setter
    def identity_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "identity_id", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[builtins.str, 'KafkaConfigurationIdentityType']]]:
        """
        Identity Type.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[builtins.str, 'KafkaConfigurationIdentityType']]]):
        pulumi.set(self, "type", value)


if not MYPY:
    class IdentityArgsDict(TypedDict):
        """
        The Managed Identity of the resource
        """
        type: NotRequired[pulumi.Input[Union[builtins.str, 'ManagedIdentityType']]]
        """
        Identity Type
        """
        user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]
        """
        User Assigned Identities
        """
elif False:
    IdentityArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class IdentityArgs:
    def __init__(__self__, *,
                 type: Optional[pulumi.Input[Union[builtins.str, 'ManagedIdentityType']]] = None,
                 user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None):
        """
        The Managed Identity of the resource
        :param pulumi.Input[Union[builtins.str, 'ManagedIdentityType']] type: Identity Type
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] user_assigned_identities: User Assigned Identities
        """
        if type is not None:
            pulumi.set(__self__, "type", type)
        if user_assigned_identities is not None:
            pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[builtins.str, 'ManagedIdentityType']]]:
        """
        Identity Type
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[builtins.str, 'ManagedIdentityType']]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]:
        """
        User Assigned Identities
        """
        return pulumi.get(self, "user_assigned_identities")

    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "user_assigned_identities", value)


if not MYPY:
    class IngestionStorageArgsDict(TypedDict):
        """
        Ingestion Storage Account Info
        """
        public_network_access: NotRequired[pulumi.Input[Union[builtins.str, 'PublicNetworkAccess']]]
        """
        Gets or sets the public network access setting
        """
elif False:
    IngestionStorageArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class IngestionStorageArgs:
    def __init__(__self__, *,
                 public_network_access: Optional[pulumi.Input[Union[builtins.str, 'PublicNetworkAccess']]] = None):
        """
        Ingestion Storage Account Info
        :param pulumi.Input[Union[builtins.str, 'PublicNetworkAccess']] public_network_access: Gets or sets the public network access setting
        """
        if public_network_access is not None:
            pulumi.set(__self__, "public_network_access", public_network_access)

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[builtins.str, 'PublicNetworkAccess']]]:
        """
        Gets or sets the public network access setting
        """
        return pulumi.get(self, "public_network_access")

    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[builtins.str, 'PublicNetworkAccess']]]):
        pulumi.set(self, "public_network_access", value)


if not MYPY:
    class PrivateEndpointArgsDict(TypedDict):
        """
        A private endpoint class.
        """
        id: NotRequired[pulumi.Input[builtins.str]]
        """
        The private endpoint identifier.
        """
elif False:
    PrivateEndpointArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PrivateEndpointArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[builtins.str]] = None):
        """
        A private endpoint class.
        :param pulumi.Input[builtins.str] id: The private endpoint identifier.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The private endpoint identifier.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "id", value)


if not MYPY:
    class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
        """
        The private link service connection state.
        """
        actions_required: NotRequired[pulumi.Input[builtins.str]]
        """
        The required actions.
        """
        description: NotRequired[pulumi.Input[builtins.str]]
        """
        The description.
        """
        status: NotRequired[pulumi.Input[Union[builtins.str, 'PrivateEndpointConnectionStatus']]]
        """
        The status.
        """
elif False:
    PrivateLinkServiceConnectionStateArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(__self__, *,
                 actions_required: Optional[pulumi.Input[builtins.str]] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 status: Optional[pulumi.Input[Union[builtins.str, 'PrivateEndpointConnectionStatus']]] = None):
        """
        The private link service connection state.
        :param pulumi.Input[builtins.str] actions_required: The required actions.
        :param pulumi.Input[builtins.str] description: The description.
        :param pulumi.Input[Union[builtins.str, 'PrivateEndpointConnectionStatus']] status: The status.
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
        The required actions.
        """
        return pulumi.get(self, "actions_required")

    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "actions_required", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[builtins.str, 'PrivateEndpointConnectionStatus']]]:
        """
        The status.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[builtins.str, 'PrivateEndpointConnectionStatus']]]):
        pulumi.set(self, "status", value)


