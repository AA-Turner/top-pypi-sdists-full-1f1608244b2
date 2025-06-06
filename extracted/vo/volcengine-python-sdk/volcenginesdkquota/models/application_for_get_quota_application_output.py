# coding: utf-8

"""
    quota

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ApplicationForGetQuotaApplicationOutput(object):
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
        'application_id': 'str',
        'apply_time': 'str',
        'approve_value': 'float',
        'audit_reason': 'str',
        'desire_value': 'float',
        'dimensions': 'list[DimensionForGetQuotaApplicationOutput]',
        'effective_time': 'str',
        'id': 'int',
        'provider_code': 'str',
        'provider_name': 'str',
        'quota_code': 'str',
        'quota_type': 'str',
        'quota_unit': 'str',
        'reason': 'str',
        'status': 'str'
    }

    attribute_map = {
        'application_id': 'ApplicationId',
        'apply_time': 'ApplyTime',
        'approve_value': 'ApproveValue',
        'audit_reason': 'AuditReason',
        'desire_value': 'DesireValue',
        'dimensions': 'Dimensions',
        'effective_time': 'EffectiveTime',
        'id': 'ID',
        'provider_code': 'ProviderCode',
        'provider_name': 'ProviderName',
        'quota_code': 'QuotaCode',
        'quota_type': 'QuotaType',
        'quota_unit': 'QuotaUnit',
        'reason': 'Reason',
        'status': 'Status'
    }

    def __init__(self, application_id=None, apply_time=None, approve_value=None, audit_reason=None, desire_value=None, dimensions=None, effective_time=None, id=None, provider_code=None, provider_name=None, quota_code=None, quota_type=None, quota_unit=None, reason=None, status=None, _configuration=None):  # noqa: E501
        """ApplicationForGetQuotaApplicationOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._application_id = None
        self._apply_time = None
        self._approve_value = None
        self._audit_reason = None
        self._desire_value = None
        self._dimensions = None
        self._effective_time = None
        self._id = None
        self._provider_code = None
        self._provider_name = None
        self._quota_code = None
        self._quota_type = None
        self._quota_unit = None
        self._reason = None
        self._status = None
        self.discriminator = None

        if application_id is not None:
            self.application_id = application_id
        if apply_time is not None:
            self.apply_time = apply_time
        if approve_value is not None:
            self.approve_value = approve_value
        if audit_reason is not None:
            self.audit_reason = audit_reason
        if desire_value is not None:
            self.desire_value = desire_value
        if dimensions is not None:
            self.dimensions = dimensions
        if effective_time is not None:
            self.effective_time = effective_time
        if id is not None:
            self.id = id
        if provider_code is not None:
            self.provider_code = provider_code
        if provider_name is not None:
            self.provider_name = provider_name
        if quota_code is not None:
            self.quota_code = quota_code
        if quota_type is not None:
            self.quota_type = quota_type
        if quota_unit is not None:
            self.quota_unit = quota_unit
        if reason is not None:
            self.reason = reason
        if status is not None:
            self.status = status

    @property
    def application_id(self):
        """Gets the application_id of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501


        :return: The application_id of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ApplicationForGetQuotaApplicationOutput.


        :param application_id: The application_id of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def apply_time(self):
        """Gets the apply_time of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501


        :return: The apply_time of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :rtype: str
        """
        return self._apply_time

    @apply_time.setter
    def apply_time(self, apply_time):
        """Sets the apply_time of this ApplicationForGetQuotaApplicationOutput.


        :param apply_time: The apply_time of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :type: str
        """

        self._apply_time = apply_time

    @property
    def approve_value(self):
        """Gets the approve_value of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501


        :return: The approve_value of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :rtype: float
        """
        return self._approve_value

    @approve_value.setter
    def approve_value(self, approve_value):
        """Sets the approve_value of this ApplicationForGetQuotaApplicationOutput.


        :param approve_value: The approve_value of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :type: float
        """

        self._approve_value = approve_value

    @property
    def audit_reason(self):
        """Gets the audit_reason of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501


        :return: The audit_reason of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :rtype: str
        """
        return self._audit_reason

    @audit_reason.setter
    def audit_reason(self, audit_reason):
        """Sets the audit_reason of this ApplicationForGetQuotaApplicationOutput.


        :param audit_reason: The audit_reason of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :type: str
        """

        self._audit_reason = audit_reason

    @property
    def desire_value(self):
        """Gets the desire_value of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501


        :return: The desire_value of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :rtype: float
        """
        return self._desire_value

    @desire_value.setter
    def desire_value(self, desire_value):
        """Sets the desire_value of this ApplicationForGetQuotaApplicationOutput.


        :param desire_value: The desire_value of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :type: float
        """

        self._desire_value = desire_value

    @property
    def dimensions(self):
        """Gets the dimensions of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501


        :return: The dimensions of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :rtype: list[DimensionForGetQuotaApplicationOutput]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this ApplicationForGetQuotaApplicationOutput.


        :param dimensions: The dimensions of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :type: list[DimensionForGetQuotaApplicationOutput]
        """

        self._dimensions = dimensions

    @property
    def effective_time(self):
        """Gets the effective_time of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501


        :return: The effective_time of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :rtype: str
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        """Sets the effective_time of this ApplicationForGetQuotaApplicationOutput.


        :param effective_time: The effective_time of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :type: str
        """

        self._effective_time = effective_time

    @property
    def id(self):
        """Gets the id of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501


        :return: The id of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApplicationForGetQuotaApplicationOutput.


        :param id: The id of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def provider_code(self):
        """Gets the provider_code of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501


        :return: The provider_code of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :rtype: str
        """
        return self._provider_code

    @provider_code.setter
    def provider_code(self, provider_code):
        """Sets the provider_code of this ApplicationForGetQuotaApplicationOutput.


        :param provider_code: The provider_code of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :type: str
        """

        self._provider_code = provider_code

    @property
    def provider_name(self):
        """Gets the provider_name of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501


        :return: The provider_name of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this ApplicationForGetQuotaApplicationOutput.


        :param provider_name: The provider_name of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :type: str
        """

        self._provider_name = provider_name

    @property
    def quota_code(self):
        """Gets the quota_code of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501


        :return: The quota_code of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :rtype: str
        """
        return self._quota_code

    @quota_code.setter
    def quota_code(self, quota_code):
        """Sets the quota_code of this ApplicationForGetQuotaApplicationOutput.


        :param quota_code: The quota_code of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :type: str
        """

        self._quota_code = quota_code

    @property
    def quota_type(self):
        """Gets the quota_type of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501


        :return: The quota_type of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :rtype: str
        """
        return self._quota_type

    @quota_type.setter
    def quota_type(self, quota_type):
        """Sets the quota_type of this ApplicationForGetQuotaApplicationOutput.


        :param quota_type: The quota_type of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :type: str
        """

        self._quota_type = quota_type

    @property
    def quota_unit(self):
        """Gets the quota_unit of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501


        :return: The quota_unit of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :rtype: str
        """
        return self._quota_unit

    @quota_unit.setter
    def quota_unit(self, quota_unit):
        """Sets the quota_unit of this ApplicationForGetQuotaApplicationOutput.


        :param quota_unit: The quota_unit of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :type: str
        """

        self._quota_unit = quota_unit

    @property
    def reason(self):
        """Gets the reason of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501


        :return: The reason of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ApplicationForGetQuotaApplicationOutput.


        :param reason: The reason of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def status(self):
        """Gets the status of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501


        :return: The status of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ApplicationForGetQuotaApplicationOutput.


        :param status: The status of this ApplicationForGetQuotaApplicationOutput.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(ApplicationForGetQuotaApplicationOutput, dict):
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
        if not isinstance(other, ApplicationForGetQuotaApplicationOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplicationForGetQuotaApplicationOutput):
            return True

        return self.to_dict() != other.to_dict()
