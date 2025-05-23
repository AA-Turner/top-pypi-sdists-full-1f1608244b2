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
from .. import outputs as _root_outputs
from ._enums import *

__all__ = [
    'GetWebExperienceResult',
    'AwaitableGetWebExperienceResult',
    'get_web_experience',
    'get_web_experience_output',
]

@pulumi.output_type
class GetWebExperienceResult:
    def __init__(__self__, browser_extension_configuration=None, created_at=None, customization_configuration=None, default_endpoint=None, identity_provider_configuration=None, origins=None, role_arn=None, sample_prompts_control_mode=None, status=None, subtitle=None, tags=None, title=None, updated_at=None, web_experience_arn=None, web_experience_id=None, welcome_message=None):
        if browser_extension_configuration and not isinstance(browser_extension_configuration, dict):
            raise TypeError("Expected argument 'browser_extension_configuration' to be a dict")
        pulumi.set(__self__, "browser_extension_configuration", browser_extension_configuration)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if customization_configuration and not isinstance(customization_configuration, dict):
            raise TypeError("Expected argument 'customization_configuration' to be a dict")
        pulumi.set(__self__, "customization_configuration", customization_configuration)
        if default_endpoint and not isinstance(default_endpoint, str):
            raise TypeError("Expected argument 'default_endpoint' to be a str")
        pulumi.set(__self__, "default_endpoint", default_endpoint)
        if identity_provider_configuration and not isinstance(identity_provider_configuration, dict):
            raise TypeError("Expected argument 'identity_provider_configuration' to be a dict")
        pulumi.set(__self__, "identity_provider_configuration", identity_provider_configuration)
        if origins and not isinstance(origins, list):
            raise TypeError("Expected argument 'origins' to be a list")
        pulumi.set(__self__, "origins", origins)
        if role_arn and not isinstance(role_arn, str):
            raise TypeError("Expected argument 'role_arn' to be a str")
        pulumi.set(__self__, "role_arn", role_arn)
        if sample_prompts_control_mode and not isinstance(sample_prompts_control_mode, str):
            raise TypeError("Expected argument 'sample_prompts_control_mode' to be a str")
        pulumi.set(__self__, "sample_prompts_control_mode", sample_prompts_control_mode)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if subtitle and not isinstance(subtitle, str):
            raise TypeError("Expected argument 'subtitle' to be a str")
        pulumi.set(__self__, "subtitle", subtitle)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if title and not isinstance(title, str):
            raise TypeError("Expected argument 'title' to be a str")
        pulumi.set(__self__, "title", title)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)
        if web_experience_arn and not isinstance(web_experience_arn, str):
            raise TypeError("Expected argument 'web_experience_arn' to be a str")
        pulumi.set(__self__, "web_experience_arn", web_experience_arn)
        if web_experience_id and not isinstance(web_experience_id, str):
            raise TypeError("Expected argument 'web_experience_id' to be a str")
        pulumi.set(__self__, "web_experience_id", web_experience_id)
        if welcome_message and not isinstance(welcome_message, str):
            raise TypeError("Expected argument 'welcome_message' to be a str")
        pulumi.set(__self__, "welcome_message", welcome_message)

    @property
    @pulumi.getter(name="browserExtensionConfiguration")
    def browser_extension_configuration(self) -> Optional['outputs.WebExperienceBrowserExtensionConfiguration']:
        """
        The container for browser extension configuration for an Amazon Q Business web experience.
        """
        return pulumi.get(self, "browser_extension_configuration")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[builtins.str]:
        """
        The Unix timestamp when the Amazon Q Business application was last updated.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="customizationConfiguration")
    def customization_configuration(self) -> Optional['outputs.WebExperienceCustomizationConfiguration']:
        """
        Contains the configuration information to customize the logo, font, and color of an Amazon Q Business web experience with individual files for each property or a CSS file for them all.
        """
        return pulumi.get(self, "customization_configuration")

    @property
    @pulumi.getter(name="defaultEndpoint")
    def default_endpoint(self) -> Optional[builtins.str]:
        """
        The endpoint URLs for your Amazon Q Business web experience. The URLs are unique and fully hosted by AWS .
        """
        return pulumi.get(self, "default_endpoint")

    @property
    @pulumi.getter(name="identityProviderConfiguration")
    def identity_provider_configuration(self) -> Optional[Any]:
        """
        Provides information about the identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.
        """
        return pulumi.get(self, "identity_provider_configuration")

    @property
    @pulumi.getter
    def origins(self) -> Optional[Sequence[builtins.str]]:
        """
        Sets the website domain origins that are allowed to embed the Amazon Q Business web experience. The *domain origin* refers to the base URL for accessing a website including the protocol ( `http/https` ), the domain name, and the port number (if specified).

        > You must only submit a *base URL* and not a full path. For example, `https://docs.aws.amazon.com` .
        """
        return pulumi.get(self, "origins")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[builtins.str]:
        """
        The Amazon Resource Name (ARN) of the service role attached to your web experience.

        > You must provide this value if you're using IAM Identity Center to manage end user access to your application. If you're using legacy identity management to manage user access, you don't need to provide this value.
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter(name="samplePromptsControlMode")
    def sample_prompts_control_mode(self) -> Optional['WebExperienceSamplePromptsControlMode']:
        """
        Determines whether sample prompts are enabled in the web experience for an end user.
        """
        return pulumi.get(self, "sample_prompts_control_mode")

    @property
    @pulumi.getter
    def status(self) -> Optional['WebExperienceStatus']:
        """
        The status of your Amazon Q Business web experience.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def subtitle(self) -> Optional[builtins.str]:
        """
        A subtitle to personalize your Amazon Q Business web experience.
        """
        return pulumi.get(self, "subtitle")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        A list of key-value pairs that identify or categorize your Amazon Q Business web experience. You can also use tags to help control access to the web experience. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def title(self) -> Optional[builtins.str]:
        """
        The title for your Amazon Q Business web experience.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[builtins.str]:
        """
        The Unix timestamp when your Amazon Q Business web experience was updated.
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter(name="webExperienceArn")
    def web_experience_arn(self) -> Optional[builtins.str]:
        """
        The Amazon Resource Name (ARN) of an Amazon Q Business web experience.
        """
        return pulumi.get(self, "web_experience_arn")

    @property
    @pulumi.getter(name="webExperienceId")
    def web_experience_id(self) -> Optional[builtins.str]:
        """
        The identifier of your Amazon Q Business web experience.
        """
        return pulumi.get(self, "web_experience_id")

    @property
    @pulumi.getter(name="welcomeMessage")
    def welcome_message(self) -> Optional[builtins.str]:
        """
        A message in an Amazon Q Business web experience.
        """
        return pulumi.get(self, "welcome_message")


class AwaitableGetWebExperienceResult(GetWebExperienceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWebExperienceResult(
            browser_extension_configuration=self.browser_extension_configuration,
            created_at=self.created_at,
            customization_configuration=self.customization_configuration,
            default_endpoint=self.default_endpoint,
            identity_provider_configuration=self.identity_provider_configuration,
            origins=self.origins,
            role_arn=self.role_arn,
            sample_prompts_control_mode=self.sample_prompts_control_mode,
            status=self.status,
            subtitle=self.subtitle,
            tags=self.tags,
            title=self.title,
            updated_at=self.updated_at,
            web_experience_arn=self.web_experience_arn,
            web_experience_id=self.web_experience_id,
            welcome_message=self.welcome_message)


def get_web_experience(application_id: Optional[builtins.str] = None,
                       web_experience_id: Optional[builtins.str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWebExperienceResult:
    """
    Definition of AWS::QBusiness::WebExperience Resource Type


    :param builtins.str application_id: The identifier of the Amazon Q Business web experience.
    :param builtins.str web_experience_id: The identifier of your Amazon Q Business web experience.
    """
    __args__ = dict()
    __args__['applicationId'] = application_id
    __args__['webExperienceId'] = web_experience_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:qbusiness:getWebExperience', __args__, opts=opts, typ=GetWebExperienceResult).value

    return AwaitableGetWebExperienceResult(
        browser_extension_configuration=pulumi.get(__ret__, 'browser_extension_configuration'),
        created_at=pulumi.get(__ret__, 'created_at'),
        customization_configuration=pulumi.get(__ret__, 'customization_configuration'),
        default_endpoint=pulumi.get(__ret__, 'default_endpoint'),
        identity_provider_configuration=pulumi.get(__ret__, 'identity_provider_configuration'),
        origins=pulumi.get(__ret__, 'origins'),
        role_arn=pulumi.get(__ret__, 'role_arn'),
        sample_prompts_control_mode=pulumi.get(__ret__, 'sample_prompts_control_mode'),
        status=pulumi.get(__ret__, 'status'),
        subtitle=pulumi.get(__ret__, 'subtitle'),
        tags=pulumi.get(__ret__, 'tags'),
        title=pulumi.get(__ret__, 'title'),
        updated_at=pulumi.get(__ret__, 'updated_at'),
        web_experience_arn=pulumi.get(__ret__, 'web_experience_arn'),
        web_experience_id=pulumi.get(__ret__, 'web_experience_id'),
        welcome_message=pulumi.get(__ret__, 'welcome_message'))
def get_web_experience_output(application_id: Optional[pulumi.Input[builtins.str]] = None,
                              web_experience_id: Optional[pulumi.Input[builtins.str]] = None,
                              opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetWebExperienceResult]:
    """
    Definition of AWS::QBusiness::WebExperience Resource Type


    :param builtins.str application_id: The identifier of the Amazon Q Business web experience.
    :param builtins.str web_experience_id: The identifier of your Amazon Q Business web experience.
    """
    __args__ = dict()
    __args__['applicationId'] = application_id
    __args__['webExperienceId'] = web_experience_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:qbusiness:getWebExperience', __args__, opts=opts, typ=GetWebExperienceResult)
    return __ret__.apply(lambda __response__: GetWebExperienceResult(
        browser_extension_configuration=pulumi.get(__response__, 'browser_extension_configuration'),
        created_at=pulumi.get(__response__, 'created_at'),
        customization_configuration=pulumi.get(__response__, 'customization_configuration'),
        default_endpoint=pulumi.get(__response__, 'default_endpoint'),
        identity_provider_configuration=pulumi.get(__response__, 'identity_provider_configuration'),
        origins=pulumi.get(__response__, 'origins'),
        role_arn=pulumi.get(__response__, 'role_arn'),
        sample_prompts_control_mode=pulumi.get(__response__, 'sample_prompts_control_mode'),
        status=pulumi.get(__response__, 'status'),
        subtitle=pulumi.get(__response__, 'subtitle'),
        tags=pulumi.get(__response__, 'tags'),
        title=pulumi.get(__response__, 'title'),
        updated_at=pulumi.get(__response__, 'updated_at'),
        web_experience_arn=pulumi.get(__response__, 'web_experience_arn'),
        web_experience_id=pulumi.get(__response__, 'web_experience_id'),
        welcome_message=pulumi.get(__response__, 'welcome_message')))
