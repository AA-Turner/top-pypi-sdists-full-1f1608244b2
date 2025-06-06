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
    'GetPrivateLinkServicePrivateEndpointConnectionResult',
    'AwaitableGetPrivateLinkServicePrivateEndpointConnectionResult',
    'get_private_link_service_private_endpoint_connection',
    'get_private_link_service_private_endpoint_connection_output',
]

@pulumi.output_type
class GetPrivateLinkServicePrivateEndpointConnectionResult:
    """
    PrivateEndpointConnection resource.
    """
    def __init__(__self__, azure_api_version=None, etag=None, id=None, link_identifier=None, name=None, private_endpoint=None, private_endpoint_location=None, private_link_service_connection_state=None, provisioning_state=None, type=None):
        if azure_api_version and not isinstance(azure_api_version, str):
            raise TypeError("Expected argument 'azure_api_version' to be a str")
        pulumi.set(__self__, "azure_api_version", azure_api_version)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if link_identifier and not isinstance(link_identifier, str):
            raise TypeError("Expected argument 'link_identifier' to be a str")
        pulumi.set(__self__, "link_identifier", link_identifier)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if private_endpoint and not isinstance(private_endpoint, dict):
            raise TypeError("Expected argument 'private_endpoint' to be a dict")
        pulumi.set(__self__, "private_endpoint", private_endpoint)
        if private_endpoint_location and not isinstance(private_endpoint_location, str):
            raise TypeError("Expected argument 'private_endpoint_location' to be a str")
        pulumi.set(__self__, "private_endpoint_location", private_endpoint_location)
        if private_link_service_connection_state and not isinstance(private_link_service_connection_state, dict):
            raise TypeError("Expected argument 'private_link_service_connection_state' to be a dict")
        pulumi.set(__self__, "private_link_service_connection_state", private_link_service_connection_state)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
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
    @pulumi.getter
    def etag(self) -> builtins.str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> Optional[builtins.str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="linkIdentifier")
    def link_identifier(self) -> builtins.str:
        """
        The consumer link id.
        """
        return pulumi.get(self, "link_identifier")

    @property
    @pulumi.getter
    def name(self) -> Optional[builtins.str]:
        """
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> 'outputs.PrivateEndpointResponse':
        """
        The resource of private end point.
        """
        return pulumi.get(self, "private_endpoint")

    @property
    @pulumi.getter(name="privateEndpointLocation")
    def private_endpoint_location(self) -> builtins.str:
        """
        The location of the private endpoint.
        """
        return pulumi.get(self, "private_endpoint_location")

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional['outputs.PrivateLinkServiceConnectionStateResponse']:
        """
        A collection of information about the state of the connection between service consumer and provider.
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> builtins.str:
        """
        The provisioning state of the private endpoint connection resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> builtins.str:
        """
        The resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetPrivateLinkServicePrivateEndpointConnectionResult(GetPrivateLinkServicePrivateEndpointConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrivateLinkServicePrivateEndpointConnectionResult(
            azure_api_version=self.azure_api_version,
            etag=self.etag,
            id=self.id,
            link_identifier=self.link_identifier,
            name=self.name,
            private_endpoint=self.private_endpoint,
            private_endpoint_location=self.private_endpoint_location,
            private_link_service_connection_state=self.private_link_service_connection_state,
            provisioning_state=self.provisioning_state,
            type=self.type)


def get_private_link_service_private_endpoint_connection(expand: Optional[builtins.str] = None,
                                                         pe_connection_name: Optional[builtins.str] = None,
                                                         resource_group_name: Optional[builtins.str] = None,
                                                         service_name: Optional[builtins.str] = None,
                                                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPrivateLinkServicePrivateEndpointConnectionResult:
    """
    Get the specific private end point connection by specific private link service in the resource group.

    Uses Azure REST API version 2024-05-01.

    Other available API versions: 2019-09-01, 2019-11-01, 2019-12-01, 2020-03-01, 2020-04-01, 2020-05-01, 2020-06-01, 2020-07-01, 2020-08-01, 2020-11-01, 2021-02-01, 2021-03-01, 2021-05-01, 2021-08-01, 2022-01-01, 2022-05-01, 2022-07-01, 2022-09-01, 2022-11-01, 2023-02-01, 2023-04-01, 2023-05-01, 2023-06-01, 2023-09-01, 2023-11-01, 2024-01-01, 2024-03-01, 2024-07-01. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native network [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param builtins.str expand: Expands referenced resources.
    :param builtins.str pe_connection_name: The name of the private end point connection.
    :param builtins.str resource_group_name: The name of the resource group.
    :param builtins.str service_name: The name of the private link service.
    """
    __args__ = dict()
    __args__['expand'] = expand
    __args__['peConnectionName'] = pe_connection_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network:getPrivateLinkServicePrivateEndpointConnection', __args__, opts=opts, typ=GetPrivateLinkServicePrivateEndpointConnectionResult).value

    return AwaitableGetPrivateLinkServicePrivateEndpointConnectionResult(
        azure_api_version=pulumi.get(__ret__, 'azure_api_version'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        link_identifier=pulumi.get(__ret__, 'link_identifier'),
        name=pulumi.get(__ret__, 'name'),
        private_endpoint=pulumi.get(__ret__, 'private_endpoint'),
        private_endpoint_location=pulumi.get(__ret__, 'private_endpoint_location'),
        private_link_service_connection_state=pulumi.get(__ret__, 'private_link_service_connection_state'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        type=pulumi.get(__ret__, 'type'))
def get_private_link_service_private_endpoint_connection_output(expand: Optional[pulumi.Input[Optional[builtins.str]]] = None,
                                                                pe_connection_name: Optional[pulumi.Input[builtins.str]] = None,
                                                                resource_group_name: Optional[pulumi.Input[builtins.str]] = None,
                                                                service_name: Optional[pulumi.Input[builtins.str]] = None,
                                                                opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetPrivateLinkServicePrivateEndpointConnectionResult]:
    """
    Get the specific private end point connection by specific private link service in the resource group.

    Uses Azure REST API version 2024-05-01.

    Other available API versions: 2019-09-01, 2019-11-01, 2019-12-01, 2020-03-01, 2020-04-01, 2020-05-01, 2020-06-01, 2020-07-01, 2020-08-01, 2020-11-01, 2021-02-01, 2021-03-01, 2021-05-01, 2021-08-01, 2022-01-01, 2022-05-01, 2022-07-01, 2022-09-01, 2022-11-01, 2023-02-01, 2023-04-01, 2023-05-01, 2023-06-01, 2023-09-01, 2023-11-01, 2024-01-01, 2024-03-01, 2024-07-01. These can be accessed by generating a local SDK package using the CLI command `pulumi package add azure-native network [ApiVersion]`. See the [version guide](../../../version-guide/#accessing-any-api-version-via-local-packages) for details.


    :param builtins.str expand: Expands referenced resources.
    :param builtins.str pe_connection_name: The name of the private end point connection.
    :param builtins.str resource_group_name: The name of the resource group.
    :param builtins.str service_name: The name of the private link service.
    """
    __args__ = dict()
    __args__['expand'] = expand
    __args__['peConnectionName'] = pe_connection_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('azure-native:network:getPrivateLinkServicePrivateEndpointConnection', __args__, opts=opts, typ=GetPrivateLinkServicePrivateEndpointConnectionResult)
    return __ret__.apply(lambda __response__: GetPrivateLinkServicePrivateEndpointConnectionResult(
        azure_api_version=pulumi.get(__response__, 'azure_api_version'),
        etag=pulumi.get(__response__, 'etag'),
        id=pulumi.get(__response__, 'id'),
        link_identifier=pulumi.get(__response__, 'link_identifier'),
        name=pulumi.get(__response__, 'name'),
        private_endpoint=pulumi.get(__response__, 'private_endpoint'),
        private_endpoint_location=pulumi.get(__response__, 'private_endpoint_location'),
        private_link_service_connection_state=pulumi.get(__response__, 'private_link_service_connection_state'),
        provisioning_state=pulumi.get(__response__, 'provisioning_state'),
        type=pulumi.get(__response__, 'type')))
