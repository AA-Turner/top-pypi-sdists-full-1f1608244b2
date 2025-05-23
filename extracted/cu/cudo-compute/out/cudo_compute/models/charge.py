# coding: utf-8

"""
    Cudo Compute service

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cudo_compute.configuration import Configuration


class Charge(object):
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
        'amount': 'Decimal',
        'create_time': 'datetime',
        'paid': 'bool',
        'refunded': 'bool',
        'status': 'str',
        'failure_code': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'create_time': 'createTime',
        'paid': 'paid',
        'refunded': 'refunded',
        'status': 'status',
        'failure_code': 'failureCode'
    }

    def __init__(self, amount=None, create_time=None, paid=None, refunded=None, status=None, failure_code=None, _configuration=None):  # noqa: E501
        """Charge - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._amount = None
        self._create_time = None
        self._paid = None
        self._refunded = None
        self._status = None
        self._failure_code = None
        self.discriminator = None

        self.amount = amount
        self.create_time = create_time
        self.paid = paid
        self.refunded = refunded
        self.status = status
        if failure_code is not None:
            self.failure_code = failure_code

    @property
    def amount(self):
        """Gets the amount of this Charge.  # noqa: E501


        :return: The amount of this Charge.  # noqa: E501
        :rtype: Decimal
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Charge.


        :param amount: The amount of this Charge.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def create_time(self):
        """Gets the create_time of this Charge.  # noqa: E501


        :return: The create_time of this Charge.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Charge.


        :param create_time: The create_time of this Charge.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and create_time is None:
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def paid(self):
        """Gets the paid of this Charge.  # noqa: E501


        :return: The paid of this Charge.  # noqa: E501
        :rtype: bool
        """
        return self._paid

    @paid.setter
    def paid(self, paid):
        """Sets the paid of this Charge.


        :param paid: The paid of this Charge.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and paid is None:
            raise ValueError("Invalid value for `paid`, must not be `None`")  # noqa: E501

        self._paid = paid

    @property
    def refunded(self):
        """Gets the refunded of this Charge.  # noqa: E501


        :return: The refunded of this Charge.  # noqa: E501
        :rtype: bool
        """
        return self._refunded

    @refunded.setter
    def refunded(self, refunded):
        """Sets the refunded of this Charge.


        :param refunded: The refunded of this Charge.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and refunded is None:
            raise ValueError("Invalid value for `refunded`, must not be `None`")  # noqa: E501

        self._refunded = refunded

    @property
    def status(self):
        """Gets the status of this Charge.  # noqa: E501


        :return: The status of this Charge.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Charge.


        :param status: The status of this Charge.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def failure_code(self):
        """Gets the failure_code of this Charge.  # noqa: E501


        :return: The failure_code of this Charge.  # noqa: E501
        :rtype: str
        """
        return self._failure_code

    @failure_code.setter
    def failure_code(self, failure_code):
        """Sets the failure_code of this Charge.


        :param failure_code: The failure_code of this Charge.  # noqa: E501
        :type: str
        """

        self._failure_code = failure_code

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
        if issubclass(Charge, dict):
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
        if not isinstance(other, Charge):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Charge):
            return True

        return self.to_dict() != other.to_dict()
