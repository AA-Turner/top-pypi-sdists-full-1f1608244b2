# -*- coding: utf-8 -*-
import ctypes as C  # NOQA
import io
import multiprocessing
import os
import platform
import random
import re
import signal
import sys
import warnings
from unittest import mock

import numpy as np

from obspy import Stream, Trace, UTCDateTime, read
from obspy.core.compatibility import from_buffer
from obspy.core.util import NamedTemporaryFile
from obspy.core.util.attribdict import AttribDict
from obspy.core.util.base import CatchAndAssertWarnings
from obspy.io.mseed import (InternalMSEEDError, InternalMSEEDWarning,
                            ObsPyMSEEDFilesizeTooSmallError,
                            ObsPyMSEEDFilesizeTooLargeError)
from obspy.io.mseed import util
from obspy.io.mseed.core import _read_mseed, _write_mseed
from obspy.io.mseed.headers import clibmseed
from obspy.io.mseed.msstruct import _MSStruct
import pytest


# some Python version don't support negative timestamps
NO_NEGATIVE_TIMESTAMPS = False
try:
    UTCDateTime(-50000)
except Exception:
    NO_NEGATIVE_TIMESTAMPS = True


def _test_function(filename):
    """
    Internal function used by MSEEDSpecialIssueTestCase.test_infinite_loop
    """
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        try:
            st = read(filename)  # noqa @UnusedVariable
        except (ValueError, InternalMSEEDError):
            # Should occur with broken files
            pass


class TestMSEEDSpecialIssue():
    """
    """
    @classmethod
    def setup_class(cls):
        # mseed steim compression is big endian
        if sys.byteorder == 'little':
            cls.swap = 1
        else:
            cls.swap = 0

    def test_invalid_record_length(self):
        """
        An invalid record length should raise an exception.
        """
        npts = 6000
        np.random.seed(815)  # make test reproducible
        with NamedTemporaryFile() as tf:
            tempfile = tf.name
            data = np.random.randint(-1000, 1000, npts).astype(np.int32)
            st = Stream([Trace(data=data)])
            # Writing should fail with invalid record lengths.
            # Not a power of 2.
            with pytest.raises(ValueError):
                _write_mseed(st, tempfile, format="MSEED", reclen=1000)
            # Too small.
            with pytest.raises(ValueError):
                _write_mseed(st, tempfile, format="MSEED", reclen=8)
            # Not a number.
            with pytest.raises(ValueError):
                _write_mseed(st, tempfile, format="MSEED", reclen='A')

    def test_invalid_encoding(self):
        """
        An invalid encoding should raise an exception.
        """
        npts = 6000
        np.random.seed(815)  # make test reproducible
        with NamedTemporaryFile() as tf:
            tempfile = tf.name
            data = np.random.randint(-1000, 1000, npts).astype(np.int32)
            st = Stream([Trace(data=data)])
            # Writing should fail with invalid record lengths.
            # Wrong number.
            with pytest.raises(ValueError):
                _write_mseed(st, tempfile, format="MSEED", encoding=2)
            # Wrong Text.
            with pytest.raises(ValueError):
                _write_mseed(st, tempfile, format="MSEED", encoding='FLOAT_64')

    def test_ctypes_arg_types(self):
        """
        Test that ctypes argtypes are set for type checking
        """
        argument_error = C.ArgumentError
        cl = clibmseed
        args = [C.pointer(C.pointer(C.c_int())), 'a', 1, 1.5, 1, 0, 0, 0, 0]
        with pytest.raises(argument_error):
            cl.ms_readtraces(*args)
        with pytest.raises(TypeError):
            cl.ms_readtraces(*args[:-1])
        with pytest.raises(argument_error):
            cl.ms_readmsr_r(*args)
        with pytest.raises(TypeError):
            cl.ms_readmsr_r(*args[:-1])
        with pytest.raises(argument_error):
            cl.mst_printtracelist(*args[:5])
        with pytest.raises(argument_error):
            cl.ms_detect(*args[:4])
        args.append(1)  # 10 argument function
        with pytest.raises(argument_error):
            cl.mst_packgroup(*args)
        args = ['hallo']  # one argument functions
        with pytest.raises(argument_error):
            cl.msr_starttime(*args)
        with pytest.raises(argument_error):
            cl.msr_endtime(*args)
        with pytest.raises(argument_error):
            cl.mst_init(*args)
        with pytest.raises(argument_error):
            cl.mst_free(*args)
        with pytest.raises(argument_error):
            cl.mst_initgroup(*args)
        with pytest.raises(argument_error):
            cl.mst_freegroup(*args)
        with pytest.raises(argument_error):
            cl.msr_init(*args)

    def test_broken_last_record(self, testdata):
        """
        Test if Libmseed is able to read files with broken last record. Use
        both methods, readMSTracesViaRecords and readMSTraces
        """
        file = testdata['brokenlastrecord.mseed']

        # independent reading of the data, 128 Bytes header
        d = np.fromfile(file, dtype=np.uint8)[128:]
        data = util._unpack_steim_2(d, 5980, swapflag=self.swap,
                                    verbose=0)

        # test readMSTraces. Will raise an internal warning.
        with CatchAndAssertWarnings() as w:
            data_record = _read_mseed(file)[0].data

        # This will raise 18 (!) warnings. It will skip 17 * 128 bytes due
        # to it not being a SEED records and then complain that the remaining
        # 30 bytes are not enough to constitute a full SEED record.
        assert len(w) == 18
        assert w[0].category == InternalMSEEDWarning

        # Test against reference data.
        assert len(data_record) == 5980
        last10samples = [2862, 2856, 2844, 2843, 2851,
                         2853, 2853, 2854, 2857, 2863]
        np.testing.assert_array_equal(data_record[-10:], last10samples)

        # Also test against independently unpacked data.
        np.testing.assert_allclose(data_record, data)

    def test_one_sample_overlap(self):
        """
        Both methods readMSTraces and readMSTracesViaRecords should recognize a
        single sample overlap.
        """
        # create a stream with one sample overlapping
        trace1 = Trace(data=np.zeros(1000))
        trace2 = Trace(data=np.zeros(10))
        trace2.stats.starttime = UTCDateTime(999)
        st = Stream([trace1, trace2])
        # write into MSEED
        with NamedTemporaryFile() as tf:
            tempfile = tf.name
            _write_mseed(st, tempfile, format="MSEED")
            # read it again
            new_stream = _read_mseed(tempfile)
            assert len(new_stream) == 2

    def test_bug_write_read_float32_seed_win32(self):
        """
        Test case for issue #64.
        """
        # create stream object
        data = np.array([395.07809448, 395.0782, 1060.28112793, -1157.37487793,
                         -1236.56237793, 355.07028198, -1181.42175293],
                        dtype=np.float32)
        st = Stream([Trace(data=data)])
        with NamedTemporaryFile() as tf:
            tempfile = tf.name
            _write_mseed(st, tempfile, format="MSEED")
            # read temp file directly without libmseed
            with open(tempfile, 'rb') as fp:
                fp.seek(56)
                dtype = np.dtype('>f4')
                bin_data = from_buffer(fp.read(7 * dtype.itemsize),
                                       dtype=dtype)
            np.testing.assert_array_equal(data, bin_data)
            # read via ObsPy
            st2 = _read_mseed(tempfile)
        # test results
        np.testing.assert_array_equal(data, st2[0].data)

    @pytest.mark.skipif(
        NO_NEGATIVE_TIMESTAMPS,
        reason='times before 1970 are not supported on this operation system')
    def test_write_with_date_time_before_1970(self):
        """
        Write an stream via libmseed with a datetime before 1970.

        This test depends on the platform specific localtime()/gmtime()
        function.
        """
        # create trace
        tr = Trace(data=np.empty(1000))
        tr.stats.starttime = UTCDateTime("1969-01-01T00:00:00")
        # write file
        with NamedTemporaryFile() as tf:
            tempfile = tf.name
            _write_mseed(Stream([tr]), tempfile, format="MSEED")
            # read again
            stream = _read_mseed(tempfile)
            stream.verify()

    def test_invalid_data_type(self):
        """
        Writing data of type int64 and int8 are not supported.

        int64 data can now be written since #2356 if it can be downcast to
        int32.
        """
        npts = 6000
        np.random.seed(815)  # make test reproducible
        with NamedTemporaryFile() as tf:
            tempfile = tf.name
            # int64
            data = np.random.randint(-1000, 1000, npts).astype(np.int64)
            # add a data point that can not be downcast (even though we have a
            # separate test for this)
            data[4] = np.iinfo(np.int32).max + 2
            st = Stream([Trace(data=data)])
            with pytest.raises(Exception):
                st.write(tempfile, format="MSEED")
            # int8
            data = np.random.randint(-1000, 1000, npts).astype(np.int8)
            st = Stream([Trace(data=data)])
            with pytest.raises(Exception):
                st.write(tempfile, format="MSEED")

    def test_write_wrong_encoding(self, testdata):
        """
        Test to write a floating point mseed file with encoding STEIM1.
        An exception should be raised.
        """
        file = testdata['BW.BGLD.__.EHE.D.2008.001.first_record']
        with NamedTemporaryFile() as tf:
            tempfile = tf.name
            # Read the data and convert them to float
            st = read(file)
            st[0].data = st[0].data.astype(np.float32) + .5
            # Type is not consistent float32 cannot be compressed with STEIM1,
            # therefore a exception should be raised.
            with pytest.raises(Exception):
                st.write(tempfile, format="MSEED", encoding=10)

    def test_write_wrong_encoding_via_mseed_stats(self, testdata):
        """
        Test to write a floating point mseed file with encoding STEIM1 with the
        encoding set in stats.mseed.encoding.
        This will just raise a warning.
        """
        file = testdata['BW.BGLD.__.EHE.D.2008.001.first_record']
        with NamedTemporaryFile() as tf:
            tempfile = tf.name
            # Read the data and convert them to float
            st = read(file)
            st[0].data = st[0].data.astype(np.float32) + .5
            # Type is not consistent float32 cannot be compressed with STEIM1,
            # therefore a warning should be raised.
            assert st[0].stats.mseed.encoding == 'STEIM1'
            with warnings.catch_warnings(record=True):
                warnings.simplefilter('error', UserWarning)
                with pytest.raises(UserWarning):
                    st.write(tempfile, format="MSEED")

    def test_wrong_record_length_as_argument(self, datapath):
        """
        Specifying a wrong record length should raise an error.
        """
        file = datapath / "encoding" / 'float32_Float32_bigEndian.mseed'
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            # invalid reclen
            read(file, reclen=111)
            assert 'Invalid record length' in str(w[0].message)
            assert w[0].category == UserWarning
            # wrong reclen - raises and also displays a warning
            with pytest.raises(Exception):
                read(file, reclen=4096)
            assert 'reclen exceeds buflen' in str(w[1].message)
            assert w[1].category == InternalMSEEDWarning

    def test_read_with_missing_blockette010(self, testdata):
        """
        Reading a Full/Mini-SEED w/o blockette 010 but blockette 008.
        """
        # 1 - Mini-SEED
        file = testdata['blockette008.mseed']
        tr = read(file)[0]
        assert 'BW.PART..EHZ' == tr.id
        assert 1642 == tr.stats.npts
        # 2 - full SEED
        file = testdata['RJOB.BW.EHZ.D.300806.0000.fullseed']
        tr = read(file)[0]
        assert 'BW.RJOB..EHZ' == tr.id
        assert 412 == tr.stats.npts

    def test_issue160(self, testdata):
        """
        Tests issue #160.

        Reading the header of SEED file.
        """
        file = testdata['BW.BGLD.__.EHE.D.2008.001.first_10_records']
        tr_one = read(file)[0]
        tr_two = read(file, headonly=True)[0]
        ms = AttribDict({'record_length': 512, 'encoding': 'STEIM1',
                         'filesize': 5120, 'dataquality': 'D',
                         'number_of_records': 10, 'byteorder': '>'})
        for tr in tr_one, tr_two:
            assert 'BW.BGLD..EHE' == tr.id
            assert ms == tr.stats.mseed
            assert 4120 == tr.stats.npts
            assert UTCDateTime(2008, 1, 1, 0, 0, 20, 510000) == \
                tr.stats.endtime

    def test_issue217(self, testdata):
        """
        Tests issue #217.

        Reading a MiniSEED file without sequence numbers and a record length of
        1024.
        """
        file = testdata['reclen_1024_without_sequence_numbers.mseed']
        tr = read(file)[0]
        ms = AttribDict({'record_length': 1024, 'encoding': 'STEIM1',
                         'filesize': 2048, 'dataquality': 'D',
                         'number_of_records': 2, 'byteorder': '>'})
        assert 'XX.STF1..HHN' == tr.id
        assert ms == tr.stats.mseed
        assert 932 == tr.stats.npts
        assert UTCDateTime(2007, 5, 31, 22, 45, 46, 720000) == tr.stats.endtime

    def test_issue296(self):
        """
        Tests issue #296.
        """
        with NamedTemporaryFile() as tf:
            tempfile = tf.name
            # 1 - transform to np.float64 values
            st = read()
            for tr in st:
                tr.data = tr.data.astype(np.float64)
            # write a single trace automatically detecting encoding
            st[0].write(tempfile, format="MSEED")
            # write a single trace automatically detecting encoding
            st.write(tempfile, format="MSEED")
            # write a single trace with encoding 5
            st[0].write(tempfile, format="MSEED", encoding=5)
            # write a single trace with encoding 5
            st.write(tempfile, format="MSEED", encoding=5)
            # 2 - transform to np.float32 values
            st = read()
            for tr in st:
                tr.data = tr.data.astype(np.float32)
            # write a single trace automatically detecting encoding
            st[0].write(tempfile, format="MSEED")
            # write a single trace automatically detecting encoding
            st.write(tempfile, format="MSEED")
            # write a single trace with encoding 4
            st[0].write(tempfile, format="MSEED", encoding=4)
            # write a single trace with encoding 4
            st.write(tempfile, format="MSEED", encoding=4)
            # 3 - transform to np.int32 values
            st = read()
            for tr in st:
                tr.data = tr.data.astype(np.int32)
            # write a single trace automatically detecting encoding
            st[0].write(tempfile, format="MSEED")
            # write a single trace automatically detecting encoding
            st.write(tempfile, format="MSEED")
            # write a single trace with encoding 3
            st[0].write(tempfile, format="MSEED", encoding=3)
            # write the whole stream with encoding 3
            st.write(tempfile, format="MSEED", encoding=3)
            # write a single trace with encoding 10
            st[0].write(tempfile, format="MSEED", encoding=10)
            # write the whole stream with encoding 10
            st.write(tempfile, format="MSEED", encoding=10)
            # write a single trace with encoding 11
            st[0].write(tempfile, format="MSEED", encoding=11)
            # write the whole stream with encoding 11
            st.write(tempfile, format="MSEED", encoding=11)
            # 4 - transform to np.int16 values
            st = read()
            for tr in st:
                tr.data = tr.data.astype(np.int16)
            # write a single trace automatically detecting encoding
            st[0].write(tempfile, format="MSEED")
            # write a single trace automatically detecting encoding
            st.write(tempfile, format="MSEED")
            # write a single trace with encoding 1
            st[0].write(tempfile, format="MSEED", encoding=1)
            # write the whole stream with encoding 1
            st.write(tempfile, format="MSEED", encoding=1)
            # 5 - transform to ASCII values
            st = read()
            for tr in st:
                tr.data = tr.data.astype('|S1')
            # write a single trace automatically detecting encoding
            st[0].write(tempfile, format="MSEED")
            # write a single trace automatically detecting encoding
            st.write(tempfile, format="MSEED")
            # write a single trace with encoding 0
            st[0].write(tempfile, format="MSEED", encoding=0)
            # write the whole stream with encoding 0
            st.write(tempfile, format="MSEED", encoding=0)

    def test_issue289(self, testdata):
        """
        Tests issue #289.

        Reading MiniSEED using start/end time outside of data should result in
        an empty Stream object.
        """
        # 1
        file = testdata['steim2.mseed']
        st = read(file, starttime=UTCDateTime() - 10, endtime=UTCDateTime())
        assert len(st) == 0
        # 2
        file = testdata['fullseed.mseed']
        st = read(file, starttime=UTCDateTime() - 10, endtime=UTCDateTime())
        assert len(st) == 0

    def test_issue312(self, testdata):
        """
        Tests issue #312

        The blkt_link struct was defined wrong.
        """
        filename = testdata['BW.BGLD.__.EHE.D.2008.001.first_10_records']
        # start and end time
        ms = _MSStruct(str(filename))
        ms.read(-1, 0, 1, 0)
        blkt_link = ms.msr.contents.blkts.contents
        # The first blockette usually begins after 48 bytes. In the test file
        # it does.
        assert blkt_link.blktoffset == 48
        # The first blockette is blockette 1000 in this file.
        assert blkt_link.blkt_type == 1000
        # Only one blockette.
        assert blkt_link.next_blkt == 0
        # Blockette data is 8 bytes - 4 bytes for the blockette header.
        assert blkt_link.blktdatalen == 4
        del ms

    def test_issue272(self, testdata):
        """
        Tests issue #272

        Option headonly should not read the actual waveform data.
        """
        filename = testdata['BW.BGLD.__.EHE.D.2008.001.first_10_records']
        # everything
        st = read(filename)
        assert st[0].stats.npts == 4120
        assert len(st[0].data) == 4120
        # headers only
        st = read(filename, headonly=True)
        assert st[0].stats.npts == 4120
        assert len(st[0].data) == 0

    def test_issue325(self, testdata):
        """
        Tests issue #325: Use selection with non default dataquality flag.
        """
        filename = testdata['dataquality-m.mseed']
        # 1 - read all
        st = read(filename)
        assert len(st) == 3
        t1 = st[0].stats.starttime
        t2 = st[0].stats.endtime
        # 2 - select full time window
        st2 = read(filename, starttime=t1, endtime=t2)
        assert len(st2) == 3
        for tr in st2:
            del tr.stats.processing
        assert st == st2
        # 3 - use selection
        st2 = read(filename, starttime=t1, endtime=t2, sourcename='*.*.*.*')
        assert len(st2) == 3
        for tr in st2:
            del tr.stats.processing
        assert st == st2
        st2 = read(filename, starttime=t1, endtime=t2, sourcename='*')
        assert len(st2) == 3
        for tr in st2:
            del tr.stats.processing
        assert st == st2
        # 4 - selection without times
        st2 = read(filename, sourcename='*.*.*.*')
        assert len(st2) == 3
        assert st == st2
        st2 = read(filename, sourcename='*')
        assert len(st2) == 3
        assert st == st2

    def test_issue332(self):
        """
        Tests issue #332

        Writing traces with wrong encoding in stats should raise only a user
        warning.
        """
        with NamedTemporaryFile() as tf:
            tempfile = tf.name
            st = read()
            tr = st[0]
            tr.data = tr.data.astype(np.float64) + .5
            tr.stats.mseed = {'encoding': 0}
            with warnings.catch_warnings(record=True):
                warnings.simplefilter('error', UserWarning)
                with pytest.raises(UserWarning):
                    st.write(tempfile, format="MSEED")

    def test_issue341(self):
        """
        Tests issue #341

        Read/write of MiniSEED files with huge sampling rates/delta values.
        """
        with NamedTemporaryFile() as tf:
            tempfile = tf.name
            # 1 - sampling rate
            st = read()
            tr = st[0]
            tr.stats.sampling_rate = 1000000000.0
            tr.write(tempfile, format="MSEED")
            # read again
            st = read(tempfile)
            assert st[0].stats.sampling_rate == 1000000000.0
            # 2 - delta
            st = read()
            tr = st[0]
            tr.stats.delta = 10000000.0
            tr.write(tempfile, format="MSEED")
            # read again
            st = read(tempfile)
            assert round(abs(st[0].stats.delta-10000000.0), 0) == 0

    def test_issue485(self, datapath):
        """
        Test reading floats and doubles, which are bytswapped nans
        """
        ref = [-1188.07800293, 638.16400146, 395.07809448, 1060.28112793]
        for filename in ('nan_float32.mseed', 'nan_float64.mseed'):
            filename = datapath / 'encoding' / filename
            data = read(filename)[0].data.tolist()
            np.testing.assert_array_almost_equal(
                data, ref, decimal=8, err_msg='Data of file %s not equal' %
                filename)

    def test_enforcing_reading_byteorder(self):
        """
        Tests if setting the byte order of the header for reading is passed to
        the C functions.

        Quite simple. It just checks if reading with the correct byte order
        works and reading with the wrong byte order fails.
        """
        tr = Trace(data=np.arange(10, dtype=np.int32))

        # Test with little endian.
        memfile = io.BytesIO()
        tr.write(memfile, format="mseed", byteorder="<")
        memfile.seek(0, 0)
        # Reading little endian should work just fine.
        tr2 = read(memfile, header_byteorder="<")[0]
        memfile.seek(0, 0)
        assert tr2.stats.mseed.byteorder == "<"
        # Remove the mseed specific header fields. These are obviously not
        # equal.
        del tr2.stats.mseed
        del tr2.stats._format
        assert tr == tr2
        # Wrong byte order raises.
        with pytest.raises(ValueError):
            read(memfile, header_byteorder=">")

        # Same test with big endian
        memfile = io.BytesIO()
        tr.write(memfile, format="mseed", byteorder=">")
        memfile.seek(0, 0)
        # Reading big endian should work just fine.
        tr2 = read(memfile, header_byteorder=">")[0]
        memfile.seek(0, 0)
        assert tr2.stats.mseed.byteorder == ">"
        # Remove the mseed specific header fields. These are obviously not
        # equal.
        del tr2.stats.mseed
        del tr2.stats._format
        assert tr == tr2
        # Wrong byte order raises.
        with pytest.raises(ValueError):
            read(memfile, header_byteorder="<")

    def test_long_year_range(self):
        """
        Tests reading and writing years 1900 to 2100.
        """
        tr = Trace(np.arange(5, dtype=np.float32))

        # Year 2056 is non-deterministic for days 1, 256 and 257. These three
        # dates are simply simply not supported right now. See the libmseed
        # documentation for more details.
        # Use every 5th year. Otherwise the test takes too long. Use 1901 as
        # start to get year 2056.
        years = range(1901, 2101, 5)
        for year in years:
            for byteorder in ["<", ">"]:
                memfile = io.BytesIO()
                # Get some random time with the year and the byte order as the
                # seed.
                random.seed(year + ord(byteorder))
                tr.stats.starttime = UTCDateTime(
                    year,
                    julday=random.randrange(1, 365),
                    hour=random.randrange(0, 24),
                    minute=random.randrange(0, 60),
                    second=random.randrange(0, 60))
                if year == 2056:
                    tr.stats.starttime = UTCDateTime(2056, 2, 1)
                tr.write(memfile, format="mseed")
                st2 = read(memfile)
                assert len(st2) == 1
                tr2 = st2[0]
                # Remove the mseed specific header fields. These are obviously
                # not equal.
                del tr2.stats.mseed
                del tr2.stats._format
                assert tr == tr2

    def test_full_seed_with_non_default_dataquality(self, testdata):
        """
        Tests the reading of full SEED files with dataqualities other then D.
        """
        # Test the normal one first.
        filename = testdata['fullseed.mseed']
        st = read(filename)
        assert st[0].stats.mseed.dataquality == "D"

        # Test the others. They should also have identical data.
        filename = testdata['fullseed_dataquality_M.mseed']
        st = read(filename)
        data_m = st[0].data
        assert len(st) == 1
        assert st[0].stats.mseed.dataquality == "M"

        filename = testdata['fullseed_dataquality_R.mseed']
        st = read(filename)
        data_r = st[0].data
        assert len(st) == 1
        assert st[0].stats.mseed.dataquality == "R"

        filename = testdata['fullseed_dataquality_Q.mseed']
        st = read(filename)
        data_q = st[0].data
        assert len(st) == 1
        assert st[0].stats.mseed.dataquality == "Q"

        # Assert that the data is the same.
        np.testing.assert_array_equal(data_m, data_r)
        np.testing.assert_array_equal(data_m, data_q)

    @pytest.mark.skipif(
        "CONDAFORGE" in os.environ and
        os.environ.get("APPVEYOR", "false").lower() == "true",
        reason='Test is known to fail when building conda package in '
               'Appveyor.')
    def test_infinite_loop(self, testdata):
        """
        Tests that libmseed doesn't enter an infinite loop on buggy files.
        """
        filename = testdata['infinite-loop.mseed']

        process = multiprocessing.Process(target=_test_function,
                                          args=(filename, ))
        process.start()
        process.join(60)

        fail = process.is_alive()
        process.terminate()
        if process.is_alive():
            if platform.system() == 'Windows':
                os.kill(process.pid, signal.CTRL_BREAK_EVENT)
            else:
                os.kill(process.pid, signal.SIGKILL)
        assert not fail

    def test_microsecond_accuracy_reading_and_writing_before_1970(self):
        """
        Tests that reading and writing data with microsecond accuracy and
        before 1970 works as expected.
        """
        # Test a couple of timestamps. Positive and negative ones.
        timestamps = [123456.789123, -123456.789123, 1.123400, 1.123412,
                      1.123449, 1.123450, 1.123499, -1.123400, -1.123412,
                      -1.123449, -1.123450, -1.123451, -1.123499]

        for timestamp in timestamps:
            starttime = UTCDateTime(timestamp)
            assert starttime.timestamp == timestamp

            tr = Trace(data=np.linspace(0, 100, 101))
            tr.stats.starttime = starttime

            with io.BytesIO() as fh:
                tr.write(fh, format="mseed")
                fh.seek(0, 0)
                tr2 = read(fh)[0]

            del tr2.stats.mseed
            del tr2.stats._format

            assert tr2.stats.starttime == starttime
            assert tr2 == tr

    def test_reading_noise_records(self, testdata):
        """
        Tests reading a noise record. See #1495.
        """
        file = testdata['single_record_plus_noise_record.mseed']
        st = read(file)
        assert len(st) == 1
        tr = st[0]
        assert tr.id == "IM.NV32..BHE"
        assert tr.stats.npts == 277
        assert tr.stats.sampling_rate == 40.0

    def test_read_file_with_various_noise_records(self, testdata):
        """
        Tests reading a custom made file with noise records.
        """
        # This file has the following layout:
        # 1. 256 byte NOISE record
        # 2. 512 byte normal record - station NV30
        # 3. 128 byte NOISE record
        # 4. 512 byte normal record - station NV31
        # 5. 512 byte NOISE record
        # 6. 512 byte NOISE record
        # 7. 512 byte normal record - station NV32
        # 8. 1024 byte NOISE record
        # 9. 512 byte normal record - station NV33
        file = testdata['various_noise_records.mseed']
        st = read(file)

        assert len(st), 4
        assert st[0].stats.station, "NV30"
        assert st[1].stats.station, "NV31"
        assert st[2].stats.station, "NV32"
        assert st[3].stats.station, "NV33"

        # Data is the same across all records.
        np.testing.assert_allclose(st[0].data, st[1].data)
        np.testing.assert_allclose(st[0].data, st[2].data)
        np.testing.assert_allclose(st[0].data, st[3].data)

    def test_mseed_zero_data_offset(self, datapath):
        """
        Tests that a data offset of zero in the fixed header does not
        confuse ObsPy.

        The file contains three records: a normal one, followed by one with
        a data-offset of zero, followed by another normal one.

        This currently results in three returned traces:

        * CH.PANIX..LHZ |
          2016-08-21T01:41:19.000000Z - 2016-08-21T01:45:30.000000Z |
          1.0 Hz, 252 samples
        * CH.PANIX..LHZ |
          2016-08-21T01:43:37.000000Z - 2016-08-21T01:43:37.000000Z |
          1.0 Hz, 0 samples
        * CH.PANIX..LHZ |
          2016-08-21T01:45:31.000000Z - 2016-08-21T01:49:52.000000Z |
          1.0 Hz, 262 samples
        """
        file = datapath / "bizarre" / "mseed_data_offset_0.mseed"
        st = read(file)

        assert len(st) == 3

        tr = st[0]
        assert tr.id == "CH.PANIX..LHZ"
        assert tr.stats.starttime == UTCDateTime("2016-08-21T01:41:19.000000Z")
        assert tr.stats.endtime == UTCDateTime("2016-08-21T01:45:30.000000Z")
        assert tr.stats.npts == len(tr.data)
        assert tr.stats.npts == 252

        tr = st[1]
        assert tr.id == "CH.PANIX..LHZ"
        assert tr.stats.starttime == UTCDateTime("2016-08-21T01:43:37.000000Z")
        assert tr.stats.endtime == UTCDateTime("2016-08-21T01:43:37.000000Z")
        assert tr.stats.npts == len(tr.data)
        assert tr.stats.npts == 0

        tr = st[2]
        assert tr.id == "CH.PANIX..LHZ"
        assert tr.stats.starttime == UTCDateTime("2016-08-21T01:45:31.000000Z")
        assert tr.stats.endtime == UTCDateTime("2016-08-21T01:49:52.000000Z")
        assert tr.stats.npts == len(tr.data)
        assert tr.stats.npts == 262

    def test_mseed_zero_data_headonly(self, testdata):
        """
        Tests that records with no data correctly work in headonly mode.
        """
        file = testdata['three_records_zero_data_in_middle.mseed']

        expected = [
            ("BW.BGLD..EHE", UTCDateTime("2007-12-31T23:59:59.765000Z"),
             UTCDateTime("2008-01-01T00:00:01.820000Z"), 200.0, 412),
            ("BW.BGLD..EHE", UTCDateTime("2008-01-01T00:00:01.825000Z"),
             UTCDateTime("2008-01-01T00:00:01.825000Z"), 200.0, 0),
            ("BW.BGLD..EHE", UTCDateTime("2008-01-01T00:00:03.885000Z"),
             UTCDateTime("2008-01-01T00:00:05.940000Z"), 200.0, 412)]

        # Default full read.
        st = read(file)
        assert len(st) == 3
        for tr, exp in zip(st, expected):
            assert tr.id == exp[0]
            assert tr.stats.starttime == exp[1]
            assert tr.stats.endtime == exp[2]
            assert tr.stats.sampling_rate == exp[3]
            assert tr.stats.npts == exp[4]

        # Headonly read.
        st = read(file, headonly=True)
        assert len(st) == 3
        for tr, exp in zip(st, expected):
            assert tr.id == exp[0]
            assert tr.stats.starttime == exp[1]
            assert tr.stats.endtime == exp[2]
            assert tr.stats.sampling_rate == exp[3]
            assert tr.stats.npts == exp[4]

    def test_read_file_with_microsecond_wrap(self, testdata):
        """
        This is not strictly valid but I encountered such a file in practice
        so I guess it happens. Libmseed can also correctly deal with it.

        The test file is a single record with the .0001 seconds field set to
        10000. SEED strictly allows only 0-9999 in this field.
        """
        file = testdata['microsecond_wrap.mseed']

        with warnings.catch_warnings(record=True) as w_1:
            warnings.simplefilter("always")
            info = util.get_record_information(file)

        assert w_1[0].message.args[0] == \
            ('Record contains a fractional seconds (.0001 secs) '
             'of 10000 - the maximum strictly allowed value is '
             '9999. It will be interpreted as one or more '
             'additional seconds.')

        with warnings.catch_warnings(record=True) as w_2:
            warnings.simplefilter("always")
            tr = read(file)[0]

        # First warning is identical.
        assert w_1[0].message.args[0] == w_2[0].message.args[0]
        # Second warning is raised by libmseed.
        assert w_2[1].message.args[0] == \
            ('readMSEEDBuffer(): Record with offset=0 has a '
             'fractional second (.0001 seconds) of 10000. This '
             'is not strictly valid but will be interpreted as '
             'one or more additional seconds.')

        # Make sure libmseed and the internal ObsPy record parser produce
        # the same result.
        assert info["starttime"] == tr.stats.starttime
        assert info["endtime"] == tr.stats.endtime

        # Read with a hex-editor.
        ref_time = UTCDateTime(year=2008, julday=8, hour=4, minute=58,
                               second=5 + 1)
        assert ref_time == info["starttime"]
        assert ref_time == tr.stats.starttime

    def test_reading_miniseed_with_no_blockette_1000(self, datapath):
        """
        Blockette 1000 was only introduced with SEED version 2.3.
        """
        file = datapath / "bizarre" / "mseed_no_blkt_1000.mseed"
        st = read(file)

        assert len(st) == 1
        tr = st[0]
        assert tr.stats.npts == 7536
        np.testing.assert_allclose(tr.stats.sampling_rate, 20.0)
        assert tr.stats.starttime == UTCDateTime(1976, 3, 10, 3, 28)
        assert tr.id == ".GRA1..BHZ"

        # Also test the data to make sure the unpacking was successful.
        np.testing.assert_equal(
            st[0].data[:10],
            [-185, -200, -209, -220, -228, -246, -252, -262, -262, -269])

    def test_writing_of_blockette_100(self):
        """
        Tests the writing of blockette 100 if necessary.
        """
        def has_blkt_100(filename):
            ms = _MSStruct(filename)
            ms.read(-1, 0, 1, 0)
            blkt_link = ms.msr.contents.blkts
            has_blkt_100 = False
            while True:
                try:
                    if blkt_link.contents.blkt_type == 100:
                        has_blkt_100 = True
                        break
                    blkt_link = blkt_link.contents.next
                except ValueError:
                    break
            del ms
            return has_blkt_100

        tr = read()[0]
        tr.data = tr.data[:10]

        with NamedTemporaryFile() as tf:
            tempfile = tf.name

            # A "clean" sampling rate does not require blockette 100.
            sr = 200.0
            tr.stats.sampling_rate = sr
            tr.write(tempfile, format="mseed")
            assert np.float32(read(tempfile)[0].stats.sampling_rate) == \
                np.float32(sr)
            assert not has_blkt_100(tempfile)

            # A more detailed one does.
            sr = 199.9997
            tr.stats.sampling_rate = sr
            tr.write(tempfile, format="mseed")
            assert np.float32(read(tempfile)[0].stats.sampling_rate) == \
                np.float32(sr)
            assert has_blkt_100(tempfile)

            # A very large (but "clean") one does not need it.
            sr = 1E6
            tr.stats.sampling_rate = sr
            tr.write(tempfile, format="mseed")
            assert np.float32(read(tempfile)[0].stats.sampling_rate) == \
                np.float32(sr)
            assert not has_blkt_100(tempfile)

            # Same for a very small but "clean" one.
            sr = 1E-6
            tr.stats.sampling_rate = sr
            tr.write(tempfile, format="mseed")
            assert np.float32(read(tempfile)[0].stats.sampling_rate) == \
                np.float32(sr)
            assert not has_blkt_100(tempfile)

            # But small perturbations resulting in "unclean" sampling rates
            # will cause blockette 100 to be written.
            sr = 1E6 + 0.123456
            tr.stats.sampling_rate = sr
            tr.write(tempfile, format="mseed")
            assert np.float32(read(tempfile)[0].stats.sampling_rate) == \
                np.float32(sr)
            assert has_blkt_100(tempfile)
            sr = 1E-6 + 0.325247 * 1E-7
            tr.stats.sampling_rate = sr
            tr.write(tempfile, format="mseed")
            assert np.float32(read(tempfile)[0].stats.sampling_rate) == \
                np.float32(sr)
            assert has_blkt_100(tempfile)

            # Three more "clean" ones.
            sr = 1.0
            tr.stats.sampling_rate = sr
            tr.write(tempfile, format="mseed")
            assert np.float32(read(tempfile)[0].stats.sampling_rate) == \
                np.float32(sr)
            assert not has_blkt_100(tempfile)

            sr = 0.5
            tr.stats.sampling_rate = sr
            tr.write(tempfile, format="mseed")
            assert np.float32(read(tempfile)[0].stats.sampling_rate) == \
                np.float32(sr)
            assert not has_blkt_100(tempfile)

            sr = 0.1
            tr.stats.sampling_rate = sr
            tr.write(tempfile, format="mseed")
            assert np.float32(read(tempfile)[0].stats.sampling_rate) == \
                np.float32(sr)
            assert not has_blkt_100(tempfile)

    def test_reading_file_with_data_offset_of_48(self, testdata):
        """
        Tests reading a file which has a data offset of 48 bytes.

        It thus does not have a single blockette.
        """
        file = testdata['mseed_not_a_single_blkt_48byte_data_offset.mseed']
        st = read(file)

        assert len(st) == 1
        tr = st[0]
        assert tr.stats.npts == 3632
        np.testing.assert_allclose(tr.stats.sampling_rate, 20.0)
        assert tr.stats.starttime == UTCDateTime(1995, 9, 22, 0, 0, 18, 238400)
        assert tr.id == "XX.TEST..BHE"

        np.testing.assert_equal(
            st[0].data[:6],
            [337, 396, 454, 503, 547, 581])

    def test_reading_truncated_miniseed_files(self, testdata):
        """
        Regression test to guard against a segfault.
        """
        filename = testdata['BW.BGLD.__.EHE.D.2008.001.first_10_records']

        with io.open(filename, 'rb') as fh:
            data = fh.read()

        data = data[:-257]
        # This is the offset for the record that later has to be recorded in
        # the warning.
        assert len(data) - 255 == 4608

        # The file now lacks information at the end. This will read the file
        # until that point and raise a warning that some things are missing.
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            with io.BytesIO(data) as buf:
                st = _read_mseed(buf)
        assert len(st) == 1
        assert len(w) == 1
        assert w[0].category is InternalMSEEDWarning
        assert w[0].message.args[0] == (
            "readMSEEDBuffer(): Unexpected end of file when "
            "parsing record starting at offset 4608. The rest of "
            "the file will not be read.")

    def test_reading_truncated_miniseed_files_case_2(self, testdata):
        """
        Second test in the same vain as
        test_reading_truncated_miniseed_files. Previously forgot a `<=` test.
        """
        filename = testdata['BW.BGLD.__.EHE.D.2008.001.first_10_records']

        with io.open(filename, 'rb') as fh:
            data = fh.read()

        data = data[:-256]
        # This is the offset for the record that later has to be recorded in
        # the warning.
        assert len(data) - 256 == 4608

        # The file now lacks information at the end. This will read the file
        # until that point and raise a warning that some things are missing.
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            with io.BytesIO(data) as buf:
                st = _read_mseed(buf)
        assert len(st) == 1
        assert len(w) == 1
        assert w[0].category is InternalMSEEDWarning
        assert w[0].message.args[0] == (
            "readMSEEDBuffer(): Unexpected end of file when "
            "parsing record starting at offset 4608. The rest of "
            "the file will not be read.")

    def test_reading_less_than_128_bytes(self, testdata):
        """
        128 bytes is the smallest possible MiniSEED record.

        Reading anything smaller should result in an error.
        """
        filename = testdata['BW.BGLD.__.EHE.D.2008.001.first_10_records']

        with io.open(filename, 'rb') as fh:
            data = fh.read()

        # Reading at exactly 128 bytes offset will result in a truncation
        # warning.
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            with io.BytesIO(data[:128]) as buf:
                st = _read_mseed(buf)
        assert len(st) == 0  # nothing is read here.
        assert len(w) >= 1
        assert w[-1].category is InternalMSEEDWarning
        assert w[-1].message.args[0] == (
            "readMSEEDBuffer(): Unexpected end of file when "
            "parsing record starting at offset 0. The rest of "
            "the file will not be read.")

        # Reading anything less result in an exception.
        msg = ("The smallest possible mini-SEED record is made up of 128 "
               "bytes. The passed buffer or file contains only 127.")
        with pytest.raises(ObsPyMSEEDFilesizeTooSmallError, match=msg):
            with io.BytesIO(data[:127]) as buf:
                _read_mseed(buf)

    @mock.patch("os.path.getsize")
    def test_reading_file_larger_than_2048_mib(self, getsize_mock, testdata):
        """
        ObsPy can currently not directly read files that are larger than
        2^31 bytes. This raises an exception with a description of how to
        get around it.
        """
        getsize_mock.return_value = 2 ** 31 + 1
        filename = testdata['BW.BGLD.__.EHE.D.2008.001.first_10_records']
        msg = (
            "ObsPy can currently not directly read mini-SEED files that are "
            "larger than 2^31 bytes (2048 MiB). To still read it, please "
            "read the file in chunks as documented here: "
            "https://github.com/obspy/obspy/pull/1419#issuecomment-221582369")
        msg = re.escape(msg)
        with pytest.raises(ObsPyMSEEDFilesizeTooLargeError, match=msg):
            _read_mseed(filename)

    def test_read_file_with_non_valid_blocks_in_between(self, testdata):
        """
        Test reading MiniSEED files that have some non-valid blocks in-between.
        """
        # This file has two 4096 bytes records.
        filename = testdata['test.mseed']
        with io.open(filename, "rb") as fh:
            rec1 = fh.read(4096)
            rec2 = fh.read(4096)

        reference = _read_mseed(filename)
        del reference[0].stats.mseed

        # Fill with zero bytes.
        for length in (128, 256, 512, 1024, 2048, 4096, 8192):
            with io.BytesIO() as buf:
                buf.write(rec1)
                buf.write(b'\x00' * length)
                buf.write(rec2)
                buf.seek(0, 0)
                # This will raise 1 warning per 128 bytes.
                with CatchAndAssertWarnings() as w:
                    st = _read_mseed(buf)
                assert len(w) == length // 128

            # Also explicitly test the first warning message which should be
            # identical for all cases.
            assert str(w[0].message) == \
                "readMSEEDBuffer(): Not a SEED record. Will skip bytes " \
                "4096 to 4223."

            # Should always be two records.
            assert st[0].stats.mseed.number_of_records == 2

            # Remove things like file-size and what not.
            del st[0].stats.mseed
            assert reference == st

        # Try the same thing but fill with random bytes.
        # The seed is not really needed but hopefully guards against the
        # very very rare case of random bytes making up a valid SEED record.
        np.random.seed(34980)
        for length in (128, 256, 512, 1024, 2048, 4096, 8192):
            with io.BytesIO() as buf:
                buf.write(rec1)
                buf.write(np.random.bytes(length))
                buf.write(rec2)
                buf.seek(0, 0)
                # This will raise 1 warning per 128 bytes.
                with CatchAndAssertWarnings() as w:
                    st = _read_mseed(buf)
                assert len(w) == length // 128

            # Should always be two records.
            assert st[0].stats.mseed.number_of_records == 2

            # Remove things like file-size and what not.
            del st[0].stats.mseed
            assert reference == st

    def test_reading_files_with_non_ascii_headers(self, testdata):
        """
        Some dataloggers appear to do this.

        See #2177.
        """
        filename = testdata['gecko_non_ascii_header.ms']
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            st = read(filename)
        # Two identical messages will be raised (but in most common cases only
        # the first will be shown).
        assert len(w) == 2
        assert w[0].message.args[0].startswith(
            "Failed to decode location code as ASCII.")
        assert len(st) == 1
        assert st[0].id == '.GECKO.A.CNZ'
