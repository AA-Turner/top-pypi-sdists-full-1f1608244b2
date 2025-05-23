# coding: utf-8

"""
    Managed Ray API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class SessionCommand(object):
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
        'id': 'str',
        'type': 'SessionCommandTypes',
        'created_at': 'datetime',
        'name': 'str',
        'params': 'object',
        'shell': 'bool',
        'shell_command': 'str',
        'message': 'str',
        'killed_at': 'datetime',
        'finished_at': 'datetime',
        'status_code': 'int',
        'web_terminal_tab_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'created_at': 'created_at',
        'name': 'name',
        'params': 'params',
        'shell': 'shell',
        'shell_command': 'shell_command',
        'message': 'message',
        'killed_at': 'killed_at',
        'finished_at': 'finished_at',
        'status_code': 'status_code',
        'web_terminal_tab_id': 'web_terminal_tab_id'
    }

    def __init__(self, id=None, type=None, created_at=None, name=None, params=None, shell=None, shell_command=None, message=None, killed_at=None, finished_at=None, status_code=None, web_terminal_tab_id=None, local_vars_configuration=None):  # noqa: E501
        """SessionCommand - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._created_at = None
        self._name = None
        self._params = None
        self._shell = None
        self._shell_command = None
        self._message = None
        self._killed_at = None
        self._finished_at = None
        self._status_code = None
        self._web_terminal_tab_id = None
        self.discriminator = None

        self.id = id
        self.type = type
        self.created_at = created_at
        self.name = name
        self.params = params
        self.shell = shell
        self.shell_command = shell_command
        if message is not None:
            self.message = message
        if killed_at is not None:
            self.killed_at = killed_at
        if finished_at is not None:
            self.finished_at = finished_at
        if status_code is not None:
            self.status_code = status_code
        if web_terminal_tab_id is not None:
            self.web_terminal_tab_id = web_terminal_tab_id

    @property
    def id(self):
        """Gets the id of this SessionCommand.  # noqa: E501


        :return: The id of this SessionCommand.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SessionCommand.


        :param id: The id of this SessionCommand.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this SessionCommand.  # noqa: E501


        :return: The type of this SessionCommand.  # noqa: E501
        :rtype: SessionCommandTypes
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SessionCommand.


        :param type: The type of this SessionCommand.  # noqa: E501
        :type: SessionCommandTypes
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def created_at(self):
        """Gets the created_at of this SessionCommand.  # noqa: E501


        :return: The created_at of this SessionCommand.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SessionCommand.


        :param created_at: The created_at of this SessionCommand.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def name(self):
        """Gets the name of this SessionCommand.  # noqa: E501


        :return: The name of this SessionCommand.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SessionCommand.


        :param name: The name of this SessionCommand.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def params(self):
        """Gets the params of this SessionCommand.  # noqa: E501


        :return: The params of this SessionCommand.  # noqa: E501
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this SessionCommand.


        :param params: The params of this SessionCommand.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and params is None:  # noqa: E501
            raise ValueError("Invalid value for `params`, must not be `None`")  # noqa: E501

        self._params = params

    @property
    def shell(self):
        """Gets the shell of this SessionCommand.  # noqa: E501


        :return: The shell of this SessionCommand.  # noqa: E501
        :rtype: bool
        """
        return self._shell

    @shell.setter
    def shell(self, shell):
        """Sets the shell of this SessionCommand.


        :param shell: The shell of this SessionCommand.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and shell is None:  # noqa: E501
            raise ValueError("Invalid value for `shell`, must not be `None`")  # noqa: E501

        self._shell = shell

    @property
    def shell_command(self):
        """Gets the shell_command of this SessionCommand.  # noqa: E501


        :return: The shell_command of this SessionCommand.  # noqa: E501
        :rtype: str
        """
        return self._shell_command

    @shell_command.setter
    def shell_command(self, shell_command):
        """Sets the shell_command of this SessionCommand.


        :param shell_command: The shell_command of this SessionCommand.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and shell_command is None:  # noqa: E501
            raise ValueError("Invalid value for `shell_command`, must not be `None`")  # noqa: E501

        self._shell_command = shell_command

    @property
    def message(self):
        """Gets the message of this SessionCommand.  # noqa: E501


        :return: The message of this SessionCommand.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this SessionCommand.


        :param message: The message of this SessionCommand.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def killed_at(self):
        """Gets the killed_at of this SessionCommand.  # noqa: E501


        :return: The killed_at of this SessionCommand.  # noqa: E501
        :rtype: datetime
        """
        return self._killed_at

    @killed_at.setter
    def killed_at(self, killed_at):
        """Sets the killed_at of this SessionCommand.


        :param killed_at: The killed_at of this SessionCommand.  # noqa: E501
        :type: datetime
        """

        self._killed_at = killed_at

    @property
    def finished_at(self):
        """Gets the finished_at of this SessionCommand.  # noqa: E501


        :return: The finished_at of this SessionCommand.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this SessionCommand.


        :param finished_at: The finished_at of this SessionCommand.  # noqa: E501
        :type: datetime
        """

        self._finished_at = finished_at

    @property
    def status_code(self):
        """Gets the status_code of this SessionCommand.  # noqa: E501


        :return: The status_code of this SessionCommand.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this SessionCommand.


        :param status_code: The status_code of this SessionCommand.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def web_terminal_tab_id(self):
        """Gets the web_terminal_tab_id of this SessionCommand.  # noqa: E501


        :return: The web_terminal_tab_id of this SessionCommand.  # noqa: E501
        :rtype: str
        """
        return self._web_terminal_tab_id

    @web_terminal_tab_id.setter
    def web_terminal_tab_id(self, web_terminal_tab_id):
        """Sets the web_terminal_tab_id of this SessionCommand.


        :param web_terminal_tab_id: The web_terminal_tab_id of this SessionCommand.  # noqa: E501
        :type: str
        """

        self._web_terminal_tab_id = web_terminal_tab_id

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
        if not isinstance(other, SessionCommand):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SessionCommand):
            return True

        return self.to_dict() != other.to_dict()
