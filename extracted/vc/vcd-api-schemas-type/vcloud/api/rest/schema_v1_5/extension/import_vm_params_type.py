"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re
from ..params_type import ParamsType


class ImportVmParamsType(ParamsType):
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
        'vm_name': 'str',
        'v_app_scoped_local_id': 'str',
        'computer_name': 'str',
        'vm_mo_ref': 'str',
        'vdc_storage_profile': 'ReferenceType',
        'vdc': 'ReferenceType',
        'imported_disk': 'list[ImportedDiskType]',
        'source_move': 'bool'
    }

    attribute_map = {
        'vm_name': 'vmName',
        'v_app_scoped_local_id': 'vAppScopedLocalId',
        'computer_name': 'computerName',
        'vm_mo_ref': 'vmMoRef',
        'vdc_storage_profile': 'vdcStorageProfile',
        'vdc': 'vdc',
        'imported_disk': 'importedDisk',
        'source_move': 'sourceMove'
    }

    def __init__(self, vm_name=None,v_app_scoped_local_id=None,computer_name=None,vm_mo_ref=None,vdc_storage_profile=None,vdc=None,imported_disk=None,source_move=None):
        self._vm_name = None
        self._v_app_scoped_local_id = None
        self._computer_name = None
        self._vm_mo_ref = None
        self._vdc_storage_profile = None
        self._vdc = None
        self._imported_disk = None
        self._source_move = None

        if vm_name is not None:
            self.vm_name = vm_name
        if v_app_scoped_local_id is not None:
            self.v_app_scoped_local_id = v_app_scoped_local_id
        if computer_name is not None:
            self.computer_name = computer_name
        if vm_mo_ref is not None:
            self.vm_mo_ref = vm_mo_ref
        if vdc_storage_profile is not None:
            self.vdc_storage_profile = vdc_storage_profile
        if vdc is not None:
            self.vdc = vdc
        if imported_disk is not None:
            self.imported_disk = imported_disk
        if source_move is not None:
            self.source_move = source_move

    @property
    def vm_name(self):
        return self._vm_name
    
    @vm_name.setter
    def vm_name(self, vm_name):
        self._vm_name = vm_name

    @property
    def v_app_scoped_local_id(self):
        return self._v_app_scoped_local_id
    
    @v_app_scoped_local_id.setter
    def v_app_scoped_local_id(self, v_app_scoped_local_id):
        self._v_app_scoped_local_id = v_app_scoped_local_id

    @property
    def computer_name(self):
        return self._computer_name
    
    @computer_name.setter
    def computer_name(self, computer_name):
        self._computer_name = computer_name

    @property
    def vm_mo_ref(self):
        return self._vm_mo_ref
    
    @vm_mo_ref.setter
    def vm_mo_ref(self, vm_mo_ref):
        self._vm_mo_ref = vm_mo_ref

    @property
    def vdc_storage_profile(self):
        return self._vdc_storage_profile
    
    @vdc_storage_profile.setter
    def vdc_storage_profile(self, vdc_storage_profile):
        self._vdc_storage_profile = vdc_storage_profile

    @property
    def vdc(self):
        return self._vdc
    
    @vdc.setter
    def vdc(self, vdc):
        self._vdc = vdc

    @property
    def imported_disk(self):
        return self._imported_disk
    
    @imported_disk.setter
    def imported_disk(self, imported_disk):
        self._imported_disk = imported_disk

    @property
    def source_move(self):
        return self._source_move
    
    @source_move.setter
    def source_move(self, source_move):
        self._source_move = source_move


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
        if not isinstance(other, ImportVmParamsType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
