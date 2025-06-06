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

__all__ = [
    'GetPolicyAssignmentArtifactResult',
    'AwaitableGetPolicyAssignmentArtifactResult',
    'get_policy_assignment_artifact',
    'get_policy_assignment_artifact_output',
]

@pulumi.output_type
class GetPolicyAssignmentArtifactResult:
    """
    Blueprint artifact that applies a Policy assignment.
    """
    def __init__(__self__, azure_api_version=None, depends_on=None, description=None, display_name=None, id=None, kind=None, name=None, parameters=None, policy_definition_id=None, resource_group=None, type=None):
        if azure_api_version and not isinstance(azure_api_version, str):
            raise TypeError("Expected argument 'azure_api_version' to be a str")
        pulumi.set(__self__, "azure_api_version", azure_api_version)
        if depends_on and not isinstance(depends_on, list):
            raise TypeError("Expected argument 'depends_on' to be a list")
        pulumi.set(__self__, "depends_on", depends_on)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if parameters and not isinstance(parameters, dict):
            raise TypeError("Expected argument 'parameters' to be a dict")
        pulumi.set(__self__, "parameters", parameters)
        if policy_definition_id and not isinstance(policy_definition_id, str):
            raise TypeError("Expected argument 'policy_definition_id' to be a str")
        pulumi.set(__self__, "policy_definition_id", policy_definition_id)
        if resource_group and not isinstance(resource_group, str):
            raise TypeError("Expected argument 'resource_group' to be a str")
        pulumi.set(__self__, "resource_group", resource_group)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> builtins.str:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter(name="dependsOn")
    def depends_on(self) -> Optional[Sequence[builtins.str]]:
        """
        Artifacts which need to be deployed before the specified artifact.
        """
        return pulumi.get(self, "depends_on")

    @property
    @pulumi.getter
    def description(self) -> Optional[builtins.str]:
        """
        Multi-line explain this resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[builtins.str]:
        """
        One-liner string explain this resource.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        """
        String Id used to locate any resource on Azure.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> builtins.str:
        """
        Specifies the kind of blueprint artifact.
        Expected value is 'policyAssignment'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> builtins.str:
        """
        Name of this resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> Mapping[str, 'outputs.ParameterValueResponse']:
        """
        Parameter values for the policy definition.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="policyDefinitionId")
    def policy_definition_id(self) -> builtins.str:
        """
        Azure resource ID of the policy definition.
        """
        return pulumi.get(self, "policy_definition_id")

    @property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[builtins.str]:
        """
        Name of the resource group placeholder to which the policy will be assigned.
        """
        return pulumi.get(self, "resource_group")

    @property
    @pulumi.getter
    def type(self) -> builtins.str:
        """
        Type of this resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetPolicyAssignmentArtifactResult(GetPolicyAssignmentArtifactResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPolicyAssignmentArtifactResult(
            azure_api_version=self.azure_api_version,
            depends_on=self.depends_on,
            description=self.description,
            display_name=self.display_name,
            id=self.id,
            kind=self.kind,
            name=self.name,
            parameters=self.parameters,
            policy_definition_id=self.policy_definition_id,
            resource_group=self.resource_group,
            type=self.type)


def get_policy_assignment_artifact(artifact_name: Optional[builtins.str] = None,
                                   blueprint_name: Optional[builtins.str] = None,
                                   resource_scope: Optional[builtins.str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPolicyAssignmentArtifactResult:
    """
    Get a blueprint artifact.

    Uses Azure REST API version 2018-11-01-preview.


    :param builtins.str artifact_name: Name of the blueprint artifact.
    :param builtins.str blueprint_name: Name of the blueprint definition.
    :param builtins.str resource_scope: The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}').
    """
    __args__ = dict()
    __args__['artifactName'] = artifact_name
    __args__['blueprintName'] = blueprint_name
    __args__['resourceScope'] = resource_scope
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:blueprint:getPolicyAssignmentArtifact', __args__, opts=opts, typ=GetPolicyAssignmentArtifactResult).value

    return AwaitableGetPolicyAssignmentArtifactResult(
        azure_api_version=pulumi.get(__ret__, 'azure_api_version'),
        depends_on=pulumi.get(__ret__, 'depends_on'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        name=pulumi.get(__ret__, 'name'),
        parameters=pulumi.get(__ret__, 'parameters'),
        policy_definition_id=pulumi.get(__ret__, 'policy_definition_id'),
        resource_group=pulumi.get(__ret__, 'resource_group'),
        type=pulumi.get(__ret__, 'type'))
def get_policy_assignment_artifact_output(artifact_name: Optional[pulumi.Input[builtins.str]] = None,
                                          blueprint_name: Optional[pulumi.Input[builtins.str]] = None,
                                          resource_scope: Optional[pulumi.Input[builtins.str]] = None,
                                          opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetPolicyAssignmentArtifactResult]:
    """
    Get a blueprint artifact.

    Uses Azure REST API version 2018-11-01-preview.


    :param builtins.str artifact_name: Name of the blueprint artifact.
    :param builtins.str blueprint_name: Name of the blueprint definition.
    :param builtins.str resource_scope: The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}').
    """
    __args__ = dict()
    __args__['artifactName'] = artifact_name
    __args__['blueprintName'] = blueprint_name
    __args__['resourceScope'] = resource_scope
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('azure-native:blueprint:getPolicyAssignmentArtifact', __args__, opts=opts, typ=GetPolicyAssignmentArtifactResult)
    return __ret__.apply(lambda __response__: GetPolicyAssignmentArtifactResult(
        azure_api_version=pulumi.get(__response__, 'azure_api_version'),
        depends_on=pulumi.get(__response__, 'depends_on'),
        description=pulumi.get(__response__, 'description'),
        display_name=pulumi.get(__response__, 'display_name'),
        id=pulumi.get(__response__, 'id'),
        kind=pulumi.get(__response__, 'kind'),
        name=pulumi.get(__response__, 'name'),
        parameters=pulumi.get(__response__, 'parameters'),
        policy_definition_id=pulumi.get(__response__, 'policy_definition_id'),
        resource_group=pulumi.get(__response__, 'resource_group'),
        type=pulumi.get(__response__, 'type')))
