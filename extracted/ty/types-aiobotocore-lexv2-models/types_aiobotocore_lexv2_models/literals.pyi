"""
Type annotations for lexv2-models service literal definitions.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/literals/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from types_aiobotocore_lexv2_models.literals import AggregatedUtterancesFilterNameType

    data: AggregatedUtterancesFilterNameType = "Utterance"
    ```
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AggregatedUtterancesFilterNameType",
    "AggregatedUtterancesFilterOperatorType",
    "AggregatedUtterancesSortAttributeType",
    "AnalyticsBinByNameType",
    "AnalyticsCommonFilterNameType",
    "AnalyticsFilterOperatorType",
    "AnalyticsIntentFieldType",
    "AnalyticsIntentFilterNameType",
    "AnalyticsIntentMetricNameType",
    "AnalyticsIntentStageFieldType",
    "AnalyticsIntentStageFilterNameType",
    "AnalyticsIntentStageMetricNameType",
    "AnalyticsIntervalType",
    "AnalyticsMetricStatisticType",
    "AnalyticsModalityType",
    "AnalyticsNodeTypeType",
    "AnalyticsSessionFieldType",
    "AnalyticsSessionFilterNameType",
    "AnalyticsSessionMetricNameType",
    "AnalyticsSessionSortByNameType",
    "AnalyticsSortOrderType",
    "AnalyticsUtteranceAttributeNameType",
    "AnalyticsUtteranceFieldType",
    "AnalyticsUtteranceFilterNameType",
    "AnalyticsUtteranceMetricNameType",
    "AnalyticsUtteranceSortByNameType",
    "AssociatedTranscriptFilterNameType",
    "AudioRecognitionStrategyType",
    "BedrockTraceStatusType",
    "BotAliasAvailableWaiterName",
    "BotAliasReplicationStatusType",
    "BotAliasStatusType",
    "BotAvailableWaiterName",
    "BotExportCompletedWaiterName",
    "BotFilterNameType",
    "BotFilterOperatorType",
    "BotImportCompletedWaiterName",
    "BotLocaleBuiltWaiterName",
    "BotLocaleCreatedWaiterName",
    "BotLocaleExpressTestingAvailableWaiterName",
    "BotLocaleFilterNameType",
    "BotLocaleFilterOperatorType",
    "BotLocaleSortAttributeType",
    "BotLocaleStatusType",
    "BotRecommendationStatusType",
    "BotReplicaStatusType",
    "BotSortAttributeType",
    "BotStatusType",
    "BotTypeType",
    "BotVersionAvailableWaiterName",
    "BotVersionReplicaSortAttributeType",
    "BotVersionReplicationStatusType",
    "BotVersionSortAttributeType",
    "BuiltInIntentSortAttributeType",
    "BuiltInSlotTypeSortAttributeType",
    "ConversationEndStateType",
    "ConversationLogsInputModeFilterType",
    "CustomVocabularyStatusType",
    "DialogActionTypeType",
    "EffectType",
    "ErrorCodeType",
    "ExportFilterNameType",
    "ExportFilterOperatorType",
    "ExportSortAttributeType",
    "ExportStatusType",
    "GenerationSortByAttributeType",
    "GenerationStatusType",
    "ImportExportFileFormatType",
    "ImportFilterNameType",
    "ImportFilterOperatorType",
    "ImportResourceTypeType",
    "ImportSortAttributeType",
    "ImportStatusType",
    "IntentFilterNameType",
    "IntentFilterOperatorType",
    "IntentSortAttributeType",
    "IntentStateType",
    "LexModelsV2ServiceName",
    "MergeStrategyType",
    "MessageSelectionStrategyType",
    "ObfuscationSettingTypeType",
    "PromptAttemptType",
    "RegionName",
    "ResourceServiceName",
    "SearchOrderType",
    "ServiceName",
    "SlotConstraintType",
    "SlotFilterNameType",
    "SlotFilterOperatorType",
    "SlotResolutionStrategyType",
    "SlotShapeType",
    "SlotSortAttributeType",
    "SlotTypeCategoryType",
    "SlotTypeFilterNameType",
    "SlotTypeFilterOperatorType",
    "SlotTypeSortAttributeType",
    "SlotValueResolutionStrategyType",
    "SortOrderType",
    "TestExecutionApiModeType",
    "TestExecutionModalityType",
    "TestExecutionSortAttributeType",
    "TestExecutionStatusType",
    "TestResultMatchStatusType",
    "TestResultTypeFilterType",
    "TestSetDiscrepancyReportStatusType",
    "TestSetGenerationStatusType",
    "TestSetModalityType",
    "TestSetSortAttributeType",
    "TestSetStatusType",
    "TimeDimensionType",
    "TranscriptFormatType",
    "UtteranceContentTypeType",
    "VoiceEngineType",
    "WaiterName",
)

AggregatedUtterancesFilterNameType = Literal["Utterance"]
AggregatedUtterancesFilterOperatorType = Literal["CO", "EQ"]
AggregatedUtterancesSortAttributeType = Literal["HitCount", "MissedCount"]
AnalyticsBinByNameType = Literal["ConversationStartTime", "UtteranceTimestamp"]
AnalyticsCommonFilterNameType = Literal[
    "BotAliasId", "BotVersion", "Channel", "LocaleId", "Modality"
]
AnalyticsFilterOperatorType = Literal["EQ", "GT", "LT"]
AnalyticsIntentFieldType = Literal["IntentEndState", "IntentLevel", "IntentName"]
AnalyticsIntentFilterNameType = Literal[
    "BotAliasId",
    "BotVersion",
    "Channel",
    "IntentEndState",
    "IntentName",
    "LocaleId",
    "Modality",
    "OriginatingRequestId",
    "SessionId",
]
AnalyticsIntentMetricNameType = Literal["Count", "Dropped", "Failure", "Success", "Switched"]
AnalyticsIntentStageFieldType = Literal["IntentStageName", "SwitchedToIntent"]
AnalyticsIntentStageFilterNameType = Literal[
    "BotAliasId",
    "BotVersion",
    "Channel",
    "IntentName",
    "IntentStageName",
    "LocaleId",
    "Modality",
    "OriginatingRequestId",
    "SessionId",
]
AnalyticsIntentStageMetricNameType = Literal["Count", "Dropped", "Failed", "Retry", "Success"]
AnalyticsIntervalType = Literal["OneDay", "OneHour"]
AnalyticsMetricStatisticType = Literal["Avg", "Max", "Sum"]
AnalyticsModalityType = Literal["DTMF", "MultiMode", "Speech", "Text"]
AnalyticsNodeTypeType = Literal["Exit", "Inner"]
AnalyticsSessionFieldType = Literal["ConversationEndState", "LocaleId"]
AnalyticsSessionFilterNameType = Literal[
    "BotAliasId",
    "BotVersion",
    "Channel",
    "ConversationEndState",
    "Duration",
    "IntentPath",
    "LocaleId",
    "Modality",
    "OriginatingRequestId",
    "SessionId",
]
AnalyticsSessionMetricNameType = Literal[
    "Concurrency", "Count", "Dropped", "Duration", "Failure", "Success", "TurnsPerConversation"
]
AnalyticsSessionSortByNameType = Literal["ConversationStartTime", "Duration", "NumberOfTurns"]
AnalyticsSortOrderType = Literal["Ascending", "Descending"]
AnalyticsUtteranceAttributeNameType = Literal["LastUsedIntent"]
AnalyticsUtteranceFieldType = Literal["UtteranceState", "UtteranceText"]
AnalyticsUtteranceFilterNameType = Literal[
    "BotAliasId",
    "BotVersion",
    "Channel",
    "LocaleId",
    "Modality",
    "OriginatingRequestId",
    "SessionId",
    "UtteranceState",
    "UtteranceText",
]
AnalyticsUtteranceMetricNameType = Literal["Count", "Detected", "Missed", "UtteranceTimestamp"]
AnalyticsUtteranceSortByNameType = Literal["UtteranceTimestamp"]
AssociatedTranscriptFilterNameType = Literal["IntentId", "SlotTypeId"]
AudioRecognitionStrategyType = Literal["UseSlotValuesAsCustomVocabulary"]
BedrockTraceStatusType = Literal["DISABLED", "ENABLED"]
BotAliasAvailableWaiterName = Literal["bot_alias_available"]
BotAliasReplicationStatusType = Literal["Available", "Creating", "Deleting", "Failed", "Updating"]
BotAliasStatusType = Literal["Available", "Creating", "Deleting", "Failed"]
BotAvailableWaiterName = Literal["bot_available"]
BotExportCompletedWaiterName = Literal["bot_export_completed"]
BotFilterNameType = Literal["BotName", "BotType"]
BotFilterOperatorType = Literal["CO", "EQ", "NE"]
BotImportCompletedWaiterName = Literal["bot_import_completed"]
BotLocaleBuiltWaiterName = Literal["bot_locale_built"]
BotLocaleCreatedWaiterName = Literal["bot_locale_created"]
BotLocaleExpressTestingAvailableWaiterName = Literal["bot_locale_express_testing_available"]
BotLocaleFilterNameType = Literal["BotLocaleName"]
BotLocaleFilterOperatorType = Literal["CO", "EQ"]
BotLocaleSortAttributeType = Literal["BotLocaleName"]
BotLocaleStatusType = Literal[
    "Building",
    "Built",
    "Creating",
    "Deleting",
    "Failed",
    "Importing",
    "NotBuilt",
    "Processing",
    "ReadyExpressTesting",
]
BotRecommendationStatusType = Literal[
    "Available",
    "Deleted",
    "Deleting",
    "Downloading",
    "Failed",
    "Processing",
    "Stopped",
    "Stopping",
    "Updating",
]
BotReplicaStatusType = Literal["Deleting", "Enabled", "Enabling", "Failed"]
BotSortAttributeType = Literal["BotName"]
BotStatusType = Literal[
    "Available", "Creating", "Deleting", "Failed", "Importing", "Inactive", "Updating", "Versioning"
]
BotTypeType = Literal["Bot", "BotNetwork"]
BotVersionAvailableWaiterName = Literal["bot_version_available"]
BotVersionReplicaSortAttributeType = Literal["BotVersion"]
BotVersionReplicationStatusType = Literal["Available", "Creating", "Deleting", "Failed"]
BotVersionSortAttributeType = Literal["BotVersion"]
BuiltInIntentSortAttributeType = Literal["IntentSignature"]
BuiltInSlotTypeSortAttributeType = Literal["SlotTypeSignature"]
ConversationEndStateType = Literal["Dropped", "Failure", "Success"]
ConversationLogsInputModeFilterType = Literal["Speech", "Text"]
CustomVocabularyStatusType = Literal["Creating", "Deleting", "Exporting", "Importing", "Ready"]
DialogActionTypeType = Literal[
    "CloseIntent",
    "ConfirmIntent",
    "ElicitIntent",
    "ElicitSlot",
    "EndConversation",
    "EvaluateConditional",
    "FulfillIntent",
    "InvokeDialogCodeHook",
    "StartIntent",
]
EffectType = Literal["Allow", "Deny"]
ErrorCodeType = Literal[
    "DUPLICATE_INPUT",
    "INTERNAL_SERVER_FAILURE",
    "RESOURCE_ALREADY_EXISTS",
    "RESOURCE_DOES_NOT_EXIST",
]
ExportFilterNameType = Literal["ExportResourceType"]
ExportFilterOperatorType = Literal["CO", "EQ"]
ExportSortAttributeType = Literal["LastUpdatedDateTime"]
ExportStatusType = Literal["Completed", "Deleting", "Failed", "InProgress"]
GenerationSortByAttributeType = Literal["creationStartTime", "lastUpdatedTime"]
GenerationStatusType = Literal["Complete", "Failed", "InProgress"]
ImportExportFileFormatType = Literal["CSV", "LexJson", "TSV"]
ImportFilterNameType = Literal["ImportResourceType"]
ImportFilterOperatorType = Literal["CO", "EQ"]
ImportResourceTypeType = Literal["Bot", "BotLocale", "CustomVocabulary", "TestSet"]
ImportSortAttributeType = Literal["LastUpdatedDateTime"]
ImportStatusType = Literal["Completed", "Deleting", "Failed", "InProgress"]
IntentFilterNameType = Literal["IntentName"]
IntentFilterOperatorType = Literal["CO", "EQ"]
IntentSortAttributeType = Literal["IntentName", "LastUpdatedDateTime"]
IntentStateType = Literal[
    "Failed", "Fulfilled", "FulfillmentInProgress", "InProgress", "ReadyForFulfillment", "Waiting"
]
MergeStrategyType = Literal["Append", "FailOnConflict", "Overwrite"]
MessageSelectionStrategyType = Literal["Ordered", "Random"]
ObfuscationSettingTypeType = Literal["DefaultObfuscation", "None"]
PromptAttemptType = Literal["Initial", "Retry1", "Retry2", "Retry3", "Retry4", "Retry5"]
SearchOrderType = Literal["Ascending", "Descending"]
SlotConstraintType = Literal["Optional", "Required"]
SlotFilterNameType = Literal["SlotName"]
SlotFilterOperatorType = Literal["CO", "EQ"]
SlotResolutionStrategyType = Literal["Default", "EnhancedFallback"]
SlotShapeType = Literal["List", "Scalar"]
SlotSortAttributeType = Literal["LastUpdatedDateTime", "SlotName"]
SlotTypeCategoryType = Literal["Composite", "Custom", "Extended", "ExternalGrammar"]
SlotTypeFilterNameType = Literal["ExternalSourceType", "SlotTypeName"]
SlotTypeFilterOperatorType = Literal["CO", "EQ"]
SlotTypeSortAttributeType = Literal["LastUpdatedDateTime", "SlotTypeName"]
SlotValueResolutionStrategyType = Literal["Concatenation", "OriginalValue", "TopResolution"]
SortOrderType = Literal["Ascending", "Descending"]
TestExecutionApiModeType = Literal["NonStreaming", "Streaming"]
TestExecutionModalityType = Literal["Audio", "Text"]
TestExecutionSortAttributeType = Literal["CreationDateTime", "TestSetName"]
TestExecutionStatusType = Literal[
    "Completed", "Failed", "InProgress", "Pending", "Stopped", "Stopping", "Waiting"
]
TestResultMatchStatusType = Literal["ExecutionError", "Matched", "Mismatched"]
TestResultTypeFilterType = Literal[
    "ConversationLevelTestResults",
    "IntentClassificationTestResults",
    "OverallTestResults",
    "SlotResolutionTestResults",
    "UtteranceLevelResults",
]
TestSetDiscrepancyReportStatusType = Literal["Completed", "Failed", "InProgress"]
TestSetGenerationStatusType = Literal["Failed", "Generating", "Pending", "Ready"]
TestSetModalityType = Literal["Audio", "Text"]
TestSetSortAttributeType = Literal["LastUpdatedDateTime", "TestSetName"]
TestSetStatusType = Literal[
    "Deleting", "Importing", "PendingAnnotation", "Ready", "ValidationError"
]
TimeDimensionType = Literal["Days", "Hours", "Weeks"]
TranscriptFormatType = Literal["Lex"]
UtteranceContentTypeType = Literal["CustomPayload", "ImageResponseCard", "PlainText", "SSML"]
VoiceEngineType = Literal["generative", "long-form", "neural", "standard"]
LexModelsV2ServiceName = Literal["lexv2-models"]
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
WaiterName = Literal[
    "bot_alias_available",
    "bot_available",
    "bot_export_completed",
    "bot_import_completed",
    "bot_locale_built",
    "bot_locale_created",
    "bot_locale_express_testing_available",
    "bot_version_available",
]
RegionName = Literal[
    "af-south-1",
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-southeast-1",
    "ap-southeast-2",
    "ca-central-1",
    "eu-central-1",
    "eu-west-1",
    "eu-west-2",
    "us-east-1",
    "us-west-2",
]
