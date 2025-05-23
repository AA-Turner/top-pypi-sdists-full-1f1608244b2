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
from ._enums import *

__all__ = [
    'GetEnvironmentResult',
    'AwaitableGetEnvironmentResult',
    'get_environment',
    'get_environment_output',
]

@pulumi.output_type
class GetEnvironmentResult:
    def __init__(__self__, aws_account_id=None, dedicated_service_account_id=None, description=None, environment_arn=None, environment_id=None, environment_url=None, federation_mode=None, name=None, sage_maker_studio_domain_url=None, status=None):
        if aws_account_id and not isinstance(aws_account_id, str):
            raise TypeError("Expected argument 'aws_account_id' to be a str")
        pulumi.set(__self__, "aws_account_id", aws_account_id)
        if dedicated_service_account_id and not isinstance(dedicated_service_account_id, str):
            raise TypeError("Expected argument 'dedicated_service_account_id' to be a str")
        pulumi.set(__self__, "dedicated_service_account_id", dedicated_service_account_id)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if environment_arn and not isinstance(environment_arn, str):
            raise TypeError("Expected argument 'environment_arn' to be a str")
        pulumi.set(__self__, "environment_arn", environment_arn)
        if environment_id and not isinstance(environment_id, str):
            raise TypeError("Expected argument 'environment_id' to be a str")
        pulumi.set(__self__, "environment_id", environment_id)
        if environment_url and not isinstance(environment_url, str):
            raise TypeError("Expected argument 'environment_url' to be a str")
        pulumi.set(__self__, "environment_url", environment_url)
        if federation_mode and not isinstance(federation_mode, str):
            raise TypeError("Expected argument 'federation_mode' to be a str")
        pulumi.set(__self__, "federation_mode", federation_mode)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if sage_maker_studio_domain_url and not isinstance(sage_maker_studio_domain_url, str):
            raise TypeError("Expected argument 'sage_maker_studio_domain_url' to be a str")
        pulumi.set(__self__, "sage_maker_studio_domain_url", sage_maker_studio_domain_url)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[builtins.str]:
        """
        AWS account ID associated with the Environment
        """
        return pulumi.get(self, "aws_account_id")

    @property
    @pulumi.getter(name="dedicatedServiceAccountId")
    def dedicated_service_account_id(self) -> Optional[builtins.str]:
        """
        ID for FinSpace created account used to store Environment artifacts
        """
        return pulumi.get(self, "dedicated_service_account_id")

    @property
    @pulumi.getter
    def description(self) -> Optional[builtins.str]:
        """
        Description of the Environment
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="environmentArn")
    def environment_arn(self) -> Optional[builtins.str]:
        """
        ARN of the Environment
        """
        return pulumi.get(self, "environment_arn")

    @property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[builtins.str]:
        """
        Unique identifier for representing FinSpace Environment
        """
        return pulumi.get(self, "environment_id")

    @property
    @pulumi.getter(name="environmentUrl")
    def environment_url(self) -> Optional[builtins.str]:
        """
        URL used to login to the Environment
        """
        return pulumi.get(self, "environment_url")

    @property
    @pulumi.getter(name="federationMode")
    def federation_mode(self) -> Optional['EnvironmentFederationMode']:
        """
        Federation mode used with the Environment
        """
        return pulumi.get(self, "federation_mode")

    @property
    @pulumi.getter
    def name(self) -> Optional[builtins.str]:
        """
        Name of the Environment
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sageMakerStudioDomainUrl")
    def sage_maker_studio_domain_url(self) -> Optional[builtins.str]:
        """
        SageMaker Studio Domain URL associated with the Environment
        """
        return pulumi.get(self, "sage_maker_studio_domain_url")

    @property
    @pulumi.getter
    def status(self) -> Optional['EnvironmentStatus']:
        """
        State of the Environment
        """
        return pulumi.get(self, "status")


class AwaitableGetEnvironmentResult(GetEnvironmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEnvironmentResult(
            aws_account_id=self.aws_account_id,
            dedicated_service_account_id=self.dedicated_service_account_id,
            description=self.description,
            environment_arn=self.environment_arn,
            environment_id=self.environment_id,
            environment_url=self.environment_url,
            federation_mode=self.federation_mode,
            name=self.name,
            sage_maker_studio_domain_url=self.sage_maker_studio_domain_url,
            status=self.status)


def get_environment(environment_id: Optional[builtins.str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEnvironmentResult:
    """
    An example resource schema demonstrating some basic constructs and validation rules.


    :param builtins.str environment_id: Unique identifier for representing FinSpace Environment
    """
    __args__ = dict()
    __args__['environmentId'] = environment_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:finspace:getEnvironment', __args__, opts=opts, typ=GetEnvironmentResult).value

    return AwaitableGetEnvironmentResult(
        aws_account_id=pulumi.get(__ret__, 'aws_account_id'),
        dedicated_service_account_id=pulumi.get(__ret__, 'dedicated_service_account_id'),
        description=pulumi.get(__ret__, 'description'),
        environment_arn=pulumi.get(__ret__, 'environment_arn'),
        environment_id=pulumi.get(__ret__, 'environment_id'),
        environment_url=pulumi.get(__ret__, 'environment_url'),
        federation_mode=pulumi.get(__ret__, 'federation_mode'),
        name=pulumi.get(__ret__, 'name'),
        sage_maker_studio_domain_url=pulumi.get(__ret__, 'sage_maker_studio_domain_url'),
        status=pulumi.get(__ret__, 'status'))
def get_environment_output(environment_id: Optional[pulumi.Input[builtins.str]] = None,
                           opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetEnvironmentResult]:
    """
    An example resource schema demonstrating some basic constructs and validation rules.


    :param builtins.str environment_id: Unique identifier for representing FinSpace Environment
    """
    __args__ = dict()
    __args__['environmentId'] = environment_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:finspace:getEnvironment', __args__, opts=opts, typ=GetEnvironmentResult)
    return __ret__.apply(lambda __response__: GetEnvironmentResult(
        aws_account_id=pulumi.get(__response__, 'aws_account_id'),
        dedicated_service_account_id=pulumi.get(__response__, 'dedicated_service_account_id'),
        description=pulumi.get(__response__, 'description'),
        environment_arn=pulumi.get(__response__, 'environment_arn'),
        environment_id=pulumi.get(__response__, 'environment_id'),
        environment_url=pulumi.get(__response__, 'environment_url'),
        federation_mode=pulumi.get(__response__, 'federation_mode'),
        name=pulumi.get(__response__, 'name'),
        sage_maker_studio_domain_url=pulumi.get(__response__, 'sage_maker_studio_domain_url'),
        status=pulumi.get(__response__, 'status')))
