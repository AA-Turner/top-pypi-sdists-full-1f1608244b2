# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
import pulumi
from enum import Enum

__all__ = [
    'DnsType',
]


@pulumi.type_token("azure-native:domainregistration:DnsType")
class DnsType(builtins.str, Enum):
    """
    Target DNS type (would be used for migration)
    """
    AZURE_DNS = "AzureDns"
    DEFAULT_DOMAIN_REGISTRAR_DNS = "DefaultDomainRegistrarDns"
