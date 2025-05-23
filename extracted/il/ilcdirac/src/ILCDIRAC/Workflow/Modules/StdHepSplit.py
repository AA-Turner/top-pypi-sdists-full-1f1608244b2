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
"""Module to concatenate LCIO files.

:author: S. Poss
:since: Mar 09, 2012
"""

from __future__ import absolute_import
import os

from DIRAC import S_OK, S_ERROR, gLogger
from DIRAC.Core.Utilities.Subprocess import shellCall

from ILCDIRAC.Core.Utilities.CombinedSoftwareInstallation import getSoftwareFolder
from ILCDIRAC.Core.Utilities.PrepareOptionFiles import getNewLDLibs
from ILCDIRAC.Core.Utilities.resolvePathsAndNames import getProdFilename, resolveIFpaths
from ILCDIRAC.Workflow.Modules.ModuleBase import ModuleBase

__RCSID__ = '$Id$'
LOG = gLogger.getSubLogger(__name__)


class StdHepSplit(ModuleBase):
  """StdHep split module, split StdHep files using A.

  Miyamoto's HepSplit utility
  """

  def __init__(self):

    super(StdHepSplit, self).__init__()

    self.STEP_NUMBER = ''
    self.result = S_ERROR()
    self.nbEventsPerSlice = 0
    self.InputFile = []
    # Step parameters
    self.prod_outputdata = []
    #
    self.listoutput = {}
    self.OutputFile = []
    LOG.info("%s initialized" % (self.__str__()))
    self.maxRead = 0

  def applicationSpecificInputs(self):
    """Resolve LCIO concatenate specific parameters, called from ModuleBase."""

    if not self.OutputFile:
      return S_ERROR('No output file defined')

    if 'IS_PROD' in self.workflow_commons and self.workflow_commons["IS_PROD"]:
      if 'ProductionOutputData' in self.workflow_commons:
        self.prod_outputdata = self.workflow_commons['ProductionOutputData'].split(";")
        for obj in self.prod_outputdata:
          if obj.lower().count("_gen_"):
            self.OutputFile = os.path.basename(obj)
      else:
        self.OutputFile = getProdFilename(self.OutputFile,
                                          int(self.workflow_commons["PRODUCTION_ID"]),
                                          int(self.workflow_commons["JOB_ID"]))

    if not len(self.InputFile) and len(self.InputData):
      for files in self.InputData:
        if files.lower().find(".stdhep") > -1:
          self.InputFile.append(files)

    if 'listoutput' in self.step_commons:
      if len(self.step_commons['listoutput']):
        self.listoutput = self.step_commons['listoutput'][0]

    return S_OK('Parameters resolved')

  def execute(self):
    """Execute the module, called by JobAgent."""
    # Get input variables

    self.result = self.resolveInputVariables()
    # Checks

    if not self.platform:
      self.result = S_ERROR('No ILC platform selected')

    if not self.result['OK']:
      LOG.error("Failed to resolve input parameters:", self.result["Message"])
      return self.result

    if len(self.InputFile):
      res = resolveIFpaths(self.InputFile)
      if not res['OK']:
        LOG.error("Cannot find input file")
        self.setApplicationStatus('StdHepSplit: missing input stdhep file')
        return S_ERROR('Missing stdhep file!')
      runonstdhep = res['Value'][0]
    else:
      LOG.warn("No files found to split")
      return S_OK("No files found to process")

    prefix = ''
    if self.OutputFile:
      prefix = self.OutputFile.split('.stdhep')[0]

    else:
      prefix = "this_split"
    # because we need to make sure the files end up in the base directory at the end
    self.OutputFile = prefix

    LOG.info("Will rename all files using '%s' as base." % prefix)

    # Setting up script
    res = getSoftwareFolder(self.platform, "stdhepsplit", self.applicationVersion)
    if not res['OK']:
      LOG.error("Failed to find the software")
      self.setApplicationStatus('StdHepSplit: Could not find neither local area not shared area install')
      return res

    mysplitDir = res['Value']
    new_ld_lib = getNewLDLibs(self.platform, "stdhepsplit", self.applicationVersion)
    LD_LIBRARY_PATH = os.path.join(mysplitDir, "lib") + ":" + new_ld_lib

    maxReadString = ''
    # hepsplit has a off-by-one error so we add 1 to max read to actually read maxRead events
    if self.maxRead:
      self.maxRead += 1
      maxReadString = " --maxread %s" % self.maxRead

    scriptContent = """
#!/bin/sh

################################################################################
# Dynamically generated script by LCIOConcatenate module                       #
################################################################################

declare -x LD_LIBRARY_PATH=%s

%s/hepsplit --infile %s --nw_per_file %s --outpref %s%s

exit $?

""" % (
        LD_LIBRARY_PATH,
        mysplitDir,
        runonstdhep,
        self.nbEventsPerSlice,
        prefix,
        maxReadString,
        )

    # Write script to file

    scriptPath = 'StdHepSplit_%s_Run_%s.tcl' % (self.applicationVersion, self.STEP_NUMBER)

    if os.path.exists(scriptPath):
      os.remove(scriptPath)

    script = open(scriptPath, 'w')
    script.write(scriptContent)
    script.close()

    # Setup log file for application stdout

    if os.path.exists(self.applicationLog):
      os.remove(self.applicationLog)

    # Run code

    os.chmod(scriptPath, 0o755)

    command = '"./%s"' % (scriptPath)

    self.setApplicationStatus('StdHepSplit %s step %s' % (self.applicationVersion, self.STEP_NUMBER))
    self.stdError = ''

    self.result = shellCall(0,
                             command,
                             callbackFunction=self.redirectLogOutput,
                             bufferLimit=20971520
                           )

    resultTuple = self.result['Value']
    status = resultTuple[0]

    if not os.path.exists(self.applicationLog):
      LOG.error("Cannot access log file, cannot proceed")
      return S_ERROR("Failed reading the log file")

    with open(self.applicationLog, "r") as logf:
      numberofeventsdict = {}
      fname = ''
      for line in logf:
        line = line.rstrip()
        if line.count('Open output file'):
          fname = line.split()[-1].rstrip().rstrip("\0")
          numberofeventsdict[fname] = 0
        elif line.count("Record") and not line.count('Output Begin Run'):
          #print line
          val = line.split("=")[1].rstrip().lstrip()
          if val != '0':
            numberofeventsdict[fname] = int(val)

    LOG.verbose("numberofeventsdict dict: %s" % numberofeventsdict)

    # Now update the workflow_commons dict with the relation between filename and number of events:
    # needed for the registerOutputData
    self.workflow_commons['file_number_of_event_relation'] = numberofeventsdict
    if self.listoutput:
      outputlist = []
      for of in numberofeventsdict:
        item = {}
        item['outputFile'] = of
        item['outputPath'] = self.listoutput['outputPath']
        item['outputDataSE'] = self.listoutput['outputDataSE']
        outputlist.append(item)
      self.step_commons['listoutput'] = outputlist

    # Not only the step_commons must be updated
    if 'ProductionOutputData' in self.workflow_commons:
      proddata = self.workflow_commons['ProductionOutputData'].split(";")
      finalproddata = []
      this_split_data = ''
      for item in proddata:
        if not item.count(prefix):
          finalproddata.append(item)
        else:
          this_split_data = item
      path = os.path.dirname(this_split_data)
      for of in numberofeventsdict:
        finalproddata.append(os.path.join(path, of))
      self.workflow_commons['ProductionOutputData'] = ";".join(finalproddata)

    LOG.info("Status after the application execution is %s" % str(status))
    if status == 2:
      LOG.info("Reached end of input file")
      status = 0

    self.listDir()
    return self.finalStatusReport(status)
