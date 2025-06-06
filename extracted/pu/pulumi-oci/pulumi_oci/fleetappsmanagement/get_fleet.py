# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
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
    'GetFleetResult',
    'AwaitableGetFleetResult',
    'get_fleet',
    'get_fleet_output',
]

@pulumi.output_type
class GetFleetResult:
    """
    A collection of values returned by getFleet.
    """
    def __init__(__self__, application_type=None, compartment_id=None, credentials=None, defined_tags=None, description=None, display_name=None, environment_type=None, fleet_id=None, fleet_type=None, freeform_tags=None, group_type=None, id=None, is_target_auto_confirm=None, lifecycle_details=None, notification_preferences=None, products=None, resource_region=None, resource_selection_type=None, rule_selection_criterias=None, state=None, system_tags=None, time_created=None, time_updated=None):
        if application_type and not isinstance(application_type, str):
            raise TypeError("Expected argument 'application_type' to be a str")
        pulumi.set(__self__, "application_type", application_type)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if credentials and not isinstance(credentials, list):
            raise TypeError("Expected argument 'credentials' to be a list")
        pulumi.set(__self__, "credentials", credentials)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if environment_type and not isinstance(environment_type, str):
            raise TypeError("Expected argument 'environment_type' to be a str")
        pulumi.set(__self__, "environment_type", environment_type)
        if fleet_id and not isinstance(fleet_id, str):
            raise TypeError("Expected argument 'fleet_id' to be a str")
        pulumi.set(__self__, "fleet_id", fleet_id)
        if fleet_type and not isinstance(fleet_type, str):
            raise TypeError("Expected argument 'fleet_type' to be a str")
        pulumi.set(__self__, "fleet_type", fleet_type)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if group_type and not isinstance(group_type, str):
            raise TypeError("Expected argument 'group_type' to be a str")
        pulumi.set(__self__, "group_type", group_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_target_auto_confirm and not isinstance(is_target_auto_confirm, bool):
            raise TypeError("Expected argument 'is_target_auto_confirm' to be a bool")
        pulumi.set(__self__, "is_target_auto_confirm", is_target_auto_confirm)
        if lifecycle_details and not isinstance(lifecycle_details, str):
            raise TypeError("Expected argument 'lifecycle_details' to be a str")
        pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if notification_preferences and not isinstance(notification_preferences, list):
            raise TypeError("Expected argument 'notification_preferences' to be a list")
        pulumi.set(__self__, "notification_preferences", notification_preferences)
        if products and not isinstance(products, list):
            raise TypeError("Expected argument 'products' to be a list")
        pulumi.set(__self__, "products", products)
        if resource_region and not isinstance(resource_region, str):
            raise TypeError("Expected argument 'resource_region' to be a str")
        pulumi.set(__self__, "resource_region", resource_region)
        if resource_selection_type and not isinstance(resource_selection_type, str):
            raise TypeError("Expected argument 'resource_selection_type' to be a str")
        pulumi.set(__self__, "resource_selection_type", resource_selection_type)
        if rule_selection_criterias and not isinstance(rule_selection_criterias, list):
            raise TypeError("Expected argument 'rule_selection_criterias' to be a list")
        pulumi.set(__self__, "rule_selection_criterias", rule_selection_criterias)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_tags and not isinstance(system_tags, dict):
            raise TypeError("Expected argument 'system_tags' to be a dict")
        pulumi.set(__self__, "system_tags", system_tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_updated and not isinstance(time_updated, str):
            raise TypeError("Expected argument 'time_updated' to be a str")
        pulumi.set(__self__, "time_updated", time_updated)

    @property
    @pulumi.getter(name="applicationType")
    def application_type(self) -> builtins.str:
        """
        Product stack associated with the Fleet. Applicable for ENVIRONMENT fleet types.
        """
        return pulumi.get(self, "application_type")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> builtins.str:
        """
        Tenancy Id (Root Compartment Id)for which the rule is created.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def credentials(self) -> Sequence['outputs.GetFleetCredentialResult']:
        """
        Credentials associated with the Fleet.
        """
        return pulumi.get(self, "credentials")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, builtins.str]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter
    def description(self) -> builtins.str:
        """
        A user-friendly description. To provide some insight about the resource. Avoid entering confidential information.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> builtins.str:
        """
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My new resource`
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="environmentType")
    def environment_type(self) -> builtins.str:
        """
        Environment Type associated with the Fleet. Applicable for ENVIRONMENT fleet types.
        """
        return pulumi.get(self, "environment_type")

    @property
    @pulumi.getter(name="fleetId")
    def fleet_id(self) -> builtins.str:
        return pulumi.get(self, "fleet_id")

    @property
    @pulumi.getter(name="fleetType")
    def fleet_type(self) -> builtins.str:
        """
        Type of the Fleet. PRODUCT - A fleet of product-specific resources for a product type. ENVIRONMENT - A fleet of environment-specific resources for a product stack. GROUP - A fleet of a fleet of either environment or product fleets. GENERIC - A fleet of resources selected dynamically or manually for reporting purposes
        """
        return pulumi.get(self, "fleet_type")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, builtins.str]:
        """
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter(name="groupType")
    def group_type(self) -> builtins.str:
        """
        Group Type associated with Group Fleet. Applicable for GROUP fleet types.
        """
        return pulumi.get(self, "group_type")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        """
        The OCID of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isTargetAutoConfirm")
    def is_target_auto_confirm(self) -> builtins.bool:
        """
        A value that represents if auto-confirming of the targets can be enabled. This will allow targets to be auto-confirmed in the fleet without manual intervention.
        """
        return pulumi.get(self, "is_target_auto_confirm")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> builtins.str:
        """
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter(name="notificationPreferences")
    def notification_preferences(self) -> Sequence['outputs.GetFleetNotificationPreferenceResult']:
        """
        Notification information to get notified when the fleet status changes.
        """
        return pulumi.get(self, "notification_preferences")

    @property
    @pulumi.getter
    def products(self) -> Sequence[builtins.str]:
        """
        Products associated with the Fleet.
        """
        return pulumi.get(self, "products")

    @property
    @pulumi.getter(name="resourceRegion")
    def resource_region(self) -> builtins.str:
        """
        Associated region
        """
        return pulumi.get(self, "resource_region")

    @property
    @pulumi.getter(name="resourceSelectionType")
    def resource_selection_type(self) -> builtins.str:
        """
        Type of resource selection in a Fleet. Select resources manually or select resources based on rules.
        """
        return pulumi.get(self, "resource_selection_type")

    @property
    @pulumi.getter(name="ruleSelectionCriterias")
    def rule_selection_criterias(self) -> Sequence['outputs.GetFleetRuleSelectionCriteriaResult']:
        """
        Rule Selection Criteria for DYNAMIC resource selection for a GENERIC fleet. Rules define what resources are members of this fleet. All resources that meet the criteria are added automatically.
        """
        return pulumi.get(self, "rule_selection_criterias")

    @property
    @pulumi.getter
    def state(self) -> builtins.str:
        """
        The lifecycle state of the Fleet.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Mapping[str, builtins.str]:
        """
        System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> builtins.str:
        """
        The time this resource was created. An RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> builtins.str:
        """
        The time this resource was last updated. An RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_updated")


class AwaitableGetFleetResult(GetFleetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFleetResult(
            application_type=self.application_type,
            compartment_id=self.compartment_id,
            credentials=self.credentials,
            defined_tags=self.defined_tags,
            description=self.description,
            display_name=self.display_name,
            environment_type=self.environment_type,
            fleet_id=self.fleet_id,
            fleet_type=self.fleet_type,
            freeform_tags=self.freeform_tags,
            group_type=self.group_type,
            id=self.id,
            is_target_auto_confirm=self.is_target_auto_confirm,
            lifecycle_details=self.lifecycle_details,
            notification_preferences=self.notification_preferences,
            products=self.products,
            resource_region=self.resource_region,
            resource_selection_type=self.resource_selection_type,
            rule_selection_criterias=self.rule_selection_criterias,
            state=self.state,
            system_tags=self.system_tags,
            time_created=self.time_created,
            time_updated=self.time_updated)


def get_fleet(fleet_id: Optional[builtins.str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFleetResult:
    """
    This data source provides details about a specific Fleet resource in Oracle Cloud Infrastructure Fleet Apps Management service.

    Get the details of a fleet in Fleet Application Management.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_fleet = oci.FleetAppsManagement.get_fleet(fleet_id=test_fleet_oci_fleet_apps_management_fleet["id"])
    ```


    :param builtins.str fleet_id: Unique Fleet identifier.
    """
    __args__ = dict()
    __args__['fleetId'] = fleet_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:FleetAppsManagement/getFleet:getFleet', __args__, opts=opts, typ=GetFleetResult).value

    return AwaitableGetFleetResult(
        application_type=pulumi.get(__ret__, 'application_type'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        credentials=pulumi.get(__ret__, 'credentials'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        environment_type=pulumi.get(__ret__, 'environment_type'),
        fleet_id=pulumi.get(__ret__, 'fleet_id'),
        fleet_type=pulumi.get(__ret__, 'fleet_type'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        group_type=pulumi.get(__ret__, 'group_type'),
        id=pulumi.get(__ret__, 'id'),
        is_target_auto_confirm=pulumi.get(__ret__, 'is_target_auto_confirm'),
        lifecycle_details=pulumi.get(__ret__, 'lifecycle_details'),
        notification_preferences=pulumi.get(__ret__, 'notification_preferences'),
        products=pulumi.get(__ret__, 'products'),
        resource_region=pulumi.get(__ret__, 'resource_region'),
        resource_selection_type=pulumi.get(__ret__, 'resource_selection_type'),
        rule_selection_criterias=pulumi.get(__ret__, 'rule_selection_criterias'),
        state=pulumi.get(__ret__, 'state'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_updated=pulumi.get(__ret__, 'time_updated'))
def get_fleet_output(fleet_id: Optional[pulumi.Input[builtins.str]] = None,
                     opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetFleetResult]:
    """
    This data source provides details about a specific Fleet resource in Oracle Cloud Infrastructure Fleet Apps Management service.

    Get the details of a fleet in Fleet Application Management.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_fleet = oci.FleetAppsManagement.get_fleet(fleet_id=test_fleet_oci_fleet_apps_management_fleet["id"])
    ```


    :param builtins.str fleet_id: Unique Fleet identifier.
    """
    __args__ = dict()
    __args__['fleetId'] = fleet_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('oci:FleetAppsManagement/getFleet:getFleet', __args__, opts=opts, typ=GetFleetResult)
    return __ret__.apply(lambda __response__: GetFleetResult(
        application_type=pulumi.get(__response__, 'application_type'),
        compartment_id=pulumi.get(__response__, 'compartment_id'),
        credentials=pulumi.get(__response__, 'credentials'),
        defined_tags=pulumi.get(__response__, 'defined_tags'),
        description=pulumi.get(__response__, 'description'),
        display_name=pulumi.get(__response__, 'display_name'),
        environment_type=pulumi.get(__response__, 'environment_type'),
        fleet_id=pulumi.get(__response__, 'fleet_id'),
        fleet_type=pulumi.get(__response__, 'fleet_type'),
        freeform_tags=pulumi.get(__response__, 'freeform_tags'),
        group_type=pulumi.get(__response__, 'group_type'),
        id=pulumi.get(__response__, 'id'),
        is_target_auto_confirm=pulumi.get(__response__, 'is_target_auto_confirm'),
        lifecycle_details=pulumi.get(__response__, 'lifecycle_details'),
        notification_preferences=pulumi.get(__response__, 'notification_preferences'),
        products=pulumi.get(__response__, 'products'),
        resource_region=pulumi.get(__response__, 'resource_region'),
        resource_selection_type=pulumi.get(__response__, 'resource_selection_type'),
        rule_selection_criterias=pulumi.get(__response__, 'rule_selection_criterias'),
        state=pulumi.get(__response__, 'state'),
        system_tags=pulumi.get(__response__, 'system_tags'),
        time_created=pulumi.get(__response__, 'time_created'),
        time_updated=pulumi.get(__response__, 'time_updated')))
