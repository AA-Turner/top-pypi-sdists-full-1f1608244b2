"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re
from .resource_type import ResourceType


class QueryResultType(ResourceType):
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
        'page_size': 'int',
        'page': 'int'
    }

    attribute_map = {
        'name': 'name',
        'page_size': 'pageSize',
        'page': 'page'
    }

    def __init__(self, name=None,page_size=None,page=None):
        self._name = None
        self._page_size = None
        self._page = None

        if name is not None:
            self.name = name
        if page_size is not None:
            self.page_size = page_size
        if page is not None:
            self.page = page

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def page_size(self):
        return self._page_size
    
    @page_size.setter
    def page_size(self, page_size):
        self._page_size = page_size

    @property
    def page(self):
        return self._page
    
    @page.setter
    def page(self, page):
        self._page = page


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
        if not isinstance(other, QueryResultType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
