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
    'GetPrimaryTaskSetResult',
    'AwaitableGetPrimaryTaskSetResult',
    'get_primary_task_set',
    'get_primary_task_set_output',
]

@pulumi.output_type
class GetPrimaryTaskSetResult:
    def __init__(__self__, task_set_id=None):
        if task_set_id and not isinstance(task_set_id, str):
            raise TypeError("Expected argument 'task_set_id' to be a str")
        pulumi.set(__self__, "task_set_id", task_set_id)

    @property
    @pulumi.getter(name="taskSetId")
    def task_set_id(self) -> Optional[builtins.str]:
        """
        The ID or full Amazon Resource Name (ARN) of the task set.
        """
        return pulumi.get(self, "task_set_id")


class AwaitableGetPrimaryTaskSetResult(GetPrimaryTaskSetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrimaryTaskSetResult(
            task_set_id=self.task_set_id)


def get_primary_task_set(cluster: Optional[builtins.str] = None,
                         service: Optional[builtins.str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPrimaryTaskSetResult:
    """
    A pseudo-resource that manages which of your ECS task sets is primary.


    :param builtins.str cluster: The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to create the task set in.
    :param builtins.str service: The short name or full Amazon Resource Name (ARN) of the service to create the task set in.
    """
    __args__ = dict()
    __args__['cluster'] = cluster
    __args__['service'] = service
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ecs:getPrimaryTaskSet', __args__, opts=opts, typ=GetPrimaryTaskSetResult).value

    return AwaitableGetPrimaryTaskSetResult(
        task_set_id=pulumi.get(__ret__, 'task_set_id'))
def get_primary_task_set_output(cluster: Optional[pulumi.Input[builtins.str]] = None,
                                service: Optional[pulumi.Input[builtins.str]] = None,
                                opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetPrimaryTaskSetResult]:
    """
    A pseudo-resource that manages which of your ECS task sets is primary.


    :param builtins.str cluster: The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to create the task set in.
    :param builtins.str service: The short name or full Amazon Resource Name (ARN) of the service to create the task set in.
    """
    __args__ = dict()
    __args__['cluster'] = cluster
    __args__['service'] = service
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:ecs:getPrimaryTaskSet', __args__, opts=opts, typ=GetPrimaryTaskSetResult)
    return __ret__.apply(lambda __response__: GetPrimaryTaskSetResult(
        task_set_id=pulumi.get(__response__, 'task_set_id')))
