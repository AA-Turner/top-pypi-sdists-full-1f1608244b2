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
    'GetKustoDatabaseDataSetResult',
    'AwaitableGetKustoDatabaseDataSetResult',
    'get_kusto_database_data_set',
    'get_kusto_database_data_set_output',
]

@pulumi.output_type
class GetKustoDatabaseDataSetResult:
    """
    A kusto database data set.
    """
    def __init__(__self__, azure_api_version=None, data_set_id=None, id=None, kind=None, kusto_database_resource_id=None, location=None, name=None, provisioning_state=None, system_data=None, type=None):
        if azure_api_version and not isinstance(azure_api_version, str):
            raise TypeError("Expected argument 'azure_api_version' to be a str")
        pulumi.set(__self__, "azure_api_version", azure_api_version)
        if data_set_id and not isinstance(data_set_id, str):
            raise TypeError("Expected argument 'data_set_id' to be a str")
        pulumi.set(__self__, "data_set_id", data_set_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if kusto_database_resource_id and not isinstance(kusto_database_resource_id, str):
            raise TypeError("Expected argument 'kusto_database_resource_id' to be a str")
        pulumi.set(__self__, "kusto_database_resource_id", kusto_database_resource_id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> builtins.str:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> builtins.str:
        """
        Unique id for identifying a data set resource
        """
        return pulumi.get(self, "data_set_id")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        """
        The resource id of the azure resource
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> builtins.str:
        """
        Kind of data set.
        Expected value is 'KustoDatabase'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="kustoDatabaseResourceId")
    def kusto_database_resource_id(self) -> builtins.str:
        """
        Resource id of the kusto database.
        """
        return pulumi.get(self, "kusto_database_resource_id")

    @property
    @pulumi.getter
    def location(self) -> builtins.str:
        """
        Location of the kusto cluster.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> builtins.str:
        """
        Name of the azure resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> builtins.str:
        """
        Provisioning state of the kusto database data set.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        System Data of the Azure resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> builtins.str:
        """
        Type of the azure resource
        """
        return pulumi.get(self, "type")


class AwaitableGetKustoDatabaseDataSetResult(GetKustoDatabaseDataSetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKustoDatabaseDataSetResult(
            azure_api_version=self.azure_api_version,
            data_set_id=self.data_set_id,
            id=self.id,
            kind=self.kind,
            kusto_database_resource_id=self.kusto_database_resource_id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_kusto_database_data_set(account_name: Optional[builtins.str] = None,
                                data_set_name: Optional[builtins.str] = None,
                                resource_group_name: Optional[builtins.str] = None,
                                share_name: Optional[builtins.str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKustoDatabaseDataSetResult:
    """
    Get a DataSet in a share

    Uses Azure REST API version 2021-08-01.


    :param builtins.str account_name: The name of the share account.
    :param builtins.str data_set_name: The name of the dataSet.
    :param builtins.str resource_group_name: The resource group name.
    :param builtins.str share_name: The name of the share.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['dataSetName'] = data_set_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['shareName'] = share_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:datashare:getKustoDatabaseDataSet', __args__, opts=opts, typ=GetKustoDatabaseDataSetResult).value

    return AwaitableGetKustoDatabaseDataSetResult(
        azure_api_version=pulumi.get(__ret__, 'azure_api_version'),
        data_set_id=pulumi.get(__ret__, 'data_set_id'),
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        kusto_database_resource_id=pulumi.get(__ret__, 'kusto_database_resource_id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))
def get_kusto_database_data_set_output(account_name: Optional[pulumi.Input[builtins.str]] = None,
                                       data_set_name: Optional[pulumi.Input[builtins.str]] = None,
                                       resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                                       share_name: Optional[pulumi.Input[builtins.str]] = None,
                                       opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetKustoDatabaseDataSetResult]:
    """
    Get a DataSet in a share

    Uses Azure REST API version 2021-08-01.


    :param builtins.str account_name: The name of the share account.
    :param builtins.str data_set_name: The name of the dataSet.
    :param builtins.str resource_group_name: The resource group name.
    :param builtins.str share_name: The name of the share.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['dataSetName'] = data_set_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['shareName'] = share_name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('azure-native:datashare:getKustoDatabaseDataSet', __args__, opts=opts, typ=GetKustoDatabaseDataSetResult)
    return __ret__.apply(lambda __response__: GetKustoDatabaseDataSetResult(
        azure_api_version=pulumi.get(__response__, 'azure_api_version'),
        data_set_id=pulumi.get(__response__, 'data_set_id'),
        id=pulumi.get(__response__, 'id'),
        kind=pulumi.get(__response__, 'kind'),
        kusto_database_resource_id=pulumi.get(__response__, 'kusto_database_resource_id'),
        location=pulumi.get(__response__, 'location'),
        name=pulumi.get(__response__, 'name'),
        provisioning_state=pulumi.get(__response__, 'provisioning_state'),
        system_data=pulumi.get(__response__, 'system_data'),
        type=pulumi.get(__response__, 'type')))
