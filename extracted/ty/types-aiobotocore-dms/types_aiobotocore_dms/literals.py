"""
Type annotations for dms service literal definitions.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/literals/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from types_aiobotocore_dms.literals import AssessmentReportTypeType

    data: AssessmentReportTypeType = "csv"
    ```
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AssessmentReportTypeType",
    "AuthMechanismValueType",
    "AuthTypeValueType",
    "CannedAclForObjectsValueType",
    "CharLengthSemanticsType",
    "CollectorStatusType",
    "CompressionTypeValueType",
    "DataFormatValueType",
    "DatabaseMigrationServiceServiceName",
    "DatabaseModeType",
    "DatePartitionDelimiterValueType",
    "DatePartitionSequenceValueType",
    "DescribeCertificatesPaginatorName",
    "DescribeConnectionsPaginatorName",
    "DescribeDataMigrationsPaginatorName",
    "DescribeEndpointTypesPaginatorName",
    "DescribeEndpointsPaginatorName",
    "DescribeEventSubscriptionsPaginatorName",
    "DescribeEventsPaginatorName",
    "DescribeOrderableReplicationInstancesPaginatorName",
    "DescribeReplicationInstancesPaginatorName",
    "DescribeReplicationSubnetGroupsPaginatorName",
    "DescribeReplicationTaskAssessmentResultsPaginatorName",
    "DescribeReplicationTasksPaginatorName",
    "DescribeSchemasPaginatorName",
    "DescribeTableStatisticsPaginatorName",
    "DmsSslModeValueType",
    "EncodingTypeValueType",
    "EncryptionModeValueType",
    "EndpointDeletedWaiterName",
    "EndpointSettingTypeValueType",
    "KafkaSaslMechanismType",
    "KafkaSecurityProtocolType",
    "KafkaSslEndpointIdentificationAlgorithmType",
    "LongVarcharMappingTypeType",
    "MessageFormatValueType",
    "MigrationTypeValueType",
    "MySQLAuthenticationMethodType",
    "NestingLevelValueType",
    "OracleAuthenticationMethodType",
    "OriginTypeValueType",
    "PaginatorName",
    "ParquetVersionValueType",
    "PluginNameValueType",
    "PostgreSQLAuthenticationMethodType",
    "RedisAuthTypeValueType",
    "RefreshSchemasStatusTypeValueType",
    "RegionName",
    "ReleaseStatusValuesType",
    "ReloadOptionValueType",
    "ReplicationEndpointTypeValueType",
    "ReplicationInstanceAvailableWaiterName",
    "ReplicationInstanceDeletedWaiterName",
    "ReplicationTaskDeletedWaiterName",
    "ReplicationTaskReadyWaiterName",
    "ReplicationTaskRunningWaiterName",
    "ReplicationTaskStoppedWaiterName",
    "ResourceServiceName",
    "SafeguardPolicyType",
    "ServiceName",
    "SourceTypeType",
    "SqlServerAuthenticationMethodType",
    "SslSecurityProtocolValueType",
    "StartReplicationMigrationTypeValueType",
    "StartReplicationTaskTypeValueType",
    "TablePreparationModeType",
    "TargetDbTypeType",
    "TestConnectionSucceedsWaiterName",
    "TlogAccessModeType",
    "VersionStatusType",
    "WaiterName",
)


AssessmentReportTypeType = Literal["csv", "pdf"]
AuthMechanismValueType = Literal["default", "mongodb_cr", "scram_sha_1"]
AuthTypeValueType = Literal["no", "password"]
CannedAclForObjectsValueType = Literal[
    "authenticated-read",
    "aws-exec-read",
    "bucket-owner-full-control",
    "bucket-owner-read",
    "none",
    "private",
    "public-read",
    "public-read-write",
]
CharLengthSemanticsType = Literal["byte", "char", "default"]
CollectorStatusType = Literal["ACTIVE", "UNREGISTERED"]
CompressionTypeValueType = Literal["gzip", "none"]
DataFormatValueType = Literal["csv", "parquet"]
DatabaseModeType = Literal["babelfish", "default"]
DatePartitionDelimiterValueType = Literal["DASH", "NONE", "SLASH", "UNDERSCORE"]
DatePartitionSequenceValueType = Literal["DDMMYYYY", "MMYYYYDD", "YYYYMM", "YYYYMMDD", "YYYYMMDDHH"]
DescribeCertificatesPaginatorName = Literal["describe_certificates"]
DescribeConnectionsPaginatorName = Literal["describe_connections"]
DescribeDataMigrationsPaginatorName = Literal["describe_data_migrations"]
DescribeEndpointTypesPaginatorName = Literal["describe_endpoint_types"]
DescribeEndpointsPaginatorName = Literal["describe_endpoints"]
DescribeEventSubscriptionsPaginatorName = Literal["describe_event_subscriptions"]
DescribeEventsPaginatorName = Literal["describe_events"]
DescribeOrderableReplicationInstancesPaginatorName = Literal[
    "describe_orderable_replication_instances"
]
DescribeReplicationInstancesPaginatorName = Literal["describe_replication_instances"]
DescribeReplicationSubnetGroupsPaginatorName = Literal["describe_replication_subnet_groups"]
DescribeReplicationTaskAssessmentResultsPaginatorName = Literal[
    "describe_replication_task_assessment_results"
]
DescribeReplicationTasksPaginatorName = Literal["describe_replication_tasks"]
DescribeSchemasPaginatorName = Literal["describe_schemas"]
DescribeTableStatisticsPaginatorName = Literal["describe_table_statistics"]
DmsSslModeValueType = Literal["none", "require", "verify-ca", "verify-full"]
EncodingTypeValueType = Literal["plain", "plain-dictionary", "rle-dictionary"]
EncryptionModeValueType = Literal["sse-kms", "sse-s3"]
EndpointDeletedWaiterName = Literal["endpoint_deleted"]
EndpointSettingTypeValueType = Literal["boolean", "enum", "integer", "string"]
KafkaSaslMechanismType = Literal["plain", "scram-sha-512"]
KafkaSecurityProtocolType = Literal["plaintext", "sasl-ssl", "ssl-authentication", "ssl-encryption"]
KafkaSslEndpointIdentificationAlgorithmType = Literal["https", "none"]
LongVarcharMappingTypeType = Literal["clob", "nclob", "wstring"]
MessageFormatValueType = Literal["json", "json-unformatted"]
MigrationTypeValueType = Literal["cdc", "full-load", "full-load-and-cdc"]
MySQLAuthenticationMethodType = Literal["iam", "password"]
NestingLevelValueType = Literal["none", "one"]
OracleAuthenticationMethodType = Literal["kerberos", "password"]
OriginTypeValueType = Literal["SOURCE", "TARGET"]
ParquetVersionValueType = Literal["parquet-1-0", "parquet-2-0"]
PluginNameValueType = Literal["no-preference", "pglogical", "test-decoding"]
PostgreSQLAuthenticationMethodType = Literal["iam", "password"]
RedisAuthTypeValueType = Literal["auth-role", "auth-token", "none"]
RefreshSchemasStatusTypeValueType = Literal["failed", "refreshing", "successful"]
ReleaseStatusValuesType = Literal["beta", "prod"]
ReloadOptionValueType = Literal["data-reload", "validate-only"]
ReplicationEndpointTypeValueType = Literal["source", "target"]
ReplicationInstanceAvailableWaiterName = Literal["replication_instance_available"]
ReplicationInstanceDeletedWaiterName = Literal["replication_instance_deleted"]
ReplicationTaskDeletedWaiterName = Literal["replication_task_deleted"]
ReplicationTaskReadyWaiterName = Literal["replication_task_ready"]
ReplicationTaskRunningWaiterName = Literal["replication_task_running"]
ReplicationTaskStoppedWaiterName = Literal["replication_task_stopped"]
SafeguardPolicyType = Literal[
    "exclusive-automatic-truncation",
    "rely-on-sql-server-replication-agent",
    "shared-automatic-truncation",
]
SourceTypeType = Literal["replication-instance"]
SqlServerAuthenticationMethodType = Literal["kerberos", "password"]
SslSecurityProtocolValueType = Literal["plaintext", "ssl-encryption"]
StartReplicationMigrationTypeValueType = Literal[
    "reload-target", "resume-processing", "start-replication"
]
StartReplicationTaskTypeValueType = Literal[
    "reload-target", "resume-processing", "start-replication"
]
TablePreparationModeType = Literal["do-nothing", "drop-tables-on-target", "truncate"]
TargetDbTypeType = Literal["multiple-databases", "specific-database"]
TestConnectionSucceedsWaiterName = Literal["test_connection_succeeds"]
TlogAccessModeType = Literal["BackupOnly", "PreferBackup", "PreferTlog", "TlogOnly"]
VersionStatusType = Literal["OUTDATED", "UNSUPPORTED", "UP_TO_DATE"]
DatabaseMigrationServiceServiceName = Literal["dms"]
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
    "describe_certificates",
    "describe_connections",
    "describe_data_migrations",
    "describe_endpoint_types",
    "describe_endpoints",
    "describe_event_subscriptions",
    "describe_events",
    "describe_orderable_replication_instances",
    "describe_replication_instances",
    "describe_replication_subnet_groups",
    "describe_replication_task_assessment_results",
    "describe_replication_tasks",
    "describe_schemas",
    "describe_table_statistics",
]
WaiterName = Literal[
    "endpoint_deleted",
    "replication_instance_available",
    "replication_instance_deleted",
    "replication_task_deleted",
    "replication_task_ready",
    "replication_task_running",
    "replication_task_stopped",
    "test_connection_succeeds",
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
