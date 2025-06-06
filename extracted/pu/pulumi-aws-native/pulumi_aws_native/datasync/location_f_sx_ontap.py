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

__all__ = ['LocationFSxOntapArgs', 'LocationFSxOntap']

@pulumi.input_type
class LocationFSxOntapArgs:
    def __init__(__self__, *,
                 security_group_arns: pulumi.Input[Sequence[pulumi.Input[builtins.str]]],
                 storage_virtual_machine_arn: pulumi.Input[builtins.str],
                 protocol: Optional[pulumi.Input['LocationFSxOntapProtocolArgs']] = None,
                 subdirectory: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a LocationFSxOntap resource.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] security_group_arns: The ARNs of the security groups that are to use to configure the FSx ONTAP file system.
        :param pulumi.Input[builtins.str] storage_virtual_machine_arn: The Amazon Resource Name (ARN) for the FSx ONTAP SVM.
        :param pulumi.Input['LocationFSxOntapProtocolArgs'] protocol: Specifies the data transfer protocol that DataSync uses to access your Amazon FSx file system.
        :param pulumi.Input[builtins.str] subdirectory: A subdirectory in the location's path.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        pulumi.set(__self__, "security_group_arns", security_group_arns)
        pulumi.set(__self__, "storage_virtual_machine_arn", storage_virtual_machine_arn)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)
        if subdirectory is not None:
            pulumi.set(__self__, "subdirectory", subdirectory)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="securityGroupArns")
    def security_group_arns(self) -> pulumi.Input[Sequence[pulumi.Input[builtins.str]]]:
        """
        The ARNs of the security groups that are to use to configure the FSx ONTAP file system.
        """
        return pulumi.get(self, "security_group_arns")

    @security_group_arns.setter
    def security_group_arns(self, value: pulumi.Input[Sequence[pulumi.Input[builtins.str]]]):
        pulumi.set(self, "security_group_arns", value)

    @property
    @pulumi.getter(name="storageVirtualMachineArn")
    def storage_virtual_machine_arn(self) -> pulumi.Input[builtins.str]:
        """
        The Amazon Resource Name (ARN) for the FSx ONTAP SVM.
        """
        return pulumi.get(self, "storage_virtual_machine_arn")

    @storage_virtual_machine_arn.setter
    def storage_virtual_machine_arn(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "storage_virtual_machine_arn", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input['LocationFSxOntapProtocolArgs']]:
        """
        Specifies the data transfer protocol that DataSync uses to access your Amazon FSx file system.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input['LocationFSxOntapProtocolArgs']]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter
    def subdirectory(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        A subdirectory in the location's path.
        """
        return pulumi.get(self, "subdirectory")

    @subdirectory.setter
    def subdirectory(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "subdirectory", value)

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


@pulumi.type_token("aws-native:datasync:LocationFSxOntap")
class LocationFSxOntap(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 protocol: Optional[pulumi.Input[Union['LocationFSxOntapProtocolArgs', 'LocationFSxOntapProtocolArgsDict']]] = None,
                 security_group_arns: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 storage_virtual_machine_arn: Optional[pulumi.Input[builtins.str]] = None,
                 subdirectory: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 __props__=None):
        """
        Resource schema for AWS::DataSync::LocationFSxONTAP.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['LocationFSxOntapProtocolArgs', 'LocationFSxOntapProtocolArgsDict']] protocol: Specifies the data transfer protocol that DataSync uses to access your Amazon FSx file system.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] security_group_arns: The ARNs of the security groups that are to use to configure the FSx ONTAP file system.
        :param pulumi.Input[builtins.str] storage_virtual_machine_arn: The Amazon Resource Name (ARN) for the FSx ONTAP SVM.
        :param pulumi.Input[builtins.str] subdirectory: A subdirectory in the location's path.
        :param pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LocationFSxOntapArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::DataSync::LocationFSxONTAP.

        :param str resource_name: The name of the resource.
        :param LocationFSxOntapArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LocationFSxOntapArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 protocol: Optional[pulumi.Input[Union['LocationFSxOntapProtocolArgs', 'LocationFSxOntapProtocolArgsDict']]] = None,
                 security_group_arns: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 storage_virtual_machine_arn: Optional[pulumi.Input[builtins.str]] = None,
                 subdirectory: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LocationFSxOntapArgs.__new__(LocationFSxOntapArgs)

            __props__.__dict__["protocol"] = protocol
            if security_group_arns is None and not opts.urn:
                raise TypeError("Missing required property 'security_group_arns'")
            __props__.__dict__["security_group_arns"] = security_group_arns
            if storage_virtual_machine_arn is None and not opts.urn:
                raise TypeError("Missing required property 'storage_virtual_machine_arn'")
            __props__.__dict__["storage_virtual_machine_arn"] = storage_virtual_machine_arn
            __props__.__dict__["subdirectory"] = subdirectory
            __props__.__dict__["tags"] = tags
            __props__.__dict__["fsx_filesystem_arn"] = None
            __props__.__dict__["location_arn"] = None
            __props__.__dict__["location_uri"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["securityGroupArns[*]", "storageVirtualMachineArn"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(LocationFSxOntap, __self__).__init__(
            'aws-native:datasync:LocationFSxOntap',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LocationFSxOntap':
        """
        Get an existing LocationFSxOntap resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LocationFSxOntapArgs.__new__(LocationFSxOntapArgs)

        __props__.__dict__["fsx_filesystem_arn"] = None
        __props__.__dict__["location_arn"] = None
        __props__.__dict__["location_uri"] = None
        __props__.__dict__["protocol"] = None
        __props__.__dict__["security_group_arns"] = None
        __props__.__dict__["storage_virtual_machine_arn"] = None
        __props__.__dict__["subdirectory"] = None
        __props__.__dict__["tags"] = None
        return LocationFSxOntap(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="fsxFilesystemArn")
    def fsx_filesystem_arn(self) -> pulumi.Output[builtins.str]:
        """
        The Amazon Resource Name (ARN) for the FSx ONAP file system.
        """
        return pulumi.get(self, "fsx_filesystem_arn")

    @property
    @pulumi.getter(name="locationArn")
    def location_arn(self) -> pulumi.Output[builtins.str]:
        """
        The Amazon Resource Name (ARN) of the Amazon FSx ONTAP file system location that is created.
        """
        return pulumi.get(self, "location_arn")

    @property
    @pulumi.getter(name="locationUri")
    def location_uri(self) -> pulumi.Output[builtins.str]:
        """
        The URL of the FSx ONTAP file system that was described.
        """
        return pulumi.get(self, "location_uri")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[Optional['outputs.LocationFSxOntapProtocol']]:
        """
        Specifies the data transfer protocol that DataSync uses to access your Amazon FSx file system.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="securityGroupArns")
    def security_group_arns(self) -> pulumi.Output[Sequence[builtins.str]]:
        """
        The ARNs of the security groups that are to use to configure the FSx ONTAP file system.
        """
        return pulumi.get(self, "security_group_arns")

    @property
    @pulumi.getter(name="storageVirtualMachineArn")
    def storage_virtual_machine_arn(self) -> pulumi.Output[builtins.str]:
        """
        The Amazon Resource Name (ARN) for the FSx ONTAP SVM.
        """
        return pulumi.get(self, "storage_virtual_machine_arn")

    @property
    @pulumi.getter
    def subdirectory(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        A subdirectory in the location's path.
        """
        return pulumi.get(self, "subdirectory")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

