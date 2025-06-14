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

__all__ = ['VdmAttributesArgs', 'VdmAttributes']

@pulumi.input_type
class VdmAttributesArgs:
    def __init__(__self__, *,
                 dashboard_attributes: Optional[pulumi.Input['VdmAttributesDashboardAttributesArgs']] = None,
                 guardian_attributes: Optional[pulumi.Input['VdmAttributesGuardianAttributesArgs']] = None):
        """
        The set of arguments for constructing a VdmAttributes resource.
        :param pulumi.Input['VdmAttributesDashboardAttributesArgs'] dashboard_attributes: Specifies additional settings for your VDM configuration as applicable to the Dashboard.
        :param pulumi.Input['VdmAttributesGuardianAttributesArgs'] guardian_attributes: Specifies additional settings for your VDM configuration as applicable to the Guardian.
        """
        if dashboard_attributes is not None:
            pulumi.set(__self__, "dashboard_attributes", dashboard_attributes)
        if guardian_attributes is not None:
            pulumi.set(__self__, "guardian_attributes", guardian_attributes)

    @property
    @pulumi.getter(name="dashboardAttributes")
    def dashboard_attributes(self) -> Optional[pulumi.Input['VdmAttributesDashboardAttributesArgs']]:
        """
        Specifies additional settings for your VDM configuration as applicable to the Dashboard.
        """
        return pulumi.get(self, "dashboard_attributes")

    @dashboard_attributes.setter
    def dashboard_attributes(self, value: Optional[pulumi.Input['VdmAttributesDashboardAttributesArgs']]):
        pulumi.set(self, "dashboard_attributes", value)

    @property
    @pulumi.getter(name="guardianAttributes")
    def guardian_attributes(self) -> Optional[pulumi.Input['VdmAttributesGuardianAttributesArgs']]:
        """
        Specifies additional settings for your VDM configuration as applicable to the Guardian.
        """
        return pulumi.get(self, "guardian_attributes")

    @guardian_attributes.setter
    def guardian_attributes(self, value: Optional[pulumi.Input['VdmAttributesGuardianAttributesArgs']]):
        pulumi.set(self, "guardian_attributes", value)


@pulumi.type_token("aws-native:ses:VdmAttributes")
class VdmAttributes(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dashboard_attributes: Optional[pulumi.Input[Union['VdmAttributesDashboardAttributesArgs', 'VdmAttributesDashboardAttributesArgsDict']]] = None,
                 guardian_attributes: Optional[pulumi.Input[Union['VdmAttributesGuardianAttributesArgs', 'VdmAttributesGuardianAttributesArgsDict']]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::SES::VdmAttributes

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['VdmAttributesDashboardAttributesArgs', 'VdmAttributesDashboardAttributesArgsDict']] dashboard_attributes: Specifies additional settings for your VDM configuration as applicable to the Dashboard.
        :param pulumi.Input[Union['VdmAttributesGuardianAttributesArgs', 'VdmAttributesGuardianAttributesArgsDict']] guardian_attributes: Specifies additional settings for your VDM configuration as applicable to the Guardian.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[VdmAttributesArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::SES::VdmAttributes

        :param str resource_name: The name of the resource.
        :param VdmAttributesArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VdmAttributesArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dashboard_attributes: Optional[pulumi.Input[Union['VdmAttributesDashboardAttributesArgs', 'VdmAttributesDashboardAttributesArgsDict']]] = None,
                 guardian_attributes: Optional[pulumi.Input[Union['VdmAttributesGuardianAttributesArgs', 'VdmAttributesGuardianAttributesArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VdmAttributesArgs.__new__(VdmAttributesArgs)

            __props__.__dict__["dashboard_attributes"] = dashboard_attributes
            __props__.__dict__["guardian_attributes"] = guardian_attributes
            __props__.__dict__["vdm_attributes_resource_id"] = None
        super(VdmAttributes, __self__).__init__(
            'aws-native:ses:VdmAttributes',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VdmAttributes':
        """
        Get an existing VdmAttributes resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VdmAttributesArgs.__new__(VdmAttributesArgs)

        __props__.__dict__["dashboard_attributes"] = None
        __props__.__dict__["guardian_attributes"] = None
        __props__.__dict__["vdm_attributes_resource_id"] = None
        return VdmAttributes(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dashboardAttributes")
    def dashboard_attributes(self) -> pulumi.Output[Optional['outputs.VdmAttributesDashboardAttributes']]:
        """
        Specifies additional settings for your VDM configuration as applicable to the Dashboard.
        """
        return pulumi.get(self, "dashboard_attributes")

    @property
    @pulumi.getter(name="guardianAttributes")
    def guardian_attributes(self) -> pulumi.Output[Optional['outputs.VdmAttributesGuardianAttributes']]:
        """
        Specifies additional settings for your VDM configuration as applicable to the Guardian.
        """
        return pulumi.get(self, "guardian_attributes")

    @property
    @pulumi.getter(name="vdmAttributesResourceId")
    def vdm_attributes_resource_id(self) -> pulumi.Output[builtins.str]:
        """
        Unique identifier for this resource
        """
        return pulumi.get(self, "vdm_attributes_resource_id")

