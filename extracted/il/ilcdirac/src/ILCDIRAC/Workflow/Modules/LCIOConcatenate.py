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

:author: Ching Bon Lam
:since: Dec 17, 2011
"""

from __future__ import absolute_import
import os

from DIRAC import S_OK, S_ERROR, gLogger
from DIRAC.Core.Utilities.Subprocess import shellCall

from ILCDIRAC.Core.Utilities.PrepareLibs import removeLibc
from ILCDIRAC.Core.Utilities.resolvePathsAndNames import getProdFilename
from ILCDIRAC.Workflow.Modules.ModuleBase import ModuleBase

__RCSID__ = '$Id$'
LOG = gLogger.getSubLogger(__name__)


class LCIOConcatenate(ModuleBase):
  """LCIO concatenate module."""

  def __init__(self):

    super(LCIOConcatenate, self).__init__()

    self.STEP_NUMBER = ''

    # Step parameters
    self.applicationName = "lcio"
    #

    LOG.info("%s initialized" % (self.__str__()))

  def applicationSpecificInputs(self):
    """Resolve LCIO concatenate specific parameters, called from ModuleBase."""

    if not self.OutputFile:
      return S_ERROR('No output file defined')

    if self.isProdJob:
      if 'ProductionOutputData' in self.workflow_commons:
        outputlist = self.workflow_commons['ProductionOutputData'].split(";")
        for obj in outputlist:
          if obj.lower().count("_sim_") or obj.lower().count("_rec_") or obj.lower().count("_dst_"):
            self.OutputFile = os.path.basename(obj)
      else:
        self.OutputFile = getProdFilename(self.OutputFile, int(self.workflow_commons["PRODUCTION_ID"]),
                                          int(self.workflow_commons["JOB_ID"]))

    return S_OK('Parameters resolved')

  def execute(self):
    """Execute the module, called by JobAgent."""
    result = S_ERROR()
    # Get input variables
    result = self.resolveInputVariables()
    # Checks
    if not result['OK']:
      LOG.error("Failed to resolve input parameters:", result['Message'])
      return result

    if not self.platform:
      result = S_ERROR('No ILC platform selected')

    if not result['OK']:
      LOG.error("Failed to resolve input parameters:", result['Message'])
      return result

    if 'LCIO' not in os.environ:
      LOG.error("Environment variable LCIO was not defined, cannot do anything")
      return S_ERROR("Environment variable LCIO was not defined, cannot do anything")

    removeLibc(os.path.join(os.environ["LCIO"], "lib"))

    # Setting up script

    LD_LIBRARY_PATH = os.path.join("$LCIO", "lib")
    if 'LD_LIBRARY_PATH' in os.environ:
      LD_LIBRARY_PATH += ":" + os.environ['LD_LIBRARY_PATH']

    PATH = "$LCIO/bin"
    if 'PATH' in os.environ:
      PATH += ":" + os.environ['PATH']

    scriptContent = """
#!/bin/sh

################################################################################
# Dynamically generated script by LCIOConcatenate module                       #
################################################################################

declare -x LD_LIBRARY_PATH=%s
declare -x PATH=%s

lcio concat -f *.slcio -o %s

exit $?

""" % (
        LD_LIBRARY_PATH,
        PATH,
        self.OutputFile
        )

    # Write script to file

    scriptPath = 'LCIOConcatenate_%s_Run_%s.tcl' % (self.applicationVersion, self.STEP_NUMBER)

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

    self.setApplicationStatus('LCIOConcatenate %s step %s' % (self.applicationVersion, self.STEP_NUMBER))
    self.stdError = ''

    result = shellCall(0,
                        command,
                        callbackFunction=self.redirectLogOutput,
                        bufferLimit=20971520
                      )

    # Check results

    resultTuple = result['Value']
    status = resultTuple[0]

    LOG.info("Status after the application execution is %s" % str(status))

    self.listDir()
    return self.finalStatusReport(status)
