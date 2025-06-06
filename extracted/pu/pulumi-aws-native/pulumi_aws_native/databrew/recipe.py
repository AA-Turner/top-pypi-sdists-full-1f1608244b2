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
from ._inputs import *

__all__ = ['RecipeArgs', 'Recipe']

@pulumi.input_type
class RecipeArgs:
    def __init__(__self__, *,
                 steps: pulumi.Input[Sequence[pulumi.Input['RecipeStepArgs']]],
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a Recipe resource.
        :param pulumi.Input[Sequence[pulumi.Input['RecipeStepArgs']]] steps: A list of steps that are defined by the recipe.
        :param pulumi.Input[builtins.str] description: Description of the recipe
        :param pulumi.Input[builtins.str] name: Recipe name
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: Metadata tags that have been applied to the recipe.
        """
        pulumi.set(__self__, "steps", steps)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def steps(self) -> pulumi.Input[Sequence[pulumi.Input['RecipeStepArgs']]]:
        """
        A list of steps that are defined by the recipe.
        """
        return pulumi.get(self, "steps")

    @steps.setter
    def steps(self, value: pulumi.Input[Sequence[pulumi.Input['RecipeStepArgs']]]):
        pulumi.set(self, "steps", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Description of the recipe
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Recipe name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        Metadata tags that have been applied to the recipe.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


@pulumi.type_token("aws-native:databrew:Recipe")
class Recipe(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 steps: Optional[pulumi.Input[Sequence[pulumi.Input[Union['RecipeStepArgs', 'RecipeStepArgsDict']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 __props__=None):
        """
        Resource schema for AWS::DataBrew::Recipe.

        ## Example Usage
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        test_data_brew_recipe = aws_native.databrew.Recipe("testDataBrewRecipe",
            name="recipe-name",
            description="This is the recipe description.",
            steps=[{
                "action": {
                    "operation": "EXTRACT_PATTERN",
                    "parameters": {
                        "sourceColumn": "Consulate",
                        "pattern": "A",
                        "targetColumn": "extract_pattern",
                    },
                },
                "condition_expressions": [{
                    "condition": "LESS_THAN_EQUAL",
                    "value": "5",
                    "target_column": "Target",
                }],
            }],
            tags=[{
                "key": "key00AtCreate",
                "value": "value001AtCreate",
            }])

        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] description: Description of the recipe
        :param pulumi.Input[builtins.str] name: Recipe name
        :param pulumi.Input[Sequence[pulumi.Input[Union['RecipeStepArgs', 'RecipeStepArgsDict']]]] steps: A list of steps that are defined by the recipe.
        :param pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]] tags: Metadata tags that have been applied to the recipe.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RecipeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::DataBrew::Recipe.

        ## Example Usage
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        test_data_brew_recipe = aws_native.databrew.Recipe("testDataBrewRecipe",
            name="recipe-name",
            description="This is the recipe description.",
            steps=[{
                "action": {
                    "operation": "EXTRACT_PATTERN",
                    "parameters": {
                        "sourceColumn": "Consulate",
                        "pattern": "A",
                        "targetColumn": "extract_pattern",
                    },
                },
                "condition_expressions": [{
                    "condition": "LESS_THAN_EQUAL",
                    "value": "5",
                    "target_column": "Target",
                }],
            }],
            tags=[{
                "key": "key00AtCreate",
                "value": "value001AtCreate",
            }])

        ```

        :param str resource_name: The name of the resource.
        :param RecipeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RecipeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 steps: Optional[pulumi.Input[Sequence[pulumi.Input[Union['RecipeStepArgs', 'RecipeStepArgsDict']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RecipeArgs.__new__(RecipeArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if steps is None and not opts.urn:
                raise TypeError("Missing required property 'steps'")
            __props__.__dict__["steps"] = steps
            __props__.__dict__["tags"] = tags
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Recipe, __self__).__init__(
            'aws-native:databrew:Recipe',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Recipe':
        """
        Get an existing Recipe resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RecipeArgs.__new__(RecipeArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["steps"] = None
        __props__.__dict__["tags"] = None
        return Recipe(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        Description of the recipe
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        Recipe name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def steps(self) -> pulumi.Output[Sequence['outputs.RecipeStep']]:
        """
        A list of steps that are defined by the recipe.
        """
        return pulumi.get(self, "steps")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        Metadata tags that have been applied to the recipe.
        """
        return pulumi.get(self, "tags")

