# AUTO GENERATED ON 2025-05-15 AT 21:20:36
# DO NOT EDIT BY HAND!
#
# To regenerate file, run
#
#     python dev/generate-tests.py
#

# fmt: off

import ctypes
import numpy as np
import pytest

from awkward_cpp.cpu_kernels import lib

def test_unit_cpuawkward_IndexedArrayU32_reduce_next_nonlocal_nextshifts_64_1():
    nextshifts = []
    nextshifts = (ctypes.c_int64*len(nextshifts))(*nextshifts)
    index = []
    index = (ctypes.c_uint32*len(index))(*index)
    length = 0
    funcC = getattr(lib, 'awkward_IndexedArrayU32_reduce_next_nonlocal_nextshifts_64')
    ret_pass = funcC(nextshifts, index, length)
    pytest_nextshifts = []
    assert nextshifts[:len(pytest_nextshifts)] == pytest.approx(pytest_nextshifts)
    assert not ret_pass.str

