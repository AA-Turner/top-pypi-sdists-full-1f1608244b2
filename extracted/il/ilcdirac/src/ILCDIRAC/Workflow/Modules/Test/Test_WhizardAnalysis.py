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
"""Unit tests for the WhizardAnalysis module."""

from __future__ import absolute_import
import unittest
import os
from mock import call, mock_open, patch, MagicMock as Mock

from DIRAC import S_OK, S_ERROR
from ILCDIRAC.Workflow.Modules.WhizardAnalysis import WhizardAnalysis
from Tests.Utilities.GeneralUtils import assertEqualsImproved, \
    assertDiracFailsWith, assertDiracSucceeds, assertDiracSucceedsWith_equals, \
    assertMockCalls
from Tests.Utilities.FileUtils import FileUtil
from six.moves import zip

__RCSID__ = "$Id$"

MODULE_NAME = 'ILCDIRAC.Workflow.Modules.WhizardAnalysis'

# pylint: disable=too-many-public-methods,missing-docstring


class WhizardAnalysisTestCase(unittest.TestCase):
  """Base class for the WhizardAnalysis test cases."""

  def setUp(self):
    self.wha = WhizardAnalysis()
    self.wha.platform = 'myTestPlatform'
    self.wha.applicationLog = '/mydir/AppLog/test.txt'
    self.wha.workflowStatus = S_OK()
    self.wha.stepStatus = S_OK()

  def test_obtainprocesslist_getfile_fails(self):
    datman_mock = Mock()
    datman_mock.getFile.return_value = S_ERROR('network_error_testME')
    operations_mock = Mock()
    operations_mock.getValue.return_value = 'mytestproclist'
    self.wha.ops = operations_mock
    self.wha.datMan = datman_mock
    with patch('%s.os.path.exists' % MODULE_NAME, new=Mock(return_value=False)):
      res = self.wha.obtainProcessList()
      assertDiracFailsWith(res, 'network_error_testme', self)
      datman_mock.getFile.assert_called_once_with('mytestproclist')
      operations_mock.getValue.assert_called_once_with('/ProcessList/Location',
                                                        '')

  def test_applicationSpecificInputs(self):
    self.wha.energy = '42189GeV'
    self.wha.RandomSeed = None
    self.wha.jobID = 840
    self.wha.workflow_commons['IS_PROD'] = True
    self.wha.workflow_commons['PRODUCTION_ID'] = '874'
    self.wha.workflow_commons['JOB_ID'] = '783'
    self.wha.workflow_commons['ProductionOutputData'] = 'myoutputfile_dontuseme;output_gen_test.exe'
    self.wha.step_commons['SusyModel'] = 2
    self.wha.step_commons['InputFile'] = '/ignore/this/inpfTest.me'
    self.wha.steeringparameters = 'testparam=9842;illegalparam;another=one'
    self.wha.willCut = False
    result = self.wha.applicationSpecificInputs()
    assertDiracSucceeds(result, self)
    assertEqualsImproved(('42189GeV', 874783, self.wha.parameters['SEED'], 2,
                           'inpfTest.me', '9842', 'one', False,
                           'output_gen_test.exe'),
                          (self.wha.parameters['ENERGY'], self.wha.RandomSeed,
                            self.wha.RandomSeed, self.wha.susymodel,
                            self.wha.SteeringFile, self.wha.parameters['testparam'],
                            self.wha.parameters['another'], self.wha.getProcessInFile,
                            self.wha.OutputFile), self)

  def test_applicationSpecificInputs_1(self):
    self.wha.RandomSeed = 'myrandseed'
    self.wha.SteeringFile = 'whizard.in'
    self.wha.steeringparameters = ''
    self.wha.OptionsDictStr = 'blab'
    with patch('%s.os.rename' % MODULE_NAME) as rename_mock, \
         patch('%s.eval' % MODULE_NAME, new=Mock(side_effect=IOError('dont use eval...'))):
      result = self.wha.applicationSpecificInputs()
      assertDiracFailsWith(
          result, 'could not convert string to dictionary for optionsdict', self)
      rename_mock.assert_called_once_with('whizard.in', 'whizardnew.in')
      assertEqualsImproved(('myrandseed', 'whizardnew.in', 0),
                            (self.wha.RandomSeed, self.wha.SteeringFile,
                              self.wha.susymodel), self)

  def test_applicationSpecificInputs_2(self):
    self.wha.RandomSeed = '9803245'
    self.wha.SteeringFile = 'testme'
    self.wha.steeringparameters = ''
    self.wha.OptionsDictStr = 'well_formed_dict'
    self.wha.GenLevelCutDictStr = 'bla'

    def replace_eval(string_to_parse):
      if string_to_parse == 'well_formed_dict':
        return {'process_input': {'sqrts': 'mytestenergywithroots'},
                 'random_entry': 'testme'}
      else:
        raise IOError('dont use eval!')
    with patch('%s.os.rename' % MODULE_NAME) as rename_mock, \
         patch('%s.eval' % MODULE_NAME, new=Mock(side_effect=replace_eval)):
      result = self.wha.applicationSpecificInputs()
      assertDiracFailsWith(
          result, 'could not convert the generator level cuts back to dictionary',
          self)
      self.assertFalse(rename_mock.called)
      assertEqualsImproved(('9803245', 'testme', 0,
                              {'integration_input': {'seed': 9803245},
                                'process_input': {'sqrts': 'mytestenergywithroots'},
                                'random_entry': 'testme'}, 'mytestenergywithroots'),
                            (self.wha.RandomSeed, self.wha.SteeringFile, self.wha.susymodel,
                              self.wha.optionsdict, self.wha.energy), self)

  def test_applicationSpecificInputs_3(self):
    self.wha.RandomSeed = 'myrandseed'
    self.wha.SteeringFile = 'testme'
    self.wha.steeringparameters = ''
    self.wha.OptionsDictStr = 'blab'
    self.wha.GenLevelCutDictStr = 'bla'
    self.wha.workflow_commons['IS_DBD_GEN_PROD'] = True
    self.wha.workflow_commons['PRODUCTION_ID'] = 348
    self.wha.workflow_commons['JOB_ID'] = 742
    self.wha.workflow_commons['ProductionOutputData'] = 'abc;ignore_me'
    with patch('%s.os.rename' % MODULE_NAME) as rename_mock, \
         patch('%s.eval' % MODULE_NAME, new=Mock(side_effect=[{'integration_input': {'seed': 'otherseed'}, 'random_entry': 'testme'}, {'something': 'else'}])):
      result = self.wha.applicationSpecificInputs()
      assertDiracSucceeds(result, self)
      self.assertFalse(rename_mock.called)
      assertEqualsImproved(({'integration_input': {'seed': 'otherseed'},
                                'random_entry': 'testme'}, {'something': 'else'},
                              'abc'), (self.wha.optionsdict, self.wha.genlevelcuts,
                                         self.wha.OutputFile), self)

  def test_runit(self):
    set_default_values(self.wha)
    self.wha.workflow_commons['Info'] = {}  # Has to stay for the refactoring
    exists_dict = {'list.txt': True, 'LesHouches.msugra_1.in': False,
                    'my/test/soft/dir/LesHouches_slsqhh.msugra_1.in': True,
                    'Whizard_myTestV1_Run_testStep12.sh': False,
                    'mytestAppLOg': False, 'whizard.out': True,
                    'my/test/soft/dir/myTestGotFile': True,
                    'myTestEvents.001.stdhep': True}

    def exists_replace(key):
      value = exists_dict[key]
      if key == 'mytestAppLOg':
        exists_dict['mytestAppLOg'] = True
      return value
    file_contents = [[], ['some_logging_ignoreme',
                            '! Event sample corresponds to luminosity 92847',
                            'Event generation finished. Success!'], [
        'a 12.1 489.3 b 91.2   843            "']]
    genmodel_mock = Mock()
    genmodel_mock.hasModel.return_value = S_OK()
    genmodel_mock.getFile.return_value = S_OK('myTestGotFile')
    self.wha.genmodel = genmodel_mock
    whizopts_mock = Mock()
    whizopts_mock.changeAndReturn.return_value = S_OK()
    whizopts_mock.toWhizardDotIn.return_value = S_OK('')
    whizopts_mock.getAsDict.return_value = S_OK({'process_input':
                                                   {'process_id': '123 843'},
                                                   'some': 'dict'})
    whiz_options_mock = Mock(return_value=whizopts_mock)
    getops_mock = Mock()
    self.wha.ops = getops_mock
    method_mock = Mock()
    method_mock.getInFile.return_value = 'mywhizardTestFile.in'
    proclist_mock = Mock(return_value=method_mock)
    expected_glob = [call('myTestEvents*.stdhep')]
    expected_shell = [call(0, 'sh -c "./Whizard_myTestV1_Run_testStep12.sh"',
                            callbackFunction=self.wha.redirectLogOutput,
                            bufferLimit=209715200)]
    expected_copy = []
    expected_genmodel = [
        call.hasModel('mytestMODEL'), call.getFile('mytestMODEL'),
        call.getFile('mytestMODEL'), call.getFile('mytestMODEL')]
    expected_getops = []
    expected_remove = []
    expected_chmod = [call('Whizard_myTestV1_Run_testStep12.sh', 0o755)]
    expected_appstat = [call('Whizard myTestV1 step testStep12'),
                         call('Whizard myTestV1 Successful')]
    expected_exists = [call('LesHouches.msugra_1.in'),
                        call('my/test/soft/dir/LesHouches_slsqhh.msugra_1.in'),
                        call('my/test/soft/dir/myTestGotFile'),
                        call('Whizard_myTestV1_Run_testStep12.sh'),
                        call('mytestAppLOg'), call('mytestAppLOg'),
                        call('whizard.out'), call('myTestEvents.001.stdhep')]
    expected_rename = [
        call('myoutputfile_123.stdhep', 'mytestwhizardOutputFile_1.stdhep'),
        call('myotherfile_121.stdhep', 'mytestwhizardOutputFile_2.stdhep'),
        call('lastfile_9824.stdhep', 'mytestwhizardOutputFile_3.stdhep')]
    expected_calls = [
        [call('#!/bin/sh \n'), call('#####################################################################\n'),
         call('# Dynamically generated script to run a production or analysis job. #\n'),
         call('#####################################################################\n'),
         call('declare -x PATH=my/test/soft/dir:$PATH\n'),
         call('declare -x LD_LIBRARY_PATH=my/test/soft/dir/lib:my/lib/path\n'),
         call('env | sort >> localEnv.log\n'),
         call('echo =============================\n'),
         call('echo Printing content of whizard.in \n'), call('cat whizard.in\n'),
         call('echo =============================\n'),
         call('cp  my/test/soft/dir/whizard.mdl ./\n'),
         call('cp my/test/soft/dir/myTestGotFile ./LesHouches.msugra_1.in\n'),
         call('ln -s LesHouches.msugra_1.in fort.71\n'),
         call('cp mygridfiles/folder/My99TestTeVFile.energy/gridfile1.txt ./\n'),
         call('cp mygridfiles/folder/My99TestTeVFile.energy/cool/gridfile2.ppt ./\n'),
         call('cp mygridfiles/folder/My99TestTeVFile.energy/My99TestTeVFile.energy ./\n'),
         call('cp my/test/soft/dir/whizard.prc ./\n'),
         call('echo =============================\n'),
         call('echo Printing content of whizard.prc \n'),
         call('cat whizard.prc\n'), call('echo =============================\n'),
         call('whizard --process_input \'process_id =\"myTestEvents\"\' --simulation_input \'write_events_file = \"myTestEvents\"\'  extraTestCLIargs \n'),
         call('declare -x appstatus=$?\n'), call('exit $appstatus\n')], [], []]
    handles = FileUtil.getMultipleReadHandles(file_contents)
    with patch('%s.getSoftwareFolder' % MODULE_NAME, new=Mock(side_effect=[S_OK('my/test/soft/dir'), S_OK('/my/test/dep/ignorethis'), S_OK('mygridfiles/folder'), S_OK('/spectra/files')])), \
         patch('%s.removeLibc' % MODULE_NAME, new=Mock(return_value=True)), \
         patch('%s.getNewLDLibs' % MODULE_NAME, new=Mock(return_value='my/lib/path')), \
         patch('%s.resolveDeps' % MODULE_NAME, new=Mock(return_value=[{'app': 'mytestdep', 'version': '4.2'}, {'app': 'gridfiles', 'version': '1.0'}, {'app': 'beam_spectra', 'version': '20.3'}])), \
         patch.dict('os.environ', {}, True), \
         patch('%s.os.listdir' % MODULE_NAME, new=Mock(side_effect=[['gridfile1.txt', 'cool/gridfile2.ppt', 'My99TestTeVFile.energy'], ['gridfile1.txt', 'cool/gridfile2.ppt', 'My99TestTeVFile.energy']])), \
         patch('%s.os.path.isdir' % MODULE_NAME, new=Mock(return_value=True)), \
         patch('%s.os.path.exists' % MODULE_NAME, new=Mock(side_effect=exists_replace)) as exists_mock, \
         patch('%s.ProcessList' % MODULE_NAME, new=proclist_mock), \
         patch('%s.WhizardAnalysis.setApplicationStatus' % MODULE_NAME) as appstat_mock, \
         patch('%s.shutil.copy' % MODULE_NAME, new=Mock(return_value=True)) as copy_mock, \
         patch('%s.WhizardOptions' % MODULE_NAME, new=whiz_options_mock), \
         patch('%s.os.remove' % MODULE_NAME, new=Mock(return_value=True)) as remove_mock, \
         patch('%s.open' % MODULE_NAME, mock_open(), create=True) as open_mock, \
         patch('%s.WhizardAnalysis.makeWhizardDotCut1' % MODULE_NAME, new=Mock(return_value=S_OK())), \
         patch('%s.os.chmod' % MODULE_NAME) as chmod_mock, \
         patch('%s.shellCall' % MODULE_NAME, new=Mock(return_value=S_OK())) as shell_mock, \
         patch('%s.glob.glob' % MODULE_NAME, new=Mock(return_value=['myoutputfile_123.stdhep', 'myotherfile_121.stdhep', 'lastfile_9824.stdhep'])) as glob_mock, \
         patch('%s.os.rename' % MODULE_NAME) as rename_mock:
      open_mock.side_effect = (h for h in handles)
      result = self.wha.runIt()
      assertDiracSucceedsWith_equals(result, {
          'OutputFile': 'mytestwhizardOutputFile'}, self)
      assertMockCalls(open_mock, [('Whizard_myTestV1_Run_testStep12.sh', 'w'), 'mytestAppLOg',
                                    ('whizard.out', 'r')], self)
      check_runit_for_parameters(self, whiz_options_mock, getops_mock,
                                  genmodel_mock, expected_calls, handles,
                                  appstat_mock, exists_mock, rename_mock,
                                  chmod_mock, glob_mock, shell_mock, copy_mock,
                                  remove_mock, open_mock, expected_appstat,
                                  expected_exists, expected_rename,
                                  expected_chmod, expected_glob,
                                  expected_shell, expected_copy, expected_genmodel,
                                  expected_getops, expected_remove)
      assertEqualsImproved(self.wha.workflow_commons['Info'], {
          'xsection': {'843': {'xsection': 12.1, 'err_xsection': 489.3,
                                 'fraction': 91.2}}}, self)
      assertEqualsImproved(self.wha.workflow_commons['Luminosity'], 92847,
                            self)
      whizopts_mock.getAsDict.assert_called_once_with()

  def test_runit_no_platform(self):
    self.wha.platform = None
    assertDiracFailsWith(self.wha.runIt(), 'no ilc platform selected', self)

  def test_runit_no_logfile(self):
    self.wha.applicationLog = None
    assertDiracFailsWith(self.wha.runIt(), 'no log file provided', self)

  def test_runit_workflowstatus_bad(self):
    self.wha.workflowStatus = S_ERROR('workflow_err_testme')
    assertDiracSucceedsWith_equals(
        self.wha.runIt(), 'Whizard should not proceed as previous step did not end properly',
        self)

  def test_runit_stepstatus_bad(self):
    self.wha.stepStatus = S_ERROR('step_err_testme')
    assertDiracSucceedsWith_equals(
        self.wha.runIt(), 'Whizard should not proceed as previous step did not end properly',
        self)

  def test_runit_getsoftwarefolder_fails(self):
    with patch('%s.getSoftwareFolder' % MODULE_NAME, new=Mock(return_value=S_ERROR('get_software_network_test_error'))) as getsoft_mock, \
        patch('%s.WhizardAnalysis.setApplicationStatus' % MODULE_NAME) as appstat_mock:
      assertDiracFailsWith(self.wha.runIt(), 'get_software_network_test_error',
                            self)
      appstat_mock.assert_called_once_with('Failed finding software')
      getsoft_mock.assert_called_once_with('myTestPlatform', 'whizard', '')

  def test_runit_getdependencies_fails(self):
    with patch('%s.getSoftwareFolder' % MODULE_NAME, new=Mock(side_effect=[S_OK('my/test/soft/dir'), S_OK('test/dep/folder/'), S_ERROR('something_fails_test')])) as getsoft_mock, \
        patch('%s.removeLibc' % MODULE_NAME, new=Mock(return_value=True)) as removlib_mock, \
        patch('%s.getNewLDLibs' % MODULE_NAME, new=Mock(return_value='my/lib/path')) as getlibs_mock, \
        patch('%s.resolveDeps' % MODULE_NAME, new=Mock(return_value=[{'testdep1': True, 'app': 'mytestdep', 'version': '4.2'}, {'failsomethingonthisdep': True, 'app': 'faulty_dep_testme', 'version': 'invalid'}])) as resolvdep_mock, \
        patch('%s.WhizardAnalysis.setApplicationStatus' % MODULE_NAME) as setappstatus_mock:
      assertDiracFailsWith(self.wha.runIt(), 'something_fails_test', self)
      setappstatus_mock.assert_called_once_with('Failed finding software')
      getlibs_mock.assert_called_once_with('myTestPlatform', 'whizard', '')
      resolvdep_mock.assert_called_once_with('myTestPlatform', 'whizard', '')
      removlib_mock.assert_called_once_with('my/test/soft/dir/lib')
      assertMockCalls(getsoft_mock, [('myTestPlatform', 'whizard', ''),
                                       ('myTestPlatform', 'mytestdep', '4.2'),
                                       ('myTestPlatform', 'faulty_dep_testme', 'invalid')], self)

  def test_runit_whizardin_fails(self):
    self.wha.useGridFiles = True
    self.wha.getProcessInFile = True
    getops_mock = Mock()
    getops_mock.getValue.return_value = '/my/process/list/list.txt'
    self.wha.ops = getops_mock
    method_mock = Mock()
    method_mock.getInFile.return_value = False
    proclist_mock = Mock(return_value=method_mock)
    with patch('%s.getSoftwareFolder' % MODULE_NAME, new=Mock(side_effect=[S_OK('my/test/soft/dir'), S_OK('/my/test/dep/ignorethis'), S_OK('mygridfiles/folder'), S_OK('/spectra/files')])), \
         patch('%s.removeLibc' % MODULE_NAME, new=Mock(return_value=True)), \
         patch('%s.getNewLDLibs' % MODULE_NAME, new=Mock(return_value='my/lib/path')), \
         patch('%s.resolveDeps' % MODULE_NAME, new=Mock(return_value=[{'app': 'mytestdep', 'version': '4.2'}, {'app': 'gridfiles', 'version': '1.0'}, {'app': 'beam_spectra', 'version': '20.3'}])), \
         patch.dict('os.environ', {}, True), \
         patch('%s.os.listdir' % MODULE_NAME, new=Mock(side_effect=[['gridfile1.txt', 'cool/gridfile2.ppt', 'last/file/ok'], []])), \
         patch('%s.os.path.isdir' % MODULE_NAME, new=Mock(return_value=True)), \
         patch('%s.glob.glob' % MODULE_NAME, new=Mock(side_effect=[['file1.grb', 'otherfile.grb'], ['testfile.grc']])), \
         patch('%s.os.path.exists' % MODULE_NAME, new=Mock(return_value=True)) as exists_mock, \
         patch('%s.ProcessList' % MODULE_NAME, new=proclist_mock), \
         patch('%s.WhizardAnalysis.setApplicationStatus' % MODULE_NAME) as appstat_mock:
      assertDiracFailsWith(self.wha.runIt(),
                            'error while resolving whizard input file', self)
      getops_mock.getValue.assert_called_once_with('/ProcessList/Location', '')
      exists_mock.assert_called_once_with('list.txt')
      appstat_mock.assert_called_once_with('Whizard input file was not found')
      assertEqualsImproved(EXPECTED_TEST_ENVIRON, os.environ, self)

  def test_runit_getprocesslist_fails(self):
    self.wha.useGridFiles = True
    self.wha.getProcessInFile = True
    getops_mock = Mock()
    getops_mock.getValue.return_value = ''
    self.wha.ops = getops_mock
    method_mock = Mock()
    method_mock.getInFile.return_value = False
    proclist_mock = Mock(return_value=method_mock)
    with patch('%s.getSoftwareFolder' % MODULE_NAME, new=Mock(side_effect=[S_OK('my/test/soft/dir'), S_OK('/my/test/dep/ignorethis'), S_OK('mygridfiles/folder'), S_OK('/spectra/files')])), \
         patch('%s.removeLibc' % MODULE_NAME, new=Mock(return_value=True)), \
         patch('%s.getNewLDLibs' % MODULE_NAME, new=Mock(return_value='my/lib/path')), \
         patch('%s.resolveDeps' % MODULE_NAME, new=Mock(return_value=[{'app': 'mytestdep', 'version': '4.2'}, {'app': 'gridfiles', 'version': '1.0'}, {'app': 'beam_spectra', 'version': '20.3'}])), \
         patch.dict('os.environ', {}, True), \
         patch('%s.os.listdir' % MODULE_NAME, new=Mock(side_effect=[['gridfile1.txt', 'cool/gridfile2.ppt', 'last/file/ok'], []])), \
         patch('%s.os.path.isdir' % MODULE_NAME, new=Mock(return_value=True)), \
         patch('%s.glob.glob' % MODULE_NAME, new=Mock(side_effect=[['file1.grb', 'otherfile.grb'], ['testfile.grc']])), \
         patch('%s.os.path.exists' % MODULE_NAME, new=Mock(return_value=True)) as exists_mock, \
         patch('%s.ProcessList' % MODULE_NAME, new=proclist_mock), \
         patch('%s.WhizardAnalysis.setApplicationStatus' % MODULE_NAME) as appstat_mock:
      assertDiracFailsWith(self.wha.runIt(), 'no process list found', self)
      getops_mock.getValue.assert_called_once_with('/ProcessList/Location', '')
      self.assertFalse(exists_mock.called)
      appstat_mock.assert_called_once_with('Failed getting processlist')

  def test_runit_leshouchesfile_missing(self):
    exists_dict = {'list.txt': True, 'LesHouches.msugra_1.in': False,
                    'my/test/soft/dir/myTestGotFile': False}
    self.wha.useGridFiles = True
    self.wha.getProcessInFile = True
    self.wha.Model = True
    self.wha.susymodel = False
    genmodel_mock = Mock()
    genmodel_mock.hasModel.return_value = S_OK()
    genmodel_mock.getFile.return_value = S_OK('myTestGotFile')
    self.wha.genmodel = genmodel_mock
    getops_mock = Mock()
    getops_mock.getValue.return_value = '/my/process/list/list.txt'
    self.wha.ops = getops_mock
    method_mock = Mock()
    method_mock.getInFile.return_value = 'mywhizardTestFile.in'
    proclist_mock = Mock(return_value=method_mock)
    with patch('%s.getSoftwareFolder' % MODULE_NAME, new=Mock(side_effect=[S_OK('my/test/soft/dir'), S_OK('/my/test/dep/ignorethis'), S_OK('mygridfiles/folder'), S_OK('/spectra/files')])), \
         patch('%s.removeLibc' % MODULE_NAME, new=Mock(return_value=True)), \
         patch('%s.getNewLDLibs' % MODULE_NAME, new=Mock(return_value='my/lib/path')), \
         patch('%s.resolveDeps' % MODULE_NAME, new=Mock(return_value=[{'app': 'mytestdep', 'version': '4.2'}, {'app': 'gridfiles', 'version': '1.0'}, {'app': 'beam_spectra', 'version': '20.3'}])), \
         patch.dict('os.environ', {}, True), \
         patch('%s.os.listdir' % MODULE_NAME, new=Mock(side_effect=[['gridfile1.txt', 'cool/gridfile2.ppt', 'last/file/ok'], []])), \
         patch('%s.os.path.isdir' % MODULE_NAME, new=Mock(return_value=True)), \
         patch('%s.glob.glob' % MODULE_NAME, new=Mock(side_effect=[['file1.grb', 'otherfile.grb'], ['testfile.grc']])), \
         patch('%s.os.path.exists' % MODULE_NAME, new=Mock(side_effect=lambda path: exists_dict[path])) as exists_mock, \
         patch('%s.ProcessList' % MODULE_NAME, new=proclist_mock), \
         patch('%s.WhizardAnalysis.setApplicationStatus' % MODULE_NAME) as appstat_mock, \
         patch('%s.shutil.copy' % MODULE_NAME, new=Mock(return_value=True)) as copy_mock:
      assertDiracFailsWith(self.wha.runIt(), 'the leshouches file was not found',
                            self)
      getops_mock.getValue.assert_called_once_with('/ProcessList/Location', '')
      assertEqualsImproved(len(exists_mock.mock_calls), 3, self)
      appstat_mock.assert_called_once_with('LesHouches file missing')
      copy_mock.assert_called_once_with('my/test/soft/dir/mywhizardTestFile.in',
                                         './whizardnew.in')
      genmodel_mock.hasModel.assert_called_once_with(True)
      assertMockCalls(genmodel_mock.getFile, [True, True], self)

  def test_runit_model_undefined(self):
    exists_dict = {'list.txt': True, 'LesHouches.msugra_1.in': False}
    self.wha.useGridFiles = True
    self.wha.getProcessInFile = True
    self.wha.Model = True
    self.wha.susymodel = False
    genmodel_mock = Mock()
    genmodel_mock.hasModel.return_value = S_ERROR()
    genmodel_mock.getFile.return_value = S_OK('myTestGotFile')
    self.wha.genmodel = genmodel_mock
    getops_mock = Mock()
    getops_mock.getValue.return_value = '/my/process/list/list.txt'
    self.wha.ops = getops_mock
    method_mock = Mock()
    method_mock.getInFile.return_value = 'mywhizardTestFile.in'
    proclist_mock = Mock(return_value=method_mock)
    with patch('%s.getSoftwareFolder' % MODULE_NAME, new=Mock(side_effect=[S_OK('my/test/soft/dir'), S_OK('/my/test/dep/ignorethis'), S_OK('mygridfiles/folder'), S_OK('/spectra/files')])), \
         patch('%s.removeLibc' % MODULE_NAME, new=Mock(return_value=True)), \
         patch('%s.getNewLDLibs' % MODULE_NAME, new=Mock(return_value='my/lib/path')), \
         patch('%s.resolveDeps' % MODULE_NAME, new=Mock(return_value=[{'app': 'mytestdep', 'version': '4.2'}, {'app': 'gridfiles', 'version': '1.0'}, {'app': 'beam_spectra', 'version': '20.3'}])), \
         patch.dict('os.environ', {}, True), \
         patch('%s.os.listdir' % MODULE_NAME, new=Mock(side_effect=[['gridfile1.txt', 'cool/gridfile2.ppt', 'last/file/ok'], []])), \
         patch('%s.os.path.isdir' % MODULE_NAME, new=Mock(return_value=True)), \
         patch('%s.glob.glob' % MODULE_NAME, new=Mock(side_effect=[['file1.grb', 'otherfile.grb'], ['testfile.grc']])), \
         patch('%s.os.path.exists' % MODULE_NAME, new=Mock(side_effect=lambda path: exists_dict[path])) as exists_mock, \
         patch('%s.ProcessList' % MODULE_NAME, new=proclist_mock), \
         patch('%s.WhizardAnalysis.setApplicationStatus' % MODULE_NAME) as appstat_mock, \
         patch('%s.shutil.copy' % MODULE_NAME, new=Mock(return_value=True)) as copy_mock:
      assertDiracFailsWith(self.wha.runIt(), 'no model true defined', self)
      getops_mock.getValue.assert_called_once_with('/ProcessList/Location', '')
      assertEqualsImproved(len(exists_mock.mock_calls), 2, self)
      appstat_mock.assert_called_once_with('Model undefined')
      copy_mock.assert_called_once_with('my/test/soft/dir/mywhizardTestFile.in',
                                         './whizardnew.in')
      genmodel_mock.hasModel.assert_called_once_with(True)
      self.assertFalse(genmodel_mock.called)

  def test_runit_copy_fails(self):
    exists_dict = {'list.txt': True}
    self.wha.useGridFiles = True
    self.wha.getProcessInFile = True
    getops_mock = Mock()
    getops_mock.getValue.return_value = '/my/process/list/list.txt'
    self.wha.ops = getops_mock
    method_mock = Mock()
    method_mock.getInFile.return_value = 'mywhizardTestFile.in'
    proclist_mock = Mock(return_value=method_mock)
    with patch('%s.getSoftwareFolder' % MODULE_NAME, new=Mock(side_effect=[S_OK('my/test/soft/dir'), S_OK('/my/test/dep/ignorethis'), S_OK('mygridfiles/folder'), S_OK('/spectra/files')])), \
         patch('%s.removeLibc' % MODULE_NAME, new=Mock(return_value=True)), \
         patch('%s.getNewLDLibs' % MODULE_NAME, new=Mock(return_value='my/lib/path')), \
         patch('%s.resolveDeps' % MODULE_NAME, new=Mock(return_value=[{'app': 'mytestdep', 'version': '4.2'}, {'app': 'gridfiles', 'version': '1.0'}, {'app': 'beam_spectra', 'version': '20.3'}])), \
         patch.dict('os.environ', {}, True), \
         patch('%s.os.listdir' % MODULE_NAME, new=Mock(side_effect=[['gridfile1.txt', 'cool/gridfile2.ppt', 'last/file/ok'], []])), \
         patch('%s.os.path.isdir' % MODULE_NAME, new=Mock(return_value=True)), \
         patch('%s.glob.glob' % MODULE_NAME, new=Mock(side_effect=[['file1.grb', 'otherfile.grb'], ['testfile.grc']])), \
         patch('%s.os.path.exists' % MODULE_NAME, new=Mock(side_effect=lambda path: exists_dict[path])) as exists_mock, \
         patch('%s.ProcessList' % MODULE_NAME, new=proclist_mock), \
         patch('%s.WhizardAnalysis.setApplicationStatus' % MODULE_NAME) as appstat_mock, \
         patch('%s.shutil.copy' % MODULE_NAME, new=Mock(side_effect=EnvironmentError('some_err_msg_test'))):
      assertDiracFailsWith(self.wha.runIt(),
                            'failed to obtain mywhizardtestfile.in', self)
      getops_mock.getValue.assert_called_once_with('/ProcessList/Location', '')
      exists_mock.assert_called_once_with('list.txt')
      appstat_mock.assert_called_once_with('Failed getting whizard.in file')

  def test_runit_changeandreturn_fails(self):
    exists_dict = {'list.txt': True, 'LesHouches.msugra_1.in': True}
    self.wha.Model = 'mytestMODEL'
    self.wha.getProcessInFile = True
    self.wha.optionsdict = 9834
    self.wha.useGridFiles = True
    genmodel_mock = Mock()
    self.wha.genmodel = genmodel_mock
    changeandret_mock = Mock()
    changeandret_mock.changeAndReturn.return_value = S_ERROR('changeandret_err_testme')
    whiz_options_mock = Mock(return_value=changeandret_mock)
    getops_mock = Mock()
    getops_mock.getValue.return_value = '/my/process/list/list.txt'
    self.wha.ops = getops_mock
    method_mock = Mock()
    method_mock.getInFile.return_value = 'mywhizardTestFile.in'
    proclist_mock = Mock(return_value=method_mock)
    with patch('%s.getSoftwareFolder' % MODULE_NAME, new=Mock(side_effect=[S_OK('my/test/soft/dir'), S_OK('/my/test/dep/ignorethis'), S_OK('mygridfiles/folder'), S_OK('/spectra/files')])), \
         patch('%s.removeLibc' % MODULE_NAME, new=Mock(return_value=True)), \
         patch('%s.getNewLDLibs' % MODULE_NAME, new=Mock(return_value='my/lib/path')), \
         patch('%s.resolveDeps' % MODULE_NAME, new=Mock(return_value=[{'app': 'mytestdep', 'version': '4.2'}, {'app': 'gridfiles', 'version': '1.0'}, {'app': 'beam_spectra', 'version': '20.3'}])), \
         patch.dict('os.environ', {}, True), \
         patch('%s.os.listdir' % MODULE_NAME, new=Mock(side_effect=[['gridfile1.txt', 'cool/gridfile2.ppt', 'last/file/ok'], []])), \
         patch('%s.os.path.isdir' % MODULE_NAME, new=Mock(return_value=True)), \
         patch('%s.glob.glob' % MODULE_NAME, new=Mock(side_effect=[['file1.grb', 'otherfile.grb'], ['testfile.grc']])), \
         patch('%s.os.path.exists' % MODULE_NAME, new=Mock(side_effect=lambda path: exists_dict[path])) as exists_mock, \
         patch('%s.ProcessList' % MODULE_NAME, new=proclist_mock), \
         patch('%s.WhizardAnalysis.setApplicationStatus' % MODULE_NAME) as appstat_mock, \
         patch('%s.shutil.copy' % MODULE_NAME, new=Mock(return_value=True)) as copy_mock, \
         patch('%s.WhizardOptions' % MODULE_NAME, new=whiz_options_mock):
      assertDiracFailsWith(self.wha.runIt(), 'changeandret_err_testme', self)
      getops_mock.getValue.assert_called_once_with('/ProcessList/Location', '')
      assertMockCalls(exists_mock, ['list.txt', 'LesHouches.msugra_1.in'], self)
      self.assertFalse(appstat_mock.called)
      copy_mock.assert_called_once_with('my/test/soft/dir/mywhizardTestFile.in',
                                         './whizardnew.in')
      self.assertFalse(genmodel_mock.called)
      changeandret_mock.changeAndReturn.assert_called_once_with(9834)

  def test_runit_prepareWhizardFile_fails(self):
    exists_dict = {'list.txt': True, 'LesHouches.msugra_1.in': True}
    self.wha.Lumi = 'mytestluminosity'
    self.wha.Model = True
    self.wha.NumberOfEvents = 'myTestNumber'
    self.wha.RandomSeed = 'notRandomTestme'
    self.wha.energy = '100TestTeV'
    self.wha.evttype = 'myTestEvent'
    self.wha.getProcessInFile = True
    self.wha.optionsdict = False
    self.wha.susymodel = False
    self.wha.template = False
    self.wha.useGridFiles = True
    genmodel_mock = Mock()
    self.wha.genmodel = genmodel_mock
    getops_mock = Mock()
    getops_mock.getValue.return_value = '/my/process/list/list.txt'
    self.wha.ops = getops_mock
    method_mock = Mock()
    method_mock.getInFile.return_value = 'mywhizardTestFile.in'
    proclist_mock = Mock(return_value=method_mock)
    with patch('%s.getSoftwareFolder' % MODULE_NAME, new=Mock(side_effect=[S_OK('my/test/soft/dir'), S_OK('/my/test/dep/ignorethis'), S_OK('mygridfiles/folder'), S_OK('/spectra/files')])), \
         patch('%s.removeLibc' % MODULE_NAME, new=Mock(return_value=True)), \
         patch('%s.getNewLDLibs' % MODULE_NAME, new=Mock(return_value='my/lib/path')), \
         patch('%s.resolveDeps' % MODULE_NAME, new=Mock(return_value=[{'app': 'mytestdep', 'version': '4.2'}, {'app': 'gridfiles', 'version': '1.0'}, {'app': 'beam_spectra', 'version': '20.3'}])), \
         patch.dict('os.environ', {}, True), \
         patch('%s.os.listdir' % MODULE_NAME, new=Mock(side_effect=[['gridfile1.txt', 'cool/gridfile2.ppt', 'last/file/ok'], []])), \
         patch('%s.os.path.isdir' % MODULE_NAME, new=Mock(return_value=True)), \
         patch('%s.glob.glob' % MODULE_NAME, new=Mock(side_effect=[['file1.grb', 'otherfile.grb'], ['testfile.grc']])), \
         patch('%s.os.path.exists' % MODULE_NAME, new=Mock(side_effect=lambda path: exists_dict[path])) as exists_mock, \
         patch('%s.ProcessList' % MODULE_NAME, new=proclist_mock), \
         patch('%s.WhizardAnalysis.setApplicationStatus' % MODULE_NAME) as appstat_mock, \
         patch('%s.shutil.copy' % MODULE_NAME, new=Mock(return_value=True)) as copy_mock, \
         patch('%s.prepareWhizardFile' % MODULE_NAME, new=Mock(return_value=S_ERROR('preparewhiz_no_template_test_err'))) as preparefile_mock:
      assertDiracFailsWith(self.wha.runIt(),
                            'something went wrong with whizard.in file generation',
                            self)
      getops_mock.getValue.assert_called_once_with('/ProcessList/Location', '')
      exists_mock.assert_any_call('list.txt')
      exists_mock.assert_any_call('LesHouches.msugra_1.in')
      assertEqualsImproved(len(exists_mock.mock_calls), 2, self)
      appstat_mock.assert_called_once_with(
          'Whizard: something went wrong with input file generation')
      copy_mock.assert_called_once_with('my/test/soft/dir/mywhizardTestFile.in',
                                         './whizardnew.in')
      self.assertFalse(genmodel_mock.called)
      preparefile_mock.assert_called_once_with(
          'whizardnew.in', 'myTestEvent', '100TestTeV', 'notRandomTestme',
          'myTestNumber', 'mytestluminosity', 'whizard.in')

  def test_runit_prepareWhizardFileTemplate_fails(self):
    exists_dict = {'list.txt': True, 'LesHouches.msugra_1.in': True}
    self.wha.Model = True
    self.wha.SteeringFile = 'templateTestme123'
    self.wha.evttype = 'myTestEvent'
    self.wha.getProcessInFile = True
    self.wha.optionsdict = False
    self.wha.parameters = 'myTESTParams'
    self.wha.susymodel = False
    self.wha.template = True
    self.wha.useGridFiles = True
    genmodel_mock = Mock()
    self.wha.genmodel = genmodel_mock
    getops_mock = Mock()
    getops_mock.getValue.return_value = '/my/process/list/list.txt'
    self.wha.ops = getops_mock
    method_mock = Mock()
    method_mock.getInFile.return_value = 'mywhizardTestFile.in'
    proclist_mock = Mock(return_value=method_mock)
    with patch('%s.getSoftwareFolder' % MODULE_NAME, new=Mock(side_effect=[S_OK('my/test/soft/dir'), S_OK('/my/test/dep/ignorethis'), S_OK('mygridfiles/folder'), S_OK('/spectra/files')])), \
         patch('%s.removeLibc' % MODULE_NAME, new=Mock(return_value=True)), \
         patch('%s.getNewLDLibs' % MODULE_NAME, new=Mock(return_value='my/lib/path')), \
         patch('%s.resolveDeps' % MODULE_NAME, new=Mock(return_value=[{'app': 'mytestdep', 'version': '4.2'}, {'app': 'gridfiles', 'version': '1.0'}, {'app': 'beam_spectra', 'version': '20.3'}])), \
         patch.dict('os.environ', {}, True), \
         patch('%s.os.listdir' % MODULE_NAME, new=Mock(side_effect=[['gridfile1.txt', 'cool/gridfile2.ppt', 'last/file/ok'], []])), \
         patch('%s.os.path.isdir' % MODULE_NAME, new=Mock(return_value=True)), \
         patch('%s.glob.glob' % MODULE_NAME, new=Mock(side_effect=[['file1.grb', 'otherfile.grb'], ['testfile.grc']])), \
         patch('%s.os.path.exists' % MODULE_NAME, new=Mock(side_effect=lambda path: exists_dict[path])) as exists_mock, \
         patch('%s.ProcessList' % MODULE_NAME, new=proclist_mock), \
         patch('%s.WhizardAnalysis.setApplicationStatus' % MODULE_NAME) as appstat_mock, \
         patch('%s.shutil.copy' % MODULE_NAME, new=Mock(return_value=True)) as copy_mock, \
         patch('%s.prepareWhizardFileTemplate' % MODULE_NAME, new=Mock(return_value=S_ERROR('preparewhiz_no_template_test_err'))) as preparetemplate_mock:
      assertDiracFailsWith(
          self.wha.runIt(), 'something went wrong with whizard.in file generation',
          self)
      getops_mock.getValue.assert_called_once_with('/ProcessList/Location', '')
      exists_mock.assert_any_call('list.txt')
      exists_mock.assert_any_call('LesHouches.msugra_1.in')
      assertEqualsImproved(len(exists_mock.mock_calls), 2, self)
      appstat_mock.assert_called_once_with(
          'Whizard: something went wrong with input file generation')
      copy_mock.assert_called_once_with(
          'my/test/soft/dir/mywhizardTestFile.in', './whizardnew.in')
      self.assertFalse(genmodel_mock.called)
      preparetemplate_mock.assert_called_once_with('whizardnew.in', 'myTestEvent',
                                                   'myTESTParams', 'whizard.in')

  def test_runit_makecut1_fails(self):
    exists_dict = {'list.txt': True, 'LesHouches.msugra_1.in': True,
                    'Whizard_myTestV1_Run_testStep12.sh': True}
    set_default_values(self.wha)
    self.wha.genlevelcuts = {'some_entry': True,
                              'this_dict_is_not_empty': True}
    self.wha.getProcessInFile = True
    genmodel_mock = Mock()
    self.wha.genmodel = genmodel_mock
    whizopts_mock = Mock()
    whizopts_mock.changeAndReturn.return_value = S_OK()
    whizopts_mock.toWhizardDotIn.return_value = S_OK('mytestprocessfindme')
    whiz_options_mock = Mock(return_value=whizopts_mock)
    getops_mock = Mock()
    getops_mock.getValue.return_value = '/my/process/list/list.txt'
    self.wha.ops = getops_mock
    method_mock = Mock()
    method_mock.getInFile.return_value = 'mywhizardTestFile.in'
    proclist_mock = Mock(return_value=method_mock)
    expected_calls = [
        [call('#!/bin/sh \n'), call('#####################################################################\n'),
         call('# Dynamically generated script to run a production or analysis job. #\n'),
         call('#####################################################################\n'),
         call('declare -x PATH=my/test/soft/dir:$PATH\n'),
         call('declare -x LD_LIBRARY_PATH=my/test/soft/dir/lib:my/lib/path\n'),
         call('env | sort >> localEnv.log\n'),
         call('echo =============================\n'),
         call('echo Printing content of whizard.in \n'),
         call('cat whizard.in\n'),
         call('echo =============================\n'),
         call('cp  my/test/soft/dir/whizard.mdl ./\n'),
         call('ln -s LesHouches.msugra_1.in fort.71\n'),
         call('cp file1.grb ./\n'), call('cp otherfile.grb ./\n'),
         call('cp testfile.grc ./\n'),
         call('cp my/test/soft/dir/whizard.prc ./\n')]]
    with patch('%s.getSoftwareFolder' % MODULE_NAME, new=Mock(side_effect=[S_OK('my/test/soft/dir'), S_OK('/my/test/dep/ignorethis'), S_OK('mygridfiles/folder'), S_OK('/spectra/files')])), \
         patch('%s.removeLibc' % MODULE_NAME, new=Mock(return_value=True)), \
         patch('%s.getNewLDLibs' % MODULE_NAME, new=Mock(return_value='my/lib/path')), \
         patch('%s.resolveDeps' % MODULE_NAME, new=Mock(return_value=[{'app': 'mytestdep', 'version': '4.2'}, {'app': 'gridfiles', 'version': '1.0'}, {'app': 'beam_spectra', 'version': '20.3'}])), \
         patch.dict('os.environ', {}, True), \
         patch('%s.os.listdir' % MODULE_NAME, new=Mock(side_effect=[['gridfile1.txt', 'cool/gridfile2.ppt', 'last/file/ok'], []])), \
         patch('%s.os.path.isdir' % MODULE_NAME, new=Mock(return_value=True)), \
         patch('%s.glob.glob' % MODULE_NAME, new=Mock(side_effect=[['file1.grb', 'otherfile.grb'], ['testfile.grc']])), \
         patch('%s.os.path.exists' % MODULE_NAME, new=Mock(side_effect=lambda path: exists_dict[path])) as exists_mock, \
         patch('%s.ProcessList' % MODULE_NAME, new=proclist_mock), \
         patch('%s.WhizardAnalysis.setApplicationStatus' % MODULE_NAME) as appstat_mock, \
         patch('%s.shutil.copy' % MODULE_NAME, new=Mock(return_value=True)) as copy_mock, \
         patch('%s.WhizardOptions' % MODULE_NAME, new=whiz_options_mock), \
         patch('%s.os.remove' % MODULE_NAME, new=Mock(return_value=True)) as remove_mock, \
         patch('%s.open' % MODULE_NAME, mock_open()) as open_mock, \
         patch('%s.WhizardAnalysis.makeWhizardDotCut1' % MODULE_NAME, new=Mock(return_value=S_ERROR())):
      # FIXME: makeWhizardDotCut1 currently cant fail (although it operates on files?!)
      result = self.wha.runIt()
      assertDiracFailsWith(result, 'could not create the cut1 file', self)
      open_mock.assert_called_once_with('Whizard_myTestV1_Run_testStep12.sh', 'w')
      rename_mock = Mock()
      chmod_mock = Mock()
      glob_mock = Mock()
      shell_mock = Mock()
      handles = [open_mock()]
      expected_appstat = []
      expected_rename = []
      expected_chmod = []
      expected_glob = []
      expected_shell = []
      expected_copy = [call('my/test/soft/dir/mywhizardTestFile.in',
                              './whizardnew.in')]
      expected_genmodel = []
      expected_getops = [call.getValue('/ProcessList/Location', '')]
      expected_remove = [call('Whizard_myTestV1_Run_testStep12.sh')]
      expected_exists = [
          call('list.txt'), call('LesHouches.msugra_1.in'),
          call('Whizard_myTestV1_Run_testStep12.sh')]
      check_runit_for_parameters(self, whiz_options_mock, getops_mock,
                                  genmodel_mock, expected_calls, handles,
                                  appstat_mock, exists_mock, rename_mock,
                                  chmod_mock, glob_mock, shell_mock, copy_mock,
                                  remove_mock, open_mock, expected_appstat,
                                  expected_exists, expected_rename, expected_chmod,
                                  expected_glob, expected_shell, expected_copy,
                                  expected_genmodel, expected_getops,
                                  expected_remove)

  def test_runit_noapplog_created(self):
    exists_dict = {'list.txt': True, 'LesHouches.msugra_1.in': True,
                    'Whizard_myTestV1_Run_testStep12.sh': True,
                    'mytestAppLOg': True}

    def replace_exists(path):
      result = exists_dict[path]
      if path == 'mytestAppLOg':
        exists_dict[path] = False
      return result
    self.wha.Model = 'mytestMODEL'
    self.wha.STEP_NUMBER = 'testStep12'
    self.wha.applicationLog = 'mytestAppLOg'
    self.wha.applicationVersion = 'myTestV1'
    self.wha.debug = False
    self.wha.evttype = 'myTestEvents'
    self.wha.extraCLIarguments = 'extraTestCLIargs'
    self.wha.genlevelcuts = False
    self.wha.getProcessInFile = True
    self.wha.ignoreapperrors = False
    self.wha.optionsdict = 9834
    self.wha.useGridFiles = True
    genmodel_mock = Mock()
    self.wha.genmodel = genmodel_mock
    whizopts_mock = Mock()
    whizopts_mock.changeAndReturn.return_value = S_OK()
    whizopts_mock.toWhizardDotIn.return_value = S_OK('mytestprocessfindme')
    whiz_options_mock = Mock(return_value=whizopts_mock)
    getops_mock = Mock()
    getops_mock.getValue.return_value = '/my/process/list/list.txt'
    self.wha.ops = getops_mock
    method_mock = Mock()
    method_mock.getInFile.return_value = 'mywhizardTestFile.in'
    proclist_mock = Mock(return_value=method_mock)
    with patch('%s.getSoftwareFolder' % MODULE_NAME, new=Mock(side_effect=[S_OK('my/test/soft/dir'), S_OK('/my/test/dep/ignorethis'), S_OK('mygridfiles/folder'), S_OK('/spectra/files')])), \
         patch('%s.removeLibc' % MODULE_NAME, new=Mock(return_value=True)), \
         patch('%s.getNewLDLibs' % MODULE_NAME, new=Mock(return_value='my/lib/path')), \
         patch('%s.resolveDeps' % MODULE_NAME, new=Mock(return_value=[{'app': 'mytestdep', 'version': '4.2'}, {'app': 'gridfiles', 'version': '1.0'}, {'app': 'beam_spectra', 'version': '20.3'}])), \
         patch.dict('os.environ', {}, True), \
         patch('%s.os.listdir' % MODULE_NAME, new=Mock(side_effect=[['gridfile1.txt', 'cool/gridfile2.ppt', 'last/file/ok'], []])), \
         patch('%s.os.path.isdir' % MODULE_NAME, new=Mock(return_value=True)), \
         patch('%s.glob.glob' % MODULE_NAME, new=Mock(side_effect=[['file1.grb', 'otherfile.grb'], ['testfile.grc']])), \
         patch('%s.os.path.exists' % MODULE_NAME, new=Mock(side_effect=replace_exists)) as exists_mock, \
         patch('%s.ProcessList' % MODULE_NAME, new=proclist_mock), \
         patch('%s.WhizardAnalysis.setApplicationStatus' % MODULE_NAME) as appstat_mock, \
         patch('%s.shutil.copy' % MODULE_NAME, new=Mock(return_value=True)) as copy_mock, \
         patch('%s.WhizardOptions' % MODULE_NAME, new=whiz_options_mock), \
         patch('%s.os.remove' % MODULE_NAME, new=Mock(return_value=True)) as remove_mock, \
         patch('%s.open' % MODULE_NAME, mock_open()) as open_mock, \
         patch('%s.WhizardAnalysis.makeWhizardDotCut1' % MODULE_NAME, new=Mock(return_value=S_OK())), \
         patch('%s.os.chmod' % MODULE_NAME) as chmod_mock, \
         patch('%s.shellCall' % MODULE_NAME, new=Mock(return_value=S_ERROR())) as shell_mock:
      # FIXME: makeWhizardDotCut1 currently cant fail (although it operates on files?!)
      assertDiracFailsWith(self.wha.runIt(), 'whizard did not produce the expected log', self)
      getops_mock.getValue.assert_called_once_with('/ProcessList/Location', '')
      assertMockCalls(exists_mock, ['list.txt', 'LesHouches.msugra_1.in',
                                      'Whizard_myTestV1_Run_testStep12.sh', 'mytestAppLOg',
                                      'mytestAppLOg'], self)
      assertMockCalls(remove_mock, ['Whizard_myTestV1_Run_testStep12.sh', 'mytestAppLOg'], self)
      assertMockCalls(appstat_mock, ['Whizard myTestV1 step testStep12',
                                       'whizard failed terribly, you are doomed!'], self)
      copy_mock.assert_called_once_with('my/test/soft/dir/mywhizardTestFile.in',
                                         './whizardnew.in')
      self.assertFalse(genmodel_mock.called)
      whizopts_mock.changeAndReturn.assert_called_once_with(9834)
      whizopts_mock.toWhizardDotIn.assert_called_once_with('whizard.in')
      assertMockCalls(remove_mock, ['Whizard_myTestV1_Run_testStep12.sh', 'mytestAppLOg'], self)
      open_mock.assert_called_once_with('Whizard_myTestV1_Run_testStep12.sh', 'w')
      assertMockCalls(open_mock().write, [
          '#!/bin/sh \n', '#####################################################################\n',
          '# Dynamically generated script to run a production or analysis job. #\n',
          '#####################################################################\n',
          'declare -x PATH=my/test/soft/dir:$PATH\n',
          'declare -x LD_LIBRARY_PATH=my/test/soft/dir/lib:my/lib/path\n', 'env | sort >> localEnv.log\n',
          'echo =============================\n', 'echo Printing content of whizard.in \n', 'cat whizard.in\n',
          'echo =============================\n', 'cp  my/test/soft/dir/whizard.mdl ./\n',
          'ln -s LesHouches.msugra_1.in fort.71\n', 'cp file1.grb ./\n', 'cp otherfile.grb ./\n',
          'cp testfile.grc ./\n', 'cp my/test/soft/dir/whizard.prc ./\n', 'echo =============================\n',
          'echo Printing content of whizard.prc \n', 'cat whizard.prc\n', 'echo =============================\n',
          'whizard --simulation_input \'write_events_file = \"myTestEvents\"\' extraTestCLIargs 2>/dev/null\n',
          'declare -x appstatus=$?\n', 'exit $appstatus\n'], self)
      chmod_mock.assert_called_once_with('Whizard_myTestV1_Run_testStep12.sh',
                                          0o755)
      shell_mock.assert_called_once_with(0, 'sh -c "./Whizard_myTestV1_Run_testStep12.sh"',
                                          callbackFunction=self.wha.redirectLogOutput,
                                          bufferLimit=209715200)

  def test_runit_no_outputfile(self):
    exists_dict = {'list.txt': True, 'LesHouches.msugra_1.in': True,
                    'Whizard_myTestV1_Run_testStep12.sh': True,
                    'mytestAppLOg': True, 'whizard.out': False,
                    'myTestEvents.001.stdhep': False}
    self.wha.Model = 'mytestMODEL'
    self.wha.OutputFile = 'mytestwhizardOutputFile'
    self.wha.STEP_NUMBER = 'testStep12'
    self.wha.applicationLog = 'mytestAppLOg'
    self.wha.applicationVersion = 'myTestV1'
    self.wha.debug = False
    self.wha.evttype = 'myTestEvents'
    self.wha.extraCLIarguments = 'extraTestCLIargs'
    self.wha.genlevelcuts = False
    self.wha.getProcessInFile = True
    self.wha.ignoreapperrors = False
    self.wha.optionsdict = 9834
    self.wha.useGridFiles = True
    genmodel_mock = Mock()
    self.wha.genmodel = genmodel_mock
    whizopts_mock = Mock()
    whizopts_mock.changeAndReturn.return_value = S_OK()
    whizopts_mock.toWhizardDotIn.return_value = S_OK('mytestprocessfindme')
    whizopts_mock.getAsDict.return_value = S_OK('this shouldnt be used')
    whiz_options_mock = Mock(return_value=whizopts_mock)
    getops_mock = Mock()
    getops_mock.getValue.return_value = '/my/process/list/list.txt'
    self.wha.ops = getops_mock
    method_mock = Mock()
    method_mock.getInFile.return_value = 'mywhizardTestFile.in'
    proclist_mock = Mock(return_value=method_mock)
    file_contents = [[], ['! Event sample corresponds to luminosity 4565.3',
                          'some_logging_ignoreme', 'Event generation finished. Success!']]
    handles = FileUtil.getMultipleReadHandles(file_contents)
    with patch('%s.getSoftwareFolder' % MODULE_NAME, new=Mock(side_effect=[S_OK('my/test/soft/dir'), S_OK('/my/test/dep/ignorethis'), S_OK('mygridfiles/folder'), S_OK('/spectra/files')])), \
         patch('%s.removeLibc' % MODULE_NAME, new=Mock(return_value=True)), \
         patch('%s.getNewLDLibs' % MODULE_NAME, new=Mock(return_value='my/lib/path')), \
         patch('%s.resolveDeps' % MODULE_NAME, new=Mock(return_value=[{'app': 'mytestdep', 'version': '4.2'}, {'app': 'gridfiles', 'version': '1.0'}, {'app': 'beam_spectra', 'version': '20.3'}])), \
         patch.dict('os.environ', {}, True), \
         patch('%s.os.listdir' % MODULE_NAME, new=Mock(side_effect=[['gridfile1.txt', 'cool/gridfile2.ppt', 'last/file/ok'], []])), \
         patch('%s.os.path.isdir' % MODULE_NAME, new=Mock(return_value=True)), \
         patch('%s.glob.glob' % MODULE_NAME, new=Mock(side_effect=[['file1.grb', 'otherfile.grb'], ['testfile.grc']])), \
         patch('%s.os.path.exists' % MODULE_NAME, new=Mock(side_effect=lambda path: exists_dict[path])) as exists_mock, \
         patch('%s.ProcessList' % MODULE_NAME, new=proclist_mock), \
         patch('%s.WhizardAnalysis.setApplicationStatus' % MODULE_NAME) as appstat_mock, \
         patch('%s.shutil.copy' % MODULE_NAME, new=Mock(return_value=True)) as copy_mock, \
         patch('%s.WhizardOptions' % MODULE_NAME, new=whiz_options_mock), \
         patch('%s.os.remove' % MODULE_NAME, new=Mock(return_value=True)) as remove_mock, \
         patch('%s.open' % MODULE_NAME, mock_open(), create=True) as open_mock, \
         patch('%s.WhizardAnalysis.makeWhizardDotCut1' % MODULE_NAME, new=Mock(return_value=S_OK())), \
         patch('%s.os.chmod' % MODULE_NAME) as chmod_mock, \
         patch('%s.shellCall' % MODULE_NAME, new=Mock(return_value=S_OK())) as shell_mock:
      open_mock.side_effect = (h for h in handles)
      assertDiracFailsWith(self.wha.runIt(), 'whizard Failed to produce STDHEP file',
                            self)
      getops_mock.getValue.assert_called_once_with('/ProcessList/Location', '')
      assertEqualsImproved(len(exists_mock.mock_calls), 7, self)
      assertMockCalls(remove_mock, ['Whizard_myTestV1_Run_testStep12.sh', 'mytestAppLOg'], self)
      assertMockCalls(appstat_mock, ['Whizard myTestV1 step testStep12',
                                       'Whizard myTestV1 Failed to produce STDHEP file'], self)
      copy_mock.assert_called_once_with('my/test/soft/dir/mywhizardTestFile.in',
                                         './whizardnew.in')
      self.assertFalse(genmodel_mock.called)
      whizopts_mock.changeAndReturn.assert_called_once_with(9834)
      whizopts_mock.toWhizardDotIn.assert_called_once_with('whizard.in')
      assertMockCalls(remove_mock, ['Whizard_myTestV1_Run_testStep12.sh', 'mytestAppLOg'], self)
      assertMockCalls(open_mock, [('Whizard_myTestV1_Run_testStep12.sh', 'w'), 'mytestAppLOg'], self)
      expected_calls = [
          [call('#!/bin/sh \n'),
           call('#####################################################################\n'),
           call('# Dynamically generated script to run a production or analysis job. #\n'),
           call('#####################################################################\n'),
           call('declare -x PATH=my/test/soft/dir:$PATH\n'),
           call('declare -x LD_LIBRARY_PATH=my/test/soft/dir/lib:my/lib/path\n'),
           call('env | sort >> localEnv.log\n'), call('echo =============================\n'),
           call('echo Printing content of whizard.in \n'), call('cat whizard.in\n'),
           call('echo =============================\n'),
           call('cp  my/test/soft/dir/whizard.mdl ./\n'),
           call('ln -s LesHouches.msugra_1.in fort.71\n'), call('cp file1.grb ./\n'),
           call('cp otherfile.grb ./\n'), call('cp testfile.grc ./\n'),
           call('cp my/test/soft/dir/whizard.prc ./\n'),
           call('echo =============================\n'),
           call('echo Printing content of whizard.prc \n'), call('cat whizard.prc\n'),
           call('echo =============================\n'),
           call('whizard --simulation_input \'write_events_file = \"myTestEvents\"\' extraTestCLIargs 2>/dev/null\n'),
           call('declare -x appstatus=$?\n'), call('exit $appstatus\n')], []]
      assertEqualsImproved(len(expected_calls), len(handles), self)
      for (expected, handle) in zip(expected_calls, handles):
        assertEqualsImproved(handle.write.mock_calls, expected, self)
      chmod_mock.assert_called_once_with('Whizard_myTestV1_Run_testStep12.sh',
                                          0o755)
      shell_mock.assert_called_once_with(0, 'sh -c "./Whizard_myTestV1_Run_testStep12.sh"',
                                          callbackFunction=self.wha.redirectLogOutput,
                                          bufferLimit=209715200)
      whizopts_mock.getAsDict.assert_called_once_with()
      assertEqualsImproved(self.wha.workflow_commons['Luminosity'],
                            4565.3, self)

  def test_log_contains_error(self):
    file_contents = [[], ['! Event sample corresponds to luminosity 4565.3',
                            '*** Fatal error: mytesterror']]
    check_logfiles(file_contents, self)

  def test_log_contains_error_1(self):
    file_contents = [[], ['! Event sample corresponds to luminosity 4565.3',
                            'PYSTOP']]
    check_logfiles(file_contents, self)

  def test_log_contains_error_2(self):
    file_contents = [[], ['! Event sample corresponds to luminosity 4565.3',
                            'No matrix element available']]
    check_logfiles(file_contents, self)

  def test_log_contains_error_3(self):
    file_contents = [[], ['! Event sample corresponds to luminosity 4565.3',
                            'Floating point exception']]
    check_logfiles(file_contents, self)

  def test_makeWhizardDotCut(self):
    self.wha.genlevelcuts = {'myprocess': ['importantvalue', 'dontmissme'],
                              'key': [], 'param': ['myparam', 'electron',
                                                      'myparam']}
    with patch('%s.open' % MODULE_NAME, mock_open(), create=True) as open_mock:
      assertDiracSucceeds(self.wha.makeWhizardDotCut1(), self)
      open_mock.assert_called_once_with('whizard.cut1', 'w')
      open_mock = open_mock()
      assertMockCalls(open_mock.write, ['process myprocess\n', '  importantvalue\n',
                                          '  dontmissme\n', 'process key\n', 'process param\n',
                                          '  myparam\n', '  electron\n', '  myparam\n'], self)
      open_mock.close.assert_called_once_with()


def check_lists_equal(list1, list2, assertobject):
  """Checks if two lists are permutations of each other."""
  assertEqualsImproved(len(list1), len(list2), assertobject)
  for element in list1:
    assertobject.assertIn(element, list2)


def check_logfiles(file_contents, assertobject):
  exists_dict = {'list.txt': True, 'LesHouches.msugra_1.in': True,
                  'Whizard_myTestV1_Run_testStep12.sh': True,
                  'mytestAppLOg': True, 'whizard.out': False}
  set_default_values(assertobject.wha)
  assertobject.wha.debug = False
  assertobject.wha.genlevelcuts = False
  assertobject.wha.getProcessInFile = True
  genmodel_mock = Mock()
  assertobject.wha.genmodel = genmodel_mock
  whizopts_mock = Mock()
  whizopts_mock.changeAndReturn.return_value = S_OK()
  whizopts_mock.toWhizardDotIn.return_value = S_OK('mytestprocessfindme')
  whizopts_mock.getAsDict.return_value = S_OK('this shouldnt be used')
  whiz_options_mock = Mock(return_value=whizopts_mock)
  getops_mock = Mock()
  getops_mock.getValue.return_value = '/my/process/list/list.txt'
  assertobject.wha.ops = getops_mock
  method_mock = Mock()
  method_mock.getInFile.return_value = 'mywhizardTestFile.in'
  proclist_mock = Mock(return_value=method_mock)
  handles = FileUtil.getMultipleReadHandles(file_contents)
  with patch('%s.getSoftwareFolder' % MODULE_NAME, new=Mock(side_effect=[S_OK('my/test/soft/dir'), S_OK('/my/test/dep/ignorethis'), S_OK('mygridfiles/folder'), S_OK('/spectra/files')])), \
       patch('%s.removeLibc' % MODULE_NAME, new=Mock(return_value=True)), \
       patch('%s.getNewLDLibs' % MODULE_NAME, new=Mock(return_value='my/lib/path')), \
       patch('%s.resolveDeps' % MODULE_NAME, new=Mock(return_value=[{'app': 'mytestdep', 'version': '4.2'}, {'app': 'gridfiles', 'version': '1.0'}, {'app': 'beam_spectra', 'version': '20.3'}])), \
       patch.dict('os.environ', {}, True), \
       patch('%s.os.listdir' % MODULE_NAME, new=Mock(side_effect=[['gridfile1.txt', 'cool/gridfile2.ppt', 'last/file/ok'], []])), \
       patch('%s.os.path.isdir' % MODULE_NAME, new=Mock(return_value=True)), \
       patch('%s.glob.glob' % MODULE_NAME, new=Mock(side_effect=[['file1.grb', 'otherfile.grb'], ['testfile.grc']])), \
       patch('%s.os.path.exists' % MODULE_NAME, new=Mock(side_effect=lambda path: exists_dict[path])) as exists_mock, \
       patch('%s.ProcessList' % MODULE_NAME, new=proclist_mock), \
       patch('%s.WhizardAnalysis.setApplicationStatus' % MODULE_NAME) as appstat_mock, \
       patch('%s.shutil.copy' % MODULE_NAME, new=Mock(return_value=True)) as copy_mock, \
       patch('%s.WhizardOptions' % MODULE_NAME, new=whiz_options_mock), \
       patch('%s.os.remove' % MODULE_NAME, new=Mock(return_value=True)) as remove_mock, \
       patch('%s.open' % MODULE_NAME, mock_open(), create=True) as open_mock, \
       patch('%s.WhizardAnalysis.makeWhizardDotCut1' % MODULE_NAME, new=Mock(return_value=S_OK())), \
       patch('%s.os.chmod' % MODULE_NAME) as chmod_mock, \
       patch('%s.shellCall' % MODULE_NAME, new=Mock(return_value=S_OK())) as shell_mock:
    open_mock.side_effect = (h for h in handles)
    assertDiracFailsWith(assertobject.wha.runIt(),
                          'Whizard Exited With Status 1', assertobject)
    getops_mock.getValue.assert_called_once_with('/ProcessList/Location', '')
    assertEqualsImproved(len(exists_mock.mock_calls), 6, assertobject)
    assertMockCalls(remove_mock, ['Whizard_myTestV1_Run_testStep12.sh', 'mytestAppLOg'], assertobject)
    assertMockCalls(appstat_mock, ['Whizard myTestV1 step testStep12', 'whizard Exited With Status 1'],
                     assertobject)
    copy_mock.assert_called_once_with('my/test/soft/dir/mywhizardTestFile.in',
                                       './whizardnew.in')
    assertobject.assertFalse(genmodel_mock.called)
    whizopts_mock.changeAndReturn.assert_called_once_with(9834)
    whizopts_mock.toWhizardDotIn.assert_called_once_with('whizard.in')
    assertMockCalls(remove_mock, ['Whizard_myTestV1_Run_testStep12.sh', 'mytestAppLOg'], assertobject)
    assertMockCalls(open_mock, [('Whizard_myTestV1_Run_testStep12.sh', 'w'), 'mytestAppLOg'], assertobject)
    expected_calls = [[
        call('#!/bin/sh \n'),
        call('#####################################################################\n'),
        call('# Dynamically generated script to run a production or analysis job. #\n'),
        call('#####################################################################\n'),
        call('declare -x PATH=my/test/soft/dir:$PATH\n'),
        call('declare -x LD_LIBRARY_PATH=my/test/soft/dir/lib:my/lib/path\n'),
        call('env | sort >> localEnv.log\n'), call('echo =============================\n'),
        call('echo Printing content of whizard.in \n'), call('cat whizard.in\n'),
        call('echo =============================\n'), call('cp  my/test/soft/dir/whizard.mdl ./\n'),
        call('ln -s LesHouches.msugra_1.in fort.71\n'), call('cp file1.grb ./\n'),
        call('cp otherfile.grb ./\n'), call('cp testfile.grc ./\n'),
        call('cp my/test/soft/dir/whizard.prc ./\n'), call('echo =============================\n'),
        call('echo Printing content of whizard.prc \n'), call('cat whizard.prc\n'),
        call('echo =============================\n'),
        call('whizard --simulation_input \'write_events_file = \"myTestEvents\"\' extraTestCLIargs 2>/dev/null\n'),
        call('declare -x appstatus=$?\n'), call('exit $appstatus\n')], []]
    assertEqualsImproved(len(expected_calls), len(handles), assertobject)
    for (expected, handle) in zip(expected_calls, handles):
      assertEqualsImproved(handle.write.mock_calls, expected, assertobject)
    chmod_mock.assert_called_once_with('Whizard_myTestV1_Run_testStep12.sh',
                                        0o755)
    shell_mock.assert_called_once_with(0, 'sh -c "./Whizard_myTestV1_Run_testStep12.sh"',
                                        callbackFunction=assertobject.wha.redirectLogOutput,
                                        bufferLimit=209715200)
    whizopts_mock.getAsDict.assert_called_once_with()
    assertEqualsImproved(assertobject.wha.workflow_commons['Luminosity'],
                          4565.3, assertobject)


def check_runit_for_parameters(testcaseobject, whiz_options_mock, getops_mock,
                                genmodel_mock, expected_calls, handles,
                                appstat_mock, exists_mock, rename_mock,
                                chmod_mock, glob_mock, shell_mock, copy_mock,
                                remove_mock, open_mock, expected_appstat,
                                expected_exists, expected_rename, expected_chmod,
                                expected_glob, expected_shell, expected_copy,
                                expected_genmodel, expected_getops,
                                expected_remove):  # pylint: disable=unused-argument
  """ Testcaseobject : self in a test method, provides access to assert methods and the WhizardAnalysis object
  exists_replace : Method thats used to mock out os.path.exists
  """
  assertEqualsImproved(len(expected_calls), len(handles), testcaseobject)
  for (expected, handle) in zip(expected_calls, handles):
    assertEqualsImproved(handle.write.mock_calls, expected, testcaseobject)
  assertEqualsImproved(appstat_mock.mock_calls, expected_appstat, testcaseobject)
  assertEqualsImproved(exists_mock.mock_calls, expected_exists, testcaseobject)
  assertEqualsImproved(rename_mock.mock_calls, expected_rename, testcaseobject)
  assertEqualsImproved(chmod_mock.mock_calls, expected_chmod, testcaseobject)
  assertEqualsImproved(glob_mock.mock_calls, expected_glob, testcaseobject)
  assertEqualsImproved(shell_mock.mock_calls, expected_shell, testcaseobject)
  assertEqualsImproved(copy_mock.mock_calls, expected_copy, testcaseobject)
  assertEqualsImproved(genmodel_mock.mock_calls, expected_genmodel, testcaseobject)
  assertEqualsImproved(getops_mock.mock_calls, expected_getops, testcaseobject)
  assertEqualsImproved(remove_mock.mock_calls, expected_remove, testcaseobject)
  whizopts_mock = whiz_options_mock.return_value
  whizopts_mock.changeAndReturn.assert_called_once_with(9834)
  whizopts_mock.toWhizardDotIn.assert_called_once_with('whizard.in')


def set_default_values(whizard_object):
  whizard_object.Model = 'mytestMODEL'
  whizard_object.OutputFile = 'mytestwhizardOutputFile'
  whizard_object.STEP_NUMBER = 'testStep12'
  whizard_object.applicationLog = 'mytestAppLOg'
  whizard_object.applicationVersion = 'myTestV1'
  whizard_object.debug = True
  whizard_object.energy = '99TestTeV'
  whizard_object.evttype = 'myTestEvents'
  whizard_object.extraCLIarguments = 'extraTestCLIargs'
  whizard_object.genlevelcuts = True
  whizard_object.getProcessInFile = False
  whizard_object.ignoreapperrors = False
  whizard_object.optionsdict = 9834
  whizard_object.susymodel = 1
  whizard_object.useGridFiles = True


# TODO Refactor this mess
# TODO Change noapplog to have different leshouches file and no list_of_gridfiles
# TODO add case with empty deps

EXPECTED_TEST_ENVIRON = {'LUMI_LINKER': '/spectra/files/lumi_linker_000',
                          'PHOTONS_B1': '/spectra/files/photons_beam1_linker_000',
                          'PHOTONS_B2': '/spectra/files/photons_beam2_linker_000',
                          'EBEAM': '/spectra/files/ebeam_in_linker_000',
                          'PBEAM': '/spectra/files/pbeam_in_linker_000',
                          'LUMI_EE_LINKER': '/spectra/files/lumi_ee_linker_000',
                          'LUMI_EG_LINKER': '/spectra/files/lumi_eg_linker_000',
                          'LUMI_GE_LINKER': '/spectra/files/lumi_ge_linker_000',
                          'LUMI_GG_LINKER': '/spectra/files/lumi_gg_linker_000'}
