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
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs
from ._inputs import *

__all__ = ['UsagePlanArgs', 'UsagePlan']

@pulumi.input_type
class UsagePlanArgs:
    def __init__(__self__, *,
                 api_stages: Optional[pulumi.Input[Sequence[pulumi.Input['UsagePlanApiStageArgs']]]] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 quota: Optional[pulumi.Input['UsagePlanQuotaSettingsArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None,
                 throttle: Optional[pulumi.Input['UsagePlanThrottleSettingsArgs']] = None,
                 usage_plan_name: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a UsagePlan resource.
        :param pulumi.Input[Sequence[pulumi.Input['UsagePlanApiStageArgs']]] api_stages: The associated API stages of a usage plan.
        :param pulumi.Input[builtins.str] description: The description of a usage plan.
        :param pulumi.Input['UsagePlanQuotaSettingsArgs'] quota: The target maximum number of permitted requests per a given unit time interval.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: The collection of tags. Each tag element is associated with a given resource.
        :param pulumi.Input['UsagePlanThrottleSettingsArgs'] throttle: A map containing method level throttling information for API stage in a usage plan.
        :param pulumi.Input[builtins.str] usage_plan_name: The name of a usage plan.
        """
        if api_stages is not None:
            pulumi.set(__self__, "api_stages", api_stages)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if quota is not None:
            pulumi.set(__self__, "quota", quota)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if throttle is not None:
            pulumi.set(__self__, "throttle", throttle)
        if usage_plan_name is not None:
            pulumi.set(__self__, "usage_plan_name", usage_plan_name)

    @property
    @pulumi.getter(name="apiStages")
    def api_stages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['UsagePlanApiStageArgs']]]]:
        """
        The associated API stages of a usage plan.
        """
        return pulumi.get(self, "api_stages")

    @api_stages.setter
    def api_stages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['UsagePlanApiStageArgs']]]]):
        pulumi.set(self, "api_stages", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The description of a usage plan.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def quota(self) -> Optional[pulumi.Input['UsagePlanQuotaSettingsArgs']]:
        """
        The target maximum number of permitted requests per a given unit time interval.
        """
        return pulumi.get(self, "quota")

    @quota.setter
    def quota(self, value: Optional[pulumi.Input['UsagePlanQuotaSettingsArgs']]):
        pulumi.set(self, "quota", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        The collection of tags. Each tag element is associated with a given resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def throttle(self) -> Optional[pulumi.Input['UsagePlanThrottleSettingsArgs']]:
        """
        A map containing method level throttling information for API stage in a usage plan.
        """
        return pulumi.get(self, "throttle")

    @throttle.setter
    def throttle(self, value: Optional[pulumi.Input['UsagePlanThrottleSettingsArgs']]):
        pulumi.set(self, "throttle", value)

    @property
    @pulumi.getter(name="usagePlanName")
    def usage_plan_name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of a usage plan.
        """
        return pulumi.get(self, "usage_plan_name")

    @usage_plan_name.setter
    def usage_plan_name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "usage_plan_name", value)


@pulumi.type_token("aws-native:apigateway:UsagePlan")
class UsagePlan(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_stages: Optional[pulumi.Input[Sequence[pulumi.Input[Union['UsagePlanApiStageArgs', 'UsagePlanApiStageArgsDict']]]]] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 quota: Optional[pulumi.Input[Union['UsagePlanQuotaSettingsArgs', 'UsagePlanQuotaSettingsArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 throttle: Optional[pulumi.Input[Union['UsagePlanThrottleSettingsArgs', 'UsagePlanThrottleSettingsArgsDict']]] = None,
                 usage_plan_name: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        The ``AWS::ApiGateway::UsagePlan`` resource creates a usage plan for deployed APIs. A usage plan sets a target for the throttling and quota limits on individual client API keys. For more information, see [Creating and Using API Usage Plans in Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html) in the *API Gateway Developer Guide*.
         In some cases clients can exceed the targets that you set. Don’t rely on usage plans to control costs. Consider using [](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) to monitor costs and [](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) to manage API requests.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['UsagePlanApiStageArgs', 'UsagePlanApiStageArgsDict']]]] api_stages: The associated API stages of a usage plan.
        :param pulumi.Input[builtins.str] description: The description of a usage plan.
        :param pulumi.Input[Union['UsagePlanQuotaSettingsArgs', 'UsagePlanQuotaSettingsArgsDict']] quota: The target maximum number of permitted requests per a given unit time interval.
        :param pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]] tags: The collection of tags. Each tag element is associated with a given resource.
        :param pulumi.Input[Union['UsagePlanThrottleSettingsArgs', 'UsagePlanThrottleSettingsArgsDict']] throttle: A map containing method level throttling information for API stage in a usage plan.
        :param pulumi.Input[builtins.str] usage_plan_name: The name of a usage plan.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[UsagePlanArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The ``AWS::ApiGateway::UsagePlan`` resource creates a usage plan for deployed APIs. A usage plan sets a target for the throttling and quota limits on individual client API keys. For more information, see [Creating and Using API Usage Plans in Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html) in the *API Gateway Developer Guide*.
         In some cases clients can exceed the targets that you set. Don’t rely on usage plans to control costs. Consider using [](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) to monitor costs and [](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) to manage API requests.

        :param str resource_name: The name of the resource.
        :param UsagePlanArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UsagePlanArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_stages: Optional[pulumi.Input[Sequence[pulumi.Input[Union['UsagePlanApiStageArgs', 'UsagePlanApiStageArgsDict']]]]] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 quota: Optional[pulumi.Input[Union['UsagePlanQuotaSettingsArgs', 'UsagePlanQuotaSettingsArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 throttle: Optional[pulumi.Input[Union['UsagePlanThrottleSettingsArgs', 'UsagePlanThrottleSettingsArgsDict']]] = None,
                 usage_plan_name: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UsagePlanArgs.__new__(UsagePlanArgs)

            __props__.__dict__["api_stages"] = api_stages
            __props__.__dict__["description"] = description
            __props__.__dict__["quota"] = quota
            __props__.__dict__["tags"] = tags
            __props__.__dict__["throttle"] = throttle
            __props__.__dict__["usage_plan_name"] = usage_plan_name
            __props__.__dict__["aws_id"] = None
        super(UsagePlan, __self__).__init__(
            'aws-native:apigateway:UsagePlan',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'UsagePlan':
        """
        Get an existing UsagePlan resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = UsagePlanArgs.__new__(UsagePlanArgs)

        __props__.__dict__["api_stages"] = None
        __props__.__dict__["aws_id"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["quota"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["throttle"] = None
        __props__.__dict__["usage_plan_name"] = None
        return UsagePlan(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiStages")
    def api_stages(self) -> pulumi.Output[Optional[Sequence['outputs.UsagePlanApiStage']]]:
        """
        The associated API stages of a usage plan.
        """
        return pulumi.get(self, "api_stages")

    @property
    @pulumi.getter(name="awsId")
    def aws_id(self) -> pulumi.Output[builtins.str]:
        """
        The ID for the usage plan. For example: `abc123` .
        """
        return pulumi.get(self, "aws_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The description of a usage plan.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def quota(self) -> pulumi.Output[Optional['outputs.UsagePlanQuotaSettings']]:
        """
        The target maximum number of permitted requests per a given unit time interval.
        """
        return pulumi.get(self, "quota")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        The collection of tags. Each tag element is associated with a given resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def throttle(self) -> pulumi.Output[Optional['outputs.UsagePlanThrottleSettings']]:
        """
        A map containing method level throttling information for API stage in a usage plan.
        """
        return pulumi.get(self, "throttle")

    @property
    @pulumi.getter(name="usagePlanName")
    def usage_plan_name(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The name of a usage plan.
        """
        return pulumi.get(self, "usage_plan_name")

