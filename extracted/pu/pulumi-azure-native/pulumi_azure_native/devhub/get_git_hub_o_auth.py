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
    'GetGitHubOAuthResult',
    'AwaitableGetGitHubOAuthResult',
    'get_git_hub_o_auth',
    'get_git_hub_o_auth_output',
]

@pulumi.output_type
class GetGitHubOAuthResult:
    """
    URL used to authorize the Developer Hub GitHub App
    """
    def __init__(__self__, auth_url=None, token=None):
        if auth_url and not isinstance(auth_url, str):
            raise TypeError("Expected argument 'auth_url' to be a str")
        pulumi.set(__self__, "auth_url", auth_url)
        if token and not isinstance(token, str):
            raise TypeError("Expected argument 'token' to be a str")
        pulumi.set(__self__, "token", token)

    @property
    @pulumi.getter(name="authURL")
    def auth_url(self) -> Optional[builtins.str]:
        """
        URL for authorizing the Developer Hub GitHub App
        """
        return pulumi.get(self, "auth_url")

    @property
    @pulumi.getter
    def token(self) -> Optional[builtins.str]:
        """
        OAuth token used to make calls to GitHub
        """
        return pulumi.get(self, "token")


class AwaitableGetGitHubOAuthResult(GetGitHubOAuthResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGitHubOAuthResult(
            auth_url=self.auth_url,
            token=self.token)


def get_git_hub_o_auth(location: Optional[builtins.str] = None,
                       redirect_url: Optional[builtins.str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGitHubOAuthResult:
    """
    URL used to authorize the Developer Hub GitHub App

    Uses Azure REST API version 2023-08-01.

    Other available API versions: 2022-10-11-preview, 2024-05-01-preview, 2024-08-01-preview, 2025-03-01-preview. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native devhub [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param builtins.str location: The name of Azure region.
    :param builtins.str redirect_url: The URL the client will redirect to on successful authentication. If empty, no redirect will occur.
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['redirectUrl'] = redirect_url
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:devhub:getGitHubOAuth', __args__, opts=opts, typ=GetGitHubOAuthResult).value

    return AwaitableGetGitHubOAuthResult(
        auth_url=pulumi.get(__ret__, 'auth_url'),
        token=pulumi.get(__ret__, 'token'))
def get_git_hub_o_auth_output(location: Optional[pulumi.Input[builtins.str]] = None,
                              redirect_url: Optional[pulumi.Input[Optional[builtins.str]]] = None,
                              opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetGitHubOAuthResult]:
    """
    URL used to authorize the Developer Hub GitHub App

    Uses Azure REST API version 2023-08-01.

    Other available API versions: 2022-10-11-preview, 2024-05-01-preview, 2024-08-01-preview, 2025-03-01-preview. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native devhub [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param builtins.str location: The name of Azure region.
    :param builtins.str redirect_url: The URL the client will redirect to on successful authentication. If empty, no redirect will occur.
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['redirectUrl'] = redirect_url
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('azure-native:devhub:getGitHubOAuth', __args__, opts=opts, typ=GetGitHubOAuthResult)
    return __ret__.apply(lambda __response__: GetGitHubOAuthResult(
        auth_url=pulumi.get(__response__, 'auth_url'),
        token=pulumi.get(__response__, 'token')))
