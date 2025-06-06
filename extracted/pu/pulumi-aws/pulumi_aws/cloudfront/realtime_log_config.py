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
from ._inputs import *

__all__ = ['RealtimeLogConfigArgs', 'RealtimeLogConfig']

@pulumi.input_type
class RealtimeLogConfigArgs:
    def __init__(__self__, *,
                 endpoint: pulumi.Input['RealtimeLogConfigEndpointArgs'],
                 fields: pulumi.Input[Sequence[pulumi.Input[builtins.str]]],
                 sampling_rate: pulumi.Input[builtins.int],
                 name: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a RealtimeLogConfig resource.
        :param pulumi.Input['RealtimeLogConfigEndpointArgs'] endpoint: The Amazon Kinesis data streams where real-time log data is sent.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] fields: The fields that are included in each real-time log record. See the [AWS documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html#understand-real-time-log-config-fields) for supported values.
        :param pulumi.Input[builtins.int] sampling_rate: The sampling rate for this real-time log configuration. The sampling rate determines the percentage of viewer requests that are represented in the real-time log data. An integer between `1` and `100`, inclusive.
        :param pulumi.Input[builtins.str] name: The unique name to identify this real-time log configuration.
        """
        pulumi.set(__self__, "endpoint", endpoint)
        pulumi.set(__self__, "fields", fields)
        pulumi.set(__self__, "sampling_rate", sampling_rate)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Input['RealtimeLogConfigEndpointArgs']:
        """
        The Amazon Kinesis data streams where real-time log data is sent.
        """
        return pulumi.get(self, "endpoint")

    @endpoint.setter
    def endpoint(self, value: pulumi.Input['RealtimeLogConfigEndpointArgs']):
        pulumi.set(self, "endpoint", value)

    @property
    @pulumi.getter
    def fields(self) -> pulumi.Input[Sequence[pulumi.Input[builtins.str]]]:
        """
        The fields that are included in each real-time log record. See the [AWS documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html#understand-real-time-log-config-fields) for supported values.
        """
        return pulumi.get(self, "fields")

    @fields.setter
    def fields(self, value: pulumi.Input[Sequence[pulumi.Input[builtins.str]]]):
        pulumi.set(self, "fields", value)

    @property
    @pulumi.getter(name="samplingRate")
    def sampling_rate(self) -> pulumi.Input[builtins.int]:
        """
        The sampling rate for this real-time log configuration. The sampling rate determines the percentage of viewer requests that are represented in the real-time log data. An integer between `1` and `100`, inclusive.
        """
        return pulumi.get(self, "sampling_rate")

    @sampling_rate.setter
    def sampling_rate(self, value: pulumi.Input[builtins.int]):
        pulumi.set(self, "sampling_rate", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The unique name to identify this real-time log configuration.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _RealtimeLogConfigState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[builtins.str]] = None,
                 endpoint: Optional[pulumi.Input['RealtimeLogConfigEndpointArgs']] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 sampling_rate: Optional[pulumi.Input[builtins.int]] = None):
        """
        Input properties used for looking up and filtering RealtimeLogConfig resources.
        :param pulumi.Input[builtins.str] arn: The ARN (Amazon Resource Name) of the CloudFront real-time log configuration.
        :param pulumi.Input['RealtimeLogConfigEndpointArgs'] endpoint: The Amazon Kinesis data streams where real-time log data is sent.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] fields: The fields that are included in each real-time log record. See the [AWS documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html#understand-real-time-log-config-fields) for supported values.
        :param pulumi.Input[builtins.str] name: The unique name to identify this real-time log configuration.
        :param pulumi.Input[builtins.int] sampling_rate: The sampling rate for this real-time log configuration. The sampling rate determines the percentage of viewer requests that are represented in the real-time log data. An integer between `1` and `100`, inclusive.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if endpoint is not None:
            pulumi.set(__self__, "endpoint", endpoint)
        if fields is not None:
            pulumi.set(__self__, "fields", fields)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if sampling_rate is not None:
            pulumi.set(__self__, "sampling_rate", sampling_rate)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The ARN (Amazon Resource Name) of the CloudFront real-time log configuration.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input['RealtimeLogConfigEndpointArgs']]:
        """
        The Amazon Kinesis data streams where real-time log data is sent.
        """
        return pulumi.get(self, "endpoint")

    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input['RealtimeLogConfigEndpointArgs']]):
        pulumi.set(self, "endpoint", value)

    @property
    @pulumi.getter
    def fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]:
        """
        The fields that are included in each real-time log record. See the [AWS documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html#understand-real-time-log-config-fields) for supported values.
        """
        return pulumi.get(self, "fields")

    @fields.setter
    def fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "fields", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The unique name to identify this real-time log configuration.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="samplingRate")
    def sampling_rate(self) -> Optional[pulumi.Input[builtins.int]]:
        """
        The sampling rate for this real-time log configuration. The sampling rate determines the percentage of viewer requests that are represented in the real-time log data. An integer between `1` and `100`, inclusive.
        """
        return pulumi.get(self, "sampling_rate")

    @sampling_rate.setter
    def sampling_rate(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "sampling_rate", value)


@pulumi.type_token("aws:cloudfront/realtimeLogConfig:RealtimeLogConfig")
class RealtimeLogConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 endpoint: Optional[pulumi.Input[Union['RealtimeLogConfigEndpointArgs', 'RealtimeLogConfigEndpointArgsDict']]] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 sampling_rate: Optional[pulumi.Input[builtins.int]] = None,
                 __props__=None):
        """
        Provides a CloudFront real-time log configuration resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        assume_role = aws.iam.get_policy_document(statements=[{
            "effect": "Allow",
            "principals": [{
                "type": "Service",
                "identifiers": ["cloudfront.amazonaws.com"],
            }],
            "actions": ["sts:AssumeRole"],
        }])
        example_role = aws.iam.Role("example",
            name="cloudfront-realtime-log-config-example",
            assume_role_policy=assume_role.json)
        example = aws.iam.get_policy_document(statements=[{
            "effect": "Allow",
            "actions": [
                "kinesis:DescribeStreamSummary",
                "kinesis:DescribeStream",
                "kinesis:PutRecord",
                "kinesis:PutRecords",
            ],
            "resources": [example_aws_kinesis_stream["arn"]],
        }])
        example_role_policy = aws.iam.RolePolicy("example",
            name="cloudfront-realtime-log-config-example",
            role=example_role.id,
            policy=example.json)
        example_realtime_log_config = aws.cloudfront.RealtimeLogConfig("example",
            name="example",
            sampling_rate=75,
            fields=[
                "timestamp",
                "c-ip",
            ],
            endpoint={
                "stream_type": "Kinesis",
                "kinesis_stream_config": {
                    "role_arn": example_role.arn,
                    "stream_arn": example_aws_kinesis_stream["arn"],
                },
            },
            opts = pulumi.ResourceOptions(depends_on=[example_role_policy]))
        ```

        ## Import

        Using `pulumi import`, import CloudFront real-time log configurations using the ARN. For example:

        ```sh
        $ pulumi import aws:cloudfront/realtimeLogConfig:RealtimeLogConfig example arn:aws:cloudfront::111122223333:realtime-log-config/ExampleNameForRealtimeLogConfig
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['RealtimeLogConfigEndpointArgs', 'RealtimeLogConfigEndpointArgsDict']] endpoint: The Amazon Kinesis data streams where real-time log data is sent.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] fields: The fields that are included in each real-time log record. See the [AWS documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html#understand-real-time-log-config-fields) for supported values.
        :param pulumi.Input[builtins.str] name: The unique name to identify this real-time log configuration.
        :param pulumi.Input[builtins.int] sampling_rate: The sampling rate for this real-time log configuration. The sampling rate determines the percentage of viewer requests that are represented in the real-time log data. An integer between `1` and `100`, inclusive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RealtimeLogConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a CloudFront real-time log configuration resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        assume_role = aws.iam.get_policy_document(statements=[{
            "effect": "Allow",
            "principals": [{
                "type": "Service",
                "identifiers": ["cloudfront.amazonaws.com"],
            }],
            "actions": ["sts:AssumeRole"],
        }])
        example_role = aws.iam.Role("example",
            name="cloudfront-realtime-log-config-example",
            assume_role_policy=assume_role.json)
        example = aws.iam.get_policy_document(statements=[{
            "effect": "Allow",
            "actions": [
                "kinesis:DescribeStreamSummary",
                "kinesis:DescribeStream",
                "kinesis:PutRecord",
                "kinesis:PutRecords",
            ],
            "resources": [example_aws_kinesis_stream["arn"]],
        }])
        example_role_policy = aws.iam.RolePolicy("example",
            name="cloudfront-realtime-log-config-example",
            role=example_role.id,
            policy=example.json)
        example_realtime_log_config = aws.cloudfront.RealtimeLogConfig("example",
            name="example",
            sampling_rate=75,
            fields=[
                "timestamp",
                "c-ip",
            ],
            endpoint={
                "stream_type": "Kinesis",
                "kinesis_stream_config": {
                    "role_arn": example_role.arn,
                    "stream_arn": example_aws_kinesis_stream["arn"],
                },
            },
            opts = pulumi.ResourceOptions(depends_on=[example_role_policy]))
        ```

        ## Import

        Using `pulumi import`, import CloudFront real-time log configurations using the ARN. For example:

        ```sh
        $ pulumi import aws:cloudfront/realtimeLogConfig:RealtimeLogConfig example arn:aws:cloudfront::111122223333:realtime-log-config/ExampleNameForRealtimeLogConfig
        ```

        :param str resource_name: The name of the resource.
        :param RealtimeLogConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RealtimeLogConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 endpoint: Optional[pulumi.Input[Union['RealtimeLogConfigEndpointArgs', 'RealtimeLogConfigEndpointArgsDict']]] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 sampling_rate: Optional[pulumi.Input[builtins.int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RealtimeLogConfigArgs.__new__(RealtimeLogConfigArgs)

            if endpoint is None and not opts.urn:
                raise TypeError("Missing required property 'endpoint'")
            __props__.__dict__["endpoint"] = endpoint
            if fields is None and not opts.urn:
                raise TypeError("Missing required property 'fields'")
            __props__.__dict__["fields"] = fields
            __props__.__dict__["name"] = name
            if sampling_rate is None and not opts.urn:
                raise TypeError("Missing required property 'sampling_rate'")
            __props__.__dict__["sampling_rate"] = sampling_rate
            __props__.__dict__["arn"] = None
        super(RealtimeLogConfig, __self__).__init__(
            'aws:cloudfront/realtimeLogConfig:RealtimeLogConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[builtins.str]] = None,
            endpoint: Optional[pulumi.Input[Union['RealtimeLogConfigEndpointArgs', 'RealtimeLogConfigEndpointArgsDict']]] = None,
            fields: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
            name: Optional[pulumi.Input[builtins.str]] = None,
            sampling_rate: Optional[pulumi.Input[builtins.int]] = None) -> 'RealtimeLogConfig':
        """
        Get an existing RealtimeLogConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] arn: The ARN (Amazon Resource Name) of the CloudFront real-time log configuration.
        :param pulumi.Input[Union['RealtimeLogConfigEndpointArgs', 'RealtimeLogConfigEndpointArgsDict']] endpoint: The Amazon Kinesis data streams where real-time log data is sent.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] fields: The fields that are included in each real-time log record. See the [AWS documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html#understand-real-time-log-config-fields) for supported values.
        :param pulumi.Input[builtins.str] name: The unique name to identify this real-time log configuration.
        :param pulumi.Input[builtins.int] sampling_rate: The sampling rate for this real-time log configuration. The sampling rate determines the percentage of viewer requests that are represented in the real-time log data. An integer between `1` and `100`, inclusive.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RealtimeLogConfigState.__new__(_RealtimeLogConfigState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["endpoint"] = endpoint
        __props__.__dict__["fields"] = fields
        __props__.__dict__["name"] = name
        __props__.__dict__["sampling_rate"] = sampling_rate
        return RealtimeLogConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[builtins.str]:
        """
        The ARN (Amazon Resource Name) of the CloudFront real-time log configuration.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output['outputs.RealtimeLogConfigEndpoint']:
        """
        The Amazon Kinesis data streams where real-time log data is sent.
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter
    def fields(self) -> pulumi.Output[Sequence[builtins.str]]:
        """
        The fields that are included in each real-time log record. See the [AWS documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html#understand-real-time-log-config-fields) for supported values.
        """
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        The unique name to identify this real-time log configuration.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="samplingRate")
    def sampling_rate(self) -> pulumi.Output[builtins.int]:
        """
        The sampling rate for this real-time log configuration. The sampling rate determines the percentage of viewer requests that are represented in the real-time log data. An integer between `1` and `100`, inclusive.
        """
        return pulumi.get(self, "sampling_rate")

