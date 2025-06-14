"""
Type annotations for customer-profiles service literal definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/literals/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_customer_profiles.literals import AttributeDimensionTypeType

    data: AttributeDimensionTypeType = "AFTER"
    ```
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AttributeDimensionTypeType",
    "AttributeMatchingModelType",
    "ComparisonOperatorType",
    "ConflictResolvingModelType",
    "CustomerProfilesServiceName",
    "DataFormatType",
    "DataPullModeType",
    "DateDimensionTypeType",
    "EstimateStatusType",
    "EventStreamDestinationStatusType",
    "EventStreamStateType",
    "EventTriggerLogicalOperatorType",
    "FieldContentTypeType",
    "FilterDimensionTypeType",
    "GenderType",
    "GetSimilarProfilesPaginatorName",
    "IdentityResolutionJobStatusType",
    "IncludeOptionsType",
    "IncludeType",
    "JobScheduleDayOfTheWeekType",
    "LayoutTypeType",
    "ListDomainLayoutsPaginatorName",
    "ListEventStreamsPaginatorName",
    "ListEventTriggersPaginatorName",
    "ListObjectTypeAttributesPaginatorName",
    "ListRuleBasedMatchesPaginatorName",
    "ListSegmentDefinitionsPaginatorName",
    "LogicalOperatorType",
    "MarketoConnectorOperatorType",
    "MatchTypeType",
    "OperatorPropertiesKeysType",
    "OperatorType",
    "PaginatorName",
    "PartyTypeType",
    "PeriodUnitType",
    "QueryResultType",
    "RangeUnitType",
    "ReadinessStatusType",
    "RegionName",
    "ResourceServiceName",
    "RuleBasedMatchingStatusType",
    "S3ConnectorOperatorType",
    "SalesforceConnectorOperatorType",
    "SegmentSnapshotStatusType",
    "ServiceName",
    "ServiceNowConnectorOperatorType",
    "SourceConnectorTypeType",
    "StandardIdentifierType",
    "StatisticType",
    "StatusType",
    "StringDimensionTypeType",
    "TaskTypeType",
    "TriggerTypeType",
    "TypeType",
    "UnitType",
    "WorkflowTypeType",
    "ZendeskConnectorOperatorType",
)

AttributeDimensionTypeType = Literal[
    "AFTER",
    "BEFORE",
    "BEGINS_WITH",
    "BETWEEN",
    "CONTAINS",
    "ENDS_WITH",
    "EQUAL",
    "EXCLUSIVE",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUAL",
    "INCLUSIVE",
    "LESS_THAN",
    "LESS_THAN_OR_EQUAL",
    "NOT_BETWEEN",
    "ON",
]
AttributeMatchingModelType = Literal["MANY_TO_MANY", "ONE_TO_ONE"]
ComparisonOperatorType = Literal[
    "AFTER",
    "BEFORE",
    "BEGINS_WITH",
    "BETWEEN",
    "CONTAINS",
    "ENDS_WITH",
    "EQUAL",
    "EXCLUSIVE",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUAL",
    "INCLUSIVE",
    "LESS_THAN",
    "LESS_THAN_OR_EQUAL",
    "NOT_BETWEEN",
    "ON",
]
ConflictResolvingModelType = Literal["RECENCY", "SOURCE"]
DataFormatType = Literal["CSV", "JSONL", "ORC"]
DataPullModeType = Literal["Complete", "Incremental"]
DateDimensionTypeType = Literal["AFTER", "BEFORE", "BETWEEN", "NOT_BETWEEN", "ON"]
EstimateStatusType = Literal["FAILED", "RUNNING", "SUCCEEDED"]
EventStreamDestinationStatusType = Literal["HEALTHY", "UNHEALTHY"]
EventStreamStateType = Literal["RUNNING", "STOPPED"]
EventTriggerLogicalOperatorType = Literal["ALL", "ANY", "NONE"]
FieldContentTypeType = Literal["EMAIL_ADDRESS", "NAME", "NUMBER", "PHONE_NUMBER", "STRING"]
FilterDimensionTypeType = Literal[
    "AFTER",
    "BEFORE",
    "BEGINS_WITH",
    "BETWEEN",
    "CONTAINS",
    "ENDS_WITH",
    "EQUAL",
    "EXCLUSIVE",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUAL",
    "INCLUSIVE",
    "LESS_THAN",
    "LESS_THAN_OR_EQUAL",
    "NOT_BETWEEN",
    "ON",
]
GenderType = Literal["FEMALE", "MALE", "UNSPECIFIED"]
GetSimilarProfilesPaginatorName = Literal["get_similar_profiles"]
IdentityResolutionJobStatusType = Literal[
    "COMPLETED", "FAILED", "FIND_MATCHING", "MERGING", "PARTIAL_SUCCESS", "PENDING", "PREPROCESSING"
]
IncludeOptionsType = Literal["ALL", "ANY", "NONE"]
IncludeType = Literal["ALL", "ANY", "NONE"]
JobScheduleDayOfTheWeekType = Literal[
    "FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"
]
LayoutTypeType = Literal["PROFILE_EXPLORER"]
ListDomainLayoutsPaginatorName = Literal["list_domain_layouts"]
ListEventStreamsPaginatorName = Literal["list_event_streams"]
ListEventTriggersPaginatorName = Literal["list_event_triggers"]
ListObjectTypeAttributesPaginatorName = Literal["list_object_type_attributes"]
ListRuleBasedMatchesPaginatorName = Literal["list_rule_based_matches"]
ListSegmentDefinitionsPaginatorName = Literal["list_segment_definitions"]
LogicalOperatorType = Literal["AND", "OR"]
MarketoConnectorOperatorType = Literal[
    "ADDITION",
    "BETWEEN",
    "DIVISION",
    "GREATER_THAN",
    "LESS_THAN",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "MULTIPLICATION",
    "NO_OP",
    "PROJECTION",
    "SUBTRACTION",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NUMERIC",
]
MatchTypeType = Literal["ML_BASED_MATCHING", "RULE_BASED_MATCHING"]
OperatorPropertiesKeysType = Literal[
    "CONCAT_FORMAT",
    "DATA_TYPE",
    "DESTINATION_DATA_TYPE",
    "LOWER_BOUND",
    "MASK_LENGTH",
    "MASK_VALUE",
    "MATH_OPERATION_FIELDS_ORDER",
    "SOURCE_DATA_TYPE",
    "SUBFIELD_CATEGORY_MAP",
    "TRUNCATE_LENGTH",
    "UPPER_BOUND",
    "VALIDATION_ACTION",
    "VALUE",
    "VALUES",
]
OperatorType = Literal["EQUAL_TO", "GREATER_THAN", "LESS_THAN", "NOT_EQUAL_TO"]
PartyTypeType = Literal["BUSINESS", "INDIVIDUAL", "OTHER"]
PeriodUnitType = Literal["DAYS", "HOURS", "MONTHS", "WEEKS"]
QueryResultType = Literal["ABSENT", "PRESENT"]
RangeUnitType = Literal["DAYS"]
ReadinessStatusType = Literal["COMPLETED", "FAILED", "IN_PROGRESS", "PREPARING"]
RuleBasedMatchingStatusType = Literal["ACTIVE", "IN_PROGRESS", "PENDING"]
S3ConnectorOperatorType = Literal[
    "ADDITION",
    "BETWEEN",
    "DIVISION",
    "EQUAL_TO",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUAL_TO",
    "LESS_THAN",
    "LESS_THAN_OR_EQUAL_TO",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "MULTIPLICATION",
    "NOT_EQUAL_TO",
    "NO_OP",
    "PROJECTION",
    "SUBTRACTION",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NUMERIC",
]
SalesforceConnectorOperatorType = Literal[
    "ADDITION",
    "BETWEEN",
    "CONTAINS",
    "DIVISION",
    "EQUAL_TO",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUAL_TO",
    "LESS_THAN",
    "LESS_THAN_OR_EQUAL_TO",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "MULTIPLICATION",
    "NOT_EQUAL_TO",
    "NO_OP",
    "PROJECTION",
    "SUBTRACTION",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NUMERIC",
]
SegmentSnapshotStatusType = Literal["COMPLETED", "FAILED", "IN_PROGRESS"]
ServiceNowConnectorOperatorType = Literal[
    "ADDITION",
    "BETWEEN",
    "CONTAINS",
    "DIVISION",
    "EQUAL_TO",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUAL_TO",
    "LESS_THAN",
    "LESS_THAN_OR_EQUAL_TO",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "MULTIPLICATION",
    "NOT_EQUAL_TO",
    "NO_OP",
    "PROJECTION",
    "SUBTRACTION",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NUMERIC",
]
SourceConnectorTypeType = Literal["Marketo", "S3", "Salesforce", "Servicenow", "Zendesk"]
StandardIdentifierType = Literal[
    "AIR_BOOKING",
    "AIR_PREFERENCE",
    "AIR_SEGMENT",
    "ASSET",
    "CASE",
    "COMMUNICATION_RECORD",
    "HOTEL_PREFERENCE",
    "HOTEL_RESERVATION",
    "HOTEL_STAY_REVENUE",
    "LOOKUP_ONLY",
    "LOYALTY",
    "LOYALTY_PROMOTION",
    "LOYALTY_TRANSACTION",
    "NEW_ONLY",
    "ORDER",
    "PROFILE",
    "SECONDARY",
    "UNIQUE",
]
StatisticType = Literal[
    "AVERAGE",
    "COUNT",
    "FIRST_OCCURRENCE",
    "LAST_OCCURRENCE",
    "MAXIMUM",
    "MAX_OCCURRENCE",
    "MINIMUM",
    "SUM",
]
StatusType = Literal[
    "CANCELLED", "COMPLETE", "FAILED", "IN_PROGRESS", "NOT_STARTED", "RETRY", "SPLIT"
]
StringDimensionTypeType = Literal["BEGINS_WITH", "CONTAINS", "ENDS_WITH", "EXCLUSIVE", "INCLUSIVE"]
TaskTypeType = Literal["Arithmetic", "Filter", "Map", "Mask", "Merge", "Truncate", "Validate"]
TriggerTypeType = Literal["Event", "OnDemand", "Scheduled"]
TypeType = Literal["ALL", "ANY", "NONE"]
UnitType = Literal["DAYS"]
WorkflowTypeType = Literal["APPFLOW_INTEGRATION"]
ZendeskConnectorOperatorType = Literal[
    "ADDITION",
    "DIVISION",
    "GREATER_THAN",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "MULTIPLICATION",
    "NO_OP",
    "PROJECTION",
    "SUBTRACTION",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NUMERIC",
]
CustomerProfilesServiceName = Literal["customer-profiles"]
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
    "get_similar_profiles",
    "list_domain_layouts",
    "list_event_streams",
    "list_event_triggers",
    "list_object_type_attributes",
    "list_rule_based_matches",
    "list_segment_definitions",
]
RegionName = Literal[
    "af-south-1",
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-southeast-1",
    "ap-southeast-2",
    "ca-central-1",
    "eu-central-1",
    "eu-west-2",
    "us-east-1",
    "us-west-2",
]
