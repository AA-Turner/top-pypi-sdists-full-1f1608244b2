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
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs
from ._enums import *

__all__ = ['ScheduledAuditArgs', 'ScheduledAudit']

@pulumi.input_type
class ScheduledAuditArgs:
    def __init__(__self__, *,
                 frequency: pulumi.Input['ScheduledAuditFrequency'],
                 target_check_names: pulumi.Input[Sequence[pulumi.Input[builtins.str]]],
                 day_of_month: Optional[pulumi.Input[builtins.str]] = None,
                 day_of_week: Optional[pulumi.Input['ScheduledAuditDayOfWeek']] = None,
                 scheduled_audit_name: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a ScheduledAudit resource.
        :param pulumi.Input['ScheduledAuditFrequency'] frequency: How often the scheduled audit takes place. Can be one of DAILY, WEEKLY, BIWEEKLY, or MONTHLY.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] target_check_names: Which checks are performed during the scheduled audit. Checks must be enabled for your account.
        :param pulumi.Input[builtins.str] day_of_month: The day of the month on which the scheduled audit takes place. Can be 1 through 31 or LAST. This field is required if the frequency parameter is set to MONTHLY.
        :param pulumi.Input['ScheduledAuditDayOfWeek'] day_of_week: The day of the week on which the scheduled audit takes place. Can be one of SUN, MON, TUE,WED, THU, FRI, or SAT. This field is required if the frequency parameter is set to WEEKLY or BIWEEKLY.
        :param pulumi.Input[builtins.str] scheduled_audit_name: The name you want to give to the scheduled audit.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        pulumi.set(__self__, "frequency", frequency)
        pulumi.set(__self__, "target_check_names", target_check_names)
        if day_of_month is not None:
            pulumi.set(__self__, "day_of_month", day_of_month)
        if day_of_week is not None:
            pulumi.set(__self__, "day_of_week", day_of_week)
        if scheduled_audit_name is not None:
            pulumi.set(__self__, "scheduled_audit_name", scheduled_audit_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def frequency(self) -> pulumi.Input['ScheduledAuditFrequency']:
        """
        How often the scheduled audit takes place. Can be one of DAILY, WEEKLY, BIWEEKLY, or MONTHLY.
        """
        return pulumi.get(self, "frequency")

    @frequency.setter
    def frequency(self, value: pulumi.Input['ScheduledAuditFrequency']):
        pulumi.set(self, "frequency", value)

    @property
    @pulumi.getter(name="targetCheckNames")
    def target_check_names(self) -> pulumi.Input[Sequence[pulumi.Input[builtins.str]]]:
        """
        Which checks are performed during the scheduled audit. Checks must be enabled for your account.
        """
        return pulumi.get(self, "target_check_names")

    @target_check_names.setter
    def target_check_names(self, value: pulumi.Input[Sequence[pulumi.Input[builtins.str]]]):
        pulumi.set(self, "target_check_names", value)

    @property
    @pulumi.getter(name="dayOfMonth")
    def day_of_month(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The day of the month on which the scheduled audit takes place. Can be 1 through 31 or LAST. This field is required if the frequency parameter is set to MONTHLY.
        """
        return pulumi.get(self, "day_of_month")

    @day_of_month.setter
    def day_of_month(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "day_of_month", value)

    @property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> Optional[pulumi.Input['ScheduledAuditDayOfWeek']]:
        """
        The day of the week on which the scheduled audit takes place. Can be one of SUN, MON, TUE,WED, THU, FRI, or SAT. This field is required if the frequency parameter is set to WEEKLY or BIWEEKLY.
        """
        return pulumi.get(self, "day_of_week")

    @day_of_week.setter
    def day_of_week(self, value: Optional[pulumi.Input['ScheduledAuditDayOfWeek']]):
        pulumi.set(self, "day_of_week", value)

    @property
    @pulumi.getter(name="scheduledAuditName")
    def scheduled_audit_name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name you want to give to the scheduled audit.
        """
        return pulumi.get(self, "scheduled_audit_name")

    @scheduled_audit_name.setter
    def scheduled_audit_name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "scheduled_audit_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


@pulumi.type_token("aws-native:iot:ScheduledAudit")
class ScheduledAudit(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 day_of_month: Optional[pulumi.Input[builtins.str]] = None,
                 day_of_week: Optional[pulumi.Input['ScheduledAuditDayOfWeek']] = None,
                 frequency: Optional[pulumi.Input['ScheduledAuditFrequency']] = None,
                 scheduled_audit_name: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 target_check_names: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        """
        Scheduled audits can be used to specify the checks you want to perform during an audit and how often the audit should be run.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] day_of_month: The day of the month on which the scheduled audit takes place. Can be 1 through 31 or LAST. This field is required if the frequency parameter is set to MONTHLY.
        :param pulumi.Input['ScheduledAuditDayOfWeek'] day_of_week: The day of the week on which the scheduled audit takes place. Can be one of SUN, MON, TUE,WED, THU, FRI, or SAT. This field is required if the frequency parameter is set to WEEKLY or BIWEEKLY.
        :param pulumi.Input['ScheduledAuditFrequency'] frequency: How often the scheduled audit takes place. Can be one of DAILY, WEEKLY, BIWEEKLY, or MONTHLY.
        :param pulumi.Input[builtins.str] scheduled_audit_name: The name you want to give to the scheduled audit.
        :param pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]] tags: An array of key-value pairs to apply to this resource.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] target_check_names: Which checks are performed during the scheduled audit. Checks must be enabled for your account.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ScheduledAuditArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Scheduled audits can be used to specify the checks you want to perform during an audit and how often the audit should be run.

        :param str resource_name: The name of the resource.
        :param ScheduledAuditArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScheduledAuditArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 day_of_month: Optional[pulumi.Input[builtins.str]] = None,
                 day_of_week: Optional[pulumi.Input['ScheduledAuditDayOfWeek']] = None,
                 frequency: Optional[pulumi.Input['ScheduledAuditFrequency']] = None,
                 scheduled_audit_name: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 target_check_names: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ScheduledAuditArgs.__new__(ScheduledAuditArgs)

            __props__.__dict__["day_of_month"] = day_of_month
            __props__.__dict__["day_of_week"] = day_of_week
            if frequency is None and not opts.urn:
                raise TypeError("Missing required property 'frequency'")
            __props__.__dict__["frequency"] = frequency
            __props__.__dict__["scheduled_audit_name"] = scheduled_audit_name
            __props__.__dict__["tags"] = tags
            if target_check_names is None and not opts.urn:
                raise TypeError("Missing required property 'target_check_names'")
            __props__.__dict__["target_check_names"] = target_check_names
            __props__.__dict__["scheduled_audit_arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["scheduledAuditName"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ScheduledAudit, __self__).__init__(
            'aws-native:iot:ScheduledAudit',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ScheduledAudit':
        """
        Get an existing ScheduledAudit resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ScheduledAuditArgs.__new__(ScheduledAuditArgs)

        __props__.__dict__["day_of_month"] = None
        __props__.__dict__["day_of_week"] = None
        __props__.__dict__["frequency"] = None
        __props__.__dict__["scheduled_audit_arn"] = None
        __props__.__dict__["scheduled_audit_name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["target_check_names"] = None
        return ScheduledAudit(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dayOfMonth")
    def day_of_month(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The day of the month on which the scheduled audit takes place. Can be 1 through 31 or LAST. This field is required if the frequency parameter is set to MONTHLY.
        """
        return pulumi.get(self, "day_of_month")

    @property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> pulumi.Output[Optional['ScheduledAuditDayOfWeek']]:
        """
        The day of the week on which the scheduled audit takes place. Can be one of SUN, MON, TUE,WED, THU, FRI, or SAT. This field is required if the frequency parameter is set to WEEKLY or BIWEEKLY.
        """
        return pulumi.get(self, "day_of_week")

    @property
    @pulumi.getter
    def frequency(self) -> pulumi.Output['ScheduledAuditFrequency']:
        """
        How often the scheduled audit takes place. Can be one of DAILY, WEEKLY, BIWEEKLY, or MONTHLY.
        """
        return pulumi.get(self, "frequency")

    @property
    @pulumi.getter(name="scheduledAuditArn")
    def scheduled_audit_arn(self) -> pulumi.Output[builtins.str]:
        """
        The ARN (Amazon resource name) of the scheduled audit.
        """
        return pulumi.get(self, "scheduled_audit_arn")

    @property
    @pulumi.getter(name="scheduledAuditName")
    def scheduled_audit_name(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The name you want to give to the scheduled audit.
        """
        return pulumi.get(self, "scheduled_audit_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetCheckNames")
    def target_check_names(self) -> pulumi.Output[Sequence[builtins.str]]:
        """
        Which checks are performed during the scheduled audit. Checks must be enabled for your account.
        """
        return pulumi.get(self, "target_check_names")

