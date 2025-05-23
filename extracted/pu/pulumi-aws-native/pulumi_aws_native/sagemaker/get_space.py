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
from .. import outputs as _root_outputs

__all__ = [
    'GetSpaceResult',
    'AwaitableGetSpaceResult',
    'get_space',
    'get_space_output',
]

@pulumi.output_type
class GetSpaceResult:
    def __init__(__self__, space_arn=None, space_display_name=None, tags=None, url=None):
        if space_arn and not isinstance(space_arn, str):
            raise TypeError("Expected argument 'space_arn' to be a str")
        pulumi.set(__self__, "space_arn", space_arn)
        if space_display_name and not isinstance(space_display_name, str):
            raise TypeError("Expected argument 'space_display_name' to be a str")
        pulumi.set(__self__, "space_display_name", space_display_name)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if url and not isinstance(url, str):
            raise TypeError("Expected argument 'url' to be a str")
        pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter(name="spaceArn")
    def space_arn(self) -> Optional[builtins.str]:
        """
        The space Amazon Resource Name (ARN).
        """
        return pulumi.get(self, "space_arn")

    @property
    @pulumi.getter(name="spaceDisplayName")
    def space_display_name(self) -> Optional[builtins.str]:
        """
        The name of the space that appears in the Studio UI.
        """
        return pulumi.get(self, "space_display_name")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        A list of tags to apply to the space.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def url(self) -> Optional[builtins.str]:
        """
        Returns the URL of the space. If the space is created with AWS IAM Identity Center (Successor to AWS Single Sign-On) authentication, users can navigate to the URL after appending the respective redirect parameter for the application type to be federated through AWS IAM Identity Center.

        The following application types are supported:

        - Studio Classic: `&redirect=JupyterServer`
        - JupyterLab: `&redirect=JupyterLab`
        - Code Editor, based on Code-OSS, Visual Studio Code - Open Source: `&redirect=CodeEditor`
        """
        return pulumi.get(self, "url")


class AwaitableGetSpaceResult(GetSpaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSpaceResult(
            space_arn=self.space_arn,
            space_display_name=self.space_display_name,
            tags=self.tags,
            url=self.url)


def get_space(domain_id: Optional[builtins.str] = None,
              space_name: Optional[builtins.str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSpaceResult:
    """
    Resource Type definition for AWS::SageMaker::Space


    :param builtins.str domain_id: The ID of the associated Domain.
    :param builtins.str space_name: A name for the Space.
    """
    __args__ = dict()
    __args__['domainId'] = domain_id
    __args__['spaceName'] = space_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:sagemaker:getSpace', __args__, opts=opts, typ=GetSpaceResult).value

    return AwaitableGetSpaceResult(
        space_arn=pulumi.get(__ret__, 'space_arn'),
        space_display_name=pulumi.get(__ret__, 'space_display_name'),
        tags=pulumi.get(__ret__, 'tags'),
        url=pulumi.get(__ret__, 'url'))
def get_space_output(domain_id: Optional[pulumi.Input[builtins.str]] = None,
                     space_name: Optional[pulumi.Input[builtins.str]] = None,
                     opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetSpaceResult]:
    """
    Resource Type definition for AWS::SageMaker::Space


    :param builtins.str domain_id: The ID of the associated Domain.
    :param builtins.str space_name: A name for the Space.
    """
    __args__ = dict()
    __args__['domainId'] = domain_id
    __args__['spaceName'] = space_name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:sagemaker:getSpace', __args__, opts=opts, typ=GetSpaceResult)
    return __ret__.apply(lambda __response__: GetSpaceResult(
        space_arn=pulumi.get(__response__, 'space_arn'),
        space_display_name=pulumi.get(__response__, 'space_display_name'),
        tags=pulumi.get(__response__, 'tags'),
        url=pulumi.get(__response__, 'url')))
