"""
Type annotations for mediaconvert service literal definitions.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconvert/literals/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from types_aiobotocore_mediaconvert.literals import AacAudioDescriptionBroadcasterMixType

    data: AacAudioDescriptionBroadcasterMixType = "BROADCASTER_MIXED_AD"
    ```
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AacAudioDescriptionBroadcasterMixType",
    "AacCodecProfileType",
    "AacCodingModeType",
    "AacRateControlModeType",
    "AacRawFormatType",
    "AacSpecificationType",
    "AacVbrQualityType",
    "Ac3BitstreamModeType",
    "Ac3CodingModeType",
    "Ac3DynamicRangeCompressionLineType",
    "Ac3DynamicRangeCompressionProfileType",
    "Ac3DynamicRangeCompressionRfType",
    "Ac3LfeFilterType",
    "Ac3MetadataControlType",
    "AccelerationModeType",
    "AccelerationStatusType",
    "AdvancedInputFilterAddTextureType",
    "AdvancedInputFilterSharpenType",
    "AdvancedInputFilterType",
    "AfdSignalingType",
    "AlphaBehaviorType",
    "AncillaryConvert608To708Type",
    "AncillaryTerminateCaptionsType",
    "AntiAliasType",
    "AudioChannelTagType",
    "AudioCodecType",
    "AudioDefaultSelectionType",
    "AudioDurationCorrectionType",
    "AudioLanguageCodeControlType",
    "AudioNormalizationAlgorithmControlType",
    "AudioNormalizationAlgorithmType",
    "AudioNormalizationLoudnessLoggingType",
    "AudioNormalizationPeakCalculationType",
    "AudioSelectorTypeType",
    "AudioTypeControlType",
    "Av1AdaptiveQuantizationType",
    "Av1BitDepthType",
    "Av1FilmGrainSynthesisType",
    "Av1FramerateControlType",
    "Av1FramerateConversionAlgorithmType",
    "Av1RateControlModeType",
    "Av1SpatialAdaptiveQuantizationType",
    "AvcIntraClassType",
    "AvcIntraFramerateControlType",
    "AvcIntraFramerateConversionAlgorithmType",
    "AvcIntraInterlaceModeType",
    "AvcIntraScanTypeConversionModeType",
    "AvcIntraSlowPalType",
    "AvcIntraTelecineType",
    "AvcIntraUhdQualityTuningLevelType",
    "BandwidthReductionFilterSharpeningType",
    "BandwidthReductionFilterStrengthType",
    "BillingTagsSourceType",
    "BurnInSubtitleStylePassthroughType",
    "BurninSubtitleAlignmentType",
    "BurninSubtitleApplyFontColorType",
    "BurninSubtitleBackgroundColorType",
    "BurninSubtitleFallbackFontType",
    "BurninSubtitleFontColorType",
    "BurninSubtitleOutlineColorType",
    "BurninSubtitleShadowColorType",
    "BurninSubtitleTeletextSpacingType",
    "CaptionDestinationTypeType",
    "CaptionSourceByteRateLimitType",
    "CaptionSourceConvertPaintOnToPopOnType",
    "CaptionSourceTypeType",
    "CaptionSourceUpconvertSTLToTeletextType",
    "ChromaPositionModeType",
    "CmafClientCacheType",
    "CmafCodecSpecificationType",
    "CmafEncryptionTypeType",
    "CmafImageBasedTrickPlayType",
    "CmafInitializationVectorInManifestType",
    "CmafIntervalCadenceType",
    "CmafKeyProviderTypeType",
    "CmafManifestCompressionType",
    "CmafManifestDurationFormatType",
    "CmafMpdManifestBandwidthTypeType",
    "CmafMpdProfileType",
    "CmafPtsOffsetHandlingForBFramesType",
    "CmafSegmentControlType",
    "CmafSegmentLengthControlType",
    "CmafStreamInfResolutionType",
    "CmafTargetDurationCompatibilityModeType",
    "CmafVideoCompositionOffsetsType",
    "CmafWriteDASHManifestType",
    "CmafWriteHLSManifestType",
    "CmafWriteSegmentTimelineInRepresentationType",
    "CmfcAudioDurationType",
    "CmfcAudioTrackTypeType",
    "CmfcDescriptiveVideoServiceFlagType",
    "CmfcIFrameOnlyManifestType",
    "CmfcKlvMetadataType",
    "CmfcManifestMetadataSignalingType",
    "CmfcScte35EsamType",
    "CmfcScte35SourceType",
    "CmfcTimedMetadataBoxVersionType",
    "CmfcTimedMetadataType",
    "CodecType",
    "ColorMetadataType",
    "ColorPrimariesType",
    "ColorSpaceConversionType",
    "ColorSpaceType",
    "ColorSpaceUsageType",
    "CommitmentType",
    "ContainerTypeType",
    "CopyProtectionActionType",
    "DashIsoGroupAudioChannelConfigSchemeIdUriType",
    "DashIsoHbbtvComplianceType",
    "DashIsoImageBasedTrickPlayType",
    "DashIsoIntervalCadenceType",
    "DashIsoMpdManifestBandwidthTypeType",
    "DashIsoMpdProfileType",
    "DashIsoPlaybackDeviceCompatibilityType",
    "DashIsoPtsOffsetHandlingForBFramesType",
    "DashIsoSegmentControlType",
    "DashIsoSegmentLengthControlType",
    "DashIsoVideoCompositionOffsetsType",
    "DashIsoWriteSegmentTimelineInRepresentationType",
    "DashManifestStyleType",
    "DecryptionModeType",
    "DeinterlaceAlgorithmType",
    "DeinterlacerControlType",
    "DeinterlacerModeType",
    "DescribeEndpointsModeType",
    "DescribeEndpointsPaginatorName",
    "DolbyVisionLevel6ModeType",
    "DolbyVisionMappingType",
    "DolbyVisionProfileType",
    "DropFrameTimecodeType",
    "DvbSubSubtitleFallbackFontType",
    "DvbSubtitleAlignmentType",
    "DvbSubtitleApplyFontColorType",
    "DvbSubtitleBackgroundColorType",
    "DvbSubtitleFontColorType",
    "DvbSubtitleOutlineColorType",
    "DvbSubtitleShadowColorType",
    "DvbSubtitleStylePassthroughType",
    "DvbSubtitleTeletextSpacingType",
    "DvbSubtitlingTypeType",
    "DvbddsHandlingType",
    "DynamicAudioSelectorTypeType",
    "Eac3AtmosBitstreamModeType",
    "Eac3AtmosCodingModeType",
    "Eac3AtmosDialogueIntelligenceType",
    "Eac3AtmosDownmixControlType",
    "Eac3AtmosDynamicRangeCompressionLineType",
    "Eac3AtmosDynamicRangeCompressionRfType",
    "Eac3AtmosDynamicRangeControlType",
    "Eac3AtmosMeteringModeType",
    "Eac3AtmosStereoDownmixType",
    "Eac3AtmosSurroundExModeType",
    "Eac3AttenuationControlType",
    "Eac3BitstreamModeType",
    "Eac3CodingModeType",
    "Eac3DcFilterType",
    "Eac3DynamicRangeCompressionLineType",
    "Eac3DynamicRangeCompressionRfType",
    "Eac3LfeControlType",
    "Eac3LfeFilterType",
    "Eac3MetadataControlType",
    "Eac3PassthroughControlType",
    "Eac3PhaseControlType",
    "Eac3StereoDownmixType",
    "Eac3SurroundExModeType",
    "Eac3SurroundModeType",
    "EmbeddedConvert608To708Type",
    "EmbeddedTerminateCaptionsType",
    "EmbeddedTimecodeOverrideType",
    "F4vMoovPlacementType",
    "FileSourceConvert608To708Type",
    "FileSourceTimeDeltaUnitsType",
    "FontScriptType",
    "FormatType",
    "FrameMetricTypeType",
    "GifFramerateControlType",
    "GifFramerateConversionAlgorithmType",
    "H264AdaptiveQuantizationType",
    "H264CodecLevelType",
    "H264CodecProfileType",
    "H264DynamicSubGopType",
    "H264EndOfStreamMarkersType",
    "H264EntropyEncodingType",
    "H264FieldEncodingType",
    "H264FlickerAdaptiveQuantizationType",
    "H264FramerateControlType",
    "H264FramerateConversionAlgorithmType",
    "H264GopBReferenceType",
    "H264GopSizeUnitsType",
    "H264InterlaceModeType",
    "H264ParControlType",
    "H264QualityTuningLevelType",
    "H264RateControlModeType",
    "H264RepeatPpsType",
    "H264SaliencyAwareEncodingType",
    "H264ScanTypeConversionModeType",
    "H264SceneChangeDetectType",
    "H264SlowPalType",
    "H264SpatialAdaptiveQuantizationType",
    "H264SyntaxType",
    "H264TelecineType",
    "H264TemporalAdaptiveQuantizationType",
    "H264UnregisteredSeiTimecodeType",
    "H264WriteMp4PackagingTypeType",
    "H265AdaptiveQuantizationType",
    "H265AlternateTransferFunctionSeiType",
    "H265CodecLevelType",
    "H265CodecProfileType",
    "H265DeblockingType",
    "H265DynamicSubGopType",
    "H265EndOfStreamMarkersType",
    "H265FlickerAdaptiveQuantizationType",
    "H265FramerateControlType",
    "H265FramerateConversionAlgorithmType",
    "H265GopBReferenceType",
    "H265GopSizeUnitsType",
    "H265InterlaceModeType",
    "H265ParControlType",
    "H265QualityTuningLevelType",
    "H265RateControlModeType",
    "H265SampleAdaptiveOffsetFilterModeType",
    "H265ScanTypeConversionModeType",
    "H265SceneChangeDetectType",
    "H265SlowPalType",
    "H265SpatialAdaptiveQuantizationType",
    "H265TelecineType",
    "H265TemporalAdaptiveQuantizationType",
    "H265TemporalIdsType",
    "H265TilesType",
    "H265UnregisteredSeiTimecodeType",
    "H265WriteMp4PackagingTypeType",
    "HDRToSDRToneMapperType",
    "HlsAdMarkersType",
    "HlsAudioOnlyContainerType",
    "HlsAudioOnlyHeaderType",
    "HlsAudioTrackTypeType",
    "HlsCaptionLanguageSettingType",
    "HlsCaptionSegmentLengthControlType",
    "HlsClientCacheType",
    "HlsCodecSpecificationType",
    "HlsDescriptiveVideoServiceFlagType",
    "HlsDirectoryStructureType",
    "HlsEncryptionTypeType",
    "HlsIFrameOnlyManifestType",
    "HlsImageBasedTrickPlayType",
    "HlsInitializationVectorInManifestType",
    "HlsIntervalCadenceType",
    "HlsKeyProviderTypeType",
    "HlsManifestCompressionType",
    "HlsManifestDurationFormatType",
    "HlsOfflineEncryptedType",
    "HlsOutputSelectionType",
    "HlsProgramDateTimeType",
    "HlsProgressiveWriteHlsManifestType",
    "HlsSegmentControlType",
    "HlsSegmentLengthControlType",
    "HlsStreamInfResolutionType",
    "HlsTargetDurationCompatibilityModeType",
    "HlsTimedMetadataId3FrameType",
    "ImscAccessibilitySubsType",
    "ImscStylePassthroughType",
    "InputDeblockFilterType",
    "InputDenoiseFilterType",
    "InputFilterEnableType",
    "InputPolicyType",
    "InputPsiControlType",
    "InputRotateType",
    "InputSampleRangeType",
    "InputScanTypeType",
    "InputTimecodeSourceType",
    "JobPhaseType",
    "JobStatusType",
    "JobTemplateListByType",
    "LanguageCodeType",
    "ListJobTemplatesPaginatorName",
    "ListJobsPaginatorName",
    "ListPresetsPaginatorName",
    "ListQueuesPaginatorName",
    "ListVersionsPaginatorName",
    "M2tsAudioBufferModelType",
    "M2tsAudioDurationType",
    "M2tsBufferModelType",
    "M2tsDataPtsControlType",
    "M2tsEbpAudioIntervalType",
    "M2tsEbpPlacementType",
    "M2tsEsRateInPesType",
    "M2tsForceTsVideoEbpOrderType",
    "M2tsKlvMetadataType",
    "M2tsNielsenId3Type",
    "M2tsPcrControlType",
    "M2tsPreventBufferUnderflowType",
    "M2tsRateModeType",
    "M2tsScte35SourceType",
    "M2tsSegmentationMarkersType",
    "M2tsSegmentationStyleType",
    "M3u8AudioDurationType",
    "M3u8DataPtsControlType",
    "M3u8NielsenId3Type",
    "M3u8PcrControlType",
    "M3u8Scte35SourceType",
    "MatrixCoefficientsType",
    "MediaConvertServiceName",
    "MotionImageInsertionModeType",
    "MotionImagePlaybackType",
    "MovClapAtomType",
    "MovCslgAtomType",
    "MovMpeg2FourCCControlType",
    "MovPaddingControlType",
    "MovReferenceType",
    "Mp3RateControlModeType",
    "Mp4CslgAtomType",
    "Mp4FreeSpaceBoxType",
    "Mp4MoovPlacementType",
    "MpdAccessibilityCaptionHintsType",
    "MpdAudioDurationType",
    "MpdCaptionContainerTypeType",
    "MpdKlvMetadataType",
    "MpdManifestMetadataSignalingType",
    "MpdScte35EsamType",
    "MpdScte35SourceType",
    "MpdTimedMetadataBoxVersionType",
    "MpdTimedMetadataType",
    "Mpeg2AdaptiveQuantizationType",
    "Mpeg2CodecLevelType",
    "Mpeg2CodecProfileType",
    "Mpeg2DynamicSubGopType",
    "Mpeg2FramerateControlType",
    "Mpeg2FramerateConversionAlgorithmType",
    "Mpeg2GopSizeUnitsType",
    "Mpeg2InterlaceModeType",
    "Mpeg2IntraDcPrecisionType",
    "Mpeg2ParControlType",
    "Mpeg2QualityTuningLevelType",
    "Mpeg2RateControlModeType",
    "Mpeg2ScanTypeConversionModeType",
    "Mpeg2SceneChangeDetectType",
    "Mpeg2SlowPalType",
    "Mpeg2SpatialAdaptiveQuantizationType",
    "Mpeg2SyntaxType",
    "Mpeg2TelecineType",
    "Mpeg2TemporalAdaptiveQuantizationType",
    "MsSmoothAudioDeduplicationType",
    "MsSmoothFragmentLengthControlType",
    "MsSmoothManifestEncodingType",
    "MxfAfdSignalingType",
    "MxfProfileType",
    "MxfXavcDurationModeType",
    "NielsenActiveWatermarkProcessTypeType",
    "NielsenSourceWatermarkStatusTypeType",
    "NielsenUniqueTicPerAudioTrackTypeType",
    "NoiseFilterPostTemporalSharpeningStrengthType",
    "NoiseFilterPostTemporalSharpeningType",
    "NoiseReducerFilterType",
    "OrderType",
    "OutputGroupTypeType",
    "OutputSdtType",
    "PadVideoType",
    "PaginatorName",
    "PresetListByType",
    "PresetSpeke20AudioType",
    "PresetSpeke20VideoType",
    "PricingPlanType",
    "ProresChromaSamplingType",
    "ProresCodecProfileType",
    "ProresFramerateControlType",
    "ProresFramerateConversionAlgorithmType",
    "ProresInterlaceModeType",
    "ProresParControlType",
    "ProresScanTypeConversionModeType",
    "ProresSlowPalType",
    "ProresTelecineType",
    "QueueListByType",
    "QueueStatusType",
    "RegionName",
    "RemoveRubyReserveAttributesType",
    "RenewalTypeType",
    "RequiredFlagType",
    "ReservationPlanStatusType",
    "ResourceServiceName",
    "RespondToAfdType",
    "RuleTypeType",
    "S3ObjectCannedAclType",
    "S3ServerSideEncryptionTypeType",
    "S3StorageClassType",
    "SampleRangeConversionType",
    "ScalingBehaviorType",
    "SccDestinationFramerateType",
    "SearchJobsPaginatorName",
    "ServiceName",
    "SimulateReservedQueueType",
    "SrtStylePassthroughType",
    "StatusUpdateIntervalType",
    "TeletextPageTypeType",
    "TimecodeBurninPositionType",
    "TimecodeSourceType",
    "TimecodeTrackType",
    "TimedMetadataType",
    "TrackTypeType",
    "TransferCharacteristicsType",
    "TsPtsOffsetType",
    "TtmlStylePassthroughType",
    "TypeType",
    "UncompressedFourccType",
    "UncompressedFramerateControlType",
    "UncompressedFramerateConversionAlgorithmType",
    "UncompressedInterlaceModeType",
    "UncompressedScanTypeConversionModeType",
    "UncompressedSlowPalType",
    "UncompressedTelecineType",
    "Vc3ClassType",
    "Vc3FramerateControlType",
    "Vc3FramerateConversionAlgorithmType",
    "Vc3InterlaceModeType",
    "Vc3ScanTypeConversionModeType",
    "Vc3SlowPalType",
    "Vc3TelecineType",
    "VchipActionType",
    "VideoCodecType",
    "VideoOverlayPlayBackModeType",
    "VideoOverlayUnitType",
    "VideoTimecodeInsertionType",
    "Vp8FramerateControlType",
    "Vp8FramerateConversionAlgorithmType",
    "Vp8ParControlType",
    "Vp8QualityTuningLevelType",
    "Vp8RateControlModeType",
    "Vp9FramerateControlType",
    "Vp9FramerateConversionAlgorithmType",
    "Vp9ParControlType",
    "Vp9QualityTuningLevelType",
    "Vp9RateControlModeType",
    "WatermarkingStrengthType",
    "WavFormatType",
    "WebvttAccessibilitySubsType",
    "WebvttStylePassthroughType",
    "Xavc4kIntraCbgProfileClassType",
    "Xavc4kIntraVbrProfileClassType",
    "Xavc4kProfileBitrateClassType",
    "Xavc4kProfileCodecProfileType",
    "Xavc4kProfileQualityTuningLevelType",
    "XavcAdaptiveQuantizationType",
    "XavcEntropyEncodingType",
    "XavcFlickerAdaptiveQuantizationType",
    "XavcFramerateControlType",
    "XavcFramerateConversionAlgorithmType",
    "XavcGopBReferenceType",
    "XavcHdIntraCbgProfileClassType",
    "XavcHdProfileBitrateClassType",
    "XavcHdProfileQualityTuningLevelType",
    "XavcHdProfileTelecineType",
    "XavcInterlaceModeType",
    "XavcProfileType",
    "XavcSlowPalType",
    "XavcSpatialAdaptiveQuantizationType",
    "XavcTemporalAdaptiveQuantizationType",
)

AacAudioDescriptionBroadcasterMixType = Literal["BROADCASTER_MIXED_AD", "NORMAL"]
AacCodecProfileType = Literal["HEV1", "HEV2", "LC"]
AacCodingModeType = Literal[
    "AD_RECEIVER_MIX", "CODING_MODE_1_0", "CODING_MODE_1_1", "CODING_MODE_2_0", "CODING_MODE_5_1"
]
AacRateControlModeType = Literal["CBR", "VBR"]
AacRawFormatType = Literal["LATM_LOAS", "NONE"]
AacSpecificationType = Literal["MPEG2", "MPEG4"]
AacVbrQualityType = Literal["HIGH", "LOW", "MEDIUM_HIGH", "MEDIUM_LOW"]
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
Ac3DynamicRangeCompressionLineType = Literal[
    "FILM_LIGHT", "FILM_STANDARD", "MUSIC_LIGHT", "MUSIC_STANDARD", "NONE", "SPEECH"
]
Ac3DynamicRangeCompressionProfileType = Literal["FILM_STANDARD", "NONE"]
Ac3DynamicRangeCompressionRfType = Literal[
    "FILM_LIGHT", "FILM_STANDARD", "MUSIC_LIGHT", "MUSIC_STANDARD", "NONE", "SPEECH"
]
Ac3LfeFilterType = Literal["DISABLED", "ENABLED"]
Ac3MetadataControlType = Literal["FOLLOW_INPUT", "USE_CONFIGURED"]
AccelerationModeType = Literal["DISABLED", "ENABLED", "PREFERRED"]
AccelerationStatusType = Literal["ACCELERATED", "IN_PROGRESS", "NOT_ACCELERATED", "NOT_APPLICABLE"]
AdvancedInputFilterAddTextureType = Literal["DISABLED", "ENABLED"]
AdvancedInputFilterSharpenType = Literal["HIGH", "LOW", "OFF"]
AdvancedInputFilterType = Literal["DISABLED", "ENABLED"]
AfdSignalingType = Literal["AUTO", "FIXED", "NONE"]
AlphaBehaviorType = Literal["DISCARD", "REMAP_TO_LUMA"]
AncillaryConvert608To708Type = Literal["DISABLED", "UPCONVERT"]
AncillaryTerminateCaptionsType = Literal["DISABLED", "END_OF_INPUT"]
AntiAliasType = Literal["DISABLED", "ENABLED"]
AudioChannelTagType = Literal[
    "C",
    "CS",
    "HI",
    "L",
    "LC",
    "LFE",
    "LFE2",
    "LS",
    "LSD",
    "LT",
    "LW",
    "M",
    "NAR",
    "R",
    "RC",
    "RS",
    "RSD",
    "RSL",
    "RSR",
    "RT",
    "RW",
    "TBC",
    "TBL",
    "TBR",
    "TCS",
    "VHC",
    "VHL",
    "VHR",
]
AudioCodecType = Literal[
    "AAC",
    "AC3",
    "AIFF",
    "EAC3",
    "EAC3_ATMOS",
    "FLAC",
    "MP2",
    "MP3",
    "OPUS",
    "PASSTHROUGH",
    "VORBIS",
    "WAV",
]
AudioDefaultSelectionType = Literal["DEFAULT", "NOT_DEFAULT"]
AudioDurationCorrectionType = Literal["AUTO", "DISABLED", "FORCE", "FRAME", "TRACK"]
AudioLanguageCodeControlType = Literal["FOLLOW_INPUT", "USE_CONFIGURED"]
AudioNormalizationAlgorithmControlType = Literal["CORRECT_AUDIO", "MEASURE_ONLY"]
AudioNormalizationAlgorithmType = Literal[
    "ITU_BS_1770_1", "ITU_BS_1770_2", "ITU_BS_1770_3", "ITU_BS_1770_4"
]
AudioNormalizationLoudnessLoggingType = Literal["DONT_LOG", "LOG"]
AudioNormalizationPeakCalculationType = Literal["NONE", "TRUE_PEAK"]
AudioSelectorTypeType = Literal["ALL_PCM", "HLS_RENDITION_GROUP", "LANGUAGE_CODE", "PID", "TRACK"]
AudioTypeControlType = Literal["FOLLOW_INPUT", "USE_CONFIGURED"]
Av1AdaptiveQuantizationType = Literal["HIGH", "HIGHER", "LOW", "MAX", "MEDIUM", "OFF"]
Av1BitDepthType = Literal["BIT_10", "BIT_8"]
Av1FilmGrainSynthesisType = Literal["DISABLED", "ENABLED"]
Av1FramerateControlType = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
Av1FramerateConversionAlgorithmType = Literal[
    "DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE", "MAINTAIN_FRAME_COUNT"
]
Av1RateControlModeType = Literal["QVBR"]
Av1SpatialAdaptiveQuantizationType = Literal["DISABLED", "ENABLED"]
AvcIntraClassType = Literal["CLASS_100", "CLASS_200", "CLASS_4K_2K", "CLASS_50"]
AvcIntraFramerateControlType = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
AvcIntraFramerateConversionAlgorithmType = Literal[
    "DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE", "MAINTAIN_FRAME_COUNT"
]
AvcIntraInterlaceModeType = Literal[
    "BOTTOM_FIELD", "FOLLOW_BOTTOM_FIELD", "FOLLOW_TOP_FIELD", "PROGRESSIVE", "TOP_FIELD"
]
AvcIntraScanTypeConversionModeType = Literal["INTERLACED", "INTERLACED_OPTIMIZE"]
AvcIntraSlowPalType = Literal["DISABLED", "ENABLED"]
AvcIntraTelecineType = Literal["HARD", "NONE"]
AvcIntraUhdQualityTuningLevelType = Literal["MULTI_PASS", "SINGLE_PASS"]
BandwidthReductionFilterSharpeningType = Literal["HIGH", "LOW", "MEDIUM", "OFF"]
BandwidthReductionFilterStrengthType = Literal["AUTO", "HIGH", "LOW", "MEDIUM", "OFF"]
BillingTagsSourceType = Literal["JOB", "JOB_TEMPLATE", "PRESET", "QUEUE"]
BurnInSubtitleStylePassthroughType = Literal["DISABLED", "ENABLED"]
BurninSubtitleAlignmentType = Literal["AUTO", "CENTERED", "LEFT"]
BurninSubtitleApplyFontColorType = Literal["ALL_TEXT", "WHITE_TEXT_ONLY"]
BurninSubtitleBackgroundColorType = Literal["AUTO", "BLACK", "NONE", "WHITE"]
BurninSubtitleFallbackFontType = Literal[
    "BEST_MATCH",
    "MONOSPACED_SANSSERIF",
    "MONOSPACED_SERIF",
    "PROPORTIONAL_SANSSERIF",
    "PROPORTIONAL_SERIF",
]
BurninSubtitleFontColorType = Literal[
    "AUTO", "BLACK", "BLUE", "GREEN", "HEX", "RED", "WHITE", "YELLOW"
]
BurninSubtitleOutlineColorType = Literal["AUTO", "BLACK", "BLUE", "GREEN", "RED", "WHITE", "YELLOW"]
BurninSubtitleShadowColorType = Literal["AUTO", "BLACK", "NONE", "WHITE"]
BurninSubtitleTeletextSpacingType = Literal["AUTO", "FIXED_GRID", "PROPORTIONAL"]
CaptionDestinationTypeType = Literal[
    "BURN_IN",
    "DVB_SUB",
    "EMBEDDED",
    "EMBEDDED_PLUS_SCTE20",
    "IMSC",
    "SCC",
    "SCTE20_PLUS_EMBEDDED",
    "SMI",
    "SRT",
    "TELETEXT",
    "TTML",
    "WEBVTT",
]
CaptionSourceByteRateLimitType = Literal["DISABLED", "ENABLED"]
CaptionSourceConvertPaintOnToPopOnType = Literal["DISABLED", "ENABLED"]
CaptionSourceTypeType = Literal[
    "ANCILLARY",
    "DVB_SUB",
    "EMBEDDED",
    "IMSC",
    "NULL_SOURCE",
    "SCC",
    "SCTE20",
    "SMI",
    "SMPTE_TT",
    "SRT",
    "STL",
    "TELETEXT",
    "TTML",
    "WEBVTT",
]
CaptionSourceUpconvertSTLToTeletextType = Literal["DISABLED", "UPCONVERT"]
ChromaPositionModeType = Literal["AUTO", "FORCE_CENTER", "FORCE_TOP_LEFT"]
CmafClientCacheType = Literal["DISABLED", "ENABLED"]
CmafCodecSpecificationType = Literal["RFC_4281", "RFC_6381"]
CmafEncryptionTypeType = Literal["AES_CTR", "SAMPLE_AES"]
CmafImageBasedTrickPlayType = Literal["ADVANCED", "NONE", "THUMBNAIL", "THUMBNAIL_AND_FULLFRAME"]
CmafInitializationVectorInManifestType = Literal["EXCLUDE", "INCLUDE"]
CmafIntervalCadenceType = Literal["FOLLOW_CUSTOM", "FOLLOW_IFRAME"]
CmafKeyProviderTypeType = Literal["SPEKE", "STATIC_KEY"]
CmafManifestCompressionType = Literal["GZIP", "NONE"]
CmafManifestDurationFormatType = Literal["FLOATING_POINT", "INTEGER"]
CmafMpdManifestBandwidthTypeType = Literal["AVERAGE", "MAX"]
CmafMpdProfileType = Literal["MAIN_PROFILE", "ON_DEMAND_PROFILE"]
CmafPtsOffsetHandlingForBFramesType = Literal["MATCH_INITIAL_PTS", "ZERO_BASED"]
CmafSegmentControlType = Literal["SEGMENTED_FILES", "SINGLE_FILE"]
CmafSegmentLengthControlType = Literal["EXACT", "GOP_MULTIPLE", "MATCH"]
CmafStreamInfResolutionType = Literal["EXCLUDE", "INCLUDE"]
CmafTargetDurationCompatibilityModeType = Literal["LEGACY", "SPEC_COMPLIANT"]
CmafVideoCompositionOffsetsType = Literal["SIGNED", "UNSIGNED"]
CmafWriteDASHManifestType = Literal["DISABLED", "ENABLED"]
CmafWriteHLSManifestType = Literal["DISABLED", "ENABLED"]
CmafWriteSegmentTimelineInRepresentationType = Literal["DISABLED", "ENABLED"]
CmfcAudioDurationType = Literal["DEFAULT_CODEC_DURATION", "MATCH_VIDEO_DURATION"]
CmfcAudioTrackTypeType = Literal[
    "ALTERNATE_AUDIO_AUTO_SELECT",
    "ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT",
    "ALTERNATE_AUDIO_NOT_AUTO_SELECT",
    "AUDIO_ONLY_VARIANT_STREAM",
]
CmfcDescriptiveVideoServiceFlagType = Literal["DONT_FLAG", "FLAG"]
CmfcIFrameOnlyManifestType = Literal["EXCLUDE", "INCLUDE"]
CmfcKlvMetadataType = Literal["NONE", "PASSTHROUGH"]
CmfcManifestMetadataSignalingType = Literal["DISABLED", "ENABLED"]
CmfcScte35EsamType = Literal["INSERT", "NONE"]
CmfcScte35SourceType = Literal["NONE", "PASSTHROUGH"]
CmfcTimedMetadataBoxVersionType = Literal["VERSION_0", "VERSION_1"]
CmfcTimedMetadataType = Literal["NONE", "PASSTHROUGH"]
CodecType = Literal[
    "AAC",
    "AC3",
    "AV1",
    "AVC",
    "C608",
    "C708",
    "EAC3",
    "FLAC",
    "HEVC",
    "MJPEG",
    "MP3",
    "MP4V",
    "MPEG2",
    "OPUS",
    "PCM",
    "PRORES",
    "THEORA",
    "UNKNOWN",
    "VORBIS",
    "VP8",
    "VP9",
    "WEBVTT",
]
ColorMetadataType = Literal["IGNORE", "INSERT"]
ColorPrimariesType = Literal[
    "EBU_3213_E",
    "GENERIC_FILM",
    "IPT",
    "ITU_2020",
    "ITU_470BG",
    "ITU_470M",
    "ITU_709",
    "LAST",
    "RESERVED",
    "SMPTE_170M",
    "SMPTE_2067XYZ",
    "SMPTE_240M",
    "SMPTE_428_1",
    "SMPTE_431_2",
    "SMPTE_EG_432_1",
    "UNSPECIFIED",
]
ColorSpaceConversionType = Literal[
    "FORCE_601",
    "FORCE_709",
    "FORCE_HDR10",
    "FORCE_HLG_2020",
    "FORCE_P3D65_HDR",
    "FORCE_P3D65_SDR",
    "FORCE_P3DCI",
    "NONE",
]
ColorSpaceType = Literal[
    "FOLLOW", "HDR10", "HLG_2020", "P3D65_HDR", "P3D65_SDR", "P3DCI", "REC_601", "REC_709"
]
ColorSpaceUsageType = Literal["FALLBACK", "FORCE"]
CommitmentType = Literal["ONE_YEAR"]
ContainerTypeType = Literal[
    "CMFC",
    "F4V",
    "GIF",
    "ISMV",
    "M2TS",
    "M3U8",
    "MOV",
    "MP4",
    "MPD",
    "MXF",
    "OGG",
    "RAW",
    "WEBM",
    "Y4M",
]
CopyProtectionActionType = Literal["PASSTHROUGH", "STRIP"]
DashIsoGroupAudioChannelConfigSchemeIdUriType = Literal[
    "DOLBY_CHANNEL_CONFIGURATION", "MPEG_CHANNEL_CONFIGURATION"
]
DashIsoHbbtvComplianceType = Literal["HBBTV_1_5", "NONE"]
DashIsoImageBasedTrickPlayType = Literal["ADVANCED", "NONE", "THUMBNAIL", "THUMBNAIL_AND_FULLFRAME"]
DashIsoIntervalCadenceType = Literal["FOLLOW_CUSTOM", "FOLLOW_IFRAME"]
DashIsoMpdManifestBandwidthTypeType = Literal["AVERAGE", "MAX"]
DashIsoMpdProfileType = Literal["MAIN_PROFILE", "ON_DEMAND_PROFILE"]
DashIsoPlaybackDeviceCompatibilityType = Literal["CENC_V1", "UNENCRYPTED_SEI"]
DashIsoPtsOffsetHandlingForBFramesType = Literal["MATCH_INITIAL_PTS", "ZERO_BASED"]
DashIsoSegmentControlType = Literal["SEGMENTED_FILES", "SINGLE_FILE"]
DashIsoSegmentLengthControlType = Literal["EXACT", "GOP_MULTIPLE", "MATCH"]
DashIsoVideoCompositionOffsetsType = Literal["SIGNED", "UNSIGNED"]
DashIsoWriteSegmentTimelineInRepresentationType = Literal["DISABLED", "ENABLED"]
DashManifestStyleType = Literal["BASIC", "COMPACT", "DISTINCT"]
DecryptionModeType = Literal["AES_CBC", "AES_CTR", "AES_GCM"]
DeinterlaceAlgorithmType = Literal[
    "BLEND", "BLEND_TICKER", "INTERPOLATE", "INTERPOLATE_TICKER", "LINEAR_INTERPOLATION"
]
DeinterlacerControlType = Literal["FORCE_ALL_FRAMES", "NORMAL"]
DeinterlacerModeType = Literal["ADAPTIVE", "DEINTERLACE", "INVERSE_TELECINE"]
DescribeEndpointsModeType = Literal["DEFAULT", "GET_ONLY"]
DescribeEndpointsPaginatorName = Literal["describe_endpoints"]
DolbyVisionLevel6ModeType = Literal["PASSTHROUGH", "RECALCULATE", "SPECIFY"]
DolbyVisionMappingType = Literal["HDR10_1000", "HDR10_NOMAP"]
DolbyVisionProfileType = Literal["PROFILE_5", "PROFILE_8_1"]
DropFrameTimecodeType = Literal["DISABLED", "ENABLED"]
DvbSubSubtitleFallbackFontType = Literal[
    "BEST_MATCH",
    "MONOSPACED_SANSSERIF",
    "MONOSPACED_SERIF",
    "PROPORTIONAL_SANSSERIF",
    "PROPORTIONAL_SERIF",
]
DvbSubtitleAlignmentType = Literal["AUTO", "CENTERED", "LEFT"]
DvbSubtitleApplyFontColorType = Literal["ALL_TEXT", "WHITE_TEXT_ONLY"]
DvbSubtitleBackgroundColorType = Literal["AUTO", "BLACK", "NONE", "WHITE"]
DvbSubtitleFontColorType = Literal[
    "AUTO", "BLACK", "BLUE", "GREEN", "HEX", "RED", "WHITE", "YELLOW"
]
DvbSubtitleOutlineColorType = Literal["AUTO", "BLACK", "BLUE", "GREEN", "RED", "WHITE", "YELLOW"]
DvbSubtitleShadowColorType = Literal["AUTO", "BLACK", "NONE", "WHITE"]
DvbSubtitleStylePassthroughType = Literal["DISABLED", "ENABLED"]
DvbSubtitleTeletextSpacingType = Literal["AUTO", "FIXED_GRID", "PROPORTIONAL"]
DvbSubtitlingTypeType = Literal["HEARING_IMPAIRED", "STANDARD"]
DvbddsHandlingType = Literal["NONE", "NO_DISPLAY_WINDOW", "SPECIFIED"]
DynamicAudioSelectorTypeType = Literal["ALL_TRACKS", "LANGUAGE_CODE"]
Eac3AtmosBitstreamModeType = Literal["COMPLETE_MAIN"]
Eac3AtmosCodingModeType = Literal[
    "CODING_MODE_5_1_4", "CODING_MODE_7_1_4", "CODING_MODE_9_1_6", "CODING_MODE_AUTO"
]
Eac3AtmosDialogueIntelligenceType = Literal["DISABLED", "ENABLED"]
Eac3AtmosDownmixControlType = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
Eac3AtmosDynamicRangeCompressionLineType = Literal[
    "FILM_LIGHT", "FILM_STANDARD", "MUSIC_LIGHT", "MUSIC_STANDARD", "NONE", "SPEECH"
]
Eac3AtmosDynamicRangeCompressionRfType = Literal[
    "FILM_LIGHT", "FILM_STANDARD", "MUSIC_LIGHT", "MUSIC_STANDARD", "NONE", "SPEECH"
]
Eac3AtmosDynamicRangeControlType = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
Eac3AtmosMeteringModeType = Literal[
    "ITU_BS_1770_1", "ITU_BS_1770_2", "ITU_BS_1770_3", "ITU_BS_1770_4", "LEQ_A"
]
Eac3AtmosStereoDownmixType = Literal["DPL2", "NOT_INDICATED", "STEREO", "SURROUND"]
Eac3AtmosSurroundExModeType = Literal["DISABLED", "ENABLED", "NOT_INDICATED"]
Eac3AttenuationControlType = Literal["ATTENUATE_3_DB", "NONE"]
Eac3BitstreamModeType = Literal[
    "COMMENTARY", "COMPLETE_MAIN", "EMERGENCY", "HEARING_IMPAIRED", "VISUALLY_IMPAIRED"
]
Eac3CodingModeType = Literal["CODING_MODE_1_0", "CODING_MODE_2_0", "CODING_MODE_3_2"]
Eac3DcFilterType = Literal["DISABLED", "ENABLED"]
Eac3DynamicRangeCompressionLineType = Literal[
    "FILM_LIGHT", "FILM_STANDARD", "MUSIC_LIGHT", "MUSIC_STANDARD", "NONE", "SPEECH"
]
Eac3DynamicRangeCompressionRfType = Literal[
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
EmbeddedConvert608To708Type = Literal["DISABLED", "UPCONVERT"]
EmbeddedTerminateCaptionsType = Literal["DISABLED", "END_OF_INPUT"]
EmbeddedTimecodeOverrideType = Literal["NONE", "USE_MDPM"]
F4vMoovPlacementType = Literal["NORMAL", "PROGRESSIVE_DOWNLOAD"]
FileSourceConvert608To708Type = Literal["DISABLED", "UPCONVERT"]
FileSourceTimeDeltaUnitsType = Literal["MILLISECONDS", "SECONDS"]
FontScriptType = Literal["AUTOMATIC", "HANS", "HANT"]
FormatType = Literal["matroska", "mp4", "quicktime", "webm"]
FrameMetricTypeType = Literal["MS_SSIM", "PSNR", "PSNR_HVS", "QVBR", "SSIM", "VMAF"]
GifFramerateControlType = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
GifFramerateConversionAlgorithmType = Literal["DUPLICATE_DROP", "INTERPOLATE"]
H264AdaptiveQuantizationType = Literal["AUTO", "HIGH", "HIGHER", "LOW", "MAX", "MEDIUM", "OFF"]
H264CodecLevelType = Literal[
    "AUTO",
    "LEVEL_1",
    "LEVEL_1_1",
    "LEVEL_1_2",
    "LEVEL_1_3",
    "LEVEL_2",
    "LEVEL_2_1",
    "LEVEL_2_2",
    "LEVEL_3",
    "LEVEL_3_1",
    "LEVEL_3_2",
    "LEVEL_4",
    "LEVEL_4_1",
    "LEVEL_4_2",
    "LEVEL_5",
    "LEVEL_5_1",
    "LEVEL_5_2",
]
H264CodecProfileType = Literal[
    "BASELINE", "HIGH", "HIGH_10BIT", "HIGH_422", "HIGH_422_10BIT", "MAIN"
]
H264DynamicSubGopType = Literal["ADAPTIVE", "STATIC"]
H264EndOfStreamMarkersType = Literal["INCLUDE", "SUPPRESS"]
H264EntropyEncodingType = Literal["CABAC", "CAVLC"]
H264FieldEncodingType = Literal["FORCE_FIELD", "MBAFF", "PAFF"]
H264FlickerAdaptiveQuantizationType = Literal["DISABLED", "ENABLED"]
H264FramerateControlType = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
H264FramerateConversionAlgorithmType = Literal[
    "DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE", "MAINTAIN_FRAME_COUNT"
]
H264GopBReferenceType = Literal["DISABLED", "ENABLED"]
H264GopSizeUnitsType = Literal["AUTO", "FRAMES", "SECONDS"]
H264InterlaceModeType = Literal[
    "BOTTOM_FIELD", "FOLLOW_BOTTOM_FIELD", "FOLLOW_TOP_FIELD", "PROGRESSIVE", "TOP_FIELD"
]
H264ParControlType = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
H264QualityTuningLevelType = Literal["MULTI_PASS_HQ", "SINGLE_PASS", "SINGLE_PASS_HQ"]
H264RateControlModeType = Literal["CBR", "QVBR", "VBR"]
H264RepeatPpsType = Literal["DISABLED", "ENABLED"]
H264SaliencyAwareEncodingType = Literal["DISABLED", "PREFERRED"]
H264ScanTypeConversionModeType = Literal["INTERLACED", "INTERLACED_OPTIMIZE"]
H264SceneChangeDetectType = Literal["DISABLED", "ENABLED", "TRANSITION_DETECTION"]
H264SlowPalType = Literal["DISABLED", "ENABLED"]
H264SpatialAdaptiveQuantizationType = Literal["DISABLED", "ENABLED"]
H264SyntaxType = Literal["DEFAULT", "RP2027"]
H264TelecineType = Literal["HARD", "NONE", "SOFT"]
H264TemporalAdaptiveQuantizationType = Literal["DISABLED", "ENABLED"]
H264UnregisteredSeiTimecodeType = Literal["DISABLED", "ENABLED"]
H264WriteMp4PackagingTypeType = Literal["AVC1", "AVC3"]
H265AdaptiveQuantizationType = Literal["AUTO", "HIGH", "HIGHER", "LOW", "MAX", "MEDIUM", "OFF"]
H265AlternateTransferFunctionSeiType = Literal["DISABLED", "ENABLED"]
H265CodecLevelType = Literal[
    "AUTO",
    "LEVEL_1",
    "LEVEL_2",
    "LEVEL_2_1",
    "LEVEL_3",
    "LEVEL_3_1",
    "LEVEL_4",
    "LEVEL_4_1",
    "LEVEL_5",
    "LEVEL_5_1",
    "LEVEL_5_2",
    "LEVEL_6",
    "LEVEL_6_1",
    "LEVEL_6_2",
]
H265CodecProfileType = Literal[
    "MAIN10_HIGH",
    "MAIN10_MAIN",
    "MAIN_422_10BIT_HIGH",
    "MAIN_422_10BIT_MAIN",
    "MAIN_422_8BIT_HIGH",
    "MAIN_422_8BIT_MAIN",
    "MAIN_HIGH",
    "MAIN_MAIN",
]
H265DeblockingType = Literal["DISABLED", "ENABLED"]
H265DynamicSubGopType = Literal["ADAPTIVE", "STATIC"]
H265EndOfStreamMarkersType = Literal["INCLUDE", "SUPPRESS"]
H265FlickerAdaptiveQuantizationType = Literal["DISABLED", "ENABLED"]
H265FramerateControlType = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
H265FramerateConversionAlgorithmType = Literal[
    "DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE", "MAINTAIN_FRAME_COUNT"
]
H265GopBReferenceType = Literal["DISABLED", "ENABLED"]
H265GopSizeUnitsType = Literal["AUTO", "FRAMES", "SECONDS"]
H265InterlaceModeType = Literal[
    "BOTTOM_FIELD", "FOLLOW_BOTTOM_FIELD", "FOLLOW_TOP_FIELD", "PROGRESSIVE", "TOP_FIELD"
]
H265ParControlType = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
H265QualityTuningLevelType = Literal["MULTI_PASS_HQ", "SINGLE_PASS", "SINGLE_PASS_HQ"]
H265RateControlModeType = Literal["CBR", "QVBR", "VBR"]
H265SampleAdaptiveOffsetFilterModeType = Literal["ADAPTIVE", "DEFAULT", "OFF"]
H265ScanTypeConversionModeType = Literal["INTERLACED", "INTERLACED_OPTIMIZE"]
H265SceneChangeDetectType = Literal["DISABLED", "ENABLED", "TRANSITION_DETECTION"]
H265SlowPalType = Literal["DISABLED", "ENABLED"]
H265SpatialAdaptiveQuantizationType = Literal["DISABLED", "ENABLED"]
H265TelecineType = Literal["HARD", "NONE", "SOFT"]
H265TemporalAdaptiveQuantizationType = Literal["DISABLED", "ENABLED"]
H265TemporalIdsType = Literal["DISABLED", "ENABLED"]
H265TilesType = Literal["DISABLED", "ENABLED"]
H265UnregisteredSeiTimecodeType = Literal["DISABLED", "ENABLED"]
H265WriteMp4PackagingTypeType = Literal["HEV1", "HVC1"]
HDRToSDRToneMapperType = Literal["PRESERVE_DETAILS", "VIBRANT"]
HlsAdMarkersType = Literal["ELEMENTAL", "ELEMENTAL_SCTE35"]
HlsAudioOnlyContainerType = Literal["AUTOMATIC", "M2TS"]
HlsAudioOnlyHeaderType = Literal["EXCLUDE", "INCLUDE"]
HlsAudioTrackTypeType = Literal[
    "ALTERNATE_AUDIO_AUTO_SELECT",
    "ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT",
    "ALTERNATE_AUDIO_NOT_AUTO_SELECT",
    "AUDIO_ONLY_VARIANT_STREAM",
]
HlsCaptionLanguageSettingType = Literal["INSERT", "NONE", "OMIT"]
HlsCaptionSegmentLengthControlType = Literal["LARGE_SEGMENTS", "MATCH_VIDEO"]
HlsClientCacheType = Literal["DISABLED", "ENABLED"]
HlsCodecSpecificationType = Literal["RFC_4281", "RFC_6381"]
HlsDescriptiveVideoServiceFlagType = Literal["DONT_FLAG", "FLAG"]
HlsDirectoryStructureType = Literal["SINGLE_DIRECTORY", "SUBDIRECTORY_PER_STREAM"]
HlsEncryptionTypeType = Literal["AES128", "SAMPLE_AES"]
HlsIFrameOnlyManifestType = Literal["EXCLUDE", "INCLUDE"]
HlsImageBasedTrickPlayType = Literal["ADVANCED", "NONE", "THUMBNAIL", "THUMBNAIL_AND_FULLFRAME"]
HlsInitializationVectorInManifestType = Literal["EXCLUDE", "INCLUDE"]
HlsIntervalCadenceType = Literal["FOLLOW_CUSTOM", "FOLLOW_IFRAME"]
HlsKeyProviderTypeType = Literal["SPEKE", "STATIC_KEY"]
HlsManifestCompressionType = Literal["GZIP", "NONE"]
HlsManifestDurationFormatType = Literal["FLOATING_POINT", "INTEGER"]
HlsOfflineEncryptedType = Literal["DISABLED", "ENABLED"]
HlsOutputSelectionType = Literal["MANIFESTS_AND_SEGMENTS", "SEGMENTS_ONLY"]
HlsProgramDateTimeType = Literal["EXCLUDE", "INCLUDE"]
HlsProgressiveWriteHlsManifestType = Literal["DISABLED", "ENABLED"]
HlsSegmentControlType = Literal["SEGMENTED_FILES", "SINGLE_FILE"]
HlsSegmentLengthControlType = Literal["EXACT", "GOP_MULTIPLE", "MATCH"]
HlsStreamInfResolutionType = Literal["EXCLUDE", "INCLUDE"]
HlsTargetDurationCompatibilityModeType = Literal["LEGACY", "SPEC_COMPLIANT"]
HlsTimedMetadataId3FrameType = Literal["NONE", "PRIV", "TDRL"]
ImscAccessibilitySubsType = Literal["DISABLED", "ENABLED"]
ImscStylePassthroughType = Literal["DISABLED", "ENABLED"]
InputDeblockFilterType = Literal["DISABLED", "ENABLED"]
InputDenoiseFilterType = Literal["DISABLED", "ENABLED"]
InputFilterEnableType = Literal["AUTO", "DISABLE", "FORCE"]
InputPolicyType = Literal["ALLOWED", "DISALLOWED"]
InputPsiControlType = Literal["IGNORE_PSI", "USE_PSI"]
InputRotateType = Literal["AUTO", "DEGREES_180", "DEGREES_270", "DEGREES_90", "DEGREE_0"]
InputSampleRangeType = Literal["FOLLOW", "FULL_RANGE", "LIMITED_RANGE"]
InputScanTypeType = Literal["AUTO", "PSF"]
InputTimecodeSourceType = Literal["EMBEDDED", "SPECIFIEDSTART", "ZEROBASED"]
JobPhaseType = Literal["PROBING", "TRANSCODING", "UPLOADING"]
JobStatusType = Literal["CANCELED", "COMPLETE", "ERROR", "PROGRESSING", "SUBMITTED"]
JobTemplateListByType = Literal["CREATION_DATE", "NAME", "SYSTEM"]
LanguageCodeType = Literal[
    "AAR",
    "ABK",
    "AFR",
    "AKA",
    "AMH",
    "ARA",
    "ARG",
    "ASM",
    "AVA",
    "AVE",
    "AYM",
    "AZE",
    "BAK",
    "BAM",
    "BEL",
    "BEN",
    "BIH",
    "BIS",
    "BOD",
    "BOS",
    "BRE",
    "BUL",
    "CAT",
    "CES",
    "CHA",
    "CHE",
    "CHU",
    "CHV",
    "COR",
    "COS",
    "CRE",
    "CYM",
    "DAN",
    "DEU",
    "DIV",
    "DZO",
    "ELL",
    "ENG",
    "ENM",
    "EPO",
    "EST",
    "EUS",
    "EWE",
    "FAO",
    "FAS",
    "FIJ",
    "FIN",
    "FRA",
    "FRM",
    "FRY",
    "FUL",
    "GER",
    "GLA",
    "GLE",
    "GLG",
    "GLV",
    "GRN",
    "GUJ",
    "HAT",
    "HAU",
    "HEB",
    "HER",
    "HIN",
    "HMO",
    "HRV",
    "HUN",
    "HYE",
    "IBO",
    "IDO",
    "III",
    "IKU",
    "ILE",
    "INA",
    "IND",
    "IPK",
    "ISL",
    "ITA",
    "JAV",
    "JPN",
    "KAL",
    "KAN",
    "KAS",
    "KAT",
    "KAU",
    "KAZ",
    "KHM",
    "KIK",
    "KIN",
    "KIR",
    "KOM",
    "KON",
    "KOR",
    "KUA",
    "KUR",
    "LAO",
    "LAT",
    "LAV",
    "LIM",
    "LIN",
    "LIT",
    "LTZ",
    "LUB",
    "LUG",
    "MAH",
    "MAL",
    "MAR",
    "MKD",
    "MLG",
    "MLT",
    "MON",
    "MRI",
    "MSA",
    "MYA",
    "NAU",
    "NAV",
    "NBL",
    "NDE",
    "NDO",
    "NEP",
    "NLD",
    "NNO",
    "NOB",
    "NOR",
    "NYA",
    "OCI",
    "OJI",
    "ORI",
    "ORJ",
    "ORM",
    "OSS",
    "PAN",
    "PLI",
    "POL",
    "POR",
    "PUS",
    "QAA",
    "QPC",
    "QUE",
    "ROH",
    "RON",
    "RUN",
    "RUS",
    "SAG",
    "SAN",
    "SIN",
    "SLK",
    "SLV",
    "SME",
    "SMO",
    "SNA",
    "SND",
    "SOM",
    "SOT",
    "SPA",
    "SQI",
    "SRB",
    "SRD",
    "SRP",
    "SSW",
    "SUN",
    "SWA",
    "SWE",
    "TAH",
    "TAM",
    "TAT",
    "TEL",
    "TGK",
    "TGL",
    "THA",
    "TIR",
    "TNG",
    "TON",
    "TSN",
    "TSO",
    "TUK",
    "TUR",
    "TWI",
    "UIG",
    "UKR",
    "URD",
    "UZB",
    "VEN",
    "VIE",
    "VOL",
    "WLN",
    "WOL",
    "XHO",
    "YID",
    "YOR",
    "ZHA",
    "ZHO",
    "ZUL",
]
ListJobTemplatesPaginatorName = Literal["list_job_templates"]
ListJobsPaginatorName = Literal["list_jobs"]
ListPresetsPaginatorName = Literal["list_presets"]
ListQueuesPaginatorName = Literal["list_queues"]
ListVersionsPaginatorName = Literal["list_versions"]
M2tsAudioBufferModelType = Literal["ATSC", "DVB"]
M2tsAudioDurationType = Literal["DEFAULT_CODEC_DURATION", "MATCH_VIDEO_DURATION"]
M2tsBufferModelType = Literal["MULTIPLEX", "NONE"]
M2tsDataPtsControlType = Literal["ALIGN_TO_VIDEO", "AUTO"]
M2tsEbpAudioIntervalType = Literal["VIDEO_AND_FIXED_INTERVALS", "VIDEO_INTERVAL"]
M2tsEbpPlacementType = Literal["VIDEO_AND_AUDIO_PIDS", "VIDEO_PID"]
M2tsEsRateInPesType = Literal["EXCLUDE", "INCLUDE"]
M2tsForceTsVideoEbpOrderType = Literal["DEFAULT", "FORCE"]
M2tsKlvMetadataType = Literal["NONE", "PASSTHROUGH"]
M2tsNielsenId3Type = Literal["INSERT", "NONE"]
M2tsPcrControlType = Literal["CONFIGURED_PCR_PERIOD", "PCR_EVERY_PES_PACKET"]
M2tsPreventBufferUnderflowType = Literal["DISABLED", "ENABLED"]
M2tsRateModeType = Literal["CBR", "VBR"]
M2tsScte35SourceType = Literal["NONE", "PASSTHROUGH"]
M2tsSegmentationMarkersType = Literal[
    "EBP", "EBP_LEGACY", "NONE", "PSI_SEGSTART", "RAI_ADAPT", "RAI_SEGSTART"
]
M2tsSegmentationStyleType = Literal["MAINTAIN_CADENCE", "RESET_CADENCE"]
M3u8AudioDurationType = Literal["DEFAULT_CODEC_DURATION", "MATCH_VIDEO_DURATION"]
M3u8DataPtsControlType = Literal["ALIGN_TO_VIDEO", "AUTO"]
M3u8NielsenId3Type = Literal["INSERT", "NONE"]
M3u8PcrControlType = Literal["CONFIGURED_PCR_PERIOD", "PCR_EVERY_PES_PACKET"]
M3u8Scte35SourceType = Literal["NONE", "PASSTHROUGH"]
MatrixCoefficientsType = Literal[
    "CD_CL",
    "CD_NCL",
    "EBU3213",
    "FCC",
    "IPT",
    "ITU_2020_CL",
    "ITU_2020_NCL",
    "ITU_2100ICtCp",
    "ITU_470BG",
    "ITU_709",
    "LAST",
    "RESERVED",
    "RGB",
    "SMPTE_170M",
    "SMPTE_2085",
    "SMPTE_240M",
    "UNSPECIFIED",
    "YCgCo",
]
MotionImageInsertionModeType = Literal["MOV", "PNG"]
MotionImagePlaybackType = Literal["ONCE", "REPEAT"]
MovClapAtomType = Literal["EXCLUDE", "INCLUDE"]
MovCslgAtomType = Literal["EXCLUDE", "INCLUDE"]
MovMpeg2FourCCControlType = Literal["MPEG", "XDCAM"]
MovPaddingControlType = Literal["NONE", "OMNEON"]
MovReferenceType = Literal["EXTERNAL", "SELF_CONTAINED"]
Mp3RateControlModeType = Literal["CBR", "VBR"]
Mp4CslgAtomType = Literal["EXCLUDE", "INCLUDE"]
Mp4FreeSpaceBoxType = Literal["EXCLUDE", "INCLUDE"]
Mp4MoovPlacementType = Literal["NORMAL", "PROGRESSIVE_DOWNLOAD"]
MpdAccessibilityCaptionHintsType = Literal["EXCLUDE", "INCLUDE"]
MpdAudioDurationType = Literal["DEFAULT_CODEC_DURATION", "MATCH_VIDEO_DURATION"]
MpdCaptionContainerTypeType = Literal["FRAGMENTED_MP4", "RAW"]
MpdKlvMetadataType = Literal["NONE", "PASSTHROUGH"]
MpdManifestMetadataSignalingType = Literal["DISABLED", "ENABLED"]
MpdScte35EsamType = Literal["INSERT", "NONE"]
MpdScte35SourceType = Literal["NONE", "PASSTHROUGH"]
MpdTimedMetadataBoxVersionType = Literal["VERSION_0", "VERSION_1"]
MpdTimedMetadataType = Literal["NONE", "PASSTHROUGH"]
Mpeg2AdaptiveQuantizationType = Literal["HIGH", "LOW", "MEDIUM", "OFF"]
Mpeg2CodecLevelType = Literal["AUTO", "HIGH", "HIGH1440", "LOW", "MAIN"]
Mpeg2CodecProfileType = Literal["MAIN", "PROFILE_422"]
Mpeg2DynamicSubGopType = Literal["ADAPTIVE", "STATIC"]
Mpeg2FramerateControlType = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
Mpeg2FramerateConversionAlgorithmType = Literal[
    "DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE", "MAINTAIN_FRAME_COUNT"
]
Mpeg2GopSizeUnitsType = Literal["FRAMES", "SECONDS"]
Mpeg2InterlaceModeType = Literal[
    "BOTTOM_FIELD", "FOLLOW_BOTTOM_FIELD", "FOLLOW_TOP_FIELD", "PROGRESSIVE", "TOP_FIELD"
]
Mpeg2IntraDcPrecisionType = Literal[
    "AUTO",
    "INTRA_DC_PRECISION_10",
    "INTRA_DC_PRECISION_11",
    "INTRA_DC_PRECISION_8",
    "INTRA_DC_PRECISION_9",
]
Mpeg2ParControlType = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
Mpeg2QualityTuningLevelType = Literal["MULTI_PASS", "SINGLE_PASS"]
Mpeg2RateControlModeType = Literal["CBR", "VBR"]
Mpeg2ScanTypeConversionModeType = Literal["INTERLACED", "INTERLACED_OPTIMIZE"]
Mpeg2SceneChangeDetectType = Literal["DISABLED", "ENABLED"]
Mpeg2SlowPalType = Literal["DISABLED", "ENABLED"]
Mpeg2SpatialAdaptiveQuantizationType = Literal["DISABLED", "ENABLED"]
Mpeg2SyntaxType = Literal["DEFAULT", "D_10"]
Mpeg2TelecineType = Literal["HARD", "NONE", "SOFT"]
Mpeg2TemporalAdaptiveQuantizationType = Literal["DISABLED", "ENABLED"]
MsSmoothAudioDeduplicationType = Literal["COMBINE_DUPLICATE_STREAMS", "NONE"]
MsSmoothFragmentLengthControlType = Literal["EXACT", "GOP_MULTIPLE"]
MsSmoothManifestEncodingType = Literal["UTF16", "UTF8"]
MxfAfdSignalingType = Literal["COPY_FROM_VIDEO", "NO_COPY"]
MxfProfileType = Literal["D_10", "OP1A", "XAVC", "XDCAM", "XDCAM_RDD9"]
MxfXavcDurationModeType = Literal["ALLOW_ANY_DURATION", "DROP_FRAMES_FOR_COMPLIANCE"]
NielsenActiveWatermarkProcessTypeType = Literal["CBET", "NAES2_AND_NW", "NAES2_AND_NW_AND_CBET"]
NielsenSourceWatermarkStatusTypeType = Literal["CLEAN", "WATERMARKED"]
NielsenUniqueTicPerAudioTrackTypeType = Literal[
    "RESERVE_UNIQUE_TICS_PER_TRACK", "SAME_TICS_PER_TRACK"
]
NoiseFilterPostTemporalSharpeningStrengthType = Literal["HIGH", "LOW", "MEDIUM"]
NoiseFilterPostTemporalSharpeningType = Literal["AUTO", "DISABLED", "ENABLED"]
NoiseReducerFilterType = Literal[
    "BILATERAL", "CONSERVE", "GAUSSIAN", "LANCZOS", "MEAN", "SHARPEN", "SPATIAL", "TEMPORAL"
]
OrderType = Literal["ASCENDING", "DESCENDING"]
OutputGroupTypeType = Literal[
    "CMAF_GROUP_SETTINGS",
    "DASH_ISO_GROUP_SETTINGS",
    "FILE_GROUP_SETTINGS",
    "HLS_GROUP_SETTINGS",
    "MS_SMOOTH_GROUP_SETTINGS",
]
OutputSdtType = Literal["SDT_FOLLOW", "SDT_FOLLOW_IF_PRESENT", "SDT_MANUAL", "SDT_NONE"]
PadVideoType = Literal["BLACK", "DISABLED"]
PresetListByType = Literal["CREATION_DATE", "NAME", "SYSTEM"]
PresetSpeke20AudioType = Literal[
    "PRESET_AUDIO_1", "PRESET_AUDIO_2", "PRESET_AUDIO_3", "SHARED", "UNENCRYPTED"
]
PresetSpeke20VideoType = Literal[
    "PRESET_VIDEO_1",
    "PRESET_VIDEO_2",
    "PRESET_VIDEO_3",
    "PRESET_VIDEO_4",
    "PRESET_VIDEO_5",
    "PRESET_VIDEO_6",
    "PRESET_VIDEO_7",
    "PRESET_VIDEO_8",
    "SHARED",
    "UNENCRYPTED",
]
PricingPlanType = Literal["ON_DEMAND", "RESERVED"]
ProresChromaSamplingType = Literal["PRESERVE_444_SAMPLING", "SUBSAMPLE_TO_422"]
ProresCodecProfileType = Literal[
    "APPLE_PRORES_422",
    "APPLE_PRORES_422_HQ",
    "APPLE_PRORES_422_LT",
    "APPLE_PRORES_422_PROXY",
    "APPLE_PRORES_4444",
    "APPLE_PRORES_4444_XQ",
]
ProresFramerateControlType = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
ProresFramerateConversionAlgorithmType = Literal[
    "DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE", "MAINTAIN_FRAME_COUNT"
]
ProresInterlaceModeType = Literal[
    "BOTTOM_FIELD", "FOLLOW_BOTTOM_FIELD", "FOLLOW_TOP_FIELD", "PROGRESSIVE", "TOP_FIELD"
]
ProresParControlType = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
ProresScanTypeConversionModeType = Literal["INTERLACED", "INTERLACED_OPTIMIZE"]
ProresSlowPalType = Literal["DISABLED", "ENABLED"]
ProresTelecineType = Literal["HARD", "NONE"]
QueueListByType = Literal["CREATION_DATE", "NAME"]
QueueStatusType = Literal["ACTIVE", "PAUSED"]
RemoveRubyReserveAttributesType = Literal["DISABLED", "ENABLED"]
RenewalTypeType = Literal["AUTO_RENEW", "EXPIRE"]
RequiredFlagType = Literal["DISABLED", "ENABLED"]
ReservationPlanStatusType = Literal["ACTIVE", "EXPIRED"]
RespondToAfdType = Literal["NONE", "PASSTHROUGH", "RESPOND"]
RuleTypeType = Literal[
    "ALLOWED_RENDITIONS",
    "FORCE_INCLUDE_RENDITIONS",
    "MIN_BOTTOM_RENDITION_SIZE",
    "MIN_TOP_RENDITION_SIZE",
]
S3ObjectCannedAclType = Literal[
    "AUTHENTICATED_READ", "BUCKET_OWNER_FULL_CONTROL", "BUCKET_OWNER_READ", "PUBLIC_READ"
]
S3ServerSideEncryptionTypeType = Literal["SERVER_SIDE_ENCRYPTION_KMS", "SERVER_SIDE_ENCRYPTION_S3"]
S3StorageClassType = Literal[
    "DEEP_ARCHIVE",
    "GLACIER",
    "INTELLIGENT_TIERING",
    "ONEZONE_IA",
    "REDUCED_REDUNDANCY",
    "STANDARD",
    "STANDARD_IA",
]
SampleRangeConversionType = Literal["LIMITED_RANGE_CLIP", "LIMITED_RANGE_SQUEEZE", "NONE"]
ScalingBehaviorType = Literal["DEFAULT", "FILL", "FIT", "FIT_NO_UPSCALE", "STRETCH_TO_OUTPUT"]
SccDestinationFramerateType = Literal[
    "FRAMERATE_23_97",
    "FRAMERATE_24",
    "FRAMERATE_25",
    "FRAMERATE_29_97_DROPFRAME",
    "FRAMERATE_29_97_NON_DROPFRAME",
]
SearchJobsPaginatorName = Literal["search_jobs"]
SimulateReservedQueueType = Literal["DISABLED", "ENABLED"]
SrtStylePassthroughType = Literal["DISABLED", "ENABLED"]
StatusUpdateIntervalType = Literal[
    "SECONDS_10",
    "SECONDS_12",
    "SECONDS_120",
    "SECONDS_15",
    "SECONDS_180",
    "SECONDS_20",
    "SECONDS_240",
    "SECONDS_30",
    "SECONDS_300",
    "SECONDS_360",
    "SECONDS_420",
    "SECONDS_480",
    "SECONDS_540",
    "SECONDS_60",
    "SECONDS_600",
]
TeletextPageTypeType = Literal[
    "PAGE_TYPE_ADDL_INFO",
    "PAGE_TYPE_HEARING_IMPAIRED_SUBTITLE",
    "PAGE_TYPE_INITIAL",
    "PAGE_TYPE_PROGRAM_SCHEDULE",
    "PAGE_TYPE_SUBTITLE",
]
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
TimecodeSourceType = Literal["EMBEDDED", "SPECIFIEDSTART", "ZEROBASED"]
TimecodeTrackType = Literal["DISABLED", "ENABLED"]
TimedMetadataType = Literal["NONE", "PASSTHROUGH"]
TrackTypeType = Literal["audio", "data", "video"]
TransferCharacteristicsType = Literal[
    "ARIB_B67",
    "IEC_61966_2_1",
    "IEC_61966_2_4",
    "ITU_1361",
    "ITU_2020_10bit",
    "ITU_2020_12bit",
    "ITU_470BG",
    "ITU_470M",
    "ITU_709",
    "LAST",
    "LINEAR",
    "LOC10_2_5",
    "LOG10_2",
    "RESERVED",
    "SMPTE_170M",
    "SMPTE_2084",
    "SMPTE_240M",
    "SMPTE_428_1",
    "UNSPECIFIED",
]
TsPtsOffsetType = Literal["AUTO", "MILLISECONDS", "SECONDS"]
TtmlStylePassthroughType = Literal["DISABLED", "ENABLED"]
TypeType = Literal["CUSTOM", "SYSTEM"]
UncompressedFourccType = Literal["I420", "I422", "I444"]
UncompressedFramerateControlType = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
UncompressedFramerateConversionAlgorithmType = Literal[
    "DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE", "MAINTAIN_FRAME_COUNT"
]
UncompressedInterlaceModeType = Literal["INTERLACED", "PROGRESSIVE"]
UncompressedScanTypeConversionModeType = Literal["INTERLACED", "INTERLACED_OPTIMIZE"]
UncompressedSlowPalType = Literal["DISABLED", "ENABLED"]
UncompressedTelecineType = Literal["HARD", "NONE"]
Vc3ClassType = Literal["CLASS_145_8BIT", "CLASS_220_10BIT", "CLASS_220_8BIT"]
Vc3FramerateControlType = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
Vc3FramerateConversionAlgorithmType = Literal[
    "DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE", "MAINTAIN_FRAME_COUNT"
]
Vc3InterlaceModeType = Literal["INTERLACED", "PROGRESSIVE"]
Vc3ScanTypeConversionModeType = Literal["INTERLACED", "INTERLACED_OPTIMIZE"]
Vc3SlowPalType = Literal["DISABLED", "ENABLED"]
Vc3TelecineType = Literal["HARD", "NONE"]
VchipActionType = Literal["PASSTHROUGH", "STRIP"]
VideoCodecType = Literal[
    "AV1",
    "AVC_INTRA",
    "FRAME_CAPTURE",
    "GIF",
    "H_264",
    "H_265",
    "MPEG2",
    "PASSTHROUGH",
    "PRORES",
    "UNCOMPRESSED",
    "VC3",
    "VP8",
    "VP9",
    "XAVC",
]
VideoOverlayPlayBackModeType = Literal["ONCE", "REPEAT"]
VideoOverlayUnitType = Literal["PERCENTAGE", "PIXELS"]
VideoTimecodeInsertionType = Literal["DISABLED", "PIC_TIMING_SEI"]
Vp8FramerateControlType = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
Vp8FramerateConversionAlgorithmType = Literal[
    "DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE", "MAINTAIN_FRAME_COUNT"
]
Vp8ParControlType = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
Vp8QualityTuningLevelType = Literal["MULTI_PASS", "MULTI_PASS_HQ"]
Vp8RateControlModeType = Literal["VBR"]
Vp9FramerateControlType = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
Vp9FramerateConversionAlgorithmType = Literal[
    "DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE", "MAINTAIN_FRAME_COUNT"
]
Vp9ParControlType = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
Vp9QualityTuningLevelType = Literal["MULTI_PASS", "MULTI_PASS_HQ"]
Vp9RateControlModeType = Literal["VBR"]
WatermarkingStrengthType = Literal["DEFAULT", "LIGHTER", "LIGHTEST", "STRONGER", "STRONGEST"]
WavFormatType = Literal["EXTENSIBLE", "RF64", "RIFF"]
WebvttAccessibilitySubsType = Literal["DISABLED", "ENABLED"]
WebvttStylePassthroughType = Literal["DISABLED", "ENABLED", "MERGE", "STRICT"]
Xavc4kIntraCbgProfileClassType = Literal["CLASS_100", "CLASS_300", "CLASS_480"]
Xavc4kIntraVbrProfileClassType = Literal["CLASS_100", "CLASS_300", "CLASS_480"]
Xavc4kProfileBitrateClassType = Literal[
    "BITRATE_CLASS_100", "BITRATE_CLASS_140", "BITRATE_CLASS_200"
]
Xavc4kProfileCodecProfileType = Literal["HIGH", "HIGH_422"]
Xavc4kProfileQualityTuningLevelType = Literal["MULTI_PASS_HQ", "SINGLE_PASS", "SINGLE_PASS_HQ"]
XavcAdaptiveQuantizationType = Literal["AUTO", "HIGH", "HIGHER", "LOW", "MAX", "MEDIUM", "OFF"]
XavcEntropyEncodingType = Literal["AUTO", "CABAC", "CAVLC"]
XavcFlickerAdaptiveQuantizationType = Literal["DISABLED", "ENABLED"]
XavcFramerateControlType = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
XavcFramerateConversionAlgorithmType = Literal[
    "DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE", "MAINTAIN_FRAME_COUNT"
]
XavcGopBReferenceType = Literal["DISABLED", "ENABLED"]
XavcHdIntraCbgProfileClassType = Literal["CLASS_100", "CLASS_200", "CLASS_50"]
XavcHdProfileBitrateClassType = Literal["BITRATE_CLASS_25", "BITRATE_CLASS_35", "BITRATE_CLASS_50"]
XavcHdProfileQualityTuningLevelType = Literal["MULTI_PASS_HQ", "SINGLE_PASS", "SINGLE_PASS_HQ"]
XavcHdProfileTelecineType = Literal["HARD", "NONE"]
XavcInterlaceModeType = Literal[
    "BOTTOM_FIELD", "FOLLOW_BOTTOM_FIELD", "FOLLOW_TOP_FIELD", "PROGRESSIVE", "TOP_FIELD"
]
XavcProfileType = Literal[
    "XAVC_4K", "XAVC_4K_INTRA_CBG", "XAVC_4K_INTRA_VBR", "XAVC_HD", "XAVC_HD_INTRA_CBG"
]
XavcSlowPalType = Literal["DISABLED", "ENABLED"]
XavcSpatialAdaptiveQuantizationType = Literal["DISABLED", "ENABLED"]
XavcTemporalAdaptiveQuantizationType = Literal["DISABLED", "ENABLED"]
MediaConvertServiceName = Literal["mediaconvert"]
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
    "describe_endpoints",
    "list_job_templates",
    "list_jobs",
    "list_presets",
    "list_queues",
    "list_versions",
    "search_jobs",
]
RegionName = Literal[
    "af-south-1",
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-northeast-3",
    "ap-south-1",
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
    "us-west-1",
    "us-west-2",
]
