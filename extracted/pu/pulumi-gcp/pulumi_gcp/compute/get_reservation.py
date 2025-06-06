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
    'GetReservationResult',
    'AwaitableGetReservationResult',
    'get_reservation',
    'get_reservation_output',
]

@pulumi.output_type
class GetReservationResult:
    """
    A collection of values returned by getReservation.
    """
    def __init__(__self__, commitment=None, creation_timestamp=None, description=None, id=None, name=None, project=None, self_link=None, share_settings=None, specific_reservation_required=None, specific_reservations=None, status=None, zone=None):
        if commitment and not isinstance(commitment, str):
            raise TypeError("Expected argument 'commitment' to be a str")
        pulumi.set(__self__, "commitment", commitment)
        if creation_timestamp and not isinstance(creation_timestamp, str):
            raise TypeError("Expected argument 'creation_timestamp' to be a str")
        pulumi.set(__self__, "creation_timestamp", creation_timestamp)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if share_settings and not isinstance(share_settings, list):
            raise TypeError("Expected argument 'share_settings' to be a list")
        pulumi.set(__self__, "share_settings", share_settings)
        if specific_reservation_required and not isinstance(specific_reservation_required, bool):
            raise TypeError("Expected argument 'specific_reservation_required' to be a bool")
        pulumi.set(__self__, "specific_reservation_required", specific_reservation_required)
        if specific_reservations and not isinstance(specific_reservations, list):
            raise TypeError("Expected argument 'specific_reservations' to be a list")
        pulumi.set(__self__, "specific_reservations", specific_reservations)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if zone and not isinstance(zone, str):
            raise TypeError("Expected argument 'zone' to be a str")
        pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def commitment(self) -> builtins.str:
        return pulumi.get(self, "commitment")

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> builtins.str:
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter
    def description(self) -> builtins.str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> builtins.str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> Optional[builtins.str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> builtins.str:
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="shareSettings")
    def share_settings(self) -> Sequence['outputs.GetReservationShareSettingResult']:
        return pulumi.get(self, "share_settings")

    @property
    @pulumi.getter(name="specificReservationRequired")
    def specific_reservation_required(self) -> builtins.bool:
        return pulumi.get(self, "specific_reservation_required")

    @property
    @pulumi.getter(name="specificReservations")
    def specific_reservations(self) -> Sequence['outputs.GetReservationSpecificReservationResult']:
        return pulumi.get(self, "specific_reservations")

    @property
    @pulumi.getter
    def status(self) -> builtins.str:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def zone(self) -> builtins.str:
        return pulumi.get(self, "zone")


class AwaitableGetReservationResult(GetReservationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetReservationResult(
            commitment=self.commitment,
            creation_timestamp=self.creation_timestamp,
            description=self.description,
            id=self.id,
            name=self.name,
            project=self.project,
            self_link=self.self_link,
            share_settings=self.share_settings,
            specific_reservation_required=self.specific_reservation_required,
            specific_reservations=self.specific_reservations,
            status=self.status,
            zone=self.zone)


def get_reservation(name: Optional[builtins.str] = None,
                    project: Optional[builtins.str] = None,
                    zone: Optional[builtins.str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetReservationResult:
    """
    Provides access to available Google Compute Reservation Resources for a given project.
    See more about [Reservations of Compute Engine resources](https://cloud.google.com/compute/docs/instances/reservations-overview) in the upstream docs.

    ```python
    import pulumi
    import pulumi_gcp as gcp

    reservation = gcp.compute.get_reservation(name="gce-reservation",
        zone="us-central1-a")
    ```


    :param builtins.str name: The name of the Compute Reservation.
    :param builtins.str project: Project from which to list the Compute Reservation. Defaults to project declared in the provider.
    :param builtins.str zone: Zone where the Compute Reservation resides.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['project'] = project
    __args__['zone'] = zone
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:compute/getReservation:getReservation', __args__, opts=opts, typ=GetReservationResult).value

    return AwaitableGetReservationResult(
        commitment=pulumi.get(__ret__, 'commitment'),
        creation_timestamp=pulumi.get(__ret__, 'creation_timestamp'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        project=pulumi.get(__ret__, 'project'),
        self_link=pulumi.get(__ret__, 'self_link'),
        share_settings=pulumi.get(__ret__, 'share_settings'),
        specific_reservation_required=pulumi.get(__ret__, 'specific_reservation_required'),
        specific_reservations=pulumi.get(__ret__, 'specific_reservations'),
        status=pulumi.get(__ret__, 'status'),
        zone=pulumi.get(__ret__, 'zone'))
def get_reservation_output(name: Optional[pulumi.Input[builtins.str]] = None,
                           project: Optional[pulumi.Input[Optional[builtins.str]]] = None,
                           zone: Optional[pulumi.Input[builtins.str]] = None,
                           opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetReservationResult]:
    """
    Provides access to available Google Compute Reservation Resources for a given project.
    See more about [Reservations of Compute Engine resources](https://cloud.google.com/compute/docs/instances/reservations-overview) in the upstream docs.

    ```python
    import pulumi
    import pulumi_gcp as gcp

    reservation = gcp.compute.get_reservation(name="gce-reservation",
        zone="us-central1-a")
    ```


    :param builtins.str name: The name of the Compute Reservation.
    :param builtins.str project: Project from which to list the Compute Reservation. Defaults to project declared in the provider.
    :param builtins.str zone: Zone where the Compute Reservation resides.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['project'] = project
    __args__['zone'] = zone
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('gcp:compute/getReservation:getReservation', __args__, opts=opts, typ=GetReservationResult)
    return __ret__.apply(lambda __response__: GetReservationResult(
        commitment=pulumi.get(__response__, 'commitment'),
        creation_timestamp=pulumi.get(__response__, 'creation_timestamp'),
        description=pulumi.get(__response__, 'description'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        project=pulumi.get(__response__, 'project'),
        self_link=pulumi.get(__response__, 'self_link'),
        share_settings=pulumi.get(__response__, 'share_settings'),
        specific_reservation_required=pulumi.get(__response__, 'specific_reservation_required'),
        specific_reservations=pulumi.get(__response__, 'specific_reservations'),
        status=pulumi.get(__response__, 'status'),
        zone=pulumi.get(__response__, 'zone')))
