"""EndpointManagementService Types and Enums."""

# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code

# Autogenerated
# DO NOT MODIFY

from dataclasses import dataclass, field

from enum import Enum

from typing import Any, Dict, List, Optional, Tuple, Union

from dataclasses_json import config, dataclass_json


from taegis_sdk_python._consts import TaegisEnum
from taegis_sdk_python.utils import encode_enum, decode_enum, parse_union_result


class EndpointPlatform(str, Enum):
    """EndpointPlatform."""

    WINDOWS = "WINDOWS"
    MAC = "MAC"
    LINUX = "LINUX"


class PolicyType(str, Enum):
    """PolicyType."""

    LOW = "LOW"
    STANDARD = "STANDARD"
    HIGH = "HIGH"
    LOW_COMPAT = "LOW_COMPAT"
    STANDARD_COMPAT = "STANDARD_COMPAT"


class BulkAssignRequestStatus(str, Enum):
    """BulkAssignRequestStatus."""

    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    COMPLETE = "COMPLETE"


class NGAVProtectionMode(str, Enum):
    """NGAVProtectionMode."""

    DETECT = "DETECT"
    PROTECT = "PROTECT"


class ShellcodeOption(str, Enum):
    """ShellcodeOption."""

    DISABLED = "Disabled"
    REPORT_ONLY = "ReportOnly"
    BLOCK_MEMORY_BASED = "BlockMemoryBased"
    BLOCK_ALL = "BlockAll"


class AgentSettingsProfile(str, Enum):
    """AgentSettingsProfile."""

    DEFAULT = "DEFAULT"
    EARLY_ACCESS = "EARLY_ACCESS"


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class DeleteEndpointGrpInput:
    """DeleteEndpointGrpInput."""

    group_id: Optional[str] = field(default=None, metadata=config(field_name="groupId"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Policy:
    """Policy."""

    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    platform: Optional[str] = field(
        default=None, metadata=config(field_name="platform")
    )
    format: Optional[str] = field(default=None, metadata=config(field_name="format"))
    value: Optional[str] = field(default=None, metadata=config(field_name="value"))
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EndpointGroupArguments:
    """EndpointGroupArguments."""

    group_id: Optional[str] = field(default=None, metadata=config(field_name="groupId"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class BulkAssignRequestInput:
    """BulkAssignRequestInput."""

    group_id: Optional[str] = field(default=None, metadata=config(field_name="groupId"))
    endpoint_ids: Optional[List[str]] = field(
        default=None, metadata=config(field_name="endpointIds")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class PartialPageInfo:
    """PartialPageInfo."""

    last_evaluated_key: Optional[str] = field(
        default=None, metadata=config(field_name="lastEvaluatedKey")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AutoArchive:
    """AutoArchive."""

    enabled: Optional[bool] = field(default=None, metadata=config(field_name="enabled"))
    period_days: Optional[int] = field(
        default=None, metadata=config(field_name="periodDays")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class PolicyOverride:
    """PolicyOverride."""

    format: Optional[str] = field(default=None, metadata=config(field_name="format"))
    value: Optional[str] = field(default=None, metadata=config(field_name="value"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class DailyWindowEntry:
    """DailyWindowEntry."""

    enabled: Optional[bool] = field(default=None, metadata=config(field_name="enabled"))
    start_time_hour: Optional[int] = field(
        default=None, metadata=config(field_name="startTimeHour")
    )
    end_time_hour: Optional[int] = field(
        default=None, metadata=config(field_name="endTimeHour")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ToggleSetting:
    """ToggleSetting."""

    enabled: Optional[bool] = field(default=None, metadata=config(field_name="enabled"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EnumValue:
    """EnumValue."""

    value: Optional[int] = field(default=None, metadata=config(field_name="value"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class BooleanSettingInput:
    """BooleanSettingInput."""

    enabled: Optional[bool] = field(default=None, metadata=config(field_name="enabled"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AutoArchiveInput:
    """AutoArchiveInput."""

    enabled: Optional[bool] = field(default=None, metadata=config(field_name="enabled"))
    period_days: Optional[float] = field(
        default=None, metadata=config(field_name="periodDays")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class DailyWindowEntryInput:
    """DailyWindowEntryInput."""

    enabled: Optional[bool] = field(default=None, metadata=config(field_name="enabled"))
    start_time_hour: Optional[int] = field(
        default=None, metadata=config(field_name="startTimeHour")
    )
    end_time_hour: Optional[int] = field(
        default=None, metadata=config(field_name="endTimeHour")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ExperimentalSettingsInput:
    """ExperimentalSettingsInput."""

    value: Optional[Any] = field(default=None, metadata=config(field_name="value"))
    path: Optional[str] = field(default=None, metadata=config(field_name="path"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class UpdatePolicyOverrideInput:
    """UpdatePolicyOverrideInput."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    format: Optional[str] = field(default=None, metadata=config(field_name="format"))
    value: Optional[str] = field(default=None, metadata=config(field_name="value"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class CreateEndpointGroupInput:
    """CreateEndpointGroupInput."""

    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    desired_agent_version: Optional[str] = field(
        default=None, metadata=config(field_name="desiredAgentVersion")
    )
    is_default: Optional[bool] = field(
        default=None, metadata=config(field_name="isDefault")
    )
    channel: Optional[str] = field(default=None, metadata=config(field_name="channel"))
    archive_endpoint_after_days: Optional[int] = field(
        default=None,
        metadata=config(
            metadata={
                "deprecated": True,
                "deprecation_reason": "Moved to agent setting",
            },
            field_name="ArchiveEndpointAfterDays",
        ),
    )
    file_analysis_flag: Optional[bool] = field(
        default=None,
        metadata=config(
            metadata={
                "deprecated": True,
                "deprecation_reason": "Moved to agent setting",
            },
            field_name="fileAnalysisFlag",
        ),
    )
    maintenance_window: Optional[str] = field(
        default=None,
        metadata=config(
            metadata={
                "deprecated": True,
                "deprecation_reason": "Moved to agent setting",
            },
            field_name="maintenanceWindow",
        ),
    )
    advanced_kernel_telemetry_enabled: Optional[bool] = field(
        default=None,
        metadata=config(
            metadata={
                "deprecated": True,
                "deprecation_reason": "Moved to agent setting",
            },
            field_name="advancedKernelTelemetryEnabled",
        ),
    )
    setting_id: Optional[str] = field(
        default=None, metadata=config(field_name="settingId")
    )
    policy_name: Optional[Union[PolicyType, TaegisEnum]] = field(
        default=None,
        metadata=config(
            metadata={
                "deprecated": True,
                "deprecation_reason": "Moved to agent setting",
            },
            encoder=encode_enum,
            decoder=lambda x: decode_enum(PolicyType, x),
            field_name="policyName",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class UpdateEndpointGroupInput:
    """UpdateEndpointGroupInput."""

    group_id: Optional[str] = field(default=None, metadata=config(field_name="groupId"))
    setting_id: Optional[str] = field(
        default=None, metadata=config(field_name="settingId")
    )
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    desired_version: Optional[str] = field(
        default=None, metadata=config(field_name="desiredVersion")
    )
    channel: Optional[str] = field(default=None, metadata=config(field_name="channel"))
    archive_endpoint_after_days: Optional[int] = field(
        default=None,
        metadata=config(
            metadata={
                "deprecated": True,
                "deprecation_reason": "Moved to agent setting",
            },
            field_name="ArchiveEndpointAfterDays",
        ),
    )
    file_analysis_flag: Optional[bool] = field(
        default=None,
        metadata=config(
            metadata={
                "deprecated": True,
                "deprecation_reason": "Moved to agent setting",
            },
            field_name="fileAnalysisFlag",
        ),
    )
    maintenance_window: Optional[str] = field(
        default=None,
        metadata=config(
            metadata={
                "deprecated": True,
                "deprecation_reason": "Moved to agent setting",
            },
            field_name="maintenanceWindow",
        ),
    )
    advanced_kernel_telemetry_enabled: Optional[bool] = field(
        default=None,
        metadata=config(
            metadata={
                "deprecated": True,
                "deprecation_reason": "Moved to agent setting",
            },
            field_name="advancedKernelTelemetryEnabled",
        ),
    )
    policy_name: Optional[Union[PolicyType, TaegisEnum]] = field(
        default=None,
        metadata=config(
            metadata={
                "deprecated": True,
                "deprecation_reason": "Moved to agent setting",
            },
            encoder=encode_enum,
            decoder=lambda x: decode_enum(PolicyType, x),
            field_name="policyName",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class BulkAssignRequestOutput:
    """BulkAssignRequestOutput."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    status: Optional[Union[BulkAssignRequestStatus, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(BulkAssignRequestStatus, x),
            field_name="status",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class NGAV:
    """NGAV."""

    enabled: Optional[bool] = field(default=None, metadata=config(field_name="enabled"))
    selected_mode: Optional[Union[NGAVProtectionMode, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(NGAVProtectionMode, x),
            field_name="selectedMode",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AdvancedKernelTelemetry:
    """AdvancedKernelTelemetry."""

    enabled: Optional[bool] = field(default=None, metadata=config(field_name="enabled"))
    shellcode_option: Optional[Union[ShellcodeOption, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(ShellcodeOption, x),
            field_name="shellcodeOption",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class NGAVInput:
    """NGAVInput."""

    enabled: Optional[bool] = field(default=None, metadata=config(field_name="enabled"))
    protection_mode: Optional[Union[NGAVProtectionMode, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(NGAVProtectionMode, x),
            field_name="protectionMode",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AdvancedKernelTelemetryInput:
    """AdvancedKernelTelemetryInput."""

    enabled: Optional[bool] = field(default=None, metadata=config(field_name="enabled"))
    shellcode_option: Optional[Union[ShellcodeOption, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(ShellcodeOption, x),
            field_name="shellcodeOption",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ToggleSettingDefaults:
    """ToggleSettingDefaults."""

    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    enabled: Optional[bool] = field(default=None, metadata=config(field_name="enabled"))
    platforms: Optional[List[Union[EndpointPlatform, TaegisEnum]]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(EndpointPlatform, x),
            field_name="platforms",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AutoArchiveDefaults:
    """AutoArchiveDefaults."""

    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    enabled: Optional[bool] = field(default=None, metadata=config(field_name="enabled"))
    period_days: Optional[int] = field(
        default=None, metadata=config(field_name="periodDays")
    )
    platforms: Optional[List[Union[EndpointPlatform, TaegisEnum]]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(EndpointPlatform, x),
            field_name="platforms",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class PolicyArguments:
    """PolicyArguments."""

    policy_name: Optional[Union[PolicyType, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(PolicyType, x),
            field_name="policyName",
        ),
    )
    platform: Optional[Union[EndpointPlatform, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(EndpointPlatform, x),
            field_name="platform",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class CreatePolicyInput:
    """CreatePolicyInput."""

    format: Optional[str] = field(default=None, metadata=config(field_name="format"))
    value: Optional[str] = field(default=None, metadata=config(field_name="value"))
    policy_name: Optional[Union[PolicyType, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(PolicyType, x),
            field_name="policyName",
        ),
    )
    platform: Optional[Union[EndpointPlatform, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(EndpointPlatform, x),
            field_name="platform",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ExperimentalSetting:
    """ExperimentalSetting."""

    path: Optional[str] = field(default=None, metadata=config(field_name="path"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    module_name: Optional[str] = field(
        default=None, metadata=config(field_name="moduleName")
    )
    field_type: Optional[str] = field(
        default=None, metadata=config(field_name="fieldType")
    )
    range: Optional[List[int]] = field(
        default=None, metadata=config(field_name="range")
    )
    value: Optional[Any] = field(default=None, metadata=config(field_name="value"))
    platforms: Optional[List[Union[EndpointPlatform, TaegisEnum]]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(EndpointPlatform, x),
            field_name="platforms",
        ),
    )
    enum_values: Optional[List[EnumValue]] = field(
        default=None, metadata=config(field_name="enumValues")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AdvancedKernelTelemetryDefaults:
    """AdvancedKernelTelemetryDefaults."""

    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    enabled: Optional[bool] = field(default=None, metadata=config(field_name="enabled"))
    platforms: Optional[List[Union[EndpointPlatform, TaegisEnum]]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(EndpointPlatform, x),
            field_name="platforms",
        ),
    )
    shellcode_options: Optional[List[EnumValue]] = field(
        default=None, metadata=config(field_name="shellcodeOptions")
    )
    selected_shellcode_option: Optional[Union[ShellcodeOption, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(ShellcodeOption, x),
            field_name="selectedShellcodeOption",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class NGAVDefaults:
    """NGAVDefaults."""

    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    enabled: Optional[bool] = field(default=None, metadata=config(field_name="enabled"))
    platforms: Optional[List[Union[EndpointPlatform, TaegisEnum]]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(EndpointPlatform, x),
            field_name="platforms",
        ),
    )
    modes: Optional[List[EnumValue]] = field(
        default=None, metadata=config(field_name="modes")
    )
    selected_mode: Optional[Union[NGAVProtectionMode, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(NGAVProtectionMode, x),
            field_name="selectedMode",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class DailyWindows:
    """DailyWindows."""

    monday: Optional[DailyWindowEntry] = field(
        default=None, metadata=config(field_name="monday")
    )
    tuesday: Optional[DailyWindowEntry] = field(
        default=None, metadata=config(field_name="tuesday")
    )
    wednesday: Optional[DailyWindowEntry] = field(
        default=None, metadata=config(field_name="wednesday")
    )
    thursday: Optional[DailyWindowEntry] = field(
        default=None, metadata=config(field_name="thursday")
    )
    friday: Optional[DailyWindowEntry] = field(
        default=None, metadata=config(field_name="friday")
    )
    saturday: Optional[DailyWindowEntry] = field(
        default=None, metadata=config(field_name="saturday")
    )
    sunday: Optional[DailyWindowEntry] = field(
        default=None, metadata=config(field_name="sunday")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class DailyWindowsInput:
    """DailyWindowsInput."""

    monday: Optional[DailyWindowEntryInput] = field(
        default=None, metadata=config(field_name="monday")
    )
    tuesday: Optional[DailyWindowEntryInput] = field(
        default=None, metadata=config(field_name="tuesday")
    )
    wednesday: Optional[DailyWindowEntryInput] = field(
        default=None, metadata=config(field_name="wednesday")
    )
    thursday: Optional[DailyWindowEntryInput] = field(
        default=None, metadata=config(field_name="thursday")
    )
    friday: Optional[DailyWindowEntryInput] = field(
        default=None, metadata=config(field_name="friday")
    )
    saturday: Optional[DailyWindowEntryInput] = field(
        default=None, metadata=config(field_name="saturday")
    )
    sunday: Optional[DailyWindowEntryInput] = field(
        default=None, metadata=config(field_name="sunday")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class MaintenanceWindow:
    """MaintenanceWindow."""

    enabled: Optional[bool] = field(default=None, metadata=config(field_name="enabled"))
    windows: Optional[DailyWindows] = field(
        default=None, metadata=config(field_name="windows")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class MaintenanceWindowInput:
    """MaintenanceWindowInput."""

    enabled: Optional[bool] = field(default=None, metadata=config(field_name="enabled"))
    windows: Optional[DailyWindowsInput] = field(
        default=None, metadata=config(field_name="windows")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class MaintenanceWindowDefaults:
    """MaintenanceWindowDefaults."""

    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    enabled: Optional[bool] = field(default=None, metadata=config(field_name="enabled"))
    platforms: Optional[List[Union[EndpointPlatform, TaegisEnum]]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(EndpointPlatform, x),
            field_name="platforms",
        ),
    )
    windows: Optional[DailyWindows] = field(
        default=None, metadata=config(field_name="windows")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class UpdateAgentSettingsInput:
    """UpdateAgentSettingsInput."""

    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    channel: Optional[str] = field(default=None, metadata=config(field_name="channel"))
    advanced_kernel_telemetry: Optional[AdvancedKernelTelemetryInput] = field(
        default=None, metadata=config(field_name="advancedKernelTelemetry")
    )
    auto_archive: Optional[AutoArchiveInput] = field(
        default=None, metadata=config(field_name="autoArchive")
    )
    file_analysis: Optional[BooleanSettingInput] = field(
        default=None, metadata=config(field_name="fileAnalysis")
    )
    tamper_protection: Optional[BooleanSettingInput] = field(
        default=None, metadata=config(field_name="tamperProtection")
    )
    ngav: Optional[NGAVInput] = field(default=None, metadata=config(field_name="ngav"))
    policy_type: Optional[Union[PolicyType, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(PolicyType, x),
            field_name="policyType",
        ),
    )
    maintenance_window: Optional[MaintenanceWindowInput] = field(
        default=None, metadata=config(field_name="maintenanceWindow")
    )
    experimental_settings: Optional[List[ExperimentalSettingsInput]] = field(
        default=None, metadata=config(field_name="experimentalSettings")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AgentSettingsInput:
    """AgentSettingsInput."""

    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    channel: Optional[str] = field(default=None, metadata=config(field_name="channel"))
    profile_name: Optional[Union[AgentSettingsProfile, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(AgentSettingsProfile, x),
            field_name="profileName",
        ),
    )
    advanced_kernel_telemetry: Optional[AdvancedKernelTelemetryInput] = field(
        default=None, metadata=config(field_name="advancedKernelTelemetry")
    )
    auto_archive: Optional[AutoArchiveInput] = field(
        default=None, metadata=config(field_name="autoArchive")
    )
    file_analysis: Optional[BooleanSettingInput] = field(
        default=None, metadata=config(field_name="fileAnalysis")
    )
    tamper_protection: Optional[BooleanSettingInput] = field(
        default=None, metadata=config(field_name="tamperProtection")
    )
    ngav: Optional[NGAVInput] = field(default=None, metadata=config(field_name="ngav"))
    policy_type: Optional[Union[PolicyType, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(PolicyType, x),
            field_name="policyType",
        ),
    )
    maintenance_window: Optional[MaintenanceWindowInput] = field(
        default=None, metadata=config(field_name="maintenanceWindow")
    )
    experimental_settings: Optional[List[ExperimentalSettingsInput]] = field(
        default=None, metadata=config(field_name="experimentalSettings")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AgentSettingsDefaults:
    """AgentSettingsDefaults."""

    channel: Optional[str] = field(default=None, metadata=config(field_name="channel"))
    profile_name: Optional[Union[AgentSettingsProfile, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(AgentSettingsProfile, x),
            field_name="profileName",
        ),
    )
    advanced_kernel_telemetry: Optional[AdvancedKernelTelemetryDefaults] = field(
        default=None, metadata=config(field_name="advancedKernelTelemetry")
    )
    auto_archive: Optional[AutoArchiveDefaults] = field(
        default=None, metadata=config(field_name="autoArchive")
    )
    file_analysis: Optional[ToggleSettingDefaults] = field(
        default=None, metadata=config(field_name="fileAnalysis")
    )
    maintenance_window: Optional[MaintenanceWindowDefaults] = field(
        default=None, metadata=config(field_name="maintenanceWindow")
    )
    tamper_protection: Optional[ToggleSettingDefaults] = field(
        default=None, metadata=config(field_name="tamperProtection")
    )
    policy_type: Optional[Union[PolicyType, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(PolicyType, x),
            field_name="policyType",
        ),
    )
    ngav: Optional[NGAVDefaults] = field(
        default=None, metadata=config(field_name="ngav")
    )
    experimental_settings: Optional[List[ExperimentalSetting]] = field(
        default=None, metadata=config(field_name="experimentalSettings")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AgentSetting:
    """AgentSetting."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    channel: Optional[str] = field(default=None, metadata=config(field_name="channel"))
    is_default: Optional[bool] = field(
        default=None, metadata=config(field_name="isDefault")
    )
    skip_upgrade: Optional[bool] = field(
        default=None, metadata=config(field_name="skipUpgrade")
    )
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    profile_name: Optional[Union[AgentSettingsProfile, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(AgentSettingsProfile, x),
            field_name="profileName",
        ),
    )
    advanced_kernel_telemetry: Optional[AdvancedKernelTelemetry] = field(
        default=None, metadata=config(field_name="advancedKernelTelemetry")
    )
    auto_archive: Optional[AutoArchive] = field(
        default=None, metadata=config(field_name="autoArchive")
    )
    file_analysis: Optional[ToggleSetting] = field(
        default=None, metadata=config(field_name="fileAnalysis")
    )
    maintenance_window: Optional[MaintenanceWindow] = field(
        default=None, metadata=config(field_name="maintenanceWindow")
    )
    tamper_protection: Optional[ToggleSetting] = field(
        default=None, metadata=config(field_name="tamperProtection")
    )
    policy_type: Optional[Union[PolicyType, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(PolicyType, x),
            field_name="policyType",
        ),
    )
    policy_override: Optional[PolicyOverride] = field(
        default=None, metadata=config(field_name="policyOverride")
    )
    ngav: Optional[NGAV] = field(default=None, metadata=config(field_name="ngav"))
    experimental_settings: Optional[List[ExperimentalSetting]] = field(
        default=None, metadata=config(field_name="experimentalSettings")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EndpointGroup:
    """EndpointGroup."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenantId")
    )
    group_id: Optional[str] = field(default=None, metadata=config(field_name="groupId"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    registration_key: Optional[str] = field(
        default=None, metadata=config(field_name="registrationKey")
    )
    registration_key_expires_at: Optional[str] = field(
        default=None, metadata=config(field_name="registrationKeyExpiresAt")
    )
    policy_name: Optional[str] = field(
        default=None,
        metadata=config(
            metadata={
                "deprecated": True,
                "deprecation_reason": "Moved to agent setting",
            },
            field_name="policyName",
        ),
    )
    is_system_generated: Optional[bool] = field(
        default=None, metadata=config(field_name="isSystemGenerated")
    )
    is_default: Optional[bool] = field(
        default=None, metadata=config(field_name="isDefault")
    )
    desired_agent_version: Optional[str] = field(
        default=None, metadata=config(field_name="desiredAgentVersion")
    )
    channel: Optional[str] = field(default=None, metadata=config(field_name="channel"))
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    skip_upgrade: Optional[bool] = field(
        default=None, metadata=config(field_name="skipUpgrade")
    )
    archive_endpoint_after_days: Optional[int] = field(
        default=None,
        metadata=config(
            metadata={
                "deprecated": True,
                "deprecation_reason": "Moved to agent setting",
            },
            field_name="ArchiveEndpointAfterDays",
        ),
    )
    is_archive_endpoint_enabled: Optional[bool] = field(
        default=None,
        metadata=config(
            metadata={
                "deprecated": True,
                "deprecation_reason": "Moved to agent setting",
            },
            field_name="IsArchiveEndpointEnabled",
        ),
    )
    file_analysis_flag: Optional[bool] = field(
        default=None,
        metadata=config(
            metadata={
                "deprecated": True,
                "deprecation_reason": "Moved to agent setting",
            },
            field_name="fileAnalysisFlag",
        ),
    )
    maintenance_window: Optional[str] = field(
        default=None,
        metadata=config(
            metadata={
                "deprecated": True,
                "deprecation_reason": "Moved to agent setting",
            },
            field_name="maintenanceWindow",
        ),
    )
    advanced_kernel_telemetry_enabled: Optional[bool] = field(
        default=None,
        metadata=config(
            metadata={
                "deprecated": True,
                "deprecation_reason": "Moved to agent setting",
            },
            field_name="advancedKernelTelemetryEnabled",
        ),
    )
    setting_id: Optional[str] = field(
        default=None, metadata=config(field_name="settingId")
    )
    agent_setting: Optional[AgentSetting] = field(
        default=None, metadata=config(field_name="agentSetting")
    )
    policy_override: Optional[PolicyOverride] = field(
        default=None,
        metadata=config(
            metadata={
                "deprecated": True,
                "deprecation_reason": "Moved to agent setting",
            },
            field_name="policyOverride",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EndpointGroupsPagedOutput:
    """EndpointGroupsPagedOutput."""

    groups: Optional[List[EndpointGroup]] = field(
        default=None, metadata=config(field_name="groups")
    )
    partial_page_info: Optional[PartialPageInfo] = field(
        default=None, metadata=config(field_name="partialPageInfo")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AgentSettings:
    """AgentSettings."""

    total_count: Optional[int] = field(
        default=None, metadata=config(field_name="totalCount")
    )
    settings: Optional[List[AgentSetting]] = field(
        default=None, metadata=config(field_name="settings")
    )
    page_info: Optional[PartialPageInfo] = field(
        default=None, metadata=config(field_name="pageInfo")
    )
