#!/usr/bin/env python
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
"""Test the DDSim WorkflowModule."""

from __future__ import print_function
from __future__ import absolute_import

import unittest
import os
import shutil
import tempfile
import tarfile
import sys
from zipfile import ZipFile
from mock import patch, MagicMock as Mock, mock_open
import six

from DIRAC import gLogger, S_OK, S_ERROR
from ILCDIRAC.Workflow.Modules.DDSimAnalysis import DDSimAnalysis
from Tests.Utilities.GeneralUtils import assertDiracSucceeds

__RCSID__ = "$Id$"

MODULE_NAME = 'ILCDIRAC.Workflow.Modules.DDSimAnalysis'
MODULEBASE_NAME = 'ILCDIRAC.Workflow.Modules.ModuleBase'
PROXYINFO_NAME = 'DIRAC.Core.Security.ProxyInfo'
DD4H_NAME = 'ILCDIRAC.Workflow.Utilities.DD4hepMixin'
BUILTIN_NAME = 'builtins' if six.PY3 else '__builtin__'

# pylint: disable=too-many-public-methods, protected-access

gLogger.setLevel("ERROR")
gLogger.showHeaders(True)


def cleanup(tempdir):
  """Remove files after run."""
  try:
    shutil.rmtree(tempdir)
  except OSError:
    pass


@patch("%s.getProxyInfoAsString" % MODULEBASE_NAME, new=Mock(return_value=S_OK()))
@patch("%s.getProxyInfoAsString" % PROXYINFO_NAME, new=Mock(return_value=S_OK()))
class TestDDSimAnalysis(unittest.TestCase):
  """test DDSimAnalysis."""

  def assertIn(self, *args, **kwargs):
    """make this existing to placate pylint."""
    return super(TestDDSimAnalysis, self).assertIn(*args, **kwargs)

  @patch("%s.getProxyInfoAsString" % MODULEBASE_NAME, new=Mock(return_value=S_OK()))
  @patch("%s.getProxyInfoAsString" % PROXYINFO_NAME, new=Mock(return_value=S_OK()))
  def setUp(self):
    self.ddsim = DDSimAnalysis()
    self.curdir = os.getcwd()
    self.tempdir = tempfile.mkdtemp("", dir="./")
    os.chdir(self.tempdir)

    mocked_modules = {'DIRAC.ConfigurationSystem.Client.Helpers.Operations': Mock()}
    self.module_patcher = patch.dict(sys.modules, mocked_modules)
    self.module_patcher.start()

  def tearDown(self):
    os.chdir(self.curdir)
    cleanup(self.tempdir)
    self.module_patcher.stop()


class TestDDSimAnalysisParticleTable(TestDDSimAnalysis):
  """test DDSim createParticleTable."""

  def setUp(self):
    """Help with setup."""
    super(TestDDSimAnalysisParticleTable, self).setUp()
    self.logFileName = "python101.log"
    with open(self.logFileName, "w") as logF:
      logF.write("logged the logging logs")

  @patch('%s.open' % BUILTIN_NAME, new_callable=mock_open, read_data="export DD4hepINSTALL=\"some/path\"")
  def test_DDSim_particleTable_success(self, mo):
    """DDSim.createParticleTable...................................................................."""
    self.ddsim.extraParticles = [[25, "Maribor", 2, 1500., 10., 100.]]
    handlers = (mo.return_value, mock_open(read_data=" 2 u 2 0.33000 0.00000 0.00000E+00").return_value)
    mo.side_effect = handlers
    with patch("os.path.exists", new=Mock(side_effect=[True])):
      res = self.ddsim.createParticleTable("Dummy/path", ['SIM.physics.pdgfile = None', 'SIM.physics.list = "AList"'])
    print(res)
    self.assertIn("25 Maribor 2 1500.0 10.0 100.0", res['Value'])

  @patch('%s.open' % BUILTIN_NAME, new_callable=mock_open, read_data="export DD4hepINSTALL=\"some/path\"")
  def test_DDSim_particleTable_success2(self, mo):
    """DDSim.createParticleTable...................................................................."""
    self.ddsim.extraParticles = [[13, "mu", 2, 1500., 10., 100.]]
    handlers = (mo.return_value, mock_open(read_data=" 2 u 2 0.33000 0.00000 0.00000E+00\n"
                                                     "  13 mu^- -3 0.10566 0.00000 6.58654E+05").return_value)
    mo.side_effect = handlers
    with patch("os.path.exists", new=Mock(side_effect=[True])):
      res = self.ddsim.createParticleTable("Dummy/path", [])
    print(res)
    self.assertEqual([' 2 u 2 0.33000 0.00000 0.00000E+00', '13 mu 2 1500.0 10.0 100.0'], res['Value'])

  @patch('%s.open' % BUILTIN_NAME, new_callable=mock_open, read_data=" 2 u 2 0.33000 0.00000 0.00000E+00\n")
  def test_DDSim_particleTable_success3(self, mo):
    """DDSim.createParticleTable...................................................................."""
    self.ddsim.extraParticles = [[13, "mu", 2, 1500., 10., 100.]]
    with patch("os.path.exists", new=Mock(side_effect=[True])):
      res = self.ddsim.createParticleTable("Dummy/path", ['SIM.physics.pdgfile = "/here/is/the/file"'])
      print(res)
      self.assertEqual([' 2 u 2 0.33000 0.00000 0.00000E+00', '13 mu 2 1500.0 10.0 100.0'], res['Value'])

  @patch("%s.open" % BUILTIN_NAME, mock_open(read_data="export INSTAL=\"some/path\""))
  def test_DDSim_particleTable_fail(self):
    """DDSim.createParticleTable...................................................................."""
    self.ddsim.extraParticles = [[25, "Maribor", 2., 1500., 10., 100.]]
    res = self.ddsim.createParticleTable("Dummy/path", [])
    print(res)
    self.assertIn("Did not find env", res['Message'])

  @patch('%s.open' % BUILTIN_NAME, new_callable=mock_open, read_data=" 2 u 2 0.33000 0.00000 0.00000E+00\n")
  def test_DDSim_particleTable_fail2(self, mo):
    """DDSim.createParticleTable...................................................................."""
    self.ddsim.extraParticles = [[13, "mu", 2, 1500., 10., 100.]]
    res = self.ddsim.createParticleTable("Dummy/path", ['SIM.physics.pdgfile = "/here/is/the/file"'])
    print(res)
    self.assertIn("/here/is/the/file", res['Message'])

  @patch('%s.open' % BUILTIN_NAME, new_callable=mock_open, read_data="read OK")
  @patch("%s.shellCall" % MODULE_NAME, new=Mock(return_value=S_OK((0, "AllGood"))))
  def test_DDSim_resolveDDSimOptions_success(self, mo):
    """DDSim.resolveDDSimOption...................................................................."""
    with patch("os.chmod", new=Mock(side_effect=[True])):
      res = self.ddsim.resolveDDSimOptions("/path/to/end", "CLIC_o2_something")
    print(res)
    self.assertIn("read OK", res['Value'])

  @patch('%s.open' % BUILTIN_NAME, new_callable=mock_open, read_data="")
  @patch("%s.shellCall" % MODULE_NAME, new=Mock(return_value=S_OK((0, "AllGood"))))
  def test_DDSim_resolveDDSimOptions_fail(self, mo):
    """DDSim.resolveDDSimOption...................................................................."""
    with patch("os.chmod", new=Mock(side_effect=[True])):
      res = self.ddsim.resolveDDSimOptions("/path/to/end", "CLIC_o2_something")
    print(res)
    self.assertIn("empty", res['Message'])


class TestDDSimAnalysisRunit(TestDDSimAnalysis):
  """test DDSim runtIt."""

  def setUp(self):
    super(TestDDSimAnalysisRunit, self).setUp()
    self.logFileName = "python101.log"
    with open(self.logFileName, "w") as logF:
      logF.write("logged the logging logs")

  @patch("%s.getEnvironmentScript" % MODULE_NAME, new=Mock(return_value=S_OK("ddsiming.sh")))
  @patch("%s.DDSimAnalysis._getDetectorXML" % MODULE_NAME, new=Mock(return_value=S_OK("myDet.xml")))
  @patch("%s.shellCall" % MODULE_NAME, new=Mock(return_value=S_OK((0, "AllGood"))))
  def test_DDSim_runIt_success(self):
    """DDSim.runit ................................................................................."""
    self.ddsim.platform = "Windows"
    self.ddsim.applicationLog = self.logFileName
    # side effect for Script, userlibs, log, logAfter
    with patch("os.path.exists", new=Mock(side_effect=[False, False, False, True])):
      res = self.ddsim.runIt()
    print(res)
    assertDiracSucceeds(res, self)

  @patch("%s.getEnvironmentScript" % MODULE_NAME, new=Mock(return_value=S_OK("ddsiming.sh")))
  @patch("%s.DDSimAnalysis._getDetectorXML" % MODULE_NAME, new=Mock(return_value=S_OK("myDet.xml")))
  @patch("%s.resolveIFpaths" % MODULE_NAME, new=Mock(return_value=S_OK(["pairs.hepmc"])))
  @patch("%s.shellCall" % MODULE_NAME, new=Mock(return_value=S_OK((0, "AllGood"))))
  def test_DDSim_runIt_success_inputFile(self):
    """DDSim.runit success with inputFile..........................................................."""
    self.ddsim.platform = "Windows"
    self.ddsim.applicationLog = self.logFileName
    self.ddsim.InputFile = "pairs.hepmc"
    # side effect for Script, userlibs, log, logAfter
    with patch("os.path.exists", new=Mock(side_effect=[False, True, False, True])):
      res = self.ddsim.runIt()
    assertDiracSucceeds(res, self)
    self.assertEqual(self.ddsim.InputFile, ["pairs.hepmc"])
    self.assertIn(" --inputFile pairs.hepmc ", self.ddsim.extraCLIarguments)

  @patch("%s.getEnvironmentScript" % MODULE_NAME, new=Mock(return_value=S_OK("ddsiming.sh")))
  @patch("%s.DDSimAnalysis._getDetectorXML" % MODULE_NAME, new=Mock(return_value=S_OK("myDet.xml")))
  @patch("%s.resolveIFpaths" % MODULE_NAME, new=Mock(return_value=S_ERROR("no pairs.hepmc")))
  @patch("%s.shellCall" % MODULE_NAME, new=Mock(return_value=S_OK((0, "AllGood"))))
  def test_DDSim_runIt_failure_inputFile(self):
    """DDSim.runit failure with inputFile..........................................................."""
    self.ddsim.platform = "Windows"
    self.ddsim.applicationLog = self.logFileName
    self.ddsim.InputFile = "pairs.hepmc"
    # side effect for Script, log, logAfter
    with patch("os.path.exists", new=Mock(side_effect=[False, False, True])):
      res = self.ddsim.runIt()
    self.assertEqual(res['Message'], "no pairs.hepmc")

  @patch("%s.getEnvironmentScript" % MODULE_NAME, new=Mock(return_value=S_OK("ddsiming.sh")))
  @patch("%s.DDSimAnalysis._getDetectorXML" % MODULE_NAME, new=Mock(return_value=S_OK("myDet.xml")))
  @patch("%s.resolveIFpaths" % MODULE_NAME, new=Mock(return_value=S_OK("pairs.hepmc")))
  @patch("%s.shellCall" % MODULE_NAME, new=Mock(return_value=S_OK((0, "AllGood"))))
  def test_DDSim_runIt_failure_LogFile(self):
    """DDSim.runit failure with applicationLog......................................................"""
    self.ddsim.platform = "Windows"
    self.ddsim.applicationLog = self.logFileName
    self.ddsim.InputFile = "pairs.hepmc"
    self.ddsim.ignoreapperrors = False
    # side effect for Script, userlibs, log, logAfter
    with patch("os.path.exists", new=Mock(side_effect=[False, False, False, False])):
      res = self.ddsim.runIt()
    self.assertIn("did not produce the expected log", res['Message'])

  @patch("%s.getEnvironmentScript" % MODULE_NAME, new=Mock(return_value=S_OK("ddsiming.sh")))
  @patch("%s.DDSimAnalysis._getDetectorXML" % MODULE_NAME, new=Mock(return_value=S_OK("myDet.xml")))
  @patch("%s.resolveIFpaths" % MODULE_NAME, new=Mock(return_value=S_OK("pairs.hepmc")))
  @patch("%s.shellCall" % MODULE_NAME, new=Mock(return_value=S_OK((0, "AllGood"))))
  def test_DDSim_runIt_failure_LogFile_ignore(self):
    """DDSim.runit failure with applicationLog but ignore..........................................."""
    self.ddsim.platform = "Windows"
    self.ddsim.applicationLog = self.logFileName
    self.ddsim.InputFile = "pairs.hepmc"
    self.ddsim.ignoreapperrors = True
    # side effect for Script, userlibs, log, logAfter
    with patch("os.path.exists", new=Mock(side_effect=[False, False, False, False])):
      res = self.ddsim.runIt()
    assertDiracSucceeds(res, self)

  @patch("%s.getEnvironmentScript" % MODULE_NAME, new=Mock(return_value=S_OK("ddsiming.sh")))
  @patch("%s.DDSimAnalysis._getDetectorXML" % MODULE_NAME, new=Mock(return_value=S_OK("myDet.xml")))
  @patch("%s.resolveIFpaths" % MODULE_NAME, new=Mock(return_value=S_OK("pairs.hepmc")))
  @patch("%s.shellCall" % MODULE_NAME, new=Mock(return_value=S_OK((0, "AllGood"))))
  def test_DDSim_runIt_success_LogAndScriptPresent(self):
    """DDSim.runit success log and script exist....................................................."""
    self.ddsim.platform = "Windows"
    self.ddsim.applicationLog = self.logFileName
    self.ddsim.InputFile = "pairs.hepmc"
    self.ddsim.ignoreapperrors = True
    with open("DDSim__Run_.sh", "w") as scr:
      scr.write("content")
    with open(self.logFileName, "w") as scr:
      scr.write("content")
    # side effect for Script, userlibs, log, logAfter
    with patch("os.path.exists", new=Mock(side_effect=[True, False, True, True])):
      res = self.ddsim.runIt()
    assertDiracSucceeds(res, self)

  @patch("%s.getEnvironmentScript" % MODULE_NAME, new=Mock(return_value=S_OK("ddsiming.sh")))
  @patch("%s.DDSimAnalysis._getDetectorXML" % MODULE_NAME, new=Mock(return_value=S_OK("myDet.xml")))
  @patch("%s.shellCall" % MODULE_NAME, new=Mock(return_value=S_OK((0, "AllGood"))))
  def test_DDSim_runIt_success_steeringFile(self):
    """DDSim.runit success with steeringFile........................................................"""
    self.ddsim.platform = "Windows"
    self.ddsim.applicationLog = self.logFileName
    self.ddsim.SteeringFile = "mySteering.py"
    # side effect for Steering1, Steering2, Script, userlib, log, logAfter
    with patch("os.path.exists", new=Mock(side_effect=[True, True, False, False, False, True])):
      res = self.ddsim.runIt()
    assertDiracSucceeds(res, self)
    self.assertEqual(self.ddsim.SteeringFile, "mySteering.py")
    steerFlag = " --steeringFile %s " % self.ddsim.SteeringFile
    self.assertIn(steerFlag, self.ddsim.extraCLIarguments)

  @patch("%s.getEnvironmentScript" % MODULE_NAME, new=Mock(return_value=S_OK("ddsiming.sh")))
  @patch("%s.DDSimAnalysis._getDetectorXML" % MODULE_NAME, new=Mock(return_value=S_OK("myDet.xml")))
  @patch("%s.shellCall" % MODULE_NAME, new=Mock(return_value=S_OK((0, "AllGood"))))
  @patch("%s.getSteeringFileDirName" % MODULE_NAME, new=Mock(return_value=S_OK("SteerFold")))
  def test_DDSim_runIt_success_steeringFile_1(self):
    """DDSim.runit success with non-local steeringFile.............................................."""
    self.ddsim.platform = "Windows"
    self.ddsim.applicationLog = self.logFileName
    self.ddsim.SteeringFile = "mySteering.py"
    # side effect for Steering1a, Steering1b, Steering2, Script, userlib, log, logAfter
    with patch("os.path.exists", new=Mock(side_effect=[False, True, True, False, False, False, True])):
      res = self.ddsim.runIt()
    assertDiracSucceeds(res, self)
    fullPath = os.path.join("SteerFold", "mySteering.py")
    self.assertEqual(self.ddsim.SteeringFile, fullPath)
    steerFlag = " --steeringFile %s " % fullPath
    self.assertIn(steerFlag, self.ddsim.extraCLIarguments)

  @patch("%s.getEnvironmentScript" % MODULE_NAME, new=Mock(return_value=S_OK("ddsiming.sh")))
  @patch("%s.DDSimAnalysis._getDetectorXML" % MODULE_NAME, new=Mock(return_value=S_OK("myDet.xml")))
  @patch("%s.shellCall" % MODULE_NAME, new=Mock(return_value=S_OK((0, "AllGood"))))
  @patch("%s.getSteeringFileDirName" % MODULE_NAME, new=Mock(return_value=S_ERROR("NothingToSee")))
  def test_DDSim_runIt_failure_steeringFile_1(self):
    """DDSim.runit failure with non-local steeringFile.............................................."""
    self.ddsim.platform = "Windows"
    self.ddsim.applicationLog = self.logFileName
    self.ddsim.SteeringFile = "mySteering.py"
    # side effect for Steering1a, Steering1b, Steering2, Script, log, logAfter
    with patch("os.path.exists", new=Mock(side_effect=[False, True, True, False, False, True])):
      res = self.ddsim.runIt()
    self.assertFalse(res['OK'])
    self.assertEqual(res['Message'], "NothingToSee")

  @patch("%s.getEnvironmentScript" % MODULE_NAME, new=Mock(return_value=S_OK("ddsiming.sh")))
  @patch("%s.DDSimAnalysis._getDetectorXML" % MODULE_NAME, new=Mock(return_value=S_OK("myDet.xml")))
  @patch("%s.shellCall" % MODULE_NAME, new=Mock(return_value=S_OK((0, "AllGood"))))
  @patch("%s.getSteeringFileDirName" % MODULE_NAME, new=Mock(return_value=S_OK("SteerFold")))
  def test_DDSim_runIt_failure_steeringFile_2(self):
    """DDSim.runit failure with non-local steeringFile 2............................................"""
    self.ddsim.platform = "Windows"
    self.ddsim.applicationLog = self.logFileName
    self.ddsim.SteeringFile = "mySteering.py"
    # side effect for Steering1a, Steering1b, Steering2, Script, log, logAfter
    with patch("os.path.exists", new=Mock(side_effect=[False, False, False, False, False, True])):
      res = self.ddsim.runIt()
    self.assertFalse(res['OK'])
    self.assertEqual(res['Message'], "Could not find steering file")

  #######################
  # Test NumberOfEvents #
  #######################

  @patch("%s.getEnvironmentScript" % MODULE_NAME, new=Mock(return_value=S_OK("ddsiming.sh")))
  @patch("%s.DDSimAnalysis._getDetectorXML" % MODULE_NAME, new=Mock(return_value=S_OK("myDet.xml")))
  @patch("%s.shellCall" % MODULE_NAME, new=Mock(return_value=S_OK((0, "AllGood"))))
  @patch("%s.getSteeringFileDirName" % MODULE_NAME, new=Mock(return_value=S_OK("SteerFold")))
  def test_DDSim_runIt_success_numberOfEvents_1(self):
    """DDSim.runit success with NumberOfEvents set.................................................."""
    self.ddsim.platform = "Windows"
    self.ddsim.applicationLog = self.logFileName
    self.ddsim.SteeringFile = "mySteering.py"
    self.ddsim.NumberOfEvents = 123
    # side effect for Steering1a, Steering1b, Steering2, Script, userlibs, log, logAfter
    with patch("os.path.exists", new=Mock(side_effect=[False, True, True, False, False, False, True])):
      res = self.ddsim.runIt()
    assertDiracSucceeds(res, self)
    self.assertIn(" --numberOfEvents 123 ", self.ddsim.extraCLIarguments)

  ##############################
  # Test skipNEvents/startFrom #
  ##############################
  @patch("%s.getEnvironmentScript" % MODULE_NAME, new=Mock(return_value=S_OK("ddsiming.sh")))
  @patch("%s.DDSimAnalysis._getDetectorXML" % MODULE_NAME, new=Mock(return_value=S_OK("myDet.xml")))
  @patch("%s.shellCall" % MODULE_NAME, new=Mock(return_value=S_OK((0, "AllGood"))))
  @patch("%s.getSteeringFileDirName" % MODULE_NAME, new=Mock(return_value=S_OK("SteerFold")))
  def test_DDSim_runIt_success_skipNevents(self):
    """DDSim.runit success with startFrom..........................................................."""
    self.ddsim.platform = "Windows"
    self.ddsim.applicationLog = self.logFileName
    self.ddsim.SteeringFile = "mySteering.py"
    self.ddsim.NumberOfEvents = 123
    self.ddsim.startFrom = 22
    # side effect for Steering1a, Steering1b, Steering2, Script, userlibs, log, logAfter
    with patch("os.path.exists", new=Mock(side_effect=[False, True, True, False, False, False, True])):
      res = self.ddsim.runIt()
    assertDiracSucceeds(res, self)
    self.assertIn(" --skipNEvents 22 ", self.ddsim.extraCLIarguments)

  ##############
  # Test Debug #
  ##############
  @patch("%s.getEnvironmentScript" % MODULE_NAME, new=Mock(return_value=S_OK("ddsiming.sh")))
  @patch("%s.DDSimAnalysis._getDetectorXML" % MODULE_NAME, new=Mock(return_value=S_OK("myDet.xml")))
  @patch("%s.shellCall" % MODULE_NAME, new=Mock(return_value=S_OK((0, "AllGood"))))
  @patch("%s.getSteeringFileDirName" % MODULE_NAME, new=Mock(return_value=S_OK("SteerFold")))
  def test_DDSim_runIt_success_Debug(self):
    """DDSim.runit success with startFrom..........................................................."""
    self.ddsim.platform = "Windows"
    self.ddsim.applicationLog = self.logFileName
    self.ddsim.SteeringFile = "mySteering.py"
    self.ddsim.NumberOfEvents = 123
    self.ddsim.debug = True
    # side effect for Steering1a, Steering1b, Steering2, Script, userlibs, log, logAfter
    with patch("os.path.exists", new=Mock(side_effect=[False, True, True, False, False, False, True])):
      res = self.ddsim.runIt()
    assertDiracSucceeds(res, self)
    self.assertIn(" --printLevel DEBUG ", self.ddsim.extraCLIarguments)

  ########################
  # Test extra particles #
  @patch("%s.getEnvironmentScript" % MODULE_NAME, new=Mock(return_value=S_OK("ddsiming.sh")))
  @patch("%s.DDSimAnalysis._getDetectorXML" % MODULE_NAME, new=Mock(return_value=S_OK("myDet.xml")))
  @patch("%s.shellCall" % MODULE_NAME, new=Mock(return_value=S_OK((0, "AllGood"))))
  @patch("%s.getSteeringFileDirName" % MODULE_NAME, new=Mock(return_value=S_OK("SteerFold")))
  @patch("%s.DDSimAnalysis.createParticleTable" % MODULE_NAME, new=Mock(return_value=S_OK(["test"])))
  @patch("%s.DDSimAnalysis.resolveDDSimOptions" % MODULE_NAME, new=Mock(return_value=S_OK(["test"])))
  def test_DDSim_runIt_success_extraParticles(self):
    """DDSim.runit success with extra particles....................................................."""
    self.ddsim.platform = "Windows"
    self.ddsim.applicationLog = self.logFileName
    self.ddsim.SteeringFile = "mySteering2.py"
    self.ddsim.NumberOfEvents = 123
    self.ddsim.extraParticles = [[25, "Maribor", 2., 1500., 10., 100.]]
    # side effect for Steering1a, Steering1b, Steering2, Script, userlibs, log, logAfter
    with patch("os.path.exists", new=Mock(side_effect=[False, True, True, False, False, False, True])):
      res = self.ddsim.runIt()
    assertDiracSucceeds(res, self)
    self.assertIn("--physics.pdgfile particle.tbl", self.ddsim.extraCLIarguments)

  ###################
  # Test OutputFile #
  ###################
  @patch("%s.getEnvironmentScript" % MODULE_NAME, new=Mock(return_value=S_OK("ddsiming.sh")))
  @patch("%s.DDSimAnalysis._getDetectorXML" % MODULE_NAME, new=Mock(return_value=S_OK("myDet.xml")))
  @patch("%s.shellCall" % MODULE_NAME, new=Mock(return_value=S_OK((0, "AllGood"))))
  @patch("%s.getSteeringFileDirName" % MODULE_NAME, new=Mock(return_value=S_OK("SteerFold")))
  def test_DDSim_runIt_success_OutputFile_1(self):
    """DDSim.runit success with OutputFile set......................................................"""
    self.ddsim.platform = "Windows"
    self.ddsim.applicationLog = self.logFileName
    self.ddsim.SteeringFile = "mySteering.py"
    self.ddsim.OutputFile = "grailDiary.root"
    # side effect for Steering1a, Steering1b, Steering2, Script, userlibs, log, logAfter
    with patch("os.path.exists", new=Mock(side_effect=[False, True, True, False, False, False, True])):
      res = self.ddsim.runIt()
    assertDiracSucceeds(res, self)
    self.assertIn(" --outputFile grailDiary.root ", self.ddsim.extraCLIarguments)

  def test_DDSim_runIt_fail_1(self):
    """DDSim.runit failure platform................................................................."""
    self.ddsim.applicationLog = self.logFileName
    res = self.ddsim.runIt()
    self.assertEqual(res['Message'], 'No ILC platform selected')

  def test_DDSim_runIt_fail_2(self):
    """DDSim.runit failure log......................................................................"""
    self.ddsim.platform = "Windows"
    res = self.ddsim.runIt()
    self.assertEqual(res['Message'], 'No Log file provided')

  def test_DDSim_runIt_fail_3(self):
    """DDSim.runit failure neither.................................................................."""
    res = self.ddsim.runIt()
    self.assertEqual(res['Message'], 'No ILC platform selected')

  def test_DDSim_runIt_fail_4(self):
    """DDSim.runit fail steps......................................................................."""
    self.ddsim.platform = "Windows"
    self.ddsim.applicationLog = self.logFileName
    self.ddsim.workflowStatus = S_ERROR("Failed earlier")
    res = self.ddsim.runIt()
    self.assertEqual(res['Value'], "DDSim should not proceed as previous step did not end properly")

  @patch("%s.getEnvironmentScript" % MODULE_NAME, new=Mock(return_value=S_ERROR("missing ddsiming.sh")))
  def test_DDSim_runIt_fail_env(self):
    """DDSim.runit failed to get env................................................................"""
    self.ddsim.platform = "Windows"
    self.ddsim.applicationLog = self.logFileName
    res = self.ddsim.runIt()
    self.assertEqual(res['Message'], "missing ddsiming.sh")

  @patch("%s.getEnvironmentScript" % MODULE_NAME, new=Mock(return_value=S_OK("ddsiming.sh")))
  @patch("%s.DDSimAnalysis._getDetectorXML" % MODULE_NAME, new=Mock(return_value=S_ERROR("no myDet.xml")))
  def test_DDSim_runIt_fail_xml(self):
    """DDSim.runit failed to get xml................................................................"""
    self.ddsim.platform = "Windows"
    self.ddsim.applicationLog = self.logFileName
    res = self.ddsim.runIt()
    self.assertEqual(res['Message'], "no myDet.xml")


class TestDDSimAnalysisEnv(TestDDSimAnalysis):
  """DDSim getEnvScript."""

  @patch("%s.getSoftwareFolder" % MODULE_NAME, new=Mock(return_value=S_OK("/win32")))
  def test_DDSim_getEnvScript_success(self):
    """DDSim.getEnvScript success..................................................................."""
    platform = "Windows"
    appname = "ddsim"
    appversion = "Vista"
    res = self.ddsim.getEnvScript(platform, appname, appversion)
    self.assertEqual(res['Value'], os.path.abspath("DDSimEnv.sh"))
    self.assertTrue(os.path.exists(os.path.abspath("DDSimEnv.sh")))
    with open("DDSimEnv.sh") as script:
      scriptLines = "".join(script.readlines())
      self.assertIn("declare -x DD4hepINSTALL=%s" % "/win32", scriptLines)

  @patch("%s.getSoftwareFolder" % MODULE_NAME, new=Mock(return_value=S_ERROR("no softFolder")))
  def test_DDSim_getEnvScript_noSoftFolder(self):
    """DDSim.getEnvScript fail softfolder..........................................................."""
    platform = "Windows"
    appname = "ddsim"
    appversion = "Vista"
    res = self.ddsim.getEnvScript(platform, appname, appversion)
    self.assertFalse(res['OK'])
    self.assertEqual(res['Message'], "no softFolder")

  @patch("%s.getSoftwareFolder" % MODULE_NAME, new=Mock(return_value=S_OK("/win32")))
  @patch("os.path.exists", new=Mock(return_value=True))
  def test_DDSim_getEnvScript_vars(self):
    """DDSim.getEnvScript with variables success...................................................."""

    platform = "Windows"
    appname = "ddsim"
    appversion = "Vista"
    self.ddsim.ops.getOptionsDict = Mock(return_value=S_OK(dict(KNIGHTSWORD="Ni",
                                                                    WHEN="Always",
                                                                    G4LEDATA="/dev/camelot",
                                                                   )
                                                             )
                                        )
    res = self.ddsim.getEnvScript(platform, appname, appversion)
    self.assertEqual(res['Value'], os.path.abspath("DDSimEnv.sh"))
    self.assertTrue(os.path.exists(os.path.abspath("DDSimEnv.sh")))
    with open("DDSimEnv.sh") as script:
      scriptLines = "".join(script.readlines())
      self.assertIn("declare -x KNIGHTSWORD=Ni", scriptLines)
      self.assertIn("declare -x WHEN=Always", scriptLines)
      self.assertIn("declare -x G4LEDATA=/dev/camelot", scriptLines)
      self.assertNotIn("declare -x G4LEDATA=$(ls -d $G4DATA/", scriptLines)
      self.assertIn("declare -x G4LEVELGAMMADATA=$(ls -d $G4DATA/", scriptLines)

  @patch("%s.getSoftwareFolder" % MODULE_NAME, new=Mock(return_value=S_OK("/win32")))
  @patch("os.path.exists", new=Mock(return_value=True))
  def test_DDSim_getEnvScript_noVars(self):
    """DDSim.getEnvScript with no additional variables.............................................."""

    platform = "Windows"
    appname = "ddsim"
    appversion = "Vista"
    self.ddsim.ops.getOptionsDict = Mock(return_value=S_ERROR("No Variables Set"))
    self.ddsim.ops.getValue = Mock(return_value=None)
    res = self.ddsim.getEnvScript(platform, appname, appversion)
    self.ddsim.ops.getValue.assert_called_once_with("/AvailableTarBalls/Windows/ddsim/Vista/InitScript", None)
    self.assertEqual(res['Value'], os.path.abspath("DDSimEnv.sh"))
    self.assertTrue(os.path.exists(os.path.abspath("DDSimEnv.sh")))
    with open("DDSimEnv.sh") as script:
      scriptLines = "".join(script.readlines())
      self.assertIn("declare -x G4LEDATA=$(ls -d $G4DATA/", scriptLines)
      self.assertNotIn("source ", scriptLines)

  @patch("%s.getSoftwareFolder" % MODULE_NAME, new=Mock(return_value=S_OK("/win32")))
  @patch("%s.getNewLDLibs" % MODULE_NAME, new=Mock(return_value=""))
  def test_DDSim_getEnvScript_init(self):
    """DDSim.getEnvScript with initscript..........................................................."""
    platform = "Windows"
    appname = "ddsim"
    appversion = "Vista"
    self.ddsim.ops.getOptionsDict = Mock(return_value=S_OK(dict(KNIGHTSWORK="Ni",
                                                                    WHEN="Always"
                                                                   )
                                                             )
                                        )
    self.ddsim.ops.getValue = Mock(return_value="/cvmfs/initthisfile.sh")
    with patch("os.path.exists", new=Mock(return_value=True)):
      res = self.ddsim.getEnvScript(platform, appname, appversion)
    self.ddsim.ops.getValue.assert_called_once_with("/AvailableTarBalls/Windows/ddsim/Vista/InitScript", None)
    self.assertEqual(res['Value'], os.path.abspath("DDSimEnv.sh"))
    self.assertTrue(os.path.exists(os.path.abspath("DDSimEnv.sh")))
    with open("DDSimEnv.sh") as script:
      scriptLines = "".join(script.readlines())
      self.assertIn("source /cvmfs/initthisfile.sh", scriptLines)


class TestDDSimAnalysisASI(TestDDSimAnalysis):
  """DDSim.ApplicationSpecificInputs."""

  @patch.dict(os.environ, {"JOBID": "12345"})
  def test_DDSim_ASI_NoVariables(self):
    """DDSim.applicationSpecificInputs: checks that no variables have been set after this call......"""
    gLogger.setLevel("ERROR")
    self.ddsim.workflow_commons = dict()
    self.ddsim.applicationSpecificInputs()
    self.assertFalse(self.ddsim.jobReport or self.ddsim.productionID)

  @patch.dict(os.environ, {"JOBID": "12345"})
  def test_DDSim_ASI_StartFrom(self):
    """DDSim.applicationSpecificInputs: check setting of startfrom variable........................."""
    gLogger.setLevel("ERROR")
    self.ddsim.workflow_commons = dict(StartFrom=321)
    self.ddsim.resolveInputVariables()
    self.ddsim.applicationSpecificInputs()
    self.assertEqual(self.ddsim.startFrom, 321)

  @patch.dict(os.environ, {"JOBID": "12345"})
  def test_DDSim_ASI_RandomSeed_Prod(self):
    """DDSim.applicationSpecificInputs: check setting of randomseed in production..................."""
    gLogger.setLevel("ERROR")
    self.ddsim.workflow_commons = dict(StartFrom=321, IS_PROD=True, PRODUCTION_ID=6666, JOB_ID=123)
    self.ddsim.OutputFile = 'simulation.root'
    self.ddsim.resolveInputVariables()
    self.ddsim.applicationSpecificInputs()
    self.assertEqual(self.ddsim.randomSeed, 6666123)

  @patch.dict(os.environ, {"JOBID": "12345"})
  def test_DDSim_ASI_RandomSeed_Set(self):
    """DDSim.applicationSpecificInputs: check setting of default randomseed in user jobs............"""
    gLogger.setLevel("ERROR")
    self.ddsim = DDSimAnalysis()
    self.ddsim.workflow_commons = dict()
    self.ddsim.resolveInputVariables()
    self.ddsim.applicationSpecificInputs()
    self.assertEqual(int(self.ddsim.randomSeed), 12345)

  @patch.dict(os.environ, {"JOBID": "12345"})
  def test_DDSim_ASI_RandomSeed_User(self):
    """DDSim.applicationSpecificInputs: check setting of randomseed in user jobs...................."""
    gLogger.setLevel("ERROR")
    self.ddsim = DDSimAnalysis()
    self.ddsim.randomSeed = 654321
    self.ddsim.workflow_commons = dict()
    self.ddsim.resolveInputVariables()
    self.ddsim.applicationSpecificInputs()
    self.assertEqual(int(self.ddsim.randomSeed), 654321)

  @patch.dict(os.environ, {"JOBID": "12345"})
  def test_DDSim_ASI_RandomSeed_User_Zero(self):
    """DDSim.applicationSpecificInputs: check setting of randomseed to zero in user jobs............"""
    gLogger.setLevel("ERROR")
    self.ddsim = DDSimAnalysis()
    self.ddsim.randomSeed = 0
    self.ddsim.workflow_commons = dict()
    self.ddsim.resolveInputVariables()
    self.ddsim.applicationSpecificInputs()
    self.assertEqual(int(self.ddsim.randomSeed), 0)

  @patch.dict(os.environ, {"JOBID": "12345"})
  def test_DDSim_ASI_InputFiles(self):
    """DDSim.applicationSpecificInputs: check setting inputData....................................."""
    gLogger.setLevel("ERROR")
    self.ddsim = DDSimAnalysis()
    self.ddsim.InputData = ["myslcio.slcio", "mystdhep.HEPEvt", "my.notforsimulation"]
    self.ddsim.workflow_commons = dict()
    self.ddsim.resolveInputVariables()
    self.ddsim.applicationSpecificInputs()
    self.assertEqual(self.ddsim.InputFile, ["myslcio.slcio", "mystdhep.HEPEvt"])


class TestDDSimAnalysisDetXMLCS(TestDDSimAnalysis):
  """tests for _getDetectorXML."""

  @patch("%s.getEnvironmentScript" % DD4H_NAME, new=Mock(return_value=S_OK("ddsiming.sh")))
  @patch("%s.shellCall" % DD4H_NAME, new=Mock(return_value={'OK': True, 'Value': (0, '/cvmfs/sw.hsf.org/spackages7/lcgeo/0.18/x86_64-centos7-gcc11.2.0-opt/6ciib/share/lcgeo/compact\n', '')}))
  def test_DDSim_getDetectorXML(self):
    """DDSim.getDetectorXML from CS................................................................."""
    gLogger.setLevel("ERROR")
    xmlPath = "/cvmfs/sw.hsf.org/spackages7/lcgeo/0.18/x86_64-centos7-gcc11.2.0-opt/6ciib/share/lcgeo/compact/CLIC/compact/CLIC_o3_v14/CLIC_o3_v14.xml"
    self.ddsim.detectorModel = "CLIC_o3_v14"
    self.ddsim.ops.getOptionsDict = Mock(return_value=S_OK(dict(CLIC_o3_v14=xmlPath)))
    self.ddsim.ops.getValue = Mock(return_value='LCGEO')
    self.ddsim.workflow_commons = dict()
    res = self.ddsim._getDetectorXML()
    self.assertEqual(res['Value'], "/cvmfs/sw.hsf.org/spackages7/lcgeo/0.18/x86_64-centos7-gcc11.2.0-opt/6ciib/share/lcgeo/compact/CLIC/compact/CLIC_o3_v14/CLIC_o3_v14.xml")

  @patch("%s.getEnvironmentScript" % DD4H_NAME, new=Mock(return_value=S_OK("ddsiming.sh")))
  @patch("%s.shellCall" % DD4H_NAME, new=Mock(return_value={'OK': True, 'Value': (0, '/cvmfs/sw.hsf.org/spackages7/lcgeo/0.18/x86_64-centos7-gcc11.2.0-opt/6ciib/share/lcgeo/compact\n', '')}))
  def test_DDSim_getDetectorXML_relPatg(self):
    """DDSim.getDetectorXML from CS with relative path.............................................."""
    gLogger.setLevel("ERROR")
    xmlPath = "CLIC/compact/CLIC_o3_v14/CLIC_o3_v14.xml"
    self.ddsim.detectorModel = "CLIC_o3_v14"
    self.ddsim.ops.getOptionsDict = Mock(return_value=S_OK(dict(CLIC_o3_v14=xmlPath)))
    self.ddsim.ops.getValue = Mock(return_value='LCGEO')
    self.ddsim.workflow_commons = dict()
    res = self.ddsim._getDetectorXML()
    self.assertEqual(res['Value'], "/cvmfs/sw.hsf.org/spackages7/lcgeo/0.18/x86_64-centos7-gcc11.2.0-opt/6ciib/share/lcgeo/compact/CLIC/compact/CLIC_o3_v14/CLIC_o3_v14.xml")

  @patch("%s.getEnvironmentScript" % DD4H_NAME, new=Mock(return_value=S_OK("ddsiming.sh")))
  @patch("%s.getSoftwareFolder" % DD4H_NAME, new=Mock(return_value=S_OK("/win32")))
  def test_DDSim_getDetectorXML_oldRelPatg(self):
    """DDSim.getDetectorXML from CS with relative path.............................................."""
    gLogger.setLevel("ERROR")
    xmlPath = "detectors/ILD_o1_v05/ILD_o1_v05.xml"
    self.ddsim.detectorModel = "ILD_o1_v05"
    self.ddsim.ops.getOptionsDict = Mock(return_value=S_OK(dict(ILD_o1_v05=xmlPath)))
    self.ddsim.ops.getValue = Mock(return_value=None)
    self.ddsim.workflow_commons = dict()
    res = self.ddsim._getDetectorXML()
    self.assertEqual(res['Value'], "/win32/detectors/ILD_o1_v05/ILD_o1_v05.xml")

  @patch("%s.getEnvironmentScript" % DD4H_NAME, new=Mock(return_value=S_OK("ddsiming.sh")))
  @patch("%s.shellCall" % DD4H_NAME, new=Mock(return_value={'OK': True, 'Value': (0, '/cvmfs/sw.hsf.org/spackages7/lcgeo/0.18/x86_64-centos7-gcc11.2.0-opt/6ciib/share/lcgeo/compact\n', '')}))
  def test_DDSim_getDetectorXML_Fail(self):
    """DDSim.getDetectorXML Failure................................................................."""
    gLogger.setLevel("ERROR")
    xmlPath = "/cvmfs/sw.hsf.org/spackages7/lcgeo/0.18/x86_64-centos7-gcc11.2.0-opt/6ciib/share/lcgeo/compact/CLIC/compact/CLIC_o3_v14/CLIC_o3_v14.xml"
    self.ddsim.detectorModel = "CLIC_o3_v1412345_unexistent"
    self.ddsim.ops.getOptionsDict = Mock(return_value=S_OK(dict(CLIC_o3_v14=xmlPath)))
    self.ddsim.ops.getValue = Mock(return_value='LCGEO')
    self.ddsim.workflow_commons = dict()
    res = self.ddsim._getDetectorXML()
    self.assertFalse(res['OK'])
    self.assertEqual(res['Message'], "Detector model was not found")

  def test_DDSim_getDetectorXML_NoDetModels(self):
    """DDSim.getDetectorXML Error no detectorModels................................................."""
    gLogger.setLevel("ERROR")
    self.ddsim.detectorModel = "camelot"
    self.ddsim.ops.getOptionsDict = Mock(return_value=S_ERROR("Nothing to see"))
    self.ddsim.workflow_commons = dict()
    res = self.ddsim._getDetectorXML()
    self.assertEqual(res['Message'], "Failed to get list of DetectorModels from the ConfigSystem")

  @patch("os.path.exists", new=Mock(return_value=True))
  @patch("%s.unzip_file_into_dir" % DD4H_NAME, new=Mock())
  def test_DDSim_getDetectorXML_CustomWithOfficialName(self):
    """DDSim.getDetectorXML CustomTarball with official name........................................"""
    gLogger.setLevel("ERROR")
    self.ddsim.detectorModel = "Camelot"
    self.ddsim.ops.getOptionsDict = Mock(return_value=S_OK({"Camelot": "/path/to/camelot.xml"}))
    self.ddsim.workflow_commons = dict()
    # only works for python 2
    with patch('%s.open' % BUILTIN_NAME, mock_open(read_data="RoundTable")):
      res = self.ddsim._getDetectorXML()
    print(res)
    self.assertEqual(res['Value'], os.path.join("Camelot", "Camelot.xml"))


class TestDDSimAnalysisDetXMLTar(TestDDSimAnalysis):
  """tests for _getDetectorXML."""

  def setUp(self):
    super(TestDDSimAnalysisDetXMLTar, self).setUp()
    self.ddsim.detectorModel = "myDet"
    outputFilename = self.ddsim.detectorModel + ".tar.gz"
    os.makedirs(self.ddsim.detectorModel)
    xmlPath = os.path.join(self.ddsim.detectorModel, self.ddsim.detectorModel + ".xml")
    with open(xmlPath, "w") as xml:
      xml.write("myDet is awesome")
    with tarfile.open(outputFilename, "w:gz") as tar:
      tar.add(xmlPath)
    cleanup(self.ddsim.detectorModel)

  @patch("%s.getSoftwareFolder" % MODULE_NAME, new=Mock(return_value=S_OK("/win32")))
  def test_DDSim_getDetectorXML_Local_TarGZ(self):
    """DDSim.getDetectorXML with local tar.gz......................................................."""
    gLogger.setLevel("ERROR")
    self.ddsim.detectorModel = "myDet"
    self.ddsim.ops.getOptionsDict = Mock(return_value=S_OK(dict(camelot="/dev/null")))
    self.ddsim.workflow_commons = dict()
    res = self.ddsim._getDetectorXML()
    gLogger.error(" res ", res)
    expectedPath = os.path.join(os.getcwd(), self.ddsim.detectorModel, self.ddsim.detectorModel + ".xml")
    self.assertEqual(res['Value'], expectedPath)
    self.assertTrue(os.path.exists(expectedPath))

  @patch("%s.getSoftwareFolder" % MODULE_NAME, new=Mock(return_value=S_OK("/win32")))
  def test_DDSim_getDetectorXML_Local_TarGZ_2(self):
    """DDSim.getDetectorXML with local tar.gz run twice............................................."""
    gLogger.setLevel("ERROR")
    self.ddsim.detectorModel = "myDet"
    self.ddsim.ops.getOptionsDict = Mock(return_value=S_OK(dict(camelot="/dev/null")))
    self.ddsim.workflow_commons = dict()
    res = self.ddsim._extractTar()
    res = self.ddsim._extractTar()
    gLogger.error(" res ", res)
    expectedPath = os.path.join(os.getcwd(), self.ddsim.detectorModel, self.ddsim.detectorModel + ".xml")
    self.assertEqual(res['Value'], expectedPath)
    self.assertTrue(os.path.exists(expectedPath))

  def test_DDSim_extractTar_Raise(self):
    """DDSim._extractTar raised exception..........................................................."""
    gLogger.setLevel("ERROR")
    self.ddsim.detectorModel = "myDet"
    self.ddsim.ops.getOptionsDict = Mock(return_value=S_OK(dict(camelot="/dev/null")))
    self.ddsim.workflow_commons = dict()
    with patch("tarfile.open", side_effect=RuntimeError("This is what happens")):
      res = self.ddsim._extractTar()
    self.assertFalse(res['OK'])
    self.assertEqual(res['Message'], "Failed to untar detector model")

  @patch("%s.getSoftwareFolder" % MODULE_NAME, new=Mock(return_value=S_OK("/win32")))
  def test_DDSim_getDetectorXML_Local_TGZ_2(self):
    """DDSim.getDetectorXML with local tgz.........................................................."""
    gLogger.setLevel("ERROR")
    self.ddsim.detectorModel = "myDet"
    self.ddsim.ops.getOptionsDict = Mock(return_value=S_OK(dict(camelot="/dev/null")))
    self.ddsim.workflow_commons = dict()
    os.rename("myDet.tar.gz", "myDet.tgz")
    res = self.ddsim._getDetectorXML()
    gLogger.error(" res ", res)
    expectedPath = os.path.join(os.getcwd(), self.ddsim.detectorModel, self.ddsim.detectorModel + ".xml")
    self.assertEqual(res['Value'], expectedPath)
    self.assertTrue(os.path.exists(expectedPath))


class TestDDSimAnalysisDetXMLZip(TestDDSimAnalysis):
  """tests for _getDetectorXML when a zip file exists."""

  def setUp(self):
    super(TestDDSimAnalysisDetXMLZip, self).setUp()
    self.ddsim.detectorModel = "myDet"
    outputFilename = self.ddsim.detectorModel + ".zip"
    os.makedirs(self.ddsim.detectorModel)
    xmlPath = os.path.join(self.ddsim.detectorModel, self.ddsim.detectorModel + ".xml")
    with open(xmlPath, "w") as xml:
      xml.write("myDet is awesome")
    with ZipFile(outputFilename, "w") as zipF:
      zipF.write(xmlPath)
    cleanup(self.ddsim.detectorModel)

  @patch("%s.getSoftwareFolder" % MODULE_NAME, new=Mock(return_value=S_OK("/win32")))
  def test_DDSim_getDetectorXML_Local_Zip(self):
    """DDSim.getDetectorXML with local zip.........................................................."""
    gLogger.setLevel("ERROR")
    self.ddsim.detectorModel = "myDet"
    self.ddsim.ops.getOptionsDict = Mock(return_value=S_OK(dict(camelot="/dev/null")))
    self.ddsim.workflow_commons = dict()
    res = self.ddsim._getDetectorXML()
    gLogger.error(" res ", res)
    expectedPath = os.path.join(os.getcwd(), self.ddsim.detectorModel, self.ddsim.detectorModel + ".xml")
    self.assertEqual(res['Value'], expectedPath)
    self.assertTrue(os.path.exists(expectedPath))

  @patch("%s.getSoftwareFolder" % MODULE_NAME, new=Mock(return_value=S_OK("/win32")))
  def test_DDSim_getDetectorXML_Local_Zip_2(self):
    """DDSim.getDetectorXML with local zip run twice................................................"""
    gLogger.setLevel("ERROR")
    self.ddsim.detectorModel = "myDet"
    self.ddsim.ops.getOptionsDict = Mock(return_value=S_OK(dict(camelot="/dev/null")))
    self.ddsim.workflow_commons = dict()
    res = self.ddsim._extractZip()
    res = self.ddsim._extractZip()
    gLogger.error(" res ", res)
    expectedPath = os.path.join(os.getcwd(), self.ddsim.detectorModel, self.ddsim.detectorModel + ".xml")
    self.assertEqual(res['Value'], expectedPath)
    self.assertTrue(os.path.exists(expectedPath))

  def test_DDSim_extractZip_Raise(self):
    """DDSim._extractZip raised exception..........................................................."""
    gLogger.setLevel("ERROR")
    self.ddsim.detectorModel = "myDet"
    self.ddsim.ops.getOptionsDict = Mock(return_value=S_OK(dict(camelot="/dev/null")))
    self.ddsim.workflow_commons = dict()
    # myDet.zip does not exist
    os.remove("myDet.zip")
    res = self.ddsim._extractZip()
    self.assertFalse(res['OK'])
    self.assertEqual(res['Message'], "Failed to unzip detector model")


def runTests():
  """Runs our tests."""
  suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestDDSimAnalysis)
  suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestDDSimAnalysisParticleTable))
  suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestDDSimAnalysisRunit))
  suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestDDSimAnalysisDetXMLTar))
  suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestDDSimAnalysisDetXMLZip))
  suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestDDSimAnalysisDetXMLCS))
  suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestDDSimAnalysisEnv))
  suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestDDSimAnalysisASI))

  testResult = unittest.TextTestRunner(verbosity=2).run(suite)
  print(testResult)


if __name__ == '__main__':
  runTests()
