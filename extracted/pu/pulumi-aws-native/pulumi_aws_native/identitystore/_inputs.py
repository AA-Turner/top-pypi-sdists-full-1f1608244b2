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
    'GroupMembershipMemberIdArgs',
    'GroupMembershipMemberIdArgsDict',
]

MYPY = False

if not MYPY:
    class GroupMembershipMemberIdArgsDict(TypedDict):
        """
        An object containing the identifier of a group member.
        """
        user_id: pulumi.Input[builtins.str]
        """
        The identifier for a user in the identity store.
        """
elif False:
    GroupMembershipMemberIdArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class GroupMembershipMemberIdArgs:
    def __init__(__self__, *,
                 user_id: pulumi.Input[builtins.str]):
        """
        An object containing the identifier of a group member.
        :param pulumi.Input[builtins.str] user_id: The identifier for a user in the identity store.
        """
        pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Input[builtins.str]:
        """
        The identifier for a user in the identity store.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "user_id", value)


