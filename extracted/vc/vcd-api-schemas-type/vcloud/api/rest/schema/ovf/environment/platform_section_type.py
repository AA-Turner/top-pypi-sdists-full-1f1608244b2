"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re
from .section_type import SectionType


class PlatformSectionType(SectionType):
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
        'kind': 'CimString',
        'version': 'CimString',
        'vendor': 'CimString',
        'locale': 'CimString',
        'timezone': 'int',
        'any': 'list[object]'
    }

    attribute_map = {
        'kind': 'kind',
        'version': 'version',
        'vendor': 'vendor',
        'locale': 'locale',
        'timezone': 'timezone',
        'any': 'any'
    }

    def __init__(self, kind=None,version=None,vendor=None,locale=None,timezone=None,any=None):
        self._kind = None
        self._version = None
        self._vendor = None
        self._locale = None
        self._timezone = None
        self._any = None

        if kind is not None:
            self.kind = kind
        if version is not None:
            self.version = version
        if vendor is not None:
            self.vendor = vendor
        if locale is not None:
            self.locale = locale
        if timezone is not None:
            self.timezone = timezone
        if any is not None:
            self.any = any

    @property
    def kind(self):
        return self._kind
    
    @kind.setter
    def kind(self, kind):
        self._kind = kind

    @property
    def version(self):
        return self._version
    
    @version.setter
    def version(self, version):
        self._version = version

    @property
    def vendor(self):
        return self._vendor
    
    @vendor.setter
    def vendor(self, vendor):
        self._vendor = vendor

    @property
    def locale(self):
        return self._locale
    
    @locale.setter
    def locale(self, locale):
        self._locale = locale

    @property
    def timezone(self):
        return self._timezone
    
    @timezone.setter
    def timezone(self, timezone):
        self._timezone = timezone

    @property
    def any(self):
        return self._any
    
    @any.setter
    def any(self, any):
        self._any = any


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
        if not isinstance(other, PlatformSectionType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
