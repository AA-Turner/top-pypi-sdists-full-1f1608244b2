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

__all__ = [
    'GetProductResult',
    'AwaitableGetProductResult',
    'get_product',
    'get_product_output',
]

@pulumi.output_type
class GetProductResult:
    """
    Product information.
    """
    def __init__(__self__, billing_part_number=None, compatibility=None, description=None, display_name=None, etag=None, gallery_item_identity=None, icon_uris=None, id=None, legal_terms=None, links=None, name=None, offer=None, offer_version=None, payload_length=None, privacy_policy=None, product_kind=None, product_properties=None, publisher_display_name=None, publisher_identifier=None, sku=None, type=None, vm_extension_type=None):
        if billing_part_number and not isinstance(billing_part_number, str):
            raise TypeError("Expected argument 'billing_part_number' to be a str")
        pulumi.set(__self__, "billing_part_number", billing_part_number)
        if compatibility and not isinstance(compatibility, dict):
            raise TypeError("Expected argument 'compatibility' to be a dict")
        pulumi.set(__self__, "compatibility", compatibility)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if gallery_item_identity and not isinstance(gallery_item_identity, str):
            raise TypeError("Expected argument 'gallery_item_identity' to be a str")
        pulumi.set(__self__, "gallery_item_identity", gallery_item_identity)
        if icon_uris and not isinstance(icon_uris, dict):
            raise TypeError("Expected argument 'icon_uris' to be a dict")
        pulumi.set(__self__, "icon_uris", icon_uris)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if legal_terms and not isinstance(legal_terms, str):
            raise TypeError("Expected argument 'legal_terms' to be a str")
        pulumi.set(__self__, "legal_terms", legal_terms)
        if links and not isinstance(links, list):
            raise TypeError("Expected argument 'links' to be a list")
        pulumi.set(__self__, "links", links)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if offer and not isinstance(offer, str):
            raise TypeError("Expected argument 'offer' to be a str")
        pulumi.set(__self__, "offer", offer)
        if offer_version and not isinstance(offer_version, str):
            raise TypeError("Expected argument 'offer_version' to be a str")
        pulumi.set(__self__, "offer_version", offer_version)
        if payload_length and not isinstance(payload_length, float):
            raise TypeError("Expected argument 'payload_length' to be a float")
        pulumi.set(__self__, "payload_length", payload_length)
        if privacy_policy and not isinstance(privacy_policy, str):
            raise TypeError("Expected argument 'privacy_policy' to be a str")
        pulumi.set(__self__, "privacy_policy", privacy_policy)
        if product_kind and not isinstance(product_kind, str):
            raise TypeError("Expected argument 'product_kind' to be a str")
        pulumi.set(__self__, "product_kind", product_kind)
        if product_properties and not isinstance(product_properties, dict):
            raise TypeError("Expected argument 'product_properties' to be a dict")
        pulumi.set(__self__, "product_properties", product_properties)
        if publisher_display_name and not isinstance(publisher_display_name, str):
            raise TypeError("Expected argument 'publisher_display_name' to be a str")
        pulumi.set(__self__, "publisher_display_name", publisher_display_name)
        if publisher_identifier and not isinstance(publisher_identifier, str):
            raise TypeError("Expected argument 'publisher_identifier' to be a str")
        pulumi.set(__self__, "publisher_identifier", publisher_identifier)
        if sku and not isinstance(sku, str):
            raise TypeError("Expected argument 'sku' to be a str")
        pulumi.set(__self__, "sku", sku)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if vm_extension_type and not isinstance(vm_extension_type, str):
            raise TypeError("Expected argument 'vm_extension_type' to be a str")
        pulumi.set(__self__, "vm_extension_type", vm_extension_type)

    @property
    @pulumi.getter(name="billingPartNumber")
    def billing_part_number(self) -> Optional[builtins.str]:
        """
        The part number used for billing purposes.
        """
        return pulumi.get(self, "billing_part_number")

    @property
    @pulumi.getter
    def compatibility(self) -> Optional['outputs.CompatibilityResponse']:
        """
        Product compatibility with current device.
        """
        return pulumi.get(self, "compatibility")

    @property
    @pulumi.getter
    def description(self) -> Optional[builtins.str]:
        """
        The description of the product.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[builtins.str]:
        """
        The display name of the product.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> Optional[builtins.str]:
        """
        The entity tag used for optimistic concurrency when modifying the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="galleryItemIdentity")
    def gallery_item_identity(self) -> Optional[builtins.str]:
        """
        The identifier of the gallery item corresponding to the product.
        """
        return pulumi.get(self, "gallery_item_identity")

    @property
    @pulumi.getter(name="iconUris")
    def icon_uris(self) -> Optional['outputs.IconUrisResponse']:
        """
        Additional links available for this product.
        """
        return pulumi.get(self, "icon_uris")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        """
        ID of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="legalTerms")
    def legal_terms(self) -> Optional[builtins.str]:
        """
        The legal terms.
        """
        return pulumi.get(self, "legal_terms")

    @property
    @pulumi.getter
    def links(self) -> Optional[Sequence['outputs.ProductLinkResponse']]:
        """
        Additional links available for this product.
        """
        return pulumi.get(self, "links")

    @property
    @pulumi.getter
    def name(self) -> builtins.str:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def offer(self) -> Optional[builtins.str]:
        """
        The offer representing the product.
        """
        return pulumi.get(self, "offer")

    @property
    @pulumi.getter(name="offerVersion")
    def offer_version(self) -> Optional[builtins.str]:
        """
        The version of the product offer.
        """
        return pulumi.get(self, "offer_version")

    @property
    @pulumi.getter(name="payloadLength")
    def payload_length(self) -> Optional[builtins.float]:
        """
        The length of product content.
        """
        return pulumi.get(self, "payload_length")

    @property
    @pulumi.getter(name="privacyPolicy")
    def privacy_policy(self) -> Optional[builtins.str]:
        """
        The privacy policy.
        """
        return pulumi.get(self, "privacy_policy")

    @property
    @pulumi.getter(name="productKind")
    def product_kind(self) -> Optional[builtins.str]:
        """
        The kind of the product (virtualMachine or virtualMachineExtension)
        """
        return pulumi.get(self, "product_kind")

    @property
    @pulumi.getter(name="productProperties")
    def product_properties(self) -> Optional['outputs.ProductPropertiesResponse']:
        """
        Additional properties for the product.
        """
        return pulumi.get(self, "product_properties")

    @property
    @pulumi.getter(name="publisherDisplayName")
    def publisher_display_name(self) -> Optional[builtins.str]:
        """
        The user-friendly name of the product publisher.
        """
        return pulumi.get(self, "publisher_display_name")

    @property
    @pulumi.getter(name="publisherIdentifier")
    def publisher_identifier(self) -> Optional[builtins.str]:
        """
        Publisher identifier.
        """
        return pulumi.get(self, "publisher_identifier")

    @property
    @pulumi.getter
    def sku(self) -> Optional[builtins.str]:
        """
        The product SKU.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def type(self) -> builtins.str:
        """
        Type of Resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vmExtensionType")
    def vm_extension_type(self) -> Optional[builtins.str]:
        """
        The type of the Virtual Machine Extension.
        """
        return pulumi.get(self, "vm_extension_type")


class AwaitableGetProductResult(GetProductResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProductResult(
            billing_part_number=self.billing_part_number,
            compatibility=self.compatibility,
            description=self.description,
            display_name=self.display_name,
            etag=self.etag,
            gallery_item_identity=self.gallery_item_identity,
            icon_uris=self.icon_uris,
            id=self.id,
            legal_terms=self.legal_terms,
            links=self.links,
            name=self.name,
            offer=self.offer,
            offer_version=self.offer_version,
            payload_length=self.payload_length,
            privacy_policy=self.privacy_policy,
            product_kind=self.product_kind,
            product_properties=self.product_properties,
            publisher_display_name=self.publisher_display_name,
            publisher_identifier=self.publisher_identifier,
            sku=self.sku,
            type=self.type,
            vm_extension_type=self.vm_extension_type)


def get_product(product_name: Optional[builtins.str] = None,
                registration_name: Optional[builtins.str] = None,
                resource_group: Optional[builtins.str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProductResult:
    """
    Returns the specified product.

    Uses Azure REST API version 2022-06-01.

    Other available API versions: 2020-06-01-preview. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native azurestack [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param builtins.str product_name: Name of the product.
    :param builtins.str registration_name: Name of the Azure Stack registration.
    :param builtins.str resource_group: Name of the resource group.
    """
    __args__ = dict()
    __args__['productName'] = product_name
    __args__['registrationName'] = registration_name
    __args__['resourceGroup'] = resource_group
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:azurestack:getProduct', __args__, opts=opts, typ=GetProductResult).value

    return AwaitableGetProductResult(
        billing_part_number=pulumi.get(__ret__, 'billing_part_number'),
        compatibility=pulumi.get(__ret__, 'compatibility'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        etag=pulumi.get(__ret__, 'etag'),
        gallery_item_identity=pulumi.get(__ret__, 'gallery_item_identity'),
        icon_uris=pulumi.get(__ret__, 'icon_uris'),
        id=pulumi.get(__ret__, 'id'),
        legal_terms=pulumi.get(__ret__, 'legal_terms'),
        links=pulumi.get(__ret__, 'links'),
        name=pulumi.get(__ret__, 'name'),
        offer=pulumi.get(__ret__, 'offer'),
        offer_version=pulumi.get(__ret__, 'offer_version'),
        payload_length=pulumi.get(__ret__, 'payload_length'),
        privacy_policy=pulumi.get(__ret__, 'privacy_policy'),
        product_kind=pulumi.get(__ret__, 'product_kind'),
        product_properties=pulumi.get(__ret__, 'product_properties'),
        publisher_display_name=pulumi.get(__ret__, 'publisher_display_name'),
        publisher_identifier=pulumi.get(__ret__, 'publisher_identifier'),
        sku=pulumi.get(__ret__, 'sku'),
        type=pulumi.get(__ret__, 'type'),
        vm_extension_type=pulumi.get(__ret__, 'vm_extension_type'))
def get_product_output(product_name: Optional[pulumi.Input[builtins.str]] = None,
                       registration_name: Optional[pulumi.Input[builtins.str]] = None,
                       resource_group: Optional[pulumi.Input[builtins.str]] = None,
                       opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetProductResult]:
    """
    Returns the specified product.

    Uses Azure REST API version 2022-06-01.

    Other available API versions: 2020-06-01-preview. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native azurestack [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param builtins.str product_name: Name of the product.
    :param builtins.str registration_name: Name of the Azure Stack registration.
    :param builtins.str resource_group: Name of the resource group.
    """
    __args__ = dict()
    __args__['productName'] = product_name
    __args__['registrationName'] = registration_name
    __args__['resourceGroup'] = resource_group
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('azure-native:azurestack:getProduct', __args__, opts=opts, typ=GetProductResult)
    return __ret__.apply(lambda __response__: GetProductResult(
        billing_part_number=pulumi.get(__response__, 'billing_part_number'),
        compatibility=pulumi.get(__response__, 'compatibility'),
        description=pulumi.get(__response__, 'description'),
        display_name=pulumi.get(__response__, 'display_name'),
        etag=pulumi.get(__response__, 'etag'),
        gallery_item_identity=pulumi.get(__response__, 'gallery_item_identity'),
        icon_uris=pulumi.get(__response__, 'icon_uris'),
        id=pulumi.get(__response__, 'id'),
        legal_terms=pulumi.get(__response__, 'legal_terms'),
        links=pulumi.get(__response__, 'links'),
        name=pulumi.get(__response__, 'name'),
        offer=pulumi.get(__response__, 'offer'),
        offer_version=pulumi.get(__response__, 'offer_version'),
        payload_length=pulumi.get(__response__, 'payload_length'),
        privacy_policy=pulumi.get(__response__, 'privacy_policy'),
        product_kind=pulumi.get(__response__, 'product_kind'),
        product_properties=pulumi.get(__response__, 'product_properties'),
        publisher_display_name=pulumi.get(__response__, 'publisher_display_name'),
        publisher_identifier=pulumi.get(__response__, 'publisher_identifier'),
        sku=pulumi.get(__response__, 'sku'),
        type=pulumi.get(__response__, 'type'),
        vm_extension_type=pulumi.get(__response__, 'vm_extension_type')))
