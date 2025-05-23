# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities
from . import outputs

__all__ = [
    'GetScalableTargetResult',
    'AwaitableGetScalableTargetResult',
    'get_scalable_target',
    'get_scalable_target_output',
]

@pulumi.output_type
class GetScalableTargetResult:
    def __init__(__self__, id=None, max_capacity=None, min_capacity=None, scheduled_actions=None, suspended_state=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if max_capacity and not isinstance(max_capacity, int):
            raise TypeError("Expected argument 'max_capacity' to be a int")
        pulumi.set(__self__, "max_capacity", max_capacity)
        if min_capacity and not isinstance(min_capacity, int):
            raise TypeError("Expected argument 'min_capacity' to be a int")
        pulumi.set(__self__, "min_capacity", min_capacity)
        if scheduled_actions and not isinstance(scheduled_actions, list):
            raise TypeError("Expected argument 'scheduled_actions' to be a list")
        pulumi.set(__self__, "scheduled_actions", scheduled_actions)
        if suspended_state and not isinstance(suspended_state, dict):
            raise TypeError("Expected argument 'suspended_state' to be a dict")
        pulumi.set(__self__, "suspended_state", suspended_state)

    @property
    @pulumi.getter
    def id(self) -> Optional[builtins.str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> Optional[builtins.int]:
        """
        The maximum value that you plan to scale out to. When a scaling policy is in effect, Application Auto Scaling can scale out (expand) as needed to the maximum capacity limit in response to changing demand.
        """
        return pulumi.get(self, "max_capacity")

    @property
    @pulumi.getter(name="minCapacity")
    def min_capacity(self) -> Optional[builtins.int]:
        """
        The minimum value that you plan to scale in to. When a scaling policy is in effect, Application Auto Scaling can scale in (contract) as needed to the minimum capacity limit in response to changing demand.
        """
        return pulumi.get(self, "min_capacity")

    @property
    @pulumi.getter(name="scheduledActions")
    def scheduled_actions(self) -> Optional[Sequence['outputs.ScalableTargetScheduledAction']]:
        """
        The scheduled actions for the scalable target. Duplicates aren't allowed.
        """
        return pulumi.get(self, "scheduled_actions")

    @property
    @pulumi.getter(name="suspendedState")
    def suspended_state(self) -> Optional['outputs.ScalableTargetSuspendedState']:
        """
        An embedded object that contains attributes and attribute values that are used to suspend and resume automatic scaling. Setting the value of an attribute to ``true`` suspends the specified scaling activities. Setting it to ``false`` (default) resumes the specified scaling activities. 
          *Suspension Outcomes* 
          +  For ``DynamicScalingInSuspended``, while a suspension is in effect, all scale-in activities that are triggered by a scaling policy are suspended.
          +  For ``DynamicScalingOutSuspended``, while a suspension is in effect, all scale-out activities that are triggered by a scaling policy are suspended.
          +  For ``ScheduledScalingSuspended``, while a suspension is in effect, all scaling activities that involve scheduled actions are suspended.
        """
        return pulumi.get(self, "suspended_state")


class AwaitableGetScalableTargetResult(GetScalableTargetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetScalableTargetResult(
            id=self.id,
            max_capacity=self.max_capacity,
            min_capacity=self.min_capacity,
            scheduled_actions=self.scheduled_actions,
            suspended_state=self.suspended_state)


def get_scalable_target(resource_id: Optional[builtins.str] = None,
                        scalable_dimension: Optional[builtins.str] = None,
                        service_namespace: Optional[builtins.str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetScalableTargetResult:
    """
    The ``AWS::ApplicationAutoScaling::ScalableTarget`` resource specifies a resource that Application Auto Scaling can scale, such as an AWS::DynamoDB::Table or AWS::ECS::Service resource.
     For more information, see [Getting started](https://docs.aws.amazon.com/autoscaling/application/userguide/getting-started.html) in the *Application Auto Scaling User Guide*.
      If the resource that you want Application Auto Scaling to scale is not yet created in your account, add a dependency on the resource when registering it as a scalable target using the [DependsOn](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html) attribute.


    :param builtins.str resource_id: The identifier of the resource associated with the scalable target. This string consists of the resource type and unique identifier.
             +  ECS service - The resource type is ``service`` and the unique identifier is the cluster name and service name. Example: ``service/my-cluster/my-service``.
             +  Spot Fleet - The resource type is ``spot-fleet-request`` and the unique identifier is the Spot Fleet request ID. Example: ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE``.
             +  EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the cluster ID and instance group ID. Example: ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0``.
             +  AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the fleet name. Example: ``fleet/sample-fleet``.
             +  DynamoDB table - The resource type is ``table`` and the unique identifier is the table name. Example: ``table/my-table``.
             +  DynamoDB global secondary index - The resource type is ``index`` and the unique identifier is the index name. Example: ``table/my-table/index/my-table-index``.
             +  Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:my-db-cluster``.
             +  SageMaker endpoint variant - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering``.
             +  Custom resources are not supported with a resource type. This parameter must specify the ``OutputValue`` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our [GitHub repository](https://docs.aws.amazon.com/https://github.com/aws/aws-auto-scaling-custom-resource).
             +  Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE``.
             +  Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE``.
             +  Lambda provisioned concurrency - The resource type is ``function`` and the unique identifier is the function name with a function version or alias name suffix that is not ``$LATEST``. Example: ``function:my-function:prod`` or ``function:my-function:1``.
             +  Amazon Keyspaces table - The resource type is ``table`` and the unique identifier is the table name. Example: ``keyspace/mykeyspace/table/mytable``.
             +  Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: ``arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5``.
             +  Amazon ElastiCache replication group - The resource type is ``replication-group`` and the unique identifier is the replication group name. Example: ``replication-group/mycluster``.
             +  Neptune cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:mycluster``.
             +  SageMaker serverless endpoint - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering``.
             +  SageMaker inference component - The resource type is ``inference-component`` and the unique identifier is the resource ID. Example: ``inference-component/my-inference-component``.
    :param builtins.str scalable_dimension: The scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property.
             +   ``ecs:service:DesiredCount`` - The desired task count of an ECS service.
             +   ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance Group.
             +   ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet.
             +   ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.
             +   ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table.
             +   ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table.
             +   ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global secondary index.
             +   ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB global secondary index.
             +   ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.
             +   ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for a SageMaker model endpoint variant.
             +   ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource provided by your own application or service.
             +   ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend document classification endpoint.
             +   ``comprehend:entity-recognizer-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend entity recognizer endpoint.
             +   ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a Lambda function.
             +   ``cassandra:table:ReadCapacityUnits`` - The provisioned read capacity for an Amazon Keyspaces table.
             +   ``cassandra:table:WriteCapacityUnits`` - The provisioned write capacity for an Amazon Keyspaces table.
             +   ``kafka:broker-storage:VolumeSize`` - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster.
             +   ``elasticache:replication-group:NodeGroups`` - The number of node groups for an Amazon ElastiCache replication group.
             +   ``elasticache:replication-group:Replicas`` - The number of replicas per node group for an Amazon ElastiCache replication group.
             +   ``neptune:cluster:ReadReplicaCount`` - The count of read replicas in an Amazon Neptune DB cluster.
             +   ``sagemaker:variant:DesiredProvisionedConcurrency`` - The provisioned concurrency for a SageMaker serverless endpoint.
             +   ``sagemaker:inference-component:DesiredCopyCount`` - The number of copies across an endpoint for a SageMaker inference component.
    :param builtins.str service_namespace: The namespace of the AWS service that provides the resource, or a ``custom-resource``.
    """
    __args__ = dict()
    __args__['resourceId'] = resource_id
    __args__['scalableDimension'] = scalable_dimension
    __args__['serviceNamespace'] = service_namespace
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:applicationautoscaling:getScalableTarget', __args__, opts=opts, typ=GetScalableTargetResult).value

    return AwaitableGetScalableTargetResult(
        id=pulumi.get(__ret__, 'id'),
        max_capacity=pulumi.get(__ret__, 'max_capacity'),
        min_capacity=pulumi.get(__ret__, 'min_capacity'),
        scheduled_actions=pulumi.get(__ret__, 'scheduled_actions'),
        suspended_state=pulumi.get(__ret__, 'suspended_state'))
def get_scalable_target_output(resource_id: Optional[pulumi.Input[builtins.str]] = None,
                               scalable_dimension: Optional[pulumi.Input[builtins.str]] = None,
                               service_namespace: Optional[pulumi.Input[builtins.str]] = None,
                               opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetScalableTargetResult]:
    """
    The ``AWS::ApplicationAutoScaling::ScalableTarget`` resource specifies a resource that Application Auto Scaling can scale, such as an AWS::DynamoDB::Table or AWS::ECS::Service resource.
     For more information, see [Getting started](https://docs.aws.amazon.com/autoscaling/application/userguide/getting-started.html) in the *Application Auto Scaling User Guide*.
      If the resource that you want Application Auto Scaling to scale is not yet created in your account, add a dependency on the resource when registering it as a scalable target using the [DependsOn](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html) attribute.


    :param builtins.str resource_id: The identifier of the resource associated with the scalable target. This string consists of the resource type and unique identifier.
             +  ECS service - The resource type is ``service`` and the unique identifier is the cluster name and service name. Example: ``service/my-cluster/my-service``.
             +  Spot Fleet - The resource type is ``spot-fleet-request`` and the unique identifier is the Spot Fleet request ID. Example: ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE``.
             +  EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the cluster ID and instance group ID. Example: ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0``.
             +  AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the fleet name. Example: ``fleet/sample-fleet``.
             +  DynamoDB table - The resource type is ``table`` and the unique identifier is the table name. Example: ``table/my-table``.
             +  DynamoDB global secondary index - The resource type is ``index`` and the unique identifier is the index name. Example: ``table/my-table/index/my-table-index``.
             +  Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:my-db-cluster``.
             +  SageMaker endpoint variant - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering``.
             +  Custom resources are not supported with a resource type. This parameter must specify the ``OutputValue`` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our [GitHub repository](https://docs.aws.amazon.com/https://github.com/aws/aws-auto-scaling-custom-resource).
             +  Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE``.
             +  Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE``.
             +  Lambda provisioned concurrency - The resource type is ``function`` and the unique identifier is the function name with a function version or alias name suffix that is not ``$LATEST``. Example: ``function:my-function:prod`` or ``function:my-function:1``.
             +  Amazon Keyspaces table - The resource type is ``table`` and the unique identifier is the table name. Example: ``keyspace/mykeyspace/table/mytable``.
             +  Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: ``arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5``.
             +  Amazon ElastiCache replication group - The resource type is ``replication-group`` and the unique identifier is the replication group name. Example: ``replication-group/mycluster``.
             +  Neptune cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:mycluster``.
             +  SageMaker serverless endpoint - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering``.
             +  SageMaker inference component - The resource type is ``inference-component`` and the unique identifier is the resource ID. Example: ``inference-component/my-inference-component``.
    :param builtins.str scalable_dimension: The scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property.
             +   ``ecs:service:DesiredCount`` - The desired task count of an ECS service.
             +   ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance Group.
             +   ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet.
             +   ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.
             +   ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table.
             +   ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table.
             +   ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global secondary index.
             +   ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB global secondary index.
             +   ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.
             +   ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for a SageMaker model endpoint variant.
             +   ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource provided by your own application or service.
             +   ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend document classification endpoint.
             +   ``comprehend:entity-recognizer-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend entity recognizer endpoint.
             +   ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a Lambda function.
             +   ``cassandra:table:ReadCapacityUnits`` - The provisioned read capacity for an Amazon Keyspaces table.
             +   ``cassandra:table:WriteCapacityUnits`` - The provisioned write capacity for an Amazon Keyspaces table.
             +   ``kafka:broker-storage:VolumeSize`` - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster.
             +   ``elasticache:replication-group:NodeGroups`` - The number of node groups for an Amazon ElastiCache replication group.
             +   ``elasticache:replication-group:Replicas`` - The number of replicas per node group for an Amazon ElastiCache replication group.
             +   ``neptune:cluster:ReadReplicaCount`` - The count of read replicas in an Amazon Neptune DB cluster.
             +   ``sagemaker:variant:DesiredProvisionedConcurrency`` - The provisioned concurrency for a SageMaker serverless endpoint.
             +   ``sagemaker:inference-component:DesiredCopyCount`` - The number of copies across an endpoint for a SageMaker inference component.
    :param builtins.str service_namespace: The namespace of the AWS service that provides the resource, or a ``custom-resource``.
    """
    __args__ = dict()
    __args__['resourceId'] = resource_id
    __args__['scalableDimension'] = scalable_dimension
    __args__['serviceNamespace'] = service_namespace
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:applicationautoscaling:getScalableTarget', __args__, opts=opts, typ=GetScalableTargetResult)
    return __ret__.apply(lambda __response__: GetScalableTargetResult(
        id=pulumi.get(__response__, 'id'),
        max_capacity=pulumi.get(__response__, 'max_capacity'),
        min_capacity=pulumi.get(__response__, 'min_capacity'),
        scheduled_actions=pulumi.get(__response__, 'scheduled_actions'),
        suspended_state=pulumi.get(__response__, 'suspended_state')))
