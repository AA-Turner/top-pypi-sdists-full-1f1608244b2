"""
Type annotations for securityhub service literal definitions.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_securityhub/literals/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from types_aiobotocore_securityhub.literals import ActorSessionMfaStatusType

    data: ActorSessionMfaStatusType = "DISABLED"
    ```
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActorSessionMfaStatusType",
    "AdminStatusType",
    "AssociationStatusType",
    "AssociationTypeType",
    "AutoEnableStandardsType",
    "AutomationRulesActionTypeType",
    "AwsIamAccessKeyStatusType",
    "AwsS3BucketNotificationConfigurationS3KeyFilterRuleNameType",
    "ComplianceStatusType",
    "ConfigurationPolicyAssociationStatusType",
    "ConnectionDirectionType",
    "ControlFindingGeneratorType",
    "ControlStatusType",
    "DateRangeUnitType",
    "DescribeActionTargetsPaginatorName",
    "DescribeProductsPaginatorName",
    "DescribeStandardsControlsPaginatorName",
    "DescribeStandardsPaginatorName",
    "FindingHistoryUpdateSourceTypeType",
    "GetEnabledStandardsPaginatorName",
    "GetFindingHistoryPaginatorName",
    "GetFindingsPaginatorName",
    "GetInsightsPaginatorName",
    "IntegrationTypeType",
    "ListConfigurationPoliciesPaginatorName",
    "ListConfigurationPolicyAssociationsPaginatorName",
    "ListEnabledProductsForImportPaginatorName",
    "ListFindingAggregatorsPaginatorName",
    "ListInvitationsPaginatorName",
    "ListMembersPaginatorName",
    "ListOrganizationAdminAccountsPaginatorName",
    "ListSecurityControlDefinitionsPaginatorName",
    "ListStandardsControlAssociationsPaginatorName",
    "MalwareStateType",
    "MalwareTypeType",
    "MapFilterComparisonType",
    "NetworkDirectionType",
    "OrganizationConfigurationConfigurationTypeType",
    "OrganizationConfigurationStatusType",
    "PaginatorName",
    "ParameterValueTypeType",
    "PartitionType",
    "RecordStateType",
    "RegionAvailabilityStatusType",
    "RegionName",
    "ResourceServiceName",
    "RuleStatusType",
    "SecurityControlPropertyType",
    "SecurityHubServiceName",
    "ServiceName",
    "SeverityLabelType",
    "SeverityRatingType",
    "SortOrderType",
    "StandardsControlsUpdatableType",
    "StandardsStatusType",
    "StatusReasonCodeType",
    "StringFilterComparisonType",
    "TargetTypeType",
    "ThreatIntelIndicatorCategoryType",
    "ThreatIntelIndicatorTypeType",
    "UnprocessedErrorCodeType",
    "UpdateStatusType",
    "VerificationStateType",
    "VulnerabilityExploitAvailableType",
    "VulnerabilityFixAvailableType",
    "WorkflowStateType",
    "WorkflowStatusType",
)

ActorSessionMfaStatusType = Literal["DISABLED", "ENABLED"]
AdminStatusType = Literal["DISABLE_IN_PROGRESS", "ENABLED"]
AssociationStatusType = Literal["DISABLED", "ENABLED"]
AssociationTypeType = Literal["APPLIED", "INHERITED"]
AutoEnableStandardsType = Literal["DEFAULT", "NONE"]
AutomationRulesActionTypeType = Literal["FINDING_FIELDS_UPDATE"]
AwsIamAccessKeyStatusType = Literal["Active", "Inactive"]
AwsS3BucketNotificationConfigurationS3KeyFilterRuleNameType = Literal["Prefix", "Suffix"]
ComplianceStatusType = Literal["FAILED", "NOT_AVAILABLE", "PASSED", "WARNING"]
ConfigurationPolicyAssociationStatusType = Literal["FAILED", "PENDING", "SUCCESS"]
ConnectionDirectionType = Literal["INBOUND", "OUTBOUND"]
ControlFindingGeneratorType = Literal["SECURITY_CONTROL", "STANDARD_CONTROL"]
ControlStatusType = Literal["DISABLED", "ENABLED"]
DateRangeUnitType = Literal["DAYS"]
DescribeActionTargetsPaginatorName = Literal["describe_action_targets"]
DescribeProductsPaginatorName = Literal["describe_products"]
DescribeStandardsControlsPaginatorName = Literal["describe_standards_controls"]
DescribeStandardsPaginatorName = Literal["describe_standards"]
FindingHistoryUpdateSourceTypeType = Literal["BATCH_IMPORT_FINDINGS", "BATCH_UPDATE_FINDINGS"]
GetEnabledStandardsPaginatorName = Literal["get_enabled_standards"]
GetFindingHistoryPaginatorName = Literal["get_finding_history"]
GetFindingsPaginatorName = Literal["get_findings"]
GetInsightsPaginatorName = Literal["get_insights"]
IntegrationTypeType = Literal[
    "RECEIVE_FINDINGS_FROM_SECURITY_HUB",
    "SEND_FINDINGS_TO_SECURITY_HUB",
    "UPDATE_FINDINGS_IN_SECURITY_HUB",
]
ListConfigurationPoliciesPaginatorName = Literal["list_configuration_policies"]
ListConfigurationPolicyAssociationsPaginatorName = Literal["list_configuration_policy_associations"]
ListEnabledProductsForImportPaginatorName = Literal["list_enabled_products_for_import"]
ListFindingAggregatorsPaginatorName = Literal["list_finding_aggregators"]
ListInvitationsPaginatorName = Literal["list_invitations"]
ListMembersPaginatorName = Literal["list_members"]
ListOrganizationAdminAccountsPaginatorName = Literal["list_organization_admin_accounts"]
ListSecurityControlDefinitionsPaginatorName = Literal["list_security_control_definitions"]
ListStandardsControlAssociationsPaginatorName = Literal["list_standards_control_associations"]
MalwareStateType = Literal["OBSERVED", "REMOVAL_FAILED", "REMOVED"]
MalwareTypeType = Literal[
    "ADWARE",
    "BLENDED_THREAT",
    "BOTNET_AGENT",
    "COIN_MINER",
    "EXPLOIT_KIT",
    "KEYLOGGER",
    "MACRO",
    "POTENTIALLY_UNWANTED",
    "RANSOMWARE",
    "REMOTE_ACCESS",
    "ROOTKIT",
    "SPYWARE",
    "TROJAN",
    "VIRUS",
    "WORM",
]
MapFilterComparisonType = Literal["CONTAINS", "EQUALS", "NOT_CONTAINS", "NOT_EQUALS"]
NetworkDirectionType = Literal["IN", "OUT"]
OrganizationConfigurationConfigurationTypeType = Literal["CENTRAL", "LOCAL"]
OrganizationConfigurationStatusType = Literal["ENABLED", "FAILED", "PENDING"]
ParameterValueTypeType = Literal["CUSTOM", "DEFAULT"]
PartitionType = Literal["aws", "aws-cn", "aws-us-gov"]
RecordStateType = Literal["ACTIVE", "ARCHIVED"]
RegionAvailabilityStatusType = Literal["AVAILABLE", "UNAVAILABLE"]
RuleStatusType = Literal["DISABLED", "ENABLED"]
SecurityControlPropertyType = Literal["Parameters"]
SeverityLabelType = Literal["CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM"]
SeverityRatingType = Literal["CRITICAL", "HIGH", "LOW", "MEDIUM"]
SortOrderType = Literal["asc", "desc"]
StandardsControlsUpdatableType = Literal["NOT_READY_FOR_UPDATES", "READY_FOR_UPDATES"]
StandardsStatusType = Literal["DELETING", "FAILED", "INCOMPLETE", "PENDING", "READY"]
StatusReasonCodeType = Literal[
    "INTERNAL_ERROR",
    "MAXIMUM_NUMBER_OF_CONFIG_RULES_EXCEEDED",
    "NO_AVAILABLE_CONFIGURATION_RECORDER",
]
StringFilterComparisonType = Literal[
    "CONTAINS", "EQUALS", "NOT_CONTAINS", "NOT_EQUALS", "PREFIX", "PREFIX_NOT_EQUALS"
]
TargetTypeType = Literal["ACCOUNT", "ORGANIZATIONAL_UNIT", "ROOT"]
ThreatIntelIndicatorCategoryType = Literal[
    "BACKDOOR", "CARD_STEALER", "COMMAND_AND_CONTROL", "DROP_SITE", "EXPLOIT_SITE", "KEYLOGGER"
]
ThreatIntelIndicatorTypeType = Literal[
    "DOMAIN",
    "EMAIL_ADDRESS",
    "HASH_MD5",
    "HASH_SHA1",
    "HASH_SHA256",
    "HASH_SHA512",
    "IPV4_ADDRESS",
    "IPV6_ADDRESS",
    "MUTEX",
    "PROCESS",
    "URL",
]
UnprocessedErrorCodeType = Literal["ACCESS_DENIED", "INVALID_INPUT", "LIMIT_EXCEEDED", "NOT_FOUND"]
UpdateStatusType = Literal["READY", "UPDATING"]
VerificationStateType = Literal["BENIGN_POSITIVE", "FALSE_POSITIVE", "TRUE_POSITIVE", "UNKNOWN"]
VulnerabilityExploitAvailableType = Literal["NO", "YES"]
VulnerabilityFixAvailableType = Literal["NO", "PARTIAL", "YES"]
WorkflowStateType = Literal["ASSIGNED", "DEFERRED", "IN_PROGRESS", "NEW", "RESOLVED"]
WorkflowStatusType = Literal["NEW", "NOTIFIED", "RESOLVED", "SUPPRESSED"]
SecurityHubServiceName = Literal["securityhub"]
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
    "describe_action_targets",
    "describe_products",
    "describe_standards",
    "describe_standards_controls",
    "get_enabled_standards",
    "get_finding_history",
    "get_findings",
    "get_insights",
    "list_configuration_policies",
    "list_configuration_policy_associations",
    "list_enabled_products_for_import",
    "list_finding_aggregators",
    "list_invitations",
    "list_members",
    "list_organization_admin_accounts",
    "list_security_control_definitions",
    "list_standards_control_associations",
]
RegionName = Literal[
    "af-south-1",
    "ap-east-1",
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-northeast-3",
    "ap-south-1",
    "ap-south-2",
    "ap-southeast-1",
    "ap-southeast-2",
    "ap-southeast-3",
    "ap-southeast-4",
    "ap-southeast-5",
    "ap-southeast-7",
    "ca-central-1",
    "ca-west-1",
    "eu-central-1",
    "eu-central-2",
    "eu-north-1",
    "eu-south-1",
    "eu-south-2",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "il-central-1",
    "me-central-1",
    "me-south-1",
    "mx-central-1",
    "sa-east-1",
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",
]
