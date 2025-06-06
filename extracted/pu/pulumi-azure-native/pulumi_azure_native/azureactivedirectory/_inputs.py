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

__all__ = [
    'B2CResourceSKUArgs',
    'B2CResourceSKUArgsDict',
    'CIAMResourceSKUArgs',
    'CIAMResourceSKUArgsDict',
    'CreateCIAMTenantPropertiesArgs',
    'CreateCIAMTenantPropertiesArgsDict',
]

MYPY = False

if not MYPY:
    class B2CResourceSKUArgsDict(TypedDict):
        """
        SKU properties of the Azure AD B2C tenant. Learn more about Azure AD B2C billing at [aka.ms/b2cBilling](https://aka.ms/b2cBilling).
        """
        name: NotRequired[pulumi.Input[Union[builtins.str, 'B2CResourceSKUName']]]
        """
        The name of the SKU for the tenant.
        """
        tier: NotRequired[pulumi.Input[Union[builtins.str, 'B2CResourceSKUTier']]]
        """
        The tier of the tenant.
        """
elif False:
    B2CResourceSKUArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class B2CResourceSKUArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[Union[builtins.str, 'B2CResourceSKUName']]] = None,
                 tier: Optional[pulumi.Input[Union[builtins.str, 'B2CResourceSKUTier']]] = None):
        """
        SKU properties of the Azure AD B2C tenant. Learn more about Azure AD B2C billing at [aka.ms/b2cBilling](https://aka.ms/b2cBilling).
        :param pulumi.Input[Union[builtins.str, 'B2CResourceSKUName']] name: The name of the SKU for the tenant.
        :param pulumi.Input[Union[builtins.str, 'B2CResourceSKUTier']] tier: The tier of the tenant.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[Union[builtins.str, 'B2CResourceSKUName']]]:
        """
        The name of the SKU for the tenant.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[Union[builtins.str, 'B2CResourceSKUName']]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[Union[builtins.str, 'B2CResourceSKUTier']]]:
        """
        The tier of the tenant.
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: Optional[pulumi.Input[Union[builtins.str, 'B2CResourceSKUTier']]]):
        pulumi.set(self, "tier", value)


if not MYPY:
    class CIAMResourceSKUArgsDict(TypedDict):
        """
        SKU properties of the Azure AD for customers tenant. Learn more about Azure AD for customers billing at [https://aka.ms/ciambilling](https://aka.ms/ciambilling).
        """
        name: pulumi.Input[Union[builtins.str, 'CIAMResourceSKUName']]
        """
        The name of the SKU for the tenant.
        """
        tier: pulumi.Input[Union[builtins.str, 'CIAMResourceSKUTier']]
        """
        The tier of the tenant.
        """
elif False:
    CIAMResourceSKUArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class CIAMResourceSKUArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[Union[builtins.str, 'CIAMResourceSKUName']],
                 tier: pulumi.Input[Union[builtins.str, 'CIAMResourceSKUTier']]):
        """
        SKU properties of the Azure AD for customers tenant. Learn more about Azure AD for customers billing at [https://aka.ms/ciambilling](https://aka.ms/ciambilling).
        :param pulumi.Input[Union[builtins.str, 'CIAMResourceSKUName']] name: The name of the SKU for the tenant.
        :param pulumi.Input[Union[builtins.str, 'CIAMResourceSKUTier']] tier: The tier of the tenant.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[builtins.str, 'CIAMResourceSKUName']]:
        """
        The name of the SKU for the tenant.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[Union[builtins.str, 'CIAMResourceSKUName']]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tier(self) -> pulumi.Input[Union[builtins.str, 'CIAMResourceSKUTier']]:
        """
        The tier of the tenant.
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: pulumi.Input[Union[builtins.str, 'CIAMResourceSKUTier']]):
        pulumi.set(self, "tier", value)


if not MYPY:
    class CreateCIAMTenantPropertiesArgsDict(TypedDict):
        """
        These properties are used to create the Azure AD for customers tenant. These properties are not part of the Azure resource.
        """
        country_code: pulumi.Input[builtins.str]
        """
        Country code of Azure tenant (e.g. 'US'). Refer to [https://aka.ms/ciam-data-location](https://aka.ms/ciam-data-location) to see valid country codes and corresponding data residency locations. If you do not see a country code in an valid data residency location, choose one from the list.
        """
        display_name: pulumi.Input[builtins.str]
        """
        The display name of the Azure AD for customers tenant.
        """
elif False:
    CreateCIAMTenantPropertiesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class CreateCIAMTenantPropertiesArgs:
    def __init__(__self__, *,
                 country_code: pulumi.Input[builtins.str],
                 display_name: pulumi.Input[builtins.str]):
        """
        These properties are used to create the Azure AD for customers tenant. These properties are not part of the Azure resource.
        :param pulumi.Input[builtins.str] country_code: Country code of Azure tenant (e.g. 'US'). Refer to [https://aka.ms/ciam-data-location](https://aka.ms/ciam-data-location) to see valid country codes and corresponding data residency locations. If you do not see a country code in an valid data residency location, choose one from the list.
        :param pulumi.Input[builtins.str] display_name: The display name of the Azure AD for customers tenant.
        """
        pulumi.set(__self__, "country_code", country_code)
        pulumi.set(__self__, "display_name", display_name)

    @property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> pulumi.Input[builtins.str]:
        """
        Country code of Azure tenant (e.g. 'US'). Refer to [https://aka.ms/ciam-data-location](https://aka.ms/ciam-data-location) to see valid country codes and corresponding data residency locations. If you do not see a country code in an valid data residency location, choose one from the list.
        """
        return pulumi.get(self, "country_code")

    @country_code.setter
    def country_code(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "country_code", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[builtins.str]:
        """
        The display name of the Azure AD for customers tenant.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "display_name", value)


