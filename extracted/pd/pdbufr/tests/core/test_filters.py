# (C) Copyright 2019- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.

import typing as T

import numpy as np

from pdbufr.core.filters import BufrFilter
from pdbufr.core.filters import filters_match


def test_BufrFilter_value() -> None:
    assert BufrFilter.from_user(1).match(1) is True
    assert BufrFilter.from_user(1).match(True) is True
    assert BufrFilter.from_user(1).match(1.0) is True

    assert BufrFilter.from_user(1).match(False) is False
    assert BufrFilter.from_user(1).match(float("inf")) is False
    assert BufrFilter.from_user(1).match(None) is False

    assert BufrFilter.from_user(1).max() == 1


def test_BufrFilter_iterator() -> None:
    assert BufrFilter.from_user([1, 2]).match(1) is True
    assert BufrFilter.from_user((1, 2)).match(True) is True
    assert BufrFilter.from_user({1, 2}).match(1.0) is True

    assert BufrFilter.from_user([1, 2]).match(False) is False
    assert BufrFilter.from_user({1, 2}).match(float("inf")) is False

    assert BufrFilter.from_user({1, 2}).max() == 2


def test_BufrFilter_slice() -> None:
    assert BufrFilter.from_user(slice(1, None)).match(float("inf")) is True
    assert BufrFilter.from_user(slice(None, 1)).match(True) is True
    assert BufrFilter.from_user(slice(1.0, 2.1)).match(1.0) is True

    assert BufrFilter.from_user(slice(0.1, 1.1, 0.1)).match(1.0) is True

    assert BufrFilter.from_user(slice(1, None)).match(False) is False
    assert BufrFilter.from_user(slice(1000.0)).match(float("inf")) is False

    assert BufrFilter.from_user(slice(1, None)).max() is None
    assert BufrFilter.from_user(slice(None, 1)).max() == 1


def test_BufrFilter_range() -> None:
    assert BufrFilter.from_user(range(1, 3)).match(1) is True
    assert BufrFilter.from_user(range(1, 3)).match(True) is True
    assert BufrFilter.from_user(range(1, 3)).match(1.0) is True
    assert BufrFilter.from_user(range(1, 3)).match(2) is True

    assert BufrFilter.from_user(range(1, 3)).match(0) is False
    assert BufrFilter.from_user(range(1, 3)).match(1.5) is False
    assert BufrFilter.from_user(range(1, 3)).match(3) is False

    assert BufrFilter.from_user(np.arange(1, 3, 0.5)).match(1.5) is True


def test_BufrFilter_callable() -> None:
    assert BufrFilter.from_user(lambda x: x > 0).match(1) is True
    assert BufrFilter.from_user(lambda x: x > 0).match(True) is True
    assert BufrFilter.from_user(lambda x: x > 0).match(1.0) is True

    assert BufrFilter.from_user(lambda x: x > 0).match(0) is False
    assert BufrFilter.from_user(lambda x: x > 0).match(-1) is False

    assert BufrFilter.from_user(lambda x: x > 0).max() is None


def test_is_match() -> None:
    compile_filters = {
        "station": BufrFilter.from_user({234}),
        "level": BufrFilter.from_user(set(range(1, 12))),
        "height": BufrFilter.from_user(slice(1.5, 2.1)),
    }

    message: T.Dict[str, T.Any] = {"station": 233}
    assert filters_match(message, compile_filters) is False

    message = {"station": 234, "temperature": 300.0}
    assert filters_match(message, compile_filters) is False

    message.update({"level": 1, "height": 1.5})
    assert filters_match(message, compile_filters) is True
