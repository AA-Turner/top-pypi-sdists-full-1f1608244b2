"""
Type annotations for pca-connector-ad service literal definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/literals/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_pca_connector_ad.literals import AccessRightType

    data: AccessRightType = "ALLOW"
    ```
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AccessRightType",
    "ApplicationPolicyTypeType",
    "ClientCompatibilityV2Type",
    "ClientCompatibilityV3Type",
    "ClientCompatibilityV4Type",
    "ConnectorStatusReasonType",
    "ConnectorStatusType",
    "DirectoryRegistrationStatusReasonType",
    "DirectoryRegistrationStatusType",
    "HashAlgorithmType",
    "IpAddressTypeType",
    "KeySpecType",
    "KeyUsagePropertyTypeType",
    "ListConnectorsPaginatorName",
    "ListDirectoryRegistrationsPaginatorName",
    "ListServicePrincipalNamesPaginatorName",
    "ListTemplateGroupAccessControlEntriesPaginatorName",
    "ListTemplatesPaginatorName",
    "PaginatorName",
    "PcaConnectorAdServiceName",
    "PrivateKeyAlgorithmType",
    "ResourceServiceName",
    "ServiceName",
    "ServicePrincipalNameStatusReasonType",
    "ServicePrincipalNameStatusType",
    "TemplateStatusType",
    "ValidityPeriodTypeType",
)


AccessRightType = Literal["ALLOW", "DENY"]
ApplicationPolicyTypeType = Literal[
    "ALL_APPLICATION_POLICIES",
    "ANY_PURPOSE",
    "ATTESTATION_IDENTITY_KEY_CERTIFICATE",
    "CERTIFICATE_REQUEST_AGENT",
    "CLIENT_AUTHENTICATION",
    "CODE_SIGNING",
    "CTL_USAGE",
    "DIGITAL_RIGHTS",
    "DIRECTORY_SERVICE_EMAIL_REPLICATION",
    "DISALLOWED_LIST",
    "DNS_SERVER_TRUST",
    "DOCUMENT_ENCRYPTION",
    "DOCUMENT_SIGNING",
    "DYNAMIC_CODE_GENERATOR",
    "EARLY_LAUNCH_ANTIMALWARE_DRIVER",
    "EMBEDDED_WINDOWS_SYSTEM_COMPONENT_VERIFICATION",
    "ENCLAVE",
    "ENCRYPTING_FILE_SYSTEM",
    "ENDORSEMENT_KEY_CERTIFICATE",
    "FILE_RECOVERY",
    "HAL_EXTENSION",
    "IP_SECURITY_END_SYSTEM",
    "IP_SECURITY_IKE_INTERMEDIATE",
    "IP_SECURITY_TUNNEL_TERMINATION",
    "IP_SECURITY_USER",
    "ISOLATED_USER_MODE",
    "KDC_AUTHENTICATION",
    "KERNEL_MODE_CODE_SIGNING",
    "KEY_PACK_LICENSES",
    "KEY_RECOVERY",
    "KEY_RECOVERY_AGENT",
    "LICENSE_SERVER_VERIFICATION",
    "LIFETIME_SIGNING",
    "MICROSOFT_PUBLISHER",
    "MICROSOFT_TIME_STAMPING",
    "MICROSOFT_TRUST_LIST_SIGNING",
    "OCSP_SIGNING",
    "OEM_WINDOWS_SYSTEM_COMPONENT_VERIFICATION",
    "PLATFORM_CERTIFICATE",
    "PREVIEW_BUILD_SIGNING",
    "PRIVATE_KEY_ARCHIVAL",
    "PROTECTED_PROCESS_LIGHT_VERIFICATION",
    "PROTECTED_PROCESS_VERIFICATION",
    "QUALIFIED_SUBORDINATION",
    "REVOKED_LIST_SIGNER",
    "ROOT_LIST_SIGNER",
    "ROOT_PROGRAM_AUTO_UPDATE_CA_REVOCATION",
    "ROOT_PROGRAM_AUTO_UPDATE_END_REVOCATION",
    "ROOT_PROGRAM_NO_OSCP_FAILOVER_TO_CRL",
    "SECURE_EMAIL",
    "SERVER_AUTHENTICATION",
    "SMART_CARD_LOGIN",
    "SPC_ENCRYPTED_DIGEST_RETRY_COUNT",
    "SPC_RELAXED_PE_MARKER_CHECK",
    "TIME_STAMPING",
    "WINDOWS_HARDWARE_DRIVER_ATTESTED_VERIFICATION",
    "WINDOWS_HARDWARE_DRIVER_EXTENDED_VERIFICATION",
    "WINDOWS_HARDWARE_DRIVER_VERIFICATION",
    "WINDOWS_HELLO_RECOVERY_KEY_ENCRYPTION",
    "WINDOWS_KITS_COMPONENT",
    "WINDOWS_RT_VERIFICATION",
    "WINDOWS_SOFTWARE_EXTENSION_VERIFICATION",
    "WINDOWS_STORE",
    "WINDOWS_SYSTEM_COMPONENT_VERIFICATION",
    "WINDOWS_TCB_COMPONENT",
    "WINDOWS_THIRD_PARTY_APPLICATION_COMPONENT",
    "WINDOWS_UPDATE",
]
ClientCompatibilityV2Type = Literal[
    "WINDOWS_SERVER_2003",
    "WINDOWS_SERVER_2008",
    "WINDOWS_SERVER_2008_R2",
    "WINDOWS_SERVER_2012",
    "WINDOWS_SERVER_2012_R2",
    "WINDOWS_SERVER_2016",
]
ClientCompatibilityV3Type = Literal[
    "WINDOWS_SERVER_2008",
    "WINDOWS_SERVER_2008_R2",
    "WINDOWS_SERVER_2012",
    "WINDOWS_SERVER_2012_R2",
    "WINDOWS_SERVER_2016",
]
ClientCompatibilityV4Type = Literal[
    "WINDOWS_SERVER_2012", "WINDOWS_SERVER_2012_R2", "WINDOWS_SERVER_2016"
]
ConnectorStatusReasonType = Literal[
    "CA_CERTIFICATE_REGISTRATION_FAILED",
    "DIRECTORY_ACCESS_DENIED",
    "INSUFFICIENT_FREE_ADDRESSES",
    "INTERNAL_FAILURE",
    "INVALID_SUBNET_IP_PROTOCOL",
    "PRIVATECA_ACCESS_DENIED",
    "PRIVATECA_RESOURCE_NOT_FOUND",
    "SECURITY_GROUP_NOT_IN_VPC",
    "VPC_ACCESS_DENIED",
    "VPC_ENDPOINT_LIMIT_EXCEEDED",
    "VPC_RESOURCE_NOT_FOUND",
]
ConnectorStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED"]
DirectoryRegistrationStatusReasonType = Literal[
    "DIRECTORY_ACCESS_DENIED",
    "DIRECTORY_NOT_ACTIVE",
    "DIRECTORY_NOT_REACHABLE",
    "DIRECTORY_RESOURCE_NOT_FOUND",
    "DIRECTORY_TYPE_NOT_SUPPORTED",
    "INTERNAL_FAILURE",
]
DirectoryRegistrationStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED"]
HashAlgorithmType = Literal["SHA256", "SHA384", "SHA512"]
IpAddressTypeType = Literal["DUALSTACK", "IPV4"]
KeySpecType = Literal["KEY_EXCHANGE", "SIGNATURE"]
KeyUsagePropertyTypeType = Literal["ALL"]
ListConnectorsPaginatorName = Literal["list_connectors"]
ListDirectoryRegistrationsPaginatorName = Literal["list_directory_registrations"]
ListServicePrincipalNamesPaginatorName = Literal["list_service_principal_names"]
ListTemplateGroupAccessControlEntriesPaginatorName = Literal[
    "list_template_group_access_control_entries"
]
ListTemplatesPaginatorName = Literal["list_templates"]
PrivateKeyAlgorithmType = Literal["ECDH_P256", "ECDH_P384", "ECDH_P521", "RSA"]
ServicePrincipalNameStatusReasonType = Literal[
    "DIRECTORY_ACCESS_DENIED",
    "DIRECTORY_NOT_REACHABLE",
    "DIRECTORY_RESOURCE_NOT_FOUND",
    "INTERNAL_FAILURE",
    "SPN_EXISTS_ON_DIFFERENT_AD_OBJECT",
    "SPN_LIMIT_EXCEEDED",
]
ServicePrincipalNameStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED"]
TemplateStatusType = Literal["ACTIVE", "DELETING"]
ValidityPeriodTypeType = Literal["DAYS", "HOURS", "MONTHS", "WEEKS", "YEARS"]
PcaConnectorAdServiceName = Literal["pca-connector-ad"]
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
    "list_connectors",
    "list_directory_registrations",
    "list_service_principal_names",
    "list_template_group_access_control_entries",
    "list_templates",
]
