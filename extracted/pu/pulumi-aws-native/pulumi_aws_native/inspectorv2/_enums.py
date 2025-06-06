# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
import pulumi
from enum import Enum

__all__ = [
    'CisScanConfigurationCisSecurityLevel',
    'CisScanConfigurationDay',
    'FilterAction',
    'FilterMapComparison',
    'FilterStringComparison',
]


@pulumi.type_token("aws-native:inspectorv2:CisScanConfigurationCisSecurityLevel")
class CisScanConfigurationCisSecurityLevel(builtins.str, Enum):
    LEVEL1 = "LEVEL_1"
    LEVEL2 = "LEVEL_2"


@pulumi.type_token("aws-native:inspectorv2:CisScanConfigurationDay")
class CisScanConfigurationDay(builtins.str, Enum):
    MON = "MON"
    TUE = "TUE"
    WED = "WED"
    THU = "THU"
    FRI = "FRI"
    SAT = "SAT"
    SUN = "SUN"


@pulumi.type_token("aws-native:inspectorv2:FilterAction")
class FilterAction(builtins.str, Enum):
    NONE = "NONE"
    SUPPRESS = "SUPPRESS"


@pulumi.type_token("aws-native:inspectorv2:FilterMapComparison")
class FilterMapComparison(builtins.str, Enum):
    EQUALS = "EQUALS"


@pulumi.type_token("aws-native:inspectorv2:FilterStringComparison")
class FilterStringComparison(builtins.str, Enum):
    EQUALS = "EQUALS"
    PREFIX = "PREFIX"
    NOT_EQUALS = "NOT_EQUALS"
