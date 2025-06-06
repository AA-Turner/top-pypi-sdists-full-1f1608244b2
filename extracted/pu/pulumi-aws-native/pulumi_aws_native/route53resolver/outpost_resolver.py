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
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs
from ._enums import *

__all__ = ['OutpostResolverArgs', 'OutpostResolver']

@pulumi.input_type
class OutpostResolverArgs:
    def __init__(__self__, *,
                 outpost_arn: pulumi.Input[builtins.str],
                 preferred_instance_type: pulumi.Input[builtins.str],
                 instance_count: Optional[pulumi.Input[builtins.int]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a OutpostResolver resource.
        :param pulumi.Input[builtins.str] outpost_arn: The Outpost ARN.
        :param pulumi.Input[builtins.str] preferred_instance_type: The OutpostResolver instance type.
        :param pulumi.Input[builtins.int] instance_count: The number of OutpostResolvers.
        :param pulumi.Input[builtins.str] name: The OutpostResolver name.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        pulumi.set(__self__, "outpost_arn", outpost_arn)
        pulumi.set(__self__, "preferred_instance_type", preferred_instance_type)
        if instance_count is not None:
            pulumi.set(__self__, "instance_count", instance_count)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> pulumi.Input[builtins.str]:
        """
        The Outpost ARN.
        """
        return pulumi.get(self, "outpost_arn")

    @outpost_arn.setter
    def outpost_arn(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "outpost_arn", value)

    @property
    @pulumi.getter(name="preferredInstanceType")
    def preferred_instance_type(self) -> pulumi.Input[builtins.str]:
        """
        The OutpostResolver instance type.
        """
        return pulumi.get(self, "preferred_instance_type")

    @preferred_instance_type.setter
    def preferred_instance_type(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "preferred_instance_type", value)

    @property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[pulumi.Input[builtins.int]]:
        """
        The number of OutpostResolvers.
        """
        return pulumi.get(self, "instance_count")

    @instance_count.setter
    def instance_count(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "instance_count", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The OutpostResolver name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


@pulumi.type_token("aws-native:route53resolver:OutpostResolver")
class OutpostResolver(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance_count: Optional[pulumi.Input[builtins.int]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 outpost_arn: Optional[pulumi.Input[builtins.str]] = None,
                 preferred_instance_type: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 __props__=None):
        """
        Resource schema for AWS::Route53Resolver::OutpostResolver.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.int] instance_count: The number of OutpostResolvers.
        :param pulumi.Input[builtins.str] name: The OutpostResolver name.
        :param pulumi.Input[builtins.str] outpost_arn: The Outpost ARN.
        :param pulumi.Input[builtins.str] preferred_instance_type: The OutpostResolver instance type.
        :param pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OutpostResolverArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::Route53Resolver::OutpostResolver.

        :param str resource_name: The name of the resource.
        :param OutpostResolverArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OutpostResolverArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance_count: Optional[pulumi.Input[builtins.int]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 outpost_arn: Optional[pulumi.Input[builtins.str]] = None,
                 preferred_instance_type: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OutpostResolverArgs.__new__(OutpostResolverArgs)

            __props__.__dict__["instance_count"] = instance_count
            __props__.__dict__["name"] = name
            if outpost_arn is None and not opts.urn:
                raise TypeError("Missing required property 'outpost_arn'")
            __props__.__dict__["outpost_arn"] = outpost_arn
            if preferred_instance_type is None and not opts.urn:
                raise TypeError("Missing required property 'preferred_instance_type'")
            __props__.__dict__["preferred_instance_type"] = preferred_instance_type
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["aws_id"] = None
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["creator_request_id"] = None
            __props__.__dict__["modification_time"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["status_message"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["outpostArn"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(OutpostResolver, __self__).__init__(
            'aws-native:route53resolver:OutpostResolver',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OutpostResolver':
        """
        Get an existing OutpostResolver resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OutpostResolverArgs.__new__(OutpostResolverArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["aws_id"] = None
        __props__.__dict__["creation_time"] = None
        __props__.__dict__["creator_request_id"] = None
        __props__.__dict__["instance_count"] = None
        __props__.__dict__["modification_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["outpost_arn"] = None
        __props__.__dict__["preferred_instance_type"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["status_message"] = None
        __props__.__dict__["tags"] = None
        return OutpostResolver(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[builtins.str]:
        """
        The OutpostResolver ARN.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="awsId")
    def aws_id(self) -> pulumi.Output[builtins.str]:
        """
        Id
        """
        return pulumi.get(self, "aws_id")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[builtins.str]:
        """
        The OutpostResolver creation time
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="creatorRequestId")
    def creator_request_id(self) -> pulumi.Output[builtins.str]:
        """
        The id of the creator request.
        """
        return pulumi.get(self, "creator_request_id")

    @property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> pulumi.Output[Optional[builtins.int]]:
        """
        The number of OutpostResolvers.
        """
        return pulumi.get(self, "instance_count")

    @property
    @pulumi.getter(name="modificationTime")
    def modification_time(self) -> pulumi.Output[builtins.str]:
        """
        The OutpostResolver last modified time
        """
        return pulumi.get(self, "modification_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        The OutpostResolver name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> pulumi.Output[builtins.str]:
        """
        The Outpost ARN.
        """
        return pulumi.get(self, "outpost_arn")

    @property
    @pulumi.getter(name="preferredInstanceType")
    def preferred_instance_type(self) -> pulumi.Output[builtins.str]:
        """
        The OutpostResolver instance type.
        """
        return pulumi.get(self, "preferred_instance_type")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['OutpostResolverStatus']:
        """
        The OutpostResolver status, possible values are CREATING, OPERATIONAL, UPDATING, DELETING, ACTION_NEEDED, FAILED_CREATION and FAILED_DELETION.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> pulumi.Output[builtins.str]:
        """
        The OutpostResolver status message.
        """
        return pulumi.get(self, "status_message")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

