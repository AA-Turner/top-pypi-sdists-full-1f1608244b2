# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
import pulumi
from enum import Enum

__all__ = [
    'ApplicationComponentInfoComponentType',
    'ApplicationCredentialCredentialType',
    'ApplicationType',
]


@pulumi.type_token("aws-native:systemsmanagersap:ApplicationComponentInfoComponentType")
class ApplicationComponentInfoComponentType(builtins.str, Enum):
    """
    This string is the type of the component.

    Accepted value is `WD` .
    """
    HANA = "HANA"
    HANA_NODE = "HANA_NODE"
    ABAP = "ABAP"
    ASCS = "ASCS"
    DIALOG = "DIALOG"
    WEBDISP = "WEBDISP"
    WD = "WD"
    ERS = "ERS"


@pulumi.type_token("aws-native:systemsmanagersap:ApplicationCredentialCredentialType")
class ApplicationCredentialCredentialType(builtins.str, Enum):
    """
    The type of the application credentials.
    """
    ADMIN = "ADMIN"


@pulumi.type_token("aws-native:systemsmanagersap:ApplicationType")
class ApplicationType(builtins.str, Enum):
    """
    The type of the application.
    """
    HANA = "HANA"
    SAP_ABAP = "SAP_ABAP"
