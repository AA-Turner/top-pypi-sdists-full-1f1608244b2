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
from ._inputs import *

__all__ = ['IscsiTargetArgs', 'IscsiTarget']

@pulumi.input_type
class IscsiTargetArgs:
    def __init__(__self__, *,
                 acl_mode: pulumi.Input[Union[builtins.str, 'IscsiTargetAclMode']],
                 disk_pool_name: pulumi.Input[builtins.str],
                 resource_group_name: pulumi.Input[builtins.str],
                 iscsi_target_name: Optional[pulumi.Input[builtins.str]] = None,
                 luns: Optional[pulumi.Input[Sequence[pulumi.Input['IscsiLunArgs']]]] = None,
                 managed_by: Optional[pulumi.Input[builtins.str]] = None,
                 managed_by_extended: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 static_acls: Optional[pulumi.Input[Sequence[pulumi.Input['AclArgs']]]] = None,
                 target_iqn: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a IscsiTarget resource.
        :param pulumi.Input[Union[builtins.str, 'IscsiTargetAclMode']] acl_mode: Mode for Target connectivity.
        :param pulumi.Input[builtins.str] disk_pool_name: The name of the Disk Pool.
        :param pulumi.Input[builtins.str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[builtins.str] iscsi_target_name: The name of the iSCSI Target.
        :param pulumi.Input[Sequence[pulumi.Input['IscsiLunArgs']]] luns: List of LUNs to be exposed through iSCSI Target.
        :param pulumi.Input[builtins.str] managed_by: Azure resource id. Indicates if this resource is managed by another Azure resource.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] managed_by_extended: List of Azure resource ids that manage this resource.
        :param pulumi.Input[Sequence[pulumi.Input['AclArgs']]] static_acls: Access Control List (ACL) for an iSCSI Target; defines LUN masking policy
        :param pulumi.Input[builtins.str] target_iqn: iSCSI Target IQN (iSCSI Qualified Name); example: "iqn.2005-03.org.iscsi:server".
        """
        pulumi.set(__self__, "acl_mode", acl_mode)
        pulumi.set(__self__, "disk_pool_name", disk_pool_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if iscsi_target_name is not None:
            pulumi.set(__self__, "iscsi_target_name", iscsi_target_name)
        if luns is not None:
            pulumi.set(__self__, "luns", luns)
        if managed_by is not None:
            pulumi.set(__self__, "managed_by", managed_by)
        if managed_by_extended is not None:
            pulumi.set(__self__, "managed_by_extended", managed_by_extended)
        if static_acls is not None:
            pulumi.set(__self__, "static_acls", static_acls)
        if target_iqn is not None:
            pulumi.set(__self__, "target_iqn", target_iqn)

    @property
    @pulumi.getter(name="aclMode")
    def acl_mode(self) -> pulumi.Input[Union[builtins.str, 'IscsiTargetAclMode']]:
        """
        Mode for Target connectivity.
        """
        return pulumi.get(self, "acl_mode")

    @acl_mode.setter
    def acl_mode(self, value: pulumi.Input[Union[builtins.str, 'IscsiTargetAclMode']]):
        pulumi.set(self, "acl_mode", value)

    @property
    @pulumi.getter(name="diskPoolName")
    def disk_pool_name(self) -> pulumi.Input[builtins.str]:
        """
        The name of the Disk Pool.
        """
        return pulumi.get(self, "disk_pool_name")

    @disk_pool_name.setter
    def disk_pool_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "disk_pool_name", value)

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
    @pulumi.getter(name="iscsiTargetName")
    def iscsi_target_name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the iSCSI Target.
        """
        return pulumi.get(self, "iscsi_target_name")

    @iscsi_target_name.setter
    def iscsi_target_name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "iscsi_target_name", value)

    @property
    @pulumi.getter
    def luns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IscsiLunArgs']]]]:
        """
        List of LUNs to be exposed through iSCSI Target.
        """
        return pulumi.get(self, "luns")

    @luns.setter
    def luns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IscsiLunArgs']]]]):
        pulumi.set(self, "luns", value)

    @property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Azure resource id. Indicates if this resource is managed by another Azure resource.
        """
        return pulumi.get(self, "managed_by")

    @managed_by.setter
    def managed_by(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "managed_by", value)

    @property
    @pulumi.getter(name="managedByExtended")
    def managed_by_extended(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]:
        """
        List of Azure resource ids that manage this resource.
        """
        return pulumi.get(self, "managed_by_extended")

    @managed_by_extended.setter
    def managed_by_extended(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "managed_by_extended", value)

    @property
    @pulumi.getter(name="staticAcls")
    def static_acls(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AclArgs']]]]:
        """
        Access Control List (ACL) for an iSCSI Target; defines LUN masking policy
        """
        return pulumi.get(self, "static_acls")

    @static_acls.setter
    def static_acls(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AclArgs']]]]):
        pulumi.set(self, "static_acls", value)

    @property
    @pulumi.getter(name="targetIqn")
    def target_iqn(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        iSCSI Target IQN (iSCSI Qualified Name); example: "iqn.2005-03.org.iscsi:server".
        """
        return pulumi.get(self, "target_iqn")

    @target_iqn.setter
    def target_iqn(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "target_iqn", value)


@pulumi.type_token("azure-native:storagepool:IscsiTarget")
class IscsiTarget(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 acl_mode: Optional[pulumi.Input[Union[builtins.str, 'IscsiTargetAclMode']]] = None,
                 disk_pool_name: Optional[pulumi.Input[builtins.str]] = None,
                 iscsi_target_name: Optional[pulumi.Input[builtins.str]] = None,
                 luns: Optional[pulumi.Input[Sequence[pulumi.Input[Union['IscsiLunArgs', 'IscsiLunArgsDict']]]]] = None,
                 managed_by: Optional[pulumi.Input[builtins.str]] = None,
                 managed_by_extended: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 static_acls: Optional[pulumi.Input[Sequence[pulumi.Input[Union['AclArgs', 'AclArgsDict']]]]] = None,
                 target_iqn: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        Response for iSCSI Target requests.

        Uses Azure REST API version 2021-08-01. In version 2.x of the Azure Native provider, it used API version 2021-08-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[builtins.str, 'IscsiTargetAclMode']] acl_mode: Mode for Target connectivity.
        :param pulumi.Input[builtins.str] disk_pool_name: The name of the Disk Pool.
        :param pulumi.Input[builtins.str] iscsi_target_name: The name of the iSCSI Target.
        :param pulumi.Input[Sequence[pulumi.Input[Union['IscsiLunArgs', 'IscsiLunArgsDict']]]] luns: List of LUNs to be exposed through iSCSI Target.
        :param pulumi.Input[builtins.str] managed_by: Azure resource id. Indicates if this resource is managed by another Azure resource.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] managed_by_extended: List of Azure resource ids that manage this resource.
        :param pulumi.Input[builtins.str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[Union['AclArgs', 'AclArgsDict']]]] static_acls: Access Control List (ACL) for an iSCSI Target; defines LUN masking policy
        :param pulumi.Input[builtins.str] target_iqn: iSCSI Target IQN (iSCSI Qualified Name); example: "iqn.2005-03.org.iscsi:server".
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IscsiTargetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Response for iSCSI Target requests.

        Uses Azure REST API version 2021-08-01. In version 2.x of the Azure Native provider, it used API version 2021-08-01.

        :param str resource_name: The name of the resource.
        :param IscsiTargetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IscsiTargetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 acl_mode: Optional[pulumi.Input[Union[builtins.str, 'IscsiTargetAclMode']]] = None,
                 disk_pool_name: Optional[pulumi.Input[builtins.str]] = None,
                 iscsi_target_name: Optional[pulumi.Input[builtins.str]] = None,
                 luns: Optional[pulumi.Input[Sequence[pulumi.Input[Union['IscsiLunArgs', 'IscsiLunArgsDict']]]]] = None,
                 managed_by: Optional[pulumi.Input[builtins.str]] = None,
                 managed_by_extended: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                 static_acls: Optional[pulumi.Input[Sequence[pulumi.Input[Union['AclArgs', 'AclArgsDict']]]]] = None,
                 target_iqn: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IscsiTargetArgs.__new__(IscsiTargetArgs)

            if acl_mode is None and not opts.urn:
                raise TypeError("Missing required property 'acl_mode'")
            __props__.__dict__["acl_mode"] = acl_mode
            if disk_pool_name is None and not opts.urn:
                raise TypeError("Missing required property 'disk_pool_name'")
            __props__.__dict__["disk_pool_name"] = disk_pool_name
            __props__.__dict__["iscsi_target_name"] = iscsi_target_name
            __props__.__dict__["luns"] = luns
            __props__.__dict__["managed_by"] = managed_by
            __props__.__dict__["managed_by_extended"] = managed_by_extended
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["static_acls"] = static_acls
            __props__.__dict__["target_iqn"] = target_iqn
            __props__.__dict__["azure_api_version"] = None
            __props__.__dict__["endpoints"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["port"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["sessions"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:storagepool/v20200315preview:IscsiTarget"), pulumi.Alias(type_="azure-native:storagepool/v20210401preview:IscsiTarget"), pulumi.Alias(type_="azure-native:storagepool/v20210801:IscsiTarget")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(IscsiTarget, __self__).__init__(
            'azure-native:storagepool:IscsiTarget',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IscsiTarget':
        """
        Get an existing IscsiTarget resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IscsiTargetArgs.__new__(IscsiTargetArgs)

        __props__.__dict__["acl_mode"] = None
        __props__.__dict__["azure_api_version"] = None
        __props__.__dict__["endpoints"] = None
        __props__.__dict__["luns"] = None
        __props__.__dict__["managed_by"] = None
        __props__.__dict__["managed_by_extended"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["port"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["sessions"] = None
        __props__.__dict__["static_acls"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["target_iqn"] = None
        __props__.__dict__["type"] = None
        return IscsiTarget(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="aclMode")
    def acl_mode(self) -> pulumi.Output[builtins.str]:
        """
        Mode for Target connectivity.
        """
        return pulumi.get(self, "acl_mode")

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[builtins.str]:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter
    def endpoints(self) -> pulumi.Output[Optional[Sequence[builtins.str]]]:
        """
        List of private IPv4 addresses to connect to the iSCSI Target.
        """
        return pulumi.get(self, "endpoints")

    @property
    @pulumi.getter
    def luns(self) -> pulumi.Output[Optional[Sequence['outputs.IscsiLunResponse']]]:
        """
        List of LUNs to be exposed through iSCSI Target.
        """
        return pulumi.get(self, "luns")

    @property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> pulumi.Output[builtins.str]:
        """
        Azure resource id. Indicates if this resource is managed by another Azure resource.
        """
        return pulumi.get(self, "managed_by")

    @property
    @pulumi.getter(name="managedByExtended")
    def managed_by_extended(self) -> pulumi.Output[Sequence[builtins.str]]:
        """
        List of Azure resource ids that manage this resource.
        """
        return pulumi.get(self, "managed_by_extended")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[Optional[builtins.int]]:
        """
        The port used by iSCSI Target portal group.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[builtins.str]:
        """
        State of the operation on the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sessions(self) -> pulumi.Output[Sequence[builtins.str]]:
        """
        List of identifiers for active sessions on the iSCSI target
        """
        return pulumi.get(self, "sessions")

    @property
    @pulumi.getter(name="staticAcls")
    def static_acls(self) -> pulumi.Output[Optional[Sequence['outputs.AclResponse']]]:
        """
        Access Control List (ACL) for an iSCSI Target; defines LUN masking policy
        """
        return pulumi.get(self, "static_acls")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[builtins.str]:
        """
        Operational status of the iSCSI Target.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemMetadataResponse']:
        """
        Resource metadata required by ARM RPC
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="targetIqn")
    def target_iqn(self) -> pulumi.Output[builtins.str]:
        """
        iSCSI Target IQN (iSCSI Qualified Name); example: "iqn.2005-03.org.iscsi:server".
        """
        return pulumi.get(self, "target_iqn")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[builtins.str]:
        """
        The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
        """
        return pulumi.get(self, "type")

