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

__all__ = [
    'GetBasePathMappingV2Result',
    'AwaitableGetBasePathMappingV2Result',
    'get_base_path_mapping_v2',
    'get_base_path_mapping_v2_output',
]

@pulumi.output_type
class GetBasePathMappingV2Result:
    def __init__(__self__, base_path_mapping_arn=None, rest_api_id=None, stage=None):
        if base_path_mapping_arn and not isinstance(base_path_mapping_arn, str):
            raise TypeError("Expected argument 'base_path_mapping_arn' to be a str")
        pulumi.set(__self__, "base_path_mapping_arn", base_path_mapping_arn)
        if rest_api_id and not isinstance(rest_api_id, str):
            raise TypeError("Expected argument 'rest_api_id' to be a str")
        pulumi.set(__self__, "rest_api_id", rest_api_id)
        if stage and not isinstance(stage, str):
            raise TypeError("Expected argument 'stage' to be a str")
        pulumi.set(__self__, "stage", stage)

    @property
    @pulumi.getter(name="basePathMappingArn")
    def base_path_mapping_arn(self) -> Optional[builtins.str]:
        """
        Amazon Resource Name (ARN) of the resource.
        """
        return pulumi.get(self, "base_path_mapping_arn")

    @property
    @pulumi.getter(name="restApiId")
    def rest_api_id(self) -> Optional[builtins.str]:
        """
        The ID of the API.
        """
        return pulumi.get(self, "rest_api_id")

    @property
    @pulumi.getter
    def stage(self) -> Optional[builtins.str]:
        """
        The name of the API's stage.
        """
        return pulumi.get(self, "stage")


class AwaitableGetBasePathMappingV2Result(GetBasePathMappingV2Result):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBasePathMappingV2Result(
            base_path_mapping_arn=self.base_path_mapping_arn,
            rest_api_id=self.rest_api_id,
            stage=self.stage)


def get_base_path_mapping_v2(base_path_mapping_arn: Optional[builtins.str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBasePathMappingV2Result:
    """
    Resource Type definition for AWS::ApiGateway::BasePathMappingV2


    :param builtins.str base_path_mapping_arn: Amazon Resource Name (ARN) of the resource.
    """
    __args__ = dict()
    __args__['basePathMappingArn'] = base_path_mapping_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:apigateway:getBasePathMappingV2', __args__, opts=opts, typ=GetBasePathMappingV2Result).value

    return AwaitableGetBasePathMappingV2Result(
        base_path_mapping_arn=pulumi.get(__ret__, 'base_path_mapping_arn'),
        rest_api_id=pulumi.get(__ret__, 'rest_api_id'),
        stage=pulumi.get(__ret__, 'stage'))
def get_base_path_mapping_v2_output(base_path_mapping_arn: Optional[pulumi.Input[builtins.str]] = None,
                                    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetBasePathMappingV2Result]:
    """
    Resource Type definition for AWS::ApiGateway::BasePathMappingV2


    :param builtins.str base_path_mapping_arn: Amazon Resource Name (ARN) of the resource.
    """
    __args__ = dict()
    __args__['basePathMappingArn'] = base_path_mapping_arn
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:apigateway:getBasePathMappingV2', __args__, opts=opts, typ=GetBasePathMappingV2Result)
    return __ret__.apply(lambda __response__: GetBasePathMappingV2Result(
        base_path_mapping_arn=pulumi.get(__response__, 'base_path_mapping_arn'),
        rest_api_id=pulumi.get(__response__, 'rest_api_id'),
        stage=pulumi.get(__response__, 'stage')))
