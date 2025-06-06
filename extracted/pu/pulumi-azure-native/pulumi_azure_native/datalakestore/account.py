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

__all__ = ['AccountArgs', 'Account']

@pulumi.input_type
class AccountArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[builtins.str],
                 account_name: Optional[pulumi.Input[builtins.str]] = None,
                 default_group: Optional[pulumi.Input[builtins.str]] = None,
                 encryption_config: Optional[pulumi.Input['EncryptionConfigArgs']] = None,
                 encryption_state: Optional[pulumi.Input['EncryptionState']] = None,
                 firewall_allow_azure_ips: Optional[pulumi.Input['FirewallAllowAzureIpsState']] = None,
                 firewall_rules: Optional[pulumi.Input[Sequence[pulumi.Input['CreateFirewallRuleWithAccountParametersArgs']]]] = None,
                 firewall_state: Optional[pulumi.Input['FirewallState']] = None,
                 identity: Optional[pulumi.Input['EncryptionIdentityArgs']] = None,
                 location: Optional[pulumi.Input[builtins.str]] = None,
                 new_tier: Optional[pulumi.Input['TierType']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 trusted_id_provider_state: Optional[pulumi.Input['TrustedIdProviderState']] = None,
                 trusted_id_providers: Optional[pulumi.Input[Sequence[pulumi.Input['CreateTrustedIdProviderWithAccountParametersArgs']]]] = None,
                 virtual_network_rules: Optional[pulumi.Input[Sequence[pulumi.Input['CreateVirtualNetworkRuleWithAccountParametersArgs']]]] = None):
        """
        The set of arguments for constructing a Account resource.
        :param pulumi.Input[builtins.str] resource_group_name: The name of the Azure resource group.
        :param pulumi.Input[builtins.str] account_name: The name of the Data Lake Store account.
        :param pulumi.Input[builtins.str] default_group: The default owner group for all new folders and files created in the Data Lake Store account.
        :param pulumi.Input['EncryptionConfigArgs'] encryption_config: The Key Vault encryption configuration.
        :param pulumi.Input['EncryptionState'] encryption_state: The current state of encryption for this Data Lake Store account.
        :param pulumi.Input['FirewallAllowAzureIpsState'] firewall_allow_azure_ips: The current state of allowing or disallowing IPs originating within Azure through the firewall. If the firewall is disabled, this is not enforced.
        :param pulumi.Input[Sequence[pulumi.Input['CreateFirewallRuleWithAccountParametersArgs']]] firewall_rules: The list of firewall rules associated with this Data Lake Store account.
        :param pulumi.Input['FirewallState'] firewall_state: The current state of the IP address firewall for this Data Lake Store account.
        :param pulumi.Input['EncryptionIdentityArgs'] identity: The Key Vault encryption identity, if any.
        :param pulumi.Input[builtins.str] location: The resource location.
        :param pulumi.Input['TierType'] new_tier: The commitment tier to use for next month.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] tags: The resource tags.
        :param pulumi.Input['TrustedIdProviderState'] trusted_id_provider_state: The current state of the trusted identity provider feature for this Data Lake Store account.
        :param pulumi.Input[Sequence[pulumi.Input['CreateTrustedIdProviderWithAccountParametersArgs']]] trusted_id_providers: The list of trusted identity providers associated with this Data Lake Store account.
        :param pulumi.Input[Sequence[pulumi.Input['CreateVirtualNetworkRuleWithAccountParametersArgs']]] virtual_network_rules: The list of virtual network rules associated with this Data Lake Store account.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if account_name is not None:
            pulumi.set(__self__, "account_name", account_name)
        if default_group is not None:
            pulumi.set(__self__, "default_group", default_group)
        if encryption_config is not None:
            pulumi.set(__self__, "encryption_config", encryption_config)
        if encryption_state is not None:
            pulumi.set(__self__, "encryption_state", encryption_state)
        if firewall_allow_azure_ips is not None:
            pulumi.set(__self__, "firewall_allow_azure_ips", firewall_allow_azure_ips)
        if firewall_rules is not None:
            pulumi.set(__self__, "firewall_rules", firewall_rules)
        if firewall_state is not None:
            pulumi.set(__self__, "firewall_state", firewall_state)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if new_tier is not None:
            pulumi.set(__self__, "new_tier", new_tier)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if trusted_id_provider_state is not None:
            pulumi.set(__self__, "trusted_id_provider_state", trusted_id_provider_state)
        if trusted_id_providers is not None:
            pulumi.set(__self__, "trusted_id_providers", trusted_id_providers)
        if virtual_network_rules is not None:
            pulumi.set(__self__, "virtual_network_rules", virtual_network_rules)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[builtins.str]:
        """
        The name of the Azure resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the Data Lake Store account.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="defaultGroup")
    def default_group(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The default owner group for all new folders and files created in the Data Lake Store account.
        """
        return pulumi.get(self, "default_group")

    @default_group.setter
    def default_group(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "default_group", value)

    @property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> Optional[pulumi.Input['EncryptionConfigArgs']]:
        """
        The Key Vault encryption configuration.
        """
        return pulumi.get(self, "encryption_config")

    @encryption_config.setter
    def encryption_config(self, value: Optional[pulumi.Input['EncryptionConfigArgs']]):
        pulumi.set(self, "encryption_config", value)

    @property
    @pulumi.getter(name="encryptionState")
    def encryption_state(self) -> Optional[pulumi.Input['EncryptionState']]:
        """
        The current state of encryption for this Data Lake Store account.
        """
        return pulumi.get(self, "encryption_state")

    @encryption_state.setter
    def encryption_state(self, value: Optional[pulumi.Input['EncryptionState']]):
        pulumi.set(self, "encryption_state", value)

    @property
    @pulumi.getter(name="firewallAllowAzureIps")
    def firewall_allow_azure_ips(self) -> Optional[pulumi.Input['FirewallAllowAzureIpsState']]:
        """
        The current state of allowing or disallowing IPs originating within Azure through the firewall. If the firewall is disabled, this is not enforced.
        """
        return pulumi.get(self, "firewall_allow_azure_ips")

    @firewall_allow_azure_ips.setter
    def firewall_allow_azure_ips(self, value: Optional[pulumi.Input['FirewallAllowAzureIpsState']]):
        pulumi.set(self, "firewall_allow_azure_ips", value)

    @property
    @pulumi.getter(name="firewallRules")
    def firewall_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CreateFirewallRuleWithAccountParametersArgs']]]]:
        """
        The list of firewall rules associated with this Data Lake Store account.
        """
        return pulumi.get(self, "firewall_rules")

    @firewall_rules.setter
    def firewall_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CreateFirewallRuleWithAccountParametersArgs']]]]):
        pulumi.set(self, "firewall_rules", value)

    @property
    @pulumi.getter(name="firewallState")
    def firewall_state(self) -> Optional[pulumi.Input['FirewallState']]:
        """
        The current state of the IP address firewall for this Data Lake Store account.
        """
        return pulumi.get(self, "firewall_state")

    @firewall_state.setter
    def firewall_state(self, value: Optional[pulumi.Input['FirewallState']]):
        pulumi.set(self, "firewall_state", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['EncryptionIdentityArgs']]:
        """
        The Key Vault encryption identity, if any.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['EncryptionIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="newTier")
    def new_tier(self) -> Optional[pulumi.Input['TierType']]:
        """
        The commitment tier to use for next month.
        """
        return pulumi.get(self, "new_tier")

    @new_tier.setter
    def new_tier(self, value: Optional[pulumi.Input['TierType']]):
        pulumi.set(self, "new_tier", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="trustedIdProviderState")
    def trusted_id_provider_state(self) -> Optional[pulumi.Input['TrustedIdProviderState']]:
        """
        The current state of the trusted identity provider feature for this Data Lake Store account.
        """
        return pulumi.get(self, "trusted_id_provider_state")

    @trusted_id_provider_state.setter
    def trusted_id_provider_state(self, value: Optional[pulumi.Input['TrustedIdProviderState']]):
        pulumi.set(self, "trusted_id_provider_state", value)

    @property
    @pulumi.getter(name="trustedIdProviders")
    def trusted_id_providers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CreateTrustedIdProviderWithAccountParametersArgs']]]]:
        """
        The list of trusted identity providers associated with this Data Lake Store account.
        """
        return pulumi.get(self, "trusted_id_providers")

    @trusted_id_providers.setter
    def trusted_id_providers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CreateTrustedIdProviderWithAccountParametersArgs']]]]):
        pulumi.set(self, "trusted_id_providers", value)

    @property
    @pulumi.getter(name="virtualNetworkRules")
    def virtual_network_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CreateVirtualNetworkRuleWithAccountParametersArgs']]]]:
        """
        The list of virtual network rules associated with this Data Lake Store account.
        """
        return pulumi.get(self, "virtual_network_rules")

    @virtual_network_rules.setter
    def virtual_network_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CreateVirtualNetworkRuleWithAccountParametersArgs']]]]):
        pulumi.set(self, "virtual_network_rules", value)


@pulumi.type_token("azure-native:datalakestore:Account")
class Account(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[builtins.str]] = None,
                 default_group: Optional[pulumi.Input[builtins.str]] = None,
                 encryption_config: Optional[pulumi.Input[Union['EncryptionConfigArgs', 'EncryptionConfigArgsDict']]] = None,
                 encryption_state: Optional[pulumi.Input['EncryptionState']] = None,
                 firewall_allow_azure_ips: Optional[pulumi.Input['FirewallAllowAzureIpsState']] = None,
                 firewall_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union['CreateFirewallRuleWithAccountParametersArgs', 'CreateFirewallRuleWithAccountParametersArgsDict']]]]] = None,
                 firewall_state: Optional[pulumi.Input['FirewallState']] = None,
                 identity: Optional[pulumi.Input[Union['EncryptionIdentityArgs', 'EncryptionIdentityArgsDict']]] = None,
                 location: Optional[pulumi.Input[builtins.str]] = None,
                 new_tier: Optional[pulumi.Input['TierType']] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 trusted_id_provider_state: Optional[pulumi.Input['TrustedIdProviderState']] = None,
                 trusted_id_providers: Optional[pulumi.Input[Sequence[pulumi.Input[Union['CreateTrustedIdProviderWithAccountParametersArgs', 'CreateTrustedIdProviderWithAccountParametersArgsDict']]]]] = None,
                 virtual_network_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union['CreateVirtualNetworkRuleWithAccountParametersArgs', 'CreateVirtualNetworkRuleWithAccountParametersArgsDict']]]]] = None,
                 __props__=None):
        """
        Data Lake Store account information.

        Uses Azure REST API version 2016-11-01. In version 2.x of the Azure Native provider, it used API version 2016-11-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] account_name: The name of the Data Lake Store account.
        :param pulumi.Input[builtins.str] default_group: The default owner group for all new folders and files created in the Data Lake Store account.
        :param pulumi.Input[Union['EncryptionConfigArgs', 'EncryptionConfigArgsDict']] encryption_config: The Key Vault encryption configuration.
        :param pulumi.Input['EncryptionState'] encryption_state: The current state of encryption for this Data Lake Store account.
        :param pulumi.Input['FirewallAllowAzureIpsState'] firewall_allow_azure_ips: The current state of allowing or disallowing IPs originating within Azure through the firewall. If the firewall is disabled, this is not enforced.
        :param pulumi.Input[Sequence[pulumi.Input[Union['CreateFirewallRuleWithAccountParametersArgs', 'CreateFirewallRuleWithAccountParametersArgsDict']]]] firewall_rules: The list of firewall rules associated with this Data Lake Store account.
        :param pulumi.Input['FirewallState'] firewall_state: The current state of the IP address firewall for this Data Lake Store account.
        :param pulumi.Input[Union['EncryptionIdentityArgs', 'EncryptionIdentityArgsDict']] identity: The Key Vault encryption identity, if any.
        :param pulumi.Input[builtins.str] location: The resource location.
        :param pulumi.Input['TierType'] new_tier: The commitment tier to use for next month.
        :param pulumi.Input[builtins.str] resource_group_name: The name of the Azure resource group.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] tags: The resource tags.
        :param pulumi.Input['TrustedIdProviderState'] trusted_id_provider_state: The current state of the trusted identity provider feature for this Data Lake Store account.
        :param pulumi.Input[Sequence[pulumi.Input[Union['CreateTrustedIdProviderWithAccountParametersArgs', 'CreateTrustedIdProviderWithAccountParametersArgsDict']]]] trusted_id_providers: The list of trusted identity providers associated with this Data Lake Store account.
        :param pulumi.Input[Sequence[pulumi.Input[Union['CreateVirtualNetworkRuleWithAccountParametersArgs', 'CreateVirtualNetworkRuleWithAccountParametersArgsDict']]]] virtual_network_rules: The list of virtual network rules associated with this Data Lake Store account.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Data Lake Store account information.

        Uses Azure REST API version 2016-11-01. In version 2.x of the Azure Native provider, it used API version 2016-11-01.

        :param str resource_name: The name of the resource.
        :param AccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[builtins.str]] = None,
                 default_group: Optional[pulumi.Input[builtins.str]] = None,
                 encryption_config: Optional[pulumi.Input[Union['EncryptionConfigArgs', 'EncryptionConfigArgsDict']]] = None,
                 encryption_state: Optional[pulumi.Input['EncryptionState']] = None,
                 firewall_allow_azure_ips: Optional[pulumi.Input['FirewallAllowAzureIpsState']] = None,
                 firewall_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union['CreateFirewallRuleWithAccountParametersArgs', 'CreateFirewallRuleWithAccountParametersArgsDict']]]]] = None,
                 firewall_state: Optional[pulumi.Input['FirewallState']] = None,
                 identity: Optional[pulumi.Input[Union['EncryptionIdentityArgs', 'EncryptionIdentityArgsDict']]] = None,
                 location: Optional[pulumi.Input[builtins.str]] = None,
                 new_tier: Optional[pulumi.Input['TierType']] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 trusted_id_provider_state: Optional[pulumi.Input['TrustedIdProviderState']] = None,
                 trusted_id_providers: Optional[pulumi.Input[Sequence[pulumi.Input[Union['CreateTrustedIdProviderWithAccountParametersArgs', 'CreateTrustedIdProviderWithAccountParametersArgsDict']]]]] = None,
                 virtual_network_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union['CreateVirtualNetworkRuleWithAccountParametersArgs', 'CreateVirtualNetworkRuleWithAccountParametersArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AccountArgs.__new__(AccountArgs)

            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["default_group"] = default_group
            __props__.__dict__["encryption_config"] = encryption_config
            __props__.__dict__["encryption_state"] = encryption_state
            __props__.__dict__["firewall_allow_azure_ips"] = firewall_allow_azure_ips
            __props__.__dict__["firewall_rules"] = firewall_rules
            __props__.__dict__["firewall_state"] = firewall_state
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["new_tier"] = new_tier
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["trusted_id_provider_state"] = trusted_id_provider_state
            __props__.__dict__["trusted_id_providers"] = trusted_id_providers
            __props__.__dict__["virtual_network_rules"] = virtual_network_rules
            __props__.__dict__["account_id"] = None
            __props__.__dict__["azure_api_version"] = None
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["current_tier"] = None
            __props__.__dict__["encryption_provisioning_state"] = None
            __props__.__dict__["endpoint"] = None
            __props__.__dict__["last_modified_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:datalakestore/v20161101:Account")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Account, __self__).__init__(
            'azure-native:datalakestore:Account',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Account':
        """
        Get an existing Account resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AccountArgs.__new__(AccountArgs)

        __props__.__dict__["account_id"] = None
        __props__.__dict__["azure_api_version"] = None
        __props__.__dict__["creation_time"] = None
        __props__.__dict__["current_tier"] = None
        __props__.__dict__["default_group"] = None
        __props__.__dict__["encryption_config"] = None
        __props__.__dict__["encryption_provisioning_state"] = None
        __props__.__dict__["encryption_state"] = None
        __props__.__dict__["endpoint"] = None
        __props__.__dict__["firewall_allow_azure_ips"] = None
        __props__.__dict__["firewall_rules"] = None
        __props__.__dict__["firewall_state"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["last_modified_time"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["new_tier"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["trusted_id_provider_state"] = None
        __props__.__dict__["trusted_id_providers"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_network_rules"] = None
        return Account(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[builtins.str]:
        """
        The unique identifier associated with this Data Lake Store account.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[builtins.str]:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[builtins.str]:
        """
        The account creation time.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="currentTier")
    def current_tier(self) -> pulumi.Output[builtins.str]:
        """
        The commitment tier in use for the current month.
        """
        return pulumi.get(self, "current_tier")

    @property
    @pulumi.getter(name="defaultGroup")
    def default_group(self) -> pulumi.Output[builtins.str]:
        """
        The default owner group for all new folders and files created in the Data Lake Store account.
        """
        return pulumi.get(self, "default_group")

    @property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> pulumi.Output['outputs.EncryptionConfigResponse']:
        """
        The Key Vault encryption configuration.
        """
        return pulumi.get(self, "encryption_config")

    @property
    @pulumi.getter(name="encryptionProvisioningState")
    def encryption_provisioning_state(self) -> pulumi.Output[builtins.str]:
        """
        The current state of encryption provisioning for this Data Lake Store account.
        """
        return pulumi.get(self, "encryption_provisioning_state")

    @property
    @pulumi.getter(name="encryptionState")
    def encryption_state(self) -> pulumi.Output[builtins.str]:
        """
        The current state of encryption for this Data Lake Store account.
        """
        return pulumi.get(self, "encryption_state")

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[builtins.str]:
        """
        The full CName endpoint for this account.
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="firewallAllowAzureIps")
    def firewall_allow_azure_ips(self) -> pulumi.Output[builtins.str]:
        """
        The current state of allowing or disallowing IPs originating within Azure through the firewall. If the firewall is disabled, this is not enforced.
        """
        return pulumi.get(self, "firewall_allow_azure_ips")

    @property
    @pulumi.getter(name="firewallRules")
    def firewall_rules(self) -> pulumi.Output[Sequence['outputs.FirewallRuleResponse']]:
        """
        The list of firewall rules associated with this Data Lake Store account.
        """
        return pulumi.get(self, "firewall_rules")

    @property
    @pulumi.getter(name="firewallState")
    def firewall_state(self) -> pulumi.Output[builtins.str]:
        """
        The current state of the IP address firewall for this Data Lake Store account.
        """
        return pulumi.get(self, "firewall_state")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output['outputs.EncryptionIdentityResponse']:
        """
        The Key Vault encryption identity, if any.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[builtins.str]:
        """
        The account last modified time.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[builtins.str]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="newTier")
    def new_tier(self) -> pulumi.Output[builtins.str]:
        """
        The commitment tier to use for next month.
        """
        return pulumi.get(self, "new_tier")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[builtins.str]:
        """
        The provisioning status of the Data Lake Store account.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[builtins.str]:
        """
        The state of the Data Lake Store account.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Mapping[str, builtins.str]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="trustedIdProviderState")
    def trusted_id_provider_state(self) -> pulumi.Output[builtins.str]:
        """
        The current state of the trusted identity provider feature for this Data Lake Store account.
        """
        return pulumi.get(self, "trusted_id_provider_state")

    @property
    @pulumi.getter(name="trustedIdProviders")
    def trusted_id_providers(self) -> pulumi.Output[Sequence['outputs.TrustedIdProviderResponse']]:
        """
        The list of trusted identity providers associated with this Data Lake Store account.
        """
        return pulumi.get(self, "trusted_id_providers")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[builtins.str]:
        """
        The resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualNetworkRules")
    def virtual_network_rules(self) -> pulumi.Output[Sequence['outputs.VirtualNetworkRuleResponse']]:
        """
        The list of virtual network rules associated with this Data Lake Store account.
        """
        return pulumi.get(self, "virtual_network_rules")

