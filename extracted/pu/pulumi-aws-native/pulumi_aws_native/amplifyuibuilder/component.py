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

__all__ = ['ComponentArgs', 'Component']

@pulumi.input_type
class ComponentArgs:
    def __init__(__self__, *,
                 app_id: Optional[pulumi.Input[builtins.str]] = None,
                 binding_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input['ComponentBindingPropertiesValueArgs']]]] = None,
                 children: Optional[pulumi.Input[Sequence[pulumi.Input['ComponentChildArgs']]]] = None,
                 collection_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input['ComponentDataConfigurationArgs']]]] = None,
                 component_type: Optional[pulumi.Input[builtins.str]] = None,
                 environment_name: Optional[pulumi.Input[builtins.str]] = None,
                 events: Optional[pulumi.Input[Mapping[str, pulumi.Input['ComponentEventArgs']]]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 overrides: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, pulumi.Input['ComponentPropertyArgs']]]] = None,
                 schema_version: Optional[pulumi.Input[builtins.str]] = None,
                 source_id: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 variants: Optional[pulumi.Input[Sequence[pulumi.Input['ComponentVariantArgs']]]] = None):
        """
        The set of arguments for constructing a Component resource.
        :param pulumi.Input[builtins.str] app_id: The unique ID of the Amplify app associated with the component.
        :param pulumi.Input[Mapping[str, pulumi.Input['ComponentBindingPropertiesValueArgs']]] binding_properties: The information to connect a component's properties to data at runtime. You can't specify `tags` as a valid property for `bindingProperties` .
        :param pulumi.Input[Sequence[pulumi.Input['ComponentChildArgs']]] children: A list of the component's `ComponentChild` instances.
        :param pulumi.Input[Mapping[str, pulumi.Input['ComponentDataConfigurationArgs']]] collection_properties: The data binding configuration for the component's properties. Use this for a collection component. You can't specify `tags` as a valid property for `collectionProperties` .
        :param pulumi.Input[builtins.str] component_type: The type of the component. This can be an Amplify custom UI component or another custom component.
        :param pulumi.Input[builtins.str] environment_name: The name of the backend environment that is a part of the Amplify app.
        :param pulumi.Input[Mapping[str, pulumi.Input['ComponentEventArgs']]] events: Describes the events that can be raised on the component. Use for the workflow feature in Amplify Studio that allows you to bind events and actions to components.
        :param pulumi.Input[builtins.str] name: The name of the component.
        :param pulumi.Input[Mapping[str, Any]] overrides: Describes the component's properties that can be overriden in a customized instance of the component. You can't specify `tags` as a valid property for `overrides` .
        :param pulumi.Input[Mapping[str, pulumi.Input['ComponentPropertyArgs']]] properties: Describes the component's properties. You can't specify `tags` as a valid property for `properties` .
        :param pulumi.Input[builtins.str] schema_version: The schema version of the component when it was imported.
        :param pulumi.Input[builtins.str] source_id: The unique ID of the component in its original source system, such as Figma.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] tags: One or more key-value pairs to use when tagging the component.
        :param pulumi.Input[Sequence[pulumi.Input['ComponentVariantArgs']]] variants: A list of the component's variants. A variant is a unique style configuration of a main component.
        """
        if app_id is not None:
            pulumi.set(__self__, "app_id", app_id)
        if binding_properties is not None:
            pulumi.set(__self__, "binding_properties", binding_properties)
        if children is not None:
            pulumi.set(__self__, "children", children)
        if collection_properties is not None:
            pulumi.set(__self__, "collection_properties", collection_properties)
        if component_type is not None:
            pulumi.set(__self__, "component_type", component_type)
        if environment_name is not None:
            pulumi.set(__self__, "environment_name", environment_name)
        if events is not None:
            pulumi.set(__self__, "events", events)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if overrides is not None:
            pulumi.set(__self__, "overrides", overrides)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if schema_version is not None:
            pulumi.set(__self__, "schema_version", schema_version)
        if source_id is not None:
            pulumi.set(__self__, "source_id", source_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if variants is not None:
            pulumi.set(__self__, "variants", variants)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The unique ID of the Amplify app associated with the component.
        """
        return pulumi.get(self, "app_id")

    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "app_id", value)

    @property
    @pulumi.getter(name="bindingProperties")
    def binding_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['ComponentBindingPropertiesValueArgs']]]]:
        """
        The information to connect a component's properties to data at runtime. You can't specify `tags` as a valid property for `bindingProperties` .
        """
        return pulumi.get(self, "binding_properties")

    @binding_properties.setter
    def binding_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['ComponentBindingPropertiesValueArgs']]]]):
        pulumi.set(self, "binding_properties", value)

    @property
    @pulumi.getter
    def children(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ComponentChildArgs']]]]:
        """
        A list of the component's `ComponentChild` instances.
        """
        return pulumi.get(self, "children")

    @children.setter
    def children(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ComponentChildArgs']]]]):
        pulumi.set(self, "children", value)

    @property
    @pulumi.getter(name="collectionProperties")
    def collection_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['ComponentDataConfigurationArgs']]]]:
        """
        The data binding configuration for the component's properties. Use this for a collection component. You can't specify `tags` as a valid property for `collectionProperties` .
        """
        return pulumi.get(self, "collection_properties")

    @collection_properties.setter
    def collection_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['ComponentDataConfigurationArgs']]]]):
        pulumi.set(self, "collection_properties", value)

    @property
    @pulumi.getter(name="componentType")
    def component_type(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The type of the component. This can be an Amplify custom UI component or another custom component.
        """
        return pulumi.get(self, "component_type")

    @component_type.setter
    def component_type(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "component_type", value)

    @property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the backend environment that is a part of the Amplify app.
        """
        return pulumi.get(self, "environment_name")

    @environment_name.setter
    def environment_name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "environment_name", value)

    @property
    @pulumi.getter
    def events(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['ComponentEventArgs']]]]:
        """
        Describes the events that can be raised on the component. Use for the workflow feature in Amplify Studio that allows you to bind events and actions to components.
        """
        return pulumi.get(self, "events")

    @events.setter
    def events(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['ComponentEventArgs']]]]):
        pulumi.set(self, "events", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the component.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def overrides(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Describes the component's properties that can be overriden in a customized instance of the component. You can't specify `tags` as a valid property for `overrides` .
        """
        return pulumi.get(self, "overrides")

    @overrides.setter
    def overrides(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "overrides", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['ComponentPropertyArgs']]]]:
        """
        Describes the component's properties. You can't specify `tags` as a valid property for `properties` .
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['ComponentPropertyArgs']]]]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="schemaVersion")
    def schema_version(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The schema version of the component when it was imported.
        """
        return pulumi.get(self, "schema_version")

    @schema_version.setter
    def schema_version(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "schema_version", value)

    @property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The unique ID of the component in its original source system, such as Figma.
        """
        return pulumi.get(self, "source_id")

    @source_id.setter
    def source_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "source_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]:
        """
        One or more key-value pairs to use when tagging the component.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def variants(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ComponentVariantArgs']]]]:
        """
        A list of the component's variants. A variant is a unique style configuration of a main component.
        """
        return pulumi.get(self, "variants")

    @variants.setter
    def variants(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ComponentVariantArgs']]]]):
        pulumi.set(self, "variants", value)


@pulumi.type_token("aws-native:amplifyuibuilder:Component")
class Component(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[builtins.str]] = None,
                 binding_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union['ComponentBindingPropertiesValueArgs', 'ComponentBindingPropertiesValueArgsDict']]]]] = None,
                 children: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ComponentChildArgs', 'ComponentChildArgsDict']]]]] = None,
                 collection_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union['ComponentDataConfigurationArgs', 'ComponentDataConfigurationArgsDict']]]]] = None,
                 component_type: Optional[pulumi.Input[builtins.str]] = None,
                 environment_name: Optional[pulumi.Input[builtins.str]] = None,
                 events: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union['ComponentEventArgs', 'ComponentEventArgsDict']]]]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 overrides: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union['ComponentPropertyArgs', 'ComponentPropertyArgsDict']]]]] = None,
                 schema_version: Optional[pulumi.Input[builtins.str]] = None,
                 source_id: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 variants: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ComponentVariantArgs', 'ComponentVariantArgsDict']]]]] = None,
                 __props__=None):
        """
        Definition of AWS::AmplifyUIBuilder::Component Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] app_id: The unique ID of the Amplify app associated with the component.
        :param pulumi.Input[Mapping[str, pulumi.Input[Union['ComponentBindingPropertiesValueArgs', 'ComponentBindingPropertiesValueArgsDict']]]] binding_properties: The information to connect a component's properties to data at runtime. You can't specify `tags` as a valid property for `bindingProperties` .
        :param pulumi.Input[Sequence[pulumi.Input[Union['ComponentChildArgs', 'ComponentChildArgsDict']]]] children: A list of the component's `ComponentChild` instances.
        :param pulumi.Input[Mapping[str, pulumi.Input[Union['ComponentDataConfigurationArgs', 'ComponentDataConfigurationArgsDict']]]] collection_properties: The data binding configuration for the component's properties. Use this for a collection component. You can't specify `tags` as a valid property for `collectionProperties` .
        :param pulumi.Input[builtins.str] component_type: The type of the component. This can be an Amplify custom UI component or another custom component.
        :param pulumi.Input[builtins.str] environment_name: The name of the backend environment that is a part of the Amplify app.
        :param pulumi.Input[Mapping[str, pulumi.Input[Union['ComponentEventArgs', 'ComponentEventArgsDict']]]] events: Describes the events that can be raised on the component. Use for the workflow feature in Amplify Studio that allows you to bind events and actions to components.
        :param pulumi.Input[builtins.str] name: The name of the component.
        :param pulumi.Input[Mapping[str, Any]] overrides: Describes the component's properties that can be overriden in a customized instance of the component. You can't specify `tags` as a valid property for `overrides` .
        :param pulumi.Input[Mapping[str, pulumi.Input[Union['ComponentPropertyArgs', 'ComponentPropertyArgsDict']]]] properties: Describes the component's properties. You can't specify `tags` as a valid property for `properties` .
        :param pulumi.Input[builtins.str] schema_version: The schema version of the component when it was imported.
        :param pulumi.Input[builtins.str] source_id: The unique ID of the component in its original source system, such as Figma.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] tags: One or more key-value pairs to use when tagging the component.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ComponentVariantArgs', 'ComponentVariantArgsDict']]]] variants: A list of the component's variants. A variant is a unique style configuration of a main component.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ComponentArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::AmplifyUIBuilder::Component Resource Type

        :param str resource_name: The name of the resource.
        :param ComponentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ComponentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[builtins.str]] = None,
                 binding_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union['ComponentBindingPropertiesValueArgs', 'ComponentBindingPropertiesValueArgsDict']]]]] = None,
                 children: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ComponentChildArgs', 'ComponentChildArgsDict']]]]] = None,
                 collection_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union['ComponentDataConfigurationArgs', 'ComponentDataConfigurationArgsDict']]]]] = None,
                 component_type: Optional[pulumi.Input[builtins.str]] = None,
                 environment_name: Optional[pulumi.Input[builtins.str]] = None,
                 events: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union['ComponentEventArgs', 'ComponentEventArgsDict']]]]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 overrides: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union['ComponentPropertyArgs', 'ComponentPropertyArgsDict']]]]] = None,
                 schema_version: Optional[pulumi.Input[builtins.str]] = None,
                 source_id: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 variants: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ComponentVariantArgs', 'ComponentVariantArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ComponentArgs.__new__(ComponentArgs)

            __props__.__dict__["app_id"] = app_id
            __props__.__dict__["binding_properties"] = binding_properties
            __props__.__dict__["children"] = children
            __props__.__dict__["collection_properties"] = collection_properties
            __props__.__dict__["component_type"] = component_type
            __props__.__dict__["environment_name"] = environment_name
            __props__.__dict__["events"] = events
            __props__.__dict__["name"] = name
            __props__.__dict__["overrides"] = overrides
            __props__.__dict__["properties"] = properties
            __props__.__dict__["schema_version"] = schema_version
            __props__.__dict__["source_id"] = source_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["variants"] = variants
            __props__.__dict__["aws_id"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["modified_at"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["appId", "environmentName"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Component, __self__).__init__(
            'aws-native:amplifyuibuilder:Component',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Component':
        """
        Get an existing Component resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ComponentArgs.__new__(ComponentArgs)

        __props__.__dict__["app_id"] = None
        __props__.__dict__["aws_id"] = None
        __props__.__dict__["binding_properties"] = None
        __props__.__dict__["children"] = None
        __props__.__dict__["collection_properties"] = None
        __props__.__dict__["component_type"] = None
        __props__.__dict__["created_at"] = None
        __props__.__dict__["environment_name"] = None
        __props__.__dict__["events"] = None
        __props__.__dict__["modified_at"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["overrides"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["schema_version"] = None
        __props__.__dict__["source_id"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["variants"] = None
        return Component(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The unique ID of the Amplify app associated with the component.
        """
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter(name="awsId")
    def aws_id(self) -> pulumi.Output[builtins.str]:
        """
        The unique ID of the component.
        """
        return pulumi.get(self, "aws_id")

    @property
    @pulumi.getter(name="bindingProperties")
    def binding_properties(self) -> pulumi.Output[Optional[Mapping[str, 'outputs.ComponentBindingPropertiesValue']]]:
        """
        The information to connect a component's properties to data at runtime. You can't specify `tags` as a valid property for `bindingProperties` .
        """
        return pulumi.get(self, "binding_properties")

    @property
    @pulumi.getter
    def children(self) -> pulumi.Output[Optional[Sequence['outputs.ComponentChild']]]:
        """
        A list of the component's `ComponentChild` instances.
        """
        return pulumi.get(self, "children")

    @property
    @pulumi.getter(name="collectionProperties")
    def collection_properties(self) -> pulumi.Output[Optional[Mapping[str, 'outputs.ComponentDataConfiguration']]]:
        """
        The data binding configuration for the component's properties. Use this for a collection component. You can't specify `tags` as a valid property for `collectionProperties` .
        """
        return pulumi.get(self, "collection_properties")

    @property
    @pulumi.getter(name="componentType")
    def component_type(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The type of the component. This can be an Amplify custom UI component or another custom component.
        """
        return pulumi.get(self, "component_type")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[builtins.str]:
        """
        The time that the component was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The name of the backend environment that is a part of the Amplify app.
        """
        return pulumi.get(self, "environment_name")

    @property
    @pulumi.getter
    def events(self) -> pulumi.Output[Optional[Mapping[str, 'outputs.ComponentEvent']]]:
        """
        Describes the events that can be raised on the component. Use for the workflow feature in Amplify Studio that allows you to bind events and actions to components.
        """
        return pulumi.get(self, "events")

    @property
    @pulumi.getter(name="modifiedAt")
    def modified_at(self) -> pulumi.Output[builtins.str]:
        """
        The time that the component was modified.
        """
        return pulumi.get(self, "modified_at")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The name of the component.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def overrides(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        Describes the component's properties that can be overriden in a customized instance of the component. You can't specify `tags` as a valid property for `overrides` .
        """
        return pulumi.get(self, "overrides")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Optional[Mapping[str, 'outputs.ComponentProperty']]]:
        """
        Describes the component's properties. You can't specify `tags` as a valid property for `properties` .
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="schemaVersion")
    def schema_version(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The schema version of the component when it was imported.
        """
        return pulumi.get(self, "schema_version")

    @property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The unique ID of the component in its original source system, such as Figma.
        """
        return pulumi.get(self, "source_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, builtins.str]]]:
        """
        One or more key-value pairs to use when tagging the component.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def variants(self) -> pulumi.Output[Optional[Sequence['outputs.ComponentVariant']]]:
        """
        A list of the component's variants. A variant is a unique style configuration of a main component.
        """
        return pulumi.get(self, "variants")

