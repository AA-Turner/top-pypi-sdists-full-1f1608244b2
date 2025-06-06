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


class ConditionMonitorInputV1(object):
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
        'capsule_event_types': 'list[str]',
        'condition_ids': 'list[str]',
        'cron_schedule': 'list[str]',
        'description': 'str',
        'enabled': 'bool',
        'first_run_look_back': 'int',
        'item_finder_id': 'str',
        'name': 'str',
        'query_range_look_ahead': 'int',
        'scoped_to': 'str',
        'suppressed_conditions': 'list[SuppressedConditionInputV1]',
        'timezone': 'str',
        'webhook_url': 'str'
    }

    attribute_map = {
        'capsule_event_types': 'capsuleEventTypes',
        'condition_ids': 'conditionIds',
        'cron_schedule': 'cronSchedule',
        'description': 'description',
        'enabled': 'enabled',
        'first_run_look_back': 'firstRunLookBack',
        'item_finder_id': 'itemFinderId',
        'name': 'name',
        'query_range_look_ahead': 'queryRangeLookAhead',
        'scoped_to': 'scopedTo',
        'suppressed_conditions': 'suppressedConditions',
        'timezone': 'timezone',
        'webhook_url': 'webhookUrl'
    }

    def __init__(self, capsule_event_types=None, condition_ids=None, cron_schedule=None, description=None, enabled=True, first_run_look_back=None, item_finder_id=None, name=None, query_range_look_ahead=None, scoped_to=None, suppressed_conditions=None, timezone=None, webhook_url=None):
        """
        ConditionMonitorInputV1 - a model defined in Swagger
        """

        self._capsule_event_types = None
        self._condition_ids = None
        self._cron_schedule = None
        self._description = None
        self._enabled = None
        self._first_run_look_back = None
        self._item_finder_id = None
        self._name = None
        self._query_range_look_ahead = None
        self._scoped_to = None
        self._suppressed_conditions = None
        self._timezone = None
        self._webhook_url = None

        if capsule_event_types is not None:
          self.capsule_event_types = capsule_event_types
        if condition_ids is not None:
          self.condition_ids = condition_ids
        if cron_schedule is not None:
          self.cron_schedule = cron_schedule
        if description is not None:
          self.description = description
        if enabled is not None:
          self.enabled = enabled
        if first_run_look_back is not None:
          self.first_run_look_back = first_run_look_back
        if item_finder_id is not None:
          self.item_finder_id = item_finder_id
        if name is not None:
          self.name = name
        if query_range_look_ahead is not None:
          self.query_range_look_ahead = query_range_look_ahead
        if scoped_to is not None:
          self.scoped_to = scoped_to
        if suppressed_conditions is not None:
          self.suppressed_conditions = suppressed_conditions
        if timezone is not None:
          self.timezone = timezone
        if webhook_url is not None:
          self.webhook_url = webhook_url

    @property
    def capsule_event_types(self):
        """
        Gets the capsule_event_types of this ConditionMonitorInputV1.
        The list of capsule event types to detect. The list can contain one or more of the following values: NEW: Detects new capsules that were not present in the previous run. BECAME_CERTAIN: Detects capsules that were previously uncertain and became certain. STILL_UNCERTAIN: Detects capsules that were previously uncertain and are still uncertain. EXTINCT: Detects capsules that were previously uncertain and became extinct. Defaults to [NEW, BECAME_CERTAIN, EXTINCT]

        :return: The capsule_event_types of this ConditionMonitorInputV1.
        :rtype: list[str]
        """
        return self._capsule_event_types

    @capsule_event_types.setter
    def capsule_event_types(self, capsule_event_types):
        """
        Sets the capsule_event_types of this ConditionMonitorInputV1.
        The list of capsule event types to detect. The list can contain one or more of the following values: NEW: Detects new capsules that were not present in the previous run. BECAME_CERTAIN: Detects capsules that were previously uncertain and became certain. STILL_UNCERTAIN: Detects capsules that were previously uncertain and are still uncertain. EXTINCT: Detects capsules that were previously uncertain and became extinct. Defaults to [NEW, BECAME_CERTAIN, EXTINCT]

        :param capsule_event_types: The capsule_event_types of this ConditionMonitorInputV1.
        :type: list[str]
        """
        allowed_values = ["NEW", "BECAME_CERTAIN", "EXTINCT", "STILL_UNCERTAIN"]
        if not set(capsule_event_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `capsule_event_types` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(capsule_event_types)-set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._capsule_event_types = capsule_event_types

    @property
    def condition_ids(self):
        """
        Gets the condition_ids of this ConditionMonitorInputV1.
        The IDs of conditions to monitor

        :return: The condition_ids of this ConditionMonitorInputV1.
        :rtype: list[str]
        """
        return self._condition_ids

    @condition_ids.setter
    def condition_ids(self, condition_ids):
        """
        Sets the condition_ids of this ConditionMonitorInputV1.
        The IDs of conditions to monitor

        :param condition_ids: The condition_ids of this ConditionMonitorInputV1.
        :type: list[str]
        """
        if condition_ids is None:
            raise ValueError("Invalid value for `condition_ids`, must not be `None`")

        self._condition_ids = condition_ids

    @property
    def cron_schedule(self):
        """
        Gets the cron_schedule of this ConditionMonitorInputV1.
        The condition monitor's check interval(s) as a list of cron expressions. If the list is empty, the system wide default check schedule is used. For more information about cron expressions, see  http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html

        :return: The cron_schedule of this ConditionMonitorInputV1.
        :rtype: list[str]
        """
        return self._cron_schedule

    @cron_schedule.setter
    def cron_schedule(self, cron_schedule):
        """
        Sets the cron_schedule of this ConditionMonitorInputV1.
        The condition monitor's check interval(s) as a list of cron expressions. If the list is empty, the system wide default check schedule is used. For more information about cron expressions, see  http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html

        :param cron_schedule: The cron_schedule of this ConditionMonitorInputV1.
        :type: list[str]
        """

        self._cron_schedule = cron_schedule

    @property
    def description(self):
        """
        Gets the description of this ConditionMonitorInputV1.
        Clarifying information or other plain language description of this item. An input of just whitespaces is equivalent to a null input.

        :return: The description of this ConditionMonitorInputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ConditionMonitorInputV1.
        Clarifying information or other plain language description of this item. An input of just whitespaces is equivalent to a null input.

        :param description: The description of this ConditionMonitorInputV1.
        :type: str
        """

        self._description = description

    @property
    def enabled(self):
        """
        Gets the enabled of this ConditionMonitorInputV1.
        Whether the condition monitor is enabled

        :return: The enabled of this ConditionMonitorInputV1.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this ConditionMonitorInputV1.
        Whether the condition monitor is enabled

        :param enabled: The enabled of this ConditionMonitorInputV1.
        :type: bool
        """

        self._enabled = enabled

    @property
    def first_run_look_back(self):
        """
        Gets the first_run_look_back of this ConditionMonitorInputV1.
        On first run, how far to look back for capsules, in seconds

        :return: The first_run_look_back of this ConditionMonitorInputV1.
        :rtype: int
        """
        return self._first_run_look_back

    @first_run_look_back.setter
    def first_run_look_back(self, first_run_look_back):
        """
        Sets the first_run_look_back of this ConditionMonitorInputV1.
        On first run, how far to look back for capsules, in seconds

        :param first_run_look_back: The first_run_look_back of this ConditionMonitorInputV1.
        :type: int
        """

        self._first_run_look_back = first_run_look_back

    @property
    def item_finder_id(self):
        """
        Gets the item_finder_id of this ConditionMonitorInputV1.
        The ID of an Item Finder to use to populate the list of conditions. If this is provided it will overwrite the list of conditionIds

        :return: The item_finder_id of this ConditionMonitorInputV1.
        :rtype: str
        """
        return self._item_finder_id

    @item_finder_id.setter
    def item_finder_id(self, item_finder_id):
        """
        Sets the item_finder_id of this ConditionMonitorInputV1.
        The ID of an Item Finder to use to populate the list of conditions. If this is provided it will overwrite the list of conditionIds

        :param item_finder_id: The item_finder_id of this ConditionMonitorInputV1.
        :type: str
        """

        self._item_finder_id = item_finder_id

    @property
    def name(self):
        """
        Gets the name of this ConditionMonitorInputV1.
        Human readable name. Required during creation. An input of just whitespaces is equivalent to a null input.

        :return: The name of this ConditionMonitorInputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ConditionMonitorInputV1.
        Human readable name. Required during creation. An input of just whitespaces is equivalent to a null input.

        :param name: The name of this ConditionMonitorInputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def query_range_look_ahead(self):
        """
        Gets the query_range_look_ahead of this ConditionMonitorInputV1.
        Query range look ahead in seconds

        :return: The query_range_look_ahead of this ConditionMonitorInputV1.
        :rtype: int
        """
        return self._query_range_look_ahead

    @query_range_look_ahead.setter
    def query_range_look_ahead(self, query_range_look_ahead):
        """
        Sets the query_range_look_ahead of this ConditionMonitorInputV1.
        Query range look ahead in seconds

        :param query_range_look_ahead: The query_range_look_ahead of this ConditionMonitorInputV1.
        :type: int
        """

        self._query_range_look_ahead = query_range_look_ahead

    @property
    def scoped_to(self):
        """
        Gets the scoped_to of this ConditionMonitorInputV1.

        :return: The scoped_to of this ConditionMonitorInputV1.
        :rtype: str
        """
        return self._scoped_to

    @scoped_to.setter
    def scoped_to(self, scoped_to):
        """
        Sets the scoped_to of this ConditionMonitorInputV1.

        :param scoped_to: The scoped_to of this ConditionMonitorInputV1.
        :type: str
        """

        self._scoped_to = scoped_to

    @property
    def suppressed_conditions(self):
        """
        Gets the suppressed_conditions of this ConditionMonitorInputV1.
        The conditions and associated logic to suppress in this monitor

        :return: The suppressed_conditions of this ConditionMonitorInputV1.
        :rtype: list[SuppressedConditionInputV1]
        """
        return self._suppressed_conditions

    @suppressed_conditions.setter
    def suppressed_conditions(self, suppressed_conditions):
        """
        Sets the suppressed_conditions of this ConditionMonitorInputV1.
        The conditions and associated logic to suppress in this monitor

        :param suppressed_conditions: The suppressed_conditions of this ConditionMonitorInputV1.
        :type: list[SuppressedConditionInputV1]
        """

        self._suppressed_conditions = suppressed_conditions

    @property
    def timezone(self):
        """
        Gets the timezone of this ConditionMonitorInputV1.
        The IANA timezone in which the scheduled times will be run, defaults to UTC

        :return: The timezone of this ConditionMonitorInputV1.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this ConditionMonitorInputV1.
        The IANA timezone in which the scheduled times will be run, defaults to UTC

        :param timezone: The timezone of this ConditionMonitorInputV1.
        :type: str
        """

        self._timezone = timezone

    @property
    def webhook_url(self):
        """
        Gets the webhook_url of this ConditionMonitorInputV1.
        A URL that is invoked whenever new capsules are found or existing capsules end in any of the conditions. Can either be a URL path relative to the Seeq server or a fully-qualified URL

        :return: The webhook_url of this ConditionMonitorInputV1.
        :rtype: str
        """
        return self._webhook_url

    @webhook_url.setter
    def webhook_url(self, webhook_url):
        """
        Sets the webhook_url of this ConditionMonitorInputV1.
        A URL that is invoked whenever new capsules are found or existing capsules end in any of the conditions. Can either be a URL path relative to the Seeq server or a fully-qualified URL

        :param webhook_url: The webhook_url of this ConditionMonitorInputV1.
        :type: str
        """

        self._webhook_url = webhook_url

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
        if not isinstance(other, ConditionMonitorInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
