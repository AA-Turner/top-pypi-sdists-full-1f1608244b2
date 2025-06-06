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
    'ListIotHubResourceKeysForKeyNameResult',
    'AwaitableListIotHubResourceKeysForKeyNameResult',
    'list_iot_hub_resource_keys_for_key_name',
    'list_iot_hub_resource_keys_for_key_name_output',
]

@pulumi.output_type
class ListIotHubResourceKeysForKeyNameResult:
    """
    The properties of an IoT hub shared access policy.
    """
    def __init__(__self__, key_name=None, primary_key=None, rights=None, secondary_key=None):
        if key_name and not isinstance(key_name, str):
            raise TypeError("Expected argument 'key_name' to be a str")
        pulumi.set(__self__, "key_name", key_name)
        if primary_key and not isinstance(primary_key, str):
            raise TypeError("Expected argument 'primary_key' to be a str")
        pulumi.set(__self__, "primary_key", primary_key)
        if rights and not isinstance(rights, str):
            raise TypeError("Expected argument 'rights' to be a str")
        pulumi.set(__self__, "rights", rights)
        if secondary_key and not isinstance(secondary_key, str):
            raise TypeError("Expected argument 'secondary_key' to be a str")
        pulumi.set(__self__, "secondary_key", secondary_key)

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> builtins.str:
        """
        The name of the shared access policy.
        """
        return pulumi.get(self, "key_name")

    @property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[builtins.str]:
        """
        The primary key.
        """
        return pulumi.get(self, "primary_key")

    @property
    @pulumi.getter
    def rights(self) -> builtins.str:
        """
        The permissions assigned to the shared access policy.
        """
        return pulumi.get(self, "rights")

    @property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> Optional[builtins.str]:
        """
        The secondary key.
        """
        return pulumi.get(self, "secondary_key")


class AwaitableListIotHubResourceKeysForKeyNameResult(ListIotHubResourceKeysForKeyNameResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListIotHubResourceKeysForKeyNameResult(
            key_name=self.key_name,
            primary_key=self.primary_key,
            rights=self.rights,
            secondary_key=self.secondary_key)


def list_iot_hub_resource_keys_for_key_name(key_name: Optional[builtins.str] = None,
                                            resource_group_name: Optional[builtins.str] = None,
                                            resource_name: Optional[builtins.str] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListIotHubResourceKeysForKeyNameResult:
    """
    Get a shared access policy by name from an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security.

    Uses Azure REST API version 2023-06-30.

    Other available API versions: 2016-02-03, 2017-01-19, 2017-07-01, 2018-01-22, 2018-04-01, 2018-12-01-preview, 2019-03-22, 2019-03-22-preview, 2019-07-01-preview, 2019-11-04, 2020-03-01, 2020-04-01, 2020-06-15, 2020-07-10-preview, 2020-08-01, 2020-08-31, 2020-08-31-preview, 2021-02-01-preview, 2021-03-03-preview, 2021-03-31, 2021-07-01, 2021-07-01-preview, 2021-07-02, 2021-07-02-preview, 2022-04-30-preview, 2022-11-15-preview, 2023-06-30-preview. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native iothub [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param builtins.str key_name: The name of the shared access policy.
    :param builtins.str resource_group_name: The name of the resource group that contains the IoT hub.
    :param builtins.str resource_name: The name of the IoT hub.
    """
    __args__ = dict()
    __args__['keyName'] = key_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:iothub:listIotHubResourceKeysForKeyName', __args__, opts=opts, typ=ListIotHubResourceKeysForKeyNameResult).value

    return AwaitableListIotHubResourceKeysForKeyNameResult(
        key_name=pulumi.get(__ret__, 'key_name'),
        primary_key=pulumi.get(__ret__, 'primary_key'),
        rights=pulumi.get(__ret__, 'rights'),
        secondary_key=pulumi.get(__ret__, 'secondary_key'))
def list_iot_hub_resource_keys_for_key_name_output(key_name: Optional[pulumi.Input[builtins.str]] = None,
                                                   resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                                                   resource_name: Optional[pulumi.Input[builtins.str]] = None,
                                                   opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[ListIotHubResourceKeysForKeyNameResult]:
    """
    Get a shared access policy by name from an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security.

    Uses Azure REST API version 2023-06-30.

    Other available API versions: 2016-02-03, 2017-01-19, 2017-07-01, 2018-01-22, 2018-04-01, 2018-12-01-preview, 2019-03-22, 2019-03-22-preview, 2019-07-01-preview, 2019-11-04, 2020-03-01, 2020-04-01, 2020-06-15, 2020-07-10-preview, 2020-08-01, 2020-08-31, 2020-08-31-preview, 2021-02-01-preview, 2021-03-03-preview, 2021-03-31, 2021-07-01, 2021-07-01-preview, 2021-07-02, 2021-07-02-preview, 2022-04-30-preview, 2022-11-15-preview, 2023-06-30-preview. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native iothub [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param builtins.str key_name: The name of the shared access policy.
    :param builtins.str resource_group_name: The name of the resource group that contains the IoT hub.
    :param builtins.str resource_name: The name of the IoT hub.
    """
    __args__ = dict()
    __args__['keyName'] = key_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('azure-native:iothub:listIotHubResourceKeysForKeyName', __args__, opts=opts, typ=ListIotHubResourceKeysForKeyNameResult)
    return __ret__.apply(lambda __response__: ListIotHubResourceKeysForKeyNameResult(
        key_name=pulumi.get(__response__, 'key_name'),
        primary_key=pulumi.get(__response__, 'primary_key'),
        rights=pulumi.get(__response__, 'rights'),
        secondary_key=pulumi.get(__response__, 'secondary_key')))
