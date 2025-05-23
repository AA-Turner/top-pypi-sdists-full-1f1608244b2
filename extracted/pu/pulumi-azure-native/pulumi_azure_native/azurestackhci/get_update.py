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
    'GetUpdateResult',
    'AwaitableGetUpdateResult',
    'get_update',
    'get_update_output',
]

@pulumi.output_type
class GetUpdateResult:
    """
    Update details
    """
    def __init__(__self__, additional_properties=None, availability_type=None, azure_api_version=None, description=None, display_name=None, health_check_date=None, id=None, installed_date=None, location=None, min_sbe_version_required=None, name=None, notify_message=None, package_path=None, package_size_in_mb=None, package_type=None, prerequisites=None, progress_percentage=None, provisioning_state=None, publisher=None, release_link=None, state=None, system_data=None, type=None, version=None):
        if additional_properties and not isinstance(additional_properties, str):
            raise TypeError("Expected argument 'additional_properties' to be a str")
        pulumi.set(__self__, "additional_properties", additional_properties)
        if availability_type and not isinstance(availability_type, str):
            raise TypeError("Expected argument 'availability_type' to be a str")
        pulumi.set(__self__, "availability_type", availability_type)
        if azure_api_version and not isinstance(azure_api_version, str):
            raise TypeError("Expected argument 'azure_api_version' to be a str")
        pulumi.set(__self__, "azure_api_version", azure_api_version)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if health_check_date and not isinstance(health_check_date, str):
            raise TypeError("Expected argument 'health_check_date' to be a str")
        pulumi.set(__self__, "health_check_date", health_check_date)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if installed_date and not isinstance(installed_date, str):
            raise TypeError("Expected argument 'installed_date' to be a str")
        pulumi.set(__self__, "installed_date", installed_date)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if min_sbe_version_required and not isinstance(min_sbe_version_required, str):
            raise TypeError("Expected argument 'min_sbe_version_required' to be a str")
        pulumi.set(__self__, "min_sbe_version_required", min_sbe_version_required)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if notify_message and not isinstance(notify_message, str):
            raise TypeError("Expected argument 'notify_message' to be a str")
        pulumi.set(__self__, "notify_message", notify_message)
        if package_path and not isinstance(package_path, str):
            raise TypeError("Expected argument 'package_path' to be a str")
        pulumi.set(__self__, "package_path", package_path)
        if package_size_in_mb and not isinstance(package_size_in_mb, float):
            raise TypeError("Expected argument 'package_size_in_mb' to be a float")
        pulumi.set(__self__, "package_size_in_mb", package_size_in_mb)
        if package_type and not isinstance(package_type, str):
            raise TypeError("Expected argument 'package_type' to be a str")
        pulumi.set(__self__, "package_type", package_type)
        if prerequisites and not isinstance(prerequisites, list):
            raise TypeError("Expected argument 'prerequisites' to be a list")
        pulumi.set(__self__, "prerequisites", prerequisites)
        if progress_percentage and not isinstance(progress_percentage, float):
            raise TypeError("Expected argument 'progress_percentage' to be a float")
        pulumi.set(__self__, "progress_percentage", progress_percentage)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if publisher and not isinstance(publisher, str):
            raise TypeError("Expected argument 'publisher' to be a str")
        pulumi.set(__self__, "publisher", publisher)
        if release_link and not isinstance(release_link, str):
            raise TypeError("Expected argument 'release_link' to be a str")
        pulumi.set(__self__, "release_link", release_link)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> Optional[builtins.str]:
        """
        Extensible KV pairs serialized as a string. This is currently used to report the stamp OEM family and hardware model information when an update is flagged as Invalid for the stamp based on OEM type.
        """
        return pulumi.get(self, "additional_properties")

    @property
    @pulumi.getter(name="availabilityType")
    def availability_type(self) -> Optional[builtins.str]:
        """
        Indicates the way the update content can be downloaded.
        """
        return pulumi.get(self, "availability_type")

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> builtins.str:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter
    def description(self) -> Optional[builtins.str]:
        """
        Description of the update.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[builtins.str]:
        """
        Display name of the Update
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="healthCheckDate")
    def health_check_date(self) -> Optional[builtins.str]:
        """
        Last time the package-specific checks were run.
        """
        return pulumi.get(self, "health_check_date")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="installedDate")
    def installed_date(self) -> Optional[builtins.str]:
        """
        Date that the update was installed.
        """
        return pulumi.get(self, "installed_date")

    @property
    @pulumi.getter
    def location(self) -> Optional[builtins.str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="minSbeVersionRequired")
    def min_sbe_version_required(self) -> Optional[builtins.str]:
        """
        Minimum Sbe Version of the update.
        """
        return pulumi.get(self, "min_sbe_version_required")

    @property
    @pulumi.getter
    def name(self) -> builtins.str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notifyMessage")
    def notify_message(self) -> Optional[builtins.str]:
        """
        Brief message with instructions for updates of AvailabilityType Notify.
        """
        return pulumi.get(self, "notify_message")

    @property
    @pulumi.getter(name="packagePath")
    def package_path(self) -> Optional[builtins.str]:
        """
        Path where the update package is available.
        """
        return pulumi.get(self, "package_path")

    @property
    @pulumi.getter(name="packageSizeInMb")
    def package_size_in_mb(self) -> Optional[builtins.float]:
        """
        Size of the package. This value is a combination of the size from update metadata and size of the payload that results from the live scan operation for OS update content.
        """
        return pulumi.get(self, "package_size_in_mb")

    @property
    @pulumi.getter(name="packageType")
    def package_type(self) -> Optional[builtins.str]:
        """
        Customer-visible type of the update.
        """
        return pulumi.get(self, "package_type")

    @property
    @pulumi.getter
    def prerequisites(self) -> Optional[Sequence['outputs.UpdatePrerequisiteResponse']]:
        """
        If update State is HasPrerequisite, this property contains an array of objects describing prerequisite updates before installing this update. Otherwise, it is empty.
        """
        return pulumi.get(self, "prerequisites")

    @property
    @pulumi.getter(name="progressPercentage")
    def progress_percentage(self) -> Optional[builtins.float]:
        """
        Progress percentage of ongoing operation. Currently this property is only valid when the update is in the Downloading state, where it maps to how much of the update content has been downloaded.
        """
        return pulumi.get(self, "progress_percentage")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> builtins.str:
        """
        Provisioning state of the Updates proxy resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def publisher(self) -> Optional[builtins.str]:
        """
        Publisher of the update package.
        """
        return pulumi.get(self, "publisher")

    @property
    @pulumi.getter(name="releaseLink")
    def release_link(self) -> Optional[builtins.str]:
        """
        Link to release notes for the update.
        """
        return pulumi.get(self, "release_link")

    @property
    @pulumi.getter
    def state(self) -> Optional[builtins.str]:
        """
        State of the update as it relates to this stamp.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> builtins.str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> Optional[builtins.str]:
        """
        Version of the update.
        """
        return pulumi.get(self, "version")


class AwaitableGetUpdateResult(GetUpdateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUpdateResult(
            additional_properties=self.additional_properties,
            availability_type=self.availability_type,
            azure_api_version=self.azure_api_version,
            description=self.description,
            display_name=self.display_name,
            health_check_date=self.health_check_date,
            id=self.id,
            installed_date=self.installed_date,
            location=self.location,
            min_sbe_version_required=self.min_sbe_version_required,
            name=self.name,
            notify_message=self.notify_message,
            package_path=self.package_path,
            package_size_in_mb=self.package_size_in_mb,
            package_type=self.package_type,
            prerequisites=self.prerequisites,
            progress_percentage=self.progress_percentage,
            provisioning_state=self.provisioning_state,
            publisher=self.publisher,
            release_link=self.release_link,
            state=self.state,
            system_data=self.system_data,
            type=self.type,
            version=self.version)


def get_update(cluster_name: Optional[builtins.str] = None,
               resource_group_name: Optional[builtins.str] = None,
               update_name: Optional[builtins.str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUpdateResult:
    """
    Get specified Update

    Uses Azure REST API version 2024-04-01.

    Other available API versions: 2022-12-15-preview, 2023-02-01, 2023-03-01, 2023-06-01, 2023-08-01, 2023-08-01-preview, 2023-11-01-preview, 2024-01-01, 2024-02-15-preview, 2024-09-01-preview, 2024-12-01-preview, 2025-02-01-preview. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native azurestackhci [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param builtins.str cluster_name: The name of the cluster.
    :param builtins.str resource_group_name: The name of the resource group. The name is case insensitive.
    :param builtins.str update_name: The name of the Update
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['updateName'] = update_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:azurestackhci:getUpdate', __args__, opts=opts, typ=GetUpdateResult).value

    return AwaitableGetUpdateResult(
        additional_properties=pulumi.get(__ret__, 'additional_properties'),
        availability_type=pulumi.get(__ret__, 'availability_type'),
        azure_api_version=pulumi.get(__ret__, 'azure_api_version'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        health_check_date=pulumi.get(__ret__, 'health_check_date'),
        id=pulumi.get(__ret__, 'id'),
        installed_date=pulumi.get(__ret__, 'installed_date'),
        location=pulumi.get(__ret__, 'location'),
        min_sbe_version_required=pulumi.get(__ret__, 'min_sbe_version_required'),
        name=pulumi.get(__ret__, 'name'),
        notify_message=pulumi.get(__ret__, 'notify_message'),
        package_path=pulumi.get(__ret__, 'package_path'),
        package_size_in_mb=pulumi.get(__ret__, 'package_size_in_mb'),
        package_type=pulumi.get(__ret__, 'package_type'),
        prerequisites=pulumi.get(__ret__, 'prerequisites'),
        progress_percentage=pulumi.get(__ret__, 'progress_percentage'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        publisher=pulumi.get(__ret__, 'publisher'),
        release_link=pulumi.get(__ret__, 'release_link'),
        state=pulumi.get(__ret__, 'state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'),
        version=pulumi.get(__ret__, 'version'))
def get_update_output(cluster_name: Optional[pulumi.Input[builtins.str]] = None,
                      resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                      update_name: Optional[pulumi.Input[builtins.str]] = None,
                      opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetUpdateResult]:
    """
    Get specified Update

    Uses Azure REST API version 2024-04-01.

    Other available API versions: 2022-12-15-preview, 2023-02-01, 2023-03-01, 2023-06-01, 2023-08-01, 2023-08-01-preview, 2023-11-01-preview, 2024-01-01, 2024-02-15-preview, 2024-09-01-preview, 2024-12-01-preview, 2025-02-01-preview. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native azurestackhci [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param builtins.str cluster_name: The name of the cluster.
    :param builtins.str resource_group_name: The name of the resource group. The name is case insensitive.
    :param builtins.str update_name: The name of the Update
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['updateName'] = update_name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('azure-native:azurestackhci:getUpdate', __args__, opts=opts, typ=GetUpdateResult)
    return __ret__.apply(lambda __response__: GetUpdateResult(
        additional_properties=pulumi.get(__response__, 'additional_properties'),
        availability_type=pulumi.get(__response__, 'availability_type'),
        azure_api_version=pulumi.get(__response__, 'azure_api_version'),
        description=pulumi.get(__response__, 'description'),
        display_name=pulumi.get(__response__, 'display_name'),
        health_check_date=pulumi.get(__response__, 'health_check_date'),
        id=pulumi.get(__response__, 'id'),
        installed_date=pulumi.get(__response__, 'installed_date'),
        location=pulumi.get(__response__, 'location'),
        min_sbe_version_required=pulumi.get(__response__, 'min_sbe_version_required'),
        name=pulumi.get(__response__, 'name'),
        notify_message=pulumi.get(__response__, 'notify_message'),
        package_path=pulumi.get(__response__, 'package_path'),
        package_size_in_mb=pulumi.get(__response__, 'package_size_in_mb'),
        package_type=pulumi.get(__response__, 'package_type'),
        prerequisites=pulumi.get(__response__, 'prerequisites'),
        progress_percentage=pulumi.get(__response__, 'progress_percentage'),
        provisioning_state=pulumi.get(__response__, 'provisioning_state'),
        publisher=pulumi.get(__response__, 'publisher'),
        release_link=pulumi.get(__response__, 'release_link'),
        state=pulumi.get(__response__, 'state'),
        system_data=pulumi.get(__response__, 'system_data'),
        type=pulumi.get(__response__, 'type'),
        version=pulumi.get(__response__, 'version')))
