"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re
from .entity_type import EntityType


class CatalogType(EntityType):
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
        'owner': 'OwnerType',
        'catalog_items': 'CatalogItemsType',
        'is_published': 'bool',
        'date_created': 'str',
        'version_number': 'int'
    }

    attribute_map = {
        'owner': 'owner',
        'catalog_items': 'catalogItems',
        'is_published': 'isPublished',
        'date_created': 'dateCreated',
        'version_number': 'versionNumber'
    }

    def __init__(self, owner=None,catalog_items=None,is_published=None,date_created=None,version_number=None):
        self._owner = None
        self._catalog_items = None
        self._is_published = None
        self._date_created = None
        self._version_number = None

        if owner is not None:
            self.owner = owner
        if catalog_items is not None:
            self.catalog_items = catalog_items
        if is_published is not None:
            self.is_published = is_published
        if date_created is not None:
            self.date_created = date_created
        if version_number is not None:
            self.version_number = version_number

    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, owner):
        self._owner = owner

    @property
    def catalog_items(self):
        return self._catalog_items
    
    @catalog_items.setter
    def catalog_items(self, catalog_items):
        self._catalog_items = catalog_items

    @property
    def is_published(self):
        return self._is_published
    
    @is_published.setter
    def is_published(self, is_published):
        self._is_published = is_published

    @property
    def date_created(self):
        return self._date_created
    
    @date_created.setter
    def date_created(self, date_created):
        self._date_created = date_created

    @property
    def version_number(self):
        return self._version_number
    
    @version_number.setter
    def version_number(self, version_number):
        self._version_number = version_number


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
        if not isinstance(other, CatalogType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
