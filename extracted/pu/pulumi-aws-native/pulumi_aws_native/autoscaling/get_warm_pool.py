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
    'GetWarmPoolResult',
    'AwaitableGetWarmPoolResult',
    'get_warm_pool',
    'get_warm_pool_output',
]

@pulumi.output_type
class GetWarmPoolResult:
    def __init__(__self__, instance_reuse_policy=None, max_group_prepared_capacity=None, min_size=None, pool_state=None):
        if instance_reuse_policy and not isinstance(instance_reuse_policy, dict):
            raise TypeError("Expected argument 'instance_reuse_policy' to be a dict")
        pulumi.set(__self__, "instance_reuse_policy", instance_reuse_policy)
        if max_group_prepared_capacity and not isinstance(max_group_prepared_capacity, int):
            raise TypeError("Expected argument 'max_group_prepared_capacity' to be a int")
        pulumi.set(__self__, "max_group_prepared_capacity", max_group_prepared_capacity)
        if min_size and not isinstance(min_size, int):
            raise TypeError("Expected argument 'min_size' to be a int")
        pulumi.set(__self__, "min_size", min_size)
        if pool_state and not isinstance(pool_state, str):
            raise TypeError("Expected argument 'pool_state' to be a str")
        pulumi.set(__self__, "pool_state", pool_state)

    @property
    @pulumi.getter(name="instanceReusePolicy")
    def instance_reuse_policy(self) -> Optional['outputs.WarmPoolInstanceReusePolicy']:
        """
        Indicates whether instances in the Auto Scaling group can be returned to the warm pool on scale in. The default is to terminate instances in the Auto Scaling group when the group scales in.
        """
        return pulumi.get(self, "instance_reuse_policy")

    @property
    @pulumi.getter(name="maxGroupPreparedCapacity")
    def max_group_prepared_capacity(self) -> Optional[builtins.int]:
        """
        Specifies the maximum number of instances that are allowed to be in the warm pool or in any state except `Terminated` for the Auto Scaling group. This is an optional property. Specify it only if you do not want the warm pool size to be determined by the difference between the group's maximum capacity and its desired capacity.

        > If a value for `MaxGroupPreparedCapacity` is not specified, Amazon EC2 Auto Scaling launches and maintains the difference between the group's maximum capacity and its desired capacity. If you specify a value for `MaxGroupPreparedCapacity` , Amazon EC2 Auto Scaling uses the difference between the `MaxGroupPreparedCapacity` and the desired capacity instead.
        > 
        > The size of the warm pool is dynamic. Only when `MaxGroupPreparedCapacity` and `MinSize` are set to the same value does the warm pool have an absolute size. 

        If the desired capacity of the Auto Scaling group is higher than the `MaxGroupPreparedCapacity` , the capacity of the warm pool is 0, unless you specify a value for `MinSize` . To remove a value that you previously set, include the property but specify -1 for the value.
        """
        return pulumi.get(self, "max_group_prepared_capacity")

    @property
    @pulumi.getter(name="minSize")
    def min_size(self) -> Optional[builtins.int]:
        """
        Specifies the minimum number of instances to maintain in the warm pool. This helps you to ensure that there is always a certain number of warmed instances available to handle traffic spikes. Defaults to 0 if not specified.
        """
        return pulumi.get(self, "min_size")

    @property
    @pulumi.getter(name="poolState")
    def pool_state(self) -> Optional[builtins.str]:
        """
        Sets the instance state to transition to after the lifecycle actions are complete. Default is `Stopped` .
        """
        return pulumi.get(self, "pool_state")


class AwaitableGetWarmPoolResult(GetWarmPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWarmPoolResult(
            instance_reuse_policy=self.instance_reuse_policy,
            max_group_prepared_capacity=self.max_group_prepared_capacity,
            min_size=self.min_size,
            pool_state=self.pool_state)


def get_warm_pool(auto_scaling_group_name: Optional[builtins.str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWarmPoolResult:
    """
    Resource schema for AWS::AutoScaling::WarmPool.


    :param builtins.str auto_scaling_group_name: The name of the Auto Scaling group.
    """
    __args__ = dict()
    __args__['autoScalingGroupName'] = auto_scaling_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:autoscaling:getWarmPool', __args__, opts=opts, typ=GetWarmPoolResult).value

    return AwaitableGetWarmPoolResult(
        instance_reuse_policy=pulumi.get(__ret__, 'instance_reuse_policy'),
        max_group_prepared_capacity=pulumi.get(__ret__, 'max_group_prepared_capacity'),
        min_size=pulumi.get(__ret__, 'min_size'),
        pool_state=pulumi.get(__ret__, 'pool_state'))
def get_warm_pool_output(auto_scaling_group_name: Optional[pulumi.Input[builtins.str]] = None,
                         opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetWarmPoolResult]:
    """
    Resource schema for AWS::AutoScaling::WarmPool.


    :param builtins.str auto_scaling_group_name: The name of the Auto Scaling group.
    """
    __args__ = dict()
    __args__['autoScalingGroupName'] = auto_scaling_group_name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:autoscaling:getWarmPool', __args__, opts=opts, typ=GetWarmPoolResult)
    return __ret__.apply(lambda __response__: GetWarmPoolResult(
        instance_reuse_policy=pulumi.get(__response__, 'instance_reuse_policy'),
        max_group_prepared_capacity=pulumi.get(__response__, 'max_group_prepared_capacity'),
        min_size=pulumi.get(__response__, 'min_size'),
        pool_state=pulumi.get(__response__, 'pool_state')))
