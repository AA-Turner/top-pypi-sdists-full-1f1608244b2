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
    'GetLiveTokenResult',
    'AwaitableGetLiveTokenResult',
    'get_live_token',
    'get_live_token_output',
]

@pulumi.output_type
class GetLiveTokenResult:
    """
    The response to a live token query.
    """
    def __init__(__self__, live_token=None):
        if live_token and not isinstance(live_token, str):
            raise TypeError("Expected argument 'live_token' to be a str")
        pulumi.set(__self__, "live_token", live_token)

    @property
    @pulumi.getter(name="liveToken")
    def live_token(self) -> builtins.str:
        """
        JWT token for accessing live metrics stream data.
        """
        return pulumi.get(self, "live_token")


class AwaitableGetLiveTokenResult(GetLiveTokenResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLiveTokenResult(
            live_token=self.live_token)


def get_live_token(resource_uri: Optional[builtins.str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLiveTokenResult:
    """
    **Gets an access token for live metrics stream data.**

    Uses Azure REST API version 2021-10-14.

    Other available API versions: 2020-06-02-preview. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native applicationinsights [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param builtins.str resource_uri: The identifier of the resource.
    """
    __args__ = dict()
    __args__['resourceUri'] = resource_uri
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:applicationinsights:getLiveToken', __args__, opts=opts, typ=GetLiveTokenResult).value

    return AwaitableGetLiveTokenResult(
        live_token=pulumi.get(__ret__, 'live_token'))
def get_live_token_output(resource_uri: Optional[pulumi.Input[builtins.str]] = None,
                          opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetLiveTokenResult]:
    """
    **Gets an access token for live metrics stream data.**

    Uses Azure REST API version 2021-10-14.

    Other available API versions: 2020-06-02-preview. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native applicationinsights [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param builtins.str resource_uri: The identifier of the resource.
    """
    __args__ = dict()
    __args__['resourceUri'] = resource_uri
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('azure-native:applicationinsights:getLiveToken', __args__, opts=opts, typ=GetLiveTokenResult)
    return __ret__.apply(lambda __response__: GetLiveTokenResult(
        live_token=pulumi.get(__response__, 'live_token')))
