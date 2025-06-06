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
from ._inputs import *

__all__ = ['AuthorizationProviderArgs', 'AuthorizationProvider']

@pulumi.input_type
class AuthorizationProviderArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[builtins.str],
                 service_name: pulumi.Input[builtins.str],
                 authorization_provider_id: Optional[pulumi.Input[builtins.str]] = None,
                 display_name: Optional[pulumi.Input[builtins.str]] = None,
                 identity_provider: Optional[pulumi.Input[builtins.str]] = None,
                 oauth2: Optional[pulumi.Input['AuthorizationProviderOAuth2SettingsArgs']] = None):
        """
        The set of arguments for constructing a AuthorizationProvider resource.
        :param pulumi.Input[builtins.str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[builtins.str] service_name: The name of the API Management service.
        :param pulumi.Input[builtins.str] authorization_provider_id: Identifier of the authorization provider.
        :param pulumi.Input[builtins.str] display_name: Authorization Provider name. Must be 1 to 300 characters long.
        :param pulumi.Input[builtins.str] identity_provider: Identity provider name. Must be 1 to 300 characters long.
        :param pulumi.Input['AuthorizationProviderOAuth2SettingsArgs'] oauth2: OAuth2 settings
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        if authorization_provider_id is not None:
            pulumi.set(__self__, "authorization_provider_id", authorization_provider_id)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if identity_provider is not None:
            pulumi.set(__self__, "identity_provider", identity_provider)
        if oauth2 is not None:
            pulumi.set(__self__, "oauth2", oauth2)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[builtins.str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[builtins.str]:
        """
        The name of the API Management service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="authorizationProviderId")
    def authorization_provider_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Identifier of the authorization provider.
        """
        return pulumi.get(self, "authorization_provider_id")

    @authorization_provider_id.setter
    def authorization_provider_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "authorization_provider_id", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Authorization Provider name. Must be 1 to 300 characters long.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="identityProvider")
    def identity_provider(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Identity provider name. Must be 1 to 300 characters long.
        """
        return pulumi.get(self, "identity_provider")

    @identity_provider.setter
    def identity_provider(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "identity_provider", value)

    @property
    @pulumi.getter
    def oauth2(self) -> Optional[pulumi.Input['AuthorizationProviderOAuth2SettingsArgs']]:
        """
        OAuth2 settings
        """
        return pulumi.get(self, "oauth2")

    @oauth2.setter
    def oauth2(self, value: Optional[pulumi.Input['AuthorizationProviderOAuth2SettingsArgs']]):
        pulumi.set(self, "oauth2", value)


@pulumi.type_token("azure-native:apimanagement:AuthorizationProvider")
class AuthorizationProvider(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorization_provider_id: Optional[pulumi.Input[builtins.str]] = None,
                 display_name: Optional[pulumi.Input[builtins.str]] = None,
                 identity_provider: Optional[pulumi.Input[builtins.str]] = None,
                 oauth2: Optional[pulumi.Input[Union['AuthorizationProviderOAuth2SettingsArgs', 'AuthorizationProviderOAuth2SettingsArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 service_name: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        Authorization Provider contract.

        Uses Azure REST API version 2022-09-01-preview. In version 2.x of the Azure Native provider, it used API version 2022-08-01.

        Other available API versions: 2022-04-01-preview, 2022-08-01, 2023-03-01-preview, 2023-05-01-preview, 2023-09-01-preview, 2024-05-01, 2024-06-01-preview. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native apimanagement [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] authorization_provider_id: Identifier of the authorization provider.
        :param pulumi.Input[builtins.str] display_name: Authorization Provider name. Must be 1 to 300 characters long.
        :param pulumi.Input[builtins.str] identity_provider: Identity provider name. Must be 1 to 300 characters long.
        :param pulumi.Input[Union['AuthorizationProviderOAuth2SettingsArgs', 'AuthorizationProviderOAuth2SettingsArgsDict']] oauth2: OAuth2 settings
        :param pulumi.Input[builtins.str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[builtins.str] service_name: The name of the API Management service.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AuthorizationProviderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Authorization Provider contract.

        Uses Azure REST API version 2022-09-01-preview. In version 2.x of the Azure Native provider, it used API version 2022-08-01.

        Other available API versions: 2022-04-01-preview, 2022-08-01, 2023-03-01-preview, 2023-05-01-preview, 2023-09-01-preview, 2024-05-01, 2024-06-01-preview. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native apimanagement [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.

        :param str resource_name: The name of the resource.
        :param AuthorizationProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AuthorizationProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorization_provider_id: Optional[pulumi.Input[builtins.str]] = None,
                 display_name: Optional[pulumi.Input[builtins.str]] = None,
                 identity_provider: Optional[pulumi.Input[builtins.str]] = None,
                 oauth2: Optional[pulumi.Input[Union['AuthorizationProviderOAuth2SettingsArgs', 'AuthorizationProviderOAuth2SettingsArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 service_name: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AuthorizationProviderArgs.__new__(AuthorizationProviderArgs)

            __props__.__dict__["authorization_provider_id"] = authorization_provider_id
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["identity_provider"] = identity_provider
            __props__.__dict__["oauth2"] = oauth2
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["azure_api_version"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:apimanagement/v20220401preview:AuthorizationProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20220801:AuthorizationProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20220901preview:AuthorizationProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20230301preview:AuthorizationProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20230501preview:AuthorizationProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20230901preview:AuthorizationProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20240501:AuthorizationProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20240601preview:AuthorizationProvider")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AuthorizationProvider, __self__).__init__(
            'azure-native:apimanagement:AuthorizationProvider',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AuthorizationProvider':
        """
        Get an existing AuthorizationProvider resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AuthorizationProviderArgs.__new__(AuthorizationProviderArgs)

        __props__.__dict__["azure_api_version"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["identity_provider"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["oauth2"] = None
        __props__.__dict__["type"] = None
        return AuthorizationProvider(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[builtins.str]:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        Authorization Provider name. Must be 1 to 300 characters long.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="identityProvider")
    def identity_provider(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        Identity provider name. Must be 1 to 300 characters long.
        """
        return pulumi.get(self, "identity_provider")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def oauth2(self) -> pulumi.Output[Optional['outputs.AuthorizationProviderOAuth2SettingsResponse']]:
        """
        OAuth2 settings
        """
        return pulumi.get(self, "oauth2")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[builtins.str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

