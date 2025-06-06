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

__all__ = ['ProjectArgs', 'Project']

@pulumi.input_type
class ProjectArgs:
    def __init__(__self__, *,
                 dataset_name: pulumi.Input[builtins.str],
                 recipe_name: pulumi.Input[builtins.str],
                 role_arn: pulumi.Input[builtins.str],
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 sample: Optional[pulumi.Input['ProjectSampleArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a Project resource.
        :param pulumi.Input[builtins.str] dataset_name: Dataset name
        :param pulumi.Input[builtins.str] recipe_name: Recipe name
        :param pulumi.Input[builtins.str] role_arn: Role arn
        :param pulumi.Input[builtins.str] name: Project name
        :param pulumi.Input['ProjectSampleArgs'] sample: Sample
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: Metadata tags that have been applied to the project.
        """
        pulumi.set(__self__, "dataset_name", dataset_name)
        pulumi.set(__self__, "recipe_name", recipe_name)
        pulumi.set(__self__, "role_arn", role_arn)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if sample is not None:
            pulumi.set(__self__, "sample", sample)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="datasetName")
    def dataset_name(self) -> pulumi.Input[builtins.str]:
        """
        Dataset name
        """
        return pulumi.get(self, "dataset_name")

    @dataset_name.setter
    def dataset_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "dataset_name", value)

    @property
    @pulumi.getter(name="recipeName")
    def recipe_name(self) -> pulumi.Input[builtins.str]:
        """
        Recipe name
        """
        return pulumi.get(self, "recipe_name")

    @recipe_name.setter
    def recipe_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "recipe_name", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[builtins.str]:
        """
        Role arn
        """
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Project name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def sample(self) -> Optional[pulumi.Input['ProjectSampleArgs']]:
        """
        Sample
        """
        return pulumi.get(self, "sample")

    @sample.setter
    def sample(self, value: Optional[pulumi.Input['ProjectSampleArgs']]):
        pulumi.set(self, "sample", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        Metadata tags that have been applied to the project.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


@pulumi.type_token("aws-native:databrew:Project")
class Project(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dataset_name: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 recipe_name: Optional[pulumi.Input[builtins.str]] = None,
                 role_arn: Optional[pulumi.Input[builtins.str]] = None,
                 sample: Optional[pulumi.Input[Union['ProjectSampleArgs', 'ProjectSampleArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 __props__=None):
        """
        Resource schema for AWS::DataBrew::Project.

        ## Example Usage
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        test_data_brew_project = aws_native.databrew.Project("testDataBrewProject",
            name="project-name",
            recipe_name="recipe-name",
            dataset_name="dataset-name",
            role_arn="arn:aws:iam::12345678910:role/PassRoleAdmin",
            sample={
                "size": 500,
                "type": aws_native.databrew.ProjectSampleType.LAST_N,
            })

        ```
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        my_data_brew_project = aws_native.databrew.Project("myDataBrewProject",
            name="test-project",
            recipe_name="test-project-recipe",
            dataset_name="test-dataset",
            role_arn="arn:aws:iam::1234567891011:role/PassRoleAdmin",
            sample={
                "size": 500,
                "type": aws_native.databrew.ProjectSampleType.LAST_N,
            },
            tags=[{
                "key": "key00AtCreate",
                "value": "value001AtCreate",
            }])

        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] dataset_name: Dataset name
        :param pulumi.Input[builtins.str] name: Project name
        :param pulumi.Input[builtins.str] recipe_name: Recipe name
        :param pulumi.Input[builtins.str] role_arn: Role arn
        :param pulumi.Input[Union['ProjectSampleArgs', 'ProjectSampleArgsDict']] sample: Sample
        :param pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]] tags: Metadata tags that have been applied to the project.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProjectArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::DataBrew::Project.

        ## Example Usage
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        test_data_brew_project = aws_native.databrew.Project("testDataBrewProject",
            name="project-name",
            recipe_name="recipe-name",
            dataset_name="dataset-name",
            role_arn="arn:aws:iam::12345678910:role/PassRoleAdmin",
            sample={
                "size": 500,
                "type": aws_native.databrew.ProjectSampleType.LAST_N,
            })

        ```
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        my_data_brew_project = aws_native.databrew.Project("myDataBrewProject",
            name="test-project",
            recipe_name="test-project-recipe",
            dataset_name="test-dataset",
            role_arn="arn:aws:iam::1234567891011:role/PassRoleAdmin",
            sample={
                "size": 500,
                "type": aws_native.databrew.ProjectSampleType.LAST_N,
            },
            tags=[{
                "key": "key00AtCreate",
                "value": "value001AtCreate",
            }])

        ```

        :param str resource_name: The name of the resource.
        :param ProjectArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProjectArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dataset_name: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 recipe_name: Optional[pulumi.Input[builtins.str]] = None,
                 role_arn: Optional[pulumi.Input[builtins.str]] = None,
                 sample: Optional[pulumi.Input[Union['ProjectSampleArgs', 'ProjectSampleArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProjectArgs.__new__(ProjectArgs)

            if dataset_name is None and not opts.urn:
                raise TypeError("Missing required property 'dataset_name'")
            __props__.__dict__["dataset_name"] = dataset_name
            __props__.__dict__["name"] = name
            if recipe_name is None and not opts.urn:
                raise TypeError("Missing required property 'recipe_name'")
            __props__.__dict__["recipe_name"] = recipe_name
            if role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'role_arn'")
            __props__.__dict__["role_arn"] = role_arn
            __props__.__dict__["sample"] = sample
            __props__.__dict__["tags"] = tags
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Project, __self__).__init__(
            'aws-native:databrew:Project',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Project':
        """
        Get an existing Project resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ProjectArgs.__new__(ProjectArgs)

        __props__.__dict__["dataset_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["recipe_name"] = None
        __props__.__dict__["role_arn"] = None
        __props__.__dict__["sample"] = None
        __props__.__dict__["tags"] = None
        return Project(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="datasetName")
    def dataset_name(self) -> pulumi.Output[builtins.str]:
        """
        Dataset name
        """
        return pulumi.get(self, "dataset_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        Project name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="recipeName")
    def recipe_name(self) -> pulumi.Output[builtins.str]:
        """
        Recipe name
        """
        return pulumi.get(self, "recipe_name")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[builtins.str]:
        """
        Role arn
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def sample(self) -> pulumi.Output[Optional['outputs.ProjectSample']]:
        """
        Sample
        """
        return pulumi.get(self, "sample")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        Metadata tags that have been applied to the project.
        """
        return pulumi.get(self, "tags")

