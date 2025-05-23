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
    'ListEdgeSiteL2ConnectionsResult',
    'AwaitableListEdgeSiteL2ConnectionsResult',
    'list_edge_site_l2_connections',
    'list_edge_site_l2_connections_output',
]

@pulumi.output_type
class ListEdgeSiteL2ConnectionsResult:
    """
    Response for an API service call that lists the resource IDs of resources associated with another resource.
    """
    def __init__(__self__, next_link=None, value=None):
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> builtins.str:
        """
        The URL to get the next set of results.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.ResourceIdListResultResponseValue']]:
        """
        A list of Azure Resource IDs.
        """
        return pulumi.get(self, "value")


class AwaitableListEdgeSiteL2ConnectionsResult(ListEdgeSiteL2ConnectionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListEdgeSiteL2ConnectionsResult(
            next_link=self.next_link,
            value=self.value)


def list_edge_site_l2_connections(edge_site_name: Optional[builtins.str] = None,
                                  resource_group_name: Optional[builtins.str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListEdgeSiteL2ConnectionsResult:
    """
    Returns a list of L2 Connections attached to an edge site.

    Uses Azure REST API version 2024-03-01-preview.

    Other available API versions: 2024-03-01. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native orbital [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param builtins.str edge_site_name: Edge site name.
    :param builtins.str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['edgeSiteName'] = edge_site_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:orbital:listEdgeSiteL2Connections', __args__, opts=opts, typ=ListEdgeSiteL2ConnectionsResult).value

    return AwaitableListEdgeSiteL2ConnectionsResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))
def list_edge_site_l2_connections_output(edge_site_name: Optional[pulumi.Input[builtins.str]] = None,
                                         resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                                         opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[ListEdgeSiteL2ConnectionsResult]:
    """
    Returns a list of L2 Connections attached to an edge site.

    Uses Azure REST API version 2024-03-01-preview.

    Other available API versions: 2024-03-01. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native orbital [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param builtins.str edge_site_name: Edge site name.
    :param builtins.str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['edgeSiteName'] = edge_site_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('azure-native:orbital:listEdgeSiteL2Connections', __args__, opts=opts, typ=ListEdgeSiteL2ConnectionsResult)
    return __ret__.apply(lambda __response__: ListEdgeSiteL2ConnectionsResult(
        next_link=pulumi.get(__response__, 'next_link'),
        value=pulumi.get(__response__, 'value')))
