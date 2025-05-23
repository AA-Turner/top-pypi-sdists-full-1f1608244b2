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
"""Run TOMATO.

:since: Feb 24, 2011

:author: S. Poss
:author: C. B. Lam
"""

from __future__ import absolute_import
import os

from DIRAC import S_OK, S_ERROR, gLogger

from ILCDIRAC.Core.Utilities.CombinedSoftwareInstallation import getSoftwareFolder, getEnvironmentScript
from ILCDIRAC.Workflow.Modules.MarlinAnalysis import MarlinAnalysis
from ILCDIRAC.Core.Utilities.PrepareOptionFiles import prepareTomatoSalad
from ILCDIRAC.Core.Utilities.ResolveDependencies import resolveDeps

__RCSID__ = '$Id$'
LOG = gLogger.getSubLogger(__name__)


class TomatoAnalysis(MarlinAnalysis):
  """Module to run Tomato: the auTOMated Analysis TOol by C.B.

  Lam.
  """

  def __init__(self):
    super(TomatoAnalysis, self).__init__()
    self.applicationName = "Tomato"
    self.collection = ''
    self.InputFile = []

  def applicationSpecificInputs(self):
    """Implement the application specific inputs defined in ModuleBase."""
    if 'Collections' in self.step_commons:
      self.collection = self.step_commons['Collections']

    if 'InputSLCIO' in self.step_commons:
      inputf = self.step_commons["InputSLCIO"]
      if not isinstance(inputf, list):
        inputf = inputf.split(";")
      self.InputFile = inputf

      for files in self.InputData:
        if files.lower().find(".slcio") > -1:
          self.InputFile.append(files)
    return S_OK()

  def runIt(self):
    """Run the module."""
    self.result = S_OK()
    if not self.platform:
      self.result = S_ERROR('No ILC platform selected')
    elif not self.applicationLog:
      self.result = S_ERROR('No Log file provided')
    if not self.result['OK']:
      LOG.error('Failed to resolve input parameters:', self.result['Message'])
      return self.result

    if not self.workflowStatus['OK'] or not self.stepStatus['OK']:
      LOG.verbose('Workflow status = %s, step status = %s' % (self.workflowStatus['OK'], self.stepStatus['OK']))
      return S_OK('%s should not proceed as previous step did not end properly' % self.applicationName)

    res = getEnvironmentScript(self.platform, "tomato", self.applicationVersion, self.getEnvScript)
    if not res["OK"]:
      LOG.error("Failed to get the env for Tomato:", res["Message"])
      return res
    env_script_path = res["Value"]

    res = self.prepareMARLIN_DLL(env_script_path)
    if not res['OK']:
      LOG.error('Failed building MARLIN_DLL: %s' % res['Message'])
      self.setApplicationStatus('Failed to setup MARLIN_DLL')
      return S_ERROR('Something wrong with software installation')

    marlin_dll = res['Value']

    res = self._getInputFiles()
    if not res['OK']:
      LOG.error(res['Message'])
      return res
    listofslcio = res['Value']

    finalXML = 'tomato.xml'
    res = prepareTomatoSalad(None, finalXML, self.OutputFile, listofslcio, self.collection)
    if not res['OK']:
      LOG.error('Could not prepare the Tomato XML: %s' % res['Message'])
      self.setApplicationStatus('Failed to setup Tomato')
      return S_ERROR('Failed to setup Tomato')

    self.result = self.runMarlin(finalXML, env_script_path, marlin_dll)
    if not self.result['OK']:
      LOG.error('Something wrong during running: %s' % self.result['Message'])
      self.setApplicationStatus('Error during running %s' % self.applicationName)
      return S_ERROR('Failed to run %s' % self.applicationName)

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

    return self.finalStatusReport(status)

  def getEnvScript(self, sysconfig, appname, appversion):
    """Called if CVMFS install is not here."""
    res = getSoftwareFolder(sysconfig, appname, appversion)
    if not res['Value']:
      self.setApplicationStatus('Tomato: Could not find neither local area not shared area install')
      return res
    myTomatoDir = res['Value']
    deps = resolveDeps(sysconfig, "tomato", appversion)
    for dep in deps:
      if dep["app"].lower() == 'marlin':
        res = getSoftwareFolder(sysconfig, "marlin", dep["version"])
        if not res['OK']:
          LOG.error('Marlin was not found in software directory')
          return res
        else:
          myMarlinDir = res['Value']
        break

    env_script_name = "TomatoEnv.sh"
    script = open(env_script_name, "w")
    script.write("#!/bin/sh\n")
    script.write('###########################################################\n')
    script.write('# Dynamically generated script to get the Env for Tomato. #\n')
    script.write('###########################################################\n')
    script.write("declare -x PATH=%s/Executable:$PATH\n" % myMarlinDir)
    script.write('declare -x ROOTSYS=%s/ROOT\n' % (myMarlinDir))
    script.write('declare -x LD_LIBRARY_PATH=$ROOTSYS/lib:%s/LDLibs\n' % (myMarlinDir))
    script.write("declare -x LD_LIBRARY_PATH=%s/LDLibs:$LD_LIBRARY_PATH\n" % myTomatoDir)

    script.close()
    return S_OK(os.path.abspath(env_script_name))
