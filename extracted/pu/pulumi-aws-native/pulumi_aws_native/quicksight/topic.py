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

__all__ = ['TopicArgs', 'Topic']

@pulumi.input_type
class TopicArgs:
    def __init__(__self__, *,
                 aws_account_id: Optional[pulumi.Input[builtins.str]] = None,
                 config_options: Optional[pulumi.Input['TopicConfigOptionsArgs']] = None,
                 data_sets: Optional[pulumi.Input[Sequence[pulumi.Input['TopicDatasetMetadataArgs']]]] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 folder_arns: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 topic_id: Optional[pulumi.Input[builtins.str]] = None,
                 user_experience_version: Optional[pulumi.Input['TopicUserExperienceVersion']] = None):
        """
        The set of arguments for constructing a Topic resource.
        :param pulumi.Input[builtins.str] aws_account_id: The ID of the AWS account that you want to create a topic in.
        :param pulumi.Input['TopicConfigOptionsArgs'] config_options: Configuration options for a `Topic` .
        :param pulumi.Input[Sequence[pulumi.Input['TopicDatasetMetadataArgs']]] data_sets: The data sets that the topic is associated with.
        :param pulumi.Input[builtins.str] description: The description of the topic.
        :param pulumi.Input[builtins.str] name: The name of the topic.
        :param pulumi.Input[builtins.str] topic_id: The ID for the topic. This ID is unique per AWS Region for each AWS account.
        :param pulumi.Input['TopicUserExperienceVersion'] user_experience_version: The user experience version of the topic.
        """
        if aws_account_id is not None:
            pulumi.set(__self__, "aws_account_id", aws_account_id)
        if config_options is not None:
            pulumi.set(__self__, "config_options", config_options)
        if data_sets is not None:
            pulumi.set(__self__, "data_sets", data_sets)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if folder_arns is not None:
            pulumi.set(__self__, "folder_arns", folder_arns)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if topic_id is not None:
            pulumi.set(__self__, "topic_id", topic_id)
        if user_experience_version is not None:
            pulumi.set(__self__, "user_experience_version", user_experience_version)

    @property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The ID of the AWS account that you want to create a topic in.
        """
        return pulumi.get(self, "aws_account_id")

    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "aws_account_id", value)

    @property
    @pulumi.getter(name="configOptions")
    def config_options(self) -> Optional[pulumi.Input['TopicConfigOptionsArgs']]:
        """
        Configuration options for a `Topic` .
        """
        return pulumi.get(self, "config_options")

    @config_options.setter
    def config_options(self, value: Optional[pulumi.Input['TopicConfigOptionsArgs']]):
        pulumi.set(self, "config_options", value)

    @property
    @pulumi.getter(name="dataSets")
    def data_sets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TopicDatasetMetadataArgs']]]]:
        """
        The data sets that the topic is associated with.
        """
        return pulumi.get(self, "data_sets")

    @data_sets.setter
    def data_sets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TopicDatasetMetadataArgs']]]]):
        pulumi.set(self, "data_sets", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The description of the topic.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="folderArns")
    def folder_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]:
        return pulumi.get(self, "folder_arns")

    @folder_arns.setter
    def folder_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "folder_arns", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the topic.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="topicId")
    def topic_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The ID for the topic. This ID is unique per AWS Region for each AWS account.
        """
        return pulumi.get(self, "topic_id")

    @topic_id.setter
    def topic_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "topic_id", value)

    @property
    @pulumi.getter(name="userExperienceVersion")
    def user_experience_version(self) -> Optional[pulumi.Input['TopicUserExperienceVersion']]:
        """
        The user experience version of the topic.
        """
        return pulumi.get(self, "user_experience_version")

    @user_experience_version.setter
    def user_experience_version(self, value: Optional[pulumi.Input['TopicUserExperienceVersion']]):
        pulumi.set(self, "user_experience_version", value)


@pulumi.type_token("aws-native:quicksight:Topic")
class Topic(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_account_id: Optional[pulumi.Input[builtins.str]] = None,
                 config_options: Optional[pulumi.Input[Union['TopicConfigOptionsArgs', 'TopicConfigOptionsArgsDict']]] = None,
                 data_sets: Optional[pulumi.Input[Sequence[pulumi.Input[Union['TopicDatasetMetadataArgs', 'TopicDatasetMetadataArgsDict']]]]] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 folder_arns: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 topic_id: Optional[pulumi.Input[builtins.str]] = None,
                 user_experience_version: Optional[pulumi.Input['TopicUserExperienceVersion']] = None,
                 __props__=None):
        """
        Definition of the AWS::QuickSight::Topic Resource Type.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] aws_account_id: The ID of the AWS account that you want to create a topic in.
        :param pulumi.Input[Union['TopicConfigOptionsArgs', 'TopicConfigOptionsArgsDict']] config_options: Configuration options for a `Topic` .
        :param pulumi.Input[Sequence[pulumi.Input[Union['TopicDatasetMetadataArgs', 'TopicDatasetMetadataArgsDict']]]] data_sets: The data sets that the topic is associated with.
        :param pulumi.Input[builtins.str] description: The description of the topic.
        :param pulumi.Input[builtins.str] name: The name of the topic.
        :param pulumi.Input[builtins.str] topic_id: The ID for the topic. This ID is unique per AWS Region for each AWS account.
        :param pulumi.Input['TopicUserExperienceVersion'] user_experience_version: The user experience version of the topic.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[TopicArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of the AWS::QuickSight::Topic Resource Type.

        :param str resource_name: The name of the resource.
        :param TopicArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TopicArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_account_id: Optional[pulumi.Input[builtins.str]] = None,
                 config_options: Optional[pulumi.Input[Union['TopicConfigOptionsArgs', 'TopicConfigOptionsArgsDict']]] = None,
                 data_sets: Optional[pulumi.Input[Sequence[pulumi.Input[Union['TopicDatasetMetadataArgs', 'TopicDatasetMetadataArgsDict']]]]] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 folder_arns: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 topic_id: Optional[pulumi.Input[builtins.str]] = None,
                 user_experience_version: Optional[pulumi.Input['TopicUserExperienceVersion']] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TopicArgs.__new__(TopicArgs)

            __props__.__dict__["aws_account_id"] = aws_account_id
            __props__.__dict__["config_options"] = config_options
            __props__.__dict__["data_sets"] = data_sets
            __props__.__dict__["description"] = description
            __props__.__dict__["folder_arns"] = folder_arns
            __props__.__dict__["name"] = name
            __props__.__dict__["topic_id"] = topic_id
            __props__.__dict__["user_experience_version"] = user_experience_version
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["awsAccountId", "folderArns[*]", "topicId"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Topic, __self__).__init__(
            'aws-native:quicksight:Topic',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Topic':
        """
        Get an existing Topic resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TopicArgs.__new__(TopicArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["aws_account_id"] = None
        __props__.__dict__["config_options"] = None
        __props__.__dict__["data_sets"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["folder_arns"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["topic_id"] = None
        __props__.__dict__["user_experience_version"] = None
        return Topic(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[builtins.str]:
        """
        The Amazon Resource Name (ARN) of the topic.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The ID of the AWS account that you want to create a topic in.
        """
        return pulumi.get(self, "aws_account_id")

    @property
    @pulumi.getter(name="configOptions")
    def config_options(self) -> pulumi.Output[Optional['outputs.TopicConfigOptions']]:
        """
        Configuration options for a `Topic` .
        """
        return pulumi.get(self, "config_options")

    @property
    @pulumi.getter(name="dataSets")
    def data_sets(self) -> pulumi.Output[Optional[Sequence['outputs.TopicDatasetMetadata']]]:
        """
        The data sets that the topic is associated with.
        """
        return pulumi.get(self, "data_sets")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The description of the topic.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="folderArns")
    def folder_arns(self) -> pulumi.Output[Optional[Sequence[builtins.str]]]:
        return pulumi.get(self, "folder_arns")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The name of the topic.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="topicId")
    def topic_id(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The ID for the topic. This ID is unique per AWS Region for each AWS account.
        """
        return pulumi.get(self, "topic_id")

    @property
    @pulumi.getter(name="userExperienceVersion")
    def user_experience_version(self) -> pulumi.Output[Optional['TopicUserExperienceVersion']]:
        """
        The user experience version of the topic.
        """
        return pulumi.get(self, "user_experience_version")

