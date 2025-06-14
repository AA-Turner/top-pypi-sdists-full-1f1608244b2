"""
Type annotations for route53resolver service literal definitions.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_route53resolver/literals/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from types_aiobotocore_route53resolver.literals import ActionType

    data: ActionType = "ALERT"
    ```
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ActionType",
    "AutodefinedReverseFlagType",
    "BlockOverrideDnsTypeType",
    "BlockResponseType",
    "ConfidenceThresholdType",
    "DnsThreatProtectionType",
    "FirewallDomainImportOperationType",
    "FirewallDomainListStatusType",
    "FirewallDomainRedirectionActionType",
    "FirewallDomainUpdateOperationType",
    "FirewallFailOpenStatusType",
    "FirewallRuleGroupAssociationStatusType",
    "FirewallRuleGroupStatusType",
    "IpAddressStatusType",
    "ListFirewallConfigsPaginatorName",
    "ListFirewallDomainListsPaginatorName",
    "ListFirewallDomainsPaginatorName",
    "ListFirewallRuleGroupAssociationsPaginatorName",
    "ListFirewallRuleGroupsPaginatorName",
    "ListFirewallRulesPaginatorName",
    "ListOutpostResolversPaginatorName",
    "ListResolverConfigsPaginatorName",
    "ListResolverDnssecConfigsPaginatorName",
    "ListResolverEndpointIpAddressesPaginatorName",
    "ListResolverEndpointsPaginatorName",
    "ListResolverQueryLogConfigAssociationsPaginatorName",
    "ListResolverQueryLogConfigsPaginatorName",
    "ListResolverRuleAssociationsPaginatorName",
    "ListResolverRulesPaginatorName",
    "ListTagsForResourcePaginatorName",
    "MutationProtectionStatusType",
    "OutpostResolverStatusType",
    "PaginatorName",
    "ProtocolType",
    "RegionName",
    "ResolverAutodefinedReverseStatusType",
    "ResolverDNSSECValidationStatusType",
    "ResolverEndpointDirectionType",
    "ResolverEndpointStatusType",
    "ResolverEndpointTypeType",
    "ResolverQueryLogConfigAssociationErrorType",
    "ResolverQueryLogConfigAssociationStatusType",
    "ResolverQueryLogConfigStatusType",
    "ResolverRuleAssociationStatusType",
    "ResolverRuleStatusType",
    "ResourceServiceName",
    "Route53ResolverServiceName",
    "RuleTypeOptionType",
    "ServiceName",
    "ShareStatusType",
    "SortOrderType",
    "ValidationType",
)


ActionType = Literal["ALERT", "ALLOW", "BLOCK"]
AutodefinedReverseFlagType = Literal["DISABLE", "ENABLE", "USE_LOCAL_RESOURCE_SETTING"]
BlockOverrideDnsTypeType = Literal["CNAME"]
BlockResponseType = Literal["NODATA", "NXDOMAIN", "OVERRIDE"]
ConfidenceThresholdType = Literal["HIGH", "LOW", "MEDIUM"]
DnsThreatProtectionType = Literal["DGA", "DNS_TUNNELING"]
FirewallDomainImportOperationType = Literal["REPLACE"]
FirewallDomainListStatusType = Literal[
    "COMPLETE", "COMPLETE_IMPORT_FAILED", "DELETING", "IMPORTING", "UPDATING"
]
FirewallDomainRedirectionActionType = Literal[
    "INSPECT_REDIRECTION_DOMAIN", "TRUST_REDIRECTION_DOMAIN"
]
FirewallDomainUpdateOperationType = Literal["ADD", "REMOVE", "REPLACE"]
FirewallFailOpenStatusType = Literal["DISABLED", "ENABLED", "USE_LOCAL_RESOURCE_SETTING"]
FirewallRuleGroupAssociationStatusType = Literal["COMPLETE", "DELETING", "UPDATING"]
FirewallRuleGroupStatusType = Literal["COMPLETE", "DELETING", "UPDATING"]
IpAddressStatusType = Literal[
    "ATTACHED",
    "ATTACHING",
    "CREATING",
    "DELETE_FAILED_FAS_EXPIRED",
    "DELETING",
    "DETACHING",
    "FAILED_CREATION",
    "FAILED_RESOURCE_GONE",
    "REMAP_ATTACHING",
    "REMAP_DETACHING",
    "UPDATE_FAILED",
    "UPDATING",
]
ListFirewallConfigsPaginatorName = Literal["list_firewall_configs"]
ListFirewallDomainListsPaginatorName = Literal["list_firewall_domain_lists"]
ListFirewallDomainsPaginatorName = Literal["list_firewall_domains"]
ListFirewallRuleGroupAssociationsPaginatorName = Literal["list_firewall_rule_group_associations"]
ListFirewallRuleGroupsPaginatorName = Literal["list_firewall_rule_groups"]
ListFirewallRulesPaginatorName = Literal["list_firewall_rules"]
ListOutpostResolversPaginatorName = Literal["list_outpost_resolvers"]
ListResolverConfigsPaginatorName = Literal["list_resolver_configs"]
ListResolverDnssecConfigsPaginatorName = Literal["list_resolver_dnssec_configs"]
ListResolverEndpointIpAddressesPaginatorName = Literal["list_resolver_endpoint_ip_addresses"]
ListResolverEndpointsPaginatorName = Literal["list_resolver_endpoints"]
ListResolverQueryLogConfigAssociationsPaginatorName = Literal[
    "list_resolver_query_log_config_associations"
]
ListResolverQueryLogConfigsPaginatorName = Literal["list_resolver_query_log_configs"]
ListResolverRuleAssociationsPaginatorName = Literal["list_resolver_rule_associations"]
ListResolverRulesPaginatorName = Literal["list_resolver_rules"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
MutationProtectionStatusType = Literal["DISABLED", "ENABLED"]
OutpostResolverStatusType = Literal[
    "ACTION_NEEDED",
    "CREATING",
    "DELETING",
    "FAILED_CREATION",
    "FAILED_DELETION",
    "OPERATIONAL",
    "UPDATING",
]
ProtocolType = Literal["Do53", "DoH", "DoH-FIPS"]
ResolverAutodefinedReverseStatusType = Literal[
    "DISABLED",
    "DISABLING",
    "ENABLED",
    "ENABLING",
    "UPDATING_TO_USE_LOCAL_RESOURCE_SETTING",
    "USE_LOCAL_RESOURCE_SETTING",
]
ResolverDNSSECValidationStatusType = Literal[
    "DISABLED",
    "DISABLING",
    "ENABLED",
    "ENABLING",
    "UPDATING_TO_USE_LOCAL_RESOURCE_SETTING",
    "USE_LOCAL_RESOURCE_SETTING",
]
ResolverEndpointDirectionType = Literal["INBOUND", "OUTBOUND"]
ResolverEndpointStatusType = Literal[
    "ACTION_NEEDED", "AUTO_RECOVERING", "CREATING", "DELETING", "OPERATIONAL", "UPDATING"
]
ResolverEndpointTypeType = Literal["DUALSTACK", "IPV4", "IPV6"]
ResolverQueryLogConfigAssociationErrorType = Literal[
    "ACCESS_DENIED", "DESTINATION_NOT_FOUND", "INTERNAL_SERVICE_ERROR", "NONE"
]
ResolverQueryLogConfigAssociationStatusType = Literal[
    "ACTION_NEEDED", "ACTIVE", "CREATING", "DELETING", "FAILED"
]
ResolverQueryLogConfigStatusType = Literal["CREATED", "CREATING", "DELETING", "FAILED"]
ResolverRuleAssociationStatusType = Literal[
    "COMPLETE", "CREATING", "DELETING", "FAILED", "OVERRIDDEN"
]
ResolverRuleStatusType = Literal["COMPLETE", "DELETING", "FAILED", "UPDATING"]
RuleTypeOptionType = Literal["FORWARD", "RECURSIVE", "SYSTEM"]
ShareStatusType = Literal["NOT_SHARED", "SHARED_BY_ME", "SHARED_WITH_ME"]
SortOrderType = Literal["ASCENDING", "DESCENDING"]
ValidationType = Literal["DISABLE", "ENABLE", "USE_LOCAL_RESOURCE_SETTING"]
Route53ResolverServiceName = Literal["route53resolver"]
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
    "list_firewall_configs",
    "list_firewall_domain_lists",
    "list_firewall_domains",
    "list_firewall_rule_group_associations",
    "list_firewall_rule_groups",
    "list_firewall_rules",
    "list_outpost_resolvers",
    "list_resolver_configs",
    "list_resolver_dnssec_configs",
    "list_resolver_endpoint_ip_addresses",
    "list_resolver_endpoints",
    "list_resolver_query_log_config_associations",
    "list_resolver_query_log_configs",
    "list_resolver_rule_associations",
    "list_resolver_rules",
    "list_tags_for_resource",
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
