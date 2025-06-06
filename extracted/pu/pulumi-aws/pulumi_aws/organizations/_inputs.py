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

__all__ = [
    'OrganizationAccountArgs',
    'OrganizationAccountArgsDict',
    'OrganizationNonMasterAccountArgs',
    'OrganizationNonMasterAccountArgsDict',
    'OrganizationRootArgs',
    'OrganizationRootArgsDict',
    'OrganizationRootPolicyTypeArgs',
    'OrganizationRootPolicyTypeArgsDict',
    'OrganizationalUnitAccountArgs',
    'OrganizationalUnitAccountArgsDict',
]

MYPY = False

if not MYPY:
    class OrganizationAccountArgsDict(TypedDict):
        arn: NotRequired[pulumi.Input[builtins.str]]
        """
        ARN of the root
        """
        email: NotRequired[pulumi.Input[builtins.str]]
        """
        Email of the account
        """
        id: NotRequired[pulumi.Input[builtins.str]]
        """
        Identifier of the root
        """
        name: NotRequired[pulumi.Input[builtins.str]]
        """
        The name of the policy type
        """
        status: NotRequired[pulumi.Input[builtins.str]]
        """
        The status of the policy type as it relates to the associated root
        """
elif False:
    OrganizationAccountArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class OrganizationAccountArgs:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[builtins.str]] = None,
                 email: Optional[pulumi.Input[builtins.str]] = None,
                 id: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 status: Optional[pulumi.Input[builtins.str]] = None):
        """
        :param pulumi.Input[builtins.str] arn: ARN of the root
        :param pulumi.Input[builtins.str] email: Email of the account
        :param pulumi.Input[builtins.str] id: Identifier of the root
        :param pulumi.Input[builtins.str] name: The name of the policy type
        :param pulumi.Input[builtins.str] status: The status of the policy type as it relates to the associated root
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if email is not None:
            pulumi.set(__self__, "email", email)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        ARN of the root
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Email of the account
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Identifier of the root
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the policy type
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The status of the policy type as it relates to the associated root
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "status", value)


if not MYPY:
    class OrganizationNonMasterAccountArgsDict(TypedDict):
        arn: NotRequired[pulumi.Input[builtins.str]]
        """
        ARN of the root
        """
        email: NotRequired[pulumi.Input[builtins.str]]
        """
        Email of the account
        """
        id: NotRequired[pulumi.Input[builtins.str]]
        """
        Identifier of the root
        """
        name: NotRequired[pulumi.Input[builtins.str]]
        """
        The name of the policy type
        """
        status: NotRequired[pulumi.Input[builtins.str]]
        """
        The status of the policy type as it relates to the associated root
        """
elif False:
    OrganizationNonMasterAccountArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class OrganizationNonMasterAccountArgs:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[builtins.str]] = None,
                 email: Optional[pulumi.Input[builtins.str]] = None,
                 id: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 status: Optional[pulumi.Input[builtins.str]] = None):
        """
        :param pulumi.Input[builtins.str] arn: ARN of the root
        :param pulumi.Input[builtins.str] email: Email of the account
        :param pulumi.Input[builtins.str] id: Identifier of the root
        :param pulumi.Input[builtins.str] name: The name of the policy type
        :param pulumi.Input[builtins.str] status: The status of the policy type as it relates to the associated root
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if email is not None:
            pulumi.set(__self__, "email", email)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        ARN of the root
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Email of the account
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Identifier of the root
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the policy type
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The status of the policy type as it relates to the associated root
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "status", value)


if not MYPY:
    class OrganizationRootArgsDict(TypedDict):
        arn: NotRequired[pulumi.Input[builtins.str]]
        """
        ARN of the root
        """
        id: NotRequired[pulumi.Input[builtins.str]]
        """
        Identifier of the root
        """
        name: NotRequired[pulumi.Input[builtins.str]]
        """
        The name of the policy type
        """
        policy_types: NotRequired[pulumi.Input[Sequence[pulumi.Input['OrganizationRootPolicyTypeArgsDict']]]]
        """
        List of policy types enabled for this root. All elements have these attributes:
        """
elif False:
    OrganizationRootArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class OrganizationRootArgs:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[builtins.str]] = None,
                 id: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 policy_types: Optional[pulumi.Input[Sequence[pulumi.Input['OrganizationRootPolicyTypeArgs']]]] = None):
        """
        :param pulumi.Input[builtins.str] arn: ARN of the root
        :param pulumi.Input[builtins.str] id: Identifier of the root
        :param pulumi.Input[builtins.str] name: The name of the policy type
        :param pulumi.Input[Sequence[pulumi.Input['OrganizationRootPolicyTypeArgs']]] policy_types: List of policy types enabled for this root. All elements have these attributes:
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if policy_types is not None:
            pulumi.set(__self__, "policy_types", policy_types)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        ARN of the root
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Identifier of the root
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the policy type
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="policyTypes")
    def policy_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['OrganizationRootPolicyTypeArgs']]]]:
        """
        List of policy types enabled for this root. All elements have these attributes:
        """
        return pulumi.get(self, "policy_types")

    @policy_types.setter
    def policy_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['OrganizationRootPolicyTypeArgs']]]]):
        pulumi.set(self, "policy_types", value)


if not MYPY:
    class OrganizationRootPolicyTypeArgsDict(TypedDict):
        status: NotRequired[pulumi.Input[builtins.str]]
        """
        The status of the policy type as it relates to the associated root
        """
        type: NotRequired[pulumi.Input[builtins.str]]
elif False:
    OrganizationRootPolicyTypeArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class OrganizationRootPolicyTypeArgs:
    def __init__(__self__, *,
                 status: Optional[pulumi.Input[builtins.str]] = None,
                 type: Optional[pulumi.Input[builtins.str]] = None):
        """
        :param pulumi.Input[builtins.str] status: The status of the policy type as it relates to the associated root
        """
        if status is not None:
            pulumi.set(__self__, "status", status)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The status of the policy type as it relates to the associated root
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "type", value)


if not MYPY:
    class OrganizationalUnitAccountArgsDict(TypedDict):
        arn: NotRequired[pulumi.Input[builtins.str]]
        """
        ARN of the organizational unit
        """
        email: NotRequired[pulumi.Input[builtins.str]]
        """
        Email of the account
        """
        id: NotRequired[pulumi.Input[builtins.str]]
        """
        Identifier of the organization unit
        """
        name: NotRequired[pulumi.Input[builtins.str]]
        """
        The name for the organizational unit
        """
elif False:
    OrganizationalUnitAccountArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class OrganizationalUnitAccountArgs:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[builtins.str]] = None,
                 email: Optional[pulumi.Input[builtins.str]] = None,
                 id: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None):
        """
        :param pulumi.Input[builtins.str] arn: ARN of the organizational unit
        :param pulumi.Input[builtins.str] email: Email of the account
        :param pulumi.Input[builtins.str] id: Identifier of the organization unit
        :param pulumi.Input[builtins.str] name: The name for the organizational unit
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if email is not None:
            pulumi.set(__self__, "email", email)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        ARN of the organizational unit
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Email of the account
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Identifier of the organization unit
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name for the organizational unit
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)


