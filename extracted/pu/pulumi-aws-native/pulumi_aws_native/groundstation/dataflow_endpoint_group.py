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
from ._enums import *
from ._inputs import *

__all__ = ['DataflowEndpointGroupArgs', 'DataflowEndpointGroup']

@pulumi.input_type
class DataflowEndpointGroupArgs:
    def __init__(__self__, *,
                 endpoint_details: pulumi.Input[Sequence[pulumi.Input['DataflowEndpointGroupEndpointDetailsArgs']]],
                 contact_post_pass_duration_seconds: Optional[pulumi.Input[builtins.int]] = None,
                 contact_pre_pass_duration_seconds: Optional[pulumi.Input[builtins.int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a DataflowEndpointGroup resource.
        :param pulumi.Input[Sequence[pulumi.Input['DataflowEndpointGroupEndpointDetailsArgs']]] endpoint_details: List of Endpoint Details, containing address and port for each endpoint. All dataflow endpoints within a single dataflow endpoint group must be of the same type. You cannot mix AWS Ground Station Agent endpoints with Dataflow endpoints in the same group. If your use case requires both types of endpoints, you must create separate dataflow endpoint groups for each type.
        :param pulumi.Input[builtins.int] contact_post_pass_duration_seconds: Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a POSTPASS state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the POSTPASS state.
        :param pulumi.Input[builtins.int] contact_pre_pass_duration_seconds: Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a PREPASS state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the PREPASS state.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: Tags assigned to a resource.
        """
        pulumi.set(__self__, "endpoint_details", endpoint_details)
        if contact_post_pass_duration_seconds is not None:
            pulumi.set(__self__, "contact_post_pass_duration_seconds", contact_post_pass_duration_seconds)
        if contact_pre_pass_duration_seconds is not None:
            pulumi.set(__self__, "contact_pre_pass_duration_seconds", contact_pre_pass_duration_seconds)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="endpointDetails")
    def endpoint_details(self) -> pulumi.Input[Sequence[pulumi.Input['DataflowEndpointGroupEndpointDetailsArgs']]]:
        """
        List of Endpoint Details, containing address and port for each endpoint. All dataflow endpoints within a single dataflow endpoint group must be of the same type. You cannot mix AWS Ground Station Agent endpoints with Dataflow endpoints in the same group. If your use case requires both types of endpoints, you must create separate dataflow endpoint groups for each type.
        """
        return pulumi.get(self, "endpoint_details")

    @endpoint_details.setter
    def endpoint_details(self, value: pulumi.Input[Sequence[pulumi.Input['DataflowEndpointGroupEndpointDetailsArgs']]]):
        pulumi.set(self, "endpoint_details", value)

    @property
    @pulumi.getter(name="contactPostPassDurationSeconds")
    def contact_post_pass_duration_seconds(self) -> Optional[pulumi.Input[builtins.int]]:
        """
        Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a POSTPASS state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the POSTPASS state.
        """
        return pulumi.get(self, "contact_post_pass_duration_seconds")

    @contact_post_pass_duration_seconds.setter
    def contact_post_pass_duration_seconds(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "contact_post_pass_duration_seconds", value)

    @property
    @pulumi.getter(name="contactPrePassDurationSeconds")
    def contact_pre_pass_duration_seconds(self) -> Optional[pulumi.Input[builtins.int]]:
        """
        Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a PREPASS state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the PREPASS state.
        """
        return pulumi.get(self, "contact_pre_pass_duration_seconds")

    @contact_pre_pass_duration_seconds.setter
    def contact_pre_pass_duration_seconds(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "contact_pre_pass_duration_seconds", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        Tags assigned to a resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


@pulumi.type_token("aws-native:groundstation:DataflowEndpointGroup")
class DataflowEndpointGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 contact_post_pass_duration_seconds: Optional[pulumi.Input[builtins.int]] = None,
                 contact_pre_pass_duration_seconds: Optional[pulumi.Input[builtins.int]] = None,
                 endpoint_details: Optional[pulumi.Input[Sequence[pulumi.Input[Union['DataflowEndpointGroupEndpointDetailsArgs', 'DataflowEndpointGroupEndpointDetailsArgsDict']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 __props__=None):
        """
        AWS Ground Station DataflowEndpointGroup schema for CloudFormation

        ## Example Usage
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        my_dataflow_endpoint_group = aws_native.groundstation.DataflowEndpointGroup("myDataflowEndpointGroup", endpoint_details=[{
            "security_details": {
                "subnet_ids": ["subnet-6782e71e"],
                "security_group_ids": ["sg-6979fe18"],
                "role_arn": "arn:aws:iam::012345678910:role/groundstation-service-role-AWSServiceRoleForAmazonGroundStation-EXAMPLEBQ4PI",
            },
            "endpoint": {
                "name": "myEndpoint",
                "address": {
                    "name": "172.10.0.2",
                    "port": 44720,
                },
                "mtu": 1500,
            },
        }])

        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.int] contact_post_pass_duration_seconds: Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a POSTPASS state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the POSTPASS state.
        :param pulumi.Input[builtins.int] contact_pre_pass_duration_seconds: Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a PREPASS state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the PREPASS state.
        :param pulumi.Input[Sequence[pulumi.Input[Union['DataflowEndpointGroupEndpointDetailsArgs', 'DataflowEndpointGroupEndpointDetailsArgsDict']]]] endpoint_details: List of Endpoint Details, containing address and port for each endpoint. All dataflow endpoints within a single dataflow endpoint group must be of the same type. You cannot mix AWS Ground Station Agent endpoints with Dataflow endpoints in the same group. If your use case requires both types of endpoints, you must create separate dataflow endpoint groups for each type.
        :param pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]] tags: Tags assigned to a resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DataflowEndpointGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        AWS Ground Station DataflowEndpointGroup schema for CloudFormation

        ## Example Usage
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        my_dataflow_endpoint_group = aws_native.groundstation.DataflowEndpointGroup("myDataflowEndpointGroup", endpoint_details=[{
            "security_details": {
                "subnet_ids": ["subnet-6782e71e"],
                "security_group_ids": ["sg-6979fe18"],
                "role_arn": "arn:aws:iam::012345678910:role/groundstation-service-role-AWSServiceRoleForAmazonGroundStation-EXAMPLEBQ4PI",
            },
            "endpoint": {
                "name": "myEndpoint",
                "address": {
                    "name": "172.10.0.2",
                    "port": 44720,
                },
                "mtu": 1500,
            },
        }])

        ```

        :param str resource_name: The name of the resource.
        :param DataflowEndpointGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DataflowEndpointGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 contact_post_pass_duration_seconds: Optional[pulumi.Input[builtins.int]] = None,
                 contact_pre_pass_duration_seconds: Optional[pulumi.Input[builtins.int]] = None,
                 endpoint_details: Optional[pulumi.Input[Sequence[pulumi.Input[Union['DataflowEndpointGroupEndpointDetailsArgs', 'DataflowEndpointGroupEndpointDetailsArgsDict']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DataflowEndpointGroupArgs.__new__(DataflowEndpointGroupArgs)

            __props__.__dict__["contact_post_pass_duration_seconds"] = contact_post_pass_duration_seconds
            __props__.__dict__["contact_pre_pass_duration_seconds"] = contact_pre_pass_duration_seconds
            if endpoint_details is None and not opts.urn:
                raise TypeError("Missing required property 'endpoint_details'")
            __props__.__dict__["endpoint_details"] = endpoint_details
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["aws_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["contactPostPassDurationSeconds", "contactPrePassDurationSeconds", "endpointDetails[*]"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(DataflowEndpointGroup, __self__).__init__(
            'aws-native:groundstation:DataflowEndpointGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DataflowEndpointGroup':
        """
        Get an existing DataflowEndpointGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DataflowEndpointGroupArgs.__new__(DataflowEndpointGroupArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["aws_id"] = None
        __props__.__dict__["contact_post_pass_duration_seconds"] = None
        __props__.__dict__["contact_pre_pass_duration_seconds"] = None
        __props__.__dict__["endpoint_details"] = None
        __props__.__dict__["tags"] = None
        return DataflowEndpointGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[builtins.str]:
        """
        The ARN of the dataflow endpoint group, such as `arn:aws:groundstation:us-east-2:1234567890:dataflow-endpoint-group/9940bf3b-d2ba-427e-9906-842b5e5d2296` .
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="awsId")
    def aws_id(self) -> pulumi.Output[builtins.str]:
        """
        UUID of a dataflow endpoint group.
        """
        return pulumi.get(self, "aws_id")

    @property
    @pulumi.getter(name="contactPostPassDurationSeconds")
    def contact_post_pass_duration_seconds(self) -> pulumi.Output[Optional[builtins.int]]:
        """
        Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a POSTPASS state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the POSTPASS state.
        """
        return pulumi.get(self, "contact_post_pass_duration_seconds")

    @property
    @pulumi.getter(name="contactPrePassDurationSeconds")
    def contact_pre_pass_duration_seconds(self) -> pulumi.Output[Optional[builtins.int]]:
        """
        Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a PREPASS state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the PREPASS state.
        """
        return pulumi.get(self, "contact_pre_pass_duration_seconds")

    @property
    @pulumi.getter(name="endpointDetails")
    def endpoint_details(self) -> pulumi.Output[Sequence['outputs.DataflowEndpointGroupEndpointDetails']]:
        """
        List of Endpoint Details, containing address and port for each endpoint. All dataflow endpoints within a single dataflow endpoint group must be of the same type. You cannot mix AWS Ground Station Agent endpoints with Dataflow endpoints in the same group. If your use case requires both types of endpoints, you must create separate dataflow endpoint groups for each type.
        """
        return pulumi.get(self, "endpoint_details")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        Tags assigned to a resource.
        """
        return pulumi.get(self, "tags")

