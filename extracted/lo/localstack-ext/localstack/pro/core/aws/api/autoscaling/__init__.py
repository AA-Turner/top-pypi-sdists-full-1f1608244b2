from datetime import datetime
from enum import StrEnum
from typing import List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

AllowedInstanceType = str
AnyPrintableAsciiStringMaxLen4000 = str
AsciiStringMaxLen255 = str
AssociatePublicIpAddress = bool
AutoRollback = bool
AutoScalingGroupDesiredCapacity = int
AutoScalingGroupMaxSize = int
AutoScalingGroupMinSize = int
AutoScalingGroupPredictedCapacity = int
AutoScalingGroupState = str
BakeTime = int
BlockDeviceEbsDeleteOnTermination = bool
BlockDeviceEbsEncrypted = bool
BlockDeviceEbsIops = int
BlockDeviceEbsThroughput = int
BlockDeviceEbsVolumeSize = int
BlockDeviceEbsVolumeType = str
CapacityRebalanceEnabled = bool
CheckpointDelay = int
Context = str
Cooldown = int
DefaultInstanceWarmup = int
DisableScaleIn = bool
EbsOptimized = bool
EstimatedInstanceWarmup = int
ExcludedInstance = str
ForceDelete = bool
GlobalTimeout = int
HealthCheckGracePeriod = int
HeartbeatTimeout = int
HonorCooldown = bool
IncludeDeletedGroups = bool
InstanceMetadataHttpPutResponseHopLimit = int
InstanceProtected = bool
InstancesToUpdate = int
IntPercent = int
IntPercent100To200 = int
IntPercent100To200Resettable = int
IntPercentResettable = int
LaunchTemplateName = str
LifecycleActionResult = str
LifecycleActionToken = str
LifecycleTransition = str
MaxGroupPreparedCapacity = int
MaxInstanceLifetime = int
MaxNumberOfAutoScalingGroups = int
MaxNumberOfLaunchConfigurations = int
MaxRecords = int
MetricDimensionName = str
MetricDimensionValue = str
MetricGranularityInSeconds = int
MetricName = str
MetricNamespace = str
MetricScale = float
MetricUnit = str
MinAdjustmentMagnitude = int
MinAdjustmentStep = int
MixedInstanceSpotPrice = str
MonitoringEnabled = bool
NoDevice = bool
NonZeroIntPercent = int
NotificationTargetResourceName = str
NullableBoolean = bool
NullablePositiveDouble = float
NullablePositiveInteger = int
NumberOfAutoScalingGroups = int
NumberOfLaunchConfigurations = int
OnDemandBaseCapacity = int
OnDemandPercentageAboveBaseCapacity = int
PolicyIncrement = int
PredictiveScalingMaxCapacityBuffer = int
PredictiveScalingSchedulingBufferTime = int
Progress = int
PropagateAtLaunch = bool
ProtectedFromScaleIn = bool
RefreshInstanceWarmup = int
ResourceName = str
ReturnData = bool
ReuseOnScaleIn = bool
ScalingPolicyEnabled = bool
ShouldDecrementDesiredCapacity = bool
ShouldRespectGracePeriod = bool
SkipMatching = bool
SkipZonalShiftValidation = bool
SpotInstancePools = int
SpotPrice = str
String = str
TagKey = str
TagValue = str
UpdatePlacementGroupParam = str
WarmPoolMinSize = int
WarmPoolSize = int
XmlString = str
XmlStringMaxLen1023 = str
XmlStringMaxLen1600 = str
XmlStringMaxLen19 = str
XmlStringMaxLen2047 = str
XmlStringMaxLen255 = str
XmlStringMaxLen32 = str
XmlStringMaxLen5000 = str
XmlStringMaxLen511 = str
XmlStringMaxLen64 = str
XmlStringMetricLabel = str
XmlStringMetricStat = str
XmlStringUserData = str
ZonalShiftEnabled = bool


class AcceleratorManufacturer(StrEnum):
    nvidia = "nvidia"
    amd = "amd"
    amazon_web_services = "amazon-web-services"
    xilinx = "xilinx"


class AcceleratorName(StrEnum):
    a100 = "a100"
    v100 = "v100"
    k80 = "k80"
    t4 = "t4"
    m60 = "m60"
    radeon_pro_v520 = "radeon-pro-v520"
    vu9p = "vu9p"


class AcceleratorType(StrEnum):
    gpu = "gpu"
    fpga = "fpga"
    inference = "inference"


class BareMetal(StrEnum):
    included = "included"
    excluded = "excluded"
    required = "required"


class BurstablePerformance(StrEnum):
    included = "included"
    excluded = "excluded"
    required = "required"


class CapacityDistributionStrategy(StrEnum):
    balanced_only = "balanced-only"
    balanced_best_effort = "balanced-best-effort"


class CapacityReservationPreference(StrEnum):
    capacity_reservations_only = "capacity-reservations-only"
    capacity_reservations_first = "capacity-reservations-first"
    none = "none"
    default = "default"


class CpuManufacturer(StrEnum):
    intel = "intel"
    amd = "amd"
    amazon_web_services = "amazon-web-services"
    apple = "apple"


class ImpairedZoneHealthCheckBehavior(StrEnum):
    ReplaceUnhealthy = "ReplaceUnhealthy"
    IgnoreUnhealthy = "IgnoreUnhealthy"


class InstanceGeneration(StrEnum):
    current = "current"
    previous = "previous"


class InstanceMetadataEndpointState(StrEnum):
    disabled = "disabled"
    enabled = "enabled"


class InstanceMetadataHttpTokensState(StrEnum):
    optional = "optional"
    required = "required"


class InstanceRefreshStatus(StrEnum):
    Pending = "Pending"
    InProgress = "InProgress"
    Successful = "Successful"
    Failed = "Failed"
    Cancelling = "Cancelling"
    Cancelled = "Cancelled"
    RollbackInProgress = "RollbackInProgress"
    RollbackFailed = "RollbackFailed"
    RollbackSuccessful = "RollbackSuccessful"
    Baking = "Baking"


class LifecycleState(StrEnum):
    Pending = "Pending"
    Pending_Wait = "Pending:Wait"
    Pending_Proceed = "Pending:Proceed"
    Quarantined = "Quarantined"
    InService = "InService"
    Terminating = "Terminating"
    Terminating_Wait = "Terminating:Wait"
    Terminating_Proceed = "Terminating:Proceed"
    Terminated = "Terminated"
    Detaching = "Detaching"
    Detached = "Detached"
    EnteringStandby = "EnteringStandby"
    Standby = "Standby"
    Warmed_Pending = "Warmed:Pending"
    Warmed_Pending_Wait = "Warmed:Pending:Wait"
    Warmed_Pending_Proceed = "Warmed:Pending:Proceed"
    Warmed_Terminating = "Warmed:Terminating"
    Warmed_Terminating_Wait = "Warmed:Terminating:Wait"
    Warmed_Terminating_Proceed = "Warmed:Terminating:Proceed"
    Warmed_Terminated = "Warmed:Terminated"
    Warmed_Stopped = "Warmed:Stopped"
    Warmed_Running = "Warmed:Running"
    Warmed_Hibernated = "Warmed:Hibernated"


class LocalStorage(StrEnum):
    included = "included"
    excluded = "excluded"
    required = "required"


class LocalStorageType(StrEnum):
    hdd = "hdd"
    ssd = "ssd"


class MetricStatistic(StrEnum):
    Average = "Average"
    Minimum = "Minimum"
    Maximum = "Maximum"
    SampleCount = "SampleCount"
    Sum = "Sum"


class MetricType(StrEnum):
    ASGAverageCPUUtilization = "ASGAverageCPUUtilization"
    ASGAverageNetworkIn = "ASGAverageNetworkIn"
    ASGAverageNetworkOut = "ASGAverageNetworkOut"
    ALBRequestCountPerTarget = "ALBRequestCountPerTarget"


class PredefinedLoadMetricType(StrEnum):
    ASGTotalCPUUtilization = "ASGTotalCPUUtilization"
    ASGTotalNetworkIn = "ASGTotalNetworkIn"
    ASGTotalNetworkOut = "ASGTotalNetworkOut"
    ALBTargetGroupRequestCount = "ALBTargetGroupRequestCount"


class PredefinedMetricPairType(StrEnum):
    ASGCPUUtilization = "ASGCPUUtilization"
    ASGNetworkIn = "ASGNetworkIn"
    ASGNetworkOut = "ASGNetworkOut"
    ALBRequestCount = "ALBRequestCount"


class PredefinedScalingMetricType(StrEnum):
    ASGAverageCPUUtilization = "ASGAverageCPUUtilization"
    ASGAverageNetworkIn = "ASGAverageNetworkIn"
    ASGAverageNetworkOut = "ASGAverageNetworkOut"
    ALBRequestCountPerTarget = "ALBRequestCountPerTarget"


class PredictiveScalingMaxCapacityBreachBehavior(StrEnum):
    HonorMaxCapacity = "HonorMaxCapacity"
    IncreaseMaxCapacity = "IncreaseMaxCapacity"


class PredictiveScalingMode(StrEnum):
    ForecastAndScale = "ForecastAndScale"
    ForecastOnly = "ForecastOnly"


class RefreshStrategy(StrEnum):
    Rolling = "Rolling"


class ScaleInProtectedInstances(StrEnum):
    Refresh = "Refresh"
    Ignore = "Ignore"
    Wait = "Wait"


class ScalingActivityStatusCode(StrEnum):
    PendingSpotBidPlacement = "PendingSpotBidPlacement"
    WaitingForSpotInstanceRequestId = "WaitingForSpotInstanceRequestId"
    WaitingForSpotInstanceId = "WaitingForSpotInstanceId"
    WaitingForInstanceId = "WaitingForInstanceId"
    PreInService = "PreInService"
    InProgress = "InProgress"
    WaitingForELBConnectionDraining = "WaitingForELBConnectionDraining"
    MidLifecycleAction = "MidLifecycleAction"
    WaitingForInstanceWarmup = "WaitingForInstanceWarmup"
    Successful = "Successful"
    Failed = "Failed"
    Cancelled = "Cancelled"
    WaitingForConnectionDraining = "WaitingForConnectionDraining"


class StandbyInstances(StrEnum):
    Terminate = "Terminate"
    Ignore = "Ignore"
    Wait = "Wait"


class WarmPoolState(StrEnum):
    Stopped = "Stopped"
    Running = "Running"
    Hibernated = "Hibernated"


class WarmPoolStatus(StrEnum):
    PendingDelete = "PendingDelete"


class ActiveInstanceRefreshNotFoundFault(ServiceException):
    """The request failed because an active instance refresh or rollback for
    the specified Auto Scaling group was not found.
    """

    code: str = "ActiveInstanceRefreshNotFound"
    sender_fault: bool = True
    status_code: int = 400


class AlreadyExistsFault(ServiceException):
    """You already have an Auto Scaling group or launch configuration with this
    name.
    """

    code: str = "AlreadyExists"
    sender_fault: bool = True
    status_code: int = 400


class InstanceRefreshInProgressFault(ServiceException):
    """The request failed because an active instance refresh already exists for
    the specified Auto Scaling group.
    """

    code: str = "InstanceRefreshInProgress"
    sender_fault: bool = True
    status_code: int = 400


class InvalidNextToken(ServiceException):
    """The ``NextToken`` value is not valid."""

    code: str = "InvalidNextToken"
    sender_fault: bool = True
    status_code: int = 400


class IrreversibleInstanceRefreshFault(ServiceException):
    """The request failed because a desired configuration was not found or an
    incompatible launch template (uses a Systems Manager parameter instead
    of an AMI ID) or launch template version (``$Latest`` or ``$Default``)
    is present on the Auto Scaling group.
    """

    code: str = "IrreversibleInstanceRefresh"
    sender_fault: bool = True
    status_code: int = 400


class LimitExceededFault(ServiceException):
    """You have already reached a limit for your Amazon EC2 Auto Scaling
    resources (for example, Auto Scaling groups, launch configurations, or
    lifecycle hooks). For more information, see
    `DescribeAccountLimits <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html>`__
    in the *Amazon EC2 Auto Scaling API Reference*.
    """

    code: str = "LimitExceeded"
    sender_fault: bool = True
    status_code: int = 400


class ResourceContentionFault(ServiceException):
    """You already have a pending update to an Amazon EC2 Auto Scaling resource
    (for example, an Auto Scaling group, instance, or load balancer).
    """

    code: str = "ResourceContention"
    sender_fault: bool = True
    status_code: int = 500


class ResourceInUseFault(ServiceException):
    """The operation can't be performed because the resource is in use."""

    code: str = "ResourceInUse"
    sender_fault: bool = True
    status_code: int = 400


class ScalingActivityInProgressFault(ServiceException):
    """The operation can't be performed because there are scaling activities in
    progress.
    """

    code: str = "ScalingActivityInProgress"
    sender_fault: bool = True
    status_code: int = 400


class ServiceLinkedRoleFailure(ServiceException):
    """The service-linked role is not yet ready for use."""

    code: str = "ServiceLinkedRoleFailure"
    sender_fault: bool = True
    status_code: int = 500


class AcceleratorCountRequest(TypedDict, total=False):
    """Specifies the minimum and maximum for the ``AcceleratorCount`` object
    when you specify
    `InstanceRequirements <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRequirements.html>`__
    for an Auto Scaling group.
    """

    Min: Optional[NullablePositiveInteger]
    Max: Optional[NullablePositiveInteger]


AcceleratorManufacturers = List[AcceleratorManufacturer]
AcceleratorNames = List[AcceleratorName]


class AcceleratorTotalMemoryMiBRequest(TypedDict, total=False):
    """Specifies the minimum and maximum for the ``AcceleratorTotalMemoryMiB``
    object when you specify
    `InstanceRequirements <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRequirements.html>`__
    for an Auto Scaling group.
    """

    Min: Optional[NullablePositiveInteger]
    Max: Optional[NullablePositiveInteger]


AcceleratorTypes = List[AcceleratorType]
TimestampType = datetime


class Activity(TypedDict, total=False):
    """Describes scaling activity, which is a long-running process that
    represents a change to your Auto Scaling group, such as changing its
    size or replacing an instance.
    """

    ActivityId: XmlString
    AutoScalingGroupName: XmlStringMaxLen255
    Description: Optional[XmlString]
    Cause: XmlStringMaxLen1023
    StartTime: TimestampType
    EndTime: Optional[TimestampType]
    StatusCode: ScalingActivityStatusCode
    StatusMessage: Optional[XmlStringMaxLen255]
    Progress: Optional[Progress]
    Details: Optional[XmlString]
    AutoScalingGroupState: Optional[AutoScalingGroupState]
    AutoScalingGroupARN: Optional[ResourceName]


Activities = List[Activity]


class ActivitiesType(TypedDict, total=False):
    Activities: Activities
    NextToken: Optional[XmlString]


ActivityIds = List[XmlString]


class ActivityType(TypedDict, total=False):
    Activity: Optional[Activity]


class AdjustmentType(TypedDict, total=False):
    """Describes a policy adjustment type."""

    AdjustmentType: Optional[XmlStringMaxLen255]


AdjustmentTypes = List[AdjustmentType]


class Alarm(TypedDict, total=False):
    """Describes an alarm."""

    AlarmName: Optional[XmlStringMaxLen255]
    AlarmARN: Optional[ResourceName]


AlarmList = List[XmlStringMaxLen255]


class AlarmSpecification(TypedDict, total=False):
    """Specifies the CloudWatch alarm specification to use in an instance
    refresh.
    """

    Alarms: Optional[AlarmList]


Alarms = List[Alarm]
AllowedInstanceTypes = List[AllowedInstanceType]
InstanceIds = List[XmlStringMaxLen19]


class AttachInstancesQuery(ServiceRequest):
    InstanceIds: Optional[InstanceIds]
    AutoScalingGroupName: XmlStringMaxLen255


class AttachLoadBalancerTargetGroupsResultType(TypedDict, total=False):
    pass


TargetGroupARNs = List[XmlStringMaxLen511]


class AttachLoadBalancerTargetGroupsType(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    TargetGroupARNs: TargetGroupARNs


class AttachLoadBalancersResultType(TypedDict, total=False):
    pass


LoadBalancerNames = List[XmlStringMaxLen255]


class AttachLoadBalancersType(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    LoadBalancerNames: LoadBalancerNames


class AttachTrafficSourcesResultType(TypedDict, total=False):
    pass


class TrafficSourceIdentifier(TypedDict, total=False):
    """Identifying information for a traffic source."""

    Identifier: XmlStringMaxLen511
    Type: Optional[XmlStringMaxLen511]


TrafficSources = List[TrafficSourceIdentifier]


class AttachTrafficSourcesType(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    TrafficSources: TrafficSources
    SkipZonalShiftValidation: Optional[SkipZonalShiftValidation]


CapacityReservationResourceGroupArns = List[ResourceName]
CapacityReservationIds = List[AsciiStringMaxLen255]


class CapacityReservationTarget(TypedDict, total=False):
    """The target for the Capacity Reservation. Specify Capacity Reservations
    IDs or Capacity Reservation resource group ARNs.
    """

    CapacityReservationIds: Optional[CapacityReservationIds]
    CapacityReservationResourceGroupArns: Optional[CapacityReservationResourceGroupArns]


class CapacityReservationSpecification(TypedDict, total=False):
    """Describes the Capacity Reservation preference and targeting options. If
    you specify ``open`` or ``none`` for ``CapacityReservationPreference``,
    do not specify a ``CapacityReservationTarget``.
    """

    CapacityReservationPreference: Optional[CapacityReservationPreference]
    CapacityReservationTarget: Optional[CapacityReservationTarget]


class AvailabilityZoneImpairmentPolicy(TypedDict, total=False):
    """Describes an Availability Zone impairment policy."""

    ZonalShiftEnabled: Optional[ZonalShiftEnabled]
    ImpairedZoneHealthCheckBehavior: Optional[ImpairedZoneHealthCheckBehavior]


class AvailabilityZoneDistribution(TypedDict, total=False):
    """Describes an Availability Zone distribution."""

    CapacityDistributionStrategy: Optional[CapacityDistributionStrategy]


class InstanceMaintenancePolicy(TypedDict, total=False):
    """Describes an instance maintenance policy.

    For more information, see `Set instance maintenance
    policy <https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-maintenance-policy.html>`__
    in the *Amazon EC2 Auto Scaling User Guide*.
    """

    MinHealthyPercentage: Optional[IntPercentResettable]
    MaxHealthyPercentage: Optional[IntPercent100To200Resettable]


class InstanceReusePolicy(TypedDict, total=False):
    """Describes an instance reuse policy for a warm pool.

    For more information, see `Warm pools for Amazon EC2 Auto
    Scaling <https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.html>`__
    in the *Amazon EC2 Auto Scaling User Guide*.
    """

    ReuseOnScaleIn: Optional[ReuseOnScaleIn]


class WarmPoolConfiguration(TypedDict, total=False):
    """Describes a warm pool configuration."""

    MaxGroupPreparedCapacity: Optional[MaxGroupPreparedCapacity]
    MinSize: Optional[WarmPoolMinSize]
    PoolState: Optional[WarmPoolState]
    Status: Optional[WarmPoolStatus]
    InstanceReusePolicy: Optional[InstanceReusePolicy]


TerminationPolicies = List[XmlStringMaxLen1600]


class TagDescription(TypedDict, total=False):
    """Describes a tag for an Auto Scaling group."""

    ResourceId: Optional[XmlString]
    ResourceType: Optional[XmlString]
    Key: Optional[TagKey]
    Value: Optional[TagValue]
    PropagateAtLaunch: Optional[PropagateAtLaunch]


TagDescriptionList = List[TagDescription]


class EnabledMetric(TypedDict, total=False):
    """Describes an enabled Auto Scaling group metric."""

    Metric: Optional[XmlStringMaxLen255]
    Granularity: Optional[XmlStringMaxLen255]


EnabledMetrics = List[EnabledMetric]


class SuspendedProcess(TypedDict, total=False):
    """Describes an auto scaling process that has been suspended.

    For more information, see `Types of
    processes <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html#process-types>`__
    in the *Amazon EC2 Auto Scaling User Guide*.
    """

    ProcessName: Optional[XmlStringMaxLen255]
    SuspensionReason: Optional[XmlStringMaxLen255]


SuspendedProcesses = List[SuspendedProcess]


class LaunchTemplateSpecification(TypedDict, total=False):
    """Describes the launch template and the version of the launch template
    that Amazon EC2 Auto Scaling uses to launch Amazon EC2 instances. For
    more information about launch templates, see `Launch
    templates <https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html>`__
    in the *Amazon EC2 Auto Scaling User Guide*.
    """

    LaunchTemplateId: Optional[XmlStringMaxLen255]
    LaunchTemplateName: Optional[LaunchTemplateName]
    Version: Optional[XmlStringMaxLen255]


class Instance(TypedDict, total=False):
    """Describes an EC2 instance."""

    InstanceId: XmlStringMaxLen19
    InstanceType: Optional[XmlStringMaxLen255]
    AvailabilityZone: XmlStringMaxLen255
    LifecycleState: LifecycleState
    HealthStatus: XmlStringMaxLen32
    LaunchConfigurationName: Optional[XmlStringMaxLen255]
    LaunchTemplate: Optional[LaunchTemplateSpecification]
    ProtectedFromScaleIn: InstanceProtected
    WeightedCapacity: Optional[XmlStringMaxLen32]


Instances = List[Instance]
AvailabilityZones = List[XmlStringMaxLen255]


class InstancesDistribution(TypedDict, total=False):
    """Use this structure to specify the distribution of On-Demand Instances
    and Spot Instances and the allocation strategies used to fulfill
    On-Demand and Spot capacities for a mixed instances policy.
    """

    OnDemandAllocationStrategy: Optional[XmlString]
    OnDemandBaseCapacity: Optional[OnDemandBaseCapacity]
    OnDemandPercentageAboveBaseCapacity: Optional[OnDemandPercentageAboveBaseCapacity]
    SpotAllocationStrategy: Optional[XmlString]
    SpotInstancePools: Optional[SpotInstancePools]
    SpotMaxPrice: Optional[MixedInstanceSpotPrice]


class PerformanceFactorReferenceRequest(TypedDict, total=False):
    """Specify an instance family to use as the baseline reference for CPU
    performance. All instance types that All instance types that match your
    specified attributes will be compared against the CPU performance of the
    referenced instance family, regardless of CPU manufacturer or
    architecture differences.

    Currently only one instance family can be specified in the list.
    """

    InstanceFamily: Optional[String]


PerformanceFactorReferenceSetRequest = List[PerformanceFactorReferenceRequest]


class CpuPerformanceFactorRequest(TypedDict, total=False):
    """The CPU performance to consider, using an instance family as the
    baseline reference.
    """

    References: Optional[PerformanceFactorReferenceSetRequest]


class BaselinePerformanceFactorsRequest(TypedDict, total=False):
    """The baseline performance to consider, using an instance family as a
    baseline reference. The instance family establishes the lowest
    acceptable level of performance. Auto Scaling uses this baseline to
    guide instance type selection, but there is no guarantee that the
    selected instance types will always exceed the baseline for every
    application.

    Currently, this parameter only supports CPU performance as a baseline
    performance factor. For example, specifying ``c6i`` uses the CPU
    performance of the ``c6i`` family as the baseline reference.
    """

    Cpu: Optional[CpuPerformanceFactorRequest]


class NetworkBandwidthGbpsRequest(TypedDict, total=False):
    """Specifies the minimum and maximum for the ``NetworkBandwidthGbps``
    object when you specify
    `InstanceRequirements <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRequirements.html>`__
    for an Auto Scaling group.

    Setting the minimum bandwidth does not guarantee that your instance will
    achieve the minimum bandwidth. Amazon EC2 will identify instance types
    that support the specified minimum bandwidth, but the actual bandwidth
    of your instance might go below the specified minimum at times. For more
    information, see `Available instance
    bandwidth <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html#available-instance-bandwidth>`__
    in the *Amazon EC2 User Guide*.
    """

    Min: Optional[NullablePositiveDouble]
    Max: Optional[NullablePositiveDouble]


class BaselineEbsBandwidthMbpsRequest(TypedDict, total=False):
    """Specifies the minimum and maximum for the ``BaselineEbsBandwidthMbps``
    object when you specify
    `InstanceRequirements <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRequirements.html>`__
    for an Auto Scaling group.
    """

    Min: Optional[NullablePositiveInteger]
    Max: Optional[NullablePositiveInteger]


class TotalLocalStorageGBRequest(TypedDict, total=False):
    """Specifies the minimum and maximum for the ``TotalLocalStorageGB`` object
    when you specify
    `InstanceRequirements <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRequirements.html>`__
    for an Auto Scaling group.
    """

    Min: Optional[NullablePositiveDouble]
    Max: Optional[NullablePositiveDouble]


LocalStorageTypes = List[LocalStorageType]


class NetworkInterfaceCountRequest(TypedDict, total=False):
    """Specifies the minimum and maximum for the ``NetworkInterfaceCount``
    object when you specify
    `InstanceRequirements <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRequirements.html>`__
    for an Auto Scaling group.
    """

    Min: Optional[NullablePositiveInteger]
    Max: Optional[NullablePositiveInteger]


InstanceGenerations = List[InstanceGeneration]
ExcludedInstanceTypes = List[ExcludedInstance]


class MemoryGiBPerVCpuRequest(TypedDict, total=False):
    """Specifies the minimum and maximum for the ``MemoryGiBPerVCpu`` object
    when you specify
    `InstanceRequirements <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRequirements.html>`__
    for an Auto Scaling group.
    """

    Min: Optional[NullablePositiveDouble]
    Max: Optional[NullablePositiveDouble]


CpuManufacturers = List[CpuManufacturer]


class MemoryMiBRequest(TypedDict, total=False):
    """Specifies the minimum and maximum for the ``MemoryMiB`` object when you
    specify
    `InstanceRequirements <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRequirements.html>`__
    for an Auto Scaling group.
    """

    Min: NullablePositiveInteger
    Max: Optional[NullablePositiveInteger]


class VCpuCountRequest(TypedDict, total=False):
    """Specifies the minimum and maximum for the ``VCpuCount`` object when you
    specify
    `InstanceRequirements <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRequirements.html>`__
    for an Auto Scaling group.
    """

    Min: NullablePositiveInteger
    Max: Optional[NullablePositiveInteger]


class InstanceRequirements(TypedDict, total=False):
    """The attributes for the instance types for a mixed instances policy.
    Amazon EC2 Auto Scaling uses your specified requirements to identify
    instance types. Then, it uses your On-Demand and Spot allocation
    strategies to launch instances from these instance types.

    When you specify multiple attributes, you get instance types that
    satisfy all of the specified attributes. If you specify multiple values
    for an attribute, you get instance types that satisfy any of the
    specified values.

    To limit the list of instance types from which Amazon EC2 Auto Scaling
    can identify matching instance types, you can use one of the following
    parameters, but not both in the same request:

    -  ``AllowedInstanceTypes`` - The instance types to include in the list.
       All other instance types are ignored, even if they match your
       specified attributes.

    -  ``ExcludedInstanceTypes`` - The instance types to exclude from the
       list, even if they match your specified attributes.

    You must specify ``VCpuCount`` and ``MemoryMiB``. All other attributes
    are optional. Any unspecified optional attribute is set to its default.

    For more information, see `Create a mixed instances group using
    attribute-based instance type
    selection <https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-mixed-instances-group-attribute-based-instance-type-selection.html>`__
    in the *Amazon EC2 Auto Scaling User Guide*. For help determining which
    instance types match your attributes before you apply them to your Auto
    Scaling group, see `Preview instance types with specified
    attributes <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html#ec2fleet-get-instance-types-from-instance-requirements>`__
    in the *Amazon EC2 User Guide*.
    """

    VCpuCount: VCpuCountRequest
    MemoryMiB: MemoryMiBRequest
    CpuManufacturers: Optional[CpuManufacturers]
    MemoryGiBPerVCpu: Optional[MemoryGiBPerVCpuRequest]
    ExcludedInstanceTypes: Optional[ExcludedInstanceTypes]
    InstanceGenerations: Optional[InstanceGenerations]
    SpotMaxPricePercentageOverLowestPrice: Optional[NullablePositiveInteger]
    MaxSpotPriceAsPercentageOfOptimalOnDemandPrice: Optional[NullablePositiveInteger]
    OnDemandMaxPricePercentageOverLowestPrice: Optional[NullablePositiveInteger]
    BareMetal: Optional[BareMetal]
    BurstablePerformance: Optional[BurstablePerformance]
    RequireHibernateSupport: Optional[NullableBoolean]
    NetworkInterfaceCount: Optional[NetworkInterfaceCountRequest]
    LocalStorage: Optional[LocalStorage]
    LocalStorageTypes: Optional[LocalStorageTypes]
    TotalLocalStorageGB: Optional[TotalLocalStorageGBRequest]
    BaselineEbsBandwidthMbps: Optional[BaselineEbsBandwidthMbpsRequest]
    AcceleratorTypes: Optional[AcceleratorTypes]
    AcceleratorCount: Optional[AcceleratorCountRequest]
    AcceleratorManufacturers: Optional[AcceleratorManufacturers]
    AcceleratorNames: Optional[AcceleratorNames]
    AcceleratorTotalMemoryMiB: Optional[AcceleratorTotalMemoryMiBRequest]
    NetworkBandwidthGbps: Optional[NetworkBandwidthGbpsRequest]
    AllowedInstanceTypes: Optional[AllowedInstanceTypes]
    BaselinePerformanceFactors: Optional[BaselinePerformanceFactorsRequest]


class LaunchTemplateOverrides(TypedDict, total=False):
    """Use this structure to let Amazon EC2 Auto Scaling do the following when
    the Auto Scaling group has a mixed instances policy:

    -  Override the instance type that is specified in the launch template.

    -  Use multiple instance types.

    Specify the instance types that you want, or define your instance
    requirements instead and let Amazon EC2 Auto Scaling provision the
    available instance types that meet your requirements. This can provide
    Amazon EC2 Auto Scaling with a larger selection of instance types to
    choose from when fulfilling Spot and On-Demand capacities. You can view
    which instance types are matched before you apply the instance
    requirements to your Auto Scaling group.

    After you define your instance requirements, you don't have to keep
    updating these settings to get new EC2 instance types automatically.
    Amazon EC2 Auto Scaling uses the instance requirements of the Auto
    Scaling group to determine whether a new EC2 instance type can be used.
    """

    InstanceType: Optional[XmlStringMaxLen255]
    WeightedCapacity: Optional[XmlStringMaxLen32]
    LaunchTemplateSpecification: Optional[LaunchTemplateSpecification]
    InstanceRequirements: Optional[InstanceRequirements]


Overrides = List[LaunchTemplateOverrides]


class LaunchTemplate(TypedDict, total=False):
    """Use this structure to specify the launch templates and instance types
    (overrides) for a mixed instances policy.
    """

    LaunchTemplateSpecification: Optional[LaunchTemplateSpecification]
    Overrides: Optional[Overrides]


class MixedInstancesPolicy(TypedDict, total=False):
    """Use this structure to launch multiple instance types and On-Demand
    Instances and Spot Instances within a single Auto Scaling group.

    A mixed instances policy contains information that Amazon EC2 Auto
    Scaling can use to launch instances and help optimize your costs. For
    more information, see `Auto Scaling groups with multiple instance types
    and purchase
    options <https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.html>`__
    in the *Amazon EC2 Auto Scaling User Guide*.
    """

    LaunchTemplate: Optional[LaunchTemplate]
    InstancesDistribution: Optional[InstancesDistribution]


class AutoScalingGroup(TypedDict, total=False):
    """Describes an Auto Scaling group."""

    AutoScalingGroupName: XmlStringMaxLen255
    AutoScalingGroupARN: Optional[ResourceName]
    LaunchConfigurationName: Optional[XmlStringMaxLen255]
    LaunchTemplate: Optional[LaunchTemplateSpecification]
    MixedInstancesPolicy: Optional[MixedInstancesPolicy]
    MinSize: AutoScalingGroupMinSize
    MaxSize: AutoScalingGroupMaxSize
    DesiredCapacity: AutoScalingGroupDesiredCapacity
    PredictedCapacity: Optional[AutoScalingGroupPredictedCapacity]
    DefaultCooldown: Cooldown
    AvailabilityZones: AvailabilityZones
    LoadBalancerNames: Optional[LoadBalancerNames]
    TargetGroupARNs: Optional[TargetGroupARNs]
    HealthCheckType: XmlStringMaxLen32
    HealthCheckGracePeriod: Optional[HealthCheckGracePeriod]
    Instances: Optional[Instances]
    CreatedTime: TimestampType
    SuspendedProcesses: Optional[SuspendedProcesses]
    PlacementGroup: Optional[XmlStringMaxLen255]
    VPCZoneIdentifier: Optional[XmlStringMaxLen5000]
    EnabledMetrics: Optional[EnabledMetrics]
    Status: Optional[XmlStringMaxLen255]
    Tags: Optional[TagDescriptionList]
    TerminationPolicies: Optional[TerminationPolicies]
    NewInstancesProtectedFromScaleIn: Optional[InstanceProtected]
    ServiceLinkedRoleARN: Optional[ResourceName]
    MaxInstanceLifetime: Optional[MaxInstanceLifetime]
    CapacityRebalance: Optional[CapacityRebalanceEnabled]
    WarmPoolConfiguration: Optional[WarmPoolConfiguration]
    WarmPoolSize: Optional[WarmPoolSize]
    Context: Optional[Context]
    DesiredCapacityType: Optional[XmlStringMaxLen255]
    DefaultInstanceWarmup: Optional[DefaultInstanceWarmup]
    TrafficSources: Optional[TrafficSources]
    InstanceMaintenancePolicy: Optional[InstanceMaintenancePolicy]
    AvailabilityZoneDistribution: Optional[AvailabilityZoneDistribution]
    AvailabilityZoneImpairmentPolicy: Optional[AvailabilityZoneImpairmentPolicy]
    CapacityReservationSpecification: Optional[CapacityReservationSpecification]


AutoScalingGroupNames = List[XmlStringMaxLen255]
Values = List[XmlString]


class Filter(TypedDict, total=False):
    """Describes a filter that is used to return a more specific list of
    results from a describe operation.

    If you specify multiple filters, the filters are automatically logically
    joined with an ``AND``, and the request returns only the results that
    match all of the specified filters.

    For more information, see `Tag Auto Scaling groups and
    instances <https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-tagging.html>`__
    in the *Amazon EC2 Auto Scaling User Guide*.
    """

    Name: Optional[XmlString]
    Values: Optional[Values]


Filters = List[Filter]


class AutoScalingGroupNamesType(ServiceRequest):
    AutoScalingGroupNames: Optional[AutoScalingGroupNames]
    NextToken: Optional[XmlString]
    MaxRecords: Optional[MaxRecords]
    Filters: Optional[Filters]


AutoScalingGroups = List[AutoScalingGroup]


class AutoScalingGroupsType(TypedDict, total=False):
    AutoScalingGroups: AutoScalingGroups
    NextToken: Optional[XmlString]


class AutoScalingInstanceDetails(TypedDict, total=False):
    """Describes an EC2 instance associated with an Auto Scaling group."""

    InstanceId: XmlStringMaxLen19
    InstanceType: Optional[XmlStringMaxLen255]
    AutoScalingGroupName: XmlStringMaxLen255
    AvailabilityZone: XmlStringMaxLen255
    LifecycleState: XmlStringMaxLen32
    HealthStatus: XmlStringMaxLen32
    LaunchConfigurationName: Optional[XmlStringMaxLen255]
    LaunchTemplate: Optional[LaunchTemplateSpecification]
    ProtectedFromScaleIn: InstanceProtected
    WeightedCapacity: Optional[XmlStringMaxLen32]


AutoScalingInstances = List[AutoScalingInstanceDetails]


class AutoScalingInstancesType(TypedDict, total=False):
    AutoScalingInstances: Optional[AutoScalingInstances]
    NextToken: Optional[XmlString]


AutoScalingNotificationTypes = List[XmlStringMaxLen255]


class FailedScheduledUpdateGroupActionRequest(TypedDict, total=False):
    """Describes a scheduled action that could not be created, updated, or
    deleted.
    """

    ScheduledActionName: XmlStringMaxLen255
    ErrorCode: Optional[XmlStringMaxLen64]
    ErrorMessage: Optional[XmlString]


FailedScheduledUpdateGroupActionRequests = List[FailedScheduledUpdateGroupActionRequest]


class BatchDeleteScheduledActionAnswer(TypedDict, total=False):
    FailedScheduledActions: Optional[FailedScheduledUpdateGroupActionRequests]


ScheduledActionNames = List[XmlStringMaxLen255]


class BatchDeleteScheduledActionType(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    ScheduledActionNames: ScheduledActionNames


class BatchPutScheduledUpdateGroupActionAnswer(TypedDict, total=False):
    FailedScheduledUpdateGroupActions: Optional[FailedScheduledUpdateGroupActionRequests]


class ScheduledUpdateGroupActionRequest(TypedDict, total=False):
    """Describes information used for one or more scheduled scaling action
    updates in a
    `BatchPutScheduledUpdateGroupAction <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_BatchPutScheduledUpdateGroupAction.html>`__
    operation.
    """

    ScheduledActionName: XmlStringMaxLen255
    StartTime: Optional[TimestampType]
    EndTime: Optional[TimestampType]
    Recurrence: Optional[XmlStringMaxLen255]
    MinSize: Optional[AutoScalingGroupMinSize]
    MaxSize: Optional[AutoScalingGroupMaxSize]
    DesiredCapacity: Optional[AutoScalingGroupDesiredCapacity]
    TimeZone: Optional[XmlStringMaxLen255]


ScheduledUpdateGroupActionRequests = List[ScheduledUpdateGroupActionRequest]


class BatchPutScheduledUpdateGroupActionType(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    ScheduledUpdateGroupActions: ScheduledUpdateGroupActionRequests


class Ebs(TypedDict, total=False):
    """Describes information used to set up an Amazon EBS volume specified in a
    block device mapping.
    """

    SnapshotId: Optional[XmlStringMaxLen255]
    VolumeSize: Optional[BlockDeviceEbsVolumeSize]
    VolumeType: Optional[BlockDeviceEbsVolumeType]
    DeleteOnTermination: Optional[BlockDeviceEbsDeleteOnTermination]
    Iops: Optional[BlockDeviceEbsIops]
    Encrypted: Optional[BlockDeviceEbsEncrypted]
    Throughput: Optional[BlockDeviceEbsThroughput]


class BlockDeviceMapping(TypedDict, total=False):
    """Describes a block device mapping."""

    VirtualName: Optional[XmlStringMaxLen255]
    DeviceName: XmlStringMaxLen255
    Ebs: Optional[Ebs]
    NoDevice: Optional[NoDevice]


BlockDeviceMappings = List[BlockDeviceMapping]


class CancelInstanceRefreshAnswer(TypedDict, total=False):
    InstanceRefreshId: Optional[XmlStringMaxLen255]


class CancelInstanceRefreshType(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255


PredictiveScalingForecastValues = List[MetricScale]
PredictiveScalingForecastTimestamps = List[TimestampType]


class CapacityForecast(TypedDict, total=False):
    """A ``GetPredictiveScalingForecast`` call returns the capacity forecast
    for a predictive scaling policy. This structure includes the data points
    for that capacity forecast, along with the timestamps of those data
    points.
    """

    Timestamps: PredictiveScalingForecastTimestamps
    Values: PredictiveScalingForecastValues


CheckpointPercentages = List[NonZeroIntPercent]
ClassicLinkVPCSecurityGroups = List[XmlStringMaxLen255]


class CompleteLifecycleActionAnswer(TypedDict, total=False):
    pass


class CompleteLifecycleActionType(ServiceRequest):
    LifecycleHookName: AsciiStringMaxLen255
    AutoScalingGroupName: ResourceName
    LifecycleActionToken: Optional[LifecycleActionToken]
    LifecycleActionResult: LifecycleActionResult
    InstanceId: Optional[XmlStringMaxLen19]


class Tag(TypedDict, total=False):
    """Describes a tag for an Auto Scaling group."""

    ResourceId: Optional[XmlString]
    ResourceType: Optional[XmlString]
    Key: TagKey
    Value: Optional[TagValue]
    PropagateAtLaunch: Optional[PropagateAtLaunch]


Tags = List[Tag]


class LifecycleHookSpecification(TypedDict, total=False):
    """Describes information used to specify a lifecycle hook for an Auto
    Scaling group.

    For more information, see `Amazon EC2 Auto Scaling lifecycle
    hooks <https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html>`__
    in the *Amazon EC2 Auto Scaling User Guide*.
    """

    LifecycleHookName: AsciiStringMaxLen255
    LifecycleTransition: LifecycleTransition
    NotificationMetadata: Optional[AnyPrintableAsciiStringMaxLen4000]
    HeartbeatTimeout: Optional[HeartbeatTimeout]
    DefaultResult: Optional[LifecycleActionResult]
    NotificationTargetARN: Optional[NotificationTargetResourceName]
    RoleARN: Optional[XmlStringMaxLen255]


LifecycleHookSpecifications = List[LifecycleHookSpecification]


class CreateAutoScalingGroupType(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    LaunchConfigurationName: Optional[XmlStringMaxLen255]
    LaunchTemplate: Optional[LaunchTemplateSpecification]
    MixedInstancesPolicy: Optional[MixedInstancesPolicy]
    InstanceId: Optional[XmlStringMaxLen19]
    MinSize: AutoScalingGroupMinSize
    MaxSize: AutoScalingGroupMaxSize
    DesiredCapacity: Optional[AutoScalingGroupDesiredCapacity]
    DefaultCooldown: Optional[Cooldown]
    AvailabilityZones: Optional[AvailabilityZones]
    LoadBalancerNames: Optional[LoadBalancerNames]
    TargetGroupARNs: Optional[TargetGroupARNs]
    HealthCheckType: Optional[XmlStringMaxLen32]
    HealthCheckGracePeriod: Optional[HealthCheckGracePeriod]
    PlacementGroup: Optional[XmlStringMaxLen255]
    VPCZoneIdentifier: Optional[XmlStringMaxLen5000]
    TerminationPolicies: Optional[TerminationPolicies]
    NewInstancesProtectedFromScaleIn: Optional[InstanceProtected]
    CapacityRebalance: Optional[CapacityRebalanceEnabled]
    LifecycleHookSpecificationList: Optional[LifecycleHookSpecifications]
    Tags: Optional[Tags]
    ServiceLinkedRoleARN: Optional[ResourceName]
    MaxInstanceLifetime: Optional[MaxInstanceLifetime]
    Context: Optional[Context]
    DesiredCapacityType: Optional[XmlStringMaxLen255]
    DefaultInstanceWarmup: Optional[DefaultInstanceWarmup]
    TrafficSources: Optional[TrafficSources]
    InstanceMaintenancePolicy: Optional[InstanceMaintenancePolicy]
    AvailabilityZoneDistribution: Optional[AvailabilityZoneDistribution]
    AvailabilityZoneImpairmentPolicy: Optional[AvailabilityZoneImpairmentPolicy]
    SkipZonalShiftValidation: Optional[SkipZonalShiftValidation]
    CapacityReservationSpecification: Optional[CapacityReservationSpecification]


class InstanceMetadataOptions(TypedDict, total=False):
    """The metadata options for the instances. For more information, see
    `Configure the instance metadata
    options <https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-config.html#launch-configurations-imds>`__
    in the *Amazon EC2 Auto Scaling User Guide*.
    """

    HttpTokens: Optional[InstanceMetadataHttpTokensState]
    HttpPutResponseHopLimit: Optional[InstanceMetadataHttpPutResponseHopLimit]
    HttpEndpoint: Optional[InstanceMetadataEndpointState]


class InstanceMonitoring(TypedDict, total=False):
    """Describes whether detailed monitoring is enabled for the Auto Scaling
    instances.
    """

    Enabled: Optional[MonitoringEnabled]


SecurityGroups = List[XmlString]


class CreateLaunchConfigurationType(ServiceRequest):
    LaunchConfigurationName: XmlStringMaxLen255
    ImageId: Optional[XmlStringMaxLen255]
    KeyName: Optional[XmlStringMaxLen255]
    SecurityGroups: Optional[SecurityGroups]
    ClassicLinkVPCId: Optional[XmlStringMaxLen255]
    ClassicLinkVPCSecurityGroups: Optional[ClassicLinkVPCSecurityGroups]
    UserData: Optional[XmlStringUserData]
    InstanceId: Optional[XmlStringMaxLen19]
    InstanceType: Optional[XmlStringMaxLen255]
    KernelId: Optional[XmlStringMaxLen255]
    RamdiskId: Optional[XmlStringMaxLen255]
    BlockDeviceMappings: Optional[BlockDeviceMappings]
    InstanceMonitoring: Optional[InstanceMonitoring]
    SpotPrice: Optional[SpotPrice]
    IamInstanceProfile: Optional[XmlStringMaxLen1600]
    EbsOptimized: Optional[EbsOptimized]
    AssociatePublicIpAddress: Optional[AssociatePublicIpAddress]
    PlacementTenancy: Optional[XmlStringMaxLen64]
    MetadataOptions: Optional[InstanceMetadataOptions]


class CreateOrUpdateTagsType(ServiceRequest):
    Tags: Tags


class MetricDimension(TypedDict, total=False):
    """Describes the dimension of a metric."""

    Name: MetricDimensionName
    Value: MetricDimensionValue


MetricDimensions = List[MetricDimension]


class Metric(TypedDict, total=False):
    """Represents a specific metric."""

    Namespace: MetricNamespace
    MetricName: MetricName
    Dimensions: Optional[MetricDimensions]


class TargetTrackingMetricStat(TypedDict, total=False):
    """This structure defines the CloudWatch metric to return, along with the
    statistic and unit.

    For more information about the CloudWatch terminology below, see `Amazon
    CloudWatch
    concepts <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html>`__
    in the *Amazon CloudWatch User Guide*.
    """

    Metric: Metric
    Stat: XmlStringMetricStat
    Unit: Optional[MetricUnit]
    Period: Optional[MetricGranularityInSeconds]


class TargetTrackingMetricDataQuery(TypedDict, total=False):
    """The metric data to return. Also defines whether this call is returning
    data for one metric only, or whether it is performing a math expression
    on the values of returned metric statistics to create a new time series.
    A time series is a series of data points, each of which is associated
    with a timestamp.
    """

    Id: XmlStringMaxLen64
    Expression: Optional[XmlStringMaxLen2047]
    MetricStat: Optional[TargetTrackingMetricStat]
    Label: Optional[XmlStringMetricLabel]
    Period: Optional[MetricGranularityInSeconds]
    ReturnData: Optional[ReturnData]


TargetTrackingMetricDataQueries = List[TargetTrackingMetricDataQuery]


class CustomizedMetricSpecification(TypedDict, total=False):
    """Represents a CloudWatch metric of your choosing for a target tracking
    scaling policy to use with Amazon EC2 Auto Scaling.

    To create your customized metric specification:

    -  Add values for each required property from CloudWatch. You can use an
       existing metric, or a new metric that you create. To use your own
       metric, you must first publish the metric to CloudWatch. For more
       information, see `Publish custom
       metrics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html>`__
       in the *Amazon CloudWatch User Guide*.

    -  Choose a metric that changes proportionally with capacity. The value
       of the metric should increase or decrease in inverse proportion to
       the number of capacity units. That is, the value of the metric should
       decrease when capacity increases.

    For more information about the CloudWatch terminology below, see `Amazon
    CloudWatch
    concepts <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html>`__.

    Each individual service provides information about the metrics,
    namespace, and dimensions they use. For more information, see `Amazon
    Web Services services that publish CloudWatch
    metrics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html>`__
    in the *Amazon CloudWatch User Guide*.
    """

    MetricName: Optional[MetricName]
    Namespace: Optional[MetricNamespace]
    Dimensions: Optional[MetricDimensions]
    Statistic: Optional[MetricStatistic]
    Unit: Optional[MetricUnit]
    Period: Optional[MetricGranularityInSeconds]
    Metrics: Optional[TargetTrackingMetricDataQueries]


class DeleteAutoScalingGroupType(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    ForceDelete: Optional[ForceDelete]


class DeleteLifecycleHookAnswer(TypedDict, total=False):
    pass


class DeleteLifecycleHookType(ServiceRequest):
    LifecycleHookName: AsciiStringMaxLen255
    AutoScalingGroupName: XmlStringMaxLen255


class DeleteNotificationConfigurationType(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    TopicARN: XmlStringMaxLen255


class DeletePolicyType(ServiceRequest):
    AutoScalingGroupName: Optional[XmlStringMaxLen255]
    PolicyName: ResourceName


class DeleteScheduledActionType(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    ScheduledActionName: XmlStringMaxLen255


class DeleteTagsType(ServiceRequest):
    Tags: Tags


class DeleteWarmPoolAnswer(TypedDict, total=False):
    pass


class DeleteWarmPoolType(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    ForceDelete: Optional[ForceDelete]


class DescribeAccountLimitsAnswer(TypedDict, total=False):
    MaxNumberOfAutoScalingGroups: Optional[MaxNumberOfAutoScalingGroups]
    MaxNumberOfLaunchConfigurations: Optional[MaxNumberOfLaunchConfigurations]
    NumberOfAutoScalingGroups: Optional[NumberOfAutoScalingGroups]
    NumberOfLaunchConfigurations: Optional[NumberOfLaunchConfigurations]


class DescribeAdjustmentTypesAnswer(TypedDict, total=False):
    AdjustmentTypes: Optional[AdjustmentTypes]


class DescribeAutoScalingInstancesType(ServiceRequest):
    InstanceIds: Optional[InstanceIds]
    MaxRecords: Optional[MaxRecords]
    NextToken: Optional[XmlString]


class DescribeAutoScalingNotificationTypesAnswer(TypedDict, total=False):
    AutoScalingNotificationTypes: Optional[AutoScalingNotificationTypes]


class InstanceRefreshWarmPoolProgress(TypedDict, total=False):
    """Reports progress on replacing instances that are in the warm pool."""

    PercentageComplete: Optional[IntPercent]
    InstancesToUpdate: Optional[InstancesToUpdate]


class InstanceRefreshLivePoolProgress(TypedDict, total=False):
    """Reports progress on replacing instances that are in the Auto Scaling
    group.
    """

    PercentageComplete: Optional[IntPercent]
    InstancesToUpdate: Optional[InstancesToUpdate]


class InstanceRefreshProgressDetails(TypedDict, total=False):
    """Reports progress on replacing instances in an Auto Scaling group that
    has a warm pool. This includes separate details for instances in the
    warm pool and instances in the Auto Scaling group (the live pool).
    """

    LivePoolProgress: Optional[InstanceRefreshLivePoolProgress]
    WarmPoolProgress: Optional[InstanceRefreshWarmPoolProgress]


class RollbackDetails(TypedDict, total=False):
    """Details about an instance refresh rollback."""

    RollbackReason: Optional[XmlStringMaxLen1023]
    RollbackStartTime: Optional[TimestampType]
    PercentageCompleteOnRollback: Optional[IntPercent]
    InstancesToUpdateOnRollback: Optional[InstancesToUpdate]
    ProgressDetailsOnRollback: Optional[InstanceRefreshProgressDetails]


class DesiredConfiguration(TypedDict, total=False):
    """Describes the desired configuration for an instance refresh.

    If you specify a desired configuration, you must specify either a
    ``LaunchTemplate`` or a ``MixedInstancesPolicy``.
    """

    LaunchTemplate: Optional[LaunchTemplateSpecification]
    MixedInstancesPolicy: Optional[MixedInstancesPolicy]


class RefreshPreferences(TypedDict, total=False):
    """Describes the preferences for an instance refresh."""

    MinHealthyPercentage: Optional[IntPercent]
    InstanceWarmup: Optional[RefreshInstanceWarmup]
    CheckpointPercentages: Optional[CheckpointPercentages]
    CheckpointDelay: Optional[CheckpointDelay]
    SkipMatching: Optional[SkipMatching]
    AutoRollback: Optional[AutoRollback]
    ScaleInProtectedInstances: Optional[ScaleInProtectedInstances]
    StandbyInstances: Optional[StandbyInstances]
    AlarmSpecification: Optional[AlarmSpecification]
    MaxHealthyPercentage: Optional[IntPercent100To200]
    BakeTime: Optional[BakeTime]


class InstanceRefresh(TypedDict, total=False):
    """Describes an instance refresh for an Auto Scaling group."""

    InstanceRefreshId: Optional[XmlStringMaxLen255]
    AutoScalingGroupName: Optional[XmlStringMaxLen255]
    Status: Optional[InstanceRefreshStatus]
    StatusReason: Optional[XmlStringMaxLen1023]
    StartTime: Optional[TimestampType]
    EndTime: Optional[TimestampType]
    PercentageComplete: Optional[IntPercent]
    InstancesToUpdate: Optional[InstancesToUpdate]
    ProgressDetails: Optional[InstanceRefreshProgressDetails]
    Preferences: Optional[RefreshPreferences]
    DesiredConfiguration: Optional[DesiredConfiguration]
    RollbackDetails: Optional[RollbackDetails]


InstanceRefreshes = List[InstanceRefresh]


class DescribeInstanceRefreshesAnswer(TypedDict, total=False):
    InstanceRefreshes: Optional[InstanceRefreshes]
    NextToken: Optional[XmlString]


InstanceRefreshIds = List[XmlStringMaxLen255]


class DescribeInstanceRefreshesType(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    InstanceRefreshIds: Optional[InstanceRefreshIds]
    NextToken: Optional[XmlString]
    MaxRecords: Optional[MaxRecords]


class DescribeLifecycleHookTypesAnswer(TypedDict, total=False):
    LifecycleHookTypes: Optional[AutoScalingNotificationTypes]


class LifecycleHook(TypedDict, total=False):
    """Describes a lifecycle hook. A lifecycle hook lets you create solutions
    that are aware of events in the Auto Scaling instance lifecycle, and
    then perform a custom action on instances when the corresponding
    lifecycle event occurs.
    """

    LifecycleHookName: Optional[AsciiStringMaxLen255]
    AutoScalingGroupName: Optional[XmlStringMaxLen255]
    LifecycleTransition: Optional[LifecycleTransition]
    NotificationTargetARN: Optional[NotificationTargetResourceName]
    RoleARN: Optional[XmlStringMaxLen255]
    NotificationMetadata: Optional[AnyPrintableAsciiStringMaxLen4000]
    HeartbeatTimeout: Optional[HeartbeatTimeout]
    GlobalTimeout: Optional[GlobalTimeout]
    DefaultResult: Optional[LifecycleActionResult]


LifecycleHooks = List[LifecycleHook]


class DescribeLifecycleHooksAnswer(TypedDict, total=False):
    LifecycleHooks: Optional[LifecycleHooks]


LifecycleHookNames = List[AsciiStringMaxLen255]


class DescribeLifecycleHooksType(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    LifecycleHookNames: Optional[LifecycleHookNames]


class DescribeLoadBalancerTargetGroupsRequest(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    NextToken: Optional[XmlString]
    MaxRecords: Optional[MaxRecords]


class LoadBalancerTargetGroupState(TypedDict, total=False):
    """Describes the state of a target group."""

    LoadBalancerTargetGroupARN: Optional[XmlStringMaxLen511]
    State: Optional[XmlStringMaxLen255]


LoadBalancerTargetGroupStates = List[LoadBalancerTargetGroupState]


class DescribeLoadBalancerTargetGroupsResponse(TypedDict, total=False):
    LoadBalancerTargetGroups: Optional[LoadBalancerTargetGroupStates]
    NextToken: Optional[XmlString]


class DescribeLoadBalancersRequest(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    NextToken: Optional[XmlString]
    MaxRecords: Optional[MaxRecords]


class LoadBalancerState(TypedDict, total=False):
    """Describes the state of a Classic Load Balancer."""

    LoadBalancerName: Optional[XmlStringMaxLen255]
    State: Optional[XmlStringMaxLen255]


LoadBalancerStates = List[LoadBalancerState]


class DescribeLoadBalancersResponse(TypedDict, total=False):
    LoadBalancers: Optional[LoadBalancerStates]
    NextToken: Optional[XmlString]


class MetricGranularityType(TypedDict, total=False):
    """Describes a granularity of a metric."""

    Granularity: Optional[XmlStringMaxLen255]


MetricGranularityTypes = List[MetricGranularityType]


class MetricCollectionType(TypedDict, total=False):
    """Describes a metric."""

    Metric: Optional[XmlStringMaxLen255]


MetricCollectionTypes = List[MetricCollectionType]


class DescribeMetricCollectionTypesAnswer(TypedDict, total=False):
    Metrics: Optional[MetricCollectionTypes]
    Granularities: Optional[MetricGranularityTypes]


class NotificationConfiguration(TypedDict, total=False):
    """Describes a notification."""

    AutoScalingGroupName: Optional[XmlStringMaxLen255]
    TopicARN: Optional[XmlStringMaxLen255]
    NotificationType: Optional[XmlStringMaxLen255]


NotificationConfigurations = List[NotificationConfiguration]


class DescribeNotificationConfigurationsAnswer(TypedDict, total=False):
    NotificationConfigurations: NotificationConfigurations
    NextToken: Optional[XmlString]


class DescribeNotificationConfigurationsType(ServiceRequest):
    AutoScalingGroupNames: Optional[AutoScalingGroupNames]
    NextToken: Optional[XmlString]
    MaxRecords: Optional[MaxRecords]


PolicyTypes = List[XmlStringMaxLen64]
PolicyNames = List[ResourceName]


class DescribePoliciesType(ServiceRequest):
    AutoScalingGroupName: Optional[XmlStringMaxLen255]
    PolicyNames: Optional[PolicyNames]
    PolicyTypes: Optional[PolicyTypes]
    NextToken: Optional[XmlString]
    MaxRecords: Optional[MaxRecords]


class DescribeScalingActivitiesType(ServiceRequest):
    ActivityIds: Optional[ActivityIds]
    AutoScalingGroupName: Optional[XmlStringMaxLen255]
    IncludeDeletedGroups: Optional[IncludeDeletedGroups]
    MaxRecords: Optional[MaxRecords]
    NextToken: Optional[XmlString]


class DescribeScheduledActionsType(ServiceRequest):
    AutoScalingGroupName: Optional[XmlStringMaxLen255]
    ScheduledActionNames: Optional[ScheduledActionNames]
    StartTime: Optional[TimestampType]
    EndTime: Optional[TimestampType]
    NextToken: Optional[XmlString]
    MaxRecords: Optional[MaxRecords]


class DescribeTagsType(ServiceRequest):
    Filters: Optional[Filters]
    NextToken: Optional[XmlString]
    MaxRecords: Optional[MaxRecords]


class DescribeTerminationPolicyTypesAnswer(TypedDict, total=False):
    TerminationPolicyTypes: Optional[TerminationPolicies]


class DescribeTrafficSourcesRequest(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    TrafficSourceType: Optional[XmlStringMaxLen255]
    NextToken: Optional[XmlString]
    MaxRecords: Optional[MaxRecords]


class TrafficSourceState(TypedDict, total=False):
    """Describes the state of a traffic source."""

    TrafficSource: Optional[XmlStringMaxLen511]
    State: Optional[XmlStringMaxLen255]
    Identifier: Optional[XmlStringMaxLen511]
    Type: Optional[XmlStringMaxLen511]


TrafficSourceStates = List[TrafficSourceState]


class DescribeTrafficSourcesResponse(TypedDict, total=False):
    TrafficSources: Optional[TrafficSourceStates]
    NextToken: Optional[XmlString]


class DescribeWarmPoolAnswer(TypedDict, total=False):
    WarmPoolConfiguration: Optional[WarmPoolConfiguration]
    Instances: Optional[Instances]
    NextToken: Optional[XmlString]


class DescribeWarmPoolType(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    MaxRecords: Optional[MaxRecords]
    NextToken: Optional[XmlString]


class DetachInstancesAnswer(TypedDict, total=False):
    Activities: Optional[Activities]


class DetachInstancesQuery(ServiceRequest):
    InstanceIds: Optional[InstanceIds]
    AutoScalingGroupName: XmlStringMaxLen255
    ShouldDecrementDesiredCapacity: ShouldDecrementDesiredCapacity


class DetachLoadBalancerTargetGroupsResultType(TypedDict, total=False):
    pass


class DetachLoadBalancerTargetGroupsType(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    TargetGroupARNs: TargetGroupARNs


class DetachLoadBalancersResultType(TypedDict, total=False):
    pass


class DetachLoadBalancersType(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    LoadBalancerNames: LoadBalancerNames


class DetachTrafficSourcesResultType(TypedDict, total=False):
    pass


class DetachTrafficSourcesType(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    TrafficSources: TrafficSources


Metrics = List[XmlStringMaxLen255]


class DisableMetricsCollectionQuery(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    Metrics: Optional[Metrics]


class EnableMetricsCollectionQuery(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    Metrics: Optional[Metrics]
    Granularity: XmlStringMaxLen255


class EnterStandbyAnswer(TypedDict, total=False):
    Activities: Optional[Activities]


class EnterStandbyQuery(ServiceRequest):
    InstanceIds: Optional[InstanceIds]
    AutoScalingGroupName: XmlStringMaxLen255
    ShouldDecrementDesiredCapacity: ShouldDecrementDesiredCapacity


class ExecutePolicyType(ServiceRequest):
    AutoScalingGroupName: Optional[XmlStringMaxLen255]
    PolicyName: ResourceName
    HonorCooldown: Optional[HonorCooldown]
    MetricValue: Optional[MetricScale]
    BreachThreshold: Optional[MetricScale]


class ExitStandbyAnswer(TypedDict, total=False):
    Activities: Optional[Activities]


class ExitStandbyQuery(ServiceRequest):
    InstanceIds: Optional[InstanceIds]
    AutoScalingGroupName: XmlStringMaxLen255


class MetricStat(TypedDict, total=False):
    """This structure defines the CloudWatch metric to return, along with the
    statistic and unit.

    For more information about the CloudWatch terminology below, see `Amazon
    CloudWatch
    concepts <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html>`__
    in the *Amazon CloudWatch User Guide*.
    """

    Metric: Metric
    Stat: XmlStringMetricStat
    Unit: Optional[MetricUnit]


class MetricDataQuery(TypedDict, total=False):
    """The metric data to return. Also defines whether this call is returning
    data for one metric only, or whether it is performing a math expression
    on the values of returned metric statistics to create a new time series.
    A time series is a series of data points, each of which is associated
    with a timestamp.

    For more information and examples, see `Advanced predictive scaling
    policy configurations using custom
    metrics <https://docs.aws.amazon.com/autoscaling/ec2/userguide/predictive-scaling-customized-metric-specification.html>`__
    in the *Amazon EC2 Auto Scaling User Guide*.
    """

    Id: XmlStringMaxLen255
    Expression: Optional[XmlStringMaxLen1023]
    MetricStat: Optional[MetricStat]
    Label: Optional[XmlStringMetricLabel]
    ReturnData: Optional[ReturnData]


MetricDataQueries = List[MetricDataQuery]


class PredictiveScalingCustomizedCapacityMetric(TypedDict, total=False):
    """Describes a customized capacity metric for a predictive scaling policy."""

    MetricDataQueries: MetricDataQueries


class PredictiveScalingCustomizedLoadMetric(TypedDict, total=False):
    """Describes a custom load metric for a predictive scaling policy."""

    MetricDataQueries: MetricDataQueries


class PredictiveScalingCustomizedScalingMetric(TypedDict, total=False):
    """Describes a custom scaling metric for a predictive scaling policy."""

    MetricDataQueries: MetricDataQueries


class PredictiveScalingPredefinedLoadMetric(TypedDict, total=False):
    """Describes a load metric for a predictive scaling policy.

    When returned in the output of ``DescribePolicies``, it indicates that a
    predictive scaling policy uses individually specified load and scaling
    metrics instead of a metric pair.
    """

    PredefinedMetricType: PredefinedLoadMetricType
    ResourceLabel: Optional[XmlStringMaxLen1023]


class PredictiveScalingPredefinedScalingMetric(TypedDict, total=False):
    """Describes a scaling metric for a predictive scaling policy.

    When returned in the output of ``DescribePolicies``, it indicates that a
    predictive scaling policy uses individually specified load and scaling
    metrics instead of a metric pair.
    """

    PredefinedMetricType: PredefinedScalingMetricType
    ResourceLabel: Optional[XmlStringMaxLen1023]


class PredictiveScalingPredefinedMetricPair(TypedDict, total=False):
    """Represents a metric pair for a predictive scaling policy."""

    PredefinedMetricType: PredefinedMetricPairType
    ResourceLabel: Optional[XmlStringMaxLen1023]


class PredictiveScalingMetricSpecification(TypedDict, total=False):
    """This structure specifies the metrics and target utilization settings for
    a predictive scaling policy.

    You must specify either a metric pair, or a load metric and a scaling
    metric individually. Specifying a metric pair instead of individual
    metrics provides a simpler way to configure metrics for a scaling
    policy. You choose the metric pair, and the policy automatically knows
    the correct sum and average statistics to use for the load metric and
    the scaling metric.

    Example

    -  You create a predictive scaling policy and specify
       ``ALBRequestCount`` as the value for the metric pair and ``1000.0``
       as the target value. For this type of metric, you must provide the
       metric dimension for the corresponding target group, so you also
       provide a resource label for the Application Load Balancer target
       group that is attached to your Auto Scaling group.

    -  The number of requests the target group receives per minute provides
       the load metric, and the request count averaged between the members
       of the target group provides the scaling metric. In CloudWatch, this
       refers to the ``RequestCount`` and ``RequestCountPerTarget`` metrics,
       respectively.

    -  For optimal use of predictive scaling, you adhere to the best
       practice of using a dynamic scaling policy to automatically scale
       between the minimum capacity and maximum capacity in response to
       real-time changes in resource utilization.

    -  Amazon EC2 Auto Scaling consumes data points for the load metric over
       the last 14 days and creates an hourly load forecast for predictive
       scaling. (A minimum of 24 hours of data is required.)

    -  After creating the load forecast, Amazon EC2 Auto Scaling determines
       when to reduce or increase the capacity of your Auto Scaling group in
       each hour of the forecast period so that the average number of
       requests received by each instance is as close to 1000 requests per
       minute as possible at all times.

    For information about using custom metrics with predictive scaling, see
    `Advanced predictive scaling policy configurations using custom
    metrics <https://docs.aws.amazon.com/autoscaling/ec2/userguide/predictive-scaling-customized-metric-specification.html>`__
    in the *Amazon EC2 Auto Scaling User Guide*.
    """

    TargetValue: MetricScale
    PredefinedMetricPairSpecification: Optional[PredictiveScalingPredefinedMetricPair]
    PredefinedScalingMetricSpecification: Optional[PredictiveScalingPredefinedScalingMetric]
    PredefinedLoadMetricSpecification: Optional[PredictiveScalingPredefinedLoadMetric]
    CustomizedScalingMetricSpecification: Optional[PredictiveScalingCustomizedScalingMetric]
    CustomizedLoadMetricSpecification: Optional[PredictiveScalingCustomizedLoadMetric]
    CustomizedCapacityMetricSpecification: Optional[PredictiveScalingCustomizedCapacityMetric]


class LoadForecast(TypedDict, total=False):
    """A ``GetPredictiveScalingForecast`` call returns the load forecast for a
    predictive scaling policy. This structure includes the data points for
    that load forecast, along with the timestamps of those data points and
    the metric specification.
    """

    Timestamps: PredictiveScalingForecastTimestamps
    Values: PredictiveScalingForecastValues
    MetricSpecification: PredictiveScalingMetricSpecification


LoadForecasts = List[LoadForecast]


class GetPredictiveScalingForecastAnswer(TypedDict, total=False):
    LoadForecast: LoadForecasts
    CapacityForecast: CapacityForecast
    UpdateTime: TimestampType


class GetPredictiveScalingForecastType(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    PolicyName: XmlStringMaxLen255
    StartTime: TimestampType
    EndTime: TimestampType


class LaunchConfiguration(TypedDict, total=False):
    """Describes a launch configuration."""

    LaunchConfigurationName: XmlStringMaxLen255
    LaunchConfigurationARN: Optional[ResourceName]
    ImageId: XmlStringMaxLen255
    KeyName: Optional[XmlStringMaxLen255]
    SecurityGroups: Optional[SecurityGroups]
    ClassicLinkVPCId: Optional[XmlStringMaxLen255]
    ClassicLinkVPCSecurityGroups: Optional[ClassicLinkVPCSecurityGroups]
    UserData: Optional[XmlStringUserData]
    InstanceType: XmlStringMaxLen255
    KernelId: Optional[XmlStringMaxLen255]
    RamdiskId: Optional[XmlStringMaxLen255]
    BlockDeviceMappings: Optional[BlockDeviceMappings]
    InstanceMonitoring: Optional[InstanceMonitoring]
    SpotPrice: Optional[SpotPrice]
    IamInstanceProfile: Optional[XmlStringMaxLen1600]
    CreatedTime: TimestampType
    EbsOptimized: Optional[EbsOptimized]
    AssociatePublicIpAddress: Optional[AssociatePublicIpAddress]
    PlacementTenancy: Optional[XmlStringMaxLen64]
    MetadataOptions: Optional[InstanceMetadataOptions]


class LaunchConfigurationNameType(ServiceRequest):
    LaunchConfigurationName: XmlStringMaxLen255


LaunchConfigurationNames = List[XmlStringMaxLen255]


class LaunchConfigurationNamesType(ServiceRequest):
    LaunchConfigurationNames: Optional[LaunchConfigurationNames]
    NextToken: Optional[XmlString]
    MaxRecords: Optional[MaxRecords]


LaunchConfigurations = List[LaunchConfiguration]


class LaunchConfigurationsType(TypedDict, total=False):
    LaunchConfigurations: LaunchConfigurations
    NextToken: Optional[XmlString]


PredictiveScalingMetricSpecifications = List[PredictiveScalingMetricSpecification]


class PredictiveScalingConfiguration(TypedDict, total=False):
    """Represents a predictive scaling policy configuration to use with Amazon
    EC2 Auto Scaling.
    """

    MetricSpecifications: PredictiveScalingMetricSpecifications
    Mode: Optional[PredictiveScalingMode]
    SchedulingBufferTime: Optional[PredictiveScalingSchedulingBufferTime]
    MaxCapacityBreachBehavior: Optional[PredictiveScalingMaxCapacityBreachBehavior]
    MaxCapacityBuffer: Optional[PredictiveScalingMaxCapacityBuffer]


class PredefinedMetricSpecification(TypedDict, total=False):
    """Represents a predefined metric for a target tracking scaling policy to
    use with Amazon EC2 Auto Scaling.
    """

    PredefinedMetricType: MetricType
    ResourceLabel: Optional[XmlStringMaxLen1023]


class TargetTrackingConfiguration(TypedDict, total=False):
    """Represents a target tracking scaling policy configuration to use with
    Amazon EC2 Auto Scaling.
    """

    PredefinedMetricSpecification: Optional[PredefinedMetricSpecification]
    CustomizedMetricSpecification: Optional[CustomizedMetricSpecification]
    TargetValue: MetricScale
    DisableScaleIn: Optional[DisableScaleIn]


class StepAdjustment(TypedDict, total=False):
    """Describes information used to create a step adjustment for a step
    scaling policy.

    For the following examples, suppose that you have an alarm with a breach
    threshold of 50:

    -  To trigger the adjustment when the metric is greater than or equal to
       50 and less than 60, specify a lower bound of 0 and an upper bound of
       10.

    -  To trigger the adjustment when the metric is greater than 40 and less
       than or equal to 50, specify a lower bound of -10 and an upper bound
       of 0.

    There are a few rules for the step adjustments for your step policy:

    -  The ranges of your step adjustments can't overlap or have a gap.

    -  At most, one step adjustment can have a null lower bound. If one step
       adjustment has a negative lower bound, then there must be a step
       adjustment with a null lower bound.

    -  At most, one step adjustment can have a null upper bound. If one step
       adjustment has a positive upper bound, then there must be a step
       adjustment with a null upper bound.

    -  The upper and lower bound can't be null in the same step adjustment.

    For more information, see `Step
    adjustments <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html#as-scaling-steps>`__
    in the *Amazon EC2 Auto Scaling User Guide*.
    """

    MetricIntervalLowerBound: Optional[MetricScale]
    MetricIntervalUpperBound: Optional[MetricScale]
    ScalingAdjustment: PolicyIncrement


StepAdjustments = List[StepAdjustment]


class ScalingPolicy(TypedDict, total=False):
    """Describes a scaling policy."""

    AutoScalingGroupName: Optional[XmlStringMaxLen255]
    PolicyName: Optional[XmlStringMaxLen255]
    PolicyARN: Optional[ResourceName]
    PolicyType: Optional[XmlStringMaxLen64]
    AdjustmentType: Optional[XmlStringMaxLen255]
    MinAdjustmentStep: Optional[MinAdjustmentStep]
    MinAdjustmentMagnitude: Optional[MinAdjustmentMagnitude]
    ScalingAdjustment: Optional[PolicyIncrement]
    Cooldown: Optional[Cooldown]
    StepAdjustments: Optional[StepAdjustments]
    MetricAggregationType: Optional[XmlStringMaxLen32]
    EstimatedInstanceWarmup: Optional[EstimatedInstanceWarmup]
    Alarms: Optional[Alarms]
    TargetTrackingConfiguration: Optional[TargetTrackingConfiguration]
    Enabled: Optional[ScalingPolicyEnabled]
    PredictiveScalingConfiguration: Optional[PredictiveScalingConfiguration]


ScalingPolicies = List[ScalingPolicy]


class PoliciesType(TypedDict, total=False):
    ScalingPolicies: Optional[ScalingPolicies]
    NextToken: Optional[XmlString]


class PolicyARNType(TypedDict, total=False):
    """Contains the output of PutScalingPolicy."""

    PolicyARN: Optional[ResourceName]
    Alarms: Optional[Alarms]


ProcessNames = List[XmlStringMaxLen255]


class ProcessType(TypedDict, total=False):
    """Describes a process type.

    For more information, see `Types of
    processes <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html#process-types>`__
    in the *Amazon EC2 Auto Scaling User Guide*.
    """

    ProcessName: XmlStringMaxLen255


Processes = List[ProcessType]


class ProcessesType(TypedDict, total=False):
    Processes: Optional[Processes]


class PutLifecycleHookAnswer(TypedDict, total=False):
    pass


class PutLifecycleHookType(ServiceRequest):
    LifecycleHookName: AsciiStringMaxLen255
    AutoScalingGroupName: XmlStringMaxLen255
    LifecycleTransition: Optional[LifecycleTransition]
    RoleARN: Optional[XmlStringMaxLen255]
    NotificationTargetARN: Optional[NotificationTargetResourceName]
    NotificationMetadata: Optional[AnyPrintableAsciiStringMaxLen4000]
    HeartbeatTimeout: Optional[HeartbeatTimeout]
    DefaultResult: Optional[LifecycleActionResult]


class PutNotificationConfigurationType(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    TopicARN: XmlStringMaxLen255
    NotificationTypes: AutoScalingNotificationTypes


class PutScalingPolicyType(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    PolicyName: XmlStringMaxLen255
    PolicyType: Optional[XmlStringMaxLen64]
    AdjustmentType: Optional[XmlStringMaxLen255]
    MinAdjustmentStep: Optional[MinAdjustmentStep]
    MinAdjustmentMagnitude: Optional[MinAdjustmentMagnitude]
    ScalingAdjustment: Optional[PolicyIncrement]
    Cooldown: Optional[Cooldown]
    MetricAggregationType: Optional[XmlStringMaxLen32]
    StepAdjustments: Optional[StepAdjustments]
    EstimatedInstanceWarmup: Optional[EstimatedInstanceWarmup]
    TargetTrackingConfiguration: Optional[TargetTrackingConfiguration]
    Enabled: Optional[ScalingPolicyEnabled]
    PredictiveScalingConfiguration: Optional[PredictiveScalingConfiguration]


class PutScheduledUpdateGroupActionType(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    ScheduledActionName: XmlStringMaxLen255
    Time: Optional[TimestampType]
    StartTime: Optional[TimestampType]
    EndTime: Optional[TimestampType]
    Recurrence: Optional[XmlStringMaxLen255]
    MinSize: Optional[AutoScalingGroupMinSize]
    MaxSize: Optional[AutoScalingGroupMaxSize]
    DesiredCapacity: Optional[AutoScalingGroupDesiredCapacity]
    TimeZone: Optional[XmlStringMaxLen255]


class PutWarmPoolAnswer(TypedDict, total=False):
    pass


class PutWarmPoolType(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    MaxGroupPreparedCapacity: Optional[MaxGroupPreparedCapacity]
    MinSize: Optional[WarmPoolMinSize]
    PoolState: Optional[WarmPoolState]
    InstanceReusePolicy: Optional[InstanceReusePolicy]


class RecordLifecycleActionHeartbeatAnswer(TypedDict, total=False):
    pass


class RecordLifecycleActionHeartbeatType(ServiceRequest):
    LifecycleHookName: AsciiStringMaxLen255
    AutoScalingGroupName: ResourceName
    LifecycleActionToken: Optional[LifecycleActionToken]
    InstanceId: Optional[XmlStringMaxLen19]


class RollbackInstanceRefreshAnswer(TypedDict, total=False):
    InstanceRefreshId: Optional[XmlStringMaxLen255]


class RollbackInstanceRefreshType(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255


class ScalingProcessQuery(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    ScalingProcesses: Optional[ProcessNames]


class ScheduledUpdateGroupAction(TypedDict, total=False):
    """Describes a scheduled scaling action."""

    AutoScalingGroupName: Optional[XmlStringMaxLen255]
    ScheduledActionName: Optional[XmlStringMaxLen255]
    ScheduledActionARN: Optional[ResourceName]
    Time: Optional[TimestampType]
    StartTime: Optional[TimestampType]
    EndTime: Optional[TimestampType]
    Recurrence: Optional[XmlStringMaxLen255]
    MinSize: Optional[AutoScalingGroupMinSize]
    MaxSize: Optional[AutoScalingGroupMaxSize]
    DesiredCapacity: Optional[AutoScalingGroupDesiredCapacity]
    TimeZone: Optional[XmlStringMaxLen255]


ScheduledUpdateGroupActions = List[ScheduledUpdateGroupAction]


class ScheduledActionsType(TypedDict, total=False):
    ScheduledUpdateGroupActions: Optional[ScheduledUpdateGroupActions]
    NextToken: Optional[XmlString]


class SetDesiredCapacityType(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    DesiredCapacity: AutoScalingGroupDesiredCapacity
    HonorCooldown: Optional[HonorCooldown]


class SetInstanceHealthQuery(ServiceRequest):
    InstanceId: XmlStringMaxLen19
    HealthStatus: XmlStringMaxLen32
    ShouldRespectGracePeriod: Optional[ShouldRespectGracePeriod]


class SetInstanceProtectionAnswer(TypedDict, total=False):
    pass


class SetInstanceProtectionQuery(ServiceRequest):
    InstanceIds: InstanceIds
    AutoScalingGroupName: XmlStringMaxLen255
    ProtectedFromScaleIn: ProtectedFromScaleIn


class StartInstanceRefreshAnswer(TypedDict, total=False):
    InstanceRefreshId: Optional[XmlStringMaxLen255]


class StartInstanceRefreshType(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    Strategy: Optional[RefreshStrategy]
    DesiredConfiguration: Optional[DesiredConfiguration]
    Preferences: Optional[RefreshPreferences]


class TagsType(TypedDict, total=False):
    Tags: Optional[TagDescriptionList]
    NextToken: Optional[XmlString]


class TerminateInstanceInAutoScalingGroupType(ServiceRequest):
    InstanceId: XmlStringMaxLen19
    ShouldDecrementDesiredCapacity: ShouldDecrementDesiredCapacity


class UpdateAutoScalingGroupType(ServiceRequest):
    AutoScalingGroupName: XmlStringMaxLen255
    LaunchConfigurationName: Optional[XmlStringMaxLen255]
    LaunchTemplate: Optional[LaunchTemplateSpecification]
    MixedInstancesPolicy: Optional[MixedInstancesPolicy]
    MinSize: Optional[AutoScalingGroupMinSize]
    MaxSize: Optional[AutoScalingGroupMaxSize]
    DesiredCapacity: Optional[AutoScalingGroupDesiredCapacity]
    DefaultCooldown: Optional[Cooldown]
    AvailabilityZones: Optional[AvailabilityZones]
    HealthCheckType: Optional[XmlStringMaxLen32]
    HealthCheckGracePeriod: Optional[HealthCheckGracePeriod]
    PlacementGroup: Optional[UpdatePlacementGroupParam]
    VPCZoneIdentifier: Optional[XmlStringMaxLen5000]
    TerminationPolicies: Optional[TerminationPolicies]
    NewInstancesProtectedFromScaleIn: Optional[InstanceProtected]
    ServiceLinkedRoleARN: Optional[ResourceName]
    MaxInstanceLifetime: Optional[MaxInstanceLifetime]
    CapacityRebalance: Optional[CapacityRebalanceEnabled]
    Context: Optional[Context]
    DesiredCapacityType: Optional[XmlStringMaxLen255]
    DefaultInstanceWarmup: Optional[DefaultInstanceWarmup]
    InstanceMaintenancePolicy: Optional[InstanceMaintenancePolicy]
    AvailabilityZoneDistribution: Optional[AvailabilityZoneDistribution]
    AvailabilityZoneImpairmentPolicy: Optional[AvailabilityZoneImpairmentPolicy]
    SkipZonalShiftValidation: Optional[SkipZonalShiftValidation]
    CapacityReservationSpecification: Optional[CapacityReservationSpecification]


class AutoscalingApi:
    service = "autoscaling"
    version = "2011-01-01"

    @handler("AttachInstances")
    def attach_instances(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        instance_ids: InstanceIds | None = None,
        **kwargs,
    ) -> None:
        """Attaches one or more EC2 instances to the specified Auto Scaling group.

        When you attach instances, Amazon EC2 Auto Scaling increases the desired
        capacity of the group by the number of instances being attached. If the
        number of instances being attached plus the desired capacity of the
        group exceeds the maximum size of the group, the operation fails.

        If there is a Classic Load Balancer attached to your Auto Scaling group,
        the instances are also registered with the load balancer. If there are
        target groups attached to your Auto Scaling group, the instances are
        also registered with the target groups.

        For more information, see `Detach or attach
        instances <https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-detach-attach-instances.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param instance_ids: The IDs of the instances.
        :raises ResourceContentionFault:
        :raises ServiceLinkedRoleFailure:
        """
        raise NotImplementedError

    @handler("AttachLoadBalancerTargetGroups")
    def attach_load_balancer_target_groups(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        target_group_arns: TargetGroupARNs,
        **kwargs,
    ) -> AttachLoadBalancerTargetGroupsResultType:
        """This API operation is superseded by
        `AttachTrafficSources <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AttachTrafficSources.html>`__,
        which can attach multiple traffic sources types. We recommend using
        ``AttachTrafficSources`` to simplify how you manage traffic sources.
        However, we continue to support ``AttachLoadBalancerTargetGroups``. You
        can use both the original ``AttachLoadBalancerTargetGroups`` API
        operation and ``AttachTrafficSources`` on the same Auto Scaling group.

        Attaches one or more target groups to the specified Auto Scaling group.

        This operation is used with the following load balancer types:

        -  Application Load Balancer - Operates at the application layer (layer
           7) and supports HTTP and HTTPS.

        -  Network Load Balancer - Operates at the transport layer (layer 4) and
           supports TCP, TLS, and UDP.

        -  Gateway Load Balancer - Operates at the network layer (layer 3).

        To describe the target groups for an Auto Scaling group, call the
        `DescribeLoadBalancerTargetGroups <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeLoadBalancerTargetGroups.html>`__
        API. To detach the target group from the Auto Scaling group, call the
        `DetachLoadBalancerTargetGroups <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachLoadBalancerTargetGroups.html>`__
        API.

        This operation is additive and does not detach existing target groups or
        Classic Load Balancers from the Auto Scaling group.

        For more information, see `Use Elastic Load Balancing to distribute
        traffic across the instances in your Auto Scaling
        group <https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param target_group_arns: The Amazon Resource Names (ARNs) of the target groups.
        :returns: AttachLoadBalancerTargetGroupsResultType
        :raises ResourceContentionFault:
        :raises ServiceLinkedRoleFailure:
        """
        raise NotImplementedError

    @handler("AttachLoadBalancers")
    def attach_load_balancers(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        load_balancer_names: LoadBalancerNames,
        **kwargs,
    ) -> AttachLoadBalancersResultType:
        """This API operation is superseded by
        https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AttachTrafficSources.html,
        which can attach multiple traffic sources types. We recommend using
        ``AttachTrafficSources`` to simplify how you manage traffic sources.
        However, we continue to support ``AttachLoadBalancers``. You can use
        both the original ``AttachLoadBalancers`` API operation and
        ``AttachTrafficSources`` on the same Auto Scaling group.

        Attaches one or more Classic Load Balancers to the specified Auto
        Scaling group. Amazon EC2 Auto Scaling registers the running instances
        with these Classic Load Balancers.

        To describe the load balancers for an Auto Scaling group, call the
        `DescribeLoadBalancers <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeLoadBalancers.html>`__
        API. To detach a load balancer from the Auto Scaling group, call the
        `DetachLoadBalancers <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachLoadBalancers.html>`__
        API.

        This operation is additive and does not detach existing Classic Load
        Balancers or target groups from the Auto Scaling group.

        For more information, see `Use Elastic Load Balancing to distribute
        traffic across the instances in your Auto Scaling
        group <https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param load_balancer_names: The names of the load balancers.
        :returns: AttachLoadBalancersResultType
        :raises ResourceContentionFault:
        :raises ServiceLinkedRoleFailure:
        """
        raise NotImplementedError

    @handler("AttachTrafficSources")
    def attach_traffic_sources(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        traffic_sources: TrafficSources,
        skip_zonal_shift_validation: SkipZonalShiftValidation | None = None,
        **kwargs,
    ) -> AttachTrafficSourcesResultType:
        """Attaches one or more traffic sources to the specified Auto Scaling
        group.

        You can use any of the following as traffic sources for an Auto Scaling
        group:

        -  Application Load Balancer

        -  Classic Load Balancer

        -  Gateway Load Balancer

        -  Network Load Balancer

        -  VPC Lattice

        This operation is additive and does not detach existing traffic sources
        from the Auto Scaling group.

        After the operation completes, use the
        `DescribeTrafficSources <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeTrafficSources.html>`__
        API to return details about the state of the attachments between traffic
        sources and your Auto Scaling group. To detach a traffic source from the
        Auto Scaling group, call the
        `DetachTrafficSources <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachTrafficSources.html>`__
        API.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param traffic_sources: The unique identifiers of one or more traffic sources.
        :param skip_zonal_shift_validation: If you enable zonal shift with cross-zone disabled load balancers,
        capacity could become imbalanced across Availability Zones.
        :returns: AttachTrafficSourcesResultType
        :raises ResourceContentionFault:
        :raises ServiceLinkedRoleFailure:
        """
        raise NotImplementedError

    @handler("BatchDeleteScheduledAction")
    def batch_delete_scheduled_action(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        scheduled_action_names: ScheduledActionNames,
        **kwargs,
    ) -> BatchDeleteScheduledActionAnswer:
        """Deletes one or more scheduled actions for the specified Auto Scaling
        group.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param scheduled_action_names: The names of the scheduled actions to delete.
        :returns: BatchDeleteScheduledActionAnswer
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("BatchPutScheduledUpdateGroupAction")
    def batch_put_scheduled_update_group_action(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        scheduled_update_group_actions: ScheduledUpdateGroupActionRequests,
        **kwargs,
    ) -> BatchPutScheduledUpdateGroupActionAnswer:
        """Creates or updates one or more scheduled scaling actions for an Auto
        Scaling group.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param scheduled_update_group_actions: One or more scheduled actions.
        :returns: BatchPutScheduledUpdateGroupActionAnswer
        :raises AlreadyExistsFault:
        :raises LimitExceededFault:
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("CancelInstanceRefresh")
    def cancel_instance_refresh(
        self, context: RequestContext, auto_scaling_group_name: XmlStringMaxLen255, **kwargs
    ) -> CancelInstanceRefreshAnswer:
        """Cancels an instance refresh or rollback that is in progress. If an
        instance refresh or rollback is not in progress, an
        ``ActiveInstanceRefreshNotFound`` error occurs.

        This operation is part of the `instance refresh
        feature <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html>`__
        in Amazon EC2 Auto Scaling, which helps you update instances in your
        Auto Scaling group after you make configuration changes.

        When you cancel an instance refresh, this does not roll back any changes
        that it made. Use the
        `RollbackInstanceRefresh <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_RollbackInstanceRefresh.html>`__
        API to roll back instead.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :returns: CancelInstanceRefreshAnswer
        :raises LimitExceededFault:
        :raises ResourceContentionFault:
        :raises ActiveInstanceRefreshNotFoundFault:
        """
        raise NotImplementedError

    @handler("CompleteLifecycleAction")
    def complete_lifecycle_action(
        self,
        context: RequestContext,
        lifecycle_hook_name: AsciiStringMaxLen255,
        auto_scaling_group_name: ResourceName,
        lifecycle_action_result: LifecycleActionResult,
        lifecycle_action_token: LifecycleActionToken | None = None,
        instance_id: XmlStringMaxLen19 | None = None,
        **kwargs,
    ) -> CompleteLifecycleActionAnswer:
        """Completes the lifecycle action for the specified token or instance with
        the specified result.

        This step is a part of the procedure for adding a lifecycle hook to an
        Auto Scaling group:

        #. (Optional) Create a launch template or launch configuration with a
           user data script that runs while an instance is in a wait state due
           to a lifecycle hook.

        #. (Optional) Create a Lambda function and a rule that allows Amazon
           EventBridge to invoke your Lambda function when an instance is put
           into a wait state due to a lifecycle hook.

        #. (Optional) Create a notification target and an IAM role. The target
           can be either an Amazon SQS queue or an Amazon SNS topic. The role
           allows Amazon EC2 Auto Scaling to publish lifecycle notifications to
           the target.

        #. Create the lifecycle hook. Specify whether the hook is used when the
           instances launch or terminate.

        #. If you need more time, record the lifecycle action heartbeat to keep
           the instance in a wait state.

        #. **If you finish before the timeout period ends, send a callback by
           using
           the** `CompleteLifecycleAction <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CompleteLifecycleAction.html>`__ **API
           call.**

        For more information, see `Complete a lifecycle
        action <https://docs.aws.amazon.com/autoscaling/ec2/userguide/completing-lifecycle-hooks.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        :param lifecycle_hook_name: The name of the lifecycle hook.
        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param lifecycle_action_result: The action for the group to take.
        :param lifecycle_action_token: A universally unique identifier (UUID) that identifies a specific
        lifecycle action associated with an instance.
        :param instance_id: The ID of the instance.
        :returns: CompleteLifecycleActionAnswer
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("CreateAutoScalingGroup", expand=False)
    def create_auto_scaling_group(
        self, context: RequestContext, request: CreateAutoScalingGroupType, **kwargs
    ) -> None:
        """**We strongly recommend using a launch template when calling this
        operation to ensure full functionality for Amazon EC2 Auto Scaling and
        Amazon EC2.**

        Creates an Auto Scaling group with the specified name and attributes.

        If you exceed your maximum limit of Auto Scaling groups, the call fails.
        To query this limit, call the
        `DescribeAccountLimits <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html>`__
        API. For information about updating this limit, see `Quotas for Amazon
        EC2 Auto
        Scaling <https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-quotas.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        If you're new to Amazon EC2 Auto Scaling, see the introductory tutorials
        in `Get started with Amazon EC2 Auto
        Scaling <https://docs.aws.amazon.com/autoscaling/ec2/userguide/get-started-with-ec2-auto-scaling.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        Every Auto Scaling group has three size properties (``DesiredCapacity``,
        ``MaxSize``, and ``MinSize``). Usually, you set these sizes based on a
        specific number of instances. However, if you configure a mixed
        instances policy that defines weights for the instance types, you must
        specify these sizes with the same units that you use for weighting
        instances.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param min_size: The minimum size of the group.
        :param max_size: The maximum size of the group.
        :param launch_configuration_name: The name of the launch configuration to use to launch instances.
        :param launch_template: Information used to specify the launch template and version to use to
        launch instances.
        :param mixed_instances_policy: The mixed instances policy.
        :param instance_id: The ID of the instance used to base the launch configuration on.
        :param desired_capacity: The desired capacity is the initial capacity of the Auto Scaling group
        at the time of its creation and the capacity it attempts to maintain.
        :param default_cooldown: *Only needed if you use simple scaling policies.
        :param availability_zones: A list of Availability Zones where instances in the Auto Scaling group
        can be created.
        :param load_balancer_names: A list of Classic Load Balancers associated with this Auto Scaling
        group.
        :param target_group_arns: The Amazon Resource Names (ARN) of the Elastic Load Balancing target
        groups to associate with the Auto Scaling group.
        :param health_check_type: A comma-separated value string of one or more health check types.
        :param health_check_grace_period: The amount of time, in seconds, that Amazon EC2 Auto Scaling waits
        before checking the health status of an EC2 instance that has come into
        service and marking it unhealthy due to a failed health check.
        :param placement_group: The name of the placement group into which to launch your instances.
        :param vpc_zone_identifier: A comma-separated list of subnet IDs for a virtual private cloud (VPC)
        where instances in the Auto Scaling group can be created.
        :param termination_policies: A policy or a list of policies that are used to select the instance to
        terminate.
        :param new_instances_protected_from_scale_in: Indicates whether newly launched instances are protected from
        termination by Amazon EC2 Auto Scaling when scaling in.
        :param capacity_rebalance: Indicates whether Capacity Rebalancing is enabled.
        :param lifecycle_hook_specification_list: One or more lifecycle hooks to add to the Auto Scaling group before
        instances are launched.
        :param tags: One or more tags.
        :param service_linked_role_arn: The Amazon Resource Name (ARN) of the service-linked role that the Auto
        Scaling group uses to call other Amazon Web Services service on your
        behalf.
        :param max_instance_lifetime: The maximum amount of time, in seconds, that an instance can be in
        service.
        :param context: Reserved.
        :param desired_capacity_type: The unit of measurement for the value specified for desired capacity.
        :param default_instance_warmup: The amount of time, in seconds, until a new instance is considered to
        have finished initializing and resource consumption to become stable
        after it enters the ``InService`` state.
        :param traffic_sources: The list of traffic sources to attach to this Auto Scaling group.
        :param instance_maintenance_policy: An instance maintenance policy.
        :param availability_zone_distribution: The instance capacity distribution across Availability Zones.
        :param availability_zone_impairment_policy: The policy for Availability Zone impairment.
        :param skip_zonal_shift_validation: If you enable zonal shift with cross-zone disabled load balancers,
        capacity could become imbalanced across Availability Zones.
        :param capacity_reservation_specification: The capacity reservation specification for the Auto Scaling group.
        :raises AlreadyExistsFault:
        :raises LimitExceededFault:
        :raises ResourceContentionFault:
        :raises ServiceLinkedRoleFailure:
        """
        raise NotImplementedError

    @handler("CreateLaunchConfiguration")
    def create_launch_configuration(
        self,
        context: RequestContext,
        launch_configuration_name: XmlStringMaxLen255,
        image_id: XmlStringMaxLen255 | None = None,
        key_name: XmlStringMaxLen255 | None = None,
        security_groups: SecurityGroups | None = None,
        classic_link_vpc_id: XmlStringMaxLen255 | None = None,
        classic_link_vpc_security_groups: ClassicLinkVPCSecurityGroups | None = None,
        user_data: XmlStringUserData | None = None,
        instance_id: XmlStringMaxLen19 | None = None,
        instance_type: XmlStringMaxLen255 | None = None,
        kernel_id: XmlStringMaxLen255 | None = None,
        ramdisk_id: XmlStringMaxLen255 | None = None,
        block_device_mappings: BlockDeviceMappings | None = None,
        instance_monitoring: InstanceMonitoring | None = None,
        spot_price: SpotPrice | None = None,
        iam_instance_profile: XmlStringMaxLen1600 | None = None,
        ebs_optimized: EbsOptimized | None = None,
        associate_public_ip_address: AssociatePublicIpAddress | None = None,
        placement_tenancy: XmlStringMaxLen64 | None = None,
        metadata_options: InstanceMetadataOptions | None = None,
        **kwargs,
    ) -> None:
        """Creates a launch configuration.

        If you exceed your maximum limit of launch configurations, the call
        fails. To query this limit, call the
        `DescribeAccountLimits <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html>`__
        API. For information about updating this limit, see `Quotas for Amazon
        EC2 Auto
        Scaling <https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-quotas.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        For more information, see `Launch
        configurations <https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-configurations.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        Amazon EC2 Auto Scaling configures instances launched as part of an Auto
        Scaling group using either a launch template or a launch configuration.
        We strongly recommend that you do not use launch configurations. They do
        not provide full functionality for Amazon EC2 Auto Scaling or Amazon
        EC2. For information about using launch templates, see `Launch
        templates <https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        :param launch_configuration_name: The name of the launch configuration.
        :param image_id: The ID of the Amazon Machine Image (AMI) that was assigned during
        registration.
        :param key_name: The name of the key pair.
        :param security_groups: A list that contains the security group IDs to assign to the instances
        in the Auto Scaling group.
        :param classic_link_vpc_id: Available for backward compatibility.
        :param classic_link_vpc_security_groups: Available for backward compatibility.
        :param user_data: The user data to make available to the launched EC2 instances.
        :param instance_id: The ID of the instance to use to create the launch configuration.
        :param instance_type: Specifies the instance type of the EC2 instance.
        :param kernel_id: The ID of the kernel associated with the AMI.
        :param ramdisk_id: The ID of the RAM disk to select.
        :param block_device_mappings: The block device mapping entries that define the block devices to attach
        to the instances at launch.
        :param instance_monitoring: Controls whether instances in this group are launched with detailed
        (``true``) or basic (``false``) monitoring.
        :param spot_price: The maximum hourly price to be paid for any Spot Instance launched to
        fulfill the request.
        :param iam_instance_profile: The name or the Amazon Resource Name (ARN) of the instance profile
        associated with the IAM role for the instance.
        :param ebs_optimized: Specifies whether the launch configuration is optimized for EBS I/O
        (``true``) or not (``false``).
        :param associate_public_ip_address: Specifies whether to assign a public IPv4 address to the group's
        instances.
        :param placement_tenancy: The tenancy of the instance, either ``default`` or ``dedicated``.
        :param metadata_options: The metadata options for the instances.
        :raises AlreadyExistsFault:
        :raises LimitExceededFault:
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("CreateOrUpdateTags")
    def create_or_update_tags(self, context: RequestContext, tags: Tags, **kwargs) -> None:
        """Creates or updates tags for the specified Auto Scaling group.

        When you specify a tag with a key that already exists, the operation
        overwrites the previous tag definition, and you do not get an error
        message.

        For more information, see `Tag Auto Scaling groups and
        instances <https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-tagging.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        :param tags: One or more tags.
        :raises LimitExceededFault:
        :raises AlreadyExistsFault:
        :raises ResourceContentionFault:
        :raises ResourceInUseFault:
        """
        raise NotImplementedError

    @handler("DeleteAutoScalingGroup")
    def delete_auto_scaling_group(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        force_delete: ForceDelete | None = None,
        **kwargs,
    ) -> None:
        """Deletes the specified Auto Scaling group.

        If the group has instances or scaling activities in progress, you must
        specify the option to force the deletion in order for it to succeed. The
        force delete operation will also terminate the EC2 instances. If the
        group has a warm pool, the force delete option also deletes the warm
        pool.

        To remove instances from the Auto Scaling group before deleting it, call
        the
        `DetachInstances <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachInstances.html>`__
        API with the list of instances and the option to decrement the desired
        capacity. This ensures that Amazon EC2 Auto Scaling does not launch
        replacement instances.

        To terminate all instances before deleting the Auto Scaling group, call
        the
        `UpdateAutoScalingGroup <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_UpdateAutoScalingGroup.html>`__
        API and set the minimum size and desired capacity of the Auto Scaling
        group to zero.

        If the group has scaling policies, deleting the group deletes the
        policies, the underlying alarm actions, and any alarm that no longer has
        an associated action.

        For more information, see `Delete your Auto Scaling
        infrastructure <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-process-shutdown.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param force_delete: Specifies that the group is to be deleted along with all instances
        associated with the group, without waiting for all instances to be
        terminated.
        :raises ScalingActivityInProgressFault:
        :raises ResourceInUseFault:
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("DeleteLaunchConfiguration")
    def delete_launch_configuration(
        self, context: RequestContext, launch_configuration_name: XmlStringMaxLen255, **kwargs
    ) -> None:
        """Deletes the specified launch configuration.

        The launch configuration must not be attached to an Auto Scaling group.
        When this call completes, the launch configuration is no longer
        available for use.

        :param launch_configuration_name: The name of the launch configuration.
        :raises ResourceInUseFault:
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("DeleteLifecycleHook")
    def delete_lifecycle_hook(
        self,
        context: RequestContext,
        lifecycle_hook_name: AsciiStringMaxLen255,
        auto_scaling_group_name: XmlStringMaxLen255,
        **kwargs,
    ) -> DeleteLifecycleHookAnswer:
        """Deletes the specified lifecycle hook.

        If there are any outstanding lifecycle actions, they are completed first
        (``ABANDON`` for launching instances, ``CONTINUE`` for terminating
        instances).

        :param lifecycle_hook_name: The name of the lifecycle hook.
        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :returns: DeleteLifecycleHookAnswer
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("DeleteNotificationConfiguration")
    def delete_notification_configuration(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        topic_arn: XmlStringMaxLen255,
        **kwargs,
    ) -> None:
        """Deletes the specified notification.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic.
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("DeletePolicy")
    def delete_policy(
        self,
        context: RequestContext,
        policy_name: ResourceName,
        auto_scaling_group_name: XmlStringMaxLen255 | None = None,
        **kwargs,
    ) -> None:
        """Deletes the specified scaling policy.

        Deleting either a step scaling policy or a simple scaling policy deletes
        the underlying alarm action, but does not delete the alarm, even if it
        no longer has an associated action.

        For more information, see `Delete a scaling
        policy <https://docs.aws.amazon.com/autoscaling/ec2/userguide/deleting-scaling-policy.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        :param policy_name: The name or Amazon Resource Name (ARN) of the policy.
        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :raises ResourceContentionFault:
        :raises ServiceLinkedRoleFailure:
        """
        raise NotImplementedError

    @handler("DeleteScheduledAction")
    def delete_scheduled_action(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        scheduled_action_name: XmlStringMaxLen255,
        **kwargs,
    ) -> None:
        """Deletes the specified scheduled action.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param scheduled_action_name: The name of the action to delete.
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("DeleteTags")
    def delete_tags(self, context: RequestContext, tags: Tags, **kwargs) -> None:
        """Deletes the specified tags.

        :param tags: One or more tags.
        :raises ResourceContentionFault:
        :raises ResourceInUseFault:
        """
        raise NotImplementedError

    @handler("DeleteWarmPool")
    def delete_warm_pool(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        force_delete: ForceDelete | None = None,
        **kwargs,
    ) -> DeleteWarmPoolAnswer:
        """Deletes the warm pool for the specified Auto Scaling group.

        For more information, see `Warm pools for Amazon EC2 Auto
        Scaling <https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param force_delete: Specifies that the warm pool is to be deleted along with all of its
        associated instances, without waiting for all instances to be
        terminated.
        :returns: DeleteWarmPoolAnswer
        :raises LimitExceededFault:
        :raises ResourceContentionFault:
        :raises ScalingActivityInProgressFault:
        :raises ResourceInUseFault:
        """
        raise NotImplementedError

    @handler("DescribeAccountLimits")
    def describe_account_limits(
        self, context: RequestContext, **kwargs
    ) -> DescribeAccountLimitsAnswer:
        """Describes the current Amazon EC2 Auto Scaling resource quotas for your
        account.

        When you establish an Amazon Web Services account, the account has
        initial quotas on the maximum number of Auto Scaling groups and launch
        configurations that you can create in a given Region. For more
        information, see `Quotas for Amazon EC2 Auto
        Scaling <https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-quotas.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        :returns: DescribeAccountLimitsAnswer
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("DescribeAdjustmentTypes")
    def describe_adjustment_types(
        self, context: RequestContext, **kwargs
    ) -> DescribeAdjustmentTypesAnswer:
        """Describes the available adjustment types for step scaling and simple
        scaling policies.

        The following adjustment types are supported:

        -  ``ChangeInCapacity``

        -  ``ExactCapacity``

        -  ``PercentChangeInCapacity``

        :returns: DescribeAdjustmentTypesAnswer
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("DescribeAutoScalingGroups")
    def describe_auto_scaling_groups(
        self,
        context: RequestContext,
        auto_scaling_group_names: AutoScalingGroupNames | None = None,
        next_token: XmlString | None = None,
        max_records: MaxRecords | None = None,
        filters: Filters | None = None,
        **kwargs,
    ) -> AutoScalingGroupsType:
        """Gets information about the Auto Scaling groups in the account and
        Region.

        If you specify Auto Scaling group names, the output includes information
        for only the specified Auto Scaling groups. If you specify filters, the
        output includes information for only those Auto Scaling groups that meet
        the filter criteria. If you do not specify group names or filters, the
        output includes information for all Auto Scaling groups.

        This operation also returns information about instances in Auto Scaling
        groups. To retrieve information about the instances in a warm pool, you
        must call the
        `DescribeWarmPool <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeWarmPool.html>`__
        API.

        :param auto_scaling_group_names: The names of the Auto Scaling groups.
        :param next_token: The token for the next set of items to return.
        :param max_records: The maximum number of items to return with this call.
        :param filters: One or more filters to limit the results based on specific tags.
        :returns: AutoScalingGroupsType
        :raises InvalidNextToken:
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("DescribeAutoScalingInstances")
    def describe_auto_scaling_instances(
        self,
        context: RequestContext,
        instance_ids: InstanceIds | None = None,
        max_records: MaxRecords | None = None,
        next_token: XmlString | None = None,
        **kwargs,
    ) -> AutoScalingInstancesType:
        """Gets information about the Auto Scaling instances in the account and
        Region.

        :param instance_ids: The IDs of the instances.
        :param max_records: The maximum number of items to return with this call.
        :param next_token: The token for the next set of items to return.
        :returns: AutoScalingInstancesType
        :raises InvalidNextToken:
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("DescribeAutoScalingNotificationTypes")
    def describe_auto_scaling_notification_types(
        self, context: RequestContext, **kwargs
    ) -> DescribeAutoScalingNotificationTypesAnswer:
        """Describes the notification types that are supported by Amazon EC2 Auto
        Scaling.

        :returns: DescribeAutoScalingNotificationTypesAnswer
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("DescribeInstanceRefreshes")
    def describe_instance_refreshes(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        instance_refresh_ids: InstanceRefreshIds | None = None,
        next_token: XmlString | None = None,
        max_records: MaxRecords | None = None,
        **kwargs,
    ) -> DescribeInstanceRefreshesAnswer:
        """Gets information about the instance refreshes for the specified Auto
        Scaling group from the previous six weeks.

        This operation is part of the `instance refresh
        feature <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html>`__
        in Amazon EC2 Auto Scaling, which helps you update instances in your
        Auto Scaling group after you make configuration changes.

        To help you determine the status of an instance refresh, Amazon EC2 Auto
        Scaling returns information about the instance refreshes you previously
        initiated, including their status, start time, end time, the percentage
        of the instance refresh that is complete, and the number of instances
        remaining to update before the instance refresh is complete. If a
        rollback is initiated while an instance refresh is in progress, Amazon
        EC2 Auto Scaling also returns information about the rollback of the
        instance refresh.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param instance_refresh_ids: One or more instance refresh IDs.
        :param next_token: The token for the next set of items to return.
        :param max_records: The maximum number of items to return with this call.
        :returns: DescribeInstanceRefreshesAnswer
        :raises InvalidNextToken:
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("DescribeLaunchConfigurations")
    def describe_launch_configurations(
        self,
        context: RequestContext,
        launch_configuration_names: LaunchConfigurationNames | None = None,
        next_token: XmlString | None = None,
        max_records: MaxRecords | None = None,
        **kwargs,
    ) -> LaunchConfigurationsType:
        """Gets information about the launch configurations in the account and
        Region.

        :param launch_configuration_names: The launch configuration names.
        :param next_token: The token for the next set of items to return.
        :param max_records: The maximum number of items to return with this call.
        :returns: LaunchConfigurationsType
        :raises InvalidNextToken:
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("DescribeLifecycleHookTypes")
    def describe_lifecycle_hook_types(
        self, context: RequestContext, **kwargs
    ) -> DescribeLifecycleHookTypesAnswer:
        """Describes the available types of lifecycle hooks.

        The following hook types are supported:

        -  ``autoscaling:EC2_INSTANCE_LAUNCHING``

        -  ``autoscaling:EC2_INSTANCE_TERMINATING``

        :returns: DescribeLifecycleHookTypesAnswer
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("DescribeLifecycleHooks")
    def describe_lifecycle_hooks(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        lifecycle_hook_names: LifecycleHookNames | None = None,
        **kwargs,
    ) -> DescribeLifecycleHooksAnswer:
        """Gets information about the lifecycle hooks for the specified Auto
        Scaling group.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param lifecycle_hook_names: The names of one or more lifecycle hooks.
        :returns: DescribeLifecycleHooksAnswer
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("DescribeLoadBalancerTargetGroups")
    def describe_load_balancer_target_groups(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        next_token: XmlString | None = None,
        max_records: MaxRecords | None = None,
        **kwargs,
    ) -> DescribeLoadBalancerTargetGroupsResponse:
        """This API operation is superseded by
        `DescribeTrafficSources <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeTrafficSources.html>`__,
        which can describe multiple traffic sources types. We recommend using
        ``DetachTrafficSources`` to simplify how you manage traffic sources.
        However, we continue to support ``DescribeLoadBalancerTargetGroups``.
        You can use both the original ``DescribeLoadBalancerTargetGroups`` API
        operation and ``DescribeTrafficSources`` on the same Auto Scaling group.

        Gets information about the Elastic Load Balancing target groups for the
        specified Auto Scaling group.

        To determine the attachment status of the target group, use the
        ``State`` element in the response. When you attach a target group to an
        Auto Scaling group, the initial ``State`` value is ``Adding``. The state
        transitions to ``Added`` after all Auto Scaling instances are registered
        with the target group. If Elastic Load Balancing health checks are
        enabled for the Auto Scaling group, the state transitions to
        ``InService`` after at least one Auto Scaling instance passes the health
        check. When the target group is in the ``InService`` state, Amazon EC2
        Auto Scaling can terminate and replace any instances that are reported
        as unhealthy. If no registered instances pass the health checks, the
        target group doesn't enter the ``InService`` state.

        Target groups also have an ``InService`` state if you attach them in the
        `CreateAutoScalingGroup <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CreateAutoScalingGroup.html>`__
        API call. If your target group state is ``InService``, but it is not
        working properly, check the scaling activities by calling
        `DescribeScalingActivities <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeScalingActivities.html>`__
        and take any corrective actions necessary.

        For help with failed health checks, see `Troubleshooting Amazon EC2 Auto
        Scaling: Health
        checks <https://docs.aws.amazon.com/autoscaling/ec2/userguide/ts-as-healthchecks.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*. For more information, see
        `Use Elastic Load Balancing to distribute traffic across the instances
        in your Auto Scaling
        group <https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        You can use this operation to describe target groups that were attached
        by using
        `AttachLoadBalancerTargetGroups <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AttachLoadBalancerTargetGroups.html>`__,
        but not for target groups that were attached by using
        `AttachTrafficSources <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AttachTrafficSources.html>`__.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param next_token: The token for the next set of items to return.
        :param max_records: The maximum number of items to return with this call.
        :returns: DescribeLoadBalancerTargetGroupsResponse
        :raises ResourceContentionFault:
        :raises InvalidNextToken:
        """
        raise NotImplementedError

    @handler("DescribeLoadBalancers")
    def describe_load_balancers(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        next_token: XmlString | None = None,
        max_records: MaxRecords | None = None,
        **kwargs,
    ) -> DescribeLoadBalancersResponse:
        """This API operation is superseded by
        `DescribeTrafficSources <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeTrafficSources.html>`__,
        which can describe multiple traffic sources types. We recommend using
        ``DescribeTrafficSources`` to simplify how you manage traffic sources.
        However, we continue to support ``DescribeLoadBalancers``. You can use
        both the original ``DescribeLoadBalancers`` API operation and
        ``DescribeTrafficSources`` on the same Auto Scaling group.

        Gets information about the load balancers for the specified Auto Scaling
        group.

        This operation describes only Classic Load Balancers. If you have
        Application Load Balancers, Network Load Balancers, or Gateway Load
        Balancers, use the
        `DescribeLoadBalancerTargetGroups <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeLoadBalancerTargetGroups.html>`__
        API instead.

        To determine the attachment status of the load balancer, use the
        ``State`` element in the response. When you attach a load balancer to an
        Auto Scaling group, the initial ``State`` value is ``Adding``. The state
        transitions to ``Added`` after all Auto Scaling instances are registered
        with the load balancer. If Elastic Load Balancing health checks are
        enabled for the Auto Scaling group, the state transitions to
        ``InService`` after at least one Auto Scaling instance passes the health
        check. When the load balancer is in the ``InService`` state, Amazon EC2
        Auto Scaling can terminate and replace any instances that are reported
        as unhealthy. If no registered instances pass the health checks, the
        load balancer doesn't enter the ``InService`` state.

        Load balancers also have an ``InService`` state if you attach them in
        the
        `CreateAutoScalingGroup <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CreateAutoScalingGroup.html>`__
        API call. If your load balancer state is ``InService``, but it is not
        working properly, check the scaling activities by calling
        `DescribeScalingActivities <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeScalingActivities.html>`__
        and take any corrective actions necessary.

        For help with failed health checks, see `Troubleshooting Amazon EC2 Auto
        Scaling: Health
        checks <https://docs.aws.amazon.com/autoscaling/ec2/userguide/ts-as-healthchecks.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*. For more information, see
        `Use Elastic Load Balancing to distribute traffic across the instances
        in your Auto Scaling
        group <https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param next_token: The token for the next set of items to return.
        :param max_records: The maximum number of items to return with this call.
        :returns: DescribeLoadBalancersResponse
        :raises ResourceContentionFault:
        :raises InvalidNextToken:
        """
        raise NotImplementedError

    @handler("DescribeMetricCollectionTypes")
    def describe_metric_collection_types(
        self, context: RequestContext, **kwargs
    ) -> DescribeMetricCollectionTypesAnswer:
        """Describes the available CloudWatch metrics for Amazon EC2 Auto Scaling.

        :returns: DescribeMetricCollectionTypesAnswer
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("DescribeNotificationConfigurations")
    def describe_notification_configurations(
        self,
        context: RequestContext,
        auto_scaling_group_names: AutoScalingGroupNames | None = None,
        next_token: XmlString | None = None,
        max_records: MaxRecords | None = None,
        **kwargs,
    ) -> DescribeNotificationConfigurationsAnswer:
        """Gets information about the Amazon SNS notifications that are configured
        for one or more Auto Scaling groups.

        :param auto_scaling_group_names: The name of the Auto Scaling group.
        :param next_token: The token for the next set of items to return.
        :param max_records: The maximum number of items to return with this call.
        :returns: DescribeNotificationConfigurationsAnswer
        :raises InvalidNextToken:
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("DescribePolicies")
    def describe_policies(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255 | None = None,
        policy_names: PolicyNames | None = None,
        policy_types: PolicyTypes | None = None,
        next_token: XmlString | None = None,
        max_records: MaxRecords | None = None,
        **kwargs,
    ) -> PoliciesType:
        """Gets information about the scaling policies in the account and Region.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param policy_names: The names of one or more policies.
        :param policy_types: One or more policy types.
        :param next_token: The token for the next set of items to return.
        :param max_records: The maximum number of items to be returned with each call.
        :returns: PoliciesType
        :raises InvalidNextToken:
        :raises ResourceContentionFault:
        :raises ServiceLinkedRoleFailure:
        """
        raise NotImplementedError

    @handler("DescribeScalingActivities")
    def describe_scaling_activities(
        self,
        context: RequestContext,
        activity_ids: ActivityIds | None = None,
        auto_scaling_group_name: XmlStringMaxLen255 | None = None,
        include_deleted_groups: IncludeDeletedGroups | None = None,
        max_records: MaxRecords | None = None,
        next_token: XmlString | None = None,
        **kwargs,
    ) -> ActivitiesType:
        """Gets information about the scaling activities in the account and Region.

        When scaling events occur, you see a record of the scaling activity in
        the scaling activities. For more information, see `Verify a scaling
        activity for an Auto Scaling
        group <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-verify-scaling-activity.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        If the scaling event succeeds, the value of the ``StatusCode`` element
        in the response is ``Successful``. If an attempt to launch instances
        failed, the ``StatusCode`` value is ``Failed`` or ``Cancelled`` and the
        ``StatusMessage`` element in the response indicates the cause of the
        failure. For help interpreting the ``StatusMessage``, see
        `Troubleshooting Amazon EC2 Auto
        Scaling <https://docs.aws.amazon.com/autoscaling/ec2/userguide/CHAP_Troubleshooting.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        :param activity_ids: The activity IDs of the desired scaling activities.
        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param include_deleted_groups: Indicates whether to include scaling activity from deleted Auto Scaling
        groups.
        :param max_records: The maximum number of items to return with this call.
        :param next_token: The token for the next set of items to return.
        :returns: ActivitiesType
        :raises InvalidNextToken:
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("DescribeScalingProcessTypes")
    def describe_scaling_process_types(self, context: RequestContext, **kwargs) -> ProcessesType:
        """Describes the scaling process types for use with the
        `ResumeProcesses <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_ResumeProcesses.html>`__
        and
        `SuspendProcesses <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_SuspendProcesses.html>`__
        APIs.

        :returns: ProcessesType
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("DescribeScheduledActions")
    def describe_scheduled_actions(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255 | None = None,
        scheduled_action_names: ScheduledActionNames | None = None,
        start_time: TimestampType | None = None,
        end_time: TimestampType | None = None,
        next_token: XmlString | None = None,
        max_records: MaxRecords | None = None,
        **kwargs,
    ) -> ScheduledActionsType:
        """Gets information about the scheduled actions that haven't run or that
        have not reached their end time.

        To describe the scaling activities for scheduled actions that have
        already run, call the
        `DescribeScalingActivities <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeScalingActivities.html>`__
        API.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param scheduled_action_names: The names of one or more scheduled actions.
        :param start_time: The earliest scheduled start time to return.
        :param end_time: The latest scheduled start time to return.
        :param next_token: The token for the next set of items to return.
        :param max_records: The maximum number of items to return with this call.
        :returns: ScheduledActionsType
        :raises InvalidNextToken:
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("DescribeTags")
    def describe_tags(
        self,
        context: RequestContext,
        filters: Filters | None = None,
        next_token: XmlString | None = None,
        max_records: MaxRecords | None = None,
        **kwargs,
    ) -> TagsType:
        """Describes the specified tags.

        You can use filters to limit the results. For example, you can query for
        the tags for a specific Auto Scaling group. You can specify multiple
        values for a filter. A tag must match at least one of the specified
        values for it to be included in the results.

        You can also specify multiple filters. The result includes information
        for a particular tag only if it matches all the filters. If there's no
        match, no special message is returned.

        For more information, see `Tag Auto Scaling groups and
        instances <https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-tagging.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        :param filters: One or more filters to scope the tags to return.
        :param next_token: The token for the next set of items to return.
        :param max_records: The maximum number of items to return with this call.
        :returns: TagsType
        :raises InvalidNextToken:
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("DescribeTerminationPolicyTypes")
    def describe_termination_policy_types(
        self, context: RequestContext, **kwargs
    ) -> DescribeTerminationPolicyTypesAnswer:
        """Describes the termination policies supported by Amazon EC2 Auto Scaling.

        For more information, see `Configure termination policies for Amazon EC2
        Auto
        Scaling <https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-termination-policies.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        :returns: DescribeTerminationPolicyTypesAnswer
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("DescribeTrafficSources")
    def describe_traffic_sources(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        traffic_source_type: XmlStringMaxLen255 | None = None,
        next_token: XmlString | None = None,
        max_records: MaxRecords | None = None,
        **kwargs,
    ) -> DescribeTrafficSourcesResponse:
        """Gets information about the traffic sources for the specified Auto
        Scaling group.

        You can optionally provide a traffic source type. If you provide a
        traffic source type, then the results only include that traffic source
        type.

        If you do not provide a traffic source type, then the results include
        all the traffic sources for the specified Auto Scaling group.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param traffic_source_type: The traffic source type that you want to describe.
        :param next_token: The token for the next set of items to return.
        :param max_records: The maximum number of items to return with this call.
        :returns: DescribeTrafficSourcesResponse
        :raises ResourceContentionFault:
        :raises InvalidNextToken:
        """
        raise NotImplementedError

    @handler("DescribeWarmPool")
    def describe_warm_pool(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        max_records: MaxRecords | None = None,
        next_token: XmlString | None = None,
        **kwargs,
    ) -> DescribeWarmPoolAnswer:
        """Gets information about a warm pool and its instances.

        For more information, see `Warm pools for Amazon EC2 Auto
        Scaling <https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param max_records: The maximum number of instances to return with this call.
        :param next_token: The token for the next set of instances to return.
        :returns: DescribeWarmPoolAnswer
        :raises InvalidNextToken:
        :raises LimitExceededFault:
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("DetachInstances")
    def detach_instances(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        should_decrement_desired_capacity: ShouldDecrementDesiredCapacity,
        instance_ids: InstanceIds | None = None,
        **kwargs,
    ) -> DetachInstancesAnswer:
        """Removes one or more instances from the specified Auto Scaling group.

        After the instances are detached, you can manage them independent of the
        Auto Scaling group.

        If you do not specify the option to decrement the desired capacity,
        Amazon EC2 Auto Scaling launches instances to replace the ones that are
        detached.

        If there is a Classic Load Balancer attached to the Auto Scaling group,
        the instances are deregistered from the load balancer. If there are
        target groups attached to the Auto Scaling group, the instances are
        deregistered from the target groups.

        For more information, see `Detach or attach
        instances <https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-detach-attach-instances.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param should_decrement_desired_capacity: Indicates whether the Auto Scaling group decrements the desired capacity
        value by the number of instances detached.
        :param instance_ids: The IDs of the instances.
        :returns: DetachInstancesAnswer
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("DetachLoadBalancerTargetGroups")
    def detach_load_balancer_target_groups(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        target_group_arns: TargetGroupARNs,
        **kwargs,
    ) -> DetachLoadBalancerTargetGroupsResultType:
        """This API operation is superseded by
        `DetachTrafficSources <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeTrafficSources.html>`__,
        which can detach multiple traffic sources types. We recommend using
        ``DetachTrafficSources`` to simplify how you manage traffic sources.
        However, we continue to support ``DetachLoadBalancerTargetGroups``. You
        can use both the original ``DetachLoadBalancerTargetGroups`` API
        operation and ``DetachTrafficSources`` on the same Auto Scaling group.

        Detaches one or more target groups from the specified Auto Scaling
        group.

        When you detach a target group, it enters the ``Removing`` state while
        deregistering the instances in the group. When all instances are
        deregistered, then you can no longer describe the target group using the
        `DescribeLoadBalancerTargetGroups <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeLoadBalancerTargetGroups.html>`__
        API call. The instances remain running.

        You can use this operation to detach target groups that were attached by
        using
        `AttachLoadBalancerTargetGroups <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AttachLoadBalancerTargetGroups.html>`__,
        but not for target groups that were attached by using
        `AttachTrafficSources <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AttachTrafficSources.html>`__.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param target_group_arns: The Amazon Resource Names (ARN) of the target groups.
        :returns: DetachLoadBalancerTargetGroupsResultType
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("DetachLoadBalancers")
    def detach_load_balancers(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        load_balancer_names: LoadBalancerNames,
        **kwargs,
    ) -> DetachLoadBalancersResultType:
        """This API operation is superseded by
        `DetachTrafficSources <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachTrafficSources.html>`__,
        which can detach multiple traffic sources types. We recommend using
        ``DetachTrafficSources`` to simplify how you manage traffic sources.
        However, we continue to support ``DetachLoadBalancers``. You can use
        both the original ``DetachLoadBalancers`` API operation and
        ``DetachTrafficSources`` on the same Auto Scaling group.

        Detaches one or more Classic Load Balancers from the specified Auto
        Scaling group.

        This operation detaches only Classic Load Balancers. If you have
        Application Load Balancers, Network Load Balancers, or Gateway Load
        Balancers, use the
        `DetachLoadBalancerTargetGroups <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachLoadBalancerTargetGroups.html>`__
        API instead.

        When you detach a load balancer, it enters the ``Removing`` state while
        deregistering the instances in the group. When all instances are
        deregistered, then you can no longer describe the load balancer using
        the
        `DescribeLoadBalancers <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeLoadBalancers.html>`__
        API call. The instances remain running.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param load_balancer_names: The names of the load balancers.
        :returns: DetachLoadBalancersResultType
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("DetachTrafficSources")
    def detach_traffic_sources(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        traffic_sources: TrafficSources,
        **kwargs,
    ) -> DetachTrafficSourcesResultType:
        """Detaches one or more traffic sources from the specified Auto Scaling
        group.

        When you detach a traffic source, it enters the ``Removing`` state while
        deregistering the instances in the group. When all instances are
        deregistered, then you can no longer describe the traffic source using
        the
        `DescribeTrafficSources <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeTrafficSources.html>`__
        API call. The instances continue to run.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param traffic_sources: The unique identifiers of one or more traffic sources.
        :returns: DetachTrafficSourcesResultType
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("DisableMetricsCollection")
    def disable_metrics_collection(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        metrics: Metrics | None = None,
        **kwargs,
    ) -> None:
        """Disables group metrics collection for the specified Auto Scaling group.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param metrics: Identifies the metrics to disable.
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("EnableMetricsCollection")
    def enable_metrics_collection(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        granularity: XmlStringMaxLen255,
        metrics: Metrics | None = None,
        **kwargs,
    ) -> None:
        """Enables group metrics collection for the specified Auto Scaling group.

        You can use these metrics to track changes in an Auto Scaling group and
        to set alarms on threshold values. You can view group metrics using the
        Amazon EC2 Auto Scaling console or the CloudWatch console. For more
        information, see `Monitor CloudWatch metrics for your Auto Scaling
        groups and
        instances <https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-cloudwatch-monitoring.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param granularity: The frequency at which Amazon EC2 Auto Scaling sends aggregated data to
        CloudWatch.
        :param metrics: Identifies the metrics to enable.
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("EnterStandby")
    def enter_standby(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        should_decrement_desired_capacity: ShouldDecrementDesiredCapacity,
        instance_ids: InstanceIds | None = None,
        **kwargs,
    ) -> EnterStandbyAnswer:
        """Moves the specified instances into the standby state.

        If you choose to decrement the desired capacity of the Auto Scaling
        group, the instances can enter standby as long as the desired capacity
        of the Auto Scaling group after the instances are placed into standby is
        equal to or greater than the minimum capacity of the group.

        If you choose not to decrement the desired capacity of the Auto Scaling
        group, the Auto Scaling group launches new instances to replace the
        instances on standby.

        For more information, see `Temporarily removing instances from your Auto
        Scaling
        group <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-enter-exit-standby.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param should_decrement_desired_capacity: Indicates whether to decrement the desired capacity of the Auto Scaling
        group by the number of instances moved to ``Standby`` mode.
        :param instance_ids: The IDs of the instances.
        :returns: EnterStandbyAnswer
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("ExecutePolicy")
    def execute_policy(
        self,
        context: RequestContext,
        policy_name: ResourceName,
        auto_scaling_group_name: XmlStringMaxLen255 | None = None,
        honor_cooldown: HonorCooldown | None = None,
        metric_value: MetricScale | None = None,
        breach_threshold: MetricScale | None = None,
        **kwargs,
    ) -> None:
        """Executes the specified policy. This can be useful for testing the design
        of your scaling policy.

        :param policy_name: The name or ARN of the policy.
        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param honor_cooldown: Indicates whether Amazon EC2 Auto Scaling waits for the cooldown period
        to complete before executing the policy.
        :param metric_value: The metric value to compare to ``BreachThreshold``.
        :param breach_threshold: The breach threshold for the alarm.
        :raises ScalingActivityInProgressFault:
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("ExitStandby")
    def exit_standby(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        instance_ids: InstanceIds | None = None,
        **kwargs,
    ) -> ExitStandbyAnswer:
        """Moves the specified instances out of the standby state.

        After you put the instances back in service, the desired capacity is
        incremented.

        For more information, see `Temporarily removing instances from your Auto
        Scaling
        group <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-enter-exit-standby.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param instance_ids: The IDs of the instances.
        :returns: ExitStandbyAnswer
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("GetPredictiveScalingForecast")
    def get_predictive_scaling_forecast(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        policy_name: XmlStringMaxLen255,
        start_time: TimestampType,
        end_time: TimestampType,
        **kwargs,
    ) -> GetPredictiveScalingForecastAnswer:
        """Retrieves the forecast data for a predictive scaling policy.

        Load forecasts are predictions of the hourly load values using
        historical load data from CloudWatch and an analysis of historical
        trends. Capacity forecasts are represented as predicted values for the
        minimum capacity that is needed on an hourly basis, based on the hourly
        load forecast.

        A minimum of 24 hours of data is required to create the initial
        forecasts. However, having a full 14 days of historical data results in
        more accurate forecasts.

        For more information, see `Predictive scaling for Amazon EC2 Auto
        Scaling <https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param policy_name: The name of the policy.
        :param start_time: The inclusive start time of the time range for the forecast data to get.
        :param end_time: The exclusive end time of the time range for the forecast data to get.
        :returns: GetPredictiveScalingForecastAnswer
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("PutLifecycleHook")
    def put_lifecycle_hook(
        self,
        context: RequestContext,
        lifecycle_hook_name: AsciiStringMaxLen255,
        auto_scaling_group_name: XmlStringMaxLen255,
        lifecycle_transition: LifecycleTransition | None = None,
        role_arn: XmlStringMaxLen255 | None = None,
        notification_target_arn: NotificationTargetResourceName | None = None,
        notification_metadata: AnyPrintableAsciiStringMaxLen4000 | None = None,
        heartbeat_timeout: HeartbeatTimeout | None = None,
        default_result: LifecycleActionResult | None = None,
        **kwargs,
    ) -> PutLifecycleHookAnswer:
        """Creates or updates a lifecycle hook for the specified Auto Scaling
        group.

        Lifecycle hooks let you create solutions that are aware of events in the
        Auto Scaling instance lifecycle, and then perform a custom action on
        instances when the corresponding lifecycle event occurs.

        This step is a part of the procedure for adding a lifecycle hook to an
        Auto Scaling group:

        #. (Optional) Create a launch template or launch configuration with a
           user data script that runs while an instance is in a wait state due
           to a lifecycle hook.

        #. (Optional) Create a Lambda function and a rule that allows Amazon
           EventBridge to invoke your Lambda function when an instance is put
           into a wait state due to a lifecycle hook.

        #. (Optional) Create a notification target and an IAM role. The target
           can be either an Amazon SQS queue or an Amazon SNS topic. The role
           allows Amazon EC2 Auto Scaling to publish lifecycle notifications to
           the target.

        #. **Create the lifecycle hook. Specify whether the hook is used when
           the instances launch or terminate.**

        #. If you need more time, record the lifecycle action heartbeat to keep
           the instance in a wait state using the
           `RecordLifecycleActionHeartbeat <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_RecordLifecycleActionHeartbeat.html>`__
           API call.

        #. If you finish before the timeout period ends, send a callback by
           using the
           `CompleteLifecycleAction <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CompleteLifecycleAction.html>`__
           API call.

        For more information, see `Amazon EC2 Auto Scaling lifecycle
        hooks <https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        If you exceed your maximum limit of lifecycle hooks, which by default is
        50 per Auto Scaling group, the call fails.

        You can view the lifecycle hooks for an Auto Scaling group using the
        `DescribeLifecycleHooks <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeLifecycleHooks.html>`__
        API call. If you are no longer using a lifecycle hook, you can delete it
        by calling the
        `DeleteLifecycleHook <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DeleteLifecycleHook.html>`__
        API.

        :param lifecycle_hook_name: The name of the lifecycle hook.
        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param lifecycle_transition: The lifecycle transition.
        :param role_arn: The ARN of the IAM role that allows the Auto Scaling group to publish to
        the specified notification target.
        :param notification_target_arn: The Amazon Resource Name (ARN) of the notification target that Amazon
        EC2 Auto Scaling uses to notify you when an instance is in a wait state
        for the lifecycle hook.
        :param notification_metadata: Additional information that you want to include any time Amazon EC2 Auto
        Scaling sends a message to the notification target.
        :param heartbeat_timeout: The maximum time, in seconds, that can elapse before the lifecycle hook
        times out.
        :param default_result: The action the Auto Scaling group takes when the lifecycle hook timeout
        elapses or if an unexpected failure occurs.
        :returns: PutLifecycleHookAnswer
        :raises LimitExceededFault:
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("PutNotificationConfiguration")
    def put_notification_configuration(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        topic_arn: XmlStringMaxLen255,
        notification_types: AutoScalingNotificationTypes,
        **kwargs,
    ) -> None:
        """Configures an Auto Scaling group to send notifications when specified
        events take place. Subscribers to the specified topic can have messages
        delivered to an endpoint such as a web server or an email address.

        This configuration overwrites any existing configuration.

        For more information, see `Amazon SNS notification options for Amazon
        EC2 Auto
        Scaling <https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-sns-notifications.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        If you exceed your maximum limit of SNS topics, which is 10 per Auto
        Scaling group, the call fails.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic.
        :param notification_types: The type of event that causes the notification to be sent.
        :raises LimitExceededFault:
        :raises ResourceContentionFault:
        :raises ServiceLinkedRoleFailure:
        """
        raise NotImplementedError

    @handler("PutScalingPolicy")
    def put_scaling_policy(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        policy_name: XmlStringMaxLen255,
        policy_type: XmlStringMaxLen64 | None = None,
        adjustment_type: XmlStringMaxLen255 | None = None,
        min_adjustment_step: MinAdjustmentStep | None = None,
        min_adjustment_magnitude: MinAdjustmentMagnitude | None = None,
        scaling_adjustment: PolicyIncrement | None = None,
        cooldown: Cooldown | None = None,
        metric_aggregation_type: XmlStringMaxLen32 | None = None,
        step_adjustments: StepAdjustments | None = None,
        estimated_instance_warmup: EstimatedInstanceWarmup | None = None,
        target_tracking_configuration: TargetTrackingConfiguration | None = None,
        enabled: ScalingPolicyEnabled | None = None,
        predictive_scaling_configuration: PredictiveScalingConfiguration | None = None,
        **kwargs,
    ) -> PolicyARNType:
        """Creates or updates a scaling policy for an Auto Scaling group. Scaling
        policies are used to scale an Auto Scaling group based on configurable
        metrics. If no policies are defined, the dynamic scaling and predictive
        scaling features are not used.

        For more information about using dynamic scaling, see `Target tracking
        scaling
        policies <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html>`__
        and `Step and simple scaling
        policies <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        For more information about using predictive scaling, see `Predictive
        scaling for Amazon EC2 Auto
        Scaling <https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        You can view the scaling policies for an Auto Scaling group using the
        `DescribePolicies <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribePolicies.html>`__
        API call. If you are no longer using a scaling policy, you can delete it
        by calling the
        `DeletePolicy <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DeletePolicy.html>`__
        API.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param policy_name: The name of the policy.
        :param policy_type: One of the following policy types:

        -  ``TargetTrackingScaling``

        -  ``StepScaling``

        -  ``SimpleScaling`` (default)

        -  ``PredictiveScaling``.
        :param adjustment_type: Specifies how the scaling adjustment is interpreted (for example, an
        absolute number or a percentage).
        :param min_adjustment_step: Available for backward compatibility.
        :param min_adjustment_magnitude: The minimum value to scale by when the adjustment type is
        ``PercentChangeInCapacity``.
        :param scaling_adjustment: The amount by which to scale, based on the specified adjustment type.
        :param cooldown: A cooldown period, in seconds, that applies to a specific simple scaling
        policy.
        :param metric_aggregation_type: The aggregation type for the CloudWatch metrics.
        :param step_adjustments: A set of adjustments that enable you to scale based on the size of the
        alarm breach.
        :param estimated_instance_warmup: *Not needed if the default instance warmup is defined for the group.
        :param target_tracking_configuration: A target tracking scaling policy.
        :param enabled: Indicates whether the scaling policy is enabled or disabled.
        :param predictive_scaling_configuration: A predictive scaling policy.
        :returns: PolicyARNType
        :raises LimitExceededFault:
        :raises ResourceContentionFault:
        :raises ServiceLinkedRoleFailure:
        """
        raise NotImplementedError

    @handler("PutScheduledUpdateGroupAction")
    def put_scheduled_update_group_action(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        scheduled_action_name: XmlStringMaxLen255,
        time: TimestampType | None = None,
        start_time: TimestampType | None = None,
        end_time: TimestampType | None = None,
        recurrence: XmlStringMaxLen255 | None = None,
        min_size: AutoScalingGroupMinSize | None = None,
        max_size: AutoScalingGroupMaxSize | None = None,
        desired_capacity: AutoScalingGroupDesiredCapacity | None = None,
        time_zone: XmlStringMaxLen255 | None = None,
        **kwargs,
    ) -> None:
        """Creates or updates a scheduled scaling action for an Auto Scaling group.

        For more information, see `Scheduled
        scaling <https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        You can view the scheduled actions for an Auto Scaling group using the
        `DescribeScheduledActions <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeScheduledActions.html>`__
        API call. If you are no longer using a scheduled action, you can delete
        it by calling the
        `DeleteScheduledAction <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DeleteScheduledAction.html>`__
        API.

        If you try to schedule your action in the past, Amazon EC2 Auto Scaling
        returns an error message.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param scheduled_action_name: The name of this scaling action.
        :param time: This property is no longer used.
        :param start_time: The date and time for this action to start, in YYYY-MM-DDThh:mm:ssZ
        format in UTC/GMT only and in quotes (for example,
        ``"2021-06-01T00:00:00Z"``).
        :param end_time: The date and time for the recurring schedule to end, in UTC.
        :param recurrence: The recurring schedule for this action.
        :param min_size: The minimum size of the Auto Scaling group.
        :param max_size: The maximum size of the Auto Scaling group.
        :param desired_capacity: The desired capacity is the initial capacity of the Auto Scaling group
        after the scheduled action runs and the capacity it attempts to
        maintain.
        :param time_zone: Specifies the time zone for a cron expression.
        :raises AlreadyExistsFault:
        :raises LimitExceededFault:
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("PutWarmPool")
    def put_warm_pool(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        max_group_prepared_capacity: MaxGroupPreparedCapacity | None = None,
        min_size: WarmPoolMinSize | None = None,
        pool_state: WarmPoolState | None = None,
        instance_reuse_policy: InstanceReusePolicy | None = None,
        **kwargs,
    ) -> PutWarmPoolAnswer:
        """Creates or updates a warm pool for the specified Auto Scaling group. A
        warm pool is a pool of pre-initialized EC2 instances that sits alongside
        the Auto Scaling group. Whenever your application needs to scale out,
        the Auto Scaling group can draw on the warm pool to meet its new desired
        capacity.

        This operation must be called from the Region in which the Auto Scaling
        group was created.

        You can view the instances in the warm pool using the
        `DescribeWarmPool <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeWarmPool.html>`__
        API call. If you are no longer using a warm pool, you can delete it by
        calling the
        `DeleteWarmPool <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DeleteWarmPool.html>`__
        API.

        For more information, see `Warm pools for Amazon EC2 Auto
        Scaling <https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param max_group_prepared_capacity: Specifies the maximum number of instances that are allowed to be in the
        warm pool or in any state except ``Terminated`` for the Auto Scaling
        group.
        :param min_size: Specifies the minimum number of instances to maintain in the warm pool.
        :param pool_state: Sets the instance state to transition to after the lifecycle actions are
        complete.
        :param instance_reuse_policy: Indicates whether instances in the Auto Scaling group can be returned to
        the warm pool on scale in.
        :returns: PutWarmPoolAnswer
        :raises LimitExceededFault:
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("RecordLifecycleActionHeartbeat")
    def record_lifecycle_action_heartbeat(
        self,
        context: RequestContext,
        lifecycle_hook_name: AsciiStringMaxLen255,
        auto_scaling_group_name: ResourceName,
        lifecycle_action_token: LifecycleActionToken | None = None,
        instance_id: XmlStringMaxLen19 | None = None,
        **kwargs,
    ) -> RecordLifecycleActionHeartbeatAnswer:
        """Records a heartbeat for the lifecycle action associated with the
        specified token or instance. This extends the timeout by the length of
        time defined using the
        `PutLifecycleHook <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PutLifecycleHook.html>`__
        API call.

        This step is a part of the procedure for adding a lifecycle hook to an
        Auto Scaling group:

        #. (Optional) Create a launch template or launch configuration with a
           user data script that runs while an instance is in a wait state due
           to a lifecycle hook.

        #. (Optional) Create a Lambda function and a rule that allows Amazon
           EventBridge to invoke your Lambda function when an instance is put
           into a wait state due to a lifecycle hook.

        #. (Optional) Create a notification target and an IAM role. The target
           can be either an Amazon SQS queue or an Amazon SNS topic. The role
           allows Amazon EC2 Auto Scaling to publish lifecycle notifications to
           the target.

        #. Create the lifecycle hook. Specify whether the hook is used when the
           instances launch or terminate.

        #. **If you need more time, record the lifecycle action heartbeat to
           keep the instance in a wait state.**

        #. If you finish before the timeout period ends, send a callback by
           using the
           `CompleteLifecycleAction <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CompleteLifecycleAction.html>`__
           API call.

        For more information, see `Amazon EC2 Auto Scaling lifecycle
        hooks <https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        :param lifecycle_hook_name: The name of the lifecycle hook.
        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param lifecycle_action_token: A token that uniquely identifies a specific lifecycle action associated
        with an instance.
        :param instance_id: The ID of the instance.
        :returns: RecordLifecycleActionHeartbeatAnswer
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("ResumeProcesses")
    def resume_processes(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        scaling_processes: ProcessNames | None = None,
        **kwargs,
    ) -> None:
        """Resumes the specified suspended auto scaling processes, or all suspended
        process, for the specified Auto Scaling group.

        For more information, see `Suspend and resume Amazon EC2 Auto Scaling
        processes <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param scaling_processes: One or more of the following processes:

        -  ``Launch``

        -  ``Terminate``

        -  ``AddToLoadBalancer``

        -  ``AlarmNotification``

        -  ``AZRebalance``

        -  ``HealthCheck``

        -  ``InstanceRefresh``

        -  ``ReplaceUnhealthy``

        -  ``ScheduledActions``

        If you omit this property, all processes are specified.
        :raises ResourceInUseFault:
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("RollbackInstanceRefresh")
    def rollback_instance_refresh(
        self, context: RequestContext, auto_scaling_group_name: XmlStringMaxLen255, **kwargs
    ) -> RollbackInstanceRefreshAnswer:
        """Cancels an instance refresh that is in progress and rolls back any
        changes that it made. Amazon EC2 Auto Scaling replaces any instances
        that were replaced during the instance refresh. This restores your Auto
        Scaling group to the configuration that it was using before the start of
        the instance refresh.

        This operation is part of the `instance refresh
        feature <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html>`__
        in Amazon EC2 Auto Scaling, which helps you update instances in your
        Auto Scaling group after you make configuration changes.

        A rollback is not supported in the following situations:

        -  There is no desired configuration specified for the instance refresh.

        -  The Auto Scaling group has a launch template that uses an Amazon Web
           Services Systems Manager parameter instead of an AMI ID for the
           ``ImageId`` property.

        -  The Auto Scaling group uses the launch template's ``$Latest`` or
           ``$Default`` version.

        When you receive a successful response from this operation, Amazon EC2
        Auto Scaling immediately begins replacing instances. You can check the
        status of this operation through the
        `DescribeInstanceRefreshes <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeInstanceRefreshes.html>`__
        API operation.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :returns: RollbackInstanceRefreshAnswer
        :raises LimitExceededFault:
        :raises ResourceContentionFault:
        :raises ActiveInstanceRefreshNotFoundFault:
        :raises IrreversibleInstanceRefreshFault:
        """
        raise NotImplementedError

    @handler("SetDesiredCapacity")
    def set_desired_capacity(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        desired_capacity: AutoScalingGroupDesiredCapacity,
        honor_cooldown: HonorCooldown | None = None,
        **kwargs,
    ) -> None:
        """Sets the size of the specified Auto Scaling group.

        If a scale-in activity occurs as a result of a new ``DesiredCapacity``
        value that is lower than the current size of the group, the Auto Scaling
        group uses its termination policy to determine which instances to
        terminate.

        For more information, see `Manual
        scaling <https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scaling-manually.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param desired_capacity: The desired capacity is the initial capacity of the Auto Scaling group
        after this operation completes and the capacity it attempts to maintain.
        :param honor_cooldown: Indicates whether Amazon EC2 Auto Scaling waits for the cooldown period
        to complete before initiating a scaling activity to set your Auto
        Scaling group to its new capacity.
        :raises ScalingActivityInProgressFault:
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("SetInstanceHealth")
    def set_instance_health(
        self,
        context: RequestContext,
        instance_id: XmlStringMaxLen19,
        health_status: XmlStringMaxLen32,
        should_respect_grace_period: ShouldRespectGracePeriod | None = None,
        **kwargs,
    ) -> None:
        """Sets the health status of the specified instance.

        For more information, see `Set up a custom health check for your Auto
        Scaling
        group <https://docs.aws.amazon.com/autoscaling/ec2/userguide/set-up-a-custom-health-check.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        :param instance_id: The ID of the instance.
        :param health_status: The health status of the instance.
        :param should_respect_grace_period: If the Auto Scaling group of the specified instance has a
        ``HealthCheckGracePeriod`` specified for the group, by default, this
        call respects the grace period.
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("SetInstanceProtection")
    def set_instance_protection(
        self,
        context: RequestContext,
        instance_ids: InstanceIds,
        auto_scaling_group_name: XmlStringMaxLen255,
        protected_from_scale_in: ProtectedFromScaleIn,
        **kwargs,
    ) -> SetInstanceProtectionAnswer:
        """Updates the instance protection settings of the specified instances.
        This operation cannot be called on instances in a warm pool.

        For more information, see `Use instance scale-in
        protection <https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        If you exceed your maximum limit of instance IDs, which is 50 per Auto
        Scaling group, the call fails.

        :param instance_ids: One or more instance IDs.
        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param protected_from_scale_in: Indicates whether the instance is protected from termination by Amazon
        EC2 Auto Scaling when scaling in.
        :returns: SetInstanceProtectionAnswer
        :raises LimitExceededFault:
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("StartInstanceRefresh")
    def start_instance_refresh(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        strategy: RefreshStrategy | None = None,
        desired_configuration: DesiredConfiguration | None = None,
        preferences: RefreshPreferences | None = None,
        **kwargs,
    ) -> StartInstanceRefreshAnswer:
        """Starts an instance refresh.

        This operation is part of the `instance refresh
        feature <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html>`__
        in Amazon EC2 Auto Scaling, which helps you update instances in your
        Auto Scaling group. This feature is helpful, for example, when you have
        a new AMI or a new user data script. You just need to create a new
        launch template that specifies the new AMI or user data script. Then
        start an instance refresh to immediately begin the process of updating
        instances in the group.

        If successful, the request's response contains a unique ID that you can
        use to track the progress of the instance refresh. To query its status,
        call the
        `DescribeInstanceRefreshes <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeInstanceRefreshes.html>`__
        API. To describe the instance refreshes that have already run, call the
        `DescribeInstanceRefreshes <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeInstanceRefreshes.html>`__
        API. To cancel an instance refresh that is in progress, use the
        `CancelInstanceRefresh <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CancelInstanceRefresh.html>`__
        API.

        An instance refresh might fail for several reasons, such as EC2 launch
        failures, misconfigured health checks, or not ignoring or allowing the
        termination of instances that are in ``Standby`` state or protected from
        scale in. You can monitor for failed EC2 launches using the scaling
        activities. To find the scaling activities, call the
        `DescribeScalingActivities <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeScalingActivities.html>`__
        API.

        If you enable auto rollback, your Auto Scaling group will be rolled back
        automatically when the instance refresh fails. You can enable this
        feature before starting an instance refresh by specifying the
        ``AutoRollback`` property in the instance refresh preferences.
        Otherwise, to roll back an instance refresh before it finishes, use the
        `RollbackInstanceRefresh <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_RollbackInstanceRefresh.html>`__
        API.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param strategy: The strategy to use for the instance refresh.
        :param desired_configuration: The desired configuration.
        :param preferences: Sets your preferences for the instance refresh so that it performs as
        expected when you start it.
        :returns: StartInstanceRefreshAnswer
        :raises LimitExceededFault:
        :raises ResourceContentionFault:
        :raises InstanceRefreshInProgressFault:
        """
        raise NotImplementedError

    @handler("SuspendProcesses")
    def suspend_processes(
        self,
        context: RequestContext,
        auto_scaling_group_name: XmlStringMaxLen255,
        scaling_processes: ProcessNames | None = None,
        **kwargs,
    ) -> None:
        """Suspends the specified auto scaling processes, or all processes, for the
        specified Auto Scaling group.

        If you suspend either the ``Launch`` or ``Terminate`` process types, it
        can prevent other process types from functioning properly. For more
        information, see `Suspend and resume Amazon EC2 Auto Scaling
        processes <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        To resume processes that have been suspended, call the
        `ResumeProcesses <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_ResumeProcesses.html>`__
        API.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param scaling_processes: One or more of the following processes:

        -  ``Launch``

        -  ``Terminate``

        -  ``AddToLoadBalancer``

        -  ``AlarmNotification``

        -  ``AZRebalance``

        -  ``HealthCheck``

        -  ``InstanceRefresh``

        -  ``ReplaceUnhealthy``

        -  ``ScheduledActions``

        If you omit this property, all processes are specified.
        :raises ResourceInUseFault:
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("TerminateInstanceInAutoScalingGroup")
    def terminate_instance_in_auto_scaling_group(
        self,
        context: RequestContext,
        instance_id: XmlStringMaxLen19,
        should_decrement_desired_capacity: ShouldDecrementDesiredCapacity,
        **kwargs,
    ) -> ActivityType:
        """Terminates the specified instance and optionally adjusts the desired
        group size. This operation cannot be called on instances in a warm pool.

        This call simply makes a termination request. The instance is not
        terminated immediately. When an instance is terminated, the instance
        status changes to ``terminated``. You can't connect to or start an
        instance after you've terminated it.

        If you do not specify the option to decrement the desired capacity,
        Amazon EC2 Auto Scaling launches instances to replace the ones that are
        terminated.

        By default, Amazon EC2 Auto Scaling balances instances across all
        Availability Zones. If you decrement the desired capacity, your Auto
        Scaling group can become unbalanced between Availability Zones. Amazon
        EC2 Auto Scaling tries to rebalance the group, and rebalancing might
        terminate instances in other zones. For more information, see `Manual
        scaling <https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scaling-manually.html>`__
        in the *Amazon EC2 Auto Scaling User Guide*.

        :param instance_id: The ID of the instance.
        :param should_decrement_desired_capacity: Indicates whether terminating the instance also decrements the size of
        the Auto Scaling group.
        :returns: ActivityType
        :raises ScalingActivityInProgressFault:
        :raises ResourceContentionFault:
        """
        raise NotImplementedError

    @handler("UpdateAutoScalingGroup", expand=False)
    def update_auto_scaling_group(
        self, context: RequestContext, request: UpdateAutoScalingGroupType, **kwargs
    ) -> None:
        """**We strongly recommend that all Auto Scaling groups use launch
        templates to ensure full functionality for Amazon EC2 Auto Scaling and
        Amazon EC2.**

        Updates the configuration for the specified Auto Scaling group.

        To update an Auto Scaling group, specify the name of the group and the
        property that you want to change. Any properties that you don't specify
        are not changed by this update request. The new settings take effect on
        any scaling activities after this call returns.

        If you associate a new launch configuration or template with an Auto
        Scaling group, all new instances will get the updated configuration.
        Existing instances continue to run with the configuration that they were
        originally launched with. When you update a group to specify a mixed
        instances policy instead of a launch configuration or template, existing
        instances may be replaced to match the new purchasing options that you
        specified in the policy. For example, if the group currently has 100%
        On-Demand capacity and the policy specifies 50% Spot capacity, this
        means that half of your instances will be gradually terminated and
        relaunched as Spot Instances. When replacing instances, Amazon EC2 Auto
        Scaling launches new instances before terminating the old ones, so that
        updating your group does not compromise the performance or availability
        of your application.

        Note the following about changing ``DesiredCapacity``, ``MaxSize``, or
        ``MinSize``:

        -  If a scale-in activity occurs as a result of a new
           ``DesiredCapacity`` value that is lower than the current size of the
           group, the Auto Scaling group uses its termination policy to
           determine which instances to terminate.

        -  If you specify a new value for ``MinSize`` without specifying a value
           for ``DesiredCapacity``, and the new ``MinSize`` is larger than the
           current size of the group, this sets the group's ``DesiredCapacity``
           to the new ``MinSize`` value.

        -  If you specify a new value for ``MaxSize`` without specifying a value
           for ``DesiredCapacity``, and the new ``MaxSize`` is smaller than the
           current size of the group, this sets the group's ``DesiredCapacity``
           to the new ``MaxSize`` value.

        To see which properties have been set, call the
        `DescribeAutoScalingGroups <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAutoScalingGroups.html>`__
        API. To view the scaling policies for an Auto Scaling group, call the
        `DescribePolicies <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribePolicies.html>`__
        API. If the group has scaling policies, you can update them by calling
        the
        `PutScalingPolicy <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PutScalingPolicy.html>`__
        API.

        :param auto_scaling_group_name: The name of the Auto Scaling group.
        :param launch_configuration_name: The name of the launch configuration.
        :param launch_template: The launch template and version to use to specify the updates.
        :param mixed_instances_policy: The mixed instances policy.
        :param min_size: The minimum size of the Auto Scaling group.
        :param max_size: The maximum size of the Auto Scaling group.
        :param desired_capacity: The desired capacity is the initial capacity of the Auto Scaling group
        after this operation completes and the capacity it attempts to maintain.
        :param default_cooldown: *Only needed if you use simple scaling policies.
        :param availability_zones: One or more Availability Zones for the group.
        :param health_check_type: A comma-separated value string of one or more health check types.
        :param health_check_grace_period: The amount of time, in seconds, that Amazon EC2 Auto Scaling waits
        before checking the health status of an EC2 instance that has come into
        service and marking it unhealthy due to a failed health check.
        :param placement_group: The name of an existing placement group into which to launch your
        instances.
        :param vpc_zone_identifier: A comma-separated list of subnet IDs for a virtual private cloud (VPC).
        :param termination_policies: A policy or a list of policies that are used to select the instances to
        terminate.
        :param new_instances_protected_from_scale_in: Indicates whether newly launched instances are protected from
        termination by Amazon EC2 Auto Scaling when scaling in.
        :param service_linked_role_arn: The Amazon Resource Name (ARN) of the service-linked role that the Auto
        Scaling group uses to call other Amazon Web Services on your behalf.
        :param max_instance_lifetime: The maximum amount of time, in seconds, that an instance can be in
        service.
        :param capacity_rebalance: Enables or disables Capacity Rebalancing.
        :param context: Reserved.
        :param desired_capacity_type: The unit of measurement for the value specified for desired capacity.
        :param default_instance_warmup: The amount of time, in seconds, until a new instance is considered to
        have finished initializing and resource consumption to become stable
        after it enters the ``InService`` state.
        :param instance_maintenance_policy: An instance maintenance policy.
        :param availability_zone_distribution: The instance capacity distribution across Availability Zones.
        :param availability_zone_impairment_policy: The policy for Availability Zone impairment.
        :param skip_zonal_shift_validation: If you enable zonal shift with cross-zone disabled load balancers,
        capacity could become imbalanced across Availability Zones.
        :param capacity_reservation_specification: The capacity reservation specification for the Auto Scaling group.
        :raises ScalingActivityInProgressFault:
        :raises ResourceContentionFault:
        :raises ServiceLinkedRoleFailure:
        """
        raise NotImplementedError
