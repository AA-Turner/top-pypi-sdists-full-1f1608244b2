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

__all__ = ['DataExportArgs', 'DataExport']

@pulumi.input_type
class DataExportArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[builtins.str],
                 resource_id: pulumi.Input[builtins.str],
                 table_names: pulumi.Input[Sequence[pulumi.Input[builtins.str]]],
                 workspace_name: pulumi.Input[builtins.str],
                 created_date: Optional[pulumi.Input[builtins.str]] = None,
                 data_export_id: Optional[pulumi.Input[builtins.str]] = None,
                 data_export_name: Optional[pulumi.Input[builtins.str]] = None,
                 enable: Optional[pulumi.Input[builtins.bool]] = None,
                 event_hub_name: Optional[pulumi.Input[builtins.str]] = None,
                 last_modified_date: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a DataExport resource.
        :param pulumi.Input[builtins.str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[builtins.str] resource_id: The destination resource ID. This can be copied from the Properties entry of the destination resource in Azure.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] table_names: An array of tables to export, for example: [“Heartbeat, SecurityEvent”].
        :param pulumi.Input[builtins.str] workspace_name: The name of the workspace.
        :param pulumi.Input[builtins.str] created_date: The latest data export rule modification time.
        :param pulumi.Input[builtins.str] data_export_id: The data export rule ID.
        :param pulumi.Input[builtins.str] data_export_name: The data export rule name.
        :param pulumi.Input[builtins.bool] enable: Active when enabled.
        :param pulumi.Input[builtins.str] event_hub_name: Optional. Allows to define an Event Hub name. Not applicable when destination is Storage Account.
        :param pulumi.Input[builtins.str] last_modified_date: Date and time when the export was last modified.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "resource_id", resource_id)
        pulumi.set(__self__, "table_names", table_names)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if created_date is not None:
            pulumi.set(__self__, "created_date", created_date)
        if data_export_id is not None:
            pulumi.set(__self__, "data_export_id", data_export_id)
        if data_export_name is not None:
            pulumi.set(__self__, "data_export_name", data_export_name)
        if enable is not None:
            pulumi.set(__self__, "enable", enable)
        if event_hub_name is not None:
            pulumi.set(__self__, "event_hub_name", event_hub_name)
        if last_modified_date is not None:
            pulumi.set(__self__, "last_modified_date", last_modified_date)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[builtins.str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[builtins.str]:
        """
        The destination resource ID. This can be copied from the Properties entry of the destination resource in Azure.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter(name="tableNames")
    def table_names(self) -> pulumi.Input[Sequence[pulumi.Input[builtins.str]]]:
        """
        An array of tables to export, for example: [“Heartbeat, SecurityEvent”].
        """
        return pulumi.get(self, "table_names")

    @table_names.setter
    def table_names(self, value: pulumi.Input[Sequence[pulumi.Input[builtins.str]]]):
        pulumi.set(self, "table_names", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[builtins.str]:
        """
        The name of the workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The latest data export rule modification time.
        """
        return pulumi.get(self, "created_date")

    @created_date.setter
    def created_date(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "created_date", value)

    @property
    @pulumi.getter(name="dataExportId")
    def data_export_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The data export rule ID.
        """
        return pulumi.get(self, "data_export_id")

    @data_export_id.setter
    def data_export_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "data_export_id", value)

    @property
    @pulumi.getter(name="dataExportName")
    def data_export_name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The data export rule name.
        """
        return pulumi.get(self, "data_export_name")

    @data_export_name.setter
    def data_export_name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "data_export_name", value)

    @property
    @pulumi.getter
    def enable(self) -> Optional[pulumi.Input[builtins.bool]]:
        """
        Active when enabled.
        """
        return pulumi.get(self, "enable")

    @enable.setter
    def enable(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "enable", value)

    @property
    @pulumi.getter(name="eventHubName")
    def event_hub_name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Optional. Allows to define an Event Hub name. Not applicable when destination is Storage Account.
        """
        return pulumi.get(self, "event_hub_name")

    @event_hub_name.setter
    def event_hub_name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "event_hub_name", value)

    @property
    @pulumi.getter(name="lastModifiedDate")
    def last_modified_date(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Date and time when the export was last modified.
        """
        return pulumi.get(self, "last_modified_date")

    @last_modified_date.setter
    def last_modified_date(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "last_modified_date", value)


@pulumi.type_token("azure-native:operationalinsights:DataExport")
class DataExport(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 created_date: Optional[pulumi.Input[builtins.str]] = None,
                 data_export_id: Optional[pulumi.Input[builtins.str]] = None,
                 data_export_name: Optional[pulumi.Input[builtins.str]] = None,
                 enable: Optional[pulumi.Input[builtins.bool]] = None,
                 event_hub_name: Optional[pulumi.Input[builtins.str]] = None,
                 last_modified_date: Optional[pulumi.Input[builtins.str]] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 resource_id: Optional[pulumi.Input[builtins.str]] = None,
                 table_names: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 workspace_name: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        The top level data export resource container.

        Uses Azure REST API version 2023-09-01. In version 2.x of the Azure Native provider, it used API version 2020-08-01.

        Other available API versions: 2019-08-01-preview, 2020-03-01-preview, 2020-08-01, 2025-02-01. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native operationalinsights [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] created_date: The latest data export rule modification time.
        :param pulumi.Input[builtins.str] data_export_id: The data export rule ID.
        :param pulumi.Input[builtins.str] data_export_name: The data export rule name.
        :param pulumi.Input[builtins.bool] enable: Active when enabled.
        :param pulumi.Input[builtins.str] event_hub_name: Optional. Allows to define an Event Hub name. Not applicable when destination is Storage Account.
        :param pulumi.Input[builtins.str] last_modified_date: Date and time when the export was last modified.
        :param pulumi.Input[builtins.str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[builtins.str] resource_id: The destination resource ID. This can be copied from the Properties entry of the destination resource in Azure.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] table_names: An array of tables to export, for example: [“Heartbeat, SecurityEvent”].
        :param pulumi.Input[builtins.str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DataExportArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The top level data export resource container.

        Uses Azure REST API version 2023-09-01. In version 2.x of the Azure Native provider, it used API version 2020-08-01.

        Other available API versions: 2019-08-01-preview, 2020-03-01-preview, 2020-08-01, 2025-02-01. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native operationalinsights [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.

        :param str resource_name: The name of the resource.
        :param DataExportArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DataExportArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 created_date: Optional[pulumi.Input[builtins.str]] = None,
                 data_export_id: Optional[pulumi.Input[builtins.str]] = None,
                 data_export_name: Optional[pulumi.Input[builtins.str]] = None,
                 enable: Optional[pulumi.Input[builtins.bool]] = None,
                 event_hub_name: Optional[pulumi.Input[builtins.str]] = None,
                 last_modified_date: Optional[pulumi.Input[builtins.str]] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 resource_id: Optional[pulumi.Input[builtins.str]] = None,
                 table_names: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 workspace_name: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DataExportArgs.__new__(DataExportArgs)

            __props__.__dict__["created_date"] = created_date
            __props__.__dict__["data_export_id"] = data_export_id
            __props__.__dict__["data_export_name"] = data_export_name
            __props__.__dict__["enable"] = enable
            __props__.__dict__["event_hub_name"] = event_hub_name
            __props__.__dict__["last_modified_date"] = last_modified_date
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'resource_id'")
            __props__.__dict__["resource_id"] = resource_id
            if table_names is None and not opts.urn:
                raise TypeError("Missing required property 'table_names'")
            __props__.__dict__["table_names"] = table_names
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["azure_api_version"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:operationalinsights/v20190801preview:DataExport"), pulumi.Alias(type_="azure-native:operationalinsights/v20200301preview:DataExport"), pulumi.Alias(type_="azure-native:operationalinsights/v20200801:DataExport"), pulumi.Alias(type_="azure-native:operationalinsights/v20230901:DataExport"), pulumi.Alias(type_="azure-native:operationalinsights/v20250201:DataExport")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DataExport, __self__).__init__(
            'azure-native:operationalinsights:DataExport',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DataExport':
        """
        Get an existing DataExport resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DataExportArgs.__new__(DataExportArgs)

        __props__.__dict__["azure_api_version"] = None
        __props__.__dict__["created_date"] = None
        __props__.__dict__["data_export_id"] = None
        __props__.__dict__["enable"] = None
        __props__.__dict__["event_hub_name"] = None
        __props__.__dict__["last_modified_date"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["resource_id"] = None
        __props__.__dict__["table_names"] = None
        __props__.__dict__["type"] = None
        return DataExport(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[builtins.str]:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The latest data export rule modification time.
        """
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter(name="dataExportId")
    def data_export_id(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The data export rule ID.
        """
        return pulumi.get(self, "data_export_id")

    @property
    @pulumi.getter
    def enable(self) -> pulumi.Output[Optional[builtins.bool]]:
        """
        Active when enabled.
        """
        return pulumi.get(self, "enable")

    @property
    @pulumi.getter(name="eventHubName")
    def event_hub_name(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        Optional. Allows to define an Event Hub name. Not applicable when destination is Storage Account.
        """
        return pulumi.get(self, "event_hub_name")

    @property
    @pulumi.getter(name="lastModifiedDate")
    def last_modified_date(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        Date and time when the export was last modified.
        """
        return pulumi.get(self, "last_modified_date")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[builtins.str]:
        """
        The destination resource ID. This can be copied from the Properties entry of the destination resource in Azure.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="tableNames")
    def table_names(self) -> pulumi.Output[Sequence[builtins.str]]:
        """
        An array of tables to export, for example: [“Heartbeat, SecurityEvent”].
        """
        return pulumi.get(self, "table_names")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[builtins.str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

