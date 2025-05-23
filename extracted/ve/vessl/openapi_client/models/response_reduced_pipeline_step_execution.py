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


class ResponseReducedPipelineStepExecution(object):
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
        'created_dt': 'datetime',
        'end_dt': 'datetime',
        'id': 'int',
        'judgment_result': 'str',
        'status': 'str',
        'step_key': 'str',
        'step_spec_id': 'int',
        'step_type': 'str',
        'sub_pipeline_execution': 'ResponsePipelineExecution',
        'title': 'str'
    }

    attribute_map = {
        'created_dt': 'created_dt',
        'end_dt': 'end_dt',
        'id': 'id',
        'judgment_result': 'judgment_result',
        'status': 'status',
        'step_key': 'step_key',
        'step_spec_id': 'step_spec_id',
        'step_type': 'step_type',
        'sub_pipeline_execution': 'sub_pipeline_execution',
        'title': 'title'
    }

    def __init__(self, created_dt=None, end_dt=None, id=None, judgment_result=None, status=None, step_key=None, step_spec_id=None, step_type=None, sub_pipeline_execution=None, title=None, local_vars_configuration=None):  # noqa: E501
        """ResponseReducedPipelineStepExecution - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_dt = None
        self._end_dt = None
        self._id = None
        self._judgment_result = None
        self._status = None
        self._step_key = None
        self._step_spec_id = None
        self._step_type = None
        self._sub_pipeline_execution = None
        self._title = None
        self.discriminator = None

        self.created_dt = created_dt
        self.end_dt = end_dt
        self.id = id
        self.judgment_result = judgment_result
        if status is not None:
            self.status = status
        self.step_key = step_key
        self.step_spec_id = step_spec_id
        self.step_type = step_type
        if sub_pipeline_execution is not None:
            self.sub_pipeline_execution = sub_pipeline_execution
        self.title = title

    @property
    def created_dt(self):
        """Gets the created_dt of this ResponseReducedPipelineStepExecution.  # noqa: E501


        :return: The created_dt of this ResponseReducedPipelineStepExecution.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this ResponseReducedPipelineStepExecution.


        :param created_dt: The created_dt of this ResponseReducedPipelineStepExecution.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def end_dt(self):
        """Gets the end_dt of this ResponseReducedPipelineStepExecution.  # noqa: E501


        :return: The end_dt of this ResponseReducedPipelineStepExecution.  # noqa: E501
        :rtype: datetime
        """
        return self._end_dt

    @end_dt.setter
    def end_dt(self, end_dt):
        """Sets the end_dt of this ResponseReducedPipelineStepExecution.


        :param end_dt: The end_dt of this ResponseReducedPipelineStepExecution.  # noqa: E501
        :type end_dt: datetime
        """

        self._end_dt = end_dt

    @property
    def id(self):
        """Gets the id of this ResponseReducedPipelineStepExecution.  # noqa: E501


        :return: The id of this ResponseReducedPipelineStepExecution.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResponseReducedPipelineStepExecution.


        :param id: The id of this ResponseReducedPipelineStepExecution.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def judgment_result(self):
        """Gets the judgment_result of this ResponseReducedPipelineStepExecution.  # noqa: E501


        :return: The judgment_result of this ResponseReducedPipelineStepExecution.  # noqa: E501
        :rtype: str
        """
        return self._judgment_result

    @judgment_result.setter
    def judgment_result(self, judgment_result):
        """Sets the judgment_result of this ResponseReducedPipelineStepExecution.


        :param judgment_result: The judgment_result of this ResponseReducedPipelineStepExecution.  # noqa: E501
        :type judgment_result: str
        """

        self._judgment_result = judgment_result

    @property
    def status(self):
        """Gets the status of this ResponseReducedPipelineStepExecution.  # noqa: E501


        :return: The status of this ResponseReducedPipelineStepExecution.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponseReducedPipelineStepExecution.


        :param status: The status of this ResponseReducedPipelineStepExecution.  # noqa: E501
        :type status: str
        """

        self._status = status

    @property
    def step_key(self):
        """Gets the step_key of this ResponseReducedPipelineStepExecution.  # noqa: E501


        :return: The step_key of this ResponseReducedPipelineStepExecution.  # noqa: E501
        :rtype: str
        """
        return self._step_key

    @step_key.setter
    def step_key(self, step_key):
        """Sets the step_key of this ResponseReducedPipelineStepExecution.


        :param step_key: The step_key of this ResponseReducedPipelineStepExecution.  # noqa: E501
        :type step_key: str
        """
        if self.local_vars_configuration.client_side_validation and step_key is None:  # noqa: E501
            raise ValueError("Invalid value for `step_key`, must not be `None`")  # noqa: E501

        self._step_key = step_key

    @property
    def step_spec_id(self):
        """Gets the step_spec_id of this ResponseReducedPipelineStepExecution.  # noqa: E501


        :return: The step_spec_id of this ResponseReducedPipelineStepExecution.  # noqa: E501
        :rtype: int
        """
        return self._step_spec_id

    @step_spec_id.setter
    def step_spec_id(self, step_spec_id):
        """Sets the step_spec_id of this ResponseReducedPipelineStepExecution.


        :param step_spec_id: The step_spec_id of this ResponseReducedPipelineStepExecution.  # noqa: E501
        :type step_spec_id: int
        """
        if self.local_vars_configuration.client_side_validation and step_spec_id is None:  # noqa: E501
            raise ValueError("Invalid value for `step_spec_id`, must not be `None`")  # noqa: E501

        self._step_spec_id = step_spec_id

    @property
    def step_type(self):
        """Gets the step_type of this ResponseReducedPipelineStepExecution.  # noqa: E501


        :return: The step_type of this ResponseReducedPipelineStepExecution.  # noqa: E501
        :rtype: str
        """
        return self._step_type

    @step_type.setter
    def step_type(self, step_type):
        """Sets the step_type of this ResponseReducedPipelineStepExecution.


        :param step_type: The step_type of this ResponseReducedPipelineStepExecution.  # noqa: E501
        :type step_type: str
        """
        if self.local_vars_configuration.client_side_validation and step_type is None:  # noqa: E501
            raise ValueError("Invalid value for `step_type`, must not be `None`")  # noqa: E501

        self._step_type = step_type

    @property
    def sub_pipeline_execution(self):
        """Gets the sub_pipeline_execution of this ResponseReducedPipelineStepExecution.  # noqa: E501


        :return: The sub_pipeline_execution of this ResponseReducedPipelineStepExecution.  # noqa: E501
        :rtype: ResponsePipelineExecution
        """
        return self._sub_pipeline_execution

    @sub_pipeline_execution.setter
    def sub_pipeline_execution(self, sub_pipeline_execution):
        """Sets the sub_pipeline_execution of this ResponseReducedPipelineStepExecution.


        :param sub_pipeline_execution: The sub_pipeline_execution of this ResponseReducedPipelineStepExecution.  # noqa: E501
        :type sub_pipeline_execution: ResponsePipelineExecution
        """

        self._sub_pipeline_execution = sub_pipeline_execution

    @property
    def title(self):
        """Gets the title of this ResponseReducedPipelineStepExecution.  # noqa: E501


        :return: The title of this ResponseReducedPipelineStepExecution.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ResponseReducedPipelineStepExecution.


        :param title: The title of this ResponseReducedPipelineStepExecution.  # noqa: E501
        :type title: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

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
        if not isinstance(other, ResponseReducedPipelineStepExecution):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseReducedPipelineStepExecution):
            return True

        return self.to_dict() != other.to_dict()
