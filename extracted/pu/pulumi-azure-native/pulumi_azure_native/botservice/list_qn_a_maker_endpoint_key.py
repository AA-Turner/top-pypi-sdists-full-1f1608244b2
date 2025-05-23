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
    'ListQnAMakerEndpointKeyResult',
    'AwaitableListQnAMakerEndpointKeyResult',
    'list_qn_a_maker_endpoint_key',
    'list_qn_a_maker_endpoint_key_output',
]

@pulumi.output_type
class ListQnAMakerEndpointKeyResult:
    """
    Schema for EndpointKeys generate/refresh operations.
    """
    def __init__(__self__, installed_version=None, last_stable_version=None, primary_endpoint_key=None, secondary_endpoint_key=None):
        if installed_version and not isinstance(installed_version, str):
            raise TypeError("Expected argument 'installed_version' to be a str")
        pulumi.set(__self__, "installed_version", installed_version)
        if last_stable_version and not isinstance(last_stable_version, str):
            raise TypeError("Expected argument 'last_stable_version' to be a str")
        pulumi.set(__self__, "last_stable_version", last_stable_version)
        if primary_endpoint_key and not isinstance(primary_endpoint_key, str):
            raise TypeError("Expected argument 'primary_endpoint_key' to be a str")
        pulumi.set(__self__, "primary_endpoint_key", primary_endpoint_key)
        if secondary_endpoint_key and not isinstance(secondary_endpoint_key, str):
            raise TypeError("Expected argument 'secondary_endpoint_key' to be a str")
        pulumi.set(__self__, "secondary_endpoint_key", secondary_endpoint_key)

    @property
    @pulumi.getter(name="installedVersion")
    def installed_version(self) -> Optional[builtins.str]:
        """
        Current version of runtime.
        """
        return pulumi.get(self, "installed_version")

    @property
    @pulumi.getter(name="lastStableVersion")
    def last_stable_version(self) -> Optional[builtins.str]:
        """
        Latest version of runtime.
        """
        return pulumi.get(self, "last_stable_version")

    @property
    @pulumi.getter(name="primaryEndpointKey")
    def primary_endpoint_key(self) -> Optional[builtins.str]:
        """
        Primary Access Key.
        """
        return pulumi.get(self, "primary_endpoint_key")

    @property
    @pulumi.getter(name="secondaryEndpointKey")
    def secondary_endpoint_key(self) -> Optional[builtins.str]:
        """
        Secondary Access Key.
        """
        return pulumi.get(self, "secondary_endpoint_key")


class AwaitableListQnAMakerEndpointKeyResult(ListQnAMakerEndpointKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListQnAMakerEndpointKeyResult(
            installed_version=self.installed_version,
            last_stable_version=self.last_stable_version,
            primary_endpoint_key=self.primary_endpoint_key,
            secondary_endpoint_key=self.secondary_endpoint_key)


def list_qn_a_maker_endpoint_key(authkey: Optional[builtins.str] = None,
                                 hostname: Optional[builtins.str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListQnAMakerEndpointKeyResult:
    """
    Lists the QnA Maker endpoint keys

    Uses Azure REST API version 2023-09-15-preview.

    Other available API versions: 2022-09-15. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native botservice [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param builtins.str authkey: Subscription key which provides access to this API.
    :param builtins.str hostname: the host name of the QnA Maker endpoint
    """
    __args__ = dict()
    __args__['authkey'] = authkey
    __args__['hostname'] = hostname
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:botservice:listQnAMakerEndpointKey', __args__, opts=opts, typ=ListQnAMakerEndpointKeyResult).value

    return AwaitableListQnAMakerEndpointKeyResult(
        installed_version=pulumi.get(__ret__, 'installed_version'),
        last_stable_version=pulumi.get(__ret__, 'last_stable_version'),
        primary_endpoint_key=pulumi.get(__ret__, 'primary_endpoint_key'),
        secondary_endpoint_key=pulumi.get(__ret__, 'secondary_endpoint_key'))
def list_qn_a_maker_endpoint_key_output(authkey: Optional[pulumi.Input[Optional[builtins.str]]] = None,
                                        hostname: Optional[pulumi.Input[Optional[builtins.str]]] = None,
                                        opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[ListQnAMakerEndpointKeyResult]:
    """
    Lists the QnA Maker endpoint keys

    Uses Azure REST API version 2023-09-15-preview.

    Other available API versions: 2022-09-15. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native botservice [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param builtins.str authkey: Subscription key which provides access to this API.
    :param builtins.str hostname: the host name of the QnA Maker endpoint
    """
    __args__ = dict()
    __args__['authkey'] = authkey
    __args__['hostname'] = hostname
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('azure-native:botservice:listQnAMakerEndpointKey', __args__, opts=opts, typ=ListQnAMakerEndpointKeyResult)
    return __ret__.apply(lambda __response__: ListQnAMakerEndpointKeyResult(
        installed_version=pulumi.get(__response__, 'installed_version'),
        last_stable_version=pulumi.get(__response__, 'last_stable_version'),
        primary_endpoint_key=pulumi.get(__response__, 'primary_endpoint_key'),
        secondary_endpoint_key=pulumi.get(__response__, 'secondary_endpoint_key')))
