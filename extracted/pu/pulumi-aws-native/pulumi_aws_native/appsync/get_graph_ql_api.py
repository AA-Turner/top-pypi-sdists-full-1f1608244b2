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
from .. import outputs as _root_outputs

__all__ = [
    'GetGraphQlApiResult',
    'AwaitableGetGraphQlApiResult',
    'get_graph_ql_api',
    'get_graph_ql_api_output',
]

@pulumi.output_type
class GetGraphQlApiResult:
    def __init__(__self__, additional_authentication_providers=None, api_id=None, api_type=None, arn=None, authentication_type=None, enhanced_metrics_config=None, environment_variables=None, graph_ql_dns=None, graph_ql_endpoint_arn=None, graph_ql_url=None, introspection_config=None, lambda_authorizer_config=None, log_config=None, merged_api_execution_role_arn=None, name=None, open_id_connect_config=None, owner_contact=None, query_depth_limit=None, realtime_dns=None, realtime_url=None, resolver_count_limit=None, tags=None, user_pool_config=None, visibility=None, xray_enabled=None):
        if additional_authentication_providers and not isinstance(additional_authentication_providers, list):
            raise TypeError("Expected argument 'additional_authentication_providers' to be a list")
        pulumi.set(__self__, "additional_authentication_providers", additional_authentication_providers)
        if api_id and not isinstance(api_id, str):
            raise TypeError("Expected argument 'api_id' to be a str")
        pulumi.set(__self__, "api_id", api_id)
        if api_type and not isinstance(api_type, str):
            raise TypeError("Expected argument 'api_type' to be a str")
        pulumi.set(__self__, "api_type", api_type)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if authentication_type and not isinstance(authentication_type, str):
            raise TypeError("Expected argument 'authentication_type' to be a str")
        pulumi.set(__self__, "authentication_type", authentication_type)
        if enhanced_metrics_config and not isinstance(enhanced_metrics_config, dict):
            raise TypeError("Expected argument 'enhanced_metrics_config' to be a dict")
        pulumi.set(__self__, "enhanced_metrics_config", enhanced_metrics_config)
        if environment_variables and not isinstance(environment_variables, dict):
            raise TypeError("Expected argument 'environment_variables' to be a dict")
        pulumi.set(__self__, "environment_variables", environment_variables)
        if graph_ql_dns and not isinstance(graph_ql_dns, str):
            raise TypeError("Expected argument 'graph_ql_dns' to be a str")
        pulumi.set(__self__, "graph_ql_dns", graph_ql_dns)
        if graph_ql_endpoint_arn and not isinstance(graph_ql_endpoint_arn, str):
            raise TypeError("Expected argument 'graph_ql_endpoint_arn' to be a str")
        pulumi.set(__self__, "graph_ql_endpoint_arn", graph_ql_endpoint_arn)
        if graph_ql_url and not isinstance(graph_ql_url, str):
            raise TypeError("Expected argument 'graph_ql_url' to be a str")
        pulumi.set(__self__, "graph_ql_url", graph_ql_url)
        if introspection_config and not isinstance(introspection_config, str):
            raise TypeError("Expected argument 'introspection_config' to be a str")
        pulumi.set(__self__, "introspection_config", introspection_config)
        if lambda_authorizer_config and not isinstance(lambda_authorizer_config, dict):
            raise TypeError("Expected argument 'lambda_authorizer_config' to be a dict")
        pulumi.set(__self__, "lambda_authorizer_config", lambda_authorizer_config)
        if log_config and not isinstance(log_config, dict):
            raise TypeError("Expected argument 'log_config' to be a dict")
        pulumi.set(__self__, "log_config", log_config)
        if merged_api_execution_role_arn and not isinstance(merged_api_execution_role_arn, str):
            raise TypeError("Expected argument 'merged_api_execution_role_arn' to be a str")
        pulumi.set(__self__, "merged_api_execution_role_arn", merged_api_execution_role_arn)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if open_id_connect_config and not isinstance(open_id_connect_config, dict):
            raise TypeError("Expected argument 'open_id_connect_config' to be a dict")
        pulumi.set(__self__, "open_id_connect_config", open_id_connect_config)
        if owner_contact and not isinstance(owner_contact, str):
            raise TypeError("Expected argument 'owner_contact' to be a str")
        pulumi.set(__self__, "owner_contact", owner_contact)
        if query_depth_limit and not isinstance(query_depth_limit, int):
            raise TypeError("Expected argument 'query_depth_limit' to be a int")
        pulumi.set(__self__, "query_depth_limit", query_depth_limit)
        if realtime_dns and not isinstance(realtime_dns, str):
            raise TypeError("Expected argument 'realtime_dns' to be a str")
        pulumi.set(__self__, "realtime_dns", realtime_dns)
        if realtime_url and not isinstance(realtime_url, str):
            raise TypeError("Expected argument 'realtime_url' to be a str")
        pulumi.set(__self__, "realtime_url", realtime_url)
        if resolver_count_limit and not isinstance(resolver_count_limit, int):
            raise TypeError("Expected argument 'resolver_count_limit' to be a int")
        pulumi.set(__self__, "resolver_count_limit", resolver_count_limit)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if user_pool_config and not isinstance(user_pool_config, dict):
            raise TypeError("Expected argument 'user_pool_config' to be a dict")
        pulumi.set(__self__, "user_pool_config", user_pool_config)
        if visibility and not isinstance(visibility, str):
            raise TypeError("Expected argument 'visibility' to be a str")
        pulumi.set(__self__, "visibility", visibility)
        if xray_enabled and not isinstance(xray_enabled, bool):
            raise TypeError("Expected argument 'xray_enabled' to be a bool")
        pulumi.set(__self__, "xray_enabled", xray_enabled)

    @property
    @pulumi.getter(name="additionalAuthenticationProviders")
    def additional_authentication_providers(self) -> Optional[Sequence['outputs.GraphQlApiAdditionalAuthenticationProvider']]:
        """
        A list of additional authentication providers for the GraphqlApi API.
        """
        return pulumi.get(self, "additional_authentication_providers")

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> Optional[builtins.str]:
        """
        Unique AWS AppSync GraphQL API identifier.
        """
        return pulumi.get(self, "api_id")

    @property
    @pulumi.getter(name="apiType")
    def api_type(self) -> Optional[builtins.str]:
        """
        The value that indicates whether the GraphQL API is a standard API (GRAPHQL) or merged API (MERGED).
        """
        return pulumi.get(self, "api_type")

    @property
    @pulumi.getter
    def arn(self) -> Optional[builtins.str]:
        """
        The Amazon Resource Name (ARN) of the API key
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> Optional[builtins.str]:
        """
        Security configuration for your GraphQL API
        """
        return pulumi.get(self, "authentication_type")

    @property
    @pulumi.getter(name="enhancedMetricsConfig")
    def enhanced_metrics_config(self) -> Optional['outputs.GraphQlApiEnhancedMetricsConfig']:
        """
        Enables and controls the enhanced metrics feature. Enhanced metrics emit granular data on API usage and performance such as AppSync request and error counts, latency, and cache hits/misses. All enhanced metric data is sent to your CloudWatch account, and you can configure the types of data that will be sent.
        """
        return pulumi.get(self, "enhanced_metrics_config")

    @property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[Mapping[str, builtins.str]]:
        """
        A map containing the list of resources with their properties and environment variables.
        """
        return pulumi.get(self, "environment_variables")

    @property
    @pulumi.getter(name="graphQlDns")
    def graph_ql_dns(self) -> Optional[builtins.str]:
        """
        The fully qualified domain name (FQDN) of the endpoint URL of your GraphQL API.
        """
        return pulumi.get(self, "graph_ql_dns")

    @property
    @pulumi.getter(name="graphQlEndpointArn")
    def graph_ql_endpoint_arn(self) -> Optional[builtins.str]:
        """
        The GraphQL endpoint ARN.
        """
        return pulumi.get(self, "graph_ql_endpoint_arn")

    @property
    @pulumi.getter(name="graphQlUrl")
    def graph_ql_url(self) -> Optional[builtins.str]:
        """
        The Endpoint URL of your GraphQL API.
        """
        return pulumi.get(self, "graph_ql_url")

    @property
    @pulumi.getter(name="introspectionConfig")
    def introspection_config(self) -> Optional[builtins.str]:
        """
        Sets the value of the GraphQL API to enable (ENABLED) or disable (DISABLED) introspection. If no value is provided, the introspection configuration will be set to ENABLED by default. This field will produce an error if the operation attempts to use the introspection feature while this field is disabled.
        """
        return pulumi.get(self, "introspection_config")

    @property
    @pulumi.getter(name="lambdaAuthorizerConfig")
    def lambda_authorizer_config(self) -> Optional['outputs.GraphQlApiLambdaAuthorizerConfig']:
        """
        A LambdaAuthorizerConfig holds configuration on how to authorize AWS AppSync API access when using the AWS_LAMBDA authorizer mode. Be aware that an AWS AppSync API may have only one Lambda authorizer configured at a time.
        """
        return pulumi.get(self, "lambda_authorizer_config")

    @property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> Optional['outputs.GraphQlApiLogConfig']:
        """
        The Amazon CloudWatch Logs configuration.
        """
        return pulumi.get(self, "log_config")

    @property
    @pulumi.getter(name="mergedApiExecutionRoleArn")
    def merged_api_execution_role_arn(self) -> Optional[builtins.str]:
        """
        The AWS Identity and Access Management service role ARN for a merged API. 
        """
        return pulumi.get(self, "merged_api_execution_role_arn")

    @property
    @pulumi.getter
    def name(self) -> Optional[builtins.str]:
        """
        The API name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="openIdConnectConfig")
    def open_id_connect_config(self) -> Optional['outputs.GraphQlApiOpenIdConnectConfig']:
        """
        The OpenID Connect configuration.
        """
        return pulumi.get(self, "open_id_connect_config")

    @property
    @pulumi.getter(name="ownerContact")
    def owner_contact(self) -> Optional[builtins.str]:
        """
        The owner contact information for an API resource.
        """
        return pulumi.get(self, "owner_contact")

    @property
    @pulumi.getter(name="queryDepthLimit")
    def query_depth_limit(self) -> Optional[builtins.int]:
        """
        The maximum depth a query can have in a single request. Depth refers to the amount of nested levels allowed in the body of query.
        """
        return pulumi.get(self, "query_depth_limit")

    @property
    @pulumi.getter(name="realtimeDns")
    def realtime_dns(self) -> Optional[builtins.str]:
        """
        The fully qualified domain name (FQDN) of the real-time endpoint URL of your GraphQL API.
        """
        return pulumi.get(self, "realtime_dns")

    @property
    @pulumi.getter(name="realtimeUrl")
    def realtime_url(self) -> Optional[builtins.str]:
        """
        The GraphQL API real-time endpoint URL.
        """
        return pulumi.get(self, "realtime_url")

    @property
    @pulumi.getter(name="resolverCountLimit")
    def resolver_count_limit(self) -> Optional[builtins.int]:
        """
        The maximum number of resolvers that can be invoked in a single request.
        """
        return pulumi.get(self, "resolver_count_limit")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        An arbitrary set of tags (key-value pairs) for this GraphQL API.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="userPoolConfig")
    def user_pool_config(self) -> Optional['outputs.GraphQlApiUserPoolConfig']:
        """
        Optional authorization configuration for using Amazon Cognito user pools with your GraphQL endpoint.
        """
        return pulumi.get(self, "user_pool_config")

    @property
    @pulumi.getter
    def visibility(self) -> Optional[builtins.str]:
        """
        Sets the scope of the GraphQL API to public (GLOBAL) or private (PRIVATE). By default, the scope is set to Global if no value is provided.
        """
        return pulumi.get(self, "visibility")

    @property
    @pulumi.getter(name="xrayEnabled")
    def xray_enabled(self) -> Optional[builtins.bool]:
        """
        A flag indicating whether to use AWS X-Ray tracing for this GraphqlApi.
        """
        return pulumi.get(self, "xray_enabled")


class AwaitableGetGraphQlApiResult(GetGraphQlApiResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGraphQlApiResult(
            additional_authentication_providers=self.additional_authentication_providers,
            api_id=self.api_id,
            api_type=self.api_type,
            arn=self.arn,
            authentication_type=self.authentication_type,
            enhanced_metrics_config=self.enhanced_metrics_config,
            environment_variables=self.environment_variables,
            graph_ql_dns=self.graph_ql_dns,
            graph_ql_endpoint_arn=self.graph_ql_endpoint_arn,
            graph_ql_url=self.graph_ql_url,
            introspection_config=self.introspection_config,
            lambda_authorizer_config=self.lambda_authorizer_config,
            log_config=self.log_config,
            merged_api_execution_role_arn=self.merged_api_execution_role_arn,
            name=self.name,
            open_id_connect_config=self.open_id_connect_config,
            owner_contact=self.owner_contact,
            query_depth_limit=self.query_depth_limit,
            realtime_dns=self.realtime_dns,
            realtime_url=self.realtime_url,
            resolver_count_limit=self.resolver_count_limit,
            tags=self.tags,
            user_pool_config=self.user_pool_config,
            visibility=self.visibility,
            xray_enabled=self.xray_enabled)


def get_graph_ql_api(api_id: Optional[builtins.str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGraphQlApiResult:
    """
    Resource Type definition for AWS::AppSync::GraphQLApi


    :param builtins.str api_id: Unique AWS AppSync GraphQL API identifier.
    """
    __args__ = dict()
    __args__['apiId'] = api_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:appsync:getGraphQlApi', __args__, opts=opts, typ=GetGraphQlApiResult).value

    return AwaitableGetGraphQlApiResult(
        additional_authentication_providers=pulumi.get(__ret__, 'additional_authentication_providers'),
        api_id=pulumi.get(__ret__, 'api_id'),
        api_type=pulumi.get(__ret__, 'api_type'),
        arn=pulumi.get(__ret__, 'arn'),
        authentication_type=pulumi.get(__ret__, 'authentication_type'),
        enhanced_metrics_config=pulumi.get(__ret__, 'enhanced_metrics_config'),
        environment_variables=pulumi.get(__ret__, 'environment_variables'),
        graph_ql_dns=pulumi.get(__ret__, 'graph_ql_dns'),
        graph_ql_endpoint_arn=pulumi.get(__ret__, 'graph_ql_endpoint_arn'),
        graph_ql_url=pulumi.get(__ret__, 'graph_ql_url'),
        introspection_config=pulumi.get(__ret__, 'introspection_config'),
        lambda_authorizer_config=pulumi.get(__ret__, 'lambda_authorizer_config'),
        log_config=pulumi.get(__ret__, 'log_config'),
        merged_api_execution_role_arn=pulumi.get(__ret__, 'merged_api_execution_role_arn'),
        name=pulumi.get(__ret__, 'name'),
        open_id_connect_config=pulumi.get(__ret__, 'open_id_connect_config'),
        owner_contact=pulumi.get(__ret__, 'owner_contact'),
        query_depth_limit=pulumi.get(__ret__, 'query_depth_limit'),
        realtime_dns=pulumi.get(__ret__, 'realtime_dns'),
        realtime_url=pulumi.get(__ret__, 'realtime_url'),
        resolver_count_limit=pulumi.get(__ret__, 'resolver_count_limit'),
        tags=pulumi.get(__ret__, 'tags'),
        user_pool_config=pulumi.get(__ret__, 'user_pool_config'),
        visibility=pulumi.get(__ret__, 'visibility'),
        xray_enabled=pulumi.get(__ret__, 'xray_enabled'))
def get_graph_ql_api_output(api_id: Optional[pulumi.Input[builtins.str]] = None,
                            opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetGraphQlApiResult]:
    """
    Resource Type definition for AWS::AppSync::GraphQLApi


    :param builtins.str api_id: Unique AWS AppSync GraphQL API identifier.
    """
    __args__ = dict()
    __args__['apiId'] = api_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:appsync:getGraphQlApi', __args__, opts=opts, typ=GetGraphQlApiResult)
    return __ret__.apply(lambda __response__: GetGraphQlApiResult(
        additional_authentication_providers=pulumi.get(__response__, 'additional_authentication_providers'),
        api_id=pulumi.get(__response__, 'api_id'),
        api_type=pulumi.get(__response__, 'api_type'),
        arn=pulumi.get(__response__, 'arn'),
        authentication_type=pulumi.get(__response__, 'authentication_type'),
        enhanced_metrics_config=pulumi.get(__response__, 'enhanced_metrics_config'),
        environment_variables=pulumi.get(__response__, 'environment_variables'),
        graph_ql_dns=pulumi.get(__response__, 'graph_ql_dns'),
        graph_ql_endpoint_arn=pulumi.get(__response__, 'graph_ql_endpoint_arn'),
        graph_ql_url=pulumi.get(__response__, 'graph_ql_url'),
        introspection_config=pulumi.get(__response__, 'introspection_config'),
        lambda_authorizer_config=pulumi.get(__response__, 'lambda_authorizer_config'),
        log_config=pulumi.get(__response__, 'log_config'),
        merged_api_execution_role_arn=pulumi.get(__response__, 'merged_api_execution_role_arn'),
        name=pulumi.get(__response__, 'name'),
        open_id_connect_config=pulumi.get(__response__, 'open_id_connect_config'),
        owner_contact=pulumi.get(__response__, 'owner_contact'),
        query_depth_limit=pulumi.get(__response__, 'query_depth_limit'),
        realtime_dns=pulumi.get(__response__, 'realtime_dns'),
        realtime_url=pulumi.get(__response__, 'realtime_url'),
        resolver_count_limit=pulumi.get(__response__, 'resolver_count_limit'),
        tags=pulumi.get(__response__, 'tags'),
        user_pool_config=pulumi.get(__response__, 'user_pool_config'),
        visibility=pulumi.get(__response__, 'visibility'),
        xray_enabled=pulumi.get(__response__, 'xray_enabled')))
