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
from .. import outputs as _root_outputs
from ._enums import *

__all__ = [
    'GetContainerGroupDefinitionResult',
    'AwaitableGetContainerGroupDefinitionResult',
    'get_container_group_definition',
    'get_container_group_definition_output',
]

@pulumi.output_type
class GetContainerGroupDefinitionResult:
    def __init__(__self__, container_group_definition_arn=None, creation_time=None, game_server_container_definition=None, operating_system=None, status=None, status_reason=None, support_container_definitions=None, tags=None, total_memory_limit_mebibytes=None, total_vcpu_limit=None, version_description=None, version_number=None):
        if container_group_definition_arn and not isinstance(container_group_definition_arn, str):
            raise TypeError("Expected argument 'container_group_definition_arn' to be a str")
        pulumi.set(__self__, "container_group_definition_arn", container_group_definition_arn)
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if game_server_container_definition and not isinstance(game_server_container_definition, dict):
            raise TypeError("Expected argument 'game_server_container_definition' to be a dict")
        pulumi.set(__self__, "game_server_container_definition", game_server_container_definition)
        if operating_system and not isinstance(operating_system, str):
            raise TypeError("Expected argument 'operating_system' to be a str")
        pulumi.set(__self__, "operating_system", operating_system)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if status_reason and not isinstance(status_reason, str):
            raise TypeError("Expected argument 'status_reason' to be a str")
        pulumi.set(__self__, "status_reason", status_reason)
        if support_container_definitions and not isinstance(support_container_definitions, list):
            raise TypeError("Expected argument 'support_container_definitions' to be a list")
        pulumi.set(__self__, "support_container_definitions", support_container_definitions)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if total_memory_limit_mebibytes and not isinstance(total_memory_limit_mebibytes, int):
            raise TypeError("Expected argument 'total_memory_limit_mebibytes' to be a int")
        pulumi.set(__self__, "total_memory_limit_mebibytes", total_memory_limit_mebibytes)
        if total_vcpu_limit and not isinstance(total_vcpu_limit, float):
            raise TypeError("Expected argument 'total_vcpu_limit' to be a float")
        pulumi.set(__self__, "total_vcpu_limit", total_vcpu_limit)
        if version_description and not isinstance(version_description, str):
            raise TypeError("Expected argument 'version_description' to be a str")
        pulumi.set(__self__, "version_description", version_description)
        if version_number and not isinstance(version_number, int):
            raise TypeError("Expected argument 'version_number' to be a int")
        pulumi.set(__self__, "version_number", version_number)

    @property
    @pulumi.getter(name="containerGroupDefinitionArn")
    def container_group_definition_arn(self) -> Optional[builtins.str]:
        """
        The Amazon Resource Name (ARN) that is assigned to a Amazon GameLift container group resource and uniquely identifies it across all AWS Regions.
        """
        return pulumi.get(self, "container_group_definition_arn")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[builtins.str]:
        """
        A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="gameServerContainerDefinition")
    def game_server_container_definition(self) -> Optional['outputs.ContainerGroupDefinitionGameServerContainerDefinition']:
        """
        The definition for the game server container in this group. This property is used only when the container group type is `GAME_SERVER` . This container definition specifies a container image with the game server build.
        """
        return pulumi.get(self, "game_server_container_definition")

    @property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> Optional['ContainerGroupDefinitionOperatingSystem']:
        """
        The operating system of the container group
        """
        return pulumi.get(self, "operating_system")

    @property
    @pulumi.getter
    def status(self) -> Optional['ContainerGroupDefinitionStatus']:
        """
        A string indicating ContainerGroupDefinition status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> Optional[builtins.str]:
        """
        A string indicating the reason for ContainerGroupDefinition status.
        """
        return pulumi.get(self, "status_reason")

    @property
    @pulumi.getter(name="supportContainerDefinitions")
    def support_container_definitions(self) -> Optional[Sequence['outputs.ContainerGroupDefinitionSupportContainerDefinition']]:
        """
        A collection of support container definitions that define the containers in this group.
        """
        return pulumi.get(self, "support_container_definitions")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="totalMemoryLimitMebibytes")
    def total_memory_limit_mebibytes(self) -> Optional[builtins.int]:
        """
        The total memory limit of container groups following this definition in MiB
        """
        return pulumi.get(self, "total_memory_limit_mebibytes")

    @property
    @pulumi.getter(name="totalVcpuLimit")
    def total_vcpu_limit(self) -> Optional[builtins.float]:
        """
        The total amount of virtual CPUs on the container group definition
        """
        return pulumi.get(self, "total_vcpu_limit")

    @property
    @pulumi.getter(name="versionDescription")
    def version_description(self) -> Optional[builtins.str]:
        """
        The description of this version
        """
        return pulumi.get(self, "version_description")

    @property
    @pulumi.getter(name="versionNumber")
    def version_number(self) -> Optional[builtins.int]:
        """
        The version of this ContainerGroupDefinition
        """
        return pulumi.get(self, "version_number")


class AwaitableGetContainerGroupDefinitionResult(GetContainerGroupDefinitionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetContainerGroupDefinitionResult(
            container_group_definition_arn=self.container_group_definition_arn,
            creation_time=self.creation_time,
            game_server_container_definition=self.game_server_container_definition,
            operating_system=self.operating_system,
            status=self.status,
            status_reason=self.status_reason,
            support_container_definitions=self.support_container_definitions,
            tags=self.tags,
            total_memory_limit_mebibytes=self.total_memory_limit_mebibytes,
            total_vcpu_limit=self.total_vcpu_limit,
            version_description=self.version_description,
            version_number=self.version_number)


def get_container_group_definition(name: Optional[builtins.str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetContainerGroupDefinitionResult:
    """
    The AWS::GameLift::ContainerGroupDefinition resource creates an Amazon GameLift container group definition.


    :param builtins.str name: A descriptive label for the container group definition.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:gamelift:getContainerGroupDefinition', __args__, opts=opts, typ=GetContainerGroupDefinitionResult).value

    return AwaitableGetContainerGroupDefinitionResult(
        container_group_definition_arn=pulumi.get(__ret__, 'container_group_definition_arn'),
        creation_time=pulumi.get(__ret__, 'creation_time'),
        game_server_container_definition=pulumi.get(__ret__, 'game_server_container_definition'),
        operating_system=pulumi.get(__ret__, 'operating_system'),
        status=pulumi.get(__ret__, 'status'),
        status_reason=pulumi.get(__ret__, 'status_reason'),
        support_container_definitions=pulumi.get(__ret__, 'support_container_definitions'),
        tags=pulumi.get(__ret__, 'tags'),
        total_memory_limit_mebibytes=pulumi.get(__ret__, 'total_memory_limit_mebibytes'),
        total_vcpu_limit=pulumi.get(__ret__, 'total_vcpu_limit'),
        version_description=pulumi.get(__ret__, 'version_description'),
        version_number=pulumi.get(__ret__, 'version_number'))
def get_container_group_definition_output(name: Optional[pulumi.Input[builtins.str]] = None,
                                          opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetContainerGroupDefinitionResult]:
    """
    The AWS::GameLift::ContainerGroupDefinition resource creates an Amazon GameLift container group definition.


    :param builtins.str name: A descriptive label for the container group definition.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:gamelift:getContainerGroupDefinition', __args__, opts=opts, typ=GetContainerGroupDefinitionResult)
    return __ret__.apply(lambda __response__: GetContainerGroupDefinitionResult(
        container_group_definition_arn=pulumi.get(__response__, 'container_group_definition_arn'),
        creation_time=pulumi.get(__response__, 'creation_time'),
        game_server_container_definition=pulumi.get(__response__, 'game_server_container_definition'),
        operating_system=pulumi.get(__response__, 'operating_system'),
        status=pulumi.get(__response__, 'status'),
        status_reason=pulumi.get(__response__, 'status_reason'),
        support_container_definitions=pulumi.get(__response__, 'support_container_definitions'),
        tags=pulumi.get(__response__, 'tags'),
        total_memory_limit_mebibytes=pulumi.get(__response__, 'total_memory_limit_mebibytes'),
        total_vcpu_limit=pulumi.get(__response__, 'total_vcpu_limit'),
        version_description=pulumi.get(__response__, 'version_description'),
        version_number=pulumi.get(__response__, 'version_number')))
