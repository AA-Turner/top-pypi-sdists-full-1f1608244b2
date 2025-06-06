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
    'GetOceInstancesFilterResult',
    'GetOceInstancesOceInstanceResult',
]

@pulumi.output_type
class GetOceInstancesFilterResult(dict):
    def __init__(__self__, *,
                 name: builtins.str,
                 values: Sequence[builtins.str],
                 regex: Optional[builtins.bool] = None):
        """
        :param builtins.str name: OceInstance Name
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "values", values)
        if regex is not None:
            pulumi.set(__self__, "regex", regex)

    @property
    @pulumi.getter
    def name(self) -> builtins.str:
        """
        OceInstance Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def values(self) -> Sequence[builtins.str]:
        return pulumi.get(self, "values")

    @property
    @pulumi.getter
    def regex(self) -> Optional[builtins.bool]:
        return pulumi.get(self, "regex")


@pulumi.output_type
class GetOceInstancesOceInstanceResult(dict):
    def __init__(__self__, *,
                 add_on_features: Sequence[builtins.str],
                 admin_email: builtins.str,
                 compartment_id: builtins.str,
                 defined_tags: Mapping[str, builtins.str],
                 description: builtins.str,
                 dr_region: builtins.str,
                 freeform_tags: Mapping[str, builtins.str],
                 guid: builtins.str,
                 id: builtins.str,
                 idcs_access_token: builtins.str,
                 idcs_tenancy: builtins.str,
                 instance_access_type: builtins.str,
                 instance_license_type: builtins.str,
                 instance_usage_type: builtins.str,
                 lifecycle_details: builtins.str,
                 name: builtins.str,
                 object_storage_namespace: builtins.str,
                 service: Mapping[str, builtins.str],
                 state: builtins.str,
                 state_message: builtins.str,
                 system_tags: Mapping[str, builtins.str],
                 tenancy_id: builtins.str,
                 tenancy_name: builtins.str,
                 time_created: builtins.str,
                 time_updated: builtins.str,
                 upgrade_schedule: builtins.str,
                 waf_primary_domain: builtins.str):
        """
        :param Sequence[builtins.str] add_on_features: a list of add-on features for the ocm instance
        :param builtins.str admin_email: Admin Email for Notification
        :param builtins.str compartment_id: The ID of the compartment in which to list resources.
        :param Mapping[str, builtins.str] defined_tags: Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{"foo-namespace.bar-key": "value"}`
        :param builtins.str description: OceInstance description, can be updated
        :param builtins.str dr_region: disaster recovery paired ragion name
        :param Mapping[str, builtins.str] freeform_tags: Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        :param builtins.str guid: Unique GUID identifier that is immutable on creation
        :param builtins.str id: Unique identifier that is immutable on creation
        :param builtins.str idcs_tenancy: IDCS Tenancy Identifier
        :param builtins.str instance_access_type: Flag indicating whether the instance access is private or public
        :param builtins.str instance_license_type: Flag indicating whether the instance license is new cloud or bring your own license
        :param builtins.str instance_usage_type: Instance type based on its usage
        :param builtins.str lifecycle_details: Details of the current state of the instance lifecycle
        :param builtins.str name: OceInstance Name
        :param builtins.str object_storage_namespace: Object Storage Namespace of tenancy
        :param Mapping[str, builtins.str] service: SERVICE data. Example: `{"service": {"IDCS": "value"}}`
        :param builtins.str state: Filter results on lifecycleState.
        :param builtins.str state_message: An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        :param Mapping[str, builtins.str] system_tags: Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        :param builtins.str tenancy_id: The ID of the tenancy in which to list resources.
        :param builtins.str tenancy_name: Tenancy Name
        :param builtins.str time_created: The time the the OceInstance was created. An RFC3339 formatted datetime string
        :param builtins.str time_updated: The time the OceInstance was updated. An RFC3339 formatted datetime string
        :param builtins.str upgrade_schedule: Upgrade schedule type representing service to be upgraded immediately whenever latest version is released or delay upgrade of the service to previous released version
        :param builtins.str waf_primary_domain: Web Application Firewall(WAF) primary domain
        """
        pulumi.set(__self__, "add_on_features", add_on_features)
        pulumi.set(__self__, "admin_email", admin_email)
        pulumi.set(__self__, "compartment_id", compartment_id)
        pulumi.set(__self__, "defined_tags", defined_tags)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "dr_region", dr_region)
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        pulumi.set(__self__, "guid", guid)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "idcs_access_token", idcs_access_token)
        pulumi.set(__self__, "idcs_tenancy", idcs_tenancy)
        pulumi.set(__self__, "instance_access_type", instance_access_type)
        pulumi.set(__self__, "instance_license_type", instance_license_type)
        pulumi.set(__self__, "instance_usage_type", instance_usage_type)
        pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "object_storage_namespace", object_storage_namespace)
        pulumi.set(__self__, "service", service)
        pulumi.set(__self__, "state", state)
        pulumi.set(__self__, "state_message", state_message)
        pulumi.set(__self__, "system_tags", system_tags)
        pulumi.set(__self__, "tenancy_id", tenancy_id)
        pulumi.set(__self__, "tenancy_name", tenancy_name)
        pulumi.set(__self__, "time_created", time_created)
        pulumi.set(__self__, "time_updated", time_updated)
        pulumi.set(__self__, "upgrade_schedule", upgrade_schedule)
        pulumi.set(__self__, "waf_primary_domain", waf_primary_domain)

    @property
    @pulumi.getter(name="addOnFeatures")
    def add_on_features(self) -> Sequence[builtins.str]:
        """
        a list of add-on features for the ocm instance
        """
        return pulumi.get(self, "add_on_features")

    @property
    @pulumi.getter(name="adminEmail")
    def admin_email(self) -> builtins.str:
        """
        Admin Email for Notification
        """
        return pulumi.get(self, "admin_email")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> builtins.str:
        """
        The ID of the compartment in which to list resources.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, builtins.str]:
        """
        Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter
    def description(self) -> builtins.str:
        """
        OceInstance description, can be updated
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="drRegion")
    def dr_region(self) -> builtins.str:
        """
        disaster recovery paired ragion name
        """
        return pulumi.get(self, "dr_region")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, builtins.str]:
        """
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def guid(self) -> builtins.str:
        """
        Unique GUID identifier that is immutable on creation
        """
        return pulumi.get(self, "guid")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        """
        Unique identifier that is immutable on creation
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="idcsAccessToken")
    def idcs_access_token(self) -> builtins.str:
        return pulumi.get(self, "idcs_access_token")

    @property
    @pulumi.getter(name="idcsTenancy")
    def idcs_tenancy(self) -> builtins.str:
        """
        IDCS Tenancy Identifier
        """
        return pulumi.get(self, "idcs_tenancy")

    @property
    @pulumi.getter(name="instanceAccessType")
    def instance_access_type(self) -> builtins.str:
        """
        Flag indicating whether the instance access is private or public
        """
        return pulumi.get(self, "instance_access_type")

    @property
    @pulumi.getter(name="instanceLicenseType")
    def instance_license_type(self) -> builtins.str:
        """
        Flag indicating whether the instance license is new cloud or bring your own license
        """
        return pulumi.get(self, "instance_license_type")

    @property
    @pulumi.getter(name="instanceUsageType")
    def instance_usage_type(self) -> builtins.str:
        """
        Instance type based on its usage
        """
        return pulumi.get(self, "instance_usage_type")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> builtins.str:
        """
        Details of the current state of the instance lifecycle
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter
    def name(self) -> builtins.str:
        """
        OceInstance Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="objectStorageNamespace")
    def object_storage_namespace(self) -> builtins.str:
        """
        Object Storage Namespace of tenancy
        """
        return pulumi.get(self, "object_storage_namespace")

    @property
    @pulumi.getter
    def service(self) -> Mapping[str, builtins.str]:
        """
        SERVICE data. Example: `{"service": {"IDCS": "value"}}`
        """
        return pulumi.get(self, "service")

    @property
    @pulumi.getter
    def state(self) -> builtins.str:
        """
        Filter results on lifecycleState.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> builtins.str:
        """
        An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        """
        return pulumi.get(self, "state_message")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Mapping[str, builtins.str]:
        """
        Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="tenancyId")
    def tenancy_id(self) -> builtins.str:
        """
        The ID of the tenancy in which to list resources.
        """
        return pulumi.get(self, "tenancy_id")

    @property
    @pulumi.getter(name="tenancyName")
    def tenancy_name(self) -> builtins.str:
        """
        Tenancy Name
        """
        return pulumi.get(self, "tenancy_name")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> builtins.str:
        """
        The time the the OceInstance was created. An RFC3339 formatted datetime string
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> builtins.str:
        """
        The time the OceInstance was updated. An RFC3339 formatted datetime string
        """
        return pulumi.get(self, "time_updated")

    @property
    @pulumi.getter(name="upgradeSchedule")
    def upgrade_schedule(self) -> builtins.str:
        """
        Upgrade schedule type representing service to be upgraded immediately whenever latest version is released or delay upgrade of the service to previous released version
        """
        return pulumi.get(self, "upgrade_schedule")

    @property
    @pulumi.getter(name="wafPrimaryDomain")
    def waf_primary_domain(self) -> builtins.str:
        """
        Web Application Firewall(WAF) primary domain
        """
        return pulumi.get(self, "waf_primary_domain")


