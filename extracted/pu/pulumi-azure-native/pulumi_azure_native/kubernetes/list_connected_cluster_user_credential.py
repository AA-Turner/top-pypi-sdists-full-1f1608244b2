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

__all__ = [
    'ListConnectedClusterUserCredentialResult',
    'AwaitableListConnectedClusterUserCredentialResult',
    'list_connected_cluster_user_credential',
    'list_connected_cluster_user_credential_output',
]

@pulumi.output_type
class ListConnectedClusterUserCredentialResult:
    """
    The list of credential result response.
    """
    def __init__(__self__, hybrid_connection_config=None, kubeconfigs=None):
        if hybrid_connection_config and not isinstance(hybrid_connection_config, dict):
            raise TypeError("Expected argument 'hybrid_connection_config' to be a dict")
        pulumi.set(__self__, "hybrid_connection_config", hybrid_connection_config)
        if kubeconfigs and not isinstance(kubeconfigs, list):
            raise TypeError("Expected argument 'kubeconfigs' to be a list")
        pulumi.set(__self__, "kubeconfigs", kubeconfigs)

    @property
    @pulumi.getter(name="hybridConnectionConfig")
    def hybrid_connection_config(self) -> 'outputs.HybridConnectionConfigResponse':
        """
        Contains the REP (rendezvous endpoint) and “Sender” access token.
        """
        return pulumi.get(self, "hybrid_connection_config")

    @property
    @pulumi.getter
    def kubeconfigs(self) -> Sequence['outputs.CredentialResultResponse']:
        """
        Base64-encoded Kubernetes configuration file.
        """
        return pulumi.get(self, "kubeconfigs")


class AwaitableListConnectedClusterUserCredentialResult(ListConnectedClusterUserCredentialResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListConnectedClusterUserCredentialResult(
            hybrid_connection_config=self.hybrid_connection_config,
            kubeconfigs=self.kubeconfigs)


def list_connected_cluster_user_credential(authentication_method: Optional[Union[builtins.str, 'AuthenticationMethod']] = None,
                                           client_proxy: Optional[builtins.bool] = None,
                                           cluster_name: Optional[builtins.str] = None,
                                           resource_group_name: Optional[builtins.str] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListConnectedClusterUserCredentialResult:
    """
    Gets cluster user credentials of the connected cluster with a specified resource group and name.

    Uses Azure REST API version 2024-02-01-preview.

    Other available API versions: 2021-10-01, 2022-05-01-preview, 2022-10-01-preview, 2023-11-01-preview, 2024-01-01, 2024-06-01-preview, 2024-07-01-preview, 2024-07-15-preview, 2024-12-01-preview. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native kubernetes [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param Union[builtins.str, 'AuthenticationMethod'] authentication_method: The mode of client authentication.
    :param builtins.bool client_proxy: Boolean value to indicate whether the request is for client side proxy or not
    :param builtins.str cluster_name: The name of the Kubernetes cluster on which get is called.
    :param builtins.str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['authenticationMethod'] = authentication_method
    __args__['clientProxy'] = client_proxy
    __args__['clusterName'] = cluster_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:kubernetes:listConnectedClusterUserCredential', __args__, opts=opts, typ=ListConnectedClusterUserCredentialResult).value

    return AwaitableListConnectedClusterUserCredentialResult(
        hybrid_connection_config=pulumi.get(__ret__, 'hybrid_connection_config'),
        kubeconfigs=pulumi.get(__ret__, 'kubeconfigs'))
def list_connected_cluster_user_credential_output(authentication_method: Optional[pulumi.Input[Union[builtins.str, 'AuthenticationMethod']]] = None,
                                                  client_proxy: Optional[pulumi.Input[builtins.bool]] = None,
                                                  cluster_name: Optional[pulumi.Input[builtins.str]] = None,
                                                  resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                                                  opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[ListConnectedClusterUserCredentialResult]:
    """
    Gets cluster user credentials of the connected cluster with a specified resource group and name.

    Uses Azure REST API version 2024-02-01-preview.

    Other available API versions: 2021-10-01, 2022-05-01-preview, 2022-10-01-preview, 2023-11-01-preview, 2024-01-01, 2024-06-01-preview, 2024-07-01-preview, 2024-07-15-preview, 2024-12-01-preview. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native kubernetes [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param Union[builtins.str, 'AuthenticationMethod'] authentication_method: The mode of client authentication.
    :param builtins.bool client_proxy: Boolean value to indicate whether the request is for client side proxy or not
    :param builtins.str cluster_name: The name of the Kubernetes cluster on which get is called.
    :param builtins.str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['authenticationMethod'] = authentication_method
    __args__['clientProxy'] = client_proxy
    __args__['clusterName'] = cluster_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('azure-native:kubernetes:listConnectedClusterUserCredential', __args__, opts=opts, typ=ListConnectedClusterUserCredentialResult)
    return __ret__.apply(lambda __response__: ListConnectedClusterUserCredentialResult(
        hybrid_connection_config=pulumi.get(__response__, 'hybrid_connection_config'),
        kubeconfigs=pulumi.get(__response__, 'kubeconfigs')))
