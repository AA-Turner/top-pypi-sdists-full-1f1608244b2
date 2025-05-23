"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re
from .query_result_record_type import QueryResultRecordType


class QueryResultAdminVdcRecordType(QueryResultRecordType):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'description': 'str',
        'compute_provider_scope': 'str',
        'network_provider_scope': 'str',
        'is_enabled': 'bool',
        'cpu_allocation_mhz': 'int',
        'cpu_limit_mhz': 'int',
        'cpu_used_mhz': 'int',
        'memory_allocation_mb': 'int',
        'memory_limit_mb': 'int',
        'memory_used_mb': 'int',
        'storage_allocation_mb': 'int',
        'storage_limit_mb': 'int',
        'storage_used_mb': 'int',
        'provider_vdc_name': 'str',
        'provider_vdc': 'str',
        'org_name': 'str',
        'org': 'str',
        'allocation_model': 'int',
        'number_of_v_apps': 'int',
        'number_of_unmanaged_v_apps': 'int',
        'number_of_media': 'int',
        'number_of_disks': 'int',
        'number_of_v_app_templates': 'int',
        'vc_name': 'str',
        'is_system_vdc': 'bool',
        'is_busy': 'bool',
        'status': 'str',
        'network_pool': 'str',
        'number_of_resource_pools': 'int',
        'number_of_storage_profiles': 'int',
        'used_networks_in_vdc': 'int',
        'number_of_v_ms': 'int',
        'network_pool_universal_id': 'str',
        'number_of_running_v_ms': 'int',
        'number_of_deployed_v_apps': 'int',
        'number_of_deployed_unmanaged_v_apps': 'int',
        'is_thin_provisioned': 'bool',
        'is_fast_provisioned': 'bool',
        'network_provider_type': 'str',
        'number_of_kubernetes_policies': 'int'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'compute_provider_scope': 'computeProviderScope',
        'network_provider_scope': 'networkProviderScope',
        'is_enabled': 'isEnabled',
        'cpu_allocation_mhz': 'cpuAllocationMhz',
        'cpu_limit_mhz': 'cpuLimitMhz',
        'cpu_used_mhz': 'cpuUsedMhz',
        'memory_allocation_mb': 'memoryAllocationMB',
        'memory_limit_mb': 'memoryLimitMB',
        'memory_used_mb': 'memoryUsedMB',
        'storage_allocation_mb': 'storageAllocationMB',
        'storage_limit_mb': 'storageLimitMB',
        'storage_used_mb': 'storageUsedMB',
        'provider_vdc_name': 'providerVdcName',
        'provider_vdc': 'providerVdc',
        'org_name': 'orgName',
        'org': 'org',
        'allocation_model': 'allocationModel',
        'number_of_v_apps': 'numberOfVApps',
        'number_of_unmanaged_v_apps': 'numberOfUnmanagedVApps',
        'number_of_media': 'numberOfMedia',
        'number_of_disks': 'numberOfDisks',
        'number_of_v_app_templates': 'numberOfVAppTemplates',
        'vc_name': 'vcName',
        'is_system_vdc': 'isSystemVdc',
        'is_busy': 'isBusy',
        'status': 'status',
        'network_pool': 'networkPool',
        'number_of_resource_pools': 'numberOfResourcePools',
        'number_of_storage_profiles': 'numberOfStorageProfiles',
        'used_networks_in_vdc': 'usedNetworksInVdc',
        'number_of_v_ms': 'numberOfVMs',
        'network_pool_universal_id': 'networkPoolUniversalId',
        'number_of_running_v_ms': 'numberOfRunningVMs',
        'number_of_deployed_v_apps': 'numberOfDeployedVApps',
        'number_of_deployed_unmanaged_v_apps': 'numberOfDeployedUnmanagedVApps',
        'is_thin_provisioned': 'isThinProvisioned',
        'is_fast_provisioned': 'isFastProvisioned',
        'network_provider_type': 'networkProviderType',
        'number_of_kubernetes_policies': 'numberOfKubernetesPolicies'
    }

    def __init__(self, name=None,description=None,compute_provider_scope=None,network_provider_scope=None,is_enabled=None,cpu_allocation_mhz=None,cpu_limit_mhz=None,cpu_used_mhz=None,memory_allocation_mb=None,memory_limit_mb=None,memory_used_mb=None,storage_allocation_mb=None,storage_limit_mb=None,storage_used_mb=None,provider_vdc_name=None,provider_vdc=None,org_name=None,org=None,allocation_model=None,number_of_v_apps=None,number_of_unmanaged_v_apps=None,number_of_media=None,number_of_disks=None,number_of_v_app_templates=None,vc_name=None,is_system_vdc=None,is_busy=None,status=None,network_pool=None,number_of_resource_pools=None,number_of_storage_profiles=None,used_networks_in_vdc=None,number_of_v_ms=None,network_pool_universal_id=None,number_of_running_v_ms=None,number_of_deployed_v_apps=None,number_of_deployed_unmanaged_v_apps=None,is_thin_provisioned=None,is_fast_provisioned=None,network_provider_type=None,number_of_kubernetes_policies=None):
        self._name = None
        self._description = None
        self._compute_provider_scope = None
        self._network_provider_scope = None
        self._is_enabled = None
        self._cpu_allocation_mhz = None
        self._cpu_limit_mhz = None
        self._cpu_used_mhz = None
        self._memory_allocation_mb = None
        self._memory_limit_mb = None
        self._memory_used_mb = None
        self._storage_allocation_mb = None
        self._storage_limit_mb = None
        self._storage_used_mb = None
        self._provider_vdc_name = None
        self._provider_vdc = None
        self._org_name = None
        self._org = None
        self._allocation_model = None
        self._number_of_v_apps = None
        self._number_of_unmanaged_v_apps = None
        self._number_of_media = None
        self._number_of_disks = None
        self._number_of_v_app_templates = None
        self._vc_name = None
        self._is_system_vdc = None
        self._is_busy = None
        self._status = None
        self._network_pool = None
        self._number_of_resource_pools = None
        self._number_of_storage_profiles = None
        self._used_networks_in_vdc = None
        self._number_of_v_ms = None
        self._network_pool_universal_id = None
        self._number_of_running_v_ms = None
        self._number_of_deployed_v_apps = None
        self._number_of_deployed_unmanaged_v_apps = None
        self._is_thin_provisioned = None
        self._is_fast_provisioned = None
        self._network_provider_type = None
        self._number_of_kubernetes_policies = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if compute_provider_scope is not None:
            self.compute_provider_scope = compute_provider_scope
        if network_provider_scope is not None:
            self.network_provider_scope = network_provider_scope
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if cpu_allocation_mhz is not None:
            self.cpu_allocation_mhz = cpu_allocation_mhz
        if cpu_limit_mhz is not None:
            self.cpu_limit_mhz = cpu_limit_mhz
        if cpu_used_mhz is not None:
            self.cpu_used_mhz = cpu_used_mhz
        if memory_allocation_mb is not None:
            self.memory_allocation_mb = memory_allocation_mb
        if memory_limit_mb is not None:
            self.memory_limit_mb = memory_limit_mb
        if memory_used_mb is not None:
            self.memory_used_mb = memory_used_mb
        if storage_allocation_mb is not None:
            self.storage_allocation_mb = storage_allocation_mb
        if storage_limit_mb is not None:
            self.storage_limit_mb = storage_limit_mb
        if storage_used_mb is not None:
            self.storage_used_mb = storage_used_mb
        if provider_vdc_name is not None:
            self.provider_vdc_name = provider_vdc_name
        if provider_vdc is not None:
            self.provider_vdc = provider_vdc
        if org_name is not None:
            self.org_name = org_name
        if org is not None:
            self.org = org
        if allocation_model is not None:
            self.allocation_model = allocation_model
        if number_of_v_apps is not None:
            self.number_of_v_apps = number_of_v_apps
        if number_of_unmanaged_v_apps is not None:
            self.number_of_unmanaged_v_apps = number_of_unmanaged_v_apps
        if number_of_media is not None:
            self.number_of_media = number_of_media
        if number_of_disks is not None:
            self.number_of_disks = number_of_disks
        if number_of_v_app_templates is not None:
            self.number_of_v_app_templates = number_of_v_app_templates
        if vc_name is not None:
            self.vc_name = vc_name
        if is_system_vdc is not None:
            self.is_system_vdc = is_system_vdc
        if is_busy is not None:
            self.is_busy = is_busy
        if status is not None:
            self.status = status
        if network_pool is not None:
            self.network_pool = network_pool
        if number_of_resource_pools is not None:
            self.number_of_resource_pools = number_of_resource_pools
        if number_of_storage_profiles is not None:
            self.number_of_storage_profiles = number_of_storage_profiles
        if used_networks_in_vdc is not None:
            self.used_networks_in_vdc = used_networks_in_vdc
        if number_of_v_ms is not None:
            self.number_of_v_ms = number_of_v_ms
        if network_pool_universal_id is not None:
            self.network_pool_universal_id = network_pool_universal_id
        if number_of_running_v_ms is not None:
            self.number_of_running_v_ms = number_of_running_v_ms
        if number_of_deployed_v_apps is not None:
            self.number_of_deployed_v_apps = number_of_deployed_v_apps
        if number_of_deployed_unmanaged_v_apps is not None:
            self.number_of_deployed_unmanaged_v_apps = number_of_deployed_unmanaged_v_apps
        if is_thin_provisioned is not None:
            self.is_thin_provisioned = is_thin_provisioned
        if is_fast_provisioned is not None:
            self.is_fast_provisioned = is_fast_provisioned
        if network_provider_type is not None:
            self.network_provider_type = network_provider_type
        if number_of_kubernetes_policies is not None:
            self.number_of_kubernetes_policies = number_of_kubernetes_policies

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        self._description = description

    @property
    def compute_provider_scope(self):
        return self._compute_provider_scope
    
    @compute_provider_scope.setter
    def compute_provider_scope(self, compute_provider_scope):
        self._compute_provider_scope = compute_provider_scope

    @property
    def network_provider_scope(self):
        return self._network_provider_scope
    
    @network_provider_scope.setter
    def network_provider_scope(self, network_provider_scope):
        self._network_provider_scope = network_provider_scope

    @property
    def is_enabled(self):
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self, is_enabled):
        self._is_enabled = is_enabled

    @property
    def cpu_allocation_mhz(self):
        return self._cpu_allocation_mhz
    
    @cpu_allocation_mhz.setter
    def cpu_allocation_mhz(self, cpu_allocation_mhz):
        self._cpu_allocation_mhz = cpu_allocation_mhz

    @property
    def cpu_limit_mhz(self):
        return self._cpu_limit_mhz
    
    @cpu_limit_mhz.setter
    def cpu_limit_mhz(self, cpu_limit_mhz):
        self._cpu_limit_mhz = cpu_limit_mhz

    @property
    def cpu_used_mhz(self):
        return self._cpu_used_mhz
    
    @cpu_used_mhz.setter
    def cpu_used_mhz(self, cpu_used_mhz):
        self._cpu_used_mhz = cpu_used_mhz

    @property
    def memory_allocation_mb(self):
        return self._memory_allocation_mb
    
    @memory_allocation_mb.setter
    def memory_allocation_mb(self, memory_allocation_mb):
        self._memory_allocation_mb = memory_allocation_mb

    @property
    def memory_limit_mb(self):
        return self._memory_limit_mb
    
    @memory_limit_mb.setter
    def memory_limit_mb(self, memory_limit_mb):
        self._memory_limit_mb = memory_limit_mb

    @property
    def memory_used_mb(self):
        return self._memory_used_mb
    
    @memory_used_mb.setter
    def memory_used_mb(self, memory_used_mb):
        self._memory_used_mb = memory_used_mb

    @property
    def storage_allocation_mb(self):
        return self._storage_allocation_mb
    
    @storage_allocation_mb.setter
    def storage_allocation_mb(self, storage_allocation_mb):
        self._storage_allocation_mb = storage_allocation_mb

    @property
    def storage_limit_mb(self):
        return self._storage_limit_mb
    
    @storage_limit_mb.setter
    def storage_limit_mb(self, storage_limit_mb):
        self._storage_limit_mb = storage_limit_mb

    @property
    def storage_used_mb(self):
        return self._storage_used_mb
    
    @storage_used_mb.setter
    def storage_used_mb(self, storage_used_mb):
        self._storage_used_mb = storage_used_mb

    @property
    def provider_vdc_name(self):
        return self._provider_vdc_name
    
    @provider_vdc_name.setter
    def provider_vdc_name(self, provider_vdc_name):
        self._provider_vdc_name = provider_vdc_name

    @property
    def provider_vdc(self):
        return self._provider_vdc
    
    @provider_vdc.setter
    def provider_vdc(self, provider_vdc):
        self._provider_vdc = provider_vdc

    @property
    def org_name(self):
        return self._org_name
    
    @org_name.setter
    def org_name(self, org_name):
        self._org_name = org_name

    @property
    def org(self):
        return self._org
    
    @org.setter
    def org(self, org):
        self._org = org

    @property
    def allocation_model(self):
        return self._allocation_model
    
    @allocation_model.setter
    def allocation_model(self, allocation_model):
        self._allocation_model = allocation_model

    @property
    def number_of_v_apps(self):
        return self._number_of_v_apps
    
    @number_of_v_apps.setter
    def number_of_v_apps(self, number_of_v_apps):
        self._number_of_v_apps = number_of_v_apps

    @property
    def number_of_unmanaged_v_apps(self):
        return self._number_of_unmanaged_v_apps
    
    @number_of_unmanaged_v_apps.setter
    def number_of_unmanaged_v_apps(self, number_of_unmanaged_v_apps):
        self._number_of_unmanaged_v_apps = number_of_unmanaged_v_apps

    @property
    def number_of_media(self):
        return self._number_of_media
    
    @number_of_media.setter
    def number_of_media(self, number_of_media):
        self._number_of_media = number_of_media

    @property
    def number_of_disks(self):
        return self._number_of_disks
    
    @number_of_disks.setter
    def number_of_disks(self, number_of_disks):
        self._number_of_disks = number_of_disks

    @property
    def number_of_v_app_templates(self):
        return self._number_of_v_app_templates
    
    @number_of_v_app_templates.setter
    def number_of_v_app_templates(self, number_of_v_app_templates):
        self._number_of_v_app_templates = number_of_v_app_templates

    @property
    def vc_name(self):
        return self._vc_name
    
    @vc_name.setter
    def vc_name(self, vc_name):
        self._vc_name = vc_name

    @property
    def is_system_vdc(self):
        return self._is_system_vdc
    
    @is_system_vdc.setter
    def is_system_vdc(self, is_system_vdc):
        self._is_system_vdc = is_system_vdc

    @property
    def is_busy(self):
        return self._is_busy
    
    @is_busy.setter
    def is_busy(self, is_busy):
        self._is_busy = is_busy

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, status):
        self._status = status

    @property
    def network_pool(self):
        return self._network_pool
    
    @network_pool.setter
    def network_pool(self, network_pool):
        self._network_pool = network_pool

    @property
    def number_of_resource_pools(self):
        return self._number_of_resource_pools
    
    @number_of_resource_pools.setter
    def number_of_resource_pools(self, number_of_resource_pools):
        self._number_of_resource_pools = number_of_resource_pools

    @property
    def number_of_storage_profiles(self):
        return self._number_of_storage_profiles
    
    @number_of_storage_profiles.setter
    def number_of_storage_profiles(self, number_of_storage_profiles):
        self._number_of_storage_profiles = number_of_storage_profiles

    @property
    def used_networks_in_vdc(self):
        return self._used_networks_in_vdc
    
    @used_networks_in_vdc.setter
    def used_networks_in_vdc(self, used_networks_in_vdc):
        self._used_networks_in_vdc = used_networks_in_vdc

    @property
    def number_of_v_ms(self):
        return self._number_of_v_ms
    
    @number_of_v_ms.setter
    def number_of_v_ms(self, number_of_v_ms):
        self._number_of_v_ms = number_of_v_ms

    @property
    def network_pool_universal_id(self):
        return self._network_pool_universal_id
    
    @network_pool_universal_id.setter
    def network_pool_universal_id(self, network_pool_universal_id):
        self._network_pool_universal_id = network_pool_universal_id

    @property
    def number_of_running_v_ms(self):
        return self._number_of_running_v_ms
    
    @number_of_running_v_ms.setter
    def number_of_running_v_ms(self, number_of_running_v_ms):
        self._number_of_running_v_ms = number_of_running_v_ms

    @property
    def number_of_deployed_v_apps(self):
        return self._number_of_deployed_v_apps
    
    @number_of_deployed_v_apps.setter
    def number_of_deployed_v_apps(self, number_of_deployed_v_apps):
        self._number_of_deployed_v_apps = number_of_deployed_v_apps

    @property
    def number_of_deployed_unmanaged_v_apps(self):
        return self._number_of_deployed_unmanaged_v_apps
    
    @number_of_deployed_unmanaged_v_apps.setter
    def number_of_deployed_unmanaged_v_apps(self, number_of_deployed_unmanaged_v_apps):
        self._number_of_deployed_unmanaged_v_apps = number_of_deployed_unmanaged_v_apps

    @property
    def is_thin_provisioned(self):
        return self._is_thin_provisioned
    
    @is_thin_provisioned.setter
    def is_thin_provisioned(self, is_thin_provisioned):
        self._is_thin_provisioned = is_thin_provisioned

    @property
    def is_fast_provisioned(self):
        return self._is_fast_provisioned
    
    @is_fast_provisioned.setter
    def is_fast_provisioned(self, is_fast_provisioned):
        self._is_fast_provisioned = is_fast_provisioned

    @property
    def network_provider_type(self):
        return self._network_provider_type
    
    @network_provider_type.setter
    def network_provider_type(self, network_provider_type):
        self._network_provider_type = network_provider_type

    @property
    def number_of_kubernetes_policies(self):
        return self._number_of_kubernetes_policies
    
    @number_of_kubernetes_policies.setter
    def number_of_kubernetes_policies(self, number_of_kubernetes_policies):
        self._number_of_kubernetes_policies = number_of_kubernetes_policies


    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, QueryResultAdminVdcRecordType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
