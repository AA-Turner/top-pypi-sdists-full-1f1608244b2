# coding: utf-8

"""
    Aron API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from openapi_client.configuration import Configuration


class LLMDocumentCreateAPIInput(object):
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
        'artifact_id': 'int',
        'download_url': 'str',
        'extension': 'str',
        'filename': 'str',
        'size': 'str'
    }

    attribute_map = {
        'artifact_id': 'artifact_id',
        'download_url': 'download_url',
        'extension': 'extension',
        'filename': 'filename',
        'size': 'size'
    }

    def __init__(self, artifact_id=None, download_url=None, extension=None, filename=None, size=None, local_vars_configuration=None):  # noqa: E501
        """LLMDocumentCreateAPIInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._artifact_id = None
        self._download_url = None
        self._extension = None
        self._filename = None
        self._size = None
        self.discriminator = None

        if artifact_id is not None:
            self.artifact_id = artifact_id
        if download_url is not None:
            self.download_url = download_url
        if extension is not None:
            self.extension = extension
        if filename is not None:
            self.filename = filename
        if size is not None:
            self.size = size

    @property
    def artifact_id(self):
        """Gets the artifact_id of this LLMDocumentCreateAPIInput.  # noqa: E501


        :return: The artifact_id of this LLMDocumentCreateAPIInput.  # noqa: E501
        :rtype: int
        """
        return self._artifact_id

    @artifact_id.setter
    def artifact_id(self, artifact_id):
        """Sets the artifact_id of this LLMDocumentCreateAPIInput.


        :param artifact_id: The artifact_id of this LLMDocumentCreateAPIInput.  # noqa: E501
        :type artifact_id: int
        """

        self._artifact_id = artifact_id

    @property
    def download_url(self):
        """Gets the download_url of this LLMDocumentCreateAPIInput.  # noqa: E501


        :return: The download_url of this LLMDocumentCreateAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """Sets the download_url of this LLMDocumentCreateAPIInput.


        :param download_url: The download_url of this LLMDocumentCreateAPIInput.  # noqa: E501
        :type download_url: str
        """

        self._download_url = download_url

    @property
    def extension(self):
        """Gets the extension of this LLMDocumentCreateAPIInput.  # noqa: E501


        :return: The extension of this LLMDocumentCreateAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this LLMDocumentCreateAPIInput.


        :param extension: The extension of this LLMDocumentCreateAPIInput.  # noqa: E501
        :type extension: str
        """

        self._extension = extension

    @property
    def filename(self):
        """Gets the filename of this LLMDocumentCreateAPIInput.  # noqa: E501


        :return: The filename of this LLMDocumentCreateAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this LLMDocumentCreateAPIInput.


        :param filename: The filename of this LLMDocumentCreateAPIInput.  # noqa: E501
        :type filename: str
        """

        self._filename = filename

    @property
    def size(self):
        """Gets the size of this LLMDocumentCreateAPIInput.  # noqa: E501


        :return: The size of this LLMDocumentCreateAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this LLMDocumentCreateAPIInput.


        :param size: The size of this LLMDocumentCreateAPIInput.  # noqa: E501
        :type size: str
        """

        self._size = size

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LLMDocumentCreateAPIInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LLMDocumentCreateAPIInput):
            return True

        return self.to_dict() != other.to_dict()
