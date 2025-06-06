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
"""Module that gets a file from its SRM definition.

:since: Aug 27, 2010
:author: sposs
"""

from __future__ import absolute_import
import os
import tempfile
import time

from DIRAC import S_OK, S_ERROR, gLogger
from DIRAC.Resources.Storage.StorageElement import StorageElementItem as StorageElement
from DIRAC.WorkloadManagementSystem.Client.JobMonitoringClient import JobMonitoringClient

from ILCDIRAC.Workflow.Modules.ModuleBase import ModuleBase

__RCSID__ = '$Id$'
LOG = gLogger.getSubLogger(__name__)


class GetSRMFile(ModuleBase):
  """When a file is not in the FileCatalog, it can still be obtained using this.

  and specifying the srm path.
  """

  def __init__(self):
    """Module initialization."""
    super(GetSRMFile, self).__init__()
    self.version = __RCSID__
    self.srmfiles = []
    self.files = []
    self.counter = 1

  def applicationSpecificInputs(self):
    """Resolve the srm files to get."""
    if not self.srmfiles:
      return S_ERROR("List of files to treat is not set")
    self.files = self.srmfiles
    return S_OK()

  def execute(self):
    """Run this."""
    if not self.workflowStatus['OK'] or not self.stepStatus['OK']:
      LOG.verbose('Workflow status = %s, step status = %s' % (self.workflowStatus['OK'], self.stepStatus['OK']))
      return S_OK('Workflow status is not OK')
    result = self.resolveInputVariables()
    if not result['OK']:
      LOG.error("Failed to resolve input parameters:", result["Message"])
      return result
    if not self.srmfiles:
      LOG.error('Files txt was not found correctly: %s' % self.srmfiles)
      return S_ERROR('Files txt was not found correctly')

    if not isinstance(self.files[0], dict):
      LOG.error('Files were not found correctly: %s' % self.files)
      return S_ERROR('Files were not found correctly')

    # Now need to check that there are not that many concurrent jobs getting the overlay at the same time
    max_concurrent_running = self.ops.getValue('/GetSRM/MaxConcurrentRunning', 100)
    error_count = 0
    while True:
      if error_count > 10:
        LOG.error('JobDB Content does not return expected dictionary')
        return S_ERROR('Failed to get number of concurrent overlay jobs')
      jobMonitor = JobMonitoringClient()
      res = jobMonitor.getCurrentJobCounters({'ApplicationStatus': 'Downloading SRM files'})
      if not res['OK']:
        error_count += 1
        time.sleep(60)
        continue
      running = 0
      if 'Running' in res['Value']:
        running = res['Value']['Running']
      if running < max_concurrent_running:
        break
      else:
        time.sleep(60)

    self.setApplicationStatus('Downloading SRM files')
    for filed in self.files:
      if 'file' not in filed or 'site' not in filed:
        LOG.error('Dictionnary does not contain correct keys')
        return S_ERROR('Dictionnary does not contain correct keys')
      start = os.getcwd()
      downloadDir = tempfile.mkdtemp(prefix='InputData_%s' % (self.counter), dir=start)
      os.chdir(downloadDir)
      storageElement = StorageElement(filed['site'])
      result = storageElement.getFile(filed['file'])
      if result['Value']['Failed']:
        result = storageElement.getFile(filed['file'])
      os.chdir(start)
      if result['Value']['Failed']:
        LOG.error("Failed to get the file from storage:", result['Value']['Failed'])
        return result
      self.counter += 1

    return S_OK()
