from datetime import datetime
from enum import StrEnum
from typing import Dict, List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

Arn = str
AwsBackupRecoveryPointArn = str
BlueGreenDeploymentIdentifier = str
BlueGreenDeploymentName = str
BlueGreenDeploymentStatus = str
BlueGreenDeploymentStatusDetails = str
BlueGreenDeploymentTaskName = str
BlueGreenDeploymentTaskStatus = str
Boolean = bool
BooleanOptional = bool
BucketName = str
CustomDBEngineVersionManifest = str
CustomEngineName = str
CustomEngineVersion = str
DBClusterIdentifier = str
DBProxyEndpointName = str
DBProxyName = str
DBShardGroupIdentifier = str
DataFilter = str
DatabaseArn = str
Description = str
Double = float
DoubleOptional = float
Engine = str
GlobalClusterIdentifier = str
Integer = int
IntegerOptional = int
IntegrationArn = str
IntegrationDescription = str
IntegrationIdentifier = str
IntegrationName = str
KmsKeyIdOrArn = str
MajorEngineVersion = str
Marker = str
MaxRecords = int
SensitiveString = str
SourceArn = str
String = str
String255 = str
SwitchoverDetailStatus = str
SwitchoverTimeout = int
TargetDBClusterParameterGroupName = str
TargetDBInstanceClass = str
TargetDBParameterGroupName = str
TargetEngineVersion = str
TargetStorageType = str


class ActivityStreamMode(StrEnum):
    sync = "sync"
    async_ = "async"


class ActivityStreamPolicyStatus(StrEnum):
    locked = "locked"
    unlocked = "unlocked"
    locking_policy = "locking-policy"
    unlocking_policy = "unlocking-policy"


class ActivityStreamStatus(StrEnum):
    stopped = "stopped"
    starting = "starting"
    started = "started"
    stopping = "stopping"


class ApplyMethod(StrEnum):
    immediate = "immediate"
    pending_reboot = "pending-reboot"


class AuditPolicyState(StrEnum):
    locked = "locked"
    unlocked = "unlocked"


class AuthScheme(StrEnum):
    SECRETS = "SECRETS"


class AutomationMode(StrEnum):
    full = "full"
    all_paused = "all-paused"


class ClientPasswordAuthType(StrEnum):
    MYSQL_NATIVE_PASSWORD = "MYSQL_NATIVE_PASSWORD"
    MYSQL_CACHING_SHA2_PASSWORD = "MYSQL_CACHING_SHA2_PASSWORD"
    POSTGRES_SCRAM_SHA_256 = "POSTGRES_SCRAM_SHA_256"
    POSTGRES_MD5 = "POSTGRES_MD5"
    SQL_SERVER_AUTHENTICATION = "SQL_SERVER_AUTHENTICATION"


class ClusterScalabilityType(StrEnum):
    standard = "standard"
    limitless = "limitless"


class CustomEngineVersionStatus(StrEnum):
    available = "available"
    inactive = "inactive"
    inactive_except_restore = "inactive-except-restore"


class DBProxyEndpointStatus(StrEnum):
    available = "available"
    modifying = "modifying"
    incompatible_network = "incompatible-network"
    insufficient_resource_limits = "insufficient-resource-limits"
    creating = "creating"
    deleting = "deleting"


class DBProxyEndpointTargetRole(StrEnum):
    READ_WRITE = "READ_WRITE"
    READ_ONLY = "READ_ONLY"


class DBProxyStatus(StrEnum):
    available = "available"
    modifying = "modifying"
    incompatible_network = "incompatible-network"
    insufficient_resource_limits = "insufficient-resource-limits"
    creating = "creating"
    deleting = "deleting"
    suspended = "suspended"
    suspending = "suspending"
    reactivating = "reactivating"


class DatabaseInsightsMode(StrEnum):
    standard = "standard"
    advanced = "advanced"


class EngineFamily(StrEnum):
    MYSQL = "MYSQL"
    POSTGRESQL = "POSTGRESQL"
    SQLSERVER = "SQLSERVER"


class ExportSourceType(StrEnum):
    SNAPSHOT = "SNAPSHOT"
    CLUSTER = "CLUSTER"


class FailoverStatus(StrEnum):
    pending = "pending"
    failing_over = "failing-over"
    cancelling = "cancelling"


class GlobalClusterMemberSynchronizationStatus(StrEnum):
    connected = "connected"
    pending_resync = "pending-resync"


class IAMAuthMode(StrEnum):
    DISABLED = "DISABLED"
    REQUIRED = "REQUIRED"
    ENABLED = "ENABLED"


class IntegrationStatus(StrEnum):
    creating = "creating"
    active = "active"
    modifying = "modifying"
    failed = "failed"
    deleting = "deleting"
    syncing = "syncing"
    needs_attention = "needs_attention"


class LifecycleSupportName(StrEnum):
    open_source_rds_standard_support = "open-source-rds-standard-support"
    open_source_rds_extended_support = "open-source-rds-extended-support"


class LimitlessDatabaseStatus(StrEnum):
    active = "active"
    not_in_use = "not-in-use"
    enabled = "enabled"
    disabled = "disabled"
    enabling = "enabling"
    disabling = "disabling"
    modifying_max_capacity = "modifying-max-capacity"
    error = "error"


class LocalWriteForwardingStatus(StrEnum):
    enabled = "enabled"
    disabled = "disabled"
    enabling = "enabling"
    disabling = "disabling"
    requested = "requested"


class ReplicaMode(StrEnum):
    open_read_only = "open-read-only"
    mounted = "mounted"


class SourceType(StrEnum):
    db_instance = "db-instance"
    db_parameter_group = "db-parameter-group"
    db_security_group = "db-security-group"
    db_snapshot = "db-snapshot"
    db_cluster = "db-cluster"
    db_cluster_snapshot = "db-cluster-snapshot"
    custom_engine_version = "custom-engine-version"
    db_proxy = "db-proxy"
    blue_green_deployment = "blue-green-deployment"


class TargetHealthReason(StrEnum):
    UNREACHABLE = "UNREACHABLE"
    CONNECTION_FAILED = "CONNECTION_FAILED"
    AUTH_FAILURE = "AUTH_FAILURE"
    PENDING_PROXY_CAPACITY = "PENDING_PROXY_CAPACITY"
    INVALID_REPLICATION_STATE = "INVALID_REPLICATION_STATE"


class TargetRole(StrEnum):
    READ_WRITE = "READ_WRITE"
    READ_ONLY = "READ_ONLY"
    UNKNOWN = "UNKNOWN"


class TargetState(StrEnum):
    REGISTERING = "REGISTERING"
    AVAILABLE = "AVAILABLE"
    UNAVAILABLE = "UNAVAILABLE"


class TargetType(StrEnum):
    RDS_INSTANCE = "RDS_INSTANCE"
    RDS_SERVERLESS_ENDPOINT = "RDS_SERVERLESS_ENDPOINT"
    TRACKED_CLUSTER = "TRACKED_CLUSTER"


class WriteForwardingStatus(StrEnum):
    enabled = "enabled"
    disabled = "disabled"
    enabling = "enabling"
    disabling = "disabling"
    unknown = "unknown"


class AuthorizationAlreadyExistsFault(ServiceException):
    """The specified CIDR IP range or Amazon EC2 security group is already
    authorized for the specified DB security group.
    """

    code: str = "AuthorizationAlreadyExists"
    sender_fault: bool = True
    status_code: int = 400


class AuthorizationNotFoundFault(ServiceException):
    """The specified CIDR IP range or Amazon EC2 security group might not be
    authorized for the specified DB security group.

    Or, RDS might not be authorized to perform necessary actions using IAM
    on your behalf.
    """

    code: str = "AuthorizationNotFound"
    sender_fault: bool = True
    status_code: int = 404


class AuthorizationQuotaExceededFault(ServiceException):
    """The DB security group authorization quota has been reached."""

    code: str = "AuthorizationQuotaExceeded"
    sender_fault: bool = True
    status_code: int = 400


class BackupPolicyNotFoundFault(ServiceException):
    code: str = "BackupPolicyNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404


class BlueGreenDeploymentAlreadyExistsFault(ServiceException):
    """A blue/green deployment with the specified name already exists."""

    code: str = "BlueGreenDeploymentAlreadyExistsFault"
    sender_fault: bool = True
    status_code: int = 400


class BlueGreenDeploymentNotFoundFault(ServiceException):
    """``BlueGreenDeploymentIdentifier`` doesn't refer to an existing
    blue/green deployment.
    """

    code: str = "BlueGreenDeploymentNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404


class CertificateNotFoundFault(ServiceException):
    """``CertificateIdentifier`` doesn't refer to an existing certificate."""

    code: str = "CertificateNotFound"
    sender_fault: bool = True
    status_code: int = 404


class CreateCustomDBEngineVersionFault(ServiceException):
    """An error occurred while trying to create the CEV."""

    code: str = "CreateCustomDBEngineVersionFault"
    sender_fault: bool = True
    status_code: int = 400


class CustomAvailabilityZoneNotFoundFault(ServiceException):
    """``CustomAvailabilityZoneId`` doesn't refer to an existing custom
    Availability Zone identifier.
    """

    code: str = "CustomAvailabilityZoneNotFound"
    sender_fault: bool = True
    status_code: int = 404


class CustomDBEngineVersionAlreadyExistsFault(ServiceException):
    """A CEV with the specified name already exists."""

    code: str = "CustomDBEngineVersionAlreadyExistsFault"
    sender_fault: bool = True
    status_code: int = 400


class CustomDBEngineVersionNotFoundFault(ServiceException):
    """The specified CEV was not found."""

    code: str = "CustomDBEngineVersionNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404


class CustomDBEngineVersionQuotaExceededFault(ServiceException):
    """You have exceeded your CEV quota."""

    code: str = "CustomDBEngineVersionQuotaExceededFault"
    sender_fault: bool = True
    status_code: int = 400


class DBClusterAlreadyExistsFault(ServiceException):
    """The user already has a DB cluster with the given identifier."""

    code: str = "DBClusterAlreadyExistsFault"
    sender_fault: bool = True
    status_code: int = 400


class DBClusterAutomatedBackupNotFoundFault(ServiceException):
    """No automated backup for this DB cluster was found."""

    code: str = "DBClusterAutomatedBackupNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404


class DBClusterAutomatedBackupQuotaExceededFault(ServiceException):
    """The quota for retained automated backups was exceeded. This prevents you
    from retaining any additional automated backups. The retained automated
    backups quota is the same as your DB cluster quota.
    """

    code: str = "DBClusterAutomatedBackupQuotaExceededFault"
    sender_fault: bool = True
    status_code: int = 400


class DBClusterBacktrackNotFoundFault(ServiceException):
    """``BacktrackIdentifier`` doesn't refer to an existing backtrack."""

    code: str = "DBClusterBacktrackNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404


class DBClusterEndpointAlreadyExistsFault(ServiceException):
    """The specified custom endpoint can't be created because it already
    exists.
    """

    code: str = "DBClusterEndpointAlreadyExistsFault"
    sender_fault: bool = True
    status_code: int = 400


class DBClusterEndpointNotFoundFault(ServiceException):
    """The specified custom endpoint doesn't exist."""

    code: str = "DBClusterEndpointNotFoundFault"
    sender_fault: bool = True
    status_code: int = 400


class DBClusterEndpointQuotaExceededFault(ServiceException):
    """The cluster already has the maximum number of custom endpoints."""

    code: str = "DBClusterEndpointQuotaExceededFault"
    sender_fault: bool = True
    status_code: int = 403


class DBClusterNotFoundFault(ServiceException):
    """``DBClusterIdentifier`` doesn't refer to an existing DB cluster."""

    code: str = "DBClusterNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404


class DBClusterParameterGroupNotFoundFault(ServiceException):
    """``DBClusterParameterGroupName`` doesn't refer to an existing DB cluster
    parameter group.
    """

    code: str = "DBClusterParameterGroupNotFound"
    sender_fault: bool = True
    status_code: int = 404


class DBClusterQuotaExceededFault(ServiceException):
    """The user attempted to create a new DB cluster and the user has already
    reached the maximum allowed DB cluster quota.
    """

    code: str = "DBClusterQuotaExceededFault"
    sender_fault: bool = True
    status_code: int = 403


class DBClusterRoleAlreadyExistsFault(ServiceException):
    """The specified IAM role Amazon Resource Name (ARN) is already associated
    with the specified DB cluster.
    """

    code: str = "DBClusterRoleAlreadyExists"
    sender_fault: bool = True
    status_code: int = 400


class DBClusterRoleNotFoundFault(ServiceException):
    """The specified IAM role Amazon Resource Name (ARN) isn't associated with
    the specified DB cluster.
    """

    code: str = "DBClusterRoleNotFound"
    sender_fault: bool = True
    status_code: int = 404


class DBClusterRoleQuotaExceededFault(ServiceException):
    """You have exceeded the maximum number of IAM roles that can be associated
    with the specified DB cluster.
    """

    code: str = "DBClusterRoleQuotaExceeded"
    sender_fault: bool = True
    status_code: int = 400


class DBClusterSnapshotAlreadyExistsFault(ServiceException):
    """The user already has a DB cluster snapshot with the given identifier."""

    code: str = "DBClusterSnapshotAlreadyExistsFault"
    sender_fault: bool = True
    status_code: int = 400


class DBClusterSnapshotNotFoundFault(ServiceException):
    """``DBClusterSnapshotIdentifier`` doesn't refer to an existing DB cluster
    snapshot.
    """

    code: str = "DBClusterSnapshotNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404


class DBInstanceAlreadyExistsFault(ServiceException):
    """The user already has a DB instance with the given identifier."""

    code: str = "DBInstanceAlreadyExists"
    sender_fault: bool = True
    status_code: int = 400


class DBInstanceAutomatedBackupNotFoundFault(ServiceException):
    """No automated backup for this DB instance was found."""

    code: str = "DBInstanceAutomatedBackupNotFound"
    sender_fault: bool = True
    status_code: int = 404


class DBInstanceAutomatedBackupQuotaExceededFault(ServiceException):
    """The quota for retained automated backups was exceeded. This prevents you
    from retaining any additional automated backups. The retained automated
    backups quota is the same as your DB instance quota.
    """

    code: str = "DBInstanceAutomatedBackupQuotaExceeded"
    sender_fault: bool = True
    status_code: int = 400


class DBInstanceNotFoundFault(ServiceException):
    """``DBInstanceIdentifier`` doesn't refer to an existing DB instance."""

    code: str = "DBInstanceNotFound"
    sender_fault: bool = True
    status_code: int = 404


class DBInstanceNotReadyFault(ServiceException):
    """An attempt to download or examine log files didn't succeed because an
    Aurora Serverless v2 instance was paused.
    """

    code: str = "DBInstanceNotReady"
    sender_fault: bool = False
    status_code: int = 503


class DBInstanceRoleAlreadyExistsFault(ServiceException):
    """The specified ``RoleArn`` or ``FeatureName`` value is already associated
    with the DB instance.
    """

    code: str = "DBInstanceRoleAlreadyExists"
    sender_fault: bool = True
    status_code: int = 400


class DBInstanceRoleNotFoundFault(ServiceException):
    """The specified ``RoleArn`` value doesn't match the specified feature for
    the DB instance.
    """

    code: str = "DBInstanceRoleNotFound"
    sender_fault: bool = True
    status_code: int = 404


class DBInstanceRoleQuotaExceededFault(ServiceException):
    """You can't associate any more Amazon Web Services Identity and Access
    Management (IAM) roles with the DB instance because the quota has been
    reached.
    """

    code: str = "DBInstanceRoleQuotaExceeded"
    sender_fault: bool = True
    status_code: int = 400


class DBLogFileNotFoundFault(ServiceException):
    """``LogFileName`` doesn't refer to an existing DB log file."""

    code: str = "DBLogFileNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404


class DBParameterGroupAlreadyExistsFault(ServiceException):
    """A DB parameter group with the same name exists."""

    code: str = "DBParameterGroupAlreadyExists"
    sender_fault: bool = True
    status_code: int = 400


class DBParameterGroupNotFoundFault(ServiceException):
    """``DBParameterGroupName`` doesn't refer to an existing DB parameter
    group.
    """

    code: str = "DBParameterGroupNotFound"
    sender_fault: bool = True
    status_code: int = 404


class DBParameterGroupQuotaExceededFault(ServiceException):
    """The request would result in the user exceeding the allowed number of DB
    parameter groups.
    """

    code: str = "DBParameterGroupQuotaExceeded"
    sender_fault: bool = True
    status_code: int = 400


class DBProxyAlreadyExistsFault(ServiceException):
    """The specified proxy name must be unique for all proxies owned by your
    Amazon Web Services account in the specified Amazon Web Services Region.
    """

    code: str = "DBProxyAlreadyExistsFault"
    sender_fault: bool = True
    status_code: int = 400


class DBProxyEndpointAlreadyExistsFault(ServiceException):
    """The specified DB proxy endpoint name must be unique for all DB proxy
    endpoints owned by your Amazon Web Services account in the specified
    Amazon Web Services Region.
    """

    code: str = "DBProxyEndpointAlreadyExistsFault"
    sender_fault: bool = True
    status_code: int = 400


class DBProxyEndpointNotFoundFault(ServiceException):
    """The DB proxy endpoint doesn't exist."""

    code: str = "DBProxyEndpointNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404


class DBProxyEndpointQuotaExceededFault(ServiceException):
    """The DB proxy already has the maximum number of endpoints."""

    code: str = "DBProxyEndpointQuotaExceededFault"
    sender_fault: bool = True
    status_code: int = 400


class DBProxyNotFoundFault(ServiceException):
    """The specified proxy name doesn't correspond to a proxy owned by your
    Amazon Web Services account in the specified Amazon Web Services Region.
    """

    code: str = "DBProxyNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404


class DBProxyQuotaExceededFault(ServiceException):
    """Your Amazon Web Services account already has the maximum number of
    proxies in the specified Amazon Web Services Region.
    """

    code: str = "DBProxyQuotaExceededFault"
    sender_fault: bool = True
    status_code: int = 400


class DBProxyTargetAlreadyRegisteredFault(ServiceException):
    """The proxy is already associated with the specified RDS DB instance or
    Aurora DB cluster.
    """

    code: str = "DBProxyTargetAlreadyRegisteredFault"
    sender_fault: bool = True
    status_code: int = 400


class DBProxyTargetGroupNotFoundFault(ServiceException):
    """The specified target group isn't available for a proxy owned by your
    Amazon Web Services account in the specified Amazon Web Services Region.
    """

    code: str = "DBProxyTargetGroupNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404


class DBProxyTargetNotFoundFault(ServiceException):
    """The specified RDS DB instance or Aurora DB cluster isn't available for a
    proxy owned by your Amazon Web Services account in the specified Amazon
    Web Services Region.
    """

    code: str = "DBProxyTargetNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404


class DBSecurityGroupAlreadyExistsFault(ServiceException):
    """A DB security group with the name specified in ``DBSecurityGroupName``
    already exists.
    """

    code: str = "DBSecurityGroupAlreadyExists"
    sender_fault: bool = True
    status_code: int = 400


class DBSecurityGroupNotFoundFault(ServiceException):
    """``DBSecurityGroupName`` doesn't refer to an existing DB security group."""

    code: str = "DBSecurityGroupNotFound"
    sender_fault: bool = True
    status_code: int = 404


class DBSecurityGroupNotSupportedFault(ServiceException):
    """A DB security group isn't allowed for this action."""

    code: str = "DBSecurityGroupNotSupported"
    sender_fault: bool = True
    status_code: int = 400


class DBSecurityGroupQuotaExceededFault(ServiceException):
    """The request would result in the user exceeding the allowed number of DB
    security groups.
    """

    code: str = "QuotaExceeded.DBSecurityGroup"
    sender_fault: bool = True
    status_code: int = 400


class DBShardGroupAlreadyExistsFault(ServiceException):
    """The specified DB shard group name must be unique in your Amazon Web
    Services account in the specified Amazon Web Services Region.
    """

    code: str = "DBShardGroupAlreadyExists"
    sender_fault: bool = True
    status_code: int = 400


class DBShardGroupNotFoundFault(ServiceException):
    """The specified DB shard group name wasn't found."""

    code: str = "DBShardGroupNotFound"
    sender_fault: bool = True
    status_code: int = 404


class DBSnapshotAlreadyExistsFault(ServiceException):
    """``DBSnapshotIdentifier`` is already used by an existing snapshot."""

    code: str = "DBSnapshotAlreadyExists"
    sender_fault: bool = True
    status_code: int = 400


class DBSnapshotNotFoundFault(ServiceException):
    """``DBSnapshotIdentifier`` doesn't refer to an existing DB snapshot."""

    code: str = "DBSnapshotNotFound"
    sender_fault: bool = True
    status_code: int = 404


class DBSnapshotTenantDatabaseNotFoundFault(ServiceException):
    """The specified snapshot tenant database wasn't found."""

    code: str = "DBSnapshotTenantDatabaseNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404


class DBSubnetGroupAlreadyExistsFault(ServiceException):
    """``DBSubnetGroupName`` is already used by an existing DB subnet group."""

    code: str = "DBSubnetGroupAlreadyExists"
    sender_fault: bool = True
    status_code: int = 400


class DBSubnetGroupDoesNotCoverEnoughAZs(ServiceException):
    """Subnets in the DB subnet group should cover at least two Availability
    Zones unless there is only one Availability Zone.
    """

    code: str = "DBSubnetGroupDoesNotCoverEnoughAZs"
    sender_fault: bool = True
    status_code: int = 400


class DBSubnetGroupNotAllowedFault(ServiceException):
    """The DBSubnetGroup shouldn't be specified while creating read replicas
    that lie in the same region as the source instance.
    """

    code: str = "DBSubnetGroupNotAllowedFault"
    sender_fault: bool = True
    status_code: int = 400


class DBSubnetGroupNotFoundFault(ServiceException):
    """``DBSubnetGroupName`` doesn't refer to an existing DB subnet group."""

    code: str = "DBSubnetGroupNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404


class DBSubnetGroupQuotaExceededFault(ServiceException):
    """The request would result in the user exceeding the allowed number of DB
    subnet groups.
    """

    code: str = "DBSubnetGroupQuotaExceeded"
    sender_fault: bool = True
    status_code: int = 400


class DBSubnetQuotaExceededFault(ServiceException):
    """The request would result in the user exceeding the allowed number of
    subnets in a DB subnet groups.
    """

    code: str = "DBSubnetQuotaExceededFault"
    sender_fault: bool = True
    status_code: int = 400


class DBUpgradeDependencyFailureFault(ServiceException):
    """The DB upgrade failed because a resource the DB depends on can't be
    modified.
    """

    code: str = "DBUpgradeDependencyFailure"
    sender_fault: bool = True
    status_code: int = 400


class DomainNotFoundFault(ServiceException):
    """``Domain`` doesn't refer to an existing Active Directory domain."""

    code: str = "DomainNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404


class Ec2ImagePropertiesNotSupportedFault(ServiceException):
    """The AMI configuration prerequisite has not been met."""

    code: str = "Ec2ImagePropertiesNotSupportedFault"
    sender_fault: bool = True
    status_code: int = 400


class EventSubscriptionQuotaExceededFault(ServiceException):
    """You have reached the maximum number of event subscriptions."""

    code: str = "EventSubscriptionQuotaExceeded"
    sender_fault: bool = True
    status_code: int = 400


class ExportTaskAlreadyExistsFault(ServiceException):
    """You can't start an export task that's already running."""

    code: str = "ExportTaskAlreadyExists"
    sender_fault: bool = True
    status_code: int = 400


class ExportTaskNotFoundFault(ServiceException):
    """The export task doesn't exist."""

    code: str = "ExportTaskNotFound"
    sender_fault: bool = True
    status_code: int = 404


class GlobalClusterAlreadyExistsFault(ServiceException):
    """The ``GlobalClusterIdentifier`` already exists. Specify a new global
    database identifier (unique name) to create a new global database
    cluster or to rename an existing one.
    """

    code: str = "GlobalClusterAlreadyExistsFault"
    sender_fault: bool = True
    status_code: int = 400


class GlobalClusterNotFoundFault(ServiceException):
    """The ``GlobalClusterIdentifier`` doesn't refer to an existing global
    database cluster.
    """

    code: str = "GlobalClusterNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404


class GlobalClusterQuotaExceededFault(ServiceException):
    """The number of global database clusters for this account is already at
    the maximum allowed.
    """

    code: str = "GlobalClusterQuotaExceededFault"
    sender_fault: bool = True
    status_code: int = 400


class IamRoleMissingPermissionsFault(ServiceException):
    """The IAM role requires additional permissions to export to an Amazon S3
    bucket.
    """

    code: str = "IamRoleMissingPermissions"
    sender_fault: bool = True
    status_code: int = 400


class IamRoleNotFoundFault(ServiceException):
    """The IAM role is missing for exporting to an Amazon S3 bucket."""

    code: str = "IamRoleNotFound"
    sender_fault: bool = True
    status_code: int = 404


class InstanceQuotaExceededFault(ServiceException):
    """The request would result in the user exceeding the allowed number of DB
    instances.
    """

    code: str = "InstanceQuotaExceeded"
    sender_fault: bool = True
    status_code: int = 400


class InsufficientAvailableIPsInSubnetFault(ServiceException):
    """The requested operation can't be performed because there aren't enough
    available IP addresses in the proxy's subnets. Add more CIDR blocks to
    the VPC or remove IP address that aren't required from the subnets.
    """

    code: str = "InsufficientAvailableIPsInSubnetFault"
    sender_fault: bool = True
    status_code: int = 400


class InsufficientDBClusterCapacityFault(ServiceException):
    """The DB cluster doesn't have enough capacity for the current operation."""

    code: str = "InsufficientDBClusterCapacityFault"
    sender_fault: bool = True
    status_code: int = 403


class InsufficientDBInstanceCapacityFault(ServiceException):
    """The specified DB instance class isn't available in the specified
    Availability Zone.
    """

    code: str = "InsufficientDBInstanceCapacity"
    sender_fault: bool = True
    status_code: int = 400


class InsufficientStorageClusterCapacityFault(ServiceException):
    """There is insufficient storage available for the current action. You
    might be able to resolve this error by updating your subnet group to use
    different Availability Zones that have more storage available.
    """

    code: str = "InsufficientStorageClusterCapacity"
    sender_fault: bool = True
    status_code: int = 400


class IntegrationAlreadyExistsFault(ServiceException):
    """The integration you are trying to create already exists."""

    code: str = "IntegrationAlreadyExistsFault"
    sender_fault: bool = True
    status_code: int = 400


class IntegrationConflictOperationFault(ServiceException):
    """A conflicting conditional operation is currently in progress against
    this resource. Typically occurs when there are multiple requests being
    made to the same resource at the same time, and these requests conflict
    with each other.
    """

    code: str = "IntegrationConflictOperationFault"
    sender_fault: bool = True
    status_code: int = 400


class IntegrationNotFoundFault(ServiceException):
    """The specified integration could not be found."""

    code: str = "IntegrationNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404


class IntegrationQuotaExceededFault(ServiceException):
    """You can't crate any more zero-ETL integrations because the quota has
    been reached.
    """

    code: str = "IntegrationQuotaExceededFault"
    sender_fault: bool = True
    status_code: int = 400


class InvalidBlueGreenDeploymentStateFault(ServiceException):
    """The blue/green deployment can't be switched over or deleted because
    there is an invalid configuration in the green environment.
    """

    code: str = "InvalidBlueGreenDeploymentStateFault"
    sender_fault: bool = True
    status_code: int = 400


class InvalidCustomDBEngineVersionStateFault(ServiceException):
    """You can't delete the CEV."""

    code: str = "InvalidCustomDBEngineVersionStateFault"
    sender_fault: bool = True
    status_code: int = 400


class InvalidDBClusterAutomatedBackupStateFault(ServiceException):
    """The automated backup is in an invalid state. For example, this automated
    backup is associated with an active cluster.
    """

    code: str = "InvalidDBClusterAutomatedBackupStateFault"
    sender_fault: bool = True
    status_code: int = 400


class InvalidDBClusterCapacityFault(ServiceException):
    """``Capacity`` isn't a valid Aurora Serverless DB cluster capacity. Valid
    capacity values are ``2``, ``4``, ``8``, ``16``, ``32``, ``64``,
    ``128``, and ``256``.
    """

    code: str = "InvalidDBClusterCapacityFault"
    sender_fault: bool = True
    status_code: int = 400


class InvalidDBClusterEndpointStateFault(ServiceException):
    """The requested operation can't be performed on the endpoint while the
    endpoint is in this state.
    """

    code: str = "InvalidDBClusterEndpointStateFault"
    sender_fault: bool = True
    status_code: int = 400


class InvalidDBClusterSnapshotStateFault(ServiceException):
    """The supplied value isn't a valid DB cluster snapshot state."""

    code: str = "InvalidDBClusterSnapshotStateFault"
    sender_fault: bool = True
    status_code: int = 400


class InvalidDBClusterStateFault(ServiceException):
    """The requested operation can't be performed while the cluster is in this
    state.
    """

    code: str = "InvalidDBClusterStateFault"
    sender_fault: bool = True
    status_code: int = 400


class InvalidDBInstanceAutomatedBackupStateFault(ServiceException):
    """The automated backup is in an invalid state. For example, this automated
    backup is associated with an active instance.
    """

    code: str = "InvalidDBInstanceAutomatedBackupState"
    sender_fault: bool = True
    status_code: int = 400


class InvalidDBInstanceStateFault(ServiceException):
    """The DB instance isn't in a valid state."""

    code: str = "InvalidDBInstanceState"
    sender_fault: bool = True
    status_code: int = 400


class InvalidDBParameterGroupStateFault(ServiceException):
    """The DB parameter group is in use or is in an invalid state. If you are
    attempting to delete the parameter group, you can't delete it when the
    parameter group is in this state.
    """

    code: str = "InvalidDBParameterGroupState"
    sender_fault: bool = True
    status_code: int = 400


class InvalidDBProxyEndpointStateFault(ServiceException):
    """You can't perform this operation while the DB proxy endpoint is in a
    particular state.
    """

    code: str = "InvalidDBProxyEndpointStateFault"
    sender_fault: bool = True
    status_code: int = 400


class InvalidDBProxyStateFault(ServiceException):
    """The requested operation can't be performed while the proxy is in this
    state.
    """

    code: str = "InvalidDBProxyStateFault"
    sender_fault: bool = True
    status_code: int = 400


class InvalidDBSecurityGroupStateFault(ServiceException):
    """The state of the DB security group doesn't allow deletion."""

    code: str = "InvalidDBSecurityGroupState"
    sender_fault: bool = True
    status_code: int = 400


class InvalidDBShardGroupStateFault(ServiceException):
    """The DB shard group must be in the available state."""

    code: str = "InvalidDBShardGroupState"
    sender_fault: bool = True
    status_code: int = 400


class InvalidDBSnapshotStateFault(ServiceException):
    """The state of the DB snapshot doesn't allow deletion."""

    code: str = "InvalidDBSnapshotState"
    sender_fault: bool = True
    status_code: int = 400


class InvalidDBSubnetGroupFault(ServiceException):
    """The DBSubnetGroup doesn't belong to the same VPC as that of an existing
    cross-region read replica of the same source instance.
    """

    code: str = "InvalidDBSubnetGroupFault"
    sender_fault: bool = True
    status_code: int = 400


class InvalidDBSubnetGroupStateFault(ServiceException):
    """The DB subnet group cannot be deleted because it's in use."""

    code: str = "InvalidDBSubnetGroupStateFault"
    sender_fault: bool = True
    status_code: int = 400


class InvalidDBSubnetStateFault(ServiceException):
    """The DB subnet isn't in the *available* state."""

    code: str = "InvalidDBSubnetStateFault"
    sender_fault: bool = True
    status_code: int = 400


class InvalidEventSubscriptionStateFault(ServiceException):
    """This error can occur if someone else is modifying a subscription. You
    should retry the action.
    """

    code: str = "InvalidEventSubscriptionState"
    sender_fault: bool = True
    status_code: int = 400


class InvalidExportOnlyFault(ServiceException):
    """The export is invalid for exporting to an Amazon S3 bucket."""

    code: str = "InvalidExportOnly"
    sender_fault: bool = True
    status_code: int = 400


class InvalidExportSourceStateFault(ServiceException):
    """The state of the export snapshot is invalid for exporting to an Amazon
    S3 bucket.
    """

    code: str = "InvalidExportSourceState"
    sender_fault: bool = True
    status_code: int = 400


class InvalidExportTaskStateFault(ServiceException):
    """You can't cancel an export task that has completed."""

    code: str = "InvalidExportTaskStateFault"
    sender_fault: bool = True
    status_code: int = 400


class InvalidGlobalClusterStateFault(ServiceException):
    """The global cluster is in an invalid state and can't perform the
    requested operation.
    """

    code: str = "InvalidGlobalClusterStateFault"
    sender_fault: bool = True
    status_code: int = 400


class InvalidIntegrationStateFault(ServiceException):
    """The integration is in an invalid state and can't perform the requested
    operation.
    """

    code: str = "InvalidIntegrationStateFault"
    sender_fault: bool = True
    status_code: int = 400


class InvalidOptionGroupStateFault(ServiceException):
    """The option group isn't in the *available* state."""

    code: str = "InvalidOptionGroupStateFault"
    sender_fault: bool = True
    status_code: int = 400


class InvalidResourceStateFault(ServiceException):
    """The operation can't be performed because another operation is in
    progress.
    """

    code: str = "InvalidResourceStateFault"
    sender_fault: bool = True
    status_code: int = 400


class InvalidRestoreFault(ServiceException):
    """Cannot restore from VPC backup to non-VPC DB instance."""

    code: str = "InvalidRestoreFault"
    sender_fault: bool = True
    status_code: int = 400


class InvalidS3BucketFault(ServiceException):
    """The specified Amazon S3 bucket name can't be found or Amazon RDS isn't
    authorized to access the specified Amazon S3 bucket. Verify the
    **SourceS3BucketName** and **S3IngestionRoleArn** values and try again.
    """

    code: str = "InvalidS3BucketFault"
    sender_fault: bool = True
    status_code: int = 400


class InvalidSubnet(ServiceException):
    """The requested subnet is invalid, or multiple subnets were requested that
    are not all in a common VPC.
    """

    code: str = "InvalidSubnet"
    sender_fault: bool = True
    status_code: int = 400


class InvalidVPCNetworkStateFault(ServiceException):
    """The DB subnet group doesn't cover all Availability Zones after it's
    created because of users' change.
    """

    code: str = "InvalidVPCNetworkStateFault"
    sender_fault: bool = True
    status_code: int = 400


class KMSKeyNotAccessibleFault(ServiceException):
    """An error occurred accessing an Amazon Web Services KMS key."""

    code: str = "KMSKeyNotAccessibleFault"
    sender_fault: bool = True
    status_code: int = 400


class MaxDBShardGroupLimitReached(ServiceException):
    """The maximum number of DB shard groups for your Amazon Web Services
    account in the specified Amazon Web Services Region has been reached.
    """

    code: str = "MaxDBShardGroupLimitReached"
    sender_fault: bool = True
    status_code: int = 400


class NetworkTypeNotSupported(ServiceException):
    """The network type is invalid for the DB instance. Valid nework type
    values are ``IPV4`` and ``DUAL``.
    """

    code: str = "NetworkTypeNotSupported"
    sender_fault: bool = True
    status_code: int = 400


class OptionGroupAlreadyExistsFault(ServiceException):
    """The option group you are trying to create already exists."""

    code: str = "OptionGroupAlreadyExistsFault"
    sender_fault: bool = True
    status_code: int = 400


class OptionGroupNotFoundFault(ServiceException):
    """The specified option group could not be found."""

    code: str = "OptionGroupNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404


class OptionGroupQuotaExceededFault(ServiceException):
    """The quota of 20 option groups was exceeded for this Amazon Web Services
    account.
    """

    code: str = "OptionGroupQuotaExceededFault"
    sender_fault: bool = True
    status_code: int = 400


class PointInTimeRestoreNotEnabledFault(ServiceException):
    """``SourceDBInstanceIdentifier`` refers to a DB instance with
    ``BackupRetentionPeriod`` equal to 0.
    """

    code: str = "PointInTimeRestoreNotEnabled"
    sender_fault: bool = True
    status_code: int = 400


class ProvisionedIopsNotAvailableInAZFault(ServiceException):
    """Provisioned IOPS not available in the specified Availability Zone."""

    code: str = "ProvisionedIopsNotAvailableInAZFault"
    sender_fault: bool = True
    status_code: int = 400


class ReservedDBInstanceAlreadyExistsFault(ServiceException):
    """User already has a reservation with the given identifier."""

    code: str = "ReservedDBInstanceAlreadyExists"
    sender_fault: bool = True
    status_code: int = 404


class ReservedDBInstanceNotFoundFault(ServiceException):
    """The specified reserved DB Instance not found."""

    code: str = "ReservedDBInstanceNotFound"
    sender_fault: bool = True
    status_code: int = 404


class ReservedDBInstanceQuotaExceededFault(ServiceException):
    """Request would exceed the user's DB Instance quota."""

    code: str = "ReservedDBInstanceQuotaExceeded"
    sender_fault: bool = True
    status_code: int = 400


class ReservedDBInstancesOfferingNotFoundFault(ServiceException):
    """Specified offering does not exist."""

    code: str = "ReservedDBInstancesOfferingNotFound"
    sender_fault: bool = True
    status_code: int = 404


class ResourceNotFoundFault(ServiceException):
    """The specified resource ID was not found."""

    code: str = "ResourceNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404


class SNSInvalidTopicFault(ServiceException):
    """SNS has responded that there is a problem with the SNS topic specified."""

    code: str = "SNSInvalidTopic"
    sender_fault: bool = True
    status_code: int = 400


class SNSNoAuthorizationFault(ServiceException):
    """You do not have permission to publish to the SNS topic ARN."""

    code: str = "SNSNoAuthorization"
    sender_fault: bool = True
    status_code: int = 400


class SNSTopicArnNotFoundFault(ServiceException):
    """The SNS topic ARN does not exist."""

    code: str = "SNSTopicArnNotFound"
    sender_fault: bool = True
    status_code: int = 404


class SharedSnapshotQuotaExceededFault(ServiceException):
    """You have exceeded the maximum number of accounts that you can share a
    manual DB snapshot with.
    """

    code: str = "SharedSnapshotQuotaExceeded"
    sender_fault: bool = True
    status_code: int = 400


class SnapshotQuotaExceededFault(ServiceException):
    """The request would result in the user exceeding the allowed number of DB
    snapshots.
    """

    code: str = "SnapshotQuotaExceeded"
    sender_fault: bool = True
    status_code: int = 400


class SourceClusterNotSupportedFault(ServiceException):
    """The source DB cluster isn't supported for a blue/green deployment."""

    code: str = "SourceClusterNotSupportedFault"
    sender_fault: bool = True
    status_code: int = 400


class SourceDatabaseNotSupportedFault(ServiceException):
    """The source DB instance isn't supported for a blue/green deployment."""

    code: str = "SourceDatabaseNotSupportedFault"
    sender_fault: bool = True
    status_code: int = 400


class SourceNotFoundFault(ServiceException):
    """The requested source could not be found."""

    code: str = "SourceNotFound"
    sender_fault: bool = True
    status_code: int = 404


class StorageQuotaExceededFault(ServiceException):
    """The request would result in the user exceeding the allowed amount of
    storage available across all DB instances.
    """

    code: str = "StorageQuotaExceeded"
    sender_fault: bool = True
    status_code: int = 400


class StorageTypeNotAvailableFault(ServiceException):
    """The ``aurora-iopt1`` storage type isn't available, because you modified
    the DB cluster to use this storage type less than one month ago.
    """

    code: str = "StorageTypeNotAvailableFault"
    sender_fault: bool = True
    status_code: int = 400


class StorageTypeNotSupportedFault(ServiceException):
    """The specified ``StorageType`` can't be associated with the DB instance."""

    code: str = "StorageTypeNotSupported"
    sender_fault: bool = True
    status_code: int = 400


class SubnetAlreadyInUse(ServiceException):
    """The DB subnet is already in use in the Availability Zone."""

    code: str = "SubnetAlreadyInUse"
    sender_fault: bool = True
    status_code: int = 400


class SubscriptionAlreadyExistFault(ServiceException):
    """The supplied subscription name already exists."""

    code: str = "SubscriptionAlreadyExist"
    sender_fault: bool = True
    status_code: int = 400


class SubscriptionCategoryNotFoundFault(ServiceException):
    """The supplied category does not exist."""

    code: str = "SubscriptionCategoryNotFound"
    sender_fault: bool = True
    status_code: int = 404


class SubscriptionNotFoundFault(ServiceException):
    """The subscription name does not exist."""

    code: str = "SubscriptionNotFound"
    sender_fault: bool = True
    status_code: int = 404


class TenantDatabaseAlreadyExistsFault(ServiceException):
    """You attempted to either create a tenant database that already exists or
    modify a tenant database to use the name of an existing tenant database.
    """

    code: str = "TenantDatabaseAlreadyExists"
    sender_fault: bool = True
    status_code: int = 400


class TenantDatabaseNotFoundFault(ServiceException):
    """The specified tenant database wasn't found in the DB instance."""

    code: str = "TenantDatabaseNotFound"
    sender_fault: bool = True
    status_code: int = 404


class TenantDatabaseQuotaExceededFault(ServiceException):
    """You attempted to create more tenant databases than are permitted in your
    Amazon Web Services account.
    """

    code: str = "TenantDatabaseQuotaExceeded"
    sender_fault: bool = True
    status_code: int = 400


class UnsupportedDBEngineVersionFault(ServiceException):
    """The specified DB engine version isn't supported for Aurora Limitless
    Database.
    """

    code: str = "UnsupportedDBEngineVersion"
    sender_fault: bool = True
    status_code: int = 400


Long = int


class AccountQuota(TypedDict, total=False):
    """Describes a quota for an Amazon Web Services account.

    The following are account quotas:

    -  ``AllocatedStorage`` - The total allocated storage per account, in
       GiB. The used value is the total allocated storage in the account, in
       GiB.

    -  ``AuthorizationsPerDBSecurityGroup`` - The number of ingress rules
       per DB security group. The used value is the highest number of
       ingress rules in a DB security group in the account. Other DB
       security groups in the account might have a lower number of ingress
       rules.

    -  ``CustomEndpointsPerDBCluster`` - The number of custom endpoints per
       DB cluster. The used value is the highest number of custom endpoints
       in a DB clusters in the account. Other DB clusters in the account
       might have a lower number of custom endpoints.

    -  ``DBClusterParameterGroups`` - The number of DB cluster parameter
       groups per account, excluding default parameter groups. The used
       value is the count of nondefault DB cluster parameter groups in the
       account.

    -  ``DBClusterRoles`` - The number of associated Amazon Web Services
       Identity and Access Management (IAM) roles per DB cluster. The used
       value is the highest number of associated IAM roles for a DB cluster
       in the account. Other DB clusters in the account might have a lower
       number of associated IAM roles.

    -  ``DBClusters`` - The number of DB clusters per account. The used
       value is the count of DB clusters in the account.

    -  ``DBInstanceRoles`` - The number of associated IAM roles per DB
       instance. The used value is the highest number of associated IAM
       roles for a DB instance in the account. Other DB instances in the
       account might have a lower number of associated IAM roles.

    -  ``DBInstances`` - The number of DB instances per account. The used
       value is the count of the DB instances in the account.

       Amazon RDS DB instances, Amazon Aurora DB instances, Amazon Neptune
       instances, and Amazon DocumentDB instances apply to this quota.

    -  ``DBParameterGroups`` - The number of DB parameter groups per
       account, excluding default parameter groups. The used value is the
       count of nondefault DB parameter groups in the account.

    -  ``DBSecurityGroups`` - The number of DB security groups (not VPC
       security groups) per account, excluding the default security group.
       The used value is the count of nondefault DB security groups in the
       account.

    -  ``DBSubnetGroups`` - The number of DB subnet groups per account. The
       used value is the count of the DB subnet groups in the account.

    -  ``EventSubscriptions`` - The number of event subscriptions per
       account. The used value is the count of the event subscriptions in
       the account.

    -  ``ManualClusterSnapshots`` - The number of manual DB cluster
       snapshots per account. The used value is the count of the manual DB
       cluster snapshots in the account.

    -  ``ManualSnapshots`` - The number of manual DB instance snapshots per
       account. The used value is the count of the manual DB instance
       snapshots in the account.

    -  ``OptionGroups`` - The number of DB option groups per account,
       excluding default option groups. The used value is the count of
       nondefault DB option groups in the account.

    -  ``ReadReplicasPerMaster`` - The number of read replicas per DB
       instance. The used value is the highest number of read replicas for a
       DB instance in the account. Other DB instances in the account might
       have a lower number of read replicas.

    -  ``ReservedDBInstances`` - The number of reserved DB instances per
       account. The used value is the count of the active reserved DB
       instances in the account.

    -  ``SubnetsPerDBSubnetGroup`` - The number of subnets per DB subnet
       group. The used value is highest number of subnets for a DB subnet
       group in the account. Other DB subnet groups in the account might
       have a lower number of subnets.

    For more information, see `Quotas for Amazon
    RDS <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Limits.html>`__
    in the *Amazon RDS User Guide* and `Quotas for Amazon
    Aurora <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Limits.html>`__
    in the *Amazon Aurora User Guide*.
    """

    AccountQuotaName: Optional[String]
    Used: Optional[Long]
    Max: Optional[Long]


AccountQuotaList = List[AccountQuota]


class AccountAttributesMessage(TypedDict, total=False):
    """Data returned by the **DescribeAccountAttributes** action."""

    AccountQuotas: Optional[AccountQuotaList]


ActivityStreamModeList = List[String]


class AddRoleToDBClusterMessage(ServiceRequest):
    DBClusterIdentifier: String
    RoleArn: String
    FeatureName: Optional[String]


class AddRoleToDBInstanceMessage(ServiceRequest):
    DBInstanceIdentifier: String
    RoleArn: String
    FeatureName: String


class AddSourceIdentifierToSubscriptionMessage(ServiceRequest):
    SubscriptionName: String
    SourceIdentifier: String


EventCategoriesList = List[String]
SourceIdsList = List[String]


class EventSubscription(TypedDict, total=False):
    """Contains the results of a successful invocation of the
    ``DescribeEventSubscriptions`` action.
    """

    CustomerAwsId: Optional[String]
    CustSubscriptionId: Optional[String]
    SnsTopicArn: Optional[String]
    Status: Optional[String]
    SubscriptionCreationTime: Optional[String]
    SourceType: Optional[String]
    SourceIdsList: Optional[SourceIdsList]
    EventCategoriesList: Optional[EventCategoriesList]
    Enabled: Optional[Boolean]
    EventSubscriptionArn: Optional[String]


class AddSourceIdentifierToSubscriptionResult(TypedDict, total=False):
    EventSubscription: Optional[EventSubscription]


class Tag(TypedDict, total=False):
    """Metadata assigned to an Amazon RDS resource consisting of a key-value
    pair.

    For more information, see `Tagging Amazon RDS
    resources <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html>`__
    in the *Amazon RDS User Guide* or `Tagging Amazon Aurora and Amazon RDS
    resources <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html>`__
    in the *Amazon Aurora User Guide*.
    """

    Key: Optional[String]
    Value: Optional[String]


TagList = List[Tag]


class AddTagsToResourceMessage(ServiceRequest):
    ResourceName: String
    Tags: TagList


class ApplyPendingMaintenanceActionMessage(ServiceRequest):
    ResourceIdentifier: String
    ApplyAction: String
    OptInType: String


TStamp = datetime


class PendingMaintenanceAction(TypedDict, total=False):
    """Provides information about a pending maintenance action for a resource."""

    Action: Optional[String]
    AutoAppliedAfterDate: Optional[TStamp]
    ForcedApplyDate: Optional[TStamp]
    OptInStatus: Optional[String]
    CurrentApplyDate: Optional[TStamp]
    Description: Optional[String]


PendingMaintenanceActionDetails = List[PendingMaintenanceAction]


class ResourcePendingMaintenanceActions(TypedDict, total=False):
    """Describes the pending maintenance actions for a resource."""

    ResourceIdentifier: Optional[String]
    PendingMaintenanceActionDetails: Optional[PendingMaintenanceActionDetails]


class ApplyPendingMaintenanceActionResult(TypedDict, total=False):
    ResourcePendingMaintenanceActions: Optional[ResourcePendingMaintenanceActions]


AttributeValueList = List[String]


class AuthorizeDBSecurityGroupIngressMessage(ServiceRequest):
    DBSecurityGroupName: String
    CIDRIP: Optional[String]
    EC2SecurityGroupName: Optional[String]
    EC2SecurityGroupId: Optional[String]
    EC2SecurityGroupOwnerId: Optional[String]


class IPRange(TypedDict, total=False):
    """This data type is used as a response element in the
    ``DescribeDBSecurityGroups`` action.
    """

    Status: Optional[String]
    CIDRIP: Optional[String]


IPRangeList = List[IPRange]


class EC2SecurityGroup(TypedDict, total=False):
    """This data type is used as a response element in the following actions:

    -  ``AuthorizeDBSecurityGroupIngress``

    -  ``DescribeDBSecurityGroups``

    -  ``RevokeDBSecurityGroupIngress``
    """

    Status: Optional[String]
    EC2SecurityGroupName: Optional[String]
    EC2SecurityGroupId: Optional[String]
    EC2SecurityGroupOwnerId: Optional[String]


EC2SecurityGroupList = List[EC2SecurityGroup]


class DBSecurityGroup(TypedDict, total=False):
    """Contains the details for an Amazon RDS DB security group.

    This data type is used as a response element in the
    ``DescribeDBSecurityGroups`` action.
    """

    OwnerId: Optional[String]
    DBSecurityGroupName: Optional[String]
    DBSecurityGroupDescription: Optional[String]
    VpcId: Optional[String]
    EC2SecurityGroups: Optional[EC2SecurityGroupList]
    IPRanges: Optional[IPRangeList]
    DBSecurityGroupArn: Optional[String]


class AuthorizeDBSecurityGroupIngressResult(TypedDict, total=False):
    DBSecurityGroup: Optional[DBSecurityGroup]


class AvailabilityZone(TypedDict, total=False):
    """Contains Availability Zone information.

    This data type is used as an element in the
    ``OrderableDBInstanceOption`` data type.
    """

    Name: Optional[String]


AvailabilityZoneList = List[AvailabilityZone]
AvailabilityZones = List[String]


class AvailableProcessorFeature(TypedDict, total=False):
    """Contains the available processor feature information for the DB instance
    class of a DB instance.

    For more information, see `Configuring the Processor of the DB Instance
    Class <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html#USER_ConfigureProcessor>`__
    in the *Amazon RDS User Guide.*
    """

    Name: Optional[String]
    DefaultValue: Optional[String]
    AllowedValues: Optional[String]


AvailableProcessorFeatureList = List[AvailableProcessorFeature]


class BacktrackDBClusterMessage(ServiceRequest):
    DBClusterIdentifier: String
    BacktrackTo: TStamp
    Force: Optional[BooleanOptional]
    UseEarliestTimeOnPointInTimeUnavailable: Optional[BooleanOptional]


class BlueGreenDeploymentTask(TypedDict, total=False):
    """Details about a task for a blue/green deployment.

    For more information, see `Using Amazon RDS Blue/Green Deployments for
    database
    updates <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html>`__
    in the *Amazon RDS User Guide* and `Using Amazon RDS Blue/Green
    Deployments for database
    updates <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html>`__
    in the *Amazon Aurora User Guide*.
    """

    Name: Optional[BlueGreenDeploymentTaskName]
    Status: Optional[BlueGreenDeploymentTaskStatus]


BlueGreenDeploymentTaskList = List[BlueGreenDeploymentTask]


class SwitchoverDetail(TypedDict, total=False):
    """Contains the details about a blue/green deployment.

    For more information, see `Using Amazon RDS Blue/Green Deployments for
    database
    updates <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html>`__
    in the *Amazon RDS User Guide* and `Using Amazon RDS Blue/Green
    Deployments for database
    updates <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html>`__
    in the *Amazon Aurora User Guide*.
    """

    SourceMember: Optional[DatabaseArn]
    TargetMember: Optional[DatabaseArn]
    Status: Optional[SwitchoverDetailStatus]


SwitchoverDetailList = List[SwitchoverDetail]


class BlueGreenDeployment(TypedDict, total=False):
    """Details about a blue/green deployment.

    For more information, see `Using Amazon RDS Blue/Green Deployments for
    database
    updates <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html>`__
    in the *Amazon RDS User Guide* and `Using Amazon RDS Blue/Green
    Deployments for database
    updates <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html>`__
    in the *Amazon Aurora User Guide*.
    """

    BlueGreenDeploymentIdentifier: Optional[BlueGreenDeploymentIdentifier]
    BlueGreenDeploymentName: Optional[BlueGreenDeploymentName]
    Source: Optional[DatabaseArn]
    Target: Optional[DatabaseArn]
    SwitchoverDetails: Optional[SwitchoverDetailList]
    Tasks: Optional[BlueGreenDeploymentTaskList]
    Status: Optional[BlueGreenDeploymentStatus]
    StatusDetails: Optional[BlueGreenDeploymentStatusDetails]
    CreateTime: Optional[TStamp]
    DeleteTime: Optional[TStamp]
    TagList: Optional[TagList]


BlueGreenDeploymentList = List[BlueGreenDeployment]
CACertificateIdentifiersList = List[String]


class CancelExportTaskMessage(ServiceRequest):
    ExportTaskIdentifier: String


class Certificate(TypedDict, total=False):
    """A CA certificate for an Amazon Web Services account.

    For more information, see `Using SSL/TLS to encrypt a connection to a DB
    instance <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html>`__
    in the *Amazon RDS User Guide* and `Using SSL/TLS to encrypt a
    connection to a DB
    cluster <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html>`__
    in the *Amazon Aurora User Guide*.
    """

    CertificateIdentifier: Optional[String]
    CertificateType: Optional[String]
    Thumbprint: Optional[String]
    ValidFrom: Optional[TStamp]
    ValidTill: Optional[TStamp]
    CertificateArn: Optional[String]
    CustomerOverride: Optional[BooleanOptional]
    CustomerOverrideValidTill: Optional[TStamp]


class CertificateDetails(TypedDict, total=False):
    """The details of the DB instance’s server certificate.

    For more information, see `Using SSL/TLS to encrypt a connection to a DB
    instance <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html>`__
    in the *Amazon RDS User Guide* and `Using SSL/TLS to encrypt a
    connection to a DB
    cluster <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html>`__
    in the *Amazon Aurora User Guide*.
    """

    CAIdentifier: Optional[String]
    ValidTill: Optional[TStamp]


CertificateList = List[Certificate]


class CertificateMessage(TypedDict, total=False):
    """Data returned by the **DescribeCertificates** action."""

    DefaultCertificateForNewLaunches: Optional[String]
    Certificates: Optional[CertificateList]
    Marker: Optional[String]


class CharacterSet(TypedDict, total=False):
    """This data type is used as a response element in the action
    ``DescribeDBEngineVersions``.
    """

    CharacterSetName: Optional[String]
    CharacterSetDescription: Optional[String]


LogTypeList = List[String]


class CloudwatchLogsExportConfiguration(TypedDict, total=False):
    """The configuration setting for the log types to be enabled for export to
    CloudWatch Logs for a specific DB instance or DB cluster.

    The ``EnableLogTypes`` and ``DisableLogTypes`` arrays determine which
    logs will be exported (or not exported) to CloudWatch Logs. The values
    within these arrays depend on the DB engine being used.

    For more information about exporting CloudWatch Logs for Amazon RDS DB
    instances, see `Publishing Database Logs to Amazon CloudWatch
    Logs <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch>`__
    in the *Amazon RDS User Guide*.

    For more information about exporting CloudWatch Logs for Amazon Aurora
    DB clusters, see `Publishing Database Logs to Amazon CloudWatch
    Logs <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch>`__
    in the *Amazon Aurora User Guide*.
    """

    EnableLogTypes: Optional[LogTypeList]
    DisableLogTypes: Optional[LogTypeList]


class RdsCustomClusterConfiguration(TypedDict, total=False):
    """Reserved for future use."""

    InterconnectSubnetId: Optional[String]
    TransitGatewayMulticastDomainId: Optional[String]
    ReplicaMode: Optional[ReplicaMode]


class PendingCloudwatchLogsExports(TypedDict, total=False):
    """A list of the log types whose configuration is still pending. In other
    words, these log types are in the process of being activated or
    deactivated.
    """

    LogTypesToEnable: Optional[LogTypeList]
    LogTypesToDisable: Optional[LogTypeList]


class ClusterPendingModifiedValues(TypedDict, total=False):
    """This data type is used as a response element in the ``ModifyDBCluster``
    operation and contains changes that will be applied during the next
    maintenance window.
    """

    PendingCloudwatchLogsExports: Optional[PendingCloudwatchLogsExports]
    DBClusterIdentifier: Optional[String]
    MasterUserPassword: Optional[String]
    IAMDatabaseAuthenticationEnabled: Optional[BooleanOptional]
    EngineVersion: Optional[String]
    BackupRetentionPeriod: Optional[IntegerOptional]
    AllocatedStorage: Optional[IntegerOptional]
    RdsCustomClusterConfiguration: Optional[RdsCustomClusterConfiguration]
    Iops: Optional[IntegerOptional]
    StorageType: Optional[String]
    CertificateDetails: Optional[CertificateDetails]


StringList = List[String]


class ConnectionPoolConfiguration(TypedDict, total=False):
    """Specifies the settings that control the size and behavior of the
    connection pool associated with a ``DBProxyTargetGroup``.
    """

    MaxConnectionsPercent: Optional[IntegerOptional]
    MaxIdleConnectionsPercent: Optional[IntegerOptional]
    ConnectionBorrowTimeout: Optional[IntegerOptional]
    SessionPinningFilters: Optional[StringList]
    InitQuery: Optional[String]


class ConnectionPoolConfigurationInfo(TypedDict, total=False):
    """Displays the settings that control the size and behavior of the
    connection pool associated with a ``DBProxyTarget``.
    """

    MaxConnectionsPercent: Optional[Integer]
    MaxIdleConnectionsPercent: Optional[Integer]
    ConnectionBorrowTimeout: Optional[Integer]
    SessionPinningFilters: Optional[StringList]
    InitQuery: Optional[String]


class ContextAttribute(TypedDict, total=False):
    """The additional attributes of ``RecommendedAction`` data type."""

    Key: Optional[String]
    Value: Optional[String]


ContextAttributeList = List[ContextAttribute]


class CopyDBClusterParameterGroupMessage(ServiceRequest):
    SourceDBClusterParameterGroupIdentifier: String
    TargetDBClusterParameterGroupIdentifier: String
    TargetDBClusterParameterGroupDescription: String
    Tags: Optional[TagList]


class DBClusterParameterGroup(TypedDict, total=False):
    """Contains the details of an Amazon RDS DB cluster parameter group.

    This data type is used as a response element in the
    ``DescribeDBClusterParameterGroups`` action.
    """

    DBClusterParameterGroupName: Optional[String]
    DBParameterGroupFamily: Optional[String]
    Description: Optional[String]
    DBClusterParameterGroupArn: Optional[String]


class CopyDBClusterParameterGroupResult(TypedDict, total=False):
    DBClusterParameterGroup: Optional[DBClusterParameterGroup]


class CopyDBClusterSnapshotMessage(ServiceRequest):
    SourceDBClusterSnapshotIdentifier: String
    TargetDBClusterSnapshotIdentifier: String
    KmsKeyId: Optional[String]
    PreSignedUrl: Optional[String]
    CopyTags: Optional[BooleanOptional]
    Tags: Optional[TagList]
    SourceRegion: Optional[String]


class DBClusterSnapshot(TypedDict, total=False):
    """Contains the details for an Amazon RDS DB cluster snapshot

    This data type is used as a response element in the
    ``DescribeDBClusterSnapshots`` action.
    """

    AvailabilityZones: Optional[AvailabilityZones]
    DBClusterSnapshotIdentifier: Optional[String]
    DBClusterIdentifier: Optional[String]
    SnapshotCreateTime: Optional[TStamp]
    Engine: Optional[String]
    EngineMode: Optional[String]
    AllocatedStorage: Optional[Integer]
    Status: Optional[String]
    Port: Optional[Integer]
    VpcId: Optional[String]
    ClusterCreateTime: Optional[TStamp]
    MasterUsername: Optional[String]
    EngineVersion: Optional[String]
    LicenseModel: Optional[String]
    SnapshotType: Optional[String]
    PercentProgress: Optional[Integer]
    StorageEncrypted: Optional[Boolean]
    KmsKeyId: Optional[String]
    DBClusterSnapshotArn: Optional[String]
    SourceDBClusterSnapshotArn: Optional[String]
    IAMDatabaseAuthenticationEnabled: Optional[Boolean]
    TagList: Optional[TagList]
    DBSystemId: Optional[String]
    StorageType: Optional[String]
    DbClusterResourceId: Optional[String]
    StorageThroughput: Optional[IntegerOptional]


class CopyDBClusterSnapshotResult(TypedDict, total=False):
    DBClusterSnapshot: Optional[DBClusterSnapshot]


class CopyDBParameterGroupMessage(ServiceRequest):
    SourceDBParameterGroupIdentifier: String
    TargetDBParameterGroupIdentifier: String
    TargetDBParameterGroupDescription: String
    Tags: Optional[TagList]


class DBParameterGroup(TypedDict, total=False):
    """Contains the details of an Amazon RDS DB parameter group.

    This data type is used as a response element in the
    ``DescribeDBParameterGroups`` action.
    """

    DBParameterGroupName: Optional[String]
    DBParameterGroupFamily: Optional[String]
    Description: Optional[String]
    DBParameterGroupArn: Optional[String]


class CopyDBParameterGroupResult(TypedDict, total=False):
    DBParameterGroup: Optional[DBParameterGroup]


class CopyDBSnapshotMessage(ServiceRequest):
    SourceDBSnapshotIdentifier: String
    TargetDBSnapshotIdentifier: String
    KmsKeyId: Optional[String]
    Tags: Optional[TagList]
    CopyTags: Optional[BooleanOptional]
    PreSignedUrl: Optional[String]
    OptionGroupName: Optional[String]
    TargetCustomAvailabilityZone: Optional[String]
    CopyOptionGroup: Optional[BooleanOptional]
    SourceRegion: Optional[String]


class ProcessorFeature(TypedDict, total=False):
    """Contains the processor features of a DB instance class.

    To specify the number of CPU cores, use the ``coreCount`` feature name
    for the ``Name`` parameter. To specify the number of threads per core,
    use the ``threadsPerCore`` feature name for the ``Name`` parameter.

    You can set the processor features of the DB instance class for a DB
    instance when you call one of the following actions:

    -  ``CreateDBInstance``

    -  ``ModifyDBInstance``

    -  ``RestoreDBInstanceFromDBSnapshot``

    -  ``RestoreDBInstanceFromS3``

    -  ``RestoreDBInstanceToPointInTime``

    You can view the valid processor values for a particular instance class
    by calling the ``DescribeOrderableDBInstanceOptions`` action and
    specifying the instance class for the ``DBInstanceClass`` parameter.

    In addition, you can use the following actions for DB instance class
    processor information:

    -  ``DescribeDBInstances``

    -  ``DescribeDBSnapshots``

    -  ``DescribeValidDBInstanceModifications``

    If you call ``DescribeDBInstances``, ``ProcessorFeature`` returns
    non-null values only if the following conditions are met:

    -  You are accessing an Oracle DB instance.

    -  Your Oracle DB instance class supports configuring the number of CPU
       cores and threads per core.

    -  The current number CPU cores and threads is set to a non-default
       value.

    For more information, see `Configuring the processor for a DB instance
    class in RDS for
    Oracle <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html#USER_ConfigureProcessor>`__
    in the *Amazon RDS User Guide.*
    """

    Name: Optional[String]
    Value: Optional[String]


ProcessorFeatureList = List[ProcessorFeature]


class DBSnapshot(TypedDict, total=False):
    """Contains the details of an Amazon RDS DB snapshot.

    This data type is used as a response element in the
    ``DescribeDBSnapshots`` action.
    """

    DBSnapshotIdentifier: Optional[String]
    DBInstanceIdentifier: Optional[String]
    SnapshotCreateTime: Optional[TStamp]
    Engine: Optional[String]
    AllocatedStorage: Optional[Integer]
    Status: Optional[String]
    Port: Optional[Integer]
    AvailabilityZone: Optional[String]
    VpcId: Optional[String]
    InstanceCreateTime: Optional[TStamp]
    MasterUsername: Optional[String]
    EngineVersion: Optional[String]
    LicenseModel: Optional[String]
    SnapshotType: Optional[String]
    Iops: Optional[IntegerOptional]
    OptionGroupName: Optional[String]
    PercentProgress: Optional[Integer]
    SourceRegion: Optional[String]
    SourceDBSnapshotIdentifier: Optional[String]
    StorageType: Optional[String]
    TdeCredentialArn: Optional[String]
    Encrypted: Optional[Boolean]
    KmsKeyId: Optional[String]
    DBSnapshotArn: Optional[String]
    Timezone: Optional[String]
    IAMDatabaseAuthenticationEnabled: Optional[Boolean]
    ProcessorFeatures: Optional[ProcessorFeatureList]
    DbiResourceId: Optional[String]
    TagList: Optional[TagList]
    OriginalSnapshotCreateTime: Optional[TStamp]
    SnapshotDatabaseTime: Optional[TStamp]
    SnapshotTarget: Optional[String]
    StorageThroughput: Optional[IntegerOptional]
    DBSystemId: Optional[String]
    DedicatedLogVolume: Optional[Boolean]
    MultiTenant: Optional[BooleanOptional]


class CopyDBSnapshotResult(TypedDict, total=False):
    DBSnapshot: Optional[DBSnapshot]


class CopyOptionGroupMessage(ServiceRequest):
    SourceOptionGroupIdentifier: String
    TargetOptionGroupIdentifier: String
    TargetOptionGroupDescription: String
    Tags: Optional[TagList]


class VpcSecurityGroupMembership(TypedDict, total=False):
    """This data type is used as a response element for queries on VPC security
    group membership.
    """

    VpcSecurityGroupId: Optional[String]
    Status: Optional[String]


VpcSecurityGroupMembershipList = List[VpcSecurityGroupMembership]


class DBSecurityGroupMembership(TypedDict, total=False):
    """This data type is used as a response element in the following actions:

    -  ``ModifyDBInstance``

    -  ``RebootDBInstance``

    -  ``RestoreDBInstanceFromDBSnapshot``

    -  ``RestoreDBInstanceToPointInTime``
    """

    DBSecurityGroupName: Optional[String]
    Status: Optional[String]


DBSecurityGroupMembershipList = List[DBSecurityGroupMembership]


class OptionSetting(TypedDict, total=False):
    """Option settings are the actual settings being applied or configured for
    that option. It is used when you modify an option group or describe
    option groups. For example, the NATIVE_NETWORK_ENCRYPTION option has a
    setting called SQLNET.ENCRYPTION_SERVER that can have several different
    values.
    """

    Name: Optional[String]
    Value: Optional[String]
    DefaultValue: Optional[String]
    Description: Optional[String]
    ApplyType: Optional[String]
    DataType: Optional[String]
    AllowedValues: Optional[String]
    IsModifiable: Optional[Boolean]
    IsCollection: Optional[Boolean]


OptionSettingConfigurationList = List[OptionSetting]


class Option(TypedDict, total=False):
    """The details of an option."""

    OptionName: Optional[String]
    OptionDescription: Optional[String]
    Persistent: Optional[Boolean]
    Permanent: Optional[Boolean]
    Port: Optional[IntegerOptional]
    OptionVersion: Optional[String]
    OptionSettings: Optional[OptionSettingConfigurationList]
    DBSecurityGroupMemberships: Optional[DBSecurityGroupMembershipList]
    VpcSecurityGroupMemberships: Optional[VpcSecurityGroupMembershipList]


OptionsList = List[Option]


class OptionGroup(TypedDict, total=False):
    OptionGroupName: Optional[String]
    OptionGroupDescription: Optional[String]
    EngineName: Optional[String]
    MajorEngineVersion: Optional[String]
    Options: Optional[OptionsList]
    AllowsVpcAndNonVpcInstanceMemberships: Optional[Boolean]
    VpcId: Optional[String]
    OptionGroupArn: Optional[String]
    SourceOptionGroup: Optional[String]
    SourceAccountId: Optional[String]
    CopyTimestamp: Optional[TStamp]


class CopyOptionGroupResult(TypedDict, total=False):
    OptionGroup: Optional[OptionGroup]


class CreateBlueGreenDeploymentRequest(ServiceRequest):
    BlueGreenDeploymentName: BlueGreenDeploymentName
    Source: DatabaseArn
    TargetEngineVersion: Optional[TargetEngineVersion]
    TargetDBParameterGroupName: Optional[TargetDBParameterGroupName]
    TargetDBClusterParameterGroupName: Optional[TargetDBClusterParameterGroupName]
    Tags: Optional[TagList]
    TargetDBInstanceClass: Optional[TargetDBInstanceClass]
    UpgradeTargetStorageConfig: Optional[BooleanOptional]
    TargetIops: Optional[IntegerOptional]
    TargetStorageType: Optional[TargetStorageType]
    TargetAllocatedStorage: Optional[IntegerOptional]
    TargetStorageThroughput: Optional[IntegerOptional]


class CreateBlueGreenDeploymentResponse(TypedDict, total=False):
    BlueGreenDeployment: Optional[BlueGreenDeployment]


class CreateCustomDBEngineVersionMessage(ServiceRequest):
    Engine: CustomEngineName
    EngineVersion: CustomEngineVersion
    DatabaseInstallationFilesS3BucketName: Optional[BucketName]
    DatabaseInstallationFilesS3Prefix: Optional[String255]
    ImageId: Optional[String255]
    KMSKeyId: Optional[KmsKeyIdOrArn]
    Description: Optional[Description]
    Manifest: Optional[CustomDBEngineVersionManifest]
    Tags: Optional[TagList]
    SourceCustomDbEngineVersionIdentifier: Optional[String255]
    UseAwsProvidedLatestImage: Optional[BooleanOptional]


class CreateDBClusterEndpointMessage(ServiceRequest):
    DBClusterIdentifier: String
    DBClusterEndpointIdentifier: String
    EndpointType: String
    StaticMembers: Optional[StringList]
    ExcludedMembers: Optional[StringList]
    Tags: Optional[TagList]


class ServerlessV2ScalingConfiguration(TypedDict, total=False):
    """Contains the scaling configuration of an Aurora Serverless v2 DB
    cluster.

    For more information, see `Using Amazon Aurora Serverless
    v2 <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html>`__
    in the *Amazon Aurora User Guide*.
    """

    MinCapacity: Optional[DoubleOptional]
    MaxCapacity: Optional[DoubleOptional]
    SecondsUntilAutoPause: Optional[IntegerOptional]


class ScalingConfiguration(TypedDict, total=False):
    """Contains the scaling configuration of an Aurora Serverless v1 DB
    cluster.

    For more information, see `Using Amazon Aurora Serverless
    v1 <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.html>`__
    in the *Amazon Aurora User Guide*.
    """

    MinCapacity: Optional[IntegerOptional]
    MaxCapacity: Optional[IntegerOptional]
    AutoPause: Optional[BooleanOptional]
    SecondsUntilAutoPause: Optional[IntegerOptional]
    TimeoutAction: Optional[String]
    SecondsBeforeTimeout: Optional[IntegerOptional]


LongOptional = int
VpcSecurityGroupIdList = List[String]


class CreateDBClusterMessage(ServiceRequest):
    AvailabilityZones: Optional[AvailabilityZones]
    BackupRetentionPeriod: Optional[IntegerOptional]
    CharacterSetName: Optional[String]
    DatabaseName: Optional[String]
    DBClusterIdentifier: String
    DBClusterParameterGroupName: Optional[String]
    VpcSecurityGroupIds: Optional[VpcSecurityGroupIdList]
    DBSubnetGroupName: Optional[String]
    Engine: String
    EngineVersion: Optional[String]
    Port: Optional[IntegerOptional]
    MasterUsername: Optional[String]
    MasterUserPassword: Optional[String]
    OptionGroupName: Optional[String]
    PreferredBackupWindow: Optional[String]
    PreferredMaintenanceWindow: Optional[String]
    ReplicationSourceIdentifier: Optional[String]
    Tags: Optional[TagList]
    StorageEncrypted: Optional[BooleanOptional]
    KmsKeyId: Optional[String]
    PreSignedUrl: Optional[String]
    EnableIAMDatabaseAuthentication: Optional[BooleanOptional]
    BacktrackWindow: Optional[LongOptional]
    EnableCloudwatchLogsExports: Optional[LogTypeList]
    EngineMode: Optional[String]
    ScalingConfiguration: Optional[ScalingConfiguration]
    RdsCustomClusterConfiguration: Optional[RdsCustomClusterConfiguration]
    DeletionProtection: Optional[BooleanOptional]
    GlobalClusterIdentifier: Optional[String]
    EnableHttpEndpoint: Optional[BooleanOptional]
    CopyTagsToSnapshot: Optional[BooleanOptional]
    Domain: Optional[String]
    DomainIAMRoleName: Optional[String]
    EnableGlobalWriteForwarding: Optional[BooleanOptional]
    DBClusterInstanceClass: Optional[String]
    AllocatedStorage: Optional[IntegerOptional]
    StorageType: Optional[String]
    Iops: Optional[IntegerOptional]
    PubliclyAccessible: Optional[BooleanOptional]
    AutoMinorVersionUpgrade: Optional[BooleanOptional]
    MonitoringInterval: Optional[IntegerOptional]
    MonitoringRoleArn: Optional[String]
    DatabaseInsightsMode: Optional[DatabaseInsightsMode]
    EnablePerformanceInsights: Optional[BooleanOptional]
    PerformanceInsightsKMSKeyId: Optional[String]
    PerformanceInsightsRetentionPeriod: Optional[IntegerOptional]
    EnableLimitlessDatabase: Optional[BooleanOptional]
    ServerlessV2ScalingConfiguration: Optional[ServerlessV2ScalingConfiguration]
    NetworkType: Optional[String]
    ClusterScalabilityType: Optional[ClusterScalabilityType]
    DBSystemId: Optional[String]
    ManageMasterUserPassword: Optional[BooleanOptional]
    MasterUserSecretKmsKeyId: Optional[String]
    EnableLocalWriteForwarding: Optional[BooleanOptional]
    CACertificateIdentifier: Optional[String]
    EngineLifecycleSupport: Optional[String]
    SourceRegion: Optional[String]


class CreateDBClusterParameterGroupMessage(ServiceRequest):
    DBClusterParameterGroupName: String
    DBParameterGroupFamily: String
    Description: String
    Tags: Optional[TagList]


class CreateDBClusterParameterGroupResult(TypedDict, total=False):
    DBClusterParameterGroup: Optional[DBClusterParameterGroup]


class LimitlessDatabase(TypedDict, total=False):
    """Contains details for Aurora Limitless Database."""

    Status: Optional[LimitlessDatabaseStatus]
    MinRequiredACU: Optional[DoubleOptional]


class MasterUserSecret(TypedDict, total=False):
    """Contains the secret managed by RDS in Amazon Web Services Secrets
    Manager for the master user password.

    For more information, see `Password management with Amazon Web Services
    Secrets
    Manager <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html>`__
    in the *Amazon RDS User Guide* and `Password management with Amazon Web
    Services Secrets
    Manager <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html>`__
    in the *Amazon Aurora User Guide.*
    """

    SecretArn: Optional[String]
    SecretStatus: Optional[String]
    KmsKeyId: Optional[String]


class ServerlessV2ScalingConfigurationInfo(TypedDict, total=False):
    """The scaling configuration for an Aurora Serverless v2 DB cluster.

    For more information, see `Using Amazon Aurora Serverless
    v2 <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html>`__
    in the *Amazon Aurora User Guide*.
    """

    MinCapacity: Optional[DoubleOptional]
    MaxCapacity: Optional[DoubleOptional]
    SecondsUntilAutoPause: Optional[IntegerOptional]


class DomainMembership(TypedDict, total=False):
    """An Active Directory Domain membership record associated with the DB
    instance or cluster.
    """

    Domain: Optional[String]
    Status: Optional[String]
    FQDN: Optional[String]
    IAMRoleName: Optional[String]
    OU: Optional[String]
    AuthSecretArn: Optional[String]
    DnsIps: Optional[StringList]


DomainMembershipList = List[DomainMembership]


class ScalingConfigurationInfo(TypedDict, total=False):
    """The scaling configuration for an Aurora DB cluster in ``serverless`` DB
    engine mode.

    For more information, see `Using Amazon Aurora Serverless
    v1 <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.html>`__
    in the *Amazon Aurora User Guide*.
    """

    MinCapacity: Optional[IntegerOptional]
    MaxCapacity: Optional[IntegerOptional]
    AutoPause: Optional[BooleanOptional]
    SecondsUntilAutoPause: Optional[IntegerOptional]
    TimeoutAction: Optional[String]
    SecondsBeforeTimeout: Optional[IntegerOptional]


class DBClusterRole(TypedDict, total=False):
    """Describes an Amazon Web Services Identity and Access Management (IAM)
    role that is associated with a DB cluster.
    """

    RoleArn: Optional[String]
    Status: Optional[String]
    FeatureName: Optional[String]


DBClusterRoles = List[DBClusterRole]


class DBClusterMember(TypedDict, total=False):
    """Contains information about an instance that is part of a DB cluster."""

    DBInstanceIdentifier: Optional[String]
    IsClusterWriter: Optional[Boolean]
    DBClusterParameterGroupStatus: Optional[String]
    PromotionTier: Optional[IntegerOptional]


DBClusterMemberList = List[DBClusterMember]


class DBClusterStatusInfo(TypedDict, total=False):
    """Reserved for future use."""

    StatusType: Optional[String]
    Normal: Optional[Boolean]
    Status: Optional[String]
    Message: Optional[String]


DBClusterStatusInfoList = List[DBClusterStatusInfo]
ReadReplicaIdentifierList = List[String]


class DBClusterOptionGroupStatus(TypedDict, total=False):
    """Contains status information for a DB cluster option group."""

    DBClusterOptionGroupName: Optional[String]
    Status: Optional[String]


DBClusterOptionGroupMemberships = List[DBClusterOptionGroupStatus]


class DBCluster(TypedDict, total=False):
    """Contains the details of an Amazon Aurora DB cluster or Multi-AZ DB
    cluster.

    For an Amazon Aurora DB cluster, this data type is used as a response
    element in the operations ``CreateDBCluster``, ``DeleteDBCluster``,
    ``DescribeDBClusters``, ``FailoverDBCluster``, ``ModifyDBCluster``,
    ``PromoteReadReplicaDBCluster``, ``RestoreDBClusterFromS3``,
    ``RestoreDBClusterFromSnapshot``, ``RestoreDBClusterToPointInTime``,
    ``StartDBCluster``, and ``StopDBCluster``.

    For a Multi-AZ DB cluster, this data type is used as a response element
    in the operations ``CreateDBCluster``, ``DeleteDBCluster``,
    ``DescribeDBClusters``, ``FailoverDBCluster``, ``ModifyDBCluster``,
    ``RebootDBCluster``, ``RestoreDBClusterFromSnapshot``, and
    ``RestoreDBClusterToPointInTime``.

    For more information on Amazon Aurora DB clusters, see `What is Amazon
    Aurora? <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html>`__
    in the *Amazon Aurora User Guide.*

    For more information on Multi-AZ DB clusters, see `Multi-AZ deployments
    with two readable standby DB
    instances <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html>`__
    in the *Amazon RDS User Guide.*
    """

    AllocatedStorage: Optional[IntegerOptional]
    AvailabilityZones: Optional[AvailabilityZones]
    BackupRetentionPeriod: Optional[IntegerOptional]
    CharacterSetName: Optional[String]
    DatabaseName: Optional[String]
    DBClusterIdentifier: Optional[String]
    DBClusterParameterGroup: Optional[String]
    DBSubnetGroup: Optional[String]
    Status: Optional[String]
    AutomaticRestartTime: Optional[TStamp]
    PercentProgress: Optional[String]
    EarliestRestorableTime: Optional[TStamp]
    Endpoint: Optional[String]
    ReaderEndpoint: Optional[String]
    CustomEndpoints: Optional[StringList]
    MultiAZ: Optional[BooleanOptional]
    Engine: Optional[String]
    EngineVersion: Optional[String]
    LatestRestorableTime: Optional[TStamp]
    Port: Optional[IntegerOptional]
    MasterUsername: Optional[String]
    DBClusterOptionGroupMemberships: Optional[DBClusterOptionGroupMemberships]
    PreferredBackupWindow: Optional[String]
    PreferredMaintenanceWindow: Optional[String]
    ReplicationSourceIdentifier: Optional[String]
    ReadReplicaIdentifiers: Optional[ReadReplicaIdentifierList]
    StatusInfos: Optional[DBClusterStatusInfoList]
    DBClusterMembers: Optional[DBClusterMemberList]
    VpcSecurityGroups: Optional[VpcSecurityGroupMembershipList]
    HostedZoneId: Optional[String]
    StorageEncrypted: Optional[Boolean]
    KmsKeyId: Optional[String]
    DbClusterResourceId: Optional[String]
    DBClusterArn: Optional[String]
    AssociatedRoles: Optional[DBClusterRoles]
    IAMDatabaseAuthenticationEnabled: Optional[BooleanOptional]
    CloneGroupId: Optional[String]
    ClusterCreateTime: Optional[TStamp]
    EarliestBacktrackTime: Optional[TStamp]
    BacktrackWindow: Optional[LongOptional]
    BacktrackConsumedChangeRecords: Optional[LongOptional]
    EnabledCloudwatchLogsExports: Optional[LogTypeList]
    Capacity: Optional[IntegerOptional]
    EngineMode: Optional[String]
    ScalingConfigurationInfo: Optional[ScalingConfigurationInfo]
    RdsCustomClusterConfiguration: Optional[RdsCustomClusterConfiguration]
    DeletionProtection: Optional[BooleanOptional]
    HttpEndpointEnabled: Optional[BooleanOptional]
    ActivityStreamMode: Optional[ActivityStreamMode]
    ActivityStreamStatus: Optional[ActivityStreamStatus]
    ActivityStreamKmsKeyId: Optional[String]
    ActivityStreamKinesisStreamName: Optional[String]
    CopyTagsToSnapshot: Optional[BooleanOptional]
    CrossAccountClone: Optional[BooleanOptional]
    DomainMemberships: Optional[DomainMembershipList]
    TagList: Optional[TagList]
    GlobalWriteForwardingStatus: Optional[WriteForwardingStatus]
    GlobalWriteForwardingRequested: Optional[BooleanOptional]
    PendingModifiedValues: Optional[ClusterPendingModifiedValues]
    DBClusterInstanceClass: Optional[String]
    StorageType: Optional[String]
    Iops: Optional[IntegerOptional]
    PubliclyAccessible: Optional[BooleanOptional]
    AutoMinorVersionUpgrade: Optional[Boolean]
    MonitoringInterval: Optional[IntegerOptional]
    MonitoringRoleArn: Optional[String]
    DatabaseInsightsMode: Optional[DatabaseInsightsMode]
    PerformanceInsightsEnabled: Optional[BooleanOptional]
    PerformanceInsightsKMSKeyId: Optional[String]
    PerformanceInsightsRetentionPeriod: Optional[IntegerOptional]
    ServerlessV2ScalingConfiguration: Optional[ServerlessV2ScalingConfigurationInfo]
    NetworkType: Optional[String]
    DBSystemId: Optional[String]
    MasterUserSecret: Optional[MasterUserSecret]
    IOOptimizedNextAllowedModificationTime: Optional[TStamp]
    LocalWriteForwardingStatus: Optional[LocalWriteForwardingStatus]
    AwsBackupRecoveryPointArn: Optional[String]
    LimitlessDatabase: Optional[LimitlessDatabase]
    StorageThroughput: Optional[IntegerOptional]
    ClusterScalabilityType: Optional[ClusterScalabilityType]
    CertificateDetails: Optional[CertificateDetails]
    EngineLifecycleSupport: Optional[String]


class CreateDBClusterResult(TypedDict, total=False):
    DBCluster: Optional[DBCluster]


class CreateDBClusterSnapshotMessage(ServiceRequest):
    DBClusterSnapshotIdentifier: String
    DBClusterIdentifier: String
    Tags: Optional[TagList]


class CreateDBClusterSnapshotResult(TypedDict, total=False):
    DBClusterSnapshot: Optional[DBClusterSnapshot]


DBSecurityGroupNameList = List[String]


class CreateDBInstanceMessage(ServiceRequest):
    DBName: Optional[String]
    DBInstanceIdentifier: String
    AllocatedStorage: Optional[IntegerOptional]
    DBInstanceClass: String
    Engine: String
    MasterUsername: Optional[String]
    MasterUserPassword: Optional[String]
    DBSecurityGroups: Optional[DBSecurityGroupNameList]
    VpcSecurityGroupIds: Optional[VpcSecurityGroupIdList]
    AvailabilityZone: Optional[String]
    DBSubnetGroupName: Optional[String]
    PreferredMaintenanceWindow: Optional[String]
    DBParameterGroupName: Optional[String]
    BackupRetentionPeriod: Optional[IntegerOptional]
    PreferredBackupWindow: Optional[String]
    Port: Optional[IntegerOptional]
    MultiAZ: Optional[BooleanOptional]
    EngineVersion: Optional[String]
    AutoMinorVersionUpgrade: Optional[BooleanOptional]
    LicenseModel: Optional[String]
    Iops: Optional[IntegerOptional]
    OptionGroupName: Optional[String]
    CharacterSetName: Optional[String]
    NcharCharacterSetName: Optional[String]
    PubliclyAccessible: Optional[BooleanOptional]
    Tags: Optional[TagList]
    DBClusterIdentifier: Optional[String]
    StorageType: Optional[String]
    TdeCredentialArn: Optional[String]
    TdeCredentialPassword: Optional[String]
    StorageEncrypted: Optional[BooleanOptional]
    KmsKeyId: Optional[String]
    Domain: Optional[String]
    DomainFqdn: Optional[String]
    DomainOu: Optional[String]
    DomainAuthSecretArn: Optional[String]
    DomainDnsIps: Optional[StringList]
    CopyTagsToSnapshot: Optional[BooleanOptional]
    MonitoringInterval: Optional[IntegerOptional]
    MonitoringRoleArn: Optional[String]
    DomainIAMRoleName: Optional[String]
    PromotionTier: Optional[IntegerOptional]
    Timezone: Optional[String]
    EnableIAMDatabaseAuthentication: Optional[BooleanOptional]
    DatabaseInsightsMode: Optional[DatabaseInsightsMode]
    EnablePerformanceInsights: Optional[BooleanOptional]
    PerformanceInsightsKMSKeyId: Optional[String]
    PerformanceInsightsRetentionPeriod: Optional[IntegerOptional]
    EnableCloudwatchLogsExports: Optional[LogTypeList]
    ProcessorFeatures: Optional[ProcessorFeatureList]
    DeletionProtection: Optional[BooleanOptional]
    MaxAllocatedStorage: Optional[IntegerOptional]
    EnableCustomerOwnedIp: Optional[BooleanOptional]
    CustomIamInstanceProfile: Optional[String]
    BackupTarget: Optional[String]
    NetworkType: Optional[String]
    StorageThroughput: Optional[IntegerOptional]
    ManageMasterUserPassword: Optional[BooleanOptional]
    MasterUserSecretKmsKeyId: Optional[String]
    CACertificateIdentifier: Optional[String]
    DBSystemId: Optional[String]
    DedicatedLogVolume: Optional[BooleanOptional]
    MultiTenant: Optional[BooleanOptional]
    EngineLifecycleSupport: Optional[String]


class CreateDBInstanceReadReplicaMessage(ServiceRequest):
    DBInstanceIdentifier: String
    SourceDBInstanceIdentifier: Optional[String]
    DBInstanceClass: Optional[String]
    AvailabilityZone: Optional[String]
    Port: Optional[IntegerOptional]
    MultiAZ: Optional[BooleanOptional]
    AutoMinorVersionUpgrade: Optional[BooleanOptional]
    Iops: Optional[IntegerOptional]
    OptionGroupName: Optional[String]
    DBParameterGroupName: Optional[String]
    PubliclyAccessible: Optional[BooleanOptional]
    Tags: Optional[TagList]
    DBSubnetGroupName: Optional[String]
    VpcSecurityGroupIds: Optional[VpcSecurityGroupIdList]
    StorageType: Optional[String]
    CopyTagsToSnapshot: Optional[BooleanOptional]
    MonitoringInterval: Optional[IntegerOptional]
    MonitoringRoleArn: Optional[String]
    KmsKeyId: Optional[String]
    PreSignedUrl: Optional[String]
    EnableIAMDatabaseAuthentication: Optional[BooleanOptional]
    DatabaseInsightsMode: Optional[DatabaseInsightsMode]
    EnablePerformanceInsights: Optional[BooleanOptional]
    PerformanceInsightsKMSKeyId: Optional[String]
    PerformanceInsightsRetentionPeriod: Optional[IntegerOptional]
    EnableCloudwatchLogsExports: Optional[LogTypeList]
    ProcessorFeatures: Optional[ProcessorFeatureList]
    UseDefaultProcessorFeatures: Optional[BooleanOptional]
    DeletionProtection: Optional[BooleanOptional]
    Domain: Optional[String]
    DomainIAMRoleName: Optional[String]
    DomainFqdn: Optional[String]
    DomainOu: Optional[String]
    DomainAuthSecretArn: Optional[String]
    DomainDnsIps: Optional[StringList]
    ReplicaMode: Optional[ReplicaMode]
    MaxAllocatedStorage: Optional[IntegerOptional]
    CustomIamInstanceProfile: Optional[String]
    NetworkType: Optional[String]
    StorageThroughput: Optional[IntegerOptional]
    EnableCustomerOwnedIp: Optional[BooleanOptional]
    AllocatedStorage: Optional[IntegerOptional]
    SourceDBClusterIdentifier: Optional[String]
    DedicatedLogVolume: Optional[BooleanOptional]
    UpgradeStorageConfig: Optional[BooleanOptional]
    CACertificateIdentifier: Optional[String]
    SourceRegion: Optional[String]


class DBInstanceAutomatedBackupsReplication(TypedDict, total=False):
    """Automated backups of a DB instance replicated to another Amazon Web
    Services Region. They consist of system backups, transaction logs, and
    database instance properties.
    """

    DBInstanceAutomatedBackupsArn: Optional[String]


DBInstanceAutomatedBackupsReplicationList = List[DBInstanceAutomatedBackupsReplication]


class Endpoint(TypedDict, total=False):
    """This data type represents the information you need to connect to an
    Amazon RDS DB instance. This data type is used as a response element in
    the following actions:

    -  ``CreateDBInstance``

    -  ``DescribeDBInstances``

    -  ``DeleteDBInstance``

    For the data structure that represents Amazon Aurora DB cluster
    endpoints, see ``DBClusterEndpoint``.
    """

    Address: Optional[String]
    Port: Optional[Integer]
    HostedZoneId: Optional[String]


class DBInstanceRole(TypedDict, total=False):
    """Information about an Amazon Web Services Identity and Access Management
    (IAM) role that is associated with a DB instance.
    """

    RoleArn: Optional[String]
    FeatureName: Optional[String]
    Status: Optional[String]


DBInstanceRoles = List[DBInstanceRole]


class DBInstanceStatusInfo(TypedDict, total=False):
    """Provides a list of status information for a DB instance."""

    StatusType: Optional[String]
    Normal: Optional[Boolean]
    Status: Optional[String]
    Message: Optional[String]


DBInstanceStatusInfoList = List[DBInstanceStatusInfo]


class OptionGroupMembership(TypedDict, total=False):
    """Provides information on the option groups the DB instance is a member
    of.
    """

    OptionGroupName: Optional[String]
    Status: Optional[String]


OptionGroupMembershipList = List[OptionGroupMembership]
ReadReplicaDBClusterIdentifierList = List[String]
ReadReplicaDBInstanceIdentifierList = List[String]


class PendingModifiedValues(TypedDict, total=False):
    """This data type is used as a response element in the ``ModifyDBInstance``
    operation and contains changes that will be applied during the next
    maintenance window.
    """

    DBInstanceClass: Optional[String]
    AllocatedStorage: Optional[IntegerOptional]
    MasterUserPassword: Optional[String]
    Port: Optional[IntegerOptional]
    BackupRetentionPeriod: Optional[IntegerOptional]
    MultiAZ: Optional[BooleanOptional]
    EngineVersion: Optional[String]
    LicenseModel: Optional[String]
    Iops: Optional[IntegerOptional]
    DBInstanceIdentifier: Optional[String]
    StorageType: Optional[String]
    CACertificateIdentifier: Optional[String]
    DBSubnetGroupName: Optional[String]
    PendingCloudwatchLogsExports: Optional[PendingCloudwatchLogsExports]
    ProcessorFeatures: Optional[ProcessorFeatureList]
    IAMDatabaseAuthenticationEnabled: Optional[BooleanOptional]
    AutomationMode: Optional[AutomationMode]
    ResumeFullAutomationModeTime: Optional[TStamp]
    StorageThroughput: Optional[IntegerOptional]
    Engine: Optional[String]
    DedicatedLogVolume: Optional[BooleanOptional]
    MultiTenant: Optional[BooleanOptional]


class Outpost(TypedDict, total=False):
    """A data type that represents an Outpost.

    For more information about RDS on Outposts, see `Amazon RDS on Amazon
    Web Services
    Outposts <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html>`__
    in the *Amazon RDS User Guide.*
    """

    Arn: Optional[String]


class Subnet(TypedDict, total=False):
    """This data type is used as a response element for the
    ``DescribeDBSubnetGroups`` operation.
    """

    SubnetIdentifier: Optional[String]
    SubnetAvailabilityZone: Optional[AvailabilityZone]
    SubnetOutpost: Optional[Outpost]
    SubnetStatus: Optional[String]


SubnetList = List[Subnet]


class DBSubnetGroup(TypedDict, total=False):
    """Contains the details of an Amazon RDS DB subnet group.

    This data type is used as a response element in the
    ``DescribeDBSubnetGroups`` action.
    """

    DBSubnetGroupName: Optional[String]
    DBSubnetGroupDescription: Optional[String]
    VpcId: Optional[String]
    SubnetGroupStatus: Optional[String]
    Subnets: Optional[SubnetList]
    DBSubnetGroupArn: Optional[String]
    SupportedNetworkTypes: Optional[StringList]


class DBParameterGroupStatus(TypedDict, total=False):
    """The status of the DB parameter group.

    This data type is used as a response element in the following actions:

    -  ``CreateDBInstance``

    -  ``CreateDBInstanceReadReplica``

    -  ``DeleteDBInstance``

    -  ``ModifyDBInstance``

    -  ``RebootDBInstance``

    -  ``RestoreDBInstanceFromDBSnapshot``
    """

    DBParameterGroupName: Optional[String]
    ParameterApplyStatus: Optional[String]


DBParameterGroupStatusList = List[DBParameterGroupStatus]


class DBInstance(TypedDict, total=False):
    """Contains the details of an Amazon RDS DB instance.

    This data type is used as a response element in the operations
    ``CreateDBInstance``, ``CreateDBInstanceReadReplica``,
    ``DeleteDBInstance``, ``DescribeDBInstances``, ``ModifyDBInstance``,
    ``PromoteReadReplica``, ``RebootDBInstance``,
    ``RestoreDBInstanceFromDBSnapshot``, ``RestoreDBInstanceFromS3``,
    ``RestoreDBInstanceToPointInTime``, ``StartDBInstance``, and
    ``StopDBInstance``.
    """

    DBInstanceIdentifier: Optional[String]
    DBInstanceClass: Optional[String]
    Engine: Optional[String]
    DBInstanceStatus: Optional[String]
    AutomaticRestartTime: Optional[TStamp]
    MasterUsername: Optional[String]
    DBName: Optional[String]
    Endpoint: Optional[Endpoint]
    AllocatedStorage: Optional[Integer]
    InstanceCreateTime: Optional[TStamp]
    PreferredBackupWindow: Optional[String]
    BackupRetentionPeriod: Optional[Integer]
    DBSecurityGroups: Optional[DBSecurityGroupMembershipList]
    VpcSecurityGroups: Optional[VpcSecurityGroupMembershipList]
    DBParameterGroups: Optional[DBParameterGroupStatusList]
    AvailabilityZone: Optional[String]
    DBSubnetGroup: Optional[DBSubnetGroup]
    PreferredMaintenanceWindow: Optional[String]
    PendingModifiedValues: Optional[PendingModifiedValues]
    LatestRestorableTime: Optional[TStamp]
    MultiAZ: Optional[Boolean]
    EngineVersion: Optional[String]
    AutoMinorVersionUpgrade: Optional[Boolean]
    ReadReplicaSourceDBInstanceIdentifier: Optional[String]
    ReadReplicaDBInstanceIdentifiers: Optional[ReadReplicaDBInstanceIdentifierList]
    ReadReplicaDBClusterIdentifiers: Optional[ReadReplicaDBClusterIdentifierList]
    ReplicaMode: Optional[ReplicaMode]
    LicenseModel: Optional[String]
    Iops: Optional[IntegerOptional]
    OptionGroupMemberships: Optional[OptionGroupMembershipList]
    CharacterSetName: Optional[String]
    NcharCharacterSetName: Optional[String]
    SecondaryAvailabilityZone: Optional[String]
    PubliclyAccessible: Optional[Boolean]
    StatusInfos: Optional[DBInstanceStatusInfoList]
    StorageType: Optional[String]
    TdeCredentialArn: Optional[String]
    DbInstancePort: Optional[Integer]
    DBClusterIdentifier: Optional[String]
    StorageEncrypted: Optional[Boolean]
    KmsKeyId: Optional[String]
    DbiResourceId: Optional[String]
    CACertificateIdentifier: Optional[String]
    DomainMemberships: Optional[DomainMembershipList]
    CopyTagsToSnapshot: Optional[Boolean]
    MonitoringInterval: Optional[IntegerOptional]
    EnhancedMonitoringResourceArn: Optional[String]
    MonitoringRoleArn: Optional[String]
    PromotionTier: Optional[IntegerOptional]
    DBInstanceArn: Optional[String]
    Timezone: Optional[String]
    IAMDatabaseAuthenticationEnabled: Optional[Boolean]
    DatabaseInsightsMode: Optional[DatabaseInsightsMode]
    PerformanceInsightsEnabled: Optional[BooleanOptional]
    PerformanceInsightsKMSKeyId: Optional[String]
    PerformanceInsightsRetentionPeriod: Optional[IntegerOptional]
    EnabledCloudwatchLogsExports: Optional[LogTypeList]
    ProcessorFeatures: Optional[ProcessorFeatureList]
    DeletionProtection: Optional[Boolean]
    AssociatedRoles: Optional[DBInstanceRoles]
    ListenerEndpoint: Optional[Endpoint]
    MaxAllocatedStorage: Optional[IntegerOptional]
    TagList: Optional[TagList]
    DBInstanceAutomatedBackupsReplications: Optional[DBInstanceAutomatedBackupsReplicationList]
    CustomerOwnedIpEnabled: Optional[BooleanOptional]
    AwsBackupRecoveryPointArn: Optional[String]
    ActivityStreamStatus: Optional[ActivityStreamStatus]
    ActivityStreamKmsKeyId: Optional[String]
    ActivityStreamKinesisStreamName: Optional[String]
    ActivityStreamMode: Optional[ActivityStreamMode]
    ActivityStreamEngineNativeAuditFieldsIncluded: Optional[BooleanOptional]
    AutomationMode: Optional[AutomationMode]
    ResumeFullAutomationModeTime: Optional[TStamp]
    CustomIamInstanceProfile: Optional[String]
    BackupTarget: Optional[String]
    NetworkType: Optional[String]
    ActivityStreamPolicyStatus: Optional[ActivityStreamPolicyStatus]
    StorageThroughput: Optional[IntegerOptional]
    DBSystemId: Optional[String]
    MasterUserSecret: Optional[MasterUserSecret]
    CertificateDetails: Optional[CertificateDetails]
    ReadReplicaSourceDBClusterIdentifier: Optional[String]
    PercentProgress: Optional[String]
    DedicatedLogVolume: Optional[Boolean]
    IsStorageConfigUpgradeAvailable: Optional[BooleanOptional]
    MultiTenant: Optional[BooleanOptional]
    EngineLifecycleSupport: Optional[String]


class CreateDBInstanceReadReplicaResult(TypedDict, total=False):
    DBInstance: Optional[DBInstance]


class CreateDBInstanceResult(TypedDict, total=False):
    DBInstance: Optional[DBInstance]


class CreateDBParameterGroupMessage(ServiceRequest):
    DBParameterGroupName: String
    DBParameterGroupFamily: String
    Description: String
    Tags: Optional[TagList]


class CreateDBParameterGroupResult(TypedDict, total=False):
    DBParameterGroup: Optional[DBParameterGroup]


class CreateDBProxyEndpointRequest(ServiceRequest):
    DBProxyName: DBProxyName
    DBProxyEndpointName: DBProxyEndpointName
    VpcSubnetIds: StringList
    VpcSecurityGroupIds: Optional[StringList]
    TargetRole: Optional[DBProxyEndpointTargetRole]
    Tags: Optional[TagList]


class DBProxyEndpoint(TypedDict, total=False):
    """The data structure representing an endpoint associated with a DB proxy.
    RDS automatically creates one endpoint for each DB proxy. For Aurora DB
    clusters, you can associate additional endpoints with the same DB proxy.
    These endpoints can be read/write or read-only. They can also reside in
    different VPCs than the associated DB proxy.

    This data type is used as a response element in the
    ``DescribeDBProxyEndpoints`` operation.
    """

    DBProxyEndpointName: Optional[String]
    DBProxyEndpointArn: Optional[String]
    DBProxyName: Optional[String]
    Status: Optional[DBProxyEndpointStatus]
    VpcId: Optional[String]
    VpcSecurityGroupIds: Optional[StringList]
    VpcSubnetIds: Optional[StringList]
    Endpoint: Optional[String]
    CreatedDate: Optional[TStamp]
    TargetRole: Optional[DBProxyEndpointTargetRole]
    IsDefault: Optional[Boolean]


class CreateDBProxyEndpointResponse(TypedDict, total=False):
    DBProxyEndpoint: Optional[DBProxyEndpoint]


class UserAuthConfig(TypedDict, total=False):
    """Specifies the details of authentication used by a proxy to log in as a
    specific database user.
    """

    Description: Optional[String]
    UserName: Optional[String]
    AuthScheme: Optional[AuthScheme]
    SecretArn: Optional[String]
    IAMAuth: Optional[IAMAuthMode]
    ClientPasswordAuthType: Optional[ClientPasswordAuthType]


UserAuthConfigList = List[UserAuthConfig]


class CreateDBProxyRequest(ServiceRequest):
    DBProxyName: String
    EngineFamily: EngineFamily
    Auth: UserAuthConfigList
    RoleArn: String
    VpcSubnetIds: StringList
    VpcSecurityGroupIds: Optional[StringList]
    RequireTLS: Optional[Boolean]
    IdleClientTimeout: Optional[IntegerOptional]
    DebugLogging: Optional[Boolean]
    Tags: Optional[TagList]


class UserAuthConfigInfo(TypedDict, total=False):
    """Returns the details of authentication used by a proxy to log in as a
    specific database user.
    """

    Description: Optional[String]
    UserName: Optional[String]
    AuthScheme: Optional[AuthScheme]
    SecretArn: Optional[String]
    IAMAuth: Optional[IAMAuthMode]
    ClientPasswordAuthType: Optional[ClientPasswordAuthType]


UserAuthConfigInfoList = List[UserAuthConfigInfo]


class DBProxy(TypedDict, total=False):
    """The data structure representing a proxy managed by the RDS Proxy.

    This data type is used as a response element in the
    ``DescribeDBProxies`` action.
    """

    DBProxyName: Optional[String]
    DBProxyArn: Optional[String]
    Status: Optional[DBProxyStatus]
    EngineFamily: Optional[String]
    VpcId: Optional[String]
    VpcSecurityGroupIds: Optional[StringList]
    VpcSubnetIds: Optional[StringList]
    Auth: Optional[UserAuthConfigInfoList]
    RoleArn: Optional[String]
    Endpoint: Optional[String]
    RequireTLS: Optional[Boolean]
    IdleClientTimeout: Optional[Integer]
    DebugLogging: Optional[Boolean]
    CreatedDate: Optional[TStamp]
    UpdatedDate: Optional[TStamp]


class CreateDBProxyResponse(TypedDict, total=False):
    DBProxy: Optional[DBProxy]


class CreateDBSecurityGroupMessage(ServiceRequest):
    DBSecurityGroupName: String
    DBSecurityGroupDescription: String
    Tags: Optional[TagList]


class CreateDBSecurityGroupResult(TypedDict, total=False):
    DBSecurityGroup: Optional[DBSecurityGroup]


class CreateDBShardGroupMessage(ServiceRequest):
    DBShardGroupIdentifier: String
    DBClusterIdentifier: String
    ComputeRedundancy: Optional[IntegerOptional]
    MaxACU: DoubleOptional
    MinACU: Optional[DoubleOptional]
    PubliclyAccessible: Optional[BooleanOptional]
    Tags: Optional[TagList]


class CreateDBSnapshotMessage(ServiceRequest):
    DBSnapshotIdentifier: String
    DBInstanceIdentifier: String
    Tags: Optional[TagList]


class CreateDBSnapshotResult(TypedDict, total=False):
    DBSnapshot: Optional[DBSnapshot]


SubnetIdentifierList = List[String]


class CreateDBSubnetGroupMessage(ServiceRequest):
    DBSubnetGroupName: String
    DBSubnetGroupDescription: String
    SubnetIds: SubnetIdentifierList
    Tags: Optional[TagList]


class CreateDBSubnetGroupResult(TypedDict, total=False):
    DBSubnetGroup: Optional[DBSubnetGroup]


class CreateEventSubscriptionMessage(ServiceRequest):
    SubscriptionName: String
    SnsTopicArn: String
    SourceType: Optional[String]
    EventCategories: Optional[EventCategoriesList]
    SourceIds: Optional[SourceIdsList]
    Enabled: Optional[BooleanOptional]
    Tags: Optional[TagList]


class CreateEventSubscriptionResult(TypedDict, total=False):
    EventSubscription: Optional[EventSubscription]


class CreateGlobalClusterMessage(ServiceRequest):
    GlobalClusterIdentifier: Optional[String]
    SourceDBClusterIdentifier: Optional[String]
    Engine: Optional[String]
    EngineVersion: Optional[String]
    EngineLifecycleSupport: Optional[String]
    DeletionProtection: Optional[BooleanOptional]
    DatabaseName: Optional[String]
    StorageEncrypted: Optional[BooleanOptional]
    Tags: Optional[TagList]


class FailoverState(TypedDict, total=False):
    """Contains the state of scheduled or in-process operations on a global
    cluster (Aurora global database). This data type is empty unless a
    switchover or failover operation is scheduled or is in progress on the
    Aurora global database.
    """

    Status: Optional[FailoverStatus]
    FromDbClusterArn: Optional[String]
    ToDbClusterArn: Optional[String]
    IsDataLossAllowed: Optional[Boolean]


ReadersArnList = List[String]


class GlobalClusterMember(TypedDict, total=False):
    """A data structure with information about any primary and secondary
    clusters associated with a global cluster (Aurora global database).
    """

    DBClusterArn: Optional[String]
    Readers: Optional[ReadersArnList]
    IsWriter: Optional[Boolean]
    GlobalWriteForwardingStatus: Optional[WriteForwardingStatus]
    SynchronizationStatus: Optional[GlobalClusterMemberSynchronizationStatus]


GlobalClusterMemberList = List[GlobalClusterMember]


class GlobalCluster(TypedDict, total=False):
    """A data type representing an Aurora global database."""

    GlobalClusterIdentifier: Optional[String]
    GlobalClusterResourceId: Optional[String]
    GlobalClusterArn: Optional[String]
    Status: Optional[String]
    Engine: Optional[String]
    EngineVersion: Optional[String]
    EngineLifecycleSupport: Optional[String]
    DatabaseName: Optional[String]
    StorageEncrypted: Optional[BooleanOptional]
    DeletionProtection: Optional[BooleanOptional]
    GlobalClusterMembers: Optional[GlobalClusterMemberList]
    Endpoint: Optional[String]
    FailoverState: Optional[FailoverState]
    TagList: Optional[TagList]


class CreateGlobalClusterResult(TypedDict, total=False):
    GlobalCluster: Optional[GlobalCluster]


EncryptionContextMap = Dict[String, String]


class CreateIntegrationMessage(ServiceRequest):
    SourceArn: SourceArn
    TargetArn: Arn
    IntegrationName: IntegrationName
    KMSKeyId: Optional[String]
    AdditionalEncryptionContext: Optional[EncryptionContextMap]
    Tags: Optional[TagList]
    DataFilter: Optional[DataFilter]
    Description: Optional[IntegrationDescription]


class CreateOptionGroupMessage(ServiceRequest):
    OptionGroupName: String
    EngineName: String
    MajorEngineVersion: String
    OptionGroupDescription: String
    Tags: Optional[TagList]


class CreateOptionGroupResult(TypedDict, total=False):
    OptionGroup: Optional[OptionGroup]


class CreateTenantDatabaseMessage(ServiceRequest):
    DBInstanceIdentifier: String
    TenantDBName: String
    MasterUsername: String
    MasterUserPassword: Optional[SensitiveString]
    CharacterSetName: Optional[String]
    NcharCharacterSetName: Optional[String]
    ManageMasterUserPassword: Optional[BooleanOptional]
    MasterUserSecretKmsKeyId: Optional[String]
    Tags: Optional[TagList]


class TenantDatabasePendingModifiedValues(TypedDict, total=False):
    """A response element in the ``ModifyTenantDatabase`` operation that
    describes changes that will be applied. Specific changes are identified
    by subelements.
    """

    MasterUserPassword: Optional[SensitiveString]
    TenantDBName: Optional[String]


class TenantDatabase(TypedDict, total=False):
    """A tenant database in the DB instance. This data type is an element in
    the response to the ``DescribeTenantDatabases`` action.
    """

    TenantDatabaseCreateTime: Optional[TStamp]
    DBInstanceIdentifier: Optional[String]
    TenantDBName: Optional[String]
    Status: Optional[String]
    MasterUsername: Optional[String]
    DbiResourceId: Optional[String]
    TenantDatabaseResourceId: Optional[String]
    TenantDatabaseARN: Optional[String]
    CharacterSetName: Optional[String]
    NcharCharacterSetName: Optional[String]
    DeletionProtection: Optional[Boolean]
    PendingModifiedValues: Optional[TenantDatabasePendingModifiedValues]
    MasterUserSecret: Optional[MasterUserSecret]
    TagList: Optional[TagList]


class CreateTenantDatabaseResult(TypedDict, total=False):
    TenantDatabase: Optional[TenantDatabase]


class CustomDBEngineVersionAMI(TypedDict, total=False):
    """A value that indicates the AMI information."""

    ImageId: Optional[String]
    Status: Optional[String]


class RestoreWindow(TypedDict, total=False):
    """Earliest and latest time an instance can be restored to:"""

    EarliestTime: Optional[TStamp]
    LatestTime: Optional[TStamp]


class DBClusterAutomatedBackup(TypedDict, total=False):
    """An automated backup of a DB cluster. It consists of system backups,
    transaction logs, and the database cluster properties that existed at
    the time you deleted the source cluster.
    """

    Engine: Optional[String]
    VpcId: Optional[String]
    DBClusterAutomatedBackupsArn: Optional[String]
    DBClusterIdentifier: Optional[String]
    RestoreWindow: Optional[RestoreWindow]
    MasterUsername: Optional[String]
    DbClusterResourceId: Optional[String]
    Region: Optional[String]
    LicenseModel: Optional[String]
    Status: Optional[String]
    IAMDatabaseAuthenticationEnabled: Optional[Boolean]
    ClusterCreateTime: Optional[TStamp]
    StorageEncrypted: Optional[Boolean]
    AllocatedStorage: Optional[Integer]
    EngineVersion: Optional[String]
    DBClusterArn: Optional[String]
    BackupRetentionPeriod: Optional[IntegerOptional]
    EngineMode: Optional[String]
    AvailabilityZones: Optional[AvailabilityZones]
    Port: Optional[Integer]
    KmsKeyId: Optional[String]
    StorageType: Optional[String]
    Iops: Optional[IntegerOptional]
    AwsBackupRecoveryPointArn: Optional[String]
    StorageThroughput: Optional[IntegerOptional]


DBClusterAutomatedBackupList = List[DBClusterAutomatedBackup]


class DBClusterAutomatedBackupMessage(TypedDict, total=False):
    Marker: Optional[String]
    DBClusterAutomatedBackups: Optional[DBClusterAutomatedBackupList]


class DBClusterBacktrack(TypedDict, total=False):
    """This data type is used as a response element in the
    ``DescribeDBClusterBacktracks`` action.
    """

    DBClusterIdentifier: Optional[String]
    BacktrackIdentifier: Optional[String]
    BacktrackTo: Optional[TStamp]
    BacktrackedFrom: Optional[TStamp]
    BacktrackRequestCreationTime: Optional[TStamp]
    Status: Optional[String]


DBClusterBacktrackList = List[DBClusterBacktrack]


class DBClusterBacktrackMessage(TypedDict, total=False):
    """Contains the result of a successful invocation of the
    ``DescribeDBClusterBacktracks`` action.
    """

    Marker: Optional[String]
    DBClusterBacktracks: Optional[DBClusterBacktrackList]


class DBClusterCapacityInfo(TypedDict, total=False):
    DBClusterIdentifier: Optional[String]
    PendingCapacity: Optional[IntegerOptional]
    CurrentCapacity: Optional[IntegerOptional]
    SecondsBeforeTimeout: Optional[IntegerOptional]
    TimeoutAction: Optional[String]


class DBClusterEndpoint(TypedDict, total=False):
    """This data type represents the information you need to connect to an
    Amazon Aurora DB cluster. This data type is used as a response element
    in the following actions:

    -  ``CreateDBClusterEndpoint``

    -  ``DescribeDBClusterEndpoints``

    -  ``ModifyDBClusterEndpoint``

    -  ``DeleteDBClusterEndpoint``

    For the data structure that represents Amazon RDS DB instance endpoints,
    see ``Endpoint``.
    """

    DBClusterEndpointIdentifier: Optional[String]
    DBClusterIdentifier: Optional[String]
    DBClusterEndpointResourceIdentifier: Optional[String]
    Endpoint: Optional[String]
    Status: Optional[String]
    EndpointType: Optional[String]
    CustomEndpointType: Optional[String]
    StaticMembers: Optional[StringList]
    ExcludedMembers: Optional[StringList]
    DBClusterEndpointArn: Optional[String]


DBClusterEndpointList = List[DBClusterEndpoint]


class DBClusterEndpointMessage(TypedDict, total=False):
    Marker: Optional[String]
    DBClusterEndpoints: Optional[DBClusterEndpointList]


DBClusterList = List[DBCluster]


class DBClusterMessage(TypedDict, total=False):
    """Contains the result of a successful invocation of the
    ``DescribeDBClusters`` action.
    """

    Marker: Optional[String]
    DBClusters: Optional[DBClusterList]


EngineModeList = List[String]


class Parameter(TypedDict, total=False):
    """This data type is used as a request parameter in the
    ``ModifyDBParameterGroup`` and ``ResetDBParameterGroup`` actions.

    This data type is used as a response element in the
    ``DescribeEngineDefaultParameters`` and ``DescribeDBParameters``
    actions.
    """

    ParameterName: Optional[String]
    ParameterValue: Optional[String]
    Description: Optional[String]
    Source: Optional[String]
    ApplyType: Optional[String]
    DataType: Optional[String]
    AllowedValues: Optional[String]
    IsModifiable: Optional[Boolean]
    MinimumEngineVersion: Optional[String]
    ApplyMethod: Optional[ApplyMethod]
    SupportedEngineModes: Optional[EngineModeList]


ParametersList = List[Parameter]


class DBClusterParameterGroupDetails(TypedDict, total=False):
    """Provides details about a DB cluster parameter group including the
    parameters in the DB cluster parameter group.
    """

    Parameters: Optional[ParametersList]
    Marker: Optional[String]


DBClusterParameterGroupList = List[DBClusterParameterGroup]


class DBClusterParameterGroupNameMessage(TypedDict, total=False):
    DBClusterParameterGroupName: Optional[String]


class DBClusterParameterGroupsMessage(TypedDict, total=False):
    Marker: Optional[String]
    DBClusterParameterGroups: Optional[DBClusterParameterGroupList]


class DBClusterSnapshotAttribute(TypedDict, total=False):
    """Contains the name and values of a manual DB cluster snapshot attribute.

    Manual DB cluster snapshot attributes are used to authorize other Amazon
    Web Services accounts to restore a manual DB cluster snapshot. For more
    information, see the ``ModifyDBClusterSnapshotAttribute`` API action.
    """

    AttributeName: Optional[String]
    AttributeValues: Optional[AttributeValueList]


DBClusterSnapshotAttributeList = List[DBClusterSnapshotAttribute]


class DBClusterSnapshotAttributesResult(TypedDict, total=False):
    """Contains the results of a successful call to the
    ``DescribeDBClusterSnapshotAttributes`` API action.

    Manual DB cluster snapshot attributes are used to authorize other Amazon
    Web Services accounts to copy or restore a manual DB cluster snapshot.
    For more information, see the ``ModifyDBClusterSnapshotAttribute`` API
    action.
    """

    DBClusterSnapshotIdentifier: Optional[String]
    DBClusterSnapshotAttributes: Optional[DBClusterSnapshotAttributeList]


DBClusterSnapshotList = List[DBClusterSnapshot]


class DBClusterSnapshotMessage(TypedDict, total=False):
    """Provides a list of DB cluster snapshots for the user as the result of a
    call to the ``DescribeDBClusterSnapshots`` action.
    """

    Marker: Optional[String]
    DBClusterSnapshots: Optional[DBClusterSnapshotList]


class ServerlessV2FeaturesSupport(TypedDict, total=False):
    """Specifies any Aurora Serverless v2 properties or limits that differ
    between Aurora engine versions. You can test the values of this
    attribute when deciding which Aurora version to use in a new or upgraded
    DB cluster. You can also retrieve the version of an existing DB cluster
    and check whether that version supports certain Aurora Serverless v2
    features before you attempt to use those features.
    """

    MinCapacity: Optional[DoubleOptional]
    MaxCapacity: Optional[DoubleOptional]


FeatureNameList = List[String]


class Timezone(TypedDict, total=False):
    """A time zone associated with a ``DBInstance`` or a ``DBSnapshot``. This
    data type is an element in the response to the ``DescribeDBInstances``,
    the ``DescribeDBSnapshots``, and the ``DescribeDBEngineVersions``
    actions.
    """

    TimezoneName: Optional[String]


SupportedTimezonesList = List[Timezone]


class UpgradeTarget(TypedDict, total=False):
    """The version of the database engine that a DB instance can be upgraded
    to.
    """

    Engine: Optional[String]
    EngineVersion: Optional[String]
    Description: Optional[String]
    AutoUpgrade: Optional[Boolean]
    IsMajorVersionUpgrade: Optional[Boolean]
    SupportedEngineModes: Optional[EngineModeList]
    SupportsParallelQuery: Optional[BooleanOptional]
    SupportsGlobalDatabases: Optional[BooleanOptional]
    SupportsBabelfish: Optional[BooleanOptional]
    SupportsLimitlessDatabase: Optional[BooleanOptional]
    SupportsLocalWriteForwarding: Optional[BooleanOptional]
    SupportsIntegrations: Optional[BooleanOptional]


ValidUpgradeTargetList = List[UpgradeTarget]
SupportedCharacterSetsList = List[CharacterSet]


class DBEngineVersion(TypedDict, total=False):
    """This data type is used as a response element in the action
    ``DescribeDBEngineVersions``.
    """

    Engine: Optional[String]
    EngineVersion: Optional[String]
    DBParameterGroupFamily: Optional[String]
    DBEngineDescription: Optional[String]
    DBEngineVersionDescription: Optional[String]
    DefaultCharacterSet: Optional[CharacterSet]
    Image: Optional[CustomDBEngineVersionAMI]
    DBEngineMediaType: Optional[String]
    SupportedCharacterSets: Optional[SupportedCharacterSetsList]
    SupportedNcharCharacterSets: Optional[SupportedCharacterSetsList]
    ValidUpgradeTarget: Optional[ValidUpgradeTargetList]
    SupportedTimezones: Optional[SupportedTimezonesList]
    ExportableLogTypes: Optional[LogTypeList]
    SupportsLogExportsToCloudwatchLogs: Optional[Boolean]
    SupportsReadReplica: Optional[Boolean]
    SupportedEngineModes: Optional[EngineModeList]
    SupportedFeatureNames: Optional[FeatureNameList]
    Status: Optional[String]
    SupportsParallelQuery: Optional[Boolean]
    SupportsGlobalDatabases: Optional[Boolean]
    MajorEngineVersion: Optional[String]
    DatabaseInstallationFilesS3BucketName: Optional[String]
    DatabaseInstallationFilesS3Prefix: Optional[String]
    DBEngineVersionArn: Optional[String]
    KMSKeyId: Optional[String]
    CreateTime: Optional[TStamp]
    TagList: Optional[TagList]
    SupportsBabelfish: Optional[Boolean]
    CustomDBEngineVersionManifest: Optional[CustomDBEngineVersionManifest]
    SupportsLimitlessDatabase: Optional[Boolean]
    SupportsCertificateRotationWithoutRestart: Optional[BooleanOptional]
    SupportedCACertificateIdentifiers: Optional[CACertificateIdentifiersList]
    SupportsLocalWriteForwarding: Optional[BooleanOptional]
    SupportsIntegrations: Optional[Boolean]
    ServerlessV2FeaturesSupport: Optional[ServerlessV2FeaturesSupport]


DBEngineVersionList = List[DBEngineVersion]


class DBEngineVersionMessage(TypedDict, total=False):
    """Contains the result of a successful invocation of the
    ``DescribeDBEngineVersions`` action.
    """

    Marker: Optional[String]
    DBEngineVersions: Optional[DBEngineVersionList]


class DBInstanceAutomatedBackup(TypedDict, total=False):
    """An automated backup of a DB instance. It consists of system backups,
    transaction logs, and the database instance properties that existed at
    the time you deleted the source instance.
    """

    DBInstanceArn: Optional[String]
    DbiResourceId: Optional[String]
    Region: Optional[String]
    DBInstanceIdentifier: Optional[String]
    RestoreWindow: Optional[RestoreWindow]
    AllocatedStorage: Optional[Integer]
    Status: Optional[String]
    Port: Optional[Integer]
    AvailabilityZone: Optional[String]
    VpcId: Optional[String]
    InstanceCreateTime: Optional[TStamp]
    MasterUsername: Optional[String]
    Engine: Optional[String]
    EngineVersion: Optional[String]
    LicenseModel: Optional[String]
    Iops: Optional[IntegerOptional]
    OptionGroupName: Optional[String]
    TdeCredentialArn: Optional[String]
    Encrypted: Optional[Boolean]
    StorageType: Optional[String]
    KmsKeyId: Optional[String]
    Timezone: Optional[String]
    IAMDatabaseAuthenticationEnabled: Optional[Boolean]
    BackupRetentionPeriod: Optional[IntegerOptional]
    DBInstanceAutomatedBackupsArn: Optional[String]
    DBInstanceAutomatedBackupsReplications: Optional[DBInstanceAutomatedBackupsReplicationList]
    BackupTarget: Optional[String]
    StorageThroughput: Optional[IntegerOptional]
    AwsBackupRecoveryPointArn: Optional[String]
    DedicatedLogVolume: Optional[BooleanOptional]
    MultiTenant: Optional[BooleanOptional]


DBInstanceAutomatedBackupList = List[DBInstanceAutomatedBackup]


class DBInstanceAutomatedBackupMessage(TypedDict, total=False):
    """Contains the result of a successful invocation of the
    ``DescribeDBInstanceAutomatedBackups`` action.
    """

    Marker: Optional[String]
    DBInstanceAutomatedBackups: Optional[DBInstanceAutomatedBackupList]


DBInstanceList = List[DBInstance]


class DBInstanceMessage(TypedDict, total=False):
    """Contains the result of a successful invocation of the
    ``DescribeDBInstances`` action.
    """

    Marker: Optional[String]
    DBInstances: Optional[DBInstanceList]


class SupportedEngineLifecycle(TypedDict, total=False):
    """This data type is used as a response element in the operation
    ``DescribeDBMajorEngineVersions``.

    You can use the information that this data type returns to plan for
    upgrades.

    This data type only returns information for the open source engines
    Amazon RDS for MariaDB, Amazon RDS for MySQL, Amazon RDS for PostgreSQL,
    Aurora MySQL, and Aurora PostgreSQL.
    """

    LifecycleSupportName: LifecycleSupportName
    LifecycleSupportStartDate: TStamp
    LifecycleSupportEndDate: TStamp


SupportedEngineLifecycleList = List[SupportedEngineLifecycle]


class DBMajorEngineVersion(TypedDict, total=False):
    """This data type is used as a response element in the operation
    ``DescribeDBMajorEngineVersions``.
    """

    Engine: Optional[String]
    MajorEngineVersion: Optional[String]
    SupportedEngineLifecycles: Optional[SupportedEngineLifecycleList]


DBMajorEngineVersionsList = List[DBMajorEngineVersion]


class DBParameterGroupDetails(TypedDict, total=False):
    """Contains the result of a successful invocation of the
    ``DescribeDBParameters`` action.
    """

    Parameters: Optional[ParametersList]
    Marker: Optional[String]


DBParameterGroupList = List[DBParameterGroup]


class DBParameterGroupNameMessage(TypedDict, total=False):
    """Contains the result of a successful invocation of the
    ``ModifyDBParameterGroup`` or ``ResetDBParameterGroup`` operation.
    """

    DBParameterGroupName: Optional[String]


class DBParameterGroupsMessage(TypedDict, total=False):
    """Contains the result of a successful invocation of the
    ``DescribeDBParameterGroups`` action.
    """

    Marker: Optional[String]
    DBParameterGroups: Optional[DBParameterGroupList]


DBProxyEndpointList = List[DBProxyEndpoint]
DBProxyList = List[DBProxy]


class TargetHealth(TypedDict, total=False):
    """Information about the connection health of an RDS Proxy target."""

    State: Optional[TargetState]
    Reason: Optional[TargetHealthReason]
    Description: Optional[String]


class DBProxyTarget(TypedDict, total=False):
    """Contains the details for an RDS Proxy target. It represents an RDS DB
    instance or Aurora DB cluster that the proxy can connect to. One or more
    targets are associated with an RDS Proxy target group.

    This data type is used as a response element in the
    ``DescribeDBProxyTargets`` action.
    """

    TargetArn: Optional[String]
    Endpoint: Optional[String]
    TrackedClusterId: Optional[String]
    RdsResourceId: Optional[String]
    Port: Optional[Integer]
    Type: Optional[TargetType]
    Role: Optional[TargetRole]
    TargetHealth: Optional[TargetHealth]


class DBProxyTargetGroup(TypedDict, total=False):
    """Represents a set of RDS DB instances, Aurora DB clusters, or both that a
    proxy can connect to. Currently, each target group is associated with
    exactly one RDS DB instance or Aurora DB cluster.

    This data type is used as a response element in the
    ``DescribeDBProxyTargetGroups`` action.
    """

    DBProxyName: Optional[String]
    TargetGroupName: Optional[String]
    TargetGroupArn: Optional[String]
    IsDefault: Optional[Boolean]
    Status: Optional[String]
    ConnectionPoolConfig: Optional[ConnectionPoolConfigurationInfo]
    CreatedDate: Optional[TStamp]
    UpdatedDate: Optional[TStamp]


class PerformanceInsightsMetricDimensionGroup(TypedDict, total=False):
    """A logical grouping of Performance Insights metrics for a related subject
    area. For example, the ``db.sql`` dimension group consists of the
    following dimensions:

    -  ``db.sql.id`` - The hash of a running SQL statement, generated by
       Performance Insights.

    -  ``db.sql.db_id`` - Either the SQL ID generated by the database
       engine, or a value generated by Performance Insights that begins with
       ``pi-``.

    -  ``db.sql.statement`` - The full text of the SQL statement that is
       running, for example, ``SELECT * FROM employees``.

    -  ``db.sql_tokenized.id`` - The hash of the SQL digest generated by
       Performance Insights.

    Each response element returns a maximum of 500 bytes. For larger
    elements, such as SQL statements, only the first 500 bytes are returned.
    """

    Dimensions: Optional[StringList]
    Group: Optional[String]
    Limit: Optional[Integer]


class PerformanceInsightsMetricQuery(TypedDict, total=False):
    """A single Performance Insights metric query to process. You must provide
    the metric to the query. If other parameters aren't specified,
    Performance Insights returns all data points for the specified metric.
    Optionally, you can request the data points to be aggregated by
    dimension group (``GroupBy``) and return only those data points that
    match your criteria (``Filter``).

    Constraints:

    -  Must be a valid Performance Insights query.
    """

    GroupBy: Optional[PerformanceInsightsMetricDimensionGroup]
    Metric: Optional[String]


class MetricQuery(TypedDict, total=False):
    """The query to retrieve metric data points."""

    PerformanceInsightsMetricQuery: Optional[PerformanceInsightsMetricQuery]


class ScalarReferenceDetails(TypedDict, total=False):
    """The metric reference details when the reference is a scalar."""

    Value: Optional[Double]


class ReferenceDetails(TypedDict, total=False):
    """The reference details of a metric."""

    ScalarReferenceDetails: Optional[ScalarReferenceDetails]


class MetricReference(TypedDict, total=False):
    """The reference (threshold) for a metric."""

    Name: Optional[String]
    ReferenceDetails: Optional[ReferenceDetails]


MetricReferenceList = List[MetricReference]


class Metric(TypedDict, total=False):
    """The representation of a metric."""

    Name: Optional[String]
    References: Optional[MetricReferenceList]
    StatisticsDetails: Optional[String]
    MetricQuery: Optional[MetricQuery]


MetricList = List[Metric]


class PerformanceIssueDetails(TypedDict, total=False):
    """Details of the performance issue."""

    StartTime: Optional[TStamp]
    EndTime: Optional[TStamp]
    Metrics: Optional[MetricList]
    Analysis: Optional[String]


class IssueDetails(TypedDict, total=False):
    """The details of an issue with your DB instances, DB clusters, and DB
    parameter groups.
    """

    PerformanceIssueDetails: Optional[PerformanceIssueDetails]


class DocLink(TypedDict, total=False):
    """A link to documentation that provides additional information for a
    recommendation.
    """

    Text: Optional[String]
    Url: Optional[String]


DocLinkList = List[DocLink]


class RecommendedActionParameter(TypedDict, total=False):
    """A single parameter to use with the ``RecommendedAction`` API operation
    to apply the action.
    """

    Key: Optional[String]
    Value: Optional[String]


RecommendedActionParameterList = List[RecommendedActionParameter]


class RecommendedAction(TypedDict, total=False):
    """The recommended actions to apply to resolve the issues associated with
    your DB instances, DB clusters, and DB parameter groups.
    """

    ActionId: Optional[String]
    Title: Optional[String]
    Description: Optional[String]
    Operation: Optional[String]
    Parameters: Optional[RecommendedActionParameterList]
    ApplyModes: Optional[StringList]
    Status: Optional[String]
    IssueDetails: Optional[IssueDetails]
    ContextAttributes: Optional[ContextAttributeList]


RecommendedActionList = List[RecommendedAction]


class DBRecommendation(TypedDict, total=False):
    """The recommendation for your DB instances, DB clusters, and DB parameter
    groups.
    """

    RecommendationId: Optional[String]
    TypeId: Optional[String]
    Severity: Optional[String]
    ResourceArn: Optional[String]
    Status: Optional[String]
    CreatedTime: Optional[TStamp]
    UpdatedTime: Optional[TStamp]
    Detection: Optional[String]
    Recommendation: Optional[String]
    Description: Optional[String]
    Reason: Optional[String]
    RecommendedActions: Optional[RecommendedActionList]
    Category: Optional[String]
    Source: Optional[String]
    TypeDetection: Optional[String]
    TypeRecommendation: Optional[String]
    Impact: Optional[String]
    AdditionalInfo: Optional[String]
    Links: Optional[DocLinkList]
    IssueDetails: Optional[IssueDetails]


DBRecommendationList = List[DBRecommendation]


class DBRecommendationMessage(TypedDict, total=False):
    DBRecommendation: Optional[DBRecommendation]


class DBRecommendationsMessage(TypedDict, total=False):
    DBRecommendations: Optional[DBRecommendationList]
    Marker: Optional[String]


DBSecurityGroups = List[DBSecurityGroup]


class DBSecurityGroupMessage(TypedDict, total=False):
    """Contains the result of a successful invocation of the
    ``DescribeDBSecurityGroups`` action.
    """

    Marker: Optional[String]
    DBSecurityGroups: Optional[DBSecurityGroups]


class DBShardGroup(TypedDict, total=False):
    """Contains the details for an Amazon RDS DB shard group."""

    DBShardGroupResourceId: Optional[String]
    DBShardGroupIdentifier: Optional[DBShardGroupIdentifier]
    DBClusterIdentifier: Optional[String]
    MaxACU: Optional[DoubleOptional]
    MinACU: Optional[DoubleOptional]
    ComputeRedundancy: Optional[IntegerOptional]
    Status: Optional[String]
    PubliclyAccessible: Optional[BooleanOptional]
    Endpoint: Optional[String]
    DBShardGroupArn: Optional[String]
    TagList: Optional[TagList]


DBShardGroupsList = List[DBShardGroup]


class DBSnapshotAttribute(TypedDict, total=False):
    """Contains the name and values of a manual DB snapshot attribute

    Manual DB snapshot attributes are used to authorize other Amazon Web
    Services accounts to restore a manual DB snapshot. For more information,
    see the ``ModifyDBSnapshotAttribute`` API.
    """

    AttributeName: Optional[String]
    AttributeValues: Optional[AttributeValueList]


DBSnapshotAttributeList = List[DBSnapshotAttribute]


class DBSnapshotAttributesResult(TypedDict, total=False):
    """Contains the results of a successful call to the
    ``DescribeDBSnapshotAttributes`` API action.

    Manual DB snapshot attributes are used to authorize other Amazon Web
    Services accounts to copy or restore a manual DB snapshot. For more
    information, see the ``ModifyDBSnapshotAttribute`` API action.
    """

    DBSnapshotIdentifier: Optional[String]
    DBSnapshotAttributes: Optional[DBSnapshotAttributeList]


DBSnapshotList = List[DBSnapshot]


class DBSnapshotMessage(TypedDict, total=False):
    """Contains the result of a successful invocation of the
    ``DescribeDBSnapshots`` action.
    """

    Marker: Optional[String]
    DBSnapshots: Optional[DBSnapshotList]


class DBSnapshotTenantDatabase(TypedDict, total=False):
    """Contains the details of a tenant database in a snapshot of a DB
    instance.
    """

    DBSnapshotIdentifier: Optional[String]
    DBInstanceIdentifier: Optional[String]
    DbiResourceId: Optional[String]
    EngineName: Optional[String]
    SnapshotType: Optional[String]
    TenantDatabaseCreateTime: Optional[TStamp]
    TenantDBName: Optional[String]
    MasterUsername: Optional[String]
    TenantDatabaseResourceId: Optional[String]
    CharacterSetName: Optional[String]
    DBSnapshotTenantDatabaseARN: Optional[String]
    NcharCharacterSetName: Optional[String]
    TagList: Optional[TagList]


DBSnapshotTenantDatabasesList = List[DBSnapshotTenantDatabase]


class DBSnapshotTenantDatabasesMessage(TypedDict, total=False):
    Marker: Optional[String]
    DBSnapshotTenantDatabases: Optional[DBSnapshotTenantDatabasesList]


DBSubnetGroups = List[DBSubnetGroup]


class DBSubnetGroupMessage(TypedDict, total=False):
    """Contains the result of a successful invocation of the
    ``DescribeDBSubnetGroups`` action.
    """

    Marker: Optional[String]
    DBSubnetGroups: Optional[DBSubnetGroups]


class DeleteBlueGreenDeploymentRequest(ServiceRequest):
    BlueGreenDeploymentIdentifier: BlueGreenDeploymentIdentifier
    DeleteTarget: Optional[BooleanOptional]


class DeleteBlueGreenDeploymentResponse(TypedDict, total=False):
    BlueGreenDeployment: Optional[BlueGreenDeployment]


class DeleteCustomDBEngineVersionMessage(ServiceRequest):
    Engine: CustomEngineName
    EngineVersion: CustomEngineVersion


class DeleteDBClusterAutomatedBackupMessage(ServiceRequest):
    DbClusterResourceId: String


class DeleteDBClusterAutomatedBackupResult(TypedDict, total=False):
    DBClusterAutomatedBackup: Optional[DBClusterAutomatedBackup]


class DeleteDBClusterEndpointMessage(ServiceRequest):
    DBClusterEndpointIdentifier: String


class DeleteDBClusterMessage(ServiceRequest):
    DBClusterIdentifier: String
    SkipFinalSnapshot: Optional[Boolean]
    FinalDBSnapshotIdentifier: Optional[String]
    DeleteAutomatedBackups: Optional[BooleanOptional]


class DeleteDBClusterParameterGroupMessage(ServiceRequest):
    DBClusterParameterGroupName: String


class DeleteDBClusterResult(TypedDict, total=False):
    DBCluster: Optional[DBCluster]


class DeleteDBClusterSnapshotMessage(ServiceRequest):
    DBClusterSnapshotIdentifier: String


class DeleteDBClusterSnapshotResult(TypedDict, total=False):
    DBClusterSnapshot: Optional[DBClusterSnapshot]


class DeleteDBInstanceAutomatedBackupMessage(ServiceRequest):
    """Parameter input for the ``DeleteDBInstanceAutomatedBackup`` operation."""

    DbiResourceId: Optional[String]
    DBInstanceAutomatedBackupsArn: Optional[String]


class DeleteDBInstanceAutomatedBackupResult(TypedDict, total=False):
    DBInstanceAutomatedBackup: Optional[DBInstanceAutomatedBackup]


class DeleteDBInstanceMessage(ServiceRequest):
    DBInstanceIdentifier: String
    SkipFinalSnapshot: Optional[Boolean]
    FinalDBSnapshotIdentifier: Optional[String]
    DeleteAutomatedBackups: Optional[BooleanOptional]


class DeleteDBInstanceResult(TypedDict, total=False):
    DBInstance: Optional[DBInstance]


class DeleteDBParameterGroupMessage(ServiceRequest):
    DBParameterGroupName: String


class DeleteDBProxyEndpointRequest(ServiceRequest):
    DBProxyEndpointName: DBProxyEndpointName


class DeleteDBProxyEndpointResponse(TypedDict, total=False):
    DBProxyEndpoint: Optional[DBProxyEndpoint]


class DeleteDBProxyRequest(ServiceRequest):
    DBProxyName: String


class DeleteDBProxyResponse(TypedDict, total=False):
    DBProxy: Optional[DBProxy]


class DeleteDBSecurityGroupMessage(ServiceRequest):
    DBSecurityGroupName: String


class DeleteDBShardGroupMessage(ServiceRequest):
    DBShardGroupIdentifier: DBShardGroupIdentifier


class DeleteDBSnapshotMessage(ServiceRequest):
    DBSnapshotIdentifier: String


class DeleteDBSnapshotResult(TypedDict, total=False):
    DBSnapshot: Optional[DBSnapshot]


class DeleteDBSubnetGroupMessage(ServiceRequest):
    DBSubnetGroupName: String


class DeleteEventSubscriptionMessage(ServiceRequest):
    SubscriptionName: String


class DeleteEventSubscriptionResult(TypedDict, total=False):
    EventSubscription: Optional[EventSubscription]


class DeleteGlobalClusterMessage(ServiceRequest):
    GlobalClusterIdentifier: String


class DeleteGlobalClusterResult(TypedDict, total=False):
    GlobalCluster: Optional[GlobalCluster]


class DeleteIntegrationMessage(ServiceRequest):
    IntegrationIdentifier: IntegrationIdentifier


class DeleteOptionGroupMessage(ServiceRequest):
    OptionGroupName: String


class DeleteTenantDatabaseMessage(ServiceRequest):
    DBInstanceIdentifier: String
    TenantDBName: String
    SkipFinalSnapshot: Optional[Boolean]
    FinalDBSnapshotIdentifier: Optional[String]


class DeleteTenantDatabaseResult(TypedDict, total=False):
    TenantDatabase: Optional[TenantDatabase]


class DeregisterDBProxyTargetsRequest(ServiceRequest):
    DBProxyName: String
    TargetGroupName: Optional[String]
    DBInstanceIdentifiers: Optional[StringList]
    DBClusterIdentifiers: Optional[StringList]


class DeregisterDBProxyTargetsResponse(TypedDict, total=False):
    pass


class DescribeAccountAttributesMessage(ServiceRequest):
    pass


FilterValueList = List[String]


class Filter(TypedDict, total=False):
    """A filter name and value pair that is used to return a more specific list
    of results from a describe operation. Filters can be used to match a set
    of resources by specific criteria, such as IDs. The filters supported by
    a describe operation are documented with the describe operation.

    Currently, wildcards are not supported in filters.

    The following actions can be filtered:

    -  ``DescribeDBClusterBacktracks``

    -  ``DescribeDBClusterEndpoints``

    -  ``DescribeDBClusters``

    -  ``DescribeDBInstances``

    -  ``DescribeDBRecommendations``

    -  ``DescribeDBShardGroups``

    -  ``DescribePendingMaintenanceActions``
    """

    Name: String
    Values: FilterValueList


FilterList = List[Filter]


class DescribeBlueGreenDeploymentsRequest(ServiceRequest):
    BlueGreenDeploymentIdentifier: Optional[BlueGreenDeploymentIdentifier]
    Filters: Optional[FilterList]
    Marker: Optional[String]
    MaxRecords: Optional[MaxRecords]


class DescribeBlueGreenDeploymentsResponse(TypedDict, total=False):
    BlueGreenDeployments: Optional[BlueGreenDeploymentList]
    Marker: Optional[String]


class DescribeCertificatesMessage(ServiceRequest):
    CertificateIdentifier: Optional[String]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class DescribeDBClusterAutomatedBackupsMessage(ServiceRequest):
    DbClusterResourceId: Optional[String]
    DBClusterIdentifier: Optional[String]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class DescribeDBClusterBacktracksMessage(ServiceRequest):
    DBClusterIdentifier: String
    BacktrackIdentifier: Optional[String]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class DescribeDBClusterEndpointsMessage(ServiceRequest):
    DBClusterIdentifier: Optional[String]
    DBClusterEndpointIdentifier: Optional[String]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class DescribeDBClusterParameterGroupsMessage(ServiceRequest):
    DBClusterParameterGroupName: Optional[String]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class DescribeDBClusterParametersMessage(ServiceRequest):
    DBClusterParameterGroupName: String
    Source: Optional[String]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class DescribeDBClusterSnapshotAttributesMessage(ServiceRequest):
    DBClusterSnapshotIdentifier: String


class DescribeDBClusterSnapshotAttributesResult(TypedDict, total=False):
    DBClusterSnapshotAttributesResult: Optional[DBClusterSnapshotAttributesResult]


class DescribeDBClusterSnapshotsMessage(ServiceRequest):
    DBClusterIdentifier: Optional[String]
    DBClusterSnapshotIdentifier: Optional[String]
    SnapshotType: Optional[String]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]
    IncludeShared: Optional[Boolean]
    IncludePublic: Optional[Boolean]
    DbClusterResourceId: Optional[String]


class DescribeDBClustersMessage(ServiceRequest):
    DBClusterIdentifier: Optional[String]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]
    IncludeShared: Optional[Boolean]


class DescribeDBEngineVersionsMessage(ServiceRequest):
    Engine: Optional[String]
    EngineVersion: Optional[String]
    DBParameterGroupFamily: Optional[String]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]
    DefaultOnly: Optional[Boolean]
    ListSupportedCharacterSets: Optional[BooleanOptional]
    ListSupportedTimezones: Optional[BooleanOptional]
    IncludeAll: Optional[BooleanOptional]


class DescribeDBInstanceAutomatedBackupsMessage(ServiceRequest):
    """Parameter input for DescribeDBInstanceAutomatedBackups."""

    DbiResourceId: Optional[String]
    DBInstanceIdentifier: Optional[String]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]
    DBInstanceAutomatedBackupsArn: Optional[String]


class DescribeDBInstancesMessage(ServiceRequest):
    DBInstanceIdentifier: Optional[String]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class DescribeDBLogFilesDetails(TypedDict, total=False):
    """This data type is used as a response element to ``DescribeDBLogFiles``."""

    LogFileName: Optional[String]
    LastWritten: Optional[Long]
    Size: Optional[Long]


DescribeDBLogFilesList = List[DescribeDBLogFilesDetails]


class DescribeDBLogFilesMessage(ServiceRequest):
    DBInstanceIdentifier: String
    FilenameContains: Optional[String]
    FileLastWritten: Optional[Long]
    FileSize: Optional[Long]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class DescribeDBLogFilesResponse(TypedDict, total=False):
    """The response from a call to ``DescribeDBLogFiles``."""

    DescribeDBLogFiles: Optional[DescribeDBLogFilesList]
    Marker: Optional[String]


class DescribeDBMajorEngineVersionsRequest(ServiceRequest):
    Engine: Optional[Engine]
    MajorEngineVersion: Optional[MajorEngineVersion]
    Marker: Optional[Marker]
    MaxRecords: Optional[MaxRecords]


class DescribeDBMajorEngineVersionsResponse(TypedDict, total=False):
    DBMajorEngineVersions: Optional[DBMajorEngineVersionsList]
    Marker: Optional[String]


class DescribeDBParameterGroupsMessage(ServiceRequest):
    DBParameterGroupName: Optional[String]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class DescribeDBParametersMessage(ServiceRequest):
    DBParameterGroupName: String
    Source: Optional[String]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class DescribeDBProxiesRequest(ServiceRequest):
    DBProxyName: Optional[String]
    Filters: Optional[FilterList]
    Marker: Optional[String]
    MaxRecords: Optional[MaxRecords]


class DescribeDBProxiesResponse(TypedDict, total=False):
    DBProxies: Optional[DBProxyList]
    Marker: Optional[String]


class DescribeDBProxyEndpointsRequest(ServiceRequest):
    DBProxyName: Optional[DBProxyName]
    DBProxyEndpointName: Optional[DBProxyEndpointName]
    Filters: Optional[FilterList]
    Marker: Optional[String]
    MaxRecords: Optional[MaxRecords]


class DescribeDBProxyEndpointsResponse(TypedDict, total=False):
    DBProxyEndpoints: Optional[DBProxyEndpointList]
    Marker: Optional[String]


class DescribeDBProxyTargetGroupsRequest(ServiceRequest):
    DBProxyName: String
    TargetGroupName: Optional[String]
    Filters: Optional[FilterList]
    Marker: Optional[String]
    MaxRecords: Optional[MaxRecords]


TargetGroupList = List[DBProxyTargetGroup]


class DescribeDBProxyTargetGroupsResponse(TypedDict, total=False):
    TargetGroups: Optional[TargetGroupList]
    Marker: Optional[String]


class DescribeDBProxyTargetsRequest(ServiceRequest):
    DBProxyName: String
    TargetGroupName: Optional[String]
    Filters: Optional[FilterList]
    Marker: Optional[String]
    MaxRecords: Optional[MaxRecords]


TargetList = List[DBProxyTarget]


class DescribeDBProxyTargetsResponse(TypedDict, total=False):
    Targets: Optional[TargetList]
    Marker: Optional[String]


class DescribeDBRecommendationsMessage(ServiceRequest):
    LastUpdatedAfter: Optional[TStamp]
    LastUpdatedBefore: Optional[TStamp]
    Locale: Optional[String]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class DescribeDBSecurityGroupsMessage(ServiceRequest):
    DBSecurityGroupName: Optional[String]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class DescribeDBShardGroupsMessage(ServiceRequest):
    DBShardGroupIdentifier: Optional[DBShardGroupIdentifier]
    Filters: Optional[FilterList]
    Marker: Optional[String]
    MaxRecords: Optional[MaxRecords]


class DescribeDBShardGroupsResponse(TypedDict, total=False):
    DBShardGroups: Optional[DBShardGroupsList]
    Marker: Optional[String]


class DescribeDBSnapshotAttributesMessage(ServiceRequest):
    DBSnapshotIdentifier: String


class DescribeDBSnapshotAttributesResult(TypedDict, total=False):
    DBSnapshotAttributesResult: Optional[DBSnapshotAttributesResult]


class DescribeDBSnapshotTenantDatabasesMessage(ServiceRequest):
    DBInstanceIdentifier: Optional[String]
    DBSnapshotIdentifier: Optional[String]
    SnapshotType: Optional[String]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]
    DbiResourceId: Optional[String]


class DescribeDBSnapshotsMessage(ServiceRequest):
    DBInstanceIdentifier: Optional[String]
    DBSnapshotIdentifier: Optional[String]
    SnapshotType: Optional[String]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]
    IncludeShared: Optional[Boolean]
    IncludePublic: Optional[Boolean]
    DbiResourceId: Optional[String]


class DescribeDBSubnetGroupsMessage(ServiceRequest):
    DBSubnetGroupName: Optional[String]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class DescribeEngineDefaultClusterParametersMessage(ServiceRequest):
    DBParameterGroupFamily: String
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class EngineDefaults(TypedDict, total=False):
    """Contains the result of a successful invocation of the
    ``DescribeEngineDefaultParameters`` action.
    """

    DBParameterGroupFamily: Optional[String]
    Marker: Optional[String]
    Parameters: Optional[ParametersList]


class DescribeEngineDefaultClusterParametersResult(TypedDict, total=False):
    EngineDefaults: Optional[EngineDefaults]


class DescribeEngineDefaultParametersMessage(ServiceRequest):
    DBParameterGroupFamily: String
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class DescribeEngineDefaultParametersResult(TypedDict, total=False):
    EngineDefaults: Optional[EngineDefaults]


class DescribeEventCategoriesMessage(ServiceRequest):
    SourceType: Optional[String]
    Filters: Optional[FilterList]


class DescribeEventSubscriptionsMessage(ServiceRequest):
    SubscriptionName: Optional[String]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class DescribeEventsMessage(ServiceRequest):
    SourceIdentifier: Optional[String]
    SourceType: Optional[SourceType]
    StartTime: Optional[TStamp]
    EndTime: Optional[TStamp]
    Duration: Optional[IntegerOptional]
    EventCategories: Optional[EventCategoriesList]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class DescribeExportTasksMessage(ServiceRequest):
    ExportTaskIdentifier: Optional[String]
    SourceArn: Optional[String]
    Filters: Optional[FilterList]
    Marker: Optional[String]
    MaxRecords: Optional[MaxRecords]
    SourceType: Optional[ExportSourceType]


class DescribeGlobalClustersMessage(ServiceRequest):
    GlobalClusterIdentifier: Optional[String]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class DescribeIntegrationsMessage(ServiceRequest):
    IntegrationIdentifier: Optional[IntegrationIdentifier]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[Marker]


class IntegrationError(TypedDict, total=False):
    """An error associated with a zero-ETL integration with Amazon Redshift."""

    ErrorCode: String
    ErrorMessage: Optional[String]


IntegrationErrorList = List[IntegrationError]


class Integration(TypedDict, total=False):
    """A zero-ETL integration with Amazon Redshift."""

    SourceArn: Optional[SourceArn]
    TargetArn: Optional[Arn]
    IntegrationName: Optional[IntegrationName]
    IntegrationArn: Optional[IntegrationArn]
    KMSKeyId: Optional[String]
    AdditionalEncryptionContext: Optional[EncryptionContextMap]
    Status: Optional[IntegrationStatus]
    Tags: Optional[TagList]
    CreateTime: Optional[TStamp]
    Errors: Optional[IntegrationErrorList]
    DataFilter: Optional[DataFilter]
    Description: Optional[IntegrationDescription]


IntegrationList = List[Integration]


class DescribeIntegrationsResponse(TypedDict, total=False):
    Marker: Optional[Marker]
    Integrations: Optional[IntegrationList]


class DescribeOptionGroupOptionsMessage(ServiceRequest):
    EngineName: String
    MajorEngineVersion: Optional[String]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class DescribeOptionGroupsMessage(ServiceRequest):
    OptionGroupName: Optional[String]
    Filters: Optional[FilterList]
    Marker: Optional[String]
    MaxRecords: Optional[IntegerOptional]
    EngineName: Optional[String]
    MajorEngineVersion: Optional[String]


class DescribeOrderableDBInstanceOptionsMessage(ServiceRequest):
    Engine: String
    EngineVersion: Optional[String]
    DBInstanceClass: Optional[String]
    LicenseModel: Optional[String]
    AvailabilityZoneGroup: Optional[String]
    Vpc: Optional[BooleanOptional]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class DescribePendingMaintenanceActionsMessage(ServiceRequest):
    ResourceIdentifier: Optional[String]
    Filters: Optional[FilterList]
    Marker: Optional[String]
    MaxRecords: Optional[IntegerOptional]


class DescribeReservedDBInstancesMessage(ServiceRequest):
    ReservedDBInstanceId: Optional[String]
    ReservedDBInstancesOfferingId: Optional[String]
    DBInstanceClass: Optional[String]
    Duration: Optional[String]
    ProductDescription: Optional[String]
    OfferingType: Optional[String]
    MultiAZ: Optional[BooleanOptional]
    LeaseId: Optional[String]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class DescribeReservedDBInstancesOfferingsMessage(ServiceRequest):
    ReservedDBInstancesOfferingId: Optional[String]
    DBInstanceClass: Optional[String]
    Duration: Optional[String]
    ProductDescription: Optional[String]
    OfferingType: Optional[String]
    MultiAZ: Optional[BooleanOptional]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class DescribeSourceRegionsMessage(ServiceRequest):
    RegionName: Optional[String]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]
    Filters: Optional[FilterList]


class DescribeTenantDatabasesMessage(ServiceRequest):
    DBInstanceIdentifier: Optional[String]
    TenantDBName: Optional[String]
    Filters: Optional[FilterList]
    Marker: Optional[String]
    MaxRecords: Optional[IntegerOptional]


class DescribeValidDBInstanceModificationsMessage(ServiceRequest):
    DBInstanceIdentifier: String


class DoubleRange(TypedDict, total=False):
    """A range of double values."""

    From: Optional[Double]
    To: Optional[Double]


DoubleRangeList = List[DoubleRange]


class Range(TypedDict, total=False):
    """A range of integer values."""

    From: Optional[Integer]
    To: Optional[Integer]
    Step: Optional[IntegerOptional]


RangeList = List[Range]


class ValidStorageOptions(TypedDict, total=False):
    """Information about valid modifications that you can make to your DB
    instance. Contains the result of a successful call to the
    ``DescribeValidDBInstanceModifications`` action.
    """

    StorageType: Optional[String]
    StorageSize: Optional[RangeList]
    ProvisionedIops: Optional[RangeList]
    IopsToStorageRatio: Optional[DoubleRangeList]
    SupportsStorageAutoscaling: Optional[Boolean]
    ProvisionedStorageThroughput: Optional[RangeList]
    StorageThroughputToIopsRatio: Optional[DoubleRangeList]


ValidStorageOptionsList = List[ValidStorageOptions]


class ValidDBInstanceModificationsMessage(TypedDict, total=False):
    """Information about valid modifications that you can make to your DB
    instance. Contains the result of a successful call to the
    ``DescribeValidDBInstanceModifications`` action. You can use this
    information when you call ``ModifyDBInstance``.
    """

    Storage: Optional[ValidStorageOptionsList]
    ValidProcessorFeatures: Optional[AvailableProcessorFeatureList]
    SupportsDedicatedLogVolume: Optional[Boolean]


class DescribeValidDBInstanceModificationsResult(TypedDict, total=False):
    ValidDBInstanceModificationsMessage: Optional[ValidDBInstanceModificationsMessage]


class DisableHttpEndpointRequest(ServiceRequest):
    ResourceArn: String


class DisableHttpEndpointResponse(TypedDict, total=False):
    ResourceArn: Optional[String]
    HttpEndpointEnabled: Optional[Boolean]


class DownloadDBLogFilePortionDetails(TypedDict, total=False):
    """This data type is used as a response element to
    ``DownloadDBLogFilePortion``.
    """

    LogFileData: Optional[String]
    Marker: Optional[String]
    AdditionalDataPending: Optional[Boolean]


class DownloadDBLogFilePortionMessage(ServiceRequest):
    DBInstanceIdentifier: String
    LogFileName: String
    Marker: Optional[String]
    NumberOfLines: Optional[Integer]


class EnableHttpEndpointRequest(ServiceRequest):
    ResourceArn: String


class EnableHttpEndpointResponse(TypedDict, total=False):
    ResourceArn: Optional[String]
    HttpEndpointEnabled: Optional[Boolean]


class Event(TypedDict, total=False):
    """This data type is used as a response element in the
    `DescribeEvents <https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeEvents.html>`__
    action.
    """

    SourceIdentifier: Optional[String]
    SourceType: Optional[SourceType]
    Message: Optional[String]
    EventCategories: Optional[EventCategoriesList]
    Date: Optional[TStamp]
    SourceArn: Optional[String]


class EventCategoriesMap(TypedDict, total=False):
    """Contains the results of a successful invocation of the
    `DescribeEventCategories <https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeEventCategories.html>`__
    operation.
    """

    SourceType: Optional[String]
    EventCategories: Optional[EventCategoriesList]


EventCategoriesMapList = List[EventCategoriesMap]


class EventCategoriesMessage(TypedDict, total=False):
    """Data returned from the ``DescribeEventCategories`` operation."""

    EventCategoriesMapList: Optional[EventCategoriesMapList]


EventList = List[Event]
EventSubscriptionsList = List[EventSubscription]


class EventSubscriptionsMessage(TypedDict, total=False):
    """Data returned by the **DescribeEventSubscriptions** action."""

    Marker: Optional[String]
    EventSubscriptionsList: Optional[EventSubscriptionsList]


class EventsMessage(TypedDict, total=False):
    """Contains the result of a successful invocation of the ``DescribeEvents``
    action.
    """

    Marker: Optional[String]
    Events: Optional[EventList]


class ExportTask(TypedDict, total=False):
    """Contains the details of a snapshot or cluster export to Amazon S3.

    This data type is used as a response element in the
    ``DescribeExportTasks`` operation.
    """

    ExportTaskIdentifier: Optional[String]
    SourceArn: Optional[String]
    ExportOnly: Optional[StringList]
    SnapshotTime: Optional[TStamp]
    TaskStartTime: Optional[TStamp]
    TaskEndTime: Optional[TStamp]
    S3Bucket: Optional[String]
    S3Prefix: Optional[String]
    IamRoleArn: Optional[String]
    KmsKeyId: Optional[String]
    Status: Optional[String]
    PercentProgress: Optional[Integer]
    TotalExtractedDataInGB: Optional[Integer]
    FailureCause: Optional[String]
    WarningMessage: Optional[String]
    SourceType: Optional[ExportSourceType]


ExportTasksList = List[ExportTask]


class ExportTasksMessage(TypedDict, total=False):
    Marker: Optional[String]
    ExportTasks: Optional[ExportTasksList]


class FailoverDBClusterMessage(ServiceRequest):
    DBClusterIdentifier: String
    TargetDBInstanceIdentifier: Optional[String]


class FailoverDBClusterResult(TypedDict, total=False):
    DBCluster: Optional[DBCluster]


class FailoverGlobalClusterMessage(ServiceRequest):
    GlobalClusterIdentifier: GlobalClusterIdentifier
    TargetDbClusterIdentifier: DBClusterIdentifier
    AllowDataLoss: Optional[BooleanOptional]
    Switchover: Optional[BooleanOptional]


class FailoverGlobalClusterResult(TypedDict, total=False):
    GlobalCluster: Optional[GlobalCluster]


GlobalClusterList = List[GlobalCluster]


class GlobalClustersMessage(TypedDict, total=False):
    Marker: Optional[String]
    GlobalClusters: Optional[GlobalClusterList]


KeyList = List[String]


class ListTagsForResourceMessage(ServiceRequest):
    ResourceName: String
    Filters: Optional[FilterList]


class MinimumEngineVersionPerAllowedValue(TypedDict, total=False):
    """The minimum DB engine version required for each corresponding allowed
    value for an option setting.
    """

    AllowedValue: Optional[String]
    MinimumEngineVersion: Optional[String]


MinimumEngineVersionPerAllowedValueList = List[MinimumEngineVersionPerAllowedValue]


class ModifyActivityStreamRequest(ServiceRequest):
    ResourceArn: Optional[String]
    AuditPolicyState: Optional[AuditPolicyState]


class ModifyActivityStreamResponse(TypedDict, total=False):
    KmsKeyId: Optional[String]
    KinesisStreamName: Optional[String]
    Status: Optional[ActivityStreamStatus]
    Mode: Optional[ActivityStreamMode]
    EngineNativeAuditFieldsIncluded: Optional[BooleanOptional]
    PolicyStatus: Optional[ActivityStreamPolicyStatus]


class ModifyCertificatesMessage(ServiceRequest):
    CertificateIdentifier: Optional[String]
    RemoveCustomerOverride: Optional[BooleanOptional]


class ModifyCertificatesResult(TypedDict, total=False):
    Certificate: Optional[Certificate]


class ModifyCurrentDBClusterCapacityMessage(ServiceRequest):
    DBClusterIdentifier: String
    Capacity: Optional[IntegerOptional]
    SecondsBeforeTimeout: Optional[IntegerOptional]
    TimeoutAction: Optional[String]


class ModifyCustomDBEngineVersionMessage(ServiceRequest):
    Engine: CustomEngineName
    EngineVersion: CustomEngineVersion
    Description: Optional[Description]
    Status: Optional[CustomEngineVersionStatus]


class ModifyDBClusterEndpointMessage(ServiceRequest):
    DBClusterEndpointIdentifier: String
    EndpointType: Optional[String]
    StaticMembers: Optional[StringList]
    ExcludedMembers: Optional[StringList]


class ModifyDBClusterMessage(ServiceRequest):
    DBClusterIdentifier: String
    NewDBClusterIdentifier: Optional[String]
    ApplyImmediately: Optional[Boolean]
    BackupRetentionPeriod: Optional[IntegerOptional]
    DBClusterParameterGroupName: Optional[String]
    VpcSecurityGroupIds: Optional[VpcSecurityGroupIdList]
    Port: Optional[IntegerOptional]
    MasterUserPassword: Optional[String]
    OptionGroupName: Optional[String]
    PreferredBackupWindow: Optional[String]
    PreferredMaintenanceWindow: Optional[String]
    EnableIAMDatabaseAuthentication: Optional[BooleanOptional]
    BacktrackWindow: Optional[LongOptional]
    CloudwatchLogsExportConfiguration: Optional[CloudwatchLogsExportConfiguration]
    EngineVersion: Optional[String]
    AllowMajorVersionUpgrade: Optional[Boolean]
    DBInstanceParameterGroupName: Optional[String]
    Domain: Optional[String]
    DomainIAMRoleName: Optional[String]
    ScalingConfiguration: Optional[ScalingConfiguration]
    DeletionProtection: Optional[BooleanOptional]
    EnableHttpEndpoint: Optional[BooleanOptional]
    CopyTagsToSnapshot: Optional[BooleanOptional]
    EnableGlobalWriteForwarding: Optional[BooleanOptional]
    DBClusterInstanceClass: Optional[String]
    AllocatedStorage: Optional[IntegerOptional]
    StorageType: Optional[String]
    Iops: Optional[IntegerOptional]
    AutoMinorVersionUpgrade: Optional[BooleanOptional]
    MonitoringInterval: Optional[IntegerOptional]
    MonitoringRoleArn: Optional[String]
    DatabaseInsightsMode: Optional[DatabaseInsightsMode]
    EnablePerformanceInsights: Optional[BooleanOptional]
    PerformanceInsightsKMSKeyId: Optional[String]
    PerformanceInsightsRetentionPeriod: Optional[IntegerOptional]
    ServerlessV2ScalingConfiguration: Optional[ServerlessV2ScalingConfiguration]
    NetworkType: Optional[String]
    ManageMasterUserPassword: Optional[BooleanOptional]
    RotateMasterUserPassword: Optional[BooleanOptional]
    MasterUserSecretKmsKeyId: Optional[String]
    EngineMode: Optional[String]
    AllowEngineModeChange: Optional[Boolean]
    EnableLocalWriteForwarding: Optional[BooleanOptional]
    AwsBackupRecoveryPointArn: Optional[AwsBackupRecoveryPointArn]
    EnableLimitlessDatabase: Optional[BooleanOptional]
    CACertificateIdentifier: Optional[String]


class ModifyDBClusterParameterGroupMessage(ServiceRequest):
    DBClusterParameterGroupName: String
    Parameters: ParametersList


class ModifyDBClusterResult(TypedDict, total=False):
    DBCluster: Optional[DBCluster]


class ModifyDBClusterSnapshotAttributeMessage(ServiceRequest):
    DBClusterSnapshotIdentifier: String
    AttributeName: String
    ValuesToAdd: Optional[AttributeValueList]
    ValuesToRemove: Optional[AttributeValueList]


class ModifyDBClusterSnapshotAttributeResult(TypedDict, total=False):
    DBClusterSnapshotAttributesResult: Optional[DBClusterSnapshotAttributesResult]


class ModifyDBInstanceMessage(ServiceRequest):
    DBInstanceIdentifier: String
    AllocatedStorage: Optional[IntegerOptional]
    DBInstanceClass: Optional[String]
    DBSubnetGroupName: Optional[String]
    DBSecurityGroups: Optional[DBSecurityGroupNameList]
    VpcSecurityGroupIds: Optional[VpcSecurityGroupIdList]
    ApplyImmediately: Optional[Boolean]
    MasterUserPassword: Optional[String]
    DBParameterGroupName: Optional[String]
    BackupRetentionPeriod: Optional[IntegerOptional]
    PreferredBackupWindow: Optional[String]
    PreferredMaintenanceWindow: Optional[String]
    MultiAZ: Optional[BooleanOptional]
    EngineVersion: Optional[String]
    AllowMajorVersionUpgrade: Optional[Boolean]
    AutoMinorVersionUpgrade: Optional[BooleanOptional]
    LicenseModel: Optional[String]
    Iops: Optional[IntegerOptional]
    OptionGroupName: Optional[String]
    NewDBInstanceIdentifier: Optional[String]
    StorageType: Optional[String]
    TdeCredentialArn: Optional[String]
    TdeCredentialPassword: Optional[String]
    CACertificateIdentifier: Optional[String]
    Domain: Optional[String]
    DomainFqdn: Optional[String]
    DomainOu: Optional[String]
    DomainAuthSecretArn: Optional[String]
    DomainDnsIps: Optional[StringList]
    CopyTagsToSnapshot: Optional[BooleanOptional]
    MonitoringInterval: Optional[IntegerOptional]
    DBPortNumber: Optional[IntegerOptional]
    PubliclyAccessible: Optional[BooleanOptional]
    MonitoringRoleArn: Optional[String]
    DomainIAMRoleName: Optional[String]
    DisableDomain: Optional[BooleanOptional]
    PromotionTier: Optional[IntegerOptional]
    EnableIAMDatabaseAuthentication: Optional[BooleanOptional]
    DatabaseInsightsMode: Optional[DatabaseInsightsMode]
    EnablePerformanceInsights: Optional[BooleanOptional]
    PerformanceInsightsKMSKeyId: Optional[String]
    PerformanceInsightsRetentionPeriod: Optional[IntegerOptional]
    CloudwatchLogsExportConfiguration: Optional[CloudwatchLogsExportConfiguration]
    ProcessorFeatures: Optional[ProcessorFeatureList]
    UseDefaultProcessorFeatures: Optional[BooleanOptional]
    DeletionProtection: Optional[BooleanOptional]
    MaxAllocatedStorage: Optional[IntegerOptional]
    CertificateRotationRestart: Optional[BooleanOptional]
    ReplicaMode: Optional[ReplicaMode]
    EnableCustomerOwnedIp: Optional[BooleanOptional]
    AwsBackupRecoveryPointArn: Optional[AwsBackupRecoveryPointArn]
    AutomationMode: Optional[AutomationMode]
    ResumeFullAutomationModeMinutes: Optional[IntegerOptional]
    NetworkType: Optional[String]
    StorageThroughput: Optional[IntegerOptional]
    ManageMasterUserPassword: Optional[BooleanOptional]
    RotateMasterUserPassword: Optional[BooleanOptional]
    MasterUserSecretKmsKeyId: Optional[String]
    Engine: Optional[String]
    DedicatedLogVolume: Optional[BooleanOptional]
    MultiTenant: Optional[BooleanOptional]


class ModifyDBInstanceResult(TypedDict, total=False):
    DBInstance: Optional[DBInstance]


class ModifyDBParameterGroupMessage(ServiceRequest):
    DBParameterGroupName: String
    Parameters: ParametersList


class ModifyDBProxyEndpointRequest(ServiceRequest):
    DBProxyEndpointName: DBProxyEndpointName
    NewDBProxyEndpointName: Optional[DBProxyEndpointName]
    VpcSecurityGroupIds: Optional[StringList]


class ModifyDBProxyEndpointResponse(TypedDict, total=False):
    DBProxyEndpoint: Optional[DBProxyEndpoint]


class ModifyDBProxyRequest(ServiceRequest):
    DBProxyName: String
    NewDBProxyName: Optional[String]
    Auth: Optional[UserAuthConfigList]
    RequireTLS: Optional[BooleanOptional]
    IdleClientTimeout: Optional[IntegerOptional]
    DebugLogging: Optional[BooleanOptional]
    RoleArn: Optional[String]
    SecurityGroups: Optional[StringList]


class ModifyDBProxyResponse(TypedDict, total=False):
    DBProxy: Optional[DBProxy]


class ModifyDBProxyTargetGroupRequest(ServiceRequest):
    TargetGroupName: String
    DBProxyName: String
    ConnectionPoolConfig: Optional[ConnectionPoolConfiguration]
    NewName: Optional[String]


class ModifyDBProxyTargetGroupResponse(TypedDict, total=False):
    DBProxyTargetGroup: Optional[DBProxyTargetGroup]


class RecommendedActionUpdate(TypedDict, total=False):
    """The recommended status to update for the specified recommendation action
    ID.
    """

    ActionId: String
    Status: String


RecommendedActionUpdateList = List[RecommendedActionUpdate]


class ModifyDBRecommendationMessage(ServiceRequest):
    RecommendationId: String
    Locale: Optional[String]
    Status: Optional[String]
    RecommendedActionUpdates: Optional[RecommendedActionUpdateList]


class ModifyDBShardGroupMessage(ServiceRequest):
    DBShardGroupIdentifier: DBShardGroupIdentifier
    MaxACU: Optional[DoubleOptional]
    MinACU: Optional[DoubleOptional]
    ComputeRedundancy: Optional[IntegerOptional]


class ModifyDBSnapshotAttributeMessage(ServiceRequest):
    DBSnapshotIdentifier: String
    AttributeName: String
    ValuesToAdd: Optional[AttributeValueList]
    ValuesToRemove: Optional[AttributeValueList]


class ModifyDBSnapshotAttributeResult(TypedDict, total=False):
    DBSnapshotAttributesResult: Optional[DBSnapshotAttributesResult]


class ModifyDBSnapshotMessage(ServiceRequest):
    DBSnapshotIdentifier: String
    EngineVersion: Optional[String]
    OptionGroupName: Optional[String]


class ModifyDBSnapshotResult(TypedDict, total=False):
    DBSnapshot: Optional[DBSnapshot]


class ModifyDBSubnetGroupMessage(ServiceRequest):
    DBSubnetGroupName: String
    DBSubnetGroupDescription: Optional[String]
    SubnetIds: SubnetIdentifierList


class ModifyDBSubnetGroupResult(TypedDict, total=False):
    DBSubnetGroup: Optional[DBSubnetGroup]


class ModifyEventSubscriptionMessage(ServiceRequest):
    SubscriptionName: String
    SnsTopicArn: Optional[String]
    SourceType: Optional[String]
    EventCategories: Optional[EventCategoriesList]
    Enabled: Optional[BooleanOptional]


class ModifyEventSubscriptionResult(TypedDict, total=False):
    EventSubscription: Optional[EventSubscription]


class ModifyGlobalClusterMessage(ServiceRequest):
    GlobalClusterIdentifier: Optional[String]
    NewGlobalClusterIdentifier: Optional[String]
    DeletionProtection: Optional[BooleanOptional]
    EngineVersion: Optional[String]
    AllowMajorVersionUpgrade: Optional[BooleanOptional]


class ModifyGlobalClusterResult(TypedDict, total=False):
    GlobalCluster: Optional[GlobalCluster]


class ModifyIntegrationMessage(ServiceRequest):
    IntegrationIdentifier: IntegrationIdentifier
    IntegrationName: Optional[IntegrationName]
    DataFilter: Optional[DataFilter]
    Description: Optional[IntegrationDescription]


OptionNamesList = List[String]
OptionSettingsList = List[OptionSetting]


class OptionConfiguration(TypedDict, total=False):
    """A list of all available options for an option group."""

    OptionName: String
    Port: Optional[IntegerOptional]
    OptionVersion: Optional[String]
    DBSecurityGroupMemberships: Optional[DBSecurityGroupNameList]
    VpcSecurityGroupMemberships: Optional[VpcSecurityGroupIdList]
    OptionSettings: Optional[OptionSettingsList]


OptionConfigurationList = List[OptionConfiguration]


class ModifyOptionGroupMessage(ServiceRequest):
    OptionGroupName: String
    OptionsToInclude: Optional[OptionConfigurationList]
    OptionsToRemove: Optional[OptionNamesList]
    ApplyImmediately: Optional[Boolean]


class ModifyOptionGroupResult(TypedDict, total=False):
    OptionGroup: Optional[OptionGroup]


class ModifyTenantDatabaseMessage(ServiceRequest):
    DBInstanceIdentifier: String
    TenantDBName: String
    MasterUserPassword: Optional[SensitiveString]
    NewTenantDBName: Optional[String]
    ManageMasterUserPassword: Optional[BooleanOptional]
    RotateMasterUserPassword: Optional[BooleanOptional]
    MasterUserSecretKmsKeyId: Optional[String]


class ModifyTenantDatabaseResult(TypedDict, total=False):
    TenantDatabase: Optional[TenantDatabase]


class OptionVersion(TypedDict, total=False):
    """The version for an option. Option group option versions are returned by
    the ``DescribeOptionGroupOptions`` action.
    """

    Version: Optional[String]
    IsDefault: Optional[Boolean]


OptionGroupOptionVersionsList = List[OptionVersion]


class OptionGroupOptionSetting(TypedDict, total=False):
    """Option group option settings are used to display settings available for
    each option with their default values and other information. These
    values are used with the DescribeOptionGroupOptions action.
    """

    SettingName: Optional[String]
    SettingDescription: Optional[String]
    DefaultValue: Optional[String]
    ApplyType: Optional[String]
    AllowedValues: Optional[String]
    IsModifiable: Optional[Boolean]
    IsRequired: Optional[Boolean]
    MinimumEngineVersionPerAllowedValue: Optional[MinimumEngineVersionPerAllowedValueList]


OptionGroupOptionSettingsList = List[OptionGroupOptionSetting]
OptionsConflictsWith = List[String]
OptionsDependedOn = List[String]


class OptionGroupOption(TypedDict, total=False):
    """Available option."""

    Name: Optional[String]
    Description: Optional[String]
    EngineName: Optional[String]
    MajorEngineVersion: Optional[String]
    MinimumRequiredMinorEngineVersion: Optional[String]
    PortRequired: Optional[Boolean]
    DefaultPort: Optional[IntegerOptional]
    OptionsDependedOn: Optional[OptionsDependedOn]
    OptionsConflictsWith: Optional[OptionsConflictsWith]
    Persistent: Optional[Boolean]
    Permanent: Optional[Boolean]
    RequiresAutoMinorEngineVersionUpgrade: Optional[Boolean]
    VpcOnly: Optional[Boolean]
    SupportsOptionVersionDowngrade: Optional[BooleanOptional]
    OptionGroupOptionSettings: Optional[OptionGroupOptionSettingsList]
    OptionGroupOptionVersions: Optional[OptionGroupOptionVersionsList]
    CopyableCrossAccount: Optional[BooleanOptional]


OptionGroupOptionsList = List[OptionGroupOption]


class OptionGroupOptionsMessage(TypedDict, total=False):
    OptionGroupOptions: Optional[OptionGroupOptionsList]
    Marker: Optional[String]


OptionGroupsList = List[OptionGroup]


class OptionGroups(TypedDict, total=False):
    """List of option groups."""

    OptionGroupsList: Optional[OptionGroupsList]
    Marker: Optional[String]


class OrderableDBInstanceOption(TypedDict, total=False):
    """Contains a list of available options for a DB instance.

    This data type is used as a response element in the
    ``DescribeOrderableDBInstanceOptions`` action.
    """

    Engine: Optional[String]
    EngineVersion: Optional[String]
    DBInstanceClass: Optional[String]
    LicenseModel: Optional[String]
    AvailabilityZoneGroup: Optional[String]
    AvailabilityZones: Optional[AvailabilityZoneList]
    MultiAZCapable: Optional[Boolean]
    ReadReplicaCapable: Optional[Boolean]
    Vpc: Optional[Boolean]
    SupportsStorageEncryption: Optional[Boolean]
    StorageType: Optional[String]
    SupportsIops: Optional[Boolean]
    SupportsEnhancedMonitoring: Optional[Boolean]
    SupportsIAMDatabaseAuthentication: Optional[Boolean]
    SupportsPerformanceInsights: Optional[Boolean]
    MinStorageSize: Optional[IntegerOptional]
    MaxStorageSize: Optional[IntegerOptional]
    MinIopsPerDbInstance: Optional[IntegerOptional]
    MaxIopsPerDbInstance: Optional[IntegerOptional]
    MinIopsPerGib: Optional[DoubleOptional]
    MaxIopsPerGib: Optional[DoubleOptional]
    AvailableProcessorFeatures: Optional[AvailableProcessorFeatureList]
    SupportedEngineModes: Optional[EngineModeList]
    SupportsStorageAutoscaling: Optional[BooleanOptional]
    SupportsKerberosAuthentication: Optional[BooleanOptional]
    OutpostCapable: Optional[Boolean]
    SupportedActivityStreamModes: Optional[ActivityStreamModeList]
    SupportsGlobalDatabases: Optional[Boolean]
    SupportsClusters: Optional[Boolean]
    SupportedNetworkTypes: Optional[StringList]
    SupportsStorageThroughput: Optional[Boolean]
    MinStorageThroughputPerDbInstance: Optional[IntegerOptional]
    MaxStorageThroughputPerDbInstance: Optional[IntegerOptional]
    MinStorageThroughputPerIops: Optional[DoubleOptional]
    MaxStorageThroughputPerIops: Optional[DoubleOptional]
    SupportsDedicatedLogVolume: Optional[Boolean]


OrderableDBInstanceOptionsList = List[OrderableDBInstanceOption]


class OrderableDBInstanceOptionsMessage(TypedDict, total=False):
    """Contains the result of a successful invocation of the
    ``DescribeOrderableDBInstanceOptions`` action.
    """

    OrderableDBInstanceOptions: Optional[OrderableDBInstanceOptionsList]
    Marker: Optional[String]


PendingMaintenanceActions = List[ResourcePendingMaintenanceActions]


class PendingMaintenanceActionsMessage(TypedDict, total=False):
    """Data returned from the **DescribePendingMaintenanceActions** action."""

    PendingMaintenanceActions: Optional[PendingMaintenanceActions]
    Marker: Optional[String]


class PromoteReadReplicaDBClusterMessage(ServiceRequest):
    DBClusterIdentifier: String


class PromoteReadReplicaDBClusterResult(TypedDict, total=False):
    DBCluster: Optional[DBCluster]


class PromoteReadReplicaMessage(ServiceRequest):
    DBInstanceIdentifier: String
    BackupRetentionPeriod: Optional[IntegerOptional]
    PreferredBackupWindow: Optional[String]


class PromoteReadReplicaResult(TypedDict, total=False):
    DBInstance: Optional[DBInstance]


class PurchaseReservedDBInstancesOfferingMessage(ServiceRequest):
    ReservedDBInstancesOfferingId: String
    ReservedDBInstanceId: Optional[String]
    DBInstanceCount: Optional[IntegerOptional]
    Tags: Optional[TagList]


class RecurringCharge(TypedDict, total=False):
    """This data type is used as a response element in the
    ``DescribeReservedDBInstances`` and
    ``DescribeReservedDBInstancesOfferings`` actions.
    """

    RecurringChargeAmount: Optional[Double]
    RecurringChargeFrequency: Optional[String]


RecurringChargeList = List[RecurringCharge]


class ReservedDBInstance(TypedDict, total=False):
    """This data type is used as a response element in the
    ``DescribeReservedDBInstances`` and
    ``PurchaseReservedDBInstancesOffering`` actions.
    """

    ReservedDBInstanceId: Optional[String]
    ReservedDBInstancesOfferingId: Optional[String]
    DBInstanceClass: Optional[String]
    StartTime: Optional[TStamp]
    Duration: Optional[Integer]
    FixedPrice: Optional[Double]
    UsagePrice: Optional[Double]
    CurrencyCode: Optional[String]
    DBInstanceCount: Optional[Integer]
    ProductDescription: Optional[String]
    OfferingType: Optional[String]
    MultiAZ: Optional[Boolean]
    State: Optional[String]
    RecurringCharges: Optional[RecurringChargeList]
    ReservedDBInstanceArn: Optional[String]
    LeaseId: Optional[String]


class PurchaseReservedDBInstancesOfferingResult(TypedDict, total=False):
    ReservedDBInstance: Optional[ReservedDBInstance]


class RebootDBClusterMessage(ServiceRequest):
    DBClusterIdentifier: String


class RebootDBClusterResult(TypedDict, total=False):
    DBCluster: Optional[DBCluster]


class RebootDBInstanceMessage(ServiceRequest):
    DBInstanceIdentifier: String
    ForceFailover: Optional[BooleanOptional]


class RebootDBInstanceResult(TypedDict, total=False):
    DBInstance: Optional[DBInstance]


class RebootDBShardGroupMessage(ServiceRequest):
    DBShardGroupIdentifier: DBShardGroupIdentifier


class RegisterDBProxyTargetsRequest(ServiceRequest):
    DBProxyName: String
    TargetGroupName: Optional[String]
    DBInstanceIdentifiers: Optional[StringList]
    DBClusterIdentifiers: Optional[StringList]


class RegisterDBProxyTargetsResponse(TypedDict, total=False):
    DBProxyTargets: Optional[TargetList]


class RemoveFromGlobalClusterMessage(ServiceRequest):
    GlobalClusterIdentifier: Optional[String]
    DbClusterIdentifier: Optional[String]


class RemoveFromGlobalClusterResult(TypedDict, total=False):
    GlobalCluster: Optional[GlobalCluster]


class RemoveRoleFromDBClusterMessage(ServiceRequest):
    DBClusterIdentifier: String
    RoleArn: String
    FeatureName: Optional[String]


class RemoveRoleFromDBInstanceMessage(ServiceRequest):
    DBInstanceIdentifier: String
    RoleArn: String
    FeatureName: String


class RemoveSourceIdentifierFromSubscriptionMessage(ServiceRequest):
    SubscriptionName: String
    SourceIdentifier: String


class RemoveSourceIdentifierFromSubscriptionResult(TypedDict, total=False):
    EventSubscription: Optional[EventSubscription]


class RemoveTagsFromResourceMessage(ServiceRequest):
    ResourceName: String
    TagKeys: KeyList


ReservedDBInstanceList = List[ReservedDBInstance]


class ReservedDBInstanceMessage(TypedDict, total=False):
    """Contains the result of a successful invocation of the
    ``DescribeReservedDBInstances`` action.
    """

    Marker: Optional[String]
    ReservedDBInstances: Optional[ReservedDBInstanceList]


class ReservedDBInstancesOffering(TypedDict, total=False):
    """This data type is used as a response element in the
    ``DescribeReservedDBInstancesOfferings`` action.
    """

    ReservedDBInstancesOfferingId: Optional[String]
    DBInstanceClass: Optional[String]
    Duration: Optional[Integer]
    FixedPrice: Optional[Double]
    UsagePrice: Optional[Double]
    CurrencyCode: Optional[String]
    ProductDescription: Optional[String]
    OfferingType: Optional[String]
    MultiAZ: Optional[Boolean]
    RecurringCharges: Optional[RecurringChargeList]


ReservedDBInstancesOfferingList = List[ReservedDBInstancesOffering]


class ReservedDBInstancesOfferingMessage(TypedDict, total=False):
    """Contains the result of a successful invocation of the
    ``DescribeReservedDBInstancesOfferings`` action.
    """

    Marker: Optional[String]
    ReservedDBInstancesOfferings: Optional[ReservedDBInstancesOfferingList]


class ResetDBClusterParameterGroupMessage(ServiceRequest):
    DBClusterParameterGroupName: String
    ResetAllParameters: Optional[Boolean]
    Parameters: Optional[ParametersList]


class ResetDBParameterGroupMessage(ServiceRequest):
    DBParameterGroupName: String
    ResetAllParameters: Optional[Boolean]
    Parameters: Optional[ParametersList]


class RestoreDBClusterFromS3Message(ServiceRequest):
    AvailabilityZones: Optional[AvailabilityZones]
    BackupRetentionPeriod: Optional[IntegerOptional]
    CharacterSetName: Optional[String]
    DatabaseName: Optional[String]
    DBClusterIdentifier: String
    DBClusterParameterGroupName: Optional[String]
    VpcSecurityGroupIds: Optional[VpcSecurityGroupIdList]
    DBSubnetGroupName: Optional[String]
    Engine: String
    EngineVersion: Optional[String]
    Port: Optional[IntegerOptional]
    MasterUsername: String
    MasterUserPassword: Optional[String]
    OptionGroupName: Optional[String]
    PreferredBackupWindow: Optional[String]
    PreferredMaintenanceWindow: Optional[String]
    Tags: Optional[TagList]
    StorageEncrypted: Optional[BooleanOptional]
    KmsKeyId: Optional[String]
    EnableIAMDatabaseAuthentication: Optional[BooleanOptional]
    SourceEngine: String
    SourceEngineVersion: String
    S3BucketName: String
    S3Prefix: Optional[String]
    S3IngestionRoleArn: String
    BacktrackWindow: Optional[LongOptional]
    EnableCloudwatchLogsExports: Optional[LogTypeList]
    DeletionProtection: Optional[BooleanOptional]
    CopyTagsToSnapshot: Optional[BooleanOptional]
    Domain: Optional[String]
    DomainIAMRoleName: Optional[String]
    ServerlessV2ScalingConfiguration: Optional[ServerlessV2ScalingConfiguration]
    NetworkType: Optional[String]
    ManageMasterUserPassword: Optional[BooleanOptional]
    MasterUserSecretKmsKeyId: Optional[String]
    StorageType: Optional[String]
    EngineLifecycleSupport: Optional[String]


class RestoreDBClusterFromS3Result(TypedDict, total=False):
    DBCluster: Optional[DBCluster]


class RestoreDBClusterFromSnapshotMessage(ServiceRequest):
    AvailabilityZones: Optional[AvailabilityZones]
    DBClusterIdentifier: String
    SnapshotIdentifier: String
    Engine: String
    EngineVersion: Optional[String]
    Port: Optional[IntegerOptional]
    DBSubnetGroupName: Optional[String]
    DatabaseName: Optional[String]
    OptionGroupName: Optional[String]
    VpcSecurityGroupIds: Optional[VpcSecurityGroupIdList]
    Tags: Optional[TagList]
    KmsKeyId: Optional[String]
    EnableIAMDatabaseAuthentication: Optional[BooleanOptional]
    BacktrackWindow: Optional[LongOptional]
    EnableCloudwatchLogsExports: Optional[LogTypeList]
    EngineMode: Optional[String]
    ScalingConfiguration: Optional[ScalingConfiguration]
    DBClusterParameterGroupName: Optional[String]
    DeletionProtection: Optional[BooleanOptional]
    CopyTagsToSnapshot: Optional[BooleanOptional]
    Domain: Optional[String]
    DomainIAMRoleName: Optional[String]
    DBClusterInstanceClass: Optional[String]
    StorageType: Optional[String]
    Iops: Optional[IntegerOptional]
    PubliclyAccessible: Optional[BooleanOptional]
    ServerlessV2ScalingConfiguration: Optional[ServerlessV2ScalingConfiguration]
    NetworkType: Optional[String]
    RdsCustomClusterConfiguration: Optional[RdsCustomClusterConfiguration]
    MonitoringInterval: Optional[IntegerOptional]
    MonitoringRoleArn: Optional[String]
    EnablePerformanceInsights: Optional[BooleanOptional]
    PerformanceInsightsKMSKeyId: Optional[String]
    PerformanceInsightsRetentionPeriod: Optional[IntegerOptional]
    EngineLifecycleSupport: Optional[String]


class RestoreDBClusterFromSnapshotResult(TypedDict, total=False):
    DBCluster: Optional[DBCluster]


class RestoreDBClusterToPointInTimeMessage(ServiceRequest):
    DBClusterIdentifier: String
    RestoreType: Optional[String]
    SourceDBClusterIdentifier: Optional[String]
    RestoreToTime: Optional[TStamp]
    UseLatestRestorableTime: Optional[Boolean]
    Port: Optional[IntegerOptional]
    DBSubnetGroupName: Optional[String]
    OptionGroupName: Optional[String]
    VpcSecurityGroupIds: Optional[VpcSecurityGroupIdList]
    Tags: Optional[TagList]
    KmsKeyId: Optional[String]
    EnableIAMDatabaseAuthentication: Optional[BooleanOptional]
    BacktrackWindow: Optional[LongOptional]
    EnableCloudwatchLogsExports: Optional[LogTypeList]
    DBClusterParameterGroupName: Optional[String]
    DeletionProtection: Optional[BooleanOptional]
    CopyTagsToSnapshot: Optional[BooleanOptional]
    Domain: Optional[String]
    DomainIAMRoleName: Optional[String]
    ScalingConfiguration: Optional[ScalingConfiguration]
    EngineMode: Optional[String]
    DBClusterInstanceClass: Optional[String]
    StorageType: Optional[String]
    PubliclyAccessible: Optional[BooleanOptional]
    Iops: Optional[IntegerOptional]
    ServerlessV2ScalingConfiguration: Optional[ServerlessV2ScalingConfiguration]
    NetworkType: Optional[String]
    SourceDbClusterResourceId: Optional[String]
    RdsCustomClusterConfiguration: Optional[RdsCustomClusterConfiguration]
    MonitoringInterval: Optional[IntegerOptional]
    MonitoringRoleArn: Optional[String]
    EnablePerformanceInsights: Optional[BooleanOptional]
    PerformanceInsightsKMSKeyId: Optional[String]
    PerformanceInsightsRetentionPeriod: Optional[IntegerOptional]
    EngineLifecycleSupport: Optional[String]


class RestoreDBClusterToPointInTimeResult(TypedDict, total=False):
    DBCluster: Optional[DBCluster]


class RestoreDBInstanceFromDBSnapshotMessage(ServiceRequest):
    DBInstanceIdentifier: String
    DBSnapshotIdentifier: Optional[String]
    DBInstanceClass: Optional[String]
    Port: Optional[IntegerOptional]
    AvailabilityZone: Optional[String]
    DBSubnetGroupName: Optional[String]
    MultiAZ: Optional[BooleanOptional]
    PubliclyAccessible: Optional[BooleanOptional]
    AutoMinorVersionUpgrade: Optional[BooleanOptional]
    LicenseModel: Optional[String]
    DBName: Optional[String]
    Engine: Optional[String]
    Iops: Optional[IntegerOptional]
    OptionGroupName: Optional[String]
    Tags: Optional[TagList]
    StorageType: Optional[String]
    TdeCredentialArn: Optional[String]
    TdeCredentialPassword: Optional[String]
    VpcSecurityGroupIds: Optional[VpcSecurityGroupIdList]
    Domain: Optional[String]
    DomainFqdn: Optional[String]
    DomainOu: Optional[String]
    DomainAuthSecretArn: Optional[String]
    DomainDnsIps: Optional[StringList]
    CopyTagsToSnapshot: Optional[BooleanOptional]
    DomainIAMRoleName: Optional[String]
    EnableIAMDatabaseAuthentication: Optional[BooleanOptional]
    EnableCloudwatchLogsExports: Optional[LogTypeList]
    ProcessorFeatures: Optional[ProcessorFeatureList]
    UseDefaultProcessorFeatures: Optional[BooleanOptional]
    DBParameterGroupName: Optional[String]
    DeletionProtection: Optional[BooleanOptional]
    EnableCustomerOwnedIp: Optional[BooleanOptional]
    CustomIamInstanceProfile: Optional[String]
    BackupTarget: Optional[String]
    NetworkType: Optional[String]
    StorageThroughput: Optional[IntegerOptional]
    DBClusterSnapshotIdentifier: Optional[String]
    AllocatedStorage: Optional[IntegerOptional]
    DedicatedLogVolume: Optional[BooleanOptional]
    CACertificateIdentifier: Optional[String]
    EngineLifecycleSupport: Optional[String]
    ManageMasterUserPassword: Optional[BooleanOptional]
    MasterUserSecretKmsKeyId: Optional[String]


class RestoreDBInstanceFromDBSnapshotResult(TypedDict, total=False):
    DBInstance: Optional[DBInstance]


class RestoreDBInstanceFromS3Message(ServiceRequest):
    DBName: Optional[String]
    DBInstanceIdentifier: String
    AllocatedStorage: Optional[IntegerOptional]
    DBInstanceClass: String
    Engine: String
    MasterUsername: Optional[String]
    MasterUserPassword: Optional[String]
    DBSecurityGroups: Optional[DBSecurityGroupNameList]
    VpcSecurityGroupIds: Optional[VpcSecurityGroupIdList]
    AvailabilityZone: Optional[String]
    DBSubnetGroupName: Optional[String]
    PreferredMaintenanceWindow: Optional[String]
    DBParameterGroupName: Optional[String]
    BackupRetentionPeriod: Optional[IntegerOptional]
    PreferredBackupWindow: Optional[String]
    Port: Optional[IntegerOptional]
    MultiAZ: Optional[BooleanOptional]
    EngineVersion: Optional[String]
    AutoMinorVersionUpgrade: Optional[BooleanOptional]
    LicenseModel: Optional[String]
    Iops: Optional[IntegerOptional]
    OptionGroupName: Optional[String]
    PubliclyAccessible: Optional[BooleanOptional]
    Tags: Optional[TagList]
    StorageType: Optional[String]
    StorageEncrypted: Optional[BooleanOptional]
    KmsKeyId: Optional[String]
    CopyTagsToSnapshot: Optional[BooleanOptional]
    MonitoringInterval: Optional[IntegerOptional]
    MonitoringRoleArn: Optional[String]
    EnableIAMDatabaseAuthentication: Optional[BooleanOptional]
    SourceEngine: String
    SourceEngineVersion: String
    S3BucketName: String
    S3Prefix: Optional[String]
    S3IngestionRoleArn: String
    DatabaseInsightsMode: Optional[DatabaseInsightsMode]
    EnablePerformanceInsights: Optional[BooleanOptional]
    PerformanceInsightsKMSKeyId: Optional[String]
    PerformanceInsightsRetentionPeriod: Optional[IntegerOptional]
    EnableCloudwatchLogsExports: Optional[LogTypeList]
    ProcessorFeatures: Optional[ProcessorFeatureList]
    UseDefaultProcessorFeatures: Optional[BooleanOptional]
    DeletionProtection: Optional[BooleanOptional]
    MaxAllocatedStorage: Optional[IntegerOptional]
    NetworkType: Optional[String]
    StorageThroughput: Optional[IntegerOptional]
    ManageMasterUserPassword: Optional[BooleanOptional]
    MasterUserSecretKmsKeyId: Optional[String]
    DedicatedLogVolume: Optional[BooleanOptional]
    CACertificateIdentifier: Optional[String]
    EngineLifecycleSupport: Optional[String]


class RestoreDBInstanceFromS3Result(TypedDict, total=False):
    DBInstance: Optional[DBInstance]


class RestoreDBInstanceToPointInTimeMessage(ServiceRequest):
    SourceDBInstanceIdentifier: Optional[String]
    TargetDBInstanceIdentifier: String
    RestoreTime: Optional[TStamp]
    UseLatestRestorableTime: Optional[Boolean]
    DBInstanceClass: Optional[String]
    Port: Optional[IntegerOptional]
    AvailabilityZone: Optional[String]
    DBSubnetGroupName: Optional[String]
    MultiAZ: Optional[BooleanOptional]
    PubliclyAccessible: Optional[BooleanOptional]
    AutoMinorVersionUpgrade: Optional[BooleanOptional]
    LicenseModel: Optional[String]
    DBName: Optional[String]
    Engine: Optional[String]
    Iops: Optional[IntegerOptional]
    OptionGroupName: Optional[String]
    CopyTagsToSnapshot: Optional[BooleanOptional]
    Tags: Optional[TagList]
    StorageType: Optional[String]
    TdeCredentialArn: Optional[String]
    TdeCredentialPassword: Optional[String]
    VpcSecurityGroupIds: Optional[VpcSecurityGroupIdList]
    Domain: Optional[String]
    DomainIAMRoleName: Optional[String]
    DomainFqdn: Optional[String]
    DomainOu: Optional[String]
    DomainAuthSecretArn: Optional[String]
    DomainDnsIps: Optional[StringList]
    EnableIAMDatabaseAuthentication: Optional[BooleanOptional]
    EnableCloudwatchLogsExports: Optional[LogTypeList]
    ProcessorFeatures: Optional[ProcessorFeatureList]
    UseDefaultProcessorFeatures: Optional[BooleanOptional]
    DBParameterGroupName: Optional[String]
    DeletionProtection: Optional[BooleanOptional]
    SourceDbiResourceId: Optional[String]
    MaxAllocatedStorage: Optional[IntegerOptional]
    SourceDBInstanceAutomatedBackupsArn: Optional[String]
    EnableCustomerOwnedIp: Optional[BooleanOptional]
    CustomIamInstanceProfile: Optional[String]
    BackupTarget: Optional[String]
    NetworkType: Optional[String]
    StorageThroughput: Optional[IntegerOptional]
    AllocatedStorage: Optional[IntegerOptional]
    DedicatedLogVolume: Optional[BooleanOptional]
    CACertificateIdentifier: Optional[String]
    EngineLifecycleSupport: Optional[String]
    ManageMasterUserPassword: Optional[BooleanOptional]
    MasterUserSecretKmsKeyId: Optional[String]


class RestoreDBInstanceToPointInTimeResult(TypedDict, total=False):
    DBInstance: Optional[DBInstance]


class RevokeDBSecurityGroupIngressMessage(ServiceRequest):
    DBSecurityGroupName: String
    CIDRIP: Optional[String]
    EC2SecurityGroupName: Optional[String]
    EC2SecurityGroupId: Optional[String]
    EC2SecurityGroupOwnerId: Optional[String]


class RevokeDBSecurityGroupIngressResult(TypedDict, total=False):
    DBSecurityGroup: Optional[DBSecurityGroup]


class SourceRegion(TypedDict, total=False):
    """Contains an Amazon Web Services Region name as the result of a
    successful call to the ``DescribeSourceRegions`` action.
    """

    RegionName: Optional[String]
    Endpoint: Optional[String]
    Status: Optional[String]
    SupportsDBInstanceAutomatedBackupsReplication: Optional[Boolean]


SourceRegionList = List[SourceRegion]


class SourceRegionMessage(TypedDict, total=False):
    """Contains the result of a successful invocation of the
    ``DescribeSourceRegions`` action.
    """

    Marker: Optional[String]
    SourceRegions: Optional[SourceRegionList]


class StartActivityStreamRequest(ServiceRequest):
    ResourceArn: String
    Mode: ActivityStreamMode
    KmsKeyId: String
    ApplyImmediately: Optional[BooleanOptional]
    EngineNativeAuditFieldsIncluded: Optional[BooleanOptional]


class StartActivityStreamResponse(TypedDict, total=False):
    KmsKeyId: Optional[String]
    KinesisStreamName: Optional[String]
    Status: Optional[ActivityStreamStatus]
    Mode: Optional[ActivityStreamMode]
    ApplyImmediately: Optional[Boolean]
    EngineNativeAuditFieldsIncluded: Optional[BooleanOptional]


class StartDBClusterMessage(ServiceRequest):
    DBClusterIdentifier: String


class StartDBClusterResult(TypedDict, total=False):
    DBCluster: Optional[DBCluster]


class StartDBInstanceAutomatedBackupsReplicationMessage(ServiceRequest):
    SourceDBInstanceArn: String
    BackupRetentionPeriod: Optional[IntegerOptional]
    KmsKeyId: Optional[String]
    PreSignedUrl: Optional[String]
    SourceRegion: Optional[String]


class StartDBInstanceAutomatedBackupsReplicationResult(TypedDict, total=False):
    DBInstanceAutomatedBackup: Optional[DBInstanceAutomatedBackup]


class StartDBInstanceMessage(ServiceRequest):
    DBInstanceIdentifier: String


class StartDBInstanceResult(TypedDict, total=False):
    DBInstance: Optional[DBInstance]


class StartExportTaskMessage(ServiceRequest):
    ExportTaskIdentifier: String
    SourceArn: String
    S3BucketName: String
    IamRoleArn: String
    KmsKeyId: String
    S3Prefix: Optional[String]
    ExportOnly: Optional[StringList]


class StopActivityStreamRequest(ServiceRequest):
    ResourceArn: String
    ApplyImmediately: Optional[BooleanOptional]


class StopActivityStreamResponse(TypedDict, total=False):
    KmsKeyId: Optional[String]
    KinesisStreamName: Optional[String]
    Status: Optional[ActivityStreamStatus]


class StopDBClusterMessage(ServiceRequest):
    DBClusterIdentifier: String


class StopDBClusterResult(TypedDict, total=False):
    DBCluster: Optional[DBCluster]


class StopDBInstanceAutomatedBackupsReplicationMessage(ServiceRequest):
    SourceDBInstanceArn: String


class StopDBInstanceAutomatedBackupsReplicationResult(TypedDict, total=False):
    DBInstanceAutomatedBackup: Optional[DBInstanceAutomatedBackup]


class StopDBInstanceMessage(ServiceRequest):
    DBInstanceIdentifier: String
    DBSnapshotIdentifier: Optional[String]


class StopDBInstanceResult(TypedDict, total=False):
    DBInstance: Optional[DBInstance]


class SwitchoverBlueGreenDeploymentRequest(ServiceRequest):
    BlueGreenDeploymentIdentifier: BlueGreenDeploymentIdentifier
    SwitchoverTimeout: Optional[SwitchoverTimeout]


class SwitchoverBlueGreenDeploymentResponse(TypedDict, total=False):
    BlueGreenDeployment: Optional[BlueGreenDeployment]


class SwitchoverGlobalClusterMessage(ServiceRequest):
    GlobalClusterIdentifier: GlobalClusterIdentifier
    TargetDbClusterIdentifier: DBClusterIdentifier


class SwitchoverGlobalClusterResult(TypedDict, total=False):
    GlobalCluster: Optional[GlobalCluster]


class SwitchoverReadReplicaMessage(ServiceRequest):
    DBInstanceIdentifier: String


class SwitchoverReadReplicaResult(TypedDict, total=False):
    DBInstance: Optional[DBInstance]


class TagListMessage(TypedDict, total=False):
    TagList: Optional[TagList]


TenantDatabasesList = List[TenantDatabase]


class TenantDatabasesMessage(TypedDict, total=False):
    Marker: Optional[String]
    TenantDatabases: Optional[TenantDatabasesList]


class RdsApi:
    service = "rds"
    version = "2014-10-31"

    @handler("AddRoleToDBCluster")
    def add_role_to_db_cluster(
        self,
        context: RequestContext,
        db_cluster_identifier: String,
        role_arn: String,
        feature_name: String | None = None,
        **kwargs,
    ) -> None:
        """Associates an Identity and Access Management (IAM) role with a DB
        cluster.

        :param db_cluster_identifier: The name of the DB cluster to associate the IAM role with.
        :param role_arn: The Amazon Resource Name (ARN) of the IAM role to associate with the
        Aurora DB cluster, for example
        ``arn:aws:iam::123456789012:role/AuroraAccessRole``.
        :param feature_name: The name of the feature for the DB cluster that the IAM role is to be
        associated with.
        :raises DBClusterNotFoundFault:
        :raises DBClusterRoleAlreadyExistsFault:
        :raises InvalidDBClusterStateFault:
        :raises DBClusterRoleQuotaExceededFault:
        """
        raise NotImplementedError

    @handler("AddRoleToDBInstance")
    def add_role_to_db_instance(
        self,
        context: RequestContext,
        db_instance_identifier: String,
        role_arn: String,
        feature_name: String,
        **kwargs,
    ) -> None:
        """Associates an Amazon Web Services Identity and Access Management (IAM)
        role with a DB instance.

        To add a role to a DB instance, the status of the DB instance must be
        ``available``.

        This command doesn't apply to RDS Custom.

        :param db_instance_identifier: The name of the DB instance to associate the IAM role with.
        :param role_arn: The Amazon Resource Name (ARN) of the IAM role to associate with the DB
        instance, for example ``arn:aws:iam::123456789012:role/AccessRole``.
        :param feature_name: The name of the feature for the DB instance that the IAM role is to be
        associated with.
        :raises DBInstanceNotFoundFault:
        :raises DBInstanceRoleAlreadyExistsFault:
        :raises InvalidDBInstanceStateFault:
        :raises DBInstanceRoleQuotaExceededFault:
        """
        raise NotImplementedError

    @handler("AddSourceIdentifierToSubscription")
    def add_source_identifier_to_subscription(
        self,
        context: RequestContext,
        subscription_name: String,
        source_identifier: String,
        **kwargs,
    ) -> AddSourceIdentifierToSubscriptionResult:
        """Adds a source identifier to an existing RDS event notification
        subscription.

        :param subscription_name: The name of the RDS event notification subscription you want to add a
        source identifier to.
        :param source_identifier: The identifier of the event source to be added.
        :returns: AddSourceIdentifierToSubscriptionResult
        :raises SubscriptionNotFoundFault:
        :raises SourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("AddTagsToResource")
    def add_tags_to_resource(
        self, context: RequestContext, resource_name: String, tags: TagList, **kwargs
    ) -> None:
        """Adds metadata tags to an Amazon RDS resource. These tags can also be
        used with cost allocation reporting to track cost associated with Amazon
        RDS resources, or used in a Condition statement in an IAM policy for
        Amazon RDS.

        For an overview on tagging your relational database resources, see
        `Tagging Amazon RDS
        Resources <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html>`__
        or `Tagging Amazon Aurora and Amazon RDS
        Resources <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html>`__.

        :param resource_name: The Amazon RDS resource that the tags are added to.
        :param tags: The tags to be assigned to the Amazon RDS resource.
        :raises DBInstanceNotFoundFault:
        :raises DBClusterNotFoundFault:
        :raises DBSnapshotNotFoundFault:
        :raises DBProxyNotFoundFault:
        :raises DBProxyTargetGroupNotFoundFault:
        :raises BlueGreenDeploymentNotFoundFault:
        :raises IntegrationNotFoundFault:
        :raises TenantDatabaseNotFoundFault:
        :raises DBSnapshotTenantDatabaseNotFoundFault:
        """
        raise NotImplementedError

    @handler("ApplyPendingMaintenanceAction")
    def apply_pending_maintenance_action(
        self,
        context: RequestContext,
        resource_identifier: String,
        apply_action: String,
        opt_in_type: String,
        **kwargs,
    ) -> ApplyPendingMaintenanceActionResult:
        """Applies a pending maintenance action to a resource (for example, to a DB
        instance).

        :param resource_identifier: The RDS Amazon Resource Name (ARN) of the resource that the pending
        maintenance action applies to.
        :param apply_action: The pending maintenance action to apply to this resource.
        :param opt_in_type: A value that specifies the type of opt-in request, or undoes an opt-in
        request.
        :returns: ApplyPendingMaintenanceActionResult
        :raises ResourceNotFoundFault:
        :raises InvalidDBClusterStateFault:
        :raises InvalidDBInstanceStateFault:
        """
        raise NotImplementedError

    @handler("AuthorizeDBSecurityGroupIngress")
    def authorize_db_security_group_ingress(
        self,
        context: RequestContext,
        db_security_group_name: String,
        cidrip: String | None = None,
        ec2_security_group_name: String | None = None,
        ec2_security_group_id: String | None = None,
        ec2_security_group_owner_id: String | None = None,
        **kwargs,
    ) -> AuthorizeDBSecurityGroupIngressResult:
        """Enables ingress to a DBSecurityGroup using one of two forms of
        authorization. First, EC2 or VPC security groups can be added to the
        DBSecurityGroup if the application using the database is running on EC2
        or VPC instances. Second, IP ranges are available if the application
        accessing your database is running on the internet. Required parameters
        for this API are one of CIDR range, EC2SecurityGroupId for VPC, or
        (EC2SecurityGroupOwnerId and either EC2SecurityGroupName or
        EC2SecurityGroupId for non-VPC).

        You can't authorize ingress from an EC2 security group in one Amazon Web
        Services Region to an Amazon RDS DB instance in another. You can't
        authorize ingress from a VPC security group in one VPC to an Amazon RDS
        DB instance in another.

        For an overview of CIDR ranges, go to the `Wikipedia
        Tutorial <http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`__.

        EC2-Classic was retired on August 15, 2022. If you haven't migrated from
        EC2-Classic to a VPC, we recommend that you migrate as soon as possible.
        For more information, see `Migrate from EC2-Classic to a
        VPC <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-migrate.html>`__
        in the *Amazon EC2 User Guide*, the blog `EC2-Classic Networking is
        Retiring – Here’s How to
        Prepare <http://aws.amazon.com/blogs/aws/ec2-classic-is-retiring-heres-how-to-prepare/>`__,
        and `Moving a DB instance not in a VPC into a
        VPC <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Non-VPC2VPC.html>`__
        in the *Amazon RDS User Guide*.

        :param db_security_group_name: The name of the DB security group to add authorization to.
        :param cidrip: The IP range to authorize.
        :param ec2_security_group_name: Name of the EC2 security group to authorize.
        :param ec2_security_group_id: Id of the EC2 security group to authorize.
        :param ec2_security_group_owner_id: Amazon Web Services account number of the owner of the EC2 security
        group specified in the ``EC2SecurityGroupName`` parameter.
        :returns: AuthorizeDBSecurityGroupIngressResult
        :raises DBSecurityGroupNotFoundFault:
        :raises InvalidDBSecurityGroupStateFault:
        :raises AuthorizationAlreadyExistsFault:
        :raises AuthorizationQuotaExceededFault:
        """
        raise NotImplementedError

    @handler("BacktrackDBCluster")
    def backtrack_db_cluster(
        self,
        context: RequestContext,
        db_cluster_identifier: String,
        backtrack_to: TStamp,
        force: BooleanOptional | None = None,
        use_earliest_time_on_point_in_time_unavailable: BooleanOptional | None = None,
        **kwargs,
    ) -> DBClusterBacktrack:
        """Backtracks a DB cluster to a specific time, without creating a new DB
        cluster.

        For more information on backtracking, see `Backtracking an Aurora DB
        Cluster <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Backtrack.html>`__
        in the *Amazon Aurora User Guide*.

        This action applies only to Aurora MySQL DB clusters.

        :param db_cluster_identifier: The DB cluster identifier of the DB cluster to be backtracked.
        :param backtrack_to: The timestamp of the time to backtrack the DB cluster to, specified in
        ISO 8601 format.
        :param force: Specifies whether to force the DB cluster to backtrack when binary
        logging is enabled.
        :param use_earliest_time_on_point_in_time_unavailable: Specifies whether to backtrack the DB cluster to the earliest possible
        backtrack time when *BacktrackTo* is set to a timestamp earlier than the
        earliest backtrack time.
        :returns: DBClusterBacktrack
        :raises DBClusterNotFoundFault:
        :raises InvalidDBClusterStateFault:
        """
        raise NotImplementedError

    @handler("CancelExportTask")
    def cancel_export_task(
        self, context: RequestContext, export_task_identifier: String, **kwargs
    ) -> ExportTask:
        """Cancels an export task in progress that is exporting a snapshot or
        cluster to Amazon S3. Any data that has already been written to the S3
        bucket isn't removed.

        :param export_task_identifier: The identifier of the snapshot or cluster export task to cancel.
        :returns: ExportTask
        :raises ExportTaskNotFoundFault:
        :raises InvalidExportTaskStateFault:
        """
        raise NotImplementedError

    @handler("CopyDBClusterParameterGroup")
    def copy_db_cluster_parameter_group(
        self,
        context: RequestContext,
        source_db_cluster_parameter_group_identifier: String,
        target_db_cluster_parameter_group_identifier: String,
        target_db_cluster_parameter_group_description: String,
        tags: TagList | None = None,
        **kwargs,
    ) -> CopyDBClusterParameterGroupResult:
        """Copies the specified DB cluster parameter group.

        You can't copy a default DB cluster parameter group. Instead, create a
        new custom DB cluster parameter group, which copies the default
        parameters and values for the specified DB cluster parameter group
        family.

        :param source_db_cluster_parameter_group_identifier: The identifier or Amazon Resource Name (ARN) for the source DB cluster
        parameter group.
        :param target_db_cluster_parameter_group_identifier: The identifier for the copied DB cluster parameter group.
        :param target_db_cluster_parameter_group_description: A description for the copied DB cluster parameter group.
        :param tags: A list of tags.
        :returns: CopyDBClusterParameterGroupResult
        :raises DBParameterGroupNotFoundFault:
        :raises DBParameterGroupQuotaExceededFault:
        :raises DBParameterGroupAlreadyExistsFault:
        """
        raise NotImplementedError

    @handler("CopyDBClusterSnapshot")
    def copy_db_cluster_snapshot(
        self,
        context: RequestContext,
        source_db_cluster_snapshot_identifier: String,
        target_db_cluster_snapshot_identifier: String,
        kms_key_id: String | None = None,
        pre_signed_url: String | None = None,
        copy_tags: BooleanOptional | None = None,
        tags: TagList | None = None,
        source_region: String | None = None,
        **kwargs,
    ) -> CopyDBClusterSnapshotResult:
        """Copies a snapshot of a DB cluster.

        To copy a DB cluster snapshot from a shared manual DB cluster snapshot,
        ``SourceDBClusterSnapshotIdentifier`` must be the Amazon Resource Name
        (ARN) of the shared DB cluster snapshot.

        You can copy an encrypted DB cluster snapshot from another Amazon Web
        Services Region. In that case, the Amazon Web Services Region where you
        call the ``CopyDBClusterSnapshot`` operation is the destination Amazon
        Web Services Region for the encrypted DB cluster snapshot to be copied
        to. To copy an encrypted DB cluster snapshot from another Amazon Web
        Services Region, you must provide the following values:

        -  ``KmsKeyId`` - The Amazon Web Services Key Management System (Amazon
           Web Services KMS) key identifier for the key to use to encrypt the
           copy of the DB cluster snapshot in the destination Amazon Web
           Services Region.

        -  ``TargetDBClusterSnapshotIdentifier`` - The identifier for the new
           copy of the DB cluster snapshot in the destination Amazon Web
           Services Region.

        -  ``SourceDBClusterSnapshotIdentifier`` - The DB cluster snapshot
           identifier for the encrypted DB cluster snapshot to be copied. This
           identifier must be in the ARN format for the source Amazon Web
           Services Region and is the same value as the
           ``SourceDBClusterSnapshotIdentifier`` in the presigned URL.

        To cancel the copy operation once it is in progress, delete the target
        DB cluster snapshot identified by ``TargetDBClusterSnapshotIdentifier``
        while that DB cluster snapshot is in "copying" status.

        For more information on copying encrypted Amazon Aurora DB cluster
        snapshots from one Amazon Web Services Region to another, see `Copying a
        Snapshot <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_CopySnapshot.html>`__
        in the *Amazon Aurora User Guide*.

        For more information on Amazon Aurora DB clusters, see `What is Amazon
        Aurora? <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html>`__
        in the *Amazon Aurora User Guide*.

        For more information on Multi-AZ DB clusters, see `Multi-AZ DB cluster
        deployments <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html>`__
        in the *Amazon RDS User Guide*.

        :param source_db_cluster_snapshot_identifier: The identifier of the DB cluster snapshot to copy.
        :param target_db_cluster_snapshot_identifier: The identifier of the new DB cluster snapshot to create from the source
        DB cluster snapshot.
        :param kms_key_id: The Amazon Web Services KMS key identifier for an encrypted DB cluster
        snapshot.
        :param pre_signed_url: When you are copying a DB cluster snapshot from one Amazon Web Services
        GovCloud (US) Region to another, the URL that contains a Signature
        Version 4 signed request for the ``CopyDBClusterSnapshot`` API operation
        in the Amazon Web Services Region that contains the source DB cluster
        snapshot to copy.
        :param copy_tags: Specifies whether to copy all tags from the source DB cluster snapshot
        to the target DB cluster snapshot.
        :param tags: A list of tags.
        :param source_region: The ID of the region that contains the snapshot to be copied.
        :returns: CopyDBClusterSnapshotResult
        :raises DBClusterSnapshotAlreadyExistsFault:
        :raises DBClusterSnapshotNotFoundFault:
        :raises InvalidDBClusterStateFault:
        :raises InvalidDBClusterSnapshotStateFault:
        :raises SnapshotQuotaExceededFault:
        :raises KMSKeyNotAccessibleFault:
        """
        raise NotImplementedError

    @handler("CopyDBParameterGroup")
    def copy_db_parameter_group(
        self,
        context: RequestContext,
        source_db_parameter_group_identifier: String,
        target_db_parameter_group_identifier: String,
        target_db_parameter_group_description: String,
        tags: TagList | None = None,
        **kwargs,
    ) -> CopyDBParameterGroupResult:
        """Copies the specified DB parameter group.

        You can't copy a default DB parameter group. Instead, create a new
        custom DB parameter group, which copies the default parameters and
        values for the specified DB parameter group family.

        :param source_db_parameter_group_identifier: The identifier or ARN for the source DB parameter group.
        :param target_db_parameter_group_identifier: The identifier for the copied DB parameter group.
        :param target_db_parameter_group_description: A description for the copied DB parameter group.
        :param tags: A list of tags.
        :returns: CopyDBParameterGroupResult
        :raises DBParameterGroupNotFoundFault:
        :raises DBParameterGroupAlreadyExistsFault:
        :raises DBParameterGroupQuotaExceededFault:
        """
        raise NotImplementedError

    @handler("CopyDBSnapshot")
    def copy_db_snapshot(
        self,
        context: RequestContext,
        source_db_snapshot_identifier: String,
        target_db_snapshot_identifier: String,
        kms_key_id: String | None = None,
        tags: TagList | None = None,
        copy_tags: BooleanOptional | None = None,
        pre_signed_url: String | None = None,
        option_group_name: String | None = None,
        target_custom_availability_zone: String | None = None,
        copy_option_group: BooleanOptional | None = None,
        source_region: String | None = None,
        **kwargs,
    ) -> CopyDBSnapshotResult:
        """Copies the specified DB snapshot. The source DB snapshot must be in the
        ``available`` state.

        You can copy a snapshot from one Amazon Web Services Region to another.
        In that case, the Amazon Web Services Region where you call the
        ``CopyDBSnapshot`` operation is the destination Amazon Web Services
        Region for the DB snapshot copy.

        This command doesn't apply to RDS Custom.

        For more information about copying snapshots, see `Copying a DB
        Snapshot <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CopySnapshot.html#USER_CopyDBSnapshot>`__
        in the *Amazon RDS User Guide*.

        :param source_db_snapshot_identifier: The identifier for the source DB snapshot.
        :param target_db_snapshot_identifier: The identifier for the copy of the snapshot.
        :param kms_key_id: The Amazon Web Services KMS key identifier for an encrypted DB snapshot.
        :param tags: A list of tags.
        :param copy_tags: Specifies whether to copy all tags from the source DB snapshot to the
        target DB snapshot.
        :param pre_signed_url: When you are copying a snapshot from one Amazon Web Services GovCloud
        (US) Region to another, the URL that contains a Signature Version 4
        signed request for the ``CopyDBSnapshot`` API operation in the source
        Amazon Web Services Region that contains the source DB snapshot to copy.
        :param option_group_name: The name of an option group to associate with the copy of the snapshot.
        :param target_custom_availability_zone: The external custom Availability Zone (CAZ) identifier for the target
        CAZ.
        :param copy_option_group: Specifies whether to copy the DB option group associated with the source
        DB snapshot to the target Amazon Web Services account and associate with
        the target DB snapshot.
        :param source_region: The ID of the region that contains the snapshot to be copied.
        :returns: CopyDBSnapshotResult
        :raises DBSnapshotAlreadyExistsFault:
        :raises DBSnapshotNotFoundFault:
        :raises InvalidDBSnapshotStateFault:
        :raises SnapshotQuotaExceededFault:
        :raises KMSKeyNotAccessibleFault:
        :raises CustomAvailabilityZoneNotFoundFault:
        """
        raise NotImplementedError

    @handler("CopyOptionGroup")
    def copy_option_group(
        self,
        context: RequestContext,
        source_option_group_identifier: String,
        target_option_group_identifier: String,
        target_option_group_description: String,
        tags: TagList | None = None,
        **kwargs,
    ) -> CopyOptionGroupResult:
        """Copies the specified option group.

        :param source_option_group_identifier: The identifier for the source option group.
        :param target_option_group_identifier: The identifier for the copied option group.
        :param target_option_group_description: The description for the copied option group.
        :param tags: A list of tags.
        :returns: CopyOptionGroupResult
        :raises OptionGroupAlreadyExistsFault:
        :raises OptionGroupNotFoundFault:
        :raises OptionGroupQuotaExceededFault:
        """
        raise NotImplementedError

    @handler("CreateBlueGreenDeployment")
    def create_blue_green_deployment(
        self,
        context: RequestContext,
        blue_green_deployment_name: BlueGreenDeploymentName,
        source: DatabaseArn,
        target_engine_version: TargetEngineVersion | None = None,
        target_db_parameter_group_name: TargetDBParameterGroupName | None = None,
        target_db_cluster_parameter_group_name: TargetDBClusterParameterGroupName | None = None,
        tags: TagList | None = None,
        target_db_instance_class: TargetDBInstanceClass | None = None,
        upgrade_target_storage_config: BooleanOptional | None = None,
        target_iops: IntegerOptional | None = None,
        target_storage_type: TargetStorageType | None = None,
        target_allocated_storage: IntegerOptional | None = None,
        target_storage_throughput: IntegerOptional | None = None,
        **kwargs,
    ) -> CreateBlueGreenDeploymentResponse:
        """Creates a blue/green deployment.

        A blue/green deployment creates a staging environment that copies the
        production environment. In a blue/green deployment, the blue environment
        is the current production environment. The green environment is the
        staging environment, and it stays in sync with the current production
        environment.

        You can make changes to the databases in the green environment without
        affecting production workloads. For example, you can upgrade the major
        or minor DB engine version, change database parameters, or make schema
        changes in the staging environment. You can thoroughly test changes in
        the green environment. When ready, you can switch over the environments
        to promote the green environment to be the new production environment.
        The switchover typically takes under a minute.

        For more information, see `Using Amazon RDS Blue/Green Deployments for
        database
        updates <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html>`__
        in the *Amazon RDS User Guide* and `Using Amazon RDS Blue/Green
        Deployments for database
        updates <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html>`__
        in the *Amazon Aurora User Guide*.

        :param blue_green_deployment_name: The name of the blue/green deployment.
        :param source: The Amazon Resource Name (ARN) of the source production database.
        :param target_engine_version: The engine version of the database in the green environment.
        :param target_db_parameter_group_name: The DB parameter group associated with the DB instance in the green
        environment.
        :param target_db_cluster_parameter_group_name: The DB cluster parameter group associated with the Aurora DB cluster in
        the green environment.
        :param tags: Tags to assign to the blue/green deployment.
        :param target_db_instance_class: Specify the DB instance class for the databases in the green
        environment.
        :param upgrade_target_storage_config: Whether to upgrade the storage file system configuration on the green
        database.
        :param target_iops: The amount of Provisioned IOPS (input/output operations per second) to
        allocate for the green DB instance.
        :param target_storage_type: The storage type to associate with the green DB instance.
        :param target_allocated_storage: The amount of storage in gibibytes (GiB) to allocate for the green DB
        instance.
        :param target_storage_throughput: The storage throughput value for the green DB instance.
        :returns: CreateBlueGreenDeploymentResponse
        :raises DBInstanceNotFoundFault:
        :raises DBClusterNotFoundFault:
        :raises SourceDatabaseNotSupportedFault:
        :raises SourceClusterNotSupportedFault:
        :raises BlueGreenDeploymentAlreadyExistsFault:
        :raises DBParameterGroupNotFoundFault:
        :raises DBClusterParameterGroupNotFoundFault:
        :raises InstanceQuotaExceededFault:
        :raises DBClusterQuotaExceededFault:
        :raises InvalidDBInstanceStateFault:
        :raises InvalidDBClusterStateFault:
        """
        raise NotImplementedError

    @handler("CreateCustomDBEngineVersion")
    def create_custom_db_engine_version(
        self,
        context: RequestContext,
        engine: CustomEngineName,
        engine_version: CustomEngineVersion,
        database_installation_files_s3_bucket_name: BucketName | None = None,
        database_installation_files_s3_prefix: String255 | None = None,
        image_id: String255 | None = None,
        kms_key_id: KmsKeyIdOrArn | None = None,
        description: Description | None = None,
        manifest: CustomDBEngineVersionManifest | None = None,
        tags: TagList | None = None,
        source_custom_db_engine_version_identifier: String255 | None = None,
        use_aws_provided_latest_image: BooleanOptional | None = None,
        **kwargs,
    ) -> DBEngineVersion:
        """Creates a custom DB engine version (CEV).

        :param engine: The database engine.
        :param engine_version: The name of your CEV.
        :param database_installation_files_s3_bucket_name: The name of an Amazon S3 bucket that contains database installation
        files for your CEV.
        :param database_installation_files_s3_prefix: The Amazon S3 directory that contains the database installation files
        for your CEV.
        :param image_id: The ID of the Amazon Machine Image (AMI).
        :param kms_key_id: The Amazon Web Services KMS key identifier for an encrypted CEV.
        :param description: An optional description of your CEV.
        :param manifest: The CEV manifest, which is a JSON document that describes the
        installation .
        :param tags: A list of tags.
        :param source_custom_db_engine_version_identifier: The ARN of a CEV to use as a source for creating a new CEV.
        :param use_aws_provided_latest_image: Specifies whether to use the latest service-provided Amazon Machine
        Image (AMI) for the CEV.
        :returns: DBEngineVersion
        :raises CustomDBEngineVersionAlreadyExistsFault:
        :raises CustomDBEngineVersionQuotaExceededFault:
        :raises Ec2ImagePropertiesNotSupportedFault:
        :raises KMSKeyNotAccessibleFault:
        :raises CreateCustomDBEngineVersionFault:
        """
        raise NotImplementedError

    @handler("CreateDBCluster")
    def create_db_cluster(
        self,
        context: RequestContext,
        db_cluster_identifier: String,
        engine: String,
        availability_zones: AvailabilityZones | None = None,
        backup_retention_period: IntegerOptional | None = None,
        character_set_name: String | None = None,
        database_name: String | None = None,
        db_cluster_parameter_group_name: String | None = None,
        vpc_security_group_ids: VpcSecurityGroupIdList | None = None,
        db_subnet_group_name: String | None = None,
        engine_version: String | None = None,
        port: IntegerOptional | None = None,
        master_username: String | None = None,
        master_user_password: String | None = None,
        option_group_name: String | None = None,
        preferred_backup_window: String | None = None,
        preferred_maintenance_window: String | None = None,
        replication_source_identifier: String | None = None,
        tags: TagList | None = None,
        storage_encrypted: BooleanOptional | None = None,
        kms_key_id: String | None = None,
        pre_signed_url: String | None = None,
        enable_iam_database_authentication: BooleanOptional | None = None,
        backtrack_window: LongOptional | None = None,
        enable_cloudwatch_logs_exports: LogTypeList | None = None,
        engine_mode: String | None = None,
        scaling_configuration: ScalingConfiguration | None = None,
        rds_custom_cluster_configuration: RdsCustomClusterConfiguration | None = None,
        deletion_protection: BooleanOptional | None = None,
        global_cluster_identifier: String | None = None,
        enable_http_endpoint: BooleanOptional | None = None,
        copy_tags_to_snapshot: BooleanOptional | None = None,
        domain: String | None = None,
        domain_iam_role_name: String | None = None,
        enable_global_write_forwarding: BooleanOptional | None = None,
        db_cluster_instance_class: String | None = None,
        allocated_storage: IntegerOptional | None = None,
        storage_type: String | None = None,
        iops: IntegerOptional | None = None,
        publicly_accessible: BooleanOptional | None = None,
        auto_minor_version_upgrade: BooleanOptional | None = None,
        monitoring_interval: IntegerOptional | None = None,
        monitoring_role_arn: String | None = None,
        database_insights_mode: DatabaseInsightsMode | None = None,
        enable_performance_insights: BooleanOptional | None = None,
        performance_insights_kms_key_id: String | None = None,
        performance_insights_retention_period: IntegerOptional | None = None,
        enable_limitless_database: BooleanOptional | None = None,
        serverless_v2_scaling_configuration: ServerlessV2ScalingConfiguration | None = None,
        network_type: String | None = None,
        cluster_scalability_type: ClusterScalabilityType | None = None,
        db_system_id: String | None = None,
        manage_master_user_password: BooleanOptional | None = None,
        master_user_secret_kms_key_id: String | None = None,
        enable_local_write_forwarding: BooleanOptional | None = None,
        ca_certificate_identifier: String | None = None,
        engine_lifecycle_support: String | None = None,
        source_region: String | None = None,
        **kwargs,
    ) -> CreateDBClusterResult:
        """Creates a new Amazon Aurora DB cluster or Multi-AZ DB cluster.

        If you create an Aurora DB cluster, the request creates an empty
        cluster. You must explicitly create the writer instance for your DB
        cluster using the
        `CreateDBInstance <https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html>`__
        operation. If you create a Multi-AZ DB cluster, the request creates a
        writer and two reader DB instances for you, each in a different
        Availability Zone.

        You can use the ``ReplicationSourceIdentifier`` parameter to create an
        Amazon Aurora DB cluster as a read replica of another DB cluster or
        Amazon RDS for MySQL or PostgreSQL DB instance. For more information
        about Amazon Aurora, see `What is Amazon
        Aurora? <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html>`__
        in the *Amazon Aurora User Guide*.

        You can also use the ``ReplicationSourceIdentifier`` parameter to create
        a Multi-AZ DB cluster read replica with an RDS for MySQL or PostgreSQL
        DB instance as the source. For more information about Multi-AZ DB
        clusters, see `Multi-AZ DB cluster
        deployments <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html>`__
        in the *Amazon RDS User Guide*.

        :param db_cluster_identifier: The identifier for this DB cluster.
        :param engine: The database engine to use for this DB cluster.
        :param availability_zones: A list of Availability Zones (AZs) where you specifically want to create
        DB instances in the DB cluster.
        :param backup_retention_period: The number of days for which automated backups are retained.
        :param character_set_name: The name of the character set (``CharacterSet``) to associate the DB
        cluster with.
        :param database_name: The name for your database of up to 64 alphanumeric characters.
        :param db_cluster_parameter_group_name: The name of the DB cluster parameter group to associate with this DB
        cluster.
        :param vpc_security_group_ids: A list of EC2 VPC security groups to associate with this DB cluster.
        :param db_subnet_group_name: A DB subnet group to associate with this DB cluster.
        :param engine_version: The version number of the database engine to use.
        :param port: The port number on which the instances in the DB cluster accept
        connections.
        :param master_username: The name of the master user for the DB cluster.
        :param master_user_password: The password for the master database user.
        :param option_group_name: The option group to associate the DB cluster with.
        :param preferred_backup_window: The daily time range during which automated backups are created if
        automated backups are enabled using the ``BackupRetentionPeriod``
        parameter.
        :param preferred_maintenance_window: The weekly time range during which system maintenance can occur.
        :param replication_source_identifier: The Amazon Resource Name (ARN) of the source DB instance or DB cluster
        if this DB cluster is created as a read replica.
        :param tags: Tags to assign to the DB cluster.
        :param storage_encrypted: Specifies whether the DB cluster is encrypted.
        :param kms_key_id: The Amazon Web Services KMS key identifier for an encrypted DB cluster.
        :param pre_signed_url: When you are replicating a DB cluster from one Amazon Web Services
        GovCloud (US) Region to another, an URL that contains a Signature
        Version 4 signed request for the ``CreateDBCluster`` operation to be
        called in the source Amazon Web Services Region where the DB cluster is
        replicated from.
        :param enable_iam_database_authentication: Specifies whether to enable mapping of Amazon Web Services Identity and
        Access Management (IAM) accounts to database accounts.
        :param backtrack_window: The target backtrack window, in seconds.
        :param enable_cloudwatch_logs_exports: The list of log types that need to be enabled for exporting to
        CloudWatch Logs.
        :param engine_mode: The DB engine mode of the DB cluster, either ``provisioned`` or
        ``serverless``.
        :param scaling_configuration: For DB clusters in ``serverless`` DB engine mode, the scaling properties
        of the DB cluster.
        :param rds_custom_cluster_configuration: Reserved for future use.
        :param deletion_protection: Specifies whether the DB cluster has deletion protection enabled.
        :param global_cluster_identifier: The global cluster ID of an Aurora cluster that becomes the primary
        cluster in the new global database cluster.
        :param enable_http_endpoint: Specifies whether to enable the HTTP endpoint for the DB cluster.
        :param copy_tags_to_snapshot: Specifies whether to copy all tags from the DB cluster to snapshots of
        the DB cluster.
        :param domain: The Active Directory directory ID to create the DB cluster in.
        :param domain_iam_role_name: The name of the IAM role to use when making API calls to the Directory
        Service.
        :param enable_global_write_forwarding: Specifies whether to enable this DB cluster to forward write operations
        to the primary cluster of a global cluster (Aurora global database).
        :param db_cluster_instance_class: The compute and memory capacity of each DB instance in the Multi-AZ DB
        cluster, for example ``db.
        :param allocated_storage: The amount of storage in gibibytes (GiB) to allocate to each DB instance
        in the Multi-AZ DB cluster.
        :param storage_type: The storage type to associate with the DB cluster.
        :param iops: The amount of Provisioned IOPS (input/output operations per second) to
        be initially allocated for each DB instance in the Multi-AZ DB cluster.
        :param publicly_accessible: Specifies whether the DB cluster is publicly accessible.
        :param auto_minor_version_upgrade: Specifies whether minor engine upgrades are applied automatically to the
        DB cluster during the maintenance window.
        :param monitoring_interval: The interval, in seconds, between points when Enhanced Monitoring
        metrics are collected for the DB cluster.
        :param monitoring_role_arn: The Amazon Resource Name (ARN) for the IAM role that permits RDS to send
        Enhanced Monitoring metrics to Amazon CloudWatch Logs.
        :param database_insights_mode: The mode of Database Insights to enable for the DB cluster.
        :param enable_performance_insights: Specifies whether to turn on Performance Insights for the DB cluster.
        :param performance_insights_kms_key_id: The Amazon Web Services KMS key identifier for encryption of Performance
        Insights data.
        :param performance_insights_retention_period: The number of days to retain Performance Insights data.
        :param enable_limitless_database: Specifies whether to enable Aurora Limitless Database.
        :param serverless_v2_scaling_configuration: Contains the scaling configuration of an Aurora Serverless v2 DB
        cluster.
        :param network_type: The network type of the DB cluster.
        :param cluster_scalability_type: Specifies the scalability mode of the Aurora DB cluster.
        :param db_system_id: Reserved for future use.
        :param manage_master_user_password: Specifies whether to manage the master user password with Amazon Web
        Services Secrets Manager.
        :param master_user_secret_kms_key_id: The Amazon Web Services KMS key identifier to encrypt a secret that is
        automatically generated and managed in Amazon Web Services Secrets
        Manager.
        :param enable_local_write_forwarding: Specifies whether read replicas can forward write operations to the
        writer DB instance in the DB cluster.
        :param ca_certificate_identifier: The CA certificate identifier to use for the DB cluster's server
        certificate.
        :param engine_lifecycle_support: The life cycle type for this DB cluster.
        :param source_region: The ID of the region that contains the source for the db cluster.
        :returns: CreateDBClusterResult
        :raises DBClusterAlreadyExistsFault:
        :raises InsufficientDBInstanceCapacityFault:
        :raises InsufficientStorageClusterCapacityFault:
        :raises DBClusterQuotaExceededFault:
        :raises StorageQuotaExceededFault:
        :raises DBSubnetGroupNotFoundFault:
        :raises InvalidVPCNetworkStateFault:
        :raises InvalidDBClusterStateFault:
        :raises InvalidDBSubnetGroupFault:
        :raises InvalidDBSubnetGroupStateFault:
        :raises InvalidSubnet:
        :raises InvalidDBInstanceStateFault:
        :raises DBClusterParameterGroupNotFoundFault:
        :raises KMSKeyNotAccessibleFault:
        :raises DBClusterNotFoundFault:
        :raises DBInstanceNotFoundFault:
        :raises DBSubnetGroupDoesNotCoverEnoughAZs:
        :raises GlobalClusterNotFoundFault:
        :raises InvalidGlobalClusterStateFault:
        :raises DomainNotFoundFault:
        :raises OptionGroupNotFoundFault:
        """
        raise NotImplementedError

    @handler("CreateDBClusterEndpoint")
    def create_db_cluster_endpoint(
        self,
        context: RequestContext,
        db_cluster_identifier: String,
        db_cluster_endpoint_identifier: String,
        endpoint_type: String,
        static_members: StringList | None = None,
        excluded_members: StringList | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> DBClusterEndpoint:
        """Creates a new custom endpoint and associates it with an Amazon Aurora DB
        cluster.

        This action applies only to Aurora DB clusters.

        :param db_cluster_identifier: The DB cluster identifier of the DB cluster associated with the
        endpoint.
        :param db_cluster_endpoint_identifier: The identifier to use for the new endpoint.
        :param endpoint_type: The type of the endpoint, one of: ``READER``, ``WRITER``, ``ANY``.
        :param static_members: List of DB instance identifiers that are part of the custom endpoint
        group.
        :param excluded_members: List of DB instance identifiers that aren't part of the custom endpoint
        group.
        :param tags: The tags to be assigned to the Amazon RDS resource.
        :returns: DBClusterEndpoint
        :raises DBClusterEndpointQuotaExceededFault:
        :raises DBClusterEndpointAlreadyExistsFault:
        :raises DBClusterNotFoundFault:
        :raises InvalidDBClusterStateFault:
        :raises DBInstanceNotFoundFault:
        :raises InvalidDBInstanceStateFault:
        """
        raise NotImplementedError

    @handler("CreateDBClusterParameterGroup")
    def create_db_cluster_parameter_group(
        self,
        context: RequestContext,
        db_cluster_parameter_group_name: String,
        db_parameter_group_family: String,
        description: String,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateDBClusterParameterGroupResult:
        """Creates a new DB cluster parameter group.

        Parameters in a DB cluster parameter group apply to all of the instances
        in a DB cluster.

        A DB cluster parameter group is initially created with the default
        parameters for the database engine used by instances in the DB cluster.
        To provide custom values for any of the parameters, you must modify the
        group after creating it using ``ModifyDBClusterParameterGroup``. Once
        you've created a DB cluster parameter group, you need to associate it
        with your DB cluster using ``ModifyDBCluster``.

        When you associate a new DB cluster parameter group with a running
        Aurora DB cluster, reboot the DB instances in the DB cluster without
        failover for the new DB cluster parameter group and associated settings
        to take effect.

        When you associate a new DB cluster parameter group with a running
        Multi-AZ DB cluster, reboot the DB cluster without failover for the new
        DB cluster parameter group and associated settings to take effect.

        After you create a DB cluster parameter group, you should wait at least
        5 minutes before creating your first DB cluster that uses that DB
        cluster parameter group as the default parameter group. This allows
        Amazon RDS to fully complete the create action before the DB cluster
        parameter group is used as the default for a new DB cluster. This is
        especially important for parameters that are critical when creating the
        default database for a DB cluster, such as the character set for the
        default database defined by the ``character_set_database`` parameter.
        You can use the *Parameter Groups* option of the `Amazon RDS
        console <https://console.aws.amazon.com/rds/>`__ or the
        ``DescribeDBClusterParameters`` operation to verify that your DB cluster
        parameter group has been created or modified.

        For more information on Amazon Aurora, see `What is Amazon
        Aurora? <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html>`__
        in the *Amazon Aurora User Guide*.

        For more information on Multi-AZ DB clusters, see `Multi-AZ DB cluster
        deployments <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html>`__
        in the *Amazon RDS User Guide*.

        :param db_cluster_parameter_group_name: The name of the DB cluster parameter group.
        :param db_parameter_group_family: The DB cluster parameter group family name.
        :param description: The description for the DB cluster parameter group.
        :param tags: Tags to assign to the DB cluster parameter group.
        :returns: CreateDBClusterParameterGroupResult
        :raises DBParameterGroupQuotaExceededFault:
        :raises DBParameterGroupAlreadyExistsFault:
        """
        raise NotImplementedError

    @handler("CreateDBClusterSnapshot")
    def create_db_cluster_snapshot(
        self,
        context: RequestContext,
        db_cluster_snapshot_identifier: String,
        db_cluster_identifier: String,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateDBClusterSnapshotResult:
        """Creates a snapshot of a DB cluster.

        For more information on Amazon Aurora, see `What is Amazon
        Aurora? <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html>`__
        in the *Amazon Aurora User Guide*.

        For more information on Multi-AZ DB clusters, see `Multi-AZ DB cluster
        deployments <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html>`__
        in the *Amazon RDS User Guide*.

        :param db_cluster_snapshot_identifier: The identifier of the DB cluster snapshot.
        :param db_cluster_identifier: The identifier of the DB cluster to create a snapshot for.
        :param tags: The tags to be assigned to the DB cluster snapshot.
        :returns: CreateDBClusterSnapshotResult
        :raises DBClusterSnapshotAlreadyExistsFault:
        :raises InvalidDBClusterStateFault:
        :raises DBClusterNotFoundFault:
        :raises SnapshotQuotaExceededFault:
        :raises InvalidDBClusterSnapshotStateFault:
        """
        raise NotImplementedError

    @handler("CreateDBInstance")
    def create_db_instance(
        self,
        context: RequestContext,
        db_instance_identifier: String,
        db_instance_class: String,
        engine: String,
        db_name: String | None = None,
        allocated_storage: IntegerOptional | None = None,
        master_username: String | None = None,
        master_user_password: String | None = None,
        db_security_groups: DBSecurityGroupNameList | None = None,
        vpc_security_group_ids: VpcSecurityGroupIdList | None = None,
        availability_zone: String | None = None,
        db_subnet_group_name: String | None = None,
        preferred_maintenance_window: String | None = None,
        db_parameter_group_name: String | None = None,
        backup_retention_period: IntegerOptional | None = None,
        preferred_backup_window: String | None = None,
        port: IntegerOptional | None = None,
        multi_az: BooleanOptional | None = None,
        engine_version: String | None = None,
        auto_minor_version_upgrade: BooleanOptional | None = None,
        license_model: String | None = None,
        iops: IntegerOptional | None = None,
        option_group_name: String | None = None,
        character_set_name: String | None = None,
        nchar_character_set_name: String | None = None,
        publicly_accessible: BooleanOptional | None = None,
        tags: TagList | None = None,
        db_cluster_identifier: String | None = None,
        storage_type: String | None = None,
        tde_credential_arn: String | None = None,
        tde_credential_password: String | None = None,
        storage_encrypted: BooleanOptional | None = None,
        kms_key_id: String | None = None,
        domain: String | None = None,
        domain_fqdn: String | None = None,
        domain_ou: String | None = None,
        domain_auth_secret_arn: String | None = None,
        domain_dns_ips: StringList | None = None,
        copy_tags_to_snapshot: BooleanOptional | None = None,
        monitoring_interval: IntegerOptional | None = None,
        monitoring_role_arn: String | None = None,
        domain_iam_role_name: String | None = None,
        promotion_tier: IntegerOptional | None = None,
        timezone: String | None = None,
        enable_iam_database_authentication: BooleanOptional | None = None,
        database_insights_mode: DatabaseInsightsMode | None = None,
        enable_performance_insights: BooleanOptional | None = None,
        performance_insights_kms_key_id: String | None = None,
        performance_insights_retention_period: IntegerOptional | None = None,
        enable_cloudwatch_logs_exports: LogTypeList | None = None,
        processor_features: ProcessorFeatureList | None = None,
        deletion_protection: BooleanOptional | None = None,
        max_allocated_storage: IntegerOptional | None = None,
        enable_customer_owned_ip: BooleanOptional | None = None,
        custom_iam_instance_profile: String | None = None,
        backup_target: String | None = None,
        network_type: String | None = None,
        storage_throughput: IntegerOptional | None = None,
        manage_master_user_password: BooleanOptional | None = None,
        master_user_secret_kms_key_id: String | None = None,
        ca_certificate_identifier: String | None = None,
        db_system_id: String | None = None,
        dedicated_log_volume: BooleanOptional | None = None,
        multi_tenant: BooleanOptional | None = None,
        engine_lifecycle_support: String | None = None,
        **kwargs,
    ) -> CreateDBInstanceResult:
        """Creates a new DB instance.

        The new DB instance can be an RDS DB instance, or it can be a DB
        instance in an Aurora DB cluster. For an Aurora DB cluster, you can call
        this operation multiple times to add more than one DB instance to the
        cluster.

        For more information about creating an RDS DB instance, see `Creating an
        Amazon RDS DB
        instance <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html>`__
        in the *Amazon RDS User Guide*.

        For more information about creating a DB instance in an Aurora DB
        cluster, see `Creating an Amazon Aurora DB
        cluster <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.CreateInstance.html>`__
        in the *Amazon Aurora User Guide*.

        :param db_instance_identifier: The identifier for this DB instance.
        :param db_instance_class: The compute and memory capacity of the DB instance, for example
        ``db.
        :param engine: The database engine to use for this DB instance.
        :param db_name: The meaning of this parameter differs according to the database engine
        you use.
        :param allocated_storage: The amount of storage in gibibytes (GiB) to allocate for the DB
        instance.
        :param master_username: The name for the master user.
        :param master_user_password: The password for the master user.
        :param db_security_groups: A list of DB security groups to associate with this DB instance.
        :param vpc_security_group_ids: A list of Amazon EC2 VPC security groups to associate with this DB
        instance.
        :param availability_zone: The Availability Zone (AZ) where the database will be created.
        :param db_subnet_group_name: A DB subnet group to associate with this DB instance.
        :param preferred_maintenance_window: The time range each week during which system maintenance can occur.
        :param db_parameter_group_name: The name of the DB parameter group to associate with this DB instance.
        :param backup_retention_period: The number of days for which automated backups are retained.
        :param preferred_backup_window: The daily time range during which automated backups are created if
        automated backups are enabled, using the ``BackupRetentionPeriod``
        parameter.
        :param port: The port number on which the database accepts connections.
        :param multi_az: Specifies whether the DB instance is a Multi-AZ deployment.
        :param engine_version: The version number of the database engine to use.
        :param auto_minor_version_upgrade: Specifies whether minor engine upgrades are applied automatically to the
        DB instance during the maintenance window.
        :param license_model: The license model information for this DB instance.
        :param iops: The amount of Provisioned IOPS (input/output operations per second) to
        initially allocate for the DB instance.
        :param option_group_name: The option group to associate the DB instance with.
        :param character_set_name: For supported engines, the character set (``CharacterSet``) to associate
        the DB instance with.
        :param nchar_character_set_name: The name of the NCHAR character set for the Oracle DB instance.
        :param publicly_accessible: Specifies whether the DB instance is publicly accessible.
        :param tags: Tags to assign to the DB instance.
        :param db_cluster_identifier: The identifier of the DB cluster that this DB instance will belong to.
        :param storage_type: The storage type to associate with the DB instance.
        :param tde_credential_arn: The ARN from the key store with which to associate the instance for TDE
        encryption.
        :param tde_credential_password: The password for the given ARN from the key store in order to access the
        device.
        :param storage_encrypted: Specifes whether the DB instance is encrypted.
        :param kms_key_id: The Amazon Web Services KMS key identifier for an encrypted DB instance.
        :param domain: The Active Directory directory ID to create the DB instance in.
        :param domain_fqdn: The fully qualified domain name (FQDN) of an Active Directory domain.
        :param domain_ou: The Active Directory organizational unit for your DB instance to join.
        :param domain_auth_secret_arn: The ARN for the Secrets Manager secret with the credentials for the user
        joining the domain.
        :param domain_dns_ips: The IPv4 DNS IP addresses of your primary and secondary Active Directory
        domain controllers.
        :param copy_tags_to_snapshot: Specifies whether to copy tags from the DB instance to snapshots of the
        DB instance.
        :param monitoring_interval: The interval, in seconds, between points when Enhanced Monitoring
        metrics are collected for the DB instance.
        :param monitoring_role_arn: The ARN for the IAM role that permits RDS to send enhanced monitoring
        metrics to Amazon CloudWatch Logs.
        :param domain_iam_role_name: The name of the IAM role to use when making API calls to the Directory
        Service.
        :param promotion_tier: The order of priority in which an Aurora Replica is promoted to the
        primary instance after a failure of the existing primary instance.
        :param timezone: The time zone of the DB instance.
        :param enable_iam_database_authentication: Specifies whether to enable mapping of Amazon Web Services Identity and
        Access Management (IAM) accounts to database accounts.
        :param database_insights_mode: The mode of Database Insights to enable for the DB instance.
        :param enable_performance_insights: Specifies whether to enable Performance Insights for the DB instance.
        :param performance_insights_kms_key_id: The Amazon Web Services KMS key identifier for encryption of Performance
        Insights data.
        :param performance_insights_retention_period: The number of days to retain Performance Insights data.
        :param enable_cloudwatch_logs_exports: The list of log types to enable for exporting to CloudWatch Logs.
        :param processor_features: The number of CPU cores and the number of threads per core for the DB
        instance class of the DB instance.
        :param deletion_protection: Specifies whether the DB instance has deletion protection enabled.
        :param max_allocated_storage: The upper limit in gibibytes (GiB) to which Amazon RDS can automatically
        scale the storage of the DB instance.
        :param enable_customer_owned_ip: Specifies whether to enable a customer-owned IP address (CoIP) for an
        RDS on Outposts DB instance.
        :param custom_iam_instance_profile: The instance profile associated with the underlying Amazon EC2 instance
        of an RDS Custom DB instance.
        :param backup_target: The location for storing automated backups and manual snapshots.
        :param network_type: The network type of the DB instance.
        :param storage_throughput: The storage throughput value, in mebibyte per second (MiBps), for the DB
        instance.
        :param manage_master_user_password: Specifies whether to manage the master user password with Amazon Web
        Services Secrets Manager.
        :param master_user_secret_kms_key_id: The Amazon Web Services KMS key identifier to encrypt a secret that is
        automatically generated and managed in Amazon Web Services Secrets
        Manager.
        :param ca_certificate_identifier: The CA certificate identifier to use for the DB instance's server
        certificate.
        :param db_system_id: The Oracle system identifier (SID), which is the name of the Oracle
        database instance that manages your database files.
        :param dedicated_log_volume: Indicates whether the DB instance has a dedicated log volume (DLV)
        enabled.
        :param multi_tenant: Specifies whether to use the multi-tenant configuration or the
        single-tenant configuration (default).
        :param engine_lifecycle_support: The life cycle type for this DB instance.
        :returns: CreateDBInstanceResult
        :raises DBInstanceAlreadyExistsFault:
        :raises InsufficientDBInstanceCapacityFault:
        :raises DBParameterGroupNotFoundFault:
        :raises DBSecurityGroupNotFoundFault:
        :raises InstanceQuotaExceededFault:
        :raises StorageQuotaExceededFault:
        :raises DBSubnetGroupNotFoundFault:
        :raises DBSubnetGroupDoesNotCoverEnoughAZs:
        :raises InvalidDBClusterStateFault:
        :raises InvalidSubnet:
        :raises InvalidVPCNetworkStateFault:
        :raises ProvisionedIopsNotAvailableInAZFault:
        :raises OptionGroupNotFoundFault:
        :raises DBClusterNotFoundFault:
        :raises StorageTypeNotSupportedFault:
        :raises AuthorizationNotFoundFault:
        :raises KMSKeyNotAccessibleFault:
        :raises DomainNotFoundFault:
        :raises BackupPolicyNotFoundFault:
        :raises NetworkTypeNotSupported:
        :raises CertificateNotFoundFault:
        :raises TenantDatabaseQuotaExceededFault:
        """
        raise NotImplementedError

    @handler("CreateDBInstanceReadReplica")
    def create_db_instance_read_replica(
        self,
        context: RequestContext,
        db_instance_identifier: String,
        source_db_instance_identifier: String | None = None,
        db_instance_class: String | None = None,
        availability_zone: String | None = None,
        port: IntegerOptional | None = None,
        multi_az: BooleanOptional | None = None,
        auto_minor_version_upgrade: BooleanOptional | None = None,
        iops: IntegerOptional | None = None,
        option_group_name: String | None = None,
        db_parameter_group_name: String | None = None,
        publicly_accessible: BooleanOptional | None = None,
        tags: TagList | None = None,
        db_subnet_group_name: String | None = None,
        vpc_security_group_ids: VpcSecurityGroupIdList | None = None,
        storage_type: String | None = None,
        copy_tags_to_snapshot: BooleanOptional | None = None,
        monitoring_interval: IntegerOptional | None = None,
        monitoring_role_arn: String | None = None,
        kms_key_id: String | None = None,
        pre_signed_url: String | None = None,
        enable_iam_database_authentication: BooleanOptional | None = None,
        database_insights_mode: DatabaseInsightsMode | None = None,
        enable_performance_insights: BooleanOptional | None = None,
        performance_insights_kms_key_id: String | None = None,
        performance_insights_retention_period: IntegerOptional | None = None,
        enable_cloudwatch_logs_exports: LogTypeList | None = None,
        processor_features: ProcessorFeatureList | None = None,
        use_default_processor_features: BooleanOptional | None = None,
        deletion_protection: BooleanOptional | None = None,
        domain: String | None = None,
        domain_iam_role_name: String | None = None,
        domain_fqdn: String | None = None,
        domain_ou: String | None = None,
        domain_auth_secret_arn: String | None = None,
        domain_dns_ips: StringList | None = None,
        replica_mode: ReplicaMode | None = None,
        max_allocated_storage: IntegerOptional | None = None,
        custom_iam_instance_profile: String | None = None,
        network_type: String | None = None,
        storage_throughput: IntegerOptional | None = None,
        enable_customer_owned_ip: BooleanOptional | None = None,
        allocated_storage: IntegerOptional | None = None,
        source_db_cluster_identifier: String | None = None,
        dedicated_log_volume: BooleanOptional | None = None,
        upgrade_storage_config: BooleanOptional | None = None,
        ca_certificate_identifier: String | None = None,
        source_region: String | None = None,
        **kwargs,
    ) -> CreateDBInstanceReadReplicaResult:
        """Creates a new DB instance that acts as a read replica for an existing
        source DB instance or Multi-AZ DB cluster. You can create a read replica
        for a DB instance running Db2, MariaDB, MySQL, Oracle, PostgreSQL, or
        SQL Server. You can create a read replica for a Multi-AZ DB cluster
        running MySQL or PostgreSQL. For more information, see `Working with
        read
        replicas <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html>`__
        and `Migrating from a Multi-AZ DB cluster to a DB instance using a read
        replica <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html#multi-az-db-clusters-migrating-to-instance-with-read-replica>`__
        in the *Amazon RDS User Guide*.

        Amazon Aurora doesn't support this operation. To create a DB instance
        for an Aurora DB cluster, use the ``CreateDBInstance`` operation.

        All read replica DB instances are created with backups disabled. All
        other attributes (including DB security groups and DB parameter groups)
        are inherited from the source DB instance or cluster, except as
        specified.

        Your source DB instance or cluster must have backup retention enabled.

        :param db_instance_identifier: The DB instance identifier of the read replica.
        :param source_db_instance_identifier: The identifier of the DB instance that will act as the source for the
        read replica.
        :param db_instance_class: The compute and memory capacity of the read replica, for example
        db.
        :param availability_zone: The Availability Zone (AZ) where the read replica will be created.
        :param port: The port number that the DB instance uses for connections.
        :param multi_az: Specifies whether the read replica is in a Multi-AZ deployment.
        :param auto_minor_version_upgrade: Specifies whether to automatically apply minor engine upgrades to the
        read replica during the maintenance window.
        :param iops: The amount of Provisioned IOPS (input/output operations per second) to
        initially allocate for the DB instance.
        :param option_group_name: The option group to associate the DB instance with.
        :param db_parameter_group_name: The name of the DB parameter group to associate with this read replica
        DB instance.
        :param publicly_accessible: Specifies whether the DB instance is publicly accessible.
        :param tags: A list of tags.
        :param db_subnet_group_name: A DB subnet group for the DB instance.
        :param vpc_security_group_ids: A list of Amazon EC2 VPC security groups to associate with the read
        replica.
        :param storage_type: The storage type to associate with the read replica.
        :param copy_tags_to_snapshot: Specifies whether to copy all tags from the read replica to snapshots of
        the read replica.
        :param monitoring_interval: The interval, in seconds, between points when Enhanced Monitoring
        metrics are collected for the read replica.
        :param monitoring_role_arn: The ARN for the IAM role that permits RDS to send enhanced monitoring
        metrics to Amazon CloudWatch Logs.
        :param kms_key_id: The Amazon Web Services KMS key identifier for an encrypted read
        replica.
        :param pre_signed_url: When you are creating a read replica from one Amazon Web Services
        GovCloud (US) Region to another or from one China Amazon Web Services
        Region to another, the URL that contains a Signature Version 4 signed
        request for the ``CreateDBInstanceReadReplica`` API operation in the
        source Amazon Web Services Region that contains the source DB instance.
        :param enable_iam_database_authentication: Specifies whether to enable mapping of Amazon Web Services Identity and
        Access Management (IAM) accounts to database accounts.
        :param database_insights_mode: The mode of Database Insights to enable for the read replica.
        :param enable_performance_insights: Specifies whether to enable Performance Insights for the read replica.
        :param performance_insights_kms_key_id: The Amazon Web Services KMS key identifier for encryption of Performance
        Insights data.
        :param performance_insights_retention_period: The number of days to retain Performance Insights data.
        :param enable_cloudwatch_logs_exports: The list of logs that the new DB instance is to export to CloudWatch
        Logs.
        :param processor_features: The number of CPU cores and the number of threads per core for the DB
        instance class of the DB instance.
        :param use_default_processor_features: Specifies whether the DB instance class of the DB instance uses its
        default processor features.
        :param deletion_protection: Specifies whether to enable deletion protection for the DB instance.
        :param domain: The Active Directory directory ID to create the DB instance in.
        :param domain_iam_role_name: The name of the IAM role to use when making API calls to the Directory
        Service.
        :param domain_fqdn: The fully qualified domain name (FQDN) of an Active Directory domain.
        :param domain_ou: The Active Directory organizational unit for your DB instance to join.
        :param domain_auth_secret_arn: The ARN for the Secrets Manager secret with the credentials for the user
        joining the domain.
        :param domain_dns_ips: The IPv4 DNS IP addresses of your primary and secondary Active Directory
        domain controllers.
        :param replica_mode: The open mode of the replica database: mounted or read-only.
        :param max_allocated_storage: The upper limit in gibibytes (GiB) to which Amazon RDS can automatically
        scale the storage of the DB instance.
        :param custom_iam_instance_profile: The instance profile associated with the underlying Amazon EC2 instance
        of an RDS Custom DB instance.
        :param network_type: The network type of the DB instance.
        :param storage_throughput: Specifies the storage throughput value for the read replica.
        :param enable_customer_owned_ip: Specifies whether to enable a customer-owned IP address (CoIP) for an
        RDS on Outposts read replica.
        :param allocated_storage: The amount of storage (in gibibytes) to allocate initially for the read
        replica.
        :param source_db_cluster_identifier: The identifier of the Multi-AZ DB cluster that will act as the source
        for the read replica.
        :param dedicated_log_volume: Indicates whether the DB instance has a dedicated log volume (DLV)
        enabled.
        :param upgrade_storage_config: Whether to upgrade the storage file system configuration on the read
        replica.
        :param ca_certificate_identifier: The CA certificate identifier to use for the read replica's server
        certificate.
        :param source_region: The ID of the region that contains the source for the read replica.
        :returns: CreateDBInstanceReadReplicaResult
        :raises DBInstanceAlreadyExistsFault:
        :raises InsufficientDBInstanceCapacityFault:
        :raises DBParameterGroupNotFoundFault:
        :raises DBSecurityGroupNotFoundFault:
        :raises InstanceQuotaExceededFault:
        :raises StorageQuotaExceededFault:
        :raises DBInstanceNotFoundFault:
        :raises DBClusterNotFoundFault:
        :raises InvalidDBInstanceStateFault:
        :raises InvalidDBClusterStateFault:
        :raises DBSubnetGroupNotFoundFault:
        :raises DBSubnetGroupDoesNotCoverEnoughAZs:
        :raises InvalidSubnet:
        :raises InvalidVPCNetworkStateFault:
        :raises ProvisionedIopsNotAvailableInAZFault:
        :raises OptionGroupNotFoundFault:
        :raises DBSubnetGroupNotAllowedFault:
        :raises InvalidDBSubnetGroupFault:
        :raises StorageTypeNotSupportedFault:
        :raises KMSKeyNotAccessibleFault:
        :raises DomainNotFoundFault:
        :raises NetworkTypeNotSupported:
        :raises TenantDatabaseQuotaExceededFault:
        :raises CertificateNotFoundFault:
        """
        raise NotImplementedError

    @handler("CreateDBParameterGroup")
    def create_db_parameter_group(
        self,
        context: RequestContext,
        db_parameter_group_name: String,
        db_parameter_group_family: String,
        description: String,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateDBParameterGroupResult:
        """Creates a new DB parameter group.

        A DB parameter group is initially created with the default parameters
        for the database engine used by the DB instance. To provide custom
        values for any of the parameters, you must modify the group after
        creating it using ``ModifyDBParameterGroup``. Once you've created a DB
        parameter group, you need to associate it with your DB instance using
        ``ModifyDBInstance``. When you associate a new DB parameter group with a
        running DB instance, you need to reboot the DB instance without failover
        for the new DB parameter group and associated settings to take effect.

        This command doesn't apply to RDS Custom.

        :param db_parameter_group_name: The name of the DB parameter group.
        :param db_parameter_group_family: The DB parameter group family name.
        :param description: The description for the DB parameter group.
        :param tags: Tags to assign to the DB parameter group.
        :returns: CreateDBParameterGroupResult
        :raises DBParameterGroupQuotaExceededFault:
        :raises DBParameterGroupAlreadyExistsFault:
        """
        raise NotImplementedError

    @handler("CreateDBProxy")
    def create_db_proxy(
        self,
        context: RequestContext,
        db_proxy_name: String,
        engine_family: EngineFamily,
        auth: UserAuthConfigList,
        role_arn: String,
        vpc_subnet_ids: StringList,
        vpc_security_group_ids: StringList | None = None,
        require_tls: Boolean | None = None,
        idle_client_timeout: IntegerOptional | None = None,
        debug_logging: Boolean | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateDBProxyResponse:
        """Creates a new DB proxy.

        :param db_proxy_name: The identifier for the proxy.
        :param engine_family: The kinds of databases that the proxy can connect to.
        :param auth: The authorization mechanism that the proxy uses.
        :param role_arn: The Amazon Resource Name (ARN) of the IAM role that the proxy uses to
        access secrets in Amazon Web Services Secrets Manager.
        :param vpc_subnet_ids: One or more VPC subnet IDs to associate with the new proxy.
        :param vpc_security_group_ids: One or more VPC security group IDs to associate with the new proxy.
        :param require_tls: Specifies whether Transport Layer Security (TLS) encryption is required
        for connections to the proxy.
        :param idle_client_timeout: The number of seconds that a connection to the proxy can be inactive
        before the proxy disconnects it.
        :param debug_logging: Specifies whether the proxy includes detailed information about SQL
        statements in its logs.
        :param tags: An optional set of key-value pairs to associate arbitrary data of your
        choosing with the proxy.
        :returns: CreateDBProxyResponse
        :raises InvalidSubnet:
        :raises DBProxyAlreadyExistsFault:
        :raises DBProxyQuotaExceededFault:
        """
        raise NotImplementedError

    @handler("CreateDBProxyEndpoint")
    def create_db_proxy_endpoint(
        self,
        context: RequestContext,
        db_proxy_name: DBProxyName,
        db_proxy_endpoint_name: DBProxyEndpointName,
        vpc_subnet_ids: StringList,
        vpc_security_group_ids: StringList | None = None,
        target_role: DBProxyEndpointTargetRole | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateDBProxyEndpointResponse:
        """Creates a ``DBProxyEndpoint``. Only applies to proxies that are
        associated with Aurora DB clusters. You can use DB proxy endpoints to
        specify read/write or read-only access to the DB cluster. You can also
        use DB proxy endpoints to access a DB proxy through a different VPC than
        the proxy's default VPC.

        :param db_proxy_name: The name of the DB proxy associated with the DB proxy endpoint that you
        create.
        :param db_proxy_endpoint_name: The name of the DB proxy endpoint to create.
        :param vpc_subnet_ids: The VPC subnet IDs for the DB proxy endpoint that you create.
        :param vpc_security_group_ids: The VPC security group IDs for the DB proxy endpoint that you create.
        :param target_role: The role of the DB proxy endpoint.
        :param tags: A list of tags.
        :returns: CreateDBProxyEndpointResponse
        :raises InvalidSubnet:
        :raises DBProxyNotFoundFault:
        :raises DBProxyEndpointAlreadyExistsFault:
        :raises DBProxyEndpointQuotaExceededFault:
        :raises InvalidDBProxyStateFault:
        """
        raise NotImplementedError

    @handler("CreateDBSecurityGroup")
    def create_db_security_group(
        self,
        context: RequestContext,
        db_security_group_name: String,
        db_security_group_description: String,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateDBSecurityGroupResult:
        """Creates a new DB security group. DB security groups control access to a
        DB instance.

        A DB security group controls access to EC2-Classic DB instances that are
        not in a VPC.

        EC2-Classic was retired on August 15, 2022. If you haven't migrated from
        EC2-Classic to a VPC, we recommend that you migrate as soon as possible.
        For more information, see `Migrate from EC2-Classic to a
        VPC <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-migrate.html>`__
        in the *Amazon EC2 User Guide*, the blog `EC2-Classic Networking is
        Retiring – Here’s How to
        Prepare <http://aws.amazon.com/blogs/aws/ec2-classic-is-retiring-heres-how-to-prepare/>`__,
        and `Moving a DB instance not in a VPC into a
        VPC <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Non-VPC2VPC.html>`__
        in the *Amazon RDS User Guide*.

        :param db_security_group_name: The name for the DB security group.
        :param db_security_group_description: The description for the DB security group.
        :param tags: Tags to assign to the DB security group.
        :returns: CreateDBSecurityGroupResult
        :raises DBSecurityGroupAlreadyExistsFault:
        :raises DBSecurityGroupQuotaExceededFault:
        :raises DBSecurityGroupNotSupportedFault:
        """
        raise NotImplementedError

    @handler("CreateDBShardGroup")
    def create_db_shard_group(
        self,
        context: RequestContext,
        db_shard_group_identifier: String,
        db_cluster_identifier: String,
        max_acu: DoubleOptional,
        compute_redundancy: IntegerOptional | None = None,
        min_acu: DoubleOptional | None = None,
        publicly_accessible: BooleanOptional | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> DBShardGroup:
        """Creates a new DB shard group for Aurora Limitless Database. You must
        enable Aurora Limitless Database to create a DB shard group.

        Valid for: Aurora DB clusters only

        :param db_shard_group_identifier: The name of the DB shard group.
        :param db_cluster_identifier: The name of the primary DB cluster for the DB shard group.
        :param max_acu: The maximum capacity of the DB shard group in Aurora capacity units
        (ACUs).
        :param compute_redundancy: Specifies whether to create standby DB shard groups for the DB shard
        group.
        :param min_acu: The minimum capacity of the DB shard group in Aurora capacity units
        (ACUs).
        :param publicly_accessible: Specifies whether the DB shard group is publicly accessible.
        :param tags: A list of tags.
        :returns: DBShardGroup
        :raises DBShardGroupAlreadyExistsFault:
        :raises DBClusterNotFoundFault:
        :raises MaxDBShardGroupLimitReached:
        :raises InvalidDBClusterStateFault:
        :raises UnsupportedDBEngineVersionFault:
        :raises InvalidVPCNetworkStateFault:
        :raises NetworkTypeNotSupported:
        """
        raise NotImplementedError

    @handler("CreateDBSnapshot")
    def create_db_snapshot(
        self,
        context: RequestContext,
        db_snapshot_identifier: String,
        db_instance_identifier: String,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateDBSnapshotResult:
        """Creates a snapshot of a DB instance. The source DB instance must be in
        the ``available`` or ``storage-optimization`` state.

        :param db_snapshot_identifier: The identifier for the DB snapshot.
        :param db_instance_identifier: The identifier of the DB instance that you want to create the snapshot
        of.
        :param tags: A list of tags.
        :returns: CreateDBSnapshotResult
        :raises DBSnapshotAlreadyExistsFault:
        :raises InvalidDBInstanceStateFault:
        :raises DBInstanceNotFoundFault:
        :raises SnapshotQuotaExceededFault:
        """
        raise NotImplementedError

    @handler("CreateDBSubnetGroup")
    def create_db_subnet_group(
        self,
        context: RequestContext,
        db_subnet_group_name: String,
        db_subnet_group_description: String,
        subnet_ids: SubnetIdentifierList,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateDBSubnetGroupResult:
        """Creates a new DB subnet group. DB subnet groups must contain at least
        one subnet in at least two AZs in the Amazon Web Services Region.

        :param db_subnet_group_name: The name for the DB subnet group.
        :param db_subnet_group_description: The description for the DB subnet group.
        :param subnet_ids: The EC2 Subnet IDs for the DB subnet group.
        :param tags: Tags to assign to the DB subnet group.
        :returns: CreateDBSubnetGroupResult
        :raises DBSubnetGroupAlreadyExistsFault:
        :raises DBSubnetGroupQuotaExceededFault:
        :raises DBSubnetQuotaExceededFault:
        :raises DBSubnetGroupDoesNotCoverEnoughAZs:
        :raises InvalidSubnet:
        """
        raise NotImplementedError

    @handler("CreateEventSubscription")
    def create_event_subscription(
        self,
        context: RequestContext,
        subscription_name: String,
        sns_topic_arn: String,
        source_type: String | None = None,
        event_categories: EventCategoriesList | None = None,
        source_ids: SourceIdsList | None = None,
        enabled: BooleanOptional | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateEventSubscriptionResult:
        """Creates an RDS event notification subscription. This operation requires
        a topic Amazon Resource Name (ARN) created by either the RDS console,
        the SNS console, or the SNS API. To obtain an ARN with SNS, you must
        create a topic in Amazon SNS and subscribe to the topic. The ARN is
        displayed in the SNS console.

        You can specify the type of source (``SourceType``) that you want to be
        notified of and provide a list of RDS sources (``SourceIds``) that
        triggers the events. You can also provide a list of event categories
        (``EventCategories``) for events that you want to be notified of. For
        example, you can specify ``SourceType`` = ``db-instance``, ``SourceIds``
        = ``mydbinstance1``, ``mydbinstance2`` and ``EventCategories`` =
        ``Availability``, ``Backup``.

        If you specify both the ``SourceType`` and ``SourceIds``, such as
        ``SourceType`` = ``db-instance`` and ``SourceIds`` = ``myDBInstance1``,
        you are notified of all the ``db-instance`` events for the specified
        source. If you specify a ``SourceType`` but do not specify
        ``SourceIds``, you receive notice of the events for that source type for
        all your RDS sources. If you don't specify either the SourceType or the
        ``SourceIds``, you are notified of events generated from all RDS sources
        belonging to your customer account.

        For more information about subscribing to an event for RDS DB engines,
        see `Subscribing to Amazon RDS event
        notification <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Subscribing.html>`__
        in the *Amazon RDS User Guide*.

        For more information about subscribing to an event for Aurora DB
        engines, see `Subscribing to Amazon RDS event
        notification <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Events.Subscribing.html>`__
        in the *Amazon Aurora User Guide*.

        :param subscription_name: The name of the subscription.
        :param sns_topic_arn: The Amazon Resource Name (ARN) of the SNS topic created for event
        notification.
        :param source_type: The type of source that is generating the events.
        :param event_categories: A list of event categories for a particular source type (``SourceType``)
        that you want to subscribe to.
        :param source_ids: The list of identifiers of the event sources for which events are
        returned.
        :param enabled: Specifies whether to activate the subscription.
        :param tags: A list of tags.
        :returns: CreateEventSubscriptionResult
        :raises EventSubscriptionQuotaExceededFault:
        :raises SubscriptionAlreadyExistFault:
        :raises SNSInvalidTopicFault:
        :raises SNSNoAuthorizationFault:
        :raises SNSTopicArnNotFoundFault:
        :raises SubscriptionCategoryNotFoundFault:
        :raises SourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("CreateGlobalCluster")
    def create_global_cluster(
        self,
        context: RequestContext,
        global_cluster_identifier: String | None = None,
        source_db_cluster_identifier: String | None = None,
        engine: String | None = None,
        engine_version: String | None = None,
        engine_lifecycle_support: String | None = None,
        deletion_protection: BooleanOptional | None = None,
        database_name: String | None = None,
        storage_encrypted: BooleanOptional | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateGlobalClusterResult:
        """Creates an Aurora global database spread across multiple Amazon Web
        Services Regions. The global database contains a single primary cluster
        with read-write capability, and a read-only secondary cluster that
        receives data from the primary cluster through high-speed replication
        performed by the Aurora storage subsystem.

        You can create a global database that is initially empty, and then
        create the primary and secondary DB clusters in the global database. Or
        you can specify an existing Aurora cluster during the create operation,
        and this cluster becomes the primary cluster of the global database.

        This operation applies only to Aurora DB clusters.

        :param global_cluster_identifier: The cluster identifier for this global database cluster.
        :param source_db_cluster_identifier: The Amazon Resource Name (ARN) to use as the primary cluster of the
        global database.
        :param engine: The database engine to use for this global database cluster.
        :param engine_version: The engine version to use for this global database cluster.
        :param engine_lifecycle_support: The life cycle type for this global database cluster.
        :param deletion_protection: Specifies whether to enable deletion protection for the new global
        database cluster.
        :param database_name: The name for your database of up to 64 alphanumeric characters.
        :param storage_encrypted: Specifies whether to enable storage encryption for the new global
        database cluster.
        :param tags: Tags to assign to the global cluster.
        :returns: CreateGlobalClusterResult
        :raises GlobalClusterAlreadyExistsFault:
        :raises GlobalClusterQuotaExceededFault:
        :raises InvalidDBClusterStateFault:
        :raises DBClusterNotFoundFault:
        """
        raise NotImplementedError

    @handler("CreateIntegration")
    def create_integration(
        self,
        context: RequestContext,
        source_arn: SourceArn,
        target_arn: Arn,
        integration_name: IntegrationName,
        kms_key_id: String | None = None,
        additional_encryption_context: EncryptionContextMap | None = None,
        tags: TagList | None = None,
        data_filter: DataFilter | None = None,
        description: IntegrationDescription | None = None,
        **kwargs,
    ) -> Integration:
        """Creates a zero-ETL integration with Amazon Redshift.

        :param source_arn: The Amazon Resource Name (ARN) of the database to use as the source for
        replication.
        :param target_arn: The ARN of the Redshift data warehouse to use as the target for
        replication.
        :param integration_name: The name of the integration.
        :param kms_key_id: The Amazon Web Services Key Management System (Amazon Web Services KMS)
        key identifier for the key to use to encrypt the integration.
        :param additional_encryption_context: An optional set of non-secret key–value pairs that contains additional
        contextual information about the data.
        :param tags: A list of tags.
        :param data_filter: Data filtering options for the integration.
        :param description: A description of the integration.
        :returns: Integration
        :raises DBClusterNotFoundFault:
        :raises DBInstanceNotFoundFault:
        :raises IntegrationAlreadyExistsFault:
        :raises IntegrationQuotaExceededFault:
        :raises KMSKeyNotAccessibleFault:
        :raises IntegrationConflictOperationFault:
        """
        raise NotImplementedError

    @handler("CreateOptionGroup")
    def create_option_group(
        self,
        context: RequestContext,
        option_group_name: String,
        engine_name: String,
        major_engine_version: String,
        option_group_description: String,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateOptionGroupResult:
        """Creates a new option group. You can create up to 20 option groups.

        This command doesn't apply to RDS Custom.

        :param option_group_name: Specifies the name of the option group to be created.
        :param engine_name: The name of the engine to associate this option group with.
        :param major_engine_version: Specifies the major version of the engine that this option group should
        be associated with.
        :param option_group_description: The description of the option group.
        :param tags: Tags to assign to the option group.
        :returns: CreateOptionGroupResult
        :raises OptionGroupAlreadyExistsFault:
        :raises OptionGroupQuotaExceededFault:
        """
        raise NotImplementedError

    @handler("CreateTenantDatabase")
    def create_tenant_database(
        self,
        context: RequestContext,
        db_instance_identifier: String,
        tenant_db_name: String,
        master_username: String,
        master_user_password: SensitiveString | None = None,
        character_set_name: String | None = None,
        nchar_character_set_name: String | None = None,
        manage_master_user_password: BooleanOptional | None = None,
        master_user_secret_kms_key_id: String | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateTenantDatabaseResult:
        """Creates a tenant database in a DB instance that uses the multi-tenant
        configuration. Only RDS for Oracle container database (CDB) instances
        are supported.

        :param db_instance_identifier: The user-supplied DB instance identifier.
        :param tenant_db_name: The user-supplied name of the tenant database that you want to create in
        your DB instance.
        :param master_username: The name for the master user account in your tenant database.
        :param master_user_password: The password for the master user in your tenant database.
        :param character_set_name: The character set for your tenant database.
        :param nchar_character_set_name: The ``NCHAR`` value for the tenant database.
        :param manage_master_user_password: Specifies whether to manage the master user password with Amazon Web
        Services Secrets Manager.
        :param master_user_secret_kms_key_id: The Amazon Web Services KMS key identifier to encrypt a secret that is
        automatically generated and managed in Amazon Web Services Secrets
        Manager.
        :param tags: A list of tags.
        :returns: CreateTenantDatabaseResult
        :raises DBInstanceNotFoundFault:
        :raises InvalidDBInstanceStateFault:
        :raises TenantDatabaseAlreadyExistsFault:
        :raises TenantDatabaseQuotaExceededFault:
        :raises KMSKeyNotAccessibleFault:
        """
        raise NotImplementedError

    @handler("DeleteBlueGreenDeployment")
    def delete_blue_green_deployment(
        self,
        context: RequestContext,
        blue_green_deployment_identifier: BlueGreenDeploymentIdentifier,
        delete_target: BooleanOptional | None = None,
        **kwargs,
    ) -> DeleteBlueGreenDeploymentResponse:
        """Deletes a blue/green deployment.

        For more information, see `Using Amazon RDS Blue/Green Deployments for
        database
        updates <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html>`__
        in the *Amazon RDS User Guide* and `Using Amazon RDS Blue/Green
        Deployments for database
        updates <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html>`__
        in the *Amazon Aurora User Guide*.

        :param blue_green_deployment_identifier: The unique identifier of the blue/green deployment to delete.
        :param delete_target: Specifies whether to delete the resources in the green environment.
        :returns: DeleteBlueGreenDeploymentResponse
        :raises BlueGreenDeploymentNotFoundFault:
        :raises InvalidBlueGreenDeploymentStateFault:
        """
        raise NotImplementedError

    @handler("DeleteCustomDBEngineVersion")
    def delete_custom_db_engine_version(
        self,
        context: RequestContext,
        engine: CustomEngineName,
        engine_version: CustomEngineVersion,
        **kwargs,
    ) -> DBEngineVersion:
        """Deletes a custom engine version. To run this command, make sure you meet
        the following prerequisites:

        -  The CEV must not be the default for RDS Custom. If it is, change the
           default before running this command.

        -  The CEV must not be associated with an RDS Custom DB instance, RDS
           Custom instance snapshot, or automated backup of your RDS Custom
           instance.

        Typically, deletion takes a few minutes.

        The MediaImport service that imports files from Amazon S3 to create CEVs
        isn't integrated with Amazon Web Services CloudTrail. If you turn on
        data logging for Amazon RDS in CloudTrail, calls to the
        ``DeleteCustomDbEngineVersion`` event aren't logged. However, you might
        see calls from the API gateway that accesses your Amazon S3 bucket.
        These calls originate from the MediaImport service for the
        ``DeleteCustomDbEngineVersion`` event.

        For more information, see `Deleting a
        CEV <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev.html#custom-cev.delete>`__
        in the *Amazon RDS User Guide*.

        :param engine: The database engine.
        :param engine_version: The custom engine version (CEV) for your DB instance.
        :returns: DBEngineVersion
        :raises CustomDBEngineVersionNotFoundFault:
        :raises InvalidCustomDBEngineVersionStateFault:
        """
        raise NotImplementedError

    @handler("DeleteDBCluster")
    def delete_db_cluster(
        self,
        context: RequestContext,
        db_cluster_identifier: String,
        skip_final_snapshot: Boolean | None = None,
        final_db_snapshot_identifier: String | None = None,
        delete_automated_backups: BooleanOptional | None = None,
        **kwargs,
    ) -> DeleteDBClusterResult:
        """The DeleteDBCluster action deletes a previously provisioned DB cluster.
        When you delete a DB cluster, all automated backups for that DB cluster
        are deleted and can't be recovered. Manual DB cluster snapshots of the
        specified DB cluster are not deleted.

        If you're deleting a Multi-AZ DB cluster with read replicas, all cluster
        members are terminated and read replicas are promoted to standalone
        instances.

        For more information on Amazon Aurora, see `What is Amazon
        Aurora? <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html>`__
        in the *Amazon Aurora User Guide*.

        For more information on Multi-AZ DB clusters, see `Multi-AZ DB cluster
        deployments <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html>`__
        in the *Amazon RDS User Guide*.

        :param db_cluster_identifier: The DB cluster identifier for the DB cluster to be deleted.
        :param skip_final_snapshot: Specifies whether to skip the creation of a final DB cluster snapshot
        before RDS deletes the DB cluster.
        :param final_db_snapshot_identifier: The DB cluster snapshot identifier of the new DB cluster snapshot
        created when ``SkipFinalSnapshot`` is disabled.
        :param delete_automated_backups: Specifies whether to remove automated backups immediately after the DB
        cluster is deleted.
        :returns: DeleteDBClusterResult
        :raises DBClusterNotFoundFault:
        :raises InvalidDBClusterStateFault:
        :raises DBClusterSnapshotAlreadyExistsFault:
        :raises SnapshotQuotaExceededFault:
        :raises InvalidDBClusterSnapshotStateFault:
        :raises DBClusterAutomatedBackupQuotaExceededFault:
        """
        raise NotImplementedError

    @handler("DeleteDBClusterAutomatedBackup")
    def delete_db_cluster_automated_backup(
        self, context: RequestContext, db_cluster_resource_id: String, **kwargs
    ) -> DeleteDBClusterAutomatedBackupResult:
        """Deletes automated backups using the ``DbClusterResourceId`` value of the
        source DB cluster or the Amazon Resource Name (ARN) of the automated
        backups.

        :param db_cluster_resource_id: The identifier for the source DB cluster, which can't be changed and
        which is unique to an Amazon Web Services Region.
        :returns: DeleteDBClusterAutomatedBackupResult
        :raises InvalidDBClusterAutomatedBackupStateFault:
        :raises DBClusterAutomatedBackupNotFoundFault:
        """
        raise NotImplementedError

    @handler("DeleteDBClusterEndpoint")
    def delete_db_cluster_endpoint(
        self, context: RequestContext, db_cluster_endpoint_identifier: String, **kwargs
    ) -> DBClusterEndpoint:
        """Deletes a custom endpoint and removes it from an Amazon Aurora DB
        cluster.

        This action only applies to Aurora DB clusters.

        :param db_cluster_endpoint_identifier: The identifier associated with the custom endpoint.
        :returns: DBClusterEndpoint
        :raises InvalidDBClusterEndpointStateFault:
        :raises DBClusterEndpointNotFoundFault:
        :raises InvalidDBClusterStateFault:
        """
        raise NotImplementedError

    @handler("DeleteDBClusterParameterGroup")
    def delete_db_cluster_parameter_group(
        self, context: RequestContext, db_cluster_parameter_group_name: String, **kwargs
    ) -> None:
        """Deletes a specified DB cluster parameter group. The DB cluster parameter
        group to be deleted can't be associated with any DB clusters.

        For more information on Amazon Aurora, see `What is Amazon
        Aurora? <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html>`__
        in the *Amazon Aurora User Guide*.

        For more information on Multi-AZ DB clusters, see `Multi-AZ DB cluster
        deployments <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html>`__
        in the *Amazon RDS User Guide*.

        :param db_cluster_parameter_group_name: The name of the DB cluster parameter group.
        :raises InvalidDBParameterGroupStateFault:
        :raises DBParameterGroupNotFoundFault:
        """
        raise NotImplementedError

    @handler("DeleteDBClusterSnapshot")
    def delete_db_cluster_snapshot(
        self, context: RequestContext, db_cluster_snapshot_identifier: String, **kwargs
    ) -> DeleteDBClusterSnapshotResult:
        """Deletes a DB cluster snapshot. If the snapshot is being copied, the copy
        operation is terminated.

        The DB cluster snapshot must be in the ``available`` state to be
        deleted.

        For more information on Amazon Aurora, see `What is Amazon
        Aurora? <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html>`__
        in the *Amazon Aurora User Guide*.

        For more information on Multi-AZ DB clusters, see `Multi-AZ DB cluster
        deployments <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html>`__
        in the *Amazon RDS User Guide*.

        :param db_cluster_snapshot_identifier: The identifier of the DB cluster snapshot to delete.
        :returns: DeleteDBClusterSnapshotResult
        :raises InvalidDBClusterSnapshotStateFault:
        :raises DBClusterSnapshotNotFoundFault:
        """
        raise NotImplementedError

    @handler("DeleteDBInstance")
    def delete_db_instance(
        self,
        context: RequestContext,
        db_instance_identifier: String,
        skip_final_snapshot: Boolean | None = None,
        final_db_snapshot_identifier: String | None = None,
        delete_automated_backups: BooleanOptional | None = None,
        **kwargs,
    ) -> DeleteDBInstanceResult:
        """Deletes a previously provisioned DB instance. When you delete a DB
        instance, all automated backups for that instance are deleted and can't
        be recovered. However, manual DB snapshots of the DB instance aren't
        deleted.

        If you request a final DB snapshot, the status of the Amazon RDS DB
        instance is ``deleting`` until the DB snapshot is created. This
        operation can't be canceled or reverted after it begins. To monitor the
        status of this operation, use ``DescribeDBInstance``.

        When a DB instance is in a failure state and has a status of ``failed``,
        ``incompatible-restore``, or ``incompatible-network``, you can only
        delete it when you skip creation of the final snapshot with the
        ``SkipFinalSnapshot`` parameter.

        If the specified DB instance is part of an Amazon Aurora DB cluster, you
        can't delete the DB instance if both of the following conditions are
        true:

        -  The DB cluster is a read replica of another Amazon Aurora DB cluster.

        -  The DB instance is the only instance in the DB cluster.

        To delete a DB instance in this case, first use the
        ``PromoteReadReplicaDBCluster`` operation to promote the DB cluster so
        that it's no longer a read replica. After the promotion completes, use
        the ``DeleteDBInstance`` operation to delete the final instance in the
        DB cluster.

        For RDS Custom DB instances, deleting the DB instance permanently
        deletes the EC2 instance and the associated EBS volumes. Make sure that
        you don't terminate or delete these resources before you delete the DB
        instance. Otherwise, deleting the DB instance and creation of the final
        snapshot might fail.

        :param db_instance_identifier: The DB instance identifier for the DB instance to be deleted.
        :param skip_final_snapshot: Specifies whether to skip the creation of a final DB snapshot before
        deleting the instance.
        :param final_db_snapshot_identifier: The ``DBSnapshotIdentifier`` of the new ``DBSnapshot`` created when the
        ``SkipFinalSnapshot`` parameter is disabled.
        :param delete_automated_backups: Specifies whether to remove automated backups immediately after the DB
        instance is deleted.
        :returns: DeleteDBInstanceResult
        :raises DBInstanceNotFoundFault:
        :raises InvalidDBInstanceStateFault:
        :raises DBSnapshotAlreadyExistsFault:
        :raises SnapshotQuotaExceededFault:
        :raises InvalidDBClusterStateFault:
        :raises DBInstanceAutomatedBackupQuotaExceededFault:
        """
        raise NotImplementedError

    @handler("DeleteDBInstanceAutomatedBackup")
    def delete_db_instance_automated_backup(
        self,
        context: RequestContext,
        dbi_resource_id: String | None = None,
        db_instance_automated_backups_arn: String | None = None,
        **kwargs,
    ) -> DeleteDBInstanceAutomatedBackupResult:
        """Deletes automated backups using the ``DbiResourceId`` value of the
        source DB instance or the Amazon Resource Name (ARN) of the automated
        backups.

        :param dbi_resource_id: The identifier for the source DB instance, which can't be changed and
        which is unique to an Amazon Web Services Region.
        :param db_instance_automated_backups_arn: The Amazon Resource Name (ARN) of the automated backups to delete, for
        example,
        ``arn:aws:rds:us-east-1:123456789012:auto-backup:ab-L2IJCEXJP7XQ7HOJ4SIEXAMPLE``.
        :returns: DeleteDBInstanceAutomatedBackupResult
        :raises InvalidDBInstanceAutomatedBackupStateFault:
        :raises DBInstanceAutomatedBackupNotFoundFault:
        """
        raise NotImplementedError

    @handler("DeleteDBParameterGroup")
    def delete_db_parameter_group(
        self, context: RequestContext, db_parameter_group_name: String, **kwargs
    ) -> None:
        """Deletes a specified DB parameter group. The DB parameter group to be
        deleted can't be associated with any DB instances.

        :param db_parameter_group_name: The name of the DB parameter group.
        :raises InvalidDBParameterGroupStateFault:
        :raises DBParameterGroupNotFoundFault:
        """
        raise NotImplementedError

    @handler("DeleteDBProxy")
    def delete_db_proxy(
        self, context: RequestContext, db_proxy_name: String, **kwargs
    ) -> DeleteDBProxyResponse:
        """Deletes an existing DB proxy.

        :param db_proxy_name: The name of the DB proxy to delete.
        :returns: DeleteDBProxyResponse
        :raises DBProxyNotFoundFault:
        :raises InvalidDBProxyStateFault:
        """
        raise NotImplementedError

    @handler("DeleteDBProxyEndpoint")
    def delete_db_proxy_endpoint(
        self, context: RequestContext, db_proxy_endpoint_name: DBProxyEndpointName, **kwargs
    ) -> DeleteDBProxyEndpointResponse:
        """Deletes a ``DBProxyEndpoint``. Doing so removes the ability to access
        the DB proxy using the endpoint that you defined. The endpoint that you
        delete might have provided capabilities such as read/write or read-only
        operations, or using a different VPC than the DB proxy's default VPC.

        :param db_proxy_endpoint_name: The name of the DB proxy endpoint to delete.
        :returns: DeleteDBProxyEndpointResponse
        :raises DBProxyEndpointNotFoundFault:
        :raises InvalidDBProxyEndpointStateFault:
        """
        raise NotImplementedError

    @handler("DeleteDBSecurityGroup")
    def delete_db_security_group(
        self, context: RequestContext, db_security_group_name: String, **kwargs
    ) -> None:
        """Deletes a DB security group.

        The specified DB security group must not be associated with any DB
        instances.

        EC2-Classic was retired on August 15, 2022. If you haven't migrated from
        EC2-Classic to a VPC, we recommend that you migrate as soon as possible.
        For more information, see `Migrate from EC2-Classic to a
        VPC <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-migrate.html>`__
        in the *Amazon EC2 User Guide*, the blog `EC2-Classic Networking is
        Retiring – Here’s How to
        Prepare <http://aws.amazon.com/blogs/aws/ec2-classic-is-retiring-heres-how-to-prepare/>`__,
        and `Moving a DB instance not in a VPC into a
        VPC <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Non-VPC2VPC.html>`__
        in the *Amazon RDS User Guide*.

        :param db_security_group_name: The name of the DB security group to delete.
        :raises InvalidDBSecurityGroupStateFault:
        :raises DBSecurityGroupNotFoundFault:
        """
        raise NotImplementedError

    @handler("DeleteDBShardGroup")
    def delete_db_shard_group(
        self, context: RequestContext, db_shard_group_identifier: DBShardGroupIdentifier, **kwargs
    ) -> DBShardGroup:
        """Deletes an Aurora Limitless Database DB shard group.

        :param db_shard_group_identifier: The name of the DB shard group to delete.
        :returns: DBShardGroup
        :raises DBShardGroupNotFoundFault:
        :raises InvalidDBShardGroupStateFault:
        :raises InvalidDBClusterStateFault:
        """
        raise NotImplementedError

    @handler("DeleteDBSnapshot")
    def delete_db_snapshot(
        self, context: RequestContext, db_snapshot_identifier: String, **kwargs
    ) -> DeleteDBSnapshotResult:
        """Deletes a DB snapshot. If the snapshot is being copied, the copy
        operation is terminated.

        The DB snapshot must be in the ``available`` state to be deleted.

        :param db_snapshot_identifier: The DB snapshot identifier.
        :returns: DeleteDBSnapshotResult
        :raises InvalidDBSnapshotStateFault:
        :raises DBSnapshotNotFoundFault:
        """
        raise NotImplementedError

    @handler("DeleteDBSubnetGroup")
    def delete_db_subnet_group(
        self, context: RequestContext, db_subnet_group_name: String, **kwargs
    ) -> None:
        """Deletes a DB subnet group.

        The specified database subnet group must not be associated with any DB
        instances.

        :param db_subnet_group_name: The name of the database subnet group to delete.
        :raises InvalidDBSubnetGroupStateFault:
        :raises InvalidDBSubnetStateFault:
        :raises DBSubnetGroupNotFoundFault:
        """
        raise NotImplementedError

    @handler("DeleteEventSubscription")
    def delete_event_subscription(
        self, context: RequestContext, subscription_name: String, **kwargs
    ) -> DeleteEventSubscriptionResult:
        """Deletes an RDS event notification subscription.

        :param subscription_name: The name of the RDS event notification subscription you want to delete.
        :returns: DeleteEventSubscriptionResult
        :raises SubscriptionNotFoundFault:
        :raises InvalidEventSubscriptionStateFault:
        """
        raise NotImplementedError

    @handler("DeleteGlobalCluster")
    def delete_global_cluster(
        self, context: RequestContext, global_cluster_identifier: String, **kwargs
    ) -> DeleteGlobalClusterResult:
        """Deletes a global database cluster. The primary and secondary clusters
        must already be detached or destroyed first.

        This action only applies to Aurora DB clusters.

        :param global_cluster_identifier: The cluster identifier of the global database cluster being deleted.
        :returns: DeleteGlobalClusterResult
        :raises GlobalClusterNotFoundFault:
        :raises InvalidGlobalClusterStateFault:
        """
        raise NotImplementedError

    @handler("DeleteIntegration")
    def delete_integration(
        self, context: RequestContext, integration_identifier: IntegrationIdentifier, **kwargs
    ) -> Integration:
        """Deletes a zero-ETL integration with Amazon Redshift.

        :param integration_identifier: The unique identifier of the integration.
        :returns: Integration
        :raises IntegrationNotFoundFault:
        :raises IntegrationConflictOperationFault:
        :raises InvalidIntegrationStateFault:
        """
        raise NotImplementedError

    @handler("DeleteOptionGroup")
    def delete_option_group(
        self, context: RequestContext, option_group_name: String, **kwargs
    ) -> None:
        """Deletes an existing option group.

        :param option_group_name: The name of the option group to be deleted.
        :raises OptionGroupNotFoundFault:
        :raises InvalidOptionGroupStateFault:
        """
        raise NotImplementedError

    @handler("DeleteTenantDatabase")
    def delete_tenant_database(
        self,
        context: RequestContext,
        db_instance_identifier: String,
        tenant_db_name: String,
        skip_final_snapshot: Boolean | None = None,
        final_db_snapshot_identifier: String | None = None,
        **kwargs,
    ) -> DeleteTenantDatabaseResult:
        """Deletes a tenant database from your DB instance. This command only
        applies to RDS for Oracle container database (CDB) instances.

        You can't delete a tenant database when it is the only tenant in the DB
        instance.

        :param db_instance_identifier: The user-supplied identifier for the DB instance that contains the
        tenant database that you want to delete.
        :param tenant_db_name: The user-supplied name of the tenant database that you want to remove
        from your DB instance.
        :param skip_final_snapshot: Specifies whether to skip the creation of a final DB snapshot before
        removing the tenant database from your DB instance.
        :param final_db_snapshot_identifier: The ``DBSnapshotIdentifier`` of the new ``DBSnapshot`` created when the
        ``SkipFinalSnapshot`` parameter is disabled.
        :returns: DeleteTenantDatabaseResult
        :raises DBInstanceNotFoundFault:
        :raises TenantDatabaseNotFoundFault:
        :raises InvalidDBInstanceStateFault:
        """
        raise NotImplementedError

    @handler("DeregisterDBProxyTargets")
    def deregister_db_proxy_targets(
        self,
        context: RequestContext,
        db_proxy_name: String,
        target_group_name: String | None = None,
        db_instance_identifiers: StringList | None = None,
        db_cluster_identifiers: StringList | None = None,
        **kwargs,
    ) -> DeregisterDBProxyTargetsResponse:
        """Remove the association between one or more ``DBProxyTarget`` data
        structures and a ``DBProxyTargetGroup``.

        :param db_proxy_name: The identifier of the ``DBProxy`` that is associated with the
        ``DBProxyTargetGroup``.
        :param target_group_name: The identifier of the ``DBProxyTargetGroup``.
        :param db_instance_identifiers: One or more DB instance identifiers.
        :param db_cluster_identifiers: One or more DB cluster identifiers.
        :returns: DeregisterDBProxyTargetsResponse
        :raises DBProxyTargetNotFoundFault:
        :raises DBProxyTargetGroupNotFoundFault:
        :raises DBProxyNotFoundFault:
        :raises InvalidDBProxyStateFault:
        """
        raise NotImplementedError

    @handler("DescribeAccountAttributes")
    def describe_account_attributes(
        self, context: RequestContext, **kwargs
    ) -> AccountAttributesMessage:
        """Lists all of the attributes for a customer account. The attributes
        include Amazon RDS quotas for the account, such as the number of DB
        instances allowed. The description for a quota includes the quota name,
        current usage toward that quota, and the quota's maximum value.

        This command doesn't take any parameters.

        :returns: AccountAttributesMessage
        """
        raise NotImplementedError

    @handler("DescribeBlueGreenDeployments")
    def describe_blue_green_deployments(
        self,
        context: RequestContext,
        blue_green_deployment_identifier: BlueGreenDeploymentIdentifier | None = None,
        filters: FilterList | None = None,
        marker: String | None = None,
        max_records: MaxRecords | None = None,
        **kwargs,
    ) -> DescribeBlueGreenDeploymentsResponse:
        """Describes one or more blue/green deployments.

        For more information, see `Using Amazon RDS Blue/Green Deployments for
        database
        updates <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html>`__
        in the *Amazon RDS User Guide* and `Using Amazon RDS Blue/Green
        Deployments for database
        updates <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html>`__
        in the *Amazon Aurora User Guide*.

        :param blue_green_deployment_identifier: The blue/green deployment identifier.
        :param filters: A filter that specifies one or more blue/green deployments to describe.
        :param marker: An optional pagination token provided by a previous
        ``DescribeBlueGreenDeployments`` request.
        :param max_records: The maximum number of records to include in the response.
        :returns: DescribeBlueGreenDeploymentsResponse
        :raises BlueGreenDeploymentNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeCertificates")
    def describe_certificates(
        self,
        context: RequestContext,
        certificate_identifier: String | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> CertificateMessage:
        """Lists the set of certificate authority (CA) certificates provided by
        Amazon RDS for this Amazon Web Services account.

        For more information, see `Using SSL/TLS to encrypt a connection to a DB
        instance <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html>`__
        in the *Amazon RDS User Guide* and `Using SSL/TLS to encrypt a
        connection to a DB
        cluster <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html>`__
        in the *Amazon Aurora User Guide*.

        :param certificate_identifier: The user-supplied certificate identifier.
        :param filters: This parameter isn't currently supported.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous
        ``DescribeCertificates`` request.
        :returns: CertificateMessage
        :raises CertificateNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeDBClusterAutomatedBackups")
    def describe_db_cluster_automated_backups(
        self,
        context: RequestContext,
        db_cluster_resource_id: String | None = None,
        db_cluster_identifier: String | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DBClusterAutomatedBackupMessage:
        """Displays backups for both current and deleted DB clusters. For example,
        use this operation to find details about automated backups for
        previously deleted clusters. Current clusters are returned for both the
        ``DescribeDBClusterAutomatedBackups`` and ``DescribeDBClusters``
        operations.

        All parameters are optional.

        :param db_cluster_resource_id: The resource ID of the DB cluster that is the source of the automated
        backup.
        :param db_cluster_identifier: (Optional) The user-supplied DB cluster identifier.
        :param filters: A filter that specifies which resources to return based on status.
        :param max_records: The maximum number of records to include in the response.
        :param marker: The pagination token provided in the previous request.
        :returns: DBClusterAutomatedBackupMessage
        :raises DBClusterAutomatedBackupNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeDBClusterBacktracks")
    def describe_db_cluster_backtracks(
        self,
        context: RequestContext,
        db_cluster_identifier: String,
        backtrack_identifier: String | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DBClusterBacktrackMessage:
        """Returns information about backtracks for a DB cluster.

        For more information on Amazon Aurora, see `What is Amazon
        Aurora? <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html>`__
        in the *Amazon Aurora User Guide*.

        This action only applies to Aurora MySQL DB clusters.

        :param db_cluster_identifier: The DB cluster identifier of the DB cluster to be described.
        :param backtrack_identifier: If specified, this value is the backtrack identifier of the backtrack to
        be described.
        :param filters: A filter that specifies one or more DB clusters to describe.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous
        ``DescribeDBClusterBacktracks`` request.
        :returns: DBClusterBacktrackMessage
        :raises DBClusterNotFoundFault:
        :raises DBClusterBacktrackNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeDBClusterEndpoints")
    def describe_db_cluster_endpoints(
        self,
        context: RequestContext,
        db_cluster_identifier: String | None = None,
        db_cluster_endpoint_identifier: String | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DBClusterEndpointMessage:
        """Returns information about endpoints for an Amazon Aurora DB cluster.

        This action only applies to Aurora DB clusters.

        :param db_cluster_identifier: The DB cluster identifier of the DB cluster associated with the
        endpoint.
        :param db_cluster_endpoint_identifier: The identifier of the endpoint to describe.
        :param filters: A set of name-value pairs that define which endpoints to include in the
        output.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous
        ``DescribeDBClusterEndpoints`` request.
        :returns: DBClusterEndpointMessage
        :raises DBClusterNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeDBClusterParameterGroups")
    def describe_db_cluster_parameter_groups(
        self,
        context: RequestContext,
        db_cluster_parameter_group_name: String | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DBClusterParameterGroupsMessage:
        """Returns a list of ``DBClusterParameterGroup`` descriptions. If a
        ``DBClusterParameterGroupName`` parameter is specified, the list will
        contain only the description of the specified DB cluster parameter
        group.

        For more information on Amazon Aurora, see `What is Amazon
        Aurora? <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html>`__
        in the *Amazon Aurora User Guide*.

        For more information on Multi-AZ DB clusters, see `Multi-AZ DB cluster
        deployments <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html>`__
        in the *Amazon RDS User Guide*.

        :param db_cluster_parameter_group_name: The name of a specific DB cluster parameter group to return details for.
        :param filters: This parameter isn't currently supported.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous
        ``DescribeDBClusterParameterGroups`` request.
        :returns: DBClusterParameterGroupsMessage
        :raises DBParameterGroupNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeDBClusterParameters")
    def describe_db_cluster_parameters(
        self,
        context: RequestContext,
        db_cluster_parameter_group_name: String,
        source: String | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DBClusterParameterGroupDetails:
        """Returns the detailed parameter list for a particular DB cluster
        parameter group.

        For more information on Amazon Aurora, see `What is Amazon
        Aurora? <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html>`__
        in the *Amazon Aurora User Guide*.

        For more information on Multi-AZ DB clusters, see `Multi-AZ DB cluster
        deployments <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html>`__
        in the *Amazon RDS User Guide*.

        :param db_cluster_parameter_group_name: The name of a specific DB cluster parameter group to return parameter
        details for.
        :param source: A specific source to return parameters for.
        :param filters: A filter that specifies one or more DB cluster parameters to describe.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous
        ``DescribeDBClusterParameters`` request.
        :returns: DBClusterParameterGroupDetails
        :raises DBParameterGroupNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeDBClusterSnapshotAttributes")
    def describe_db_cluster_snapshot_attributes(
        self, context: RequestContext, db_cluster_snapshot_identifier: String, **kwargs
    ) -> DescribeDBClusterSnapshotAttributesResult:
        """Returns a list of DB cluster snapshot attribute names and values for a
        manual DB cluster snapshot.

        When sharing snapshots with other Amazon Web Services accounts,
        ``DescribeDBClusterSnapshotAttributes`` returns the ``restore``
        attribute and a list of IDs for the Amazon Web Services accounts that
        are authorized to copy or restore the manual DB cluster snapshot. If
        ``all`` is included in the list of values for the ``restore`` attribute,
        then the manual DB cluster snapshot is public and can be copied or
        restored by all Amazon Web Services accounts.

        To add or remove access for an Amazon Web Services account to copy or
        restore a manual DB cluster snapshot, or to make the manual DB cluster
        snapshot public or private, use the ``ModifyDBClusterSnapshotAttribute``
        API action.

        :param db_cluster_snapshot_identifier: The identifier for the DB cluster snapshot to describe the attributes
        for.
        :returns: DescribeDBClusterSnapshotAttributesResult
        :raises DBClusterSnapshotNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeDBClusterSnapshots")
    def describe_db_cluster_snapshots(
        self,
        context: RequestContext,
        db_cluster_identifier: String | None = None,
        db_cluster_snapshot_identifier: String | None = None,
        snapshot_type: String | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        include_shared: Boolean | None = None,
        include_public: Boolean | None = None,
        db_cluster_resource_id: String | None = None,
        **kwargs,
    ) -> DBClusterSnapshotMessage:
        """Returns information about DB cluster snapshots. This API action supports
        pagination.

        For more information on Amazon Aurora DB clusters, see `What is Amazon
        Aurora? <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html>`__
        in the *Amazon Aurora User Guide*.

        For more information on Multi-AZ DB clusters, see `Multi-AZ DB cluster
        deployments <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html>`__
        in the *Amazon RDS User Guide*.

        :param db_cluster_identifier: The ID of the DB cluster to retrieve the list of DB cluster snapshots
        for.
        :param db_cluster_snapshot_identifier: A specific DB cluster snapshot identifier to describe.
        :param snapshot_type: The type of DB cluster snapshots to be returned.
        :param filters: A filter that specifies one or more DB cluster snapshots to describe.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous
        ``DescribeDBClusterSnapshots`` request.
        :param include_shared: Specifies whether to include shared manual DB cluster snapshots from
        other Amazon Web Services accounts that this Amazon Web Services account
        has been given permission to copy or restore.
        :param include_public: Specifies whether to include manual DB cluster snapshots that are public
        and can be copied or restored by any Amazon Web Services account.
        :param db_cluster_resource_id: A specific DB cluster resource ID to describe.
        :returns: DBClusterSnapshotMessage
        :raises DBClusterSnapshotNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeDBClusters")
    def describe_db_clusters(
        self,
        context: RequestContext,
        db_cluster_identifier: String | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        include_shared: Boolean | None = None,
        **kwargs,
    ) -> DBClusterMessage:
        """Describes existing Amazon Aurora DB clusters and Multi-AZ DB clusters.
        This API supports pagination.

        For more information on Amazon Aurora DB clusters, see `What is Amazon
        Aurora? <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html>`__
        in the *Amazon Aurora User Guide*.

        For more information on Multi-AZ DB clusters, see `Multi-AZ DB cluster
        deployments <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html>`__
        in the *Amazon RDS User Guide*.

        This operation can also return information for Amazon Neptune DB
        instances and Amazon DocumentDB instances.

        :param db_cluster_identifier: The user-supplied DB cluster identifier or the Amazon Resource Name
        (ARN) of the DB cluster.
        :param filters: A filter that specifies one or more DB clusters to describe.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous
        ``DescribeDBClusters`` request.
        :param include_shared: Specifies whether the output includes information about clusters shared
        from other Amazon Web Services accounts.
        :returns: DBClusterMessage
        :raises DBClusterNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeDBEngineVersions")
    def describe_db_engine_versions(
        self,
        context: RequestContext,
        engine: String | None = None,
        engine_version: String | None = None,
        db_parameter_group_family: String | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        default_only: Boolean | None = None,
        list_supported_character_sets: BooleanOptional | None = None,
        list_supported_timezones: BooleanOptional | None = None,
        include_all: BooleanOptional | None = None,
        **kwargs,
    ) -> DBEngineVersionMessage:
        """Describes the properties of specific versions of DB engines.

        :param engine: The database engine to return version details for.
        :param engine_version: A specific database engine version to return details for.
        :param db_parameter_group_family: The name of a specific DB parameter group family to return details for.
        :param filters: A filter that specifies one or more DB engine versions to describe.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous request.
        :param default_only: Specifies whether to return only the default version of the specified
        engine or the engine and major version combination.
        :param list_supported_character_sets: Specifies whether to list the supported character sets for each engine
        version.
        :param list_supported_timezones: Specifies whether to list the supported time zones for each engine
        version.
        :param include_all: Specifies whether to also list the engine versions that aren't
        available.
        :returns: DBEngineVersionMessage
        """
        raise NotImplementedError

    @handler("DescribeDBInstanceAutomatedBackups")
    def describe_db_instance_automated_backups(
        self,
        context: RequestContext,
        dbi_resource_id: String | None = None,
        db_instance_identifier: String | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        db_instance_automated_backups_arn: String | None = None,
        **kwargs,
    ) -> DBInstanceAutomatedBackupMessage:
        """Displays backups for both current and deleted instances. For example,
        use this operation to find details about automated backups for
        previously deleted instances. Current instances with retention periods
        greater than zero (0) are returned for both the
        ``DescribeDBInstanceAutomatedBackups`` and ``DescribeDBInstances``
        operations.

        All parameters are optional.

        :param dbi_resource_id: The resource ID of the DB instance that is the source of the automated
        backup.
        :param db_instance_identifier: (Optional) The user-supplied instance identifier.
        :param filters: A filter that specifies which resources to return based on status.
        :param max_records: The maximum number of records to include in the response.
        :param marker: The pagination token provided in the previous request.
        :param db_instance_automated_backups_arn: The Amazon Resource Name (ARN) of the replicated automated backups, for
        example,
        ``arn:aws:rds:us-east-1:123456789012:auto-backup:ab-L2IJCEXJP7XQ7HOJ4SIEXAMPLE``.
        :returns: DBInstanceAutomatedBackupMessage
        :raises DBInstanceAutomatedBackupNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeDBInstances")
    def describe_db_instances(
        self,
        context: RequestContext,
        db_instance_identifier: String | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DBInstanceMessage:
        """Describes provisioned RDS instances. This API supports pagination.

        This operation can also return information for Amazon Neptune DB
        instances and Amazon DocumentDB instances.

        :param db_instance_identifier: The user-supplied instance identifier or the Amazon Resource Name (ARN)
        of the DB instance.
        :param filters: A filter that specifies one or more DB instances to describe.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous
        ``DescribeDBInstances`` request.
        :returns: DBInstanceMessage
        :raises DBInstanceNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeDBLogFiles")
    def describe_db_log_files(
        self,
        context: RequestContext,
        db_instance_identifier: String,
        filename_contains: String | None = None,
        file_last_written: Long | None = None,
        file_size: Long | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DescribeDBLogFilesResponse:
        """Returns a list of DB log files for the DB instance.

        This command doesn't apply to RDS Custom.

        :param db_instance_identifier: The customer-assigned name of the DB instance that contains the log
        files you want to list.
        :param filename_contains: Filters the available log files for log file names that contain the
        specified string.
        :param file_last_written: Filters the available log files for files written since the specified
        date, in POSIX timestamp format with milliseconds.
        :param file_size: Filters the available log files for files larger than the specified
        size.
        :param filters: This parameter isn't currently supported.
        :param max_records: The maximum number of records to include in the response.
        :param marker: The pagination token provided in the previous request.
        :returns: DescribeDBLogFilesResponse
        :raises DBInstanceNotFoundFault:
        :raises DBInstanceNotReadyFault:
        """
        raise NotImplementedError

    @handler("DescribeDBMajorEngineVersions")
    def describe_db_major_engine_versions(
        self,
        context: RequestContext,
        engine: Engine | None = None,
        major_engine_version: MajorEngineVersion | None = None,
        marker: Marker | None = None,
        max_records: MaxRecords | None = None,
        **kwargs,
    ) -> DescribeDBMajorEngineVersionsResponse:
        """Describes the properties of specific major versions of DB engines.

        :param engine: The database engine to return major version details for.
        :param major_engine_version: A specific database major engine version to return details for.
        :param marker: An optional pagination token provided by a previous request.
        :param max_records: The maximum number of records to include in the response.
        :returns: DescribeDBMajorEngineVersionsResponse
        """
        raise NotImplementedError

    @handler("DescribeDBParameterGroups")
    def describe_db_parameter_groups(
        self,
        context: RequestContext,
        db_parameter_group_name: String | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DBParameterGroupsMessage:
        """Returns a list of ``DBParameterGroup`` descriptions. If a
        ``DBParameterGroupName`` is specified, the list will contain only the
        description of the specified DB parameter group.

        :param db_parameter_group_name: The name of a specific DB parameter group to return details for.
        :param filters: This parameter isn't currently supported.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous
        ``DescribeDBParameterGroups`` request.
        :returns: DBParameterGroupsMessage
        :raises DBParameterGroupNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeDBParameters")
    def describe_db_parameters(
        self,
        context: RequestContext,
        db_parameter_group_name: String,
        source: String | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DBParameterGroupDetails:
        """Returns the detailed parameter list for a particular DB parameter group.

        :param db_parameter_group_name: The name of a specific DB parameter group to return details for.
        :param source: The parameter types to return.
        :param filters: A filter that specifies one or more DB parameters to describe.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous
        ``DescribeDBParameters`` request.
        :returns: DBParameterGroupDetails
        :raises DBParameterGroupNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeDBProxies")
    def describe_db_proxies(
        self,
        context: RequestContext,
        db_proxy_name: String | None = None,
        filters: FilterList | None = None,
        marker: String | None = None,
        max_records: MaxRecords | None = None,
        **kwargs,
    ) -> DescribeDBProxiesResponse:
        """Returns information about DB proxies.

        :param db_proxy_name: The name of the DB proxy.
        :param filters: This parameter is not currently supported.
        :param marker: An optional pagination token provided by a previous request.
        :param max_records: The maximum number of records to include in the response.
        :returns: DescribeDBProxiesResponse
        :raises DBProxyNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeDBProxyEndpoints")
    def describe_db_proxy_endpoints(
        self,
        context: RequestContext,
        db_proxy_name: DBProxyName | None = None,
        db_proxy_endpoint_name: DBProxyEndpointName | None = None,
        filters: FilterList | None = None,
        marker: String | None = None,
        max_records: MaxRecords | None = None,
        **kwargs,
    ) -> DescribeDBProxyEndpointsResponse:
        """Returns information about DB proxy endpoints.

        :param db_proxy_name: The name of the DB proxy whose endpoints you want to describe.
        :param db_proxy_endpoint_name: The name of a DB proxy endpoint to describe.
        :param filters: This parameter is not currently supported.
        :param marker: An optional pagination token provided by a previous request.
        :param max_records: The maximum number of records to include in the response.
        :returns: DescribeDBProxyEndpointsResponse
        :raises DBProxyNotFoundFault:
        :raises DBProxyEndpointNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeDBProxyTargetGroups")
    def describe_db_proxy_target_groups(
        self,
        context: RequestContext,
        db_proxy_name: String,
        target_group_name: String | None = None,
        filters: FilterList | None = None,
        marker: String | None = None,
        max_records: MaxRecords | None = None,
        **kwargs,
    ) -> DescribeDBProxyTargetGroupsResponse:
        """Returns information about DB proxy target groups, represented by
        ``DBProxyTargetGroup`` data structures.

        :param db_proxy_name: The identifier of the ``DBProxy`` associated with the target group.
        :param target_group_name: The identifier of the ``DBProxyTargetGroup`` to describe.
        :param filters: This parameter is not currently supported.
        :param marker: An optional pagination token provided by a previous request.
        :param max_records: The maximum number of records to include in the response.
        :returns: DescribeDBProxyTargetGroupsResponse
        :raises DBProxyNotFoundFault:
        :raises DBProxyTargetGroupNotFoundFault:
        :raises InvalidDBProxyStateFault:
        """
        raise NotImplementedError

    @handler("DescribeDBProxyTargets")
    def describe_db_proxy_targets(
        self,
        context: RequestContext,
        db_proxy_name: String,
        target_group_name: String | None = None,
        filters: FilterList | None = None,
        marker: String | None = None,
        max_records: MaxRecords | None = None,
        **kwargs,
    ) -> DescribeDBProxyTargetsResponse:
        """Returns information about ``DBProxyTarget`` objects. This API supports
        pagination.

        :param db_proxy_name: The identifier of the ``DBProxyTarget`` to describe.
        :param target_group_name: The identifier of the ``DBProxyTargetGroup`` to describe.
        :param filters: This parameter is not currently supported.
        :param marker: An optional pagination token provided by a previous request.
        :param max_records: The maximum number of records to include in the response.
        :returns: DescribeDBProxyTargetsResponse
        :raises DBProxyNotFoundFault:
        :raises DBProxyTargetNotFoundFault:
        :raises DBProxyTargetGroupNotFoundFault:
        :raises InvalidDBProxyStateFault:
        """
        raise NotImplementedError

    @handler("DescribeDBRecommendations")
    def describe_db_recommendations(
        self,
        context: RequestContext,
        last_updated_after: TStamp | None = None,
        last_updated_before: TStamp | None = None,
        locale: String | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DBRecommendationsMessage:
        """Describes the recommendations to resolve the issues for your DB
        instances, DB clusters, and DB parameter groups.

        :param last_updated_after: A filter to include only the recommendations that were updated after
        this specified time.
        :param last_updated_before: A filter to include only the recommendations that were updated before
        this specified time.
        :param locale: The language that you choose to return the list of recommendations.
        :param filters: A filter that specifies one or more recommendations to describe.
        :param max_records: The maximum number of recommendations to include in the response.
        :param marker: An optional pagination token provided by a previous
        ``DescribeDBRecommendations`` request.
        :returns: DBRecommendationsMessage
        """
        raise NotImplementedError

    @handler("DescribeDBSecurityGroups")
    def describe_db_security_groups(
        self,
        context: RequestContext,
        db_security_group_name: String | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DBSecurityGroupMessage:
        """Returns a list of ``DBSecurityGroup`` descriptions. If a
        ``DBSecurityGroupName`` is specified, the list will contain only the
        descriptions of the specified DB security group.

        EC2-Classic was retired on August 15, 2022. If you haven't migrated from
        EC2-Classic to a VPC, we recommend that you migrate as soon as possible.
        For more information, see `Migrate from EC2-Classic to a
        VPC <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-migrate.html>`__
        in the *Amazon EC2 User Guide*, the blog `EC2-Classic Networking is
        Retiring – Here’s How to
        Prepare <http://aws.amazon.com/blogs/aws/ec2-classic-is-retiring-heres-how-to-prepare/>`__,
        and `Moving a DB instance not in a VPC into a
        VPC <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Non-VPC2VPC.html>`__
        in the *Amazon RDS User Guide*.

        :param db_security_group_name: The name of the DB security group to return details for.
        :param filters: This parameter isn't currently supported.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous
        ``DescribeDBSecurityGroups`` request.
        :returns: DBSecurityGroupMessage
        :raises DBSecurityGroupNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeDBShardGroups")
    def describe_db_shard_groups(
        self,
        context: RequestContext,
        db_shard_group_identifier: DBShardGroupIdentifier | None = None,
        filters: FilterList | None = None,
        marker: String | None = None,
        max_records: MaxRecords | None = None,
        **kwargs,
    ) -> DescribeDBShardGroupsResponse:
        """Describes existing Aurora Limitless Database DB shard groups.

        :param db_shard_group_identifier: The user-supplied DB shard group identifier.
        :param filters: A filter that specifies one or more DB shard groups to describe.
        :param marker: An optional pagination token provided by a previous
        ``DescribeDBShardGroups`` request.
        :param max_records: The maximum number of records to include in the response.
        :returns: DescribeDBShardGroupsResponse
        :raises DBShardGroupNotFoundFault:
        :raises DBClusterNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeDBSnapshotAttributes")
    def describe_db_snapshot_attributes(
        self, context: RequestContext, db_snapshot_identifier: String, **kwargs
    ) -> DescribeDBSnapshotAttributesResult:
        """Returns a list of DB snapshot attribute names and values for a manual DB
        snapshot.

        When sharing snapshots with other Amazon Web Services accounts,
        ``DescribeDBSnapshotAttributes`` returns the ``restore`` attribute and a
        list of IDs for the Amazon Web Services accounts that are authorized to
        copy or restore the manual DB snapshot. If ``all`` is included in the
        list of values for the ``restore`` attribute, then the manual DB
        snapshot is public and can be copied or restored by all Amazon Web
        Services accounts.

        To add or remove access for an Amazon Web Services account to copy or
        restore a manual DB snapshot, or to make the manual DB snapshot public
        or private, use the ``ModifyDBSnapshotAttribute`` API action.

        :param db_snapshot_identifier: The identifier for the DB snapshot to describe the attributes for.
        :returns: DescribeDBSnapshotAttributesResult
        :raises DBSnapshotNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeDBSnapshotTenantDatabases")
    def describe_db_snapshot_tenant_databases(
        self,
        context: RequestContext,
        db_instance_identifier: String | None = None,
        db_snapshot_identifier: String | None = None,
        snapshot_type: String | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        dbi_resource_id: String | None = None,
        **kwargs,
    ) -> DBSnapshotTenantDatabasesMessage:
        """Describes the tenant databases that exist in a DB snapshot. This command
        only applies to RDS for Oracle DB instances in the multi-tenant
        configuration.

        You can use this command to inspect the tenant databases within a
        snapshot before restoring it. You can't directly interact with the
        tenant databases in a DB snapshot. If you restore a snapshot that was
        taken from DB instance using the multi-tenant configuration, you restore
        all its tenant databases.

        :param db_instance_identifier: The ID of the DB instance used to create the DB snapshots.
        :param db_snapshot_identifier: The ID of a DB snapshot that contains the tenant databases to describe.
        :param snapshot_type: The type of DB snapshots to be returned.
        :param filters: A filter that specifies one or more tenant databases to describe.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous
        ``DescribeDBSnapshotTenantDatabases`` request.
        :param dbi_resource_id: A specific DB resource identifier to describe.
        :returns: DBSnapshotTenantDatabasesMessage
        :raises DBSnapshotNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeDBSnapshots")
    def describe_db_snapshots(
        self,
        context: RequestContext,
        db_instance_identifier: String | None = None,
        db_snapshot_identifier: String | None = None,
        snapshot_type: String | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        include_shared: Boolean | None = None,
        include_public: Boolean | None = None,
        dbi_resource_id: String | None = None,
        **kwargs,
    ) -> DBSnapshotMessage:
        """Returns information about DB snapshots. This API action supports
        pagination.

        :param db_instance_identifier: The ID of the DB instance to retrieve the list of DB snapshots for.
        :param db_snapshot_identifier: A specific DB snapshot identifier to describe.
        :param snapshot_type: The type of snapshots to be returned.
        :param filters: A filter that specifies one or more DB snapshots to describe.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous
        ``DescribeDBSnapshots`` request.
        :param include_shared: Specifies whether to include shared manual DB cluster snapshots from
        other Amazon Web Services accounts that this Amazon Web Services account
        has been given permission to copy or restore.
        :param include_public: Specifies whether to include manual DB cluster snapshots that are public
        and can be copied or restored by any Amazon Web Services account.
        :param dbi_resource_id: A specific DB resource ID to describe.
        :returns: DBSnapshotMessage
        :raises DBSnapshotNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeDBSubnetGroups")
    def describe_db_subnet_groups(
        self,
        context: RequestContext,
        db_subnet_group_name: String | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DBSubnetGroupMessage:
        """Returns a list of DBSubnetGroup descriptions. If a DBSubnetGroupName is
        specified, the list will contain only the descriptions of the specified
        DBSubnetGroup.

        For an overview of CIDR ranges, go to the `Wikipedia
        Tutorial <http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`__.

        :param db_subnet_group_name: The name of the DB subnet group to return details for.
        :param filters: This parameter isn't currently supported.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous
        DescribeDBSubnetGroups request.
        :returns: DBSubnetGroupMessage
        :raises DBSubnetGroupNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeEngineDefaultClusterParameters")
    def describe_engine_default_cluster_parameters(
        self,
        context: RequestContext,
        db_parameter_group_family: String,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DescribeEngineDefaultClusterParametersResult:
        """Returns the default engine and system parameter information for the
        cluster database engine.

        For more information on Amazon Aurora, see `What is Amazon
        Aurora? <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html>`__
        in the *Amazon Aurora User Guide*.

        :param db_parameter_group_family: The name of the DB cluster parameter group family to return engine
        parameter information for.
        :param filters: This parameter isn't currently supported.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous
        ``DescribeEngineDefaultClusterParameters`` request.
        :returns: DescribeEngineDefaultClusterParametersResult
        """
        raise NotImplementedError

    @handler("DescribeEngineDefaultParameters")
    def describe_engine_default_parameters(
        self,
        context: RequestContext,
        db_parameter_group_family: String,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DescribeEngineDefaultParametersResult:
        """Returns the default engine and system parameter information for the
        specified database engine.

        :param db_parameter_group_family: The name of the DB parameter group family.
        :param filters: A filter that specifies one or more parameters to describe.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous
        ``DescribeEngineDefaultParameters`` request.
        :returns: DescribeEngineDefaultParametersResult
        """
        raise NotImplementedError

    @handler("DescribeEventCategories")
    def describe_event_categories(
        self,
        context: RequestContext,
        source_type: String | None = None,
        filters: FilterList | None = None,
        **kwargs,
    ) -> EventCategoriesMessage:
        """Displays a list of categories for all event source types, or, if
        specified, for a specified source type. You can also see this list in
        the "Amazon RDS event categories and event messages" section of the
        `Amazon RDS User
        Guide <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Messages.html>`__
        or the `Amazon Aurora User
        Guide <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Events.Messages.html>`__
        .

        :param source_type: The type of source that is generating the events.
        :param filters: This parameter isn't currently supported.
        :returns: EventCategoriesMessage
        """
        raise NotImplementedError

    @handler("DescribeEventSubscriptions")
    def describe_event_subscriptions(
        self,
        context: RequestContext,
        subscription_name: String | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> EventSubscriptionsMessage:
        """Lists all the subscription descriptions for a customer account. The
        description for a subscription includes ``SubscriptionName``,
        ``SNSTopicARN``, ``CustomerID``, ``SourceType``, ``SourceID``,
        ``CreationTime``, and ``Status``.

        If you specify a ``SubscriptionName``, lists the description for that
        subscription.

        :param subscription_name: The name of the RDS event notification subscription you want to
        describe.
        :param filters: This parameter isn't currently supported.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous
        DescribeOrderableDBInstanceOptions request.
        :returns: EventSubscriptionsMessage
        :raises SubscriptionNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeEvents")
    def describe_events(
        self,
        context: RequestContext,
        source_identifier: String | None = None,
        source_type: SourceType | None = None,
        start_time: TStamp | None = None,
        end_time: TStamp | None = None,
        duration: IntegerOptional | None = None,
        event_categories: EventCategoriesList | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> EventsMessage:
        """Returns events related to DB instances, DB clusters, DB parameter
        groups, DB security groups, DB snapshots, DB cluster snapshots, and RDS
        Proxies for the past 14 days. Events specific to a particular DB
        instance, DB cluster, DB parameter group, DB security group, DB
        snapshot, DB cluster snapshot group, or RDS Proxy can be obtained by
        providing the name as a parameter.

        For more information on working with events, see `Monitoring Amazon RDS
        events <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/working-with-events.html>`__
        in the *Amazon RDS User Guide* and `Monitoring Amazon Aurora
        events <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/working-with-events.html>`__
        in the *Amazon Aurora User Guide*.

        By default, RDS returns events that were generated in the past hour.

        :param source_identifier: The identifier of the event source for which events are returned.
        :param source_type: The event source to retrieve events for.
        :param start_time: The beginning of the time interval to retrieve events for, specified in
        ISO 8601 format.
        :param end_time: The end of the time interval for which to retrieve events, specified in
        ISO 8601 format.
        :param duration: The number of minutes to retrieve events for.
        :param event_categories: A list of event categories that trigger notifications for a event
        notification subscription.
        :param filters: This parameter isn't currently supported.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous DescribeEvents
        request.
        :returns: EventsMessage
        """
        raise NotImplementedError

    @handler("DescribeExportTasks")
    def describe_export_tasks(
        self,
        context: RequestContext,
        export_task_identifier: String | None = None,
        source_arn: String | None = None,
        filters: FilterList | None = None,
        marker: String | None = None,
        max_records: MaxRecords | None = None,
        source_type: ExportSourceType | None = None,
        **kwargs,
    ) -> ExportTasksMessage:
        """Returns information about a snapshot or cluster export to Amazon S3.
        This API operation supports pagination.

        :param export_task_identifier: The identifier of the snapshot or cluster export task to be described.
        :param source_arn: The Amazon Resource Name (ARN) of the snapshot or cluster exported to
        Amazon S3.
        :param filters: Filters specify one or more snapshot or cluster exports to describe.
        :param marker: An optional pagination token provided by a previous
        ``DescribeExportTasks`` request.
        :param max_records: The maximum number of records to include in the response.
        :param source_type: The type of source for the export.
        :returns: ExportTasksMessage
        :raises ExportTaskNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeGlobalClusters")
    def describe_global_clusters(
        self,
        context: RequestContext,
        global_cluster_identifier: String | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> GlobalClustersMessage:
        """Returns information about Aurora global database clusters. This API
        supports pagination.

        For more information on Amazon Aurora, see `What is Amazon
        Aurora? <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html>`__
        in the *Amazon Aurora User Guide*.

        This action only applies to Aurora DB clusters.

        :param global_cluster_identifier: The user-supplied DB cluster identifier.
        :param filters: A filter that specifies one or more global database clusters to
        describe.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous
        ``DescribeGlobalClusters`` request.
        :returns: GlobalClustersMessage
        :raises GlobalClusterNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeIntegrations")
    def describe_integrations(
        self,
        context: RequestContext,
        integration_identifier: IntegrationIdentifier | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: Marker | None = None,
        **kwargs,
    ) -> DescribeIntegrationsResponse:
        """Describe one or more zero-ETL integrations with Amazon Redshift.

        :param integration_identifier: The unique identifier of the integration.
        :param filters: A filter that specifies one or more resources to return.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous
        ``DescribeIntegrations`` request.
        :returns: DescribeIntegrationsResponse
        :raises IntegrationNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeOptionGroupOptions")
    def describe_option_group_options(
        self,
        context: RequestContext,
        engine_name: String,
        major_engine_version: String | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> OptionGroupOptionsMessage:
        """Describes all available options for the specified engine.

        :param engine_name: The name of the engine to describe options for.
        :param major_engine_version: If specified, filters the results to include only options for the
        specified major engine version.
        :param filters: This parameter isn't currently supported.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous request.
        :returns: OptionGroupOptionsMessage
        """
        raise NotImplementedError

    @handler("DescribeOptionGroups")
    def describe_option_groups(
        self,
        context: RequestContext,
        option_group_name: String | None = None,
        filters: FilterList | None = None,
        marker: String | None = None,
        max_records: IntegerOptional | None = None,
        engine_name: String | None = None,
        major_engine_version: String | None = None,
        **kwargs,
    ) -> OptionGroups:
        """Describes the available option groups.

        :param option_group_name: The name of the option group to describe.
        :param filters: This parameter isn't currently supported.
        :param marker: An optional pagination token provided by a previous DescribeOptionGroups
        request.
        :param max_records: The maximum number of records to include in the response.
        :param engine_name: A filter to only include option groups associated with this database
        engine.
        :param major_engine_version: Filters the list of option groups to only include groups associated with
        a specific database engine version.
        :returns: OptionGroups
        :raises OptionGroupNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeOrderableDBInstanceOptions")
    def describe_orderable_db_instance_options(
        self,
        context: RequestContext,
        engine: String,
        engine_version: String | None = None,
        db_instance_class: String | None = None,
        license_model: String | None = None,
        availability_zone_group: String | None = None,
        vpc: BooleanOptional | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> OrderableDBInstanceOptionsMessage:
        """Describes the orderable DB instance options for a specified DB engine.

        :param engine: The name of the database engine to describe DB instance options for.
        :param engine_version: A filter to include only the available options for the specified engine
        version.
        :param db_instance_class: A filter to include only the available options for the specified DB
        instance class.
        :param license_model: A filter to include only the available options for the specified license
        model.
        :param availability_zone_group: The Availability Zone group associated with a Local Zone.
        :param vpc: Specifies whether to show only VPC or non-VPC offerings.
        :param filters: This parameter isn't currently supported.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous
        DescribeOrderableDBInstanceOptions request.
        :returns: OrderableDBInstanceOptionsMessage
        """
        raise NotImplementedError

    @handler("DescribePendingMaintenanceActions")
    def describe_pending_maintenance_actions(
        self,
        context: RequestContext,
        resource_identifier: String | None = None,
        filters: FilterList | None = None,
        marker: String | None = None,
        max_records: IntegerOptional | None = None,
        **kwargs,
    ) -> PendingMaintenanceActionsMessage:
        """Returns a list of resources (for example, DB instances) that have at
        least one pending maintenance action.

        This API follows an eventual consistency model. This means that the
        result of the ``DescribePendingMaintenanceActions`` command might not be
        immediately visible to all subsequent RDS commands. Keep this in mind
        when you use ``DescribePendingMaintenanceActions`` immediately after
        using a previous API command such as ``ApplyPendingMaintenanceActions``.

        :param resource_identifier: The ARN of a resource to return pending maintenance actions for.
        :param filters: A filter that specifies one or more resources to return pending
        maintenance actions for.
        :param marker: An optional pagination token provided by a previous
        ``DescribePendingMaintenanceActions`` request.
        :param max_records: The maximum number of records to include in the response.
        :returns: PendingMaintenanceActionsMessage
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeReservedDBInstances")
    def describe_reserved_db_instances(
        self,
        context: RequestContext,
        reserved_db_instance_id: String | None = None,
        reserved_db_instances_offering_id: String | None = None,
        db_instance_class: String | None = None,
        duration: String | None = None,
        product_description: String | None = None,
        offering_type: String | None = None,
        multi_az: BooleanOptional | None = None,
        lease_id: String | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> ReservedDBInstanceMessage:
        """Returns information about reserved DB instances for this account, or
        about a specified reserved DB instance.

        :param reserved_db_instance_id: The reserved DB instance identifier filter value.
        :param reserved_db_instances_offering_id: The offering identifier filter value.
        :param db_instance_class: The DB instance class filter value.
        :param duration: The duration filter value, specified in years or seconds.
        :param product_description: The product description filter value.
        :param offering_type: The offering type filter value.
        :param multi_az: Specifies whether to show only those reservations that support Multi-AZ.
        :param lease_id: The lease identifier filter value.
        :param filters: This parameter isn't currently supported.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous request.
        :returns: ReservedDBInstanceMessage
        :raises ReservedDBInstanceNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeReservedDBInstancesOfferings")
    def describe_reserved_db_instances_offerings(
        self,
        context: RequestContext,
        reserved_db_instances_offering_id: String | None = None,
        db_instance_class: String | None = None,
        duration: String | None = None,
        product_description: String | None = None,
        offering_type: String | None = None,
        multi_az: BooleanOptional | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> ReservedDBInstancesOfferingMessage:
        """Lists available reserved DB instance offerings.

        :param reserved_db_instances_offering_id: The offering identifier filter value.
        :param db_instance_class: The DB instance class filter value.
        :param duration: Duration filter value, specified in years or seconds.
        :param product_description: Product description filter value.
        :param offering_type: The offering type filter value.
        :param multi_az: Specifies whether to show only those reservations that support Multi-AZ.
        :param filters: This parameter isn't currently supported.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous request.
        :returns: ReservedDBInstancesOfferingMessage
        :raises ReservedDBInstancesOfferingNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeSourceRegions")
    def describe_source_regions(
        self,
        context: RequestContext,
        region_name: String | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        filters: FilterList | None = None,
        **kwargs,
    ) -> SourceRegionMessage:
        """Returns a list of the source Amazon Web Services Regions where the
        current Amazon Web Services Region can create a read replica, copy a DB
        snapshot from, or replicate automated backups from.

        Use this operation to determine whether cross-Region features are
        supported between other Regions and your current Region. This operation
        supports pagination.

        To return information about the Regions that are enabled for your
        account, or all Regions, use the EC2 operation ``DescribeRegions``. For
        more information, see
        `DescribeRegions <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeRegions.html>`__
        in the *Amazon EC2 API Reference*.

        :param region_name: The source Amazon Web Services Region name.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous
        ``DescribeSourceRegions`` request.
        :param filters: This parameter isn't currently supported.
        :returns: SourceRegionMessage
        """
        raise NotImplementedError

    @handler("DescribeTenantDatabases")
    def describe_tenant_databases(
        self,
        context: RequestContext,
        db_instance_identifier: String | None = None,
        tenant_db_name: String | None = None,
        filters: FilterList | None = None,
        marker: String | None = None,
        max_records: IntegerOptional | None = None,
        **kwargs,
    ) -> TenantDatabasesMessage:
        """Describes the tenant databases in a DB instance that uses the
        multi-tenant configuration. Only RDS for Oracle CDB instances are
        supported.

        :param db_instance_identifier: The user-supplied DB instance identifier, which must match the
        identifier of an existing instance owned by the Amazon Web Services
        account.
        :param tenant_db_name: The user-supplied tenant database name, which must match the name of an
        existing tenant database on the specified DB instance owned by your
        Amazon Web Services account.
        :param filters: A filter that specifies one or more database tenants to describe.
        :param marker: An optional pagination token provided by a previous
        ``DescribeTenantDatabases`` request.
        :param max_records: The maximum number of records to include in the response.
        :returns: TenantDatabasesMessage
        :raises DBInstanceNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeValidDBInstanceModifications")
    def describe_valid_db_instance_modifications(
        self, context: RequestContext, db_instance_identifier: String, **kwargs
    ) -> DescribeValidDBInstanceModificationsResult:
        """You can call ``DescribeValidDBInstanceModifications`` to learn what
        modifications you can make to your DB instance. You can use this
        information when you call ``ModifyDBInstance``.

        This command doesn't apply to RDS Custom.

        :param db_instance_identifier: The customer identifier or the ARN of your DB instance.
        :returns: DescribeValidDBInstanceModificationsResult
        :raises DBInstanceNotFoundFault:
        :raises InvalidDBInstanceStateFault:
        """
        raise NotImplementedError

    @handler("DisableHttpEndpoint")
    def disable_http_endpoint(
        self, context: RequestContext, resource_arn: String, **kwargs
    ) -> DisableHttpEndpointResponse:
        """Disables the HTTP endpoint for the specified DB cluster. Disabling this
        endpoint disables RDS Data API.

        For more information, see `Using RDS Data
        API <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html>`__
        in the *Amazon Aurora User Guide*.

        This operation applies only to Aurora Serverless v2 and provisioned DB
        clusters. To disable the HTTP endpoint for Aurora Serverless v1 DB
        clusters, use the ``EnableHttpEndpoint`` parameter of the
        ``ModifyDBCluster`` operation.

        :param resource_arn: The Amazon Resource Name (ARN) of the DB cluster.
        :returns: DisableHttpEndpointResponse
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        """
        raise NotImplementedError

    @handler("DownloadDBLogFilePortion")
    def download_db_log_file_portion(
        self,
        context: RequestContext,
        db_instance_identifier: String,
        log_file_name: String,
        marker: String | None = None,
        number_of_lines: Integer | None = None,
        **kwargs,
    ) -> DownloadDBLogFilePortionDetails:
        """Downloads all or a portion of the specified log file, up to 1 MB in
        size.

        This command doesn't apply to RDS Custom.

        :param db_instance_identifier: The customer-assigned name of the DB instance that contains the log
        files you want to list.
        :param log_file_name: The name of the log file to be downloaded.
        :param marker: The pagination token provided in the previous request or "0".
        :param number_of_lines: The number of lines to download.
        :returns: DownloadDBLogFilePortionDetails
        :raises DBInstanceNotFoundFault:
        :raises DBInstanceNotReadyFault:
        :raises DBLogFileNotFoundFault:
        """
        raise NotImplementedError

    @handler("EnableHttpEndpoint")
    def enable_http_endpoint(
        self, context: RequestContext, resource_arn: String, **kwargs
    ) -> EnableHttpEndpointResponse:
        """Enables the HTTP endpoint for the DB cluster. By default, the HTTP
        endpoint isn't enabled.

        When enabled, this endpoint provides a connectionless web service API
        (RDS Data API) for running SQL queries on the Aurora DB cluster. You can
        also query your database from inside the RDS console with the RDS query
        editor.

        For more information, see `Using RDS Data
        API <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html>`__
        in the *Amazon Aurora User Guide*.

        This operation applies only to Aurora Serverless v2 and provisioned DB
        clusters. To enable the HTTP endpoint for Aurora Serverless v1 DB
        clusters, use the ``EnableHttpEndpoint`` parameter of the
        ``ModifyDBCluster`` operation.

        :param resource_arn: The Amazon Resource Name (ARN) of the DB cluster.
        :returns: EnableHttpEndpointResponse
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        """
        raise NotImplementedError

    @handler("FailoverDBCluster")
    def failover_db_cluster(
        self,
        context: RequestContext,
        db_cluster_identifier: String,
        target_db_instance_identifier: String | None = None,
        **kwargs,
    ) -> FailoverDBClusterResult:
        """Forces a failover for a DB cluster.

        For an Aurora DB cluster, failover for a DB cluster promotes one of the
        Aurora Replicas (read-only instances) in the DB cluster to be the
        primary DB instance (the cluster writer).

        For a Multi-AZ DB cluster, after RDS terminates the primary DB instance,
        the internal monitoring system detects that the primary DB instance is
        unhealthy and promotes a readable standby (read-only instances) in the
        DB cluster to be the primary DB instance (the cluster writer). Failover
        times are typically less than 35 seconds.

        An Amazon Aurora DB cluster automatically fails over to an Aurora
        Replica, if one exists, when the primary DB instance fails. A Multi-AZ
        DB cluster automatically fails over to a readable standby DB instance
        when the primary DB instance fails.

        To simulate a failure of a primary instance for testing, you can force a
        failover. Because each instance in a DB cluster has its own endpoint
        address, make sure to clean up and re-establish any existing connections
        that use those endpoint addresses when the failover is complete.

        For more information on Amazon Aurora DB clusters, see `What is Amazon
        Aurora? <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html>`__
        in the *Amazon Aurora User Guide*.

        For more information on Multi-AZ DB clusters, see `Multi-AZ DB cluster
        deployments <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html>`__
        in the *Amazon RDS User Guide*.

        :param db_cluster_identifier: The identifier of the DB cluster to force a failover for.
        :param target_db_instance_identifier: The name of the DB instance to promote to the primary DB instance.
        :returns: FailoverDBClusterResult
        :raises DBClusterNotFoundFault:
        :raises InvalidDBClusterStateFault:
        :raises InvalidDBInstanceStateFault:
        """
        raise NotImplementedError

    @handler("FailoverGlobalCluster")
    def failover_global_cluster(
        self,
        context: RequestContext,
        global_cluster_identifier: GlobalClusterIdentifier,
        target_db_cluster_identifier: DBClusterIdentifier,
        allow_data_loss: BooleanOptional | None = None,
        switchover: BooleanOptional | None = None,
        **kwargs,
    ) -> FailoverGlobalClusterResult:
        """Promotes the specified secondary DB cluster to be the primary DB cluster
        in the global database cluster to fail over or switch over a global
        database. Switchover operations were previously called "managed planned
        failovers."

        Although this operation can be used either to fail over or to switch
        over a global database cluster, its intended use is for global database
        failover. To switch over a global database cluster, we recommend that
        you use the SwitchoverGlobalCluster operation instead.

        How you use this operation depends on whether you are failing over or
        switching over your global database cluster:

        -  Failing over - Specify the ``AllowDataLoss`` parameter and don't
           specify the ``Switchover`` parameter.

        -  Switching over - Specify the ``Switchover`` parameter or omit it, but
           don't specify the ``AllowDataLoss`` parameter.

        **About failing over and switching over**

        While failing over and switching over a global database cluster both
        change the primary DB cluster, you use these operations for different
        reasons:

        -  *Failing over* - Use this operation to respond to an unplanned event,
           such as a Regional disaster in the primary Region. Failing over can
           result in a loss of write transaction data that wasn't replicated to
           the chosen secondary before the failover event occurred. However, the
           recovery process that promotes a DB instance on the chosen seconday
           DB cluster to be the primary writer DB instance guarantees that the
           data is in a transactionally consistent state.

           For more information about failing over an Amazon Aurora global
           database, see `Performing managed failovers for Aurora global
           databases <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html#aurora-global-database-failover.managed-unplanned>`__
           in the *Amazon Aurora User Guide*.

        -  *Switching over* - Use this operation on a healthy global database
           cluster for planned events, such as Regional rotation or to fail back
           to the original primary DB cluster after a failover operation. With
           this operation, there is no data loss.

           For more information about switching over an Amazon Aurora global
           database, see `Performing switchovers for Aurora global
           databases <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html#aurora-global-database-disaster-recovery.managed-failover>`__
           in the *Amazon Aurora User Guide*.

        :param global_cluster_identifier: The identifier of the global database cluster (Aurora global database)
        this operation should apply to.
        :param target_db_cluster_identifier: The identifier of the secondary Aurora DB cluster that you want to
        promote to the primary for the global database cluster.
        :param allow_data_loss: Specifies whether to allow data loss for this global database cluster
        operation.
        :param switchover: Specifies whether to switch over this global database cluster.
        :returns: FailoverGlobalClusterResult
        :raises GlobalClusterNotFoundFault:
        :raises InvalidGlobalClusterStateFault:
        :raises InvalidDBClusterStateFault:
        :raises DBClusterNotFoundFault:
        """
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(
        self,
        context: RequestContext,
        resource_name: String,
        filters: FilterList | None = None,
        **kwargs,
    ) -> TagListMessage:
        """Lists all tags on an Amazon RDS resource.

        For an overview on tagging an Amazon RDS resource, see `Tagging Amazon
        RDS
        Resources <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html>`__
        in the *Amazon RDS User Guide* or `Tagging Amazon Aurora and Amazon RDS
        Resources <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html>`__
        in the *Amazon Aurora User Guide*.

        :param resource_name: The Amazon RDS resource with tags to be listed.
        :param filters: This parameter isn't currently supported.
        :returns: TagListMessage
        :raises DBInstanceNotFoundFault:
        :raises DBSnapshotNotFoundFault:
        :raises DBClusterNotFoundFault:
        :raises DBProxyNotFoundFault:
        :raises DBProxyTargetGroupNotFoundFault:
        :raises BlueGreenDeploymentNotFoundFault:
        :raises IntegrationNotFoundFault:
        :raises TenantDatabaseNotFoundFault:
        :raises DBSnapshotTenantDatabaseNotFoundFault:
        """
        raise NotImplementedError

    @handler("ModifyActivityStream")
    def modify_activity_stream(
        self,
        context: RequestContext,
        resource_arn: String | None = None,
        audit_policy_state: AuditPolicyState | None = None,
        **kwargs,
    ) -> ModifyActivityStreamResponse:
        """Changes the audit policy state of a database activity stream to either
        locked (default) or unlocked. A locked policy is read-only, whereas an
        unlocked policy is read/write. If your activity stream is started and
        locked, you can unlock it, customize your audit policy, and then lock
        your activity stream. Restarting the activity stream isn't required. For
        more information, see `Modifying a database activity
        stream <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/DBActivityStreams.Modifying.html>`__
        in the *Amazon RDS User Guide*.

        This operation is supported for RDS for Oracle and Microsoft SQL Server.

        :param resource_arn: The Amazon Resource Name (ARN) of the RDS for Oracle or Microsoft SQL
        Server DB instance.
        :param audit_policy_state: The audit policy state.
        :returns: ModifyActivityStreamResponse
        :raises InvalidDBInstanceStateFault:
        :raises ResourceNotFoundFault:
        :raises DBInstanceNotFoundFault:
        """
        raise NotImplementedError

    @handler("ModifyCertificates")
    def modify_certificates(
        self,
        context: RequestContext,
        certificate_identifier: String | None = None,
        remove_customer_override: BooleanOptional | None = None,
        **kwargs,
    ) -> ModifyCertificatesResult:
        """Override the system-default Secure Sockets Layer/Transport Layer
        Security (SSL/TLS) certificate for Amazon RDS for new DB instances, or
        remove the override.

        By using this operation, you can specify an RDS-approved SSL/TLS
        certificate for new DB instances that is different from the default
        certificate provided by RDS. You can also use this operation to remove
        the override, so that new DB instances use the default certificate
        provided by RDS.

        You might need to override the default certificate in the following
        situations:

        -  You already migrated your applications to support the latest
           certificate authority (CA) certificate, but the new CA certificate is
           not yet the RDS default CA certificate for the specified Amazon Web
           Services Region.

        -  RDS has already moved to a new default CA certificate for the
           specified Amazon Web Services Region, but you are still in the
           process of supporting the new CA certificate. In this case, you
           temporarily need additional time to finish your application changes.

        For more information about rotating your SSL/TLS certificate for RDS DB
        engines, see `Rotating Your SSL/TLS
        Certificate <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL-certificate-rotation.html>`__
        in the *Amazon RDS User Guide*.

        For more information about rotating your SSL/TLS certificate for Aurora
        DB engines, see `Rotating Your SSL/TLS
        Certificate <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL-certificate-rotation.html>`__
        in the *Amazon Aurora User Guide*.

        :param certificate_identifier: The new default certificate identifier to override the current one with.
        :param remove_customer_override: Specifies whether to remove the override for the default certificate.
        :returns: ModifyCertificatesResult
        :raises CertificateNotFoundFault:
        """
        raise NotImplementedError

    @handler("ModifyCurrentDBClusterCapacity")
    def modify_current_db_cluster_capacity(
        self,
        context: RequestContext,
        db_cluster_identifier: String,
        capacity: IntegerOptional | None = None,
        seconds_before_timeout: IntegerOptional | None = None,
        timeout_action: String | None = None,
        **kwargs,
    ) -> DBClusterCapacityInfo:
        """Set the capacity of an Aurora Serverless v1 DB cluster to a specific
        value.

        Aurora Serverless v1 scales seamlessly based on the workload on the DB
        cluster. In some cases, the capacity might not scale fast enough to meet
        a sudden change in workload, such as a large number of new transactions.
        Call ``ModifyCurrentDBClusterCapacity`` to set the capacity explicitly.

        After this call sets the DB cluster capacity, Aurora Serverless v1 can
        automatically scale the DB cluster based on the cooldown period for
        scaling up and the cooldown period for scaling down.

        For more information about Aurora Serverless v1, see `Using Amazon
        Aurora Serverless
        v1 <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.html>`__
        in the *Amazon Aurora User Guide*.

        If you call ``ModifyCurrentDBClusterCapacity`` with the default
        ``TimeoutAction``, connections that prevent Aurora Serverless v1 from
        finding a scaling point might be dropped. For more information about
        scaling points, see `Autoscaling for Aurora Serverless
        v1 <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.how-it-works.html#aurora-serverless.how-it-works.auto-scaling>`__
        in the *Amazon Aurora User Guide*.

        This operation only applies to Aurora Serverless v1 DB clusters.

        :param db_cluster_identifier: The DB cluster identifier for the cluster being modified.
        :param capacity: The DB cluster capacity.
        :param seconds_before_timeout: The amount of time, in seconds, that Aurora Serverless v1 tries to find
        a scaling point to perform seamless scaling before enforcing the timeout
        action.
        :param timeout_action: The action to take when the timeout is reached, either
        ``ForceApplyCapacityChange`` or ``RollbackCapacityChange``.
        :returns: DBClusterCapacityInfo
        :raises DBClusterNotFoundFault:
        :raises InvalidDBClusterStateFault:
        :raises InvalidDBClusterCapacityFault:
        """
        raise NotImplementedError

    @handler("ModifyCustomDBEngineVersion")
    def modify_custom_db_engine_version(
        self,
        context: RequestContext,
        engine: CustomEngineName,
        engine_version: CustomEngineVersion,
        description: Description | None = None,
        status: CustomEngineVersionStatus | None = None,
        **kwargs,
    ) -> DBEngineVersion:
        """Modifies the status of a custom engine version (CEV). You can find CEVs
        to modify by calling ``DescribeDBEngineVersions``.

        The MediaImport service that imports files from Amazon S3 to create CEVs
        isn't integrated with Amazon Web Services CloudTrail. If you turn on
        data logging for Amazon RDS in CloudTrail, calls to the
        ``ModifyCustomDbEngineVersion`` event aren't logged. However, you might
        see calls from the API gateway that accesses your Amazon S3 bucket.
        These calls originate from the MediaImport service for the
        ``ModifyCustomDbEngineVersion`` event.

        For more information, see `Modifying CEV
        status <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev.html#custom-cev.modify>`__
        in the *Amazon RDS User Guide*.

        :param engine: The database engine.
        :param engine_version: The custom engine version (CEV) that you want to modify.
        :param description: An optional description of your CEV.
        :param status: The availability status to be assigned to the CEV.
        :returns: DBEngineVersion
        :raises CustomDBEngineVersionNotFoundFault:
        :raises InvalidCustomDBEngineVersionStateFault:
        """
        raise NotImplementedError

    @handler("ModifyDBCluster")
    def modify_db_cluster(
        self,
        context: RequestContext,
        db_cluster_identifier: String,
        new_db_cluster_identifier: String | None = None,
        apply_immediately: Boolean | None = None,
        backup_retention_period: IntegerOptional | None = None,
        db_cluster_parameter_group_name: String | None = None,
        vpc_security_group_ids: VpcSecurityGroupIdList | None = None,
        port: IntegerOptional | None = None,
        master_user_password: String | None = None,
        option_group_name: String | None = None,
        preferred_backup_window: String | None = None,
        preferred_maintenance_window: String | None = None,
        enable_iam_database_authentication: BooleanOptional | None = None,
        backtrack_window: LongOptional | None = None,
        cloudwatch_logs_export_configuration: CloudwatchLogsExportConfiguration | None = None,
        engine_version: String | None = None,
        allow_major_version_upgrade: Boolean | None = None,
        db_instance_parameter_group_name: String | None = None,
        domain: String | None = None,
        domain_iam_role_name: String | None = None,
        scaling_configuration: ScalingConfiguration | None = None,
        deletion_protection: BooleanOptional | None = None,
        enable_http_endpoint: BooleanOptional | None = None,
        copy_tags_to_snapshot: BooleanOptional | None = None,
        enable_global_write_forwarding: BooleanOptional | None = None,
        db_cluster_instance_class: String | None = None,
        allocated_storage: IntegerOptional | None = None,
        storage_type: String | None = None,
        iops: IntegerOptional | None = None,
        auto_minor_version_upgrade: BooleanOptional | None = None,
        monitoring_interval: IntegerOptional | None = None,
        monitoring_role_arn: String | None = None,
        database_insights_mode: DatabaseInsightsMode | None = None,
        enable_performance_insights: BooleanOptional | None = None,
        performance_insights_kms_key_id: String | None = None,
        performance_insights_retention_period: IntegerOptional | None = None,
        serverless_v2_scaling_configuration: ServerlessV2ScalingConfiguration | None = None,
        network_type: String | None = None,
        manage_master_user_password: BooleanOptional | None = None,
        rotate_master_user_password: BooleanOptional | None = None,
        master_user_secret_kms_key_id: String | None = None,
        engine_mode: String | None = None,
        allow_engine_mode_change: Boolean | None = None,
        enable_local_write_forwarding: BooleanOptional | None = None,
        aws_backup_recovery_point_arn: AwsBackupRecoveryPointArn | None = None,
        enable_limitless_database: BooleanOptional | None = None,
        ca_certificate_identifier: String | None = None,
        **kwargs,
    ) -> ModifyDBClusterResult:
        """Modifies the settings of an Amazon Aurora DB cluster or a Multi-AZ DB
        cluster. You can change one or more settings by specifying these
        parameters and the new values in the request.

        For more information on Amazon Aurora DB clusters, see `What is Amazon
        Aurora? <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html>`__
        in the *Amazon Aurora User Guide*.

        For more information on Multi-AZ DB clusters, see `Multi-AZ DB cluster
        deployments <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html>`__
        in the *Amazon RDS User Guide*.

        :param db_cluster_identifier: The DB cluster identifier for the cluster being modified.
        :param new_db_cluster_identifier: The new DB cluster identifier for the DB cluster when renaming a DB
        cluster.
        :param apply_immediately: Specifies whether the modifications in this request are asynchronously
        applied as soon as possible, regardless of the
        ``PreferredMaintenanceWindow`` setting for the DB cluster.
        :param backup_retention_period: The number of days for which automated backups are retained.
        :param db_cluster_parameter_group_name: The name of the DB cluster parameter group to use for the DB cluster.
        :param vpc_security_group_ids: A list of EC2 VPC security groups to associate with this DB cluster.
        :param port: The port number on which the DB cluster accepts connections.
        :param master_user_password: The new password for the master database user.
        :param option_group_name: The option group to associate the DB cluster with.
        :param preferred_backup_window: The daily time range during which automated backups are created if
        automated backups are enabled, using the ``BackupRetentionPeriod``
        parameter.
        :param preferred_maintenance_window: The weekly time range during which system maintenance can occur, in
        Universal Coordinated Time (UTC).
        :param enable_iam_database_authentication: Specifies whether to enable mapping of Amazon Web Services Identity and
        Access Management (IAM) accounts to database accounts.
        :param backtrack_window: The target backtrack window, in seconds.
        :param cloudwatch_logs_export_configuration: The configuration setting for the log types to be enabled for export to
        CloudWatch Logs for a specific DB cluster.
        :param engine_version: The version number of the database engine to which you want to upgrade.
        :param allow_major_version_upgrade: Specifies whether major version upgrades are allowed.
        :param db_instance_parameter_group_name: The name of the DB parameter group to apply to all instances of the DB
        cluster.
        :param domain: The Active Directory directory ID to move the DB cluster to.
        :param domain_iam_role_name: The name of the IAM role to use when making API calls to the Directory
        Service.
        :param scaling_configuration: The scaling properties of the DB cluster.
        :param deletion_protection: Specifies whether the DB cluster has deletion protection enabled.
        :param enable_http_endpoint: Specifies whether to enable the HTTP endpoint for an Aurora Serverless
        v1 DB cluster.
        :param copy_tags_to_snapshot: Specifies whether to copy all tags from the DB cluster to snapshots of
        the DB cluster.
        :param enable_global_write_forwarding: Specifies whether to enable this DB cluster to forward write operations
        to the primary cluster of a global cluster (Aurora global database).
        :param db_cluster_instance_class: The compute and memory capacity of each DB instance in the Multi-AZ DB
        cluster, for example ``db.
        :param allocated_storage: The amount of storage in gibibytes (GiB) to allocate to each DB instance
        in the Multi-AZ DB cluster.
        :param storage_type: The storage type to associate with the DB cluster.
        :param iops: The amount of Provisioned IOPS (input/output operations per second) to
        be initially allocated for each DB instance in the Multi-AZ DB cluster.
        :param auto_minor_version_upgrade: Specifies whether minor engine upgrades are applied automatically to the
        DB cluster during the maintenance window.
        :param monitoring_interval: The interval, in seconds, between points when Enhanced Monitoring
        metrics are collected for the DB cluster.
        :param monitoring_role_arn: The Amazon Resource Name (ARN) for the IAM role that permits RDS to send
        Enhanced Monitoring metrics to Amazon CloudWatch Logs.
        :param database_insights_mode: Specifies the mode of Database Insights to enable for the DB cluster.
        :param enable_performance_insights: Specifies whether to turn on Performance Insights for the DB cluster.
        :param performance_insights_kms_key_id: The Amazon Web Services KMS key identifier for encryption of Performance
        Insights data.
        :param performance_insights_retention_period: The number of days to retain Performance Insights data.
        :param serverless_v2_scaling_configuration: Contains the scaling configuration of an Aurora Serverless v2 DB
        cluster.
        :param network_type: The network type of the DB cluster.
        :param manage_master_user_password: Specifies whether to manage the master user password with Amazon Web
        Services Secrets Manager.
        :param rotate_master_user_password: Specifies whether to rotate the secret managed by Amazon Web Services
        Secrets Manager for the master user password.
        :param master_user_secret_kms_key_id: The Amazon Web Services KMS key identifier to encrypt a secret that is
        automatically generated and managed in Amazon Web Services Secrets
        Manager.
        :param engine_mode: The DB engine mode of the DB cluster, either ``provisioned`` or
        ``serverless``.
        :param allow_engine_mode_change: Specifies whether engine mode changes from ``serverless`` to
        ``provisioned`` are allowed.
        :param enable_local_write_forwarding: Specifies whether read replicas can forward write operations to the
        writer DB instance in the DB cluster.
        :param aws_backup_recovery_point_arn: The Amazon Resource Name (ARN) of the recovery point in Amazon Web
        Services Backup.
        :param enable_limitless_database: Specifies whether to enable Aurora Limitless Database.
        :param ca_certificate_identifier: The CA certificate identifier to use for the DB cluster's server
        certificate.
        :returns: ModifyDBClusterResult
        :raises DBClusterNotFoundFault:
        :raises InvalidDBClusterStateFault:
        :raises StorageQuotaExceededFault:
        :raises DBSubnetGroupNotFoundFault:
        :raises InvalidVPCNetworkStateFault:
        :raises InvalidDBSubnetGroupStateFault:
        :raises InvalidSubnet:
        :raises DBClusterParameterGroupNotFoundFault:
        :raises InvalidDBSecurityGroupStateFault:
        :raises InvalidDBInstanceStateFault:
        :raises DBClusterAlreadyExistsFault:
        :raises DBInstanceAlreadyExistsFault:
        :raises DomainNotFoundFault:
        :raises StorageTypeNotAvailableFault:
        :raises OptionGroupNotFoundFault:
        """
        raise NotImplementedError

    @handler("ModifyDBClusterEndpoint")
    def modify_db_cluster_endpoint(
        self,
        context: RequestContext,
        db_cluster_endpoint_identifier: String,
        endpoint_type: String | None = None,
        static_members: StringList | None = None,
        excluded_members: StringList | None = None,
        **kwargs,
    ) -> DBClusterEndpoint:
        """Modifies the properties of an endpoint in an Amazon Aurora DB cluster.

        This operation only applies to Aurora DB clusters.

        :param db_cluster_endpoint_identifier: The identifier of the endpoint to modify.
        :param endpoint_type: The type of the endpoint.
        :param static_members: List of DB instance identifiers that are part of the custom endpoint
        group.
        :param excluded_members: List of DB instance identifiers that aren't part of the custom endpoint
        group.
        :returns: DBClusterEndpoint
        :raises InvalidDBClusterStateFault:
        :raises InvalidDBClusterEndpointStateFault:
        :raises DBClusterEndpointNotFoundFault:
        :raises DBInstanceNotFoundFault:
        :raises InvalidDBInstanceStateFault:
        """
        raise NotImplementedError

    @handler("ModifyDBClusterParameterGroup")
    def modify_db_cluster_parameter_group(
        self,
        context: RequestContext,
        db_cluster_parameter_group_name: String,
        parameters: ParametersList,
        **kwargs,
    ) -> DBClusterParameterGroupNameMessage:
        """Modifies the parameters of a DB cluster parameter group. To modify more
        than one parameter, submit a list of the following: ``ParameterName``,
        ``ParameterValue``, and ``ApplyMethod``. A maximum of 20 parameters can
        be modified in a single request.

        After you create a DB cluster parameter group, you should wait at least
        5 minutes before creating your first DB cluster that uses that DB
        cluster parameter group as the default parameter group. This allows
        Amazon RDS to fully complete the create operation before the parameter
        group is used as the default for a new DB cluster. This is especially
        important for parameters that are critical when creating the default
        database for a DB cluster, such as the character set for the default
        database defined by the ``character_set_database`` parameter. You can
        use the *Parameter Groups* option of the `Amazon RDS
        console <https://console.aws.amazon.com/rds/>`__ or the
        ``DescribeDBClusterParameters`` operation to verify that your DB cluster
        parameter group has been created or modified.

        If the modified DB cluster parameter group is used by an Aurora
        Serverless v1 cluster, Aurora applies the update immediately. The
        cluster restart might interrupt your workload. In that case, your
        application must reopen any connections and retry any transactions that
        were active when the parameter changes took effect.

        For more information on Amazon Aurora DB clusters, see `What is Amazon
        Aurora? <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html>`__
        in the *Amazon Aurora User Guide*.

        For more information on Multi-AZ DB clusters, see `Multi-AZ DB cluster
        deployments <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html>`__
        in the *Amazon RDS User Guide.*

        :param db_cluster_parameter_group_name: The name of the DB cluster parameter group to modify.
        :param parameters: A list of parameters in the DB cluster parameter group to modify.
        :returns: DBClusterParameterGroupNameMessage
        :raises DBParameterGroupNotFoundFault:
        :raises InvalidDBParameterGroupStateFault:
        """
        raise NotImplementedError

    @handler("ModifyDBClusterSnapshotAttribute")
    def modify_db_cluster_snapshot_attribute(
        self,
        context: RequestContext,
        db_cluster_snapshot_identifier: String,
        attribute_name: String,
        values_to_add: AttributeValueList | None = None,
        values_to_remove: AttributeValueList | None = None,
        **kwargs,
    ) -> ModifyDBClusterSnapshotAttributeResult:
        """Adds an attribute and values to, or removes an attribute and values
        from, a manual DB cluster snapshot.

        To share a manual DB cluster snapshot with other Amazon Web Services
        accounts, specify ``restore`` as the ``AttributeName`` and use the
        ``ValuesToAdd`` parameter to add a list of IDs of the Amazon Web
        Services accounts that are authorized to restore the manual DB cluster
        snapshot. Use the value ``all`` to make the manual DB cluster snapshot
        public, which means that it can be copied or restored by all Amazon Web
        Services accounts.

        Don't add the ``all`` value for any manual DB cluster snapshots that
        contain private information that you don't want available to all Amazon
        Web Services accounts.

        If a manual DB cluster snapshot is encrypted, it can be shared, but only
        by specifying a list of authorized Amazon Web Services account IDs for
        the ``ValuesToAdd`` parameter. You can't use ``all`` as a value for that
        parameter in this case.

        To view which Amazon Web Services accounts have access to copy or
        restore a manual DB cluster snapshot, or whether a manual DB cluster
        snapshot is public or private, use the
        DescribeDBClusterSnapshotAttributes API operation. The accounts are
        returned as values for the ``restore`` attribute.

        :param db_cluster_snapshot_identifier: The identifier for the DB cluster snapshot to modify the attributes for.
        :param attribute_name: The name of the DB cluster snapshot attribute to modify.
        :param values_to_add: A list of DB cluster snapshot attributes to add to the attribute
        specified by ``AttributeName``.
        :param values_to_remove: A list of DB cluster snapshot attributes to remove from the attribute
        specified by ``AttributeName``.
        :returns: ModifyDBClusterSnapshotAttributeResult
        :raises DBClusterSnapshotNotFoundFault:
        :raises InvalidDBClusterSnapshotStateFault:
        :raises SharedSnapshotQuotaExceededFault:
        """
        raise NotImplementedError

    @handler("ModifyDBInstance")
    def modify_db_instance(
        self,
        context: RequestContext,
        db_instance_identifier: String,
        allocated_storage: IntegerOptional | None = None,
        db_instance_class: String | None = None,
        db_subnet_group_name: String | None = None,
        db_security_groups: DBSecurityGroupNameList | None = None,
        vpc_security_group_ids: VpcSecurityGroupIdList | None = None,
        apply_immediately: Boolean | None = None,
        master_user_password: String | None = None,
        db_parameter_group_name: String | None = None,
        backup_retention_period: IntegerOptional | None = None,
        preferred_backup_window: String | None = None,
        preferred_maintenance_window: String | None = None,
        multi_az: BooleanOptional | None = None,
        engine_version: String | None = None,
        allow_major_version_upgrade: Boolean | None = None,
        auto_minor_version_upgrade: BooleanOptional | None = None,
        license_model: String | None = None,
        iops: IntegerOptional | None = None,
        option_group_name: String | None = None,
        new_db_instance_identifier: String | None = None,
        storage_type: String | None = None,
        tde_credential_arn: String | None = None,
        tde_credential_password: String | None = None,
        ca_certificate_identifier: String | None = None,
        domain: String | None = None,
        domain_fqdn: String | None = None,
        domain_ou: String | None = None,
        domain_auth_secret_arn: String | None = None,
        domain_dns_ips: StringList | None = None,
        copy_tags_to_snapshot: BooleanOptional | None = None,
        monitoring_interval: IntegerOptional | None = None,
        db_port_number: IntegerOptional | None = None,
        publicly_accessible: BooleanOptional | None = None,
        monitoring_role_arn: String | None = None,
        domain_iam_role_name: String | None = None,
        disable_domain: BooleanOptional | None = None,
        promotion_tier: IntegerOptional | None = None,
        enable_iam_database_authentication: BooleanOptional | None = None,
        database_insights_mode: DatabaseInsightsMode | None = None,
        enable_performance_insights: BooleanOptional | None = None,
        performance_insights_kms_key_id: String | None = None,
        performance_insights_retention_period: IntegerOptional | None = None,
        cloudwatch_logs_export_configuration: CloudwatchLogsExportConfiguration | None = None,
        processor_features: ProcessorFeatureList | None = None,
        use_default_processor_features: BooleanOptional | None = None,
        deletion_protection: BooleanOptional | None = None,
        max_allocated_storage: IntegerOptional | None = None,
        certificate_rotation_restart: BooleanOptional | None = None,
        replica_mode: ReplicaMode | None = None,
        enable_customer_owned_ip: BooleanOptional | None = None,
        aws_backup_recovery_point_arn: AwsBackupRecoveryPointArn | None = None,
        automation_mode: AutomationMode | None = None,
        resume_full_automation_mode_minutes: IntegerOptional | None = None,
        network_type: String | None = None,
        storage_throughput: IntegerOptional | None = None,
        manage_master_user_password: BooleanOptional | None = None,
        rotate_master_user_password: BooleanOptional | None = None,
        master_user_secret_kms_key_id: String | None = None,
        engine: String | None = None,
        dedicated_log_volume: BooleanOptional | None = None,
        multi_tenant: BooleanOptional | None = None,
        **kwargs,
    ) -> ModifyDBInstanceResult:
        """Modifies settings for a DB instance. You can change one or more database
        configuration parameters by specifying these parameters and the new
        values in the request. To learn what modifications you can make to your
        DB instance, call ``DescribeValidDBInstanceModifications`` before you
        call ``ModifyDBInstance``.

        :param db_instance_identifier: The identifier of DB instance to modify.
        :param allocated_storage: The new amount of storage in gibibytes (GiB) to allocate for the DB
        instance.
        :param db_instance_class: The new compute and memory capacity of the DB instance, for example
        ``db.
        :param db_subnet_group_name: The new DB subnet group for the DB instance.
        :param db_security_groups: A list of DB security groups to authorize on this DB instance.
        :param vpc_security_group_ids: A list of Amazon EC2 VPC security groups to associate with this DB
        instance.
        :param apply_immediately: Specifies whether the modifications in this request and any pending
        modifications are asynchronously applied as soon as possible, regardless
        of the ``PreferredMaintenanceWindow`` setting for the DB instance.
        :param master_user_password: The new password for the master user.
        :param db_parameter_group_name: The name of the DB parameter group to apply to the DB instance.
        :param backup_retention_period: The number of days to retain automated backups.
        :param preferred_backup_window: The daily time range during which automated backups are created if
        automated backups are enabled, as determined by the
        ``BackupRetentionPeriod`` parameter.
        :param preferred_maintenance_window: The weekly time range during which system maintenance can occur, which
        might result in an outage.
        :param multi_az: Specifies whether the DB instance is a Multi-AZ deployment.
        :param engine_version: The version number of the database engine to upgrade to.
        :param allow_major_version_upgrade: Specifies whether major version upgrades are allowed.
        :param auto_minor_version_upgrade: Specifies whether minor version upgrades are applied automatically to
        the DB instance during the maintenance window.
        :param license_model: The license model for the DB instance.
        :param iops: The new Provisioned IOPS (I/O operations per second) value for the RDS
        instance.
        :param option_group_name: The option group to associate the DB instance with.
        :param new_db_instance_identifier: The new identifier for the DB instance when renaming a DB instance.
        :param storage_type: The storage type to associate with the DB instance.
        :param tde_credential_arn: The ARN from the key store with which to associate the instance for TDE
        encryption.
        :param tde_credential_password: The password for the given ARN from the key store in order to access the
        device.
        :param ca_certificate_identifier: The CA certificate identifier to use for the DB instance's server
        certificate.
        :param domain: The Active Directory directory ID to move the DB instance to.
        :param domain_fqdn: The fully qualified domain name (FQDN) of an Active Directory domain.
        :param domain_ou: The Active Directory organizational unit for your DB instance to join.
        :param domain_auth_secret_arn: The ARN for the Secrets Manager secret with the credentials for the user
        joining the domain.
        :param domain_dns_ips: The IPv4 DNS IP addresses of your primary and secondary Active Directory
        domain controllers.
        :param copy_tags_to_snapshot: Specifies whether to copy all tags from the DB instance to snapshots of
        the DB instance.
        :param monitoring_interval: The interval, in seconds, between points when Enhanced Monitoring
        metrics are collected for the DB instance.
        :param db_port_number: The port number on which the database accepts connections.
        :param publicly_accessible: Specifies whether the DB instance is publicly accessible.
        :param monitoring_role_arn: The ARN for the IAM role that permits RDS to send enhanced monitoring
        metrics to Amazon CloudWatch Logs.
        :param domain_iam_role_name: The name of the IAM role to use when making API calls to the Directory
        Service.
        :param disable_domain: Specifies whether to remove the DB instance from the Active Directory
        domain.
        :param promotion_tier: The order of priority in which an Aurora Replica is promoted to the
        primary instance after a failure of the existing primary instance.
        :param enable_iam_database_authentication: Specifies whether to enable mapping of Amazon Web Services Identity and
        Access Management (IAM) accounts to database accounts.
        :param database_insights_mode: Specifies the mode of Database Insights to enable for the DB instance.
        :param enable_performance_insights: Specifies whether to enable Performance Insights for the DB instance.
        :param performance_insights_kms_key_id: The Amazon Web Services KMS key identifier for encryption of Performance
        Insights data.
        :param performance_insights_retention_period: The number of days to retain Performance Insights data.
        :param cloudwatch_logs_export_configuration: The log types to be enabled for export to CloudWatch Logs for a specific
        DB instance.
        :param processor_features: The number of CPU cores and the number of threads per core for the DB
        instance class of the DB instance.
        :param use_default_processor_features: Specifies whether the DB instance class of the DB instance uses its
        default processor features.
        :param deletion_protection: Specifies whether the DB instance has deletion protection enabled.
        :param max_allocated_storage: The upper limit in gibibytes (GiB) to which Amazon RDS can automatically
        scale the storage of the DB instance.
        :param certificate_rotation_restart: Specifies whether the DB instance is restarted when you rotate your
        SSL/TLS certificate.
        :param replica_mode: A value that sets the open mode of a replica database to either mounted
        or read-only.
        :param enable_customer_owned_ip: Specifies whether to enable a customer-owned IP address (CoIP) for an
        RDS on Outposts DB instance.
        :param aws_backup_recovery_point_arn: The Amazon Resource Name (ARN) of the recovery point in Amazon Web
        Services Backup.
        :param automation_mode: The automation mode of the RDS Custom DB instance.
        :param resume_full_automation_mode_minutes: The number of minutes to pause the automation.
        :param network_type: The network type of the DB instance.
        :param storage_throughput: The storage throughput value for the DB instance.
        :param manage_master_user_password: Specifies whether to manage the master user password with Amazon Web
        Services Secrets Manager.
        :param rotate_master_user_password: Specifies whether to rotate the secret managed by Amazon Web Services
        Secrets Manager for the master user password.
        :param master_user_secret_kms_key_id: The Amazon Web Services KMS key identifier to encrypt a secret that is
        automatically generated and managed in Amazon Web Services Secrets
        Manager.
        :param engine: The target Oracle DB engine when you convert a non-CDB to a CDB.
        :param dedicated_log_volume: Indicates whether the DB instance has a dedicated log volume (DLV)
        enabled.
        :param multi_tenant: Specifies whether the to convert your DB instance from the single-tenant
        conﬁguration to the multi-tenant conﬁguration.
        :returns: ModifyDBInstanceResult
        :raises InvalidDBInstanceStateFault:
        :raises InvalidDBSecurityGroupStateFault:
        :raises DBInstanceAlreadyExistsFault:
        :raises DBInstanceNotFoundFault:
        :raises DBSecurityGroupNotFoundFault:
        :raises DBParameterGroupNotFoundFault:
        :raises InsufficientDBInstanceCapacityFault:
        :raises StorageQuotaExceededFault:
        :raises InvalidVPCNetworkStateFault:
        :raises ProvisionedIopsNotAvailableInAZFault:
        :raises OptionGroupNotFoundFault:
        :raises DBUpgradeDependencyFailureFault:
        :raises StorageTypeNotSupportedFault:
        :raises AuthorizationNotFoundFault:
        :raises CertificateNotFoundFault:
        :raises DomainNotFoundFault:
        :raises BackupPolicyNotFoundFault:
        :raises KMSKeyNotAccessibleFault:
        :raises InvalidDBClusterStateFault:
        :raises NetworkTypeNotSupported:
        :raises TenantDatabaseQuotaExceededFault:
        """
        raise NotImplementedError

    @handler("ModifyDBParameterGroup")
    def modify_db_parameter_group(
        self,
        context: RequestContext,
        db_parameter_group_name: String,
        parameters: ParametersList,
        **kwargs,
    ) -> DBParameterGroupNameMessage:
        """Modifies the parameters of a DB parameter group. To modify more than one
        parameter, submit a list of the following: ``ParameterName``,
        ``ParameterValue``, and ``ApplyMethod``. A maximum of 20 parameters can
        be modified in a single request.

        After you modify a DB parameter group, you should wait at least 5
        minutes before creating your first DB instance that uses that DB
        parameter group as the default parameter group. This allows Amazon RDS
        to fully complete the modify operation before the parameter group is
        used as the default for a new DB instance. This is especially important
        for parameters that are critical when creating the default database for
        a DB instance, such as the character set for the default database
        defined by the ``character_set_database`` parameter. You can use the
        *Parameter Groups* option of the `Amazon RDS
        console <https://console.aws.amazon.com/rds/>`__ or the
        *DescribeDBParameters* command to verify that your DB parameter group
        has been created or modified.

        :param db_parameter_group_name: The name of the DB parameter group.
        :param parameters: An array of parameter names, values, and the application methods for the
        parameter update.
        :returns: DBParameterGroupNameMessage
        :raises DBParameterGroupNotFoundFault:
        :raises InvalidDBParameterGroupStateFault:
        """
        raise NotImplementedError

    @handler("ModifyDBProxy")
    def modify_db_proxy(
        self,
        context: RequestContext,
        db_proxy_name: String,
        new_db_proxy_name: String | None = None,
        auth: UserAuthConfigList | None = None,
        require_tls: BooleanOptional | None = None,
        idle_client_timeout: IntegerOptional | None = None,
        debug_logging: BooleanOptional | None = None,
        role_arn: String | None = None,
        security_groups: StringList | None = None,
        **kwargs,
    ) -> ModifyDBProxyResponse:
        """Changes the settings for an existing DB proxy.

        :param db_proxy_name: The identifier for the ``DBProxy`` to modify.
        :param new_db_proxy_name: The new identifier for the ``DBProxy``.
        :param auth: The new authentication settings for the ``DBProxy``.
        :param require_tls: Whether Transport Layer Security (TLS) encryption is required for
        connections to the proxy.
        :param idle_client_timeout: The number of seconds that a connection to the proxy can be inactive
        before the proxy disconnects it.
        :param debug_logging: Whether the proxy includes detailed information about SQL statements in
        its logs.
        :param role_arn: The Amazon Resource Name (ARN) of the IAM role that the proxy uses to
        access secrets in Amazon Web Services Secrets Manager.
        :param security_groups: The new list of security groups for the ``DBProxy``.
        :returns: ModifyDBProxyResponse
        :raises DBProxyNotFoundFault:
        :raises DBProxyAlreadyExistsFault:
        :raises InvalidDBProxyStateFault:
        """
        raise NotImplementedError

    @handler("ModifyDBProxyEndpoint")
    def modify_db_proxy_endpoint(
        self,
        context: RequestContext,
        db_proxy_endpoint_name: DBProxyEndpointName,
        new_db_proxy_endpoint_name: DBProxyEndpointName | None = None,
        vpc_security_group_ids: StringList | None = None,
        **kwargs,
    ) -> ModifyDBProxyEndpointResponse:
        """Changes the settings for an existing DB proxy endpoint.

        :param db_proxy_endpoint_name: The name of the DB proxy sociated with the DB proxy endpoint that you
        want to modify.
        :param new_db_proxy_endpoint_name: The new identifier for the ``DBProxyEndpoint``.
        :param vpc_security_group_ids: The VPC security group IDs for the DB proxy endpoint.
        :returns: ModifyDBProxyEndpointResponse
        :raises DBProxyEndpointNotFoundFault:
        :raises DBProxyEndpointAlreadyExistsFault:
        :raises InvalidDBProxyEndpointStateFault:
        :raises InvalidDBProxyStateFault:
        """
        raise NotImplementedError

    @handler("ModifyDBProxyTargetGroup")
    def modify_db_proxy_target_group(
        self,
        context: RequestContext,
        target_group_name: String,
        db_proxy_name: String,
        connection_pool_config: ConnectionPoolConfiguration | None = None,
        new_name: String | None = None,
        **kwargs,
    ) -> ModifyDBProxyTargetGroupResponse:
        """Modifies the properties of a ``DBProxyTargetGroup``.

        :param target_group_name: The name of the target group to modify.
        :param db_proxy_name: The name of the proxy.
        :param connection_pool_config: The settings that determine the size and behavior of the connection pool
        for the target group.
        :param new_name: The new name for the modified ``DBProxyTarget``.
        :returns: ModifyDBProxyTargetGroupResponse
        :raises DBProxyNotFoundFault:
        :raises DBProxyTargetGroupNotFoundFault:
        :raises InvalidDBProxyStateFault:
        """
        raise NotImplementedError

    @handler("ModifyDBRecommendation")
    def modify_db_recommendation(
        self,
        context: RequestContext,
        recommendation_id: String,
        locale: String | None = None,
        status: String | None = None,
        recommended_action_updates: RecommendedActionUpdateList | None = None,
        **kwargs,
    ) -> DBRecommendationMessage:
        """Updates the recommendation status and recommended action status for the
        specified recommendation.

        :param recommendation_id: The identifier of the recommendation to update.
        :param locale: The language of the modified recommendation.
        :param status: The recommendation status to update.
        :param recommended_action_updates: The list of recommended action status to update.
        :returns: DBRecommendationMessage
        """
        raise NotImplementedError

    @handler("ModifyDBShardGroup")
    def modify_db_shard_group(
        self,
        context: RequestContext,
        db_shard_group_identifier: DBShardGroupIdentifier,
        max_acu: DoubleOptional | None = None,
        min_acu: DoubleOptional | None = None,
        compute_redundancy: IntegerOptional | None = None,
        **kwargs,
    ) -> DBShardGroup:
        """Modifies the settings of an Aurora Limitless Database DB shard group.
        You can change one or more settings by specifying these parameters and
        the new values in the request.

        :param db_shard_group_identifier: The name of the DB shard group to modify.
        :param max_acu: The maximum capacity of the DB shard group in Aurora capacity units
        (ACUs).
        :param min_acu: The minimum capacity of the DB shard group in Aurora capacity units
        (ACUs).
        :param compute_redundancy: Specifies whether to create standby DB shard groups for the DB shard
        group.
        :returns: DBShardGroup
        :raises InvalidDBClusterStateFault:
        :raises DBShardGroupAlreadyExistsFault:
        :raises DBShardGroupNotFoundFault:
        """
        raise NotImplementedError

    @handler("ModifyDBSnapshot")
    def modify_db_snapshot(
        self,
        context: RequestContext,
        db_snapshot_identifier: String,
        engine_version: String | None = None,
        option_group_name: String | None = None,
        **kwargs,
    ) -> ModifyDBSnapshotResult:
        """Updates a manual DB snapshot with a new engine version. The snapshot can
        be encrypted or unencrypted, but not shared or public.

        Amazon RDS supports upgrading DB snapshots for MySQL, PostgreSQL, and
        Oracle. This operation doesn't apply to RDS Custom or RDS for Db2.

        :param db_snapshot_identifier: The identifier of the DB snapshot to modify.
        :param engine_version: The engine version to upgrade the DB snapshot to.
        :param option_group_name: The option group to identify with the upgraded DB snapshot.
        :returns: ModifyDBSnapshotResult
        :raises DBSnapshotNotFoundFault:
        """
        raise NotImplementedError

    @handler("ModifyDBSnapshotAttribute")
    def modify_db_snapshot_attribute(
        self,
        context: RequestContext,
        db_snapshot_identifier: String,
        attribute_name: String,
        values_to_add: AttributeValueList | None = None,
        values_to_remove: AttributeValueList | None = None,
        **kwargs,
    ) -> ModifyDBSnapshotAttributeResult:
        """Adds an attribute and values to, or removes an attribute and values
        from, a manual DB snapshot.

        To share a manual DB snapshot with other Amazon Web Services accounts,
        specify ``restore`` as the ``AttributeName`` and use the ``ValuesToAdd``
        parameter to add a list of IDs of the Amazon Web Services accounts that
        are authorized to restore the manual DB snapshot. Uses the value ``all``
        to make the manual DB snapshot public, which means it can be copied or
        restored by all Amazon Web Services accounts.

        Don't add the ``all`` value for any manual DB snapshots that contain
        private information that you don't want available to all Amazon Web
        Services accounts.

        If the manual DB snapshot is encrypted, it can be shared, but only by
        specifying a list of authorized Amazon Web Services account IDs for the
        ``ValuesToAdd`` parameter. You can't use ``all`` as a value for that
        parameter in this case.

        To view which Amazon Web Services accounts have access to copy or
        restore a manual DB snapshot, or whether a manual DB snapshot public or
        private, use the DescribeDBSnapshotAttributes API operation. The
        accounts are returned as values for the ``restore`` attribute.

        :param db_snapshot_identifier: The identifier for the DB snapshot to modify the attributes for.
        :param attribute_name: The name of the DB snapshot attribute to modify.
        :param values_to_add: A list of DB snapshot attributes to add to the attribute specified by
        ``AttributeName``.
        :param values_to_remove: A list of DB snapshot attributes to remove from the attribute specified
        by ``AttributeName``.
        :returns: ModifyDBSnapshotAttributeResult
        :raises DBSnapshotNotFoundFault:
        :raises InvalidDBSnapshotStateFault:
        :raises SharedSnapshotQuotaExceededFault:
        """
        raise NotImplementedError

    @handler("ModifyDBSubnetGroup")
    def modify_db_subnet_group(
        self,
        context: RequestContext,
        db_subnet_group_name: String,
        subnet_ids: SubnetIdentifierList,
        db_subnet_group_description: String | None = None,
        **kwargs,
    ) -> ModifyDBSubnetGroupResult:
        """Modifies an existing DB subnet group. DB subnet groups must contain at
        least one subnet in at least two AZs in the Amazon Web Services Region.

        :param db_subnet_group_name: The name for the DB subnet group.
        :param subnet_ids: The EC2 subnet IDs for the DB subnet group.
        :param db_subnet_group_description: The description for the DB subnet group.
        :returns: ModifyDBSubnetGroupResult
        :raises DBSubnetGroupNotFoundFault:
        :raises DBSubnetQuotaExceededFault:
        :raises SubnetAlreadyInUse:
        :raises DBSubnetGroupDoesNotCoverEnoughAZs:
        :raises InvalidSubnet:
        """
        raise NotImplementedError

    @handler("ModifyEventSubscription")
    def modify_event_subscription(
        self,
        context: RequestContext,
        subscription_name: String,
        sns_topic_arn: String | None = None,
        source_type: String | None = None,
        event_categories: EventCategoriesList | None = None,
        enabled: BooleanOptional | None = None,
        **kwargs,
    ) -> ModifyEventSubscriptionResult:
        """Modifies an existing RDS event notification subscription. You can't
        modify the source identifiers using this call. To change source
        identifiers for a subscription, use the
        ``AddSourceIdentifierToSubscription`` and
        ``RemoveSourceIdentifierFromSubscription`` calls.

        You can see a list of the event categories for a given source type
        (``SourceType``) in
        `Events <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html>`__
        in the *Amazon RDS User Guide* or by using the
        ``DescribeEventCategories`` operation.

        :param subscription_name: The name of the RDS event notification subscription.
        :param sns_topic_arn: The Amazon Resource Name (ARN) of the SNS topic created for event
        notification.
        :param source_type: The type of source that is generating the events.
        :param event_categories: A list of event categories for a source type (``SourceType``) that you
        want to subscribe to.
        :param enabled: Specifies whether to activate the subscription.
        :returns: ModifyEventSubscriptionResult
        :raises EventSubscriptionQuotaExceededFault:
        :raises SubscriptionNotFoundFault:
        :raises SNSInvalidTopicFault:
        :raises SNSNoAuthorizationFault:
        :raises SNSTopicArnNotFoundFault:
        :raises SubscriptionCategoryNotFoundFault:
        """
        raise NotImplementedError

    @handler("ModifyGlobalCluster")
    def modify_global_cluster(
        self,
        context: RequestContext,
        global_cluster_identifier: String | None = None,
        new_global_cluster_identifier: String | None = None,
        deletion_protection: BooleanOptional | None = None,
        engine_version: String | None = None,
        allow_major_version_upgrade: BooleanOptional | None = None,
        **kwargs,
    ) -> ModifyGlobalClusterResult:
        """Modifies a setting for an Amazon Aurora global database cluster. You can
        change one or more database configuration parameters by specifying these
        parameters and the new values in the request. For more information on
        Amazon Aurora, see `What is Amazon
        Aurora? <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html>`__
        in the *Amazon Aurora User Guide*.

        This operation only applies to Aurora global database clusters.

        :param global_cluster_identifier: The cluster identifier for the global cluster to modify.
        :param new_global_cluster_identifier: The new cluster identifier for the global database cluster.
        :param deletion_protection: Specifies whether to enable deletion protection for the global database
        cluster.
        :param engine_version: The version number of the database engine to which you want to upgrade.
        :param allow_major_version_upgrade: Specifies whether to allow major version upgrades.
        :returns: ModifyGlobalClusterResult
        :raises GlobalClusterNotFoundFault:
        :raises GlobalClusterAlreadyExistsFault:
        :raises InvalidGlobalClusterStateFault:
        :raises InvalidDBClusterStateFault:
        :raises InvalidDBInstanceStateFault:
        """
        raise NotImplementedError

    @handler("ModifyIntegration")
    def modify_integration(
        self,
        context: RequestContext,
        integration_identifier: IntegrationIdentifier,
        integration_name: IntegrationName | None = None,
        data_filter: DataFilter | None = None,
        description: IntegrationDescription | None = None,
        **kwargs,
    ) -> Integration:
        """Modifies a zero-ETL integration with Amazon Redshift.

        :param integration_identifier: The unique identifier of the integration to modify.
        :param integration_name: A new name for the integration.
        :param data_filter: A new data filter for the integration.
        :param description: A new description for the integration.
        :returns: Integration
        :raises IntegrationNotFoundFault:
        :raises InvalidIntegrationStateFault:
        :raises IntegrationConflictOperationFault:
        """
        raise NotImplementedError

    @handler("ModifyOptionGroup")
    def modify_option_group(
        self,
        context: RequestContext,
        option_group_name: String,
        options_to_include: OptionConfigurationList | None = None,
        options_to_remove: OptionNamesList | None = None,
        apply_immediately: Boolean | None = None,
        **kwargs,
    ) -> ModifyOptionGroupResult:
        """Modifies an existing option group.

        :param option_group_name: The name of the option group to be modified.
        :param options_to_include: Options in this list are added to the option group or, if already
        present, the specified configuration is used to update the existing
        configuration.
        :param options_to_remove: Options in this list are removed from the option group.
        :param apply_immediately: Specifies whether to apply the change immediately or during the next
        maintenance window for each instance associated with the option group.
        :returns: ModifyOptionGroupResult
        :raises InvalidOptionGroupStateFault:
        :raises OptionGroupNotFoundFault:
        """
        raise NotImplementedError

    @handler("ModifyTenantDatabase")
    def modify_tenant_database(
        self,
        context: RequestContext,
        db_instance_identifier: String,
        tenant_db_name: String,
        master_user_password: SensitiveString | None = None,
        new_tenant_db_name: String | None = None,
        manage_master_user_password: BooleanOptional | None = None,
        rotate_master_user_password: BooleanOptional | None = None,
        master_user_secret_kms_key_id: String | None = None,
        **kwargs,
    ) -> ModifyTenantDatabaseResult:
        """Modifies an existing tenant database in a DB instance. You can change
        the tenant database name or the master user password. This operation is
        supported only for RDS for Oracle CDB instances using the multi-tenant
        configuration.

        :param db_instance_identifier: The identifier of the DB instance that contains the tenant database that
        you are modifying.
        :param tenant_db_name: The user-supplied name of the tenant database that you want to modify.
        :param master_user_password: The new password for the master user of the specified tenant database in
        your DB instance.
        :param new_tenant_db_name: The new name of the tenant database when renaming a tenant database.
        :param manage_master_user_password: Specifies whether to manage the master user password with Amazon Web
        Services Secrets Manager.
        :param rotate_master_user_password: Specifies whether to rotate the secret managed by Amazon Web Services
        Secrets Manager for the master user password.
        :param master_user_secret_kms_key_id: The Amazon Web Services KMS key identifier to encrypt a secret that is
        automatically generated and managed in Amazon Web Services Secrets
        Manager.
        :returns: ModifyTenantDatabaseResult
        :raises DBInstanceNotFoundFault:
        :raises TenantDatabaseNotFoundFault:
        :raises TenantDatabaseAlreadyExistsFault:
        :raises InvalidDBInstanceStateFault:
        :raises KMSKeyNotAccessibleFault:
        """
        raise NotImplementedError

    @handler("PromoteReadReplica")
    def promote_read_replica(
        self,
        context: RequestContext,
        db_instance_identifier: String,
        backup_retention_period: IntegerOptional | None = None,
        preferred_backup_window: String | None = None,
        **kwargs,
    ) -> PromoteReadReplicaResult:
        """Promotes a read replica DB instance to a standalone DB instance.

        -  Backup duration is a function of the amount of changes to the
           database since the previous backup. If you plan to promote a read
           replica to a standalone instance, we recommend that you enable
           backups and complete at least one backup prior to promotion. In
           addition, a read replica cannot be promoted to a standalone instance
           when it is in the ``backing-up`` status. If you have enabled backups
           on your read replica, configure the automated backup window so that
           daily backups do not interfere with read replica promotion.

        -  This command doesn't apply to Aurora MySQL, Aurora PostgreSQL, or RDS
           Custom.

        :param db_instance_identifier: The DB instance identifier.
        :param backup_retention_period: The number of days for which automated backups are retained.
        :param preferred_backup_window: The daily time range during which automated backups are created if
        automated backups are enabled, using the ``BackupRetentionPeriod``
        parameter.
        :returns: PromoteReadReplicaResult
        :raises InvalidDBInstanceStateFault:
        :raises DBInstanceNotFoundFault:
        """
        raise NotImplementedError

    @handler("PromoteReadReplicaDBCluster")
    def promote_read_replica_db_cluster(
        self, context: RequestContext, db_cluster_identifier: String, **kwargs
    ) -> PromoteReadReplicaDBClusterResult:
        """Promotes a read replica DB cluster to a standalone DB cluster.

        :param db_cluster_identifier: The identifier of the DB cluster read replica to promote.
        :returns: PromoteReadReplicaDBClusterResult
        :raises DBClusterNotFoundFault:
        :raises InvalidDBClusterStateFault:
        """
        raise NotImplementedError

    @handler("PurchaseReservedDBInstancesOffering")
    def purchase_reserved_db_instances_offering(
        self,
        context: RequestContext,
        reserved_db_instances_offering_id: String,
        reserved_db_instance_id: String | None = None,
        db_instance_count: IntegerOptional | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> PurchaseReservedDBInstancesOfferingResult:
        """Purchases a reserved DB instance offering.

        :param reserved_db_instances_offering_id: The ID of the Reserved DB instance offering to purchase.
        :param reserved_db_instance_id: Customer-specified identifier to track this reservation.
        :param db_instance_count: The number of instances to reserve.
        :param tags: A list of tags.
        :returns: PurchaseReservedDBInstancesOfferingResult
        :raises ReservedDBInstancesOfferingNotFoundFault:
        :raises ReservedDBInstanceAlreadyExistsFault:
        :raises ReservedDBInstanceQuotaExceededFault:
        """
        raise NotImplementedError

    @handler("RebootDBCluster")
    def reboot_db_cluster(
        self, context: RequestContext, db_cluster_identifier: String, **kwargs
    ) -> RebootDBClusterResult:
        """You might need to reboot your DB cluster, usually for maintenance
        reasons. For example, if you make certain modifications, or if you
        change the DB cluster parameter group associated with the DB cluster,
        reboot the DB cluster for the changes to take effect.

        Rebooting a DB cluster restarts the database engine service. Rebooting a
        DB cluster results in a momentary outage, during which the DB cluster
        status is set to rebooting.

        Use this operation only for a non-Aurora Multi-AZ DB cluster.

        For more information on Multi-AZ DB clusters, see `Multi-AZ DB cluster
        deployments <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html>`__
        in the *Amazon RDS User Guide.*

        :param db_cluster_identifier: The DB cluster identifier.
        :returns: RebootDBClusterResult
        :raises DBClusterNotFoundFault:
        :raises InvalidDBClusterStateFault:
        :raises InvalidDBInstanceStateFault:
        """
        raise NotImplementedError

    @handler("RebootDBInstance")
    def reboot_db_instance(
        self,
        context: RequestContext,
        db_instance_identifier: String,
        force_failover: BooleanOptional | None = None,
        **kwargs,
    ) -> RebootDBInstanceResult:
        """You might need to reboot your DB instance, usually for maintenance
        reasons. For example, if you make certain modifications, or if you
        change the DB parameter group associated with the DB instance, you must
        reboot the instance for the changes to take effect.

        Rebooting a DB instance restarts the database engine service. Rebooting
        a DB instance results in a momentary outage, during which the DB
        instance status is set to rebooting.

        For more information about rebooting, see `Rebooting a DB
        Instance <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_RebootInstance.html>`__
        in the *Amazon RDS User Guide.*

        This command doesn't apply to RDS Custom.

        If your DB instance is part of a Multi-AZ DB cluster, you can reboot the
        DB cluster with the ``RebootDBCluster`` operation.

        :param db_instance_identifier: The DB instance identifier.
        :param force_failover: Specifies whether the reboot is conducted through a Multi-AZ failover.
        :returns: RebootDBInstanceResult
        :raises InvalidDBInstanceStateFault:
        :raises DBInstanceNotFoundFault:
        """
        raise NotImplementedError

    @handler("RebootDBShardGroup")
    def reboot_db_shard_group(
        self, context: RequestContext, db_shard_group_identifier: DBShardGroupIdentifier, **kwargs
    ) -> DBShardGroup:
        """You might need to reboot your DB shard group, usually for maintenance
        reasons. For example, if you make certain modifications, reboot the DB
        shard group for the changes to take effect.

        This operation applies only to Aurora Limitless Database DBb shard
        groups.

        :param db_shard_group_identifier: The name of the DB shard group to reboot.
        :returns: DBShardGroup
        :raises DBShardGroupNotFoundFault:
        :raises InvalidDBShardGroupStateFault:
        """
        raise NotImplementedError

    @handler("RegisterDBProxyTargets")
    def register_db_proxy_targets(
        self,
        context: RequestContext,
        db_proxy_name: String,
        target_group_name: String | None = None,
        db_instance_identifiers: StringList | None = None,
        db_cluster_identifiers: StringList | None = None,
        **kwargs,
    ) -> RegisterDBProxyTargetsResponse:
        """Associate one or more ``DBProxyTarget`` data structures with a
        ``DBProxyTargetGroup``.

        :param db_proxy_name: The identifier of the ``DBProxy`` that is associated with the
        ``DBProxyTargetGroup``.
        :param target_group_name: The identifier of the ``DBProxyTargetGroup``.
        :param db_instance_identifiers: One or more DB instance identifiers.
        :param db_cluster_identifiers: One or more DB cluster identifiers.
        :returns: RegisterDBProxyTargetsResponse
        :raises DBProxyNotFoundFault:
        :raises DBProxyTargetGroupNotFoundFault:
        :raises DBClusterNotFoundFault:
        :raises DBInstanceNotFoundFault:
        :raises DBProxyTargetAlreadyRegisteredFault:
        :raises InvalidDBInstanceStateFault:
        :raises InvalidDBClusterStateFault:
        :raises InvalidDBProxyStateFault:
        :raises InsufficientAvailableIPsInSubnetFault:
        """
        raise NotImplementedError

    @handler("RemoveFromGlobalCluster")
    def remove_from_global_cluster(
        self,
        context: RequestContext,
        global_cluster_identifier: String | None = None,
        db_cluster_identifier: String | None = None,
        **kwargs,
    ) -> RemoveFromGlobalClusterResult:
        """Detaches an Aurora secondary cluster from an Aurora global database
        cluster. The cluster becomes a standalone cluster with read-write
        capability instead of being read-only and receiving data from a primary
        cluster in a different Region.

        This operation only applies to Aurora DB clusters.

        :param global_cluster_identifier: The cluster identifier to detach from the Aurora global database
        cluster.
        :param db_cluster_identifier: The Amazon Resource Name (ARN) identifying the cluster that was detached
        from the Aurora global database cluster.
        :returns: RemoveFromGlobalClusterResult
        :raises GlobalClusterNotFoundFault:
        :raises InvalidGlobalClusterStateFault:
        :raises DBClusterNotFoundFault:
        """
        raise NotImplementedError

    @handler("RemoveRoleFromDBCluster")
    def remove_role_from_db_cluster(
        self,
        context: RequestContext,
        db_cluster_identifier: String,
        role_arn: String,
        feature_name: String | None = None,
        **kwargs,
    ) -> None:
        """Removes the asssociation of an Amazon Web Services Identity and Access
        Management (IAM) role from a DB cluster.

        For more information on Amazon Aurora DB clusters, see `What is Amazon
        Aurora? <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html>`__
        in the *Amazon Aurora User Guide*.

        For more information on Multi-AZ DB clusters, see `Multi-AZ DB cluster
        deployments <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html>`__
        in the *Amazon RDS User Guide.*

        :param db_cluster_identifier: The name of the DB cluster to disassociate the IAM role from.
        :param role_arn: The Amazon Resource Name (ARN) of the IAM role to disassociate from the
        Aurora DB cluster, for example
        ``arn:aws:iam::123456789012:role/AuroraAccessRole``.
        :param feature_name: The name of the feature for the DB cluster that the IAM role is to be
        disassociated from.
        :raises DBClusterNotFoundFault:
        :raises DBClusterRoleNotFoundFault:
        :raises InvalidDBClusterStateFault:
        """
        raise NotImplementedError

    @handler("RemoveRoleFromDBInstance")
    def remove_role_from_db_instance(
        self,
        context: RequestContext,
        db_instance_identifier: String,
        role_arn: String,
        feature_name: String,
        **kwargs,
    ) -> None:
        """Disassociates an Amazon Web Services Identity and Access Management
        (IAM) role from a DB instance.

        :param db_instance_identifier: The name of the DB instance to disassociate the IAM role from.
        :param role_arn: The Amazon Resource Name (ARN) of the IAM role to disassociate from the
        DB instance, for example, ``arn:aws:iam::123456789012:role/AccessRole``.
        :param feature_name: The name of the feature for the DB instance that the IAM role is to be
        disassociated from.
        :raises DBInstanceNotFoundFault:
        :raises DBInstanceRoleNotFoundFault:
        :raises InvalidDBInstanceStateFault:
        """
        raise NotImplementedError

    @handler("RemoveSourceIdentifierFromSubscription")
    def remove_source_identifier_from_subscription(
        self,
        context: RequestContext,
        subscription_name: String,
        source_identifier: String,
        **kwargs,
    ) -> RemoveSourceIdentifierFromSubscriptionResult:
        """Removes a source identifier from an existing RDS event notification
        subscription.

        :param subscription_name: The name of the RDS event notification subscription you want to remove a
        source identifier from.
        :param source_identifier: The source identifier to be removed from the subscription, such as the
        **DB instance identifier** for a DB instance or the name of a security
        group.
        :returns: RemoveSourceIdentifierFromSubscriptionResult
        :raises SubscriptionNotFoundFault:
        :raises SourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("RemoveTagsFromResource")
    def remove_tags_from_resource(
        self, context: RequestContext, resource_name: String, tag_keys: KeyList, **kwargs
    ) -> None:
        """Removes metadata tags from an Amazon RDS resource.

        For an overview on tagging an Amazon RDS resource, see `Tagging Amazon
        RDS
        Resources <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html>`__
        in the *Amazon RDS User Guide* or `Tagging Amazon Aurora and Amazon RDS
        Resources <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html>`__
        in the *Amazon Aurora User Guide*.

        :param resource_name: The Amazon RDS resource that the tags are removed from.
        :param tag_keys: The tag key (name) of the tag to be removed.
        :raises DBInstanceNotFoundFault:
        :raises DBSnapshotNotFoundFault:
        :raises DBClusterNotFoundFault:
        :raises DBProxyNotFoundFault:
        :raises DBProxyTargetGroupNotFoundFault:
        :raises BlueGreenDeploymentNotFoundFault:
        :raises IntegrationNotFoundFault:
        :raises TenantDatabaseNotFoundFault:
        :raises DBSnapshotTenantDatabaseNotFoundFault:
        """
        raise NotImplementedError

    @handler("ResetDBClusterParameterGroup")
    def reset_db_cluster_parameter_group(
        self,
        context: RequestContext,
        db_cluster_parameter_group_name: String,
        reset_all_parameters: Boolean | None = None,
        parameters: ParametersList | None = None,
        **kwargs,
    ) -> DBClusterParameterGroupNameMessage:
        """Modifies the parameters of a DB cluster parameter group to the default
        value. To reset specific parameters submit a list of the following:
        ``ParameterName`` and ``ApplyMethod``. To reset the entire DB cluster
        parameter group, specify the ``DBClusterParameterGroupName`` and
        ``ResetAllParameters`` parameters.

        When resetting the entire group, dynamic parameters are updated
        immediately and static parameters are set to ``pending-reboot`` to take
        effect on the next DB instance restart or ``RebootDBInstance`` request.
        You must call ``RebootDBInstance`` for every DB instance in your DB
        cluster that you want the updated static parameter to apply to.

        For more information on Amazon Aurora DB clusters, see `What is Amazon
        Aurora? <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html>`__
        in the *Amazon Aurora User Guide*.

        For more information on Multi-AZ DB clusters, see `Multi-AZ DB cluster
        deployments <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html>`__
        in the *Amazon RDS User Guide.*

        :param db_cluster_parameter_group_name: The name of the DB cluster parameter group to reset.
        :param reset_all_parameters: Specifies whether to reset all parameters in the DB cluster parameter
        group to their default values.
        :param parameters: A list of parameter names in the DB cluster parameter group to reset to
        the default values.
        :returns: DBClusterParameterGroupNameMessage
        :raises InvalidDBParameterGroupStateFault:
        :raises DBParameterGroupNotFoundFault:
        """
        raise NotImplementedError

    @handler("ResetDBParameterGroup")
    def reset_db_parameter_group(
        self,
        context: RequestContext,
        db_parameter_group_name: String,
        reset_all_parameters: Boolean | None = None,
        parameters: ParametersList | None = None,
        **kwargs,
    ) -> DBParameterGroupNameMessage:
        """Modifies the parameters of a DB parameter group to the engine/system
        default value. To reset specific parameters, provide a list of the
        following: ``ParameterName`` and ``ApplyMethod``. To reset the entire DB
        parameter group, specify the ``DBParameterGroup`` name and
        ``ResetAllParameters`` parameters. When resetting the entire group,
        dynamic parameters are updated immediately and static parameters are set
        to ``pending-reboot`` to take effect on the next DB instance restart or
        ``RebootDBInstance`` request.

        :param db_parameter_group_name: The name of the DB parameter group.
        :param reset_all_parameters: Specifies whether to reset all parameters in the DB parameter group to
        default values.
        :param parameters: To reset the entire DB parameter group, specify the ``DBParameterGroup``
        name and ``ResetAllParameters`` parameters.
        :returns: DBParameterGroupNameMessage
        :raises InvalidDBParameterGroupStateFault:
        :raises DBParameterGroupNotFoundFault:
        """
        raise NotImplementedError

    @handler("RestoreDBClusterFromS3")
    def restore_db_cluster_from_s3(
        self,
        context: RequestContext,
        db_cluster_identifier: String,
        engine: String,
        master_username: String,
        source_engine: String,
        source_engine_version: String,
        s3_bucket_name: String,
        s3_ingestion_role_arn: String,
        availability_zones: AvailabilityZones | None = None,
        backup_retention_period: IntegerOptional | None = None,
        character_set_name: String | None = None,
        database_name: String | None = None,
        db_cluster_parameter_group_name: String | None = None,
        vpc_security_group_ids: VpcSecurityGroupIdList | None = None,
        db_subnet_group_name: String | None = None,
        engine_version: String | None = None,
        port: IntegerOptional | None = None,
        master_user_password: String | None = None,
        option_group_name: String | None = None,
        preferred_backup_window: String | None = None,
        preferred_maintenance_window: String | None = None,
        tags: TagList | None = None,
        storage_encrypted: BooleanOptional | None = None,
        kms_key_id: String | None = None,
        enable_iam_database_authentication: BooleanOptional | None = None,
        s3_prefix: String | None = None,
        backtrack_window: LongOptional | None = None,
        enable_cloudwatch_logs_exports: LogTypeList | None = None,
        deletion_protection: BooleanOptional | None = None,
        copy_tags_to_snapshot: BooleanOptional | None = None,
        domain: String | None = None,
        domain_iam_role_name: String | None = None,
        serverless_v2_scaling_configuration: ServerlessV2ScalingConfiguration | None = None,
        network_type: String | None = None,
        manage_master_user_password: BooleanOptional | None = None,
        master_user_secret_kms_key_id: String | None = None,
        storage_type: String | None = None,
        engine_lifecycle_support: String | None = None,
        **kwargs,
    ) -> RestoreDBClusterFromS3Result:
        """Creates an Amazon Aurora DB cluster from MySQL data stored in an Amazon
        S3 bucket. Amazon RDS must be authorized to access the Amazon S3 bucket
        and the data must be created using the Percona XtraBackup utility as
        described in `Migrating Data from MySQL by Using an Amazon S3
        Bucket <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrating.ExtMySQL.html#AuroraMySQL.Migrating.ExtMySQL.S3>`__
        in the *Amazon Aurora User Guide*.

        This operation only restores the DB cluster, not the DB instances for
        that DB cluster. You must invoke the ``CreateDBInstance`` operation to
        create DB instances for the restored DB cluster, specifying the
        identifier of the restored DB cluster in ``DBClusterIdentifier``. You
        can create DB instances only after the ``RestoreDBClusterFromS3``
        operation has completed and the DB cluster is available.

        For more information on Amazon Aurora, see `What is Amazon
        Aurora? <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html>`__
        in the *Amazon Aurora User Guide*.

        This operation only applies to Aurora DB clusters. The source DB engine
        must be MySQL.

        :param db_cluster_identifier: The name of the DB cluster to create from the source data in the Amazon
        S3 bucket.
        :param engine: The name of the database engine to be used for this DB cluster.
        :param master_username: The name of the master user for the restored DB cluster.
        :param source_engine: The identifier for the database engine that was backed up to create the
        files stored in the Amazon S3 bucket.
        :param source_engine_version: The version of the database that the backup files were created from.
        :param s3_bucket_name: The name of the Amazon S3 bucket that contains the data used to create
        the Amazon Aurora DB cluster.
        :param s3_ingestion_role_arn: The Amazon Resource Name (ARN) of the Amazon Web Services Identity and
        Access Management (IAM) role that authorizes Amazon RDS to access the
        Amazon S3 bucket on your behalf.
        :param availability_zones: A list of Availability Zones (AZs) where instances in the restored DB
        cluster can be created.
        :param backup_retention_period: The number of days for which automated backups of the restored DB
        cluster are retained.
        :param character_set_name: A value that indicates that the restored DB cluster should be associated
        with the specified CharacterSet.
        :param database_name: The database name for the restored DB cluster.
        :param db_cluster_parameter_group_name: The name of the DB cluster parameter group to associate with the
        restored DB cluster.
        :param vpc_security_group_ids: A list of EC2 VPC security groups to associate with the restored DB
        cluster.
        :param db_subnet_group_name: A DB subnet group to associate with the restored DB cluster.
        :param engine_version: The version number of the database engine to use.
        :param port: The port number on which the instances in the restored DB cluster accept
        connections.
        :param master_user_password: The password for the master database user.
        :param option_group_name: A value that indicates that the restored DB cluster should be associated
        with the specified option group.
        :param preferred_backup_window: The daily time range during which automated backups are created if
        automated backups are enabled using the ``BackupRetentionPeriod``
        parameter.
        :param preferred_maintenance_window: The weekly time range during which system maintenance can occur, in
        Universal Coordinated Time (UTC).
        :param tags: A list of tags.
        :param storage_encrypted: Specifies whether the restored DB cluster is encrypted.
        :param kms_key_id: The Amazon Web Services KMS key identifier for an encrypted DB cluster.
        :param enable_iam_database_authentication: Specifies whether to enable mapping of Amazon Web Services Identity and
        Access Management (IAM) accounts to database accounts.
        :param s3_prefix: The prefix for all of the file names that contain the data used to
        create the Amazon Aurora DB cluster.
        :param backtrack_window: The target backtrack window, in seconds.
        :param enable_cloudwatch_logs_exports: The list of logs that the restored DB cluster is to export to CloudWatch
        Logs.
        :param deletion_protection: Specifies whether to enable deletion protection for the DB cluster.
        :param copy_tags_to_snapshot: Specifies whether to copy all tags from the restored DB cluster to
        snapshots of the restored DB cluster.
        :param domain: Specify the Active Directory directory ID to restore the DB cluster in.
        :param domain_iam_role_name: Specify the name of the IAM role to be used when making API calls to the
        Directory Service.
        :param serverless_v2_scaling_configuration: Contains the scaling configuration of an Aurora Serverless v2 DB
        cluster.
        :param network_type: The network type of the DB cluster.
        :param manage_master_user_password: Specifies whether to manage the master user password with Amazon Web
        Services Secrets Manager.
        :param master_user_secret_kms_key_id: The Amazon Web Services KMS key identifier to encrypt a secret that is
        automatically generated and managed in Amazon Web Services Secrets
        Manager.
        :param storage_type: Specifies the storage type to be associated with the DB cluster.
        :param engine_lifecycle_support: The life cycle type for this DB cluster.
        :returns: RestoreDBClusterFromS3Result
        :raises DBClusterAlreadyExistsFault:
        :raises DBClusterQuotaExceededFault:
        :raises StorageQuotaExceededFault:
        :raises DBSubnetGroupNotFoundFault:
        :raises InvalidVPCNetworkStateFault:
        :raises InvalidDBClusterStateFault:
        :raises InvalidDBSubnetGroupStateFault:
        :raises InvalidSubnet:
        :raises InvalidS3BucketFault:
        :raises DBClusterParameterGroupNotFoundFault:
        :raises KMSKeyNotAccessibleFault:
        :raises DBClusterNotFoundFault:
        :raises DomainNotFoundFault:
        :raises InsufficientStorageClusterCapacityFault:
        :raises StorageTypeNotSupportedFault:
        """
        raise NotImplementedError

    @handler("RestoreDBClusterFromSnapshot")
    def restore_db_cluster_from_snapshot(
        self,
        context: RequestContext,
        db_cluster_identifier: String,
        snapshot_identifier: String,
        engine: String,
        availability_zones: AvailabilityZones | None = None,
        engine_version: String | None = None,
        port: IntegerOptional | None = None,
        db_subnet_group_name: String | None = None,
        database_name: String | None = None,
        option_group_name: String | None = None,
        vpc_security_group_ids: VpcSecurityGroupIdList | None = None,
        tags: TagList | None = None,
        kms_key_id: String | None = None,
        enable_iam_database_authentication: BooleanOptional | None = None,
        backtrack_window: LongOptional | None = None,
        enable_cloudwatch_logs_exports: LogTypeList | None = None,
        engine_mode: String | None = None,
        scaling_configuration: ScalingConfiguration | None = None,
        db_cluster_parameter_group_name: String | None = None,
        deletion_protection: BooleanOptional | None = None,
        copy_tags_to_snapshot: BooleanOptional | None = None,
        domain: String | None = None,
        domain_iam_role_name: String | None = None,
        db_cluster_instance_class: String | None = None,
        storage_type: String | None = None,
        iops: IntegerOptional | None = None,
        publicly_accessible: BooleanOptional | None = None,
        serverless_v2_scaling_configuration: ServerlessV2ScalingConfiguration | None = None,
        network_type: String | None = None,
        rds_custom_cluster_configuration: RdsCustomClusterConfiguration | None = None,
        monitoring_interval: IntegerOptional | None = None,
        monitoring_role_arn: String | None = None,
        enable_performance_insights: BooleanOptional | None = None,
        performance_insights_kms_key_id: String | None = None,
        performance_insights_retention_period: IntegerOptional | None = None,
        engine_lifecycle_support: String | None = None,
        **kwargs,
    ) -> RestoreDBClusterFromSnapshotResult:
        """Creates a new DB cluster from a DB snapshot or DB cluster snapshot.

        The target DB cluster is created from the source snapshot with a default
        configuration. If you don't specify a security group, the new DB cluster
        is associated with the default security group.

        This operation only restores the DB cluster, not the DB instances for
        that DB cluster. You must invoke the ``CreateDBInstance`` operation to
        create DB instances for the restored DB cluster, specifying the
        identifier of the restored DB cluster in ``DBClusterIdentifier``. You
        can create DB instances only after the ``RestoreDBClusterFromSnapshot``
        operation has completed and the DB cluster is available.

        For more information on Amazon Aurora DB clusters, see `What is Amazon
        Aurora? <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html>`__
        in the *Amazon Aurora User Guide*.

        For more information on Multi-AZ DB clusters, see `Multi-AZ DB cluster
        deployments <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html>`__
        in the *Amazon RDS User Guide.*

        :param db_cluster_identifier: The name of the DB cluster to create from the DB snapshot or DB cluster
        snapshot.
        :param snapshot_identifier: The identifier for the DB snapshot or DB cluster snapshot to restore
        from.
        :param engine: The database engine to use for the new DB cluster.
        :param availability_zones: Provides the list of Availability Zones (AZs) where instances in the
        restored DB cluster can be created.
        :param engine_version: The version of the database engine to use for the new DB cluster.
        :param port: The port number on which the new DB cluster accepts connections.
        :param db_subnet_group_name: The name of the DB subnet group to use for the new DB cluster.
        :param database_name: The database name for the restored DB cluster.
        :param option_group_name: The name of the option group to use for the restored DB cluster.
        :param vpc_security_group_ids: A list of VPC security groups that the new DB cluster will belong to.
        :param tags: The tags to be assigned to the restored DB cluster.
        :param kms_key_id: The Amazon Web Services KMS key identifier to use when restoring an
        encrypted DB cluster from a DB snapshot or DB cluster snapshot.
        :param enable_iam_database_authentication: Specifies whether to enable mapping of Amazon Web Services Identity and
        Access Management (IAM) accounts to database accounts.
        :param backtrack_window: The target backtrack window, in seconds.
        :param enable_cloudwatch_logs_exports: The list of logs that the restored DB cluster is to export to Amazon
        CloudWatch Logs.
        :param engine_mode: The DB engine mode of the DB cluster, either ``provisioned`` or
        ``serverless``.
        :param scaling_configuration: For DB clusters in ``serverless`` DB engine mode, the scaling properties
        of the DB cluster.
        :param db_cluster_parameter_group_name: The name of the DB cluster parameter group to associate with this DB
        cluster.
        :param deletion_protection: Specifies whether to enable deletion protection for the DB cluster.
        :param copy_tags_to_snapshot: Specifies whether to copy all tags from the restored DB cluster to
        snapshots of the restored DB cluster.
        :param domain: The Active Directory directory ID to restore the DB cluster in.
        :param domain_iam_role_name: The name of the IAM role to be used when making API calls to the
        Directory Service.
        :param db_cluster_instance_class: The compute and memory capacity of the each DB instance in the Multi-AZ
        DB cluster, for example db.
        :param storage_type: Specifies the storage type to be associated with the DB cluster.
        :param iops: The amount of Provisioned IOPS (input/output operations per second) to
        be initially allocated for each DB instance in the Multi-AZ DB cluster.
        :param publicly_accessible: Specifies whether the DB cluster is publicly accessible.
        :param serverless_v2_scaling_configuration: Contains the scaling configuration of an Aurora Serverless v2 DB
        cluster.
        :param network_type: The network type of the DB cluster.
        :param rds_custom_cluster_configuration: Reserved for future use.
        :param monitoring_interval: The interval, in seconds, between points when Enhanced Monitoring
        metrics are collected for the DB cluster.
        :param monitoring_role_arn: The Amazon Resource Name (ARN) for the IAM role that permits RDS to send
        Enhanced Monitoring metrics to Amazon CloudWatch Logs.
        :param enable_performance_insights: Specifies whether to turn on Performance Insights for the DB cluster.
        :param performance_insights_kms_key_id: The Amazon Web Services KMS key identifier for encryption of Performance
        Insights data.
        :param performance_insights_retention_period: The number of days to retain Performance Insights data.
        :param engine_lifecycle_support: The life cycle type for this DB cluster.
        :returns: RestoreDBClusterFromSnapshotResult
        :raises DBClusterAlreadyExistsFault:
        :raises DBClusterQuotaExceededFault:
        :raises StorageQuotaExceededFault:
        :raises DBSubnetGroupNotFoundFault:
        :raises DBSnapshotNotFoundFault:
        :raises DBClusterSnapshotNotFoundFault:
        :raises InsufficientDBClusterCapacityFault:
        :raises InsufficientStorageClusterCapacityFault:
        :raises InvalidDBSnapshotStateFault:
        :raises InvalidDBClusterSnapshotStateFault:
        :raises StorageQuotaExceededFault:
        :raises InvalidVPCNetworkStateFault:
        :raises DBSubnetGroupDoesNotCoverEnoughAZs:
        :raises InvalidRestoreFault:
        :raises DBSubnetGroupNotFoundFault:
        :raises InvalidSubnet:
        :raises OptionGroupNotFoundFault:
        :raises KMSKeyNotAccessibleFault:
        :raises DomainNotFoundFault:
        :raises DBClusterParameterGroupNotFoundFault:
        :raises InvalidDBInstanceStateFault:
        :raises InsufficientDBInstanceCapacityFault:
        """
        raise NotImplementedError

    @handler("RestoreDBClusterToPointInTime")
    def restore_db_cluster_to_point_in_time(
        self,
        context: RequestContext,
        db_cluster_identifier: String,
        restore_type: String | None = None,
        source_db_cluster_identifier: String | None = None,
        restore_to_time: TStamp | None = None,
        use_latest_restorable_time: Boolean | None = None,
        port: IntegerOptional | None = None,
        db_subnet_group_name: String | None = None,
        option_group_name: String | None = None,
        vpc_security_group_ids: VpcSecurityGroupIdList | None = None,
        tags: TagList | None = None,
        kms_key_id: String | None = None,
        enable_iam_database_authentication: BooleanOptional | None = None,
        backtrack_window: LongOptional | None = None,
        enable_cloudwatch_logs_exports: LogTypeList | None = None,
        db_cluster_parameter_group_name: String | None = None,
        deletion_protection: BooleanOptional | None = None,
        copy_tags_to_snapshot: BooleanOptional | None = None,
        domain: String | None = None,
        domain_iam_role_name: String | None = None,
        scaling_configuration: ScalingConfiguration | None = None,
        engine_mode: String | None = None,
        db_cluster_instance_class: String | None = None,
        storage_type: String | None = None,
        publicly_accessible: BooleanOptional | None = None,
        iops: IntegerOptional | None = None,
        serverless_v2_scaling_configuration: ServerlessV2ScalingConfiguration | None = None,
        network_type: String | None = None,
        source_db_cluster_resource_id: String | None = None,
        rds_custom_cluster_configuration: RdsCustomClusterConfiguration | None = None,
        monitoring_interval: IntegerOptional | None = None,
        monitoring_role_arn: String | None = None,
        enable_performance_insights: BooleanOptional | None = None,
        performance_insights_kms_key_id: String | None = None,
        performance_insights_retention_period: IntegerOptional | None = None,
        engine_lifecycle_support: String | None = None,
        **kwargs,
    ) -> RestoreDBClusterToPointInTimeResult:
        """Restores a DB cluster to an arbitrary point in time. Users can restore
        to any point in time before ``LatestRestorableTime`` for up to
        ``BackupRetentionPeriod`` days. The target DB cluster is created from
        the source DB cluster with the same configuration as the original DB
        cluster, except that the new DB cluster is created with the default DB
        security group. Unless the ``RestoreType`` is set to ``copy-on-write``,
        the restore may occur in a different Availability Zone (AZ) from the
        original DB cluster. The AZ where RDS restores the DB cluster depends on
        the AZs in the specified subnet group.

        For Aurora, this operation only restores the DB cluster, not the DB
        instances for that DB cluster. You must invoke the ``CreateDBInstance``
        operation to create DB instances for the restored DB cluster, specifying
        the identifier of the restored DB cluster in ``DBClusterIdentifier``.
        You can create DB instances only after the
        ``RestoreDBClusterToPointInTime`` operation has completed and the DB
        cluster is available.

        For more information on Amazon Aurora DB clusters, see `What is Amazon
        Aurora? <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html>`__
        in the *Amazon Aurora User Guide*.

        For more information on Multi-AZ DB clusters, see `Multi-AZ DB cluster
        deployments <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html>`__
        in the *Amazon RDS User Guide.*

        :param db_cluster_identifier: The name of the new DB cluster to be created.
        :param restore_type: The type of restore to be performed.
        :param source_db_cluster_identifier: The identifier of the source DB cluster from which to restore.
        :param restore_to_time: The date and time to restore the DB cluster to.
        :param use_latest_restorable_time: Specifies whether to restore the DB cluster to the latest restorable
        backup time.
        :param port: The port number on which the new DB cluster accepts connections.
        :param db_subnet_group_name: The DB subnet group name to use for the new DB cluster.
        :param option_group_name: The name of the option group for the new DB cluster.
        :param vpc_security_group_ids: A list of VPC security groups that the new DB cluster belongs to.
        :param tags: A list of tags.
        :param kms_key_id: The Amazon Web Services KMS key identifier to use when restoring an
        encrypted DB cluster from an encrypted DB cluster.
        :param enable_iam_database_authentication: Specifies whether to enable mapping of Amazon Web Services Identity and
        Access Management (IAM) accounts to database accounts.
        :param backtrack_window: The target backtrack window, in seconds.
        :param enable_cloudwatch_logs_exports: The list of logs that the restored DB cluster is to export to CloudWatch
        Logs.
        :param db_cluster_parameter_group_name: The name of the custom DB cluster parameter group to associate with this
        DB cluster.
        :param deletion_protection: Specifies whether to enable deletion protection for the DB cluster.
        :param copy_tags_to_snapshot: Specifies whether to copy all tags from the restored DB cluster to
        snapshots of the restored DB cluster.
        :param domain: The Active Directory directory ID to restore the DB cluster in.
        :param domain_iam_role_name: The name of the IAM role to be used when making API calls to the
        Directory Service.
        :param scaling_configuration: For DB clusters in ``serverless`` DB engine mode, the scaling properties
        of the DB cluster.
        :param engine_mode: The engine mode of the new cluster.
        :param db_cluster_instance_class: The compute and memory capacity of the each DB instance in the Multi-AZ
        DB cluster, for example db.
        :param storage_type: Specifies the storage type to be associated with the DB cluster.
        :param publicly_accessible: Specifies whether the DB cluster is publicly accessible.
        :param iops: The amount of Provisioned IOPS (input/output operations per second) to
        be initially allocated for each DB instance in the Multi-AZ DB cluster.
        :param serverless_v2_scaling_configuration: Contains the scaling configuration of an Aurora Serverless v2 DB
        cluster.
        :param network_type: The network type of the DB cluster.
        :param source_db_cluster_resource_id: The resource ID of the source DB cluster from which to restore.
        :param rds_custom_cluster_configuration: Reserved for future use.
        :param monitoring_interval: The interval, in seconds, between points when Enhanced Monitoring
        metrics are collected for the DB cluster.
        :param monitoring_role_arn: The Amazon Resource Name (ARN) for the IAM role that permits RDS to send
        Enhanced Monitoring metrics to Amazon CloudWatch Logs.
        :param enable_performance_insights: Specifies whether to turn on Performance Insights for the DB cluster.
        :param performance_insights_kms_key_id: The Amazon Web Services KMS key identifier for encryption of Performance
        Insights data.
        :param performance_insights_retention_period: The number of days to retain Performance Insights data.
        :param engine_lifecycle_support: The life cycle type for this DB cluster.
        :returns: RestoreDBClusterToPointInTimeResult
        :raises DBClusterAlreadyExistsFault:
        :raises DBClusterNotFoundFault:
        :raises DBClusterQuotaExceededFault:
        :raises DBClusterSnapshotNotFoundFault:
        :raises DBSubnetGroupNotFoundFault:
        :raises InsufficientDBClusterCapacityFault:
        :raises InsufficientStorageClusterCapacityFault:
        :raises InvalidDBClusterSnapshotStateFault:
        :raises InvalidDBClusterStateFault:
        :raises InvalidDBSnapshotStateFault:
        :raises InvalidRestoreFault:
        :raises InvalidSubnet:
        :raises InvalidVPCNetworkStateFault:
        :raises KMSKeyNotAccessibleFault:
        :raises OptionGroupNotFoundFault:
        :raises StorageQuotaExceededFault:
        :raises DomainNotFoundFault:
        :raises DBClusterParameterGroupNotFoundFault:
        :raises DBClusterAutomatedBackupNotFoundFault:
        :raises InsufficientDBInstanceCapacityFault:
        """
        raise NotImplementedError

    @handler("RestoreDBInstanceFromDBSnapshot")
    def restore_db_instance_from_db_snapshot(
        self,
        context: RequestContext,
        db_instance_identifier: String,
        db_snapshot_identifier: String | None = None,
        db_instance_class: String | None = None,
        port: IntegerOptional | None = None,
        availability_zone: String | None = None,
        db_subnet_group_name: String | None = None,
        multi_az: BooleanOptional | None = None,
        publicly_accessible: BooleanOptional | None = None,
        auto_minor_version_upgrade: BooleanOptional | None = None,
        license_model: String | None = None,
        db_name: String | None = None,
        engine: String | None = None,
        iops: IntegerOptional | None = None,
        option_group_name: String | None = None,
        tags: TagList | None = None,
        storage_type: String | None = None,
        tde_credential_arn: String | None = None,
        tde_credential_password: String | None = None,
        vpc_security_group_ids: VpcSecurityGroupIdList | None = None,
        domain: String | None = None,
        domain_fqdn: String | None = None,
        domain_ou: String | None = None,
        domain_auth_secret_arn: String | None = None,
        domain_dns_ips: StringList | None = None,
        copy_tags_to_snapshot: BooleanOptional | None = None,
        domain_iam_role_name: String | None = None,
        enable_iam_database_authentication: BooleanOptional | None = None,
        enable_cloudwatch_logs_exports: LogTypeList | None = None,
        processor_features: ProcessorFeatureList | None = None,
        use_default_processor_features: BooleanOptional | None = None,
        db_parameter_group_name: String | None = None,
        deletion_protection: BooleanOptional | None = None,
        enable_customer_owned_ip: BooleanOptional | None = None,
        custom_iam_instance_profile: String | None = None,
        backup_target: String | None = None,
        network_type: String | None = None,
        storage_throughput: IntegerOptional | None = None,
        db_cluster_snapshot_identifier: String | None = None,
        allocated_storage: IntegerOptional | None = None,
        dedicated_log_volume: BooleanOptional | None = None,
        ca_certificate_identifier: String | None = None,
        engine_lifecycle_support: String | None = None,
        manage_master_user_password: BooleanOptional | None = None,
        master_user_secret_kms_key_id: String | None = None,
        **kwargs,
    ) -> RestoreDBInstanceFromDBSnapshotResult:
        """Creates a new DB instance from a DB snapshot. The target database is
        created from the source database restore point with most of the source's
        original configuration, including the default security group and DB
        parameter group. By default, the new DB instance is created as a
        Single-AZ deployment, except when the instance is a SQL Server instance
        that has an option group associated with mirroring. In this case, the
        instance becomes a Multi-AZ deployment, not a Single-AZ deployment.

        If you want to replace your original DB instance with the new, restored
        DB instance, then rename your original DB instance before you call the
        ``RestoreDBInstanceFromDBSnapshot`` operation. RDS doesn't allow two DB
        instances with the same name. After you have renamed your original DB
        instance with a different identifier, then you can pass the original
        name of the DB instance as the ``DBInstanceIdentifier`` in the call to
        the ``RestoreDBInstanceFromDBSnapshot`` operation. The result is that
        you replace the original DB instance with the DB instance created from
        the snapshot.

        If you are restoring from a shared manual DB snapshot, the
        ``DBSnapshotIdentifier`` must be the ARN of the shared DB snapshot.

        To restore from a DB snapshot with an unsupported engine version, you
        must first upgrade the engine version of the snapshot. For more
        information about upgrading a RDS for MySQL DB snapshot engine version,
        see `Upgrading a MySQL DB snapshot engine
        version <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-upgrade-snapshot.html>`__.
        For more information about upgrading a RDS for PostgreSQL DB snapshot
        engine version, `Upgrading a PostgreSQL DB snapshot engine
        version <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBSnapshot.PostgreSQL.html>`__.

        This command doesn't apply to Aurora MySQL and Aurora PostgreSQL. For
        Aurora, use ``RestoreDBClusterFromSnapshot``.

        :param db_instance_identifier: The name of the DB instance to create from the DB snapshot.
        :param db_snapshot_identifier: The identifier for the DB snapshot to restore from.
        :param db_instance_class: The compute and memory capacity of the Amazon RDS DB instance, for
        example db.
        :param port: The port number on which the database accepts connections.
        :param availability_zone: The Availability Zone (AZ) where the DB instance will be created.
        :param db_subnet_group_name: The name of the DB subnet group to use for the new instance.
        :param multi_az: Specifies whether the DB instance is a Multi-AZ deployment.
        :param publicly_accessible: Specifies whether the DB instance is publicly accessible.
        :param auto_minor_version_upgrade: Specifies whether to automatically apply minor version upgrades to the
        DB instance during the maintenance window.
        :param license_model: License model information for the restored DB instance.
        :param db_name: The name of the database for the restored DB instance.
        :param engine: The database engine to use for the new instance.
        :param iops: Specifies the amount of provisioned IOPS for the DB instance, expressed
        in I/O operations per second.
        :param option_group_name: The name of the option group to be used for the restored DB instance.
        :param tags: A list of tags.
        :param storage_type: Specifies the storage type to be associated with the DB instance.
        :param tde_credential_arn: The ARN from the key store with which to associate the instance for TDE
        encryption.
        :param tde_credential_password: The password for the given ARN from the key store in order to access the
        device.
        :param vpc_security_group_ids: A list of EC2 VPC security groups to associate with this DB instance.
        :param domain: The Active Directory directory ID to restore the DB instance in.
        :param domain_fqdn: The fully qualified domain name (FQDN) of an Active Directory domain.
        :param domain_ou: The Active Directory organizational unit for your DB instance to join.
        :param domain_auth_secret_arn: The ARN for the Secrets Manager secret with the credentials for the user
        joining the domain.
        :param domain_dns_ips: The IPv4 DNS IP addresses of your primary and secondary Active Directory
        domain controllers.
        :param copy_tags_to_snapshot: Specifies whether to copy all tags from the restored DB instance to
        snapshots of the DB instance.
        :param domain_iam_role_name: The name of the IAM role to use when making API calls to the Directory
        Service.
        :param enable_iam_database_authentication: Specifies whether to enable mapping of Amazon Web Services Identity and
        Access Management (IAM) accounts to database accounts.
        :param enable_cloudwatch_logs_exports: The list of logs for the restored DB instance to export to CloudWatch
        Logs.
        :param processor_features: The number of CPU cores and the number of threads per core for the DB
        instance class of the DB instance.
        :param use_default_processor_features: Specifies whether the DB instance class of the DB instance uses its
        default processor features.
        :param db_parameter_group_name: The name of the DB parameter group to associate with this DB instance.
        :param deletion_protection: Specifies whether to enable deletion protection for the DB instance.
        :param enable_customer_owned_ip: Specifies whether to enable a customer-owned IP address (CoIP) for an
        RDS on Outposts DB instance.
        :param custom_iam_instance_profile: The instance profile associated with the underlying Amazon EC2 instance
        of an RDS Custom DB instance.
        :param backup_target: Specifies where automated backups and manual snapshots are stored for
        the restored DB instance.
        :param network_type: The network type of the DB instance.
        :param storage_throughput: Specifies the storage throughput value for the DB instance.
        :param db_cluster_snapshot_identifier: The identifier for the Multi-AZ DB cluster snapshot to restore from.
        :param allocated_storage: The amount of storage (in gibibytes) to allocate initially for the DB
        instance.
        :param dedicated_log_volume: Specifies whether to enable a dedicated log volume (DLV) for the DB
        instance.
        :param ca_certificate_identifier: The CA certificate identifier to use for the DB instance's server
        certificate.
        :param engine_lifecycle_support: The life cycle type for this DB instance.
        :param manage_master_user_password: Specifies whether to manage the master user password with Amazon Web
        Services Secrets Manager in the restored DB instance.
        :param master_user_secret_kms_key_id: The Amazon Web Services KMS key identifier to encrypt a secret that is
        automatically generated and managed in Amazon Web Services Secrets
        Manager.
        :returns: RestoreDBInstanceFromDBSnapshotResult
        :raises DBInstanceAlreadyExistsFault:
        :raises DBSnapshotNotFoundFault:
        :raises InstanceQuotaExceededFault:
        :raises InsufficientDBInstanceCapacityFault:
        :raises InvalidDBSnapshotStateFault:
        :raises StorageQuotaExceededFault:
        :raises InvalidVPCNetworkStateFault:
        :raises InvalidRestoreFault:
        :raises DBSubnetGroupNotFoundFault:
        :raises DBSubnetGroupDoesNotCoverEnoughAZs:
        :raises InvalidSubnet:
        :raises ProvisionedIopsNotAvailableInAZFault:
        :raises OptionGroupNotFoundFault:
        :raises StorageTypeNotSupportedFault:
        :raises AuthorizationNotFoundFault:
        :raises KMSKeyNotAccessibleFault:
        :raises DBSecurityGroupNotFoundFault:
        :raises DomainNotFoundFault:
        :raises DBParameterGroupNotFoundFault:
        :raises BackupPolicyNotFoundFault:
        :raises NetworkTypeNotSupported:
        :raises DBClusterSnapshotNotFoundFault:
        :raises CertificateNotFoundFault:
        :raises TenantDatabaseQuotaExceededFault:
        """
        raise NotImplementedError

    @handler("RestoreDBInstanceFromS3")
    def restore_db_instance_from_s3(
        self,
        context: RequestContext,
        db_instance_identifier: String,
        db_instance_class: String,
        engine: String,
        source_engine: String,
        source_engine_version: String,
        s3_bucket_name: String,
        s3_ingestion_role_arn: String,
        db_name: String | None = None,
        allocated_storage: IntegerOptional | None = None,
        master_username: String | None = None,
        master_user_password: String | None = None,
        db_security_groups: DBSecurityGroupNameList | None = None,
        vpc_security_group_ids: VpcSecurityGroupIdList | None = None,
        availability_zone: String | None = None,
        db_subnet_group_name: String | None = None,
        preferred_maintenance_window: String | None = None,
        db_parameter_group_name: String | None = None,
        backup_retention_period: IntegerOptional | None = None,
        preferred_backup_window: String | None = None,
        port: IntegerOptional | None = None,
        multi_az: BooleanOptional | None = None,
        engine_version: String | None = None,
        auto_minor_version_upgrade: BooleanOptional | None = None,
        license_model: String | None = None,
        iops: IntegerOptional | None = None,
        option_group_name: String | None = None,
        publicly_accessible: BooleanOptional | None = None,
        tags: TagList | None = None,
        storage_type: String | None = None,
        storage_encrypted: BooleanOptional | None = None,
        kms_key_id: String | None = None,
        copy_tags_to_snapshot: BooleanOptional | None = None,
        monitoring_interval: IntegerOptional | None = None,
        monitoring_role_arn: String | None = None,
        enable_iam_database_authentication: BooleanOptional | None = None,
        s3_prefix: String | None = None,
        database_insights_mode: DatabaseInsightsMode | None = None,
        enable_performance_insights: BooleanOptional | None = None,
        performance_insights_kms_key_id: String | None = None,
        performance_insights_retention_period: IntegerOptional | None = None,
        enable_cloudwatch_logs_exports: LogTypeList | None = None,
        processor_features: ProcessorFeatureList | None = None,
        use_default_processor_features: BooleanOptional | None = None,
        deletion_protection: BooleanOptional | None = None,
        max_allocated_storage: IntegerOptional | None = None,
        network_type: String | None = None,
        storage_throughput: IntegerOptional | None = None,
        manage_master_user_password: BooleanOptional | None = None,
        master_user_secret_kms_key_id: String | None = None,
        dedicated_log_volume: BooleanOptional | None = None,
        ca_certificate_identifier: String | None = None,
        engine_lifecycle_support: String | None = None,
        **kwargs,
    ) -> RestoreDBInstanceFromS3Result:
        """Amazon Relational Database Service (Amazon RDS) supports importing MySQL
        databases by using backup files. You can create a backup of your
        on-premises database, store it on Amazon Simple Storage Service (Amazon
        S3), and then restore the backup file onto a new Amazon RDS DB instance
        running MySQL. For more information, see `Importing Data into an Amazon
        RDS MySQL DB
        Instance <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.html>`__
        in the *Amazon RDS User Guide.*

        This operation doesn't apply to RDS Custom.

        :param db_instance_identifier: The DB instance identifier.
        :param db_instance_class: The compute and memory capacity of the DB instance, for example
        db.
        :param engine: The name of the database engine to be used for this instance.
        :param source_engine: The name of the engine of your source database.
        :param source_engine_version: The version of the database that the backup files were created from.
        :param s3_bucket_name: The name of your Amazon S3 bucket that contains your database backup
        file.
        :param s3_ingestion_role_arn: An Amazon Web Services Identity and Access Management (IAM) role with a
        trust policy and a permissions policy that allows Amazon RDS to access
        your Amazon S3 bucket.
        :param db_name: The name of the database to create when the DB instance is created.
        :param allocated_storage: The amount of storage (in gibibytes) to allocate initially for the DB
        instance.
        :param master_username: The name for the master user.
        :param master_user_password: The password for the master user.
        :param db_security_groups: A list of DB security groups to associate with this DB instance.
        :param vpc_security_group_ids: A list of VPC security groups to associate with this DB instance.
        :param availability_zone: The Availability Zone that the DB instance is created in.
        :param db_subnet_group_name: A DB subnet group to associate with this DB instance.
        :param preferred_maintenance_window: The time range each week during which system maintenance can occur, in
        Universal Coordinated Time (UTC).
        :param db_parameter_group_name: The name of the DB parameter group to associate with this DB instance.
        :param backup_retention_period: The number of days for which automated backups are retained.
        :param preferred_backup_window: The time range each day during which automated backups are created if
        automated backups are enabled.
        :param port: The port number on which the database accepts connections.
        :param multi_az: Specifies whether the DB instance is a Multi-AZ deployment.
        :param engine_version: The version number of the database engine to use.
        :param auto_minor_version_upgrade: Specifies whether to automatically apply minor engine upgrades to the DB
        instance during the maintenance window.
        :param license_model: The license model for this DB instance.
        :param iops: The amount of Provisioned IOPS (input/output operations per second) to
        allocate initially for the DB instance.
        :param option_group_name: The name of the option group to associate with this DB instance.
        :param publicly_accessible: Specifies whether the DB instance is publicly accessible.
        :param tags: A list of tags to associate with this DB instance.
        :param storage_type: Specifies the storage type to be associated with the DB instance.
        :param storage_encrypted: Specifies whether the new DB instance is encrypted or not.
        :param kms_key_id: The Amazon Web Services KMS key identifier for an encrypted DB instance.
        :param copy_tags_to_snapshot: Specifies whether to copy all tags from the DB instance to snapshots of
        the DB instance.
        :param monitoring_interval: The interval, in seconds, between points when Enhanced Monitoring
        metrics are collected for the DB instance.
        :param monitoring_role_arn: The ARN for the IAM role that permits RDS to send enhanced monitoring
        metrics to Amazon CloudWatch Logs.
        :param enable_iam_database_authentication: Specifies whether to enable mapping of Amazon Web Services Identity and
        Access Management (IAM) accounts to database accounts.
        :param s3_prefix: The prefix of your Amazon S3 bucket.
        :param database_insights_mode: Specifies the mode of Database Insights to enable for the DB instance.
        :param enable_performance_insights: Specifies whether to enable Performance Insights for the DB instance.
        :param performance_insights_kms_key_id: The Amazon Web Services KMS key identifier for encryption of Performance
        Insights data.
        :param performance_insights_retention_period: The number of days to retain Performance Insights data.
        :param enable_cloudwatch_logs_exports: The list of logs that the restored DB instance is to export to
        CloudWatch Logs.
        :param processor_features: The number of CPU cores and the number of threads per core for the DB
        instance class of the DB instance.
        :param use_default_processor_features: Specifies whether the DB instance class of the DB instance uses its
        default processor features.
        :param deletion_protection: Specifies whether to enable deletion protection for the DB instance.
        :param max_allocated_storage: The upper limit in gibibytes (GiB) to which Amazon RDS can automatically
        scale the storage of the DB instance.
        :param network_type: The network type of the DB instance.
        :param storage_throughput: Specifies the storage throughput value for the DB instance.
        :param manage_master_user_password: Specifies whether to manage the master user password with Amazon Web
        Services Secrets Manager.
        :param master_user_secret_kms_key_id: The Amazon Web Services KMS key identifier to encrypt a secret that is
        automatically generated and managed in Amazon Web Services Secrets
        Manager.
        :param dedicated_log_volume: Specifies whether to enable a dedicated log volume (DLV) for the DB
        instance.
        :param ca_certificate_identifier: The CA certificate identifier to use for the DB instance's server
        certificate.
        :param engine_lifecycle_support: The life cycle type for this DB instance.
        :returns: RestoreDBInstanceFromS3Result
        :raises DBInstanceAlreadyExistsFault:
        :raises InsufficientDBInstanceCapacityFault:
        :raises DBParameterGroupNotFoundFault:
        :raises DBSecurityGroupNotFoundFault:
        :raises InstanceQuotaExceededFault:
        :raises StorageQuotaExceededFault:
        :raises DBSubnetGroupNotFoundFault:
        :raises DBSubnetGroupDoesNotCoverEnoughAZs:
        :raises InvalidSubnet:
        :raises InvalidVPCNetworkStateFault:
        :raises InvalidS3BucketFault:
        :raises ProvisionedIopsNotAvailableInAZFault:
        :raises OptionGroupNotFoundFault:
        :raises StorageTypeNotSupportedFault:
        :raises AuthorizationNotFoundFault:
        :raises KMSKeyNotAccessibleFault:
        :raises BackupPolicyNotFoundFault:
        :raises NetworkTypeNotSupported:
        :raises CertificateNotFoundFault:
        """
        raise NotImplementedError

    @handler("RestoreDBInstanceToPointInTime")
    def restore_db_instance_to_point_in_time(
        self,
        context: RequestContext,
        target_db_instance_identifier: String,
        source_db_instance_identifier: String | None = None,
        restore_time: TStamp | None = None,
        use_latest_restorable_time: Boolean | None = None,
        db_instance_class: String | None = None,
        port: IntegerOptional | None = None,
        availability_zone: String | None = None,
        db_subnet_group_name: String | None = None,
        multi_az: BooleanOptional | None = None,
        publicly_accessible: BooleanOptional | None = None,
        auto_minor_version_upgrade: BooleanOptional | None = None,
        license_model: String | None = None,
        db_name: String | None = None,
        engine: String | None = None,
        iops: IntegerOptional | None = None,
        option_group_name: String | None = None,
        copy_tags_to_snapshot: BooleanOptional | None = None,
        tags: TagList | None = None,
        storage_type: String | None = None,
        tde_credential_arn: String | None = None,
        tde_credential_password: String | None = None,
        vpc_security_group_ids: VpcSecurityGroupIdList | None = None,
        domain: String | None = None,
        domain_iam_role_name: String | None = None,
        domain_fqdn: String | None = None,
        domain_ou: String | None = None,
        domain_auth_secret_arn: String | None = None,
        domain_dns_ips: StringList | None = None,
        enable_iam_database_authentication: BooleanOptional | None = None,
        enable_cloudwatch_logs_exports: LogTypeList | None = None,
        processor_features: ProcessorFeatureList | None = None,
        use_default_processor_features: BooleanOptional | None = None,
        db_parameter_group_name: String | None = None,
        deletion_protection: BooleanOptional | None = None,
        source_dbi_resource_id: String | None = None,
        max_allocated_storage: IntegerOptional | None = None,
        source_db_instance_automated_backups_arn: String | None = None,
        enable_customer_owned_ip: BooleanOptional | None = None,
        custom_iam_instance_profile: String | None = None,
        backup_target: String | None = None,
        network_type: String | None = None,
        storage_throughput: IntegerOptional | None = None,
        allocated_storage: IntegerOptional | None = None,
        dedicated_log_volume: BooleanOptional | None = None,
        ca_certificate_identifier: String | None = None,
        engine_lifecycle_support: String | None = None,
        manage_master_user_password: BooleanOptional | None = None,
        master_user_secret_kms_key_id: String | None = None,
        **kwargs,
    ) -> RestoreDBInstanceToPointInTimeResult:
        """Restores a DB instance to an arbitrary point in time. You can restore to
        any point in time before the time identified by the
        ``LatestRestorableTime`` property. You can restore to a point up to the
        number of days specified by the ``BackupRetentionPeriod`` property.

        The target database is created with most of the original configuration,
        but in a system-selected Availability Zone, with the default security
        group, the default subnet group, and the default DB parameter group. By
        default, the new DB instance is created as a single-AZ deployment except
        when the instance is a SQL Server instance that has an option group that
        is associated with mirroring; in this case, the instance becomes a
        mirrored deployment and not a single-AZ deployment.

        This operation doesn't apply to Aurora MySQL and Aurora PostgreSQL. For
        Aurora, use ``RestoreDBClusterToPointInTime``.

        :param target_db_instance_identifier: The name of the new DB instance to create.
        :param source_db_instance_identifier: The identifier of the source DB instance from which to restore.
        :param restore_time: The date and time to restore from.
        :param use_latest_restorable_time: Specifies whether the DB instance is restored from the latest backup
        time.
        :param db_instance_class: The compute and memory capacity of the Amazon RDS DB instance, for
        example db.
        :param port: The port number on which the database accepts connections.
        :param availability_zone: The Availability Zone (AZ) where the DB instance will be created.
        :param db_subnet_group_name: The DB subnet group name to use for the new instance.
        :param multi_az: Secifies whether the DB instance is a Multi-AZ deployment.
        :param publicly_accessible: Specifies whether the DB instance is publicly accessible.
        :param auto_minor_version_upgrade: Specifies whether minor version upgrades are applied automatically to
        the DB instance during the maintenance window.
        :param license_model: The license model information for the restored DB instance.
        :param db_name: The database name for the restored DB instance.
        :param engine: The database engine to use for the new instance.
        :param iops: The amount of Provisioned IOPS (input/output operations per second) to
        initially allocate for the DB instance.
        :param option_group_name: The name of the option group to use for the restored DB instance.
        :param copy_tags_to_snapshot: Specifies whether to copy all tags from the restored DB instance to
        snapshots of the DB instance.
        :param tags: A list of tags.
        :param storage_type: The storage type to associate with the DB instance.
        :param tde_credential_arn: The ARN from the key store with which to associate the instance for TDE
        encryption.
        :param tde_credential_password: The password for the given ARN from the key store in order to access the
        device.
        :param vpc_security_group_ids: A list of EC2 VPC security groups to associate with this DB instance.
        :param domain: The Active Directory directory ID to restore the DB instance in.
        :param domain_iam_role_name: The name of the IAM role to use when making API calls to the Directory
        Service.
        :param domain_fqdn: The fully qualified domain name (FQDN) of an Active Directory domain.
        :param domain_ou: The Active Directory organizational unit for your DB instance to join.
        :param domain_auth_secret_arn: The ARN for the Secrets Manager secret with the credentials for the user
        joining the domain.
        :param domain_dns_ips: The IPv4 DNS IP addresses of your primary and secondary Active Directory
        domain controllers.
        :param enable_iam_database_authentication: Specifies whether to enable mapping of Amazon Web Services Identity and
        Access Management (IAM) accounts to database accounts.
        :param enable_cloudwatch_logs_exports: The list of logs that the restored DB instance is to export to
        CloudWatch Logs.
        :param processor_features: The number of CPU cores and the number of threads per core for the DB
        instance class of the DB instance.
        :param use_default_processor_features: Specifies whether the DB instance class of the DB instance uses its
        default processor features.
        :param db_parameter_group_name: The name of the DB parameter group to associate with this DB instance.
        :param deletion_protection: Specifies whether the DB instance has deletion protection enabled.
        :param source_dbi_resource_id: The resource ID of the source DB instance from which to restore.
        :param max_allocated_storage: The upper limit in gibibytes (GiB) to which Amazon RDS can automatically
        scale the storage of the DB instance.
        :param source_db_instance_automated_backups_arn: The Amazon Resource Name (ARN) of the replicated automated backups from
        which to restore, for example,
        ``arn:aws:rds:us-east-1:123456789012:auto-backup:ab-L2IJCEXJP7XQ7HOJ4SIEXAMPLE``.
        :param enable_customer_owned_ip: Specifies whether to enable a customer-owned IP address (CoIP) for an
        RDS on Outposts DB instance.
        :param custom_iam_instance_profile: The instance profile associated with the underlying Amazon EC2 instance
        of an RDS Custom DB instance.
        :param backup_target: The location for storing automated backups and manual snapshots for the
        restored DB instance.
        :param network_type: The network type of the DB instance.
        :param storage_throughput: The storage throughput value for the DB instance.
        :param allocated_storage: The amount of storage (in gibibytes) to allocate initially for the DB
        instance.
        :param dedicated_log_volume: Specifies whether to enable a dedicated log volume (DLV) for the DB
        instance.
        :param ca_certificate_identifier: The CA certificate identifier to use for the DB instance's server
        certificate.
        :param engine_lifecycle_support: The life cycle type for this DB instance.
        :param manage_master_user_password: Specifies whether to manage the master user password with Amazon Web
        Services Secrets Manager in the restored DB instance.
        :param master_user_secret_kms_key_id: The Amazon Web Services KMS key identifier to encrypt a secret that is
        automatically generated and managed in Amazon Web Services Secrets
        Manager.
        :returns: RestoreDBInstanceToPointInTimeResult
        :raises DBInstanceAlreadyExistsFault:
        :raises DBInstanceNotFoundFault:
        :raises InstanceQuotaExceededFault:
        :raises InsufficientDBInstanceCapacityFault:
        :raises InvalidDBInstanceStateFault:
        :raises PointInTimeRestoreNotEnabledFault:
        :raises StorageQuotaExceededFault:
        :raises InvalidVPCNetworkStateFault:
        :raises InvalidRestoreFault:
        :raises DBSubnetGroupNotFoundFault:
        :raises DBSubnetGroupDoesNotCoverEnoughAZs:
        :raises InvalidSubnet:
        :raises ProvisionedIopsNotAvailableInAZFault:
        :raises OptionGroupNotFoundFault:
        :raises StorageTypeNotSupportedFault:
        :raises AuthorizationNotFoundFault:
        :raises KMSKeyNotAccessibleFault:
        :raises DBSecurityGroupNotFoundFault:
        :raises DomainNotFoundFault:
        :raises BackupPolicyNotFoundFault:
        :raises DBParameterGroupNotFoundFault:
        :raises DBInstanceAutomatedBackupNotFoundFault:
        :raises NetworkTypeNotSupported:
        :raises TenantDatabaseQuotaExceededFault:
        :raises CertificateNotFoundFault:
        """
        raise NotImplementedError

    @handler("RevokeDBSecurityGroupIngress")
    def revoke_db_security_group_ingress(
        self,
        context: RequestContext,
        db_security_group_name: String,
        cidrip: String | None = None,
        ec2_security_group_name: String | None = None,
        ec2_security_group_id: String | None = None,
        ec2_security_group_owner_id: String | None = None,
        **kwargs,
    ) -> RevokeDBSecurityGroupIngressResult:
        """Revokes ingress from a DBSecurityGroup for previously authorized IP
        ranges or EC2 or VPC security groups. Required parameters for this API
        are one of CIDRIP, EC2SecurityGroupId for VPC, or
        (EC2SecurityGroupOwnerId and either EC2SecurityGroupName or
        EC2SecurityGroupId).

        EC2-Classic was retired on August 15, 2022. If you haven't migrated from
        EC2-Classic to a VPC, we recommend that you migrate as soon as possible.
        For more information, see `Migrate from EC2-Classic to a
        VPC <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-migrate.html>`__
        in the *Amazon EC2 User Guide*, the blog `EC2-Classic Networking is
        Retiring – Here’s How to
        Prepare <http://aws.amazon.com/blogs/aws/ec2-classic-is-retiring-heres-how-to-prepare/>`__,
        and `Moving a DB instance not in a VPC into a
        VPC <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Non-VPC2VPC.html>`__
        in the *Amazon RDS User Guide*.

        :param db_security_group_name: The name of the DB security group to revoke ingress from.
        :param cidrip: The IP range to revoke access from.
        :param ec2_security_group_name: The name of the EC2 security group to revoke access from.
        :param ec2_security_group_id: The id of the EC2 security group to revoke access from.
        :param ec2_security_group_owner_id: The Amazon Web Services account number of the owner of the EC2 security
        group specified in the ``EC2SecurityGroupName`` parameter.
        :returns: RevokeDBSecurityGroupIngressResult
        :raises DBSecurityGroupNotFoundFault:
        :raises AuthorizationNotFoundFault:
        :raises InvalidDBSecurityGroupStateFault:
        """
        raise NotImplementedError

    @handler("StartActivityStream")
    def start_activity_stream(
        self,
        context: RequestContext,
        resource_arn: String,
        mode: ActivityStreamMode,
        kms_key_id: String,
        apply_immediately: BooleanOptional | None = None,
        engine_native_audit_fields_included: BooleanOptional | None = None,
        **kwargs,
    ) -> StartActivityStreamResponse:
        """Starts a database activity stream to monitor activity on the database.
        For more information, see `Monitoring Amazon Aurora with Database
        Activity
        Streams <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/DBActivityStreams.html>`__
        in the *Amazon Aurora User Guide* or `Monitoring Amazon RDS with
        Database Activity
        Streams <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/DBActivityStreams.html>`__
        in the *Amazon RDS User Guide*.

        :param resource_arn: The Amazon Resource Name (ARN) of the DB cluster, for example,
        ``arn:aws:rds:us-east-1:12345667890:cluster:das-cluster``.
        :param mode: Specifies the mode of the database activity stream.
        :param kms_key_id: The Amazon Web Services KMS key identifier for encrypting messages in
        the database activity stream.
        :param apply_immediately: Specifies whether or not the database activity stream is to start as
        soon as possible, regardless of the maintenance window for the database.
        :param engine_native_audit_fields_included: Specifies whether the database activity stream includes engine-native
        audit fields.
        :returns: StartActivityStreamResponse
        :raises InvalidDBInstanceStateFault:
        :raises InvalidDBClusterStateFault:
        :raises ResourceNotFoundFault:
        :raises DBClusterNotFoundFault:
        :raises DBInstanceNotFoundFault:
        :raises KMSKeyNotAccessibleFault:
        """
        raise NotImplementedError

    @handler("StartDBCluster")
    def start_db_cluster(
        self, context: RequestContext, db_cluster_identifier: String, **kwargs
    ) -> StartDBClusterResult:
        """Starts an Amazon Aurora DB cluster that was stopped using the Amazon Web
        Services console, the stop-db-cluster CLI command, or the
        ``StopDBCluster`` operation.

        For more information, see `Stopping and Starting an Aurora
        Cluster <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-cluster-stop-start.html>`__
        in the *Amazon Aurora User Guide*.

        This operation only applies to Aurora DB clusters.

        :param db_cluster_identifier: The DB cluster identifier of the Amazon Aurora DB cluster to be started.
        :returns: StartDBClusterResult
        :raises DBClusterNotFoundFault:
        :raises InvalidDBClusterStateFault:
        :raises InvalidDBInstanceStateFault:
        """
        raise NotImplementedError

    @handler("StartDBInstance")
    def start_db_instance(
        self, context: RequestContext, db_instance_identifier: String, **kwargs
    ) -> StartDBInstanceResult:
        """Starts an Amazon RDS DB instance that was stopped using the Amazon Web
        Services console, the stop-db-instance CLI command, or the
        ``StopDBInstance`` operation.

        For more information, see `Starting an Amazon RDS DB instance That Was
        Previously
        Stopped <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_StartInstance.html>`__
        in the *Amazon RDS User Guide.*

        This command doesn't apply to RDS Custom, Aurora MySQL, and Aurora
        PostgreSQL. For Aurora DB clusters, use ``StartDBCluster`` instead.

        :param db_instance_identifier: The user-supplied instance identifier.
        :returns: StartDBInstanceResult
        :raises DBInstanceNotFoundFault:
        :raises InvalidDBInstanceStateFault:
        :raises InsufficientDBInstanceCapacityFault:
        :raises DBSubnetGroupNotFoundFault:
        :raises DBSubnetGroupDoesNotCoverEnoughAZs:
        :raises InvalidDBClusterStateFault:
        :raises InvalidSubnet:
        :raises InvalidVPCNetworkStateFault:
        :raises DBClusterNotFoundFault:
        :raises AuthorizationNotFoundFault:
        :raises KMSKeyNotAccessibleFault:
        """
        raise NotImplementedError

    @handler("StartDBInstanceAutomatedBackupsReplication")
    def start_db_instance_automated_backups_replication(
        self,
        context: RequestContext,
        source_db_instance_arn: String,
        backup_retention_period: IntegerOptional | None = None,
        kms_key_id: String | None = None,
        pre_signed_url: String | None = None,
        source_region: String | None = None,
        **kwargs,
    ) -> StartDBInstanceAutomatedBackupsReplicationResult:
        """Enables replication of automated backups to a different Amazon Web
        Services Region.

        This command doesn't apply to RDS Custom.

        For more information, see `Replicating Automated Backups to Another
        Amazon Web Services
        Region <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReplicateBackups.html>`__
        in the *Amazon RDS User Guide.*

        :param source_db_instance_arn: The Amazon Resource Name (ARN) of the source DB instance for the
        replicated automated backups, for example,
        ``arn:aws:rds:us-west-2:123456789012:db:mydatabase``.
        :param backup_retention_period: The retention period for the replicated automated backups.
        :param kms_key_id: The Amazon Web Services KMS key identifier for encryption of the
        replicated automated backups.
        :param pre_signed_url: In an Amazon Web Services GovCloud (US) Region, an URL that contains a
        Signature Version 4 signed request for the
        ``StartDBInstanceAutomatedBackupsReplication`` operation to call in the
        Amazon Web Services Region of the source DB instance.
        :param source_region: The ID of the region that contains the source for the db instance.
        :returns: StartDBInstanceAutomatedBackupsReplicationResult
        :raises DBInstanceNotFoundFault:
        :raises InvalidDBInstanceStateFault:
        :raises KMSKeyNotAccessibleFault:
        :raises DBInstanceAutomatedBackupQuotaExceededFault:
        :raises StorageTypeNotSupportedFault:
        """
        raise NotImplementedError

    @handler("StartExportTask")
    def start_export_task(
        self,
        context: RequestContext,
        export_task_identifier: String,
        source_arn: String,
        s3_bucket_name: String,
        iam_role_arn: String,
        kms_key_id: String,
        s3_prefix: String | None = None,
        export_only: StringList | None = None,
        **kwargs,
    ) -> ExportTask:
        """Starts an export of DB snapshot or DB cluster data to Amazon S3. The
        provided IAM role must have access to the S3 bucket.

        You can't export snapshot data from RDS Custom DB instances. For more
        information, see `Supported Regions and DB engines for exporting
        snapshots to S3 in Amazon
        RDS <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.ExportSnapshotToS3.html>`__.

        For more information on exporting DB snapshot data, see `Exporting DB
        snapshot data to Amazon
        S3 <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ExportSnapshot.html>`__
        in the *Amazon RDS User Guide* or `Exporting DB cluster snapshot data to
        Amazon
        S3 <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-export-snapshot.html>`__
        in the *Amazon Aurora User Guide*.

        For more information on exporting DB cluster data, see `Exporting DB
        cluster data to Amazon
        S3 <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/export-cluster-data.html>`__
        in the *Amazon Aurora User Guide*.

        :param export_task_identifier: A unique identifier for the export task.
        :param source_arn: The Amazon Resource Name (ARN) of the snapshot or cluster to export to
        Amazon S3.
        :param s3_bucket_name: The name of the Amazon S3 bucket to export the snapshot or cluster data
        to.
        :param iam_role_arn: The name of the IAM role to use for writing to the Amazon S3 bucket when
        exporting a snapshot or cluster.
        :param kms_key_id: The ID of the Amazon Web Services KMS key to use to encrypt the data
        exported to Amazon S3.
        :param s3_prefix: The Amazon S3 bucket prefix to use as the file name and path of the
        exported data.
        :param export_only: The data to be exported from the snapshot or cluster.
        :returns: ExportTask
        :raises DBSnapshotNotFoundFault:
        :raises DBClusterSnapshotNotFoundFault:
        :raises DBClusterNotFoundFault:
        :raises ExportTaskAlreadyExistsFault:
        :raises InvalidS3BucketFault:
        :raises IamRoleNotFoundFault:
        :raises IamRoleMissingPermissionsFault:
        :raises InvalidExportOnlyFault:
        :raises KMSKeyNotAccessibleFault:
        :raises InvalidExportSourceStateFault:
        """
        raise NotImplementedError

    @handler("StopActivityStream")
    def stop_activity_stream(
        self,
        context: RequestContext,
        resource_arn: String,
        apply_immediately: BooleanOptional | None = None,
        **kwargs,
    ) -> StopActivityStreamResponse:
        """Stops a database activity stream that was started using the Amazon Web
        Services console, the ``start-activity-stream`` CLI command, or the
        ``StartActivityStream`` operation.

        For more information, see `Monitoring Amazon Aurora with Database
        Activity
        Streams <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/DBActivityStreams.html>`__
        in the *Amazon Aurora User Guide* or `Monitoring Amazon RDS with
        Database Activity
        Streams <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/DBActivityStreams.html>`__
        in the *Amazon RDS User Guide*.

        :param resource_arn: The Amazon Resource Name (ARN) of the DB cluster for the database
        activity stream.
        :param apply_immediately: Specifies whether or not the database activity stream is to stop as soon
        as possible, regardless of the maintenance window for the database.
        :returns: StopActivityStreamResponse
        :raises InvalidDBInstanceStateFault:
        :raises InvalidDBClusterStateFault:
        :raises ResourceNotFoundFault:
        :raises DBClusterNotFoundFault:
        :raises DBInstanceNotFoundFault:
        """
        raise NotImplementedError

    @handler("StopDBCluster")
    def stop_db_cluster(
        self, context: RequestContext, db_cluster_identifier: String, **kwargs
    ) -> StopDBClusterResult:
        """Stops an Amazon Aurora DB cluster. When you stop a DB cluster, Aurora
        retains the DB cluster's metadata, including its endpoints and DB
        parameter groups. Aurora also retains the transaction logs so you can do
        a point-in-time restore if necessary.

        For more information, see `Stopping and Starting an Aurora
        Cluster <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-cluster-stop-start.html>`__
        in the *Amazon Aurora User Guide*.

        This operation only applies to Aurora DB clusters.

        :param db_cluster_identifier: The DB cluster identifier of the Amazon Aurora DB cluster to be stopped.
        :returns: StopDBClusterResult
        :raises DBClusterNotFoundFault:
        :raises InvalidDBClusterStateFault:
        :raises InvalidDBInstanceStateFault:
        """
        raise NotImplementedError

    @handler("StopDBInstance")
    def stop_db_instance(
        self,
        context: RequestContext,
        db_instance_identifier: String,
        db_snapshot_identifier: String | None = None,
        **kwargs,
    ) -> StopDBInstanceResult:
        """Stops an Amazon RDS DB instance temporarily. When you stop a DB
        instance, Amazon RDS retains the DB instance's metadata, including its
        endpoint, DB parameter group, and option group membership. Amazon RDS
        also retains the transaction logs so you can do a point-in-time restore
        if necessary. The instance restarts automatically after 7 days.

        For more information, see `Stopping an Amazon RDS DB Instance
        Temporarily <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_StopInstance.html>`__
        in the *Amazon RDS User Guide.*

        This command doesn't apply to RDS Custom, Aurora MySQL, and Aurora
        PostgreSQL. For Aurora clusters, use ``StopDBCluster`` instead.

        :param db_instance_identifier: The user-supplied instance identifier.
        :param db_snapshot_identifier: The user-supplied instance identifier of the DB Snapshot created
        immediately before the DB instance is stopped.
        :returns: StopDBInstanceResult
        :raises DBInstanceNotFoundFault:
        :raises InvalidDBInstanceStateFault:
        :raises DBSnapshotAlreadyExistsFault:
        :raises SnapshotQuotaExceededFault:
        :raises InvalidDBClusterStateFault:
        """
        raise NotImplementedError

    @handler("StopDBInstanceAutomatedBackupsReplication")
    def stop_db_instance_automated_backups_replication(
        self, context: RequestContext, source_db_instance_arn: String, **kwargs
    ) -> StopDBInstanceAutomatedBackupsReplicationResult:
        """Stops automated backup replication for a DB instance.

        This command doesn't apply to RDS Custom, Aurora MySQL, and Aurora
        PostgreSQL.

        For more information, see `Replicating Automated Backups to Another
        Amazon Web Services
        Region <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReplicateBackups.html>`__
        in the *Amazon RDS User Guide.*

        :param source_db_instance_arn: The Amazon Resource Name (ARN) of the source DB instance for which to
        stop replicating automate backups, for example,
        ``arn:aws:rds:us-west-2:123456789012:db:mydatabase``.
        :returns: StopDBInstanceAutomatedBackupsReplicationResult
        :raises DBInstanceNotFoundFault:
        :raises InvalidDBInstanceStateFault:
        """
        raise NotImplementedError

    @handler("SwitchoverBlueGreenDeployment")
    def switchover_blue_green_deployment(
        self,
        context: RequestContext,
        blue_green_deployment_identifier: BlueGreenDeploymentIdentifier,
        switchover_timeout: SwitchoverTimeout | None = None,
        **kwargs,
    ) -> SwitchoverBlueGreenDeploymentResponse:
        """Switches over a blue/green deployment.

        Before you switch over, production traffic is routed to the databases in
        the blue environment. After you switch over, production traffic is
        routed to the databases in the green environment.

        For more information, see `Using Amazon RDS Blue/Green Deployments for
        database
        updates <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html>`__
        in the *Amazon RDS User Guide* and `Using Amazon RDS Blue/Green
        Deployments for database
        updates <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html>`__
        in the *Amazon Aurora User Guide*.

        :param blue_green_deployment_identifier: The resource ID of the blue/green deployment.
        :param switchover_timeout: The amount of time, in seconds, for the switchover to complete.
        :returns: SwitchoverBlueGreenDeploymentResponse
        :raises BlueGreenDeploymentNotFoundFault:
        :raises InvalidBlueGreenDeploymentStateFault:
        """
        raise NotImplementedError

    @handler("SwitchoverGlobalCluster")
    def switchover_global_cluster(
        self,
        context: RequestContext,
        global_cluster_identifier: GlobalClusterIdentifier,
        target_db_cluster_identifier: DBClusterIdentifier,
        **kwargs,
    ) -> SwitchoverGlobalClusterResult:
        """Switches over the specified secondary DB cluster to be the new primary
        DB cluster in the global database cluster. Switchover operations were
        previously called "managed planned failovers."

        Aurora promotes the specified secondary cluster to assume full
        read/write capabilities and demotes the current primary cluster to a
        secondary (read-only) cluster, maintaining the orginal replication
        topology. All secondary clusters are synchronized with the primary at
        the beginning of the process so the new primary continues operations for
        the Aurora global database without losing any data. Your database is
        unavailable for a short time while the primary and selected secondary
        clusters are assuming their new roles. For more information about
        switching over an Aurora global database, see `Performing switchovers
        for Amazon Aurora global
        databases <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html#aurora-global-database-disaster-recovery.managed-failover>`__
        in the *Amazon Aurora User Guide*.

        This operation is intended for controlled environments, for operations
        such as "regional rotation" or to fall back to the original primary
        after a global database failover.

        :param global_cluster_identifier: The identifier of the global database cluster to switch over.
        :param target_db_cluster_identifier: The identifier of the secondary Aurora DB cluster to promote to the new
        primary for the global database cluster.
        :returns: SwitchoverGlobalClusterResult
        :raises GlobalClusterNotFoundFault:
        :raises InvalidGlobalClusterStateFault:
        :raises InvalidDBClusterStateFault:
        :raises DBClusterNotFoundFault:
        """
        raise NotImplementedError

    @handler("SwitchoverReadReplica")
    def switchover_read_replica(
        self, context: RequestContext, db_instance_identifier: String, **kwargs
    ) -> SwitchoverReadReplicaResult:
        """Switches over an Oracle standby database in an Oracle Data Guard
        environment, making it the new primary database. Issue this command in
        the Region that hosts the current standby database.

        :param db_instance_identifier: The DB instance identifier of the current standby database.
        :returns: SwitchoverReadReplicaResult
        :raises DBInstanceNotFoundFault:
        :raises InvalidDBInstanceStateFault:
        """
        raise NotImplementedError
