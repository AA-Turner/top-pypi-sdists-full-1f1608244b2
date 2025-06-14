"""
Type annotations for migrationhubstrategy service literal definitions.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhubstrategy/literals/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from types_aiobotocore_migrationhubstrategy.literals import AnalysisTypeType

    data: AnalysisTypeType = "BINARY_ANALYSIS"
    ```
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AnalysisTypeType",
    "AntipatternReportStatusType",
    "AppTypeType",
    "AppUnitErrorCategoryType",
    "ApplicationComponentCriteriaType",
    "ApplicationModeType",
    "AssessmentDataSourceTypeType",
    "AssessmentStatusType",
    "AuthTypeType",
    "AwsManagedTargetDestinationType",
    "BinaryAnalyzerNameType",
    "CollectorHealthType",
    "ConditionType",
    "DataSourceTypeType",
    "DatabaseManagementPreferenceType",
    "GetServerDetailsPaginatorName",
    "GroupNameType",
    "HeterogeneousTargetDatabaseEngineType",
    "HomogeneousTargetDatabaseEngineType",
    "ImportFileTaskStatusType",
    "InclusionStatusType",
    "ListAnalyzableServersPaginatorName",
    "ListApplicationComponentsPaginatorName",
    "ListCollectorsPaginatorName",
    "ListImportFileTaskPaginatorName",
    "ListServersPaginatorName",
    "MigrationHubStrategyRecommendationsServiceName",
    "NoPreferenceTargetDestinationType",
    "OSTypeType",
    "OutputFormatType",
    "PaginatorName",
    "PipelineTypeType",
    "RecommendationReportStatusType",
    "RegionName",
    "ResourceServiceName",
    "ResourceSubTypeType",
    "RunTimeAnalyzerNameType",
    "RunTimeAssessmentStatusType",
    "RuntimeAnalysisStatusType",
    "SelfManageTargetDestinationType",
    "ServerCriteriaType",
    "ServerErrorCategoryType",
    "ServerOsTypeType",
    "ServiceName",
    "SeverityType",
    "SortOrderType",
    "SourceCodeAnalyzerNameType",
    "SrcCodeOrDbAnalysisStatusType",
    "StrategyRecommendationType",
    "StrategyType",
    "TargetDatabaseEngineType",
    "TargetDestinationType",
    "TransformationToolNameType",
    "VersionControlType",
    "VersionControlTypeType",
)

AnalysisTypeType = Literal[
    "BINARY_ANALYSIS", "DATABASE_ANALYSIS", "RUNTIME_ANALYSIS", "SOURCE_CODE_ANALYSIS"
]
AntipatternReportStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCESS"]
AppTypeType = Literal[
    "Cassandra",
    "DB2",
    "DotNetFramework",
    "Dotnet",
    "DotnetCore",
    "IBM WebSphere",
    "IIS",
    "JBoss",
    "Java",
    "Maria DB",
    "Mongo DB",
    "MySQL",
    "Oracle",
    "Oracle WebLogic",
    "Other",
    "PostgreSQLServer",
    "SQLServer",
    "Spring",
    "Sybase",
    "Tomcat",
    "Unknown",
    "Visual Basic",
]
AppUnitErrorCategoryType = Literal[
    "CONNECTIVITY_ERROR", "CREDENTIAL_ERROR", "OTHER_ERROR", "PERMISSION_ERROR", "UNSUPPORTED_ERROR"
]
ApplicationComponentCriteriaType = Literal[
    "ANALYSIS_STATUS",
    "APP_NAME",
    "APP_TYPE",
    "DESTINATION",
    "ERROR_CATEGORY",
    "NOT_DEFINED",
    "SERVER_ID",
    "STRATEGY",
]
ApplicationModeType = Literal["ALL", "KNOWN", "UNKNOWN"]
AssessmentDataSourceTypeType = Literal[
    "ApplicationDiscoveryService", "ManualImport", "StrategyRecommendationsApplicationDataCollector"
]
AssessmentStatusType = Literal["COMPLETE", "FAILED", "IN_PROGRESS", "STOPPED"]
AuthTypeType = Literal["CERT", "NTLM", "SSH"]
AwsManagedTargetDestinationType = Literal["AWS Elastic BeanStalk", "AWS Fargate", "None specified"]
BinaryAnalyzerNameType = Literal["BYTECODE_ANALYZER", "DLL_ANALYZER"]
CollectorHealthType = Literal["COLLECTOR_HEALTHY", "COLLECTOR_UNHEALTHY"]
ConditionType = Literal["CONTAINS", "EQUALS", "NOT_CONTAINS", "NOT_EQUALS"]
DataSourceTypeType = Literal[
    "ApplicationDiscoveryService",
    "Import",
    "MPA",
    "StrategyRecommendationsApplicationDataCollector",
]
DatabaseManagementPreferenceType = Literal["AWS-managed", "No preference", "Self-manage"]
GetServerDetailsPaginatorName = Literal["get_server_details"]
GroupNameType = Literal["ExternalId", "ExternalSourceType"]
HeterogeneousTargetDatabaseEngineType = Literal[
    "AWS PostgreSQL",
    "Amazon Aurora",
    "Db2 LUW",
    "MariaDB",
    "Microsoft SQL Server",
    "MongoDB",
    "MySQL",
    "None specified",
    "Oracle Database",
    "SAP",
]
HomogeneousTargetDatabaseEngineType = Literal["None specified"]
ImportFileTaskStatusType = Literal[
    "DeleteFailed",
    "DeleteInProgress",
    "DeletePartialSuccess",
    "DeleteSuccess",
    "ImportFailed",
    "ImportInProgress",
    "ImportPartialSuccess",
    "ImportSuccess",
]
InclusionStatusType = Literal["excludeFromAssessment", "includeInAssessment"]
ListAnalyzableServersPaginatorName = Literal["list_analyzable_servers"]
ListApplicationComponentsPaginatorName = Literal["list_application_components"]
ListCollectorsPaginatorName = Literal["list_collectors"]
ListImportFileTaskPaginatorName = Literal["list_import_file_task"]
ListServersPaginatorName = Literal["list_servers"]
NoPreferenceTargetDestinationType = Literal[
    "AWS Elastic BeanStalk",
    "AWS Fargate",
    "Amazon Elastic Cloud Compute (EC2)",
    "Amazon Elastic Container Service (ECS)",
    "Amazon Elastic Kubernetes Service (EKS)",
    "None specified",
]
OSTypeType = Literal["LINUX", "WINDOWS"]
OutputFormatType = Literal["Excel", "Json"]
PipelineTypeType = Literal["AZURE_DEVOPS"]
RecommendationReportStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCESS"]
ResourceSubTypeType = Literal["Database", "DatabaseProcess", "Process"]
RunTimeAnalyzerNameType = Literal[
    "A2C_ANALYZER", "DATABASE_ANALYZER", "EMP_PA_ANALYZER", "REHOST_ANALYZER", "SCT_ANALYZER"
]
RunTimeAssessmentStatusType = Literal[
    "dataCollectionTaskFailed",
    "dataCollectionTaskPartialSuccess",
    "dataCollectionTaskScheduled",
    "dataCollectionTaskStarted",
    "dataCollectionTaskStopped",
    "dataCollectionTaskSuccess",
    "dataCollectionTaskToBeScheduled",
]
RuntimeAnalysisStatusType = Literal[
    "ANALYSIS_FAILED", "ANALYSIS_STARTED", "ANALYSIS_SUCCESS", "ANALYSIS_TO_BE_SCHEDULED"
]
SelfManageTargetDestinationType = Literal[
    "Amazon Elastic Cloud Compute (EC2)",
    "Amazon Elastic Container Service (ECS)",
    "Amazon Elastic Kubernetes Service (EKS)",
    "None specified",
]
ServerCriteriaType = Literal[
    "ANALYSIS_STATUS",
    "DESTINATION",
    "ERROR_CATEGORY",
    "NOT_DEFINED",
    "OS_NAME",
    "SERVER_ID",
    "STRATEGY",
]
ServerErrorCategoryType = Literal[
    "ARCHITECTURE_ERROR",
    "CONNECTIVITY_ERROR",
    "CREDENTIAL_ERROR",
    "OTHER_ERROR",
    "PERMISSION_ERROR",
]
ServerOsTypeType = Literal[
    "AmazonLinux", "EndOfSupportWindowsServer", "Other", "Redhat", "WindowsServer"
]
SeverityType = Literal["HIGH", "LOW", "MEDIUM"]
SortOrderType = Literal["ASC", "DESC"]
SourceCodeAnalyzerNameType = Literal[
    "BYTECODE_ANALYZER", "CSHARP_ANALYZER", "JAVA_ANALYZER", "PORTING_ASSISTANT"
]
SrcCodeOrDbAnalysisStatusType = Literal[
    "ANALYSIS_FAILED",
    "ANALYSIS_PARTIAL_SUCCESS",
    "ANALYSIS_STARTED",
    "ANALYSIS_SUCCESS",
    "ANALYSIS_TO_BE_SCHEDULED",
    "CONFIGURED",
    "UNCONFIGURED",
]
StrategyRecommendationType = Literal["notRecommended", "potential", "recommended", "viableOption"]
StrategyType = Literal[
    "Refactor", "Rehost", "Relocate", "Replatform", "Repurchase", "Retain", "Retirement"
]
TargetDatabaseEngineType = Literal[
    "AWS PostgreSQL",
    "Amazon Aurora",
    "Db2 LUW",
    "MariaDB",
    "Microsoft SQL Server",
    "MongoDB",
    "MySQL",
    "None specified",
    "Oracle Database",
    "SAP",
]
TargetDestinationType = Literal[
    "AWS Elastic BeanStalk",
    "AWS Fargate",
    "Amazon DocumentDB",
    "Amazon DynamoDB",
    "Amazon Elastic Cloud Compute (EC2)",
    "Amazon Elastic Container Service (ECS)",
    "Amazon Elastic Kubernetes Service (EKS)",
    "Amazon Relational Database Service",
    "Amazon Relational Database Service on MySQL",
    "Amazon Relational Database Service on PostgreSQL",
    "Aurora MySQL",
    "Aurora PostgreSQL",
    "Babelfish for Aurora PostgreSQL",
    "None specified",
]
TransformationToolNameType = Literal[
    "App2Container",
    "Application Migration Service",
    "Database Migration Service",
    "End of Support Migration",
    "In Place Operating System Upgrade",
    "Native SQL Server Backup/Restore",
    "Porting Assistant For .NET",
    "Schema Conversion Tool",
    "Strategy Recommendation Support",
    "Windows Web Application Migration Assistant",
]
VersionControlType = Literal["AZURE_DEVOPS_GIT", "GITHUB", "GITHUB_ENTERPRISE"]
VersionControlTypeType = Literal["AZURE_DEVOPS_GIT", "GITHUB", "GITHUB_ENTERPRISE"]
MigrationHubStrategyRecommendationsServiceName = Literal["migrationhubstrategy"]
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
    "get_server_details",
    "list_analyzable_servers",
    "list_application_components",
    "list_collectors",
    "list_import_file_task",
    "list_servers",
]
RegionName = Literal[
    "ap-northeast-1",
    "ap-southeast-2",
    "eu-central-1",
    "eu-west-1",
    "eu-west-2",
    "us-east-1",
    "us-west-2",
]
