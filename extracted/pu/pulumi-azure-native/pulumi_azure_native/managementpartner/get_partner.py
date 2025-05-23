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
    'GetPartnerResult',
    'AwaitableGetPartnerResult',
    'get_partner',
    'get_partner_output',
]

@pulumi.output_type
class GetPartnerResult:
    """
    this is the management partner operations response
    """
    def __init__(__self__, azure_api_version=None, created_time=None, etag=None, id=None, name=None, object_id=None, partner_id=None, partner_name=None, tenant_id=None, type=None, updated_time=None, version=None):
        if azure_api_version and not isinstance(azure_api_version, str):
            raise TypeError("Expected argument 'azure_api_version' to be a str")
        pulumi.set(__self__, "azure_api_version", azure_api_version)
        if created_time and not isinstance(created_time, str):
            raise TypeError("Expected argument 'created_time' to be a str")
        pulumi.set(__self__, "created_time", created_time)
        if etag and not isinstance(etag, int):
            raise TypeError("Expected argument 'etag' to be a int")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if object_id and not isinstance(object_id, str):
            raise TypeError("Expected argument 'object_id' to be a str")
        pulumi.set(__self__, "object_id", object_id)
        if partner_id and not isinstance(partner_id, str):
            raise TypeError("Expected argument 'partner_id' to be a str")
        pulumi.set(__self__, "partner_id", partner_id)
        if partner_name and not isinstance(partner_name, str):
            raise TypeError("Expected argument 'partner_name' to be a str")
        pulumi.set(__self__, "partner_name", partner_name)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if updated_time and not isinstance(updated_time, str):
            raise TypeError("Expected argument 'updated_time' to be a str")
        pulumi.set(__self__, "updated_time", updated_time)
        if version and not isinstance(version, int):
            raise TypeError("Expected argument 'version' to be a int")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> builtins.str:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[builtins.str]:
        """
        This is the DateTime when the partner was created.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter
    def etag(self) -> Optional[builtins.int]:
        """
        Type of the partner
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        """
        Identifier of the partner
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> builtins.str:
        """
        Name of the partner
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[builtins.str]:
        """
        This is the object id.
        """
        return pulumi.get(self, "object_id")

    @property
    @pulumi.getter(name="partnerId")
    def partner_id(self) -> Optional[builtins.str]:
        """
        This is the partner id
        """
        return pulumi.get(self, "partner_id")

    @property
    @pulumi.getter(name="partnerName")
    def partner_name(self) -> Optional[builtins.str]:
        """
        This is the partner name
        """
        return pulumi.get(self, "partner_name")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[builtins.str]:
        """
        This is the tenant id.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> builtins.str:
        """
        Type of resource. "Microsoft.ManagementPartner/partners"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedTime")
    def updated_time(self) -> Optional[builtins.str]:
        """
        This is the DateTime when the partner was updated.
        """
        return pulumi.get(self, "updated_time")

    @property
    @pulumi.getter
    def version(self) -> Optional[builtins.int]:
        """
        This is the version.
        """
        return pulumi.get(self, "version")


class AwaitableGetPartnerResult(GetPartnerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPartnerResult(
            azure_api_version=self.azure_api_version,
            created_time=self.created_time,
            etag=self.etag,
            id=self.id,
            name=self.name,
            object_id=self.object_id,
            partner_id=self.partner_id,
            partner_name=self.partner_name,
            tenant_id=self.tenant_id,
            type=self.type,
            updated_time=self.updated_time,
            version=self.version)


def get_partner(partner_id: Optional[builtins.str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPartnerResult:
    """
    Get the management partner using the partnerId, objectId and tenantId.

    Uses Azure REST API version 2018-02-01.


    :param builtins.str partner_id: Id of the Partner
    """
    __args__ = dict()
    __args__['partnerId'] = partner_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:managementpartner:getPartner', __args__, opts=opts, typ=GetPartnerResult).value

    return AwaitableGetPartnerResult(
        azure_api_version=pulumi.get(__ret__, 'azure_api_version'),
        created_time=pulumi.get(__ret__, 'created_time'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        object_id=pulumi.get(__ret__, 'object_id'),
        partner_id=pulumi.get(__ret__, 'partner_id'),
        partner_name=pulumi.get(__ret__, 'partner_name'),
        tenant_id=pulumi.get(__ret__, 'tenant_id'),
        type=pulumi.get(__ret__, 'type'),
        updated_time=pulumi.get(__ret__, 'updated_time'),
        version=pulumi.get(__ret__, 'version'))
def get_partner_output(partner_id: Optional[pulumi.Input[builtins.str]] = None,
                       opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetPartnerResult]:
    """
    Get the management partner using the partnerId, objectId and tenantId.

    Uses Azure REST API version 2018-02-01.


    :param builtins.str partner_id: Id of the Partner
    """
    __args__ = dict()
    __args__['partnerId'] = partner_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('azure-native:managementpartner:getPartner', __args__, opts=opts, typ=GetPartnerResult)
    return __ret__.apply(lambda __response__: GetPartnerResult(
        azure_api_version=pulumi.get(__response__, 'azure_api_version'),
        created_time=pulumi.get(__response__, 'created_time'),
        etag=pulumi.get(__response__, 'etag'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        object_id=pulumi.get(__response__, 'object_id'),
        partner_id=pulumi.get(__response__, 'partner_id'),
        partner_name=pulumi.get(__response__, 'partner_name'),
        tenant_id=pulumi.get(__response__, 'tenant_id'),
        type=pulumi.get(__response__, 'type'),
        updated_time=pulumi.get(__response__, 'updated_time'),
        version=pulumi.get(__response__, 'version')))
