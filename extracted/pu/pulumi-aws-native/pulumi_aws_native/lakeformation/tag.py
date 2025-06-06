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

__all__ = ['TagArgs', 'Tag']

@pulumi.input_type
class TagArgs:
    def __init__(__self__, *,
                 tag_key: pulumi.Input[builtins.str],
                 tag_values: pulumi.Input[Sequence[pulumi.Input[builtins.str]]],
                 catalog_id: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a Tag resource.
        :param pulumi.Input[builtins.str] tag_key: The key-name for the LF-tag.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] tag_values: A list of possible values an attribute can take.
        :param pulumi.Input[builtins.str] catalog_id: The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.
        """
        pulumi.set(__self__, "tag_key", tag_key)
        pulumi.set(__self__, "tag_values", tag_values)
        if catalog_id is not None:
            pulumi.set(__self__, "catalog_id", catalog_id)

    @property
    @pulumi.getter(name="tagKey")
    def tag_key(self) -> pulumi.Input[builtins.str]:
        """
        The key-name for the LF-tag.
        """
        return pulumi.get(self, "tag_key")

    @tag_key.setter
    def tag_key(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "tag_key", value)

    @property
    @pulumi.getter(name="tagValues")
    def tag_values(self) -> pulumi.Input[Sequence[pulumi.Input[builtins.str]]]:
        """
        A list of possible values an attribute can take.
        """
        return pulumi.get(self, "tag_values")

    @tag_values.setter
    def tag_values(self, value: pulumi.Input[Sequence[pulumi.Input[builtins.str]]]):
        pulumi.set(self, "tag_values", value)

    @property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.
        """
        return pulumi.get(self, "catalog_id")

    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "catalog_id", value)


@pulumi.type_token("aws-native:lakeformation:Tag")
class Tag(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 catalog_id: Optional[pulumi.Input[builtins.str]] = None,
                 tag_key: Optional[pulumi.Input[builtins.str]] = None,
                 tag_values: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        """
        A resource schema representing a Lake Formation Tag.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] catalog_id: The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.
        :param pulumi.Input[builtins.str] tag_key: The key-name for the LF-tag.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] tag_values: A list of possible values an attribute can take.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TagArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A resource schema representing a Lake Formation Tag.

        :param str resource_name: The name of the resource.
        :param TagArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TagArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 catalog_id: Optional[pulumi.Input[builtins.str]] = None,
                 tag_key: Optional[pulumi.Input[builtins.str]] = None,
                 tag_values: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TagArgs.__new__(TagArgs)

            __props__.__dict__["catalog_id"] = catalog_id
            if tag_key is None and not opts.urn:
                raise TypeError("Missing required property 'tag_key'")
            __props__.__dict__["tag_key"] = tag_key
            if tag_values is None and not opts.urn:
                raise TypeError("Missing required property 'tag_values'")
            __props__.__dict__["tag_values"] = tag_values
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["catalogId", "tagKey"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Tag, __self__).__init__(
            'aws-native:lakeformation:Tag',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Tag':
        """
        Get an existing Tag resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TagArgs.__new__(TagArgs)

        __props__.__dict__["catalog_id"] = None
        __props__.__dict__["tag_key"] = None
        __props__.__dict__["tag_values"] = None
        return Tag(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.
        """
        return pulumi.get(self, "catalog_id")

    @property
    @pulumi.getter(name="tagKey")
    def tag_key(self) -> pulumi.Output[builtins.str]:
        """
        The key-name for the LF-tag.
        """
        return pulumi.get(self, "tag_key")

    @property
    @pulumi.getter(name="tagValues")
    def tag_values(self) -> pulumi.Output[Sequence[builtins.str]]:
        """
        A list of possible values an attribute can take.
        """
        return pulumi.get(self, "tag_values")

