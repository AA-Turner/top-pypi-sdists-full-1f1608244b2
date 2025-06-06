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
    'GetPremiumMicrosoftDefenderForThreatIntelligenceResult',
    'AwaitableGetPremiumMicrosoftDefenderForThreatIntelligenceResult',
    'get_premium_microsoft_defender_for_threat_intelligence',
    'get_premium_microsoft_defender_for_threat_intelligence_output',
]

@pulumi.output_type
class GetPremiumMicrosoftDefenderForThreatIntelligenceResult:
    """
    Represents Premium Microsoft Defender for Threat Intelligence data connector.
    """
    def __init__(__self__, azure_api_version=None, data_types=None, etag=None, id=None, kind=None, lookback_period=None, name=None, required_skus_present=None, system_data=None, tenant_id=None, type=None):
        if azure_api_version and not isinstance(azure_api_version, str):
            raise TypeError("Expected argument 'azure_api_version' to be a str")
        pulumi.set(__self__, "azure_api_version", azure_api_version)
        if data_types and not isinstance(data_types, dict):
            raise TypeError("Expected argument 'data_types' to be a dict")
        pulumi.set(__self__, "data_types", data_types)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if lookback_period and not isinstance(lookback_period, str):
            raise TypeError("Expected argument 'lookback_period' to be a str")
        pulumi.set(__self__, "lookback_period", lookback_period)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if required_skus_present and not isinstance(required_skus_present, bool):
            raise TypeError("Expected argument 'required_skus_present' to be a bool")
        pulumi.set(__self__, "required_skus_present", required_skus_present)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
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
    @pulumi.getter(name="dataTypes")
    def data_types(self) -> 'outputs.PremiumMdtiDataConnectorDataTypesResponse':
        """
        The available data types for the connector.
        """
        return pulumi.get(self, "data_types")

    @property
    @pulumi.getter
    def etag(self) -> Optional[builtins.str]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> builtins.str:
        """
        The kind of the data connector
        Expected value is 'PremiumMicrosoftDefenderForThreatIntelligence'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="lookbackPeriod")
    def lookback_period(self) -> builtins.str:
        """
        The lookback period for the feed to be imported. The date-time to begin importing the feed from, for example: 2024-01-01T00:00:00.000Z.
        """
        return pulumi.get(self, "lookback_period")

    @property
    @pulumi.getter
    def name(self) -> builtins.str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="requiredSKUsPresent")
    def required_skus_present(self) -> Optional[builtins.bool]:
        """
        The flag to indicate whether the tenant has the premium SKU required to access this connector.
        """
        return pulumi.get(self, "required_skus_present")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[builtins.str]:
        """
        The tenant id to connect to, and get the data from.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> builtins.str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetPremiumMicrosoftDefenderForThreatIntelligenceResult(GetPremiumMicrosoftDefenderForThreatIntelligenceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPremiumMicrosoftDefenderForThreatIntelligenceResult(
            azure_api_version=self.azure_api_version,
            data_types=self.data_types,
            etag=self.etag,
            id=self.id,
            kind=self.kind,
            lookback_period=self.lookback_period,
            name=self.name,
            required_skus_present=self.required_skus_present,
            system_data=self.system_data,
            tenant_id=self.tenant_id,
            type=self.type)


def get_premium_microsoft_defender_for_threat_intelligence(data_connector_id: Optional[builtins.str] = None,
                                                           resource_group_name: Optional[builtins.str] = None,
                                                           workspace_name: Optional[builtins.str] = None,
                                                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPremiumMicrosoftDefenderForThreatIntelligenceResult:
    """
    Gets a data connector.

    Uses Azure REST API version 2024-09-01.


    :param builtins.str data_connector_id: Connector ID
    :param builtins.str resource_group_name: The name of the resource group. The name is case insensitive.
    :param builtins.str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['dataConnectorId'] = data_connector_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights:getPremiumMicrosoftDefenderForThreatIntelligence', __args__, opts=opts, typ=GetPremiumMicrosoftDefenderForThreatIntelligenceResult).value

    return AwaitableGetPremiumMicrosoftDefenderForThreatIntelligenceResult(
        azure_api_version=pulumi.get(__ret__, 'azure_api_version'),
        data_types=pulumi.get(__ret__, 'data_types'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        lookback_period=pulumi.get(__ret__, 'lookback_period'),
        name=pulumi.get(__ret__, 'name'),
        required_skus_present=pulumi.get(__ret__, 'required_skus_present'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tenant_id=pulumi.get(__ret__, 'tenant_id'),
        type=pulumi.get(__ret__, 'type'))
def get_premium_microsoft_defender_for_threat_intelligence_output(data_connector_id: Optional[pulumi.Input[builtins.str]] = None,
                                                                  resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                                                                  workspace_name: Optional[pulumi.Input[builtins.str]] = None,
                                                                  opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetPremiumMicrosoftDefenderForThreatIntelligenceResult]:
    """
    Gets a data connector.

    Uses Azure REST API version 2024-09-01.


    :param builtins.str data_connector_id: Connector ID
    :param builtins.str resource_group_name: The name of the resource group. The name is case insensitive.
    :param builtins.str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['dataConnectorId'] = data_connector_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('azure-native:securityinsights:getPremiumMicrosoftDefenderForThreatIntelligence', __args__, opts=opts, typ=GetPremiumMicrosoftDefenderForThreatIntelligenceResult)
    return __ret__.apply(lambda __response__: GetPremiumMicrosoftDefenderForThreatIntelligenceResult(
        azure_api_version=pulumi.get(__response__, 'azure_api_version'),
        data_types=pulumi.get(__response__, 'data_types'),
        etag=pulumi.get(__response__, 'etag'),
        id=pulumi.get(__response__, 'id'),
        kind=pulumi.get(__response__, 'kind'),
        lookback_period=pulumi.get(__response__, 'lookback_period'),
        name=pulumi.get(__response__, 'name'),
        required_skus_present=pulumi.get(__response__, 'required_skus_present'),
        system_data=pulumi.get(__response__, 'system_data'),
        tenant_id=pulumi.get(__response__, 'tenant_id'),
        type=pulumi.get(__response__, 'type')))
