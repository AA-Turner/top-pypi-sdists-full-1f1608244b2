# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
import pulumi
from enum import Enum

__all__ = [
    'AccessLogSubscriptionServiceNetworkLogType',
    'AuthPolicyState',
    'ListenerProtocol',
    'ResourceConfigurationAuthType',
    'ResourceConfigurationDnsResourceIpAddressType',
    'ResourceConfigurationProtocolType',
    'ResourceConfigurationType',
    'ResourceGatewayIpAddressType',
    'RuleHttpMatchMethod',
    'ServiceAuthType',
    'ServiceNetworkAuthType',
    'ServiceNetworkServiceAssociationStatus',
    'ServiceNetworkVpcAssociationStatus',
    'ServiceStatus',
    'TargetGroupConfigIpAddressType',
    'TargetGroupConfigLambdaEventStructureVersion',
    'TargetGroupConfigProtocol',
    'TargetGroupConfigProtocolVersion',
    'TargetGroupHealthCheckConfigProtocol',
    'TargetGroupHealthCheckConfigProtocolVersion',
    'TargetGroupStatus',
    'TargetGroupType',
]


@pulumi.type_token("aws-native:vpclattice:AccessLogSubscriptionServiceNetworkLogType")
class AccessLogSubscriptionServiceNetworkLogType(builtins.str, Enum):
    """
    Log type of the service network.
    """
    SERVICE = "SERVICE"
    RESOURCE = "RESOURCE"


@pulumi.type_token("aws-native:vpclattice:AuthPolicyState")
class AuthPolicyState(builtins.str, Enum):
    """
    The state of the auth policy. The auth policy is only active when the auth type is set to `AWS _IAM` . If you provide a policy, then authentication and authorization decisions are made based on this policy and the client's IAM policy. If the auth type is `NONE` , then any auth policy you provide will remain inactive.
    """
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


@pulumi.type_token("aws-native:vpclattice:ListenerProtocol")
class ListenerProtocol(builtins.str, Enum):
    """
    The listener protocol.
    """
    HTTP = "HTTP"
    HTTPS = "HTTPS"
    TLS_PASSTHROUGH = "TLS_PASSTHROUGH"


@pulumi.type_token("aws-native:vpclattice:ResourceConfigurationAuthType")
class ResourceConfigurationAuthType(builtins.str, Enum):
    """
    The auth type for the resource configuration.
    """
    NONE = "NONE"
    AWS_IAM = "AWS_IAM"


@pulumi.type_token("aws-native:vpclattice:ResourceConfigurationDnsResourceIpAddressType")
class ResourceConfigurationDnsResourceIpAddressType(builtins.str, Enum):
    IPV4 = "IPV4"
    IPV6 = "IPV6"
    DUALSTACK = "DUALSTACK"


@pulumi.type_token("aws-native:vpclattice:ResourceConfigurationProtocolType")
class ResourceConfigurationProtocolType(builtins.str, Enum):
    """
    (SINGLE, GROUP) The protocol accepted by the resource configuration.
    """
    TCP = "TCP"


@pulumi.type_token("aws-native:vpclattice:ResourceConfigurationType")
class ResourceConfigurationType(builtins.str, Enum):
    """
    The type of resource configuration. A resource configuration can be one of the following types:

    - *SINGLE* - A single resource.
    - *GROUP* - A group of resources. You must create a group resource configuration before you create a child resource configuration.
    - *CHILD* - A single resource that is part of a group resource configuration.
    - *ARN* - An AWS resource.
    """
    GROUP = "GROUP"
    CHILD = "CHILD"
    SINGLE = "SINGLE"
    ARN = "ARN"


@pulumi.type_token("aws-native:vpclattice:ResourceGatewayIpAddressType")
class ResourceGatewayIpAddressType(builtins.str, Enum):
    """
    The type of IP address used by the resource gateway.
    """
    IPV4 = "IPV4"
    IPV6 = "IPV6"
    DUALSTACK = "DUALSTACK"


@pulumi.type_token("aws-native:vpclattice:RuleHttpMatchMethod")
class RuleHttpMatchMethod(builtins.str, Enum):
    """
    The HTTP method type.
    """
    CONNECT = "CONNECT"
    DELETE = "DELETE"
    GET = "GET"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"
    POST = "POST"
    PUT = "PUT"
    TRACE = "TRACE"


@pulumi.type_token("aws-native:vpclattice:ServiceAuthType")
class ServiceAuthType(builtins.str, Enum):
    """
    The type of IAM policy.

    - `NONE` : The resource does not use an IAM policy. This is the default.
    - `AWS_IAM` : The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.
    """
    NONE = "NONE"
    AWS_IAM = "AWS_IAM"


@pulumi.type_token("aws-native:vpclattice:ServiceNetworkAuthType")
class ServiceNetworkAuthType(builtins.str, Enum):
    """
    The type of IAM policy.

    - `NONE` : The resource does not use an IAM policy. This is the default.
    - `AWS_IAM` : The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.
    """
    NONE = "NONE"
    AWS_IAM = "AWS_IAM"


@pulumi.type_token("aws-native:vpclattice:ServiceNetworkServiceAssociationStatus")
class ServiceNetworkServiceAssociationStatus(builtins.str, Enum):
    """
    The status of the association between the service network and the service.
    """
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    ACTIVE = "ACTIVE"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_FAILED = "DELETE_FAILED"


@pulumi.type_token("aws-native:vpclattice:ServiceNetworkVpcAssociationStatus")
class ServiceNetworkVpcAssociationStatus(builtins.str, Enum):
    """
    The status of the association.
    """
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    ACTIVE = "ACTIVE"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_FAILED = "DELETE_FAILED"


@pulumi.type_token("aws-native:vpclattice:ServiceStatus")
class ServiceStatus(builtins.str, Enum):
    """
    The status of the service.
    """
    ACTIVE = "ACTIVE"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_FAILED = "DELETE_FAILED"


@pulumi.type_token("aws-native:vpclattice:TargetGroupConfigIpAddressType")
class TargetGroupConfigIpAddressType(builtins.str, Enum):
    """
    The type of IP address used for the target group. Supported only if the target group type is `IP` . The default is `IPV4` .
    """
    IPV4 = "IPV4"
    IPV6 = "IPV6"


@pulumi.type_token("aws-native:vpclattice:TargetGroupConfigLambdaEventStructureVersion")
class TargetGroupConfigLambdaEventStructureVersion(builtins.str, Enum):
    """
    The version of the event structure that your Lambda function receives. Supported only if the target group type is `LAMBDA` . The default is `V1` .
    """
    V1 = "V1"
    V2 = "V2"


@pulumi.type_token("aws-native:vpclattice:TargetGroupConfigProtocol")
class TargetGroupConfigProtocol(builtins.str, Enum):
    """
    The protocol to use for routing traffic to the targets. The default is the protocol of the target group. Not supported if the target group type is `LAMBDA` .
    """
    HTTP = "HTTP"
    HTTPS = "HTTPS"
    TCP = "TCP"


@pulumi.type_token("aws-native:vpclattice:TargetGroupConfigProtocolVersion")
class TargetGroupConfigProtocolVersion(builtins.str, Enum):
    """
    The protocol version. The default is `HTTP1` . Not supported if the target group type is `LAMBDA` .
    """
    HTTP1 = "HTTP1"
    HTTP2 = "HTTP2"
    GRPC = "GRPC"


@pulumi.type_token("aws-native:vpclattice:TargetGroupHealthCheckConfigProtocol")
class TargetGroupHealthCheckConfigProtocol(builtins.str, Enum):
    """
    The protocol used when performing health checks on targets. The possible protocols are `HTTP` and `HTTPS` . The default is `HTTP` .
    """
    HTTP = "HTTP"
    HTTPS = "HTTPS"


@pulumi.type_token("aws-native:vpclattice:TargetGroupHealthCheckConfigProtocolVersion")
class TargetGroupHealthCheckConfigProtocolVersion(builtins.str, Enum):
    """
    The protocol version used when performing health checks on targets. The possible protocol versions are `HTTP1` and `HTTP2` .
    """
    HTTP1 = "HTTP1"
    HTTP2 = "HTTP2"


@pulumi.type_token("aws-native:vpclattice:TargetGroupStatus")
class TargetGroupStatus(builtins.str, Enum):
    """
    The operation's status. You can retry the operation if the status is `CREATE_FAILED` . However, if you retry it while the status is `CREATE_IN_PROGRESS` , there is no change in the status.
    """
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    ACTIVE = "ACTIVE"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_FAILED = "DELETE_FAILED"


@pulumi.type_token("aws-native:vpclattice:TargetGroupType")
class TargetGroupType(builtins.str, Enum):
    """
    The type of target group.
    """
    IP = "IP"
    LAMBDA_ = "LAMBDA"
    INSTANCE = "INSTANCE"
    ALB = "ALB"
