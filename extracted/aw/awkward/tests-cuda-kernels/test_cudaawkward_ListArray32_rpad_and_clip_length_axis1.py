# AUTO GENERATED ON 2025-05-15 AT 21:20:36
# DO NOT EDIT BY HAND!
#
# To regenerate file, run
#
#     python dev/generate-tests.py
#

# fmt: off

import cupy
import cupy.testing as cpt
import numpy as np
import pytest

import awkward as ak
import awkward._connect.cuda as ak_cu
from awkward._backends.cupy import CupyBackend

cupy_backend = CupyBackend.instance()

def test_cudaawkward_ListArray32_rpad_and_clip_length_axis1_1():
    tomin = cupy.array([123], dtype=cupy.int64)
    fromstarts = cupy.array([2, 0, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1], dtype=cupy.int32)
    fromstops = cupy.array([3, 2, 4, 5, 3, 4, 2, 5, 3, 4, 6, 11], dtype=cupy.int32)
    target = 3
    lenstarts = 3
    funcC = cupy_backend['awkward_ListArray_rpad_and_clip_length_axis1', cupy.int64, cupy.int32, cupy.int32]
    funcC(tomin, fromstarts, fromstops, target, lenstarts)

    try:
        ak_cu.synchronize_cuda()
    except:
        pytest.fail("This test case shouldn't have raised an error")
    pytest_tomin = [9]
    cpt.assert_allclose(tomin[:len(pytest_tomin)], cupy.array(pytest_tomin))

def test_cudaawkward_ListArray32_rpad_and_clip_length_axis1_2():
    tomin = cupy.array([123], dtype=cupy.int64)
    fromstarts = cupy.array([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1], dtype=cupy.int32)
    fromstops = cupy.array([8, 4, 5, 6, 5, 5, 7], dtype=cupy.int32)
    target = 3
    lenstarts = 3
    funcC = cupy_backend['awkward_ListArray_rpad_and_clip_length_axis1', cupy.int64, cupy.int32, cupy.int32]
    funcC(tomin, fromstarts, fromstops, target, lenstarts)

    try:
        ak_cu.synchronize_cuda()
    except:
        pytest.fail("This test case shouldn't have raised an error")
    pytest_tomin = [16]
    cpt.assert_allclose(tomin[:len(pytest_tomin)], cupy.array(pytest_tomin))

def test_cudaawkward_ListArray32_rpad_and_clip_length_axis1_3():
    tomin = cupy.array([123], dtype=cupy.int64)
    fromstarts = cupy.array([1, 4, 5, 6, 5, 5, 7, 1, 2, 1, 3, 1, 5, 3, 2], dtype=cupy.int32)
    fromstops = cupy.array([1, 4, 5, 6, 5, 5, 7, 1, 2, 1, 3, 1, 5, 3, 2], dtype=cupy.int32)
    target = 3
    lenstarts = 3
    funcC = cupy_backend['awkward_ListArray_rpad_and_clip_length_axis1', cupy.int64, cupy.int32, cupy.int32]
    funcC(tomin, fromstarts, fromstops, target, lenstarts)

    try:
        ak_cu.synchronize_cuda()
    except:
        pytest.fail("This test case shouldn't have raised an error")
    pytest_tomin = [9]
    cpt.assert_allclose(tomin[:len(pytest_tomin)], cupy.array(pytest_tomin))

def test_cudaawkward_ListArray32_rpad_and_clip_length_axis1_4():
    tomin = cupy.array([123], dtype=cupy.int64)
    fromstarts = cupy.array([1, 7, 6, 1, 3, 4, 2, 5, 2, 3, 1, 2, 3, 4, 5, 6, 7, 1, 2], dtype=cupy.int32)
    fromstops = cupy.array([1, 9, 6, 2, 4, 5, 3, 6, 3, 4, 2, 4, 5, 5, 7, 8, 2, 3], dtype=cupy.int32)
    target = 3
    lenstarts = 3
    funcC = cupy_backend['awkward_ListArray_rpad_and_clip_length_axis1', cupy.int64, cupy.int32, cupy.int32]
    funcC(tomin, fromstarts, fromstops, target, lenstarts)

    try:
        ak_cu.synchronize_cuda()
    except:
        pytest.fail("This test case shouldn't have raised an error")
    pytest_tomin = [9]
    cpt.assert_allclose(tomin[:len(pytest_tomin)], cupy.array(pytest_tomin))

def test_cudaawkward_ListArray32_rpad_and_clip_length_axis1_5():
    tomin = cupy.array([123], dtype=cupy.int64)
    fromstarts = cupy.array([0, 0, 0, 0, 0, 0, 0, 0], dtype=cupy.int32)
    fromstops = cupy.array([1, 1, 1, 1, 1, 1, 1, 1], dtype=cupy.int32)
    target = 3
    lenstarts = 3
    funcC = cupy_backend['awkward_ListArray_rpad_and_clip_length_axis1', cupy.int64, cupy.int32, cupy.int32]
    funcC(tomin, fromstarts, fromstops, target, lenstarts)

    try:
        ak_cu.synchronize_cuda()
    except:
        pytest.fail("This test case shouldn't have raised an error")
    pytest_tomin = [9]
    cpt.assert_allclose(tomin[:len(pytest_tomin)], cupy.array(pytest_tomin))

