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

__all__ = ['LocationFSxWindowsArgs', 'LocationFSxWindows']

@pulumi.input_type
class LocationFSxWindowsArgs:
    def __init__(__self__, *,
                 security_group_arns: pulumi.Input[Sequence[pulumi.Input[builtins.str]]],
                 user: pulumi.Input[builtins.str],
                 domain: Optional[pulumi.Input[builtins.str]] = None,
                 fsx_filesystem_arn: Optional[pulumi.Input[builtins.str]] = None,
                 password: Optional[pulumi.Input[builtins.str]] = None,
                 subdirectory: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a LocationFSxWindows resource.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] security_group_arns: The ARNs of the security groups that are to use to configure the FSx for Windows file system.
        :param pulumi.Input[builtins.str] user: The user who has the permissions to access files and folders in the FSx for Windows file system.
        :param pulumi.Input[builtins.str] domain: The name of the Windows domain that the FSx for Windows server belongs to.
        :param pulumi.Input[builtins.str] fsx_filesystem_arn: The Amazon Resource Name (ARN) for the FSx for Windows file system.
        :param pulumi.Input[builtins.str] password: The password of the user who has the permissions to access files and folders in the FSx for Windows file system.
        :param pulumi.Input[builtins.str] subdirectory: A subdirectory in the location's path.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        pulumi.set(__self__, "security_group_arns", security_group_arns)
        pulumi.set(__self__, "user", user)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if fsx_filesystem_arn is not None:
            pulumi.set(__self__, "fsx_filesystem_arn", fsx_filesystem_arn)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if subdirectory is not None:
            pulumi.set(__self__, "subdirectory", subdirectory)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="securityGroupArns")
    def security_group_arns(self) -> pulumi.Input[Sequence[pulumi.Input[builtins.str]]]:
        """
        The ARNs of the security groups that are to use to configure the FSx for Windows file system.
        """
        return pulumi.get(self, "security_group_arns")

    @security_group_arns.setter
    def security_group_arns(self, value: pulumi.Input[Sequence[pulumi.Input[builtins.str]]]):
        pulumi.set(self, "security_group_arns", value)

    @property
    @pulumi.getter
    def user(self) -> pulumi.Input[builtins.str]:
        """
        The user who has the permissions to access files and folders in the FSx for Windows file system.
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "user", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the Windows domain that the FSx for Windows server belongs to.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter(name="fsxFilesystemArn")
    def fsx_filesystem_arn(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The Amazon Resource Name (ARN) for the FSx for Windows file system.
        """
        return pulumi.get(self, "fsx_filesystem_arn")

    @fsx_filesystem_arn.setter
    def fsx_filesystem_arn(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "fsx_filesystem_arn", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The password of the user who has the permissions to access files and folders in the FSx for Windows file system.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def subdirectory(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        A subdirectory in the location's path.
        """
        return pulumi.get(self, "subdirectory")

    @subdirectory.setter
    def subdirectory(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "subdirectory", value)

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


@pulumi.type_token("aws-native:datasync:LocationFSxWindows")
class LocationFSxWindows(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain: Optional[pulumi.Input[builtins.str]] = None,
                 fsx_filesystem_arn: Optional[pulumi.Input[builtins.str]] = None,
                 password: Optional[pulumi.Input[builtins.str]] = None,
                 security_group_arns: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 subdirectory: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 user: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        Resource schema for AWS::DataSync::LocationFSxWindows.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] domain: The name of the Windows domain that the FSx for Windows server belongs to.
        :param pulumi.Input[builtins.str] fsx_filesystem_arn: The Amazon Resource Name (ARN) for the FSx for Windows file system.
        :param pulumi.Input[builtins.str] password: The password of the user who has the permissions to access files and folders in the FSx for Windows file system.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] security_group_arns: The ARNs of the security groups that are to use to configure the FSx for Windows file system.
        :param pulumi.Input[builtins.str] subdirectory: A subdirectory in the location's path.
        :param pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]] tags: An array of key-value pairs to apply to this resource.
        :param pulumi.Input[builtins.str] user: The user who has the permissions to access files and folders in the FSx for Windows file system.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LocationFSxWindowsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::DataSync::LocationFSxWindows.

        :param str resource_name: The name of the resource.
        :param LocationFSxWindowsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LocationFSxWindowsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain: Optional[pulumi.Input[builtins.str]] = None,
                 fsx_filesystem_arn: Optional[pulumi.Input[builtins.str]] = None,
                 password: Optional[pulumi.Input[builtins.str]] = None,
                 security_group_arns: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 subdirectory: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 user: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LocationFSxWindowsArgs.__new__(LocationFSxWindowsArgs)

            __props__.__dict__["domain"] = domain
            __props__.__dict__["fsx_filesystem_arn"] = fsx_filesystem_arn
            __props__.__dict__["password"] = password
            if security_group_arns is None and not opts.urn:
                raise TypeError("Missing required property 'security_group_arns'")
            __props__.__dict__["security_group_arns"] = security_group_arns
            __props__.__dict__["subdirectory"] = subdirectory
            __props__.__dict__["tags"] = tags
            if user is None and not opts.urn:
                raise TypeError("Missing required property 'user'")
            __props__.__dict__["user"] = user
            __props__.__dict__["location_arn"] = None
            __props__.__dict__["location_uri"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["fsxFilesystemArn", "securityGroupArns[*]"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(LocationFSxWindows, __self__).__init__(
            'aws-native:datasync:LocationFSxWindows',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LocationFSxWindows':
        """
        Get an existing LocationFSxWindows resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LocationFSxWindowsArgs.__new__(LocationFSxWindowsArgs)

        __props__.__dict__["domain"] = None
        __props__.__dict__["fsx_filesystem_arn"] = None
        __props__.__dict__["location_arn"] = None
        __props__.__dict__["location_uri"] = None
        __props__.__dict__["password"] = None
        __props__.__dict__["security_group_arns"] = None
        __props__.__dict__["subdirectory"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["user"] = None
        return LocationFSxWindows(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The name of the Windows domain that the FSx for Windows server belongs to.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="fsxFilesystemArn")
    def fsx_filesystem_arn(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The Amazon Resource Name (ARN) for the FSx for Windows file system.
        """
        return pulumi.get(self, "fsx_filesystem_arn")

    @property
    @pulumi.getter(name="locationArn")
    def location_arn(self) -> pulumi.Output[builtins.str]:
        """
        The Amazon Resource Name (ARN) of the Amazon FSx for Windows file system location that is created.
        """
        return pulumi.get(self, "location_arn")

    @property
    @pulumi.getter(name="locationUri")
    def location_uri(self) -> pulumi.Output[builtins.str]:
        """
        The URL of the FSx for Windows location that was described.
        """
        return pulumi.get(self, "location_uri")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The password of the user who has the permissions to access files and folders in the FSx for Windows file system.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="securityGroupArns")
    def security_group_arns(self) -> pulumi.Output[Sequence[builtins.str]]:
        """
        The ARNs of the security groups that are to use to configure the FSx for Windows file system.
        """
        return pulumi.get(self, "security_group_arns")

    @property
    @pulumi.getter
    def subdirectory(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        A subdirectory in the location's path.
        """
        return pulumi.get(self, "subdirectory")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def user(self) -> pulumi.Output[builtins.str]:
        """
        The user who has the permissions to access files and folders in the FSx for Windows file system.
        """
        return pulumi.get(self, "user")

