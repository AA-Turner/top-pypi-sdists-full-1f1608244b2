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

def test_cudaawkward_UnionArray_fillindex_to64_from32_1():
    toindex = cupy.array([123, 123, 123, 123, 123, 123], dtype=cupy.int64)
    toindexoffset = 3
    fromindex = cupy.array([1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1], dtype=cupy.int32)
    length = 3
    funcC = cupy_backend['awkward_UnionArray_fillindex', cupy.int64, cupy.int32]
    funcC(toindex, toindexoffset, fromindex, length)

    try:
        ak_cu.synchronize_cuda()
    except:
        pytest.fail("This test case shouldn't have raised an error")
    pytest_toindex = [123, 123, 123, 1, 0, 0]
    cpt.assert_allclose(toindex[:len(pytest_toindex)], cupy.array(pytest_toindex))

def test_cudaawkward_UnionArray_fillindex_to64_from32_2():
    toindex = cupy.array([123, 123, 123, 123, 123, 123], dtype=cupy.int64)
    toindexoffset = 3
    fromindex = cupy.array([1, 2, 2, 3, 0, 2, 0, 2, 1, 1], dtype=cupy.int32)
    length = 3
    funcC = cupy_backend['awkward_UnionArray_fillindex', cupy.int64, cupy.int32]
    funcC(toindex, toindexoffset, fromindex, length)

    try:
        ak_cu.synchronize_cuda()
    except:
        pytest.fail("This test case shouldn't have raised an error")
    pytest_toindex = [123, 123, 123, 1, 2, 2]
    cpt.assert_allclose(toindex[:len(pytest_toindex)], cupy.array(pytest_toindex))

def test_cudaawkward_UnionArray_fillindex_to64_from32_3():
    toindex = cupy.array([123, 123, 123, 123, 123, 123], dtype=cupy.int64)
    toindexoffset = 3
    fromindex = cupy.array([1, 3, 0, 3, 5, 2, 0, 2, 1, 1], dtype=cupy.int32)
    length = 3
    funcC = cupy_backend['awkward_UnionArray_fillindex', cupy.int64, cupy.int32]
    funcC(toindex, toindexoffset, fromindex, length)

    try:
        ak_cu.synchronize_cuda()
    except:
        pytest.fail("This test case shouldn't have raised an error")
    pytest_toindex = [123, 123, 123, 1, 3, 0]
    cpt.assert_allclose(toindex[:len(pytest_toindex)], cupy.array(pytest_toindex))

def test_cudaawkward_UnionArray_fillindex_to64_from32_4():
    toindex = cupy.array([123, 123, 123, 123, 123, 123], dtype=cupy.int64)
    toindexoffset = 3
    fromindex = cupy.array([1, 4, 2, 3, 1, 2, 3, 1, 4, 3, 2, 1, 3, 2, 4, 5, 1, 2, 3, 4, 5], dtype=cupy.int32)
    length = 3
    funcC = cupy_backend['awkward_UnionArray_fillindex', cupy.int64, cupy.int32]
    funcC(toindex, toindexoffset, fromindex, length)

    try:
        ak_cu.synchronize_cuda()
    except:
        pytest.fail("This test case shouldn't have raised an error")
    pytest_toindex = [123, 123, 123, 1, 4, 2]
    cpt.assert_allclose(toindex[:len(pytest_toindex)], cupy.array(pytest_toindex))

def test_cudaawkward_UnionArray_fillindex_to64_from32_5():
    toindex = cupy.array([123, 123, 123, 123, 123, 123], dtype=cupy.int64)
    toindexoffset = 3
    fromindex = cupy.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=cupy.int32)
    length = 3
    funcC = cupy_backend['awkward_UnionArray_fillindex', cupy.int64, cupy.int32]
    funcC(toindex, toindexoffset, fromindex, length)

    try:
        ak_cu.synchronize_cuda()
    except:
        pytest.fail("This test case shouldn't have raised an error")
    pytest_toindex = [123, 123, 123, 0, 0, 0]
    cpt.assert_allclose(toindex[:len(pytest_toindex)], cupy.array(pytest_toindex))

