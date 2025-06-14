"""
Type annotations for firehose service literal definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_firehose/literals/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_firehose.literals import AmazonOpenSearchServerlessS3BackupModeType

    data: AmazonOpenSearchServerlessS3BackupModeType = "AllDocuments"
    ```
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AmazonOpenSearchServerlessS3BackupModeType",
    "AmazonopensearchserviceIndexRotationPeriodType",
    "AmazonopensearchserviceS3BackupModeType",
    "CompressionFormatType",
    "ConnectivityType",
    "ContentEncodingType",
    "DatabaseTypeType",
    "DefaultDocumentIdFormatType",
    "DeliveryStreamEncryptionStatusType",
    "DeliveryStreamFailureTypeType",
    "DeliveryStreamStatusType",
    "DeliveryStreamTypeType",
    "ElasticsearchIndexRotationPeriodType",
    "ElasticsearchS3BackupModeType",
    "FirehoseServiceName",
    "HECEndpointTypeType",
    "HttpEndpointS3BackupModeType",
    "IcebergS3BackupModeType",
    "KeyTypeType",
    "NoEncryptionConfigType",
    "OrcCompressionType",
    "OrcFormatVersionType",
    "ParquetCompressionType",
    "ParquetWriterVersionType",
    "ProcessorParameterNameType",
    "ProcessorTypeType",
    "RedshiftS3BackupModeType",
    "RegionName",
    "ResourceServiceName",
    "S3BackupModeType",
    "SSLModeType",
    "ServiceName",
    "SnapshotRequestedByType",
    "SnapshotStatusType",
    "SnowflakeDataLoadingOptionType",
    "SnowflakeS3BackupModeType",
    "SplunkS3BackupModeType",
)

AmazonOpenSearchServerlessS3BackupModeType = Literal["AllDocuments", "FailedDocumentsOnly"]
AmazonopensearchserviceIndexRotationPeriodType = Literal[
    "NoRotation", "OneDay", "OneHour", "OneMonth", "OneWeek"
]
AmazonopensearchserviceS3BackupModeType = Literal["AllDocuments", "FailedDocumentsOnly"]
CompressionFormatType = Literal["GZIP", "HADOOP_SNAPPY", "Snappy", "UNCOMPRESSED", "ZIP"]
ConnectivityType = Literal["PRIVATE", "PUBLIC"]
ContentEncodingType = Literal["GZIP", "NONE"]
DatabaseTypeType = Literal["MySQL", "PostgreSQL"]
DefaultDocumentIdFormatType = Literal["FIREHOSE_DEFAULT", "NO_DOCUMENT_ID"]
DeliveryStreamEncryptionStatusType = Literal[
    "DISABLED", "DISABLING", "DISABLING_FAILED", "ENABLED", "ENABLING", "ENABLING_FAILED"
]
DeliveryStreamFailureTypeType = Literal[
    "CREATE_ENI_FAILED",
    "CREATE_KMS_GRANT_FAILED",
    "DELETE_ENI_FAILED",
    "DISABLED_KMS_KEY",
    "ENI_ACCESS_DENIED",
    "INVALID_KMS_KEY",
    "KMS_ACCESS_DENIED",
    "KMS_KEY_NOT_FOUND",
    "KMS_OPT_IN_REQUIRED",
    "RETIRE_KMS_GRANT_FAILED",
    "SECURITY_GROUP_ACCESS_DENIED",
    "SECURITY_GROUP_NOT_FOUND",
    "SUBNET_ACCESS_DENIED",
    "SUBNET_NOT_FOUND",
    "UNKNOWN_ERROR",
    "VPC_ENDPOINT_SERVICE_NAME_NOT_FOUND",
    "VPC_INTERFACE_ENDPOINT_SERVICE_ACCESS_DENIED",
]
DeliveryStreamStatusType = Literal[
    "ACTIVE", "CREATING", "CREATING_FAILED", "DELETING", "DELETING_FAILED"
]
DeliveryStreamTypeType = Literal[
    "DatabaseAsSource", "DirectPut", "KinesisStreamAsSource", "MSKAsSource"
]
ElasticsearchIndexRotationPeriodType = Literal[
    "NoRotation", "OneDay", "OneHour", "OneMonth", "OneWeek"
]
ElasticsearchS3BackupModeType = Literal["AllDocuments", "FailedDocumentsOnly"]
HECEndpointTypeType = Literal["Event", "Raw"]
HttpEndpointS3BackupModeType = Literal["AllData", "FailedDataOnly"]
IcebergS3BackupModeType = Literal["AllData", "FailedDataOnly"]
KeyTypeType = Literal["AWS_OWNED_CMK", "CUSTOMER_MANAGED_CMK"]
NoEncryptionConfigType = Literal["NoEncryption"]
OrcCompressionType = Literal["NONE", "SNAPPY", "ZLIB"]
OrcFormatVersionType = Literal["V0_11", "V0_12"]
ParquetCompressionType = Literal["GZIP", "SNAPPY", "UNCOMPRESSED"]
ParquetWriterVersionType = Literal["V1", "V2"]
ProcessorParameterNameType = Literal[
    "BufferIntervalInSeconds",
    "BufferSizeInMBs",
    "CompressionFormat",
    "DataMessageExtraction",
    "Delimiter",
    "JsonParsingEngine",
    "LambdaArn",
    "MetadataExtractionQuery",
    "NumberOfRetries",
    "RoleArn",
    "SubRecordType",
]
ProcessorTypeType = Literal[
    "AppendDelimiterToRecord",
    "CloudWatchLogProcessing",
    "Decompression",
    "Lambda",
    "MetadataExtraction",
    "RecordDeAggregation",
]
RedshiftS3BackupModeType = Literal["Disabled", "Enabled"]
S3BackupModeType = Literal["Disabled", "Enabled"]
SSLModeType = Literal["Disabled", "Enabled"]
SnapshotRequestedByType = Literal["FIREHOSE", "USER"]
SnapshotStatusType = Literal["COMPLETE", "IN_PROGRESS", "SUSPENDED"]
SnowflakeDataLoadingOptionType = Literal[
    "JSON_MAPPING", "VARIANT_CONTENT_AND_METADATA_MAPPING", "VARIANT_CONTENT_MAPPING"
]
SnowflakeS3BackupModeType = Literal["AllData", "FailedDataOnly"]
SplunkS3BackupModeType = Literal["AllEvents", "FailedEventsOnly"]
FirehoseServiceName = Literal["firehose"]
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
    "privatenetworks",
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
