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
"""Run the StdHepCut utility.

Apply a set of cuts on input stdhep files

:since: May 11, 2011
:author: Stephane Poss
"""

from __future__ import absolute_import
import os
import shutil

from DIRAC import S_OK, S_ERROR, gLogger
from DIRAC.Core.Utilities.Subprocess import shellCall

from ILCDIRAC.Workflow.Modules.ModuleBase import ModuleBase
from ILCDIRAC.Core.Utilities.CombinedSoftwareInstallation import getSoftwareFolder
from ILCDIRAC.Core.Utilities.PrepareOptionFiles import getNewLDLibs
from ILCDIRAC.Core.Utilities.FindSteeringFileDir import getSteeringFileDirName
from ILCDIRAC.Core.Utilities.resolvePathsAndNames import getProdFilename

__RCSID__ = '$Id$'
LOG = gLogger.getSubLogger(__name__)


class StdHepCut(ModuleBase):
  """Apply cuts on stdhep files, based on L.

  Weuste utility.
  """

  def __init__(self):
    super(StdHepCut, self).__init__()
    self.applicationName = 'stdhepCut'
    self.STEP_NUMBER = ''
    self.inlineCuts = ""
    self.MaxNbEvts = 0
    self.scriptName = ""
    self.fileMask = '*.stdhep'

  def applicationSpecificInputs(self):

    if not self.OutputFile:
      dircont = os.listdir("./")
      for myfile in dircont:
        if myfile.count(".stdhep"):
          self.OutputFile = myfile.replace(".stdhep", "_reduced.stdhep")
          break
      if not self.OutputFile:
        return S_ERROR("Could not find suitable OutputFile name")

    if "IS_PROD" in self.workflow_commons and self.workflow_commons["IS_PROD"]:
      # self.OutputFile = getProdFilename(self.OutputFile,int(self.workflow_commons["PRODUCTION_ID"]),
      #                                  int(self.workflow_commons["JOB_ID"]))
      if 'ProductionOutputData' in self.workflow_commons:
        outputlist = self.workflow_commons['ProductionOutputData'].split(";")
        for obj in outputlist:
          if obj.lower().count("_gen_"):
            self.OutputFile = os.path.basename(obj)
            break
      else:
        self.OutputFile = getProdFilename(self.OutputFile,
                                          int(self.workflow_commons["PRODUCTION_ID"]),
                                          int(self.workflow_commons["JOB_ID"]))

    LOG.notice("Outputfile: %s" % self.OutputFile)
    if self.inlineCuts:
      cfile = open("cuts_local.txt", "w")
      cfile.write("\n".join(self.inlineCuts.split(";")))
      cfile.close()
      self.SteeringFile = "cuts_local.txt"
    return S_OK()

  def runIt(self):
    """Called from Workflow."""

    if not self.workflowStatus['OK'] or not self.stepStatus['OK']:
      LOG.verbose('Workflow status = %s, step status = %s' % (self.workflowStatus['OK'], self.stepStatus['OK']))
      return S_OK('%s should not proceed as previous step did not end properly' % self.applicationName)

    if not self.OutputFile:
      LOG.error("OutputFile not specified")
      return S_ERROR("OutputFile not specified")

    res = getSoftwareFolder(self.platform, self.applicationName, self.applicationVersion)
    if not res['OK']:
      LOG.error('Application %s was not found in either the local area or shared area' % self.applicationName)
      self.setApplicationStatus('%s: Could not find neither local area not shared area install' % self.applicationName)
      return res
    mySoftDir = res['Value']

    self.SteeringFile = os.path.basename(self.SteeringFile)
    if not os.path.exists(self.SteeringFile):
      LOG.verbose('Getting the steering files directory')
      res = getSteeringFileDirName(self.platform, self.applicationName, self.applicationVersion)
      if not res['OK']:
        LOG.error("Could not locate the steering file directory")
        return res
      steeringfiledirname = res['Value']
      if os.path.exists(os.path.join(steeringfiledirname, self.SteeringFile)):
        try:
          shutil.copy(os.path.join(steeringfiledirname, self.SteeringFile), "./" + self.SteeringFile)
        except EnvironmentError as x:
          LOG.error("Failed to get the cuts file")
          return S_ERROR('Failed to access file %s: %s' % (self.SteeringFile, str(x)))
    cuts = open(self.SteeringFile, "r")
    cutslines = "".join(cuts.readlines())
    cuts.close()
    LOG.verbose("Content of cuts file: ", cutslines)

    # Create the cut specific run script. Overloaded in the StdhepCutJava
    self.prepareScript(mySoftDir)

    if os.path.exists(self.applicationLog):
      os.remove(self.applicationLog)
    os.chmod(self.scriptName, 0o755)
    comm = 'sh -c "./%s"' % (self.scriptName)
    self.setApplicationStatus('%s %s step %s' % (self.applicationName, self.applicationVersion, self.STEP_NUMBER))
    self.stdError = ''
    self.result = shellCall(0, comm, callbackFunction=self.redirectLogOutput, bufferLimit=20971520)
    #self.result = {'OK':True,'Value':(0,'Disabled Execution','')}
    resultTuple = self.result['Value']
    if not os.path.exists(self.applicationLog):
      LOG.error("Something went terribly wrong, the log file is not present")
      self.setApplicationStatus('%s failed terribly, you are doomed!' % (self.applicationName))
      if not self.ignoreapperrors:
        LOG.error('Missing log file')
        return S_ERROR('%s did not produce the expected log' % (self.applicationName))
    status = resultTuple[0]
    # stdOutput = resultTuple[1]
    # stdError = resultTuple[2]
    LOG.info("Status after the application execution is %s" % str(status))

    nbevtswritten = -1
    nbevtspassing = 0
    nbevtsread = 0
    with open(self.applicationLog, 'r') as logf:
      for line in logf:
        line = line.rstrip()
        if line.count('Events kept'):
          nbevtswritten = int(line.split()[-1])
        if line.count('Events passing cuts'):
          nbevtspassing = int(line.split()[-1])
        if line.count('Events total'):
          nbevtsread = int(line.split()[-1])
    if nbevtswritten > 0 and nbevtspassing > 0 and nbevtsread > 0:
      cut_eff = 1. * nbevtspassing / nbevtsread
      LOG.info('Selection cut efficiency : %s%%' % (100 * cut_eff))
      sel_eff = 1. * nbevtswritten / nbevtspassing
      if nbevtswritten < self.MaxNbEvts:
        LOG.error('Not enough events to fill up')
      if 'Luminosity' in self.workflow_commons:
        self.workflow_commons['Luminosity'] = self.workflow_commons['Luminosity'] * sel_eff
      self.workflow_commons['NbOfEvts'] = nbevtswritten
      info = {}
      info['stdhepcut'] = {}
      info['stdhepcut']['Reduction'] = sel_eff
      info['stdhepcut']['CutEfficiency'] = cut_eff
      if 'Info' not in self.workflow_commons:
        self.workflow_commons['Info'] = info
      else:
        self.workflow_commons['Info'].update(info)
    else:
      LOG.error('Not enough events somewhere: read: %s, pass:%s, written:%s' % (nbevtsread, nbevtspassing,
                                                                                     nbevtswritten))
      status = 1

    return self.finalStatusReport(status)

  def prepareScript(self, mySoftDir):
    """Prepare the script."""
    new_ld_lib_path = getNewLDLibs(self.platform, self.applicationName, self.applicationVersion)
    new_ld_lib_path = mySoftDir + "/lib:" + new_ld_lib_path
    if os.path.exists("./lib"):
      new_ld_lib_path = "./lib:" + new_ld_lib_path

    self.scriptName = '%s_%s_Run_%s.sh' % (self.applicationName, self.applicationVersion, self.STEP_NUMBER)
    if os.path.exists(self.scriptName):
      os.remove(self.scriptName)
    script = open(self.scriptName, 'w')
    script.write('#!/bin/sh \n')
    script.write('#####################################################################\n')
    script.write('# Dynamically generated script to run a production or analysis job. #\n')
    script.write('#####################################################################\n')
    script.write('declare -x PATH=%s:$PATH\n' % mySoftDir)
    script.write('declare -x LD_LIBRARY_PATH=%s\n' % new_ld_lib_path)
    script.write('env | sort >> localEnv.log\n')
    script.write('echo =============================\n')
    extraopts = ""
    if self.MaxNbEvts:
      extraopts = '-m %s' % self.MaxNbEvts
    comm = 'stdhepCut %s -o %s -c %s %s\n' % (extraopts, self.OutputFile, self.SteeringFile, self.fileMask)
    LOG.info("Running %s" % comm)
    script.write(comm)
    script.write('declare -x appstatus=$?\n')
    script.write('exit $appstatus\n')
    script.close()
