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
    'GetAccountPolicyResult',
    'AwaitableGetAccountPolicyResult',
    'get_account_policy',
    'get_account_policy_output',
]

@pulumi.output_type
class GetAccountPolicyResult:
    def __init__(__self__, account_id=None, policy_document=None, scope=None, selection_criteria=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if policy_document and not isinstance(policy_document, str):
            raise TypeError("Expected argument 'policy_document' to be a str")
        pulumi.set(__self__, "policy_document", policy_document)
        if scope and not isinstance(scope, str):
            raise TypeError("Expected argument 'scope' to be a str")
        pulumi.set(__self__, "scope", scope)
        if selection_criteria and not isinstance(selection_criteria, str):
            raise TypeError("Expected argument 'selection_criteria' to be a str")
        pulumi.set(__self__, "selection_criteria", selection_criteria)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[builtins.str]:
        """
        User account id
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> Optional[builtins.str]:
        """
        The body of the policy document you want to use for this topic.

        You can only add one policy per PolicyType.

        The policy must be in JSON string format.

        Length Constraints: Maximum length of 30720
        """
        return pulumi.get(self, "policy_document")

    @property
    @pulumi.getter
    def scope(self) -> Optional['AccountPolicyScope']:
        """
        Scope for policy application
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter(name="selectionCriteria")
    def selection_criteria(self) -> Optional[builtins.str]:
        """
        Log group  selection criteria to apply policy only to a subset of log groups. SelectionCriteria string can be up to 25KB and cloudwatchlogs determines the length of selectionCriteria by using its UTF-8 bytes
        """
        return pulumi.get(self, "selection_criteria")


class AwaitableGetAccountPolicyResult(GetAccountPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccountPolicyResult(
            account_id=self.account_id,
            policy_document=self.policy_document,
            scope=self.scope,
            selection_criteria=self.selection_criteria)


def get_account_policy(account_id: Optional[builtins.str] = None,
                       policy_name: Optional[builtins.str] = None,
                       policy_type: Optional['AccountPolicyPolicyType'] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccountPolicyResult:
    """
    The AWS::Logs::AccountPolicy resource specifies a CloudWatch Logs AccountPolicy.


    :param builtins.str account_id: User account id
    :param builtins.str policy_name: The name of the account policy
    :param 'AccountPolicyPolicyType' policy_type: Type of the policy.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['policyName'] = policy_name
    __args__['policyType'] = policy_type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:logs:getAccountPolicy', __args__, opts=opts, typ=GetAccountPolicyResult).value

    return AwaitableGetAccountPolicyResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        policy_document=pulumi.get(__ret__, 'policy_document'),
        scope=pulumi.get(__ret__, 'scope'),
        selection_criteria=pulumi.get(__ret__, 'selection_criteria'))
def get_account_policy_output(account_id: Optional[pulumi.Input[builtins.str]] = None,
                              policy_name: Optional[pulumi.Input[builtins.str]] = None,
                              policy_type: Optional[pulumi.Input['AccountPolicyPolicyType']] = None,
                              opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetAccountPolicyResult]:
    """
    The AWS::Logs::AccountPolicy resource specifies a CloudWatch Logs AccountPolicy.


    :param builtins.str account_id: User account id
    :param builtins.str policy_name: The name of the account policy
    :param 'AccountPolicyPolicyType' policy_type: Type of the policy.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['policyName'] = policy_name
    __args__['policyType'] = policy_type
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:logs:getAccountPolicy', __args__, opts=opts, typ=GetAccountPolicyResult)
    return __ret__.apply(lambda __response__: GetAccountPolicyResult(
        account_id=pulumi.get(__response__, 'account_id'),
        policy_document=pulumi.get(__response__, 'policy_document'),
        scope=pulumi.get(__response__, 'scope'),
        selection_criteria=pulumi.get(__response__, 'selection_criteria')))
