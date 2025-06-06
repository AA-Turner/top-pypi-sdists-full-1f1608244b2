# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 66.25.0-v202506042330-CD
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class ThresholdMetricInputV1(object):
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
        'additional_properties': 'list[ScalarPropertyV1]',
        'aggregation_function': 'str',
        'bounding_condition': 'str',
        'bounding_condition_maximum_duration': 'str',
        'data_id': 'str',
        'datasource_class': 'str',
        'datasource_id': 'str',
        'duration': 'str',
        'measured_item': 'str',
        'name': 'str',
        'neutral_color': 'str',
        'number_format': 'str',
        'period': 'str',
        'scoped_to': 'str',
        'sync_token': 'str',
        'thresholds': 'list[str]'
    }

    attribute_map = {
        'additional_properties': 'additionalProperties',
        'aggregation_function': 'aggregationFunction',
        'bounding_condition': 'boundingCondition',
        'bounding_condition_maximum_duration': 'boundingConditionMaximumDuration',
        'data_id': 'dataId',
        'datasource_class': 'datasourceClass',
        'datasource_id': 'datasourceId',
        'duration': 'duration',
        'measured_item': 'measuredItem',
        'name': 'name',
        'neutral_color': 'neutralColor',
        'number_format': 'numberFormat',
        'period': 'period',
        'scoped_to': 'scopedTo',
        'sync_token': 'syncToken',
        'thresholds': 'thresholds'
    }

    def __init__(self, additional_properties=None, aggregation_function=None, bounding_condition=None, bounding_condition_maximum_duration=None, data_id=None, datasource_class=None, datasource_id=None, duration=None, measured_item=None, name=None, neutral_color=None, number_format=None, period=None, scoped_to=None, sync_token=None, thresholds=None):
        """
        ThresholdMetricInputV1 - a model defined in Swagger
        """

        self._additional_properties = None
        self._aggregation_function = None
        self._bounding_condition = None
        self._bounding_condition_maximum_duration = None
        self._data_id = None
        self._datasource_class = None
        self._datasource_id = None
        self._duration = None
        self._measured_item = None
        self._name = None
        self._neutral_color = None
        self._number_format = None
        self._period = None
        self._scoped_to = None
        self._sync_token = None
        self._thresholds = None

        if additional_properties is not None:
          self.additional_properties = additional_properties
        if aggregation_function is not None:
          self.aggregation_function = aggregation_function
        if bounding_condition is not None:
          self.bounding_condition = bounding_condition
        if bounding_condition_maximum_duration is not None:
          self.bounding_condition_maximum_duration = bounding_condition_maximum_duration
        if data_id is not None:
          self.data_id = data_id
        if datasource_class is not None:
          self.datasource_class = datasource_class
        if datasource_id is not None:
          self.datasource_id = datasource_id
        if duration is not None:
          self.duration = duration
        if measured_item is not None:
          self.measured_item = measured_item
        if name is not None:
          self.name = name
        if neutral_color is not None:
          self.neutral_color = neutral_color
        if number_format is not None:
          self.number_format = number_format
        if period is not None:
          self.period = period
        if scoped_to is not None:
          self.scoped_to = scoped_to
        if sync_token is not None:
          self.sync_token = sync_token
        if thresholds is not None:
          self.thresholds = thresholds

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this ThresholdMetricInputV1.
        Additional properties to set on this threshold metric. A property consists of a name, a value, and a unit of measure.

        :return: The additional_properties of this ThresholdMetricInputV1.
        :rtype: list[ScalarPropertyV1]
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this ThresholdMetricInputV1.
        Additional properties to set on this threshold metric. A property consists of a name, a value, and a unit of measure.

        :param additional_properties: The additional_properties of this ThresholdMetricInputV1.
        :type: list[ScalarPropertyV1]
        """

        self._additional_properties = additional_properties

    @property
    def aggregation_function(self):
        """
        Gets the aggregation_function of this ThresholdMetricInputV1.
        Aggregation formula function that can aggregate the measured item and used when evaluating the thresholds as well as for display in outputs such as scorecard.

        :return: The aggregation_function of this ThresholdMetricInputV1.
        :rtype: str
        """
        return self._aggregation_function

    @aggregation_function.setter
    def aggregation_function(self, aggregation_function):
        """
        Sets the aggregation_function of this ThresholdMetricInputV1.
        Aggregation formula function that can aggregate the measured item and used when evaluating the thresholds as well as for display in outputs such as scorecard.

        :param aggregation_function: The aggregation_function of this ThresholdMetricInputV1.
        :type: str
        """

        self._aggregation_function = aggregation_function

    @property
    def bounding_condition(self):
        """
        Gets the bounding_condition of this ThresholdMetricInputV1.
        Used when measuring a batch process, the ID of a condition that will be used to aggregate the measured item and to break scorecard output into multiple columns, one per capsule.

        :return: The bounding_condition of this ThresholdMetricInputV1.
        :rtype: str
        """
        return self._bounding_condition

    @bounding_condition.setter
    def bounding_condition(self, bounding_condition):
        """
        Sets the bounding_condition of this ThresholdMetricInputV1.
        Used when measuring a batch process, the ID of a condition that will be used to aggregate the measured item and to break scorecard output into multiple columns, one per capsule.

        :param bounding_condition: The bounding_condition of this ThresholdMetricInputV1.
        :type: str
        """

        self._bounding_condition = bounding_condition

    @property
    def bounding_condition_maximum_duration(self):
        """
        Gets the bounding_condition_maximum_duration of this ThresholdMetricInputV1.
        If bounding condition is used and does not have a Maximum Capsule Duration this value must be supplied to allow aggregation.

        :return: The bounding_condition_maximum_duration of this ThresholdMetricInputV1.
        :rtype: str
        """
        return self._bounding_condition_maximum_duration

    @bounding_condition_maximum_duration.setter
    def bounding_condition_maximum_duration(self, bounding_condition_maximum_duration):
        """
        Sets the bounding_condition_maximum_duration of this ThresholdMetricInputV1.
        If bounding condition is used and does not have a Maximum Capsule Duration this value must be supplied to allow aggregation.

        :param bounding_condition_maximum_duration: The bounding_condition_maximum_duration of this ThresholdMetricInputV1.
        :type: str
        """

        self._bounding_condition_maximum_duration = bounding_condition_maximum_duration

    @property
    def data_id(self):
        """
        Gets the data_id of this ThresholdMetricInputV1.
        A unique identifier for the metric within its datasource.

        :return: The data_id of this ThresholdMetricInputV1.
        :rtype: str
        """
        return self._data_id

    @data_id.setter
    def data_id(self, data_id):
        """
        Sets the data_id of this ThresholdMetricInputV1.
        A unique identifier for the metric within its datasource.

        :param data_id: The data_id of this ThresholdMetricInputV1.
        :type: str
        """

        self._data_id = data_id

    @property
    def datasource_class(self):
        """
        Gets the datasource_class of this ThresholdMetricInputV1.
        Along with the Datasource ID, the Datasource Class uniquely identifies a datasource. For example, a datasource may be a particular instance of an OSIsoft PI historian.

        :return: The datasource_class of this ThresholdMetricInputV1.
        :rtype: str
        """
        return self._datasource_class

    @datasource_class.setter
    def datasource_class(self, datasource_class):
        """
        Sets the datasource_class of this ThresholdMetricInputV1.
        Along with the Datasource ID, the Datasource Class uniquely identifies a datasource. For example, a datasource may be a particular instance of an OSIsoft PI historian.

        :param datasource_class: The datasource_class of this ThresholdMetricInputV1.
        :type: str
        """

        self._datasource_class = datasource_class

    @property
    def datasource_id(self):
        """
        Gets the datasource_id of this ThresholdMetricInputV1.
        Along with the Datasource Class, the Datasource ID uniquely identifies a datasource. For example, a datasource may be a particular instance of an OSIsoft PI historian.

        :return: The datasource_id of this ThresholdMetricInputV1.
        :rtype: str
        """
        return self._datasource_id

    @datasource_id.setter
    def datasource_id(self, datasource_id):
        """
        Sets the datasource_id of this ThresholdMetricInputV1.
        Along with the Datasource Class, the Datasource ID uniquely identifies a datasource. For example, a datasource may be a particular instance of an OSIsoft PI historian.

        :param datasource_id: The datasource_id of this ThresholdMetricInputV1.
        :type: str
        """

        self._datasource_id = datasource_id

    @property
    def duration(self):
        """
        Gets the duration of this ThresholdMetricInputV1.
        Used when measuring a continuous process, the duration over which to calculate a moving aggregation. Example: 1day

        :return: The duration of this ThresholdMetricInputV1.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this ThresholdMetricInputV1.
        Used when measuring a continuous process, the duration over which to calculate a moving aggregation. Example: 1day

        :param duration: The duration of this ThresholdMetricInputV1.
        :type: str
        """

        self._duration = duration

    @property
    def measured_item(self):
        """
        Gets the measured_item of this ThresholdMetricInputV1.
        ID of an input Signal or Condition to measure. This item is measured using the thresholds to find deviations.

        :return: The measured_item of this ThresholdMetricInputV1.
        :rtype: str
        """
        return self._measured_item

    @measured_item.setter
    def measured_item(self, measured_item):
        """
        Sets the measured_item of this ThresholdMetricInputV1.
        ID of an input Signal or Condition to measure. This item is measured using the thresholds to find deviations.

        :param measured_item: The measured_item of this ThresholdMetricInputV1.
        :type: str
        """
        if measured_item is None:
            raise ValueError("Invalid value for `measured_item`, must not be `None`")

        self._measured_item = measured_item

    @property
    def name(self):
        """
        Gets the name of this ThresholdMetricInputV1.
        The name of the metric.

        :return: The name of this ThresholdMetricInputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ThresholdMetricInputV1.
        The name of the metric.

        :param name: The name of this ThresholdMetricInputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def neutral_color(self):
        """
        Gets the neutral_color of this ThresholdMetricInputV1.
        A hex code that specifies a color that will override the neutral (level 0) priority color

        :return: The neutral_color of this ThresholdMetricInputV1.
        :rtype: str
        """
        return self._neutral_color

    @neutral_color.setter
    def neutral_color(self, neutral_color):
        """
        Sets the neutral_color of this ThresholdMetricInputV1.
        A hex code that specifies a color that will override the neutral (level 0) priority color

        :param neutral_color: The neutral_color of this ThresholdMetricInputV1.
        :type: str
        """

        self._neutral_color = neutral_color

    @property
    def number_format(self):
        """
        Gets the number_format of this ThresholdMetricInputV1.
        The format string used for numbers associated with this signal. The format for the string follows ECMA-376 spreadsheet format standards.

        :return: The number_format of this ThresholdMetricInputV1.
        :rtype: str
        """
        return self._number_format

    @number_format.setter
    def number_format(self, number_format):
        """
        Sets the number_format of this ThresholdMetricInputV1.
        The format string used for numbers associated with this signal. The format for the string follows ECMA-376 spreadsheet format standards.

        :param number_format: The number_format of this ThresholdMetricInputV1.
        :type: str
        """

        self._number_format = number_format

    @property
    def period(self):
        """
        Gets the period of this ThresholdMetricInputV1.
        Used when measuring a continuous process, the period at which to sample when creating the moving aggregation. Example: 30min

        :return: The period of this ThresholdMetricInputV1.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """
        Sets the period of this ThresholdMetricInputV1.
        Used when measuring a continuous process, the period at which to sample when creating the moving aggregation. Example: 30min

        :param period: The period of this ThresholdMetricInputV1.
        :type: str
        """

        self._period = period

    @property
    def scoped_to(self):
        """
        Gets the scoped_to of this ThresholdMetricInputV1.
        The ID of the workbook to which this item will be scoped.

        :return: The scoped_to of this ThresholdMetricInputV1.
        :rtype: str
        """
        return self._scoped_to

    @scoped_to.setter
    def scoped_to(self, scoped_to):
        """
        Sets the scoped_to of this ThresholdMetricInputV1.
        The ID of the workbook to which this item will be scoped.

        :param scoped_to: The scoped_to of this ThresholdMetricInputV1.
        :type: str
        """

        self._scoped_to = scoped_to

    @property
    def sync_token(self):
        """
        Gets the sync_token of this ThresholdMetricInputV1.
        An arbitrary token (often a date or random ID) that is used during metadata syncs. At the end of a full sync, items with mismatching sync tokens are identified as stale and will be archived using the Datasources clean-up API.

        :return: The sync_token of this ThresholdMetricInputV1.
        :rtype: str
        """
        return self._sync_token

    @sync_token.setter
    def sync_token(self, sync_token):
        """
        Sets the sync_token of this ThresholdMetricInputV1.
        An arbitrary token (often a date or random ID) that is used during metadata syncs. At the end of a full sync, items with mismatching sync tokens are identified as stale and will be archived using the Datasources clean-up API.

        :param sync_token: The sync_token of this ThresholdMetricInputV1.
        :type: str
        """

        self._sync_token = sync_token

    @property
    def thresholds(self):
        """
        Gets the thresholds of this ThresholdMetricInputV1.

        :return: The thresholds of this ThresholdMetricInputV1.
        :rtype: list[str]
        """
        return self._thresholds

    @thresholds.setter
    def thresholds(self, thresholds):
        """
        Sets the thresholds of this ThresholdMetricInputV1.

        :param thresholds: The thresholds of this ThresholdMetricInputV1.
        :type: list[str]
        """

        self._thresholds = thresholds

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
        if not isinstance(other, ThresholdMetricInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
