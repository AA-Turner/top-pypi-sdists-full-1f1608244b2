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


class OrmLLMModelConnectionEdges(object):
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
        'created_by': 'OrmUser',
        'llm_knowledge': 'list[OrmLLMKnowledge]',
        'llm_model_parameter_definitions': 'list[OrmLLMModelParameterDefinition]',
        'llm_model_parameter_presets': 'list[OrmLLMModelParameterPreset]',
        'organization': 'OrmOrganization',
        'secret': 'OrmOrganizationCredentials'
    }

    attribute_map = {
        'created_by': 'created_by',
        'llm_knowledge': 'llm_knowledge',
        'llm_model_parameter_definitions': 'llm_model_parameter_definitions',
        'llm_model_parameter_presets': 'llm_model_parameter_presets',
        'organization': 'organization',
        'secret': 'secret'
    }

    def __init__(self, created_by=None, llm_knowledge=None, llm_model_parameter_definitions=None, llm_model_parameter_presets=None, organization=None, secret=None, local_vars_configuration=None):  # noqa: E501
        """OrmLLMModelConnectionEdges - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_by = None
        self._llm_knowledge = None
        self._llm_model_parameter_definitions = None
        self._llm_model_parameter_presets = None
        self._organization = None
        self._secret = None
        self.discriminator = None

        if created_by is not None:
            self.created_by = created_by
        if llm_knowledge is not None:
            self.llm_knowledge = llm_knowledge
        if llm_model_parameter_definitions is not None:
            self.llm_model_parameter_definitions = llm_model_parameter_definitions
        if llm_model_parameter_presets is not None:
            self.llm_model_parameter_presets = llm_model_parameter_presets
        if organization is not None:
            self.organization = organization
        if secret is not None:
            self.secret = secret

    @property
    def created_by(self):
        """Gets the created_by of this OrmLLMModelConnectionEdges.  # noqa: E501


        :return: The created_by of this OrmLLMModelConnectionEdges.  # noqa: E501
        :rtype: OrmUser
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this OrmLLMModelConnectionEdges.


        :param created_by: The created_by of this OrmLLMModelConnectionEdges.  # noqa: E501
        :type created_by: OrmUser
        """

        self._created_by = created_by

    @property
    def llm_knowledge(self):
        """Gets the llm_knowledge of this OrmLLMModelConnectionEdges.  # noqa: E501


        :return: The llm_knowledge of this OrmLLMModelConnectionEdges.  # noqa: E501
        :rtype: list[OrmLLMKnowledge]
        """
        return self._llm_knowledge

    @llm_knowledge.setter
    def llm_knowledge(self, llm_knowledge):
        """Sets the llm_knowledge of this OrmLLMModelConnectionEdges.


        :param llm_knowledge: The llm_knowledge of this OrmLLMModelConnectionEdges.  # noqa: E501
        :type llm_knowledge: list[OrmLLMKnowledge]
        """

        self._llm_knowledge = llm_knowledge

    @property
    def llm_model_parameter_definitions(self):
        """Gets the llm_model_parameter_definitions of this OrmLLMModelConnectionEdges.  # noqa: E501


        :return: The llm_model_parameter_definitions of this OrmLLMModelConnectionEdges.  # noqa: E501
        :rtype: list[OrmLLMModelParameterDefinition]
        """
        return self._llm_model_parameter_definitions

    @llm_model_parameter_definitions.setter
    def llm_model_parameter_definitions(self, llm_model_parameter_definitions):
        """Sets the llm_model_parameter_definitions of this OrmLLMModelConnectionEdges.


        :param llm_model_parameter_definitions: The llm_model_parameter_definitions of this OrmLLMModelConnectionEdges.  # noqa: E501
        :type llm_model_parameter_definitions: list[OrmLLMModelParameterDefinition]
        """

        self._llm_model_parameter_definitions = llm_model_parameter_definitions

    @property
    def llm_model_parameter_presets(self):
        """Gets the llm_model_parameter_presets of this OrmLLMModelConnectionEdges.  # noqa: E501


        :return: The llm_model_parameter_presets of this OrmLLMModelConnectionEdges.  # noqa: E501
        :rtype: list[OrmLLMModelParameterPreset]
        """
        return self._llm_model_parameter_presets

    @llm_model_parameter_presets.setter
    def llm_model_parameter_presets(self, llm_model_parameter_presets):
        """Sets the llm_model_parameter_presets of this OrmLLMModelConnectionEdges.


        :param llm_model_parameter_presets: The llm_model_parameter_presets of this OrmLLMModelConnectionEdges.  # noqa: E501
        :type llm_model_parameter_presets: list[OrmLLMModelParameterPreset]
        """

        self._llm_model_parameter_presets = llm_model_parameter_presets

    @property
    def organization(self):
        """Gets the organization of this OrmLLMModelConnectionEdges.  # noqa: E501


        :return: The organization of this OrmLLMModelConnectionEdges.  # noqa: E501
        :rtype: OrmOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this OrmLLMModelConnectionEdges.


        :param organization: The organization of this OrmLLMModelConnectionEdges.  # noqa: E501
        :type organization: OrmOrganization
        """

        self._organization = organization

    @property
    def secret(self):
        """Gets the secret of this OrmLLMModelConnectionEdges.  # noqa: E501


        :return: The secret of this OrmLLMModelConnectionEdges.  # noqa: E501
        :rtype: OrmOrganizationCredentials
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this OrmLLMModelConnectionEdges.


        :param secret: The secret of this OrmLLMModelConnectionEdges.  # noqa: E501
        :type secret: OrmOrganizationCredentials
        """

        self._secret = secret

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
        if not isinstance(other, OrmLLMModelConnectionEdges):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmLLMModelConnectionEdges):
            return True

        return self.to_dict() != other.to_dict()
