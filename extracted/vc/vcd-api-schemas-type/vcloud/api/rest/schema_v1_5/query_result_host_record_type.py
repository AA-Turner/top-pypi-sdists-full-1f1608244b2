"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re
from .query_result_record_type import QueryResultRecordType


class QueryResultHostRecordType(QueryResultRecordType):
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
        'is_enabled': 'bool',
        'is_deleted': 'bool',
        'is_busy': 'bool',
        'is_prepared': 'bool',
        'is_supported': 'bool',
        'is_hung': 'bool',
        'is_pending_upgrade': 'bool',
        'state': 'int',
        'os_version': 'str',
        'is_cross_host_enabled': 'bool',
        'number_of_v_ms': 'int',
        'is_in_maintenance_mode': 'bool',
        'connection_state': 'str',
        'vc': 'str',
        'vc_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'is_enabled': 'isEnabled',
        'is_deleted': 'isDeleted',
        'is_busy': 'isBusy',
        'is_prepared': 'isPrepared',
        'is_supported': 'isSupported',
        'is_hung': 'isHung',
        'is_pending_upgrade': 'isPendingUpgrade',
        'state': 'state',
        'os_version': 'osVersion',
        'is_cross_host_enabled': 'isCrossHostEnabled',
        'number_of_v_ms': 'numberOfVMs',
        'is_in_maintenance_mode': 'isInMaintenanceMode',
        'connection_state': 'connectionState',
        'vc': 'vc',
        'vc_name': 'vcName'
    }

    def __init__(self, name=None,is_enabled=None,is_deleted=None,is_busy=None,is_prepared=None,is_supported=None,is_hung=None,is_pending_upgrade=None,state=None,os_version=None,is_cross_host_enabled=None,number_of_v_ms=None,is_in_maintenance_mode=None,connection_state=None,vc=None,vc_name=None):
        self._name = None
        self._is_enabled = None
        self._is_deleted = None
        self._is_busy = None
        self._is_prepared = None
        self._is_supported = None
        self._is_hung = None
        self._is_pending_upgrade = None
        self._state = None
        self._os_version = None
        self._is_cross_host_enabled = None
        self._number_of_v_ms = None
        self._is_in_maintenance_mode = None
        self._connection_state = None
        self._vc = None
        self._vc_name = None

        if name is not None:
            self.name = name
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if is_busy is not None:
            self.is_busy = is_busy
        if is_prepared is not None:
            self.is_prepared = is_prepared
        if is_supported is not None:
            self.is_supported = is_supported
        if is_hung is not None:
            self.is_hung = is_hung
        if is_pending_upgrade is not None:
            self.is_pending_upgrade = is_pending_upgrade
        if state is not None:
            self.state = state
        if os_version is not None:
            self.os_version = os_version
        if is_cross_host_enabled is not None:
            self.is_cross_host_enabled = is_cross_host_enabled
        if number_of_v_ms is not None:
            self.number_of_v_ms = number_of_v_ms
        if is_in_maintenance_mode is not None:
            self.is_in_maintenance_mode = is_in_maintenance_mode
        if connection_state is not None:
            self.connection_state = connection_state
        if vc is not None:
            self.vc = vc
        if vc_name is not None:
            self.vc_name = vc_name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def is_enabled(self):
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self, is_enabled):
        self._is_enabled = is_enabled

    @property
    def is_deleted(self):
        return self._is_deleted
    
    @is_deleted.setter
    def is_deleted(self, is_deleted):
        self._is_deleted = is_deleted

    @property
    def is_busy(self):
        return self._is_busy
    
    @is_busy.setter
    def is_busy(self, is_busy):
        self._is_busy = is_busy

    @property
    def is_prepared(self):
        return self._is_prepared
    
    @is_prepared.setter
    def is_prepared(self, is_prepared):
        self._is_prepared = is_prepared

    @property
    def is_supported(self):
        return self._is_supported
    
    @is_supported.setter
    def is_supported(self, is_supported):
        self._is_supported = is_supported

    @property
    def is_hung(self):
        return self._is_hung
    
    @is_hung.setter
    def is_hung(self, is_hung):
        self._is_hung = is_hung

    @property
    def is_pending_upgrade(self):
        return self._is_pending_upgrade
    
    @is_pending_upgrade.setter
    def is_pending_upgrade(self, is_pending_upgrade):
        self._is_pending_upgrade = is_pending_upgrade

    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, state):
        self._state = state

    @property
    def os_version(self):
        return self._os_version
    
    @os_version.setter
    def os_version(self, os_version):
        self._os_version = os_version

    @property
    def is_cross_host_enabled(self):
        return self._is_cross_host_enabled
    
    @is_cross_host_enabled.setter
    def is_cross_host_enabled(self, is_cross_host_enabled):
        self._is_cross_host_enabled = is_cross_host_enabled

    @property
    def number_of_v_ms(self):
        return self._number_of_v_ms
    
    @number_of_v_ms.setter
    def number_of_v_ms(self, number_of_v_ms):
        self._number_of_v_ms = number_of_v_ms

    @property
    def is_in_maintenance_mode(self):
        return self._is_in_maintenance_mode
    
    @is_in_maintenance_mode.setter
    def is_in_maintenance_mode(self, is_in_maintenance_mode):
        self._is_in_maintenance_mode = is_in_maintenance_mode

    @property
    def connection_state(self):
        return self._connection_state
    
    @connection_state.setter
    def connection_state(self, connection_state):
        self._connection_state = connection_state

    @property
    def vc(self):
        return self._vc
    
    @vc.setter
    def vc(self, vc):
        self._vc = vc

    @property
    def vc_name(self):
        return self._vc_name
    
    @vc_name.setter
    def vc_name(self, vc_name):
        self._vc_name = vc_name


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
        if not isinstance(other, QueryResultHostRecordType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
