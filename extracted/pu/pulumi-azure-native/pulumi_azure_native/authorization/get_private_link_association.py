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
    'GetPrivateLinkAssociationResult',
    'AwaitableGetPrivateLinkAssociationResult',
    'get_private_link_association',
    'get_private_link_association_output',
]

@pulumi.output_type
class GetPrivateLinkAssociationResult:
    def __init__(__self__, azure_api_version=None, id=None, name=None, properties=None, type=None):
        if azure_api_version and not isinstance(azure_api_version, str):
            raise TypeError("Expected argument 'azure_api_version' to be a str")
        pulumi.set(__self__, "azure_api_version", azure_api_version)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> builtins.str:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        """
        The plaResourceID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> builtins.str:
        """
        The pla name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.PrivateLinkAssociationPropertiesExpandedResponse':
        """
        The private link association properties.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> builtins.str:
        """
        The operation type.
        """
        return pulumi.get(self, "type")


class AwaitableGetPrivateLinkAssociationResult(GetPrivateLinkAssociationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrivateLinkAssociationResult(
            azure_api_version=self.azure_api_version,
            id=self.id,
            name=self.name,
            properties=self.properties,
            type=self.type)


def get_private_link_association(group_id: Optional[builtins.str] = None,
                                 pla_id: Optional[builtins.str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPrivateLinkAssociationResult:
    """
    Get a single private link association

    Uses Azure REST API version 2020-05-01.


    :param builtins.str group_id: The management group ID.
    :param builtins.str pla_id: The ID of the PLA
    """
    __args__ = dict()
    __args__['groupId'] = group_id
    __args__['plaId'] = pla_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:authorization:getPrivateLinkAssociation', __args__, opts=opts, typ=GetPrivateLinkAssociationResult).value

    return AwaitableGetPrivateLinkAssociationResult(
        azure_api_version=pulumi.get(__ret__, 'azure_api_version'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        type=pulumi.get(__ret__, 'type'))
def get_private_link_association_output(group_id: Optional[pulumi.Input[builtins.str]] = None,
                                        pla_id: Optional[pulumi.Input[builtins.str]] = None,
                                        opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetPrivateLinkAssociationResult]:
    """
    Get a single private link association

    Uses Azure REST API version 2020-05-01.


    :param builtins.str group_id: The management group ID.
    :param builtins.str pla_id: The ID of the PLA
    """
    __args__ = dict()
    __args__['groupId'] = group_id
    __args__['plaId'] = pla_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('azure-native:authorization:getPrivateLinkAssociation', __args__, opts=opts, typ=GetPrivateLinkAssociationResult)
    return __ret__.apply(lambda __response__: GetPrivateLinkAssociationResult(
        azure_api_version=pulumi.get(__response__, 'azure_api_version'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        properties=pulumi.get(__response__, 'properties'),
        type=pulumi.get(__response__, 'type')))
