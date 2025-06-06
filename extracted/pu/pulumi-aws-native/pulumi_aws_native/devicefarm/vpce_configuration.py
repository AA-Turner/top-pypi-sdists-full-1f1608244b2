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

__all__ = ['VpceConfigurationArgs', 'VpceConfiguration']

@pulumi.input_type
class VpceConfigurationArgs:
    def __init__(__self__, *,
                 service_dns_name: pulumi.Input[builtins.str],
                 vpce_service_name: pulumi.Input[builtins.str],
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None,
                 vpce_configuration_description: Optional[pulumi.Input[builtins.str]] = None,
                 vpce_configuration_name: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a VpceConfiguration resource.
        :param pulumi.Input[builtins.str] service_dns_name: The DNS name that Device Farm will use to map to the private service you want to access.
        :param pulumi.Input[builtins.str] vpce_service_name: The name of the VPC endpoint service that you want to access from Device Farm.
               
               The name follows the format `com.amazonaws.vpce.us-west-2.vpce-svc-id` .
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: An array of key-value pairs to apply to this resource.
               
               For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html) in the *guide* .
        :param pulumi.Input[builtins.str] vpce_configuration_description: An optional description that provides details about your VPC endpoint configuration.
        :param pulumi.Input[builtins.str] vpce_configuration_name: The friendly name you give to your VPC endpoint configuration to manage your configurations more easily.
        """
        pulumi.set(__self__, "service_dns_name", service_dns_name)
        pulumi.set(__self__, "vpce_service_name", vpce_service_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if vpce_configuration_description is not None:
            pulumi.set(__self__, "vpce_configuration_description", vpce_configuration_description)
        if vpce_configuration_name is not None:
            pulumi.set(__self__, "vpce_configuration_name", vpce_configuration_name)

    @property
    @pulumi.getter(name="serviceDnsName")
    def service_dns_name(self) -> pulumi.Input[builtins.str]:
        """
        The DNS name that Device Farm will use to map to the private service you want to access.
        """
        return pulumi.get(self, "service_dns_name")

    @service_dns_name.setter
    def service_dns_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "service_dns_name", value)

    @property
    @pulumi.getter(name="vpceServiceName")
    def vpce_service_name(self) -> pulumi.Input[builtins.str]:
        """
        The name of the VPC endpoint service that you want to access from Device Farm.

        The name follows the format `com.amazonaws.vpce.us-west-2.vpce-svc-id` .
        """
        return pulumi.get(self, "vpce_service_name")

    @vpce_service_name.setter
    def vpce_service_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "vpce_service_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.

        For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html) in the *guide* .
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="vpceConfigurationDescription")
    def vpce_configuration_description(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        An optional description that provides details about your VPC endpoint configuration.
        """
        return pulumi.get(self, "vpce_configuration_description")

    @vpce_configuration_description.setter
    def vpce_configuration_description(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "vpce_configuration_description", value)

    @property
    @pulumi.getter(name="vpceConfigurationName")
    def vpce_configuration_name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The friendly name you give to your VPC endpoint configuration to manage your configurations more easily.
        """
        return pulumi.get(self, "vpce_configuration_name")

    @vpce_configuration_name.setter
    def vpce_configuration_name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "vpce_configuration_name", value)


@pulumi.type_token("aws-native:devicefarm:VpceConfiguration")
class VpceConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 service_dns_name: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 vpce_configuration_description: Optional[pulumi.Input[builtins.str]] = None,
                 vpce_configuration_name: Optional[pulumi.Input[builtins.str]] = None,
                 vpce_service_name: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        Resource Type definition for a Device Farm VPCE Configuration

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] service_dns_name: The DNS name that Device Farm will use to map to the private service you want to access.
        :param pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]] tags: An array of key-value pairs to apply to this resource.
               
               For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html) in the *guide* .
        :param pulumi.Input[builtins.str] vpce_configuration_description: An optional description that provides details about your VPC endpoint configuration.
        :param pulumi.Input[builtins.str] vpce_configuration_name: The friendly name you give to your VPC endpoint configuration to manage your configurations more easily.
        :param pulumi.Input[builtins.str] vpce_service_name: The name of the VPC endpoint service that you want to access from Device Farm.
               
               The name follows the format `com.amazonaws.vpce.us-west-2.vpce-svc-id` .
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VpceConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for a Device Farm VPCE Configuration

        :param str resource_name: The name of the resource.
        :param VpceConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VpceConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 service_dns_name: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 vpce_configuration_description: Optional[pulumi.Input[builtins.str]] = None,
                 vpce_configuration_name: Optional[pulumi.Input[builtins.str]] = None,
                 vpce_service_name: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VpceConfigurationArgs.__new__(VpceConfigurationArgs)

            if service_dns_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_dns_name'")
            __props__.__dict__["service_dns_name"] = service_dns_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["vpce_configuration_description"] = vpce_configuration_description
            __props__.__dict__["vpce_configuration_name"] = vpce_configuration_name
            if vpce_service_name is None and not opts.urn:
                raise TypeError("Missing required property 'vpce_service_name'")
            __props__.__dict__["vpce_service_name"] = vpce_service_name
            __props__.__dict__["arn"] = None
        super(VpceConfiguration, __self__).__init__(
            'aws-native:devicefarm:VpceConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VpceConfiguration':
        """
        Get an existing VpceConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VpceConfigurationArgs.__new__(VpceConfigurationArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["service_dns_name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["vpce_configuration_description"] = None
        __props__.__dict__["vpce_configuration_name"] = None
        __props__.__dict__["vpce_service_name"] = None
        return VpceConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[builtins.str]:
        """
        The Amazon Resource Name (ARN) of the VPC endpoint. See [Amazon resource names](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *General Reference guide* .
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="serviceDnsName")
    def service_dns_name(self) -> pulumi.Output[builtins.str]:
        """
        The DNS name that Device Farm will use to map to the private service you want to access.
        """
        return pulumi.get(self, "service_dns_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        An array of key-value pairs to apply to this resource.

        For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html) in the *guide* .
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpceConfigurationDescription")
    def vpce_configuration_description(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        An optional description that provides details about your VPC endpoint configuration.
        """
        return pulumi.get(self, "vpce_configuration_description")

    @property
    @pulumi.getter(name="vpceConfigurationName")
    def vpce_configuration_name(self) -> pulumi.Output[builtins.str]:
        """
        The friendly name you give to your VPC endpoint configuration to manage your configurations more easily.
        """
        return pulumi.get(self, "vpce_configuration_name")

    @property
    @pulumi.getter(name="vpceServiceName")
    def vpce_service_name(self) -> pulumi.Output[builtins.str]:
        """
        The name of the VPC endpoint service that you want to access from Device Farm.

        The name follows the format `com.amazonaws.vpce.us-west-2.vpce-svc-id` .
        """
        return pulumi.get(self, "vpce_service_name")

