# (C) Copyright 2019- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.

import typing as T

import eccodes  # type: ignore
import numpy as np
import pytest

from pdbufr import stream_bufr
from pdbufr.core.filters import BufrFilter
from pdbufr.core.keys import BufrKey
from pdbufr.core.keys import datetime_from_bufr
from pdbufr.core.keys import wigos_id_from_bufr
from pdbufr.core.keys import wmo_station_id_from_bufr
from pdbufr.core.structure import filter_keys
from pdbufr.core.structure import filter_keys_cached
from pdbufr.core.structure import message_structure
from pdbufr.readers.generic import extract_observations


def test_BufrKey() -> None:
    res = BufrKey.from_level_key(0, "edition")

    assert res.level == 0
    assert res.rank == 0
    assert res.name == "edition"
    assert res.key == "edition"

    res = BufrKey.from_level_key(0, "#1#temperature")

    assert res.level == 0
    assert res.rank == 1
    assert res.name == "temperature"
    assert res.key == "#1#temperature"


def test_message_structure() -> None:
    message: T.Mapping[str, T.Any] = {
        "edition": 1,
    }

    res = message_structure(message)

    assert list(res) == [(0, "edition")]

    message = {
        "edition": 1,
        "#1#year": 2020,
        "#1#subsetNumber": 1,
        "#1#latitude": 43.0,
        "#1#temperature": 300.0,
        "#2#latitude": 42.0,
        "#2#temperature": 310.0,
        "#2#subsetNumber": 2,
        "#3#temperature": 300.0,
        "#1#latitude->code": "005002",
        "#2#latitude->code": "005002",
    }
    expected = [
        (0, "edition"),
        (0, "#1#year"),
        (0, "#1#subsetNumber"),
        (1, "#1#latitude"),
        (2, "#1#temperature"),
        (1, "#2#latitude"),
        (2, "#2#temperature"),
        (0, "#2#subsetNumber"),
        (1, "#3#temperature"),
    ]

    res = message_structure(message)

    assert list(res)[:-2] == expected


def test_filter_keys() -> None:
    message = {
        "edition": 1,
        "#1#year": 2020,
        "#1#subsetNumber": 1,
        "#1#latitude": 43.0,
        "#1#temperature": 300.0,
        "#2#latitude": 42.0,
        "#2#temperature": 310.0,
        "#2#subsetNumber": 2,
        "#3#temperature": 300.0,
        "#1#latitude->code": "005002",
        "#2#latitude->code": "005002",
    }
    expected = [
        (0, "edition"),
        (0, "#1#year"),
        (0, "#1#subsetNumber"),
        (1, "#1#latitude"),
        (2, "#1#temperature"),
        (1, "#2#latitude"),
        (2, "#2#temperature"),
        (0, "#2#subsetNumber"),
        (1, "#3#temperature"),
    ]
    expected_obj = [BufrKey.from_level_key(*i) for i in expected]

    res = filter_keys(message)

    assert list(res)[:-2] == expected_obj

    res = filter_keys(message, include=("edition",))

    assert list(res) == [BufrKey.from_level_key(0, "edition")]


def test_filter_keys_cached() -> None:
    cache: T.Dict[T.Tuple[T.Hashable, ...], T.List[T.Any]] = {}
    message = {
        "edition": 3,
        "masterTableNumber": 0,
        "unexpandedDescriptors": [321212, 321213],
        "numberOfSubsets": 1,
    }
    expected = [
        (0, "edition"),
        (0, "masterTableNumber"),
        (0, "unexpandedDescriptors"),
        (0, "numberOfSubsets"),
    ]
    expected_obj = [BufrKey.from_level_key(*i) for i in expected]

    res1 = filter_keys_cached(message, cache)

    assert len(cache) == 1
    assert res1 == expected_obj

    res2 = filter_keys_cached(message, cache)

    assert len(cache) == 1
    assert res1 is res2

    res = filter_keys_cached(message, cache, include=("edition",))

    assert len(cache) == 2
    assert res == [BufrKey(0, 0, "edition")]

    message["unexpandedDescriptors"] = 321212

    res = filter_keys_cached(message, cache)

    assert len(cache) == 3
    assert res == expected_obj

    message["delayedDescriptorReplicationFactor"] = 1
    res = filter_keys_cached(message, cache)
    assert len(cache) == 4
    assert len(res) == 5

    message["delayedDescriptorReplicationFactor"] = (1, 2)
    res = filter_keys_cached(message, cache)
    assert len(cache) == 5
    assert len(res) == 5

    message["delayedDescriptorReplicationFactor"] = 1
    res = filter_keys_cached(message, cache)
    assert len(cache) == 5
    assert len(res) == 5

    message["shortDelayedDescriptorReplicationFactor"] = 1
    res = filter_keys_cached(message, cache)
    assert len(cache) == 6
    assert len(res) == 6

    message["shortDelayedDescriptorReplicationFactor"] = (1, 2)
    res = filter_keys_cached(message, cache)
    assert len(cache) == 7
    assert len(res) == 6

    message["shortDelayedDescriptorReplicationFactor"] = 1
    res = filter_keys_cached(message, cache)
    assert len(cache) == 7
    assert len(res) == 6

    message["extendedDelayedDescriptorReplicationFactor"] = 1
    res = filter_keys_cached(message, cache)
    assert len(cache) == 8
    assert len(res) == 7

    message["extendedDelayedDescriptorReplicationFactor"] = (1, 2)
    res = filter_keys_cached(message, cache)
    assert len(cache) == 9
    assert len(res) == 7

    message["extendedDelayedDescriptorReplicationFactor"] = 1
    res = filter_keys_cached(message, cache)
    assert len(cache) == 9
    assert len(res) == 7


def test_datetime_from_bufr() -> None:
    obs = {"Y": 2020, "M": 3, "D": 18}

    res = datetime_from_bufr(obs, "", ["Y", "M", "D", "h", "m", "s"])

    assert str(res) == "2020-03-18 00:00:00"


def test_wmo_station_id_from_bufr() -> None:
    res = wmo_station_id_from_bufr({"b": "01", "s": "20"}, "", ["b", "s"])

    assert res == 1020


def test_wigos_id_from_bufr() -> None:
    res = wigos_id_from_bufr({"s": 0, "ii": 705, "in": 0, "l": "1931"}, "", ["s", "ii", "in", "l"])

    assert res == "0-705-0-1931"


def test_extract_observations_simple() -> None:
    message = {
        "#1#pressure": 100,
        "#1#temperature": 300.0,
        "#2#pressure": eccodes.CODES_MISSING_LONG,
        "#2#temperature": eccodes.CODES_MISSING_DOUBLE,
        "#1#pressure->code": "005002",
        "#2#pressure->code": "005002",
    }
    filtered_keys = list(filter_keys(message))[:-2]
    expected = [
        {"pressure": 100, "temperature": 300.0},
        {"pressure": None, "temperature": None},
    ]

    res = extract_observations(message, filtered_keys)

    assert list(res) == expected

    filters = {"pressure": BufrFilter.from_user(slice(95, None))}

    res = extract_observations(message, filtered_keys, filters)

    assert list(res) == expected[:1]


def test_extract_observations_medium() -> None:
    message = {
        "#1#pressure": 100,
        "#1#temperature": 300.0,
        "#2#pressure": 90,
        "#2#temperature": eccodes.CODES_MISSING_DOUBLE,
        "#1#pressure->code": "005002",
        "#2#pressure->code": "005002",
    }
    filtered_keys = list(filter_keys(message))[:-2]
    filters = {"count": BufrFilter.from_user({1})}
    expected = [
        {"count": 1, "pressure": 100, "temperature": 300.0},
        {"count": 1, "pressure": 90, "temperature": None},
    ]

    res = extract_observations(message, filtered_keys, filters, {"count": 1})

    assert list(res) == expected

    filters = {"pressure": BufrFilter.from_user(slice(95, 100))}

    res = extract_observations(message, filtered_keys, filters, {"count": 1})

    assert list(res) == expected[:1]


def test_extract_observations_complex() -> None:
    message = {
        "#1#latitude": 42,
        "#1#pressure": 100,
        "#1#temperature": 300.0,
        "#2#pressure": 90,
        "#2#temperature": eccodes.CODES_MISSING_DOUBLE,
        "#2#latitude": 43,
        "#3#temperature": 290.0,
        "#1#latitude->code": "005002",
        "#1#pressure->code": "005002",
        "#2#latitude->code": "005002",
        "#2#pressure->code": "005002",
    }
    filtered_keys = list(filter_keys(message))[:-2]
    expected = [
        {"latitude": 42, "pressure": 100, "temperature": 300.0},
        {"latitude": 42, "pressure": 90, "temperature": None},
        {
            "latitude": 43,
            "temperature": 290.0,
            # these are an artifact of testing with dicts
            "latitude->code": "005002",
            "pressure->code": "005002",
        },
    ]

    res = extract_observations(message, filtered_keys, {})

    assert list(res) == expected

    filters = {"latitude": BufrFilter.from_user(slice(None))}
    expected = [
        {"latitude": 42, "pressure": 100, "temperature": 300.0},
        {"latitude": 42, "pressure": 90, "temperature": None},
        {
            "latitude": 43,
            "temperature": 290.0,
            # these are an artifact of testing with dicts
            "latitude->code": "005002",
            "pressure->code": "005002",
        },
    ]

    res = extract_observations(message, filtered_keys, filters)

    assert list(res) == expected


def test_extract_observations_subsets_simple() -> None:
    message = {
        "compressedData": 1,
        "numberOfSubsets": 2,
        "#1#pressure": np.array([100, 90]),
        "#1#temperature": np.array([300.0, eccodes.CODES_MISSING_DOUBLE]),
        "#1#pressure->code": "005002",
    }
    filtered_keys = list(filter_keys(message))[:-1]
    expected = [
        {
            "compressedData": 1,
            "numberOfSubsets": 2,
            "pressure": 100,
            "temperature": 300.0,
        },
        {
            "compressedData": 1,
            "numberOfSubsets": 2,
            "pressure": 90,
            "temperature": None,
        },
    ]

    res = extract_observations(message, filtered_keys)

    assert list(res) == expected

    filters = {"pressure": BufrFilter.from_user(slice(95, None))}

    res = extract_observations(message, filtered_keys, filters)

    assert list(res) == expected[:1]


def test_stream_bufr() -> None:
    messages = [
        {
            "edition": 3,
            "masterTableNumber": 0,
            "numberOfSubsets": 1,
            "unexpandedDescriptors": 0,
            "blockNumber": 1,
            "stationNumber": 128,
        },
        {
            "edition": 4,
            "masterTableNumber": 1,
            "numberOfSubsets": 1,
            "unexpandedDescriptors": 1,
            "stationNumber": 129,
        },
    ]
    columns = ["edition"]
    expected = [{"edition": 3}, {"edition": 4}]
    res = list(stream_bufr(messages, columns))

    assert len(res) == 2
    assert res == expected

    res = list(stream_bufr(messages, columns, required_columns=False))

    assert len(res) == 2
    assert res == expected

    res = list(
        stream_bufr(
            messages,
            ["blockNumber", "WMO_station_id"],
            required_columns=["blockNumber"],
        )
    )

    assert len(res) == 1

    with pytest.raises(TypeError):
        list(stream_bufr(messages, columns, required_columns=len))  # type: ignore

    res = list(stream_bufr(messages, columns, filters={"count": 1}))

    assert len(res) == 1
    assert res == expected[:1]

    res = list(stream_bufr(messages, columns, filters={"count": 2}))

    assert len(res) == 1
    assert res == expected[1:]

    res = list(stream_bufr(messages, columns, filters={"edition": 3}, prefilter_headers=True))

    assert len(res) == 1
    assert res == expected[:1]

    expected_2 = [{"WMO_station_id": 1128}]

    res = list(
        stream_bufr(
            messages,
            ["WMO_station_id"],
        )
    )

    assert len(res) == 1
    assert res == expected_2


def test_code_is_coord() -> None:
    """Ensures that the different ways of identifying a coordinate key from
    the BUFR descriptor/code agree"""

    from pdbufr.high_level_bufr.bufr import bufr_code_is_coord

    data = {
        "000300": True,
        "010000": False,
        "009999": True,
        "010999": False,
        "100000": False,
        "201001": False,
        "301001": False,
    }

    for k, v in data.items():
        assert bufr_code_is_coord(k) == v
        assert bufr_code_is_coord(int(k)) == v
