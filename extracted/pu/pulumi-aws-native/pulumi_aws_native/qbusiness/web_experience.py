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

__all__ = ['WebExperienceArgs', 'WebExperience']

@pulumi.input_type
class WebExperienceArgs:
    def __init__(__self__, *,
                 application_id: pulumi.Input[builtins.str],
                 browser_extension_configuration: Optional[pulumi.Input['WebExperienceBrowserExtensionConfigurationArgs']] = None,
                 customization_configuration: Optional[pulumi.Input['WebExperienceCustomizationConfigurationArgs']] = None,
                 identity_provider_configuration: Optional[pulumi.Input[Union['WebExperienceIdentityProviderConfiguration0PropertiesArgs', 'WebExperienceIdentityProviderConfiguration1PropertiesArgs']]] = None,
                 origins: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 role_arn: Optional[pulumi.Input[builtins.str]] = None,
                 sample_prompts_control_mode: Optional[pulumi.Input['WebExperienceSamplePromptsControlMode']] = None,
                 subtitle: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None,
                 title: Optional[pulumi.Input[builtins.str]] = None,
                 welcome_message: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a WebExperience resource.
        :param pulumi.Input[builtins.str] application_id: The identifier of the Amazon Q Business web experience.
        :param pulumi.Input['WebExperienceBrowserExtensionConfigurationArgs'] browser_extension_configuration: The container for browser extension configuration for an Amazon Q Business web experience.
        :param pulumi.Input['WebExperienceCustomizationConfigurationArgs'] customization_configuration: Contains the configuration information to customize the logo, font, and color of an Amazon Q Business web experience with individual files for each property or a CSS file for them all.
        :param pulumi.Input[Union['WebExperienceIdentityProviderConfiguration0PropertiesArgs', 'WebExperienceIdentityProviderConfiguration1PropertiesArgs']] identity_provider_configuration: Provides information about the identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] origins: Sets the website domain origins that are allowed to embed the Amazon Q Business web experience. The *domain origin* refers to the base URL for accessing a website including the protocol ( `http/https` ), the domain name, and the port number (if specified).
               
               > You must only submit a *base URL* and not a full path. For example, `https://docs.aws.amazon.com` .
        :param pulumi.Input[builtins.str] role_arn: The Amazon Resource Name (ARN) of the service role attached to your web experience.
               
               > You must provide this value if you're using IAM Identity Center to manage end user access to your application. If you're using legacy identity management to manage user access, you don't need to provide this value.
        :param pulumi.Input['WebExperienceSamplePromptsControlMode'] sample_prompts_control_mode: Determines whether sample prompts are enabled in the web experience for an end user.
        :param pulumi.Input[builtins.str] subtitle: A subtitle to personalize your Amazon Q Business web experience.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: A list of key-value pairs that identify or categorize your Amazon Q Business web experience. You can also use tags to help control access to the web experience. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.
        :param pulumi.Input[builtins.str] title: The title for your Amazon Q Business web experience.
        :param pulumi.Input[builtins.str] welcome_message: A message in an Amazon Q Business web experience.
        """
        pulumi.set(__self__, "application_id", application_id)
        if browser_extension_configuration is not None:
            pulumi.set(__self__, "browser_extension_configuration", browser_extension_configuration)
        if customization_configuration is not None:
            pulumi.set(__self__, "customization_configuration", customization_configuration)
        if identity_provider_configuration is not None:
            pulumi.set(__self__, "identity_provider_configuration", identity_provider_configuration)
        if origins is not None:
            pulumi.set(__self__, "origins", origins)
        if role_arn is not None:
            pulumi.set(__self__, "role_arn", role_arn)
        if sample_prompts_control_mode is not None:
            pulumi.set(__self__, "sample_prompts_control_mode", sample_prompts_control_mode)
        if subtitle is not None:
            pulumi.set(__self__, "subtitle", subtitle)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if title is not None:
            pulumi.set(__self__, "title", title)
        if welcome_message is not None:
            pulumi.set(__self__, "welcome_message", welcome_message)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Input[builtins.str]:
        """
        The identifier of the Amazon Q Business web experience.
        """
        return pulumi.get(self, "application_id")

    @application_id.setter
    def application_id(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "application_id", value)

    @property
    @pulumi.getter(name="browserExtensionConfiguration")
    def browser_extension_configuration(self) -> Optional[pulumi.Input['WebExperienceBrowserExtensionConfigurationArgs']]:
        """
        The container for browser extension configuration for an Amazon Q Business web experience.
        """
        return pulumi.get(self, "browser_extension_configuration")

    @browser_extension_configuration.setter
    def browser_extension_configuration(self, value: Optional[pulumi.Input['WebExperienceBrowserExtensionConfigurationArgs']]):
        pulumi.set(self, "browser_extension_configuration", value)

    @property
    @pulumi.getter(name="customizationConfiguration")
    def customization_configuration(self) -> Optional[pulumi.Input['WebExperienceCustomizationConfigurationArgs']]:
        """
        Contains the configuration information to customize the logo, font, and color of an Amazon Q Business web experience with individual files for each property or a CSS file for them all.
        """
        return pulumi.get(self, "customization_configuration")

    @customization_configuration.setter
    def customization_configuration(self, value: Optional[pulumi.Input['WebExperienceCustomizationConfigurationArgs']]):
        pulumi.set(self, "customization_configuration", value)

    @property
    @pulumi.getter(name="identityProviderConfiguration")
    def identity_provider_configuration(self) -> Optional[pulumi.Input[Union['WebExperienceIdentityProviderConfiguration0PropertiesArgs', 'WebExperienceIdentityProviderConfiguration1PropertiesArgs']]]:
        """
        Provides information about the identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.
        """
        return pulumi.get(self, "identity_provider_configuration")

    @identity_provider_configuration.setter
    def identity_provider_configuration(self, value: Optional[pulumi.Input[Union['WebExperienceIdentityProviderConfiguration0PropertiesArgs', 'WebExperienceIdentityProviderConfiguration1PropertiesArgs']]]):
        pulumi.set(self, "identity_provider_configuration", value)

    @property
    @pulumi.getter
    def origins(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]:
        """
        Sets the website domain origins that are allowed to embed the Amazon Q Business web experience. The *domain origin* refers to the base URL for accessing a website including the protocol ( `http/https` ), the domain name, and the port number (if specified).

        > You must only submit a *base URL* and not a full path. For example, `https://docs.aws.amazon.com` .
        """
        return pulumi.get(self, "origins")

    @origins.setter
    def origins(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "origins", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The Amazon Resource Name (ARN) of the service role attached to your web experience.

        > You must provide this value if you're using IAM Identity Center to manage end user access to your application. If you're using legacy identity management to manage user access, you don't need to provide this value.
        """
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter(name="samplePromptsControlMode")
    def sample_prompts_control_mode(self) -> Optional[pulumi.Input['WebExperienceSamplePromptsControlMode']]:
        """
        Determines whether sample prompts are enabled in the web experience for an end user.
        """
        return pulumi.get(self, "sample_prompts_control_mode")

    @sample_prompts_control_mode.setter
    def sample_prompts_control_mode(self, value: Optional[pulumi.Input['WebExperienceSamplePromptsControlMode']]):
        pulumi.set(self, "sample_prompts_control_mode", value)

    @property
    @pulumi.getter
    def subtitle(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        A subtitle to personalize your Amazon Q Business web experience.
        """
        return pulumi.get(self, "subtitle")

    @subtitle.setter
    def subtitle(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "subtitle", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        A list of key-value pairs that identify or categorize your Amazon Q Business web experience. You can also use tags to help control access to the web experience. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The title for your Amazon Q Business web experience.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter(name="welcomeMessage")
    def welcome_message(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        A message in an Amazon Q Business web experience.
        """
        return pulumi.get(self, "welcome_message")

    @welcome_message.setter
    def welcome_message(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "welcome_message", value)


@pulumi.type_token("aws-native:qbusiness:WebExperience")
class WebExperience(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_id: Optional[pulumi.Input[builtins.str]] = None,
                 browser_extension_configuration: Optional[pulumi.Input[Union['WebExperienceBrowserExtensionConfigurationArgs', 'WebExperienceBrowserExtensionConfigurationArgsDict']]] = None,
                 customization_configuration: Optional[pulumi.Input[Union['WebExperienceCustomizationConfigurationArgs', 'WebExperienceCustomizationConfigurationArgsDict']]] = None,
                 identity_provider_configuration: Optional[pulumi.Input[Union[Union['WebExperienceIdentityProviderConfiguration0PropertiesArgs', 'WebExperienceIdentityProviderConfiguration0PropertiesArgsDict'], Union['WebExperienceIdentityProviderConfiguration1PropertiesArgs', 'WebExperienceIdentityProviderConfiguration1PropertiesArgsDict']]]] = None,
                 origins: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 role_arn: Optional[pulumi.Input[builtins.str]] = None,
                 sample_prompts_control_mode: Optional[pulumi.Input['WebExperienceSamplePromptsControlMode']] = None,
                 subtitle: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 title: Optional[pulumi.Input[builtins.str]] = None,
                 welcome_message: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        Definition of AWS::QBusiness::WebExperience Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] application_id: The identifier of the Amazon Q Business web experience.
        :param pulumi.Input[Union['WebExperienceBrowserExtensionConfigurationArgs', 'WebExperienceBrowserExtensionConfigurationArgsDict']] browser_extension_configuration: The container for browser extension configuration for an Amazon Q Business web experience.
        :param pulumi.Input[Union['WebExperienceCustomizationConfigurationArgs', 'WebExperienceCustomizationConfigurationArgsDict']] customization_configuration: Contains the configuration information to customize the logo, font, and color of an Amazon Q Business web experience with individual files for each property or a CSS file for them all.
        :param pulumi.Input[Union[Union['WebExperienceIdentityProviderConfiguration0PropertiesArgs', 'WebExperienceIdentityProviderConfiguration0PropertiesArgsDict'], Union['WebExperienceIdentityProviderConfiguration1PropertiesArgs', 'WebExperienceIdentityProviderConfiguration1PropertiesArgsDict']]] identity_provider_configuration: Provides information about the identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] origins: Sets the website domain origins that are allowed to embed the Amazon Q Business web experience. The *domain origin* refers to the base URL for accessing a website including the protocol ( `http/https` ), the domain name, and the port number (if specified).
               
               > You must only submit a *base URL* and not a full path. For example, `https://docs.aws.amazon.com` .
        :param pulumi.Input[builtins.str] role_arn: The Amazon Resource Name (ARN) of the service role attached to your web experience.
               
               > You must provide this value if you're using IAM Identity Center to manage end user access to your application. If you're using legacy identity management to manage user access, you don't need to provide this value.
        :param pulumi.Input['WebExperienceSamplePromptsControlMode'] sample_prompts_control_mode: Determines whether sample prompts are enabled in the web experience for an end user.
        :param pulumi.Input[builtins.str] subtitle: A subtitle to personalize your Amazon Q Business web experience.
        :param pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]] tags: A list of key-value pairs that identify or categorize your Amazon Q Business web experience. You can also use tags to help control access to the web experience. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.
        :param pulumi.Input[builtins.str] title: The title for your Amazon Q Business web experience.
        :param pulumi.Input[builtins.str] welcome_message: A message in an Amazon Q Business web experience.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WebExperienceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::QBusiness::WebExperience Resource Type

        :param str resource_name: The name of the resource.
        :param WebExperienceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WebExperienceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_id: Optional[pulumi.Input[builtins.str]] = None,
                 browser_extension_configuration: Optional[pulumi.Input[Union['WebExperienceBrowserExtensionConfigurationArgs', 'WebExperienceBrowserExtensionConfigurationArgsDict']]] = None,
                 customization_configuration: Optional[pulumi.Input[Union['WebExperienceCustomizationConfigurationArgs', 'WebExperienceCustomizationConfigurationArgsDict']]] = None,
                 identity_provider_configuration: Optional[pulumi.Input[Union[Union['WebExperienceIdentityProviderConfiguration0PropertiesArgs', 'WebExperienceIdentityProviderConfiguration0PropertiesArgsDict'], Union['WebExperienceIdentityProviderConfiguration1PropertiesArgs', 'WebExperienceIdentityProviderConfiguration1PropertiesArgsDict']]]] = None,
                 origins: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 role_arn: Optional[pulumi.Input[builtins.str]] = None,
                 sample_prompts_control_mode: Optional[pulumi.Input['WebExperienceSamplePromptsControlMode']] = None,
                 subtitle: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 title: Optional[pulumi.Input[builtins.str]] = None,
                 welcome_message: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WebExperienceArgs.__new__(WebExperienceArgs)

            if application_id is None and not opts.urn:
                raise TypeError("Missing required property 'application_id'")
            __props__.__dict__["application_id"] = application_id
            __props__.__dict__["browser_extension_configuration"] = browser_extension_configuration
            __props__.__dict__["customization_configuration"] = customization_configuration
            __props__.__dict__["identity_provider_configuration"] = identity_provider_configuration
            __props__.__dict__["origins"] = origins
            __props__.__dict__["role_arn"] = role_arn
            __props__.__dict__["sample_prompts_control_mode"] = sample_prompts_control_mode
            __props__.__dict__["subtitle"] = subtitle
            __props__.__dict__["tags"] = tags
            __props__.__dict__["title"] = title
            __props__.__dict__["welcome_message"] = welcome_message
            __props__.__dict__["created_at"] = None
            __props__.__dict__["default_endpoint"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["updated_at"] = None
            __props__.__dict__["web_experience_arn"] = None
            __props__.__dict__["web_experience_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["applicationId"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(WebExperience, __self__).__init__(
            'aws-native:qbusiness:WebExperience',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WebExperience':
        """
        Get an existing WebExperience resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WebExperienceArgs.__new__(WebExperienceArgs)

        __props__.__dict__["application_id"] = None
        __props__.__dict__["browser_extension_configuration"] = None
        __props__.__dict__["created_at"] = None
        __props__.__dict__["customization_configuration"] = None
        __props__.__dict__["default_endpoint"] = None
        __props__.__dict__["identity_provider_configuration"] = None
        __props__.__dict__["origins"] = None
        __props__.__dict__["role_arn"] = None
        __props__.__dict__["sample_prompts_control_mode"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["subtitle"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["title"] = None
        __props__.__dict__["updated_at"] = None
        __props__.__dict__["web_experience_arn"] = None
        __props__.__dict__["web_experience_id"] = None
        __props__.__dict__["welcome_message"] = None
        return WebExperience(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[builtins.str]:
        """
        The identifier of the Amazon Q Business web experience.
        """
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter(name="browserExtensionConfiguration")
    def browser_extension_configuration(self) -> pulumi.Output[Optional['outputs.WebExperienceBrowserExtensionConfiguration']]:
        """
        The container for browser extension configuration for an Amazon Q Business web experience.
        """
        return pulumi.get(self, "browser_extension_configuration")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[builtins.str]:
        """
        The Unix timestamp when the Amazon Q Business application was last updated.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="customizationConfiguration")
    def customization_configuration(self) -> pulumi.Output[Optional['outputs.WebExperienceCustomizationConfiguration']]:
        """
        Contains the configuration information to customize the logo, font, and color of an Amazon Q Business web experience with individual files for each property or a CSS file for them all.
        """
        return pulumi.get(self, "customization_configuration")

    @property
    @pulumi.getter(name="defaultEndpoint")
    def default_endpoint(self) -> pulumi.Output[builtins.str]:
        """
        The endpoint URLs for your Amazon Q Business web experience. The URLs are unique and fully hosted by AWS .
        """
        return pulumi.get(self, "default_endpoint")

    @property
    @pulumi.getter(name="identityProviderConfiguration")
    def identity_provider_configuration(self) -> pulumi.Output[Optional[Any]]:
        """
        Provides information about the identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.
        """
        return pulumi.get(self, "identity_provider_configuration")

    @property
    @pulumi.getter
    def origins(self) -> pulumi.Output[Optional[Sequence[builtins.str]]]:
        """
        Sets the website domain origins that are allowed to embed the Amazon Q Business web experience. The *domain origin* refers to the base URL for accessing a website including the protocol ( `http/https` ), the domain name, and the port number (if specified).

        > You must only submit a *base URL* and not a full path. For example, `https://docs.aws.amazon.com` .
        """
        return pulumi.get(self, "origins")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The Amazon Resource Name (ARN) of the service role attached to your web experience.

        > You must provide this value if you're using IAM Identity Center to manage end user access to your application. If you're using legacy identity management to manage user access, you don't need to provide this value.
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter(name="samplePromptsControlMode")
    def sample_prompts_control_mode(self) -> pulumi.Output[Optional['WebExperienceSamplePromptsControlMode']]:
        """
        Determines whether sample prompts are enabled in the web experience for an end user.
        """
        return pulumi.get(self, "sample_prompts_control_mode")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['WebExperienceStatus']:
        """
        The status of your Amazon Q Business web experience.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def subtitle(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        A subtitle to personalize your Amazon Q Business web experience.
        """
        return pulumi.get(self, "subtitle")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        A list of key-value pairs that identify or categorize your Amazon Q Business web experience. You can also use tags to help control access to the web experience. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The title for your Amazon Q Business web experience.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[builtins.str]:
        """
        The Unix timestamp when your Amazon Q Business web experience was updated.
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter(name="webExperienceArn")
    def web_experience_arn(self) -> pulumi.Output[builtins.str]:
        """
        The Amazon Resource Name (ARN) of an Amazon Q Business web experience.
        """
        return pulumi.get(self, "web_experience_arn")

    @property
    @pulumi.getter(name="webExperienceId")
    def web_experience_id(self) -> pulumi.Output[builtins.str]:
        """
        The identifier of your Amazon Q Business web experience.
        """
        return pulumi.get(self, "web_experience_id")

    @property
    @pulumi.getter(name="welcomeMessage")
    def welcome_message(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        A message in an Amazon Q Business web experience.
        """
        return pulumi.get(self, "welcome_message")

