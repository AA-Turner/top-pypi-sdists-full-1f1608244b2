# encoding: utf-8
#
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at https://www.mozilla.org/en-US/MPL/2.0/.
#
# Contact: Kyle Lahnakoski (kyle@lahnakoski.com)
#
import json as _json
from datetime import date, datetime
from datetime import timezone

from mo_future import utcfromtimestamp

MAX_TIME = datetime(2286, 11, 20, 17, 46, 39, 0, timezone.utc)


def unix2datetime(u):
    try:
        if u == None:
            return None
        if u == 9999999999:  # PYPY BUG https://bugs.pypy.org/issue1697
            return MAX_TIME
        return utcfromtimestamp(u)
    except Exception as e:
        from mo_logs import logger

        logger.error("Can not convert {value} to datetime", value=u, cause=e)


def milli2datetime(u):
    if u == None:
        return None
    return unix2datetime(u / 1000.0)


def datetime2string(value, format="%Y-%m-%d %H:%M:%S"):
    try:
        return value.strftime(format)
    except Exception as e:
        from mo_logs import logger

        logger.error(
            "Can not format {value} with {format}", value=value, format=format, cause=e,
        )


def datetime2unix(d):
    try:
        if d == None:
            return None
        elif isinstance(d, datetime.datetime):
            epoch = datetime(1970, 1, 1)
        elif isinstance(d, date):
            epoch = date(1970, 1, 1)
        else:
            from mo_logs import logger

            raise logger.error("Can not convert {value} of type {type}", value=d, type=d.__class__)

        diff = d - epoch
        return float(diff.total_seconds())
    except Exception as e:
        from mo_logs import logger

        logger.error("Can not convert {value}", value=d, cause=e)


def int2hex(value, size):
    return (("0" * size) + hex(value)[2:])[-size:]


_map2url = {chr(i).encode("latin1"): chr(i) for i in range(32, 256)}
for c in [
    b" ",
    b"{",
    b"}",
    b"<",
    b">",
    b";",
    b"/",
    b"?",
    b":",
    b"@",
    b"&",
    b"=",
    b"+",
    b"$",
    b",",
    b"%",
]:
    _map2url[c] = "%" + int2hex(ord(c.decode("latin1")), 2)


def value2json(value):
    return _json.dumps(value)


def unicode2latin1(value):
    output = value.encode("latin1")
    return output
