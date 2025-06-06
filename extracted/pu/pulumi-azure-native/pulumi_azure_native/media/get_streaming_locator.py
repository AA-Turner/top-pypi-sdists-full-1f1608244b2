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
    'GetStreamingLocatorResult',
    'AwaitableGetStreamingLocatorResult',
    'get_streaming_locator',
    'get_streaming_locator_output',
]

@pulumi.output_type
class GetStreamingLocatorResult:
    """
    A Streaming Locator resource
    """
    def __init__(__self__, alternative_media_id=None, asset_name=None, azure_api_version=None, content_keys=None, created=None, default_content_key_policy_name=None, end_time=None, filters=None, id=None, name=None, start_time=None, streaming_locator_id=None, streaming_policy_name=None, system_data=None, type=None):
        if alternative_media_id and not isinstance(alternative_media_id, str):
            raise TypeError("Expected argument 'alternative_media_id' to be a str")
        pulumi.set(__self__, "alternative_media_id", alternative_media_id)
        if asset_name and not isinstance(asset_name, str):
            raise TypeError("Expected argument 'asset_name' to be a str")
        pulumi.set(__self__, "asset_name", asset_name)
        if azure_api_version and not isinstance(azure_api_version, str):
            raise TypeError("Expected argument 'azure_api_version' to be a str")
        pulumi.set(__self__, "azure_api_version", azure_api_version)
        if content_keys and not isinstance(content_keys, list):
            raise TypeError("Expected argument 'content_keys' to be a list")
        pulumi.set(__self__, "content_keys", content_keys)
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if default_content_key_policy_name and not isinstance(default_content_key_policy_name, str):
            raise TypeError("Expected argument 'default_content_key_policy_name' to be a str")
        pulumi.set(__self__, "default_content_key_policy_name", default_content_key_policy_name)
        if end_time and not isinstance(end_time, str):
            raise TypeError("Expected argument 'end_time' to be a str")
        pulumi.set(__self__, "end_time", end_time)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if start_time and not isinstance(start_time, str):
            raise TypeError("Expected argument 'start_time' to be a str")
        pulumi.set(__self__, "start_time", start_time)
        if streaming_locator_id and not isinstance(streaming_locator_id, str):
            raise TypeError("Expected argument 'streaming_locator_id' to be a str")
        pulumi.set(__self__, "streaming_locator_id", streaming_locator_id)
        if streaming_policy_name and not isinstance(streaming_policy_name, str):
            raise TypeError("Expected argument 'streaming_policy_name' to be a str")
        pulumi.set(__self__, "streaming_policy_name", streaming_policy_name)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="alternativeMediaId")
    def alternative_media_id(self) -> Optional[builtins.str]:
        """
        Alternative Media ID of this Streaming Locator
        """
        return pulumi.get(self, "alternative_media_id")

    @property
    @pulumi.getter(name="assetName")
    def asset_name(self) -> builtins.str:
        """
        Asset Name
        """
        return pulumi.get(self, "asset_name")

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> builtins.str:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter(name="contentKeys")
    def content_keys(self) -> Optional[Sequence['outputs.StreamingLocatorContentKeyResponse']]:
        """
        The ContentKeys used by this Streaming Locator.
        """
        return pulumi.get(self, "content_keys")

    @property
    @pulumi.getter
    def created(self) -> builtins.str:
        """
        The creation time of the Streaming Locator.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="defaultContentKeyPolicyName")
    def default_content_key_policy_name(self) -> Optional[builtins.str]:
        """
        Name of the default ContentKeyPolicy used by this Streaming Locator.
        """
        return pulumi.get(self, "default_content_key_policy_name")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[builtins.str]:
        """
        The end time of the Streaming Locator.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[builtins.str]]:
        """
        A list of asset or account filters which apply to this streaming locator
        """
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> builtins.str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[builtins.str]:
        """
        The start time of the Streaming Locator.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter(name="streamingLocatorId")
    def streaming_locator_id(self) -> Optional[builtins.str]:
        """
        The StreamingLocatorId of the Streaming Locator.
        """
        return pulumi.get(self, "streaming_locator_id")

    @property
    @pulumi.getter(name="streamingPolicyName")
    def streaming_policy_name(self) -> builtins.str:
        """
        Name of the Streaming Policy used by this Streaming Locator. Either specify the name of Streaming Policy you created or use one of the predefined Streaming Policies. The predefined Streaming Policies available are: 'Predefined_DownloadOnly', 'Predefined_ClearStreamingOnly', 'Predefined_DownloadAndClearStreaming', 'Predefined_ClearKey', 'Predefined_MultiDrmCencStreaming' and 'Predefined_MultiDrmStreaming'
        """
        return pulumi.get(self, "streaming_policy_name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> builtins.str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetStreamingLocatorResult(GetStreamingLocatorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStreamingLocatorResult(
            alternative_media_id=self.alternative_media_id,
            asset_name=self.asset_name,
            azure_api_version=self.azure_api_version,
            content_keys=self.content_keys,
            created=self.created,
            default_content_key_policy_name=self.default_content_key_policy_name,
            end_time=self.end_time,
            filters=self.filters,
            id=self.id,
            name=self.name,
            start_time=self.start_time,
            streaming_locator_id=self.streaming_locator_id,
            streaming_policy_name=self.streaming_policy_name,
            system_data=self.system_data,
            type=self.type)


def get_streaming_locator(account_name: Optional[builtins.str] = None,
                          resource_group_name: Optional[builtins.str] = None,
                          streaming_locator_name: Optional[builtins.str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStreamingLocatorResult:
    """
    Get the details of a Streaming Locator in the Media Services account

    Uses Azure REST API version 2023-01-01.

    Other available API versions: 2018-03-30-preview, 2018-06-01-preview, 2018-07-01, 2020-05-01, 2021-06-01, 2021-11-01, 2022-08-01. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native media [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param builtins.str account_name: The Media Services account name.
    :param builtins.str resource_group_name: The name of the resource group within the Azure subscription.
    :param builtins.str streaming_locator_name: The Streaming Locator name.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['streamingLocatorName'] = streaming_locator_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:media:getStreamingLocator', __args__, opts=opts, typ=GetStreamingLocatorResult).value

    return AwaitableGetStreamingLocatorResult(
        alternative_media_id=pulumi.get(__ret__, 'alternative_media_id'),
        asset_name=pulumi.get(__ret__, 'asset_name'),
        azure_api_version=pulumi.get(__ret__, 'azure_api_version'),
        content_keys=pulumi.get(__ret__, 'content_keys'),
        created=pulumi.get(__ret__, 'created'),
        default_content_key_policy_name=pulumi.get(__ret__, 'default_content_key_policy_name'),
        end_time=pulumi.get(__ret__, 'end_time'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        start_time=pulumi.get(__ret__, 'start_time'),
        streaming_locator_id=pulumi.get(__ret__, 'streaming_locator_id'),
        streaming_policy_name=pulumi.get(__ret__, 'streaming_policy_name'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))
def get_streaming_locator_output(account_name: Optional[pulumi.Input[builtins.str]] = None,
                                 resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                                 streaming_locator_name: Optional[pulumi.Input[builtins.str]] = None,
                                 opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetStreamingLocatorResult]:
    """
    Get the details of a Streaming Locator in the Media Services account

    Uses Azure REST API version 2023-01-01.

    Other available API versions: 2018-03-30-preview, 2018-06-01-preview, 2018-07-01, 2020-05-01, 2021-06-01, 2021-11-01, 2022-08-01. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native media [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param builtins.str account_name: The Media Services account name.
    :param builtins.str resource_group_name: The name of the resource group within the Azure subscription.
    :param builtins.str streaming_locator_name: The Streaming Locator name.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['streamingLocatorName'] = streaming_locator_name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('azure-native:media:getStreamingLocator', __args__, opts=opts, typ=GetStreamingLocatorResult)
    return __ret__.apply(lambda __response__: GetStreamingLocatorResult(
        alternative_media_id=pulumi.get(__response__, 'alternative_media_id'),
        asset_name=pulumi.get(__response__, 'asset_name'),
        azure_api_version=pulumi.get(__response__, 'azure_api_version'),
        content_keys=pulumi.get(__response__, 'content_keys'),
        created=pulumi.get(__response__, 'created'),
        default_content_key_policy_name=pulumi.get(__response__, 'default_content_key_policy_name'),
        end_time=pulumi.get(__response__, 'end_time'),
        filters=pulumi.get(__response__, 'filters'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        start_time=pulumi.get(__response__, 'start_time'),
        streaming_locator_id=pulumi.get(__response__, 'streaming_locator_id'),
        streaming_policy_name=pulumi.get(__response__, 'streaming_policy_name'),
        system_data=pulumi.get(__response__, 'system_data'),
        type=pulumi.get(__response__, 'type')))
