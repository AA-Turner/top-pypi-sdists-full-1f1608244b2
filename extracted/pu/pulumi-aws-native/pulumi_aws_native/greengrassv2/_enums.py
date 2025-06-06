# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
import pulumi
from enum import Enum

__all__ = [
    'ComponentVersionComponentDependencyRequirementDependencyType',
    'ComponentVersionLambdaEventSourceType',
    'ComponentVersionLambdaExecutionParametersInputPayloadEncodingType',
    'ComponentVersionLambdaFilesystemPermission',
    'ComponentVersionLambdaLinuxProcessParamsIsolationMode',
    'DeploymentComponentUpdatePolicyAction',
    'DeploymentIoTJobAbortCriteriaAction',
    'DeploymentIoTJobAbortCriteriaFailureType',
    'DeploymentPoliciesFailureHandlingPolicy',
]


@pulumi.type_token("aws-native:greengrassv2:ComponentVersionComponentDependencyRequirementDependencyType")
class ComponentVersionComponentDependencyRequirementDependencyType(builtins.str, Enum):
    SOFT = "SOFT"
    HARD = "HARD"


@pulumi.type_token("aws-native:greengrassv2:ComponentVersionLambdaEventSourceType")
class ComponentVersionLambdaEventSourceType(builtins.str, Enum):
    """
    The type of event source. Choose from the following options:

    - `PUB_SUB` – Subscribe to local publish/subscribe messages. This event source type doesn't support MQTT wildcards ( `+` and `#` ) in the event source topic.
    - `IOT_CORE` – Subscribe to AWS IoT Core MQTT messages. This event source type supports MQTT wildcards ( `+` and `#` ) in the event source topic.
    """
    PUB_SUB = "PUB_SUB"
    IOT_CORE = "IOT_CORE"


@pulumi.type_token("aws-native:greengrassv2:ComponentVersionLambdaExecutionParametersInputPayloadEncodingType")
class ComponentVersionLambdaExecutionParametersInputPayloadEncodingType(builtins.str, Enum):
    """
    The encoding type that the Lambda function supports.

    Default: `json`
    """
    JSON = "json"
    BINARY = "binary"


@pulumi.type_token("aws-native:greengrassv2:ComponentVersionLambdaFilesystemPermission")
class ComponentVersionLambdaFilesystemPermission(builtins.str, Enum):
    RO = "ro"
    RW = "rw"


@pulumi.type_token("aws-native:greengrassv2:ComponentVersionLambdaLinuxProcessParamsIsolationMode")
class ComponentVersionLambdaLinuxProcessParamsIsolationMode(builtins.str, Enum):
    """
    The isolation mode for the process that contains the Lambda function. The process can run in an isolated runtime environment inside the AWS IoT Greengrass container, or as a regular process outside any container.

    Default: `GreengrassContainer`
    """
    GREENGRASS_CONTAINER = "GreengrassContainer"
    NO_CONTAINER = "NoContainer"


@pulumi.type_token("aws-native:greengrassv2:DeploymentComponentUpdatePolicyAction")
class DeploymentComponentUpdatePolicyAction(builtins.str, Enum):
    """
    Whether or not to notify components and wait for components to become safe to update. Choose from the following options:

    - `NOTIFY_COMPONENTS` – The deployment notifies each component before it stops and updates that component. Components can use the [SubscribeToComponentUpdates](https://docs.aws.amazon.com/greengrass/v2/developerguide/interprocess-communication.html#ipc-operation-subscribetocomponentupdates) IPC operation to receive these notifications. Then, components can respond with the [DeferComponentUpdate](https://docs.aws.amazon.com/greengrass/v2/developerguide/interprocess-communication.html#ipc-operation-defercomponentupdate) IPC operation. For more information, see the [Create deployments](https://docs.aws.amazon.com/greengrass/v2/developerguide/create-deployments.html) in the *AWS IoT Greengrass V2 Developer Guide* .
    - `SKIP_NOTIFY_COMPONENTS` – The deployment doesn't notify components or wait for them to be safe to update.

    Default: `NOTIFY_COMPONENTS`
    """
    NOTIFY_COMPONENTS = "NOTIFY_COMPONENTS"
    SKIP_NOTIFY_COMPONENTS = "SKIP_NOTIFY_COMPONENTS"


@pulumi.type_token("aws-native:greengrassv2:DeploymentIoTJobAbortCriteriaAction")
class DeploymentIoTJobAbortCriteriaAction(builtins.str, Enum):
    """
    The action to perform when the criteria are met.
    """
    CANCEL = "CANCEL"


@pulumi.type_token("aws-native:greengrassv2:DeploymentIoTJobAbortCriteriaFailureType")
class DeploymentIoTJobAbortCriteriaFailureType(builtins.str, Enum):
    """
    The type of job deployment failure that can cancel a job.
    """
    FAILED = "FAILED"
    REJECTED = "REJECTED"
    TIMED_OUT = "TIMED_OUT"
    ALL = "ALL"


@pulumi.type_token("aws-native:greengrassv2:DeploymentPoliciesFailureHandlingPolicy")
class DeploymentPoliciesFailureHandlingPolicy(builtins.str, Enum):
    """
    The failure handling policy for the configuration deployment. This policy defines what to do if the deployment fails.

    Default: `ROLLBACK`
    """
    ROLLBACK = "ROLLBACK"
    DO_NOTHING = "DO_NOTHING"
