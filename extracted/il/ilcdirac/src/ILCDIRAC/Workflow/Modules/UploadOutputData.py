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
"""Module to upload specified job output files according to the parameters defined in the production workflow.

:author: S. Poss
:since: Sep 01, 2010
"""

from __future__ import absolute_import
import os
import random
import time
from pprint import pformat

from DIRAC.DataManagementSystem.Client.FailoverTransfer import FailoverTransfer
from DIRAC import S_OK, S_ERROR, gLogger, gConfig
from DIRAC.ConfigurationSystem.Client.Helpers.Operations import Operations
import DIRAC

from ILCDIRAC.Core.Utilities.ResolveSE import getDestinationSEList
from ILCDIRAC.Core.Utilities.resolvePathsAndNames import getProdFilename
from ILCDIRAC.Workflow.Modules.ModuleBase import ModuleBase
from ILCDIRAC.Core.Utilities.ProductionData import getExperimentFromPath
import six

__RCSID__ = '$Id$'
LOG = gLogger.getSubLogger(__name__)


class UploadOutputData(ModuleBase):
  """As name suggest: upload output data.

  For Production only: See :mod:`~ILCDIRAC.Workflow.Modules.UserJobFinalization` for User job upload.
  """
  #############################################################################

  def __init__(self):
    """Module initialization."""
    super(UploadOutputData, self).__init__()
    self.version = __RCSID__
    self.commandTimeOut = 10 * 60
    self.enable = True
    self.failoverSEs = gConfig.getValue('/Resources/StorageElementGroups/Tier1-Failover', [])
    self.ops = Operations()

    # List all parameters here
    self.outputDataFileMask = ''
    self.outputMode = 'Any'  # or 'Local' for reco case
    self.outputList = []
    self.productionID = 0
    self.prodOutputLFNs = []
    self.experiment = "CLIC"

  #############################################################################
  def applicationSpecificInputs(self):
    """By convention the module parameters are resolved here."""
    LOG.debug("Workflow commons: %s" % pformat(self.workflow_commons))

    self.enable = self.step_commons.get('Enable', self.enable)
    if not isinstance(self.enable, bool):
      LOG.warn('Enable flag set to non-boolean value %s, setting to False' % self.enable)
      self.enable = False

    self.productionID = self.workflow_commons.get("PRODUCTION_ID", self.productionID)

    self.jobID = os.environ.get('JOBID', self.jobID)
    if self.jobID:
      LOG.verbose('Found WMS JobID = %s' % self.jobID)
    else:
      LOG.info('No WMS JobID found, disabling module via control flag')
      self.enable = False

    # This is the thing that is used to establish the list of outpufiles to treat:
    # Make sure that all that is in the : "outputList" and also in the ProductionData
    # is treated properly. Needed as whatever is in outputList does not contain any reference to the
    # prodID and task ID. Also if for some reason a step failed, then the corresponding data will not be there
    self.outputList = self.workflow_commons.get('outputList', self.outputList)
    if self.outputList:
      if 'ProductionOutputData' in self.workflow_commons:
        productionData = self.workflow_commons['ProductionOutputData'].split(";")
        LOG.verbose("prod data : %s" % productionData)
        treatedOutputlist = {}
        for expectedOutputfile in self.outputList:
          LOG.debug("Treating file: %s" % expectedOutputfile['outputFile'])
          self.getTreatedOutputlistNew(productionData, treatedOutputlist, expectedOutputfile)
        self.outputList = list(treatedOutputlist.values())
      else:
        olist = []
        for expectedOutputfile in self.outputList:
          appdict = expectedOutputfile
          appdict['outputFile'] = getProdFilename(expectedOutputfile['outputFile'],
                                                  int(self.workflow_commons["PRODUCTION_ID"]),
                                                  int(self.workflow_commons["JOB_ID"]))
          olist.append(appdict)
        self.outputList = olist

      LOG.verbose("OutputList : %s" % self.outputList)

    self.outputMode = self.workflow_commons.get('outputMode', self.outputMode)

    self.outputDataFileMask = self.workflow_commons.get('outputDataFileMask', self.outputDataFileMask)
    if not isinstance(self.outputDataFileMask, list):
      self.outputDataFileMask = [i.lower().strip() for i in self.outputDataFileMask.split(';')]

    #result = constructProductionLFNs(self.workflow_commons)
    # if not result['OK']:
    #  LOG.error('Could not create production LFNs',result['Message'])
    #  return result
    # self.prodOutputLFNs=result['Value']['ProductionOutputData']

    tempOutputLFNs = self.workflow_commons.get('ProductionOutputData', self.prodOutputLFNs)
    if isinstance(tempOutputLFNs, six.string_types):
      self.prodOutputLFNs = tempOutputLFNs.split(";")
    else:
      self.prodOutputLFNs = tempOutputLFNs
    self.setJobParameter('ProductionOutputData', ';'.join(self.prodOutputLFNs), sendFlag=True)

    return S_OK('Parameters resolved')

  #############################################################################
  def execute(self):
    """Main execution function."""
    LOG.info('Initializing %s' % self.version)
    result = self.resolveInputVariables()
    if not result['OK']:
      LOG.error("Failed to resolve input parameters:", result['Message'])
      return result

    if not self.workflowStatus['OK'] or not self.stepStatus['OK']:
      LOG.verbose('Workflow status = %s, step status = %s' % (self.workflowStatus['OK'], self.stepStatus['OK']))
      return S_OK('No output data upload attempted')

    self.experiment = getExperimentFromPath(LOG, self.prodOutputLFNs[0], self.experiment)

    # Determine the final list of possible output files for the
    # workflow and all the parameters needed to upload them.
    result = self.getCandidateFiles(self.outputList, self.prodOutputLFNs, self.outputDataFileMask)
    if not result['OK']:
      LOG.error(result['Message'])
      self.setApplicationStatus(result['Message'])
      return result

    fileDict = result['Value']
    result = self.getFileMetadata(fileDict)
    if not result['OK']:
      LOG.error(result['Message'])
      self.setApplicationStatus(result['Message'])
      return result

    if not result['Value']:
      LOG.info('No output data files were determined to be uploaded for this workflow')
      return S_OK()

    fileMetadata = result['Value']

    # Get final, resolved SE list for files
    final = {}
    for fileName, metadata in fileMetadata.items():
      result = getDestinationSEList(metadata['workflowSE'], DIRAC.siteName(), self.outputMode)
      if not result['OK']:
        LOG.error('Could not resolve output data SE', result['Message'])
        self.setApplicationStatus('Failed To Resolve OutputSE')
        return result

      resolvedSE = result['Value']
      final[fileName] = metadata
      final[fileName]['resolvedSE'] = resolvedSE

    LOG.info('The following files will be uploaded: %s' % (', '.join(list(final.keys()))))
    for fileName, metadata in final.items():
      LOG.info('--------%s--------' % fileName)
      for metaName, metaValue in metadata.items():
        LOG.info('%s = %s' % (metaName, metaValue))

    # At this point can exit and see exactly what the module would have uploaded
    if not self.enable:
      LOG.info('Module is disabled by control flag, would have attempted to upload the \
      following files %s' % ', '.join(list(final.keys())))
      return S_OK('Module is disabled by control flag')

    # Disable the watchdog check in case the file uploading takes a long time
    LOG.info('Creating DISABLE_WATCHDOG_CPU_WALLCLOCK_CHECK in order to disable the Watchdog prior to upload')
    fopen = open('DISABLE_WATCHDOG_CPU_WALLCLOCK_CHECK', 'w')
    fopen.write('%s' % time.asctime())
    fopen.close()

    # Instantiate the failover transfer client with the global request object
    failoverTransfer = FailoverTransfer(self._getRequestContainer())

    catalogs = self.ops.getValue('Production/%s/Catalogs' % self.experiment,
                                 ['FileCatalog', 'LcgFileCatalog'])

    self.failoverSEs = self.ops.getValue("Production/%s/FailOverSE" % self.experiment, self.failoverSEs)

    # One by one upload the files with failover if necessary
    cleanUp = False
    for fileName, metadata in final.items():
      LOG.info("Attempting to store file %s to the following SE(s):\n%s" % (fileName,
                                                                                 ', '.join(metadata['resolvedSE'])))
      resultPrimary = failoverTransfer.transferAndRegisterFile(fileName,
                                                               metadata['localpath'],
                                                               metadata['lfn'],
                                                               metadata['resolvedSE'],
                                                               fileMetaDict=metadata['filedict'],
                                                               fileCatalog=catalogs)

      if resultPrimary['OK']:
        LOG.info("Successfully uploaded %s to %s" % (fileName, ', '.join(metadata['resolvedSE'])))
        continue

      # do the failover transfer
      LOG.error('Could not transfer and register %s with metadata:\n %s' %
                     (fileName, pformat(metadata['filedict'])))
      failovers = self.failoverSEs
      targetSE = metadata['resolvedSE'][0]
      try:  # remove duplicate site, otherwise it will do nasty things where processing the request
        failovers.remove(targetSE)
      except ValueError:
        pass
      random.shuffle(failovers)
      metadata['resolvedSE'] = failovers
      resultFailover = failoverTransfer.transferAndRegisterFileFailover(fileName=fileName,
                                                                        localPath=metadata['localpath'],
                                                                        lfn=metadata['lfn'],
                                                                        targetSE=targetSE,
                                                                        failoverSEList=metadata['resolvedSE'],
                                                                        fileMetaDict=metadata['filedict'],
                                                                        fileCatalog=catalogs)
      if not resultFailover['OK']:
        LOG.error('Could not transfer and register %s with metadata:\n %s' %
                       (fileName, pformat(metadata['filedict'])))
        cleanUp = True
        break  # no point continuing if one completely fails

    os.remove("DISABLE_WATCHDOG_CPU_WALLCLOCK_CHECK")  # cleanup the mess

    self.workflow_commons['Request'] = failoverTransfer.request

    # If some or all of the files failed to be saved to failover
    if cleanUp:
      lfns = []
      for fileName, metadata in final.items():
        lfns.append(metadata['lfn'])

      result = self._cleanUp(lfns)
      return S_ERROR('Failed to upload output data')

    return S_OK('Output data uploaded')

  def _getExtensionDictionary(self):
    """Return dictionary of extensions and patterns for the respective files."""
    operationsValue = self.ops.getOptionsDict('/Production/ExtensionToFiletypes')
    if not operationsValue['OK']:
      # the default value, for ilc VO
      return {'.stdhep': ['_gen'], '.slcio': ['_sim', '_rec', '_dst']}
    opValue = operationsValue['Value']
    resultDict = {}
    for extension, patterns in opValue.items():
      resultDict[extension] = [pattern.strip() for pattern in patterns.split(',')]
    return resultDict

  def _expectedExtension(self, filename):
    """Return the expected extension based on the production type hinted in the filename."""
    extensionTofiletype = self._getExtensionDictionary()
    for extension, patterns in extensionTofiletype.items():
      if any(pattern in filename for pattern in patterns):
        LOG.info("Matched %s with %s: expecting %s" % (patterns, filename, extension))
        return extension
    LOG.warn("Unknown production file type: %s" % filename)
    return ''

  def getTreatedOutputlistNew(self, producedData, treatedOutputlist, outputfileObject):
    """Return properly formated outputList in treatedOutputlist.

    TODO: describe what a properly formatted outputList looks like so we know what this function actually does.
    """
    expectedOutputFile, dummy_ext = self.getBasenameAndExtension(outputfileObject['outputFile'].lower())
    for productionFile in producedData:
      LOG.debug("Prodfile %s; outFile %s" % (productionFile, expectedOutputFile))
      productionFile, extension = self.getBasenameAndExtension(productionFile)
      LOG.debug("Removed extension: %s" % productionFile)
      if productionFile in treatedOutputlist:
        # This has already been treated, no need to come back to it.
        continue
      appdict = {}
      extensionTofiletype = self._getExtensionDictionary()
      fileTypes = []
      for _extension, patterns in extensionTofiletype.items():
        fileTypes.extend(patterns)
      for fType in fileTypes:
        # No idea why the second thing is necessary, but it is there in the original function
        if fType in expectedOutputFile and (fType != '_dst' or '_dst_' in productionFile.lower()):
          filePrototype = outputfileObject['outputFile'].split(fType)[0]
          if filePrototype in productionFile and fType in productionFile:
            appdict.update(outputfileObject)
            appdict['outputFile'] = productionFile + extension
            treatedOutputlist[productionFile] = appdict
            if fType in ('_rec', '_dst'):  # there will only be one _rec or _dst file...
              return

  def getBasenameAndExtension(self, filepath):
    """returns tuple of basename and extenion."""
    baseFileName = os.path.basename(filepath)
    extension = self._expectedExtension(baseFileName)
    baseFileNameWoExtension = baseFileName.replace(extension, "")
    return baseFileNameWoExtension, extension

#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#
