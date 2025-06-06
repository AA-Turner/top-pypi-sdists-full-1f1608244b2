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
"""Run Pythia, but only specific versions (the CDR ttbar ones)

:since:  Jun 3, 2011

:author: Stephane Poss
"""

from __future__ import absolute_import
from DIRAC.Core.Utilities.Subprocess import shellCall
from ILCDIRAC.Workflow.Modules.ModuleBase import ModuleBase, generateRandomString
from ILCDIRAC.Core.Utilities.CombinedSoftwareInstallation import getSoftwareFolder
from ILCDIRAC.Core.Utilities.PrepareOptionFiles import getNewLDLibs
from ILCDIRAC.Core.Utilities.ResolveDependencies import resolveDeps
from ILCDIRAC.Core.Utilities.resolvePathsAndNames import getProdFilename
from DIRAC import gLogger, S_OK, S_ERROR

import os

__RCSID__ = '$Id$'
LOG = gLogger.getSubLogger(__name__)


class PythiaAnalysis(ModuleBase):
  """Run pythia.

  Used for CDR vol2, but not for vol3: easier to produce the files locally.
  """

  def __init__(self):
    super(PythiaAnalysis, self).__init__()
    self.enable = True
    self.STEP_NUMBER = ''
    self.debug = True

  def applicationSpecificInputs(self):

    if 'IS_PROD' in self.workflow_commons:
      if self.workflow_commons["IS_PROD"]:
        # self.OutputFile = getProdFilename(self.OutputFile,int(self.workflow_commons["PRODUCTION_ID"]),
        #                                  int(self.workflow_commons["JOB_ID"]))
        if 'ProductionOutputData' in self.workflow_commons:
          outputlist = self.workflow_commons['ProductionOutputData'].split(";")
          baseoutputfile = self.OutputFile.split(".stdhep")[0]
          for obj in outputlist:
            if obj.count(baseoutputfile):
              self.OutputFile = os.path.basename(obj)
        else:
          self.OutputFile = getProdFilename(self.OutputFile,
                                            int(self.workflow_commons["PRODUCTION_ID"]),
                                            int(self.workflow_commons["JOB_ID"]))

    return S_OK()

  def execute(self):
    """Run the module."""
    self.result = self.resolveInputVariables()
    if not self.platform:
      self.result = S_ERROR('No ILC platform selected')
    elif not self.applicationName:
      self.result = S_ERROR("Pythia version name not given")
    elif not self.applicationLog:
      self.result = S_ERROR('No Log file provided')
    if not self.result['OK']:
      LOG.error("Failed to resolve the input parameters:", self.result["Message"])
      return self.result

    if not self.workflowStatus['OK'] or not self.stepStatus['OK']:
      LOG.verbose('Workflow status = %s, step status = %s' % (self.workflowStatus['OK'], self.stepStatus['OK']))
      return S_OK('%s should not proceed as previous step did not end properly' % self.applicationName)

    res = getSoftwareFolder(self.platform, self.applicationName, self.applicationVersion)
    if not res['OK']:
      LOG.error('Failed finding the software area')
      self.setApplicationStatus('Could find neither local area nor shared area install')
      return res
    myappDir = res['Value']

    deptar = resolveDeps(self.platform, self.applicationName, self.applicationVersion)[0]
    res = getSoftwareFolder(self.platform, deptar["app"], deptar["version"])
    if not res['OK']:
      LOG.error("Failed finding the dependency location")
      return res
    path = res['Value']
    if not os.path.exists("%s.ep" % path):
      LOG.error('Could not find the lumi files!')
      return S_ERROR("Lumi files not found")

    originpath = "%s.ep" % path
    randomName = '/tmp/LumiFile-' + generateRandomString(8)
    try:
      os.mkdir(randomName)
    except EnvironmentError as x:
      LOG.error("Failed setting up the temp directory")
      return S_ERROR("Could not create temp dir: %s" % str(x))

    try:
      os.symlink(originpath, "%s/%s" % (randomName, os.path.basename(originpath)))
    except EnvironmentError as why:
      LOG.error('Failed setting up the sym link to lumi files')
      return S_ERROR("Cannot sym link lumi file: %s %s" % str(why))
    # try :
    #  shutil.copy(originpath,"/tmp/")
    # except:
    #  return S_ERROR("Could not copy to /tmp")
    #self.lumifile = path+"/%s.ep"%depdir
    lumifile = "%s/%s" % (randomName, os.path.basename(originpath).replace(".ep", ""))
    # Need to fetch the new LD_LIBRARY_PATH
    new_ld_lib_path = getNewLDLibs(self.platform, self.applicationName, self.applicationVersion)
    new_ld_lib_path = myappDir + "/lib:" + new_ld_lib_path

    scriptName = '%s_%s_Run_%s.sh' % (self.applicationName, self.applicationVersion, self.STEP_NUMBER)
    if os.path.exists(scriptName):
      os.remove(scriptName)
    script = open(scriptName, 'w')
    script.write('#!/bin/sh \n')
    script.write('#####################################################################\n')
    script.write('# Dynamically generated script to run a production or analysis job. #\n')
    script.write('#####################################################################\n')
    if new_ld_lib_path:
      script.write('declare -x LD_LIBRARY_PATH=%s\n' % new_ld_lib_path)
    script.write("declare -x NBEVTS=%s\n" % self.NumberOfEvents)
    script.write("declare -x LumiFile=%s\n" % lumifile)
    script.write("declare -x OUTPUTFILE=%s\n" % self.OutputFile)
    script.write('echo ======================================\n')
    script.write('env | sort >> localEnv.log\n')
    comm = "%s/%s_%s.exe\n" % (myappDir, self.applicationName, self.applicationVersion)
    LOG.info("Will run %s" % comm)
    script.write(comm)
    script.write('declare -x appstatus=$?\n')
    script.write('exit $appstatus\n')
    script.close()
    if os.path.exists(self.applicationLog):
      os.remove(self.applicationLog)

    os.chmod(scriptName, 0o755)
    comm = 'sh -c "./%s"' % scriptName
    self.setApplicationStatus('%s %s step %s' % (self.applicationName, self.applicationVersion, self.STEP_NUMBER))
    self.stdError = ''
    self.result = shellCall(0, comm, callbackFunction=self.redirectLogOutput, bufferLimit=20971520)
    if not self.result['OK']:
      LOG.error('Something wrong during running:', self.result['Message'])
      self.setApplicationStatus('Error during running %s' % self.applicationName)
      return S_ERROR('Failed to run %s' % self.applicationName)

    #self.result = {'OK':True,'Value':(0,'Disabled Execution','')}
    resultTuple = self.result['Value']
    status = resultTuple[0]

    if not os.path.exists(self.applicationLog):
      LOG.error("Something went terribly wrong, the log file is not present")
      self.setApplicationStatus('%s failed terribly, you are doomed!' % (self.applicationName))
      if not self.ignoreapperrors:
        return S_ERROR('%s did not produce the expected log' % (self.applicationName))

    if os.path.exists("pythiaGen.lpt"):
      base = "pythiaGen.lpt".split(".lpt")[0]
      try:
        os.rename("pythiaGen.lpt", base + self.STEP_NUMBER + ".lpt")
      except EnvironmentError:
        LOG.error("Could not rename, deleting")
        os.unlink("pythiaGen.lpt")

    with open(self.applicationLog) as logf:
      success = False
      for line in logf:
        if line.count("Evts Generated= "):
          success = True
      if not success:
        status = 1

    return self.finalStatusReport(status)
