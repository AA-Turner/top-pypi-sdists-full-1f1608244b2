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
    'GetLicenseResult',
    'AwaitableGetLicenseResult',
    'get_license',
    'get_license_output',
]

@pulumi.output_type
class GetLicenseResult:
    def __init__(__self__, beneficiary=None, consumption_configuration=None, entitlements=None, home_region=None, issuer=None, license_arn=None, license_metadata=None, license_name=None, product_name=None, product_sku=None, validity=None, version=None):
        if beneficiary and not isinstance(beneficiary, str):
            raise TypeError("Expected argument 'beneficiary' to be a str")
        pulumi.set(__self__, "beneficiary", beneficiary)
        if consumption_configuration and not isinstance(consumption_configuration, dict):
            raise TypeError("Expected argument 'consumption_configuration' to be a dict")
        pulumi.set(__self__, "consumption_configuration", consumption_configuration)
        if entitlements and not isinstance(entitlements, list):
            raise TypeError("Expected argument 'entitlements' to be a list")
        pulumi.set(__self__, "entitlements", entitlements)
        if home_region and not isinstance(home_region, str):
            raise TypeError("Expected argument 'home_region' to be a str")
        pulumi.set(__self__, "home_region", home_region)
        if issuer and not isinstance(issuer, dict):
            raise TypeError("Expected argument 'issuer' to be a dict")
        pulumi.set(__self__, "issuer", issuer)
        if license_arn and not isinstance(license_arn, str):
            raise TypeError("Expected argument 'license_arn' to be a str")
        pulumi.set(__self__, "license_arn", license_arn)
        if license_metadata and not isinstance(license_metadata, list):
            raise TypeError("Expected argument 'license_metadata' to be a list")
        pulumi.set(__self__, "license_metadata", license_metadata)
        if license_name and not isinstance(license_name, str):
            raise TypeError("Expected argument 'license_name' to be a str")
        pulumi.set(__self__, "license_name", license_name)
        if product_name and not isinstance(product_name, str):
            raise TypeError("Expected argument 'product_name' to be a str")
        pulumi.set(__self__, "product_name", product_name)
        if product_sku and not isinstance(product_sku, str):
            raise TypeError("Expected argument 'product_sku' to be a str")
        pulumi.set(__self__, "product_sku", product_sku)
        if validity and not isinstance(validity, dict):
            raise TypeError("Expected argument 'validity' to be a dict")
        pulumi.set(__self__, "validity", validity)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def beneficiary(self) -> Optional[builtins.str]:
        """
        Beneficiary of the license.
        """
        return pulumi.get(self, "beneficiary")

    @property
    @pulumi.getter(name="consumptionConfiguration")
    def consumption_configuration(self) -> Optional['outputs.LicenseConsumptionConfiguration']:
        """
        Configuration for consumption of the license.
        """
        return pulumi.get(self, "consumption_configuration")

    @property
    @pulumi.getter
    def entitlements(self) -> Optional[Sequence['outputs.LicenseEntitlement']]:
        """
        License entitlements.
        """
        return pulumi.get(self, "entitlements")

    @property
    @pulumi.getter(name="homeRegion")
    def home_region(self) -> Optional[builtins.str]:
        """
        Home region for the created license.
        """
        return pulumi.get(self, "home_region")

    @property
    @pulumi.getter
    def issuer(self) -> Optional['outputs.LicenseIssuerData']:
        """
        License issuer.
        """
        return pulumi.get(self, "issuer")

    @property
    @pulumi.getter(name="licenseArn")
    def license_arn(self) -> Optional[builtins.str]:
        """
        Amazon Resource Name is a unique name for each resource.
        """
        return pulumi.get(self, "license_arn")

    @property
    @pulumi.getter(name="licenseMetadata")
    def license_metadata(self) -> Optional[Sequence['outputs.LicenseMetadata']]:
        """
        License metadata.
        """
        return pulumi.get(self, "license_metadata")

    @property
    @pulumi.getter(name="licenseName")
    def license_name(self) -> Optional[builtins.str]:
        """
        Name for the created license.
        """
        return pulumi.get(self, "license_name")

    @property
    @pulumi.getter(name="productName")
    def product_name(self) -> Optional[builtins.str]:
        """
        Product name for the created license.
        """
        return pulumi.get(self, "product_name")

    @property
    @pulumi.getter(name="productSku")
    def product_sku(self) -> Optional[builtins.str]:
        """
        ProductSKU of the license.
        """
        return pulumi.get(self, "product_sku")

    @property
    @pulumi.getter
    def validity(self) -> Optional['outputs.LicenseValidityDateFormat']:
        """
        Date and time range during which the license is valid, in ISO8601-UTC format.
        """
        return pulumi.get(self, "validity")

    @property
    @pulumi.getter
    def version(self) -> Optional[builtins.str]:
        """
        The version of the license.
        """
        return pulumi.get(self, "version")


class AwaitableGetLicenseResult(GetLicenseResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLicenseResult(
            beneficiary=self.beneficiary,
            consumption_configuration=self.consumption_configuration,
            entitlements=self.entitlements,
            home_region=self.home_region,
            issuer=self.issuer,
            license_arn=self.license_arn,
            license_metadata=self.license_metadata,
            license_name=self.license_name,
            product_name=self.product_name,
            product_sku=self.product_sku,
            validity=self.validity,
            version=self.version)


def get_license(license_arn: Optional[builtins.str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLicenseResult:
    """
    Resource Type definition for AWS::LicenseManager::License


    :param builtins.str license_arn: Amazon Resource Name is a unique name for each resource.
    """
    __args__ = dict()
    __args__['licenseArn'] = license_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:licensemanager:getLicense', __args__, opts=opts, typ=GetLicenseResult).value

    return AwaitableGetLicenseResult(
        beneficiary=pulumi.get(__ret__, 'beneficiary'),
        consumption_configuration=pulumi.get(__ret__, 'consumption_configuration'),
        entitlements=pulumi.get(__ret__, 'entitlements'),
        home_region=pulumi.get(__ret__, 'home_region'),
        issuer=pulumi.get(__ret__, 'issuer'),
        license_arn=pulumi.get(__ret__, 'license_arn'),
        license_metadata=pulumi.get(__ret__, 'license_metadata'),
        license_name=pulumi.get(__ret__, 'license_name'),
        product_name=pulumi.get(__ret__, 'product_name'),
        product_sku=pulumi.get(__ret__, 'product_sku'),
        validity=pulumi.get(__ret__, 'validity'),
        version=pulumi.get(__ret__, 'version'))
def get_license_output(license_arn: Optional[pulumi.Input[builtins.str]] = None,
                       opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetLicenseResult]:
    """
    Resource Type definition for AWS::LicenseManager::License


    :param builtins.str license_arn: Amazon Resource Name is a unique name for each resource.
    """
    __args__ = dict()
    __args__['licenseArn'] = license_arn
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:licensemanager:getLicense', __args__, opts=opts, typ=GetLicenseResult)
    return __ret__.apply(lambda __response__: GetLicenseResult(
        beneficiary=pulumi.get(__response__, 'beneficiary'),
        consumption_configuration=pulumi.get(__response__, 'consumption_configuration'),
        entitlements=pulumi.get(__response__, 'entitlements'),
        home_region=pulumi.get(__response__, 'home_region'),
        issuer=pulumi.get(__response__, 'issuer'),
        license_arn=pulumi.get(__response__, 'license_arn'),
        license_metadata=pulumi.get(__response__, 'license_metadata'),
        license_name=pulumi.get(__response__, 'license_name'),
        product_name=pulumi.get(__response__, 'product_name'),
        product_sku=pulumi.get(__response__, 'product_sku'),
        validity=pulumi.get(__response__, 'validity'),
        version=pulumi.get(__response__, 'version')))
