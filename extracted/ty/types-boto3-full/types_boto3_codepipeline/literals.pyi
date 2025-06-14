"""
Type annotations for codepipeline service literal definitions.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codepipeline/literals/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from types_boto3_codepipeline.literals import ActionCategoryType

    data: ActionCategoryType = "Approval"
    ```
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActionCategoryType",
    "ActionConfigurationPropertyTypeType",
    "ActionExecutionStatusType",
    "ActionOwnerType",
    "ApprovalStatusType",
    "ArtifactLocationTypeType",
    "ArtifactStoreTypeType",
    "BlockerTypeType",
    "CodePipelineServiceName",
    "ConditionExecutionStatusType",
    "ConditionTypeType",
    "EncryptionKeyTypeType",
    "EnvironmentVariableTypeType",
    "ExecutionModeType",
    "ExecutionTypeType",
    "ExecutorTypeType",
    "FailureTypeType",
    "GitPullRequestEventTypeType",
    "JobStatusType",
    "ListActionExecutionsPaginatorName",
    "ListActionTypesPaginatorName",
    "ListDeployActionExecutionTargetsPaginatorName",
    "ListPipelineExecutionsPaginatorName",
    "ListPipelinesPaginatorName",
    "ListRuleExecutionsPaginatorName",
    "ListTagsForResourcePaginatorName",
    "ListWebhooksPaginatorName",
    "PaginatorName",
    "PipelineExecutionStatusType",
    "PipelineTriggerProviderTypeType",
    "PipelineTypeType",
    "RegionName",
    "ResourceServiceName",
    "ResultType",
    "RetryTriggerType",
    "RuleCategoryType",
    "RuleConfigurationPropertyTypeType",
    "RuleExecutionStatusType",
    "RuleOwnerType",
    "ServiceName",
    "SourceRevisionTypeType",
    "StageExecutionStatusType",
    "StageRetryModeType",
    "StageTransitionTypeType",
    "StartTimeRangeType",
    "TargetFilterNameType",
    "TriggerTypeType",
    "WebhookAuthenticationTypeType",
)

ActionCategoryType = Literal["Approval", "Build", "Compute", "Deploy", "Invoke", "Source", "Test"]
ActionConfigurationPropertyTypeType = Literal["Boolean", "Number", "String"]
ActionExecutionStatusType = Literal["Abandoned", "Failed", "InProgress", "Succeeded"]
ActionOwnerType = Literal["AWS", "Custom", "ThirdParty"]
ApprovalStatusType = Literal["Approved", "Rejected"]
ArtifactLocationTypeType = Literal["S3"]
ArtifactStoreTypeType = Literal["S3"]
BlockerTypeType = Literal["Schedule"]
ConditionExecutionStatusType = Literal[
    "Abandoned", "Cancelled", "Errored", "Failed", "InProgress", "Overridden", "Succeeded"
]
ConditionTypeType = Literal["BEFORE_ENTRY", "ON_SUCCESS"]
EncryptionKeyTypeType = Literal["KMS"]
EnvironmentVariableTypeType = Literal["PLAINTEXT", "SECRETS_MANAGER"]
ExecutionModeType = Literal["PARALLEL", "QUEUED", "SUPERSEDED"]
ExecutionTypeType = Literal["ROLLBACK", "STANDARD"]
ExecutorTypeType = Literal["JobWorker", "Lambda"]
FailureTypeType = Literal[
    "ConfigurationError",
    "JobFailed",
    "PermissionError",
    "RevisionOutOfSync",
    "RevisionUnavailable",
    "SystemUnavailable",
]
GitPullRequestEventTypeType = Literal["CLOSED", "OPEN", "UPDATED"]
JobStatusType = Literal[
    "Created", "Dispatched", "Failed", "InProgress", "Queued", "Succeeded", "TimedOut"
]
ListActionExecutionsPaginatorName = Literal["list_action_executions"]
ListActionTypesPaginatorName = Literal["list_action_types"]
ListDeployActionExecutionTargetsPaginatorName = Literal["list_deploy_action_execution_targets"]
ListPipelineExecutionsPaginatorName = Literal["list_pipeline_executions"]
ListPipelinesPaginatorName = Literal["list_pipelines"]
ListRuleExecutionsPaginatorName = Literal["list_rule_executions"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
ListWebhooksPaginatorName = Literal["list_webhooks"]
PipelineExecutionStatusType = Literal[
    "Cancelled", "Failed", "InProgress", "Stopped", "Stopping", "Succeeded", "Superseded"
]
PipelineTriggerProviderTypeType = Literal["CodeStarSourceConnection"]
PipelineTypeType = Literal["V1", "V2"]
ResultType = Literal["FAIL", "RETRY", "ROLLBACK", "SKIP"]
RetryTriggerType = Literal["AutomatedStageRetry", "ManualStageRetry"]
RuleCategoryType = Literal["Rule"]
RuleConfigurationPropertyTypeType = Literal["Boolean", "Number", "String"]
RuleExecutionStatusType = Literal["Abandoned", "Failed", "InProgress", "Succeeded"]
RuleOwnerType = Literal["AWS"]
SourceRevisionTypeType = Literal[
    "COMMIT_ID", "IMAGE_DIGEST", "S3_OBJECT_KEY", "S3_OBJECT_VERSION_ID"
]
StageExecutionStatusType = Literal[
    "Cancelled", "Failed", "InProgress", "Skipped", "Stopped", "Stopping", "Succeeded"
]
StageRetryModeType = Literal["ALL_ACTIONS", "FAILED_ACTIONS"]
StageTransitionTypeType = Literal["Inbound", "Outbound"]
StartTimeRangeType = Literal["All", "Latest"]
TargetFilterNameType = Literal["TARGET_STATUS"]
TriggerTypeType = Literal[
    "AutomatedRollback",
    "CloudWatchEvent",
    "CreatePipeline",
    "ManualRollback",
    "PollForSourceChanges",
    "PutActionRevision",
    "StartPipelineExecution",
    "Webhook",
    "WebhookV2",
]
WebhookAuthenticationTypeType = Literal["GITHUB_HMAC", "IP", "UNAUTHENTICATED"]
CodePipelineServiceName = Literal["codepipeline"]
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
    "list_action_executions",
    "list_action_types",
    "list_deploy_action_execution_targets",
    "list_pipeline_executions",
    "list_pipelines",
    "list_rule_executions",
    "list_tags_for_resource",
    "list_webhooks",
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
    "ca-central-1",
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
    "sa-east-1",
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",
]
