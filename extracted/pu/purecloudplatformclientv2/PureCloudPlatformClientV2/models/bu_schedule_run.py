# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from datetime import datetime
from datetime import date
from pprint import pformat
import re
import json

from ..utils import sanitize_for_serialization

# type hinting support
from typing import TYPE_CHECKING
from typing import List
from typing import Dict

if TYPE_CHECKING:
    from . import BuScheduleReference
    from . import ReschedulingOptionsRunResponse
    from . import SchedulerMessageSeverityCount
    from . import UserReference

class BuScheduleRun(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        BuScheduleRun - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'scheduler_run_id': 'str',
            'intraday_rescheduling': 'bool',
            'state': 'str',
            'week_count': 'int',
            'percent_complete': 'float',
            'target_week': 'date',
            'schedule': 'BuScheduleReference',
            'schedule_description': 'str',
            'scheduling_start_time': 'datetime',
            'scheduling_started_by': 'UserReference',
            'scheduling_canceled_by': 'UserReference',
            'scheduling_completed_time': 'datetime',
            'message_count': 'int',
            'message_severity_counts': 'list[SchedulerMessageSeverityCount]',
            'rescheduling_options': 'ReschedulingOptionsRunResponse',
            'rescheduling_result_expiration': 'datetime',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'scheduler_run_id': 'schedulerRunId',
            'intraday_rescheduling': 'intradayRescheduling',
            'state': 'state',
            'week_count': 'weekCount',
            'percent_complete': 'percentComplete',
            'target_week': 'targetWeek',
            'schedule': 'schedule',
            'schedule_description': 'scheduleDescription',
            'scheduling_start_time': 'schedulingStartTime',
            'scheduling_started_by': 'schedulingStartedBy',
            'scheduling_canceled_by': 'schedulingCanceledBy',
            'scheduling_completed_time': 'schedulingCompletedTime',
            'message_count': 'messageCount',
            'message_severity_counts': 'messageSeverityCounts',
            'rescheduling_options': 'reschedulingOptions',
            'rescheduling_result_expiration': 'reschedulingResultExpiration',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._scheduler_run_id = None
        self._intraday_rescheduling = None
        self._state = None
        self._week_count = None
        self._percent_complete = None
        self._target_week = None
        self._schedule = None
        self._schedule_description = None
        self._scheduling_start_time = None
        self._scheduling_started_by = None
        self._scheduling_canceled_by = None
        self._scheduling_completed_time = None
        self._message_count = None
        self._message_severity_counts = None
        self._rescheduling_options = None
        self._rescheduling_result_expiration = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this BuScheduleRun.
        The globally unique identifier for the object.

        :return: The id of this BuScheduleRun.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this BuScheduleRun.
        The globally unique identifier for the object.

        :param id: The id of this BuScheduleRun.
        :type: str
        """
        

        self._id = id

    @property
    def scheduler_run_id(self) -> str:
        """
        Gets the scheduler_run_id of this BuScheduleRun.
        The scheduler run ID.  Reference this value for support

        :return: The scheduler_run_id of this BuScheduleRun.
        :rtype: str
        """
        return self._scheduler_run_id

    @scheduler_run_id.setter
    def scheduler_run_id(self, scheduler_run_id: str) -> None:
        """
        Sets the scheduler_run_id of this BuScheduleRun.
        The scheduler run ID.  Reference this value for support

        :param scheduler_run_id: The scheduler_run_id of this BuScheduleRun.
        :type: str
        """
        

        self._scheduler_run_id = scheduler_run_id

    @property
    def intraday_rescheduling(self) -> bool:
        """
        Gets the intraday_rescheduling of this BuScheduleRun.
        Whether this is an intraday rescheduling run

        :return: The intraday_rescheduling of this BuScheduleRun.
        :rtype: bool
        """
        return self._intraday_rescheduling

    @intraday_rescheduling.setter
    def intraday_rescheduling(self, intraday_rescheduling: bool) -> None:
        """
        Sets the intraday_rescheduling of this BuScheduleRun.
        Whether this is an intraday rescheduling run

        :param intraday_rescheduling: The intraday_rescheduling of this BuScheduleRun.
        :type: bool
        """
        

        self._intraday_rescheduling = intraday_rescheduling

    @property
    def state(self) -> str:
        """
        Gets the state of this BuScheduleRun.
        The state of the generation run

        :return: The state of this BuScheduleRun.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str) -> None:
        """
        Sets the state of this BuScheduleRun.
        The state of the generation run

        :param state: The state of this BuScheduleRun.
        :type: str
        """
        if isinstance(state, int):
            state = str(state)
        allowed_values = ["None", "Queued", "Scheduling", "Canceled", "Failed", "Complete"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def week_count(self) -> int:
        """
        Gets the week_count of this BuScheduleRun.
        The number of weeks spanned by the schedule

        :return: The week_count of this BuScheduleRun.
        :rtype: int
        """
        return self._week_count

    @week_count.setter
    def week_count(self, week_count: int) -> None:
        """
        Sets the week_count of this BuScheduleRun.
        The number of weeks spanned by the schedule

        :param week_count: The week_count of this BuScheduleRun.
        :type: int
        """
        

        self._week_count = week_count

    @property
    def percent_complete(self) -> float:
        """
        Gets the percent_complete of this BuScheduleRun.
        Percent completion of the schedule run

        :return: The percent_complete of this BuScheduleRun.
        :rtype: float
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete: float) -> None:
        """
        Sets the percent_complete of this BuScheduleRun.
        Percent completion of the schedule run

        :param percent_complete: The percent_complete of this BuScheduleRun.
        :type: float
        """
        

        self._percent_complete = percent_complete

    @property
    def target_week(self) -> date:
        """
        Gets the target_week of this BuScheduleRun.
        The start date of the target week. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

        :return: The target_week of this BuScheduleRun.
        :rtype: date
        """
        return self._target_week

    @target_week.setter
    def target_week(self, target_week: date) -> None:
        """
        Sets the target_week of this BuScheduleRun.
        The start date of the target week. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

        :param target_week: The target_week of this BuScheduleRun.
        :type: date
        """
        

        self._target_week = target_week

    @property
    def schedule(self) -> 'BuScheduleReference':
        """
        Gets the schedule of this BuScheduleRun.
        The generated schedule.  Null unless the schedule run is complete

        :return: The schedule of this BuScheduleRun.
        :rtype: BuScheduleReference
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule: 'BuScheduleReference') -> None:
        """
        Sets the schedule of this BuScheduleRun.
        The generated schedule.  Null unless the schedule run is complete

        :param schedule: The schedule of this BuScheduleRun.
        :type: BuScheduleReference
        """
        

        self._schedule = schedule

    @property
    def schedule_description(self) -> str:
        """
        Gets the schedule_description of this BuScheduleRun.
        The description of the generated schedule

        :return: The schedule_description of this BuScheduleRun.
        :rtype: str
        """
        return self._schedule_description

    @schedule_description.setter
    def schedule_description(self, schedule_description: str) -> None:
        """
        Sets the schedule_description of this BuScheduleRun.
        The description of the generated schedule

        :param schedule_description: The schedule_description of this BuScheduleRun.
        :type: str
        """
        

        self._schedule_description = schedule_description

    @property
    def scheduling_start_time(self) -> datetime:
        """
        Gets the scheduling_start_time of this BuScheduleRun.
        When the schedule generation run started. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The scheduling_start_time of this BuScheduleRun.
        :rtype: datetime
        """
        return self._scheduling_start_time

    @scheduling_start_time.setter
    def scheduling_start_time(self, scheduling_start_time: datetime) -> None:
        """
        Sets the scheduling_start_time of this BuScheduleRun.
        When the schedule generation run started. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param scheduling_start_time: The scheduling_start_time of this BuScheduleRun.
        :type: datetime
        """
        

        self._scheduling_start_time = scheduling_start_time

    @property
    def scheduling_started_by(self) -> 'UserReference':
        """
        Gets the scheduling_started_by of this BuScheduleRun.
        The user who started the scheduling run

        :return: The scheduling_started_by of this BuScheduleRun.
        :rtype: UserReference
        """
        return self._scheduling_started_by

    @scheduling_started_by.setter
    def scheduling_started_by(self, scheduling_started_by: 'UserReference') -> None:
        """
        Sets the scheduling_started_by of this BuScheduleRun.
        The user who started the scheduling run

        :param scheduling_started_by: The scheduling_started_by of this BuScheduleRun.
        :type: UserReference
        """
        

        self._scheduling_started_by = scheduling_started_by

    @property
    def scheduling_canceled_by(self) -> 'UserReference':
        """
        Gets the scheduling_canceled_by of this BuScheduleRun.
        The user who canceled the scheduling run, if applicable

        :return: The scheduling_canceled_by of this BuScheduleRun.
        :rtype: UserReference
        """
        return self._scheduling_canceled_by

    @scheduling_canceled_by.setter
    def scheduling_canceled_by(self, scheduling_canceled_by: 'UserReference') -> None:
        """
        Sets the scheduling_canceled_by of this BuScheduleRun.
        The user who canceled the scheduling run, if applicable

        :param scheduling_canceled_by: The scheduling_canceled_by of this BuScheduleRun.
        :type: UserReference
        """
        

        self._scheduling_canceled_by = scheduling_canceled_by

    @property
    def scheduling_completed_time(self) -> datetime:
        """
        Gets the scheduling_completed_time of this BuScheduleRun.
        When the scheduling run was completed, if applicable. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The scheduling_completed_time of this BuScheduleRun.
        :rtype: datetime
        """
        return self._scheduling_completed_time

    @scheduling_completed_time.setter
    def scheduling_completed_time(self, scheduling_completed_time: datetime) -> None:
        """
        Sets the scheduling_completed_time of this BuScheduleRun.
        When the scheduling run was completed, if applicable. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param scheduling_completed_time: The scheduling_completed_time of this BuScheduleRun.
        :type: datetime
        """
        

        self._scheduling_completed_time = scheduling_completed_time

    @property
    def message_count(self) -> int:
        """
        Gets the message_count of this BuScheduleRun.
        The number of schedule generation messages for this schedule generation run

        :return: The message_count of this BuScheduleRun.
        :rtype: int
        """
        return self._message_count

    @message_count.setter
    def message_count(self, message_count: int) -> None:
        """
        Sets the message_count of this BuScheduleRun.
        The number of schedule generation messages for this schedule generation run

        :param message_count: The message_count of this BuScheduleRun.
        :type: int
        """
        

        self._message_count = message_count

    @property
    def message_severity_counts(self) -> List['SchedulerMessageSeverityCount']:
        """
        Gets the message_severity_counts of this BuScheduleRun.
        The list of schedule generation message counts by severity for this schedule generation run

        :return: The message_severity_counts of this BuScheduleRun.
        :rtype: list[SchedulerMessageSeverityCount]
        """
        return self._message_severity_counts

    @message_severity_counts.setter
    def message_severity_counts(self, message_severity_counts: List['SchedulerMessageSeverityCount']) -> None:
        """
        Sets the message_severity_counts of this BuScheduleRun.
        The list of schedule generation message counts by severity for this schedule generation run

        :param message_severity_counts: The message_severity_counts of this BuScheduleRun.
        :type: list[SchedulerMessageSeverityCount]
        """
        

        self._message_severity_counts = message_severity_counts

    @property
    def rescheduling_options(self) -> 'ReschedulingOptionsRunResponse':
        """
        Gets the rescheduling_options of this BuScheduleRun.
        Rescheduling options for this run.  Null unless intradayRescheduling is true

        :return: The rescheduling_options of this BuScheduleRun.
        :rtype: ReschedulingOptionsRunResponse
        """
        return self._rescheduling_options

    @rescheduling_options.setter
    def rescheduling_options(self, rescheduling_options: 'ReschedulingOptionsRunResponse') -> None:
        """
        Sets the rescheduling_options of this BuScheduleRun.
        Rescheduling options for this run.  Null unless intradayRescheduling is true

        :param rescheduling_options: The rescheduling_options of this BuScheduleRun.
        :type: ReschedulingOptionsRunResponse
        """
        

        self._rescheduling_options = rescheduling_options

    @property
    def rescheduling_result_expiration(self) -> datetime:
        """
        Gets the rescheduling_result_expiration of this BuScheduleRun.
        When the reschedule result will expire.  Null unless intradayRescheduling is true. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The rescheduling_result_expiration of this BuScheduleRun.
        :rtype: datetime
        """
        return self._rescheduling_result_expiration

    @rescheduling_result_expiration.setter
    def rescheduling_result_expiration(self, rescheduling_result_expiration: datetime) -> None:
        """
        Sets the rescheduling_result_expiration of this BuScheduleRun.
        When the reschedule result will expire.  Null unless intradayRescheduling is true. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param rescheduling_result_expiration: The rescheduling_result_expiration of this BuScheduleRun.
        :type: datetime
        """
        

        self._rescheduling_result_expiration = rescheduling_result_expiration

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this BuScheduleRun.
        The URI for this object

        :return: The self_uri of this BuScheduleRun.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this BuScheduleRun.
        The URI for this object

        :param self_uri: The self_uri of this BuScheduleRun.
        :type: str
        """
        

        self._self_uri = self_uri

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in self.swagger_types.items():
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

    def to_json(self):
        """
        Returns the model as raw JSON
        """
        return json.dumps(sanitize_for_serialization(self.to_dict()))

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

