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
    'GetResponseHeadersPolicyResult',
    'AwaitableGetResponseHeadersPolicyResult',
    'get_response_headers_policy',
    'get_response_headers_policy_output',
]

@pulumi.output_type
class GetResponseHeadersPolicyResult:
    def __init__(__self__, id=None, last_modified_time=None, response_headers_policy_config=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_modified_time and not isinstance(last_modified_time, str):
            raise TypeError("Expected argument 'last_modified_time' to be a str")
        pulumi.set(__self__, "last_modified_time", last_modified_time)
        if response_headers_policy_config and not isinstance(response_headers_policy_config, dict):
            raise TypeError("Expected argument 'response_headers_policy_config' to be a dict")
        pulumi.set(__self__, "response_headers_policy_config", response_headers_policy_config)

    @property
    @pulumi.getter
    def id(self) -> Optional[builtins.str]:
        """
        The unique identifier for the response headers policy. For example: `57f99797-3b20-4e1b-a728-27972a74082a` .
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[builtins.str]:
        """
        The date and time when the response headers policy was last modified.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter(name="responseHeadersPolicyConfig")
    def response_headers_policy_config(self) -> Optional['outputs.ResponseHeadersPolicyConfig']:
        """
        A response headers policy configuration.
        """
        return pulumi.get(self, "response_headers_policy_config")


class AwaitableGetResponseHeadersPolicyResult(GetResponseHeadersPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResponseHeadersPolicyResult(
            id=self.id,
            last_modified_time=self.last_modified_time,
            response_headers_policy_config=self.response_headers_policy_config)


def get_response_headers_policy(id: Optional[builtins.str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResponseHeadersPolicyResult:
    """
    A response headers policy.
     A response headers policy contains information about a set of HTTP response headers.
     After you create a response headers policy, you can use its ID to attach it to one or more cache behaviors in a CloudFront distribution. When it's attached to a cache behavior, the response headers policy affects the HTTP headers that CloudFront includes in HTTP responses to requests that match the cache behavior. CloudFront adds or removes response headers according to the configuration of the response headers policy.
     For more information, see [Adding or removing HTTP headers in CloudFront responses](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/modifying-response-headers.html) in the *Amazon CloudFront Developer Guide*.


    :param builtins.str id: The unique identifier for the response headers policy. For example: `57f99797-3b20-4e1b-a728-27972a74082a` .
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:cloudfront:getResponseHeadersPolicy', __args__, opts=opts, typ=GetResponseHeadersPolicyResult).value

    return AwaitableGetResponseHeadersPolicyResult(
        id=pulumi.get(__ret__, 'id'),
        last_modified_time=pulumi.get(__ret__, 'last_modified_time'),
        response_headers_policy_config=pulumi.get(__ret__, 'response_headers_policy_config'))
def get_response_headers_policy_output(id: Optional[pulumi.Input[builtins.str]] = None,
                                       opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetResponseHeadersPolicyResult]:
    """
    A response headers policy.
     A response headers policy contains information about a set of HTTP response headers.
     After you create a response headers policy, you can use its ID to attach it to one or more cache behaviors in a CloudFront distribution. When it's attached to a cache behavior, the response headers policy affects the HTTP headers that CloudFront includes in HTTP responses to requests that match the cache behavior. CloudFront adds or removes response headers according to the configuration of the response headers policy.
     For more information, see [Adding or removing HTTP headers in CloudFront responses](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/modifying-response-headers.html) in the *Amazon CloudFront Developer Guide*.


    :param builtins.str id: The unique identifier for the response headers policy. For example: `57f99797-3b20-4e1b-a728-27972a74082a` .
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:cloudfront:getResponseHeadersPolicy', __args__, opts=opts, typ=GetResponseHeadersPolicyResult)
    return __ret__.apply(lambda __response__: GetResponseHeadersPolicyResult(
        id=pulumi.get(__response__, 'id'),
        last_modified_time=pulumi.get(__response__, 'last_modified_time'),
        response_headers_policy_config=pulumi.get(__response__, 'response_headers_policy_config')))
