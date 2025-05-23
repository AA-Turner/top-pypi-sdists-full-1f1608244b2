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
from ._enums import *

__all__ = [
    'WorkspacesPoolApplicationSettingsArgs',
    'WorkspacesPoolApplicationSettingsArgsDict',
    'WorkspacesPoolCapacityArgs',
    'WorkspacesPoolCapacityArgsDict',
    'WorkspacesPoolTimeoutSettingsArgs',
    'WorkspacesPoolTimeoutSettingsArgsDict',
]

MYPY = False

if not MYPY:
    class WorkspacesPoolApplicationSettingsArgsDict(TypedDict):
        status: pulumi.Input['WorkspacesPoolApplicationSettingsStatus']
        """
        Enables or disables persistent application settings for users during their pool sessions.
        """
        settings_group: NotRequired[pulumi.Input[builtins.str]]
        """
        The path prefix for the S3 bucket where users’ persistent application settings are stored.
        """
elif False:
    WorkspacesPoolApplicationSettingsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class WorkspacesPoolApplicationSettingsArgs:
    def __init__(__self__, *,
                 status: pulumi.Input['WorkspacesPoolApplicationSettingsStatus'],
                 settings_group: Optional[pulumi.Input[builtins.str]] = None):
        """
        :param pulumi.Input['WorkspacesPoolApplicationSettingsStatus'] status: Enables or disables persistent application settings for users during their pool sessions.
        :param pulumi.Input[builtins.str] settings_group: The path prefix for the S3 bucket where users’ persistent application settings are stored.
        """
        pulumi.set(__self__, "status", status)
        if settings_group is not None:
            pulumi.set(__self__, "settings_group", settings_group)

    @property
    @pulumi.getter
    def status(self) -> pulumi.Input['WorkspacesPoolApplicationSettingsStatus']:
        """
        Enables or disables persistent application settings for users during their pool sessions.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: pulumi.Input['WorkspacesPoolApplicationSettingsStatus']):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="settingsGroup")
    def settings_group(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The path prefix for the S3 bucket where users’ persistent application settings are stored.
        """
        return pulumi.get(self, "settings_group")

    @settings_group.setter
    def settings_group(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "settings_group", value)


if not MYPY:
    class WorkspacesPoolCapacityArgsDict(TypedDict):
        desired_user_sessions: pulumi.Input[builtins.int]
        """
        The desired number of user sessions for the WorkSpaces in the pool.
        """
elif False:
    WorkspacesPoolCapacityArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class WorkspacesPoolCapacityArgs:
    def __init__(__self__, *,
                 desired_user_sessions: pulumi.Input[builtins.int]):
        """
        :param pulumi.Input[builtins.int] desired_user_sessions: The desired number of user sessions for the WorkSpaces in the pool.
        """
        pulumi.set(__self__, "desired_user_sessions", desired_user_sessions)

    @property
    @pulumi.getter(name="desiredUserSessions")
    def desired_user_sessions(self) -> pulumi.Input[builtins.int]:
        """
        The desired number of user sessions for the WorkSpaces in the pool.
        """
        return pulumi.get(self, "desired_user_sessions")

    @desired_user_sessions.setter
    def desired_user_sessions(self, value: pulumi.Input[builtins.int]):
        pulumi.set(self, "desired_user_sessions", value)


if not MYPY:
    class WorkspacesPoolTimeoutSettingsArgsDict(TypedDict):
        disconnect_timeout_in_seconds: NotRequired[pulumi.Input[builtins.int]]
        """
        Specifies the amount of time, in seconds, that a streaming session remains active after users disconnect. If users try to reconnect to the streaming session after a disconnection or network interruption within the time set, they are connected to their previous session. Otherwise, they are connected to a new session with a new streaming instance.
        """
        idle_disconnect_timeout_in_seconds: NotRequired[pulumi.Input[builtins.int]]
        """
        The amount of time in seconds a connection will stay active while idle.
        """
        max_user_duration_in_seconds: NotRequired[pulumi.Input[builtins.int]]
        """
        Specifies the maximum amount of time, in seconds, that a streaming session can remain active. If users are still connected to a streaming instance five minutes before this limit is reached, they are prompted to save any open documents before being disconnected. After this time elapses, the instance is terminated and replaced by a new instance.
        """
elif False:
    WorkspacesPoolTimeoutSettingsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class WorkspacesPoolTimeoutSettingsArgs:
    def __init__(__self__, *,
                 disconnect_timeout_in_seconds: Optional[pulumi.Input[builtins.int]] = None,
                 idle_disconnect_timeout_in_seconds: Optional[pulumi.Input[builtins.int]] = None,
                 max_user_duration_in_seconds: Optional[pulumi.Input[builtins.int]] = None):
        """
        :param pulumi.Input[builtins.int] disconnect_timeout_in_seconds: Specifies the amount of time, in seconds, that a streaming session remains active after users disconnect. If users try to reconnect to the streaming session after a disconnection or network interruption within the time set, they are connected to their previous session. Otherwise, they are connected to a new session with a new streaming instance.
        :param pulumi.Input[builtins.int] idle_disconnect_timeout_in_seconds: The amount of time in seconds a connection will stay active while idle.
        :param pulumi.Input[builtins.int] max_user_duration_in_seconds: Specifies the maximum amount of time, in seconds, that a streaming session can remain active. If users are still connected to a streaming instance five minutes before this limit is reached, they are prompted to save any open documents before being disconnected. After this time elapses, the instance is terminated and replaced by a new instance.
        """
        if disconnect_timeout_in_seconds is not None:
            pulumi.set(__self__, "disconnect_timeout_in_seconds", disconnect_timeout_in_seconds)
        if idle_disconnect_timeout_in_seconds is not None:
            pulumi.set(__self__, "idle_disconnect_timeout_in_seconds", idle_disconnect_timeout_in_seconds)
        if max_user_duration_in_seconds is not None:
            pulumi.set(__self__, "max_user_duration_in_seconds", max_user_duration_in_seconds)

    @property
    @pulumi.getter(name="disconnectTimeoutInSeconds")
    def disconnect_timeout_in_seconds(self) -> Optional[pulumi.Input[builtins.int]]:
        """
        Specifies the amount of time, in seconds, that a streaming session remains active after users disconnect. If users try to reconnect to the streaming session after a disconnection or network interruption within the time set, they are connected to their previous session. Otherwise, they are connected to a new session with a new streaming instance.
        """
        return pulumi.get(self, "disconnect_timeout_in_seconds")

    @disconnect_timeout_in_seconds.setter
    def disconnect_timeout_in_seconds(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "disconnect_timeout_in_seconds", value)

    @property
    @pulumi.getter(name="idleDisconnectTimeoutInSeconds")
    def idle_disconnect_timeout_in_seconds(self) -> Optional[pulumi.Input[builtins.int]]:
        """
        The amount of time in seconds a connection will stay active while idle.
        """
        return pulumi.get(self, "idle_disconnect_timeout_in_seconds")

    @idle_disconnect_timeout_in_seconds.setter
    def idle_disconnect_timeout_in_seconds(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "idle_disconnect_timeout_in_seconds", value)

    @property
    @pulumi.getter(name="maxUserDurationInSeconds")
    def max_user_duration_in_seconds(self) -> Optional[pulumi.Input[builtins.int]]:
        """
        Specifies the maximum amount of time, in seconds, that a streaming session can remain active. If users are still connected to a streaming instance five minutes before this limit is reached, they are prompted to save any open documents before being disconnected. After this time elapses, the instance is terminated and replaced by a new instance.
        """
        return pulumi.get(self, "max_user_duration_in_seconds")

    @max_user_duration_in_seconds.setter
    def max_user_duration_in_seconds(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "max_user_duration_in_seconds", value)


