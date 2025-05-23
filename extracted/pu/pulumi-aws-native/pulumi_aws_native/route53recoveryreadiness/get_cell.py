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
    'GetCellResult',
    'AwaitableGetCellResult',
    'get_cell',
    'get_cell_output',
]

@pulumi.output_type
class GetCellResult:
    def __init__(__self__, cell_arn=None, cells=None, parent_readiness_scopes=None, tags=None):
        if cell_arn and not isinstance(cell_arn, str):
            raise TypeError("Expected argument 'cell_arn' to be a str")
        pulumi.set(__self__, "cell_arn", cell_arn)
        if cells and not isinstance(cells, list):
            raise TypeError("Expected argument 'cells' to be a list")
        pulumi.set(__self__, "cells", cells)
        if parent_readiness_scopes and not isinstance(parent_readiness_scopes, list):
            raise TypeError("Expected argument 'parent_readiness_scopes' to be a list")
        pulumi.set(__self__, "parent_readiness_scopes", parent_readiness_scopes)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="cellArn")
    def cell_arn(self) -> Optional[builtins.str]:
        """
        The Amazon Resource Name (ARN) of the cell.
        """
        return pulumi.get(self, "cell_arn")

    @property
    @pulumi.getter
    def cells(self) -> Optional[Sequence[builtins.str]]:
        """
        A list of cell Amazon Resource Names (ARNs) contained within this cell, for use in nested cells. For example, Availability Zones within specific Regions.
        """
        return pulumi.get(self, "cells")

    @property
    @pulumi.getter(name="parentReadinessScopes")
    def parent_readiness_scopes(self) -> Optional[Sequence[builtins.str]]:
        """
        The readiness scope for the cell, which can be a cell Amazon Resource Name (ARN) or a recovery group ARN. This is a list but currently can have only one element.
        """
        return pulumi.get(self, "parent_readiness_scopes")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        A collection of tags associated with a resource
        """
        return pulumi.get(self, "tags")


class AwaitableGetCellResult(GetCellResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCellResult(
            cell_arn=self.cell_arn,
            cells=self.cells,
            parent_readiness_scopes=self.parent_readiness_scopes,
            tags=self.tags)


def get_cell(cell_name: Optional[builtins.str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCellResult:
    """
    The API Schema for AWS Route53 Recovery Readiness Cells.


    :param builtins.str cell_name: The name of the cell to create.
    """
    __args__ = dict()
    __args__['cellName'] = cell_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:route53recoveryreadiness:getCell', __args__, opts=opts, typ=GetCellResult).value

    return AwaitableGetCellResult(
        cell_arn=pulumi.get(__ret__, 'cell_arn'),
        cells=pulumi.get(__ret__, 'cells'),
        parent_readiness_scopes=pulumi.get(__ret__, 'parent_readiness_scopes'),
        tags=pulumi.get(__ret__, 'tags'))
def get_cell_output(cell_name: Optional[pulumi.Input[builtins.str]] = None,
                    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetCellResult]:
    """
    The API Schema for AWS Route53 Recovery Readiness Cells.


    :param builtins.str cell_name: The name of the cell to create.
    """
    __args__ = dict()
    __args__['cellName'] = cell_name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:route53recoveryreadiness:getCell', __args__, opts=opts, typ=GetCellResult)
    return __ret__.apply(lambda __response__: GetCellResult(
        cell_arn=pulumi.get(__response__, 'cell_arn'),
        cells=pulumi.get(__response__, 'cells'),
        parent_readiness_scopes=pulumi.get(__response__, 'parent_readiness_scopes'),
        tags=pulumi.get(__response__, 'tags')))
