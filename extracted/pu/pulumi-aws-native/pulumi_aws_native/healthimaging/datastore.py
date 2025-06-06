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
from ._enums import *

__all__ = ['DatastoreArgs', 'Datastore']

@pulumi.input_type
class DatastoreArgs:
    def __init__(__self__, *,
                 datastore_name: Optional[pulumi.Input[builtins.str]] = None,
                 kms_key_arn: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None):
        """
        The set of arguments for constructing a Datastore resource.
        :param pulumi.Input[builtins.str] datastore_name: The data store name.
        :param pulumi.Input[builtins.str] kms_key_arn: The Amazon Resource Name (ARN) assigned to the Key Management Service (KMS) key for accessing encrypted data.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] tags: The tags provided when creating a data store.
        """
        if datastore_name is not None:
            pulumi.set(__self__, "datastore_name", datastore_name)
        if kms_key_arn is not None:
            pulumi.set(__self__, "kms_key_arn", kms_key_arn)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="datastoreName")
    def datastore_name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The data store name.
        """
        return pulumi.get(self, "datastore_name")

    @datastore_name.setter
    def datastore_name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "datastore_name", value)

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The Amazon Resource Name (ARN) assigned to the Key Management Service (KMS) key for accessing encrypted data.
        """
        return pulumi.get(self, "kms_key_arn")

    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "kms_key_arn", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]:
        """
        The tags provided when creating a data store.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.type_token("aws-native:healthimaging:Datastore")
class Datastore(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datastore_name: Optional[pulumi.Input[builtins.str]] = None,
                 kms_key_arn: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        """
        Definition of AWS::HealthImaging::Datastore Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] datastore_name: The data store name.
        :param pulumi.Input[builtins.str] kms_key_arn: The Amazon Resource Name (ARN) assigned to the Key Management Service (KMS) key for accessing encrypted data.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] tags: The tags provided when creating a data store.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DatastoreArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::HealthImaging::Datastore Resource Type

        :param str resource_name: The name of the resource.
        :param DatastoreArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatastoreArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datastore_name: Optional[pulumi.Input[builtins.str]] = None,
                 kms_key_arn: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DatastoreArgs.__new__(DatastoreArgs)

            __props__.__dict__["datastore_name"] = datastore_name
            __props__.__dict__["kms_key_arn"] = kms_key_arn
            __props__.__dict__["tags"] = tags
            __props__.__dict__["created_at"] = None
            __props__.__dict__["datastore_arn"] = None
            __props__.__dict__["datastore_id"] = None
            __props__.__dict__["datastore_status"] = None
            __props__.__dict__["updated_at"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["datastoreName", "kmsKeyArn", "tags.*"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Datastore, __self__).__init__(
            'aws-native:healthimaging:Datastore',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Datastore':
        """
        Get an existing Datastore resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DatastoreArgs.__new__(DatastoreArgs)

        __props__.__dict__["created_at"] = None
        __props__.__dict__["datastore_arn"] = None
        __props__.__dict__["datastore_id"] = None
        __props__.__dict__["datastore_name"] = None
        __props__.__dict__["datastore_status"] = None
        __props__.__dict__["kms_key_arn"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["updated_at"] = None
        return Datastore(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[builtins.str]:
        """
        The timestamp when the data store was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="datastoreArn")
    def datastore_arn(self) -> pulumi.Output[builtins.str]:
        """
        The Amazon Resource Name (ARN) for the data store.
        """
        return pulumi.get(self, "datastore_arn")

    @property
    @pulumi.getter(name="datastoreId")
    def datastore_id(self) -> pulumi.Output[builtins.str]:
        """
        The data store identifier.
        """
        return pulumi.get(self, "datastore_id")

    @property
    @pulumi.getter(name="datastoreName")
    def datastore_name(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The data store name.
        """
        return pulumi.get(self, "datastore_name")

    @property
    @pulumi.getter(name="datastoreStatus")
    def datastore_status(self) -> pulumi.Output['DatastoreStatus']:
        """
        The data store status.
        """
        return pulumi.get(self, "datastore_status")

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The Amazon Resource Name (ARN) assigned to the Key Management Service (KMS) key for accessing encrypted data.
        """
        return pulumi.get(self, "kms_key_arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, builtins.str]]]:
        """
        The tags provided when creating a data store.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[builtins.str]:
        """
        The timestamp when the data store was last updated.
        """
        return pulumi.get(self, "updated_at")

