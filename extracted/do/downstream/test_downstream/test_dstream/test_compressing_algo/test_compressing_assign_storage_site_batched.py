import functools
import itertools as it
from random import randrange as rand
import typing

import numpy as np
import pytest

from downstream.dstream import compressing_algo as algo

_dtypes = [
    np.uint8,
    np.uint16,
    np.uint32,
    np.uint64,
    np.int8,
    np.int16,
    np.int32,
    np.int64,
]


def validate_compressing_site_selection(
    fn: typing.Callable,
) -> typing.Callable:
    """Decorator to validate pre- and post-conditions on site selection."""

    @functools.wraps(fn)
    def wrapper(S: int, T: int) -> typing.Optional[int]:
        assert np.array(np.bitwise_count(S) == 1).all()  # S is a power of two
        assert np.asarray(0 <= T).all()  # T is non-negative
        res = fn(S, T)
        assert (np.clip(res, 0, S) == res).all()  # Assert valid output
        return res

    return wrapper


site_selection = validate_compressing_site_selection(
    algo.assign_storage_site_batched,
)


def test_compressing_site_selection_batched8_scalar():
    # fmt: off
    actual = (site_selection(8, T) for T in it.count())
    expected = [
        0, 1, 2, 3, 4, 5, 6, 7,  # T 0-7
        8, 2, 8, 4, 8, 6, 8, 8,  # T 8-15
        8, 3, 8, 8, 8, 7, 8, 8,  # T 16-23
        8, 4, 8, 8, 8, 8, 8, 8,  # T 24-31
        8, 5, 8, 8, 8, 8, 8, 8, # T 32-39
        8, 6, 8, 8, 8, 8, 8, 8, # T 40-47
    ]
    assert all(x.tolist() == [y] for x, y in zip(actual, expected))


def test_compressing_site_selection_batched16_scalar():
    # fmt: off
    actual = (site_selection(16, T) for T in it.count())
    expected = [
        0, 1, 2, 3, 4, 5, 6, 7,  # T 0-7
        8, 9, 10, 11, 12, 13, 14, 15,  # T 8-15
        16, 2, 16, 4, 16, 6, 16, 8,  # T 16-23
        16, 10, 16, 12, 16, 14, 16, 16,  # T 24-31
    ]
    assert all(x.tolist() == [y] for x, y in zip(actual, expected))


def test_compressing_site_selection_batched8():
    # fmt: off
    T = np.arange(48)

    actual = site_selection(8, T)
    expected = [
        0, 1, 2, 3, 4, 5, 6, 7,  # T 0-7
        8, 2, 8, 4, 8, 6, 8, 8,  # T 8-15
        8, 3, 8, 8, 8, 7, 8, 8,  # T 16-23
        8, 4, 8, 8, 8, 8, 8, 8,  # T 24-31
        8, 5, 8, 8, 8, 8, 8, 8, # T 32-39
        8, 6, 8, 8, 8, 8, 8, 8, # T 40-47
    ]
    assert all(x == y for x, y in zip(actual, expected))


def test_compressing_site_selection_batched16():
    # fmt: off
    T = np.arange(32)

    actual = site_selection(16, T)
    expected = [
        0, 1, 2, 3, 4, 5, 6, 7,  # T 0-7
        8, 9, 10, 11, 12, 13, 14, 15,  # T 8-15
        16, 2, 16, 4, 16, 6, 16, 8,  # T 16-23
        16, 10, 16, 12, 16, 14, 16, 16,  # T 24-31
    ]
    assert all(x == y for x, y in zip(actual, expected))


def test_compressing_site_selection_batched_dualS():
    # fmt: off
    T = np.array([*range(48), *range(32)])
    S = np.array([8] * 48 + [16] * 32)

    actual = site_selection(S, T)
    expected = [
        0, 1, 2, 3, 4, 5, 6, 7,  # T 0-7
        8, 2, 8, 4, 8, 6, 8, 8,  # T 8-15
        8, 3, 8, 8, 8, 7, 8, 8,  # T 16-23
        8, 4, 8, 8, 8, 8, 8, 8,  # T 24-31
        8, 5, 8, 8, 8, 8, 8, 8, # T 32-39
        8, 6, 8, 8, 8, 8, 8, 8, # T 40-47
    ] + [
        0, 1, 2, 3, 4, 5, 6, 7,  # T 0-7
        8, 9, 10, 11, 12, 13, 14, 15,  # T 8-15
        16, 2, 16, 4, 16, 6, 16, 8,  # T 16-23
        16, 10, 16, 12, 16, 14, 16, 16,  # T 24-31
    ]
    assert all(x == y for x, y in zip(actual, expected))


@pytest.mark.parametrize("dtype1", _dtypes)
@pytest.mark.parametrize("dtype2", _dtypes)
def test_compressing_site_selection_batched_fuzz(
    dtype1: typing.Type,
    dtype2: typing.Type,
):
    Smax = min(np.iinfo(dtype1).max, 2**52)
    testS = np.array(
        [2**s for s in range(1, 64) if 2**s <= Smax],
        dtype=dtype1,
    )
    Tmax = min(np.iinfo(dtype2).max, 2**52)
    testT = np.fromiter(
        it.chain(
            range(min(10**5, Tmax + 1)),
            (rand(Tmax) for _ in range(10**5)),
        ),
        dtype=dtype2,
    )

    batchS, batchT = map(np.array, zip(*it.product(testS, testT)))
    assert (np.bitwise_count(batchS) == 1).all()
    site_selection(batchS, batchT)


@pytest.mark.parametrize("S", [1 << s for s in range(1, 21)])
def test_compressing_site_selection_epoch0(S: int):
    actual = set(site_selection(S, np.arange(S)))
    expected = set(range(S))
    assert actual == expected
