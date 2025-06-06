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

__all__ = ['GameServerGroupArgs', 'GameServerGroup']

@pulumi.input_type
class GameServerGroupArgs:
    def __init__(__self__, *,
                 instance_definitions: pulumi.Input[Sequence[pulumi.Input['GameServerGroupInstanceDefinitionArgs']]],
                 role_arn: pulumi.Input[builtins.str],
                 auto_scaling_policy: Optional[pulumi.Input['GameServerGroupAutoScalingPolicyArgs']] = None,
                 balancing_strategy: Optional[pulumi.Input['GameServerGroupBalancingStrategy']] = None,
                 delete_option: Optional[pulumi.Input['GameServerGroupDeleteOption']] = None,
                 game_server_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 game_server_protection_policy: Optional[pulumi.Input['GameServerGroupGameServerProtectionPolicy']] = None,
                 launch_template: Optional[pulumi.Input['GameServerGroupLaunchTemplateArgs']] = None,
                 max_size: Optional[pulumi.Input[builtins.float]] = None,
                 min_size: Optional[pulumi.Input[builtins.float]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None,
                 vpc_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None):
        """
        The set of arguments for constructing a GameServerGroup resource.
        :param pulumi.Input[Sequence[pulumi.Input['GameServerGroupInstanceDefinitionArgs']]] instance_definitions: A set of EC2 instance types to use when creating instances in the group.
        :param pulumi.Input[builtins.str] role_arn: The Amazon Resource Name (ARN) for an IAM role that allows Amazon GameLift to access your EC2 Auto Scaling groups.
        :param pulumi.Input['GameServerGroupAutoScalingPolicyArgs'] auto_scaling_policy: Configuration settings to define a scaling policy for the Auto Scaling group that is optimized for game hosting. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.
        :param pulumi.Input['GameServerGroupBalancingStrategy'] balancing_strategy: The fallback balancing method to use for the game server group when Spot Instances in a Region become unavailable or are not viable for game hosting.
        :param pulumi.Input['GameServerGroupDeleteOption'] delete_option: The type of delete to perform.
        :param pulumi.Input[builtins.str] game_server_group_name: An identifier for the new game server group.
        :param pulumi.Input['GameServerGroupGameServerProtectionPolicy'] game_server_protection_policy: A flag that indicates whether instances in the game server group are protected from early termination.
        :param pulumi.Input['GameServerGroupLaunchTemplateArgs'] launch_template: The EC2 launch template that contains configuration settings and game server code to be deployed to all instances in the game server group. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.
        :param pulumi.Input[builtins.float] max_size: The maximum number of instances allowed in the EC2 Auto Scaling group. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.
        :param pulumi.Input[builtins.float] min_size: The minimum number of instances allowed in the EC2 Auto Scaling group. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: A list of labels to assign to the new game server group resource. Updating game server group tags with CloudFormation will not take effect. Please update this property using AWS GameLift APIs instead.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] vpc_subnets: A list of virtual private cloud (VPC) subnets to use with instances in the game server group. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.
        """
        pulumi.set(__self__, "instance_definitions", instance_definitions)
        pulumi.set(__self__, "role_arn", role_arn)
        if auto_scaling_policy is not None:
            pulumi.set(__self__, "auto_scaling_policy", auto_scaling_policy)
        if balancing_strategy is not None:
            pulumi.set(__self__, "balancing_strategy", balancing_strategy)
        if delete_option is not None:
            pulumi.set(__self__, "delete_option", delete_option)
        if game_server_group_name is not None:
            pulumi.set(__self__, "game_server_group_name", game_server_group_name)
        if game_server_protection_policy is not None:
            pulumi.set(__self__, "game_server_protection_policy", game_server_protection_policy)
        if launch_template is not None:
            pulumi.set(__self__, "launch_template", launch_template)
        if max_size is not None:
            pulumi.set(__self__, "max_size", max_size)
        if min_size is not None:
            pulumi.set(__self__, "min_size", min_size)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if vpc_subnets is not None:
            pulumi.set(__self__, "vpc_subnets", vpc_subnets)

    @property
    @pulumi.getter(name="instanceDefinitions")
    def instance_definitions(self) -> pulumi.Input[Sequence[pulumi.Input['GameServerGroupInstanceDefinitionArgs']]]:
        """
        A set of EC2 instance types to use when creating instances in the group.
        """
        return pulumi.get(self, "instance_definitions")

    @instance_definitions.setter
    def instance_definitions(self, value: pulumi.Input[Sequence[pulumi.Input['GameServerGroupInstanceDefinitionArgs']]]):
        pulumi.set(self, "instance_definitions", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[builtins.str]:
        """
        The Amazon Resource Name (ARN) for an IAM role that allows Amazon GameLift to access your EC2 Auto Scaling groups.
        """
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter(name="autoScalingPolicy")
    def auto_scaling_policy(self) -> Optional[pulumi.Input['GameServerGroupAutoScalingPolicyArgs']]:
        """
        Configuration settings to define a scaling policy for the Auto Scaling group that is optimized for game hosting. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.
        """
        return pulumi.get(self, "auto_scaling_policy")

    @auto_scaling_policy.setter
    def auto_scaling_policy(self, value: Optional[pulumi.Input['GameServerGroupAutoScalingPolicyArgs']]):
        pulumi.set(self, "auto_scaling_policy", value)

    @property
    @pulumi.getter(name="balancingStrategy")
    def balancing_strategy(self) -> Optional[pulumi.Input['GameServerGroupBalancingStrategy']]:
        """
        The fallback balancing method to use for the game server group when Spot Instances in a Region become unavailable or are not viable for game hosting.
        """
        return pulumi.get(self, "balancing_strategy")

    @balancing_strategy.setter
    def balancing_strategy(self, value: Optional[pulumi.Input['GameServerGroupBalancingStrategy']]):
        pulumi.set(self, "balancing_strategy", value)

    @property
    @pulumi.getter(name="deleteOption")
    def delete_option(self) -> Optional[pulumi.Input['GameServerGroupDeleteOption']]:
        """
        The type of delete to perform.
        """
        return pulumi.get(self, "delete_option")

    @delete_option.setter
    def delete_option(self, value: Optional[pulumi.Input['GameServerGroupDeleteOption']]):
        pulumi.set(self, "delete_option", value)

    @property
    @pulumi.getter(name="gameServerGroupName")
    def game_server_group_name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        An identifier for the new game server group.
        """
        return pulumi.get(self, "game_server_group_name")

    @game_server_group_name.setter
    def game_server_group_name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "game_server_group_name", value)

    @property
    @pulumi.getter(name="gameServerProtectionPolicy")
    def game_server_protection_policy(self) -> Optional[pulumi.Input['GameServerGroupGameServerProtectionPolicy']]:
        """
        A flag that indicates whether instances in the game server group are protected from early termination.
        """
        return pulumi.get(self, "game_server_protection_policy")

    @game_server_protection_policy.setter
    def game_server_protection_policy(self, value: Optional[pulumi.Input['GameServerGroupGameServerProtectionPolicy']]):
        pulumi.set(self, "game_server_protection_policy", value)

    @property
    @pulumi.getter(name="launchTemplate")
    def launch_template(self) -> Optional[pulumi.Input['GameServerGroupLaunchTemplateArgs']]:
        """
        The EC2 launch template that contains configuration settings and game server code to be deployed to all instances in the game server group. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.
        """
        return pulumi.get(self, "launch_template")

    @launch_template.setter
    def launch_template(self, value: Optional[pulumi.Input['GameServerGroupLaunchTemplateArgs']]):
        pulumi.set(self, "launch_template", value)

    @property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> Optional[pulumi.Input[builtins.float]]:
        """
        The maximum number of instances allowed in the EC2 Auto Scaling group. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.
        """
        return pulumi.get(self, "max_size")

    @max_size.setter
    def max_size(self, value: Optional[pulumi.Input[builtins.float]]):
        pulumi.set(self, "max_size", value)

    @property
    @pulumi.getter(name="minSize")
    def min_size(self) -> Optional[pulumi.Input[builtins.float]]:
        """
        The minimum number of instances allowed in the EC2 Auto Scaling group. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.
        """
        return pulumi.get(self, "min_size")

    @min_size.setter
    def min_size(self, value: Optional[pulumi.Input[builtins.float]]):
        pulumi.set(self, "min_size", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        A list of labels to assign to the new game server group resource. Updating game server group tags with CloudFormation will not take effect. Please update this property using AWS GameLift APIs instead.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="vpcSubnets")
    def vpc_subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]:
        """
        A list of virtual private cloud (VPC) subnets to use with instances in the game server group. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.
        """
        return pulumi.get(self, "vpc_subnets")

    @vpc_subnets.setter
    def vpc_subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "vpc_subnets", value)


@pulumi.type_token("aws-native:gamelift:GameServerGroup")
class GameServerGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_scaling_policy: Optional[pulumi.Input[Union['GameServerGroupAutoScalingPolicyArgs', 'GameServerGroupAutoScalingPolicyArgsDict']]] = None,
                 balancing_strategy: Optional[pulumi.Input['GameServerGroupBalancingStrategy']] = None,
                 delete_option: Optional[pulumi.Input['GameServerGroupDeleteOption']] = None,
                 game_server_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 game_server_protection_policy: Optional[pulumi.Input['GameServerGroupGameServerProtectionPolicy']] = None,
                 instance_definitions: Optional[pulumi.Input[Sequence[pulumi.Input[Union['GameServerGroupInstanceDefinitionArgs', 'GameServerGroupInstanceDefinitionArgsDict']]]]] = None,
                 launch_template: Optional[pulumi.Input[Union['GameServerGroupLaunchTemplateArgs', 'GameServerGroupLaunchTemplateArgsDict']]] = None,
                 max_size: Optional[pulumi.Input[builtins.float]] = None,
                 min_size: Optional[pulumi.Input[builtins.float]] = None,
                 role_arn: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 vpc_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        """
        The AWS::GameLift::GameServerGroup resource creates an Amazon GameLift (GameLift) GameServerGroup.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['GameServerGroupAutoScalingPolicyArgs', 'GameServerGroupAutoScalingPolicyArgsDict']] auto_scaling_policy: Configuration settings to define a scaling policy for the Auto Scaling group that is optimized for game hosting. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.
        :param pulumi.Input['GameServerGroupBalancingStrategy'] balancing_strategy: The fallback balancing method to use for the game server group when Spot Instances in a Region become unavailable or are not viable for game hosting.
        :param pulumi.Input['GameServerGroupDeleteOption'] delete_option: The type of delete to perform.
        :param pulumi.Input[builtins.str] game_server_group_name: An identifier for the new game server group.
        :param pulumi.Input['GameServerGroupGameServerProtectionPolicy'] game_server_protection_policy: A flag that indicates whether instances in the game server group are protected from early termination.
        :param pulumi.Input[Sequence[pulumi.Input[Union['GameServerGroupInstanceDefinitionArgs', 'GameServerGroupInstanceDefinitionArgsDict']]]] instance_definitions: A set of EC2 instance types to use when creating instances in the group.
        :param pulumi.Input[Union['GameServerGroupLaunchTemplateArgs', 'GameServerGroupLaunchTemplateArgsDict']] launch_template: The EC2 launch template that contains configuration settings and game server code to be deployed to all instances in the game server group. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.
        :param pulumi.Input[builtins.float] max_size: The maximum number of instances allowed in the EC2 Auto Scaling group. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.
        :param pulumi.Input[builtins.float] min_size: The minimum number of instances allowed in the EC2 Auto Scaling group. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.
        :param pulumi.Input[builtins.str] role_arn: The Amazon Resource Name (ARN) for an IAM role that allows Amazon GameLift to access your EC2 Auto Scaling groups.
        :param pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]] tags: A list of labels to assign to the new game server group resource. Updating game server group tags with CloudFormation will not take effect. Please update this property using AWS GameLift APIs instead.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] vpc_subnets: A list of virtual private cloud (VPC) subnets to use with instances in the game server group. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GameServerGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::GameLift::GameServerGroup resource creates an Amazon GameLift (GameLift) GameServerGroup.

        :param str resource_name: The name of the resource.
        :param GameServerGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GameServerGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_scaling_policy: Optional[pulumi.Input[Union['GameServerGroupAutoScalingPolicyArgs', 'GameServerGroupAutoScalingPolicyArgsDict']]] = None,
                 balancing_strategy: Optional[pulumi.Input['GameServerGroupBalancingStrategy']] = None,
                 delete_option: Optional[pulumi.Input['GameServerGroupDeleteOption']] = None,
                 game_server_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 game_server_protection_policy: Optional[pulumi.Input['GameServerGroupGameServerProtectionPolicy']] = None,
                 instance_definitions: Optional[pulumi.Input[Sequence[pulumi.Input[Union['GameServerGroupInstanceDefinitionArgs', 'GameServerGroupInstanceDefinitionArgsDict']]]]] = None,
                 launch_template: Optional[pulumi.Input[Union['GameServerGroupLaunchTemplateArgs', 'GameServerGroupLaunchTemplateArgsDict']]] = None,
                 max_size: Optional[pulumi.Input[builtins.float]] = None,
                 min_size: Optional[pulumi.Input[builtins.float]] = None,
                 role_arn: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 vpc_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GameServerGroupArgs.__new__(GameServerGroupArgs)

            __props__.__dict__["auto_scaling_policy"] = auto_scaling_policy
            __props__.__dict__["balancing_strategy"] = balancing_strategy
            __props__.__dict__["delete_option"] = delete_option
            __props__.__dict__["game_server_group_name"] = game_server_group_name
            __props__.__dict__["game_server_protection_policy"] = game_server_protection_policy
            if instance_definitions is None and not opts.urn:
                raise TypeError("Missing required property 'instance_definitions'")
            __props__.__dict__["instance_definitions"] = instance_definitions
            __props__.__dict__["launch_template"] = launch_template
            __props__.__dict__["max_size"] = max_size
            __props__.__dict__["min_size"] = min_size
            if role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'role_arn'")
            __props__.__dict__["role_arn"] = role_arn
            __props__.__dict__["tags"] = tags
            __props__.__dict__["vpc_subnets"] = vpc_subnets
            __props__.__dict__["auto_scaling_group_arn"] = None
            __props__.__dict__["game_server_group_arn"] = None
        super(GameServerGroup, __self__).__init__(
            'aws-native:gamelift:GameServerGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'GameServerGroup':
        """
        Get an existing GameServerGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GameServerGroupArgs.__new__(GameServerGroupArgs)

        __props__.__dict__["auto_scaling_group_arn"] = None
        __props__.__dict__["auto_scaling_policy"] = None
        __props__.__dict__["balancing_strategy"] = None
        __props__.__dict__["delete_option"] = None
        __props__.__dict__["game_server_group_arn"] = None
        __props__.__dict__["game_server_group_name"] = None
        __props__.__dict__["game_server_protection_policy"] = None
        __props__.__dict__["instance_definitions"] = None
        __props__.__dict__["launch_template"] = None
        __props__.__dict__["max_size"] = None
        __props__.__dict__["min_size"] = None
        __props__.__dict__["role_arn"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["vpc_subnets"] = None
        return GameServerGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoScalingGroupArn")
    def auto_scaling_group_arn(self) -> pulumi.Output[builtins.str]:
        """
        A generated unique ID for the EC2 Auto Scaling group that is associated with this game server group.
        """
        return pulumi.get(self, "auto_scaling_group_arn")

    @property
    @pulumi.getter(name="autoScalingPolicy")
    def auto_scaling_policy(self) -> pulumi.Output[Optional['outputs.GameServerGroupAutoScalingPolicy']]:
        """
        Configuration settings to define a scaling policy for the Auto Scaling group that is optimized for game hosting. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.
        """
        return pulumi.get(self, "auto_scaling_policy")

    @property
    @pulumi.getter(name="balancingStrategy")
    def balancing_strategy(self) -> pulumi.Output[Optional['GameServerGroupBalancingStrategy']]:
        """
        The fallback balancing method to use for the game server group when Spot Instances in a Region become unavailable or are not viable for game hosting.
        """
        return pulumi.get(self, "balancing_strategy")

    @property
    @pulumi.getter(name="deleteOption")
    def delete_option(self) -> pulumi.Output[Optional['GameServerGroupDeleteOption']]:
        """
        The type of delete to perform.
        """
        return pulumi.get(self, "delete_option")

    @property
    @pulumi.getter(name="gameServerGroupArn")
    def game_server_group_arn(self) -> pulumi.Output[builtins.str]:
        """
        A generated unique ID for the game server group.
        """
        return pulumi.get(self, "game_server_group_arn")

    @property
    @pulumi.getter(name="gameServerGroupName")
    def game_server_group_name(self) -> pulumi.Output[builtins.str]:
        """
        An identifier for the new game server group.
        """
        return pulumi.get(self, "game_server_group_name")

    @property
    @pulumi.getter(name="gameServerProtectionPolicy")
    def game_server_protection_policy(self) -> pulumi.Output[Optional['GameServerGroupGameServerProtectionPolicy']]:
        """
        A flag that indicates whether instances in the game server group are protected from early termination.
        """
        return pulumi.get(self, "game_server_protection_policy")

    @property
    @pulumi.getter(name="instanceDefinitions")
    def instance_definitions(self) -> pulumi.Output[Sequence['outputs.GameServerGroupInstanceDefinition']]:
        """
        A set of EC2 instance types to use when creating instances in the group.
        """
        return pulumi.get(self, "instance_definitions")

    @property
    @pulumi.getter(name="launchTemplate")
    def launch_template(self) -> pulumi.Output[Optional['outputs.GameServerGroupLaunchTemplate']]:
        """
        The EC2 launch template that contains configuration settings and game server code to be deployed to all instances in the game server group. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.
        """
        return pulumi.get(self, "launch_template")

    @property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> pulumi.Output[Optional[builtins.float]]:
        """
        The maximum number of instances allowed in the EC2 Auto Scaling group. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.
        """
        return pulumi.get(self, "max_size")

    @property
    @pulumi.getter(name="minSize")
    def min_size(self) -> pulumi.Output[Optional[builtins.float]]:
        """
        The minimum number of instances allowed in the EC2 Auto Scaling group. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.
        """
        return pulumi.get(self, "min_size")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[builtins.str]:
        """
        The Amazon Resource Name (ARN) for an IAM role that allows Amazon GameLift to access your EC2 Auto Scaling groups.
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        A list of labels to assign to the new game server group resource. Updating game server group tags with CloudFormation will not take effect. Please update this property using AWS GameLift APIs instead.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcSubnets")
    def vpc_subnets(self) -> pulumi.Output[Optional[Sequence[builtins.str]]]:
        """
        A list of virtual private cloud (VPC) subnets to use with instances in the game server group. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.
        """
        return pulumi.get(self, "vpc_subnets")

