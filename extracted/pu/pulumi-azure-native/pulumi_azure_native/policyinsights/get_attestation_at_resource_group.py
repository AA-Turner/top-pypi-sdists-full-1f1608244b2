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
    'GetAttestationAtResourceGroupResult',
    'AwaitableGetAttestationAtResourceGroupResult',
    'get_attestation_at_resource_group',
    'get_attestation_at_resource_group_output',
]

@pulumi.output_type
class GetAttestationAtResourceGroupResult:
    """
    An attestation resource.
    """
    def __init__(__self__, assessment_date=None, azure_api_version=None, comments=None, compliance_state=None, evidence=None, expires_on=None, id=None, last_compliance_state_change_at=None, metadata=None, name=None, owner=None, policy_assignment_id=None, policy_definition_reference_id=None, provisioning_state=None, system_data=None, type=None):
        if assessment_date and not isinstance(assessment_date, str):
            raise TypeError("Expected argument 'assessment_date' to be a str")
        pulumi.set(__self__, "assessment_date", assessment_date)
        if azure_api_version and not isinstance(azure_api_version, str):
            raise TypeError("Expected argument 'azure_api_version' to be a str")
        pulumi.set(__self__, "azure_api_version", azure_api_version)
        if comments and not isinstance(comments, str):
            raise TypeError("Expected argument 'comments' to be a str")
        pulumi.set(__self__, "comments", comments)
        if compliance_state and not isinstance(compliance_state, str):
            raise TypeError("Expected argument 'compliance_state' to be a str")
        pulumi.set(__self__, "compliance_state", compliance_state)
        if evidence and not isinstance(evidence, list):
            raise TypeError("Expected argument 'evidence' to be a list")
        pulumi.set(__self__, "evidence", evidence)
        if expires_on and not isinstance(expires_on, str):
            raise TypeError("Expected argument 'expires_on' to be a str")
        pulumi.set(__self__, "expires_on", expires_on)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_compliance_state_change_at and not isinstance(last_compliance_state_change_at, str):
            raise TypeError("Expected argument 'last_compliance_state_change_at' to be a str")
        pulumi.set(__self__, "last_compliance_state_change_at", last_compliance_state_change_at)
        if metadata and not isinstance(metadata, dict):
            raise TypeError("Expected argument 'metadata' to be a dict")
        pulumi.set(__self__, "metadata", metadata)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if owner and not isinstance(owner, str):
            raise TypeError("Expected argument 'owner' to be a str")
        pulumi.set(__self__, "owner", owner)
        if policy_assignment_id and not isinstance(policy_assignment_id, str):
            raise TypeError("Expected argument 'policy_assignment_id' to be a str")
        pulumi.set(__self__, "policy_assignment_id", policy_assignment_id)
        if policy_definition_reference_id and not isinstance(policy_definition_reference_id, str):
            raise TypeError("Expected argument 'policy_definition_reference_id' to be a str")
        pulumi.set(__self__, "policy_definition_reference_id", policy_definition_reference_id)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="assessmentDate")
    def assessment_date(self) -> Optional[builtins.str]:
        """
        The time the evidence was assessed
        """
        return pulumi.get(self, "assessment_date")

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> builtins.str:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter
    def comments(self) -> Optional[builtins.str]:
        """
        Comments describing why this attestation was created.
        """
        return pulumi.get(self, "comments")

    @property
    @pulumi.getter(name="complianceState")
    def compliance_state(self) -> Optional[builtins.str]:
        """
        The compliance state that should be set on the resource.
        """
        return pulumi.get(self, "compliance_state")

    @property
    @pulumi.getter
    def evidence(self) -> Optional[Sequence['outputs.AttestationEvidenceResponse']]:
        """
        The evidence supporting the compliance state set in this attestation.
        """
        return pulumi.get(self, "evidence")

    @property
    @pulumi.getter(name="expiresOn")
    def expires_on(self) -> Optional[builtins.str]:
        """
        The time the compliance state should expire.
        """
        return pulumi.get(self, "expires_on")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastComplianceStateChangeAt")
    def last_compliance_state_change_at(self) -> builtins.str:
        """
        The time the compliance state was last changed in this attestation.
        """
        return pulumi.get(self, "last_compliance_state_change_at")

    @property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        """
        Additional metadata for this attestation
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> builtins.str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def owner(self) -> Optional[builtins.str]:
        """
        The person responsible for setting the state of the resource. This value is typically an Azure Active Directory object ID.
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter(name="policyAssignmentId")
    def policy_assignment_id(self) -> builtins.str:
        """
        The resource ID of the policy assignment that the attestation is setting the state for.
        """
        return pulumi.get(self, "policy_assignment_id")

    @property
    @pulumi.getter(name="policyDefinitionReferenceId")
    def policy_definition_reference_id(self) -> Optional[builtins.str]:
        """
        The policy definition reference ID from a policy set definition that the attestation is setting the state for. If the policy assignment assigns a policy set definition the attestation can choose a definition within the set definition with this property or omit this and set the state for the entire set definition.
        """
        return pulumi.get(self, "policy_definition_reference_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> builtins.str:
        """
        The status of the attestation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> builtins.str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetAttestationAtResourceGroupResult(GetAttestationAtResourceGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAttestationAtResourceGroupResult(
            assessment_date=self.assessment_date,
            azure_api_version=self.azure_api_version,
            comments=self.comments,
            compliance_state=self.compliance_state,
            evidence=self.evidence,
            expires_on=self.expires_on,
            id=self.id,
            last_compliance_state_change_at=self.last_compliance_state_change_at,
            metadata=self.metadata,
            name=self.name,
            owner=self.owner,
            policy_assignment_id=self.policy_assignment_id,
            policy_definition_reference_id=self.policy_definition_reference_id,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_attestation_at_resource_group(attestation_name: Optional[builtins.str] = None,
                                      resource_group_name: Optional[builtins.str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAttestationAtResourceGroupResult:
    """
    Gets an existing attestation at resource group scope.

    Uses Azure REST API version 2024-10-01.

    Other available API versions: 2022-09-01. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native policyinsights [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param builtins.str attestation_name: The name of the attestation.
    :param builtins.str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['attestationName'] = attestation_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:policyinsights:getAttestationAtResourceGroup', __args__, opts=opts, typ=GetAttestationAtResourceGroupResult).value

    return AwaitableGetAttestationAtResourceGroupResult(
        assessment_date=pulumi.get(__ret__, 'assessment_date'),
        azure_api_version=pulumi.get(__ret__, 'azure_api_version'),
        comments=pulumi.get(__ret__, 'comments'),
        compliance_state=pulumi.get(__ret__, 'compliance_state'),
        evidence=pulumi.get(__ret__, 'evidence'),
        expires_on=pulumi.get(__ret__, 'expires_on'),
        id=pulumi.get(__ret__, 'id'),
        last_compliance_state_change_at=pulumi.get(__ret__, 'last_compliance_state_change_at'),
        metadata=pulumi.get(__ret__, 'metadata'),
        name=pulumi.get(__ret__, 'name'),
        owner=pulumi.get(__ret__, 'owner'),
        policy_assignment_id=pulumi.get(__ret__, 'policy_assignment_id'),
        policy_definition_reference_id=pulumi.get(__ret__, 'policy_definition_reference_id'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))
def get_attestation_at_resource_group_output(attestation_name: Optional[pulumi.Input[builtins.str]] = None,
                                             resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                                             opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetAttestationAtResourceGroupResult]:
    """
    Gets an existing attestation at resource group scope.

    Uses Azure REST API version 2024-10-01.

    Other available API versions: 2022-09-01. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native policyinsights [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param builtins.str attestation_name: The name of the attestation.
    :param builtins.str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['attestationName'] = attestation_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('azure-native:policyinsights:getAttestationAtResourceGroup', __args__, opts=opts, typ=GetAttestationAtResourceGroupResult)
    return __ret__.apply(lambda __response__: GetAttestationAtResourceGroupResult(
        assessment_date=pulumi.get(__response__, 'assessment_date'),
        azure_api_version=pulumi.get(__response__, 'azure_api_version'),
        comments=pulumi.get(__response__, 'comments'),
        compliance_state=pulumi.get(__response__, 'compliance_state'),
        evidence=pulumi.get(__response__, 'evidence'),
        expires_on=pulumi.get(__response__, 'expires_on'),
        id=pulumi.get(__response__, 'id'),
        last_compliance_state_change_at=pulumi.get(__response__, 'last_compliance_state_change_at'),
        metadata=pulumi.get(__response__, 'metadata'),
        name=pulumi.get(__response__, 'name'),
        owner=pulumi.get(__response__, 'owner'),
        policy_assignment_id=pulumi.get(__response__, 'policy_assignment_id'),
        policy_definition_reference_id=pulumi.get(__response__, 'policy_definition_reference_id'),
        provisioning_state=pulumi.get(__response__, 'provisioning_state'),
        system_data=pulumi.get(__response__, 'system_data'),
        type=pulumi.get(__response__, 'type')))
