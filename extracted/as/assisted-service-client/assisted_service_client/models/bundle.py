# coding: utf-8

"""
    AssistedInstall

    Assisted installation  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Bundle(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'id': 'str',
        'title': 'str',
        'description': 'str',
        'operators': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'description': 'description',
        'operators': 'operators'
    }

    def __init__(self, id=None, title=None, description=None, operators=None):  # noqa: E501
        """Bundle - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._title = None
        self._description = None
        self._operators = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if operators is not None:
            self.operators = operators

    @property
    def id(self):
        """Gets the id of this Bundle.  # noqa: E501

        Unique identifier of the bundle, for example `virtualization` or `openshift-ai-nvidia`.  # noqa: E501

        :return: The id of this Bundle.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Bundle.

        Unique identifier of the bundle, for example `virtualization` or `openshift-ai-nvidia`.  # noqa: E501

        :param id: The id of this Bundle.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this Bundle.  # noqa: E501

        Short human friendly description for the bundle, usually only a few words, for example `Virtualization` or `OpenShift AI (NVIDIA)`.   # noqa: E501

        :return: The title of this Bundle.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Bundle.

        Short human friendly description for the bundle, usually only a few words, for example `Virtualization` or `OpenShift AI (NVIDIA)`.   # noqa: E501

        :param title: The title of this Bundle.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this Bundle.  # noqa: E501

        Longer human friendly description for the bundle, usually one or more sentences.   # noqa: E501

        :return: The description of this Bundle.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Bundle.

        Longer human friendly description for the bundle, usually one or more sentences.   # noqa: E501

        :param description: The description of this Bundle.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def operators(self):
        """Gets the operators of this Bundle.  # noqa: E501

        List of operators associated with the bundle.  # noqa: E501

        :return: The operators of this Bundle.  # noqa: E501
        :rtype: list[str]
        """
        return self._operators

    @operators.setter
    def operators(self, operators):
        """Sets the operators of this Bundle.

        List of operators associated with the bundle.  # noqa: E501

        :param operators: The operators of this Bundle.  # noqa: E501
        :type: list[str]
        """

        self._operators = operators

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Bundle, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Bundle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
