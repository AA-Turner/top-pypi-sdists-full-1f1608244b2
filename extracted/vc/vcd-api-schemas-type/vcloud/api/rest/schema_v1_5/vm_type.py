"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re
from .abstract_v_app_type import AbstractVAppType


class VmType(AbstractVAppType):
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
        'v_app_scoped_local_id': 'str',
        'environment': 'EnvironmentType',
        'vm_capabilities': 'VmCapabilitiesType',
        'storage_profile': 'ReferenceType',
        'vdc_compute_policy': 'ReferenceType',
        'compute_policy': 'ComputePolicyType',
        'compute_policy_compliance': 'list[ComputePolicyComplianceType]',
        'is_compute_policy_compliant': 'bool',
        'boot_options': 'BootOptionsType',
        'media': 'ReferenceType',
        'encrypted': 'bool',
        'needs_customization': 'bool',
        'nested_hypervisor_enabled': 'bool'
    }

    attribute_map = {
        'v_app_scoped_local_id': 'vAppScopedLocalId',
        'environment': 'environment',
        'vm_capabilities': 'vmCapabilities',
        'storage_profile': 'storageProfile',
        'vdc_compute_policy': 'vdcComputePolicy',
        'compute_policy': 'computePolicy',
        'compute_policy_compliance': 'computePolicyCompliance',
        'is_compute_policy_compliant': 'isComputePolicyCompliant',
        'boot_options': 'bootOptions',
        'media': 'media',
        'encrypted': 'encrypted',
        'needs_customization': 'needsCustomization',
        'nested_hypervisor_enabled': 'nestedHypervisorEnabled'
    }

    def __init__(self, v_app_scoped_local_id=None,environment=None,vm_capabilities=None,storage_profile=None,vdc_compute_policy=None,compute_policy=None,compute_policy_compliance=None,is_compute_policy_compliant=None,boot_options=None,media=None,encrypted=None,needs_customization=None,nested_hypervisor_enabled=None):
        self._v_app_scoped_local_id = None
        self._environment = None
        self._vm_capabilities = None
        self._storage_profile = None
        self._vdc_compute_policy = None
        self._compute_policy = None
        self._compute_policy_compliance = None
        self._is_compute_policy_compliant = None
        self._boot_options = None
        self._media = None
        self._encrypted = None
        self._needs_customization = None
        self._nested_hypervisor_enabled = None

        if v_app_scoped_local_id is not None:
            self.v_app_scoped_local_id = v_app_scoped_local_id
        if environment is not None:
            self.environment = environment
        if vm_capabilities is not None:
            self.vm_capabilities = vm_capabilities
        if storage_profile is not None:
            self.storage_profile = storage_profile
        if vdc_compute_policy is not None:
            self.vdc_compute_policy = vdc_compute_policy
        if compute_policy is not None:
            self.compute_policy = compute_policy
        if compute_policy_compliance is not None:
            self.compute_policy_compliance = compute_policy_compliance
        if is_compute_policy_compliant is not None:
            self.is_compute_policy_compliant = is_compute_policy_compliant
        if boot_options is not None:
            self.boot_options = boot_options
        if media is not None:
            self.media = media
        if encrypted is not None:
            self.encrypted = encrypted
        if needs_customization is not None:
            self.needs_customization = needs_customization
        if nested_hypervisor_enabled is not None:
            self.nested_hypervisor_enabled = nested_hypervisor_enabled

    @property
    def v_app_scoped_local_id(self):
        return self._v_app_scoped_local_id
    
    @v_app_scoped_local_id.setter
    def v_app_scoped_local_id(self, v_app_scoped_local_id):
        self._v_app_scoped_local_id = v_app_scoped_local_id

    @property
    def environment(self):
        return self._environment
    
    @environment.setter
    def environment(self, environment):
        self._environment = environment

    @property
    def vm_capabilities(self):
        return self._vm_capabilities
    
    @vm_capabilities.setter
    def vm_capabilities(self, vm_capabilities):
        self._vm_capabilities = vm_capabilities

    @property
    def storage_profile(self):
        return self._storage_profile
    
    @storage_profile.setter
    def storage_profile(self, storage_profile):
        self._storage_profile = storage_profile

    @property
    def vdc_compute_policy(self):
        return self._vdc_compute_policy
    
    @vdc_compute_policy.setter
    def vdc_compute_policy(self, vdc_compute_policy):
        self._vdc_compute_policy = vdc_compute_policy

    @property
    def compute_policy(self):
        return self._compute_policy
    
    @compute_policy.setter
    def compute_policy(self, compute_policy):
        self._compute_policy = compute_policy

    @property
    def compute_policy_compliance(self):
        return self._compute_policy_compliance
    
    @compute_policy_compliance.setter
    def compute_policy_compliance(self, compute_policy_compliance):
        self._compute_policy_compliance = compute_policy_compliance

    @property
    def is_compute_policy_compliant(self):
        return self._is_compute_policy_compliant
    
    @is_compute_policy_compliant.setter
    def is_compute_policy_compliant(self, is_compute_policy_compliant):
        self._is_compute_policy_compliant = is_compute_policy_compliant

    @property
    def boot_options(self):
        return self._boot_options
    
    @boot_options.setter
    def boot_options(self, boot_options):
        self._boot_options = boot_options

    @property
    def media(self):
        return self._media
    
    @media.setter
    def media(self, media):
        self._media = media

    @property
    def encrypted(self):
        return self._encrypted
    
    @encrypted.setter
    def encrypted(self, encrypted):
        self._encrypted = encrypted

    @property
    def needs_customization(self):
        return self._needs_customization
    
    @needs_customization.setter
    def needs_customization(self, needs_customization):
        self._needs_customization = needs_customization

    @property
    def nested_hypervisor_enabled(self):
        return self._nested_hypervisor_enabled
    
    @nested_hypervisor_enabled.setter
    def nested_hypervisor_enabled(self, nested_hypervisor_enabled):
        self._nested_hypervisor_enabled = nested_hypervisor_enabled


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
        if not isinstance(other, VmType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
