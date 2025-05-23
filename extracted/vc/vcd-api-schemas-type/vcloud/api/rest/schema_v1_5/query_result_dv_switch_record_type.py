"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re
from .query_result_record_type import QueryResultRecordType


class QueryResultDvSwitchRecordType(QueryResultRecordType):
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
        'moref': 'str',
        'name': 'str',
        'vc': 'str',
        'vc_name': 'str',
        'is_vc_enabled': 'bool'
    }

    attribute_map = {
        'moref': 'moref',
        'name': 'name',
        'vc': 'vc',
        'vc_name': 'vcName',
        'is_vc_enabled': 'isVCEnabled'
    }

    def __init__(self, moref=None,name=None,vc=None,vc_name=None,is_vc_enabled=None):
        self._moref = None
        self._name = None
        self._vc = None
        self._vc_name = None
        self._is_vc_enabled = None

        if moref is not None:
            self.moref = moref
        if name is not None:
            self.name = name
        if vc is not None:
            self.vc = vc
        if vc_name is not None:
            self.vc_name = vc_name
        if is_vc_enabled is not None:
            self.is_vc_enabled = is_vc_enabled

    @property
    def moref(self):
        return self._moref
    
    @moref.setter
    def moref(self, moref):
        self._moref = moref

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

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

    @property
    def is_vc_enabled(self):
        return self._is_vc_enabled
    
    @is_vc_enabled.setter
    def is_vc_enabled(self, is_vc_enabled):
        self._is_vc_enabled = is_vc_enabled


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
        if not isinstance(other, QueryResultDvSwitchRecordType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
