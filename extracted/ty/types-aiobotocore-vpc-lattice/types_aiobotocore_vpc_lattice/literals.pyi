"""
Type annotations for vpc-lattice service literal definitions.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/literals/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from types_aiobotocore_vpc_lattice.literals import AuthPolicyStateType

    data: AuthPolicyStateType = "Active"
    ```
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AuthPolicyStateType",
    "AuthTypeType",
    "HealthCheckProtocolVersionType",
    "IpAddressTypeType",
    "LambdaEventStructureVersionType",
    "ListAccessLogSubscriptionsPaginatorName",
    "ListListenersPaginatorName",
    "ListResourceConfigurationsPaginatorName",
    "ListResourceEndpointAssociationsPaginatorName",
    "ListResourceGatewaysPaginatorName",
    "ListRulesPaginatorName",
    "ListServiceNetworkResourceAssociationsPaginatorName",
    "ListServiceNetworkServiceAssociationsPaginatorName",
    "ListServiceNetworkVpcAssociationsPaginatorName",
    "ListServiceNetworkVpcEndpointAssociationsPaginatorName",
    "ListServiceNetworksPaginatorName",
    "ListServicesPaginatorName",
    "ListTargetGroupsPaginatorName",
    "ListTargetsPaginatorName",
    "ListenerProtocolType",
    "PaginatorName",
    "ProtocolTypeType",
    "RegionName",
    "ResourceConfigurationIpAddressTypeType",
    "ResourceConfigurationStatusType",
    "ResourceConfigurationTypeType",
    "ResourceGatewayIpAddressTypeType",
    "ResourceGatewayStatusType",
    "ResourceServiceName",
    "ServiceName",
    "ServiceNetworkLogTypeType",
    "ServiceNetworkResourceAssociationStatusType",
    "ServiceNetworkServiceAssociationStatusType",
    "ServiceNetworkVpcAssociationStatusType",
    "ServiceStatusType",
    "TargetGroupProtocolType",
    "TargetGroupProtocolVersionType",
    "TargetGroupStatusType",
    "TargetGroupTypeType",
    "TargetStatusType",
    "VPCLatticeServiceName",
)

AuthPolicyStateType = Literal["Active", "Inactive"]
AuthTypeType = Literal["AWS_IAM", "NONE"]
HealthCheckProtocolVersionType = Literal["HTTP1", "HTTP2"]
IpAddressTypeType = Literal["IPV4", "IPV6"]
LambdaEventStructureVersionType = Literal["V1", "V2"]
ListAccessLogSubscriptionsPaginatorName = Literal["list_access_log_subscriptions"]
ListListenersPaginatorName = Literal["list_listeners"]
ListResourceConfigurationsPaginatorName = Literal["list_resource_configurations"]
ListResourceEndpointAssociationsPaginatorName = Literal["list_resource_endpoint_associations"]
ListResourceGatewaysPaginatorName = Literal["list_resource_gateways"]
ListRulesPaginatorName = Literal["list_rules"]
ListServiceNetworkResourceAssociationsPaginatorName = Literal[
    "list_service_network_resource_associations"
]
ListServiceNetworkServiceAssociationsPaginatorName = Literal[
    "list_service_network_service_associations"
]
ListServiceNetworkVpcAssociationsPaginatorName = Literal["list_service_network_vpc_associations"]
ListServiceNetworkVpcEndpointAssociationsPaginatorName = Literal[
    "list_service_network_vpc_endpoint_associations"
]
ListServiceNetworksPaginatorName = Literal["list_service_networks"]
ListServicesPaginatorName = Literal["list_services"]
ListTargetGroupsPaginatorName = Literal["list_target_groups"]
ListTargetsPaginatorName = Literal["list_targets"]
ListenerProtocolType = Literal["HTTP", "HTTPS", "TLS_PASSTHROUGH"]
ProtocolTypeType = Literal["TCP"]
ResourceConfigurationIpAddressTypeType = Literal["DUALSTACK", "IPV4", "IPV6"]
ResourceConfigurationStatusType = Literal[
    "ACTIVE",
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
]
ResourceConfigurationTypeType = Literal["ARN", "CHILD", "GROUP", "SINGLE"]
ResourceGatewayIpAddressTypeType = Literal["DUALSTACK", "IPV4", "IPV6"]
ResourceGatewayStatusType = Literal[
    "ACTIVE",
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
]
ServiceNetworkLogTypeType = Literal["RESOURCE", "SERVICE"]
ServiceNetworkResourceAssociationStatusType = Literal[
    "ACTIVE",
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "PARTIAL",
]
ServiceNetworkServiceAssociationStatusType = Literal[
    "ACTIVE", "CREATE_FAILED", "CREATE_IN_PROGRESS", "DELETE_FAILED", "DELETE_IN_PROGRESS"
]
ServiceNetworkVpcAssociationStatusType = Literal[
    "ACTIVE",
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
]
ServiceStatusType = Literal[
    "ACTIVE", "CREATE_FAILED", "CREATE_IN_PROGRESS", "DELETE_FAILED", "DELETE_IN_PROGRESS"
]
TargetGroupProtocolType = Literal["HTTP", "HTTPS", "TCP"]
TargetGroupProtocolVersionType = Literal["GRPC", "HTTP1", "HTTP2"]
TargetGroupStatusType = Literal[
    "ACTIVE", "CREATE_FAILED", "CREATE_IN_PROGRESS", "DELETE_FAILED", "DELETE_IN_PROGRESS"
]
TargetGroupTypeType = Literal["ALB", "INSTANCE", "IP", "LAMBDA"]
TargetStatusType = Literal["DRAINING", "HEALTHY", "INITIAL", "UNAVAILABLE", "UNHEALTHY", "UNUSED"]
VPCLatticeServiceName = Literal["vpc-lattice"]
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
    "sms-voice",
    "snow-device-management",
    "snowball",
    "sns",
    "socialmessaging",
    "sqs",
    "ssm",
    "ssm-contacts",
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
    "list_access_log_subscriptions",
    "list_listeners",
    "list_resource_configurations",
    "list_resource_endpoint_associations",
    "list_resource_gateways",
    "list_rules",
    "list_service_network_resource_associations",
    "list_service_network_service_associations",
    "list_service_network_vpc_associations",
    "list_service_network_vpc_endpoint_associations",
    "list_service_networks",
    "list_services",
    "list_target_groups",
    "list_targets",
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
    "me-central-1",
    "me-south-1",
    "sa-east-1",
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",
]
