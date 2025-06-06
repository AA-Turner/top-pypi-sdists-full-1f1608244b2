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

__all__ = ['DedicatedIpPoolArgs', 'DedicatedIpPool']

@pulumi.input_type
class DedicatedIpPoolArgs:
    def __init__(__self__, *,
                 pool_name: Optional[pulumi.Input[builtins.str]] = None,
                 scaling_mode: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a DedicatedIpPool resource.
        :param pulumi.Input[builtins.str] pool_name: The name of the dedicated IP pool.
        :param pulumi.Input[builtins.str] scaling_mode: Specifies whether the dedicated IP pool is managed or not. The default value is STANDARD.
        """
        if pool_name is not None:
            pulumi.set(__self__, "pool_name", pool_name)
        if scaling_mode is not None:
            pulumi.set(__self__, "scaling_mode", scaling_mode)

    @property
    @pulumi.getter(name="poolName")
    def pool_name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the dedicated IP pool.
        """
        return pulumi.get(self, "pool_name")

    @pool_name.setter
    def pool_name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "pool_name", value)

    @property
    @pulumi.getter(name="scalingMode")
    def scaling_mode(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Specifies whether the dedicated IP pool is managed or not. The default value is STANDARD.
        """
        return pulumi.get(self, "scaling_mode")

    @scaling_mode.setter
    def scaling_mode(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "scaling_mode", value)


@pulumi.type_token("aws-native:ses:DedicatedIpPool")
class DedicatedIpPool(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 pool_name: Optional[pulumi.Input[builtins.str]] = None,
                 scaling_mode: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::SES::DedicatedIpPool

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] pool_name: The name of the dedicated IP pool.
        :param pulumi.Input[builtins.str] scaling_mode: Specifies whether the dedicated IP pool is managed or not. The default value is STANDARD.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DedicatedIpPoolArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::SES::DedicatedIpPool

        :param str resource_name: The name of the resource.
        :param DedicatedIpPoolArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DedicatedIpPoolArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 pool_name: Optional[pulumi.Input[builtins.str]] = None,
                 scaling_mode: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DedicatedIpPoolArgs.__new__(DedicatedIpPoolArgs)

            __props__.__dict__["pool_name"] = pool_name
            __props__.__dict__["scaling_mode"] = scaling_mode
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["poolName"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(DedicatedIpPool, __self__).__init__(
            'aws-native:ses:DedicatedIpPool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DedicatedIpPool':
        """
        Get an existing DedicatedIpPool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DedicatedIpPoolArgs.__new__(DedicatedIpPoolArgs)

        __props__.__dict__["pool_name"] = None
        __props__.__dict__["scaling_mode"] = None
        return DedicatedIpPool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="poolName")
    def pool_name(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The name of the dedicated IP pool.
        """
        return pulumi.get(self, "pool_name")

    @property
    @pulumi.getter(name="scalingMode")
    def scaling_mode(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        Specifies whether the dedicated IP pool is managed or not. The default value is STANDARD.
        """
        return pulumi.get(self, "scaling_mode")

