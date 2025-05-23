#!/usr/bin/env python3

# (C) Copyright 2020 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import datetime

import pytest

from earthkit.data import from_source
from earthkit.data.decorators import normalize
from earthkit.data.testing import earthkit_examples_file


def f(d):
    return d


@pytest.mark.xfail
def test_normalize_dates_from_source():
    dates_3 = normalize("d", "date")(f)
    dates_list_3 = normalize("d", "date", multiple=True)(f)

    source = from_source("file", earthkit_examples_file("test.grib"))
    assert dates_3(source[0]) == datetime.datetime(2020, 5, 13, 12, 0)
    assert dates_list_3(source[0]) == [datetime.datetime(2020, 5, 13, 12, 0)]

    source = from_source("file", earthkit_examples_file("test.nc"))

    #  For now
    with pytest.raises(NotImplementedError):
        assert dates_3(source[0]) == datetime.datetime(2020, 5, 13, 12, 0)
        assert dates_list_3(source[0]) == [datetime.datetime(2020, 5, 13, 12, 0)]


def test_normalize_dates_formatted_1():
    date_formatted = normalize("d", "date", format="%Y.%m.%d")(f)

    assert date_formatted("20200513") == "2020.05.13"


@pytest.mark.skip(reason="Not implemented yet.")
def test_normalize_enum_dates_formatted():
    date_formatted = normalize("d", values=["20010512", "20020512"], type="date", format="%Y.%m.%d")(f)

    assert date_formatted("20200513") == "2020.05.13"


def test_normalize_dates_formatted():
    date_formatted = normalize("d", "date-list(%Y.%m.%d)")(f)

    assert date_formatted(["20200513", "20200514"]) == ["2020.05.13", "2020.05.14"]
    assert date_formatted("20200513") == ["2020.05.13"]
    assert date_formatted([datetime.datetime(2020, 5, 13, 0, 0)]) == ["2020.05.13"]
    assert date_formatted([datetime.datetime(2020, 5, 13, 23, 59)]) == ["2020.05.13"]


def test_normalize_dates_multiple():
    date_1 = normalize("d", "date-list(%Y.%m.%d)")(f)
    date_2 = normalize("d", "date(%Y.%m.%d)", multiple=True)(f)
    date_3 = normalize("d", "date(%Y.%m.%d)", multiple=False)(f)
    date_4 = normalize("d", "date-list(%Y.%m.%d)", multiple=False)(f)

    assert date_1("20200511") == ["2020.05.11"]
    assert date_2("20200512") == ["2020.05.12"]
    assert date_3("20200513") == "2020.05.13"

    with pytest.raises(ValueError):
        date_4("20200514")


@pytest.mark.parametrize(
    "date,expected",
    [
        (
            "20200511/20200512",
            [
                "2020.05.11",
                "2020.05.12",
            ],
        ),
        (
            "20200511/20200514",
            [
                "2020.05.11",
                "2020.05.14",
            ],
        ),
        (
            "20200511/TO/20200512",
            [
                "2020.05.11",
                "2020.05.12",
            ],
        ),
        (
            "20200511/to/20200512",
            [
                "2020.05.11",
                "2020.05.12",
            ],
        ),
        (
            "20200511/TO/20200513/BY/2",
            [
                "2020.05.11",
                "2020.05.13",
            ],
        ),
        (
            "20200511/to/20200513/by/2",
            [
                "2020.05.11",
                "2020.05.13",
            ],
        ),
        (
            ["20200511", "20200513"],
            [
                "2020.05.11",
                "2020.05.13",
            ],
        ),
        (
            ["2020-05-11", "2020-05-13"],
            [
                "2020.05.11",
                "2020.05.13",
            ],
        ),
        (
            "20200511/to/20200513",
            [
                "2020.05.11",
                "2020.05.12",
                "2020.05.13",
            ],
        ),
        (
            ["20200511", "20200512", "20200513"],
            [
                "2020.05.11",
                "2020.05.12",
                "2020.05.13",
            ],
        ),
        (
            "20200511/to/20200515",
            [
                "2020.05.11",
                "2020.05.12",
                "2020.05.13",
                "2020.05.14",
                "2020.05.15",
            ],
        ),
        (
            ["20200511", "20200512", "20200513", "20200514", "20200515"],
            [
                "2020.05.11",
                "2020.05.12",
                "2020.05.13",
                "2020.05.14",
                "2020.05.15",
            ],
        ),
    ],
)
def test_normalize_date_list(date, expected):
    n = normalize("d", "date-list(%Y.%m.%d)")(f)
    assert n(date) == expected


@pytest.mark.xfail
def test_normalize_dates_formatted_from_pandas():
    import pandas as pd

    df1 = pd.DataFrame(
        [
            datetime.datetime(2005, 8, 27, 18, 0),
        ],
        columns=["date"],
    )
    df2 = pd.DataFrame(
        [
            datetime.datetime(2005, 8, 26, 18, 0),
            datetime.datetime(2005, 8, 27, 18, 0),
        ],
        columns=["date"],
    )

    @normalize("date", "date-list(%Y-%m-%d)")
    def f(date):
        return date

    print(f(df1))
    print(f(df2))

    @normalize("date", "date(%Y-%m-%d)")
    def f(date):
        return date

    print(f(df1))
    with pytest.raises(AssertionError):
        print(f(df2))


@pytest.mark.skip("Not implemented (yet?).")
def test_normalize_dates_formatted_from_object():
    date_formatted = normalize("d", "date", format="%Y.%m.%d")(f)

    class CustomDateObject:
        def __init__(self, dates):
            self.dates = dates

        def to_datetime_list(self):
            return self.dates

    obj = CustomDateObject(
        [
            datetime.datetime(2005, 8, 26, 18, 0),
            datetime.datetime(2005, 8, 26, 18, 0),
        ]
    )

    assert date_formatted(obj) == "2020.05.13"


def test_normalize_date_none_1():
    @normalize(
        "name",
        "date(%Y%m%d)",
    )
    def date_default_none(name=None):
        return name

    assert date_default_none("2012-12-02") == "20121202"
    assert date_default_none() is None


def test_normalize_date_list_none_1():
    @normalize(
        "name",
        "date-list(%Y%m%d)",
    )
    def date_default_none(name=None):
        return name

    assert date_default_none("2012-12-02") == ["20121202"]
    assert date_default_none() is None


def test_normalize_date_default_1():
    @normalize(
        "name",
        "date",
    )
    def date_default_1(name="wrong-default"):
        return name

    date_default_1("2012-12-02")
    with pytest.raises(ValueError, match=".*wrong-default.*"):
        date_default_1()


if __name__ == "__main__":
    from earthkit.data.testing import main

    main(__file__)
