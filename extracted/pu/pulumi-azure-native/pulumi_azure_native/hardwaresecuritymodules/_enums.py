# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
import pulumi
from enum import Enum

__all__ = [
    'AutoGeneratedDomainNameLabelScope',
    'CloudHsmClusterSkuFamily',
    'CloudHsmClusterSkuName',
    'ManagedServiceIdentityType',
    'PrivateEndpointServiceConnectionStatus',
    'PublicNetworkAccess',
    'SkuName',
]


@pulumi.type_token("azure-native:hardwaresecuritymodules:AutoGeneratedDomainNameLabelScope")
class AutoGeneratedDomainNameLabelScope(builtins.str, Enum):
    """
    The Cloud HSM Cluster's auto-generated Domain Name Label Scope
    """
    TENANT_REUSE = "TenantReuse"
    SUBSCRIPTION_REUSE = "SubscriptionReuse"
    RESOURCE_GROUP_REUSE = "ResourceGroupReuse"
    NO_REUSE = "NoReuse"


@pulumi.type_token("azure-native:hardwaresecuritymodules:CloudHsmClusterSkuFamily")
class CloudHsmClusterSkuFamily(builtins.str, Enum):
    """
    Sku family of the Cloud HSM Cluster
    """
    B = "B"


@pulumi.type_token("azure-native:hardwaresecuritymodules:CloudHsmClusterSkuName")
class CloudHsmClusterSkuName(builtins.str, Enum):
    """
    Sku name of the Cloud HSM Cluster
    """
    STANDARD_B1 = "Standard_B1"
    STANDARD_B10 = "Standard B10"


@pulumi.type_token("azure-native:hardwaresecuritymodules:ManagedServiceIdentityType")
class ManagedServiceIdentityType(builtins.str, Enum):
    """
    Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"


@pulumi.type_token("azure-native:hardwaresecuritymodules:PrivateEndpointServiceConnectionStatus")
class PrivateEndpointServiceConnectionStatus(builtins.str, Enum):
    """
    Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


@pulumi.type_token("azure-native:hardwaresecuritymodules:PublicNetworkAccess")
class PublicNetworkAccess(builtins.str, Enum):
    """
    The Cloud HSM Cluster public network access
    """
    DISABLED = "Disabled"


@pulumi.type_token("azure-native:hardwaresecuritymodules:SkuName")
class SkuName(builtins.str, Enum):
    """
    SKU of the dedicated HSM
    """
    SAFE_NET_LUNA_NETWORK_HS_M_A790 = "SafeNet Luna Network HSM A790"
    """
    The dedicated HSM is a Safenet Luna Network HSM A790 device.
    """
    PAY_SHIELD10_K_LMK1_CPS60 = "payShield10K_LMK1_CPS60"
    """
    The dedicated HSM is a payShield 10K, model PS10-D, 10Gb Ethernet Hardware Platform device with 1 local master key which supports up to 60 calls per second.
    """
    PAY_SHIELD10_K_LMK1_CPS250 = "payShield10K_LMK1_CPS250"
    """
    The dedicated HSM is a payShield 10K, model PS10-D, 10Gb Ethernet Hardware Platform device with 1 local master key which supports up to 250 calls per second.
    """
    PAY_SHIELD10_K_LMK1_CPS2500 = "payShield10K_LMK1_CPS2500"
    """
    The dedicated HSM is a payShield 10K, model PS10-D, 10Gb Ethernet Hardware Platform device with 1 local master key which supports up to 2500 calls per second.
    """
    PAY_SHIELD10_K_LMK2_CPS60 = "payShield10K_LMK2_CPS60"
    """
    The dedicated HSM is a payShield 10K, model PS10-D, 10Gb Ethernet Hardware Platform device with 2 local master keys which supports up to 60 calls per second.
    """
    PAY_SHIELD10_K_LMK2_CPS250 = "payShield10K_LMK2_CPS250"
    """
    The dedicated HSM is a payShield 10K, model PS10-D, 10Gb Ethernet Hardware Platform device with 2 local master keys which supports up to 250 calls per second.
    """
    PAY_SHIELD10_K_LMK2_CPS2500 = "payShield10K_LMK2_CPS2500"
    """
    The dedicated HSM is a payShield 10K, model PS10-D, 10Gb Ethernet Hardware Platform device with 2 local master keys which supports up to 2500 calls per second.
    """
