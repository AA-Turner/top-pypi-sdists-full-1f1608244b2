# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
import pulumi
from enum import Enum

__all__ = [
    'ResourceIdentityType',
    'SkuName',
]


@pulumi.type_token("azure-native:healthbot:ResourceIdentityType")
class ResourceIdentityType(builtins.str, Enum):
    """
    The identity type. The type 'SystemAssigned, UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the Azure Health Bot
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    NONE = "None"


@pulumi.type_token("azure-native:healthbot:SkuName")
class SkuName(builtins.str, Enum):
    """
    The name of the Azure Health Bot SKU
    """
    F0 = "F0"
    S1 = "S1"
    C0 = "C0"
    PES = "PES"
    C1 = "C1"
