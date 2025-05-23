# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 66.22.1-v202505231115-CD
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class FormulaPackageOutputV1(object):
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
        'created_at': 'str',
        'creator_contact_info': 'str',
        'creator_name': 'str',
        'datasource': 'DatasourcePreviewV1',
        'description': 'str',
        'docs': 'list[ItemPreviewV1]',
        'effective_permissions': 'PermissionsV1',
        'functions': 'list[ItemPreviewV1]',
        'id': 'str',
        'installer': 'IdentityPreviewV1',
        'is_archived': 'bool',
        'is_redacted': 'bool',
        'name': 'str',
        'status_message': 'str',
        'translation_key': 'str',
        'type': 'str',
        'updated_at': 'str',
        'version_string': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'creator_contact_info': 'creatorContactInfo',
        'creator_name': 'creatorName',
        'datasource': 'datasource',
        'description': 'description',
        'docs': 'docs',
        'effective_permissions': 'effectivePermissions',
        'functions': 'functions',
        'id': 'id',
        'installer': 'installer',
        'is_archived': 'isArchived',
        'is_redacted': 'isRedacted',
        'name': 'name',
        'status_message': 'statusMessage',
        'translation_key': 'translationKey',
        'type': 'type',
        'updated_at': 'updatedAt',
        'version_string': 'versionString'
    }

    def __init__(self, created_at=None, creator_contact_info=None, creator_name=None, datasource=None, description=None, docs=None, effective_permissions=None, functions=None, id=None, installer=None, is_archived=False, is_redacted=False, name=None, status_message=None, translation_key=None, type=None, updated_at=None, version_string=None):
        """
        FormulaPackageOutputV1 - a model defined in Swagger
        """

        self._created_at = None
        self._creator_contact_info = None
        self._creator_name = None
        self._datasource = None
        self._description = None
        self._docs = None
        self._effective_permissions = None
        self._functions = None
        self._id = None
        self._installer = None
        self._is_archived = None
        self._is_redacted = None
        self._name = None
        self._status_message = None
        self._translation_key = None
        self._type = None
        self._updated_at = None
        self._version_string = None

        if created_at is not None:
          self.created_at = created_at
        if creator_contact_info is not None:
          self.creator_contact_info = creator_contact_info
        if creator_name is not None:
          self.creator_name = creator_name
        if datasource is not None:
          self.datasource = datasource
        if description is not None:
          self.description = description
        if docs is not None:
          self.docs = docs
        if effective_permissions is not None:
          self.effective_permissions = effective_permissions
        if functions is not None:
          self.functions = functions
        if id is not None:
          self.id = id
        if installer is not None:
          self.installer = installer
        if is_archived is not None:
          self.is_archived = is_archived
        if is_redacted is not None:
          self.is_redacted = is_redacted
        if name is not None:
          self.name = name
        if status_message is not None:
          self.status_message = status_message
        if translation_key is not None:
          self.translation_key = translation_key
        if type is not None:
          self.type = type
        if updated_at is not None:
          self.updated_at = updated_at
        if version_string is not None:
          self.version_string = version_string

    @property
    def created_at(self):
        """
        Gets the created_at of this FormulaPackageOutputV1.
        The ISO 8601 date of when the FormulaPackage was created (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm).

        :return: The created_at of this FormulaPackageOutputV1.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this FormulaPackageOutputV1.
        The ISO 8601 date of when the FormulaPackage was created (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm).

        :param created_at: The created_at of this FormulaPackageOutputV1.
        :type: str
        """

        self._created_at = created_at

    @property
    def creator_contact_info(self):
        """
        Gets the creator_contact_info of this FormulaPackageOutputV1.
        The contact information of the entity that created this FormulaPackage.

        :return: The creator_contact_info of this FormulaPackageOutputV1.
        :rtype: str
        """
        return self._creator_contact_info

    @creator_contact_info.setter
    def creator_contact_info(self, creator_contact_info):
        """
        Sets the creator_contact_info of this FormulaPackageOutputV1.
        The contact information of the entity that created this FormulaPackage.

        :param creator_contact_info: The creator_contact_info of this FormulaPackageOutputV1.
        :type: str
        """

        self._creator_contact_info = creator_contact_info

    @property
    def creator_name(self):
        """
        Gets the creator_name of this FormulaPackageOutputV1.
        The name of the entity that created this FormulaPackage.

        :return: The creator_name of this FormulaPackageOutputV1.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """
        Sets the creator_name of this FormulaPackageOutputV1.
        The name of the entity that created this FormulaPackage.

        :param creator_name: The creator_name of this FormulaPackageOutputV1.
        :type: str
        """

        self._creator_name = creator_name

    @property
    def datasource(self):
        """
        Gets the datasource of this FormulaPackageOutputV1.

        :return: The datasource of this FormulaPackageOutputV1.
        :rtype: DatasourcePreviewV1
        """
        return self._datasource

    @datasource.setter
    def datasource(self, datasource):
        """
        Sets the datasource of this FormulaPackageOutputV1.

        :param datasource: The datasource of this FormulaPackageOutputV1.
        :type: DatasourcePreviewV1
        """

        self._datasource = datasource

    @property
    def description(self):
        """
        Gets the description of this FormulaPackageOutputV1.
        Clarifying information or other plain language description of this item

        :return: The description of this FormulaPackageOutputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FormulaPackageOutputV1.
        Clarifying information or other plain language description of this item

        :param description: The description of this FormulaPackageOutputV1.
        :type: str
        """

        self._description = description

    @property
    def docs(self):
        """
        Gets the docs of this FormulaPackageOutputV1.
        The list of formula docs contained in this FormulaPackage.

        :return: The docs of this FormulaPackageOutputV1.
        :rtype: list[ItemPreviewV1]
        """
        return self._docs

    @docs.setter
    def docs(self, docs):
        """
        Sets the docs of this FormulaPackageOutputV1.
        The list of formula docs contained in this FormulaPackage.

        :param docs: The docs of this FormulaPackageOutputV1.
        :type: list[ItemPreviewV1]
        """

        self._docs = docs

    @property
    def effective_permissions(self):
        """
        Gets the effective_permissions of this FormulaPackageOutputV1.

        :return: The effective_permissions of this FormulaPackageOutputV1.
        :rtype: PermissionsV1
        """
        return self._effective_permissions

    @effective_permissions.setter
    def effective_permissions(self, effective_permissions):
        """
        Sets the effective_permissions of this FormulaPackageOutputV1.

        :param effective_permissions: The effective_permissions of this FormulaPackageOutputV1.
        :type: PermissionsV1
        """

        self._effective_permissions = effective_permissions

    @property
    def functions(self):
        """
        Gets the functions of this FormulaPackageOutputV1.
        The list of user defined functions contained in this FormulaPackage

        :return: The functions of this FormulaPackageOutputV1.
        :rtype: list[ItemPreviewV1]
        """
        return self._functions

    @functions.setter
    def functions(self, functions):
        """
        Sets the functions of this FormulaPackageOutputV1.
        The list of user defined functions contained in this FormulaPackage

        :param functions: The functions of this FormulaPackageOutputV1.
        :type: list[ItemPreviewV1]
        """

        self._functions = functions

    @property
    def id(self):
        """
        Gets the id of this FormulaPackageOutputV1.
        The ID that can be used to interact with the item

        :return: The id of this FormulaPackageOutputV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FormulaPackageOutputV1.
        The ID that can be used to interact with the item

        :param id: The id of this FormulaPackageOutputV1.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def installer(self):
        """
        Gets the installer of this FormulaPackageOutputV1.

        :return: The installer of this FormulaPackageOutputV1.
        :rtype: IdentityPreviewV1
        """
        return self._installer

    @installer.setter
    def installer(self, installer):
        """
        Sets the installer of this FormulaPackageOutputV1.

        :param installer: The installer of this FormulaPackageOutputV1.
        :type: IdentityPreviewV1
        """

        self._installer = installer

    @property
    def is_archived(self):
        """
        Gets the is_archived of this FormulaPackageOutputV1.
        Whether item is archived

        :return: The is_archived of this FormulaPackageOutputV1.
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """
        Sets the is_archived of this FormulaPackageOutputV1.
        Whether item is archived

        :param is_archived: The is_archived of this FormulaPackageOutputV1.
        :type: bool
        """

        self._is_archived = is_archived

    @property
    def is_redacted(self):
        """
        Gets the is_redacted of this FormulaPackageOutputV1.
        Whether item is redacted

        :return: The is_redacted of this FormulaPackageOutputV1.
        :rtype: bool
        """
        return self._is_redacted

    @is_redacted.setter
    def is_redacted(self, is_redacted):
        """
        Sets the is_redacted of this FormulaPackageOutputV1.
        Whether item is redacted

        :param is_redacted: The is_redacted of this FormulaPackageOutputV1.
        :type: bool
        """

        self._is_redacted = is_redacted

    @property
    def name(self):
        """
        Gets the name of this FormulaPackageOutputV1.
        The human readable name

        :return: The name of this FormulaPackageOutputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FormulaPackageOutputV1.
        The human readable name

        :param name: The name of this FormulaPackageOutputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def status_message(self):
        """
        Gets the status_message of this FormulaPackageOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :return: The status_message of this FormulaPackageOutputV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this FormulaPackageOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :param status_message: The status_message of this FormulaPackageOutputV1.
        :type: str
        """

        self._status_message = status_message

    @property
    def translation_key(self):
        """
        Gets the translation_key of this FormulaPackageOutputV1.
        The item's translation key, if any

        :return: The translation_key of this FormulaPackageOutputV1.
        :rtype: str
        """
        return self._translation_key

    @translation_key.setter
    def translation_key(self, translation_key):
        """
        Sets the translation_key of this FormulaPackageOutputV1.
        The item's translation key, if any

        :param translation_key: The translation_key of this FormulaPackageOutputV1.
        :type: str
        """

        self._translation_key = translation_key

    @property
    def type(self):
        """
        Gets the type of this FormulaPackageOutputV1.
        The type of the item

        :return: The type of this FormulaPackageOutputV1.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this FormulaPackageOutputV1.
        The type of the item

        :param type: The type of this FormulaPackageOutputV1.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def updated_at(self):
        """
        Gets the updated_at of this FormulaPackageOutputV1.
        The ISO 8601 date of when the FormulaPackage was updated (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm).

        :return: The updated_at of this FormulaPackageOutputV1.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this FormulaPackageOutputV1.
        The ISO 8601 date of when the FormulaPackage was updated (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm).

        :param updated_at: The updated_at of this FormulaPackageOutputV1.
        :type: str
        """

        self._updated_at = updated_at

    @property
    def version_string(self):
        """
        Gets the version_string of this FormulaPackageOutputV1.
        The version of this FormulaPackage.

        :return: The version_string of this FormulaPackageOutputV1.
        :rtype: str
        """
        return self._version_string

    @version_string.setter
    def version_string(self, version_string):
        """
        Sets the version_string of this FormulaPackageOutputV1.
        The version of this FormulaPackage.

        :param version_string: The version_string of this FormulaPackageOutputV1.
        :type: str
        """

        self._version_string = version_string

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
        if not isinstance(other, FormulaPackageOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
