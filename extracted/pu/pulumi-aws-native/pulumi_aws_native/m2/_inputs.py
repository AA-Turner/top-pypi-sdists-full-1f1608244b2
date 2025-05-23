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
    'ApplicationDefinition0PropertiesArgs',
    'ApplicationDefinition0PropertiesArgsDict',
    'ApplicationDefinition1PropertiesArgs',
    'ApplicationDefinition1PropertiesArgsDict',
    'EnvironmentHighAvailabilityConfigArgs',
    'EnvironmentHighAvailabilityConfigArgsDict',
    'EnvironmentStorageConfigurationArgs',
    'EnvironmentStorageConfigurationArgsDict',
]

MYPY = False

if not MYPY:
    class ApplicationDefinition0PropertiesArgsDict(TypedDict):
        s3_location: pulumi.Input[builtins.str]
elif False:
    ApplicationDefinition0PropertiesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ApplicationDefinition0PropertiesArgs:
    def __init__(__self__, *,
                 s3_location: pulumi.Input[builtins.str]):
        pulumi.set(__self__, "s3_location", s3_location)

    @property
    @pulumi.getter(name="s3Location")
    def s3_location(self) -> pulumi.Input[builtins.str]:
        return pulumi.get(self, "s3_location")

    @s3_location.setter
    def s3_location(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "s3_location", value)


if not MYPY:
    class ApplicationDefinition1PropertiesArgsDict(TypedDict):
        content: pulumi.Input[builtins.str]
elif False:
    ApplicationDefinition1PropertiesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ApplicationDefinition1PropertiesArgs:
    def __init__(__self__, *,
                 content: pulumi.Input[builtins.str]):
        pulumi.set(__self__, "content", content)

    @property
    @pulumi.getter
    def content(self) -> pulumi.Input[builtins.str]:
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "content", value)


if not MYPY:
    class EnvironmentHighAvailabilityConfigArgsDict(TypedDict):
        """
        Defines the details of a high availability configuration.
        """
        desired_capacity: pulumi.Input[builtins.int]
        """
        The number of instances in a high availability configuration. The minimum possible value is 1 and the maximum is 100.
        """
elif False:
    EnvironmentHighAvailabilityConfigArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class EnvironmentHighAvailabilityConfigArgs:
    def __init__(__self__, *,
                 desired_capacity: pulumi.Input[builtins.int]):
        """
        Defines the details of a high availability configuration.
        :param pulumi.Input[builtins.int] desired_capacity: The number of instances in a high availability configuration. The minimum possible value is 1 and the maximum is 100.
        """
        pulumi.set(__self__, "desired_capacity", desired_capacity)

    @property
    @pulumi.getter(name="desiredCapacity")
    def desired_capacity(self) -> pulumi.Input[builtins.int]:
        """
        The number of instances in a high availability configuration. The minimum possible value is 1 and the maximum is 100.
        """
        return pulumi.get(self, "desired_capacity")

    @desired_capacity.setter
    def desired_capacity(self, value: pulumi.Input[builtins.int]):
        pulumi.set(self, "desired_capacity", value)


if not MYPY:
    class EnvironmentStorageConfigurationArgsDict(TypedDict):
        """
        Defines the storage configuration for an environment.
        """
        pass
elif False:
    EnvironmentStorageConfigurationArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class EnvironmentStorageConfigurationArgs:
    def __init__(__self__):
        """
        Defines the storage configuration for an environment.
        """
        pass


