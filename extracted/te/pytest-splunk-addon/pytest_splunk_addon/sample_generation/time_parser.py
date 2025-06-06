#
# Copyright 2025 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from datetime import timedelta, datetime
import math
import logging
import re

LOGGER = logging.getLogger("pytest-splunk-addon")


class time_parse:
    def __init__(self):
        pass

    def convert_to_time(self, sign, num, unit):
        """
        converts splunk time into datetime format for earliest and latest

        Args :
            sign (str): to increase or decrease time
            num (num): time value
            unit (str): unit of time eg: seconds,minutes etc

        Returns :
            datetime formatted time
        """
        num = int(num)
        unittime = None
        if unit in ("s", "sec", "secs", "second", "seconds"):
            unittime = timedelta(seconds=int(num))
        elif unit in ("m", "min", "minute", "minutes"):
            unittime = timedelta(minutes=int(num))
        elif unit in ("h", "hr", "hrs", "hour", "hours"):
            unittime = timedelta(hours=int(num))
        elif unit in ("d", "day", "days"):
            unittime = timedelta(days=int(num))
        elif unit in ("w", "week", "weeks"):
            unittime = timedelta(days=(int(num) * 7))
        elif (
            unit in ("mon", "month", "months")
            or unit in ("q", "qtr", "qtrs", "quarter", "quarters")
            or unit in ("y", "yr", "yrs", "year", "years")
        ):
            if unit in ("q", "qtr", "qtrs", "quarter", "quarters"):
                num *= 3
            elif unit in ("y", "yr", "yrs", "year", "years"):
                num = num * 12

            unittime = datetime.utcnow()
            monthnum = int(num) * -1 if sign == "-" else int(num)

            if int(abs(monthnum) / 12) > 0:
                # if months are more than 12 than increase or decrease the year based on the sign value
                yearnum = int(
                    math.floor(abs(monthnum) / 12) * -1
                    if sign == "-"
                    else int(math.floor(abs(monthnum) / 12))
                )
                monthnum = int(
                    (abs(monthnum) % 12) * -1
                    if sign == "-"
                    else int((abs(monthnum) % 12))
                )
                unittime = datetime(
                    unittime.year + yearnum,
                    unittime.month + monthnum,
                    unittime.day,
                    unittime.hour,
                    unittime.minute,
                    unittime.second,
                    unittime.microsecond,
                )
            elif monthnum > 0:
                if unittime.month + monthnum > 12:
                    # if
                    unittime = datetime(
                        unittime.year + 1,
                        ((unittime.month + monthnum) % 12),
                        unittime.day,
                        unittime.hour,
                        unittime.minute,
                        unittime.second,
                        unittime.microsecond,
                    )
                else:
                    unittime = datetime(
                        unittime.year,
                        unittime.month + monthnum,
                        unittime.day,
                        unittime.hour,
                        unittime.minute,
                        unittime.second,
                        unittime.microsecond,
                    )
            elif monthnum <= 0:
                if unittime.month + monthnum <= 0:
                    unittime = datetime(
                        unittime.year - 1,
                        (12 - abs(unittime.month + monthnum)),
                        unittime.day,
                        unittime.hour,
                        unittime.minute,
                        unittime.second,
                        unittime.microsecond,
                    )
                else:
                    unittime = datetime(
                        unittime.year,
                        unittime.month + monthnum,
                        unittime.day,
                        unittime.hour,
                        unittime.minute,
                        unittime.second,
                        unittime.microsecond,
                    )
            return unittime
        random_time = datetime.utcnow()
        if sign == "-":
            random_time = random_time - unittime
        else:
            random_time = random_time + unittime

        return random_time

    def get_timezone_time(self, random_time, timezone_time):
        """
        Converts timezone formatted time into datetime object for earliest and latest

        Args:
            random_time (datetime): datetime object
            timezone_time (str): timezone time string

        Returns:
            datetime formatted time
        """

        sign, hrs, mins = re.match(r"([+-])(\d\d)(\d\d)", timezone_time).groups()

        if (hrs <= "00" or hrs >= "23") or (mins <= "00" or mins >= "59"):
            LOGGER.info(
                "Provided the following Hrs:%s and Mins:%s. Hours should be in range 0-23 and minutes should be in range 0-59",
                hrs,
                mins,
            )
            return random_time
        if sign == "-":
            random_time = random_time - timedelta(hours=int(hrs), minutes=int(mins))
        else:
            random_time = random_time + timedelta(hours=int(hrs), minutes=int(mins))
        LOGGER.info("Returning the following time for the timezone: %s", random_time)
        return random_time
