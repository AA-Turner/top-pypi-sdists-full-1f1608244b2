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
from ._enums import *

__all__ = ['WorkspaceProductArgs', 'WorkspaceProduct']

@pulumi.input_type
class WorkspaceProductArgs:
    def __init__(__self__, *,
                 display_name: pulumi.Input[builtins.str],
                 resource_group_name: pulumi.Input[builtins.str],
                 service_name: pulumi.Input[builtins.str],
                 workspace_id: pulumi.Input[builtins.str],
                 approval_required: Optional[pulumi.Input[builtins.bool]] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 product_id: Optional[pulumi.Input[builtins.str]] = None,
                 state: Optional[pulumi.Input['ProductState']] = None,
                 subscription_required: Optional[pulumi.Input[builtins.bool]] = None,
                 subscriptions_limit: Optional[pulumi.Input[builtins.int]] = None,
                 terms: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a WorkspaceProduct resource.
        :param pulumi.Input[builtins.str] display_name: Product name.
        :param pulumi.Input[builtins.str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[builtins.str] service_name: The name of the API Management service.
        :param pulumi.Input[builtins.str] workspace_id: Workspace identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[builtins.bool] approval_required: whether subscription approval is required. If false, new subscriptions will be approved automatically enabling developers to call the product’s APIs immediately after subscribing. If true, administrators must manually approve the subscription before the developer can any of the product’s APIs. Can be present only if subscriptionRequired property is present and has a value of false.
        :param pulumi.Input[builtins.str] description: Product description. May include HTML formatting tags.
        :param pulumi.Input[builtins.str] product_id: Product identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input['ProductState'] state: whether product is published or not. Published products are discoverable by users of developer portal. Non published products are visible only to administrators. Default state of Product is notPublished.
        :param pulumi.Input[builtins.bool] subscription_required: Whether a product subscription is required for accessing APIs included in this product. If true, the product is referred to as "protected" and a valid subscription key is required for a request to an API included in the product to succeed. If false, the product is referred to as "open" and requests to an API included in the product can be made without a subscription key. If property is omitted when creating a new product it's value is assumed to be true.
        :param pulumi.Input[builtins.int] subscriptions_limit: Whether the number of subscriptions a user can have to this product at the same time. Set to null or omit to allow unlimited per user subscriptions. Can be present only if subscriptionRequired property is present and has a value of false.
        :param pulumi.Input[builtins.str] terms: Product terms of use. Developers trying to subscribe to the product will be presented and required to accept these terms before they can complete the subscription process.
        """
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        pulumi.set(__self__, "workspace_id", workspace_id)
        if approval_required is not None:
            pulumi.set(__self__, "approval_required", approval_required)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if product_id is not None:
            pulumi.set(__self__, "product_id", product_id)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if subscription_required is not None:
            pulumi.set(__self__, "subscription_required", subscription_required)
        if subscriptions_limit is not None:
            pulumi.set(__self__, "subscriptions_limit", subscriptions_limit)
        if terms is not None:
            pulumi.set(__self__, "terms", terms)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[builtins.str]:
        """
        Product name.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "display_name", value)

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
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Input[builtins.str]:
        """
        Workspace identifier. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "workspace_id")

    @workspace_id.setter
    def workspace_id(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "workspace_id", value)

    @property
    @pulumi.getter(name="approvalRequired")
    def approval_required(self) -> Optional[pulumi.Input[builtins.bool]]:
        """
        whether subscription approval is required. If false, new subscriptions will be approved automatically enabling developers to call the product’s APIs immediately after subscribing. If true, administrators must manually approve the subscription before the developer can any of the product’s APIs. Can be present only if subscriptionRequired property is present and has a value of false.
        """
        return pulumi.get(self, "approval_required")

    @approval_required.setter
    def approval_required(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "approval_required", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Product description. May include HTML formatting tags.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Product identifier. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "product_id")

    @product_id.setter
    def product_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "product_id", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input['ProductState']]:
        """
        whether product is published or not. Published products are discoverable by users of developer portal. Non published products are visible only to administrators. Default state of Product is notPublished.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input['ProductState']]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="subscriptionRequired")
    def subscription_required(self) -> Optional[pulumi.Input[builtins.bool]]:
        """
        Whether a product subscription is required for accessing APIs included in this product. If true, the product is referred to as "protected" and a valid subscription key is required for a request to an API included in the product to succeed. If false, the product is referred to as "open" and requests to an API included in the product can be made without a subscription key. If property is omitted when creating a new product it's value is assumed to be true.
        """
        return pulumi.get(self, "subscription_required")

    @subscription_required.setter
    def subscription_required(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "subscription_required", value)

    @property
    @pulumi.getter(name="subscriptionsLimit")
    def subscriptions_limit(self) -> Optional[pulumi.Input[builtins.int]]:
        """
        Whether the number of subscriptions a user can have to this product at the same time. Set to null or omit to allow unlimited per user subscriptions. Can be present only if subscriptionRequired property is present and has a value of false.
        """
        return pulumi.get(self, "subscriptions_limit")

    @subscriptions_limit.setter
    def subscriptions_limit(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "subscriptions_limit", value)

    @property
    @pulumi.getter
    def terms(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Product terms of use. Developers trying to subscribe to the product will be presented and required to accept these terms before they can complete the subscription process.
        """
        return pulumi.get(self, "terms")

    @terms.setter
    def terms(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "terms", value)


@pulumi.type_token("azure-native:apimanagement:WorkspaceProduct")
class WorkspaceProduct(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 approval_required: Optional[pulumi.Input[builtins.bool]] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 display_name: Optional[pulumi.Input[builtins.str]] = None,
                 product_id: Optional[pulumi.Input[builtins.str]] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 service_name: Optional[pulumi.Input[builtins.str]] = None,
                 state: Optional[pulumi.Input['ProductState']] = None,
                 subscription_required: Optional[pulumi.Input[builtins.bool]] = None,
                 subscriptions_limit: Optional[pulumi.Input[builtins.int]] = None,
                 terms: Optional[pulumi.Input[builtins.str]] = None,
                 workspace_id: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        Product details.

        Uses Azure REST API version 2022-09-01-preview. In version 2.x of the Azure Native provider, it used API version 2022-09-01-preview.

        Other available API versions: 2023-03-01-preview, 2023-05-01-preview, 2023-09-01-preview, 2024-05-01, 2024-06-01-preview. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native apimanagement [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.bool] approval_required: whether subscription approval is required. If false, new subscriptions will be approved automatically enabling developers to call the product’s APIs immediately after subscribing. If true, administrators must manually approve the subscription before the developer can any of the product’s APIs. Can be present only if subscriptionRequired property is present and has a value of false.
        :param pulumi.Input[builtins.str] description: Product description. May include HTML formatting tags.
        :param pulumi.Input[builtins.str] display_name: Product name.
        :param pulumi.Input[builtins.str] product_id: Product identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[builtins.str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[builtins.str] service_name: The name of the API Management service.
        :param pulumi.Input['ProductState'] state: whether product is published or not. Published products are discoverable by users of developer portal. Non published products are visible only to administrators. Default state of Product is notPublished.
        :param pulumi.Input[builtins.bool] subscription_required: Whether a product subscription is required for accessing APIs included in this product. If true, the product is referred to as "protected" and a valid subscription key is required for a request to an API included in the product to succeed. If false, the product is referred to as "open" and requests to an API included in the product can be made without a subscription key. If property is omitted when creating a new product it's value is assumed to be true.
        :param pulumi.Input[builtins.int] subscriptions_limit: Whether the number of subscriptions a user can have to this product at the same time. Set to null or omit to allow unlimited per user subscriptions. Can be present only if subscriptionRequired property is present and has a value of false.
        :param pulumi.Input[builtins.str] terms: Product terms of use. Developers trying to subscribe to the product will be presented and required to accept these terms before they can complete the subscription process.
        :param pulumi.Input[builtins.str] workspace_id: Workspace identifier. Must be unique in the current API Management service instance.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkspaceProductArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Product details.

        Uses Azure REST API version 2022-09-01-preview. In version 2.x of the Azure Native provider, it used API version 2022-09-01-preview.

        Other available API versions: 2023-03-01-preview, 2023-05-01-preview, 2023-09-01-preview, 2024-05-01, 2024-06-01-preview. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native apimanagement [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.

        :param str resource_name: The name of the resource.
        :param WorkspaceProductArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkspaceProductArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 approval_required: Optional[pulumi.Input[builtins.bool]] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 display_name: Optional[pulumi.Input[builtins.str]] = None,
                 product_id: Optional[pulumi.Input[builtins.str]] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 service_name: Optional[pulumi.Input[builtins.str]] = None,
                 state: Optional[pulumi.Input['ProductState']] = None,
                 subscription_required: Optional[pulumi.Input[builtins.bool]] = None,
                 subscriptions_limit: Optional[pulumi.Input[builtins.int]] = None,
                 terms: Optional[pulumi.Input[builtins.str]] = None,
                 workspace_id: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkspaceProductArgs.__new__(WorkspaceProductArgs)

            __props__.__dict__["approval_required"] = approval_required
            __props__.__dict__["description"] = description
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["product_id"] = product_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["state"] = state
            __props__.__dict__["subscription_required"] = subscription_required
            __props__.__dict__["subscriptions_limit"] = subscriptions_limit
            __props__.__dict__["terms"] = terms
            if workspace_id is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_id'")
            __props__.__dict__["workspace_id"] = workspace_id
            __props__.__dict__["azure_api_version"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:apimanagement/v20220901preview:WorkspaceProduct"), pulumi.Alias(type_="azure-native:apimanagement/v20230301preview:WorkspaceProduct"), pulumi.Alias(type_="azure-native:apimanagement/v20230501preview:WorkspaceProduct"), pulumi.Alias(type_="azure-native:apimanagement/v20230901preview:WorkspaceProduct"), pulumi.Alias(type_="azure-native:apimanagement/v20240501:WorkspaceProduct"), pulumi.Alias(type_="azure-native:apimanagement/v20240601preview:WorkspaceProduct")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WorkspaceProduct, __self__).__init__(
            'azure-native:apimanagement:WorkspaceProduct',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WorkspaceProduct':
        """
        Get an existing WorkspaceProduct resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkspaceProductArgs.__new__(WorkspaceProductArgs)

        __props__.__dict__["approval_required"] = None
        __props__.__dict__["azure_api_version"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["subscription_required"] = None
        __props__.__dict__["subscriptions_limit"] = None
        __props__.__dict__["terms"] = None
        __props__.__dict__["type"] = None
        return WorkspaceProduct(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="approvalRequired")
    def approval_required(self) -> pulumi.Output[Optional[builtins.bool]]:
        """
        whether subscription approval is required. If false, new subscriptions will be approved automatically enabling developers to call the product’s APIs immediately after subscribing. If true, administrators must manually approve the subscription before the developer can any of the product’s APIs. Can be present only if subscriptionRequired property is present and has a value of false.
        """
        return pulumi.get(self, "approval_required")

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[builtins.str]:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        Product description. May include HTML formatting tags.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[builtins.str]:
        """
        Product name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        whether product is published or not. Published products are discoverable by users of developer portal. Non published products are visible only to administrators. Default state of Product is notPublished.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="subscriptionRequired")
    def subscription_required(self) -> pulumi.Output[Optional[builtins.bool]]:
        """
        Whether a product subscription is required for accessing APIs included in this product. If true, the product is referred to as "protected" and a valid subscription key is required for a request to an API included in the product to succeed. If false, the product is referred to as "open" and requests to an API included in the product can be made without a subscription key. If property is omitted when creating a new product it's value is assumed to be true.
        """
        return pulumi.get(self, "subscription_required")

    @property
    @pulumi.getter(name="subscriptionsLimit")
    def subscriptions_limit(self) -> pulumi.Output[Optional[builtins.int]]:
        """
        Whether the number of subscriptions a user can have to this product at the same time. Set to null or omit to allow unlimited per user subscriptions. Can be present only if subscriptionRequired property is present and has a value of false.
        """
        return pulumi.get(self, "subscriptions_limit")

    @property
    @pulumi.getter
    def terms(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        Product terms of use. Developers trying to subscribe to the product will be presented and required to accept these terms before they can complete the subscription process.
        """
        return pulumi.get(self, "terms")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[builtins.str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

