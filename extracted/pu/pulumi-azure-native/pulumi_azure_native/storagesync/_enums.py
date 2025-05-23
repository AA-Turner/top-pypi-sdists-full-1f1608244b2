# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
import pulumi
from enum import Enum

__all__ = [
    'FeatureStatus',
    'IncomingTrafficPolicy',
    'InitialDownloadPolicy',
    'InitialUploadPolicy',
    'LocalCacheMode',
    'ManagedServiceIdentityType',
    'PrivateEndpointServiceConnectionStatus',
]


@pulumi.type_token("azure-native:storagesync:FeatureStatus")
class FeatureStatus(builtins.str, Enum):
    """
    Offline data transfer
    """
    ON = "on"
    OFF = "off"


@pulumi.type_token("azure-native:storagesync:IncomingTrafficPolicy")
class IncomingTrafficPolicy(builtins.str, Enum):
    """
    Incoming Traffic Policy
    """
    ALLOW_ALL_TRAFFIC = "AllowAllTraffic"
    ALLOW_VIRTUAL_NETWORKS_ONLY = "AllowVirtualNetworksOnly"


@pulumi.type_token("azure-native:storagesync:InitialDownloadPolicy")
class InitialDownloadPolicy(builtins.str, Enum):
    """
    Policy for how namespace and files are recalled during FastDr.
    """
    NAMESPACE_ONLY = "NamespaceOnly"
    NAMESPACE_THEN_MODIFIED_FILES = "NamespaceThenModifiedFiles"
    AVOID_TIERED_FILES = "AvoidTieredFiles"


@pulumi.type_token("azure-native:storagesync:InitialUploadPolicy")
class InitialUploadPolicy(builtins.str, Enum):
    """
    Policy for how the initial upload sync session is performed.
    """
    SERVER_AUTHORITATIVE = "ServerAuthoritative"
    MERGE = "Merge"


@pulumi.type_token("azure-native:storagesync:LocalCacheMode")
class LocalCacheMode(builtins.str, Enum):
    """
    Policy for enabling follow-the-sun business models: link local cache to cloud behavior to pre-populate before local access.
    """
    DOWNLOAD_NEW_AND_MODIFIED_FILES = "DownloadNewAndModifiedFiles"
    UPDATE_LOCALLY_CACHED_FILES = "UpdateLocallyCachedFiles"


@pulumi.type_token("azure-native:storagesync:ManagedServiceIdentityType")
class ManagedServiceIdentityType(builtins.str, Enum):
    """
    Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"


@pulumi.type_token("azure-native:storagesync:PrivateEndpointServiceConnectionStatus")
class PrivateEndpointServiceConnectionStatus(builtins.str, Enum):
    """
    Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
