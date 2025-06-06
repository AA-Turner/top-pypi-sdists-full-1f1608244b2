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
from .. import outputs as _root_outputs
from ._enums import *

__all__ = [
    'GetIdentityProviderConfigResult',
    'AwaitableGetIdentityProviderConfigResult',
    'get_identity_provider_config',
    'get_identity_provider_config_output',
]

@pulumi.output_type
class GetIdentityProviderConfigResult:
    def __init__(__self__, identity_provider_config_arn=None, tags=None):
        if identity_provider_config_arn and not isinstance(identity_provider_config_arn, str):
            raise TypeError("Expected argument 'identity_provider_config_arn' to be a str")
        pulumi.set(__self__, "identity_provider_config_arn", identity_provider_config_arn)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="identityProviderConfigArn")
    def identity_provider_config_arn(self) -> Optional[builtins.str]:
        """
        The ARN of the configuration.
        """
        return pulumi.get(self, "identity_provider_config_arn")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetIdentityProviderConfigResult(GetIdentityProviderConfigResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIdentityProviderConfigResult(
            identity_provider_config_arn=self.identity_provider_config_arn,
            tags=self.tags)


def get_identity_provider_config(cluster_name: Optional[builtins.str] = None,
                                 identity_provider_config_name: Optional[builtins.str] = None,
                                 type: Optional['IdentityProviderConfigType'] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIdentityProviderConfigResult:
    """
    An object representing an Amazon EKS IdentityProviderConfig.


    :param builtins.str cluster_name: The name of the identity provider configuration.
    :param builtins.str identity_provider_config_name: The name of the OIDC provider configuration.
    :param 'IdentityProviderConfigType' type: The type of the identity provider configuration.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['identityProviderConfigName'] = identity_provider_config_name
    __args__['type'] = type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:eks:getIdentityProviderConfig', __args__, opts=opts, typ=GetIdentityProviderConfigResult).value

    return AwaitableGetIdentityProviderConfigResult(
        identity_provider_config_arn=pulumi.get(__ret__, 'identity_provider_config_arn'),
        tags=pulumi.get(__ret__, 'tags'))
def get_identity_provider_config_output(cluster_name: Optional[pulumi.Input[builtins.str]] = None,
                                        identity_provider_config_name: Optional[pulumi.Input[builtins.str]] = None,
                                        type: Optional[pulumi.Input['IdentityProviderConfigType']] = None,
                                        opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetIdentityProviderConfigResult]:
    """
    An object representing an Amazon EKS IdentityProviderConfig.


    :param builtins.str cluster_name: The name of the identity provider configuration.
    :param builtins.str identity_provider_config_name: The name of the OIDC provider configuration.
    :param 'IdentityProviderConfigType' type: The type of the identity provider configuration.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['identityProviderConfigName'] = identity_provider_config_name
    __args__['type'] = type
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:eks:getIdentityProviderConfig', __args__, opts=opts, typ=GetIdentityProviderConfigResult)
    return __ret__.apply(lambda __response__: GetIdentityProviderConfigResult(
        identity_provider_config_arn=pulumi.get(__response__, 'identity_provider_config_arn'),
        tags=pulumi.get(__response__, 'tags')))
