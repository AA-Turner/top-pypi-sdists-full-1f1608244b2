# coding: utf-8

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: support@akeyless.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from akeyless.configuration import Configuration


class UIDTokenDetails(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'children': 'dict(str, UIDTokenDetails)',
        'comment': 'str',
        'deny_inheritance': 'bool',
        'deny_rotate': 'bool',
        'depth': 'int',
        'expired_date': 'str',
        'id': 'str',
        'last_rotate': 'str',
        'revoked': 'bool',
        'ttl': 'int'
    }

    attribute_map = {
        'children': 'children',
        'comment': 'comment',
        'deny_inheritance': 'deny_inheritance',
        'deny_rotate': 'deny_rotate',
        'depth': 'depth',
        'expired_date': 'expired_date',
        'id': 'id',
        'last_rotate': 'last_rotate',
        'revoked': 'revoked',
        'ttl': 'ttl'
    }

    def __init__(self, children=None, comment=None, deny_inheritance=None, deny_rotate=None, depth=None, expired_date=None, id=None, last_rotate=None, revoked=None, ttl=None, local_vars_configuration=None):  # noqa: E501
        """UIDTokenDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._children = None
        self._comment = None
        self._deny_inheritance = None
        self._deny_rotate = None
        self._depth = None
        self._expired_date = None
        self._id = None
        self._last_rotate = None
        self._revoked = None
        self._ttl = None
        self.discriminator = None

        if children is not None:
            self.children = children
        if comment is not None:
            self.comment = comment
        if deny_inheritance is not None:
            self.deny_inheritance = deny_inheritance
        if deny_rotate is not None:
            self.deny_rotate = deny_rotate
        if depth is not None:
            self.depth = depth
        if expired_date is not None:
            self.expired_date = expired_date
        if id is not None:
            self.id = id
        if last_rotate is not None:
            self.last_rotate = last_rotate
        if revoked is not None:
            self.revoked = revoked
        if ttl is not None:
            self.ttl = ttl

    @property
    def children(self):
        """Gets the children of this UIDTokenDetails.  # noqa: E501


        :return: The children of this UIDTokenDetails.  # noqa: E501
        :rtype: dict(str, UIDTokenDetails)
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this UIDTokenDetails.


        :param children: The children of this UIDTokenDetails.  # noqa: E501
        :type: dict(str, UIDTokenDetails)
        """

        self._children = children

    @property
    def comment(self):
        """Gets the comment of this UIDTokenDetails.  # noqa: E501


        :return: The comment of this UIDTokenDetails.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this UIDTokenDetails.


        :param comment: The comment of this UIDTokenDetails.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def deny_inheritance(self):
        """Gets the deny_inheritance of this UIDTokenDetails.  # noqa: E501


        :return: The deny_inheritance of this UIDTokenDetails.  # noqa: E501
        :rtype: bool
        """
        return self._deny_inheritance

    @deny_inheritance.setter
    def deny_inheritance(self, deny_inheritance):
        """Sets the deny_inheritance of this UIDTokenDetails.


        :param deny_inheritance: The deny_inheritance of this UIDTokenDetails.  # noqa: E501
        :type: bool
        """

        self._deny_inheritance = deny_inheritance

    @property
    def deny_rotate(self):
        """Gets the deny_rotate of this UIDTokenDetails.  # noqa: E501


        :return: The deny_rotate of this UIDTokenDetails.  # noqa: E501
        :rtype: bool
        """
        return self._deny_rotate

    @deny_rotate.setter
    def deny_rotate(self, deny_rotate):
        """Sets the deny_rotate of this UIDTokenDetails.


        :param deny_rotate: The deny_rotate of this UIDTokenDetails.  # noqa: E501
        :type: bool
        """

        self._deny_rotate = deny_rotate

    @property
    def depth(self):
        """Gets the depth of this UIDTokenDetails.  # noqa: E501


        :return: The depth of this UIDTokenDetails.  # noqa: E501
        :rtype: int
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """Sets the depth of this UIDTokenDetails.


        :param depth: The depth of this UIDTokenDetails.  # noqa: E501
        :type: int
        """

        self._depth = depth

    @property
    def expired_date(self):
        """Gets the expired_date of this UIDTokenDetails.  # noqa: E501


        :return: The expired_date of this UIDTokenDetails.  # noqa: E501
        :rtype: str
        """
        return self._expired_date

    @expired_date.setter
    def expired_date(self, expired_date):
        """Sets the expired_date of this UIDTokenDetails.


        :param expired_date: The expired_date of this UIDTokenDetails.  # noqa: E501
        :type: str
        """

        self._expired_date = expired_date

    @property
    def id(self):
        """Gets the id of this UIDTokenDetails.  # noqa: E501


        :return: The id of this UIDTokenDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UIDTokenDetails.


        :param id: The id of this UIDTokenDetails.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_rotate(self):
        """Gets the last_rotate of this UIDTokenDetails.  # noqa: E501


        :return: The last_rotate of this UIDTokenDetails.  # noqa: E501
        :rtype: str
        """
        return self._last_rotate

    @last_rotate.setter
    def last_rotate(self, last_rotate):
        """Sets the last_rotate of this UIDTokenDetails.


        :param last_rotate: The last_rotate of this UIDTokenDetails.  # noqa: E501
        :type: str
        """

        self._last_rotate = last_rotate

    @property
    def revoked(self):
        """Gets the revoked of this UIDTokenDetails.  # noqa: E501


        :return: The revoked of this UIDTokenDetails.  # noqa: E501
        :rtype: bool
        """
        return self._revoked

    @revoked.setter
    def revoked(self, revoked):
        """Sets the revoked of this UIDTokenDetails.


        :param revoked: The revoked of this UIDTokenDetails.  # noqa: E501
        :type: bool
        """

        self._revoked = revoked

    @property
    def ttl(self):
        """Gets the ttl of this UIDTokenDetails.  # noqa: E501


        :return: The ttl of this UIDTokenDetails.  # noqa: E501
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this UIDTokenDetails.


        :param ttl: The ttl of this UIDTokenDetails.  # noqa: E501
        :type: int
        """

        self._ttl = ttl

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UIDTokenDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UIDTokenDetails):
            return True

        return self.to_dict() != other.to_dict()
