# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
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
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['RepositoryRulesetArgs', 'RepositoryRuleset']

@pulumi.input_type
class RepositoryRulesetArgs:
    def __init__(__self__, *,
                 enforcement: pulumi.Input[builtins.str],
                 rules: pulumi.Input['RepositoryRulesetRulesArgs'],
                 target: pulumi.Input[builtins.str],
                 bypass_actors: Optional[pulumi.Input[Sequence[pulumi.Input['RepositoryRulesetBypassActorArgs']]]] = None,
                 conditions: Optional[pulumi.Input['RepositoryRulesetConditionsArgs']] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 repository: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a RepositoryRuleset resource.
        :param pulumi.Input[builtins.str] enforcement: (String) Possible values for Enforcement are `disabled`, `active`, `evaluate`. Note: `evaluate` is currently only supported for owners of type `organization`.
        :param pulumi.Input['RepositoryRulesetRulesArgs'] rules: (Block List, Min: 1, Max: 1) Rules within the ruleset. (see below for nested schema)
        :param pulumi.Input[builtins.str] target: (String) Possible values are `branch` and `tag`.
        :param pulumi.Input[Sequence[pulumi.Input['RepositoryRulesetBypassActorArgs']]] bypass_actors: (Block List) The actors that can bypass the rules in this ruleset. (see below for nested schema)
        :param pulumi.Input['RepositoryRulesetConditionsArgs'] conditions: (Block List, Max: 1) Parameters for a repository ruleset ref name condition. (see below for nested schema)
        :param pulumi.Input[builtins.str] name: (String) The name of the ruleset.
        :param pulumi.Input[builtins.str] repository: (String) Name of the repository to apply rulset to.
        """
        pulumi.set(__self__, "enforcement", enforcement)
        pulumi.set(__self__, "rules", rules)
        pulumi.set(__self__, "target", target)
        if bypass_actors is not None:
            pulumi.set(__self__, "bypass_actors", bypass_actors)
        if conditions is not None:
            pulumi.set(__self__, "conditions", conditions)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if repository is not None:
            pulumi.set(__self__, "repository", repository)

    @property
    @pulumi.getter
    def enforcement(self) -> pulumi.Input[builtins.str]:
        """
        (String) Possible values for Enforcement are `disabled`, `active`, `evaluate`. Note: `evaluate` is currently only supported for owners of type `organization`.
        """
        return pulumi.get(self, "enforcement")

    @enforcement.setter
    def enforcement(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "enforcement", value)

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Input['RepositoryRulesetRulesArgs']:
        """
        (Block List, Min: 1, Max: 1) Rules within the ruleset. (see below for nested schema)
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: pulumi.Input['RepositoryRulesetRulesArgs']):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter
    def target(self) -> pulumi.Input[builtins.str]:
        """
        (String) Possible values are `branch` and `tag`.
        """
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "target", value)

    @property
    @pulumi.getter(name="bypassActors")
    def bypass_actors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RepositoryRulesetBypassActorArgs']]]]:
        """
        (Block List) The actors that can bypass the rules in this ruleset. (see below for nested schema)
        """
        return pulumi.get(self, "bypass_actors")

    @bypass_actors.setter
    def bypass_actors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RepositoryRulesetBypassActorArgs']]]]):
        pulumi.set(self, "bypass_actors", value)

    @property
    @pulumi.getter
    def conditions(self) -> Optional[pulumi.Input['RepositoryRulesetConditionsArgs']]:
        """
        (Block List, Max: 1) Parameters for a repository ruleset ref name condition. (see below for nested schema)
        """
        return pulumi.get(self, "conditions")

    @conditions.setter
    def conditions(self, value: Optional[pulumi.Input['RepositoryRulesetConditionsArgs']]):
        pulumi.set(self, "conditions", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        (String) The name of the ruleset.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def repository(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        (String) Name of the repository to apply rulset to.
        """
        return pulumi.get(self, "repository")

    @repository.setter
    def repository(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "repository", value)


@pulumi.input_type
class _RepositoryRulesetState:
    def __init__(__self__, *,
                 bypass_actors: Optional[pulumi.Input[Sequence[pulumi.Input['RepositoryRulesetBypassActorArgs']]]] = None,
                 conditions: Optional[pulumi.Input['RepositoryRulesetConditionsArgs']] = None,
                 enforcement: Optional[pulumi.Input[builtins.str]] = None,
                 etag: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 node_id: Optional[pulumi.Input[builtins.str]] = None,
                 repository: Optional[pulumi.Input[builtins.str]] = None,
                 rules: Optional[pulumi.Input['RepositoryRulesetRulesArgs']] = None,
                 ruleset_id: Optional[pulumi.Input[builtins.int]] = None,
                 target: Optional[pulumi.Input[builtins.str]] = None):
        """
        Input properties used for looking up and filtering RepositoryRuleset resources.
        :param pulumi.Input[Sequence[pulumi.Input['RepositoryRulesetBypassActorArgs']]] bypass_actors: (Block List) The actors that can bypass the rules in this ruleset. (see below for nested schema)
        :param pulumi.Input['RepositoryRulesetConditionsArgs'] conditions: (Block List, Max: 1) Parameters for a repository ruleset ref name condition. (see below for nested schema)
        :param pulumi.Input[builtins.str] enforcement: (String) Possible values for Enforcement are `disabled`, `active`, `evaluate`. Note: `evaluate` is currently only supported for owners of type `organization`.
        :param pulumi.Input[builtins.str] etag: (String)
        :param pulumi.Input[builtins.str] name: (String) The name of the ruleset.
        :param pulumi.Input[builtins.str] node_id: (String) GraphQL global node id for use with v4 API.
        :param pulumi.Input[builtins.str] repository: (String) Name of the repository to apply rulset to.
        :param pulumi.Input['RepositoryRulesetRulesArgs'] rules: (Block List, Min: 1, Max: 1) Rules within the ruleset. (see below for nested schema)
        :param pulumi.Input[builtins.int] ruleset_id: (Number) GitHub ID for the ruleset.
        :param pulumi.Input[builtins.str] target: (String) Possible values are `branch` and `tag`.
        """
        if bypass_actors is not None:
            pulumi.set(__self__, "bypass_actors", bypass_actors)
        if conditions is not None:
            pulumi.set(__self__, "conditions", conditions)
        if enforcement is not None:
            pulumi.set(__self__, "enforcement", enforcement)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if node_id is not None:
            pulumi.set(__self__, "node_id", node_id)
        if repository is not None:
            pulumi.set(__self__, "repository", repository)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)
        if ruleset_id is not None:
            pulumi.set(__self__, "ruleset_id", ruleset_id)
        if target is not None:
            pulumi.set(__self__, "target", target)

    @property
    @pulumi.getter(name="bypassActors")
    def bypass_actors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RepositoryRulesetBypassActorArgs']]]]:
        """
        (Block List) The actors that can bypass the rules in this ruleset. (see below for nested schema)
        """
        return pulumi.get(self, "bypass_actors")

    @bypass_actors.setter
    def bypass_actors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RepositoryRulesetBypassActorArgs']]]]):
        pulumi.set(self, "bypass_actors", value)

    @property
    @pulumi.getter
    def conditions(self) -> Optional[pulumi.Input['RepositoryRulesetConditionsArgs']]:
        """
        (Block List, Max: 1) Parameters for a repository ruleset ref name condition. (see below for nested schema)
        """
        return pulumi.get(self, "conditions")

    @conditions.setter
    def conditions(self, value: Optional[pulumi.Input['RepositoryRulesetConditionsArgs']]):
        pulumi.set(self, "conditions", value)

    @property
    @pulumi.getter
    def enforcement(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        (String) Possible values for Enforcement are `disabled`, `active`, `evaluate`. Note: `evaluate` is currently only supported for owners of type `organization`.
        """
        return pulumi.get(self, "enforcement")

    @enforcement.setter
    def enforcement(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "enforcement", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        (String)
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        (String) The name of the ruleset.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="nodeId")
    def node_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        (String) GraphQL global node id for use with v4 API.
        """
        return pulumi.get(self, "node_id")

    @node_id.setter
    def node_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "node_id", value)

    @property
    @pulumi.getter
    def repository(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        (String) Name of the repository to apply rulset to.
        """
        return pulumi.get(self, "repository")

    @repository.setter
    def repository(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "repository", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input['RepositoryRulesetRulesArgs']]:
        """
        (Block List, Min: 1, Max: 1) Rules within the ruleset. (see below for nested schema)
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input['RepositoryRulesetRulesArgs']]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter(name="rulesetId")
    def ruleset_id(self) -> Optional[pulumi.Input[builtins.int]]:
        """
        (Number) GitHub ID for the ruleset.
        """
        return pulumi.get(self, "ruleset_id")

    @ruleset_id.setter
    def ruleset_id(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "ruleset_id", value)

    @property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        (String) Possible values are `branch` and `tag`.
        """
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "target", value)


class RepositoryRuleset(pulumi.CustomResource):

    pulumi_type = "github:index/repositoryRuleset:RepositoryRuleset"

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bypass_actors: Optional[pulumi.Input[Sequence[pulumi.Input[Union['RepositoryRulesetBypassActorArgs', 'RepositoryRulesetBypassActorArgsDict']]]]] = None,
                 conditions: Optional[pulumi.Input[Union['RepositoryRulesetConditionsArgs', 'RepositoryRulesetConditionsArgsDict']]] = None,
                 enforcement: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 repository: Optional[pulumi.Input[builtins.str]] = None,
                 rules: Optional[pulumi.Input[Union['RepositoryRulesetRulesArgs', 'RepositoryRulesetRulesArgsDict']]] = None,
                 target: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        Creates a GitHub repository ruleset.

        This resource allows you to create and manage rulesets on the repository level. When applied, a new ruleset will be created. When destroyed, that ruleset will be removed.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_github as github

        example = github.Repository("example",
            name="example",
            description="Example repository")
        example_repository_ruleset = github.RepositoryRuleset("example",
            name="example",
            repository=example.name,
            target="branch",
            enforcement="active",
            conditions={
                "ref_name": {
                    "includes": ["~ALL"],
                    "excludes": [],
                },
            },
            bypass_actors=[{
                "actor_id": 13473,
                "actor_type": "Integration",
                "bypass_mode": "always",
            }],
            rules={
                "creation": True,
                "update": True,
                "deletion": True,
                "required_linear_history": True,
                "required_signatures": True,
                "required_deployments": {
                    "required_deployment_environments": ["test"],
                },
            })
        ```

        ## Import

        GitHub Repository Rulesets can be imported using the GitHub repository name and ruleset ID e.g.

        ```sh
        $ pulumi import github:index/repositoryRuleset:RepositoryRuleset example example:12345`
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['RepositoryRulesetBypassActorArgs', 'RepositoryRulesetBypassActorArgsDict']]]] bypass_actors: (Block List) The actors that can bypass the rules in this ruleset. (see below for nested schema)
        :param pulumi.Input[Union['RepositoryRulesetConditionsArgs', 'RepositoryRulesetConditionsArgsDict']] conditions: (Block List, Max: 1) Parameters for a repository ruleset ref name condition. (see below for nested schema)
        :param pulumi.Input[builtins.str] enforcement: (String) Possible values for Enforcement are `disabled`, `active`, `evaluate`. Note: `evaluate` is currently only supported for owners of type `organization`.
        :param pulumi.Input[builtins.str] name: (String) The name of the ruleset.
        :param pulumi.Input[builtins.str] repository: (String) Name of the repository to apply rulset to.
        :param pulumi.Input[Union['RepositoryRulesetRulesArgs', 'RepositoryRulesetRulesArgsDict']] rules: (Block List, Min: 1, Max: 1) Rules within the ruleset. (see below for nested schema)
        :param pulumi.Input[builtins.str] target: (String) Possible values are `branch` and `tag`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RepositoryRulesetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a GitHub repository ruleset.

        This resource allows you to create and manage rulesets on the repository level. When applied, a new ruleset will be created. When destroyed, that ruleset will be removed.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_github as github

        example = github.Repository("example",
            name="example",
            description="Example repository")
        example_repository_ruleset = github.RepositoryRuleset("example",
            name="example",
            repository=example.name,
            target="branch",
            enforcement="active",
            conditions={
                "ref_name": {
                    "includes": ["~ALL"],
                    "excludes": [],
                },
            },
            bypass_actors=[{
                "actor_id": 13473,
                "actor_type": "Integration",
                "bypass_mode": "always",
            }],
            rules={
                "creation": True,
                "update": True,
                "deletion": True,
                "required_linear_history": True,
                "required_signatures": True,
                "required_deployments": {
                    "required_deployment_environments": ["test"],
                },
            })
        ```

        ## Import

        GitHub Repository Rulesets can be imported using the GitHub repository name and ruleset ID e.g.

        ```sh
        $ pulumi import github:index/repositoryRuleset:RepositoryRuleset example example:12345`
        ```

        :param str resource_name: The name of the resource.
        :param RepositoryRulesetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RepositoryRulesetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bypass_actors: Optional[pulumi.Input[Sequence[pulumi.Input[Union['RepositoryRulesetBypassActorArgs', 'RepositoryRulesetBypassActorArgsDict']]]]] = None,
                 conditions: Optional[pulumi.Input[Union['RepositoryRulesetConditionsArgs', 'RepositoryRulesetConditionsArgsDict']]] = None,
                 enforcement: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 repository: Optional[pulumi.Input[builtins.str]] = None,
                 rules: Optional[pulumi.Input[Union['RepositoryRulesetRulesArgs', 'RepositoryRulesetRulesArgsDict']]] = None,
                 target: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RepositoryRulesetArgs.__new__(RepositoryRulesetArgs)

            __props__.__dict__["bypass_actors"] = bypass_actors
            __props__.__dict__["conditions"] = conditions
            if enforcement is None and not opts.urn:
                raise TypeError("Missing required property 'enforcement'")
            __props__.__dict__["enforcement"] = enforcement
            __props__.__dict__["name"] = name
            __props__.__dict__["repository"] = repository
            if rules is None and not opts.urn:
                raise TypeError("Missing required property 'rules'")
            __props__.__dict__["rules"] = rules
            if target is None and not opts.urn:
                raise TypeError("Missing required property 'target'")
            __props__.__dict__["target"] = target
            __props__.__dict__["etag"] = None
            __props__.__dict__["node_id"] = None
            __props__.__dict__["ruleset_id"] = None
        super(RepositoryRuleset, __self__).__init__(
            'github:index/repositoryRuleset:RepositoryRuleset',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bypass_actors: Optional[pulumi.Input[Sequence[pulumi.Input[Union['RepositoryRulesetBypassActorArgs', 'RepositoryRulesetBypassActorArgsDict']]]]] = None,
            conditions: Optional[pulumi.Input[Union['RepositoryRulesetConditionsArgs', 'RepositoryRulesetConditionsArgsDict']]] = None,
            enforcement: Optional[pulumi.Input[builtins.str]] = None,
            etag: Optional[pulumi.Input[builtins.str]] = None,
            name: Optional[pulumi.Input[builtins.str]] = None,
            node_id: Optional[pulumi.Input[builtins.str]] = None,
            repository: Optional[pulumi.Input[builtins.str]] = None,
            rules: Optional[pulumi.Input[Union['RepositoryRulesetRulesArgs', 'RepositoryRulesetRulesArgsDict']]] = None,
            ruleset_id: Optional[pulumi.Input[builtins.int]] = None,
            target: Optional[pulumi.Input[builtins.str]] = None) -> 'RepositoryRuleset':
        """
        Get an existing RepositoryRuleset resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['RepositoryRulesetBypassActorArgs', 'RepositoryRulesetBypassActorArgsDict']]]] bypass_actors: (Block List) The actors that can bypass the rules in this ruleset. (see below for nested schema)
        :param pulumi.Input[Union['RepositoryRulesetConditionsArgs', 'RepositoryRulesetConditionsArgsDict']] conditions: (Block List, Max: 1) Parameters for a repository ruleset ref name condition. (see below for nested schema)
        :param pulumi.Input[builtins.str] enforcement: (String) Possible values for Enforcement are `disabled`, `active`, `evaluate`. Note: `evaluate` is currently only supported for owners of type `organization`.
        :param pulumi.Input[builtins.str] etag: (String)
        :param pulumi.Input[builtins.str] name: (String) The name of the ruleset.
        :param pulumi.Input[builtins.str] node_id: (String) GraphQL global node id for use with v4 API.
        :param pulumi.Input[builtins.str] repository: (String) Name of the repository to apply rulset to.
        :param pulumi.Input[Union['RepositoryRulesetRulesArgs', 'RepositoryRulesetRulesArgsDict']] rules: (Block List, Min: 1, Max: 1) Rules within the ruleset. (see below for nested schema)
        :param pulumi.Input[builtins.int] ruleset_id: (Number) GitHub ID for the ruleset.
        :param pulumi.Input[builtins.str] target: (String) Possible values are `branch` and `tag`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RepositoryRulesetState.__new__(_RepositoryRulesetState)

        __props__.__dict__["bypass_actors"] = bypass_actors
        __props__.__dict__["conditions"] = conditions
        __props__.__dict__["enforcement"] = enforcement
        __props__.__dict__["etag"] = etag
        __props__.__dict__["name"] = name
        __props__.__dict__["node_id"] = node_id
        __props__.__dict__["repository"] = repository
        __props__.__dict__["rules"] = rules
        __props__.__dict__["ruleset_id"] = ruleset_id
        __props__.__dict__["target"] = target
        return RepositoryRuleset(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bypassActors")
    def bypass_actors(self) -> pulumi.Output[Optional[Sequence['outputs.RepositoryRulesetBypassActor']]]:
        """
        (Block List) The actors that can bypass the rules in this ruleset. (see below for nested schema)
        """
        return pulumi.get(self, "bypass_actors")

    @property
    @pulumi.getter
    def conditions(self) -> pulumi.Output[Optional['outputs.RepositoryRulesetConditions']]:
        """
        (Block List, Max: 1) Parameters for a repository ruleset ref name condition. (see below for nested schema)
        """
        return pulumi.get(self, "conditions")

    @property
    @pulumi.getter
    def enforcement(self) -> pulumi.Output[builtins.str]:
        """
        (String) Possible values for Enforcement are `disabled`, `active`, `evaluate`. Note: `evaluate` is currently only supported for owners of type `organization`.
        """
        return pulumi.get(self, "enforcement")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[builtins.str]:
        """
        (String)
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        (String) The name of the ruleset.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeId")
    def node_id(self) -> pulumi.Output[builtins.str]:
        """
        (String) GraphQL global node id for use with v4 API.
        """
        return pulumi.get(self, "node_id")

    @property
    @pulumi.getter
    def repository(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        (String) Name of the repository to apply rulset to.
        """
        return pulumi.get(self, "repository")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output['outputs.RepositoryRulesetRules']:
        """
        (Block List, Min: 1, Max: 1) Rules within the ruleset. (see below for nested schema)
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter(name="rulesetId")
    def ruleset_id(self) -> pulumi.Output[builtins.int]:
        """
        (Number) GitHub ID for the ruleset.
        """
        return pulumi.get(self, "ruleset_id")

    @property
    @pulumi.getter
    def target(self) -> pulumi.Output[builtins.str]:
        """
        (String) Possible values are `branch` and `tag`.
        """
        return pulumi.get(self, "target")

