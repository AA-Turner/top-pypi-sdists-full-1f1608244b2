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
'''
:since: May 30, 2013

:author: sposs
'''

from __future__ import absolute_import
import os
import socket

from ILCDIRAC.Core.Utilities.CombinedSoftwareInstallation import getSharedAreaLocation
from ILCDIRAC.Workflow.Modules.ModuleBase import ModuleBase
from DIRAC.Core.Utilities.Os import getDiskSpace, getDirectorySize

from DIRAC import S_OK, S_ERROR, gLogger

__RCSID__ = '$Id$'
LOG = gLogger.getSubLogger(__name__)


class AnalyseWN(ModuleBase):
  """Module that will dump the host properties, and also the SharedArea content if it's there."""

  def __init__(self):
    """Constructor."""
    super(AnalyseWN, self).__init__()

  def execute(self):
    """Run the module."""
    result = self.resolveInputVariables()
    if not result['OK']:
      LOG.error("Failed to get the input parameters:", result['Message'])
      return result

    if not self.applicationLog:
      LOG.warn("Log file name missing, reverting to default")
      self.applicationLog = "AnalyseWN.log"

    info = []
    try:
      info.append("Host is %s" % socket.gethostname())
    except EnvironmentError:
      info.append("Could not determine host")

    size = getDiskSpace()
    if size > 0:
      info.append("Local disk is %s MB" % size)

    fileName = '/proc/cpuinfo'
    if os.path.exists(fileName):
      nCPU = 0
      freq = 0
      cpuModel = 'Unknown'
      with open(fileName, 'r') as cpuInfoFile:
        cpu = cpuInfoFile.readlines()
      for line in cpu:
        if line.find('cpu MHz') == 0:
          nCPU += 1
          freq = line.split()[3]
        elif line.find('model name') == 0:
          cpuModel = line.split(': ')[1].strip()
      info.append('CPU (model)    = %s' % cpuModel)
      info.append('CPU (MHz)      = %s x %s' % (nCPU, freq))

    fileName = '/proc/meminfo'
    if os.path.exists(fileName):
      with open(fileName, 'r') as memInfoFile:
        mem = memInfoFile.readlines()
      freeMem = 0
      totalMem = 0
      for line in mem:
        if line.find('MemTotal:') == 0:
          totalMem = int(line.split()[1])
        if line.find('MemFree:') == 0:
          freeMem += int(line.split()[1])
        if line.find('Cached:') == 0:
          freeMem += int(line.split()[1])
      info.append('Memory (kB)    = %s' % totalMem)
      info.append('FreeMem. (kB)  = %s' % freeMem)

    fs = os.statvfs(".")
    # bsize;    /* file system block size */
    # frsize;   /* fragment size */
    # blocks;   /* size of fs in f_frsize units */
    # bfree;    /* # free blocks */
    # bavail;   /* # free blocks for non-root */
    # files;    /* # inodes */
    # ffree;    /* # free inodes */
    # favail;   /* # free inodes for non-root */
    # flag;     /* mount flags */
    # namemax;  /* maximum filename length */
    diskSpace = fs[4] * fs[0] // 1024 // 1024
    info.append('DiskSpace (MB) = %s' % diskSpace)

    sha = getSharedAreaLocation()
    if not sha:
      info.append("No shared Area found here")
    else:
      info.append("Shared Area found: %s" % sha)
      info.append("Content:")
      sha_list = os.listdir(sha)
      for item in sha_list:
        info.append("   %s" % item)
      sha_size = getDirectorySize(sha)
      if sha_size:
        info.append("It uses %s MB of disk" % sha_size)

    if os.path.isdir("/cvmfs/ilc.cern.ch"):
      info.append("Has CVMFS")

    try:
      of = open(self.applicationLog, "w")
      of.write("\n".join(info))
      of.close()
    except OSError:
      LOG.error("Could not create the log file")
      return S_ERROR("Failed saving the site info")

    return S_OK()
