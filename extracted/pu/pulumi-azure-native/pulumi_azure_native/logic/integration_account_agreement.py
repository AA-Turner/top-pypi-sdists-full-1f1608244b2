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

__all__ = ['IntegrationAccountAgreementArgs', 'IntegrationAccountAgreement']

@pulumi.input_type
class IntegrationAccountAgreementArgs:
    def __init__(__self__, *,
                 agreement_type: pulumi.Input['AgreementType'],
                 content: pulumi.Input['AgreementContentArgs'],
                 guest_identity: pulumi.Input['BusinessIdentityArgs'],
                 guest_partner: pulumi.Input[builtins.str],
                 host_identity: pulumi.Input['BusinessIdentityArgs'],
                 host_partner: pulumi.Input[builtins.str],
                 integration_account_name: pulumi.Input[builtins.str],
                 resource_group_name: pulumi.Input[builtins.str],
                 agreement_name: Optional[pulumi.Input[builtins.str]] = None,
                 location: Optional[pulumi.Input[builtins.str]] = None,
                 metadata: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None):
        """
        The set of arguments for constructing a IntegrationAccountAgreement resource.
        :param pulumi.Input['AgreementType'] agreement_type: The agreement type.
        :param pulumi.Input['AgreementContentArgs'] content: The agreement content.
        :param pulumi.Input['BusinessIdentityArgs'] guest_identity: The business identity of the guest partner.
        :param pulumi.Input[builtins.str] guest_partner: The integration account partner that is set as guest partner for this agreement.
        :param pulumi.Input['BusinessIdentityArgs'] host_identity: The business identity of the host partner.
        :param pulumi.Input[builtins.str] host_partner: The integration account partner that is set as host partner for this agreement.
        :param pulumi.Input[builtins.str] integration_account_name: The integration account name.
        :param pulumi.Input[builtins.str] resource_group_name: The resource group name.
        :param pulumi.Input[builtins.str] agreement_name: The integration account agreement name.
        :param pulumi.Input[builtins.str] location: The resource location.
        :param Any metadata: The metadata.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] tags: The resource tags.
        """
        pulumi.set(__self__, "agreement_type", agreement_type)
        pulumi.set(__self__, "content", content)
        pulumi.set(__self__, "guest_identity", guest_identity)
        pulumi.set(__self__, "guest_partner", guest_partner)
        pulumi.set(__self__, "host_identity", host_identity)
        pulumi.set(__self__, "host_partner", host_partner)
        pulumi.set(__self__, "integration_account_name", integration_account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if agreement_name is not None:
            pulumi.set(__self__, "agreement_name", agreement_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="agreementType")
    def agreement_type(self) -> pulumi.Input['AgreementType']:
        """
        The agreement type.
        """
        return pulumi.get(self, "agreement_type")

    @agreement_type.setter
    def agreement_type(self, value: pulumi.Input['AgreementType']):
        pulumi.set(self, "agreement_type", value)

    @property
    @pulumi.getter
    def content(self) -> pulumi.Input['AgreementContentArgs']:
        """
        The agreement content.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: pulumi.Input['AgreementContentArgs']):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter(name="guestIdentity")
    def guest_identity(self) -> pulumi.Input['BusinessIdentityArgs']:
        """
        The business identity of the guest partner.
        """
        return pulumi.get(self, "guest_identity")

    @guest_identity.setter
    def guest_identity(self, value: pulumi.Input['BusinessIdentityArgs']):
        pulumi.set(self, "guest_identity", value)

    @property
    @pulumi.getter(name="guestPartner")
    def guest_partner(self) -> pulumi.Input[builtins.str]:
        """
        The integration account partner that is set as guest partner for this agreement.
        """
        return pulumi.get(self, "guest_partner")

    @guest_partner.setter
    def guest_partner(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "guest_partner", value)

    @property
    @pulumi.getter(name="hostIdentity")
    def host_identity(self) -> pulumi.Input['BusinessIdentityArgs']:
        """
        The business identity of the host partner.
        """
        return pulumi.get(self, "host_identity")

    @host_identity.setter
    def host_identity(self, value: pulumi.Input['BusinessIdentityArgs']):
        pulumi.set(self, "host_identity", value)

    @property
    @pulumi.getter(name="hostPartner")
    def host_partner(self) -> pulumi.Input[builtins.str]:
        """
        The integration account partner that is set as host partner for this agreement.
        """
        return pulumi.get(self, "host_partner")

    @host_partner.setter
    def host_partner(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "host_partner", value)

    @property
    @pulumi.getter(name="integrationAccountName")
    def integration_account_name(self) -> pulumi.Input[builtins.str]:
        """
        The integration account name.
        """
        return pulumi.get(self, "integration_account_name")

    @integration_account_name.setter
    def integration_account_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "integration_account_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[builtins.str]:
        """
        The resource group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="agreementName")
    def agreement_name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The integration account agreement name.
        """
        return pulumi.get(self, "agreement_name")

    @agreement_name.setter
    def agreement_name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "agreement_name", value)

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
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        """
        The metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[Any]):
        pulumi.set(self, "metadata", value)

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


@pulumi.type_token("azure-native:logic:IntegrationAccountAgreement")
class IntegrationAccountAgreement(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agreement_name: Optional[pulumi.Input[builtins.str]] = None,
                 agreement_type: Optional[pulumi.Input['AgreementType']] = None,
                 content: Optional[pulumi.Input[Union['AgreementContentArgs', 'AgreementContentArgsDict']]] = None,
                 guest_identity: Optional[pulumi.Input[Union['BusinessIdentityArgs', 'BusinessIdentityArgsDict']]] = None,
                 guest_partner: Optional[pulumi.Input[builtins.str]] = None,
                 host_identity: Optional[pulumi.Input[Union['BusinessIdentityArgs', 'BusinessIdentityArgsDict']]] = None,
                 host_partner: Optional[pulumi.Input[builtins.str]] = None,
                 integration_account_name: Optional[pulumi.Input[builtins.str]] = None,
                 location: Optional[pulumi.Input[builtins.str]] = None,
                 metadata: Optional[Any] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        """
        The integration account agreement.

        Uses Azure REST API version 2019-05-01. In version 2.x of the Azure Native provider, it used API version 2019-05-01.

        Other available API versions: 2015-08-01-preview, 2018-07-01-preview. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native logic [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] agreement_name: The integration account agreement name.
        :param pulumi.Input['AgreementType'] agreement_type: The agreement type.
        :param pulumi.Input[Union['AgreementContentArgs', 'AgreementContentArgsDict']] content: The agreement content.
        :param pulumi.Input[Union['BusinessIdentityArgs', 'BusinessIdentityArgsDict']] guest_identity: The business identity of the guest partner.
        :param pulumi.Input[builtins.str] guest_partner: The integration account partner that is set as guest partner for this agreement.
        :param pulumi.Input[Union['BusinessIdentityArgs', 'BusinessIdentityArgsDict']] host_identity: The business identity of the host partner.
        :param pulumi.Input[builtins.str] host_partner: The integration account partner that is set as host partner for this agreement.
        :param pulumi.Input[builtins.str] integration_account_name: The integration account name.
        :param pulumi.Input[builtins.str] location: The resource location.
        :param Any metadata: The metadata.
        :param pulumi.Input[builtins.str] resource_group_name: The resource group name.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] tags: The resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IntegrationAccountAgreementArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The integration account agreement.

        Uses Azure REST API version 2019-05-01. In version 2.x of the Azure Native provider, it used API version 2019-05-01.

        Other available API versions: 2015-08-01-preview, 2018-07-01-preview. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native logic [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.

        :param str resource_name: The name of the resource.
        :param IntegrationAccountAgreementArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IntegrationAccountAgreementArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agreement_name: Optional[pulumi.Input[builtins.str]] = None,
                 agreement_type: Optional[pulumi.Input['AgreementType']] = None,
                 content: Optional[pulumi.Input[Union['AgreementContentArgs', 'AgreementContentArgsDict']]] = None,
                 guest_identity: Optional[pulumi.Input[Union['BusinessIdentityArgs', 'BusinessIdentityArgsDict']]] = None,
                 guest_partner: Optional[pulumi.Input[builtins.str]] = None,
                 host_identity: Optional[pulumi.Input[Union['BusinessIdentityArgs', 'BusinessIdentityArgsDict']]] = None,
                 host_partner: Optional[pulumi.Input[builtins.str]] = None,
                 integration_account_name: Optional[pulumi.Input[builtins.str]] = None,
                 location: Optional[pulumi.Input[builtins.str]] = None,
                 metadata: Optional[Any] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IntegrationAccountAgreementArgs.__new__(IntegrationAccountAgreementArgs)

            __props__.__dict__["agreement_name"] = agreement_name
            if agreement_type is None and not opts.urn:
                raise TypeError("Missing required property 'agreement_type'")
            __props__.__dict__["agreement_type"] = agreement_type
            if content is None and not opts.urn:
                raise TypeError("Missing required property 'content'")
            __props__.__dict__["content"] = content
            if guest_identity is None and not opts.urn:
                raise TypeError("Missing required property 'guest_identity'")
            __props__.__dict__["guest_identity"] = guest_identity
            if guest_partner is None and not opts.urn:
                raise TypeError("Missing required property 'guest_partner'")
            __props__.__dict__["guest_partner"] = guest_partner
            if host_identity is None and not opts.urn:
                raise TypeError("Missing required property 'host_identity'")
            __props__.__dict__["host_identity"] = host_identity
            if host_partner is None and not opts.urn:
                raise TypeError("Missing required property 'host_partner'")
            __props__.__dict__["host_partner"] = host_partner
            if integration_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'integration_account_name'")
            __props__.__dict__["integration_account_name"] = integration_account_name
            __props__.__dict__["location"] = location
            __props__.__dict__["metadata"] = metadata
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["azure_api_version"] = None
            __props__.__dict__["changed_time"] = None
            __props__.__dict__["created_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:logic/v20150801preview:IntegrationAccountAgreement"), pulumi.Alias(type_="azure-native:logic/v20160601:Agreement"), pulumi.Alias(type_="azure-native:logic/v20160601:IntegrationAccountAgreement"), pulumi.Alias(type_="azure-native:logic/v20180701preview:IntegrationAccountAgreement"), pulumi.Alias(type_="azure-native:logic/v20190501:IntegrationAccountAgreement")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(IntegrationAccountAgreement, __self__).__init__(
            'azure-native:logic:IntegrationAccountAgreement',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IntegrationAccountAgreement':
        """
        Get an existing IntegrationAccountAgreement resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IntegrationAccountAgreementArgs.__new__(IntegrationAccountAgreementArgs)

        __props__.__dict__["agreement_type"] = None
        __props__.__dict__["azure_api_version"] = None
        __props__.__dict__["changed_time"] = None
        __props__.__dict__["content"] = None
        __props__.__dict__["created_time"] = None
        __props__.__dict__["guest_identity"] = None
        __props__.__dict__["guest_partner"] = None
        __props__.__dict__["host_identity"] = None
        __props__.__dict__["host_partner"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return IntegrationAccountAgreement(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="agreementType")
    def agreement_type(self) -> pulumi.Output[builtins.str]:
        """
        The agreement type.
        """
        return pulumi.get(self, "agreement_type")

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[builtins.str]:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter(name="changedTime")
    def changed_time(self) -> pulumi.Output[builtins.str]:
        """
        The changed time.
        """
        return pulumi.get(self, "changed_time")

    @property
    @pulumi.getter
    def content(self) -> pulumi.Output['outputs.AgreementContentResponse']:
        """
        The agreement content.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[builtins.str]:
        """
        The created time.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter(name="guestIdentity")
    def guest_identity(self) -> pulumi.Output['outputs.BusinessIdentityResponse']:
        """
        The business identity of the guest partner.
        """
        return pulumi.get(self, "guest_identity")

    @property
    @pulumi.getter(name="guestPartner")
    def guest_partner(self) -> pulumi.Output[builtins.str]:
        """
        The integration account partner that is set as guest partner for this agreement.
        """
        return pulumi.get(self, "guest_partner")

    @property
    @pulumi.getter(name="hostIdentity")
    def host_identity(self) -> pulumi.Output['outputs.BusinessIdentityResponse']:
        """
        The business identity of the host partner.
        """
        return pulumi.get(self, "host_identity")

    @property
    @pulumi.getter(name="hostPartner")
    def host_partner(self) -> pulumi.Output[builtins.str]:
        """
        The integration account partner that is set as host partner for this agreement.
        """
        return pulumi.get(self, "host_partner")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Any]]:
        """
        The metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        Gets the resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, builtins.str]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[builtins.str]:
        """
        Gets the resource type.
        """
        return pulumi.get(self, "type")

