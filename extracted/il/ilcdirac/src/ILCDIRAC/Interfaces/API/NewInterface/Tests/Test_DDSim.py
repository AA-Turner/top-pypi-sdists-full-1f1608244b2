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
"""Test DDSim module."""

from __future__ import print_function
from __future__ import absolute_import
import inspect
import unittest
from mock import create_autospec, patch, MagicMock as Mock

from DIRAC import gLogger, S_OK, S_ERROR
from ILCDIRAC.Interfaces.API.NewInterface.Applications import DDSim
from Tests.Utilities.GeneralUtils import assertEqualsImproved, assertDiracFailsWith, \
    assertDiracSucceeds

__RCSID__ = "$Id$"

MODULE_NAME = 'ILCDIRAC.Interfaces.API.NewInterface.Applications.DDSim'

gLogger.setLevel("DEBUG")
gLogger.showHeaders(True)

# pylint: disable=protected-access


class DDSimTestCase(unittest.TestCase):
  """Base class for the DDSim test cases."""

  def setUp(self):
    """set up the objects."""
    self.dds = DDSim({})

  def test_setrandomseed(self):
    self.assertFalse(self.dds._errorDict)
    self.dds.setRandomSeed(89421)
    self.assertFalse(self.dds._errorDict)
    assertEqualsImproved(self.dds.randomSeed, 89421, self)

  def test_setrandomseed_fails(self):
    self.assertFalse(self.dds._errorDict)
    self.dds.setRandomSeed(['abc'])
    self.assertIn('_checkArgs', self.dds._errorDict)

  def test_addextraparticles_pass(self):
    """Test if API write correctly."""
    self.assertFalse(self.dds._errorDict)
    self.dds.setExtraParticles([[25, "Maribor", 2, 1500., 10., 100.]])
    self.assertFalse(self.dds._errorDict)
    assertEqualsImproved(self.dds.extraParticles, [[25, "Maribor", 2, 1500., 10., 100.]], self)

  def test_addextraparticles_pass2(self):
    """Test if API write correctly."""
    self.assertFalse(self.dds._errorDict)
    self.dds.setExtraParticles("25 Maribor 2 1500. 10. -100. -25 Radizel 2 -1500. 10. 100.")
    self.assertFalse(self.dds._errorDict)
    assertEqualsImproved(self.dds.extraParticles, [[25, "Maribor", 2, 1500., 10., -100.],
                                                   [-25, "Radizel", 2, -1500., 10., 100.]], self)

  def test_addextraparticles_fails(self):
    """Test if API detects wrong input."""
    self.assertFalse(self.dds._errorDict)
    ret = self.dds.setExtraParticles('abc')
    self.assertIn("multiples of 6", ret['Message'])
    self.assertIn('setExtraParticles', self.dds._errorDict)

  def test_addextraparticles_fail2(self):
    """Test if API detects wrong input."""
    self.assertFalse(self.dds._errorDict)
    ret = self.dds.setExtraParticles("25 Ptuj 2 1500. 10. 100. 10.")
    self.assertIn("multiples of 6", ret['Message'])
    self.assertIn('setExtraParticles', self.dds._errorDict)

  def test_addextraparticles_fail3(self):
    """Test if API detects wrong input."""
    self.assertFalse(self.dds._errorDict)
    ret = self.dds.setExtraParticles("25.0 Sentilj 2 1500. 10. 100.")
    self.assertIn("Cannot convert input string to proper format", ret['Message'])
    self.assertIn('setExtraParticles', self.dds._errorDict)

  def test_addextraparticles_fail4(self):
    """Test if API detects wrong input."""
    self.assertFalse(self.dds._errorDict)
    ret = self.dds.setExtraParticles("25 Graz 2 a 10. 100.")
    self.assertIn("Cannot convert input string to proper format", ret['Message'])
    self.assertIn('setExtraParticles', self.dds._errorDict)

  def test_setstartfrom(self):
    self.assertFalse(self.dds._errorDict)
    self.dds.setStartFrom(89421)
    self.assertFalse(self.dds._errorDict)
    assertEqualsImproved(self.dds.startFrom, 89421, self)

  def test_setstartfrom_fails(self):
    self.assertFalse(self.dds._errorDict)
    self.dds.setStartFrom('adgiuj')
    self.assertIn('_checkArgs', self.dds._errorDict)

  def test_resolvelinkedparams(self):
    step_mock = Mock()
    input_mock = Mock()
    input_mock.getType.return_value = {'abc': False}
    self.dds._linkedidx = 3
    self.dds._jobsteps = [None, None, None, input_mock]
    assertDiracSucceeds(self.dds._resolveLinkedStepParameters(step_mock), self)
    step_mock.setLink.assert_called_once_with('InputFile', {'abc': False}, 'OutputFile')

  def test_resolvelinkedparams_noinputstep(self):
    self.dds._linkedidx = None
    self.dds._inputappstep = []
    assertDiracSucceeds(self.dds._resolveLinkedStepParameters(None), self)

  def test_checkworkflow_app_missing(self):
    self.dds._inputapp = ['some_depdency', 'unavailable_dependency_fail_on_this']
    self.dds._jobapps = ['myjobapp_1', 'some_dependency']
    assertDiracFailsWith(self.dds._checkWorkflowConsistency(), 'job order not correct', self)

  def test_checkworkflow_empty(self):
    self.dds._inputapp = []
    self.dds._jobapps = []
    assertDiracSucceeds(self.dds._checkWorkflowConsistency(), self)

  def test_checkworkflow_success(self):
    self.dds._inputapp = ['some_dependency', 'other_dependencies', 'many_more']
    self.dds._jobapps = ['ignore_me', 'many_more', 'some_dependency', 'other_dependencies']
    assertDiracSucceeds(self.dds._checkWorkflowConsistency(), self)

  def test_userjobmodules(self):
    module_mock = Mock()
    assertDiracSucceeds(self.dds._userjobmodules(module_mock), self)

  def test_prodjobmodules(self):
    module_mock = Mock()
    assertDiracSucceeds(self.dds._prodjobmodules(module_mock), self)

  def test_userjobmodules_fails(self):
    with patch('%s._setUserJobFinalization' % MODULE_NAME, new=Mock(return_value=S_OK('something'))),\
        patch('%s._setApplicationModuleAndParameters' % MODULE_NAME, new=Mock(return_value=S_ERROR('some_test_err'))):
      assertDiracFailsWith(self.dds._userjobmodules(None),
                            'userjobmodules failed', self)

  def test_prodjobmodules_fails(self):
    with patch('%s._setApplicationModuleAndParameters' % MODULE_NAME, new=Mock(return_value=S_OK('something'))), \
        patch('%s._setOutputComputeDataList' % MODULE_NAME, new=Mock(return_value=S_ERROR('some_other_test_err'))):
      assertDiracFailsWith(self.dds._prodjobmodules(None),
                            'prodjobmodules failed', self)

  def test_checkconsistency(self):
    self.dds.version = '134'
    self.dds.detectorModel = 'mymodel.det'
    self.dds.outputFile = 'myoutput.file'
    self.dds._jobtype = 'User'
    assertDiracSucceeds(self.dds._checkConsistency(Mock()), self)
    self.assertNotIn({'outputFile': '@{OutputFile}', 'outputPath': '@{OutputPath}',
                        'outputDataSE': '@{OutputSE}'}, self.dds._listofoutput)
    self.assertNotIn('nbevts', self.dds.prodparameters)
    self.assertNotIn('Process', self.dds.prodparameters)

  def test_checkconsistency_extraparticles(self):
    """Check if consistency check for extra particles passes."""
    self.dds.version = '134'
    self.dds.detectorModel = 'mymodel.det'
    self.dds.outputFile = 'myoutput.file'
    self.dds._jobtype = 'User'
    self.dds.extraParticles = [[25, "Maribor", 2, 1500., 10., 100.]]
    assertDiracSucceeds(self.dds._checkConsistency(Mock()), self)

  def test_checkconsistency_extraparticles1(self):
    """Check if consistency check for extra particles detects wrong type."""
    self.dds.version = '134'
    self.dds.detectorModel = 'mymodel.det'
    self.dds.outputFile = 'myoutput.file'
    self.dds._jobtype = 'User'
    self.dds.extraParticles = [25, "Maribor", 2, 1500., 10., 100.]
    assertDiracFailsWith(self.dds._checkConsistency(Mock()), 'Wrong format', self)

  def test_checkconsistency_extraparticles2(self):
    """Check if consistency check for extra particles detects too long input."""
    self.dds.version = '134'
    self.dds.detectorModel = 'mymodel.det'
    self.dds.outputFile = 'myoutput.file'
    self.dds._jobtype = 'User'
    self.dds.extraParticles = [[25, "Maribor", 2, 1500., 10., 100., 10]]
    assertDiracFailsWith(self.dds._checkConsistency(Mock()), 'Particle property not of correct format', self)

  def test_checkconsistency_extraparticles3(self):
    """Check if consistency check for extra particles detects first argument correctly."""
    self.dds.version = '134'
    self.dds.detectorModel = 'mymodel.det'
    self.dds.outputFile = 'myoutput.file'
    self.dds._jobtype = 'User'
    self.dds.extraParticles = [[25., "Maribor", 2, 1500., 10., 100.]]
    assertDiracFailsWith(self.dds._checkConsistency(Mock()), 'Particle property ID not int', self)

  def test_checkconsistency_extraparticles4(self):
    """Check if consistency check for extra particles detects second argument correctly."""
    self.dds.version = '134'
    self.dds.detectorModel = 'mymodel.det'
    self.dds.outputFile = 'myoutput.file'
    self.dds._jobtype = 'User'
    self.dds.extraParticles = [[25, 1, 2, 1500., 10., 100.]]
    assertDiracFailsWith(self.dds._checkConsistency(Mock()), 'Particle property name not string', self)

  def test_checkconsistency_extraparticles5(self):
    """Check if consistency check for extra particles detects third argument correctly."""
    self.dds.version = '134'
    self.dds.detectorModel = 'mymodel.det'
    self.dds.outputFile = 'myoutput.file'
    self.dds._jobtype = 'User'
    self.dds.extraParticles = [[25, "Maribor", 2., 1500., 10., 100.]]
    assertDiracFailsWith(self.dds._checkConsistency(Mock()), 'Particle property chg not int', self)

  def test_checkconsistency_extraparticles6(self):
    """Check if consistency check for extra particles detects fourth argument correctly."""
    self.dds.version = '134'
    self.dds.detectorModel = 'mymodel.det'
    self.dds.outputFile = 'myoutput.file'
    self.dds._jobtype = 'User'
    self.dds.extraParticles = [[25, "Maribor", 2, 1500, 10., 100.]]
    assertDiracFailsWith(self.dds._checkConsistency(Mock()), 'Particle property mass not float', self)

  def test_checkconsistency_extraparticles7(self):
    """Check if consistency check for extra particles detects fifth argument correctly."""
    self.dds.version = '134'
    self.dds.detectorModel = 'mymodel.det'
    self.dds.outputFile = 'myoutput.file'
    self.dds._jobtype = 'User'
    self.dds.extraParticles = [[25, "Maribor", 2, 1500., "10.", 100.]]
    assertDiracFailsWith(self.dds._checkConsistency(Mock()), 'Particle property total width not float', self)

  def test_checkconsistency_extraparticles8(self):
    """Check if consistency check for extra particles detects sixth argument correctly."""
    self.dds.version = '134'
    self.dds.detectorModel = 'mymodel.det'
    self.dds.outputFile = 'myoutput.file'
    self.dds._jobtype = 'User'
    self.dds.extraParticles = [[25, "Maribor", 2, 1500., 10., 'test']]
    assertDiracFailsWith(self.dds._checkConsistency(Mock()), 'Particle property lifetime not float', self)

  def test_checkconsistency_nodetectormodel(self):
    self.dds.version = 123
    self.dds.steeringFile = None
    self.dds.detectorModel = None
    assertDiracFailsWith(self.dds._checkConsistency(Mock()), 'no detectormodel set', self)

  def test_checkconsistency_noversion(self):
    self.dds.version = None
    assertDiracFailsWith(self.dds._checkConsistency(Mock()), 'no version found', self)

  def test_checkconsistency_existsfails(self):
    self.dds.version = '134'
    self.dds.steeringFile = 'mysteer.file'
    with patch('os.path.exists', new=Mock(return_value=False)), \
         patch.object(inspect.getmodule(DDSim), 'Exists', new=Mock(return_value=S_ERROR('testerr_exists_mock'))):
      assertDiracFailsWith(self.dds._checkConsistency(Mock()), 'testerr_exists_mock', self)

  def test_checkconsistency_userjob(self):
    self.dds.version = '134'
    self.dds.steeringFile = 'mysteer.file'
    self.dds._jobtype = 'notUser'
    self.dds.detectorModel = 'myDetectorv200'
    with patch('os.path.exists', new=Mock(return_value=True)), \
         patch.object(inspect.getmodule(DDSim), 'Exists', new=Mock(return_value=S_ERROR('testerr_exists_mock'))):
      assertDiracSucceeds(self.dds._checkConsistency(Mock()), self)
      self.assertIn({'outputFile': '@{OutputFile}', 'outputPath': '@{OutputPath}',
                       'outputDataSE': '@{OutputSE}'}, self.dds._listofoutput)
      for keyword in ['detectorType', 'slic_detectormodel']:
        self.assertIn(keyword, self.dds.prodparameters)

  def test_checkconsistency_userjob_notdetmodel(self):
    self.dds.version = '134'
    self.dds.steeringFile = 'mysteer.file'
    self.dds._jobtype = 'notUser'
    self.dds.detectorModel = True
    self.dds.setStartFrom(148)
    with patch('os.path.exists', new=Mock(return_value=False)), \
         patch.object(inspect.getmodule(DDSim), 'Exists', new=Mock(return_value=S_OK())):
      assertDiracSucceeds(self.dds._checkConsistency(Mock()), self)
      self.assertIn({'outputFile': '@{OutputFile}', 'outputPath': '@{OutputPath}',
                       'outputDataSE': '@{OutputSE}'}, self.dds._listofoutput)
      for keyword in ['detectorType', 'slic_detectormodel']:
        self.assertIn(keyword, self.dds.prodparameters)

# pylint: disable=protected-access


class TestDDSim(unittest.TestCase):
  """tests for the DDSim interface."""

  def setUp(self):
    pass

  def tearDown(self):
    """cleanup any files."""
    pass

  @patch("ILCDIRAC.Interfaces.API.NewInterface.Applications.DDSim.getKnownDetectorModels",
          new=Mock(return_value=S_OK({'CLIC_o2_v03': "/some/path"})))
  def test_setDetectorModel1(self):
    """test DDSIm setDetectorModel part of software................................................."""
    detModel = "CLIC_o2_v03"
    ddsim = DDSim()
    ddsim.setDetectorModel(detModel)
    self.assertEqual(ddsim.detectorModel, detModel)

  @patch("ILCDIRAC.Interfaces.API.NewInterface.Applications.DDSim.getKnownDetectorModels",
          new=Mock(return_value=S_ERROR("No known models")))
  def test_setDetectorModel2(self):
    """test DDSIm setDetectorModel part of software failure........................................."""
    detModel = "CLIC_o2_v03"
    ddsim = DDSim()
    res = ddsim.setDetectorModel(detModel)
    self.assertIn("No known models", res['Message'])

  @patch("ILCDIRAC.Interfaces.API.NewInterface.Applications.DDSim.getKnownDetectorModels",
          new=Mock(return_value=S_OK({'CLIC_o2_v04': "/some/path"})))
  def test_setDetectorModel3(self):
    """test DDSIm setDetectorModel is not known....................................................."""
    detModel = "ATLAS"
    ddsim = DDSim()
    ret = ddsim.setDetectorModel(detModel)
    self.assertEqual(ddsim.detectorModel, '')
    self.assertFalse(ret['OK'])
    self.assertIn("Unknown detector model in ddsim: ATLAS", ret['Message'])
    self.assertIn("setDetectorModel", ddsim._errorDict)

  @patch("os.path.exists", new=Mock(return_value=True))
  def test_setDetectorModel_TB_success(self):
    """test DDSIm setDetectorModel tarBall success.................................................."""
    detModel = "CLIC_o2_v03"
    ext = ".tar.gz"
    ddsim = DDSim()
    ddsim.setDetectorModel(detModel + ext)
    self.assertEqual(ddsim.detectorModel, detModel)
    self.assertTrue(detModel + ext in ddsim.inputSB)

  @patch("os.path.exists", new=Mock(return_value=False))
  def test_setDetectorModel_TB_notLocal(self):
    """test DDSIm setDetectorModel tarBall notLocal................................................."""
    detModel = "CLIC_o2_v03"
    ext = ".tgz"
    ddsim = DDSim()
    ddsim.setDetectorModel(detModel + ext)
    self.assertEqual(ddsim.inputSB, [])
    self.assertEqual(ddsim.detectorModel, detModel)

  def test_setDetectorModel_LFN_succcess(self):
    """test DDSIm setDetectorModel lfn success......................................................"""
    detModel = "lfn:/ilc/user/s/sailer/CLIC_o2_v03.tar.gz"
    ddsim = DDSim()
    ddsim.setDetectorModel(detModel)
    self.assertEqual(ddsim.detectorModel, "CLIC_o2_v03")
    self.assertTrue(detModel in ddsim.inputSB)

  def test_setStartFrom1(self):
    """test DDSIm setStartFrom 1...................................................................."""
    ddsim = DDSim()
    ddsim.setStartFrom("Arg")
    self.assertTrue(ddsim._errorDict)

  def test_setStartFrom2(self):
    """test DDSIm setStartFrom 2...................................................................."""
    ddsim = DDSim()
    ddsim.setStartFrom(42)
    self.assertEqual(ddsim.startFrom, 42)

  def test_getKnownDetModels1(self):
    """test getKnownDetectorModels failure no version..............................................."""
    ddsim = DDSim()
    ret = ddsim.getKnownDetectorModels()
    self.assertFalse(ret['OK'])
    self.assertEqual("No software version defined", ret['Message'])

  def test_getKnownDetModels2(self):
    """test getKnownDetectorModels success.........................................................."""
    ddsim = DDSim()
    ddsim.version = "test"
    import DIRAC
    ddsim._ops = create_autospec(DIRAC.ConfigurationSystem.Client.Helpers.Operations.Operations, spec_set=True)
    ddsim._ops.getOptionsDict.return_value = S_OK({"detModel1": "/path", "detModel2": "/path2"})
    ret = ddsim.getKnownDetectorModels()
    self.assertIn("detModel1", ret['Value'])
    self.assertTrue(ret['OK'])


def runTests():
  """Runs our tests."""
  suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestDDSim)
  testResult = unittest.TextTestRunner(verbosity=2).run(suite)
  print(testResult)
  suite = unittest.defaultTestLoader.loadTestsFromTestCase(DDSimTestCase)
  testResult = unittest.TextTestRunner(verbosity=2).run(suite)
  print(testResult)


if __name__ == '__main__':
  runTests()
