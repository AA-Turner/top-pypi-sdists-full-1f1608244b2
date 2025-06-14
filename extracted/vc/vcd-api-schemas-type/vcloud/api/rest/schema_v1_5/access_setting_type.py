"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re
from .v_cloud_extensible_type import VCloudExtensibleType


class AccessSettingType(VCloudExtensibleType):
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
        'subject': 'ReferenceType',
        'external_subject': 'ExternalSubjectType',
        'access_level': 'str'
    }

    attribute_map = {
        'subject': 'subject',
        'external_subject': 'externalSubject',
        'access_level': 'accessLevel'
    }

    def __init__(self, subject=None,external_subject=None,access_level=None):
        self._subject = None
        self._external_subject = None
        self._access_level = None

        if subject is not None:
            self.subject = subject
        if external_subject is not None:
            self.external_subject = external_subject
        if access_level is not None:
            self.access_level = access_level

    @property
    def subject(self):
        return self._subject
    
    @subject.setter
    def subject(self, subject):
        self._subject = subject

    @property
    def external_subject(self):
        return self._external_subject
    
    @external_subject.setter
    def external_subject(self, external_subject):
        self._external_subject = external_subject

    @property
    def access_level(self):
        return self._access_level
    
    @access_level.setter
    def access_level(self, access_level):
        self._access_level = access_level


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
        if not isinstance(other, AccessSettingType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
