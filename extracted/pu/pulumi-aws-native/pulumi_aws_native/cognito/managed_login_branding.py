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

__all__ = ['ManagedLoginBrandingArgs', 'ManagedLoginBranding']

@pulumi.input_type
class ManagedLoginBrandingArgs:
    def __init__(__self__, *,
                 user_pool_id: pulumi.Input[builtins.str],
                 assets: Optional[pulumi.Input[Sequence[pulumi.Input['ManagedLoginBrandingAssetTypeArgs']]]] = None,
                 client_id: Optional[pulumi.Input[builtins.str]] = None,
                 return_merged_resources: Optional[pulumi.Input[builtins.bool]] = None,
                 settings: Optional[Any] = None,
                 use_cognito_provided_values: Optional[pulumi.Input[builtins.bool]] = None):
        """
        The set of arguments for constructing a ManagedLoginBranding resource.
        :param pulumi.Input[builtins.str] user_pool_id: The user pool where the branding style is assigned.
        :param pulumi.Input[Sequence[pulumi.Input['ManagedLoginBrandingAssetTypeArgs']]] assets: An array of image files that you want to apply to roles like backgrounds, logos, and icons. Each object must also indicate whether it is for dark mode, light mode, or browser-adaptive mode.
        :param pulumi.Input[builtins.str] client_id: The app client that you want to assign the branding style to. Each style is linked to an app client until you delete it.
        :param pulumi.Input[builtins.bool] return_merged_resources: When `true` , returns values for branding options that are unchanged from Amazon Cognito defaults. When `false` or when you omit this parameter, returns only values that you customized in your branding style.
        :param Any settings: A JSON file, encoded as a `Document` type, with the the settings that you want to apply to your style.
               
               Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Cognito::ManagedLoginBranding` for more information about the expected schema for this property.
        :param pulumi.Input[builtins.bool] use_cognito_provided_values: When true, applies the default branding style options. This option reverts to default style options that are managed by Amazon Cognito. You can modify them later in the branding editor.
               
               When you specify `true` for this option, you must also omit values for `Settings` and `Assets` in the request.
        """
        pulumi.set(__self__, "user_pool_id", user_pool_id)
        if assets is not None:
            pulumi.set(__self__, "assets", assets)
        if client_id is not None:
            pulumi.set(__self__, "client_id", client_id)
        if return_merged_resources is not None:
            pulumi.set(__self__, "return_merged_resources", return_merged_resources)
        if settings is not None:
            pulumi.set(__self__, "settings", settings)
        if use_cognito_provided_values is not None:
            pulumi.set(__self__, "use_cognito_provided_values", use_cognito_provided_values)

    @property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> pulumi.Input[builtins.str]:
        """
        The user pool where the branding style is assigned.
        """
        return pulumi.get(self, "user_pool_id")

    @user_pool_id.setter
    def user_pool_id(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "user_pool_id", value)

    @property
    @pulumi.getter
    def assets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ManagedLoginBrandingAssetTypeArgs']]]]:
        """
        An array of image files that you want to apply to roles like backgrounds, logos, and icons. Each object must also indicate whether it is for dark mode, light mode, or browser-adaptive mode.
        """
        return pulumi.get(self, "assets")

    @assets.setter
    def assets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ManagedLoginBrandingAssetTypeArgs']]]]):
        pulumi.set(self, "assets", value)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The app client that you want to assign the branding style to. Each style is linked to an app client until you delete it.
        """
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="returnMergedResources")
    def return_merged_resources(self) -> Optional[pulumi.Input[builtins.bool]]:
        """
        When `true` , returns values for branding options that are unchanged from Amazon Cognito defaults. When `false` or when you omit this parameter, returns only values that you customized in your branding style.
        """
        return pulumi.get(self, "return_merged_resources")

    @return_merged_resources.setter
    def return_merged_resources(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "return_merged_resources", value)

    @property
    @pulumi.getter
    def settings(self) -> Optional[Any]:
        """
        A JSON file, encoded as a `Document` type, with the the settings that you want to apply to your style.

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Cognito::ManagedLoginBranding` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "settings")

    @settings.setter
    def settings(self, value: Optional[Any]):
        pulumi.set(self, "settings", value)

    @property
    @pulumi.getter(name="useCognitoProvidedValues")
    def use_cognito_provided_values(self) -> Optional[pulumi.Input[builtins.bool]]:
        """
        When true, applies the default branding style options. This option reverts to default style options that are managed by Amazon Cognito. You can modify them later in the branding editor.

        When you specify `true` for this option, you must also omit values for `Settings` and `Assets` in the request.
        """
        return pulumi.get(self, "use_cognito_provided_values")

    @use_cognito_provided_values.setter
    def use_cognito_provided_values(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "use_cognito_provided_values", value)


@pulumi.type_token("aws-native:cognito:ManagedLoginBranding")
class ManagedLoginBranding(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assets: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ManagedLoginBrandingAssetTypeArgs', 'ManagedLoginBrandingAssetTypeArgsDict']]]]] = None,
                 client_id: Optional[pulumi.Input[builtins.str]] = None,
                 return_merged_resources: Optional[pulumi.Input[builtins.bool]] = None,
                 settings: Optional[Any] = None,
                 use_cognito_provided_values: Optional[pulumi.Input[builtins.bool]] = None,
                 user_pool_id: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Cognito::ManagedLoginBranding

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ManagedLoginBrandingAssetTypeArgs', 'ManagedLoginBrandingAssetTypeArgsDict']]]] assets: An array of image files that you want to apply to roles like backgrounds, logos, and icons. Each object must also indicate whether it is for dark mode, light mode, or browser-adaptive mode.
        :param pulumi.Input[builtins.str] client_id: The app client that you want to assign the branding style to. Each style is linked to an app client until you delete it.
        :param pulumi.Input[builtins.bool] return_merged_resources: When `true` , returns values for branding options that are unchanged from Amazon Cognito defaults. When `false` or when you omit this parameter, returns only values that you customized in your branding style.
        :param Any settings: A JSON file, encoded as a `Document` type, with the the settings that you want to apply to your style.
               
               Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Cognito::ManagedLoginBranding` for more information about the expected schema for this property.
        :param pulumi.Input[builtins.bool] use_cognito_provided_values: When true, applies the default branding style options. This option reverts to default style options that are managed by Amazon Cognito. You can modify them later in the branding editor.
               
               When you specify `true` for this option, you must also omit values for `Settings` and `Assets` in the request.
        :param pulumi.Input[builtins.str] user_pool_id: The user pool where the branding style is assigned.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ManagedLoginBrandingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Cognito::ManagedLoginBranding

        :param str resource_name: The name of the resource.
        :param ManagedLoginBrandingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagedLoginBrandingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assets: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ManagedLoginBrandingAssetTypeArgs', 'ManagedLoginBrandingAssetTypeArgsDict']]]]] = None,
                 client_id: Optional[pulumi.Input[builtins.str]] = None,
                 return_merged_resources: Optional[pulumi.Input[builtins.bool]] = None,
                 settings: Optional[Any] = None,
                 use_cognito_provided_values: Optional[pulumi.Input[builtins.bool]] = None,
                 user_pool_id: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ManagedLoginBrandingArgs.__new__(ManagedLoginBrandingArgs)

            __props__.__dict__["assets"] = assets
            __props__.__dict__["client_id"] = client_id
            __props__.__dict__["return_merged_resources"] = return_merged_resources
            __props__.__dict__["settings"] = settings
            __props__.__dict__["use_cognito_provided_values"] = use_cognito_provided_values
            if user_pool_id is None and not opts.urn:
                raise TypeError("Missing required property 'user_pool_id'")
            __props__.__dict__["user_pool_id"] = user_pool_id
            __props__.__dict__["managed_login_branding_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["clientId", "userPoolId"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ManagedLoginBranding, __self__).__init__(
            'aws-native:cognito:ManagedLoginBranding',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ManagedLoginBranding':
        """
        Get an existing ManagedLoginBranding resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ManagedLoginBrandingArgs.__new__(ManagedLoginBrandingArgs)

        __props__.__dict__["assets"] = None
        __props__.__dict__["client_id"] = None
        __props__.__dict__["managed_login_branding_id"] = None
        __props__.__dict__["return_merged_resources"] = None
        __props__.__dict__["settings"] = None
        __props__.__dict__["use_cognito_provided_values"] = None
        __props__.__dict__["user_pool_id"] = None
        return ManagedLoginBranding(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def assets(self) -> pulumi.Output[Optional[Sequence['outputs.ManagedLoginBrandingAssetType']]]:
        """
        An array of image files that you want to apply to roles like backgrounds, logos, and icons. Each object must also indicate whether it is for dark mode, light mode, or browser-adaptive mode.
        """
        return pulumi.get(self, "assets")

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The app client that you want to assign the branding style to. Each style is linked to an app client until you delete it.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="managedLoginBrandingId")
    def managed_login_branding_id(self) -> pulumi.Output[builtins.str]:
        """
        The ID of the managed login branding style.
        """
        return pulumi.get(self, "managed_login_branding_id")

    @property
    @pulumi.getter(name="returnMergedResources")
    def return_merged_resources(self) -> pulumi.Output[Optional[builtins.bool]]:
        """
        When `true` , returns values for branding options that are unchanged from Amazon Cognito defaults. When `false` or when you omit this parameter, returns only values that you customized in your branding style.
        """
        return pulumi.get(self, "return_merged_resources")

    @property
    @pulumi.getter
    def settings(self) -> pulumi.Output[Optional[Any]]:
        """
        A JSON file, encoded as a `Document` type, with the the settings that you want to apply to your style.

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Cognito::ManagedLoginBranding` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "settings")

    @property
    @pulumi.getter(name="useCognitoProvidedValues")
    def use_cognito_provided_values(self) -> pulumi.Output[Optional[builtins.bool]]:
        """
        When true, applies the default branding style options. This option reverts to default style options that are managed by Amazon Cognito. You can modify them later in the branding editor.

        When you specify `true` for this option, you must also omit values for `Settings` and `Assets` in the request.
        """
        return pulumi.get(self, "use_cognito_provided_values")

    @property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> pulumi.Output[builtins.str]:
        """
        The user pool where the branding style is assigned.
        """
        return pulumi.get(self, "user_pool_id")

