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


class LlmLLMKnowledgeListResponse(object):
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
        'knowledge_list': 'list[ProtoLLMKnowledgeAndDocuments]',
        'page_info_with_count': 'RepositoryutilPageInfoWithCount'
    }

    attribute_map = {
        'knowledge_list': 'knowledge_list',
        'page_info_with_count': 'page_info_with_count'
    }

    def __init__(self, knowledge_list=None, page_info_with_count=None, local_vars_configuration=None):  # noqa: E501
        """LlmLLMKnowledgeListResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._knowledge_list = None
        self._page_info_with_count = None
        self.discriminator = None

        if knowledge_list is not None:
            self.knowledge_list = knowledge_list
        if page_info_with_count is not None:
            self.page_info_with_count = page_info_with_count

    @property
    def knowledge_list(self):
        """Gets the knowledge_list of this LlmLLMKnowledgeListResponse.  # noqa: E501


        :return: The knowledge_list of this LlmLLMKnowledgeListResponse.  # noqa: E501
        :rtype: list[ProtoLLMKnowledgeAndDocuments]
        """
        return self._knowledge_list

    @knowledge_list.setter
    def knowledge_list(self, knowledge_list):
        """Sets the knowledge_list of this LlmLLMKnowledgeListResponse.


        :param knowledge_list: The knowledge_list of this LlmLLMKnowledgeListResponse.  # noqa: E501
        :type knowledge_list: list[ProtoLLMKnowledgeAndDocuments]
        """

        self._knowledge_list = knowledge_list

    @property
    def page_info_with_count(self):
        """Gets the page_info_with_count of this LlmLLMKnowledgeListResponse.  # noqa: E501


        :return: The page_info_with_count of this LlmLLMKnowledgeListResponse.  # noqa: E501
        :rtype: RepositoryutilPageInfoWithCount
        """
        return self._page_info_with_count

    @page_info_with_count.setter
    def page_info_with_count(self, page_info_with_count):
        """Sets the page_info_with_count of this LlmLLMKnowledgeListResponse.


        :param page_info_with_count: The page_info_with_count of this LlmLLMKnowledgeListResponse.  # noqa: E501
        :type page_info_with_count: RepositoryutilPageInfoWithCount
        """

        self._page_info_with_count = page_info_with_count

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
        if not isinstance(other, LlmLLMKnowledgeListResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LlmLLMKnowledgeListResponse):
            return True

        return self.to_dict() != other.to_dict()
