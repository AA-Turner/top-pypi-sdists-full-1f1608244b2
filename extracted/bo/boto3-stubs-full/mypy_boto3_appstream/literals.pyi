"""
Type annotations for appstream service literal definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/literals/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_appstream.literals import AccessEndpointTypeType

    data: AccessEndpointTypeType = "STREAMING"
    ```
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AccessEndpointTypeType",
    "ActionType",
    "AppBlockBuilderAttributeType",
    "AppBlockBuilderPlatformTypeType",
    "AppBlockBuilderStateChangeReasonCodeType",
    "AppBlockBuilderStateType",
    "AppBlockStateType",
    "AppStreamServiceName",
    "AppVisibilityType",
    "ApplicationAttributeType",
    "AuthenticationTypeType",
    "CertificateBasedAuthStatusType",
    "DescribeDirectoryConfigsPaginatorName",
    "DescribeFleetsPaginatorName",
    "DescribeImageBuildersPaginatorName",
    "DescribeImagesPaginatorName",
    "DescribeSessionsPaginatorName",
    "DescribeStacksPaginatorName",
    "DescribeUserStackAssociationsPaginatorName",
    "DescribeUsersPaginatorName",
    "DynamicAppProvidersEnabledType",
    "FleetAttributeType",
    "FleetErrorCodeType",
    "FleetStartedWaiterName",
    "FleetStateType",
    "FleetStoppedWaiterName",
    "FleetTypeType",
    "ImageBuilderStateChangeReasonCodeType",
    "ImageBuilderStateType",
    "ImageSharedWithOthersType",
    "ImageStateChangeReasonCodeType",
    "ImageStateType",
    "LatestAppstreamAgentVersionType",
    "ListAssociatedFleetsPaginatorName",
    "ListAssociatedStacksPaginatorName",
    "MessageActionType",
    "PackagingTypeType",
    "PaginatorName",
    "PermissionType",
    "PlatformTypeType",
    "PreferredProtocolType",
    "RegionName",
    "ResourceServiceName",
    "ServiceName",
    "SessionConnectionStateType",
    "SessionStateType",
    "StackAttributeType",
    "StackErrorCodeType",
    "StorageConnectorTypeType",
    "StreamViewType",
    "ThemeAttributeType",
    "ThemeStateType",
    "ThemeStylingType",
    "UsageReportExecutionErrorCodeType",
    "UsageReportScheduleType",
    "UserStackAssociationErrorCodeType",
    "VisibilityTypeType",
    "WaiterName",
)

AccessEndpointTypeType = Literal["STREAMING"]
ActionType = Literal[
    "AUTO_TIME_ZONE_REDIRECTION",
    "CLIPBOARD_COPY_FROM_LOCAL_DEVICE",
    "CLIPBOARD_COPY_TO_LOCAL_DEVICE",
    "DOMAIN_PASSWORD_SIGNIN",
    "DOMAIN_SMART_CARD_SIGNIN",
    "FILE_DOWNLOAD",
    "FILE_UPLOAD",
    "PRINTING_TO_LOCAL_DEVICE",
]
AppBlockBuilderAttributeType = Literal[
    "ACCESS_ENDPOINTS", "IAM_ROLE_ARN", "VPC_CONFIGURATION_SECURITY_GROUP_IDS"
]
AppBlockBuilderPlatformTypeType = Literal["WINDOWS_SERVER_2019"]
AppBlockBuilderStateChangeReasonCodeType = Literal["INTERNAL_ERROR"]
AppBlockBuilderStateType = Literal["RUNNING", "STARTING", "STOPPED", "STOPPING"]
AppBlockStateType = Literal["ACTIVE", "INACTIVE"]
AppVisibilityType = Literal["ALL", "ASSOCIATED"]
ApplicationAttributeType = Literal["LAUNCH_PARAMETERS", "WORKING_DIRECTORY"]
AuthenticationTypeType = Literal["API", "AWS_AD", "SAML", "USERPOOL"]
CertificateBasedAuthStatusType = Literal[
    "DISABLED", "ENABLED", "ENABLED_NO_DIRECTORY_LOGIN_FALLBACK"
]
DescribeDirectoryConfigsPaginatorName = Literal["describe_directory_configs"]
DescribeFleetsPaginatorName = Literal["describe_fleets"]
DescribeImageBuildersPaginatorName = Literal["describe_image_builders"]
DescribeImagesPaginatorName = Literal["describe_images"]
DescribeSessionsPaginatorName = Literal["describe_sessions"]
DescribeStacksPaginatorName = Literal["describe_stacks"]
DescribeUserStackAssociationsPaginatorName = Literal["describe_user_stack_associations"]
DescribeUsersPaginatorName = Literal["describe_users"]
DynamicAppProvidersEnabledType = Literal["DISABLED", "ENABLED"]
FleetAttributeType = Literal[
    "DOMAIN_JOIN_INFO",
    "IAM_ROLE_ARN",
    "MAX_SESSIONS_PER_INSTANCE",
    "SESSION_SCRIPT_S3_LOCATION",
    "USB_DEVICE_FILTER_STRINGS",
    "VPC_CONFIGURATION",
    "VPC_CONFIGURATION_SECURITY_GROUP_IDS",
]
FleetErrorCodeType = Literal[
    "DOMAIN_JOIN_ERROR_ACCESS_DENIED",
    "DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED",
    "DOMAIN_JOIN_ERROR_FILE_NOT_FOUND",
    "DOMAIN_JOIN_ERROR_INVALID_PARAMETER",
    "DOMAIN_JOIN_ERROR_LOGON_FAILURE",
    "DOMAIN_JOIN_ERROR_MORE_DATA",
    "DOMAIN_JOIN_ERROR_NOT_SUPPORTED",
    "DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN",
    "DOMAIN_JOIN_INTERNAL_SERVICE_ERROR",
    "DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME",
    "DOMAIN_JOIN_NERR_PASSWORD_EXPIRED",
    "DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED",
    "FLEET_INSTANCE_PROVISIONING_FAILURE",
    "FLEET_STOPPED",
    "IAM_SERVICE_ROLE_IS_MISSING",
    "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION",
    "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION",
    "IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION",
    "IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION",
    "IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION",
    "IGW_NOT_ATTACHED",
    "IMAGE_NOT_FOUND",
    "INTERNAL_SERVICE_ERROR",
    "INVALID_SUBNET_CONFIGURATION",
    "MACHINE_ROLE_IS_MISSING",
    "NETWORK_INTERFACE_LIMIT_EXCEEDED",
    "SECURITY_GROUPS_NOT_FOUND",
    "STS_DISABLED_IN_REGION",
    "SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES",
    "SUBNET_NOT_FOUND",
]
FleetStartedWaiterName = Literal["fleet_started"]
FleetStateType = Literal["RUNNING", "STARTING", "STOPPED", "STOPPING"]
FleetStoppedWaiterName = Literal["fleet_stopped"]
FleetTypeType = Literal["ALWAYS_ON", "ELASTIC", "ON_DEMAND"]
ImageBuilderStateChangeReasonCodeType = Literal["IMAGE_UNAVAILABLE", "INTERNAL_ERROR"]
ImageBuilderStateType = Literal[
    "DELETING",
    "FAILED",
    "PENDING",
    "PENDING_QUALIFICATION",
    "REBOOTING",
    "RUNNING",
    "SNAPSHOTTING",
    "STOPPED",
    "STOPPING",
    "UPDATING",
    "UPDATING_AGENT",
]
ImageSharedWithOthersType = Literal["FALSE", "TRUE"]
ImageStateChangeReasonCodeType = Literal[
    "IMAGE_BUILDER_NOT_AVAILABLE", "IMAGE_COPY_FAILURE", "INTERNAL_ERROR"
]
ImageStateType = Literal[
    "AVAILABLE", "COPYING", "CREATING", "DELETING", "FAILED", "IMPORTING", "PENDING"
]
LatestAppstreamAgentVersionType = Literal["FALSE", "TRUE"]
ListAssociatedFleetsPaginatorName = Literal["list_associated_fleets"]
ListAssociatedStacksPaginatorName = Literal["list_associated_stacks"]
MessageActionType = Literal["RESEND", "SUPPRESS"]
PackagingTypeType = Literal["APPSTREAM2", "CUSTOM"]
PermissionType = Literal["DISABLED", "ENABLED"]
PlatformTypeType = Literal[
    "AMAZON_LINUX2",
    "RHEL8",
    "ROCKY_LINUX8",
    "WINDOWS",
    "WINDOWS_SERVER_2016",
    "WINDOWS_SERVER_2019",
    "WINDOWS_SERVER_2022",
]
PreferredProtocolType = Literal["TCP", "UDP"]
SessionConnectionStateType = Literal["CONNECTED", "NOT_CONNECTED"]
SessionStateType = Literal["ACTIVE", "EXPIRED", "PENDING"]
StackAttributeType = Literal[
    "ACCESS_ENDPOINTS",
    "EMBED_HOST_DOMAINS",
    "FEEDBACK_URL",
    "IAM_ROLE_ARN",
    "REDIRECT_URL",
    "STORAGE_CONNECTORS",
    "STORAGE_CONNECTOR_GOOGLE_DRIVE",
    "STORAGE_CONNECTOR_HOMEFOLDERS",
    "STORAGE_CONNECTOR_ONE_DRIVE",
    "STREAMING_EXPERIENCE_SETTINGS",
    "THEME_NAME",
    "USER_SETTINGS",
]
StackErrorCodeType = Literal["INTERNAL_SERVICE_ERROR", "STORAGE_CONNECTOR_ERROR"]
StorageConnectorTypeType = Literal["GOOGLE_DRIVE", "HOMEFOLDERS", "ONE_DRIVE"]
StreamViewType = Literal["APP", "DESKTOP"]
ThemeAttributeType = Literal["FOOTER_LINKS"]
ThemeStateType = Literal["DISABLED", "ENABLED"]
ThemeStylingType = Literal["BLUE", "LIGHT_BLUE", "PINK", "RED"]
UsageReportExecutionErrorCodeType = Literal[
    "ACCESS_DENIED", "INTERNAL_SERVICE_ERROR", "RESOURCE_NOT_FOUND"
]
UsageReportScheduleType = Literal["DAILY"]
UserStackAssociationErrorCodeType = Literal[
    "DIRECTORY_NOT_FOUND", "INTERNAL_ERROR", "STACK_NOT_FOUND", "USER_NAME_NOT_FOUND"
]
VisibilityTypeType = Literal["PRIVATE", "PUBLIC", "SHARED"]
AppStreamServiceName = Literal["appstream"]
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
    "describe_directory_configs",
    "describe_fleets",
    "describe_image_builders",
    "describe_images",
    "describe_sessions",
    "describe_stacks",
    "describe_user_stack_associations",
    "describe_users",
    "list_associated_fleets",
    "list_associated_stacks",
]
WaiterName = Literal["fleet_started", "fleet_stopped"]
RegionName = Literal[
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-south-1",
    "ap-southeast-1",
    "ap-southeast-2",
    "ca-central-1",
    "eu-central-1",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "sa-east-1",
    "us-east-1",
    "us-east-2",
    "us-west-2",
]
