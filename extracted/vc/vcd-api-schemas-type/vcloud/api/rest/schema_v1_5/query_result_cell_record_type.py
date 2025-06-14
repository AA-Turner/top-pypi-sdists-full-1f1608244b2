"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re
from .query_result_record_type import QueryResultRecordType


class QueryResultCellRecordType(QueryResultRecordType):
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
        'primary_ip': 'str',
        'name': 'str',
        'is_active': 'int',
        'is_v_mware_vc': 'int',
        'build_date': 'str',
        'version': 'str'
    }

    attribute_map = {
        'primary_ip': 'primaryIp',
        'name': 'name',
        'is_active': 'isActive',
        'is_v_mware_vc': 'isVMwareVc',
        'build_date': 'buildDate',
        'version': 'version'
    }

    def __init__(self, primary_ip=None,name=None,is_active=None,is_v_mware_vc=None,build_date=None,version=None):
        self._primary_ip = None
        self._name = None
        self._is_active = None
        self._is_v_mware_vc = None
        self._build_date = None
        self._version = None

        if primary_ip is not None:
            self.primary_ip = primary_ip
        if name is not None:
            self.name = name
        if is_active is not None:
            self.is_active = is_active
        if is_v_mware_vc is not None:
            self.is_v_mware_vc = is_v_mware_vc
        if build_date is not None:
            self.build_date = build_date
        if version is not None:
            self.version = version

    @property
    def primary_ip(self):
        return self._primary_ip
    
    @primary_ip.setter
    def primary_ip(self, primary_ip):
        self._primary_ip = primary_ip

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def is_active(self):
        return self._is_active
    
    @is_active.setter
    def is_active(self, is_active):
        self._is_active = is_active

    @property
    def is_v_mware_vc(self):
        return self._is_v_mware_vc
    
    @is_v_mware_vc.setter
    def is_v_mware_vc(self, is_v_mware_vc):
        self._is_v_mware_vc = is_v_mware_vc

    @property
    def build_date(self):
        return self._build_date
    
    @build_date.setter
    def build_date(self, build_date):
        self._build_date = build_date

    @property
    def version(self):
        return self._version
    
    @version.setter
    def version(self, version):
        self._version = version


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
        if not isinstance(other, QueryResultCellRecordType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
