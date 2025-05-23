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
    'GetQueryResult',
    'AwaitableGetQueryResult',
    'get_query',
    'get_query_output',
]

@pulumi.output_type
class GetQueryResult:
    """
    A Log Analytics QueryPack-Query definition.
    """
    def __init__(__self__, author=None, azure_api_version=None, body=None, description=None, display_name=None, id=None, name=None, properties=None, related=None, system_data=None, tags=None, time_created=None, time_modified=None, type=None):
        if author and not isinstance(author, str):
            raise TypeError("Expected argument 'author' to be a str")
        pulumi.set(__self__, "author", author)
        if azure_api_version and not isinstance(azure_api_version, str):
            raise TypeError("Expected argument 'azure_api_version' to be a str")
        pulumi.set(__self__, "azure_api_version", azure_api_version)
        if body and not isinstance(body, str):
            raise TypeError("Expected argument 'body' to be a str")
        pulumi.set(__self__, "body", body)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if related and not isinstance(related, dict):
            raise TypeError("Expected argument 'related' to be a dict")
        pulumi.set(__self__, "related", related)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_modified and not isinstance(time_modified, str):
            raise TypeError("Expected argument 'time_modified' to be a str")
        pulumi.set(__self__, "time_modified", time_modified)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def author(self) -> builtins.str:
        """
        Object Id of user creating the query.
        """
        return pulumi.get(self, "author")

    @property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> builtins.str:
        """
        The Azure API version of the resource.
        """
        return pulumi.get(self, "azure_api_version")

    @property
    @pulumi.getter
    def body(self) -> builtins.str:
        """
        Body of the query.
        """
        return pulumi.get(self, "body")

    @property
    @pulumi.getter
    def description(self) -> Optional[builtins.str]:
        """
        Description of the query.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> builtins.str:
        """
        Unique display name for your query within the Query Pack.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
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
    @pulumi.getter
    def properties(self) -> Any:
        """
        Additional properties that can be set for the query.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def related(self) -> Optional['outputs.LogAnalyticsQueryPackQueryPropertiesResponseRelated']:
        """
        The related metadata items for the function.
        """
        return pulumi.get(self, "related")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, Sequence[builtins.str]]]:
        """
        Tags associated with the query.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> builtins.str:
        """
        Creation Date for the Log Analytics Query, in ISO 8601 format.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeModified")
    def time_modified(self) -> builtins.str:
        """
        Last modified date of the Log Analytics Query, in ISO 8601 format.
        """
        return pulumi.get(self, "time_modified")

    @property
    @pulumi.getter
    def type(self) -> builtins.str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetQueryResult(GetQueryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetQueryResult(
            author=self.author,
            azure_api_version=self.azure_api_version,
            body=self.body,
            description=self.description,
            display_name=self.display_name,
            id=self.id,
            name=self.name,
            properties=self.properties,
            related=self.related,
            system_data=self.system_data,
            tags=self.tags,
            time_created=self.time_created,
            time_modified=self.time_modified,
            type=self.type)


def get_query(id: Optional[builtins.str] = None,
              query_pack_name: Optional[builtins.str] = None,
              resource_group_name: Optional[builtins.str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetQueryResult:
    """
    Gets a specific Log Analytics Query defined within a Log Analytics QueryPack.

    Uses Azure REST API version 2023-09-01.

    Other available API versions: 2019-09-01, 2019-09-01-preview, 2025-02-01. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native operationalinsights [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param builtins.str id: The id of a specific query defined in the Log Analytics QueryPack
    :param builtins.str query_pack_name: The name of the Log Analytics QueryPack resource.
    :param builtins.str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['queryPackName'] = query_pack_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:operationalinsights:getQuery', __args__, opts=opts, typ=GetQueryResult).value

    return AwaitableGetQueryResult(
        author=pulumi.get(__ret__, 'author'),
        azure_api_version=pulumi.get(__ret__, 'azure_api_version'),
        body=pulumi.get(__ret__, 'body'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        related=pulumi.get(__ret__, 'related'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_modified=pulumi.get(__ret__, 'time_modified'),
        type=pulumi.get(__ret__, 'type'))
def get_query_output(id: Optional[pulumi.Input[builtins.str]] = None,
                     query_pack_name: Optional[pulumi.Input[builtins.str]] = None,
                     resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                     opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetQueryResult]:
    """
    Gets a specific Log Analytics Query defined within a Log Analytics QueryPack.

    Uses Azure REST API version 2023-09-01.

    Other available API versions: 2019-09-01, 2019-09-01-preview, 2025-02-01. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native operationalinsights [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param builtins.str id: The id of a specific query defined in the Log Analytics QueryPack
    :param builtins.str query_pack_name: The name of the Log Analytics QueryPack resource.
    :param builtins.str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['queryPackName'] = query_pack_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('azure-native:operationalinsights:getQuery', __args__, opts=opts, typ=GetQueryResult)
    return __ret__.apply(lambda __response__: GetQueryResult(
        author=pulumi.get(__response__, 'author'),
        azure_api_version=pulumi.get(__response__, 'azure_api_version'),
        body=pulumi.get(__response__, 'body'),
        description=pulumi.get(__response__, 'description'),
        display_name=pulumi.get(__response__, 'display_name'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        properties=pulumi.get(__response__, 'properties'),
        related=pulumi.get(__response__, 'related'),
        system_data=pulumi.get(__response__, 'system_data'),
        tags=pulumi.get(__response__, 'tags'),
        time_created=pulumi.get(__response__, 'time_created'),
        time_modified=pulumi.get(__response__, 'time_modified'),
        type=pulumi.get(__response__, 'type')))
