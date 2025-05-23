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
"""Download the production log files from the Log storage element.

See the JDL of production jobs for the log file location. One can also download a full directory of log files.

Example::

  dirac-ilc-get-prod-log -F /ilc/prod/clic/..../1225_23.tar.gz

Options:
   -D, --LogFileDir lfnDirectory      Production log dir to download
   -F, --LogFile lfn                  Production log to download
   -O, --OutputDir localDir           Output directory (default ./)
   -P, --ProdID prodID                Download the log folder 000 for this production ID
   -A, --All                          Get logs from all sub-directories
   --Query                            Set the metadata query to use for finding production files: Key1:Val1[,K2:V2,...]
   -N, --NoPrompt                     Do not query before download.

:since: Mar 21, 2013
:author: Stephane Poss
"""
from __future__ import absolute_import
__RCSID__ = "$Id$"

import os

from DIRAC.Core.Base.Script import Script
from DIRAC import gLogger, S_OK, S_ERROR, exit as dexit
from DIRAC.Core.Utilities.PromptUser import promptUser


class _Params(object):
  """Parameter object."""

  def __init__(self):
    self.logD = ''
    self.logF = ''
    self.outputdir = './'
    self.prodid = ''
    self.query = {}
    self.getAllSubdirs = False
    self.noPromptBeforeDL = False

  def setLogFileD(self, opt):
    self.logD = opt
    return S_OK()

  def setLogFileF(self, opt):
    self.logF = opt
    return S_OK()

  def setOutputDir(self, opt):
    self.outputdir = opt
    return S_OK()

  def setProdID(self, opt):
    self.prodid = opt
    return S_OK()

  def setAllGet(self, _):
    self.getAllSubdirs = True
    return S_OK()

  def setNoPrompt(self, _):
    self.noPromptBeforeDL = True
    return S_OK()

  def setQuery(self, query):
    if ':' not in query:
      return S_ERROR('Query syntax not correct')
    self.query = dict(q.split(':') for q in query.split(','))
    return S_OK()

  def registerSwitches(self):
    """registers switches."""
    Script.registerSwitch('D:', 'LogFileDir=', 'Production log dir to download', self.setLogFileD)
    Script.registerSwitch('F:', 'LogFile=', 'Production log to download', self.setLogFileF)
    Script.registerSwitch('O:', 'OutputDir=', 'Output directory (default %s)' % self.outputdir,
                          self.setOutputDir)
    Script.registerSwitch(
        'P:',
        'ProdID=',
        'Production ID. The folder will be found my metadata query for ProdID',
        self.setProdID)
    Script.registerSwitch('A', 'All', 'Get logs from all sub-directories', self.setAllGet)
    Script.registerSwitch('N', 'NoPrompt', 'No prompt before download', self.setNoPrompt)
    Script.registerSwitch('', 'Query=', 'Overwrite Meta query: Key1:Val1[,Key2:Val2...]', self.setQuery)
    Script.setUsageMessage('%s -F /ilc/prod/.../LOG/.../somefile' % Script.scriptName)


def _printErrorReport(res):
  """Print the failures for the call to getFile or Directory."""
  if res['Value'] and res['Value']['Failed']:
    for lfn in res['Value']['Failed']:
      gLogger.error("%s %s" % (lfn, res['Value']['Failed'][lfn]))
      return S_ERROR()
  return S_OK()


@Script()
def main():
  """get production log files from LogSE."""
  clip = _Params()
  clip.registerSwitches()
  Script.parseCommandLine()
  if not (clip.logF or clip.logD or clip.prodid):
    Script.showHelp()
    dexit(1)
  from DIRAC.ConfigurationSystem.Client.Helpers.Operations import Operations
  ops = Operations()
  storageElementName = ops.getValue('/LogStorage/LogSE', 'LogSE')
  from DIRAC.Resources.Storage.StorageElement import StorageElementItem as StorageElement
  logSE = StorageElement(storageElementName)

  if clip.prodid and not (clip.logD or clip.logF):
    result = _getLogFolderFromID(clip)
    if not result['OK']:
      gLogger.error(result['Message'])
      dexit(1)

  if clip.logD:
    if not clip.noPromptBeforeDL:
      res = promptUser('Are you sure you want to get ALL the files in this directory?')
      if not res['OK']:
        dexit()
      choice = res['Value']
      if choice.lower() == 'n':
        dexit(0)

    if isinstance(clip.logD, str):
      res = logSE.getDirectory(clip.logD, localPath=clip.outputdir)
      _printErrorReport(res)
    elif isinstance(clip.logD, list):
      for logdir in clip.logD:
        gLogger.notice('Getting log files from ' + str(logdir))
        res = logSE.getDirectory(logdir, localPath=clip.outputdir)
        _printErrorReport(res)

  if clip.logF:
    res = logSE.getFile(clip.logF, localPath=clip.outputdir)
    _printErrorReport(res)


def _getLogFolderFromID(clip):
  """Obtain the folder of the logfiles from the prodID.

  Fills the clip.logD variable
  """
  from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient
  from DIRAC.TransformationSystem.Client.TransformationClient import TransformationClient

  # Check if transformation exists and get its type
  server = TransformationClient()
  result = server.getTransformation(clip.prodid)
  if not result['OK']:
    return result
  transType = result['Value']['Type']
  query = {'ProdID': clip.prodid}
  if 'Reconstruction' in transType:
    query['Datatype'] = 'DST'
  if clip.query:
    query.update(clip.query)
    gLogger.notice('Using query: %r' % query)

  result = FileCatalogClient().findDirectoriesByMetadata(query, '/')
  if not result['OK']:
    return result
  elif result['Value']:
    # return value is dictionary with (directory ID: directory)
    folders = list(result['Value'].values())
    # remove the base directory of the production, keep only 000, 001 etc.
    folders = [folder for folder in folders if not folder.endswith(str(clip.prodid))]
    if not clip.getAllSubdirs:
      folders = folders[:1]
    clip.logD = []
    # drop the trailing, e.g., 00X
    baseLFN = folders[0].rsplit('/', 1)[0]
    for folder in folders:
      subFolderNumber = folder.rsplit('/', 1)[1]
      logdir = os.path.join(baseLFN, 'LOG', subFolderNumber)
      if logdir not in clip.logD:
        gLogger.notice('Setting logdir to %s' % logdir)
        clip.logD.append(logdir)

  else:
    return S_ERROR("Cannot discover the LogFilePath: No output files yet")

  return S_OK()


if __name__ == '__main__':
  main()
