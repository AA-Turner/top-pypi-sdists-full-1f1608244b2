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
from .. import outputs as _root_outputs
from ._enums import *

__all__ = [
    'GetDestinationResult',
    'AwaitableGetDestinationResult',
    'get_destination',
    'get_destination_output',
]

@pulumi.output_type
class GetDestinationResult:
    def __init__(__self__, arn=None, description=None, expression=None, expression_type=None, role_arn=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if expression and not isinstance(expression, str):
            raise TypeError("Expected argument 'expression' to be a str")
        pulumi.set(__self__, "expression", expression)
        if expression_type and not isinstance(expression_type, str):
            raise TypeError("Expected argument 'expression_type' to be a str")
        pulumi.set(__self__, "expression_type", expression_type)
        if role_arn and not isinstance(role_arn, str):
            raise TypeError("Expected argument 'role_arn' to be a str")
        pulumi.set(__self__, "role_arn", role_arn)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[builtins.str]:
        """
        Destination arn. Returned after successful create.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> Optional[builtins.str]:
        """
        Destination description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def expression(self) -> Optional[builtins.str]:
        """
        Destination expression
        """
        return pulumi.get(self, "expression")

    @property
    @pulumi.getter(name="expressionType")
    def expression_type(self) -> Optional['DestinationExpressionType']:
        """
        Must be RuleName
        """
        return pulumi.get(self, "expression_type")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[builtins.str]:
        """
        AWS role ARN that grants access
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        A list of key-value pairs that contain metadata for the destination.
        """
        return pulumi.get(self, "tags")


class AwaitableGetDestinationResult(GetDestinationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDestinationResult(
            arn=self.arn,
            description=self.description,
            expression=self.expression,
            expression_type=self.expression_type,
            role_arn=self.role_arn,
            tags=self.tags)


def get_destination(name: Optional[builtins.str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDestinationResult:
    """
    Destination's resource schema demonstrating some basic constructs and validation rules.


    :param builtins.str name: Unique name of destination
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:iotwireless:getDestination', __args__, opts=opts, typ=GetDestinationResult).value

    return AwaitableGetDestinationResult(
        arn=pulumi.get(__ret__, 'arn'),
        description=pulumi.get(__ret__, 'description'),
        expression=pulumi.get(__ret__, 'expression'),
        expression_type=pulumi.get(__ret__, 'expression_type'),
        role_arn=pulumi.get(__ret__, 'role_arn'),
        tags=pulumi.get(__ret__, 'tags'))
def get_destination_output(name: Optional[pulumi.Input[builtins.str]] = None,
                           opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetDestinationResult]:
    """
    Destination's resource schema demonstrating some basic constructs and validation rules.


    :param builtins.str name: Unique name of destination
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:iotwireless:getDestination', __args__, opts=opts, typ=GetDestinationResult)
    return __ret__.apply(lambda __response__: GetDestinationResult(
        arn=pulumi.get(__response__, 'arn'),
        description=pulumi.get(__response__, 'description'),
        expression=pulumi.get(__response__, 'expression'),
        expression_type=pulumi.get(__response__, 'expression_type'),
        role_arn=pulumi.get(__response__, 'role_arn'),
        tags=pulumi.get(__response__, 'tags')))
