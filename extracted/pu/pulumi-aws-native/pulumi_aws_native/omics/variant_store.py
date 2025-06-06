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

__all__ = ['VariantStoreArgs', 'VariantStore']

@pulumi.input_type
class VariantStoreArgs:
    def __init__(__self__, *,
                 reference: pulumi.Input['VariantStoreReferenceItemArgs'],
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 sse_config: Optional[pulumi.Input['VariantStoreSseConfigArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None):
        """
        The set of arguments for constructing a VariantStore resource.
        :param pulumi.Input['VariantStoreReferenceItemArgs'] reference: The genome reference for the store's variants.
        :param pulumi.Input[builtins.str] description: A description for the store.
        :param pulumi.Input[builtins.str] name: A name for the store.
        :param pulumi.Input['VariantStoreSseConfigArgs'] sse_config: Server-side encryption (SSE) settings for the store.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] tags: Tags for the store.
        """
        pulumi.set(__self__, "reference", reference)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if sse_config is not None:
            pulumi.set(__self__, "sse_config", sse_config)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def reference(self) -> pulumi.Input['VariantStoreReferenceItemArgs']:
        """
        The genome reference for the store's variants.
        """
        return pulumi.get(self, "reference")

    @reference.setter
    def reference(self, value: pulumi.Input['VariantStoreReferenceItemArgs']):
        pulumi.set(self, "reference", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        A description for the store.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        A name for the store.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="sseConfig")
    def sse_config(self) -> Optional[pulumi.Input['VariantStoreSseConfigArgs']]:
        """
        Server-side encryption (SSE) settings for the store.
        """
        return pulumi.get(self, "sse_config")

    @sse_config.setter
    def sse_config(self, value: Optional[pulumi.Input['VariantStoreSseConfigArgs']]):
        pulumi.set(self, "sse_config", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]:
        """
        Tags for the store.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.type_token("aws-native:omics:VariantStore")
class VariantStore(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 reference: Optional[pulumi.Input[Union['VariantStoreReferenceItemArgs', 'VariantStoreReferenceItemArgsDict']]] = None,
                 sse_config: Optional[pulumi.Input[Union['VariantStoreSseConfigArgs', 'VariantStoreSseConfigArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        """
        Definition of AWS::Omics::VariantStore Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] description: A description for the store.
        :param pulumi.Input[builtins.str] name: A name for the store.
        :param pulumi.Input[Union['VariantStoreReferenceItemArgs', 'VariantStoreReferenceItemArgsDict']] reference: The genome reference for the store's variants.
        :param pulumi.Input[Union['VariantStoreSseConfigArgs', 'VariantStoreSseConfigArgsDict']] sse_config: Server-side encryption (SSE) settings for the store.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] tags: Tags for the store.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VariantStoreArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::Omics::VariantStore Resource Type

        :param str resource_name: The name of the resource.
        :param VariantStoreArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VariantStoreArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 reference: Optional[pulumi.Input[Union['VariantStoreReferenceItemArgs', 'VariantStoreReferenceItemArgsDict']]] = None,
                 sse_config: Optional[pulumi.Input[Union['VariantStoreSseConfigArgs', 'VariantStoreSseConfigArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VariantStoreArgs.__new__(VariantStoreArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if reference is None and not opts.urn:
                raise TypeError("Missing required property 'reference'")
            __props__.__dict__["reference"] = reference
            __props__.__dict__["sse_config"] = sse_config
            __props__.__dict__["tags"] = tags
            __props__.__dict__["aws_id"] = None
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["status_message"] = None
            __props__.__dict__["store_arn"] = None
            __props__.__dict__["store_size_bytes"] = None
            __props__.__dict__["update_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name", "reference", "sseConfig", "tags.*"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(VariantStore, __self__).__init__(
            'aws-native:omics:VariantStore',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VariantStore':
        """
        Get an existing VariantStore resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VariantStoreArgs.__new__(VariantStoreArgs)

        __props__.__dict__["aws_id"] = None
        __props__.__dict__["creation_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["reference"] = None
        __props__.__dict__["sse_config"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["status_message"] = None
        __props__.__dict__["store_arn"] = None
        __props__.__dict__["store_size_bytes"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["update_time"] = None
        return VariantStore(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="awsId")
    def aws_id(self) -> pulumi.Output[builtins.str]:
        """
        The store's ID.
        """
        return pulumi.get(self, "aws_id")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[builtins.str]:
        """
        When the store was created.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        A description for the store.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        A name for the store.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def reference(self) -> pulumi.Output['outputs.VariantStoreReferenceItem']:
        """
        The genome reference for the store's variants.
        """
        return pulumi.get(self, "reference")

    @property
    @pulumi.getter(name="sseConfig")
    def sse_config(self) -> pulumi.Output[Optional['outputs.VariantStoreSseConfig']]:
        """
        Server-side encryption (SSE) settings for the store.
        """
        return pulumi.get(self, "sse_config")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['VariantStoreStoreStatus']:
        """
        The store's status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> pulumi.Output[builtins.str]:
        """
        The store's status message.
        """
        return pulumi.get(self, "status_message")

    @property
    @pulumi.getter(name="storeArn")
    def store_arn(self) -> pulumi.Output[builtins.str]:
        """
        The store's ARN.
        """
        return pulumi.get(self, "store_arn")

    @property
    @pulumi.getter(name="storeSizeBytes")
    def store_size_bytes(self) -> pulumi.Output[builtins.float]:
        """
        The store's size in bytes.
        """
        return pulumi.get(self, "store_size_bytes")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, builtins.str]]]:
        """
        Tags for the store.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[builtins.str]:
        """
        When the store was updated.
        """
        return pulumi.get(self, "update_time")

