"""
Type annotations for quicksight service literal definitions.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_quicksight/literals/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from types_boto3_quicksight.literals import AggTypeType

    data: AggTypeType = "AVERAGE"
    ```
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AggTypeType",
    "AnalysisErrorTypeType",
    "AnalysisFilterAttributeType",
    "AnchorOptionType",
    "AnchorTypeType",
    "AnonymousUserDashboardEmbeddingConfigurationDisabledFeatureType",
    "AnonymousUserDashboardEmbeddingConfigurationEnabledFeatureType",
    "ArcThicknessOptionsType",
    "ArcThicknessType",
    "AssetBundleExportFormatType",
    "AssetBundleExportJobAnalysisPropertyToOverrideType",
    "AssetBundleExportJobDashboardPropertyToOverrideType",
    "AssetBundleExportJobDataSetPropertyToOverrideType",
    "AssetBundleExportJobDataSourcePropertyToOverrideType",
    "AssetBundleExportJobFolderPropertyToOverrideType",
    "AssetBundleExportJobRefreshSchedulePropertyToOverrideType",
    "AssetBundleExportJobStatusType",
    "AssetBundleExportJobThemePropertyToOverrideType",
    "AssetBundleExportJobVPCConnectionPropertyToOverrideType",
    "AssetBundleImportFailureActionType",
    "AssetBundleImportJobStatusType",
    "AssignmentStatusType",
    "AuthenticationMethodOptionType",
    "AuthenticationTypeType",
    "AuthorSpecifiedAggregationType",
    "AxisBindingType",
    "BarChartOrientationType",
    "BarsArrangementType",
    "BaseMapStyleTypeType",
    "BoxPlotFillStyleType",
    "BrandStatusType",
    "BrandVersionStatusType",
    "CapabilityStateType",
    "CategoricalAggregationFunctionType",
    "CategoryFilterFunctionType",
    "CategoryFilterMatchOperatorType",
    "CategoryFilterSelectAllOptionsType",
    "CategoryFilterTypeType",
    "ColorFillTypeType",
    "ColumnDataRoleType",
    "ColumnDataSubTypeType",
    "ColumnDataTypeType",
    "ColumnOrderingTypeType",
    "ColumnRoleType",
    "ColumnTagNameType",
    "CommitModeType",
    "ComparisonMethodType",
    "ComparisonMethodTypeType",
    "ConditionalFormattingIconDisplayOptionType",
    "ConditionalFormattingIconSetTypeType",
    "ConstantTypeType",
    "ContributionAnalysisDirectionType",
    "ContributionAnalysisSortTypeType",
    "CrossDatasetTypesType",
    "CustomContentImageScalingConfigurationType",
    "CustomContentTypeType",
    "DashboardBehaviorType",
    "DashboardErrorTypeType",
    "DashboardFilterAttributeType",
    "DashboardUIStateType",
    "DashboardsQAStatusType",
    "DataLabelContentType",
    "DataLabelOverlapType",
    "DataLabelPositionType",
    "DataSetFilterAttributeType",
    "DataSetImportModeType",
    "DataSetUseAsType",
    "DataSourceErrorInfoTypeType",
    "DataSourceFilterAttributeType",
    "DataSourceTypeType",
    "DatasetParameterValueTypeType",
    "DateAggregationFunctionType",
    "DayOfTheWeekType",
    "DayOfWeekType",
    "DefaultAggregationType",
    "DescribeFolderPermissionsPaginatorName",
    "DescribeFolderResolvedPermissionsPaginatorName",
    "DigitGroupingStyleType",
    "DisplayFormatType",
    "EditionType",
    "EmbeddingIdentityTypeType",
    "FileFormatType",
    "FilterClassType",
    "FilterNullOptionType",
    "FilterOperatorType",
    "FilterVisualScopeType",
    "FolderFilterAttributeType",
    "FolderTypeType",
    "FontDecorationType",
    "FontStyleType",
    "FontWeightNameType",
    "ForecastComputationSeasonalityType",
    "FunnelChartMeasureDataLabelStyleType",
    "GeneratedAnswerStatusType",
    "GeoSpatialCountryCodeType",
    "GeoSpatialDataRoleType",
    "GeospatialColorStateType",
    "GeospatialLayerTypeType",
    "GeospatialMapNavigationType",
    "GeospatialSelectedPointStyleType",
    "GroupFilterAttributeType",
    "GroupFilterOperatorType",
    "HistogramBinTypeType",
    "HorizontalTextAlignmentType",
    "IconType",
    "IdentityStoreType",
    "IdentityTypeType",
    "ImageCustomActionTriggerType",
    "IncludeFolderMembersType",
    "IncludeGeneratedAnswerType",
    "IncludeQuickSightQIndexType",
    "IngestionErrorTypeType",
    "IngestionRequestSourceType",
    "IngestionRequestTypeType",
    "IngestionStatusType",
    "IngestionTypeType",
    "InputColumnDataTypeType",
    "JoinTypeType",
    "KPISparklineTypeType",
    "KPIVisualStandardLayoutTypeType",
    "LayerCustomActionTriggerType",
    "LayoutElementTypeType",
    "LegendPositionType",
    "LineChartLineStyleType",
    "LineChartMarkerShapeType",
    "LineChartTypeType",
    "LineInterpolationType",
    "ListAnalysesPaginatorName",
    "ListAssetBundleExportJobsPaginatorName",
    "ListAssetBundleImportJobsPaginatorName",
    "ListBrandsPaginatorName",
    "ListCustomPermissionsPaginatorName",
    "ListDashboardVersionsPaginatorName",
    "ListDashboardsPaginatorName",
    "ListDataSetsPaginatorName",
    "ListDataSourcesPaginatorName",
    "ListFolderMembersPaginatorName",
    "ListFoldersForResourcePaginatorName",
    "ListFoldersPaginatorName",
    "ListGroupMembershipsPaginatorName",
    "ListGroupsPaginatorName",
    "ListIAMPolicyAssignmentsForUserPaginatorName",
    "ListIAMPolicyAssignmentsPaginatorName",
    "ListIngestionsPaginatorName",
    "ListNamespacesPaginatorName",
    "ListRoleMembershipsPaginatorName",
    "ListTemplateAliasesPaginatorName",
    "ListTemplateVersionsPaginatorName",
    "ListTemplatesPaginatorName",
    "ListThemeVersionsPaginatorName",
    "ListThemesPaginatorName",
    "ListUserGroupsPaginatorName",
    "ListUsersPaginatorName",
    "LookbackWindowSizeUnitType",
    "MapZoomModeType",
    "MaximumMinimumComputationTypeType",
    "MemberTypeType",
    "MissingDataTreatmentOptionType",
    "NamedEntityAggTypeType",
    "NamedFilterAggTypeType",
    "NamedFilterTypeType",
    "NamespaceErrorTypeType",
    "NamespaceStatusType",
    "NegativeValueDisplayModeType",
    "NetworkInterfaceStatusType",
    "NullFilterOptionType",
    "NumberScaleType",
    "NumericEqualityMatchOperatorType",
    "NumericFilterSelectAllOptionsType",
    "NumericSeparatorSymbolType",
    "OtherCategoriesType",
    "PaginatorName",
    "PanelBorderStyleType",
    "PaperOrientationType",
    "PaperSizeType",
    "ParameterValueTypeType",
    "PersonalizationModeType",
    "PivotTableConditionalFormattingScopeRoleType",
    "PivotTableDataPathTypeType",
    "PivotTableFieldCollapseStateType",
    "PivotTableMetricPlacementType",
    "PivotTableRowsLayoutType",
    "PivotTableSubtotalLevelType",
    "PluginVisualAxisNameType",
    "PrimaryValueDisplayTypeType",
    "PropertyRoleType",
    "PropertyUsageType",
    "PurchaseModeType",
    "QAResultTypeType",
    "QBusinessInsightsStatusType",
    "QSearchStatusType",
    "QueryExecutionModeType",
    "QuickSightServiceName",
    "RadarChartAxesRangeScaleType",
    "RadarChartShapeType",
    "ReferenceLineLabelHorizontalPositionType",
    "ReferenceLineLabelVerticalPositionType",
    "ReferenceLinePatternTypeType",
    "ReferenceLineSeriesTypeType",
    "ReferenceLineValueLabelRelativePositionType",
    "RefreshFailureAlertStatusType",
    "RefreshIntervalType",
    "RegionName",
    "RelativeDateTypeType",
    "RelativeFontSizeType",
    "ResizeOptionType",
    "ResourceServiceName",
    "ResourceStatusType",
    "ReviewedAnswerErrorCodeType",
    "RoleType",
    "RowLevelPermissionFormatVersionType",
    "RowLevelPermissionPolicyType",
    "SearchAnalysesPaginatorName",
    "SearchDashboardsPaginatorName",
    "SearchDataSetsPaginatorName",
    "SearchDataSourcesPaginatorName",
    "SearchFoldersPaginatorName",
    "SearchGroupsPaginatorName",
    "SearchTopicsPaginatorName",
    "SectionPageBreakStatusType",
    "SelectAllValueOptionsType",
    "SelectedFieldOptionsType",
    "SelectedTooltipTypeType",
    "ServiceName",
    "ServiceTypeType",
    "SharingModelType",
    "SheetContentTypeType",
    "SheetControlDateTimePickerTypeType",
    "SheetControlListTypeType",
    "SheetControlSliderTypeType",
    "SheetImageScalingTypeType",
    "SimpleAttributeAggregationFunctionType",
    "SimpleNumericalAggregationFunctionType",
    "SimpleTotalAggregationFunctionType",
    "SingleYAxisOptionType",
    "SmallMultiplesAxisPlacementType",
    "SmallMultiplesAxisScaleType",
    "SnapshotFileFormatTypeType",
    "SnapshotFileSheetSelectionScopeType",
    "SnapshotJobStatusType",
    "SortDirectionType",
    "SpecialValueType",
    "StarburstProductTypeType",
    "StatusType",
    "StyledCellTypeType",
    "TableBorderStyleType",
    "TableCellImageScalingConfigurationType",
    "TableFieldIconSetTypeType",
    "TableOrientationType",
    "TableTotalsPlacementType",
    "TableTotalsScrollStatusType",
    "TargetVisualOptionsType",
    "TemplateErrorTypeType",
    "TextQualifierType",
    "TextWrapType",
    "ThemeErrorTypeType",
    "ThemeTypeType",
    "TimeGranularityType",
    "TooltipTargetType",
    "TooltipTitleTypeType",
    "TopBottomComputationTypeType",
    "TopBottomSortOrderType",
    "TopicFilterAttributeType",
    "TopicFilterOperatorType",
    "TopicIRFilterFunctionType",
    "TopicIRFilterTypeType",
    "TopicNumericSeparatorSymbolType",
    "TopicRefreshStatusType",
    "TopicRelativeDateFilterFunctionType",
    "TopicScheduleTypeType",
    "TopicSortDirectionType",
    "TopicTimeGranularityType",
    "TopicUserExperienceVersionType",
    "TransposedColumnTypeType",
    "URLTargetConfigurationType",
    "UndefinedSpecifiedValueTypeType",
    "UserRoleType",
    "VPCConnectionAvailabilityStatusType",
    "VPCConnectionResourceStatusType",
    "ValidationStrategyModeType",
    "ValueWhenUnsetOptionType",
    "VerticalTextAlignmentType",
    "VisibilityType",
    "VisualCustomActionTriggerType",
    "VisualHighlightTriggerType",
    "VisualRoleType",
    "WidgetStatusType",
    "WordCloudCloudLayoutType",
    "WordCloudWordCasingType",
    "WordCloudWordOrientationType",
    "WordCloudWordPaddingType",
    "WordCloudWordScalingType",
)

AggTypeType = Literal[
    "AVERAGE",
    "COLUMN",
    "COUNT",
    "CUSTOM",
    "DISTINCT_COUNT",
    "MAX",
    "MEDIAN",
    "MIN",
    "PERCENTILE",
    "PTD_AVERAGE",
    "PTD_COUNT",
    "PTD_DISTINCT_COUNT",
    "PTD_MAX",
    "PTD_MIN",
    "PTD_SUM",
    "STDEV",
    "STDEVP",
    "SUM",
    "VAR",
    "VARP",
]
AnalysisErrorTypeType = Literal[
    "ACCESS_DENIED",
    "COLUMN_GEOGRAPHIC_ROLE_MISMATCH",
    "COLUMN_REPLACEMENT_MISSING",
    "COLUMN_TYPE_MISMATCH",
    "DATA_SET_NOT_FOUND",
    "INTERNAL_FAILURE",
    "PARAMETER_NOT_FOUND",
    "PARAMETER_TYPE_INVALID",
    "PARAMETER_VALUE_INCOMPATIBLE",
    "SOURCE_NOT_FOUND",
]
AnalysisFilterAttributeType = Literal[
    "ANALYSIS_NAME",
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
    "QUICKSIGHT_OWNER",
    "QUICKSIGHT_USER",
    "QUICKSIGHT_VIEWER_OR_OWNER",
]
AnchorOptionType = Literal["NOW"]
AnchorTypeType = Literal["TODAY"]
AnonymousUserDashboardEmbeddingConfigurationDisabledFeatureType = Literal["SHARED_VIEW"]
AnonymousUserDashboardEmbeddingConfigurationEnabledFeatureType = Literal["SHARED_VIEW"]
ArcThicknessOptionsType = Literal["LARGE", "MEDIUM", "SMALL"]
ArcThicknessType = Literal["LARGE", "MEDIUM", "SMALL", "WHOLE"]
AssetBundleExportFormatType = Literal["CLOUDFORMATION_JSON", "QUICKSIGHT_JSON"]
AssetBundleExportJobAnalysisPropertyToOverrideType = Literal["Name"]
AssetBundleExportJobDashboardPropertyToOverrideType = Literal["Name"]
AssetBundleExportJobDataSetPropertyToOverrideType = Literal[
    "Name", "RefreshFailureEmailAlertStatus"
]
AssetBundleExportJobDataSourcePropertyToOverrideType = Literal[
    "Catalog",
    "ClusterId",
    "DataSetName",
    "Database",
    "DisableSsl",
    "Domain",
    "Host",
    "InstanceId",
    "ManifestFileLocation",
    "Name",
    "Password",
    "Port",
    "ProductType",
    "RoleArn",
    "SecretArn",
    "Username",
    "Warehouse",
    "WorkGroup",
]
AssetBundleExportJobFolderPropertyToOverrideType = Literal["Name", "ParentFolderArn"]
AssetBundleExportJobRefreshSchedulePropertyToOverrideType = Literal["StartAfterDateTime"]
AssetBundleExportJobStatusType = Literal[
    "FAILED", "IN_PROGRESS", "QUEUED_FOR_IMMEDIATE_EXECUTION", "SUCCESSFUL"
]
AssetBundleExportJobThemePropertyToOverrideType = Literal["Name"]
AssetBundleExportJobVPCConnectionPropertyToOverrideType = Literal["DnsResolvers", "Name", "RoleArn"]
AssetBundleImportFailureActionType = Literal["DO_NOTHING", "ROLLBACK"]
AssetBundleImportJobStatusType = Literal[
    "FAILED",
    "FAILED_ROLLBACK_COMPLETED",
    "FAILED_ROLLBACK_ERROR",
    "FAILED_ROLLBACK_IN_PROGRESS",
    "IN_PROGRESS",
    "QUEUED_FOR_IMMEDIATE_EXECUTION",
    "SUCCESSFUL",
]
AssignmentStatusType = Literal["DISABLED", "DRAFT", "ENABLED"]
AuthenticationMethodOptionType = Literal[
    "ACTIVE_DIRECTORY", "IAM_AND_QUICKSIGHT", "IAM_IDENTITY_CENTER", "IAM_ONLY"
]
AuthenticationTypeType = Literal["PASSWORD", "TOKEN", "X509"]
AuthorSpecifiedAggregationType = Literal[
    "AVERAGE",
    "COUNT",
    "DISTINCT_COUNT",
    "MAX",
    "MEDIAN",
    "MIN",
    "PERCENTILE",
    "STDEV",
    "STDEVP",
    "SUM",
    "VAR",
    "VARP",
]
AxisBindingType = Literal["PRIMARY_YAXIS", "SECONDARY_YAXIS"]
BarChartOrientationType = Literal["HORIZONTAL", "VERTICAL"]
BarsArrangementType = Literal["CLUSTERED", "STACKED", "STACKED_PERCENT"]
BaseMapStyleTypeType = Literal["DARK_GRAY", "IMAGERY", "LIGHT_GRAY", "STREET"]
BoxPlotFillStyleType = Literal["SOLID", "TRANSPARENT"]
BrandStatusType = Literal[
    "CREATE_FAILED", "CREATE_IN_PROGRESS", "CREATE_SUCCEEDED", "DELETE_FAILED", "DELETE_IN_PROGRESS"
]
BrandVersionStatusType = Literal["CREATE_FAILED", "CREATE_IN_PROGRESS", "CREATE_SUCCEEDED"]
CapabilityStateType = Literal["DENY"]
CategoricalAggregationFunctionType = Literal["COUNT", "DISTINCT_COUNT"]
CategoryFilterFunctionType = Literal["CONTAINS", "EXACT"]
CategoryFilterMatchOperatorType = Literal[
    "CONTAINS", "DOES_NOT_CONTAIN", "DOES_NOT_EQUAL", "ENDS_WITH", "EQUALS", "STARTS_WITH"
]
CategoryFilterSelectAllOptionsType = Literal["FILTER_ALL_VALUES"]
CategoryFilterTypeType = Literal["CUSTOM_FILTER", "CUSTOM_FILTER_LIST", "FILTER_LIST"]
ColorFillTypeType = Literal["DISCRETE", "GRADIENT"]
ColumnDataRoleType = Literal["DIMENSION", "MEASURE"]
ColumnDataSubTypeType = Literal["FIXED", "FLOAT"]
ColumnDataTypeType = Literal["DATETIME", "DECIMAL", "INTEGER", "STRING"]
ColumnOrderingTypeType = Literal["GREATER_IS_BETTER", "LESSER_IS_BETTER", "SPECIFIED"]
ColumnRoleType = Literal["DIMENSION", "MEASURE"]
ColumnTagNameType = Literal["COLUMN_DESCRIPTION", "COLUMN_GEOGRAPHIC_ROLE"]
CommitModeType = Literal["AUTO", "MANUAL"]
ComparisonMethodType = Literal["DIFFERENCE", "PERCENT", "PERCENT_DIFFERENCE"]
ComparisonMethodTypeType = Literal[
    "DIFF",
    "DIFF_AS_PERC",
    "MOVING_AVERAGE",
    "PERCENT_OF_TOTAL",
    "PERC_DIFF",
    "POP_CURRENT_DIFF",
    "POP_CURRENT_DIFF_AS_PERC",
    "POP_OVERTIME_DIFF",
    "POP_OVERTIME_DIFF_AS_PERC",
    "RUNNING_SUM",
]
ConditionalFormattingIconDisplayOptionType = Literal["ICON_ONLY"]
ConditionalFormattingIconSetTypeType = Literal[
    "BARS",
    "CARET_UP_MINUS_DOWN",
    "CHECK_X",
    "FLAGS",
    "FOUR_COLOR_ARROW",
    "FOUR_GRAY_ARROW",
    "PLUS_MINUS",
    "THREE_CIRCLE",
    "THREE_COLOR_ARROW",
    "THREE_GRAY_ARROW",
    "THREE_SHAPE",
]
ConstantTypeType = Literal["COLLECTIVE", "RANGE", "SINGULAR"]
ContributionAnalysisDirectionType = Literal["DECREASE", "INCREASE", "NEUTRAL"]
ContributionAnalysisSortTypeType = Literal[
    "ABSOLUTE_DIFFERENCE",
    "CONTRIBUTION_PERCENTAGE",
    "DEVIATION_FROM_EXPECTED",
    "PERCENTAGE_DIFFERENCE",
]
CrossDatasetTypesType = Literal["ALL_DATASETS", "SINGLE_DATASET"]
CustomContentImageScalingConfigurationType = Literal[
    "DO_NOT_SCALE", "FIT_TO_HEIGHT", "FIT_TO_WIDTH", "SCALE_TO_VISUAL"
]
CustomContentTypeType = Literal["IMAGE", "OTHER_EMBEDDED_CONTENT"]
DashboardBehaviorType = Literal["DISABLED", "ENABLED"]
DashboardErrorTypeType = Literal[
    "ACCESS_DENIED",
    "COLUMN_GEOGRAPHIC_ROLE_MISMATCH",
    "COLUMN_REPLACEMENT_MISSING",
    "COLUMN_TYPE_MISMATCH",
    "DATA_SET_NOT_FOUND",
    "INTERNAL_FAILURE",
    "PARAMETER_NOT_FOUND",
    "PARAMETER_TYPE_INVALID",
    "PARAMETER_VALUE_INCOMPATIBLE",
    "SOURCE_NOT_FOUND",
]
DashboardFilterAttributeType = Literal[
    "DASHBOARD_NAME",
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
    "QUICKSIGHT_OWNER",
    "QUICKSIGHT_USER",
    "QUICKSIGHT_VIEWER_OR_OWNER",
]
DashboardUIStateType = Literal["COLLAPSED", "EXPANDED"]
DashboardsQAStatusType = Literal["DISABLED", "ENABLED"]
DataLabelContentType = Literal["PERCENT", "VALUE", "VALUE_AND_PERCENT"]
DataLabelOverlapType = Literal["DISABLE_OVERLAP", "ENABLE_OVERLAP"]
DataLabelPositionType = Literal["BOTTOM", "INSIDE", "LEFT", "OUTSIDE", "RIGHT", "TOP"]
DataSetFilterAttributeType = Literal[
    "DATASET_NAME",
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
    "QUICKSIGHT_OWNER",
    "QUICKSIGHT_VIEWER_OR_OWNER",
]
DataSetImportModeType = Literal["DIRECT_QUERY", "SPICE"]
DataSetUseAsType = Literal["RLS_RULES"]
DataSourceErrorInfoTypeType = Literal[
    "ACCESS_DENIED",
    "CONFLICT",
    "COPY_SOURCE_NOT_FOUND",
    "ENGINE_VERSION_NOT_SUPPORTED",
    "GENERIC_SQL_FAILURE",
    "TIMEOUT",
    "UNKNOWN",
    "UNKNOWN_HOST",
]
DataSourceFilterAttributeType = Literal[
    "DATASOURCE_NAME",
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
]
DataSourceTypeType = Literal[
    "ADOBE_ANALYTICS",
    "AMAZON_ELASTICSEARCH",
    "AMAZON_OPENSEARCH",
    "ATHENA",
    "AURORA",
    "AURORA_POSTGRESQL",
    "AWS_IOT_ANALYTICS",
    "BIGQUERY",
    "DATABRICKS",
    "EXASOL",
    "GITHUB",
    "JIRA",
    "MARIADB",
    "MYSQL",
    "ORACLE",
    "POSTGRESQL",
    "PRESTO",
    "REDSHIFT",
    "S3",
    "SALESFORCE",
    "SERVICENOW",
    "SNOWFLAKE",
    "SPARK",
    "SQLSERVER",
    "STARBURST",
    "TERADATA",
    "TIMESTREAM",
    "TRINO",
    "TWITTER",
]
DatasetParameterValueTypeType = Literal["MULTI_VALUED", "SINGLE_VALUED"]
DateAggregationFunctionType = Literal["COUNT", "DISTINCT_COUNT", "MAX", "MIN"]
DayOfTheWeekType = Literal[
    "FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"
]
DayOfWeekType = Literal[
    "FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"
]
DefaultAggregationType = Literal[
    "AVERAGE",
    "COUNT",
    "DISTINCT_COUNT",
    "MAX",
    "MEDIAN",
    "MIN",
    "STDEV",
    "STDEVP",
    "SUM",
    "VAR",
    "VARP",
]
DescribeFolderPermissionsPaginatorName = Literal["describe_folder_permissions"]
DescribeFolderResolvedPermissionsPaginatorName = Literal["describe_folder_resolved_permissions"]
DigitGroupingStyleType = Literal["DEFAULT", "LAKHS"]
DisplayFormatType = Literal["AUTO", "CURRENCY", "DATE", "NUMBER", "PERCENT", "STRING"]
EditionType = Literal["ENTERPRISE", "ENTERPRISE_AND_Q", "STANDARD"]
EmbeddingIdentityTypeType = Literal["ANONYMOUS", "IAM", "QUICKSIGHT"]
FileFormatType = Literal["CLF", "CSV", "ELF", "JSON", "TSV", "XLSX"]
FilterClassType = Literal["CONDITIONAL_VALUE_FILTER", "ENFORCED_VALUE_FILTER", "NAMED_VALUE_FILTER"]
FilterNullOptionType = Literal["ALL_VALUES", "NON_NULLS_ONLY", "NULLS_ONLY"]
FilterOperatorType = Literal["StringEquals", "StringLike"]
FilterVisualScopeType = Literal["ALL_VISUALS", "SELECTED_VISUALS"]
FolderFilterAttributeType = Literal[
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
    "FOLDER_NAME",
    "PARENT_FOLDER_ARN",
    "QUICKSIGHT_OWNER",
    "QUICKSIGHT_VIEWER_OR_OWNER",
]
FolderTypeType = Literal["RESTRICTED", "SHARED"]
FontDecorationType = Literal["NONE", "UNDERLINE"]
FontStyleType = Literal["ITALIC", "NORMAL"]
FontWeightNameType = Literal["BOLD", "NORMAL"]
ForecastComputationSeasonalityType = Literal["AUTOMATIC", "CUSTOM"]
FunnelChartMeasureDataLabelStyleType = Literal[
    "PERCENTAGE_BY_FIRST_STAGE",
    "PERCENTAGE_BY_PREVIOUS_STAGE",
    "VALUE_AND_PERCENTAGE_BY_FIRST_STAGE",
    "VALUE_AND_PERCENTAGE_BY_PREVIOUS_STAGE",
    "VALUE_ONLY",
]
GeneratedAnswerStatusType = Literal["ANSWER_DOWNGRADE", "ANSWER_GENERATED", "ANSWER_RETRIEVED"]
GeoSpatialCountryCodeType = Literal["US"]
GeoSpatialDataRoleType = Literal[
    "CITY", "COUNTRY", "COUNTY", "LATITUDE", "LONGITUDE", "POSTCODE", "STATE"
]
GeospatialColorStateType = Literal["DISABLED", "ENABLED"]
GeospatialLayerTypeType = Literal["LINE", "POINT", "POLYGON"]
GeospatialMapNavigationType = Literal["DISABLED", "ENABLED"]
GeospatialSelectedPointStyleType = Literal["CLUSTER", "HEATMAP", "POINT"]
GroupFilterAttributeType = Literal["GROUP_NAME"]
GroupFilterOperatorType = Literal["StartsWith"]
HistogramBinTypeType = Literal["BIN_COUNT", "BIN_WIDTH"]
HorizontalTextAlignmentType = Literal["AUTO", "CENTER", "LEFT", "RIGHT"]
IconType = Literal[
    "ARROW_DOWN",
    "ARROW_DOWN_LEFT",
    "ARROW_DOWN_RIGHT",
    "ARROW_LEFT",
    "ARROW_RIGHT",
    "ARROW_UP",
    "ARROW_UP_LEFT",
    "ARROW_UP_RIGHT",
    "CARET_DOWN",
    "CARET_UP",
    "CHECKMARK",
    "CIRCLE",
    "FACE_DOWN",
    "FACE_FLAT",
    "FACE_UP",
    "FLAG",
    "MINUS",
    "ONE_BAR",
    "PLUS",
    "SQUARE",
    "THREE_BAR",
    "THUMBS_DOWN",
    "THUMBS_UP",
    "TRIANGLE",
    "TWO_BAR",
    "X",
]
IdentityStoreType = Literal["QUICKSIGHT"]
IdentityTypeType = Literal["IAM", "IAM_IDENTITY_CENTER", "QUICKSIGHT"]
ImageCustomActionTriggerType = Literal["CLICK", "MENU"]
IncludeFolderMembersType = Literal["NONE", "ONE_LEVEL", "RECURSE"]
IncludeGeneratedAnswerType = Literal["EXCLUDE", "INCLUDE"]
IncludeQuickSightQIndexType = Literal["EXCLUDE", "INCLUDE"]
IngestionErrorTypeType = Literal[
    "ACCOUNT_CAPACITY_LIMIT_EXCEEDED",
    "CONNECTION_FAILURE",
    "CURSOR_NOT_ENABLED",
    "CUSTOMER_ERROR",
    "DATA_SET_DELETED",
    "DATA_SET_NOT_SPICE",
    "DATA_SET_SIZE_LIMIT_EXCEEDED",
    "DATA_SOURCE_AUTH_FAILED",
    "DATA_SOURCE_CONNECTION_FAILED",
    "DATA_SOURCE_NOT_FOUND",
    "DATA_TOLERANCE_EXCEPTION",
    "DUPLICATE_COLUMN_NAMES_FOUND",
    "ELASTICSEARCH_CURSOR_NOT_ENABLED",
    "FAILURE_TO_ASSUME_ROLE",
    "FAILURE_TO_PROCESS_JSON_FILE",
    "IAM_ROLE_NOT_AVAILABLE",
    "INGESTION_CANCELED",
    "INGESTION_SUPERSEDED",
    "INTERNAL_SERVICE_ERROR",
    "INVALID_DATAPREP_SYNTAX",
    "INVALID_DATA_SOURCE_CONFIG",
    "INVALID_DATE_FORMAT",
    "IOT_DATA_SET_FILE_EMPTY",
    "IOT_FILE_NOT_FOUND",
    "OAUTH_TOKEN_FAILURE",
    "PASSWORD_AUTHENTICATION_FAILURE",
    "PERMISSION_DENIED",
    "PERMISSION_NOT_FOUND",
    "QUERY_TIMEOUT",
    "REFRESH_SUPPRESSED_BY_EDIT",
    "ROW_SIZE_LIMIT_EXCEEDED",
    "S3_FILE_INACCESSIBLE",
    "S3_MANIFEST_ERROR",
    "S3_UPLOADED_FILE_DELETED",
    "SOURCE_API_LIMIT_EXCEEDED_FAILURE",
    "SOURCE_RESOURCE_LIMIT_EXCEEDED",
    "SPICE_TABLE_NOT_FOUND",
    "SQL_EXCEPTION",
    "SQL_INVALID_PARAMETER_VALUE",
    "SQL_NUMERIC_OVERFLOW",
    "SQL_SCHEMA_MISMATCH_ERROR",
    "SQL_TABLE_NOT_FOUND",
    "SSL_CERTIFICATE_VALIDATION_FAILURE",
    "UNRESOLVABLE_HOST",
    "UNROUTABLE_HOST",
]
IngestionRequestSourceType = Literal["MANUAL", "SCHEDULED"]
IngestionRequestTypeType = Literal[
    "EDIT", "FULL_REFRESH", "INCREMENTAL_REFRESH", "INITIAL_INGESTION"
]
IngestionStatusType = Literal[
    "CANCELLED", "COMPLETED", "FAILED", "INITIALIZED", "QUEUED", "RUNNING"
]
IngestionTypeType = Literal["FULL_REFRESH", "INCREMENTAL_REFRESH"]
InputColumnDataTypeType = Literal[
    "BIT", "BOOLEAN", "DATETIME", "DECIMAL", "INTEGER", "JSON", "STRING"
]
JoinTypeType = Literal["INNER", "LEFT", "OUTER", "RIGHT"]
KPISparklineTypeType = Literal["AREA", "LINE"]
KPIVisualStandardLayoutTypeType = Literal["CLASSIC", "VERTICAL"]
LayerCustomActionTriggerType = Literal["DATA_POINT_CLICK", "DATA_POINT_MENU"]
LayoutElementTypeType = Literal[
    "FILTER_CONTROL", "IMAGE", "PARAMETER_CONTROL", "TEXT_BOX", "VISUAL"
]
LegendPositionType = Literal["AUTO", "BOTTOM", "RIGHT", "TOP"]
LineChartLineStyleType = Literal["DASHED", "DOTTED", "SOLID"]
LineChartMarkerShapeType = Literal["CIRCLE", "DIAMOND", "ROUNDED_SQUARE", "SQUARE", "TRIANGLE"]
LineChartTypeType = Literal["AREA", "LINE", "STACKED_AREA"]
LineInterpolationType = Literal["LINEAR", "SMOOTH", "STEPPED"]
ListAnalysesPaginatorName = Literal["list_analyses"]
ListAssetBundleExportJobsPaginatorName = Literal["list_asset_bundle_export_jobs"]
ListAssetBundleImportJobsPaginatorName = Literal["list_asset_bundle_import_jobs"]
ListBrandsPaginatorName = Literal["list_brands"]
ListCustomPermissionsPaginatorName = Literal["list_custom_permissions"]
ListDashboardVersionsPaginatorName = Literal["list_dashboard_versions"]
ListDashboardsPaginatorName = Literal["list_dashboards"]
ListDataSetsPaginatorName = Literal["list_data_sets"]
ListDataSourcesPaginatorName = Literal["list_data_sources"]
ListFolderMembersPaginatorName = Literal["list_folder_members"]
ListFoldersForResourcePaginatorName = Literal["list_folders_for_resource"]
ListFoldersPaginatorName = Literal["list_folders"]
ListGroupMembershipsPaginatorName = Literal["list_group_memberships"]
ListGroupsPaginatorName = Literal["list_groups"]
ListIAMPolicyAssignmentsForUserPaginatorName = Literal["list_iam_policy_assignments_for_user"]
ListIAMPolicyAssignmentsPaginatorName = Literal["list_iam_policy_assignments"]
ListIngestionsPaginatorName = Literal["list_ingestions"]
ListNamespacesPaginatorName = Literal["list_namespaces"]
ListRoleMembershipsPaginatorName = Literal["list_role_memberships"]
ListTemplateAliasesPaginatorName = Literal["list_template_aliases"]
ListTemplateVersionsPaginatorName = Literal["list_template_versions"]
ListTemplatesPaginatorName = Literal["list_templates"]
ListThemeVersionsPaginatorName = Literal["list_theme_versions"]
ListThemesPaginatorName = Literal["list_themes"]
ListUserGroupsPaginatorName = Literal["list_user_groups"]
ListUsersPaginatorName = Literal["list_users"]
LookbackWindowSizeUnitType = Literal["DAY", "HOUR", "WEEK"]
MapZoomModeType = Literal["AUTO", "MANUAL"]
MaximumMinimumComputationTypeType = Literal["MAXIMUM", "MINIMUM"]
MemberTypeType = Literal["ANALYSIS", "DASHBOARD", "DATASET", "DATASOURCE", "TOPIC"]
MissingDataTreatmentOptionType = Literal["INTERPOLATE", "SHOW_AS_BLANK", "SHOW_AS_ZERO"]
NamedEntityAggTypeType = Literal[
    "AVERAGE",
    "COUNT",
    "CUSTOM",
    "DISTINCT_COUNT",
    "MAX",
    "MEDIAN",
    "MIN",
    "PERCENTILE",
    "STDEV",
    "STDEVP",
    "SUM",
    "VAR",
    "VARP",
]
NamedFilterAggTypeType = Literal[
    "AVERAGE",
    "COUNT",
    "DISTINCT_COUNT",
    "MAX",
    "MEDIAN",
    "MIN",
    "NO_AGGREGATION",
    "STDEV",
    "STDEVP",
    "SUM",
    "VAR",
    "VARP",
]
NamedFilterTypeType = Literal[
    "CATEGORY_FILTER",
    "DATE_RANGE_FILTER",
    "NUMERIC_EQUALITY_FILTER",
    "NUMERIC_RANGE_FILTER",
    "RELATIVE_DATE_FILTER",
]
NamespaceErrorTypeType = Literal["INTERNAL_SERVICE_ERROR", "PERMISSION_DENIED"]
NamespaceStatusType = Literal[
    "CREATED", "CREATING", "DELETING", "NON_RETRYABLE_FAILURE", "RETRYABLE_FAILURE"
]
NegativeValueDisplayModeType = Literal["NEGATIVE", "POSITIVE"]
NetworkInterfaceStatusType = Literal[
    "ATTACHMENT_FAILED_ROLLBACK_FAILED",
    "AVAILABLE",
    "CREATING",
    "CREATION_FAILED",
    "DELETED",
    "DELETING",
    "DELETION_FAILED",
    "DELETION_SCHEDULED",
    "UPDATE_FAILED",
    "UPDATING",
]
NullFilterOptionType = Literal["ALL_VALUES", "NON_NULLS_ONLY", "NULLS_ONLY"]
NumberScaleType = Literal[
    "AUTO", "BILLIONS", "CRORES", "LAKHS", "MILLIONS", "NONE", "THOUSANDS", "TRILLIONS"
]
NumericEqualityMatchOperatorType = Literal["DOES_NOT_EQUAL", "EQUALS"]
NumericFilterSelectAllOptionsType = Literal["FILTER_ALL_VALUES"]
NumericSeparatorSymbolType = Literal["COMMA", "DOT", "SPACE"]
OtherCategoriesType = Literal["EXCLUDE", "INCLUDE"]
PanelBorderStyleType = Literal["DASHED", "DOTTED", "SOLID"]
PaperOrientationType = Literal["LANDSCAPE", "PORTRAIT"]
PaperSizeType = Literal[
    "A0",
    "A1",
    "A2",
    "A3",
    "A4",
    "A5",
    "JIS_B4",
    "JIS_B5",
    "US_LEGAL",
    "US_LETTER",
    "US_TABLOID_LEDGER",
]
ParameterValueTypeType = Literal["MULTI_VALUED", "SINGLE_VALUED"]
PersonalizationModeType = Literal["DISABLED", "ENABLED"]
PivotTableConditionalFormattingScopeRoleType = Literal["FIELD", "FIELD_TOTAL", "GRAND_TOTAL"]
PivotTableDataPathTypeType = Literal[
    "COUNT_METRIC_COLUMN",
    "EMPTY_COLUMN_HEADER",
    "HIERARCHY_ROWS_LAYOUT_COLUMN",
    "MULTIPLE_ROW_METRICS_COLUMN",
]
PivotTableFieldCollapseStateType = Literal["COLLAPSED", "EXPANDED"]
PivotTableMetricPlacementType = Literal["COLUMN", "ROW"]
PivotTableRowsLayoutType = Literal["HIERARCHY", "TABULAR"]
PivotTableSubtotalLevelType = Literal["ALL", "CUSTOM", "LAST"]
PluginVisualAxisNameType = Literal["GROUP_BY", "VALUE"]
PrimaryValueDisplayTypeType = Literal["ACTUAL", "COMPARISON", "HIDDEN"]
PropertyRoleType = Literal["ID", "PRIMARY"]
PropertyUsageType = Literal["DIMENSION", "INHERIT", "MEASURE"]
PurchaseModeType = Literal["AUTO_PURCHASE", "MANUAL"]
QAResultTypeType = Literal["DASHBOARD_VISUAL", "GENERATED_ANSWER", "NO_ANSWER"]
QBusinessInsightsStatusType = Literal["DISABLED", "ENABLED"]
QSearchStatusType = Literal["DISABLED", "ENABLED"]
QueryExecutionModeType = Literal["AUTO", "MANUAL"]
RadarChartAxesRangeScaleType = Literal["AUTO", "INDEPENDENT", "SHARED"]
RadarChartShapeType = Literal["CIRCLE", "POLYGON"]
ReferenceLineLabelHorizontalPositionType = Literal["CENTER", "LEFT", "RIGHT"]
ReferenceLineLabelVerticalPositionType = Literal["ABOVE", "BELOW"]
ReferenceLinePatternTypeType = Literal["DASHED", "DOTTED", "SOLID"]
ReferenceLineSeriesTypeType = Literal["BAR", "LINE"]
ReferenceLineValueLabelRelativePositionType = Literal["AFTER_CUSTOM_LABEL", "BEFORE_CUSTOM_LABEL"]
RefreshFailureAlertStatusType = Literal["DISABLED", "ENABLED"]
RefreshIntervalType = Literal["DAILY", "HOURLY", "MINUTE15", "MINUTE30", "MONTHLY", "WEEKLY"]
RelativeDateTypeType = Literal["LAST", "NEXT", "NOW", "PREVIOUS", "THIS"]
RelativeFontSizeType = Literal["EXTRA_LARGE", "EXTRA_SMALL", "LARGE", "MEDIUM", "SMALL"]
ResizeOptionType = Literal["FIXED", "RESPONSIVE"]
ResourceStatusType = Literal[
    "CREATION_FAILED",
    "CREATION_IN_PROGRESS",
    "CREATION_SUCCESSFUL",
    "DELETED",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_SUCCESSFUL",
]
ReviewedAnswerErrorCodeType = Literal[
    "DATASET_DOES_NOT_EXIST",
    "DUPLICATED_ANSWER",
    "INTERNAL_ERROR",
    "INVALID_DATA",
    "INVALID_DATASET_ARN",
    "MISSING_ANSWER",
    "MISSING_REQUIRED_FIELDS",
]
RoleType = Literal["ADMIN", "ADMIN_PRO", "AUTHOR", "AUTHOR_PRO", "READER", "READER_PRO"]
RowLevelPermissionFormatVersionType = Literal["VERSION_1", "VERSION_2"]
RowLevelPermissionPolicyType = Literal["DENY_ACCESS", "GRANT_ACCESS"]
SearchAnalysesPaginatorName = Literal["search_analyses"]
SearchDashboardsPaginatorName = Literal["search_dashboards"]
SearchDataSetsPaginatorName = Literal["search_data_sets"]
SearchDataSourcesPaginatorName = Literal["search_data_sources"]
SearchFoldersPaginatorName = Literal["search_folders"]
SearchGroupsPaginatorName = Literal["search_groups"]
SearchTopicsPaginatorName = Literal["search_topics"]
SectionPageBreakStatusType = Literal["DISABLED", "ENABLED"]
SelectAllValueOptionsType = Literal["ALL_VALUES"]
SelectedFieldOptionsType = Literal["ALL_FIELDS"]
SelectedTooltipTypeType = Literal["BASIC", "DETAILED"]
ServiceTypeType = Literal["QBUSINESS", "REDSHIFT"]
SharingModelType = Literal["ACCOUNT", "NAMESPACE"]
SheetContentTypeType = Literal["INTERACTIVE", "PAGINATED"]
SheetControlDateTimePickerTypeType = Literal["DATE_RANGE", "SINGLE_VALUED"]
SheetControlListTypeType = Literal["MULTI_SELECT", "SINGLE_SELECT"]
SheetControlSliderTypeType = Literal["RANGE", "SINGLE_POINT"]
SheetImageScalingTypeType = Literal[
    "SCALE_NONE", "SCALE_TO_CONTAINER", "SCALE_TO_HEIGHT", "SCALE_TO_WIDTH"
]
SimpleAttributeAggregationFunctionType = Literal["UNIQUE_VALUE"]
SimpleNumericalAggregationFunctionType = Literal[
    "AVERAGE",
    "COUNT",
    "DISTINCT_COUNT",
    "MAX",
    "MEDIAN",
    "MIN",
    "STDEV",
    "STDEVP",
    "SUM",
    "VAR",
    "VARP",
]
SimpleTotalAggregationFunctionType = Literal["AVERAGE", "DEFAULT", "MAX", "MIN", "NONE", "SUM"]
SingleYAxisOptionType = Literal["PRIMARY_Y_AXIS"]
SmallMultiplesAxisPlacementType = Literal["INSIDE", "OUTSIDE"]
SmallMultiplesAxisScaleType = Literal["INDEPENDENT", "SHARED"]
SnapshotFileFormatTypeType = Literal["CSV", "EXCEL", "PDF"]
SnapshotFileSheetSelectionScopeType = Literal["ALL_VISUALS", "SELECTED_VISUALS"]
SnapshotJobStatusType = Literal["COMPLETED", "FAILED", "QUEUED", "RUNNING"]
SortDirectionType = Literal["ASC", "DESC"]
SpecialValueType = Literal["EMPTY", "NULL", "OTHER"]
StarburstProductTypeType = Literal["ENTERPRISE", "GALAXY"]
StatusType = Literal["DISABLED", "ENABLED"]
StyledCellTypeType = Literal["METRIC_HEADER", "TOTAL", "VALUE"]
TableBorderStyleType = Literal["NONE", "SOLID"]
TableCellImageScalingConfigurationType = Literal[
    "DO_NOT_SCALE", "FIT_TO_CELL_HEIGHT", "FIT_TO_CELL_WIDTH"
]
TableFieldIconSetTypeType = Literal["LINK"]
TableOrientationType = Literal["HORIZONTAL", "VERTICAL"]
TableTotalsPlacementType = Literal["AUTO", "END", "START"]
TableTotalsScrollStatusType = Literal["PINNED", "SCROLLED"]
TargetVisualOptionsType = Literal["ALL_VISUALS"]
TemplateErrorTypeType = Literal[
    "ACCESS_DENIED", "DATA_SET_NOT_FOUND", "INTERNAL_FAILURE", "SOURCE_NOT_FOUND"
]
TextQualifierType = Literal["DOUBLE_QUOTE", "SINGLE_QUOTE"]
TextWrapType = Literal["NONE", "WRAP"]
ThemeErrorTypeType = Literal["INTERNAL_FAILURE"]
ThemeTypeType = Literal["ALL", "CUSTOM", "QUICKSIGHT"]
TimeGranularityType = Literal[
    "DAY", "HOUR", "MILLISECOND", "MINUTE", "MONTH", "QUARTER", "SECOND", "WEEK", "YEAR"
]
TooltipTargetType = Literal["BAR", "BOTH", "LINE"]
TooltipTitleTypeType = Literal["NONE", "PRIMARY_VALUE"]
TopBottomComputationTypeType = Literal["BOTTOM", "TOP"]
TopBottomSortOrderType = Literal["ABSOLUTE_DIFFERENCE", "PERCENT_DIFFERENCE"]
TopicFilterAttributeType = Literal[
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
    "QUICKSIGHT_OWNER",
    "QUICKSIGHT_USER",
    "QUICKSIGHT_VIEWER_OR_OWNER",
    "TOPIC_NAME",
]
TopicFilterOperatorType = Literal["StringEquals", "StringLike"]
TopicIRFilterFunctionType = Literal[
    "CONTAINS",
    "CONTAINS_STRING",
    "ENDS_WITH",
    "EXACT",
    "LAST",
    "NEXT",
    "NOW",
    "PREVIOUS",
    "STARTS_WITH",
    "THIS",
]
TopicIRFilterTypeType = Literal[
    "ACCEPT_ALL_FILTER",
    "CATEGORY_FILTER",
    "DATE_RANGE_FILTER",
    "EQUALS",
    "NUMERIC_EQUALITY_FILTER",
    "NUMERIC_RANGE_FILTER",
    "RANK_LIMIT_FILTER",
    "RELATIVE_DATE_FILTER",
    "TOP_BOTTOM_FILTER",
]
TopicNumericSeparatorSymbolType = Literal["COMMA", "DOT"]
TopicRefreshStatusType = Literal["CANCELLED", "COMPLETED", "FAILED", "INITIALIZED", "RUNNING"]
TopicRelativeDateFilterFunctionType = Literal["LAST", "NEXT", "NOW", "PREVIOUS", "THIS"]
TopicScheduleTypeType = Literal["DAILY", "HOURLY", "MONTHLY", "WEEKLY"]
TopicSortDirectionType = Literal["ASCENDING", "DESCENDING"]
TopicTimeGranularityType = Literal[
    "DAY", "HOUR", "MINUTE", "MONTH", "QUARTER", "SECOND", "WEEK", "YEAR"
]
TopicUserExperienceVersionType = Literal["LEGACY", "NEW_READER_EXPERIENCE"]
TransposedColumnTypeType = Literal["ROW_HEADER_COLUMN", "VALUE_COLUMN"]
URLTargetConfigurationType = Literal["NEW_TAB", "NEW_WINDOW", "SAME_TAB"]
UndefinedSpecifiedValueTypeType = Literal["LEAST", "MOST"]
UserRoleType = Literal[
    "ADMIN",
    "ADMIN_PRO",
    "AUTHOR",
    "AUTHOR_PRO",
    "READER",
    "READER_PRO",
    "RESTRICTED_AUTHOR",
    "RESTRICTED_READER",
]
VPCConnectionAvailabilityStatusType = Literal["AVAILABLE", "PARTIALLY_AVAILABLE", "UNAVAILABLE"]
VPCConnectionResourceStatusType = Literal[
    "CREATION_FAILED",
    "CREATION_IN_PROGRESS",
    "CREATION_SUCCESSFUL",
    "DELETED",
    "DELETION_FAILED",
    "DELETION_IN_PROGRESS",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_SUCCESSFUL",
]
ValidationStrategyModeType = Literal["LENIENT", "STRICT"]
ValueWhenUnsetOptionType = Literal["NULL", "RECOMMENDED_VALUE"]
VerticalTextAlignmentType = Literal["AUTO", "BOTTOM", "MIDDLE", "TOP"]
VisibilityType = Literal["HIDDEN", "VISIBLE"]
VisualCustomActionTriggerType = Literal["DATA_POINT_CLICK", "DATA_POINT_MENU"]
VisualHighlightTriggerType = Literal["DATA_POINT_CLICK", "DATA_POINT_HOVER", "NONE"]
VisualRoleType = Literal["COMPLIMENTARY", "FALLBACK", "FRAGMENT", "MULTI_INTENT", "PRIMARY"]
WidgetStatusType = Literal["DISABLED", "ENABLED"]
WordCloudCloudLayoutType = Literal["FLUID", "NORMAL"]
WordCloudWordCasingType = Literal["EXISTING_CASE", "LOWER_CASE"]
WordCloudWordOrientationType = Literal["HORIZONTAL", "HORIZONTAL_AND_VERTICAL"]
WordCloudWordPaddingType = Literal["LARGE", "MEDIUM", "NONE", "SMALL"]
WordCloudWordScalingType = Literal["EMPHASIZE", "NORMAL"]
QuickSightServiceName = Literal["quicksight"]
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
    "evs",
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
    "describe_folder_permissions",
    "describe_folder_resolved_permissions",
    "list_analyses",
    "list_asset_bundle_export_jobs",
    "list_asset_bundle_import_jobs",
    "list_brands",
    "list_custom_permissions",
    "list_dashboard_versions",
    "list_dashboards",
    "list_data_sets",
    "list_data_sources",
    "list_folder_members",
    "list_folders",
    "list_folders_for_resource",
    "list_group_memberships",
    "list_groups",
    "list_iam_policy_assignments",
    "list_iam_policy_assignments_for_user",
    "list_ingestions",
    "list_namespaces",
    "list_role_memberships",
    "list_template_aliases",
    "list_template_versions",
    "list_templates",
    "list_theme_versions",
    "list_themes",
    "list_user_groups",
    "list_users",
    "search_analyses",
    "search_dashboards",
    "search_data_sets",
    "search_data_sources",
    "search_folders",
    "search_groups",
    "search_topics",
]
RegionName = Literal[
    "af-south-1",
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-south-1",
    "ap-southeast-1",
    "ap-southeast-2",
    "ap-southeast-3",
    "ca-central-1",
    "eu-central-1",
    "eu-central-2",
    "eu-north-1",
    "eu-south-1",
    "eu-south-2",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "sa-east-1",
    "us-east-1",
    "us-east-2",
    "us-west-2",
]
