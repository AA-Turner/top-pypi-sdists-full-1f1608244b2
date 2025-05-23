# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
import pulumi
from enum import Enum

__all__ = [
    'CopyMode',
    'CredentialType',
    'DayOfWeek',
    'EndpointType',
    'NfsVersion',
]


@pulumi.type_token("azure-native:storagemover:CopyMode")
class CopyMode(builtins.str, Enum):
    """
    Strategy to use for copy.
    """
    ADDITIVE = "Additive"
    MIRROR = "Mirror"


@pulumi.type_token("azure-native:storagemover:CredentialType")
class CredentialType(builtins.str, Enum):
    """
    The Credentials type.
    """
    AZURE_KEY_VAULT_SMB = "AzureKeyVaultSmb"


@pulumi.type_token("azure-native:storagemover:DayOfWeek")
class DayOfWeek(builtins.str, Enum):
    """
    The day of week.
    """
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


@pulumi.type_token("azure-native:storagemover:EndpointType")
class EndpointType(builtins.str, Enum):
    """
    The Endpoint resource type.
    """
    AZURE_STORAGE_BLOB_CONTAINER = "AzureStorageBlobContainer"
    NFS_MOUNT = "NfsMount"
    AZURE_STORAGE_SMB_FILE_SHARE = "AzureStorageSmbFileShare"
    SMB_MOUNT = "SmbMount"


@pulumi.type_token("azure-native:storagemover:NfsVersion")
class NfsVersion(builtins.str, Enum):
    """
    The NFS protocol version.
    """
    NF_SAUTO = "NFSauto"
    NF_SV3 = "NFSv3"
    NF_SV4 = "NFSv4"
