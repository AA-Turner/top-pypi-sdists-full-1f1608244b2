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
"""Tests for the Fcc module."""

from __future__ import absolute_import
import inspect
import os
import unittest
from mock import patch, MagicMock as Mock
import six

from DIRAC import S_OK, S_ERROR
from ILCDIRAC.Interfaces.API.NewInterface.Applications import FccSw, FccAnalysis

from Tests.Utilities.GeneralUtils import assertEqualsImproved, assertDiracFailsWith, \
    assertDiracSucceeds, assertDiracSucceedsWith

__RCSID__ = "$Id$"

MODULE_NAME = 'ILCDIRAC.Interfaces.API.NewInterface.Applications.Fcc'
BUILTIN_NAME = 'builtins' if six.PY3 else '__builtin__'

# pylint: disable=protected-access, too-many-public-methods, missing-docstring


class FccMixin(object):
  """Base class for the Fcc test cases."""

  def setUp(self):
    """set up the objects."""

    def replace_realpath(path):
      return os.path.join("/test/realpath", path)

    self.patches = [patch("os.getcwd", new=Mock(return_value="/test/curdir")),
                    patch("os.path.dirname", new=Mock(return_value="/test/dirname")),
                    patch("os.path.realpath", new=Mock(side_effect=replace_realpath)),
                    ]

    for patcher in self.patches:
      patcher.start()

    self.fcc = None
    self.log_mock = Mock()

  def tearDown(self):
    for patcher in self.patches:
      patcher.stop()
    del self.fcc

  def test_userjobmodules(self):
    module_mock = Mock()
    assertDiracSucceeds(self.fcc._userjobmodules(module_mock), self)

  def test_prodjobmodules(self):
    module_mock = Mock()
    assertDiracSucceeds(self.fcc._prodjobmodules(module_mock), self)

  def test_prodjobmodules_outputpath(self):
    module_mock = Mock()
    self.fcc.outputPath = 'aef'
    assertDiracSucceeds(self.fcc._prodjobmodules(module_mock), self)
    self.assertIn({'OutputFile': '@{OutputFile}', 'outputPath': '@{OutputPath}',
                     'outputDataSE': '@{OutputSE}'}, self.fcc._listofoutput)

  def test_userjobmodules_fails(self):
    with patch('%s._setUserJobFinalization' % MODULE_NAME, new=Mock(return_value=S_OK('something'))),\
        patch('%s._setApplicationModuleAndParameters' % MODULE_NAME, new=Mock(return_value=S_ERROR('some_test_err'))):
      assertDiracFailsWith(self.fcc._userjobmodules(None),
                            'userjobmodules failed', self)

  def test_prodjobmodules_fails(self):
    with patch('%s._setApplicationModuleAndParameters' % MODULE_NAME, new=Mock(return_value=S_OK('something'))), \
        patch('%s._setOutputComputeDataList' % MODULE_NAME, new=Mock(return_value=S_ERROR('some_other_test_err'))):
      assertDiracFailsWith(self.fcc._prodjobmodules(None),
                            'prodjobmodules failed', self)

  def test_checkwfconsistency(self):
    assertDiracSucceeds(self.fcc._checkWorkflowConsistency(), self)

  def test_resolveparameters(self):
    step_mock = Mock()
    assertDiracSucceeds(self.fcc._resolveLinkedStepParameters(step_mock()), self)

  def test_resolveparameters_setlink(self):
    step_mock = Mock()
    self.fcc._linkedidx = 1
    self.fcc._jobsteps = [None, Mock()]
    assertDiracSucceeds(self.fcc._resolveLinkedStepParameters(step_mock()), self)

  @patch("os.listdir", new=Mock(return_value=[]))
  @patch("os.path.exists", new=Mock(return_value=True))
  def test_checkconsistency(self):
    with patch.object(self.fcc, '_importToSandbox', new=Mock(return_value=True)), \
        patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):

      info_message = ("Application general consistency : _checkConsistency()"
                      " on '%(name)s' successfull" % {'name': self.fcc.appname}
                      )
      assertDiracSucceedsWith(self.fcc._checkConsistency(), info_message, self)
      self.log_mock.info.assert_called_with(info_message)
      self.log_mock.info.assert_any_call("Sandboxing : Sandboxing successfull")

  @patch("os.listdir", new=Mock(return_value=[]))
  @patch("os.path.exists", new=Mock(return_value=True))
  def test_checkconsistency_noversion(self):
    self.fcc.version = None
    error_message = 'Version not set!'
    with patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):
      assertDiracFailsWith(self.fcc._checkConsistency(), error_message, self)
    self.log_mock.error.assert_called_once_with(error_message)

  @patch("os.path.exists", new=Mock(return_value=True))
  def test_checkconsistency_noexecutable(self):
    self.fcc.fccExecutable = None
    error_message = (
        "Consistency : Error in parsing '%(name)s' application :\n"
        "You have to provide at least an executable"
        " and a configuration file for each application" % {'name': self.fcc.appname}
        )
    with patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):
      assertDiracFailsWith(self.fcc._checkConsistency(), error_message, self)
    self.log_mock.error.assert_called_once_with(error_message)

  @patch("os.listdir", new=Mock(return_value=[]))
  @patch("os.path.exists", new=Mock(return_value=True))
  def test_checkconsistency_no_cfgfile(self):
    self.fcc.steeringFile = None
    error_message = (
        "Consistency : Error in parsing '%(name)s' application :\n"
        "You have to provide at least an executable"
        " and a configuration file for each application" % {'name': self.fcc.appname}
        )
    with patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):
      assertDiracFailsWith(self.fcc._checkConsistency(), error_message, self)
    self.log_mock.error.assert_called_once_with(error_message)

  @patch("os.listdir", new=Mock(return_value=[]))
  @patch("os.path.exists", new=Mock(return_value=True))
  def test_checkconsistency_many_cfgfiles(self):
    self.fcc.steeringFile = ["/path/to/cfgFile1", "/path/to/cfgFile2"]
    error_message = (
        "Consistency : Fcc Application accepts only one input configuration file:\n"
        "If you want to run the application '%(name)s' with many configurations then\n"
        "Create an new application with the other configuration\n"
        "You can also use the 'getInputFromApp' method to link applications" % {'name': self.fcc.appname}
        )
    with patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):
      assertDiracFailsWith(self.fcc._checkConsistency(), error_message, self)
    self.log_mock.error.assert_called_once_with(error_message)

  def test_checkfinalconsistency_outputfile(self):
    self.fcc.logFile = "logFile"
    self.fcc.outputFile = "output.root"

    self.fcc._checkFinalConsistency()
    self.assertIn(self.fcc.logFile, self.fcc._outputSandbox)
    self.assertIn("output(_JobID).root (Name of the eventual output root file)", self.fcc._outputSandbox)

  # During release v0.8.1 of FCCSW, 'Application.setOutputFile' does not accept list
  def test_checkfinalconsistency_outputfiles(self):
    self.fcc.logFile = "logFile"
    self.fcc.outputFile = ["output1.root", "output2.root"]

    self.fcc._checkFinalConsistency()
    self.assertIn(self.fcc.logFile, self.fcc._outputSandbox)
    self.assertIn("output1(_JobID).root (Name of the eventual output root file)", self.fcc._outputSandbox)
    self.assertIn("output2(_JobID).root (Name of the eventual output root file)", self.fcc._outputSandbox)

  def test_importfiles_no_sandbox(self):
    self.fcc._tempInputSandbox = None
    with patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):
      self.assertTrue(self.fcc._importFiles())
    self.log_mock.warn.assert_called_once_with("Sandboxing : Your application has an empty input sandbox")

  @patch("%s._findPath" % MODULE_NAME, new=Mock(return_value=('sandboxFile1', False)))
  def test_importfiles_findpath_failed(self):
    self.fcc._tempInputSandbox = ['sandboxFile1']
    with patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):
      self.assertFalse(self.fcc._importFiles())
    error_message = (
        "Sandboxing : The path 'sandboxFile1' does not exist\n"
        "Please ensure that your path exists in an accessible file system "
        "(AFS or CVMFS)"
        )
    self.log_mock.error.assert_called_once_with(error_message)

  @patch("%s._findPath" % MODULE_NAME, new=Mock(return_value=('/afs/sandboxFile1', True)))
  def test_importfiles_afs_warn_check(self):
    self.fcc._tempInputSandbox = ['/afs/sandboxFile1']
    with patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):
      self.assertTrue(self.fcc._importFiles())
    warn_message = (
        "Sandboxing : You plan to upload '/afs/sandboxFile1'"
        " which is stored on AFS\n"
        "STORING FILES ON AFS IS DEPRECATED"
        )

    self.assertIn('/afs/sandboxFile1', self.fcc._inputSandbox)
    self.log_mock.warn.assert_called_once_with(warn_message)

    debug_message = (
        "Sandboxing : The path '/afs/sandboxFile1' required by the application"
        " has been added to te sandbox"
        )
    self.log_mock.debug.assert_any_call(debug_message)

    debug_message = (
        "Sandboxing : Files required by FCC application"
        " verified and added successfully to the sandbox"
        )
    self.log_mock.debug.assert_called_with(debug_message)

  def test_readfromfile(self):
    with patch('%s.open' % BUILTIN_NAME) as mock_open:
      manager = mock_open.return_value.__enter__.return_value
      manager.read.return_value = 'some data'
      content, message = self.fcc._readFromFile("/my/file/to/read")
      assertEqualsImproved(content, 'some data', self)
      mock_open.assert_called_with("/my/file/to/read", 'r')
      assertEqualsImproved(message, 'Sandboxing : FCC file reading successfull', self)

  @patch('%s.open' % BUILTIN_NAME, new=Mock(side_effect=IOError("ioerror")))
  def test_readfromfile_failed(self):
    content, message = self.fcc._readFromFile("/my/file/to/read")
    assertEqualsImproved(None, content, self)
    assertEqualsImproved('Sandboxing : FCC file reading failed\nioerror', message, self)

  @patch("os.listdir", new=Mock(return_value=[]))
  @patch('os.path.exists', new=Mock(return_value=True))
  @patch("%s._importToSandbox" % MODULE_NAME, new=Mock(return_value=False))
  def test_checkconsistency_importtosandbox_failed(self):
    assertDiracFailsWith(self.fcc._checkConsistency(), "_importToSandbox() failed", self)

  @patch('os.path.exists', new=Mock(return_value=True))
  def test_findPath(self):
    filename = '/path/to/file'
    assertEqualsImproved(self.fcc._findPath(filename), (filename, True), self)

  @patch('os.path.exists', new=Mock(return_value=False))
  def test_findPath_failed(self):
    filename = '/path/to/file'
    assertEqualsImproved(self.fcc._findPath(filename), (filename, False), self)


class FccSwTestCase(FccMixin, unittest.TestCase):
  """Tests for FccSw."""

  def setUp(self):
    super(FccSwTestCase, self).setUp()

    fcc_conf_file = '/build/YOUR_USERNAME/FCC/FCCSW/Examples/options/geant_fullsim_field.py'
    fccsw_path = '/build/YOUR_USERNAME/FCC/FCCSW'

    fccsw = FccSw(
        fccConfFile=fcc_conf_file,
        fccSwPath=fccsw_path
        )

    self.fcc = fccsw
    self.fcc._log = self.log_mock

  def test_checkconsistency_noexecutable(self):
    # NOTHING TO DO
    pass

  def test_checkconsistency_nofccswpath(self):
    self.fcc.fccSwPath = None
    error_message = (
        "FCCSW specific consistency : Error in parsing FCCSW application :\n"
        "You have to provide a valid path of the FCCSW installation"
        )
    with patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):
      assertDiracFailsWith(self.fcc._checkConsistency(), error_message, self)
    self.log_mock.error.assert_called_once_with(error_message)

  @patch('os.path.exists', new=Mock(return_value=False))
  def test_checkconsistency_exists_failed(self):
    error_message = (
        "FCCSW specific consistency : Error in parsing FCCSW application :\n"
        "You have to provide a valid path of the FCCSW installation"
        )
    with patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):
      assertDiracFailsWith(self.fcc._checkConsistency(), error_message, self)
    self.log_mock.error.assert_called_once_with(error_message)

  def test_checkconsistency_makedirs_failed(self):
    exists_dict = {self.fcc.fccSwPath: True, self.fcc._tempCwd: False}

    def replace_exists(path):
      return exists_dict[path]

    with patch('os.path.exists') as mock_exists, \
         patch('os.makedirs') as mock_makedirs, \
         patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):

      mock_exists.side_effect = replace_exists
      # Throw OS error
      mock_makedirs.side_effect = OSError("oserror")

      error_message = "FCCSW specific consistency : Creation of 'temp_fcc_dirac' folder failed\noserror"
      assertDiracFailsWith(self.fcc._checkConsistency(), error_message, self)
      self.log_mock.error.assert_called_once_with(error_message)
      mock_makedirs.assert_called_once_with(self.fcc._tempCwd)

  def test_checkconsistency_run_read(self):

    file_content = (
        '#!/bin/sh\n'
        'exec  /cvmfs/sft.cern.ch/lcg/views/LCG_88/x86_64-slc6-gcc49-opt/bin/python'
        ' /cvmfs/fcc.cern.ch/sw/0.8/gaudi/v28r2/x86_64-slc6-gcc49-opt/scripts/xenv '
        '--xml /afs/cern.ch/user/s/sfernana/FCC/FCCSW/build.x86_64-slc6-gcc49-opt/config/FCCSW-build.xenv "$@"\n'
        )

    build_folder = 'build.x86_64-slc6-gcc49-opt'
    build_path = os.path.join(self.fcc.fccSwPath, build_folder)
    executable_path = os.path.join(build_path, 'run')

    info_message = (
        "Application general consistency : _checkConsistency()"
        " on '%(name)s' successfull" % {'name': self.fcc.appname}
        )

    read_message = 'Sandboxing : FCC file reading successfull'

    with patch('os.path.exists') as mock_exists, \
         patch('os.listdir') as mock_listdir, \
         patch('os.path.isfile') as mock_isfile, \
         patch("%s._checkConsistency" % MODULE_NAME) as mock_check, \
         patch("%s._readFromFile" % MODULE_NAME) as mock_read, \
         patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):

      mock_exists.return_value = True
      mock_listdir.return_value = [build_folder]
      mock_isfile.return_value = False
      mock_read.return_value = (file_content, read_message)
      mock_check.return_value = S_OK(info_message)

      assertDiracSucceedsWith(self.fcc._checkConsistency(), info_message, self)
      self.log_mock.debug.assert_any_call(
          "FCCSW specific consistency : The temporary folder 'temp_fcc_dirac' already exists")
      mock_listdir.assert_called_once_with(self.fcc.fccSwPath)
      mock_isfile.assert_called_once_with(build_path)
      mock_exists.assert_any_call(executable_path)
      mock_read.assert_called_once_with(executable_path)
      self.log_mock.debug.assert_any_call(read_message)

  def test_checkconsistency_run_read_failed(self):

    build_folder = 'build.x86_64-slc6-gcc49-opt'
    build_path = os.path.join(self.fcc.fccSwPath, build_folder)
    executable_path = os.path.join(build_path, 'run')

    info_message = (
        "Application general consistency : _checkConsistency()"
        " on '%(name)s' successfull" % {'name': self.fcc.appname}
        )

    with patch('os.path.exists') as mock_exists, \
         patch('os.listdir') as mock_listdir, \
         patch('os.path.isfile') as mock_isfile, \
         patch("%s._checkConsistency" % MODULE_NAME) as mock_check, \
         patch("%s._readFromFile" % MODULE_NAME) as mock_read, \
         patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):

      mock_exists.return_value = True
      mock_listdir.return_value = [build_folder]
      mock_isfile.return_value = False
      mock_read.return_value = (None, 'DO NOT READ ME !')
      mock_check.return_value = S_OK(info_message)

      assertDiracSucceedsWith(self.fcc._checkConsistency(), info_message, self)
      self.log_mock.debug.assert_any_call(
          "FCCSW specific consistency : The temporary folder 'temp_fcc_dirac' already exists")
      mock_listdir.assert_called_once_with(self.fcc.fccSwPath)
      mock_isfile.assert_called_once_with(build_path)
      mock_exists.assert_any_call(executable_path)
      mock_read.assert_called_once_with(executable_path)
      self.log_mock.warn.assert_called_once_with('DO NOT READ ME !')
      self.log_mock.debug.assert_any_call(
          'FCCSW specific consistency : Using by default the command of the 0.8.1 release !')

  def test_resolvetreeoffiles(self):
    files = ['file1']
    source = os.path.realpath(os.path.join(self.fcc.fccSwPath, files[0]))
    destination = os.path.realpath(os.path.join(self.fcc._tempCwd, files[0]))

    tree = os.path.dirname(files[0])
    tree_full_path = os.path.join(self.fcc._tempCwd, tree)

    exists_dict = {tree_full_path: True, source: True, destination: False}

    def replace_exists(path):
      return exists_dict[path]

    with patch('os.path.exists') as mock_exists, \
         patch('shutil.copyfile') as mock_shutil, \
         patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):

      mock_exists.side_effect = replace_exists
      self.assertTrue(self.fcc._resolveTreeOfFiles(files, ".ext"))

      debug_message = "Sandboxing : Tree '%s' already exists" % tree_full_path
      self.log_mock.debug.assert_any_call(debug_message)

      debug_message = (
          "Sandboxing : Additionnal files"
          " '%(src)s' copy successfull to '%(dst)s'" % {'src': source, 'dst': destination}
          )
      self.log_mock.debug.assert_called_with(debug_message)
      mock_shutil.assert_called_once_with(source, destination)

  def test_resolvetreeoffiles_nofiles(self):
    files = []
    with patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):
      self.assertTrue(self.fcc._resolveTreeOfFiles(files, ".ext"))
    warn_message = (
        "Sandboxing : FCCSW configuration file"
        " does not seem to need any additional '.ext' files"
        )
    self.log_mock.warn.assert_called_once_with(warn_message)

  def test_resolvetreeoffiles_makedirs_failed(self):
    files = ['file1']
    source = os.path.realpath(os.path.join(self.fcc.fccSwPath, files[0]))

    tree = os.path.dirname(files[0])
    tree_full_path = os.path.join(self.fcc._tempCwd, tree)

    exists_dict = {tree_full_path: False, source: True}

    def replace_exists(path):
      return exists_dict[path]

    with patch('os.path.exists') as mock_exists, \
         patch('os.makedirs') as mock_makedirs, \
         patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):

      mock_makedirs.side_effect = OSError("oserror")
      mock_exists.side_effect = replace_exists

      self.assertFalse(self.fcc._resolveTreeOfFiles(files, ".ext"))
      error_message = (
          "Sandboxing : Tree '%(tree)s' of additionnal"
          " '.ext' files creation failed\noserror" % {'tree': tree_full_path}
          )
      self.log_mock.error.assert_called_once_with(error_message)
      mock_makedirs.assert_called_once_with(tree_full_path)

  @patch('os.path.exists', new=Mock(return_value=False))
  def test_resolvetreeoffiles_not_exists(self):
    files = ['file1']

    source = os.path.realpath(os.path.join(self.fcc.fccSwPath, files[0]))

    warn_message = (
        "Sandboxing : The file '%s' does not exist,"
        " it is not present in the FCCSW installation"
        "\nThen you should have added it manually to the input sandbox !" % {'source': source}
        )
    self.assertTrue(self.fcc._resolveTreeOfFiles(files, ".ext"))
    self.log_mock.warn(warn_message)

  def test_resolvetreeoffiles_shutil_failed(self):
    files = ['file1']

    tree = os.path.dirname(files[0])
    tree_full_path = os.path.join(self.fcc._tempCwd, tree)

    source = os.path.realpath(os.path.join(self.fcc.fccSwPath, files[0]))
    destination = os.path.realpath(os.path.join(self.fcc._tempCwd, files[0]))

    exists_dict = {source: True, tree_full_path: True, destination: False}

    def replace_exists(path):
      return exists_dict[path]

    with patch('os.path.exists') as mock_exists, \
         patch('os.makedirs'), \
         patch('shutil.copyfile') as mock_shutil, \
         patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):

      mock_exists.side_effect = replace_exists
      # throw OS error
      mock_shutil.side_effect = IOError("ioerror")

      self.assertFalse(self.fcc._resolveTreeOfFiles(files, ".ext"))

      error_message = (
          "Sandboxing : Additionnal files"
          " '%(src)s' copy failed\nioerror" % {'src': source}
          )

      self.log_mock.error.assert_called_once_with(error_message)
      mock_shutil.assert_called_once_with(source, destination)

  @patch("%s._importFiles" % MODULE_NAME, new=Mock(return_value=True))
  @patch("%s._importToSandbox" % MODULE_NAME, new=Mock(return_value=True))
  def test_importtosandbox(self):
    with patch.object(self.fcc, '_importFccswFiles', new=Mock(return_value=True)):
      self.assertTrue(self.fcc._importToSandbox())

  @patch("%s._importFiles" % MODULE_NAME, new=Mock(return_value=True))
  @patch("%s._importToSandbox" % MODULE_NAME, new=Mock(return_value=True))
  def test_importtosandbox_fccsw_files_failed(self):
    with patch.object(self.fcc, '_importFccswFiles', new=Mock(return_value=False)):
      self.assertFalse(self.fcc._importToSandbox())

  @patch("%s._importFiles" % MODULE_NAME, new=Mock(return_value=True))
  @patch("%s._importToSandbox" % MODULE_NAME, new=Mock(return_value=True))
  def test_importtosandbox_setfiltertofolders_failed(self):
    with patch.object(self.fcc, '_importFccswFiles', new=Mock(return_value=True)), \
        patch.object(self.fcc, '_setFilterToFolders', new=Mock(return_value=False)), \
        patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):

      self.assertFalse(self.fcc._importToSandbox())
      self.log_mock.error.assert_called_once_with("_setFilterToFolders() failed")

  @patch("%s._importFiles" % MODULE_NAME, new=Mock(return_value=True))
  @patch("%s._importToSandbox" % MODULE_NAME, new=Mock(return_value=False))
  def test_importtosandbox_super_method_failed(self):
    with patch.object(self.fcc, '_importFccswFiles', new=Mock(return_value=True)), \
        patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):
      self.assertFalse(self.fcc._importToSandbox())
      self.log_mock.error.assert_called_once_with("Sandboxing : _importToSandbox() failed")

  @patch("%s._readFromFile" % MODULE_NAME, new=Mock(return_value=('some content',
         'Sandboxing : FCC configuration file reading successfull')))
  def test_importfccswfiles(self):
    with patch.object(self.fcc, '_resolveTreeOfFiles') as mock_resolve:

      mock_resolve.return_value = True
      self.assertTrue(self.fcc._importFccswFiles())
      mock_resolve.assert_any_call([], '.txt')
      mock_resolve.assert_called_with([], '.cmd')

  def test_importfccswfiles_useof_pythia_generator(self):
    cmdFiles = ["Generation/data/Pythia_standard.cmd"]
    file_content = 'pythia8gentool = PythiaInterface("Pythia8Interface", Filename=pythiafile)\npythiafile="%s"' % cmdFiles[
        0]

    with patch.object(self.fcc, '_resolveTreeOfFiles') as mock_resolve, \
         patch("%s._readFromFile" % MODULE_NAME) as mock_read:

      mock_resolve.return_value = True
      mock_read.return_value = (file_content, 'Sandboxing : FCC file reading successfull')
      self.assertTrue(self.fcc._importFccswFiles())
      assertEqualsImproved(self.fcc.randomGenerator["Pythia"], cmdFiles, self)
      mock_resolve.assert_called_with(cmdFiles, '.cmd')
      mock_resolve.assert_any_call([], '.txt')

  def test_importfccswfiles_useof_gaudi_generator(self):
    cmdFiles = ["Generation/data/Pythia_standard.cmd"]
    file_content = 'Pythia is not used, it is commented\n#pythia8gentool = PythiaInterface("Pythia8Interface", Filename=pythiafile)\npythiafile="%s"\nGaudi ParticleGun somewhere' % cmdFiles[
        0]

    with patch.object(self.fcc, '_resolveTreeOfFiles') as mock_resolve, \
         patch("%s._readFromFile" % MODULE_NAME) as mock_read:

      mock_resolve.return_value = True
      mock_read.return_value = (file_content, 'Sandboxing : FCC configuration file reading successfull')
      self.assertTrue(self.fcc._importFccswFiles())
      self.assertTrue(self.fcc.randomGenerator["Gaudi"])
      mock_resolve.assert_called_with(cmdFiles, '.cmd')
      mock_resolve.assert_any_call([], '.txt')

  @patch("%s._readFromFile" % MODULE_NAME, new=Mock(return_value=("", "error message")))
  def test_importfccswfiles_read_failed(self):
    with patch.object(self.fcc, '_resolveTreeOfFiles', new=Mock(return_value=True)), \
        patch("os.path.exists", new=Mock(return_value=True)), \
        patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):

      self.assertFalse(self.fcc._importFccswFiles())
      self.log_mock.error.assert_called_once_with("error message")
      detectorFolder = os.path.join(self.fcc.fccSwPath, 'Detector')
      self.assertIn(detectorFolder, self.fcc._foldersToFilter)

  @patch("os.path.exists", new=Mock(return_value=False))
  @patch("%s._readFromFile" % MODULE_NAME, new=Mock(return_value=("some content", "some message")))
  def test_importfccswfiles_detector_warn(self):
    with patch.object(self.fcc, '_resolveTreeOfFiles', new=Mock(return_value=True)):

      self.assertTrue(self.fcc._importFccswFiles())

      warn_message = (
          "Sandboxing : The folder 'Detector' does not exist,"
          " it is not present in the FCCSW installation"
          "\nThen you should have added it manually to the input sandbox !"
          )
      self.log_mock.warn(warn_message)

      detectorFolder = os.path.join(self.fcc.fccSwPath, 'Detector')
      self.assertNotIn(detectorFolder, self.fcc._foldersToFilter)

  @patch("%s._readFromFile" % MODULE_NAME, new=Mock(return_value=("some content", "some message")))
  def test_importfccswfiles_resolvefiles_failed(self):
    with patch.object(self.fcc, '_resolveTreeOfFiles', new=Mock(return_value=False)), \
        patch("os.path.exists", new=Mock(return_value=True)), \
        patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):

      self.assertFalse(self.fcc._importFccswFiles())
      self.log_mock.error.assert_called_once_with("Sandboxing : _resolveTreeOfFiles() failed")
      detectorFolder = os.path.join(self.fcc.fccSwPath, 'Detector')
      self.assertIn(detectorFolder, self.fcc._foldersToFilter)

  def test_checkfinalconsistency(self):
    self.fcc._checkFinalConsistency()
    self.assertTrue(self.fcc.isGaudiOptionsFileNeeded)

  @patch("os.path.exists", new=Mock(return_value=False))
  def test_setfiltertofolders_exists_failed(self):
    self.fcc._foldersToFilter = set(['folder_to_filter1'])
    with patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):
      self.assertFalse(self.fcc._setFilterToFolders())
    error_message = (
        "Sandboxing : _filterFolders() failed\n"
        "The folder '%(folder)s' does not exist\n"
        "Check if you're FCCSW installation is complete"
        ) % {'folder': self.fcc._foldersToFilter.pop()}
    self.log_mock.error.assert_called_once_with(error_message)

  @patch("os.path.exists", new=Mock(return_value=True))
  def test_setfiltertofolders_filtering_failed(self):
    with patch.object(self.fcc, '_filterFolders', new=Mock(return_value=False)), \
        patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):
      self.fcc._foldersToFilter = set(['folder_to_filter1'])
      self.assertFalse(self.fcc._setFilterToFolders())
      self.log_mock.error.assert_called_once_with("Sandboxing : _filterFolders() failed")

  @patch("os.path.exists", new=Mock(return_value=True))
  def test_setfiltertofolders_filtering_succeed(self):
    with patch.object(self.fcc, '_filterFolders', new=Mock(return_value=True)), \
        patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):
      self.fcc._foldersToFilter = set(['folder_to_filter1'])
      self.assertTrue(self.fcc._setFilterToFolders())
      self.log_mock.debug.assert_called_with("Sandboxing : Folders filtering successfull")
      temp_folder = os.path.join(self.fcc._tempCwd, os.path.basename('folder_to_filter1'))
      self.assertIn(temp_folder, self.fcc._foldersToFilter)

  def test_filterfolders_recursivity(self):
    temp_folder = "/my/temp/folder"
    actual_folder = "/my/actual/folder"
    actual_sub_folder = os.path.join(actual_folder, 'folder2')

    listdir_dict = {actual_folder: ['file11', 'file12', 'folder2'], actual_sub_folder: ['file21', 'file22']}

    def replace_listdir(path):
      return listdir_dict[path]

    isfile_dict = {'file11': True, 'file12': True, 'folder2': False, 'file21': True, 'file22': True}

    def replace_isfile(path):
      return isfile_dict[os.path.basename(path)]

    with patch('os.path.exists') as mock_exists, \
         patch('os.listdir') as mock_listdir, \
         patch('os.makedirs'), \
         patch('shutil.copyfile'), \
         patch('os.path.isfile') as mock_isfile, \
         patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):

      mock_exists.return_value = True

      mock_listdir.side_effect = replace_listdir
      mock_isfile.side_effect = replace_isfile

      self.assertTrue(self.fcc._filterFolders(temp_folder, actual_folder, ".ext", False))

      mock_exists.assert_any_call(temp_folder)

      mock_listdir.assert_any_call(actual_folder)
      mock_listdir.assert_any_call(actual_sub_folder)

      actual_folder = os.path.realpath(actual_folder)
      actual_sub_folder = os.path.realpath(actual_sub_folder)

      mock_isfile.assert_any_call(os.path.join(actual_folder, 'file11'))
      mock_isfile.assert_any_call(os.path.join(actual_folder, 'file12'))
      mock_isfile.assert_any_call(os.path.join(actual_folder, 'folder2'))
      mock_isfile.assert_any_call(os.path.join(actual_sub_folder, 'file21'))
      mock_isfile.assert_any_call(os.path.join(actual_sub_folder, 'file22'))

      mock_exists.assert_any_call(os.path.join(actual_folder, 'file11'))
      mock_exists.assert_any_call(os.path.join(actual_folder, 'file12'))
      mock_exists.assert_any_call(os.path.join(actual_folder, 'folder2'))
      mock_exists.assert_any_call(os.path.join(actual_sub_folder, 'file21'))
      mock_exists.assert_any_call(os.path.join(actual_sub_folder, 'file22'))

      debug_message = "Sandboxing : Folder '%s' filtering successfull" % temp_folder
      self.log_mock.debug.assert_any_call(debug_message)

  def test_filterfolders_exists_failed(self):
    temp_folder = "/my/temp/folder"
    actual_folder = "/my/actual/folder"
    actual_sub_folder = os.path.join(actual_folder, 'folder2')

    listdir_dict = {actual_folder: ['file11', 'file12', 'folder2'], actual_sub_folder: ['file21', 'file22']}

    def replace_listdir(path):
      return listdir_dict[path]

    with patch('os.path.exists') as mock_exists, \
         patch('os.listdir') as mock_listdir, \
         patch('os.makedirs') as mock_makedirs, \
         patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):

      mock_exists.return_value = False

      mock_listdir.side_effect = replace_listdir

      self.assertFalse(self.fcc._filterFolders(temp_folder, actual_folder, ".ext", False))

      mock_exists.assert_any_call(temp_folder)
      mock_makedirs.assert_called_once_with(temp_folder)

      mock_listdir.assert_called_once_with(actual_folder)

      debug_message = (
          "Sandboxing : Creation of the filtered folder"
          " '%(temp)s' successfull" % {'temp': temp_folder}
          )

      self.log_mock.debug.assert_any_call(debug_message)

      error_message = "Sandboxing : The file '%s' does not exist" % os.path.realpath(
          os.path.join(actual_folder, 'file11'))
      self.log_mock.error.assert_called_once_with(error_message)

  @patch('os.path.exists', new=Mock(return_value=False))
  def test_filterfolders_makedirs_failed(self):
    temp_folder = "/my/temp/folder"
    actual_folder = "/my/actual/folder"

    with patch('os.makedirs') as mock_makedirs, \
         patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):

      mock_makedirs.side_effect = OSError("oserror")

      self.assertFalse(self.fcc._filterFolders(temp_folder, actual_folder, ".ext", False))

      error_message = (
          "Sandboxing : Creation of the filtered folder"
          " '%(temp)s' failed\noserror" % {'temp': temp_folder}
          )
      self.log_mock.error.assert_called_once_with(error_message)

      mock_makedirs.assert_called_once_with(temp_folder)

  def test_filterfolders_shutil_failed(self):
    temp_folder = "/my/temp/folder"
    actual_folder = "/my/actual/folder"

    source = os.path.realpath(os.path.join(actual_folder, 'file11'))
    destination = os.path.realpath(os.path.join(temp_folder, 'file11'))

    exists_dict = {temp_folder: True, source: True, destination: False}

    def replace_exists(path):
      return exists_dict[path]

    listdir_dict = {actual_folder: ['file11']}

    def replace_listdir(path):
      return listdir_dict[path]

    isfile_dict = {'file11': True}

    def replace_isfile(path):
      return isfile_dict[os.path.basename(path)]

    with patch('os.path.exists') as mock_exists, \
         patch('os.listdir') as mock_listdir, \
         patch('shutil.copyfile') as mock_shutil, \
         patch('os.path.isfile') as mock_isfile, \
         patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):

      # throw OS error
      mock_shutil.side_effect = IOError("ioerror")

      mock_listdir.side_effect = replace_listdir
      mock_isfile.side_effect = replace_isfile
      mock_exists.side_effect = replace_exists

      self.assertTrue(self.fcc._filterFolders(temp_folder, actual_folder, ".ext", True))

      mock_exists.assert_any_call(temp_folder)
      mock_exists.assert_any_call(source)
      mock_exists.assert_any_call(destination)

      mock_listdir.assert_called_once_with(actual_folder)

      mock_isfile.assert_called_once_with(os.path.realpath(os.path.join(actual_folder, 'file11')))

      mock_shutil.assert_called_once_with(source, destination)

      warn_message = "Sandboxing : The copy of the file '%s' failed\nioerror" % destination
      self.log_mock.warn.assert_called_once_with(warn_message)

  def test_filterfolders_exclude_txt(self):
    temp_folder = "/my/temp/folder"
    actual_folder = "/my/actual/folder"

    source1 = os.path.realpath(os.path.join(actual_folder, 'file11.txt'))
    destination1 = os.path.realpath(os.path.join(temp_folder, 'file11.txt'))

    source2 = os.path.realpath(os.path.join(actual_folder, 'file12.zip'))
    destination2 = os.path.realpath(os.path.join(temp_folder, 'file12.zip'))

    exists_dict = {temp_folder: True, source1: True, destination1: False, source2: True, destination2: False}

    def replace_exists(path):
      return exists_dict[path]

    listdir_dict = {actual_folder: ['file11.txt', 'file12.zip']}

    def replace_listdir(path):
      return listdir_dict[path]

    isfile_dict = {'file11.txt': True, 'file12.zip': True}

    def replace_isfile(path):
      return isfile_dict[os.path.basename(path)]

    with patch('os.path.exists') as mock_exists, \
         patch('os.listdir') as mock_listdir, \
         patch('shutil.copyfile') as mock_shutil, \
         patch('os.path.isfile') as mock_isfile, \
         patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):

      mock_listdir.side_effect = replace_listdir
      mock_isfile.side_effect = replace_isfile
      mock_exists.side_effect = replace_exists

      # exclude all txt files
      self.assertTrue(self.fcc._filterFolders(temp_folder, actual_folder, ".txt", True))

      mock_exists.assert_any_call(temp_folder)
      mock_exists.assert_any_call(source1)
      mock_exists.assert_any_call(destination1)

      mock_exists.assert_any_call(source2)
      mock_exists.assert_any_call(destination2)

      mock_listdir.assert_called_once_with(actual_folder)

      mock_isfile.assert_any_call(os.path.realpath(os.path.join(actual_folder, 'file11.txt')))

      # zip files are copied so shutil called for these files
      mock_shutil.assert_any_call(source2, destination2)

      # txt files are not copied (they are excluded) so shutil not called for these files
      self.assertFalse((source1, destination1) in mock_shutil.call_args_list)

      debug_message = "Sandboxing : Folder '%s' filtering successfull" % temp_folder
      self.log_mock.debug.assert_called_with(debug_message)

  def test_filterfolders_include_txt(self):
    temp_folder = "/my/temp/folder"
    actual_folder = "/my/actual/folder"

    source1 = os.path.realpath(os.path.join(actual_folder, 'file11.txt'))
    destination1 = os.path.realpath(os.path.join(temp_folder, 'file11.txt'))

    source2 = os.path.realpath(os.path.join(actual_folder, 'file12.zip'))
    destination2 = os.path.realpath(os.path.join(temp_folder, 'file12.zip'))

    exists_dict = {temp_folder: True, source1: True, destination1: False, source2: True, destination2: False}

    def replace_exists(path):
      return exists_dict[path]

    listdir_dict = {actual_folder: ['file11.txt', 'file12.zip']}

    def replace_listdir(path):
      return listdir_dict[path]

    isfile_dict = {'file11.txt': True, 'file12.zip': True}

    def replace_isfile(path):
      return isfile_dict[os.path.basename(path)]

    with patch('os.path.exists') as mock_exists, \
         patch('os.listdir') as mock_listdir, \
         patch('shutil.copyfile') as mock_shutil, \
         patch('os.path.isfile') as mock_isfile, \
         patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):

      mock_listdir.side_effect = replace_listdir
      mock_isfile.side_effect = replace_isfile
      mock_exists.side_effect = replace_exists

      # include only txt files
      self.assertTrue(self.fcc._filterFolders(temp_folder, actual_folder, ".txt", False))

      mock_exists.assert_any_call(temp_folder)
      mock_exists.assert_any_call(source1)
      mock_exists.assert_any_call(destination1)

      mock_exists.assert_any_call(source2)
      mock_exists.assert_any_call(destination2)

      mock_listdir.assert_called_once_with(actual_folder)

      mock_isfile.assert_any_call(os.path.realpath(os.path.join(actual_folder, 'file11.txt')))

      # txt files are copied so shutil called for these files
      mock_shutil.assert_any_call(source1, destination1)

      # zip files are not copied (they are excluded) so shutil not called for these files
      self.assertFalse((source2, destination2) in mock_shutil.call_args_list)

      debug_message = "Sandboxing : Folder '%s' filtering successfull" % temp_folder
      self.log_mock.debug.assert_called_with(debug_message)


class FccAnalysisTestCase(FccMixin, unittest.TestCase):
  """Tests for FccAnalysis."""

  def setUp(self):

    super(FccAnalysisTestCase, self).setUp()

    fcc_conf_file = '/path/to/ee_ZH_Zmumu_Hbb.txt'
    output_file = "ee_ZH_Zmumu_Hbb.root"

    fccphysics = FccAnalysis(
        fccConfFile=fcc_conf_file
        )

    fccphysics.setOutputFile(output_file)

    self.fcc = fccphysics

  def test_randomGenerator(self):
    assertEqualsImproved(self.fcc.randomGenerator, {"Pythia": []}, self)

  def test_readeventfalse(self):
    self.assertFalse(self.fcc.read)

  def test_readeventtrue(self):
    fccphysics_read = FccAnalysis(
        executable='fcc-physics-read',
        fccConfFile="/path/to/confFile"
        )
    self.assertTrue(fccphysics_read.read)

    fccphysics_read_delphes = FccAnalysis(
        executable='fcc-physics-read-delphes',
        fccConfFile="/path/to/confFile"
        )
    self.assertTrue(fccphysics_read_delphes.read)

  @patch("%s._importFiles" % MODULE_NAME, new=Mock(return_value=True))
  def test_importtosandbox(self):
    with patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):
      self.assertTrue(self.fcc._importToSandbox())
    self.log_mock.debug.assert_called_with("Sandboxing : Importation of user files/folders successfull")

  @patch("%s._importFiles" % MODULE_NAME, new=Mock(return_value=False))
  def test_importtosandbox_failed(self):
    with patch.object(inspect.getmodule(FccSw), 'LOG', new=self.log_mock):
      self.assertFalse(self.fcc._importToSandbox())
    self.log_mock.error.assert_called_once_with("Sandboxing : _importFiles() failed")
