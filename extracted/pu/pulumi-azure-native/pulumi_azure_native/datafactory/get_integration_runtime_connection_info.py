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

__all__ = [
    'GetIntegrationRuntimeConnectionInfoResult',
    'AwaitableGetIntegrationRuntimeConnectionInfoResult',
    'get_integration_runtime_connection_info',
    'get_integration_runtime_connection_info_output',
]

@pulumi.output_type
class GetIntegrationRuntimeConnectionInfoResult:
    """
    Connection information for encrypting the on-premises data source credentials.
    """
    def __init__(__self__, host_service_uri=None, identity_cert_thumbprint=None, is_identity_cert_exprired=None, public_key=None, service_token=None, version=None):
        if host_service_uri and not isinstance(host_service_uri, str):
            raise TypeError("Expected argument 'host_service_uri' to be a str")
        pulumi.set(__self__, "host_service_uri", host_service_uri)
        if identity_cert_thumbprint and not isinstance(identity_cert_thumbprint, str):
            raise TypeError("Expected argument 'identity_cert_thumbprint' to be a str")
        pulumi.set(__self__, "identity_cert_thumbprint", identity_cert_thumbprint)
        if is_identity_cert_exprired and not isinstance(is_identity_cert_exprired, bool):
            raise TypeError("Expected argument 'is_identity_cert_exprired' to be a bool")
        pulumi.set(__self__, "is_identity_cert_exprired", is_identity_cert_exprired)
        if public_key and not isinstance(public_key, str):
            raise TypeError("Expected argument 'public_key' to be a str")
        pulumi.set(__self__, "public_key", public_key)
        if service_token and not isinstance(service_token, str):
            raise TypeError("Expected argument 'service_token' to be a str")
        pulumi.set(__self__, "service_token", service_token)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="hostServiceUri")
    def host_service_uri(self) -> builtins.str:
        """
        The on-premises integration runtime host URL.
        """
        return pulumi.get(self, "host_service_uri")

    @property
    @pulumi.getter(name="identityCertThumbprint")
    def identity_cert_thumbprint(self) -> builtins.str:
        """
        The integration runtime SSL certificate thumbprint. Click-Once application uses it to do server validation.
        """
        return pulumi.get(self, "identity_cert_thumbprint")

    @property
    @pulumi.getter(name="isIdentityCertExprired")
    def is_identity_cert_exprired(self) -> builtins.bool:
        """
        Whether the identity certificate is expired.
        """
        return pulumi.get(self, "is_identity_cert_exprired")

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> builtins.str:
        """
        The public key for encrypting a credential when transferring the credential to the integration runtime.
        """
        return pulumi.get(self, "public_key")

    @property
    @pulumi.getter(name="serviceToken")
    def service_token(self) -> builtins.str:
        """
        The token generated in service. Callers use this token to authenticate to integration runtime.
        """
        return pulumi.get(self, "service_token")

    @property
    @pulumi.getter
    def version(self) -> builtins.str:
        """
        The integration runtime version.
        """
        return pulumi.get(self, "version")


class AwaitableGetIntegrationRuntimeConnectionInfoResult(GetIntegrationRuntimeConnectionInfoResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIntegrationRuntimeConnectionInfoResult(
            host_service_uri=self.host_service_uri,
            identity_cert_thumbprint=self.identity_cert_thumbprint,
            is_identity_cert_exprired=self.is_identity_cert_exprired,
            public_key=self.public_key,
            service_token=self.service_token,
            version=self.version)


def get_integration_runtime_connection_info(factory_name: Optional[builtins.str] = None,
                                            integration_runtime_name: Optional[builtins.str] = None,
                                            resource_group_name: Optional[builtins.str] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIntegrationRuntimeConnectionInfoResult:
    """
    Gets the on-premises integration runtime connection information for encrypting the on-premises data source credentials.

    Uses Azure REST API version 2018-06-01.


    :param builtins.str factory_name: The factory name.
    :param builtins.str integration_runtime_name: The integration runtime name.
    :param builtins.str resource_group_name: The resource group name.
    """
    __args__ = dict()
    __args__['factoryName'] = factory_name
    __args__['integrationRuntimeName'] = integration_runtime_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:datafactory:getIntegrationRuntimeConnectionInfo', __args__, opts=opts, typ=GetIntegrationRuntimeConnectionInfoResult).value

    return AwaitableGetIntegrationRuntimeConnectionInfoResult(
        host_service_uri=pulumi.get(__ret__, 'host_service_uri'),
        identity_cert_thumbprint=pulumi.get(__ret__, 'identity_cert_thumbprint'),
        is_identity_cert_exprired=pulumi.get(__ret__, 'is_identity_cert_exprired'),
        public_key=pulumi.get(__ret__, 'public_key'),
        service_token=pulumi.get(__ret__, 'service_token'),
        version=pulumi.get(__ret__, 'version'))
def get_integration_runtime_connection_info_output(factory_name: Optional[pulumi.Input[builtins.str]] = None,
                                                   integration_runtime_name: Optional[pulumi.Input[builtins.str]] = None,
                                                   resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                                                   opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetIntegrationRuntimeConnectionInfoResult]:
    """
    Gets the on-premises integration runtime connection information for encrypting the on-premises data source credentials.

    Uses Azure REST API version 2018-06-01.


    :param builtins.str factory_name: The factory name.
    :param builtins.str integration_runtime_name: The integration runtime name.
    :param builtins.str resource_group_name: The resource group name.
    """
    __args__ = dict()
    __args__['factoryName'] = factory_name
    __args__['integrationRuntimeName'] = integration_runtime_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('azure-native:datafactory:getIntegrationRuntimeConnectionInfo', __args__, opts=opts, typ=GetIntegrationRuntimeConnectionInfoResult)
    return __ret__.apply(lambda __response__: GetIntegrationRuntimeConnectionInfoResult(
        host_service_uri=pulumi.get(__response__, 'host_service_uri'),
        identity_cert_thumbprint=pulumi.get(__response__, 'identity_cert_thumbprint'),
        is_identity_cert_exprired=pulumi.get(__response__, 'is_identity_cert_exprired'),
        public_key=pulumi.get(__response__, 'public_key'),
        service_token=pulumi.get(__response__, 'service_token'),
        version=pulumi.get(__response__, 'version')))
