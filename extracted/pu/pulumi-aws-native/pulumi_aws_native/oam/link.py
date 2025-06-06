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
from ._enums import *
from ._inputs import *

__all__ = ['LinkArgs', 'Link']

@pulumi.input_type
class LinkArgs:
    def __init__(__self__, *,
                 resource_types: pulumi.Input[Sequence[pulumi.Input['LinkResourceType']]],
                 sink_identifier: pulumi.Input[builtins.str],
                 label_template: Optional[pulumi.Input[builtins.str]] = None,
                 link_configuration: Optional[pulumi.Input['LinkConfigurationArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None):
        """
        The set of arguments for constructing a Link resource.
        :param pulumi.Input[Sequence[pulumi.Input['LinkResourceType']]] resource_types: An array of strings that define which types of data that the source account shares with the monitoring account. Valid values are `AWS::CloudWatch::Metric | AWS::Logs::LogGroup | AWS::XRay::Trace | AWS::ApplicationInsights::Application | AWS::InternetMonitor::Monitor` .
        :param pulumi.Input[builtins.str] sink_identifier: The ARN of the sink in the monitoring account that you want to link to. You can use [ListSinks](https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListSinks.html) to find the ARNs of sinks.
        :param pulumi.Input[builtins.str] label_template: Specify a friendly human-readable name to use to identify this source account when you are viewing data from it in the monitoring account.
               
               You can include the following variables in your template:
               
               - `$AccountName` is the name of the account
               - `$AccountEmail` is a globally-unique email address, which includes the email domain, such as `mariagarcia@example.com`
               - `$AccountEmailNoDomain` is an email address without the domain name, such as `mariagarcia`
               
               > In the  and  Regions, the only supported option is to use custom labels, and the `$AccountName` , `$AccountEmail` , and `$AccountEmailNoDomain` variables all resolve as *account-id* instead of the specified variable.
        :param pulumi.Input['LinkConfigurationArgs'] link_configuration: Use this structure to optionally create filters that specify that only some metric namespaces or log groups are to be shared from the source account to the monitoring account.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] tags: Tags to apply to the link
        """
        pulumi.set(__self__, "resource_types", resource_types)
        pulumi.set(__self__, "sink_identifier", sink_identifier)
        if label_template is not None:
            pulumi.set(__self__, "label_template", label_template)
        if link_configuration is not None:
            pulumi.set(__self__, "link_configuration", link_configuration)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> pulumi.Input[Sequence[pulumi.Input['LinkResourceType']]]:
        """
        An array of strings that define which types of data that the source account shares with the monitoring account. Valid values are `AWS::CloudWatch::Metric | AWS::Logs::LogGroup | AWS::XRay::Trace | AWS::ApplicationInsights::Application | AWS::InternetMonitor::Monitor` .
        """
        return pulumi.get(self, "resource_types")

    @resource_types.setter
    def resource_types(self, value: pulumi.Input[Sequence[pulumi.Input['LinkResourceType']]]):
        pulumi.set(self, "resource_types", value)

    @property
    @pulumi.getter(name="sinkIdentifier")
    def sink_identifier(self) -> pulumi.Input[builtins.str]:
        """
        The ARN of the sink in the monitoring account that you want to link to. You can use [ListSinks](https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListSinks.html) to find the ARNs of sinks.
        """
        return pulumi.get(self, "sink_identifier")

    @sink_identifier.setter
    def sink_identifier(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "sink_identifier", value)

    @property
    @pulumi.getter(name="labelTemplate")
    def label_template(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Specify a friendly human-readable name to use to identify this source account when you are viewing data from it in the monitoring account.

        You can include the following variables in your template:

        - `$AccountName` is the name of the account
        - `$AccountEmail` is a globally-unique email address, which includes the email domain, such as `mariagarcia@example.com`
        - `$AccountEmailNoDomain` is an email address without the domain name, such as `mariagarcia`

        > In the  and  Regions, the only supported option is to use custom labels, and the `$AccountName` , `$AccountEmail` , and `$AccountEmailNoDomain` variables all resolve as *account-id* instead of the specified variable.
        """
        return pulumi.get(self, "label_template")

    @label_template.setter
    def label_template(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "label_template", value)

    @property
    @pulumi.getter(name="linkConfiguration")
    def link_configuration(self) -> Optional[pulumi.Input['LinkConfigurationArgs']]:
        """
        Use this structure to optionally create filters that specify that only some metric namespaces or log groups are to be shared from the source account to the monitoring account.
        """
        return pulumi.get(self, "link_configuration")

    @link_configuration.setter
    def link_configuration(self, value: Optional[pulumi.Input['LinkConfigurationArgs']]):
        pulumi.set(self, "link_configuration", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]:
        """
        Tags to apply to the link
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.type_token("aws-native:oam:Link")
class Link(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 label_template: Optional[pulumi.Input[builtins.str]] = None,
                 link_configuration: Optional[pulumi.Input[Union['LinkConfigurationArgs', 'LinkConfigurationArgsDict']]] = None,
                 resource_types: Optional[pulumi.Input[Sequence[pulumi.Input['LinkResourceType']]]] = None,
                 sink_identifier: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        """
        Definition of AWS::Oam::Link Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] label_template: Specify a friendly human-readable name to use to identify this source account when you are viewing data from it in the monitoring account.
               
               You can include the following variables in your template:
               
               - `$AccountName` is the name of the account
               - `$AccountEmail` is a globally-unique email address, which includes the email domain, such as `mariagarcia@example.com`
               - `$AccountEmailNoDomain` is an email address without the domain name, such as `mariagarcia`
               
               > In the  and  Regions, the only supported option is to use custom labels, and the `$AccountName` , `$AccountEmail` , and `$AccountEmailNoDomain` variables all resolve as *account-id* instead of the specified variable.
        :param pulumi.Input[Union['LinkConfigurationArgs', 'LinkConfigurationArgsDict']] link_configuration: Use this structure to optionally create filters that specify that only some metric namespaces or log groups are to be shared from the source account to the monitoring account.
        :param pulumi.Input[Sequence[pulumi.Input['LinkResourceType']]] resource_types: An array of strings that define which types of data that the source account shares with the monitoring account. Valid values are `AWS::CloudWatch::Metric | AWS::Logs::LogGroup | AWS::XRay::Trace | AWS::ApplicationInsights::Application | AWS::InternetMonitor::Monitor` .
        :param pulumi.Input[builtins.str] sink_identifier: The ARN of the sink in the monitoring account that you want to link to. You can use [ListSinks](https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListSinks.html) to find the ARNs of sinks.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] tags: Tags to apply to the link
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LinkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::Oam::Link Resource Type

        :param str resource_name: The name of the resource.
        :param LinkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LinkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 label_template: Optional[pulumi.Input[builtins.str]] = None,
                 link_configuration: Optional[pulumi.Input[Union['LinkConfigurationArgs', 'LinkConfigurationArgsDict']]] = None,
                 resource_types: Optional[pulumi.Input[Sequence[pulumi.Input['LinkResourceType']]]] = None,
                 sink_identifier: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LinkArgs.__new__(LinkArgs)

            __props__.__dict__["label_template"] = label_template
            __props__.__dict__["link_configuration"] = link_configuration
            if resource_types is None and not opts.urn:
                raise TypeError("Missing required property 'resource_types'")
            __props__.__dict__["resource_types"] = resource_types
            if sink_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'sink_identifier'")
            __props__.__dict__["sink_identifier"] = sink_identifier
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["label"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["labelTemplate", "sinkIdentifier"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Link, __self__).__init__(
            'aws-native:oam:Link',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Link':
        """
        Get an existing Link resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LinkArgs.__new__(LinkArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["label"] = None
        __props__.__dict__["label_template"] = None
        __props__.__dict__["link_configuration"] = None
        __props__.__dict__["resource_types"] = None
        __props__.__dict__["sink_identifier"] = None
        __props__.__dict__["tags"] = None
        return Link(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[builtins.str]:
        """
        The ARN of the link. For example, `arn:aws:oam:us-west-1:111111111111:link:abcd1234-a123-456a-a12b-a123b456c789`
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def label(self) -> pulumi.Output[builtins.str]:
        """
        The friendly human-readable name used to identify this source account when it is viewed from the monitoring account. For example, `my-account1` .
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter(name="labelTemplate")
    def label_template(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        Specify a friendly human-readable name to use to identify this source account when you are viewing data from it in the monitoring account.

        You can include the following variables in your template:

        - `$AccountName` is the name of the account
        - `$AccountEmail` is a globally-unique email address, which includes the email domain, such as `mariagarcia@example.com`
        - `$AccountEmailNoDomain` is an email address without the domain name, such as `mariagarcia`

        > In the  and  Regions, the only supported option is to use custom labels, and the `$AccountName` , `$AccountEmail` , and `$AccountEmailNoDomain` variables all resolve as *account-id* instead of the specified variable.
        """
        return pulumi.get(self, "label_template")

    @property
    @pulumi.getter(name="linkConfiguration")
    def link_configuration(self) -> pulumi.Output[Optional['outputs.LinkConfiguration']]:
        """
        Use this structure to optionally create filters that specify that only some metric namespaces or log groups are to be shared from the source account to the monitoring account.
        """
        return pulumi.get(self, "link_configuration")

    @property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> pulumi.Output[Sequence['LinkResourceType']]:
        """
        An array of strings that define which types of data that the source account shares with the monitoring account. Valid values are `AWS::CloudWatch::Metric | AWS::Logs::LogGroup | AWS::XRay::Trace | AWS::ApplicationInsights::Application | AWS::InternetMonitor::Monitor` .
        """
        return pulumi.get(self, "resource_types")

    @property
    @pulumi.getter(name="sinkIdentifier")
    def sink_identifier(self) -> pulumi.Output[builtins.str]:
        """
        The ARN of the sink in the monitoring account that you want to link to. You can use [ListSinks](https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListSinks.html) to find the ARNs of sinks.
        """
        return pulumi.get(self, "sink_identifier")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, builtins.str]]]:
        """
        Tags to apply to the link
        """
        return pulumi.get(self, "tags")

