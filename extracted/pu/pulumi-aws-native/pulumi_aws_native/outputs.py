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
from . import _utilities
from ._enums import *

__all__ = [
    'CreateOnlyTag',
    'Tag',
]

@pulumi.output_type
class CreateOnlyTag(dict):
    """
    A set of tags to apply to the resource.
    """
    def __init__(__self__, *,
                 key: builtins.str,
                 value: builtins.str):
        """
        A set of tags to apply to the resource.
        :param builtins.str key: The key name of the tag
        :param builtins.str value: The value of the tag
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> builtins.str:
        """
        The key name of the tag
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> builtins.str:
        """
        The value of the tag
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class Tag(dict):
    """
    A set of tags to apply to the resource.
    """
    def __init__(__self__, *,
                 key: builtins.str,
                 value: builtins.str):
        """
        A set of tags to apply to the resource.
        :param builtins.str key: The key name of the tag
        :param builtins.str value: The value of the tag
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> builtins.str:
        """
        The key name of the tag
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> builtins.str:
        """
        The value of the tag
        """
        return pulumi.get(self, "value")


