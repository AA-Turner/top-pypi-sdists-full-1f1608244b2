# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails and SMS from dynamically allocated email addresses and phone numbers. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://docs.mailslurp.com/) - [Examples](https://github.com/mailslurp/examples) repository  # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Contact: contact@mailslurp.dev
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailslurp_client.configuration import Configuration


class ForwardEmailOptions(object):
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
        'to': 'list[str]',
        'subject': 'str',
        'cc': 'list[str]',
        'bcc': 'list[str]',
        '_from': 'str',
        'use_inbox_name': 'bool',
        'filter_bounced_recipients': 'bool'
    }

    attribute_map = {
        'to': 'to',
        'subject': 'subject',
        'cc': 'cc',
        'bcc': 'bcc',
        '_from': 'from',
        'use_inbox_name': 'useInboxName',
        'filter_bounced_recipients': 'filterBouncedRecipients'
    }

    def __init__(self, to=None, subject=None, cc=None, bcc=None, _from=None, use_inbox_name=None, filter_bounced_recipients=None, local_vars_configuration=None):  # noqa: E501
        """ForwardEmailOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._to = None
        self._subject = None
        self._cc = None
        self._bcc = None
        self.__from = None
        self._use_inbox_name = None
        self._filter_bounced_recipients = None
        self.discriminator = None

        self.to = to
        self.subject = subject
        self.cc = cc
        self.bcc = bcc
        self._from = _from
        self.use_inbox_name = use_inbox_name
        self.filter_bounced_recipients = filter_bounced_recipients

    @property
    def to(self):
        """Gets the to of this ForwardEmailOptions.  # noqa: E501

        To recipients for forwarded email  # noqa: E501

        :return: The to of this ForwardEmailOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this ForwardEmailOptions.

        To recipients for forwarded email  # noqa: E501

        :param to: The to of this ForwardEmailOptions.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and to is None:  # noqa: E501
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def subject(self):
        """Gets the subject of this ForwardEmailOptions.  # noqa: E501

        Subject for forwarded email  # noqa: E501

        :return: The subject of this ForwardEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this ForwardEmailOptions.

        Subject for forwarded email  # noqa: E501

        :param subject: The subject of this ForwardEmailOptions.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def cc(self):
        """Gets the cc of this ForwardEmailOptions.  # noqa: E501

        Optional cc recipients  # noqa: E501

        :return: The cc of this ForwardEmailOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        """Sets the cc of this ForwardEmailOptions.

        Optional cc recipients  # noqa: E501

        :param cc: The cc of this ForwardEmailOptions.  # noqa: E501
        :type: list[str]
        """

        self._cc = cc

    @property
    def bcc(self):
        """Gets the bcc of this ForwardEmailOptions.  # noqa: E501

        Optional bcc recipients  # noqa: E501

        :return: The bcc of this ForwardEmailOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._bcc

    @bcc.setter
    def bcc(self, bcc):
        """Sets the bcc of this ForwardEmailOptions.

        Optional bcc recipients  # noqa: E501

        :param bcc: The bcc of this ForwardEmailOptions.  # noqa: E501
        :type: list[str]
        """

        self._bcc = bcc

    @property
    def _from(self):
        """Gets the _from of this ForwardEmailOptions.  # noqa: E501

        Optional from override  # noqa: E501

        :return: The _from of this ForwardEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this ForwardEmailOptions.

        Optional from override  # noqa: E501

        :param _from: The _from of this ForwardEmailOptions.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def use_inbox_name(self):
        """Gets the use_inbox_name of this ForwardEmailOptions.  # noqa: E501

        Optionally use inbox name as display name for sender email address  # noqa: E501

        :return: The use_inbox_name of this ForwardEmailOptions.  # noqa: E501
        :rtype: bool
        """
        return self._use_inbox_name

    @use_inbox_name.setter
    def use_inbox_name(self, use_inbox_name):
        """Sets the use_inbox_name of this ForwardEmailOptions.

        Optionally use inbox name as display name for sender email address  # noqa: E501

        :param use_inbox_name: The use_inbox_name of this ForwardEmailOptions.  # noqa: E501
        :type: bool
        """

        self._use_inbox_name = use_inbox_name

    @property
    def filter_bounced_recipients(self):
        """Gets the filter_bounced_recipients of this ForwardEmailOptions.  # noqa: E501

        Filter recipients to remove any bounced recipients from to, bcc, and cc before sending  # noqa: E501

        :return: The filter_bounced_recipients of this ForwardEmailOptions.  # noqa: E501
        :rtype: bool
        """
        return self._filter_bounced_recipients

    @filter_bounced_recipients.setter
    def filter_bounced_recipients(self, filter_bounced_recipients):
        """Sets the filter_bounced_recipients of this ForwardEmailOptions.

        Filter recipients to remove any bounced recipients from to, bcc, and cc before sending  # noqa: E501

        :param filter_bounced_recipients: The filter_bounced_recipients of this ForwardEmailOptions.  # noqa: E501
        :type: bool
        """

        self._filter_bounced_recipients = filter_bounced_recipients

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
        if not isinstance(other, ForwardEmailOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ForwardEmailOptions):
            return True

        return self.to_dict() != other.to_dict()
