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
"""Run SLICPandora.

:since: Oct 25, 2010
:author: sposs
"""

from __future__ import absolute_import
import os
import six.moves.urllib.request
import six.moves.urllib.parse
import six.moves.urllib.error

from DIRAC import S_OK, S_ERROR, gLogger
from DIRAC.Core.Utilities.Subprocess import shellCall

from ILCDIRAC.Workflow.Modules.ModuleBase import ModuleBase
from ILCDIRAC.Core.Utilities.CombinedSoftwareInstallation import getSoftwareFolder, getEnvironmentScript, unzip_file_into_dir
from ILCDIRAC.Core.Utilities.resolvePathsAndNames import resolveIFpaths
from ILCDIRAC.Core.Utilities.PrepareOptionFiles import getNewLDLibs, getNewPATH
from ILCDIRAC.Core.Utilities.PrepareLibs import removeLibc


__RCSID__ = '$Id$'
LOG = gLogger.getSubLogger(__name__)


class SLICPandoraAnalysis (ModuleBase):
  """Run SLIC Pandora."""

  def __init__(self):
    super(SLICPandoraAnalysis, self).__init__()
    self.STEP_NUMBER = ''
    self.result = S_ERROR()
    self.applicationName = 'SLICPandora'
    self.pandorasettings = ""
    self.detectorxml = ""
    self.startFrom = 0
    self.eventstring = ['>>>>>> EVENT']

  def applicationSpecificInputs(self):

    if not self.pandorasettings:
      self.pandorasettings = "PandoraSettings.xml"

    if not len(self.InputFile) and len(self.InputData):
      for files in self.InputData:
        if files.lower().find(".slcio") > -1:
          self.InputFile.append(files)

    return S_OK('Parameters resolved')

  def runIt(self):
    """Called from ModuleBase."""
    self.result = S_OK()
    if not self.platform:
      self.result = S_ERROR('No ILC platform selected')
    elif not self.applicationLog:
      self.result = S_ERROR('No Log file provided')
    if not self.result['OK']:
      LOG.error("Failed to resolve input parameters:", self.result["Message"])
      return self.result

    if not self.workflowStatus['OK'] or not self.stepStatus['OK']:
      LOG.verbose('Workflow status = %s, step status = %s' % (self.workflowStatus['OK'], self.stepStatus['OK']))
      return S_OK('SLIC Pandora should not proceed as previous step did not end properly')

    # Get the env script
    res = getEnvironmentScript(self.platform, self.applicationName, self.applicationVersion, self.getEnvScript)
    if not res['OK']:
      LOG.error("Failed to get the environment script:", res["Message"])
      return res
    env_script_path = res["Value"]

    res = resolveIFpaths(self.InputFile)
    if not res['OK']:
      LOG.error('Could not find input files')
      self.setApplicationStatus('SLICPandora: missing slcio file')
      return S_ERROR('Missing slcio file!')
    runonslcio = res['Value'][0]

    if not self.detectorxml.count(".xml") or not os.path.exists(os.path.basename(self.detectorxml)):
      detmodel = self.detectorxml.replace("_pandora.xml", "")
      if os.path.exists(detmodel + ".zip"):
        try:
          unzip_file_into_dir(open(detmodel + ".zip", 'rb'), os.getcwd())
        except (RuntimeError, OSError) as err:
          LOG.error("Exception when unpacking detectormodel zip file:", str(err))
          os.unlink(detmodel + ".zip")
      if not os.path.exists(detmodel + ".zip"):
        # retrieve detector model from web
        detector_urls = self.ops.getValue('/SLICweb/SLICDetectorModels', [''])
        if len(detector_urls[0]) < 1:
          LOG.error('Could not find in CS the URL for detector model')
          return S_ERROR('Could not find in CS the URL for detector model')

        for detector_url in detector_urls:
          try:
            six.moves.urllib.request.urlretrieve("%s%s" % (detector_url, detmodel + ".zip"), detmodel + ".zip")
          except IOError:
            LOG.error("Download of detector model failed")
            continue
          try:
            unzip_file_into_dir(open(detmodel + ".zip", 'rb'), os.getcwd())
            break
          except (RuntimeError, OSError) as err:
            LOG.error("Exception for zip file obtained from ", detector_url)
            LOG.error("Exception:", str(err))
            os.unlink(detmodel + ".zip")
            continue
      # if os.path.exists(detmodel): #and os.path.isdir(detmodel):
      self.detectorxml = os.path.join(os.getcwd(), self.detectorxml)
      if not self.detectorxml.endswith('xml'):
        self.detectorxml = self.detectorxml + "_pandora.xml"

    if not os.path.exists(self.detectorxml):
      LOG.error('Detector model xml %s was not found, exiting' % self.detectorxml)
      return S_ERROR('Detector model xml was not found, exiting')

    oldversion = False
    if self.applicationVersion in ['CLIC_CDR', 'CDR1', 'CDR2', 'CDR0', 'V2', 'V3', 'V4']:
      oldversion = True

    scriptName = 'SLICPandora_%s_Run_%s.sh' % (self.applicationVersion, self.STEP_NUMBER)
    if os.path.exists(scriptName):
      os.remove(scriptName)
    script = open(scriptName, 'w')
    script.write('#!/bin/bash \n')
    script.write('#####################################################################\n')
    script.write('# Dynamically generated script to run a production or analysis job. #\n')
    script.write('#####################################################################\n')
    script.write("source %s\n" % env_script_path)
    script.write("declare -x file=./Settings/%s\n" % self.pandorasettings)
    script.write("""
if [ -e "${file}" ]
then
   declare -x PANDORASETTINGS=$file
else
  if [ -d "${PANDORASETTINGSDIR}" ]
  then
    cp $PANDORASETTINGSDIR/*.xml .
    declare -x PANDORASETTINGS=%s
  fi
fi
if [ ! -e "${PANDORASETTINGS}" ]
then
  echo "Missing PandoraSettings file"
  exit 1
fi
""" % self.pandorasettings)
    script.write('echo =============================\n')
    script.write('echo PATH is \n')
    script.write('echo $PATH | tr ":" "\n"  \n')
    script.write('echo ==============\n')
    if os.path.exists("./lib"):
      script.write('declare -x LD_LIBRARY_PATH=./lib:$LD_LIBRARY_PATH\n')
    script.write('echo =============================\n')
    script.write('echo LD_LIBRARY_PATH is \n')
    script.write('echo $LD_LIBRARY_PATH | tr ":" "\n"\n')
    script.write('echo ============================= \n')
    script.write('env | sort >> localEnv.log\n')
    # Now run it
    if oldversion:
      comm = 'PandoraFrontend %s $PANDORASETTINGS %s %s %s' % (self.detectorxml, runonslcio,
                                                               self.OutputFile, str(self.NumberOfEvents))
    else:
      comm = 'PandoraFrontend -g %s -c $PANDORASETTINGS -i %s -o %s -r %s' % (self.detectorxml,
                                                                              runonslcio, self.OutputFile,
                                                                              str(self.NumberOfEvents))
    comm = "%s %s\n" % (comm, self.extraCLIarguments)
    LOG.info("Will run %s" % comm)
    script.write(comm)
    script.write('declare -x appstatus=$?\n')
    # script.write('where\n')
    # script.write('quit\n')
    # script.write('EOF\n')
    script.write('exit $appstatus\n')

    script.close()
    if os.path.exists(self.applicationLog):
      os.remove(self.applicationLog)

    os.chmod(scriptName, 0o755)
    comm = 'sh -c "./%s"' % (scriptName)
    self.setApplicationStatus('SLICPandora %s step %s' % (self.applicationVersion, self.STEP_NUMBER))
    self.stdError = ''
    self.result = shellCall(0, comm, callbackFunction=self.redirectLogOutput,
                            bufferLimit=20971520)
    #self.result = {'OK':True,'Value':(0,'Disabled Execution','')}
    resultTuple = self.result['Value']
    if resultTuple[0]:
      LOG.error("There was an error during the execution")

    if not os.path.exists(self.applicationLog):
      LOG.error("Something went terribly wrong, the log file is not present")
      self.setApplicationStatus('%s failed terribly, you are doomed!' % (self.applicationName))
      if not self.ignoreapperrors:
        return S_ERROR('%s did not produce the expected log' % (self.applicationName))

    logf = open(self.applicationLog, 'r')
    if "Missing PandoraSettings file" in logf.readlines()[-1]:
      LOG.error("Issue with the Pandora Settings file.")
    logf.close()

    status = resultTuple[0]
    # stdOutput = resultTuple[1]
    # stdError = resultTuple[2]
    LOG.info("Status after the application execution is %s" % str(status))

    return self.finalStatusReport(status)
    #############################################################################

  def getEnvScript(self, sysconfig, appname, appversion):
    """Produce the environment file in case CVMFS is not here."""
    env_script_name = "SLICPandora.sh"

    res = getSoftwareFolder(sysconfig, appname, appversion)
    if not res['OK']:
      self.setApplicationStatus('SLICPandora: Could not find neither local area not shared area install')
      return res
    myslicPandoraDir = res['Value']

    # Remove libc lib
    removeLibc(myslicPandoraDir + "/LDLibs")

    # Need to fetch the new LD_LIBRARY_PATH
    new_ld_lib_path = getNewLDLibs(sysconfig, appname, appversion)

    new_path = getNewPATH(sysconfig, appname, appversion)

    prefixpath = ""
    if os.path.exists("PandoraFrontend"):
      prefixpath = "."
    elif os.path.exists("%s/Executable/PandoraFrontend" % myslicPandoraDir):
      prefixpath = "%s/Executable" % myslicPandoraDir
    else:
      return S_ERROR("Missing PandoraFrontend binary")
    with open(env_script_name, "w") as script:
      script.write('#!/bin/sh \n')
      script.write('############################################################\n')
      script.write('# Dynamically generated script to get the SLICPandora env. #\n')
      script.write('############################################################\n')
      script.write("declare -x PATH=%s:$PATH\n" % new_path)
      script.write('declare -x ROOTSYS=%s/ROOT\n' % (myslicPandoraDir))
      script.write('declare -x LD_LIBRARY_PATH=$ROOTSYS/lib:%s/LDLibs:%s\n' % (myslicPandoraDir, new_ld_lib_path))
      script.write('declare -x PANDORASETTINGSDIR=%s/Settings\n' % myslicPandoraDir)
      script.write("declare -x PATH=%s:$PATH\n" % prefixpath)
    os.chmod(env_script_name, 0o755)
    return S_OK(os.path.abspath(env_script_name))
