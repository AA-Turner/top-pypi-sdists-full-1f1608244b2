#
# Copyright (c) 2009-2022 CERN. All rights nots expressly granted are
# reserved.
#
# This file is part of iLCDirac
# (see ilcdirac.cern.ch, contact: ilcdirac-support@cern.ch).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# In applying this licence, CERN does not waive the privileges and
# immunities granted to it by virtue of its status as an
# Intergovernmental Organization or submit itself to any jurisdiction.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
"""Test for WMS clients."""
# pylint: disable=protected-access, missing-docstring, invalid-name, line-too-long

from __future__ import print_function
from __future__ import absolute_import
import pytest

from mock import MagicMock

from DIRAC import S_OK, S_ERROR
from ILCDIRAC.WorkloadManagementSystem.Client.DownloadInputData import DownloadInputData

MODULE_NAME = 'ILCDIRAC.WorkloadManagementSystem.Client.DownloadInputData'

# pylint: disable=redefined-outer-name, unused-argument


@pytest.fixture(autouse=True)
def setUpLogger():
  from DIRAC import gLogger
  gLogger.setLevel('DEBUG')


@pytest.fixture
def mockSE(mocker):
  mockObjectSE = MagicMock()
  mockObjectSE.getFileMetadata.return_value = S_OK({'Successful': {'/a/lfn/1.txt': {'Cached': 1, 'Accessible': 1}},
                                                    'Failed': {}})
  mockObjectSE.getFile.return_value = S_OK({'Successful': {'/a/lfn/1.txt': {}}, 'Failed': {}})
  mockObjectSE.getStatus.return_value = S_OK({'Read': True, 'DiskSE': True})
  mockObjectSE.status.return_value = {'Read': True, 'DiskSE': True}

  theMockSE = MagicMock()
  theMockSE.return_value = mockObjectSE
  mocker.patch(MODULE_NAME + '.StorageElement', new=theMockSE)
  return theMockSE


@pytest.fixture
def dli():
  theDLI = DownloadInputData({'InputData': [],
                              'Configuration': {'LocalSEList': ['SE_Local']},
                              'InputDataDirectory': 'CWD',
                              'FileCatalog':
                                S_OK({'Successful': {'/a/lfn/1.txt': {'Size': 10,
                                                                      'GUID': 'aGUID',
                                                                      'SE_Local': '',
                                                                      'SE_Remote': '',
                                                                      'SE_Bad': '',
                                                                      'SE_Tape': '',
                                                                      }}})})
  theDLI._DownloadInputData__checkDiskSpace = MagicMock(return_value=S_OK(1000))
  theDLI.availableSEs = ['SE_Local', 'SE_Remote']
  return theDLI


@pytest.fixture
def osPathExists(mocker):
  osPathMock = MagicMock(return_value=True)
  mocker.patch('%s.os.path.exists' % MODULE_NAME, new=osPathMock)
  return osPathMock


@pytest.fixture
def getDiskSpace(mocker):
  gdsMock = MagicMock(return_value=True)
  mocker.patch('%s.getDiskSpace' % MODULE_NAME, new=gdsMock)
  return gdsMock


def test_DLIDownloadFromSE_fail(dli, mockSE, osPathExists):
  osPathExists.return_value = False
  res = dli._downloadFromSE('/a/lfn/1.txt', 'mySE', {'mySE': []}, 'aGuid')
  assert not res['OK']


def test_DLIDownloadFromSE_local(dli, mockSE, osPathExists):
  res = dli._downloadFromSE('/a/lfn/1.txt', 'mySE', {'mySE': []}, 'aGuid')
  assert res['OK'], res
  assert res['Value']['protocol'] == 'LocalData'


def test_DLIDownloadFromSE_realDown(dli, mockSE, osPathExists):
  osPathExists.side_effect = (False, False, True)
  res = dli._downloadFromSE('/a/lfn/1.txt', 'mySE', {'mySE': []}, 'aGuid')
  assert res['OK'], res.get('Message', 'No Error')
  assert res['Value']['protocol'] == 'Downloaded'
  assert 'path' in res['Value']
  assert res['Value']['path'].endswith('1.txt')


def test_DLIDownloadFromSE_realDown_Fail(dli, mockSE, osPathExists):
  mockObjectSE = mockSE.return_value
  mockObjectSE.getFile.return_value = S_OK({'Successful': {},
                                            'Failed': {'/a/lfn/1.txt': {}}})
  mockObjectSE.getStatus.return_value = S_OK({'Read': True, 'DiskSE': True})

  osPathExists.return_value = False
  res = dli._downloadFromSE('/a/lfn/1.txt', 'mySE', {'mySE': []}, 'aGuid')
  assert not res['OK'], res.get('Message', 'No Error')


def test_DLIDownloadFromBestSE_isLocal(dli, mockSE, osPathExists):
  res = dli._downloadFromBestSE('/a/lfn/1.txt', {'mySE': []}, 'aGuid')
  assert res['OK'], res.get('Message', 'No error')
  assert res['Value']['protocol'] == 'LocalData'


def test_DLIDownloadFromBestSE_Fail(dli, mockSE, osPathExists):
  osPathExists.return_value = False
  res = dli._downloadFromBestSE('/a/lfn/1.txt', {'mySE': []}, 'aGuid')
  assert not res['OK']


def test_DLI_execute(dli, mockSE):
  dli._downloadFromSE = MagicMock(return_value=S_OK({'path': '/local/path/1.txt'}))
  res = dli.execute(dataToResolve=['/a/lfn/1.txt'])
  assert res['OK']
  assert not res['Value']['Failed']
  assert '/a/lfn/1.txt' in res['Value']['Successful'], res


def test_DLI_execute_getFileMetadata_Fails(dli, mockSE):
  """When getFileMetadata fails for the first SE, we should fall back to the second."""
  mockObjectSE = mockSE.return_value
  mockObjectSE.getFileMetadata.return_value = S_OK({'Successful': {},
                                                    'Failed': {'/a/lfn/1.txt': 'Error Getting MetaData'}})

  dli._downloadFromSE = MagicMock(return_value=S_OK({'path': '/local/path/1.txt'}))
  dli._isCache = MagicMock(return_value=True)
  res = dli.execute(dataToResolve=['/a/lfn/1.txt'])
  assert res['OK']
  assert not res['Value']['Failed']
  assert '/a/lfn/1.txt' in res['Value']['Successful'], res
  assert res['Value']['Successful']['/a/lfn/1.txt']['path'] == '/local/path/1.txt', res


def test_DLI_execute_getFileMetadata_Lost(dli, mockSE):
  """When getFileMetadata fails for the first SE, we should fall back to the second."""
  mockObjectSE = mockSE.return_value
  mockObjectSE.getFileMetadata.return_value = S_OK({'Successful':
                                                    {'/a/lfn/1.txt':
                                                     {'Cached': 1, 'Accessible': 0,
                                                      'Lost': True,
                                                      }},
                                                    'Failed': {}})
  dli._downloadFromSE = MagicMock(return_value=S_OK({'path': '/local/path/1.txt'}))
  dli._isCache = MagicMock(return_value=True)
  res = dli.execute(dataToResolve=['/a/lfn/1.txt'])
  assert res['OK']
  assert not res['Value']['Failed']
  assert '/a/lfn/1.txt' in res['Value']['Successful'], res
  assert res['Value']['Successful']['/a/lfn/1.txt']['path'] == '/local/path/1.txt', res


def test_DLI_execute_getFileMetadata_Unavailable(dli, mockSE):
  """When getFileMetadata fails for the first SE, we should fall back to the second."""
  mockObjectSE = mockSE.return_value
  mockObjectSE.getFileMetadata.return_value = S_OK({'Successful':
                                                    {'/a/lfn/1.txt':
                                                     {'Cached': 0, 'Accessible': 0,
                                                      'Unavailable': True,
                                                      }},
                                                    'Failed': {}})
  dli._downloadFromSE = MagicMock(return_value=S_OK({'path': '/local/path/1.txt'}))
  dli._isCache = MagicMock(return_value=True)
  res = dli.execute(dataToResolve=['/a/lfn/1.txt'])
  assert res['OK']
  assert not res['Value']['Failed']
  assert '/a/lfn/1.txt' in res['Value']['Successful'], res
  assert res['Value']['Successful']['/a/lfn/1.txt']['path'] == '/local/path/1.txt', res


def test_DLI_execute_getFileMetadata_Cached(dli, mockSE):
  """When getFileMetadata fails for the first SE, we should fall back to the second."""
  mockObjectSE = mockSE.return_value
  mockObjectSE.getFileMetadata.return_value = S_OK({'Successful':
                                                    {'/a/lfn/1.txt':
                                                     {'Cached': 0, 'Accessible': 0,
                                                      'Unavailable': False,
                                                      }},
                                                    'Failed': {}})
  dli._downloadFromSE = MagicMock(return_value=S_OK({'path': '/local/path/1.txt'}))
  dli._isCache = MagicMock(return_value=True)
  res = dli.execute(dataToResolve=['/a/lfn/1.txt'])
  assert res['OK']
  assert not res['Value']['Failed']
  assert '/a/lfn/1.txt' in res['Value']['Successful'], res
  assert res['Value']['Successful']['/a/lfn/1.txt']['path'] == '/local/path/1.txt', res


def test_DLI_execute_FirstDownFailed(dli, mockSE):
  """When getFileMetadata fails for the first SE, we should fall back to the second."""
  mockObjectSE = mockSE.return_value
  mockObjectSE.getFileMetadata.return_value = S_OK({'Successful':
                                                    {'/a/lfn/1.txt': {'Cached': 1, 'Accessible': 0}},
                                                    'Failed': {}})
  dli._downloadFromSE = MagicMock(side_effect=[S_ERROR('Failed to down'),
                                               S_OK({'path': '/local/path/1.txt'})])
  dli._isCache = MagicMock(return_value=True)
  res = dli.execute(dataToResolve=['/a/lfn/1.txt'])
  assert res['OK']
  assert not res['Value']['Failed']
  assert '/a/lfn/1.txt' in res['Value']['Successful'], res
  assert res['Value']['Successful']['/a/lfn/1.txt']['path'] == '/local/path/1.txt', res


def test_DLI_execute_AllDownFailed(dli, mockSE):
  """When getFileMetadata fails for the first SE, we should fall back to the second."""
  mockObjectSE = mockSE.return_value
  mockObjectSE.getFileMetadata.return_value = S_OK({'Successful':
                                                    {'/a/lfn/1.txt': {'Cached': 1, 'Accessible': 0}},
                                                    'Failed': {}})
  dli._downloadFromSE = MagicMock(return_value=S_ERROR('Failed to down'))
  dli._isCache = MagicMock(return_value=True)
  res = dli.execute(dataToResolve=['/a/lfn/1.txt'])
  assert res['OK']
  assert res['Value']['Failed']
  assert '/a/lfn/1.txt' in res['Value']['Failed'], res
  assert res['Value']['Failed'][0] == '/a/lfn/1.txt', res


def test_DLI_execute_NoLocal(mockSE):
  """Data only at the remote SE."""
  dli = DownloadInputData({'InputData': [],
                           'Configuration': {'LocalSEList': ['SE_Local', 'SE_Tape']},
                           'InputDataDirectory': 'CWD',
                           'FileCatalog':
                           S_OK({'Successful': {'/a/lfn/1.txt': {'Size': 10, 'GUID': 'aGUID',
                                                                 'SE_Tape': '',
                                                                 }}})})
  dli._DownloadInputData__checkDiskSpace = MagicMock(return_value=S_OK(1000))
  dli.availableSEs = ['SE_Local', 'SE_Remote', 'SE_Tape']
  mockObjectSE = mockSE.return_value
  statDict = {'Read': True, 'TapeSE': True, 'DiskSE': False}
  mockObjectSE.getStatus.return_value = S_OK(statDict)
  mockObjectSE.status.return_value = statDict
  dli._downloadFromSE = MagicMock(return_value=S_ERROR('Failed to down'))
  dli._isCache = MagicMock(return_value=True)

  res = dli.execute(dataToResolve=['/a/lfn/1.txt'])
  assert res['OK']
  assert res['Value']['Failed']
  assert '/a/lfn/1.txt' in res['Value']['Failed'], res
  assert res['Value']['Failed'][0] == '/a/lfn/1.txt', res


def test_DLI_checkDiskSpace_success(getDiskSpace):
  """CheckDiskSpace function."""
  getDiskSpace.return_value = 10 * 1024  # in MB
  dli = DownloadInputData({'InputData': [],
                           'Configuration': {'LocalSEList': ['SE_Local', 'SE_Tape']},
                           'InputDataDirectory': 'CWD',
                           'FileCatalog':
                           S_OK({'Successful': {'/a/lfn/1.txt': {'Size': 10, 'GUID': 'aGUID',
                                                                 'SE_Tape': '',
                                                                 }}})})
  res = dli._DownloadInputData__checkDiskSpace(totalSize=10)
  assert res['OK']
  assert 'Enough disk space' in res['Value']


def test_DLI_checkDiskSpace_fail(getDiskSpace):
  """CheckDiskSpace function."""
  getDiskSpace.return_value = 10  # in MB
  dli = DownloadInputData({'InputData': [],
                           'Configuration': {'LocalSEList': ['SE_Local', 'SE_Tape']},
                           'InputDataDirectory': 'CWD',
                           'FileCatalog':
                           S_OK({'Successful': {'/a/lfn/1.txt': {'Size': 10, 'GUID': 'aGUID',
                                                                 'SE_Tape': '',
                                                                 }}})})
  res = dli._DownloadInputData__checkDiskSpace(totalSize=10 * 1024 * 1024)
  assert not res['OK']
  assert 'Not enough' in res['Message']
