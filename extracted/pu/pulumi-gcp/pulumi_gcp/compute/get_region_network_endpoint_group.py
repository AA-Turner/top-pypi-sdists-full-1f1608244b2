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
    'GetRegionNetworkEndpointGroupResult',
    'AwaitableGetRegionNetworkEndpointGroupResult',
    'get_region_network_endpoint_group',
    'get_region_network_endpoint_group_output',
]

@pulumi.output_type
class GetRegionNetworkEndpointGroupResult:
    """
    A collection of values returned by getRegionNetworkEndpointGroup.
    """
    def __init__(__self__, app_engines=None, cloud_functions=None, cloud_runs=None, description=None, id=None, name=None, network=None, network_endpoint_type=None, project=None, psc_datas=None, psc_target_service=None, region=None, self_link=None, serverless_deployments=None, subnetwork=None):
        if app_engines and not isinstance(app_engines, list):
            raise TypeError("Expected argument 'app_engines' to be a list")
        pulumi.set(__self__, "app_engines", app_engines)
        if cloud_functions and not isinstance(cloud_functions, list):
            raise TypeError("Expected argument 'cloud_functions' to be a list")
        pulumi.set(__self__, "cloud_functions", cloud_functions)
        if cloud_runs and not isinstance(cloud_runs, list):
            raise TypeError("Expected argument 'cloud_runs' to be a list")
        pulumi.set(__self__, "cloud_runs", cloud_runs)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network and not isinstance(network, str):
            raise TypeError("Expected argument 'network' to be a str")
        pulumi.set(__self__, "network", network)
        if network_endpoint_type and not isinstance(network_endpoint_type, str):
            raise TypeError("Expected argument 'network_endpoint_type' to be a str")
        pulumi.set(__self__, "network_endpoint_type", network_endpoint_type)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if psc_datas and not isinstance(psc_datas, list):
            raise TypeError("Expected argument 'psc_datas' to be a list")
        pulumi.set(__self__, "psc_datas", psc_datas)
        if psc_target_service and not isinstance(psc_target_service, str):
            raise TypeError("Expected argument 'psc_target_service' to be a str")
        pulumi.set(__self__, "psc_target_service", psc_target_service)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if serverless_deployments and not isinstance(serverless_deployments, list):
            raise TypeError("Expected argument 'serverless_deployments' to be a list")
        pulumi.set(__self__, "serverless_deployments", serverless_deployments)
        if subnetwork and not isinstance(subnetwork, str):
            raise TypeError("Expected argument 'subnetwork' to be a str")
        pulumi.set(__self__, "subnetwork", subnetwork)

    @property
    @pulumi.getter(name="appEngines")
    def app_engines(self) -> Sequence['outputs.GetRegionNetworkEndpointGroupAppEngineResult']:
        return pulumi.get(self, "app_engines")

    @property
    @pulumi.getter(name="cloudFunctions")
    def cloud_functions(self) -> Sequence['outputs.GetRegionNetworkEndpointGroupCloudFunctionResult']:
        return pulumi.get(self, "cloud_functions")

    @property
    @pulumi.getter(name="cloudRuns")
    def cloud_runs(self) -> Sequence['outputs.GetRegionNetworkEndpointGroupCloudRunResult']:
        return pulumi.get(self, "cloud_runs")

    @property
    @pulumi.getter
    def description(self) -> builtins.str:
        """
        The RNEG description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[builtins.str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network(self) -> builtins.str:
        """
        The network to which all network endpoints in the RNEG belong.
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter(name="networkEndpointType")
    def network_endpoint_type(self) -> builtins.str:
        """
        Type of network endpoints in this network endpoint group.
        """
        return pulumi.get(self, "network_endpoint_type")

    @property
    @pulumi.getter
    def project(self) -> Optional[builtins.str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="pscDatas")
    def psc_datas(self) -> Sequence['outputs.GetRegionNetworkEndpointGroupPscDataResult']:
        return pulumi.get(self, "psc_datas")

    @property
    @pulumi.getter(name="pscTargetService")
    def psc_target_service(self) -> builtins.str:
        """
        The target service url used to set up private service connection to a Google API or a PSC Producer Service Attachment.
        """
        return pulumi.get(self, "psc_target_service")

    @property
    @pulumi.getter
    def region(self) -> Optional[builtins.str]:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[builtins.str]:
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="serverlessDeployments")
    def serverless_deployments(self) -> Sequence['outputs.GetRegionNetworkEndpointGroupServerlessDeploymentResult']:
        return pulumi.get(self, "serverless_deployments")

    @property
    @pulumi.getter
    def subnetwork(self) -> builtins.str:
        """
        subnetwork to which all network endpoints in the RNEG belong.
        """
        return pulumi.get(self, "subnetwork")


class AwaitableGetRegionNetworkEndpointGroupResult(GetRegionNetworkEndpointGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRegionNetworkEndpointGroupResult(
            app_engines=self.app_engines,
            cloud_functions=self.cloud_functions,
            cloud_runs=self.cloud_runs,
            description=self.description,
            id=self.id,
            name=self.name,
            network=self.network,
            network_endpoint_type=self.network_endpoint_type,
            project=self.project,
            psc_datas=self.psc_datas,
            psc_target_service=self.psc_target_service,
            region=self.region,
            self_link=self.self_link,
            serverless_deployments=self.serverless_deployments,
            subnetwork=self.subnetwork)


def get_region_network_endpoint_group(name: Optional[builtins.str] = None,
                                      project: Optional[builtins.str] = None,
                                      region: Optional[builtins.str] = None,
                                      self_link: Optional[builtins.str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRegionNetworkEndpointGroupResult:
    """
    Use this data source to access a Region Network Endpoint Group's attributes.

    The RNEG may be found by providing either a `self_link`, or a `name` and a `region`.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    rneg1 = gcp.compute.get_region_network_endpoint_group(name="k8s1-abcdef01-myns-mysvc-8080-4b6bac43",
        region="us-central1")
    rneg2 = gcp.compute.get_region_network_endpoint_group(self_link="https://www.googleapis.com/compute/v1/projects/myproject/regions/us-central1/networkEndpointGroups/k8s1-abcdef01-myns-mysvc-8080-4b6bac43")
    ```


    :param builtins.str name: The Network Endpoint Group name. Provide either this or a `self_link`.
    :param builtins.str project: The ID of the project to list versions in. If it is not provided, the provider project is used.
    :param builtins.str region: A reference to the region where the Serverless REGs Reside. Provide either this or a `self_link`.
    :param builtins.str self_link: The Network Endpoint Group self_link.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['project'] = project
    __args__['region'] = region
    __args__['selfLink'] = self_link
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:compute/getRegionNetworkEndpointGroup:getRegionNetworkEndpointGroup', __args__, opts=opts, typ=GetRegionNetworkEndpointGroupResult).value

    return AwaitableGetRegionNetworkEndpointGroupResult(
        app_engines=pulumi.get(__ret__, 'app_engines'),
        cloud_functions=pulumi.get(__ret__, 'cloud_functions'),
        cloud_runs=pulumi.get(__ret__, 'cloud_runs'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        network=pulumi.get(__ret__, 'network'),
        network_endpoint_type=pulumi.get(__ret__, 'network_endpoint_type'),
        project=pulumi.get(__ret__, 'project'),
        psc_datas=pulumi.get(__ret__, 'psc_datas'),
        psc_target_service=pulumi.get(__ret__, 'psc_target_service'),
        region=pulumi.get(__ret__, 'region'),
        self_link=pulumi.get(__ret__, 'self_link'),
        serverless_deployments=pulumi.get(__ret__, 'serverless_deployments'),
        subnetwork=pulumi.get(__ret__, 'subnetwork'))
def get_region_network_endpoint_group_output(name: Optional[pulumi.Input[Optional[builtins.str]]] = None,
                                             project: Optional[pulumi.Input[Optional[builtins.str]]] = None,
                                             region: Optional[pulumi.Input[Optional[builtins.str]]] = None,
                                             self_link: Optional[pulumi.Input[Optional[builtins.str]]] = None,
                                             opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetRegionNetworkEndpointGroupResult]:
    """
    Use this data source to access a Region Network Endpoint Group's attributes.

    The RNEG may be found by providing either a `self_link`, or a `name` and a `region`.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    rneg1 = gcp.compute.get_region_network_endpoint_group(name="k8s1-abcdef01-myns-mysvc-8080-4b6bac43",
        region="us-central1")
    rneg2 = gcp.compute.get_region_network_endpoint_group(self_link="https://www.googleapis.com/compute/v1/projects/myproject/regions/us-central1/networkEndpointGroups/k8s1-abcdef01-myns-mysvc-8080-4b6bac43")
    ```


    :param builtins.str name: The Network Endpoint Group name. Provide either this or a `self_link`.
    :param builtins.str project: The ID of the project to list versions in. If it is not provided, the provider project is used.
    :param builtins.str region: A reference to the region where the Serverless REGs Reside. Provide either this or a `self_link`.
    :param builtins.str self_link: The Network Endpoint Group self_link.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['project'] = project
    __args__['region'] = region
    __args__['selfLink'] = self_link
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('gcp:compute/getRegionNetworkEndpointGroup:getRegionNetworkEndpointGroup', __args__, opts=opts, typ=GetRegionNetworkEndpointGroupResult)
    return __ret__.apply(lambda __response__: GetRegionNetworkEndpointGroupResult(
        app_engines=pulumi.get(__response__, 'app_engines'),
        cloud_functions=pulumi.get(__response__, 'cloud_functions'),
        cloud_runs=pulumi.get(__response__, 'cloud_runs'),
        description=pulumi.get(__response__, 'description'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        network=pulumi.get(__response__, 'network'),
        network_endpoint_type=pulumi.get(__response__, 'network_endpoint_type'),
        project=pulumi.get(__response__, 'project'),
        psc_datas=pulumi.get(__response__, 'psc_datas'),
        psc_target_service=pulumi.get(__response__, 'psc_target_service'),
        region=pulumi.get(__response__, 'region'),
        self_link=pulumi.get(__response__, 'self_link'),
        serverless_deployments=pulumi.get(__response__, 'serverless_deployments'),
        subnetwork=pulumi.get(__response__, 'subnetwork')))
