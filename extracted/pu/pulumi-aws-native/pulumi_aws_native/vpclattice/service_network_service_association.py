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

__all__ = ['ServiceNetworkServiceAssociationArgs', 'ServiceNetworkServiceAssociation']

@pulumi.input_type
class ServiceNetworkServiceAssociationArgs:
    def __init__(__self__, *,
                 dns_entry: Optional[pulumi.Input['ServiceNetworkServiceAssociationDnsEntryArgs']] = None,
                 service_identifier: Optional[pulumi.Input[builtins.str]] = None,
                 service_network_identifier: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a ServiceNetworkServiceAssociation resource.
        :param pulumi.Input['ServiceNetworkServiceAssociationDnsEntryArgs'] dns_entry: The DNS information of the service.
        :param pulumi.Input[builtins.str] service_identifier: The ID or ARN of the service.
        :param pulumi.Input[builtins.str] service_network_identifier: The ID or ARN of the service network. You must use an ARN if the resources are in different accounts.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: The tags for the association.
        """
        if dns_entry is not None:
            pulumi.set(__self__, "dns_entry", dns_entry)
        if service_identifier is not None:
            pulumi.set(__self__, "service_identifier", service_identifier)
        if service_network_identifier is not None:
            pulumi.set(__self__, "service_network_identifier", service_network_identifier)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="dnsEntry")
    def dns_entry(self) -> Optional[pulumi.Input['ServiceNetworkServiceAssociationDnsEntryArgs']]:
        """
        The DNS information of the service.
        """
        return pulumi.get(self, "dns_entry")

    @dns_entry.setter
    def dns_entry(self, value: Optional[pulumi.Input['ServiceNetworkServiceAssociationDnsEntryArgs']]):
        pulumi.set(self, "dns_entry", value)

    @property
    @pulumi.getter(name="serviceIdentifier")
    def service_identifier(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The ID or ARN of the service.
        """
        return pulumi.get(self, "service_identifier")

    @service_identifier.setter
    def service_identifier(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "service_identifier", value)

    @property
    @pulumi.getter(name="serviceNetworkIdentifier")
    def service_network_identifier(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The ID or ARN of the service network. You must use an ARN if the resources are in different accounts.
        """
        return pulumi.get(self, "service_network_identifier")

    @service_network_identifier.setter
    def service_network_identifier(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "service_network_identifier", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        The tags for the association.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


@pulumi.type_token("aws-native:vpclattice:ServiceNetworkServiceAssociation")
class ServiceNetworkServiceAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dns_entry: Optional[pulumi.Input[Union['ServiceNetworkServiceAssociationDnsEntryArgs', 'ServiceNetworkServiceAssociationDnsEntryArgsDict']]] = None,
                 service_identifier: Optional[pulumi.Input[builtins.str]] = None,
                 service_network_identifier: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 __props__=None):
        """
        Associates a service with a service network.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['ServiceNetworkServiceAssociationDnsEntryArgs', 'ServiceNetworkServiceAssociationDnsEntryArgsDict']] dns_entry: The DNS information of the service.
        :param pulumi.Input[builtins.str] service_identifier: The ID or ARN of the service.
        :param pulumi.Input[builtins.str] service_network_identifier: The ID or ARN of the service network. You must use an ARN if the resources are in different accounts.
        :param pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]] tags: The tags for the association.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ServiceNetworkServiceAssociationArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Associates a service with a service network.

        :param str resource_name: The name of the resource.
        :param ServiceNetworkServiceAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServiceNetworkServiceAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dns_entry: Optional[pulumi.Input[Union['ServiceNetworkServiceAssociationDnsEntryArgs', 'ServiceNetworkServiceAssociationDnsEntryArgsDict']]] = None,
                 service_identifier: Optional[pulumi.Input[builtins.str]] = None,
                 service_network_identifier: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServiceNetworkServiceAssociationArgs.__new__(ServiceNetworkServiceAssociationArgs)

            __props__.__dict__["dns_entry"] = dns_entry
            __props__.__dict__["service_identifier"] = service_identifier
            __props__.__dict__["service_network_identifier"] = service_network_identifier
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["aws_id"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["service_arn"] = None
            __props__.__dict__["service_id"] = None
            __props__.__dict__["service_name"] = None
            __props__.__dict__["service_network_arn"] = None
            __props__.__dict__["service_network_id"] = None
            __props__.__dict__["service_network_name"] = None
            __props__.__dict__["status"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["serviceIdentifier", "serviceNetworkIdentifier"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ServiceNetworkServiceAssociation, __self__).__init__(
            'aws-native:vpclattice:ServiceNetworkServiceAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ServiceNetworkServiceAssociation':
        """
        Get an existing ServiceNetworkServiceAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServiceNetworkServiceAssociationArgs.__new__(ServiceNetworkServiceAssociationArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["aws_id"] = None
        __props__.__dict__["created_at"] = None
        __props__.__dict__["dns_entry"] = None
        __props__.__dict__["service_arn"] = None
        __props__.__dict__["service_id"] = None
        __props__.__dict__["service_identifier"] = None
        __props__.__dict__["service_name"] = None
        __props__.__dict__["service_network_arn"] = None
        __props__.__dict__["service_network_id"] = None
        __props__.__dict__["service_network_identifier"] = None
        __props__.__dict__["service_network_name"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        return ServiceNetworkServiceAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[builtins.str]:
        """
        The Amazon Resource Name (ARN) of the association between the service network and the service.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="awsId")
    def aws_id(self) -> pulumi.Output[builtins.str]:
        """
        The ID of the of the association between the service network and the service.
        """
        return pulumi.get(self, "aws_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[builtins.str]:
        """
        The date and time that the association was created, specified in ISO-8601 format.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="dnsEntry")
    def dns_entry(self) -> pulumi.Output[Optional['outputs.ServiceNetworkServiceAssociationDnsEntry']]:
        """
        The DNS information of the service.
        """
        return pulumi.get(self, "dns_entry")

    @property
    @pulumi.getter(name="serviceArn")
    def service_arn(self) -> pulumi.Output[builtins.str]:
        """
        The Amazon Resource Name (ARN) of the service.
        """
        return pulumi.get(self, "service_arn")

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> pulumi.Output[builtins.str]:
        """
        The ID of the service.
        """
        return pulumi.get(self, "service_id")

    @property
    @pulumi.getter(name="serviceIdentifier")
    def service_identifier(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The ID or ARN of the service.
        """
        return pulumi.get(self, "service_identifier")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[builtins.str]:
        """
        The name of the service.
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter(name="serviceNetworkArn")
    def service_network_arn(self) -> pulumi.Output[builtins.str]:
        """
        The Amazon Resource Name (ARN) of the service network
        """
        return pulumi.get(self, "service_network_arn")

    @property
    @pulumi.getter(name="serviceNetworkId")
    def service_network_id(self) -> pulumi.Output[builtins.str]:
        """
        The ID of the service network.
        """
        return pulumi.get(self, "service_network_id")

    @property
    @pulumi.getter(name="serviceNetworkIdentifier")
    def service_network_identifier(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The ID or ARN of the service network. You must use an ARN if the resources are in different accounts.
        """
        return pulumi.get(self, "service_network_identifier")

    @property
    @pulumi.getter(name="serviceNetworkName")
    def service_network_name(self) -> pulumi.Output[builtins.str]:
        """
        The name of the service network.
        """
        return pulumi.get(self, "service_network_name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['ServiceNetworkServiceAssociationStatus']:
        """
        The status of the association between the service network and the service.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        The tags for the association.
        """
        return pulumi.get(self, "tags")

