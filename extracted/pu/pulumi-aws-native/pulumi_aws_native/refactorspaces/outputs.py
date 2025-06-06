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
    'ApplicationApiGatewayProxyInput',
    'RouteDefaultRouteInput',
    'RouteUriPathRouteInput',
    'ServiceLambdaEndpointInput',
    'ServiceUrlEndpointInput',
]

@pulumi.output_type
class ApplicationApiGatewayProxyInput(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "endpointType":
            suggest = "endpoint_type"
        elif key == "stageName":
            suggest = "stage_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationApiGatewayProxyInput. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationApiGatewayProxyInput.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationApiGatewayProxyInput.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 endpoint_type: Optional['ApplicationApiGatewayEndpointType'] = None,
                 stage_name: Optional[builtins.str] = None):
        """
        :param 'ApplicationApiGatewayEndpointType' endpoint_type: The type of endpoint to use for the API Gateway proxy. If no value is specified in the request, the value is set to `REGIONAL` by default.
               
               If the value is set to `PRIVATE` in the request, this creates a private API endpoint that is isolated from the public internet. The private endpoint can only be accessed by using Amazon Virtual Private Cloud (Amazon VPC) interface endpoints for the Amazon API Gateway that has been granted access. For more information about creating a private connection with Refactor Spaces and interface endpoint ( AWS PrivateLink ) availability, see [Access Refactor Spaces using an interface endpoint ( AWS PrivateLink )](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/vpc-interface-endpoints.html) .
        :param builtins.str stage_name: The name of the API Gateway stage. The name defaults to `prod` .
        """
        if endpoint_type is not None:
            pulumi.set(__self__, "endpoint_type", endpoint_type)
        if stage_name is not None:
            pulumi.set(__self__, "stage_name", stage_name)

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional['ApplicationApiGatewayEndpointType']:
        """
        The type of endpoint to use for the API Gateway proxy. If no value is specified in the request, the value is set to `REGIONAL` by default.

        If the value is set to `PRIVATE` in the request, this creates a private API endpoint that is isolated from the public internet. The private endpoint can only be accessed by using Amazon Virtual Private Cloud (Amazon VPC) interface endpoints for the Amazon API Gateway that has been granted access. For more information about creating a private connection with Refactor Spaces and interface endpoint ( AWS PrivateLink ) availability, see [Access Refactor Spaces using an interface endpoint ( AWS PrivateLink )](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/vpc-interface-endpoints.html) .
        """
        return pulumi.get(self, "endpoint_type")

    @property
    @pulumi.getter(name="stageName")
    def stage_name(self) -> Optional[builtins.str]:
        """
        The name of the API Gateway stage. The name defaults to `prod` .
        """
        return pulumi.get(self, "stage_name")


@pulumi.output_type
class RouteDefaultRouteInput(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "activationState":
            suggest = "activation_state"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RouteDefaultRouteInput. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RouteDefaultRouteInput.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RouteDefaultRouteInput.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 activation_state: 'RouteActivationState'):
        """
        :param 'RouteActivationState' activation_state: If set to `ACTIVE` , traffic is forwarded to this route’s service after the route is created.
        """
        pulumi.set(__self__, "activation_state", activation_state)

    @property
    @pulumi.getter(name="activationState")
    def activation_state(self) -> 'RouteActivationState':
        """
        If set to `ACTIVE` , traffic is forwarded to this route’s service after the route is created.
        """
        return pulumi.get(self, "activation_state")


@pulumi.output_type
class RouteUriPathRouteInput(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "activationState":
            suggest = "activation_state"
        elif key == "appendSourcePath":
            suggest = "append_source_path"
        elif key == "includeChildPaths":
            suggest = "include_child_paths"
        elif key == "sourcePath":
            suggest = "source_path"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RouteUriPathRouteInput. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RouteUriPathRouteInput.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RouteUriPathRouteInput.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 activation_state: 'RouteActivationState',
                 append_source_path: Optional[builtins.bool] = None,
                 include_child_paths: Optional[builtins.bool] = None,
                 methods: Optional[Sequence['RouteMethod']] = None,
                 source_path: Optional[builtins.str] = None):
        """
        :param 'RouteActivationState' activation_state: If set to `ACTIVE` , traffic is forwarded to this route’s service after the route is created.
        :param builtins.bool append_source_path: If set to `true` , this option appends the source path to the service URL endpoint.
        :param builtins.bool include_child_paths: Indicates whether to match all subpaths of the given source path. If this value is `false` , requests must match the source path exactly before they are forwarded to this route's service.
        :param Sequence['RouteMethod'] methods: A list of HTTP methods to match. An empty list matches all values. If a method is present, only HTTP requests using that method are forwarded to this route’s service.
        :param builtins.str source_path: This is the path that Refactor Spaces uses to match traffic. Paths must start with `/` and are relative to the base of the application. To use path parameters in the source path, add a variable in curly braces. For example, the resource path {user} represents a path parameter called 'user'.
        """
        pulumi.set(__self__, "activation_state", activation_state)
        if append_source_path is not None:
            pulumi.set(__self__, "append_source_path", append_source_path)
        if include_child_paths is not None:
            pulumi.set(__self__, "include_child_paths", include_child_paths)
        if methods is not None:
            pulumi.set(__self__, "methods", methods)
        if source_path is not None:
            pulumi.set(__self__, "source_path", source_path)

    @property
    @pulumi.getter(name="activationState")
    def activation_state(self) -> 'RouteActivationState':
        """
        If set to `ACTIVE` , traffic is forwarded to this route’s service after the route is created.
        """
        return pulumi.get(self, "activation_state")

    @property
    @pulumi.getter(name="appendSourcePath")
    def append_source_path(self) -> Optional[builtins.bool]:
        """
        If set to `true` , this option appends the source path to the service URL endpoint.
        """
        return pulumi.get(self, "append_source_path")

    @property
    @pulumi.getter(name="includeChildPaths")
    def include_child_paths(self) -> Optional[builtins.bool]:
        """
        Indicates whether to match all subpaths of the given source path. If this value is `false` , requests must match the source path exactly before they are forwarded to this route's service.
        """
        return pulumi.get(self, "include_child_paths")

    @property
    @pulumi.getter
    def methods(self) -> Optional[Sequence['RouteMethod']]:
        """
        A list of HTTP methods to match. An empty list matches all values. If a method is present, only HTTP requests using that method are forwarded to this route’s service.
        """
        return pulumi.get(self, "methods")

    @property
    @pulumi.getter(name="sourcePath")
    def source_path(self) -> Optional[builtins.str]:
        """
        This is the path that Refactor Spaces uses to match traffic. Paths must start with `/` and are relative to the base of the application. To use path parameters in the source path, add a variable in curly braces. For example, the resource path {user} represents a path parameter called 'user'.
        """
        return pulumi.get(self, "source_path")


@pulumi.output_type
class ServiceLambdaEndpointInput(dict):
    def __init__(__self__, *,
                 arn: builtins.str):
        """
        :param builtins.str arn: The Amazon Resource Name (ARN) of the Lambda function or alias.
        """
        pulumi.set(__self__, "arn", arn)

    @property
    @pulumi.getter
    def arn(self) -> builtins.str:
        """
        The Amazon Resource Name (ARN) of the Lambda function or alias.
        """
        return pulumi.get(self, "arn")


@pulumi.output_type
class ServiceUrlEndpointInput(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "healthUrl":
            suggest = "health_url"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServiceUrlEndpointInput. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceUrlEndpointInput.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceUrlEndpointInput.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 url: builtins.str,
                 health_url: Optional[builtins.str] = None):
        """
        :param builtins.str url: The URL to route traffic to. The URL must be an [rfc3986-formatted URL](https://docs.aws.amazon.com/https://datatracker.ietf.org/doc/html/rfc3986) . If the host is a domain name, the name must be resolvable over the public internet. If the scheme is `https` , the top level domain of the host must be listed in the [IANA root zone database](https://docs.aws.amazon.com/https://www.iana.org/domains/root/db) .
        :param builtins.str health_url: The health check URL of the URL endpoint type. If the URL is a public endpoint, the `HealthUrl` must also be a public endpoint. If the URL is a private endpoint inside a virtual private cloud (VPC), the health URL must also be a private endpoint, and the host must be the same as the URL.
        """
        pulumi.set(__self__, "url", url)
        if health_url is not None:
            pulumi.set(__self__, "health_url", health_url)

    @property
    @pulumi.getter
    def url(self) -> builtins.str:
        """
        The URL to route traffic to. The URL must be an [rfc3986-formatted URL](https://docs.aws.amazon.com/https://datatracker.ietf.org/doc/html/rfc3986) . If the host is a domain name, the name must be resolvable over the public internet. If the scheme is `https` , the top level domain of the host must be listed in the [IANA root zone database](https://docs.aws.amazon.com/https://www.iana.org/domains/root/db) .
        """
        return pulumi.get(self, "url")

    @property
    @pulumi.getter(name="healthUrl")
    def health_url(self) -> Optional[builtins.str]:
        """
        The health check URL of the URL endpoint type. If the URL is a public endpoint, the `HealthUrl` must also be a public endpoint. If the URL is a private endpoint inside a virtual private cloud (VPC), the health URL must also be a private endpoint, and the host must be the same as the URL.
        """
        return pulumi.get(self, "health_url")


