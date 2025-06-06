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

__all__ = ['OwnerArgs', 'Owner']

@pulumi.input_type
class OwnerArgs:
    def __init__(__self__, *,
                 domain_identifier: pulumi.Input[builtins.str],
                 entity_identifier: pulumi.Input[builtins.str],
                 entity_type: pulumi.Input['OwnerEntityType'],
                 owner: pulumi.Input['OwnerPropertiesArgs']):
        """
        The set of arguments for constructing a Owner resource.
        :param pulumi.Input[builtins.str] domain_identifier: The ID of the domain in which you want to add the entity owner.
        :param pulumi.Input[builtins.str] entity_identifier: The ID of the entity to which you want to add an owner.
        :param pulumi.Input['OwnerEntityType'] entity_type: The type of an entity.
        :param pulumi.Input['OwnerPropertiesArgs'] owner: The owner that you want to add to the entity.
        """
        pulumi.set(__self__, "domain_identifier", domain_identifier)
        pulumi.set(__self__, "entity_identifier", entity_identifier)
        pulumi.set(__self__, "entity_type", entity_type)
        pulumi.set(__self__, "owner", owner)

    @property
    @pulumi.getter(name="domainIdentifier")
    def domain_identifier(self) -> pulumi.Input[builtins.str]:
        """
        The ID of the domain in which you want to add the entity owner.
        """
        return pulumi.get(self, "domain_identifier")

    @domain_identifier.setter
    def domain_identifier(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "domain_identifier", value)

    @property
    @pulumi.getter(name="entityIdentifier")
    def entity_identifier(self) -> pulumi.Input[builtins.str]:
        """
        The ID of the entity to which you want to add an owner.
        """
        return pulumi.get(self, "entity_identifier")

    @entity_identifier.setter
    def entity_identifier(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "entity_identifier", value)

    @property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> pulumi.Input['OwnerEntityType']:
        """
        The type of an entity.
        """
        return pulumi.get(self, "entity_type")

    @entity_type.setter
    def entity_type(self, value: pulumi.Input['OwnerEntityType']):
        pulumi.set(self, "entity_type", value)

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Input['OwnerPropertiesArgs']:
        """
        The owner that you want to add to the entity.
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: pulumi.Input['OwnerPropertiesArgs']):
        pulumi.set(self, "owner", value)


@pulumi.type_token("aws-native:datazone:Owner")
class Owner(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_identifier: Optional[pulumi.Input[builtins.str]] = None,
                 entity_identifier: Optional[pulumi.Input[builtins.str]] = None,
                 entity_type: Optional[pulumi.Input['OwnerEntityType']] = None,
                 owner: Optional[pulumi.Input[Union['OwnerPropertiesArgs', 'OwnerPropertiesArgsDict']]] = None,
                 __props__=None):
        """
        A owner can set up authorization permissions on their resources.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] domain_identifier: The ID of the domain in which you want to add the entity owner.
        :param pulumi.Input[builtins.str] entity_identifier: The ID of the entity to which you want to add an owner.
        :param pulumi.Input['OwnerEntityType'] entity_type: The type of an entity.
        :param pulumi.Input[Union['OwnerPropertiesArgs', 'OwnerPropertiesArgsDict']] owner: The owner that you want to add to the entity.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OwnerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A owner can set up authorization permissions on their resources.

        :param str resource_name: The name of the resource.
        :param OwnerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OwnerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_identifier: Optional[pulumi.Input[builtins.str]] = None,
                 entity_identifier: Optional[pulumi.Input[builtins.str]] = None,
                 entity_type: Optional[pulumi.Input['OwnerEntityType']] = None,
                 owner: Optional[pulumi.Input[Union['OwnerPropertiesArgs', 'OwnerPropertiesArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OwnerArgs.__new__(OwnerArgs)

            if domain_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'domain_identifier'")
            __props__.__dict__["domain_identifier"] = domain_identifier
            if entity_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'entity_identifier'")
            __props__.__dict__["entity_identifier"] = entity_identifier
            if entity_type is None and not opts.urn:
                raise TypeError("Missing required property 'entity_type'")
            __props__.__dict__["entity_type"] = entity_type
            if owner is None and not opts.urn:
                raise TypeError("Missing required property 'owner'")
            __props__.__dict__["owner"] = owner
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["domainIdentifier", "entityIdentifier", "entityType", "owner"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Owner, __self__).__init__(
            'aws-native:datazone:Owner',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Owner':
        """
        Get an existing Owner resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OwnerArgs.__new__(OwnerArgs)

        __props__.__dict__["domain_identifier"] = None
        __props__.__dict__["entity_identifier"] = None
        __props__.__dict__["entity_type"] = None
        __props__.__dict__["owner"] = None
        return Owner(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="domainIdentifier")
    def domain_identifier(self) -> pulumi.Output[builtins.str]:
        """
        The ID of the domain in which you want to add the entity owner.
        """
        return pulumi.get(self, "domain_identifier")

    @property
    @pulumi.getter(name="entityIdentifier")
    def entity_identifier(self) -> pulumi.Output[builtins.str]:
        """
        The ID of the entity to which you want to add an owner.
        """
        return pulumi.get(self, "entity_identifier")

    @property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> pulumi.Output['OwnerEntityType']:
        """
        The type of an entity.
        """
        return pulumi.get(self, "entity_type")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output['outputs.OwnerProperties']:
        """
        The owner that you want to add to the entity.
        """
        return pulumi.get(self, "owner")

