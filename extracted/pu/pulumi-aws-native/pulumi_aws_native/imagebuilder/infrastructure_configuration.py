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
from ._enums import *
from ._inputs import *

__all__ = ['InfrastructureConfigurationArgs', 'InfrastructureConfiguration']

@pulumi.input_type
class InfrastructureConfigurationArgs:
    def __init__(__self__, *,
                 instance_profile_name: pulumi.Input[builtins.str],
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 instance_metadata_options: Optional[pulumi.Input['InfrastructureConfigurationInstanceMetadataOptionsArgs']] = None,
                 instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 key_pair: Optional[pulumi.Input[builtins.str]] = None,
                 logging: Optional[pulumi.Input['InfrastructureConfigurationLoggingArgs']] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 placement: Optional[pulumi.Input['InfrastructureConfigurationPlacementArgs']] = None,
                 resource_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 sns_topic_arn: Optional[pulumi.Input[builtins.str]] = None,
                 subnet_id: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 terminate_instance_on_failure: Optional[pulumi.Input[builtins.bool]] = None):
        """
        The set of arguments for constructing a InfrastructureConfiguration resource.
        :param pulumi.Input[builtins.str] instance_profile_name: The instance profile of the infrastructure configuration.
        :param pulumi.Input[builtins.str] description: The description of the infrastructure configuration.
        :param pulumi.Input['InfrastructureConfigurationInstanceMetadataOptionsArgs'] instance_metadata_options: The instance metadata option settings for the infrastructure configuration.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] instance_types: The instance types of the infrastructure configuration.
        :param pulumi.Input[builtins.str] key_pair: The EC2 key pair of the infrastructure configuration..
        :param pulumi.Input['InfrastructureConfigurationLoggingArgs'] logging: The logging configuration of the infrastructure configuration.
        :param pulumi.Input[builtins.str] name: The name of the infrastructure configuration.
        :param pulumi.Input['InfrastructureConfigurationPlacementArgs'] placement: The placement option settings for the infrastructure configuration.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] resource_tags: The tags attached to the resource created by Image Builder.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] security_group_ids: The security group IDs of the infrastructure configuration.
        :param pulumi.Input[builtins.str] sns_topic_arn: The SNS Topic Amazon Resource Name (ARN) of the infrastructure configuration.
        :param pulumi.Input[builtins.str] subnet_id: The subnet ID of the infrastructure configuration.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] tags: The tags associated with the component.
        :param pulumi.Input[builtins.bool] terminate_instance_on_failure: The terminate instance on failure configuration of the infrastructure configuration.
        """
        pulumi.set(__self__, "instance_profile_name", instance_profile_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if instance_metadata_options is not None:
            pulumi.set(__self__, "instance_metadata_options", instance_metadata_options)
        if instance_types is not None:
            pulumi.set(__self__, "instance_types", instance_types)
        if key_pair is not None:
            pulumi.set(__self__, "key_pair", key_pair)
        if logging is not None:
            pulumi.set(__self__, "logging", logging)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if placement is not None:
            pulumi.set(__self__, "placement", placement)
        if resource_tags is not None:
            pulumi.set(__self__, "resource_tags", resource_tags)
        if security_group_ids is not None:
            pulumi.set(__self__, "security_group_ids", security_group_ids)
        if sns_topic_arn is not None:
            pulumi.set(__self__, "sns_topic_arn", sns_topic_arn)
        if subnet_id is not None:
            pulumi.set(__self__, "subnet_id", subnet_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if terminate_instance_on_failure is not None:
            pulumi.set(__self__, "terminate_instance_on_failure", terminate_instance_on_failure)

    @property
    @pulumi.getter(name="instanceProfileName")
    def instance_profile_name(self) -> pulumi.Input[builtins.str]:
        """
        The instance profile of the infrastructure configuration.
        """
        return pulumi.get(self, "instance_profile_name")

    @instance_profile_name.setter
    def instance_profile_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "instance_profile_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The description of the infrastructure configuration.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="instanceMetadataOptions")
    def instance_metadata_options(self) -> Optional[pulumi.Input['InfrastructureConfigurationInstanceMetadataOptionsArgs']]:
        """
        The instance metadata option settings for the infrastructure configuration.
        """
        return pulumi.get(self, "instance_metadata_options")

    @instance_metadata_options.setter
    def instance_metadata_options(self, value: Optional[pulumi.Input['InfrastructureConfigurationInstanceMetadataOptionsArgs']]):
        pulumi.set(self, "instance_metadata_options", value)

    @property
    @pulumi.getter(name="instanceTypes")
    def instance_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]:
        """
        The instance types of the infrastructure configuration.
        """
        return pulumi.get(self, "instance_types")

    @instance_types.setter
    def instance_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "instance_types", value)

    @property
    @pulumi.getter(name="keyPair")
    def key_pair(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The EC2 key pair of the infrastructure configuration..
        """
        return pulumi.get(self, "key_pair")

    @key_pair.setter
    def key_pair(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "key_pair", value)

    @property
    @pulumi.getter
    def logging(self) -> Optional[pulumi.Input['InfrastructureConfigurationLoggingArgs']]:
        """
        The logging configuration of the infrastructure configuration.
        """
        return pulumi.get(self, "logging")

    @logging.setter
    def logging(self, value: Optional[pulumi.Input['InfrastructureConfigurationLoggingArgs']]):
        pulumi.set(self, "logging", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the infrastructure configuration.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def placement(self) -> Optional[pulumi.Input['InfrastructureConfigurationPlacementArgs']]:
        """
        The placement option settings for the infrastructure configuration.
        """
        return pulumi.get(self, "placement")

    @placement.setter
    def placement(self, value: Optional[pulumi.Input['InfrastructureConfigurationPlacementArgs']]):
        pulumi.set(self, "placement", value)

    @property
    @pulumi.getter(name="resourceTags")
    def resource_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]:
        """
        The tags attached to the resource created by Image Builder.
        """
        return pulumi.get(self, "resource_tags")

    @resource_tags.setter
    def resource_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "resource_tags", value)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]:
        """
        The security group IDs of the infrastructure configuration.
        """
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "security_group_ids", value)

    @property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The SNS Topic Amazon Resource Name (ARN) of the infrastructure configuration.
        """
        return pulumi.get(self, "sns_topic_arn")

    @sns_topic_arn.setter
    def sns_topic_arn(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "sns_topic_arn", value)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The subnet ID of the infrastructure configuration.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]:
        """
        The tags associated with the component.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="terminateInstanceOnFailure")
    def terminate_instance_on_failure(self) -> Optional[pulumi.Input[builtins.bool]]:
        """
        The terminate instance on failure configuration of the infrastructure configuration.
        """
        return pulumi.get(self, "terminate_instance_on_failure")

    @terminate_instance_on_failure.setter
    def terminate_instance_on_failure(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "terminate_instance_on_failure", value)


@pulumi.type_token("aws-native:imagebuilder:InfrastructureConfiguration")
class InfrastructureConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 instance_metadata_options: Optional[pulumi.Input[Union['InfrastructureConfigurationInstanceMetadataOptionsArgs', 'InfrastructureConfigurationInstanceMetadataOptionsArgsDict']]] = None,
                 instance_profile_name: Optional[pulumi.Input[builtins.str]] = None,
                 instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 key_pair: Optional[pulumi.Input[builtins.str]] = None,
                 logging: Optional[pulumi.Input[Union['InfrastructureConfigurationLoggingArgs', 'InfrastructureConfigurationLoggingArgsDict']]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 placement: Optional[pulumi.Input[Union['InfrastructureConfigurationPlacementArgs', 'InfrastructureConfigurationPlacementArgsDict']]] = None,
                 resource_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 sns_topic_arn: Optional[pulumi.Input[builtins.str]] = None,
                 subnet_id: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 terminate_instance_on_failure: Optional[pulumi.Input[builtins.bool]] = None,
                 __props__=None):
        """
        Resource schema for AWS::ImageBuilder::InfrastructureConfiguration

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] description: The description of the infrastructure configuration.
        :param pulumi.Input[Union['InfrastructureConfigurationInstanceMetadataOptionsArgs', 'InfrastructureConfigurationInstanceMetadataOptionsArgsDict']] instance_metadata_options: The instance metadata option settings for the infrastructure configuration.
        :param pulumi.Input[builtins.str] instance_profile_name: The instance profile of the infrastructure configuration.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] instance_types: The instance types of the infrastructure configuration.
        :param pulumi.Input[builtins.str] key_pair: The EC2 key pair of the infrastructure configuration..
        :param pulumi.Input[Union['InfrastructureConfigurationLoggingArgs', 'InfrastructureConfigurationLoggingArgsDict']] logging: The logging configuration of the infrastructure configuration.
        :param pulumi.Input[builtins.str] name: The name of the infrastructure configuration.
        :param pulumi.Input[Union['InfrastructureConfigurationPlacementArgs', 'InfrastructureConfigurationPlacementArgsDict']] placement: The placement option settings for the infrastructure configuration.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] resource_tags: The tags attached to the resource created by Image Builder.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] security_group_ids: The security group IDs of the infrastructure configuration.
        :param pulumi.Input[builtins.str] sns_topic_arn: The SNS Topic Amazon Resource Name (ARN) of the infrastructure configuration.
        :param pulumi.Input[builtins.str] subnet_id: The subnet ID of the infrastructure configuration.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] tags: The tags associated with the component.
        :param pulumi.Input[builtins.bool] terminate_instance_on_failure: The terminate instance on failure configuration of the infrastructure configuration.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InfrastructureConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::ImageBuilder::InfrastructureConfiguration

        :param str resource_name: The name of the resource.
        :param InfrastructureConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InfrastructureConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 instance_metadata_options: Optional[pulumi.Input[Union['InfrastructureConfigurationInstanceMetadataOptionsArgs', 'InfrastructureConfigurationInstanceMetadataOptionsArgsDict']]] = None,
                 instance_profile_name: Optional[pulumi.Input[builtins.str]] = None,
                 instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 key_pair: Optional[pulumi.Input[builtins.str]] = None,
                 logging: Optional[pulumi.Input[Union['InfrastructureConfigurationLoggingArgs', 'InfrastructureConfigurationLoggingArgsDict']]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 placement: Optional[pulumi.Input[Union['InfrastructureConfigurationPlacementArgs', 'InfrastructureConfigurationPlacementArgsDict']]] = None,
                 resource_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 sns_topic_arn: Optional[pulumi.Input[builtins.str]] = None,
                 subnet_id: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 terminate_instance_on_failure: Optional[pulumi.Input[builtins.bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InfrastructureConfigurationArgs.__new__(InfrastructureConfigurationArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["instance_metadata_options"] = instance_metadata_options
            if instance_profile_name is None and not opts.urn:
                raise TypeError("Missing required property 'instance_profile_name'")
            __props__.__dict__["instance_profile_name"] = instance_profile_name
            __props__.__dict__["instance_types"] = instance_types
            __props__.__dict__["key_pair"] = key_pair
            __props__.__dict__["logging"] = logging
            __props__.__dict__["name"] = name
            __props__.__dict__["placement"] = placement
            __props__.__dict__["resource_tags"] = resource_tags
            __props__.__dict__["security_group_ids"] = security_group_ids
            __props__.__dict__["sns_topic_arn"] = sns_topic_arn
            __props__.__dict__["subnet_id"] = subnet_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["terminate_instance_on_failure"] = terminate_instance_on_failure
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(InfrastructureConfiguration, __self__).__init__(
            'aws-native:imagebuilder:InfrastructureConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'InfrastructureConfiguration':
        """
        Get an existing InfrastructureConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = InfrastructureConfigurationArgs.__new__(InfrastructureConfigurationArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["instance_metadata_options"] = None
        __props__.__dict__["instance_profile_name"] = None
        __props__.__dict__["instance_types"] = None
        __props__.__dict__["key_pair"] = None
        __props__.__dict__["logging"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["placement"] = None
        __props__.__dict__["resource_tags"] = None
        __props__.__dict__["security_group_ids"] = None
        __props__.__dict__["sns_topic_arn"] = None
        __props__.__dict__["subnet_id"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["terminate_instance_on_failure"] = None
        return InfrastructureConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[builtins.str]:
        """
        The Amazon Resource Name (ARN) of the infrastructure configuration.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The description of the infrastructure configuration.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="instanceMetadataOptions")
    def instance_metadata_options(self) -> pulumi.Output[Optional['outputs.InfrastructureConfigurationInstanceMetadataOptions']]:
        """
        The instance metadata option settings for the infrastructure configuration.
        """
        return pulumi.get(self, "instance_metadata_options")

    @property
    @pulumi.getter(name="instanceProfileName")
    def instance_profile_name(self) -> pulumi.Output[builtins.str]:
        """
        The instance profile of the infrastructure configuration.
        """
        return pulumi.get(self, "instance_profile_name")

    @property
    @pulumi.getter(name="instanceTypes")
    def instance_types(self) -> pulumi.Output[Optional[Sequence[builtins.str]]]:
        """
        The instance types of the infrastructure configuration.
        """
        return pulumi.get(self, "instance_types")

    @property
    @pulumi.getter(name="keyPair")
    def key_pair(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The EC2 key pair of the infrastructure configuration..
        """
        return pulumi.get(self, "key_pair")

    @property
    @pulumi.getter
    def logging(self) -> pulumi.Output[Optional['outputs.InfrastructureConfigurationLogging']]:
        """
        The logging configuration of the infrastructure configuration.
        """
        return pulumi.get(self, "logging")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        The name of the infrastructure configuration.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def placement(self) -> pulumi.Output[Optional['outputs.InfrastructureConfigurationPlacement']]:
        """
        The placement option settings for the infrastructure configuration.
        """
        return pulumi.get(self, "placement")

    @property
    @pulumi.getter(name="resourceTags")
    def resource_tags(self) -> pulumi.Output[Optional[Mapping[str, builtins.str]]]:
        """
        The tags attached to the resource created by Image Builder.
        """
        return pulumi.get(self, "resource_tags")

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Output[Optional[Sequence[builtins.str]]]:
        """
        The security group IDs of the infrastructure configuration.
        """
        return pulumi.get(self, "security_group_ids")

    @property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The SNS Topic Amazon Resource Name (ARN) of the infrastructure configuration.
        """
        return pulumi.get(self, "sns_topic_arn")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The subnet ID of the infrastructure configuration.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, builtins.str]]]:
        """
        The tags associated with the component.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="terminateInstanceOnFailure")
    def terminate_instance_on_failure(self) -> pulumi.Output[Optional[builtins.bool]]:
        """
        The terminate instance on failure configuration of the infrastructure configuration.
        """
        return pulumi.get(self, "terminate_instance_on_failure")

