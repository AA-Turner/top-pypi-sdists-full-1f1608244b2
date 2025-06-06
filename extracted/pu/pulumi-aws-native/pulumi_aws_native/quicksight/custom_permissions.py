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

__all__ = ['CustomPermissionsArgs', 'CustomPermissions']

@pulumi.input_type
class CustomPermissionsArgs:
    def __init__(__self__, *,
                 aws_account_id: pulumi.Input[builtins.str],
                 capabilities: Optional[pulumi.Input['CustomPermissionsCapabilitiesArgs']] = None,
                 custom_permissions_name: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a CustomPermissions resource.
        :param pulumi.Input[builtins.str] aws_account_id: The ID of the AWS account that contains the custom permission configuration that you want to update.
        :param pulumi.Input['CustomPermissionsCapabilitiesArgs'] capabilities: A set of actions in the custom permissions profile.
        :param pulumi.Input[builtins.str] custom_permissions_name: The name of the custom permissions profile.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: The tags to associate with the custom permissions profile.
        """
        pulumi.set(__self__, "aws_account_id", aws_account_id)
        if capabilities is not None:
            pulumi.set(__self__, "capabilities", capabilities)
        if custom_permissions_name is not None:
            pulumi.set(__self__, "custom_permissions_name", custom_permissions_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Input[builtins.str]:
        """
        The ID of the AWS account that contains the custom permission configuration that you want to update.
        """
        return pulumi.get(self, "aws_account_id")

    @aws_account_id.setter
    def aws_account_id(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "aws_account_id", value)

    @property
    @pulumi.getter
    def capabilities(self) -> Optional[pulumi.Input['CustomPermissionsCapabilitiesArgs']]:
        """
        A set of actions in the custom permissions profile.
        """
        return pulumi.get(self, "capabilities")

    @capabilities.setter
    def capabilities(self, value: Optional[pulumi.Input['CustomPermissionsCapabilitiesArgs']]):
        pulumi.set(self, "capabilities", value)

    @property
    @pulumi.getter(name="customPermissionsName")
    def custom_permissions_name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the custom permissions profile.
        """
        return pulumi.get(self, "custom_permissions_name")

    @custom_permissions_name.setter
    def custom_permissions_name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "custom_permissions_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        The tags to associate with the custom permissions profile.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


@pulumi.type_token("aws-native:quicksight:CustomPermissions")
class CustomPermissions(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_account_id: Optional[pulumi.Input[builtins.str]] = None,
                 capabilities: Optional[pulumi.Input[Union['CustomPermissionsCapabilitiesArgs', 'CustomPermissionsCapabilitiesArgsDict']]] = None,
                 custom_permissions_name: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 __props__=None):
        """
        Definition of the AWS::QuickSight::CustomPermissions Resource Type.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] aws_account_id: The ID of the AWS account that contains the custom permission configuration that you want to update.
        :param pulumi.Input[Union['CustomPermissionsCapabilitiesArgs', 'CustomPermissionsCapabilitiesArgsDict']] capabilities: A set of actions in the custom permissions profile.
        :param pulumi.Input[builtins.str] custom_permissions_name: The name of the custom permissions profile.
        :param pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]] tags: The tags to associate with the custom permissions profile.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CustomPermissionsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of the AWS::QuickSight::CustomPermissions Resource Type.

        :param str resource_name: The name of the resource.
        :param CustomPermissionsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CustomPermissionsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_account_id: Optional[pulumi.Input[builtins.str]] = None,
                 capabilities: Optional[pulumi.Input[Union['CustomPermissionsCapabilitiesArgs', 'CustomPermissionsCapabilitiesArgsDict']]] = None,
                 custom_permissions_name: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CustomPermissionsArgs.__new__(CustomPermissionsArgs)

            if aws_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'aws_account_id'")
            __props__.__dict__["aws_account_id"] = aws_account_id
            __props__.__dict__["capabilities"] = capabilities
            __props__.__dict__["custom_permissions_name"] = custom_permissions_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["awsAccountId", "customPermissionsName"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(CustomPermissions, __self__).__init__(
            'aws-native:quicksight:CustomPermissions',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CustomPermissions':
        """
        Get an existing CustomPermissions resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CustomPermissionsArgs.__new__(CustomPermissionsArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["aws_account_id"] = None
        __props__.__dict__["capabilities"] = None
        __props__.__dict__["custom_permissions_name"] = None
        __props__.__dict__["tags"] = None
        return CustomPermissions(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[builtins.str]:
        """
        The Amazon Resource Name (ARN) of the custom permissions profile.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Output[builtins.str]:
        """
        The ID of the AWS account that contains the custom permission configuration that you want to update.
        """
        return pulumi.get(self, "aws_account_id")

    @property
    @pulumi.getter
    def capabilities(self) -> pulumi.Output[Optional['outputs.CustomPermissionsCapabilities']]:
        """
        A set of actions in the custom permissions profile.
        """
        return pulumi.get(self, "capabilities")

    @property
    @pulumi.getter(name="customPermissionsName")
    def custom_permissions_name(self) -> pulumi.Output[builtins.str]:
        """
        The name of the custom permissions profile.
        """
        return pulumi.get(self, "custom_permissions_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        The tags to associate with the custom permissions profile.
        """
        return pulumi.get(self, "tags")

