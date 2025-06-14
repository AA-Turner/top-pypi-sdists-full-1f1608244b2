# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 66.26.0-v202506111109-CD
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class ItemParameterOfOutputV1(object):
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
        'ancestors': 'list[ItemPreviewV1]',
        'has_children': 'bool',
        'id': 'str',
        'is_archived': 'bool',
        'is_generated': 'bool',
        'is_redacted': 'bool',
        'name': 'str',
        'parameter_of': 'list[ItemPreviewWithAssetsV1]',
        'translation_key': 'str',
        'type': 'str'
    }

    attribute_map = {
        'ancestors': 'ancestors',
        'has_children': 'hasChildren',
        'id': 'id',
        'is_archived': 'isArchived',
        'is_generated': 'isGenerated',
        'is_redacted': 'isRedacted',
        'name': 'name',
        'parameter_of': 'parameterOf',
        'translation_key': 'translationKey',
        'type': 'type'
    }

    def __init__(self, ancestors=None, has_children=False, id=None, is_archived=False, is_generated=False, is_redacted=False, name=None, parameter_of=None, translation_key=None, type=None):
        """
        ItemParameterOfOutputV1 - a model defined in Swagger
        """

        self._ancestors = None
        self._has_children = None
        self._id = None
        self._is_archived = None
        self._is_generated = None
        self._is_redacted = None
        self._name = None
        self._parameter_of = None
        self._translation_key = None
        self._type = None

        if ancestors is not None:
          self.ancestors = ancestors
        if has_children is not None:
          self.has_children = has_children
        if id is not None:
          self.id = id
        if is_archived is not None:
          self.is_archived = is_archived
        if is_generated is not None:
          self.is_generated = is_generated
        if is_redacted is not None:
          self.is_redacted = is_redacted
        if name is not None:
          self.name = name
        if parameter_of is not None:
          self.parameter_of = parameter_of
        if translation_key is not None:
          self.translation_key = translation_key
        if type is not None:
          self.type = type

    @property
    def ancestors(self):
        """
        Gets the ancestors of this ItemParameterOfOutputV1.
        The list of ancestors in the asset tree, ordered with the root ancestor first, if the item is in an asset tree. If an item is in more than one asset tree an arbitrary one will be chosen.

        :return: The ancestors of this ItemParameterOfOutputV1.
        :rtype: list[ItemPreviewV1]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this ItemParameterOfOutputV1.
        The list of ancestors in the asset tree, ordered with the root ancestor first, if the item is in an asset tree. If an item is in more than one asset tree an arbitrary one will be chosen.

        :param ancestors: The ancestors of this ItemParameterOfOutputV1.
        :type: list[ItemPreviewV1]
        """

        self._ancestors = ancestors

    @property
    def has_children(self):
        """
        Gets the has_children of this ItemParameterOfOutputV1.
        A boolean indicating whether or not child items exist for this item in the asset tree; the value will be true even if the child items are archived unless the tree for this item is deleted.

        :return: The has_children of this ItemParameterOfOutputV1.
        :rtype: bool
        """
        return self._has_children

    @has_children.setter
    def has_children(self, has_children):
        """
        Sets the has_children of this ItemParameterOfOutputV1.
        A boolean indicating whether or not child items exist for this item in the asset tree; the value will be true even if the child items are archived unless the tree for this item is deleted.

        :param has_children: The has_children of this ItemParameterOfOutputV1.
        :type: bool
        """

        self._has_children = has_children

    @property
    def id(self):
        """
        Gets the id of this ItemParameterOfOutputV1.
        The ID that can be used to interact with the item

        :return: The id of this ItemParameterOfOutputV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ItemParameterOfOutputV1.
        The ID that can be used to interact with the item

        :param id: The id of this ItemParameterOfOutputV1.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def is_archived(self):
        """
        Gets the is_archived of this ItemParameterOfOutputV1.
        Whether item is archived

        :return: The is_archived of this ItemParameterOfOutputV1.
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """
        Sets the is_archived of this ItemParameterOfOutputV1.
        Whether item is archived

        :param is_archived: The is_archived of this ItemParameterOfOutputV1.
        :type: bool
        """

        self._is_archived = is_archived

    @property
    def is_generated(self):
        """
        Gets the is_generated of this ItemParameterOfOutputV1.
        Whether the item is generated

        :return: The is_generated of this ItemParameterOfOutputV1.
        :rtype: bool
        """
        return self._is_generated

    @is_generated.setter
    def is_generated(self, is_generated):
        """
        Sets the is_generated of this ItemParameterOfOutputV1.
        Whether the item is generated

        :param is_generated: The is_generated of this ItemParameterOfOutputV1.
        :type: bool
        """

        self._is_generated = is_generated

    @property
    def is_redacted(self):
        """
        Gets the is_redacted of this ItemParameterOfOutputV1.
        Whether item is redacted

        :return: The is_redacted of this ItemParameterOfOutputV1.
        :rtype: bool
        """
        return self._is_redacted

    @is_redacted.setter
    def is_redacted(self, is_redacted):
        """
        Sets the is_redacted of this ItemParameterOfOutputV1.
        Whether item is redacted

        :param is_redacted: The is_redacted of this ItemParameterOfOutputV1.
        :type: bool
        """

        self._is_redacted = is_redacted

    @property
    def name(self):
        """
        Gets the name of this ItemParameterOfOutputV1.
        The human readable name

        :return: The name of this ItemParameterOfOutputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ItemParameterOfOutputV1.
        The human readable name

        :param name: The name of this ItemParameterOfOutputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def parameter_of(self):
        """
        Gets the parameter_of of this ItemParameterOfOutputV1.
        Formula items in the dependency list that use this item

        :return: The parameter_of of this ItemParameterOfOutputV1.
        :rtype: list[ItemPreviewWithAssetsV1]
        """
        return self._parameter_of

    @parameter_of.setter
    def parameter_of(self, parameter_of):
        """
        Sets the parameter_of of this ItemParameterOfOutputV1.
        Formula items in the dependency list that use this item

        :param parameter_of: The parameter_of of this ItemParameterOfOutputV1.
        :type: list[ItemPreviewWithAssetsV1]
        """

        self._parameter_of = parameter_of

    @property
    def translation_key(self):
        """
        Gets the translation_key of this ItemParameterOfOutputV1.
        The item's translation key, if any

        :return: The translation_key of this ItemParameterOfOutputV1.
        :rtype: str
        """
        return self._translation_key

    @translation_key.setter
    def translation_key(self, translation_key):
        """
        Sets the translation_key of this ItemParameterOfOutputV1.
        The item's translation key, if any

        :param translation_key: The translation_key of this ItemParameterOfOutputV1.
        :type: str
        """

        self._translation_key = translation_key

    @property
    def type(self):
        """
        Gets the type of this ItemParameterOfOutputV1.
        The type of the item

        :return: The type of this ItemParameterOfOutputV1.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ItemParameterOfOutputV1.
        The type of the item

        :param type: The type of this ItemParameterOfOutputV1.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ItemParameterOfOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
