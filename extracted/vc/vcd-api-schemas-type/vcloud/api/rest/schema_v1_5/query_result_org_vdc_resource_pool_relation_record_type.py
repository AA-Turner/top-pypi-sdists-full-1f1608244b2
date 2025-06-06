"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re
from .query_result_record_type import QueryResultRecordType


class QueryResultOrgVdcResourcePoolRelationRecordType(QueryResultRecordType):
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
        'vdc': 'str',
        'vc': 'str',
        'resource_pool_moref': 'str',
        'vc_name': 'str',
        'resource_pool_name': 'str'
    }

    attribute_map = {
        'vdc': 'vdc',
        'vc': 'vc',
        'resource_pool_moref': 'resourcePoolMoref',
        'vc_name': 'vcName',
        'resource_pool_name': 'resourcePoolName'
    }

    def __init__(self, vdc=None,vc=None,resource_pool_moref=None,vc_name=None,resource_pool_name=None):
        self._vdc = None
        self._vc = None
        self._resource_pool_moref = None
        self._vc_name = None
        self._resource_pool_name = None

        if vdc is not None:
            self.vdc = vdc
        if vc is not None:
            self.vc = vc
        if resource_pool_moref is not None:
            self.resource_pool_moref = resource_pool_moref
        if vc_name is not None:
            self.vc_name = vc_name
        if resource_pool_name is not None:
            self.resource_pool_name = resource_pool_name

    @property
    def vdc(self):
        return self._vdc
    
    @vdc.setter
    def vdc(self, vdc):
        self._vdc = vdc

    @property
    def vc(self):
        return self._vc
    
    @vc.setter
    def vc(self, vc):
        self._vc = vc

    @property
    def resource_pool_moref(self):
        return self._resource_pool_moref
    
    @resource_pool_moref.setter
    def resource_pool_moref(self, resource_pool_moref):
        self._resource_pool_moref = resource_pool_moref

    @property
    def vc_name(self):
        return self._vc_name
    
    @vc_name.setter
    def vc_name(self, vc_name):
        self._vc_name = vc_name

    @property
    def resource_pool_name(self):
        return self._resource_pool_name
    
    @resource_pool_name.setter
    def resource_pool_name(self, resource_pool_name):
        self._resource_pool_name = resource_pool_name


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
        if not isinstance(other, QueryResultOrgVdcResourcePoolRelationRecordType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
