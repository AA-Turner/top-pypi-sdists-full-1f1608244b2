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

__all__ = ['DataCollectionRuleArgs', 'DataCollectionRule']

@pulumi.input_type
class DataCollectionRuleArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[builtins.str],
                 data_collection_endpoint_id: Optional[pulumi.Input[builtins.str]] = None,
                 data_collection_rule_name: Optional[pulumi.Input[builtins.str]] = None,
                 data_flows: Optional[pulumi.Input[Sequence[pulumi.Input['DataFlowArgs']]]] = None,
                 data_sources: Optional[pulumi.Input['DataCollectionRuleDataSourcesArgs']] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 destinations: Optional[pulumi.Input['DataCollectionRuleDestinationsArgs']] = None,
                 identity: Optional[pulumi.Input['DataCollectionRuleResourceIdentityArgs']] = None,
                 kind: Optional[pulumi.Input[Union[builtins.str, 'KnownDataCollectionRuleResourceKind']]] = None,
                 location: Optional[pulumi.Input[builtins.str]] = None,
                 stream_declarations: Optional[pulumi.Input[Mapping[str, pulumi.Input['StreamDeclarationArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None):
        """
        The set of arguments for constructing a DataCollectionRule resource.
        :param pulumi.Input[builtins.str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[builtins.str] data_collection_endpoint_id: The resource ID of the data collection endpoint that this rule can be used with.
        :param pulumi.Input[builtins.str] data_collection_rule_name: The name of the data collection rule. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input['DataFlowArgs']]] data_flows: The specification of data flows.
        :param pulumi.Input['DataCollectionRuleDataSourcesArgs'] data_sources: The specification of data sources. 
               This property is optional and can be omitted if the rule is meant to be used via direct calls to the provisioned endpoint.
        :param pulumi.Input[builtins.str] description: Description of the data collection rule.
        :param pulumi.Input['DataCollectionRuleDestinationsArgs'] destinations: The specification of destinations.
        :param pulumi.Input['DataCollectionRuleResourceIdentityArgs'] identity: Managed service identity of the resource.
        :param pulumi.Input[Union[builtins.str, 'KnownDataCollectionRuleResourceKind']] kind: The kind of the resource.
        :param pulumi.Input[builtins.str] location: The geo-location where the resource lives.
        :param pulumi.Input[Mapping[str, pulumi.Input['StreamDeclarationArgs']]] stream_declarations: Declaration of custom streams used in this rule.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if data_collection_endpoint_id is not None:
            pulumi.set(__self__, "data_collection_endpoint_id", data_collection_endpoint_id)
        if data_collection_rule_name is not None:
            pulumi.set(__self__, "data_collection_rule_name", data_collection_rule_name)
        if data_flows is not None:
            pulumi.set(__self__, "data_flows", data_flows)
        if data_sources is not None:
            pulumi.set(__self__, "data_sources", data_sources)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if destinations is not None:
            pulumi.set(__self__, "destinations", destinations)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if stream_declarations is not None:
            pulumi.set(__self__, "stream_declarations", stream_declarations)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[builtins.str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="dataCollectionEndpointId")
    def data_collection_endpoint_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The resource ID of the data collection endpoint that this rule can be used with.
        """
        return pulumi.get(self, "data_collection_endpoint_id")

    @data_collection_endpoint_id.setter
    def data_collection_endpoint_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "data_collection_endpoint_id", value)

    @property
    @pulumi.getter(name="dataCollectionRuleName")
    def data_collection_rule_name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the data collection rule. The name is case insensitive.
        """
        return pulumi.get(self, "data_collection_rule_name")

    @data_collection_rule_name.setter
    def data_collection_rule_name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "data_collection_rule_name", value)

    @property
    @pulumi.getter(name="dataFlows")
    def data_flows(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DataFlowArgs']]]]:
        """
        The specification of data flows.
        """
        return pulumi.get(self, "data_flows")

    @data_flows.setter
    def data_flows(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DataFlowArgs']]]]):
        pulumi.set(self, "data_flows", value)

    @property
    @pulumi.getter(name="dataSources")
    def data_sources(self) -> Optional[pulumi.Input['DataCollectionRuleDataSourcesArgs']]:
        """
        The specification of data sources. 
        This property is optional and can be omitted if the rule is meant to be used via direct calls to the provisioned endpoint.
        """
        return pulumi.get(self, "data_sources")

    @data_sources.setter
    def data_sources(self, value: Optional[pulumi.Input['DataCollectionRuleDataSourcesArgs']]):
        pulumi.set(self, "data_sources", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Description of the data collection rule.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def destinations(self) -> Optional[pulumi.Input['DataCollectionRuleDestinationsArgs']]:
        """
        The specification of destinations.
        """
        return pulumi.get(self, "destinations")

    @destinations.setter
    def destinations(self, value: Optional[pulumi.Input['DataCollectionRuleDestinationsArgs']]):
        pulumi.set(self, "destinations", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['DataCollectionRuleResourceIdentityArgs']]:
        """
        Managed service identity of the resource.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['DataCollectionRuleResourceIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[builtins.str, 'KnownDataCollectionRuleResourceKind']]]:
        """
        The kind of the resource.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[Union[builtins.str, 'KnownDataCollectionRuleResourceKind']]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The geo-location where the resource lives.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="streamDeclarations")
    def stream_declarations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['StreamDeclarationArgs']]]]:
        """
        Declaration of custom streams used in this rule.
        """
        return pulumi.get(self, "stream_declarations")

    @stream_declarations.setter
    def stream_declarations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['StreamDeclarationArgs']]]]):
        pulumi.set(self, "stream_declarations", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.type_token("azure-native:monitor:DataCollectionRule")
class DataCollectionRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_collection_endpoint_id: Optional[pulumi.Input[builtins.str]] = None,
                 data_collection_rule_name: Optional[pulumi.Input[builtins.str]] = None,
                 data_flows: Optional[pulumi.Input[Sequence[pulumi.Input[Union['DataFlowArgs', 'DataFlowArgsDict']]]]] = None,
                 data_sources: Optional[pulumi.Input[Union['DataCollectionRuleDataSourcesArgs', 'DataCollectionRuleDataSourcesArgsDict']]] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 destinations: Optional[pulumi.Input[Union['DataCollectionRuleDestinationsArgs', 'DataCollectionRuleDestinationsArgsDict']]] = None,
                 identity: Optional[pulumi.Input[Union['DataCollectionRuleResourceIdentityArgs', 'DataCollectionRuleResourceIdentityArgsDict']]] = None,
                 kind: Optional[pulumi.Input[Union[builtins.str, 'KnownDataCollectionRuleResourceKind']]] = None,
                 location: Optional[pulumi.Input[builtins.str]] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 stream_declarations: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union['StreamDeclarationArgs', 'StreamDeclarationArgsDict']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        """
        Definition of ARM tracked top level resource.

        Uses Azure REST API version 2022-06-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] data_collection_endpoint_id: The resource ID of the data collection endpoint that this rule can be used with.
        :param pulumi.Input[builtins.str] data_collection_rule_name: The name of the data collection rule. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[Union['DataFlowArgs', 'DataFlowArgsDict']]]] data_flows: The specification of data flows.
        :param pulumi.Input[Union['DataCollectionRuleDataSourcesArgs', 'DataCollectionRuleDataSourcesArgsDict']] data_sources: The specification of data sources. 
               This property is optional and can be omitted if the rule is meant to be used via direct calls to the provisioned endpoint.
        :param pulumi.Input[builtins.str] description: Description of the data collection rule.
        :param pulumi.Input[Union['DataCollectionRuleDestinationsArgs', 'DataCollectionRuleDestinationsArgsDict']] destinations: The specification of destinations.
        :param pulumi.Input[Union['DataCollectionRuleResourceIdentityArgs', 'DataCollectionRuleResourceIdentityArgsDict']] identity: Managed service identity of the resource.
        :param pulumi.Input[Union[builtins.str, 'KnownDataCollectionRuleResourceKind']] kind: The kind of the resource.
        :param pulumi.Input[builtins.str] location: The geo-location where the resource lives.
        :param pulumi.Input[builtins.str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[Union['StreamDeclarationArgs', 'StreamDeclarationArgsDict']]]] stream_declarations: Declaration of custom streams used in this rule.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DataCollectionRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of ARM tracked top level resource.

        Uses Azure REST API version 2022-06-01.

        :param str resource_name: The name of the resource.
        :param DataCollectionRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DataCollectionRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_collection_endpoint_id: Optional[pulumi.Input[builtins.str]] = None,
                 data_collection_rule_name: Optional[pulumi.Input[builtins.str]] = None,
                 data_flows: Optional[pulumi.Input[Sequence[pulumi.Input[Union['DataFlowArgs', 'DataFlowArgsDict']]]]] = None,
                 data_sources: Optional[pulumi.Input[Union['DataCollectionRuleDataSourcesArgs', 'DataCollectionRuleDataSourcesArgsDict']]] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 destinations: Optional[pulumi.Input[Union['DataCollectionRuleDestinationsArgs', 'DataCollectionRuleDestinationsArgsDict']]] = None,
                 identity: Optional[pulumi.Input[Union['DataCollectionRuleResourceIdentityArgs', 'DataCollectionRuleResourceIdentityArgsDict']]] = None,
                 kind: Optional[pulumi.Input[Union[builtins.str, 'KnownDataCollectionRuleResourceKind']]] = None,
                 location: Optional[pulumi.Input[builtins.str]] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 stream_declarations: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union['StreamDeclarationArgs', 'StreamDeclarationArgsDict']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DataCollectionRuleArgs.__new__(DataCollectionRuleArgs)

            __props__.__dict__["data_collection_endpoint_id"] = data_collection_endpoint_id
            __props__.__dict__["data_collection_rule_name"] = data_collection_rule_name
            __props__.__dict__["data_flows"] = data_flows
            __props__.__dict__["data_sources"] = data_sources
            __props__.__dict__["description"] = description
            __props__.__dict__["destinations"] = destinations
            __props__.__dict__["identity"] = identity
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["stream_declarations"] = stream_declarations
            __props__.__dict__["tags"] = tags
            __props__.__dict__["azure_api_version"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["immutable_id"] = None
            __props__.__dict__["metadata"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:insights/v20220601:DataCollectionRule"), pulumi.Alias(type_="azure-native:insights/v20230311:DataCollectionRule"), pulumi.Alias(type_="azure-native:insights:DataCollectionRule"), pulumi.Alias(type_="azure-native:monitor/v20191101preview:DataCollectionRule"), pulumi.Alias(type_="azure-native:monitor/v20210401:DataCollectionRule"), pulumi.Alias(type_="azure-native:monitor/v20210901preview:DataCollectionRule"), pulumi.Alias(type_="azure-native:monitor/v20220601:DataCollectionRule"), pulumi.Alias(type_="azure-native:monitor/v20230311:DataCollectionRule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DataCollectionRule, __self__).__init__(
            'azure-native:monitor:DataCollectionRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DataCollectionRule':
        """
        Get an existing DataCollectionRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DataCollectionRuleArgs.__new__(DataCollectionRuleArgs)

        __props__.__dict__["azure_api_version"] = None
        __props__.__dict__["data_collection_endpoint_id"] = None
        __props__.__dict__["data_flows"] = None
        __props__.__dict__["data_sources"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["destinations"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["immutable_id"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["stream_declarations"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return DataCollectionRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[builtins.str]:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter(name="dataCollectionEndpointId")
    def data_collection_endpoint_id(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The resource ID of the data collection endpoint that this rule can be used with.
        """
        return pulumi.get(self, "data_collection_endpoint_id")

    @property
    @pulumi.getter(name="dataFlows")
    def data_flows(self) -> pulumi.Output[Optional[Sequence['outputs.DataFlowResponse']]]:
        """
        The specification of data flows.
        """
        return pulumi.get(self, "data_flows")

    @property
    @pulumi.getter(name="dataSources")
    def data_sources(self) -> pulumi.Output[Optional['outputs.DataCollectionRuleResponseDataSources']]:
        """
        The specification of data sources. 
        This property is optional and can be omitted if the rule is meant to be used via direct calls to the provisioned endpoint.
        """
        return pulumi.get(self, "data_sources")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        Description of the data collection rule.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def destinations(self) -> pulumi.Output[Optional['outputs.DataCollectionRuleResponseDestinations']]:
        """
        The specification of destinations.
        """
        return pulumi.get(self, "destinations")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[builtins.str]:
        """
        Resource entity tag (ETag).
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.DataCollectionRuleResourceResponseIdentity']]:
        """
        Managed service identity of the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="immutableId")
    def immutable_id(self) -> pulumi.Output[builtins.str]:
        """
        The immutable ID of this data collection rule. This property is READ-ONLY.
        """
        return pulumi.get(self, "immutable_id")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The kind of the resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[builtins.str]:
        """
        The geo-location where the resource lives.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output['outputs.DataCollectionRuleResponseMetadata']:
        """
        Metadata about the resource
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[builtins.str]:
        """
        The resource provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="streamDeclarations")
    def stream_declarations(self) -> pulumi.Output[Optional[Mapping[str, 'outputs.StreamDeclarationResponse']]]:
        """
        Declaration of custom streams used in this rule.
        """
        return pulumi.get(self, "stream_declarations")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.DataCollectionRuleResourceResponseSystemData']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, builtins.str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[builtins.str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

