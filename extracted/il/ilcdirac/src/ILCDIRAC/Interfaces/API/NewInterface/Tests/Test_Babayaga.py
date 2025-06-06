#!/usr/local/env python
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
"""Test Babayaga module."""

from __future__ import print_function
from __future__ import absolute_import
import linecache
import unittest
from mock import patch, MagicMock as Mock
from mock import mock_open
from mock import mock as mock_module
import six

from DIRAC import gLogger, S_OK, S_ERROR
from ILCDIRAC.Interfaces.API.NewInterface.Applications import Babayaga
from Tests.Utilities.GeneralUtils import assertEqualsImproved, assertDiracFailsWith, \
    assertDiracSucceeds

__RCSID__ = "$Id$"

MODULE_NAME = 'ILCDIRAC.Interfaces.API.NewInterface.Applications.Babayaga'
BUILTIN_NAME = 'builtins' if six.PY3 else '__builtin__'

gLogger.setLevel("DEBUG")
gLogger.showHeaders(True)

# pylint: disable=protected-access

class BabayagaTestCase(unittest.TestCase):
  """Base class for the Babayaga test cases."""

  @classmethod
  def setUpClass(cls):
    """Load the Application file into the linecache to prevent exceptions when mocking the builtin open."""
    from ILCDIRAC.Interfaces.API.NewInterface import Application
    for fName in [Application.__file__, mock_module.__file__]:
      if fName.endswith(('.pyc', '.pyo')):
        fName = fName[:-1]
      linecache.getlines(fName)

  @classmethod
  def tearDownClass(cls):
    """Remove all entries from linecache because we mock builtin open."""
    linecache.clearcache()

  def setUp(self):
    """set up the objects."""
    self.babayaga = Babayaga({})
    self.babayaga._jobtype = 'User'
    self.babayaga._ops = Mock(name='OpsMock')

  @patch('os.path.isfile', new=Mock(return_value=True))
  @patch('%s.open' % BUILTIN_NAME, mock_open(read_data='configFile content'))
  def test_setConfigFile(self):
    """Test setConfigFile."""
    self.assertFalse(self.babayaga._errorDict)
    self.babayaga.setConfigFile('/some/path/configFile.input')
    self.assertFalse(self.babayaga._errorDict)
    assertEqualsImproved(self.babayaga.babayagaConfigFile, 'configFile content', self)

  @patch('os.path.isfile', new=Mock(return_value=False))
  def test_setConfigFile_fail(self):
    """Test setConfigFile."""
    self.assertFalse(self.babayaga._errorDict)
    assertDiracFailsWith(self.babayaga.setConfigFile('/some/path/configFile.input'), 'Babayaga config file does not exist!', self)

  def test_checkworkflow_app_missing(self):
    self.babayaga._inputapp = ['some_depdency', 'unavailable_dependency_fail_on_this']
    self.babayaga._jobapps = ['myjobapp_1', 'some_dependency']
    assertDiracFailsWith(self.babayaga._checkWorkflowConsistency(), 'job order not correct', self)

  def test_checkworkflow_empty(self):
    self.babayaga._inputapp = []
    self.babayaga._jobapps = []
    assertDiracSucceeds(self.babayaga._checkWorkflowConsistency(), self)

  def test_setrandomseed(self):
    self.assertFalse(self.babayaga._errorDict)
    self.babayaga.setRandomSeed(89421)
    self.assertFalse(self.babayaga._errorDict)
    assertEqualsImproved(self.babayaga.randomSeed, 89421, self)

  def test_setrandomseed_fails(self):
    self.assertFalse(self.babayaga._errorDict)
    self.babayaga.setRandomSeed(['abc'])
    self.assertIn('_checkArgs', self.babayaga._errorDict)

  def test_setBabayagaConfigFile(self):
    self.assertFalse(self.babayaga._errorDict)
    with patch("builtins.open", mock_open(read_data='content')), \
         patch('os.path.isfile', new=Mock(return_value=True)):
      res = self.babayaga.setBabayagaConfigFile("babayaga.input")
      assertDiracSucceeds(res, self)
      assertEqualsImproved(self.babayaga.babayagaConfigFileContent, 'content', self)

  def test_setbabayagaConfigFile_fails_file(self):
    self.assertFalse(self.babayaga._errorDict)
    res = self.babayaga.setBabayagaConfigFile("content")
    assertDiracFailsWith(res, 'Babayaga configuration file does not exist!', self)

  def test_setbabayagaConfigFile_fails_argument(self):
    self.assertFalse(self.babayaga._errorDict)
    res = self.babayaga.setBabayagaConfigFile(1)
    self.assertIn('_checkArgs', self.babayaga._errorDict)

  def test_setarguments(self):
    self.assertFalse(self.babayaga._errorDict)
    self.babayaga.setArguments("arguments")
    self.assertFalse(self.babayaga._errorDict)
    assertEqualsImproved(self.babayaga.extraCLIArguments, "arguments", self)
    assertDiracSucceeds(self.babayaga.setArguments("arguments"), self)

  def test_setarguments_fails(self):
    self.assertFalse(self.babayaga._errorDict)
    self.babayaga.setArguments(None)
    self.assertIn('_checkArgs', self.babayaga._errorDict) 

  def test_userjobmodules(self):
    module_mock = Mock()
    assertDiracSucceeds(self.babayaga._userjobmodules(module_mock), self)

  def test_prodjobmodules(self):
    module_mock = Mock()
    assertDiracSucceeds(self.babayaga._prodjobmodules(module_mock), self)

  def test_userjobmodules_fails(self):
    with patch('%s._setUserJobFinalization' % MODULE_NAME, new=Mock(return_value=S_OK('something'))),\
            patch('%s._setApplicationModuleAndParameters' % MODULE_NAME, new=Mock(return_value=S_ERROR('some_test_err'))):
      assertDiracFailsWith(self.babayaga._userjobmodules(None),
                           'userjobmodules failed', self)

  def test_prodjobmodules_fails(self):
    with patch('%s._setApplicationModuleAndParameters' % MODULE_NAME, new=Mock(return_value=S_OK('something'))), \
            patch('%s._setOutputComputeDataList' % MODULE_NAME, new=Mock(return_value=S_ERROR('some_other_test_err'))):
      assertDiracFailsWith(self.babayaga._prodjobmodules(None),
                           'prodjobmodules failed', self)
      
# ---------------------------------------------------------------------------------------------------------------------------------

  def test_checkconsistency_noVersion(self):
    self.babayaga.version = None
    assertDiracFailsWith(self.babayaga._checkConsistency(Mock()), 'No version found!', self)

  def test_checkconsistency_notuserjob(self):
    self.babayaga.version = 'LCG_97a_FCC_4'
    self.babayaga._jobtype = 'not a User'
    assertDiracSucceeds(self.babayaga._checkConsistency(Mock()), self)

  def test_checkconsistency_configFile(self):
    self.babayaga.version = 'LCG_97a_FCC_4'
    self.babayaga.babayagaConfigFile = 'babayaga_steer.input'
    assertDiracSucceeds(self.babayaga._checkConsistency(Mock()), self)

  def test_checkconsistency_noConfigFile(self):
    self.babayaga.version = 'LCG_97a_FCC_4'
    self.babayaga.babayagaConfigFile = None
    assertDiracFailsWith(self.babayaga._checkConsistency(Mock()), 'No config file set!', self)

  def test_checkconsistency_parameters(self):
    self.babayaga.version = 'LCG_97a_FCC_4'
    self.babayaga.babayagaConfigFile = None
    self.babayaga.energy = '91.2'
    self.babayaga.numberOfEvents = '1000'
    self.babayaga.outputFile = 'babayaga_1000.LHE'
    assertDiracSucceeds(self.babayaga._checkConsistency(Mock()), self)

  def test_checkconsistency_noEnergy(self):
    self.babayaga.version = 'LCG_97a_FCC_4'
    self.babayaga.babayagaConfigFile = None
    self.babayaga.energy = None
    self.babayaga.numberOfEvents = 1000
    self.babayaga.outputFile = 'babayaga_1000.LHE'
    assertDiracFailsWith(self.babayaga._checkConsistency(Mock()), 'No energy set!', self)

  def test_checkconsistency_noNumberOfEvents(self):
    self.babayaga.version = 'LCG_97a_FCC_4'
    self.babayaga.babayagaConfigFile = None
    self.babayaga.energy = 91.2
    self.babayaga.numberOfEvents = None
    self.babayaga.outputFile = 'babayaga_1000.LHE'
    assertDiracFailsWith(self.babayaga._checkConsistency(Mock()), 'No number of events set!', self)

  def test_checkconsistency_noOutputFile(self):
    self.babayaga.version = 'LCG_97a_FCC_4'
    self.babayaga.babayagaConfigFile = None
    self.babayaga.energy = 91.2
    self.babayaga.numberOfEvents = 1000
    self.babayaga.outputFile = None
    assertDiracFailsWith(self.babayaga._checkConsistency(Mock()), 'No output file set!', self)

  def test_checkconsistency_badseed(self):
    self.babayaga.version = 'LCG_97a_FCC_4'
    self.babayaga.babayagaConfigFile = None
    self.babayaga.energy = 91.2
    self.babayaga.numberOfEvents = 1000
    self.babayaga.outputFile = 'babayaga_1000.LHE'
    self.babayaga.randomSeed = -2
    assertDiracFailsWith(self.babayaga._checkConsistency(Mock()), 'Random Seed has to be equal or greater than -1', self)

    self.babayaga._jobtype = 'User'



def runTests():
  """Runs our tests."""
  suite = unittest.defaultTestLoader.loadTestsFromTestCase(BabayagaTestCase)
  testResult = unittest.TextTestRunner(verbosity=2).run(suite)
  print(testResult)


if __name__ == '__main__':
  runTests()
