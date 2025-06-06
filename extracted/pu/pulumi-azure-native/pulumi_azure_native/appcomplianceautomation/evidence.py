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
from ._enums import *

__all__ = ['EvidenceArgs', 'Evidence']

@pulumi.input_type
class EvidenceArgs:
    def __init__(__self__, *,
                 file_path: pulumi.Input[builtins.str],
                 report_name: pulumi.Input[builtins.str],
                 control_id: Optional[pulumi.Input[builtins.str]] = None,
                 evidence_name: Optional[pulumi.Input[builtins.str]] = None,
                 evidence_type: Optional[pulumi.Input[Union[builtins.str, 'EvidenceType']]] = None,
                 extra_data: Optional[pulumi.Input[builtins.str]] = None,
                 offer_guid: Optional[pulumi.Input[builtins.str]] = None,
                 report_creator_tenant_id: Optional[pulumi.Input[builtins.str]] = None,
                 responsibility_id: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a Evidence resource.
        :param pulumi.Input[builtins.str] file_path: The path of the file in storage.
        :param pulumi.Input[builtins.str] report_name: Report Name.
        :param pulumi.Input[builtins.str] control_id: Control id.
        :param pulumi.Input[builtins.str] evidence_name: The evidence name.
        :param pulumi.Input[Union[builtins.str, 'EvidenceType']] evidence_type: Evidence type.
        :param pulumi.Input[builtins.str] extra_data: Extra data considered as evidence.
        :param pulumi.Input[builtins.str] offer_guid: The offerGuid which mapping to the reports.
        :param pulumi.Input[builtins.str] report_creator_tenant_id: The tenant id of the report creator.
        :param pulumi.Input[builtins.str] responsibility_id: Responsibility id.
        """
        pulumi.set(__self__, "file_path", file_path)
        pulumi.set(__self__, "report_name", report_name)
        if control_id is not None:
            pulumi.set(__self__, "control_id", control_id)
        if evidence_name is not None:
            pulumi.set(__self__, "evidence_name", evidence_name)
        if evidence_type is not None:
            pulumi.set(__self__, "evidence_type", evidence_type)
        if extra_data is not None:
            pulumi.set(__self__, "extra_data", extra_data)
        if offer_guid is not None:
            pulumi.set(__self__, "offer_guid", offer_guid)
        if report_creator_tenant_id is not None:
            pulumi.set(__self__, "report_creator_tenant_id", report_creator_tenant_id)
        if responsibility_id is not None:
            pulumi.set(__self__, "responsibility_id", responsibility_id)

    @property
    @pulumi.getter(name="filePath")
    def file_path(self) -> pulumi.Input[builtins.str]:
        """
        The path of the file in storage.
        """
        return pulumi.get(self, "file_path")

    @file_path.setter
    def file_path(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "file_path", value)

    @property
    @pulumi.getter(name="reportName")
    def report_name(self) -> pulumi.Input[builtins.str]:
        """
        Report Name.
        """
        return pulumi.get(self, "report_name")

    @report_name.setter
    def report_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "report_name", value)

    @property
    @pulumi.getter(name="controlId")
    def control_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Control id.
        """
        return pulumi.get(self, "control_id")

    @control_id.setter
    def control_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "control_id", value)

    @property
    @pulumi.getter(name="evidenceName")
    def evidence_name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The evidence name.
        """
        return pulumi.get(self, "evidence_name")

    @evidence_name.setter
    def evidence_name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "evidence_name", value)

    @property
    @pulumi.getter(name="evidenceType")
    def evidence_type(self) -> Optional[pulumi.Input[Union[builtins.str, 'EvidenceType']]]:
        """
        Evidence type.
        """
        return pulumi.get(self, "evidence_type")

    @evidence_type.setter
    def evidence_type(self, value: Optional[pulumi.Input[Union[builtins.str, 'EvidenceType']]]):
        pulumi.set(self, "evidence_type", value)

    @property
    @pulumi.getter(name="extraData")
    def extra_data(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Extra data considered as evidence.
        """
        return pulumi.get(self, "extra_data")

    @extra_data.setter
    def extra_data(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "extra_data", value)

    @property
    @pulumi.getter(name="offerGuid")
    def offer_guid(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The offerGuid which mapping to the reports.
        """
        return pulumi.get(self, "offer_guid")

    @offer_guid.setter
    def offer_guid(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "offer_guid", value)

    @property
    @pulumi.getter(name="reportCreatorTenantId")
    def report_creator_tenant_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The tenant id of the report creator.
        """
        return pulumi.get(self, "report_creator_tenant_id")

    @report_creator_tenant_id.setter
    def report_creator_tenant_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "report_creator_tenant_id", value)

    @property
    @pulumi.getter(name="responsibilityId")
    def responsibility_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Responsibility id.
        """
        return pulumi.get(self, "responsibility_id")

    @responsibility_id.setter
    def responsibility_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "responsibility_id", value)


@pulumi.type_token("azure-native:appcomplianceautomation:Evidence")
class Evidence(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 control_id: Optional[pulumi.Input[builtins.str]] = None,
                 evidence_name: Optional[pulumi.Input[builtins.str]] = None,
                 evidence_type: Optional[pulumi.Input[Union[builtins.str, 'EvidenceType']]] = None,
                 extra_data: Optional[pulumi.Input[builtins.str]] = None,
                 file_path: Optional[pulumi.Input[builtins.str]] = None,
                 offer_guid: Optional[pulumi.Input[builtins.str]] = None,
                 report_creator_tenant_id: Optional[pulumi.Input[builtins.str]] = None,
                 report_name: Optional[pulumi.Input[builtins.str]] = None,
                 responsibility_id: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        A class represent an AppComplianceAutomation evidence resource.

        Uses Azure REST API version 2024-06-27. In version 2.x of the Azure Native provider, it used API version 2024-06-27.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] control_id: Control id.
        :param pulumi.Input[builtins.str] evidence_name: The evidence name.
        :param pulumi.Input[Union[builtins.str, 'EvidenceType']] evidence_type: Evidence type.
        :param pulumi.Input[builtins.str] extra_data: Extra data considered as evidence.
        :param pulumi.Input[builtins.str] file_path: The path of the file in storage.
        :param pulumi.Input[builtins.str] offer_guid: The offerGuid which mapping to the reports.
        :param pulumi.Input[builtins.str] report_creator_tenant_id: The tenant id of the report creator.
        :param pulumi.Input[builtins.str] report_name: Report Name.
        :param pulumi.Input[builtins.str] responsibility_id: Responsibility id.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EvidenceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A class represent an AppComplianceAutomation evidence resource.

        Uses Azure REST API version 2024-06-27. In version 2.x of the Azure Native provider, it used API version 2024-06-27.

        :param str resource_name: The name of the resource.
        :param EvidenceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EvidenceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 control_id: Optional[pulumi.Input[builtins.str]] = None,
                 evidence_name: Optional[pulumi.Input[builtins.str]] = None,
                 evidence_type: Optional[pulumi.Input[Union[builtins.str, 'EvidenceType']]] = None,
                 extra_data: Optional[pulumi.Input[builtins.str]] = None,
                 file_path: Optional[pulumi.Input[builtins.str]] = None,
                 offer_guid: Optional[pulumi.Input[builtins.str]] = None,
                 report_creator_tenant_id: Optional[pulumi.Input[builtins.str]] = None,
                 report_name: Optional[pulumi.Input[builtins.str]] = None,
                 responsibility_id: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EvidenceArgs.__new__(EvidenceArgs)

            __props__.__dict__["control_id"] = control_id
            __props__.__dict__["evidence_name"] = evidence_name
            __props__.__dict__["evidence_type"] = evidence_type
            __props__.__dict__["extra_data"] = extra_data
            if file_path is None and not opts.urn:
                raise TypeError("Missing required property 'file_path'")
            __props__.__dict__["file_path"] = file_path
            __props__.__dict__["offer_guid"] = offer_guid
            __props__.__dict__["report_creator_tenant_id"] = report_creator_tenant_id
            if report_name is None and not opts.urn:
                raise TypeError("Missing required property 'report_name'")
            __props__.__dict__["report_name"] = report_name
            __props__.__dict__["responsibility_id"] = responsibility_id
            __props__.__dict__["azure_api_version"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:appcomplianceautomation/v20240627:Evidence")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Evidence, __self__).__init__(
            'azure-native:appcomplianceautomation:Evidence',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Evidence':
        """
        Get an existing Evidence resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EvidenceArgs.__new__(EvidenceArgs)

        __props__.__dict__["azure_api_version"] = None
        __props__.__dict__["control_id"] = None
        __props__.__dict__["evidence_type"] = None
        __props__.__dict__["extra_data"] = None
        __props__.__dict__["file_path"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["responsibility_id"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return Evidence(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[builtins.str]:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter(name="controlId")
    def control_id(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        Control id.
        """
        return pulumi.get(self, "control_id")

    @property
    @pulumi.getter(name="evidenceType")
    def evidence_type(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        Evidence type.
        """
        return pulumi.get(self, "evidence_type")

    @property
    @pulumi.getter(name="extraData")
    def extra_data(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        Extra data considered as evidence.
        """
        return pulumi.get(self, "extra_data")

    @property
    @pulumi.getter(name="filePath")
    def file_path(self) -> pulumi.Output[builtins.str]:
        """
        The path of the file in storage.
        """
        return pulumi.get(self, "file_path")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[builtins.str]:
        """
        Azure lifecycle management
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="responsibilityId")
    def responsibility_id(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        Responsibility id.
        """
        return pulumi.get(self, "responsibility_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[builtins.str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

