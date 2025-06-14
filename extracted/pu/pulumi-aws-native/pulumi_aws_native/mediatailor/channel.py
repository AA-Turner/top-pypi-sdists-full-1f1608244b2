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

__all__ = ['ChannelArgs', 'Channel']

@pulumi.input_type
class ChannelArgs:
    def __init__(__self__, *,
                 outputs: pulumi.Input[Sequence[pulumi.Input['ChannelRequestOutputItemArgs']]],
                 playback_mode: pulumi.Input['ChannelPlaybackMode'],
                 audiences: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 channel_name: Optional[pulumi.Input[builtins.str]] = None,
                 filler_slate: Optional[pulumi.Input['ChannelSlateSourceArgs']] = None,
                 log_configuration: Optional[pulumi.Input['ChannelLogConfigurationForChannelArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None,
                 tier: Optional[pulumi.Input['ChannelTier']] = None,
                 time_shift_configuration: Optional[pulumi.Input['ChannelTimeShiftConfigurationArgs']] = None):
        """
        The set of arguments for constructing a Channel resource.
        :param pulumi.Input[Sequence[pulumi.Input['ChannelRequestOutputItemArgs']]] outputs: <p>The channel's output properties.</p>
        :param pulumi.Input['ChannelPlaybackMode'] playback_mode: The type of playback mode for this channel.
               
               `LINEAR` - Programs play back-to-back only once.
               
               `LOOP` - Programs play back-to-back in an endless loop. When the last program in the schedule plays, playback loops back to the first program in the schedule.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] audiences: <p>The list of audiences defined in channel.</p>
        :param pulumi.Input[builtins.str] channel_name: The name of the channel.
        :param pulumi.Input['ChannelSlateSourceArgs'] filler_slate: The slate used to fill gaps between programs in the schedule. You must configure filler slate if your channel uses the `LINEAR` `PlaybackMode` . MediaTailor doesn't support filler slate for channels using the `LOOP` `PlaybackMode` .
        :param pulumi.Input['ChannelLogConfigurationForChannelArgs'] log_configuration: The log configuration.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: The tags to assign to the channel.
        :param pulumi.Input['ChannelTier'] tier: The tier for this channel. STANDARD tier channels can contain live programs.
        :param pulumi.Input['ChannelTimeShiftConfigurationArgs'] time_shift_configuration: The configuration for time-shifted viewing.
        """
        pulumi.set(__self__, "outputs", outputs)
        pulumi.set(__self__, "playback_mode", playback_mode)
        if audiences is not None:
            pulumi.set(__self__, "audiences", audiences)
        if channel_name is not None:
            pulumi.set(__self__, "channel_name", channel_name)
        if filler_slate is not None:
            pulumi.set(__self__, "filler_slate", filler_slate)
        if log_configuration is not None:
            pulumi.set(__self__, "log_configuration", log_configuration)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)
        if time_shift_configuration is not None:
            pulumi.set(__self__, "time_shift_configuration", time_shift_configuration)

    @property
    @pulumi.getter
    def outputs(self) -> pulumi.Input[Sequence[pulumi.Input['ChannelRequestOutputItemArgs']]]:
        """
        <p>The channel's output properties.</p>
        """
        return pulumi.get(self, "outputs")

    @outputs.setter
    def outputs(self, value: pulumi.Input[Sequence[pulumi.Input['ChannelRequestOutputItemArgs']]]):
        pulumi.set(self, "outputs", value)

    @property
    @pulumi.getter(name="playbackMode")
    def playback_mode(self) -> pulumi.Input['ChannelPlaybackMode']:
        """
        The type of playback mode for this channel.

        `LINEAR` - Programs play back-to-back only once.

        `LOOP` - Programs play back-to-back in an endless loop. When the last program in the schedule plays, playback loops back to the first program in the schedule.
        """
        return pulumi.get(self, "playback_mode")

    @playback_mode.setter
    def playback_mode(self, value: pulumi.Input['ChannelPlaybackMode']):
        pulumi.set(self, "playback_mode", value)

    @property
    @pulumi.getter
    def audiences(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]:
        """
        <p>The list of audiences defined in channel.</p>
        """
        return pulumi.get(self, "audiences")

    @audiences.setter
    def audiences(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "audiences", value)

    @property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the channel.
        """
        return pulumi.get(self, "channel_name")

    @channel_name.setter
    def channel_name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "channel_name", value)

    @property
    @pulumi.getter(name="fillerSlate")
    def filler_slate(self) -> Optional[pulumi.Input['ChannelSlateSourceArgs']]:
        """
        The slate used to fill gaps between programs in the schedule. You must configure filler slate if your channel uses the `LINEAR` `PlaybackMode` . MediaTailor doesn't support filler slate for channels using the `LOOP` `PlaybackMode` .
        """
        return pulumi.get(self, "filler_slate")

    @filler_slate.setter
    def filler_slate(self, value: Optional[pulumi.Input['ChannelSlateSourceArgs']]):
        pulumi.set(self, "filler_slate", value)

    @property
    @pulumi.getter(name="logConfiguration")
    def log_configuration(self) -> Optional[pulumi.Input['ChannelLogConfigurationForChannelArgs']]:
        """
        The log configuration.
        """
        return pulumi.get(self, "log_configuration")

    @log_configuration.setter
    def log_configuration(self, value: Optional[pulumi.Input['ChannelLogConfigurationForChannelArgs']]):
        pulumi.set(self, "log_configuration", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        The tags to assign to the channel.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input['ChannelTier']]:
        """
        The tier for this channel. STANDARD tier channels can contain live programs.
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: Optional[pulumi.Input['ChannelTier']]):
        pulumi.set(self, "tier", value)

    @property
    @pulumi.getter(name="timeShiftConfiguration")
    def time_shift_configuration(self) -> Optional[pulumi.Input['ChannelTimeShiftConfigurationArgs']]:
        """
        The configuration for time-shifted viewing.
        """
        return pulumi.get(self, "time_shift_configuration")

    @time_shift_configuration.setter
    def time_shift_configuration(self, value: Optional[pulumi.Input['ChannelTimeShiftConfigurationArgs']]):
        pulumi.set(self, "time_shift_configuration", value)


@pulumi.type_token("aws-native:mediatailor:Channel")
class Channel(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 audiences: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 channel_name: Optional[pulumi.Input[builtins.str]] = None,
                 filler_slate: Optional[pulumi.Input[Union['ChannelSlateSourceArgs', 'ChannelSlateSourceArgsDict']]] = None,
                 log_configuration: Optional[pulumi.Input[Union['ChannelLogConfigurationForChannelArgs', 'ChannelLogConfigurationForChannelArgsDict']]] = None,
                 outputs: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ChannelRequestOutputItemArgs', 'ChannelRequestOutputItemArgsDict']]]]] = None,
                 playback_mode: Optional[pulumi.Input['ChannelPlaybackMode']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 tier: Optional[pulumi.Input['ChannelTier']] = None,
                 time_shift_configuration: Optional[pulumi.Input[Union['ChannelTimeShiftConfigurationArgs', 'ChannelTimeShiftConfigurationArgsDict']]] = None,
                 __props__=None):
        """
        Definition of AWS::MediaTailor::Channel Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] audiences: <p>The list of audiences defined in channel.</p>
        :param pulumi.Input[builtins.str] channel_name: The name of the channel.
        :param pulumi.Input[Union['ChannelSlateSourceArgs', 'ChannelSlateSourceArgsDict']] filler_slate: The slate used to fill gaps between programs in the schedule. You must configure filler slate if your channel uses the `LINEAR` `PlaybackMode` . MediaTailor doesn't support filler slate for channels using the `LOOP` `PlaybackMode` .
        :param pulumi.Input[Union['ChannelLogConfigurationForChannelArgs', 'ChannelLogConfigurationForChannelArgsDict']] log_configuration: The log configuration.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ChannelRequestOutputItemArgs', 'ChannelRequestOutputItemArgsDict']]]] outputs: <p>The channel's output properties.</p>
        :param pulumi.Input['ChannelPlaybackMode'] playback_mode: The type of playback mode for this channel.
               
               `LINEAR` - Programs play back-to-back only once.
               
               `LOOP` - Programs play back-to-back in an endless loop. When the last program in the schedule plays, playback loops back to the first program in the schedule.
        :param pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]] tags: The tags to assign to the channel.
        :param pulumi.Input['ChannelTier'] tier: The tier for this channel. STANDARD tier channels can contain live programs.
        :param pulumi.Input[Union['ChannelTimeShiftConfigurationArgs', 'ChannelTimeShiftConfigurationArgsDict']] time_shift_configuration: The configuration for time-shifted viewing.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ChannelArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::MediaTailor::Channel Resource Type

        :param str resource_name: The name of the resource.
        :param ChannelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ChannelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 audiences: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 channel_name: Optional[pulumi.Input[builtins.str]] = None,
                 filler_slate: Optional[pulumi.Input[Union['ChannelSlateSourceArgs', 'ChannelSlateSourceArgsDict']]] = None,
                 log_configuration: Optional[pulumi.Input[Union['ChannelLogConfigurationForChannelArgs', 'ChannelLogConfigurationForChannelArgsDict']]] = None,
                 outputs: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ChannelRequestOutputItemArgs', 'ChannelRequestOutputItemArgsDict']]]]] = None,
                 playback_mode: Optional[pulumi.Input['ChannelPlaybackMode']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 tier: Optional[pulumi.Input['ChannelTier']] = None,
                 time_shift_configuration: Optional[pulumi.Input[Union['ChannelTimeShiftConfigurationArgs', 'ChannelTimeShiftConfigurationArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ChannelArgs.__new__(ChannelArgs)

            __props__.__dict__["audiences"] = audiences
            __props__.__dict__["channel_name"] = channel_name
            __props__.__dict__["filler_slate"] = filler_slate
            __props__.__dict__["log_configuration"] = log_configuration
            if outputs is None and not opts.urn:
                raise TypeError("Missing required property 'outputs'")
            __props__.__dict__["outputs"] = outputs
            if playback_mode is None and not opts.urn:
                raise TypeError("Missing required property 'playback_mode'")
            __props__.__dict__["playback_mode"] = playback_mode
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tier"] = tier
            __props__.__dict__["time_shift_configuration"] = time_shift_configuration
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["channelName", "tier"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Channel, __self__).__init__(
            'aws-native:mediatailor:Channel',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Channel':
        """
        Get an existing Channel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ChannelArgs.__new__(ChannelArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["audiences"] = None
        __props__.__dict__["channel_name"] = None
        __props__.__dict__["filler_slate"] = None
        __props__.__dict__["log_configuration"] = None
        __props__.__dict__["outputs"] = None
        __props__.__dict__["playback_mode"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["tier"] = None
        __props__.__dict__["time_shift_configuration"] = None
        return Channel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[builtins.str]:
        """
        <p>The ARN of the channel.</p>
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def audiences(self) -> pulumi.Output[Optional[Sequence[builtins.str]]]:
        """
        <p>The list of audiences defined in channel.</p>
        """
        return pulumi.get(self, "audiences")

    @property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Output[builtins.str]:
        """
        The name of the channel.
        """
        return pulumi.get(self, "channel_name")

    @property
    @pulumi.getter(name="fillerSlate")
    def filler_slate(self) -> pulumi.Output[Optional['outputs.ChannelSlateSource']]:
        """
        The slate used to fill gaps between programs in the schedule. You must configure filler slate if your channel uses the `LINEAR` `PlaybackMode` . MediaTailor doesn't support filler slate for channels using the `LOOP` `PlaybackMode` .
        """
        return pulumi.get(self, "filler_slate")

    @property
    @pulumi.getter(name="logConfiguration")
    def log_configuration(self) -> pulumi.Output[Optional['outputs.ChannelLogConfigurationForChannel']]:
        """
        The log configuration.
        """
        return pulumi.get(self, "log_configuration")

    @property
    @pulumi.getter
    def outputs(self) -> pulumi.Output[Sequence['outputs.ChannelRequestOutputItem']]:
        """
        <p>The channel's output properties.</p>
        """
        return pulumi.get(self, "outputs")

    @property
    @pulumi.getter(name="playbackMode")
    def playback_mode(self) -> pulumi.Output['ChannelPlaybackMode']:
        """
        The type of playback mode for this channel.

        `LINEAR` - Programs play back-to-back only once.

        `LOOP` - Programs play back-to-back in an endless loop. When the last program in the schedule plays, playback loops back to the first program in the schedule.
        """
        return pulumi.get(self, "playback_mode")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        The tags to assign to the channel.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def tier(self) -> pulumi.Output[Optional['ChannelTier']]:
        """
        The tier for this channel. STANDARD tier channels can contain live programs.
        """
        return pulumi.get(self, "tier")

    @property
    @pulumi.getter(name="timeShiftConfiguration")
    def time_shift_configuration(self) -> pulumi.Output[Optional['outputs.ChannelTimeShiftConfiguration']]:
        """
        The configuration for time-shifted viewing.
        """
        return pulumi.get(self, "time_shift_configuration")

