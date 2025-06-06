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
from ._inputs import *

__all__ = [
    'GetVlansResult',
    'AwaitableGetVlansResult',
    'get_vlans',
    'get_vlans_output',
]

@pulumi.output_type
class GetVlansResult:
    """
    A collection of values returned by getVlans.
    """
    def __init__(__self__, compartment_id=None, display_name=None, filters=None, id=None, state=None, vcn_id=None, vlans=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if vcn_id and not isinstance(vcn_id, str):
            raise TypeError("Expected argument 'vcn_id' to be a str")
        pulumi.set(__self__, "vcn_id", vcn_id)
        if vlans and not isinstance(vlans, list):
            raise TypeError("Expected argument 'vlans' to be a list")
        pulumi.set(__self__, "vlans", vlans)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> builtins.str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the VLAN.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[builtins.str]:
        """
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetVlansFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def state(self) -> Optional[builtins.str]:
        """
        The VLAN's current state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="vcnId")
    def vcn_id(self) -> Optional[builtins.str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN the VLAN is in.
        """
        return pulumi.get(self, "vcn_id")

    @property
    @pulumi.getter
    def vlans(self) -> Sequence['outputs.GetVlansVlanResult']:
        """
        The list of vlans.
        """
        return pulumi.get(self, "vlans")


class AwaitableGetVlansResult(GetVlansResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVlansResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            state=self.state,
            vcn_id=self.vcn_id,
            vlans=self.vlans)


def get_vlans(compartment_id: Optional[builtins.str] = None,
              display_name: Optional[builtins.str] = None,
              filters: Optional[Sequence[Union['GetVlansFilterArgs', 'GetVlansFilterArgsDict']]] = None,
              state: Optional[builtins.str] = None,
              vcn_id: Optional[builtins.str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVlansResult:
    """
    This data source provides the list of Vlans in Oracle Cloud Infrastructure Core service.

    Lists the VLANs in the specified VCN and the specified compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_vlans = oci.Core.get_vlans(compartment_id=compartment_id,
        display_name=vlan_display_name,
        state=vlan_state,
        vcn_id=test_vcn["id"])
    ```


    :param builtins.str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param builtins.str display_name: A filter to return only resources that match the given display name exactly.
    :param builtins.str state: A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.
    :param builtins.str vcn_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['state'] = state
    __args__['vcnId'] = vcn_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Core/getVlans:getVlans', __args__, opts=opts, typ=GetVlansResult).value

    return AwaitableGetVlansResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        state=pulumi.get(__ret__, 'state'),
        vcn_id=pulumi.get(__ret__, 'vcn_id'),
        vlans=pulumi.get(__ret__, 'vlans'))
def get_vlans_output(compartment_id: Optional[pulumi.Input[builtins.str]] = None,
                     display_name: Optional[pulumi.Input[Optional[builtins.str]]] = None,
                     filters: Optional[pulumi.Input[Optional[Sequence[Union['GetVlansFilterArgs', 'GetVlansFilterArgsDict']]]]] = None,
                     state: Optional[pulumi.Input[Optional[builtins.str]]] = None,
                     vcn_id: Optional[pulumi.Input[Optional[builtins.str]]] = None,
                     opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetVlansResult]:
    """
    This data source provides the list of Vlans in Oracle Cloud Infrastructure Core service.

    Lists the VLANs in the specified VCN and the specified compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_vlans = oci.Core.get_vlans(compartment_id=compartment_id,
        display_name=vlan_display_name,
        state=vlan_state,
        vcn_id=test_vcn["id"])
    ```


    :param builtins.str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param builtins.str display_name: A filter to return only resources that match the given display name exactly.
    :param builtins.str state: A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.
    :param builtins.str vcn_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['state'] = state
    __args__['vcnId'] = vcn_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('oci:Core/getVlans:getVlans', __args__, opts=opts, typ=GetVlansResult)
    return __ret__.apply(lambda __response__: GetVlansResult(
        compartment_id=pulumi.get(__response__, 'compartment_id'),
        display_name=pulumi.get(__response__, 'display_name'),
        filters=pulumi.get(__response__, 'filters'),
        id=pulumi.get(__response__, 'id'),
        state=pulumi.get(__response__, 'state'),
        vcn_id=pulumi.get(__response__, 'vcn_id'),
        vlans=pulumi.get(__response__, 'vlans')))
