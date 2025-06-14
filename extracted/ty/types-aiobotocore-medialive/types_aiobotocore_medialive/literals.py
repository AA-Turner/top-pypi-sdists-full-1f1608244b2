"""
Type annotations for medialive service literal definitions.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/literals/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from types_aiobotocore_medialive.literals import AacCodingModeType

    data: AacCodingModeType = "AD_RECEIVER_MIX"
    ```
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AacCodingModeType",
    "AacInputTypeType",
    "AacProfileType",
    "AacRateControlModeType",
    "AacRawFormatType",
    "AacSpecType",
    "AacVbrQualityType",
    "Ac3AttenuationControlType",
    "Ac3BitstreamModeType",
    "Ac3CodingModeType",
    "Ac3DrcProfileType",
    "Ac3LfeFilterType",
    "Ac3MetadataControlType",
    "AcceptHeaderType",
    "AccessibilityTypeType",
    "AfdSignalingType",
    "AlgorithmType",
    "AudioDescriptionAudioTypeControlType",
    "AudioDescriptionLanguageCodeControlType",
    "AudioLanguageSelectionPolicyType",
    "AudioNormalizationAlgorithmControlType",
    "AudioNormalizationAlgorithmType",
    "AudioOnlyHlsSegmentTypeType",
    "AudioOnlyHlsTrackTypeType",
    "AudioTypeType",
    "AuthenticationSchemeType",
    "Av1GopSizeUnitsType",
    "Av1LevelType",
    "Av1LookAheadRateControlType",
    "Av1RateControlModeType",
    "Av1SceneChangeDetectType",
    "AvailBlankingStateType",
    "BandwidthReductionFilterStrengthType",
    "BandwidthReductionPostFilterSharpeningType",
    "BlackoutSlateNetworkEndBlackoutType",
    "BlackoutSlateStateType",
    "BurnInAlignmentType",
    "BurnInBackgroundColorType",
    "BurnInFontColorType",
    "BurnInOutlineColorType",
    "BurnInShadowColorType",
    "BurnInTeletextGridControlType",
    "CdiInputResolutionType",
    "ChannelClassType",
    "ChannelCreatedWaiterName",
    "ChannelDeletedWaiterName",
    "ChannelPipelineIdToRestartType",
    "ChannelPlacementGroupAssignedWaiterName",
    "ChannelPlacementGroupDeletedWaiterName",
    "ChannelPlacementGroupStateType",
    "ChannelPlacementGroupUnassignedWaiterName",
    "ChannelRunningWaiterName",
    "ChannelStateType",
    "ChannelStoppedWaiterName",
    "CloudWatchAlarmTemplateComparisonOperatorType",
    "CloudWatchAlarmTemplateStatisticType",
    "CloudWatchAlarmTemplateTargetResourceTypeType",
    "CloudWatchAlarmTemplateTreatMissingDataType",
    "ClusterCreatedWaiterName",
    "ClusterDeletedWaiterName",
    "ClusterStateType",
    "ClusterTypeType",
    "CmafId3BehaviorType",
    "CmafIngestSegmentLengthUnitsType",
    "CmafKLVBehaviorType",
    "CmafNielsenId3BehaviorType",
    "CmafTimedMetadataId3FrameType",
    "CmafTimedMetadataPassthroughType",
    "ColorSpaceType",
    "ContentTypeType",
    "DashRoleAudioType",
    "DashRoleCaptionType",
    "DescribeSchedulePaginatorName",
    "DeviceSettingsSyncStateType",
    "DeviceUpdateStatusType",
    "DolbyEProgramSelectionType",
    "DvbDashAccessibilityType",
    "DvbSdtOutputSdtType",
    "DvbSubDestinationAlignmentType",
    "DvbSubDestinationBackgroundColorType",
    "DvbSubDestinationFontColorType",
    "DvbSubDestinationOutlineColorType",
    "DvbSubDestinationShadowColorType",
    "DvbSubDestinationTeletextGridControlType",
    "DvbSubOcrLanguageType",
    "Eac3AtmosCodingModeType",
    "Eac3AtmosDrcLineType",
    "Eac3AtmosDrcRfType",
    "Eac3AttenuationControlType",
    "Eac3BitstreamModeType",
    "Eac3CodingModeType",
    "Eac3DcFilterType",
    "Eac3DrcLineType",
    "Eac3DrcRfType",
    "Eac3LfeControlType",
    "Eac3LfeFilterType",
    "Eac3MetadataControlType",
    "Eac3PassthroughControlType",
    "Eac3PhaseControlType",
    "Eac3StereoDownmixType",
    "Eac3SurroundExModeType",
    "Eac3SurroundModeType",
    "EbuTtDDestinationStyleControlType",
    "EbuTtDFillLineGapControlType",
    "EmbeddedConvert608To708Type",
    "EmbeddedScte20DetectionType",
    "EventBridgeRuleTemplateEventTypeType",
    "FeatureActivationsInputPrepareScheduleActionsType",
    "FeatureActivationsOutputStaticImageOverlayScheduleActionsType",
    "FecOutputIncludeFecType",
    "FixedAfdType",
    "Fmp4NielsenId3BehaviorType",
    "Fmp4TimedMetadataBehaviorType",
    "FollowPointType",
    "FrameCaptureIntervalUnitType",
    "GlobalConfigurationInputEndActionType",
    "GlobalConfigurationLowFramerateInputsType",
    "GlobalConfigurationOutputLockingModeType",
    "GlobalConfigurationOutputTimingSourceType",
    "H264AdaptiveQuantizationType",
    "H264ColorMetadataType",
    "H264EntropyEncodingType",
    "H264FlickerAqType",
    "H264ForceFieldPicturesType",
    "H264FramerateControlType",
    "H264GopBReferenceType",
    "H264GopSizeUnitsType",
    "H264LevelType",
    "H264LookAheadRateControlType",
    "H264ParControlType",
    "H264ProfileType",
    "H264QualityLevelType",
    "H264RateControlModeType",
    "H264ScanTypeType",
    "H264SceneChangeDetectType",
    "H264SpatialAqType",
    "H264SubGopLengthType",
    "H264SyntaxType",
    "H264TemporalAqType",
    "H264TimecodeInsertionBehaviorType",
    "H265AdaptiveQuantizationType",
    "H265AlternativeTransferFunctionType",
    "H265ColorMetadataType",
    "H265DeblockingType",
    "H265FlickerAqType",
    "H265GopSizeUnitsType",
    "H265LevelType",
    "H265LookAheadRateControlType",
    "H265MvOverPictureBoundariesType",
    "H265MvTemporalPredictorType",
    "H265ProfileType",
    "H265RateControlModeType",
    "H265ScanTypeType",
    "H265SceneChangeDetectType",
    "H265TierType",
    "H265TilePaddingType",
    "H265TimecodeInsertionBehaviorType",
    "H265TreeblockSizeType",
    "HlsAdMarkersType",
    "HlsAkamaiHttpTransferModeType",
    "HlsCaptionLanguageSettingType",
    "HlsClientCacheType",
    "HlsCodecSpecificationType",
    "HlsDirectoryStructureType",
    "HlsDiscontinuityTagsType",
    "HlsEncryptionTypeType",
    "HlsH265PackagingTypeType",
    "HlsId3SegmentTaggingStateType",
    "HlsIncompleteSegmentBehaviorType",
    "HlsIvInManifestType",
    "HlsIvSourceType",
    "HlsManifestCompressionType",
    "HlsManifestDurationFormatType",
    "HlsMediaStoreStorageClassType",
    "HlsModeType",
    "HlsOutputSelectionType",
    "HlsProgramDateTimeClockType",
    "HlsProgramDateTimeType",
    "HlsRedundantManifestType",
    "HlsScte35SourceTypeType",
    "HlsSegmentationModeType",
    "HlsStreamInfResolutionType",
    "HlsTimedMetadataId3FrameType",
    "HlsTsFileModeType",
    "HlsWebdavHttpTransferModeType",
    "IFrameOnlyPlaylistTypeType",
    "IncludeFillerNalUnitsType",
    "InputAttachedWaiterName",
    "InputClassType",
    "InputCodecType",
    "InputDeblockFilterType",
    "InputDeletedWaiterName",
    "InputDenoiseFilterType",
    "InputDetachedWaiterName",
    "InputDeviceActiveInputType",
    "InputDeviceCodecType",
    "InputDeviceConfigurableAudioChannelPairProfileType",
    "InputDeviceConfiguredInputType",
    "InputDeviceConnectionStateType",
    "InputDeviceIpSchemeType",
    "InputDeviceOutputTypeType",
    "InputDeviceScanTypeType",
    "InputDeviceStateType",
    "InputDeviceTransferTypeType",
    "InputDeviceTypeType",
    "InputDeviceUhdAudioChannelPairProfileType",
    "InputFilterType",
    "InputLossActionForHlsOutType",
    "InputLossActionForMsSmoothOutType",
    "InputLossActionForRtmpOutType",
    "InputLossActionForUdpOutType",
    "InputLossImageTypeType",
    "InputMaximumBitrateType",
    "InputNetworkLocationType",
    "InputPreferenceType",
    "InputResolutionType",
    "InputSecurityGroupStateType",
    "InputSourceEndBehaviorType",
    "InputSourceTypeType",
    "InputStateType",
    "InputTimecodeSourceType",
    "InputTypeType",
    "LastFrameClippingBehaviorType",
    "ListChannelPlacementGroupsPaginatorName",
    "ListChannelsPaginatorName",
    "ListCloudWatchAlarmTemplateGroupsPaginatorName",
    "ListCloudWatchAlarmTemplatesPaginatorName",
    "ListClustersPaginatorName",
    "ListEventBridgeRuleTemplateGroupsPaginatorName",
    "ListEventBridgeRuleTemplatesPaginatorName",
    "ListInputDeviceTransfersPaginatorName",
    "ListInputDevicesPaginatorName",
    "ListInputSecurityGroupsPaginatorName",
    "ListInputsPaginatorName",
    "ListMultiplexProgramsPaginatorName",
    "ListMultiplexesPaginatorName",
    "ListNetworksPaginatorName",
    "ListNodesPaginatorName",
    "ListOfferingsPaginatorName",
    "ListReservationsPaginatorName",
    "ListSdiSourcesPaginatorName",
    "ListSignalMapsPaginatorName",
    "LogLevelType",
    "M2tsAbsentInputAudioBehaviorType",
    "M2tsAribCaptionsPidControlType",
    "M2tsAribType",
    "M2tsAudioBufferModelType",
    "M2tsAudioIntervalType",
    "M2tsAudioStreamTypeType",
    "M2tsBufferModelType",
    "M2tsCcDescriptorType",
    "M2tsEbifControlType",
    "M2tsEbpPlacementType",
    "M2tsEsRateInPesType",
    "M2tsKlvType",
    "M2tsNielsenId3BehaviorType",
    "M2tsPcrControlType",
    "M2tsRateModeType",
    "M2tsScte35ControlType",
    "M2tsSegmentationMarkersType",
    "M2tsSegmentationStyleType",
    "M2tsTimedMetadataBehaviorType",
    "M3u8KlvBehaviorType",
    "M3u8NielsenId3BehaviorType",
    "M3u8PcrControlType",
    "M3u8Scte35BehaviorType",
    "M3u8TimedMetadataBehaviorType",
    "MaintenanceDayType",
    "MediaLiveServiceName",
    "MotionGraphicsInsertionType",
    "Mp2CodingModeType",
    "Mpeg2AdaptiveQuantizationType",
    "Mpeg2ColorMetadataType",
    "Mpeg2ColorSpaceType",
    "Mpeg2DisplayRatioType",
    "Mpeg2GopSizeUnitsType",
    "Mpeg2ScanTypeType",
    "Mpeg2SubGopLengthType",
    "Mpeg2TimecodeInsertionBehaviorType",
    "MsSmoothH265PackagingTypeType",
    "MultiplexCreatedWaiterName",
    "MultiplexDeletedWaiterName",
    "MultiplexRunningWaiterName",
    "MultiplexStateType",
    "MultiplexStoppedWaiterName",
    "NetworkInputServerValidationType",
    "NetworkInterfaceModeType",
    "NetworkStateType",
    "NielsenPcmToId3TaggingStateType",
    "NielsenWatermarkTimezonesType",
    "NielsenWatermarksCbetStepasideType",
    "NielsenWatermarksDistributionTypesType",
    "NodeConnectionStateType",
    "NodeDeregisteredWaiterName",
    "NodeRegisteredWaiterName",
    "NodeRoleType",
    "NodeStateType",
    "OfferingDurationUnitsType",
    "OfferingTypeType",
    "PaginatorName",
    "PipelineIdType",
    "PreferredChannelPipelineType",
    "RebootInputDeviceForceType",
    "RegionName",
    "ReservationAutomaticRenewalType",
    "ReservationCodecType",
    "ReservationMaximumBitrateType",
    "ReservationMaximumFramerateType",
    "ReservationResolutionType",
    "ReservationResourceTypeType",
    "ReservationSpecialFeatureType",
    "ReservationStateType",
    "ReservationVideoQualityType",
    "ResourceServiceName",
    "RtmpAdMarkersType",
    "RtmpCacheFullBehaviorType",
    "RtmpCaptionDataType",
    "RtmpOutputCertificateModeType",
    "S3CannedAclType",
    "Scte20Convert608To708Type",
    "Scte27OcrLanguageType",
    "Scte35AposNoRegionalBlackoutBehaviorType",
    "Scte35AposWebDeliveryAllowedBehaviorType",
    "Scte35ArchiveAllowedFlagType",
    "Scte35DeviceRestrictionsType",
    "Scte35InputModeType",
    "Scte35NoRegionalBlackoutFlagType",
    "Scte35SegmentationCancelIndicatorType",
    "Scte35SegmentationScopeType",
    "Scte35SpliceInsertNoRegionalBlackoutBehaviorType",
    "Scte35SpliceInsertWebDeliveryAllowedBehaviorType",
    "Scte35TypeType",
    "Scte35WebDeliveryAllowedFlagType",
    "SdiSourceModeType",
    "SdiSourceStateType",
    "SdiSourceTypeType",
    "ServiceName",
    "SignalMapCreatedWaiterName",
    "SignalMapMonitorDeletedWaiterName",
    "SignalMapMonitorDeployedWaiterName",
    "SignalMapMonitorDeploymentStatusType",
    "SignalMapStatusType",
    "SignalMapUpdatedWaiterName",
    "SmoothGroupAudioOnlyTimecodeControlType",
    "SmoothGroupCertificateModeType",
    "SmoothGroupEventIdModeType",
    "SmoothGroupEventStopBehaviorType",
    "SmoothGroupSegmentationModeType",
    "SmoothGroupSparseTrackTypeType",
    "SmoothGroupStreamManifestBehaviorType",
    "SmoothGroupTimestampOffsetModeType",
    "Smpte2038DataPreferenceType",
    "SrtEncryptionTypeType",
    "TemporalFilterPostFilterSharpeningType",
    "TemporalFilterStrengthType",
    "ThumbnailStateType",
    "ThumbnailTypeType",
    "TimecodeBurninFontSizeType",
    "TimecodeBurninPositionType",
    "TimecodeConfigSourceType",
    "TtmlDestinationStyleControlType",
    "UdpTimedMetadataId3FrameType",
    "UpdateNodeStateType",
    "VideoDescriptionRespondToAfdType",
    "VideoDescriptionScalingBehaviorType",
    "VideoSelectorColorSpaceType",
    "VideoSelectorColorSpaceUsageType",
    "WaiterName",
    "WavCodingModeType",
    "WebvttDestinationStyleControlType",
)


AacCodingModeType = Literal[
    "AD_RECEIVER_MIX", "CODING_MODE_1_0", "CODING_MODE_1_1", "CODING_MODE_2_0", "CODING_MODE_5_1"
]
AacInputTypeType = Literal["BROADCASTER_MIXED_AD", "NORMAL"]
AacProfileType = Literal["HEV1", "HEV2", "LC"]
AacRateControlModeType = Literal["CBR", "VBR"]
AacRawFormatType = Literal["LATM_LOAS", "NONE"]
AacSpecType = Literal["MPEG2", "MPEG4"]
AacVbrQualityType = Literal["HIGH", "LOW", "MEDIUM_HIGH", "MEDIUM_LOW"]
Ac3AttenuationControlType = Literal["ATTENUATE_3_DB", "NONE"]
Ac3BitstreamModeType = Literal[
    "COMMENTARY",
    "COMPLETE_MAIN",
    "DIALOGUE",
    "EMERGENCY",
    "HEARING_IMPAIRED",
    "MUSIC_AND_EFFECTS",
    "VISUALLY_IMPAIRED",
    "VOICE_OVER",
]
Ac3CodingModeType = Literal[
    "CODING_MODE_1_0", "CODING_MODE_1_1", "CODING_MODE_2_0", "CODING_MODE_3_2_LFE"
]
Ac3DrcProfileType = Literal["FILM_STANDARD", "NONE"]
Ac3LfeFilterType = Literal["DISABLED", "ENABLED"]
Ac3MetadataControlType = Literal["FOLLOW_INPUT", "USE_CONFIGURED"]
AcceptHeaderType = Literal["image/jpeg"]
AccessibilityTypeType = Literal[
    "DOES_NOT_IMPLEMENT_ACCESSIBILITY_FEATURES", "IMPLEMENTS_ACCESSIBILITY_FEATURES"
]
AfdSignalingType = Literal["AUTO", "FIXED", "NONE"]
AlgorithmType = Literal["AES128", "AES192", "AES256"]
AudioDescriptionAudioTypeControlType = Literal["FOLLOW_INPUT", "USE_CONFIGURED"]
AudioDescriptionLanguageCodeControlType = Literal["FOLLOW_INPUT", "USE_CONFIGURED"]
AudioLanguageSelectionPolicyType = Literal["LOOSE", "STRICT"]
AudioNormalizationAlgorithmControlType = Literal["CORRECT_AUDIO"]
AudioNormalizationAlgorithmType = Literal["ITU_1770_1", "ITU_1770_2"]
AudioOnlyHlsSegmentTypeType = Literal["AAC", "FMP4"]
AudioOnlyHlsTrackTypeType = Literal[
    "ALTERNATE_AUDIO_AUTO_SELECT",
    "ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT",
    "ALTERNATE_AUDIO_NOT_AUTO_SELECT",
    "AUDIO_ONLY_VARIANT_STREAM",
]
AudioTypeType = Literal[
    "CLEAN_EFFECTS", "HEARING_IMPAIRED", "UNDEFINED", "VISUAL_IMPAIRED_COMMENTARY"
]
AuthenticationSchemeType = Literal["AKAMAI", "COMMON"]
Av1GopSizeUnitsType = Literal["FRAMES", "SECONDS"]
Av1LevelType = Literal[
    "AV1_LEVEL_2",
    "AV1_LEVEL_2_1",
    "AV1_LEVEL_3",
    "AV1_LEVEL_3_1",
    "AV1_LEVEL_4",
    "AV1_LEVEL_4_1",
    "AV1_LEVEL_5",
    "AV1_LEVEL_5_1",
    "AV1_LEVEL_5_2",
    "AV1_LEVEL_5_3",
    "AV1_LEVEL_6",
    "AV1_LEVEL_6_1",
    "AV1_LEVEL_6_2",
    "AV1_LEVEL_6_3",
    "AV1_LEVEL_AUTO",
]
Av1LookAheadRateControlType = Literal["HIGH", "LOW", "MEDIUM"]
Av1RateControlModeType = Literal["CBR", "QVBR"]
Av1SceneChangeDetectType = Literal["DISABLED", "ENABLED"]
AvailBlankingStateType = Literal["DISABLED", "ENABLED"]
BandwidthReductionFilterStrengthType = Literal[
    "AUTO", "STRENGTH_1", "STRENGTH_2", "STRENGTH_3", "STRENGTH_4"
]
BandwidthReductionPostFilterSharpeningType = Literal[
    "DISABLED", "SHARPENING_1", "SHARPENING_2", "SHARPENING_3"
]
BlackoutSlateNetworkEndBlackoutType = Literal["DISABLED", "ENABLED"]
BlackoutSlateStateType = Literal["DISABLED", "ENABLED"]
BurnInAlignmentType = Literal["CENTERED", "LEFT", "SMART"]
BurnInBackgroundColorType = Literal["BLACK", "NONE", "WHITE"]
BurnInFontColorType = Literal["BLACK", "BLUE", "GREEN", "RED", "WHITE", "YELLOW"]
BurnInOutlineColorType = Literal["BLACK", "BLUE", "GREEN", "RED", "WHITE", "YELLOW"]
BurnInShadowColorType = Literal["BLACK", "NONE", "WHITE"]
BurnInTeletextGridControlType = Literal["FIXED", "SCALED"]
CdiInputResolutionType = Literal["FHD", "HD", "SD", "UHD"]
ChannelClassType = Literal["SINGLE_PIPELINE", "STANDARD"]
ChannelCreatedWaiterName = Literal["channel_created"]
ChannelDeletedWaiterName = Literal["channel_deleted"]
ChannelPipelineIdToRestartType = Literal["PIPELINE_0", "PIPELINE_1"]
ChannelPlacementGroupAssignedWaiterName = Literal["channel_placement_group_assigned"]
ChannelPlacementGroupDeletedWaiterName = Literal["channel_placement_group_deleted"]
ChannelPlacementGroupStateType = Literal[
    "ASSIGNED", "ASSIGNING", "DELETED", "DELETE_FAILED", "DELETING", "UNASSIGNED", "UNASSIGNING"
]
ChannelPlacementGroupUnassignedWaiterName = Literal["channel_placement_group_unassigned"]
ChannelRunningWaiterName = Literal["channel_running"]
ChannelStateType = Literal[
    "CREATE_FAILED",
    "CREATING",
    "DELETED",
    "DELETING",
    "IDLE",
    "RECOVERING",
    "RUNNING",
    "STARTING",
    "STOPPING",
    "UPDATE_FAILED",
    "UPDATING",
]
ChannelStoppedWaiterName = Literal["channel_stopped"]
CloudWatchAlarmTemplateComparisonOperatorType = Literal[
    "GreaterThanOrEqualToThreshold",
    "GreaterThanThreshold",
    "LessThanOrEqualToThreshold",
    "LessThanThreshold",
]
CloudWatchAlarmTemplateStatisticType = Literal[
    "Average", "Maximum", "Minimum", "SampleCount", "Sum"
]
CloudWatchAlarmTemplateTargetResourceTypeType = Literal[
    "CLOUDFRONT_DISTRIBUTION",
    "MEDIACONNECT_FLOW",
    "MEDIALIVE_CHANNEL",
    "MEDIALIVE_INPUT_DEVICE",
    "MEDIALIVE_MULTIPLEX",
    "MEDIAPACKAGE_CHANNEL",
    "MEDIAPACKAGE_ORIGIN_ENDPOINT",
    "MEDIATAILOR_PLAYBACK_CONFIGURATION",
    "S3_BUCKET",
]
CloudWatchAlarmTemplateTreatMissingDataType = Literal[
    "breaching", "ignore", "missing", "notBreaching"
]
ClusterCreatedWaiterName = Literal["cluster_created"]
ClusterDeletedWaiterName = Literal["cluster_deleted"]
ClusterStateType = Literal[
    "ACTIVE", "CREATE_FAILED", "CREATING", "DELETED", "DELETE_FAILED", "DELETING"
]
ClusterTypeType = Literal["ON_PREMISES"]
CmafId3BehaviorType = Literal["DISABLED", "ENABLED"]
CmafIngestSegmentLengthUnitsType = Literal["MILLISECONDS", "SECONDS"]
CmafKLVBehaviorType = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
CmafNielsenId3BehaviorType = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
CmafTimedMetadataId3FrameType = Literal["NONE", "PRIV", "TDRL"]
CmafTimedMetadataPassthroughType = Literal["DISABLED", "ENABLED"]
ColorSpaceType = Literal["HDR10", "HLG_2020", "REC_601", "REC_709"]
ContentTypeType = Literal["image/jpeg"]
DashRoleAudioType = Literal[
    "ALTERNATE",
    "COMMENTARY",
    "DESCRIPTION",
    "DUB",
    "EMERGENCY",
    "ENHANCED-AUDIO-INTELLIGIBILITY",
    "KARAOKE",
    "MAIN",
    "SUPPLEMENTARY",
]
DashRoleCaptionType = Literal[
    "ALTERNATE",
    "CAPTION",
    "COMMENTARY",
    "DESCRIPTION",
    "DUB",
    "EASYREADER",
    "EMERGENCY",
    "FORCED-SUBTITLE",
    "KARAOKE",
    "MAIN",
    "METADATA",
    "SUBTITLE",
    "SUPPLEMENTARY",
]
DescribeSchedulePaginatorName = Literal["describe_schedule"]
DeviceSettingsSyncStateType = Literal["SYNCED", "SYNCING"]
DeviceUpdateStatusType = Literal["NOT_UP_TO_DATE", "UPDATING", "UP_TO_DATE"]
DolbyEProgramSelectionType = Literal[
    "ALL_CHANNELS",
    "PROGRAM_1",
    "PROGRAM_2",
    "PROGRAM_3",
    "PROGRAM_4",
    "PROGRAM_5",
    "PROGRAM_6",
    "PROGRAM_7",
    "PROGRAM_8",
]
DvbDashAccessibilityType = Literal[
    "DVBDASH_1_VISUALLY_IMPAIRED",
    "DVBDASH_2_HARD_OF_HEARING",
    "DVBDASH_3_SUPPLEMENTAL_COMMENTARY",
    "DVBDASH_4_DIRECTORS_COMMENTARY",
    "DVBDASH_5_EDUCATIONAL_NOTES",
    "DVBDASH_6_MAIN_PROGRAM",
    "DVBDASH_7_CLEAN_FEED",
]
DvbSdtOutputSdtType = Literal["SDT_FOLLOW", "SDT_FOLLOW_IF_PRESENT", "SDT_MANUAL", "SDT_NONE"]
DvbSubDestinationAlignmentType = Literal["CENTERED", "LEFT", "SMART"]
DvbSubDestinationBackgroundColorType = Literal["BLACK", "NONE", "WHITE"]
DvbSubDestinationFontColorType = Literal["BLACK", "BLUE", "GREEN", "RED", "WHITE", "YELLOW"]
DvbSubDestinationOutlineColorType = Literal["BLACK", "BLUE", "GREEN", "RED", "WHITE", "YELLOW"]
DvbSubDestinationShadowColorType = Literal["BLACK", "NONE", "WHITE"]
DvbSubDestinationTeletextGridControlType = Literal["FIXED", "SCALED"]
DvbSubOcrLanguageType = Literal["DEU", "ENG", "FRA", "NLD", "POR", "SPA"]
Eac3AtmosCodingModeType = Literal["CODING_MODE_5_1_4", "CODING_MODE_7_1_4", "CODING_MODE_9_1_6"]
Eac3AtmosDrcLineType = Literal[
    "FILM_LIGHT", "FILM_STANDARD", "MUSIC_LIGHT", "MUSIC_STANDARD", "NONE", "SPEECH"
]
Eac3AtmosDrcRfType = Literal[
    "FILM_LIGHT", "FILM_STANDARD", "MUSIC_LIGHT", "MUSIC_STANDARD", "NONE", "SPEECH"
]
Eac3AttenuationControlType = Literal["ATTENUATE_3_DB", "NONE"]
Eac3BitstreamModeType = Literal[
    "COMMENTARY", "COMPLETE_MAIN", "EMERGENCY", "HEARING_IMPAIRED", "VISUALLY_IMPAIRED"
]
Eac3CodingModeType = Literal["CODING_MODE_1_0", "CODING_MODE_2_0", "CODING_MODE_3_2"]
Eac3DcFilterType = Literal["DISABLED", "ENABLED"]
Eac3DrcLineType = Literal[
    "FILM_LIGHT", "FILM_STANDARD", "MUSIC_LIGHT", "MUSIC_STANDARD", "NONE", "SPEECH"
]
Eac3DrcRfType = Literal[
    "FILM_LIGHT", "FILM_STANDARD", "MUSIC_LIGHT", "MUSIC_STANDARD", "NONE", "SPEECH"
]
Eac3LfeControlType = Literal["LFE", "NO_LFE"]
Eac3LfeFilterType = Literal["DISABLED", "ENABLED"]
Eac3MetadataControlType = Literal["FOLLOW_INPUT", "USE_CONFIGURED"]
Eac3PassthroughControlType = Literal["NO_PASSTHROUGH", "WHEN_POSSIBLE"]
Eac3PhaseControlType = Literal["NO_SHIFT", "SHIFT_90_DEGREES"]
Eac3StereoDownmixType = Literal["DPL2", "LO_RO", "LT_RT", "NOT_INDICATED"]
Eac3SurroundExModeType = Literal["DISABLED", "ENABLED", "NOT_INDICATED"]
Eac3SurroundModeType = Literal["DISABLED", "ENABLED", "NOT_INDICATED"]
EbuTtDDestinationStyleControlType = Literal["EXCLUDE", "INCLUDE"]
EbuTtDFillLineGapControlType = Literal["DISABLED", "ENABLED"]
EmbeddedConvert608To708Type = Literal["DISABLED", "UPCONVERT"]
EmbeddedScte20DetectionType = Literal["AUTO", "OFF"]
EventBridgeRuleTemplateEventTypeType = Literal[
    "MEDIACONNECT_ALERT",
    "MEDIACONNECT_FLOW_STATUS_CHANGE",
    "MEDIACONNECT_OUTPUT_HEALTH",
    "MEDIACONNECT_SOURCE_HEALTH",
    "MEDIALIVE_CHANNEL_ALERT",
    "MEDIALIVE_CHANNEL_INPUT_CHANGE",
    "MEDIALIVE_CHANNEL_STATE_CHANGE",
    "MEDIALIVE_MULTIPLEX_ALERT",
    "MEDIALIVE_MULTIPLEX_STATE_CHANGE",
    "MEDIAPACKAGE_HARVEST_JOB_NOTIFICATION",
    "MEDIAPACKAGE_INPUT_NOTIFICATION",
    "MEDIAPACKAGE_KEY_PROVIDER_NOTIFICATION",
    "SIGNAL_MAP_ACTIVE_ALARM",
]
FeatureActivationsInputPrepareScheduleActionsType = Literal["DISABLED", "ENABLED"]
FeatureActivationsOutputStaticImageOverlayScheduleActionsType = Literal["DISABLED", "ENABLED"]
FecOutputIncludeFecType = Literal["COLUMN", "COLUMN_AND_ROW"]
FixedAfdType = Literal[
    "AFD_0000",
    "AFD_0010",
    "AFD_0011",
    "AFD_0100",
    "AFD_1000",
    "AFD_1001",
    "AFD_1010",
    "AFD_1011",
    "AFD_1101",
    "AFD_1110",
    "AFD_1111",
]
Fmp4NielsenId3BehaviorType = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
Fmp4TimedMetadataBehaviorType = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
FollowPointType = Literal["END", "START"]
FrameCaptureIntervalUnitType = Literal["MILLISECONDS", "SECONDS"]
GlobalConfigurationInputEndActionType = Literal["NONE", "SWITCH_AND_LOOP_INPUTS"]
GlobalConfigurationLowFramerateInputsType = Literal["DISABLED", "ENABLED"]
GlobalConfigurationOutputLockingModeType = Literal["DISABLED", "EPOCH_LOCKING", "PIPELINE_LOCKING"]
GlobalConfigurationOutputTimingSourceType = Literal["INPUT_CLOCK", "SYSTEM_CLOCK"]
H264AdaptiveQuantizationType = Literal["AUTO", "HIGH", "HIGHER", "LOW", "MAX", "MEDIUM", "OFF"]
H264ColorMetadataType = Literal["IGNORE", "INSERT"]
H264EntropyEncodingType = Literal["CABAC", "CAVLC"]
H264FlickerAqType = Literal["DISABLED", "ENABLED"]
H264ForceFieldPicturesType = Literal["DISABLED", "ENABLED"]
H264FramerateControlType = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
H264GopBReferenceType = Literal["DISABLED", "ENABLED"]
H264GopSizeUnitsType = Literal["FRAMES", "SECONDS"]
H264LevelType = Literal[
    "H264_LEVEL_1",
    "H264_LEVEL_1_1",
    "H264_LEVEL_1_2",
    "H264_LEVEL_1_3",
    "H264_LEVEL_2",
    "H264_LEVEL_2_1",
    "H264_LEVEL_2_2",
    "H264_LEVEL_3",
    "H264_LEVEL_3_1",
    "H264_LEVEL_3_2",
    "H264_LEVEL_4",
    "H264_LEVEL_4_1",
    "H264_LEVEL_4_2",
    "H264_LEVEL_5",
    "H264_LEVEL_5_1",
    "H264_LEVEL_5_2",
    "H264_LEVEL_AUTO",
]
H264LookAheadRateControlType = Literal["HIGH", "LOW", "MEDIUM"]
H264ParControlType = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
H264ProfileType = Literal["BASELINE", "HIGH", "HIGH_10BIT", "HIGH_422", "HIGH_422_10BIT", "MAIN"]
H264QualityLevelType = Literal["ENHANCED_QUALITY", "STANDARD_QUALITY"]
H264RateControlModeType = Literal["CBR", "MULTIPLEX", "QVBR", "VBR"]
H264ScanTypeType = Literal["INTERLACED", "PROGRESSIVE"]
H264SceneChangeDetectType = Literal["DISABLED", "ENABLED"]
H264SpatialAqType = Literal["DISABLED", "ENABLED"]
H264SubGopLengthType = Literal["DYNAMIC", "FIXED"]
H264SyntaxType = Literal["DEFAULT", "RP2027"]
H264TemporalAqType = Literal["DISABLED", "ENABLED"]
H264TimecodeInsertionBehaviorType = Literal["DISABLED", "PIC_TIMING_SEI"]
H265AdaptiveQuantizationType = Literal["AUTO", "HIGH", "HIGHER", "LOW", "MAX", "MEDIUM", "OFF"]
H265AlternativeTransferFunctionType = Literal["INSERT", "OMIT"]
H265ColorMetadataType = Literal["IGNORE", "INSERT"]
H265DeblockingType = Literal["DISABLED", "ENABLED"]
H265FlickerAqType = Literal["DISABLED", "ENABLED"]
H265GopSizeUnitsType = Literal["FRAMES", "SECONDS"]
H265LevelType = Literal[
    "H265_LEVEL_1",
    "H265_LEVEL_2",
    "H265_LEVEL_2_1",
    "H265_LEVEL_3",
    "H265_LEVEL_3_1",
    "H265_LEVEL_4",
    "H265_LEVEL_4_1",
    "H265_LEVEL_5",
    "H265_LEVEL_5_1",
    "H265_LEVEL_5_2",
    "H265_LEVEL_6",
    "H265_LEVEL_6_1",
    "H265_LEVEL_6_2",
    "H265_LEVEL_AUTO",
]
H265LookAheadRateControlType = Literal["HIGH", "LOW", "MEDIUM"]
H265MvOverPictureBoundariesType = Literal["DISABLED", "ENABLED"]
H265MvTemporalPredictorType = Literal["DISABLED", "ENABLED"]
H265ProfileType = Literal["MAIN", "MAIN_10BIT"]
H265RateControlModeType = Literal["CBR", "MULTIPLEX", "QVBR"]
H265ScanTypeType = Literal["INTERLACED", "PROGRESSIVE"]
H265SceneChangeDetectType = Literal["DISABLED", "ENABLED"]
H265TierType = Literal["HIGH", "MAIN"]
H265TilePaddingType = Literal["NONE", "PADDED"]
H265TimecodeInsertionBehaviorType = Literal["DISABLED", "PIC_TIMING_SEI"]
H265TreeblockSizeType = Literal["AUTO", "TREE_SIZE_32X32"]
HlsAdMarkersType = Literal["ADOBE", "ELEMENTAL", "ELEMENTAL_SCTE35"]
HlsAkamaiHttpTransferModeType = Literal["CHUNKED", "NON_CHUNKED"]
HlsCaptionLanguageSettingType = Literal["INSERT", "NONE", "OMIT"]
HlsClientCacheType = Literal["DISABLED", "ENABLED"]
HlsCodecSpecificationType = Literal["RFC_4281", "RFC_6381"]
HlsDirectoryStructureType = Literal["SINGLE_DIRECTORY", "SUBDIRECTORY_PER_STREAM"]
HlsDiscontinuityTagsType = Literal["INSERT", "NEVER_INSERT"]
HlsEncryptionTypeType = Literal["AES128", "SAMPLE_AES"]
HlsH265PackagingTypeType = Literal["HEV1", "HVC1"]
HlsId3SegmentTaggingStateType = Literal["DISABLED", "ENABLED"]
HlsIncompleteSegmentBehaviorType = Literal["AUTO", "SUPPRESS"]
HlsIvInManifestType = Literal["EXCLUDE", "INCLUDE"]
HlsIvSourceType = Literal["EXPLICIT", "FOLLOWS_SEGMENT_NUMBER"]
HlsManifestCompressionType = Literal["GZIP", "NONE"]
HlsManifestDurationFormatType = Literal["FLOATING_POINT", "INTEGER"]
HlsMediaStoreStorageClassType = Literal["TEMPORAL"]
HlsModeType = Literal["LIVE", "VOD"]
HlsOutputSelectionType = Literal[
    "MANIFESTS_AND_SEGMENTS", "SEGMENTS_ONLY", "VARIANT_MANIFESTS_AND_SEGMENTS"
]
HlsProgramDateTimeClockType = Literal["INITIALIZE_FROM_OUTPUT_TIMECODE", "SYSTEM_CLOCK"]
HlsProgramDateTimeType = Literal["EXCLUDE", "INCLUDE"]
HlsRedundantManifestType = Literal["DISABLED", "ENABLED"]
HlsScte35SourceTypeType = Literal["MANIFEST", "SEGMENTS"]
HlsSegmentationModeType = Literal["USE_INPUT_SEGMENTATION", "USE_SEGMENT_DURATION"]
HlsStreamInfResolutionType = Literal["EXCLUDE", "INCLUDE"]
HlsTimedMetadataId3FrameType = Literal["NONE", "PRIV", "TDRL"]
HlsTsFileModeType = Literal["SEGMENTED_FILES", "SINGLE_FILE"]
HlsWebdavHttpTransferModeType = Literal["CHUNKED", "NON_CHUNKED"]
IFrameOnlyPlaylistTypeType = Literal["DISABLED", "STANDARD"]
IncludeFillerNalUnitsType = Literal["AUTO", "DROP", "INCLUDE"]
InputAttachedWaiterName = Literal["input_attached"]
InputClassType = Literal["SINGLE_PIPELINE", "STANDARD"]
InputCodecType = Literal["AVC", "HEVC", "MPEG2"]
InputDeblockFilterType = Literal["DISABLED", "ENABLED"]
InputDeletedWaiterName = Literal["input_deleted"]
InputDenoiseFilterType = Literal["DISABLED", "ENABLED"]
InputDetachedWaiterName = Literal["input_detached"]
InputDeviceActiveInputType = Literal["HDMI", "SDI"]
InputDeviceCodecType = Literal["AVC", "HEVC"]
InputDeviceConfigurableAudioChannelPairProfileType = Literal[
    "CBR-AAC_HQ-192000",
    "CBR-AAC_HQ-256000",
    "CBR-AAC_HQ-384000",
    "CBR-AAC_HQ-512000",
    "DISABLED",
    "VBR-AAC_HE-64000",
    "VBR-AAC_HHE-16000",
    "VBR-AAC_LC-128000",
]
InputDeviceConfiguredInputType = Literal["AUTO", "HDMI", "SDI"]
InputDeviceConnectionStateType = Literal["CONNECTED", "DISCONNECTED"]
InputDeviceIpSchemeType = Literal["DHCP", "STATIC"]
InputDeviceOutputTypeType = Literal["MEDIACONNECT_FLOW", "MEDIALIVE_INPUT", "NONE"]
InputDeviceScanTypeType = Literal["INTERLACED", "PROGRESSIVE"]
InputDeviceStateType = Literal["IDLE", "STREAMING"]
InputDeviceTransferTypeType = Literal["INCOMING", "OUTGOING"]
InputDeviceTypeType = Literal["HD", "UHD"]
InputDeviceUhdAudioChannelPairProfileType = Literal[
    "CBR-AAC_HQ-192000",
    "CBR-AAC_HQ-256000",
    "CBR-AAC_HQ-384000",
    "CBR-AAC_HQ-512000",
    "DISABLED",
    "VBR-AAC_HE-64000",
    "VBR-AAC_HHE-16000",
    "VBR-AAC_LC-128000",
]
InputFilterType = Literal["AUTO", "DISABLED", "FORCED"]
InputLossActionForHlsOutType = Literal["EMIT_OUTPUT", "PAUSE_OUTPUT"]
InputLossActionForMsSmoothOutType = Literal["EMIT_OUTPUT", "PAUSE_OUTPUT"]
InputLossActionForRtmpOutType = Literal["EMIT_OUTPUT", "PAUSE_OUTPUT"]
InputLossActionForUdpOutType = Literal["DROP_PROGRAM", "DROP_TS", "EMIT_PROGRAM"]
InputLossImageTypeType = Literal["COLOR", "SLATE"]
InputMaximumBitrateType = Literal["MAX_10_MBPS", "MAX_20_MBPS", "MAX_50_MBPS"]
InputNetworkLocationType = Literal["AWS", "ON_PREMISES"]
InputPreferenceType = Literal["EQUAL_INPUT_PREFERENCE", "PRIMARY_INPUT_PREFERRED"]
InputResolutionType = Literal["HD", "SD", "UHD"]
InputSecurityGroupStateType = Literal["DELETED", "IDLE", "IN_USE", "UPDATING"]
InputSourceEndBehaviorType = Literal["CONTINUE", "LOOP"]
InputSourceTypeType = Literal["DYNAMIC", "STATIC"]
InputStateType = Literal["ATTACHED", "CREATING", "DELETED", "DELETING", "DETACHED"]
InputTimecodeSourceType = Literal["EMBEDDED", "ZEROBASED"]
InputTypeType = Literal[
    "AWS_CDI",
    "INPUT_DEVICE",
    "MEDIACONNECT",
    "MP4_FILE",
    "MULTICAST",
    "RTMP_PULL",
    "RTMP_PUSH",
    "RTP_PUSH",
    "SDI",
    "SMPTE_2110_RECEIVER_GROUP",
    "SRT_CALLER",
    "TS_FILE",
    "UDP_PUSH",
    "URL_PULL",
]
LastFrameClippingBehaviorType = Literal["EXCLUDE_LAST_FRAME", "INCLUDE_LAST_FRAME"]
ListChannelPlacementGroupsPaginatorName = Literal["list_channel_placement_groups"]
ListChannelsPaginatorName = Literal["list_channels"]
ListCloudWatchAlarmTemplateGroupsPaginatorName = Literal["list_cloud_watch_alarm_template_groups"]
ListCloudWatchAlarmTemplatesPaginatorName = Literal["list_cloud_watch_alarm_templates"]
ListClustersPaginatorName = Literal["list_clusters"]
ListEventBridgeRuleTemplateGroupsPaginatorName = Literal["list_event_bridge_rule_template_groups"]
ListEventBridgeRuleTemplatesPaginatorName = Literal["list_event_bridge_rule_templates"]
ListInputDeviceTransfersPaginatorName = Literal["list_input_device_transfers"]
ListInputDevicesPaginatorName = Literal["list_input_devices"]
ListInputSecurityGroupsPaginatorName = Literal["list_input_security_groups"]
ListInputsPaginatorName = Literal["list_inputs"]
ListMultiplexProgramsPaginatorName = Literal["list_multiplex_programs"]
ListMultiplexesPaginatorName = Literal["list_multiplexes"]
ListNetworksPaginatorName = Literal["list_networks"]
ListNodesPaginatorName = Literal["list_nodes"]
ListOfferingsPaginatorName = Literal["list_offerings"]
ListReservationsPaginatorName = Literal["list_reservations"]
ListSdiSourcesPaginatorName = Literal["list_sdi_sources"]
ListSignalMapsPaginatorName = Literal["list_signal_maps"]
LogLevelType = Literal["DEBUG", "DISABLED", "ERROR", "INFO", "WARNING"]
M2tsAbsentInputAudioBehaviorType = Literal["DROP", "ENCODE_SILENCE"]
M2tsAribCaptionsPidControlType = Literal["AUTO", "USE_CONFIGURED"]
M2tsAribType = Literal["DISABLED", "ENABLED"]
M2tsAudioBufferModelType = Literal["ATSC", "DVB"]
M2tsAudioIntervalType = Literal["VIDEO_AND_FIXED_INTERVALS", "VIDEO_INTERVAL"]
M2tsAudioStreamTypeType = Literal["ATSC", "DVB"]
M2tsBufferModelType = Literal["MULTIPLEX", "NONE"]
M2tsCcDescriptorType = Literal["DISABLED", "ENABLED"]
M2tsEbifControlType = Literal["NONE", "PASSTHROUGH"]
M2tsEbpPlacementType = Literal["VIDEO_AND_AUDIO_PIDS", "VIDEO_PID"]
M2tsEsRateInPesType = Literal["EXCLUDE", "INCLUDE"]
M2tsKlvType = Literal["NONE", "PASSTHROUGH"]
M2tsNielsenId3BehaviorType = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
M2tsPcrControlType = Literal["CONFIGURED_PCR_PERIOD", "PCR_EVERY_PES_PACKET"]
M2tsRateModeType = Literal["CBR", "VBR"]
M2tsScte35ControlType = Literal["NONE", "PASSTHROUGH"]
M2tsSegmentationMarkersType = Literal[
    "EBP", "EBP_LEGACY", "NONE", "PSI_SEGSTART", "RAI_ADAPT", "RAI_SEGSTART"
]
M2tsSegmentationStyleType = Literal["MAINTAIN_CADENCE", "RESET_CADENCE"]
M2tsTimedMetadataBehaviorType = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
M3u8KlvBehaviorType = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
M3u8NielsenId3BehaviorType = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
M3u8PcrControlType = Literal["CONFIGURED_PCR_PERIOD", "PCR_EVERY_PES_PACKET"]
M3u8Scte35BehaviorType = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
M3u8TimedMetadataBehaviorType = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
MaintenanceDayType = Literal[
    "FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"
]
MotionGraphicsInsertionType = Literal["DISABLED", "ENABLED"]
Mp2CodingModeType = Literal["CODING_MODE_1_0", "CODING_MODE_2_0"]
Mpeg2AdaptiveQuantizationType = Literal["AUTO", "HIGH", "LOW", "MEDIUM", "OFF"]
Mpeg2ColorMetadataType = Literal["IGNORE", "INSERT"]
Mpeg2ColorSpaceType = Literal["AUTO", "PASSTHROUGH"]
Mpeg2DisplayRatioType = Literal["DISPLAYRATIO16X9", "DISPLAYRATIO4X3"]
Mpeg2GopSizeUnitsType = Literal["FRAMES", "SECONDS"]
Mpeg2ScanTypeType = Literal["INTERLACED", "PROGRESSIVE"]
Mpeg2SubGopLengthType = Literal["DYNAMIC", "FIXED"]
Mpeg2TimecodeInsertionBehaviorType = Literal["DISABLED", "GOP_TIMECODE"]
MsSmoothH265PackagingTypeType = Literal["HEV1", "HVC1"]
MultiplexCreatedWaiterName = Literal["multiplex_created"]
MultiplexDeletedWaiterName = Literal["multiplex_deleted"]
MultiplexRunningWaiterName = Literal["multiplex_running"]
MultiplexStateType = Literal[
    "CREATE_FAILED",
    "CREATING",
    "DELETED",
    "DELETING",
    "IDLE",
    "RECOVERING",
    "RUNNING",
    "STARTING",
    "STOPPING",
]
MultiplexStoppedWaiterName = Literal["multiplex_stopped"]
NetworkInputServerValidationType = Literal[
    "CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME", "CHECK_CRYPTOGRAPHY_ONLY"
]
NetworkInterfaceModeType = Literal["BRIDGE", "NAT"]
NetworkStateType = Literal[
    "ACTIVE",
    "CREATE_FAILED",
    "CREATING",
    "DELETED",
    "DELETE_FAILED",
    "DELETING",
    "IDLE",
    "IN_USE",
    "UPDATING",
]
NielsenPcmToId3TaggingStateType = Literal["DISABLED", "ENABLED"]
NielsenWatermarkTimezonesType = Literal[
    "AMERICA_PUERTO_RICO",
    "US_ALASKA",
    "US_ARIZONA",
    "US_CENTRAL",
    "US_EASTERN",
    "US_HAWAII",
    "US_MOUNTAIN",
    "US_PACIFIC",
    "US_SAMOA",
    "UTC",
]
NielsenWatermarksCbetStepasideType = Literal["DISABLED", "ENABLED"]
NielsenWatermarksDistributionTypesType = Literal["FINAL_DISTRIBUTOR", "PROGRAM_CONTENT"]
NodeConnectionStateType = Literal["CONNECTED", "DISCONNECTED"]
NodeDeregisteredWaiterName = Literal["node_deregistered"]
NodeRegisteredWaiterName = Literal["node_registered"]
NodeRoleType = Literal["ACTIVE", "BACKUP"]
NodeStateType = Literal[
    "ACTIVATION_FAILED",
    "ACTIVE",
    "CREATED",
    "DEREGISTERED",
    "DEREGISTERING",
    "DEREGISTRATION_FAILED",
    "DRAINING",
    "IN_USE",
    "READY",
    "READY_TO_ACTIVATE",
    "REGISTERING",
    "REGISTRATION_FAILED",
]
OfferingDurationUnitsType = Literal["MONTHS"]
OfferingTypeType = Literal["NO_UPFRONT"]
PipelineIdType = Literal["PIPELINE_0", "PIPELINE_1"]
PreferredChannelPipelineType = Literal["CURRENTLY_ACTIVE", "PIPELINE_0", "PIPELINE_1"]
RebootInputDeviceForceType = Literal["NO", "YES"]
ReservationAutomaticRenewalType = Literal["DISABLED", "ENABLED", "UNAVAILABLE"]
ReservationCodecType = Literal["AUDIO", "AV1", "AVC", "HEVC", "LINK", "MPEG2"]
ReservationMaximumBitrateType = Literal["MAX_10_MBPS", "MAX_20_MBPS", "MAX_50_MBPS"]
ReservationMaximumFramerateType = Literal["MAX_30_FPS", "MAX_60_FPS"]
ReservationResolutionType = Literal["FHD", "HD", "SD", "UHD"]
ReservationResourceTypeType = Literal["CHANNEL", "INPUT", "MULTIPLEX", "OUTPUT"]
ReservationSpecialFeatureType = Literal["ADVANCED_AUDIO", "AUDIO_NORMALIZATION", "MGHD", "MGUHD"]
ReservationStateType = Literal["ACTIVE", "CANCELED", "DELETED", "EXPIRED"]
ReservationVideoQualityType = Literal["ENHANCED", "PREMIUM", "STANDARD"]
RtmpAdMarkersType = Literal["ON_CUE_POINT_SCTE35"]
RtmpCacheFullBehaviorType = Literal["DISCONNECT_IMMEDIATELY", "WAIT_FOR_SERVER"]
RtmpCaptionDataType = Literal["ALL", "FIELD1_608", "FIELD1_AND_FIELD2_608"]
RtmpOutputCertificateModeType = Literal["SELF_SIGNED", "VERIFY_AUTHENTICITY"]
S3CannedAclType = Literal[
    "AUTHENTICATED_READ", "BUCKET_OWNER_FULL_CONTROL", "BUCKET_OWNER_READ", "PUBLIC_READ"
]
Scte20Convert608To708Type = Literal["DISABLED", "UPCONVERT"]
Scte27OcrLanguageType = Literal["DEU", "ENG", "FRA", "NLD", "POR", "SPA"]
Scte35AposNoRegionalBlackoutBehaviorType = Literal["FOLLOW", "IGNORE"]
Scte35AposWebDeliveryAllowedBehaviorType = Literal["FOLLOW", "IGNORE"]
Scte35ArchiveAllowedFlagType = Literal["ARCHIVE_ALLOWED", "ARCHIVE_NOT_ALLOWED"]
Scte35DeviceRestrictionsType = Literal[
    "NONE", "RESTRICT_GROUP0", "RESTRICT_GROUP1", "RESTRICT_GROUP2"
]
Scte35InputModeType = Literal["FIXED", "FOLLOW_ACTIVE"]
Scte35NoRegionalBlackoutFlagType = Literal["NO_REGIONAL_BLACKOUT", "REGIONAL_BLACKOUT"]
Scte35SegmentationCancelIndicatorType = Literal[
    "SEGMENTATION_EVENT_CANCELED", "SEGMENTATION_EVENT_NOT_CANCELED"
]
Scte35SegmentationScopeType = Literal["ALL_OUTPUT_GROUPS", "SCTE35_ENABLED_OUTPUT_GROUPS"]
Scte35SpliceInsertNoRegionalBlackoutBehaviorType = Literal["FOLLOW", "IGNORE"]
Scte35SpliceInsertWebDeliveryAllowedBehaviorType = Literal["FOLLOW", "IGNORE"]
Scte35TypeType = Literal["NONE", "SCTE_35_WITHOUT_SEGMENTATION"]
Scte35WebDeliveryAllowedFlagType = Literal["WEB_DELIVERY_ALLOWED", "WEB_DELIVERY_NOT_ALLOWED"]
SdiSourceModeType = Literal["INTERLEAVE", "QUADRANT"]
SdiSourceStateType = Literal["DELETED", "IDLE", "IN_USE"]
SdiSourceTypeType = Literal["QUAD", "SINGLE"]
SignalMapCreatedWaiterName = Literal["signal_map_created"]
SignalMapMonitorDeletedWaiterName = Literal["signal_map_monitor_deleted"]
SignalMapMonitorDeployedWaiterName = Literal["signal_map_monitor_deployed"]
SignalMapMonitorDeploymentStatusType = Literal[
    "DELETE_COMPLETE",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "DEPLOYMENT_COMPLETE",
    "DEPLOYMENT_FAILED",
    "DEPLOYMENT_IN_PROGRESS",
    "DRY_RUN_DEPLOYMENT_COMPLETE",
    "DRY_RUN_DEPLOYMENT_FAILED",
    "DRY_RUN_DEPLOYMENT_IN_PROGRESS",
    "NOT_DEPLOYED",
]
SignalMapStatusType = Literal[
    "CREATE_COMPLETE",
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "NOT_READY",
    "READY",
    "UPDATE_COMPLETE",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_REVERTED",
]
SignalMapUpdatedWaiterName = Literal["signal_map_updated"]
SmoothGroupAudioOnlyTimecodeControlType = Literal["PASSTHROUGH", "USE_CONFIGURED_CLOCK"]
SmoothGroupCertificateModeType = Literal["SELF_SIGNED", "VERIFY_AUTHENTICITY"]
SmoothGroupEventIdModeType = Literal["NO_EVENT_ID", "USE_CONFIGURED", "USE_TIMESTAMP"]
SmoothGroupEventStopBehaviorType = Literal["NONE", "SEND_EOS"]
SmoothGroupSegmentationModeType = Literal["USE_INPUT_SEGMENTATION", "USE_SEGMENT_DURATION"]
SmoothGroupSparseTrackTypeType = Literal["NONE", "SCTE_35", "SCTE_35_WITHOUT_SEGMENTATION"]
SmoothGroupStreamManifestBehaviorType = Literal["DO_NOT_SEND", "SEND"]
SmoothGroupTimestampOffsetModeType = Literal["USE_CONFIGURED_OFFSET", "USE_EVENT_START_DATE"]
Smpte2038DataPreferenceType = Literal["IGNORE", "PREFER"]
SrtEncryptionTypeType = Literal["AES128", "AES192", "AES256"]
TemporalFilterPostFilterSharpeningType = Literal["AUTO", "DISABLED", "ENABLED"]
TemporalFilterStrengthType = Literal[
    "AUTO",
    "STRENGTH_1",
    "STRENGTH_10",
    "STRENGTH_11",
    "STRENGTH_12",
    "STRENGTH_13",
    "STRENGTH_14",
    "STRENGTH_15",
    "STRENGTH_16",
    "STRENGTH_2",
    "STRENGTH_3",
    "STRENGTH_4",
    "STRENGTH_5",
    "STRENGTH_6",
    "STRENGTH_7",
    "STRENGTH_8",
    "STRENGTH_9",
]
ThumbnailStateType = Literal["AUTO", "DISABLED"]
ThumbnailTypeType = Literal["CURRENT_ACTIVE", "UNSPECIFIED"]
TimecodeBurninFontSizeType = Literal["EXTRA_SMALL_10", "LARGE_48", "MEDIUM_32", "SMALL_16"]
TimecodeBurninPositionType = Literal[
    "BOTTOM_CENTER",
    "BOTTOM_LEFT",
    "BOTTOM_RIGHT",
    "MIDDLE_CENTER",
    "MIDDLE_LEFT",
    "MIDDLE_RIGHT",
    "TOP_CENTER",
    "TOP_LEFT",
    "TOP_RIGHT",
]
TimecodeConfigSourceType = Literal["EMBEDDED", "SYSTEMCLOCK", "ZEROBASED"]
TtmlDestinationStyleControlType = Literal["PASSTHROUGH", "USE_CONFIGURED"]
UdpTimedMetadataId3FrameType = Literal["NONE", "PRIV", "TDRL"]
UpdateNodeStateType = Literal["ACTIVE", "DRAINING"]
VideoDescriptionRespondToAfdType = Literal["NONE", "PASSTHROUGH", "RESPOND"]
VideoDescriptionScalingBehaviorType = Literal["DEFAULT", "STRETCH_TO_OUTPUT"]
VideoSelectorColorSpaceType = Literal["FOLLOW", "HDR10", "HLG_2020", "REC_601", "REC_709"]
VideoSelectorColorSpaceUsageType = Literal["FALLBACK", "FORCE"]
WavCodingModeType = Literal[
    "CODING_MODE_1_0", "CODING_MODE_2_0", "CODING_MODE_4_0", "CODING_MODE_8_0"
]
WebvttDestinationStyleControlType = Literal["NO_STYLE_DATA", "PASSTHROUGH"]
MediaLiveServiceName = Literal["medialive"]
ServiceName = Literal[
    "accessanalyzer",
    "account",
    "acm",
    "acm-pca",
    "amp",
    "amplify",
    "amplifybackend",
    "amplifyuibuilder",
    "apigateway",
    "apigatewaymanagementapi",
    "apigatewayv2",
    "appconfig",
    "appconfigdata",
    "appfabric",
    "appflow",
    "appintegrations",
    "application-autoscaling",
    "application-insights",
    "application-signals",
    "applicationcostprofiler",
    "appmesh",
    "apprunner",
    "appstream",
    "appsync",
    "apptest",
    "arc-zonal-shift",
    "artifact",
    "athena",
    "auditmanager",
    "autoscaling",
    "autoscaling-plans",
    "b2bi",
    "backup",
    "backup-gateway",
    "backupsearch",
    "batch",
    "bcm-data-exports",
    "bcm-pricing-calculator",
    "bedrock",
    "bedrock-agent",
    "bedrock-agent-runtime",
    "bedrock-data-automation",
    "bedrock-data-automation-runtime",
    "bedrock-runtime",
    "billing",
    "billingconductor",
    "braket",
    "budgets",
    "ce",
    "chatbot",
    "chime",
    "chime-sdk-identity",
    "chime-sdk-media-pipelines",
    "chime-sdk-meetings",
    "chime-sdk-messaging",
    "chime-sdk-voice",
    "cleanrooms",
    "cleanroomsml",
    "cloud9",
    "cloudcontrol",
    "clouddirectory",
    "cloudformation",
    "cloudfront",
    "cloudfront-keyvaluestore",
    "cloudhsm",
    "cloudhsmv2",
    "cloudsearch",
    "cloudsearchdomain",
    "cloudtrail",
    "cloudtrail-data",
    "cloudwatch",
    "codeartifact",
    "codebuild",
    "codecatalyst",
    "codecommit",
    "codeconnections",
    "codedeploy",
    "codeguru-reviewer",
    "codeguru-security",
    "codeguruprofiler",
    "codepipeline",
    "codestar-connections",
    "codestar-notifications",
    "cognito-identity",
    "cognito-idp",
    "cognito-sync",
    "comprehend",
    "comprehendmedical",
    "compute-optimizer",
    "config",
    "connect",
    "connect-contact-lens",
    "connectcampaigns",
    "connectcampaignsv2",
    "connectcases",
    "connectparticipant",
    "controlcatalog",
    "controltower",
    "cost-optimization-hub",
    "cur",
    "customer-profiles",
    "databrew",
    "dataexchange",
    "datapipeline",
    "datasync",
    "datazone",
    "dax",
    "deadline",
    "detective",
    "devicefarm",
    "devops-guru",
    "directconnect",
    "discovery",
    "dlm",
    "dms",
    "docdb",
    "docdb-elastic",
    "drs",
    "ds",
    "ds-data",
    "dsql",
    "dynamodb",
    "dynamodbstreams",
    "ebs",
    "ec2",
    "ec2-instance-connect",
    "ecr",
    "ecr-public",
    "ecs",
    "efs",
    "eks",
    "eks-auth",
    "elasticache",
    "elasticbeanstalk",
    "elastictranscoder",
    "elb",
    "elbv2",
    "emr",
    "emr-containers",
    "emr-serverless",
    "entityresolution",
    "es",
    "events",
    "evidently",
    "finspace",
    "finspace-data",
    "firehose",
    "fis",
    "fms",
    "forecast",
    "forecastquery",
    "frauddetector",
    "freetier",
    "fsx",
    "gamelift",
    "gameliftstreams",
    "geo-maps",
    "geo-places",
    "geo-routes",
    "glacier",
    "globalaccelerator",
    "glue",
    "grafana",
    "greengrass",
    "greengrassv2",
    "groundstation",
    "guardduty",
    "health",
    "healthlake",
    "iam",
    "identitystore",
    "imagebuilder",
    "importexport",
    "inspector",
    "inspector-scan",
    "inspector2",
    "internetmonitor",
    "invoicing",
    "iot",
    "iot-data",
    "iot-jobs-data",
    "iot-managed-integrations",
    "iotanalytics",
    "iotdeviceadvisor",
    "iotevents",
    "iotevents-data",
    "iotfleethub",
    "iotfleetwise",
    "iotsecuretunneling",
    "iotsitewise",
    "iotthingsgraph",
    "iottwinmaker",
    "iotwireless",
    "ivs",
    "ivs-realtime",
    "ivschat",
    "kafka",
    "kafkaconnect",
    "kendra",
    "kendra-ranking",
    "keyspaces",
    "kinesis",
    "kinesis-video-archived-media",
    "kinesis-video-media",
    "kinesis-video-signaling",
    "kinesis-video-webrtc-storage",
    "kinesisanalytics",
    "kinesisanalyticsv2",
    "kinesisvideo",
    "kms",
    "lakeformation",
    "lambda",
    "launch-wizard",
    "lex-models",
    "lex-runtime",
    "lexv2-models",
    "lexv2-runtime",
    "license-manager",
    "license-manager-linux-subscriptions",
    "license-manager-user-subscriptions",
    "lightsail",
    "location",
    "logs",
    "lookoutequipment",
    "lookoutmetrics",
    "lookoutvision",
    "m2",
    "machinelearning",
    "macie2",
    "mailmanager",
    "managedblockchain",
    "managedblockchain-query",
    "marketplace-agreement",
    "marketplace-catalog",
    "marketplace-deployment",
    "marketplace-entitlement",
    "marketplace-reporting",
    "marketplacecommerceanalytics",
    "mediaconnect",
    "mediaconvert",
    "medialive",
    "mediapackage",
    "mediapackage-vod",
    "mediapackagev2",
    "mediastore",
    "mediastore-data",
    "mediatailor",
    "medical-imaging",
    "memorydb",
    "meteringmarketplace",
    "mgh",
    "mgn",
    "migration-hub-refactor-spaces",
    "migrationhub-config",
    "migrationhuborchestrator",
    "migrationhubstrategy",
    "mq",
    "mturk",
    "mwaa",
    "neptune",
    "neptune-graph",
    "neptunedata",
    "network-firewall",
    "networkflowmonitor",
    "networkmanager",
    "networkmonitor",
    "notifications",
    "notificationscontacts",
    "oam",
    "observabilityadmin",
    "omics",
    "opensearch",
    "opensearchserverless",
    "opsworks",
    "opsworkscm",
    "organizations",
    "osis",
    "outposts",
    "panorama",
    "partnercentral-selling",
    "payment-cryptography",
    "payment-cryptography-data",
    "pca-connector-ad",
    "pca-connector-scep",
    "pcs",
    "personalize",
    "personalize-events",
    "personalize-runtime",
    "pi",
    "pinpoint",
    "pinpoint-email",
    "pinpoint-sms-voice",
    "pinpoint-sms-voice-v2",
    "pipes",
    "polly",
    "pricing",
    "proton",
    "qapps",
    "qbusiness",
    "qconnect",
    "qldb",
    "qldb-session",
    "quicksight",
    "ram",
    "rbin",
    "rds",
    "rds-data",
    "redshift",
    "redshift-data",
    "redshift-serverless",
    "rekognition",
    "repostspace",
    "resiliencehub",
    "resource-explorer-2",
    "resource-groups",
    "resourcegroupstaggingapi",
    "robomaker",
    "rolesanywhere",
    "route53",
    "route53-recovery-cluster",
    "route53-recovery-control-config",
    "route53-recovery-readiness",
    "route53domains",
    "route53profiles",
    "route53resolver",
    "rum",
    "s3",
    "s3control",
    "s3outposts",
    "s3tables",
    "sagemaker",
    "sagemaker-a2i-runtime",
    "sagemaker-edge",
    "sagemaker-featurestore-runtime",
    "sagemaker-geospatial",
    "sagemaker-metrics",
    "sagemaker-runtime",
    "savingsplans",
    "scheduler",
    "schemas",
    "sdb",
    "secretsmanager",
    "security-ir",
    "securityhub",
    "securitylake",
    "serverlessrepo",
    "service-quotas",
    "servicecatalog",
    "servicecatalog-appregistry",
    "servicediscovery",
    "ses",
    "sesv2",
    "shield",
    "signer",
    "simspaceweaver",
    "sms",
    "snow-device-management",
    "snowball",
    "sns",
    "socialmessaging",
    "sqs",
    "ssm",
    "ssm-contacts",
    "ssm-guiconnect",
    "ssm-incidents",
    "ssm-quicksetup",
    "ssm-sap",
    "sso",
    "sso-admin",
    "sso-oidc",
    "stepfunctions",
    "storagegateway",
    "sts",
    "supplychain",
    "support",
    "support-app",
    "swf",
    "synthetics",
    "taxsettings",
    "textract",
    "timestream-influxdb",
    "timestream-query",
    "timestream-write",
    "tnb",
    "transcribe",
    "transfer",
    "translate",
    "trustedadvisor",
    "verifiedpermissions",
    "voice-id",
    "vpc-lattice",
    "waf",
    "waf-regional",
    "wafv2",
    "wellarchitected",
    "wisdom",
    "workdocs",
    "workmail",
    "workmailmessageflow",
    "workspaces",
    "workspaces-thin-client",
    "workspaces-web",
    "xray",
]
ResourceServiceName = Literal[
    "cloudformation",
    "cloudwatch",
    "dynamodb",
    "ec2",
    "glacier",
    "iam",
    "opsworks",
    "s3",
    "sns",
    "sqs",
]
PaginatorName = Literal[
    "describe_schedule",
    "list_channel_placement_groups",
    "list_channels",
    "list_cloud_watch_alarm_template_groups",
    "list_cloud_watch_alarm_templates",
    "list_clusters",
    "list_event_bridge_rule_template_groups",
    "list_event_bridge_rule_templates",
    "list_input_device_transfers",
    "list_input_devices",
    "list_input_security_groups",
    "list_inputs",
    "list_multiplex_programs",
    "list_multiplexes",
    "list_networks",
    "list_nodes",
    "list_offerings",
    "list_reservations",
    "list_sdi_sources",
    "list_signal_maps",
]
WaiterName = Literal[
    "channel_created",
    "channel_deleted",
    "channel_placement_group_assigned",
    "channel_placement_group_deleted",
    "channel_placement_group_unassigned",
    "channel_running",
    "channel_stopped",
    "cluster_created",
    "cluster_deleted",
    "input_attached",
    "input_deleted",
    "input_detached",
    "multiplex_created",
    "multiplex_deleted",
    "multiplex_running",
    "multiplex_stopped",
    "node_deregistered",
    "node_registered",
    "signal_map_created",
    "signal_map_monitor_deleted",
    "signal_map_monitor_deployed",
    "signal_map_updated",
]
RegionName = Literal[
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-northeast-3",
    "ap-south-1",
    "ap-south-2",
    "ap-southeast-1",
    "ap-southeast-2",
    "ap-southeast-4",
    "ca-central-1",
    "eu-central-1",
    "eu-north-1",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "me-central-1",
    "sa-east-1",
    "us-east-1",
    "us-east-2",
    "us-west-2",
]
