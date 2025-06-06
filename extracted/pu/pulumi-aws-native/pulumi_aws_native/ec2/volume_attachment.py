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

__all__ = ['VolumeAttachmentArgs', 'VolumeAttachment']

@pulumi.input_type
class VolumeAttachmentArgs:
    def __init__(__self__, *,
                 instance_id: pulumi.Input[builtins.str],
                 volume_id: pulumi.Input[builtins.str],
                 device: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a VolumeAttachment resource.
        :param pulumi.Input[builtins.str] instance_id: The ID of the instance to which the volume attaches. This value can be a reference to an [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html) resource, or it can be the physical ID of an existing EC2 instance.
        :param pulumi.Input[builtins.str] volume_id: The ID of the Amazon EBS volume. The volume and instance must be within the same Availability Zone. This value can be a reference to an [AWS::EC2::Volume](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html) resource, or it can be the volume ID of an existing Amazon EBS volume.
        :param pulumi.Input[builtins.str] device: The device name (for example, ``/dev/sdh`` or ``xvdh``).
        """
        pulumi.set(__self__, "instance_id", instance_id)
        pulumi.set(__self__, "volume_id", volume_id)
        if device is not None:
            pulumi.set(__self__, "device", device)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[builtins.str]:
        """
        The ID of the instance to which the volume attaches. This value can be a reference to an [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html) resource, or it can be the physical ID of an existing EC2 instance.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> pulumi.Input[builtins.str]:
        """
        The ID of the Amazon EBS volume. The volume and instance must be within the same Availability Zone. This value can be a reference to an [AWS::EC2::Volume](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html) resource, or it can be the volume ID of an existing Amazon EBS volume.
        """
        return pulumi.get(self, "volume_id")

    @volume_id.setter
    def volume_id(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "volume_id", value)

    @property
    @pulumi.getter
    def device(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The device name (for example, ``/dev/sdh`` or ``xvdh``).
        """
        return pulumi.get(self, "device")

    @device.setter
    def device(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "device", value)


@pulumi.type_token("aws-native:ec2:VolumeAttachment")
class VolumeAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 device: Optional[pulumi.Input[builtins.str]] = None,
                 instance_id: Optional[pulumi.Input[builtins.str]] = None,
                 volume_id: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        Attaches an Amazon EBS volume to a running instance and exposes it to the instance with the specified device name.
         Before this resource can be deleted (and therefore the volume detached), you must first unmount the volume in the instance. Failure to do so results in the volume being stuck in the busy state while it is trying to detach, which could possibly damage the file system or the data it contains.
         If an Amazon EBS volume is the root device of an instance, it cannot be detached while the instance is in the "running" state. To detach the root volume, stop the instance first.
         If the root volume is detached from an instance with an MKT product code, then the product codes from that volume are no longer associated with the instance.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] device: The device name (for example, ``/dev/sdh`` or ``xvdh``).
        :param pulumi.Input[builtins.str] instance_id: The ID of the instance to which the volume attaches. This value can be a reference to an [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html) resource, or it can be the physical ID of an existing EC2 instance.
        :param pulumi.Input[builtins.str] volume_id: The ID of the Amazon EBS volume. The volume and instance must be within the same Availability Zone. This value can be a reference to an [AWS::EC2::Volume](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html) resource, or it can be the volume ID of an existing Amazon EBS volume.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VolumeAttachmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Attaches an Amazon EBS volume to a running instance and exposes it to the instance with the specified device name.
         Before this resource can be deleted (and therefore the volume detached), you must first unmount the volume in the instance. Failure to do so results in the volume being stuck in the busy state while it is trying to detach, which could possibly damage the file system or the data it contains.
         If an Amazon EBS volume is the root device of an instance, it cannot be detached while the instance is in the "running" state. To detach the root volume, stop the instance first.
         If the root volume is detached from an instance with an MKT product code, then the product codes from that volume are no longer associated with the instance.

        :param str resource_name: The name of the resource.
        :param VolumeAttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VolumeAttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 device: Optional[pulumi.Input[builtins.str]] = None,
                 instance_id: Optional[pulumi.Input[builtins.str]] = None,
                 volume_id: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VolumeAttachmentArgs.__new__(VolumeAttachmentArgs)

            __props__.__dict__["device"] = device
            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__.__dict__["instance_id"] = instance_id
            if volume_id is None and not opts.urn:
                raise TypeError("Missing required property 'volume_id'")
            __props__.__dict__["volume_id"] = volume_id
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["device", "instanceId", "volumeId"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(VolumeAttachment, __self__).__init__(
            'aws-native:ec2:VolumeAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VolumeAttachment':
        """
        Get an existing VolumeAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VolumeAttachmentArgs.__new__(VolumeAttachmentArgs)

        __props__.__dict__["device"] = None
        __props__.__dict__["instance_id"] = None
        __props__.__dict__["volume_id"] = None
        return VolumeAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def device(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The device name (for example, ``/dev/sdh`` or ``xvdh``).
        """
        return pulumi.get(self, "device")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[builtins.str]:
        """
        The ID of the instance to which the volume attaches. This value can be a reference to an [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html) resource, or it can be the physical ID of an existing EC2 instance.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> pulumi.Output[builtins.str]:
        """
        The ID of the Amazon EBS volume. The volume and instance must be within the same Availability Zone. This value can be a reference to an [AWS::EC2::Volume](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html) resource, or it can be the volume ID of an existing Amazon EBS volume.
        """
        return pulumi.get(self, "volume_id")

