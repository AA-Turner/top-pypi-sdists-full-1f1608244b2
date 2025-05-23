from copy import copy, deepcopy

import numpy as np
from hdmf.data_utils import DataIO
from hdmf.testing import TestCase


class DataIOTests(TestCase):

    def test_copy(self):
        obj = DataIO(data=[1., 2., 3.])
        obj_copy = copy(obj)
        self.assertNotEqual(id(obj), id(obj_copy))
        self.assertEqual(id(obj.data), id(obj_copy.data))

    def test_deepcopy(self):
        obj = DataIO(data=[1., 2., 3.])
        obj_copy = deepcopy(obj)
        self.assertNotEqual(id(obj), id(obj_copy))
        self.assertNotEqual(id(obj.data), id(obj_copy.data))

    def test_dataio_slice_delegation(self):
        indata = np.arange(30)
        dset = DataIO(indata)
        self.assertTrue(np.all(dset[2:15] == indata[2:15]))

        indata = np.arange(50).reshape(5, 10)
        dset = DataIO(indata)
        self.assertTrue(np.all(dset[1:3, 5:8] == indata[1:3, 5:8]))

    def test_set_data_io_data_already_set(self):
        """
        Test that Data.set_dataio works as intended
        """
        dataio = DataIO(data=np.arange(30).reshape(5, 2, 3))
        with self.assertRaisesWith(ValueError, "cannot overwrite 'data' on DataIO"):
            dataio.data=[1,2,3,4]

    def test_dataio_options(self):
        """
        Test that either data or dtype+shape are specified exclusively
        """
        with self.assertWarnsRegex(UserWarning, "Argument 'dtype' is ignored when 'data' is specified"):
            DataIO(data=np.arange(5), dtype=int)
        with self.assertWarnsRegex(UserWarning, "Argument 'shape' is ignored when 'data' is specified"):
            DataIO(data=np.arange(5), shape=(3,))

        dataio = DataIO(shape=(3,), dtype=int)
        with self.assertRaisesRegex(ValueError, "Setting data when dtype and shape are not None is not supported"):
            dataio.data = np.arange(5)
