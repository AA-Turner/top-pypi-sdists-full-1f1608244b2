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
"""Test OverlayInput module."""
from __future__ import absolute_import
import inspect
import unittest
from mock import patch, MagicMock as Mock

from DIRAC import S_OK, S_ERROR
from ILCDIRAC.Interfaces.API.NewInterface.Applications import OverlayInput
from Tests.Utilities.GeneralUtils import assertEqualsImproved, assertDiracFailsWith, \
    assertDiracSucceeds

__RCSID__ = "$Id$"

MODULE_NAME = 'ILCDIRAC.Interfaces.API.NewInterface.Applications.OverlayInput'

# pylint: disable=protected-access,too-many-public-methods


class OverlayInputTestCase(unittest.TestCase):
  """Base class for the OverlayInput test cases."""

  def setUp(self):
    """set up the objects."""
    self.olin = OverlayInput({})

  def test_setters(self):
    assertEqualsImproved((self.olin.machine, self.olin.prodID, self.olin.useEnergyForFileLookup,
                            self.olin.detectorModel, self.olin.backgroundEventType),
                          ('clic_cdr', 0, True, '', ''), self)
    self.assertFalse(self.olin._errorDict)
    self.olin.setMachine('mytestMachine')
    assertDiracSucceeds(self.olin.setProdID(14983), self)
    self.olin.setUseEnergyForFileLookup(False)
    self.olin.setDetectorModel('mytestDetector')
    self.olin.setBackgroundType('myBackgroundParticle.Testme')
    assertEqualsImproved((self.olin.machine, self.olin.prodID, self.olin.useEnergyForFileLookup,
                            self.olin.detectorModel, self.olin.backgroundEventType),
                          ('mytestMachine', 14983, False, 'mytestDetector', 'myBackgroundParticle.Testme'),
                          self)
    self.assertFalse(self.olin._errorDict)

  def test_setters_checks(self):
    self.olin.setMachine({'138rj': True})
    self.olin.setProdID([])
    self.olin.setUseEnergyForFileLookup('False')
    self.olin.setDetectorModel(9024)
    self.olin.setBackgroundType(8914)
    assertEqualsImproved(len(self.olin._errorDict['_checkArgs']), 5, self)

  def test_userjobmodules(self):
    with patch.object(self.olin, '_setApplicationModuleAndParameters', new=Mock(return_value=S_OK())):
      assertDiracSucceeds(self.olin._userjobmodules(Mock()), self)

  def test_userjobmodules_fails(self):
    with patch.object(self.olin, '_setApplicationModuleAndParameters', new=Mock(return_value=S_ERROR('bla'))):
      assertDiracFailsWith(self.olin._userjobmodules(Mock()), 'userjobmodules failed', self)

  def test_prodjobmodules(self):
    with patch.object(self.olin, '_setApplicationModuleAndParameters', new=Mock(return_value=S_OK())):
      assertDiracSucceeds(self.olin._prodjobmodules(Mock()), self)

  def test_prodjobmodules_fails(self):
    with patch.object(self.olin, '_setApplicationModuleAndParameters', new=Mock(return_value=S_ERROR('bla'))):
      assertDiracFailsWith(self.olin._prodjobmodules(Mock()), 'prodjobmodules failed', self)

  def test_addparameterstostep_fails(self):
    with patch.object(self.olin, '_addBaseParameters', new=Mock(return_value=S_ERROR('bla'))):
      assertDiracFailsWith(self.olin._addParametersToStep(Mock()), 'failed to set base param', self)

  def test_addparameterstostep(self):
    with patch.object(self.olin, '_addBaseParameters', new=Mock(return_value=S_OK())):
      assertDiracSucceeds(self.olin._addParametersToStep(Mock()), self)

  def test_checkconsistency(self):
    self.olin.pathToOverlayFiles = ''
    self.olin.bxToOverlay = True
    self.olin.numberOfGGToHadronInteractions = 1345
    self.olin.backgroundEventType = 'myTestBGEvt'
    self.olin._jobtype = 'notUser'
    assertDiracSucceeds(self.olin._checkConsistency(), self)
    assertEqualsImproved(
        (self.olin.prodparameters['detectorModel'], self.olin.prodparameters['BXOverlay'],
         self.olin.prodparameters['GGtoHadInt']),
        ('', True, 1345), self)

  def test_checkconsistency_nofilesinpath(self):
    self.olin.pathToOverlayFiles = '/my/path/overlay.files'
    with patch('DIRAC.Resources.Catalog.FileCatalogClient.FileCatalogClient.findFilesByMetadata', new=Mock(return_value=S_OK([]))) as fcc_mock:
      assertDiracFailsWith(self.olin._checkConsistency(), 'no files in that path', self)
      fcc_mock.assert_called_once_with({}, '/my/path/overlay.files')

  def test_checkconsistency_no_bunchcrossings(self):
    self.olin.pathToOverlayFiles = ''
    self.olin.bxToOverlay = None
    assertDiracFailsWith(self.olin._checkConsistency(), 'number of overlay bunch crossings not defined', self)

  def test_checkconsistency_no_backgroundevts(self):
    self.olin.pathToOverlayFiles = ''
    self.olin.bxToOverlay = True
    self.olin.numberOfGGToHadronInteractions = 0
    assertDiracFailsWith(self.olin._checkConsistency(), 'background events per bunch crossing is not defined',
                          self)

  def test_checkconsistency_no_bgevttype(self):
    self.olin.pathToOverlayFiles = ''
    self.olin.bxToOverlay = True
    self.olin.numberOfGGToHadronInteractions = 1345
    self.olin.backgroundEventType = ''
    assertDiracFailsWith(self.olin._checkConsistency(), 'event type is not defined', self)

  def test_checkconsistency_nosignalevtperjob(self):
    self.olin.pathToOverlayFiles = ''
    self.olin.bxToOverlay = True
    self.olin.numberOfGGToHadronInteractions = 1345
    self.olin.backgroundEventType = 'gghad'
    self.olin._jobtype = 'User'
    self.olin.numberOfSignalEventsPerJob = 0
    assertDiracFailsWith(self.olin._checkConsistency(), 'signal event per job is not defined',
                          self)

  def test_checkfinalconsistency_simple(self):
    self.olin.pathToOverlayFiles = 'some/path'
    assertDiracSucceeds(self.olin._checkFinalConsistency(), self)

  def test_checkfinalconsistency_noenergy(self):
    self.olin.energy = 0
    assertDiracFailsWith(self.olin._checkFinalConsistency(), 'energy must be specified', self)

  def test_checkfinalconsistency_ops_fails(self):
    ops_mock = Mock()
    ops_mock.getSections.return_value = S_ERROR('some_ops_error')
    self.olin._ops = ops_mock
    self.olin.energy = 198
    assertDiracFailsWith(self.olin._checkFinalConsistency(), 'could not resolve the cs path', self)

  def test_checkfinalconsistency_machinemissing(self):
    ops_mock = Mock()
    ops_mock.getSections.return_value = S_OK(['allowed_machine_1', 'other_mach'])
    self.olin._ops = ops_mock
    self.olin.machine = 'myTestMachineVeryRare'
    self.olin.energy = 198
    res = self.olin._checkFinalConsistency()
    assertDiracFailsWith(res,
                         "machine 'mytestmachineveryrare' does not have overlay data", self)

  def test_checkfinalconsistency_energynotfound(self):
    self.olin.energy = 824
    section_dict = {'/Overlay': ['myTestMachineVeryRare'],
                     '/Overlay/myTestMachineVeryRare': ['other_energy_tev', '824tev']}
    ops_mock = Mock()
    ops_mock.getSections.side_effect = lambda path: S_OK(section_dict[path])
    self.olin._ops = ops_mock
    self.olin.machine = 'myTestMachineVeryRare'
    assertDiracFailsWith(self.olin._checkFinalConsistency(),
                          'no overlay files corresponding to 824gev', self)

  def test_checkfinalconsistency_nodetectormodels(self):
    self.olin.energy = 1000.0
    section_dict = {'/Overlay': S_OK(['myTestMachineVeryRare']),
                     '/Overlay/myTestMachineVeryRare': S_OK(['other_energy_tev', '1tev']),
                     '/Overlay/myTestMachineVeryRare/1tev': S_ERROR('bla')}
    ops_mock = Mock()
    ops_mock.getSections.side_effect = lambda path: section_dict[path]
    self.olin._ops = ops_mock
    self.olin.machine = 'myTestMachineVeryRare'
    assertDiracFailsWith(self.olin._checkFinalConsistency(),
                          'could not find the detector models', self)

  def test_checkfinalconsistency_detectormodelnotfound(self):
    self.olin.energy = 981324
    section_dict = {'/Overlay': ['myTestMachineVeryRare'],
                     '/Overlay/myTestMachineVeryRare': ['other_energy_tev', '981.3gev'],
                     '/Overlay/myTestMachineVeryRare/981.3tev': ['some_other_detector_model',
                                                                   'neither_this']}
    ops_mock = Mock()
    ops_mock.getSections.side_effect = lambda path: S_OK(section_dict[path])
    self.olin._ops = ops_mock
    self.olin.machine = 'myTestMachineVeryRare'
    assertDiracFailsWith(self.olin._checkFinalConsistency(),
                          'no overlay files corresponding to 981.3tev', self)

  def test_checkfinalconsistency_nobkg(self):
    self.olin.detectorModel = 'testDetMod'
    self.olin.energy = 981000
    section_dict = {'/Overlay': ['myTestMachineVeryRare'],
                     '/Overlay/myTestMachineVeryRare': ['other_energy_tev', '981tev'],
                     '/Overlay/myTestMachineVeryRare/981tev': ['testDetMod']}
    ops_mock = Mock()
    ops_mock.getSections.side_effect = lambda path: S_OK(section_dict[path])
    self.olin._ops = ops_mock
    self.olin.machine = 'myTestMachineVeryRare'
    with patch.object(inspect.getmodule(OverlayInput), 'allowedBkg', new=Mock(return_value=S_ERROR('bkg_test_err'))):
      assertDiracFailsWith(self.olin._checkFinalConsistency(), 'bkg_test_err', self)

  def test_checkfinalconsistency_negativeprodid(self):
    self.olin.detectorModel = 'testDetMod'
    self.olin.energy = 981000
    section_dict = {'/Overlay': ['myTestMachineVeryRare'],
                     '/Overlay/myTestMachineVeryRare': ['other_energy_tev', '981tev'],
                     '/Overlay/myTestMachineVeryRare/981tev': ['testDetMod']}
    ops_mock = Mock()
    ops_mock.getSections.side_effect = lambda path: S_OK(section_dict[path])
    self.olin._ops = ops_mock
    self.olin.machine = 'myTestMachineVeryRare'
    with patch.object(inspect.getmodule(OverlayInput), 'allowedBkg', new=Mock(return_value=S_OK(-147))):
      assertDiracFailsWith(self.olin._checkFinalConsistency(), 'no proper production id found', self)

  def test_checkfinalconsistency(self):
    self.olin.detectorModel = 'testDetMod'
    self.olin.energy = 981000
    section_dict = {'/Overlay': ['myTestMachineVeryRare'],
                     '/Overlay/myTestMachineVeryRare': ['other_energy_tev', '981tev'],
                     '/Overlay/myTestMachineVeryRare/981tev': ['testDetMod']}
    ops_mock = Mock()
    ops_mock.getSections.side_effect = lambda path: S_OK(section_dict[path])
    self.olin._ops = ops_mock
    self.olin.machine = 'myTestMachineVeryRare'
    with patch.object(inspect.getmodule(OverlayInput), 'allowedBkg', new=Mock(return_value=S_OK(13987))):
      assertDiracSucceeds(self.olin._checkFinalConsistency(), self)

  def test_printAvailableOptions(self):
    """Tests for printAvailableOptions.

    As there are no return values we check that the proper log messages are printed to error or notice.
    """
    confMock = Mock()
    confMock.getConfigurationTree.return_value = S_ERROR('')
    logMock = Mock(name='Logger')
    with patch.object(inspect.getmodule(OverlayInput), 'gConfig', new=confMock), \
         patch.object(inspect.getmodule(OverlayInput), 'LOG', new=logMock):
      self.olin.printAvailableOptions()
    logMock.error.assert_called_once()

    confMock = Mock()
    confMock.getConfigurationTree.return_value = S_OK({'/Operations/Defaults/Overlay/CLIC/1tev/DET/SUSY': 12,
                                                       '/Operations/Defaults/Overlay/Not_CLIC/1tev/DET/BKG_TYPE': 14,
                                                       '/Operations/Defaults/Overlay/CLIC/1tev/Other_DET/BKG_TYPE': 15,
                                                       '/Operations/Defaults/Overlay/CLIC/1tev/DET': 13,
                                                     })

    logMock.reset()
    with patch.object(inspect.getmodule(OverlayInput), 'gConfig', new=confMock), \
         patch.object(inspect.getmodule(OverlayInput), 'LOG', new=logMock):
      self.olin.printAvailableOptions()
    logMock.info.assert_not_called()  # make sure we use notice

    logMock.reset()
    with patch.object(inspect.getmodule(OverlayInput), 'gConfig', new=confMock), \
         patch.object(inspect.getmodule(OverlayInput), 'LOG', new=logMock):
      self.olin.printAvailableOptions(detModel='DET')
    logMock.info.assert_not_called()
    logMock.notice.assert_any_call('Printing options compatible with')
    logMock.notice.assert_any_call(' * DetModel = DET')

    logMock.reset()
    with patch.object(inspect.getmodule(OverlayInput), 'gConfig', new=confMock), \
         patch.object(inspect.getmodule(OverlayInput), 'LOG', new=logMock):
      self.olin.printAvailableOptions(energy=2000)
    logMock.info.assert_not_called()
    logMock.notice.assert_any_call('Printing options compatible with')
    logMock.notice.assert_any_call(' * Energy = 2tev')

    logMock.reset()
    with patch.object(inspect.getmodule(OverlayInput), 'gConfig', new=confMock), \
         patch.object(inspect.getmodule(OverlayInput), 'LOG', new=logMock):
      self.olin.printAvailableOptions(machine='CLIC')
    logMock.info.assert_not_called()
    logMock.notice.assert_any_call('Printing options compatible with')
    logMock.notice.assert_any_call(' * Machine = CLIC')

    logMock.reset()
    with patch.object(inspect.getmodule(OverlayInput), 'gConfig', new=confMock), \
         patch.object(inspect.getmodule(OverlayInput), 'LOG', new=logMock):
      self.olin.printAvailableOptions(energy=2000, machine='FCCee', detModel='NO_DET')
    logMock.notice.assert_any_call('No overlay options compatible with your selection')
