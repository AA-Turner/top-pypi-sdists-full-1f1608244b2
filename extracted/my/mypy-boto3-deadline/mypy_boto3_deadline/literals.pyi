"""
Type annotations for deadline service literal definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/literals/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_deadline.literals import AcceleratorNameType

    data: AcceleratorNameType = "a10g"
    ```
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AcceleratorNameType",
    "AcceleratorTypeType",
    "AutoScalingModeType",
    "AutoScalingStatusType",
    "BudgetActionTypeType",
    "BudgetStatusType",
    "ComparisonOperatorType",
    "CompletedStatusType",
    "CpuArchitectureTypeType",
    "CreateJobTargetTaskRunStatusType",
    "CustomerManagedFleetOperatingSystemFamilyType",
    "DeadlineCloudServiceName",
    "DefaultQueueBudgetActionType",
    "DependencyConsumerResolutionStatusType",
    "DesiredWorkerStatusType",
    "Ec2MarketTypeType",
    "EnvironmentTemplateTypeType",
    "FileSystemLocationTypeType",
    "FleetActiveWaiterName",
    "FleetStatusType",
    "GetSessionsStatisticsAggregationPaginatorName",
    "JobAttachmentsFileSystemType",
    "JobCreateCompleteWaiterName",
    "JobEntityErrorCodeType",
    "JobLifecycleStatusType",
    "JobTargetTaskRunStatusType",
    "JobTemplateTypeType",
    "LicenseEndpointDeletedWaiterName",
    "LicenseEndpointStatusType",
    "LicenseEndpointValidWaiterName",
    "ListAvailableMeteredProductsPaginatorName",
    "ListBudgetsPaginatorName",
    "ListFarmMembersPaginatorName",
    "ListFarmsPaginatorName",
    "ListFleetMembersPaginatorName",
    "ListFleetsPaginatorName",
    "ListJobMembersPaginatorName",
    "ListJobParameterDefinitionsPaginatorName",
    "ListJobsPaginatorName",
    "ListLicenseEndpointsPaginatorName",
    "ListLimitsPaginatorName",
    "ListMeteredProductsPaginatorName",
    "ListMonitorsPaginatorName",
    "ListQueueEnvironmentsPaginatorName",
    "ListQueueFleetAssociationsPaginatorName",
    "ListQueueLimitAssociationsPaginatorName",
    "ListQueueMembersPaginatorName",
    "ListQueuesPaginatorName",
    "ListSessionActionsPaginatorName",
    "ListSessionsForWorkerPaginatorName",
    "ListSessionsPaginatorName",
    "ListStepConsumersPaginatorName",
    "ListStepDependenciesPaginatorName",
    "ListStepsPaginatorName",
    "ListStorageProfilesForQueuePaginatorName",
    "ListStorageProfilesPaginatorName",
    "ListTasksPaginatorName",
    "ListWorkersPaginatorName",
    "LogicalOperatorType",
    "MembershipLevelType",
    "PaginatorName",
    "PathFormatType",
    "PeriodType",
    "PrincipalTypeType",
    "QueueBlockedReasonType",
    "QueueFleetAssociationStatusType",
    "QueueFleetAssociationStoppedWaiterName",
    "QueueLimitAssociationStatusType",
    "QueueLimitAssociationStoppedWaiterName",
    "QueueSchedulingBlockedWaiterName",
    "QueueSchedulingWaiterName",
    "QueueStatusType",
    "ResourceServiceName",
    "RunAsType",
    "SearchTermMatchingTypeType",
    "ServiceManagedFleetOperatingSystemFamilyType",
    "ServiceName",
    "SessionActionStatusType",
    "SessionLifecycleStatusType",
    "SessionLifecycleTargetStatusType",
    "SessionsStatisticsAggregationStatusType",
    "SortOrderType",
    "StepLifecycleStatusType",
    "StepParameterTypeType",
    "StepTargetTaskRunStatusType",
    "StorageProfileOperatingSystemFamilyType",
    "TagPropagationModeType",
    "TaskRunStatusType",
    "TaskTargetRunStatusType",
    "UpdateJobLifecycleStatusType",
    "UpdateQueueFleetAssociationStatusType",
    "UpdateQueueLimitAssociationStatusType",
    "UpdatedWorkerStatusType",
    "UsageGroupByFieldType",
    "UsageStatisticType",
    "UsageTypeType",
    "WaiterName",
    "WorkerStatusType",
)

AcceleratorNameType = Literal["a10g", "l4", "l40s", "t4"]
AcceleratorTypeType = Literal["gpu"]
AutoScalingModeType = Literal["EVENT_BASED_AUTO_SCALING", "NO_SCALING"]
AutoScalingStatusType = Literal["GROWING", "SHRINKING", "STEADY"]
BudgetActionTypeType = Literal[
    "STOP_SCHEDULING_AND_CANCEL_TASKS", "STOP_SCHEDULING_AND_COMPLETE_TASKS"
]
BudgetStatusType = Literal["ACTIVE", "INACTIVE"]
ComparisonOperatorType = Literal[
    "EQUAL", "GREATER_THAN", "GREATER_THAN_EQUAL_TO", "LESS_THAN", "LESS_THAN_EQUAL_TO", "NOT_EQUAL"
]
CompletedStatusType = Literal["CANCELED", "FAILED", "INTERRUPTED", "NEVER_ATTEMPTED", "SUCCEEDED"]
CpuArchitectureTypeType = Literal["arm64", "x86_64"]
CreateJobTargetTaskRunStatusType = Literal["READY", "SUSPENDED"]
CustomerManagedFleetOperatingSystemFamilyType = Literal["LINUX", "MACOS", "WINDOWS"]
DefaultQueueBudgetActionType = Literal[
    "NONE", "STOP_SCHEDULING_AND_CANCEL_TASKS", "STOP_SCHEDULING_AND_COMPLETE_TASKS"
]
DependencyConsumerResolutionStatusType = Literal["RESOLVED", "UNRESOLVED"]
DesiredWorkerStatusType = Literal["STOPPED"]
Ec2MarketTypeType = Literal["on-demand", "spot"]
EnvironmentTemplateTypeType = Literal["JSON", "YAML"]
FileSystemLocationTypeType = Literal["LOCAL", "SHARED"]
FleetActiveWaiterName = Literal["fleet_active"]
FleetStatusType = Literal[
    "ACTIVE", "CREATE_FAILED", "CREATE_IN_PROGRESS", "UPDATE_FAILED", "UPDATE_IN_PROGRESS"
]
GetSessionsStatisticsAggregationPaginatorName = Literal["get_sessions_statistics_aggregation"]
JobAttachmentsFileSystemType = Literal["COPIED", "VIRTUAL"]
JobCreateCompleteWaiterName = Literal["job_create_complete"]
JobEntityErrorCodeType = Literal[
    "AccessDeniedException",
    "ConflictException",
    "InternalServerException",
    "MaxPayloadSizeExceeded",
    "ResourceNotFoundException",
    "ValidationException",
]
JobLifecycleStatusType = Literal[
    "ARCHIVED",
    "CREATE_COMPLETE",
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_SUCCEEDED",
    "UPLOAD_FAILED",
    "UPLOAD_IN_PROGRESS",
]
JobTargetTaskRunStatusType = Literal[
    "CANCELED", "FAILED", "PENDING", "READY", "SUCCEEDED", "SUSPENDED"
]
JobTemplateTypeType = Literal["JSON", "YAML"]
LicenseEndpointDeletedWaiterName = Literal["license_endpoint_deleted"]
LicenseEndpointStatusType = Literal[
    "CREATE_IN_PROGRESS", "DELETE_IN_PROGRESS", "NOT_READY", "READY"
]
LicenseEndpointValidWaiterName = Literal["license_endpoint_valid"]
ListAvailableMeteredProductsPaginatorName = Literal["list_available_metered_products"]
ListBudgetsPaginatorName = Literal["list_budgets"]
ListFarmMembersPaginatorName = Literal["list_farm_members"]
ListFarmsPaginatorName = Literal["list_farms"]
ListFleetMembersPaginatorName = Literal["list_fleet_members"]
ListFleetsPaginatorName = Literal["list_fleets"]
ListJobMembersPaginatorName = Literal["list_job_members"]
ListJobParameterDefinitionsPaginatorName = Literal["list_job_parameter_definitions"]
ListJobsPaginatorName = Literal["list_jobs"]
ListLicenseEndpointsPaginatorName = Literal["list_license_endpoints"]
ListLimitsPaginatorName = Literal["list_limits"]
ListMeteredProductsPaginatorName = Literal["list_metered_products"]
ListMonitorsPaginatorName = Literal["list_monitors"]
ListQueueEnvironmentsPaginatorName = Literal["list_queue_environments"]
ListQueueFleetAssociationsPaginatorName = Literal["list_queue_fleet_associations"]
ListQueueLimitAssociationsPaginatorName = Literal["list_queue_limit_associations"]
ListQueueMembersPaginatorName = Literal["list_queue_members"]
ListQueuesPaginatorName = Literal["list_queues"]
ListSessionActionsPaginatorName = Literal["list_session_actions"]
ListSessionsForWorkerPaginatorName = Literal["list_sessions_for_worker"]
ListSessionsPaginatorName = Literal["list_sessions"]
ListStepConsumersPaginatorName = Literal["list_step_consumers"]
ListStepDependenciesPaginatorName = Literal["list_step_dependencies"]
ListStepsPaginatorName = Literal["list_steps"]
ListStorageProfilesForQueuePaginatorName = Literal["list_storage_profiles_for_queue"]
ListStorageProfilesPaginatorName = Literal["list_storage_profiles"]
ListTasksPaginatorName = Literal["list_tasks"]
ListWorkersPaginatorName = Literal["list_workers"]
LogicalOperatorType = Literal["AND", "OR"]
MembershipLevelType = Literal["CONTRIBUTOR", "MANAGER", "OWNER", "VIEWER"]
PathFormatType = Literal["posix", "windows"]
PeriodType = Literal["DAILY", "HOURLY", "MONTHLY", "WEEKLY"]
PrincipalTypeType = Literal["GROUP", "USER"]
QueueBlockedReasonType = Literal["BUDGET_THRESHOLD_REACHED", "NO_BUDGET_CONFIGURED"]
QueueFleetAssociationStatusType = Literal[
    "ACTIVE", "STOPPED", "STOP_SCHEDULING_AND_CANCEL_TASKS", "STOP_SCHEDULING_AND_COMPLETE_TASKS"
]
QueueFleetAssociationStoppedWaiterName = Literal["queue_fleet_association_stopped"]
QueueLimitAssociationStatusType = Literal[
    "ACTIVE", "STOPPED", "STOP_LIMIT_USAGE_AND_CANCEL_TASKS", "STOP_LIMIT_USAGE_AND_COMPLETE_TASKS"
]
QueueLimitAssociationStoppedWaiterName = Literal["queue_limit_association_stopped"]
QueueSchedulingBlockedWaiterName = Literal["queue_scheduling_blocked"]
QueueSchedulingWaiterName = Literal["queue_scheduling"]
QueueStatusType = Literal["IDLE", "SCHEDULING", "SCHEDULING_BLOCKED"]
RunAsType = Literal["QUEUE_CONFIGURED_USER", "WORKER_AGENT_USER"]
SearchTermMatchingTypeType = Literal["CONTAINS", "FUZZY_MATCH"]
ServiceManagedFleetOperatingSystemFamilyType = Literal["LINUX", "WINDOWS"]
SessionActionStatusType = Literal[
    "ASSIGNED",
    "CANCELED",
    "CANCELING",
    "FAILED",
    "INTERRUPTED",
    "NEVER_ATTEMPTED",
    "RECLAIMED",
    "RECLAIMING",
    "RUNNING",
    "SCHEDULED",
    "SUCCEEDED",
]
SessionLifecycleStatusType = Literal[
    "ENDED", "STARTED", "UPDATE_FAILED", "UPDATE_IN_PROGRESS", "UPDATE_SUCCEEDED"
]
SessionLifecycleTargetStatusType = Literal["ENDED"]
SessionsStatisticsAggregationStatusType = Literal["COMPLETED", "FAILED", "IN_PROGRESS", "TIMEOUT"]
SortOrderType = Literal["ASCENDING", "DESCENDING"]
StepLifecycleStatusType = Literal[
    "CREATE_COMPLETE", "UPDATE_FAILED", "UPDATE_IN_PROGRESS", "UPDATE_SUCCEEDED"
]
StepParameterTypeType = Literal["FLOAT", "INT", "PATH", "STRING"]
StepTargetTaskRunStatusType = Literal[
    "CANCELED", "FAILED", "PENDING", "READY", "SUCCEEDED", "SUSPENDED"
]
StorageProfileOperatingSystemFamilyType = Literal["LINUX", "MACOS", "WINDOWS"]
TagPropagationModeType = Literal["NO_PROPAGATION", "PROPAGATE_TAGS_TO_WORKERS_AT_LAUNCH"]
TaskRunStatusType = Literal[
    "ASSIGNED",
    "CANCELED",
    "FAILED",
    "INTERRUPTING",
    "NOT_COMPATIBLE",
    "PENDING",
    "READY",
    "RUNNING",
    "SCHEDULED",
    "STARTING",
    "SUCCEEDED",
    "SUSPENDED",
]
TaskTargetRunStatusType = Literal[
    "CANCELED", "FAILED", "PENDING", "READY", "SUCCEEDED", "SUSPENDED"
]
UpdateJobLifecycleStatusType = Literal["ARCHIVED"]
UpdateQueueFleetAssociationStatusType = Literal[
    "ACTIVE", "STOP_SCHEDULING_AND_CANCEL_TASKS", "STOP_SCHEDULING_AND_COMPLETE_TASKS"
]
UpdateQueueLimitAssociationStatusType = Literal[
    "ACTIVE", "STOP_LIMIT_USAGE_AND_CANCEL_TASKS", "STOP_LIMIT_USAGE_AND_COMPLETE_TASKS"
]
UpdatedWorkerStatusType = Literal["STARTED", "STOPPED", "STOPPING"]
UsageGroupByFieldType = Literal[
    "FLEET_ID", "INSTANCE_TYPE", "JOB_ID", "LICENSE_PRODUCT", "QUEUE_ID", "USAGE_TYPE", "USER_ID"
]
UsageStatisticType = Literal["AVG", "MAX", "MIN", "SUM"]
UsageTypeType = Literal["COMPUTE", "LICENSE"]
WorkerStatusType = Literal[
    "CREATED",
    "IDLE",
    "NOT_COMPATIBLE",
    "NOT_RESPONDING",
    "RUNNING",
    "STARTED",
    "STOPPED",
    "STOPPING",
]
DeadlineCloudServiceName = Literal["deadline"]
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
    "get_sessions_statistics_aggregation",
    "list_available_metered_products",
    "list_budgets",
    "list_farm_members",
    "list_farms",
    "list_fleet_members",
    "list_fleets",
    "list_job_members",
    "list_job_parameter_definitions",
    "list_jobs",
    "list_license_endpoints",
    "list_limits",
    "list_metered_products",
    "list_monitors",
    "list_queue_environments",
    "list_queue_fleet_associations",
    "list_queue_limit_associations",
    "list_queue_members",
    "list_queues",
    "list_session_actions",
    "list_sessions",
    "list_sessions_for_worker",
    "list_step_consumers",
    "list_step_dependencies",
    "list_steps",
    "list_storage_profiles",
    "list_storage_profiles_for_queue",
    "list_tasks",
    "list_workers",
]
WaiterName = Literal[
    "fleet_active",
    "job_create_complete",
    "license_endpoint_deleted",
    "license_endpoint_valid",
    "queue_fleet_association_stopped",
    "queue_limit_association_stopped",
    "queue_scheduling",
    "queue_scheduling_blocked",
]
