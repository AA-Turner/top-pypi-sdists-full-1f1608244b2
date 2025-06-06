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

__all__ = ['EventInvokeConfigArgs', 'EventInvokeConfig']

@pulumi.input_type
class EventInvokeConfigArgs:
    def __init__(__self__, *,
                 function_name: pulumi.Input[builtins.str],
                 qualifier: pulumi.Input[builtins.str],
                 destination_config: Optional[pulumi.Input['EventInvokeConfigDestinationConfigArgs']] = None,
                 maximum_event_age_in_seconds: Optional[pulumi.Input[builtins.int]] = None,
                 maximum_retry_attempts: Optional[pulumi.Input[builtins.int]] = None):
        """
        The set of arguments for constructing a EventInvokeConfig resource.
        :param pulumi.Input[builtins.str] function_name: The name of the Lambda function.
        :param pulumi.Input[builtins.str] qualifier: The identifier of a version or alias.
        :param pulumi.Input['EventInvokeConfigDestinationConfigArgs'] destination_config: A destination for events after they have been sent to a function for processing.
               
               **Destinations** - *Function* - The Amazon Resource Name (ARN) of a Lambda function.
               - *Queue* - The ARN of a standard SQS queue.
               - *Bucket* - The ARN of an Amazon S3 bucket.
               - *Topic* - The ARN of a standard SNS topic.
               - *Event Bus* - The ARN of an Amazon EventBridge event bus.
               
               > S3 buckets are supported only for on-failure destinations. To retain records of successful invocations, use another destination type.
        :param pulumi.Input[builtins.int] maximum_event_age_in_seconds: The maximum age of a request that Lambda sends to a function for processing.
        :param pulumi.Input[builtins.int] maximum_retry_attempts: The maximum number of times to retry when the function returns an error.
        """
        pulumi.set(__self__, "function_name", function_name)
        pulumi.set(__self__, "qualifier", qualifier)
        if destination_config is not None:
            pulumi.set(__self__, "destination_config", destination_config)
        if maximum_event_age_in_seconds is not None:
            pulumi.set(__self__, "maximum_event_age_in_seconds", maximum_event_age_in_seconds)
        if maximum_retry_attempts is not None:
            pulumi.set(__self__, "maximum_retry_attempts", maximum_retry_attempts)

    @property
    @pulumi.getter(name="functionName")
    def function_name(self) -> pulumi.Input[builtins.str]:
        """
        The name of the Lambda function.
        """
        return pulumi.get(self, "function_name")

    @function_name.setter
    def function_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "function_name", value)

    @property
    @pulumi.getter
    def qualifier(self) -> pulumi.Input[builtins.str]:
        """
        The identifier of a version or alias.
        """
        return pulumi.get(self, "qualifier")

    @qualifier.setter
    def qualifier(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "qualifier", value)

    @property
    @pulumi.getter(name="destinationConfig")
    def destination_config(self) -> Optional[pulumi.Input['EventInvokeConfigDestinationConfigArgs']]:
        """
        A destination for events after they have been sent to a function for processing.

        **Destinations** - *Function* - The Amazon Resource Name (ARN) of a Lambda function.
        - *Queue* - The ARN of a standard SQS queue.
        - *Bucket* - The ARN of an Amazon S3 bucket.
        - *Topic* - The ARN of a standard SNS topic.
        - *Event Bus* - The ARN of an Amazon EventBridge event bus.

        > S3 buckets are supported only for on-failure destinations. To retain records of successful invocations, use another destination type.
        """
        return pulumi.get(self, "destination_config")

    @destination_config.setter
    def destination_config(self, value: Optional[pulumi.Input['EventInvokeConfigDestinationConfigArgs']]):
        pulumi.set(self, "destination_config", value)

    @property
    @pulumi.getter(name="maximumEventAgeInSeconds")
    def maximum_event_age_in_seconds(self) -> Optional[pulumi.Input[builtins.int]]:
        """
        The maximum age of a request that Lambda sends to a function for processing.
        """
        return pulumi.get(self, "maximum_event_age_in_seconds")

    @maximum_event_age_in_seconds.setter
    def maximum_event_age_in_seconds(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "maximum_event_age_in_seconds", value)

    @property
    @pulumi.getter(name="maximumRetryAttempts")
    def maximum_retry_attempts(self) -> Optional[pulumi.Input[builtins.int]]:
        """
        The maximum number of times to retry when the function returns an error.
        """
        return pulumi.get(self, "maximum_retry_attempts")

    @maximum_retry_attempts.setter
    def maximum_retry_attempts(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "maximum_retry_attempts", value)


@pulumi.type_token("aws-native:lambda:EventInvokeConfig")
class EventInvokeConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destination_config: Optional[pulumi.Input[Union['EventInvokeConfigDestinationConfigArgs', 'EventInvokeConfigDestinationConfigArgsDict']]] = None,
                 function_name: Optional[pulumi.Input[builtins.str]] = None,
                 maximum_event_age_in_seconds: Optional[pulumi.Input[builtins.int]] = None,
                 maximum_retry_attempts: Optional[pulumi.Input[builtins.int]] = None,
                 qualifier: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        The AWS::Lambda::EventInvokeConfig resource configures options for asynchronous invocation on a version or an alias.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['EventInvokeConfigDestinationConfigArgs', 'EventInvokeConfigDestinationConfigArgsDict']] destination_config: A destination for events after they have been sent to a function for processing.
               
               **Destinations** - *Function* - The Amazon Resource Name (ARN) of a Lambda function.
               - *Queue* - The ARN of a standard SQS queue.
               - *Bucket* - The ARN of an Amazon S3 bucket.
               - *Topic* - The ARN of a standard SNS topic.
               - *Event Bus* - The ARN of an Amazon EventBridge event bus.
               
               > S3 buckets are supported only for on-failure destinations. To retain records of successful invocations, use another destination type.
        :param pulumi.Input[builtins.str] function_name: The name of the Lambda function.
        :param pulumi.Input[builtins.int] maximum_event_age_in_seconds: The maximum age of a request that Lambda sends to a function for processing.
        :param pulumi.Input[builtins.int] maximum_retry_attempts: The maximum number of times to retry when the function returns an error.
        :param pulumi.Input[builtins.str] qualifier: The identifier of a version or alias.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EventInvokeConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::Lambda::EventInvokeConfig resource configures options for asynchronous invocation on a version or an alias.

        :param str resource_name: The name of the resource.
        :param EventInvokeConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EventInvokeConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destination_config: Optional[pulumi.Input[Union['EventInvokeConfigDestinationConfigArgs', 'EventInvokeConfigDestinationConfigArgsDict']]] = None,
                 function_name: Optional[pulumi.Input[builtins.str]] = None,
                 maximum_event_age_in_seconds: Optional[pulumi.Input[builtins.int]] = None,
                 maximum_retry_attempts: Optional[pulumi.Input[builtins.int]] = None,
                 qualifier: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EventInvokeConfigArgs.__new__(EventInvokeConfigArgs)

            __props__.__dict__["destination_config"] = destination_config
            if function_name is None and not opts.urn:
                raise TypeError("Missing required property 'function_name'")
            __props__.__dict__["function_name"] = function_name
            __props__.__dict__["maximum_event_age_in_seconds"] = maximum_event_age_in_seconds
            __props__.__dict__["maximum_retry_attempts"] = maximum_retry_attempts
            if qualifier is None and not opts.urn:
                raise TypeError("Missing required property 'qualifier'")
            __props__.__dict__["qualifier"] = qualifier
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["functionName", "qualifier"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(EventInvokeConfig, __self__).__init__(
            'aws-native:lambda:EventInvokeConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EventInvokeConfig':
        """
        Get an existing EventInvokeConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EventInvokeConfigArgs.__new__(EventInvokeConfigArgs)

        __props__.__dict__["destination_config"] = None
        __props__.__dict__["function_name"] = None
        __props__.__dict__["maximum_event_age_in_seconds"] = None
        __props__.__dict__["maximum_retry_attempts"] = None
        __props__.__dict__["qualifier"] = None
        return EventInvokeConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="destinationConfig")
    def destination_config(self) -> pulumi.Output[Optional['outputs.EventInvokeConfigDestinationConfig']]:
        """
        A destination for events after they have been sent to a function for processing.

        **Destinations** - *Function* - The Amazon Resource Name (ARN) of a Lambda function.
        - *Queue* - The ARN of a standard SQS queue.
        - *Bucket* - The ARN of an Amazon S3 bucket.
        - *Topic* - The ARN of a standard SNS topic.
        - *Event Bus* - The ARN of an Amazon EventBridge event bus.

        > S3 buckets are supported only for on-failure destinations. To retain records of successful invocations, use another destination type.
        """
        return pulumi.get(self, "destination_config")

    @property
    @pulumi.getter(name="functionName")
    def function_name(self) -> pulumi.Output[builtins.str]:
        """
        The name of the Lambda function.
        """
        return pulumi.get(self, "function_name")

    @property
    @pulumi.getter(name="maximumEventAgeInSeconds")
    def maximum_event_age_in_seconds(self) -> pulumi.Output[Optional[builtins.int]]:
        """
        The maximum age of a request that Lambda sends to a function for processing.
        """
        return pulumi.get(self, "maximum_event_age_in_seconds")

    @property
    @pulumi.getter(name="maximumRetryAttempts")
    def maximum_retry_attempts(self) -> pulumi.Output[Optional[builtins.int]]:
        """
        The maximum number of times to retry when the function returns an error.
        """
        return pulumi.get(self, "maximum_retry_attempts")

    @property
    @pulumi.getter
    def qualifier(self) -> pulumi.Output[builtins.str]:
        """
        The identifier of a version or alias.
        """
        return pulumi.get(self, "qualifier")

