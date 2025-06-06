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
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs
from ._enums import *
from ._inputs import *

__all__ = ['ClusterArgs', 'Cluster']

@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *,
                 cluster_type: Optional[pulumi.Input['ClusterType']] = None,
                 instance_role_arn: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 network_settings: Optional[pulumi.Input['ClusterNetworkSettingsArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a Cluster resource.
        :param pulumi.Input[builtins.str] instance_role_arn: The IAM role your nodes will use.
        :param pulumi.Input[builtins.str] name: The user-specified name of the Cluster to be created.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: A collection of key-value pairs.
        """
        if cluster_type is not None:
            pulumi.set(__self__, "cluster_type", cluster_type)
        if instance_role_arn is not None:
            pulumi.set(__self__, "instance_role_arn", instance_role_arn)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network_settings is not None:
            pulumi.set(__self__, "network_settings", network_settings)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> Optional[pulumi.Input['ClusterType']]:
        return pulumi.get(self, "cluster_type")

    @cluster_type.setter
    def cluster_type(self, value: Optional[pulumi.Input['ClusterType']]):
        pulumi.set(self, "cluster_type", value)

    @property
    @pulumi.getter(name="instanceRoleArn")
    def instance_role_arn(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The IAM role your nodes will use.
        """
        return pulumi.get(self, "instance_role_arn")

    @instance_role_arn.setter
    def instance_role_arn(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "instance_role_arn", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The user-specified name of the Cluster to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="networkSettings")
    def network_settings(self) -> Optional[pulumi.Input['ClusterNetworkSettingsArgs']]:
        return pulumi.get(self, "network_settings")

    @network_settings.setter
    def network_settings(self, value: Optional[pulumi.Input['ClusterNetworkSettingsArgs']]):
        pulumi.set(self, "network_settings", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        A collection of key-value pairs.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


@pulumi.type_token("aws-native:medialive:Cluster")
class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_type: Optional[pulumi.Input['ClusterType']] = None,
                 instance_role_arn: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 network_settings: Optional[pulumi.Input[Union['ClusterNetworkSettingsArgs', 'ClusterNetworkSettingsArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 __props__=None):
        """
        Definition of AWS::MediaLive::Cluster Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] instance_role_arn: The IAM role your nodes will use.
        :param pulumi.Input[builtins.str] name: The user-specified name of the Cluster to be created.
        :param pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]] tags: A collection of key-value pairs.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ClusterArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::MediaLive::Cluster Resource Type

        :param str resource_name: The name of the resource.
        :param ClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_type: Optional[pulumi.Input['ClusterType']] = None,
                 instance_role_arn: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 network_settings: Optional[pulumi.Input[Union['ClusterNetworkSettingsArgs', 'ClusterNetworkSettingsArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ClusterArgs.__new__(ClusterArgs)

            __props__.__dict__["cluster_type"] = cluster_type
            __props__.__dict__["instance_role_arn"] = instance_role_arn
            __props__.__dict__["name"] = name
            __props__.__dict__["network_settings"] = network_settings
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["aws_id"] = None
            __props__.__dict__["channel_ids"] = None
            __props__.__dict__["state"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["clusterType", "instanceRoleArn"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Cluster, __self__).__init__(
            'aws-native:medialive:Cluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Cluster':
        """
        Get an existing Cluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ClusterArgs.__new__(ClusterArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["aws_id"] = None
        __props__.__dict__["channel_ids"] = None
        __props__.__dict__["cluster_type"] = None
        __props__.__dict__["instance_role_arn"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_settings"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["tags"] = None
        return Cluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[builtins.str]:
        """
        The ARN of the Cluster.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="awsId")
    def aws_id(self) -> pulumi.Output[builtins.str]:
        """
        The unique ID of the Cluster.
        """
        return pulumi.get(self, "aws_id")

    @property
    @pulumi.getter(name="channelIds")
    def channel_ids(self) -> pulumi.Output[Sequence[builtins.str]]:
        """
        The MediaLive Channels that are currently running on Nodes in this Cluster.
        """
        return pulumi.get(self, "channel_ids")

    @property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> pulumi.Output[Optional['ClusterType']]:
        return pulumi.get(self, "cluster_type")

    @property
    @pulumi.getter(name="instanceRoleArn")
    def instance_role_arn(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The IAM role your nodes will use.
        """
        return pulumi.get(self, "instance_role_arn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The user-specified name of the Cluster to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkSettings")
    def network_settings(self) -> pulumi.Output[Optional['outputs.ClusterNetworkSettings']]:
        return pulumi.get(self, "network_settings")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output['ClusterState']:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        A collection of key-value pairs.
        """
        return pulumi.get(self, "tags")

