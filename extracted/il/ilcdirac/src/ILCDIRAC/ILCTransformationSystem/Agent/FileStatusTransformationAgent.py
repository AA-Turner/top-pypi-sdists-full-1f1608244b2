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
"""FileStatusTransformation Agent performs the following actions:

+-----------------------+------------------+---------------------------+--------------+---------------+---------------+
|  Transformation Type  |  Request Status  | Transformation File Status|    Source    |    Target     |    Action     |
+-----------------------+------------------+---------------------------+--------------+---------------+---------------+
| Moving                | Any              | Problematic / Processed   | Available    | Available     | Retry         |
| Replication / Moving  | Any              | Problematic / Processed   | Available    | Not Available | Retry         |
| Moving                | Failed           | Assigned                  | Available    | Available     | Retry         |
| Replication / Moving  | Failed           | Assigned                  | Available    | Not Available | Retry         |
| Replication           | Failed           | Assigned                  | Available    | Available     | Set PROCESSED |
| Replication / Moving  | Any              | Other than Processed      | Not Available| Available     | Set PROCESSED |
| Replication / Moving  | Any              | Any                       | Not Available| Not Available | Set DELETED   |
+-----------------------+------------------+---------------------------+--------------+---------------+---------------+

* If the action is Retry then the request is reset if it exists in RMS, otherwise the file status is set to unused
* Available means the file exists in File Catalog and also exists physically on Storage Elements
* Not Available means the file doesn't exist in File Catalog or one or more replicas are lost on the Storage Elements
"""

from __future__ import absolute_import
import json
from collections import defaultdict

from DIRAC import S_OK, S_ERROR
from DIRAC.Core.Base.AgentModule import AgentModule
from DIRAC.Core.Utilities.PrettyPrint import printTable
from DIRAC.Core.Utilities.List import breakListIntoChunks
from DIRAC.Core.Utilities.Proxy import UserProxy
from DIRAC.FrameworkSystem.Client.NotificationClient import NotificationClient
from DIRAC.TransformationSystem.Client.TransformationClient import TransformationClient
from DIRAC.RequestManagementSystem.Client.ReqClient import ReqClient
from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient
from DIRAC.Resources.Storage.StorageElement import StorageElement
from six.moves import filter

__RCSID__ = "$Id$"

AGENT_NAME = 'ILCTransformation/FileStatusTransformationAgent'

SET_PROCESSED = 'SET_PROCESSED'
SET_DELETED = 'SET_DELETED'
SET_UNUSED = 'SET_UNUSED'

RETRY = 'retry'
RESET_REQUEST = 'RESET_REQUEST'

REPLICATION_TRANS = 'Replication'
MOVING_TRANS = 'Moving'


class FileStatusTransformationAgent(AgentModule):
  """FileStatusTransformationAgent."""

  def __init__(self, *args, **kwargs):
    AgentModule.__init__(self, *args, **kwargs)
    self.name = 'FileStatusTransformationAgent'
    self.enabled = False
    self.shifterProxy = 'DataManager'
    self.transformationTypes = ["Replication"]
    self.transformationStatuses = ["Active"]
    self.transformationFileStatuses = ["Assigned", "Problematic", "Processed", "Unused"]

    self.addressTo = ["andre.philippe.sailer@cern.ch"]
    self.addressFrom = "ilcdirac-admin@cern.ch"
    self.emailSubject = "FileStatusTransformationAgent"

    self.accounting = defaultdict(list)
    self.errors = []

    self.fcClient = FileCatalogClient()
    self.tClient = TransformationClient()
    self.reqClient = ReqClient()
    self.nClient = NotificationClient()

  def checkFileStatusFuncExists(self, status):
    """returns True/False if a function to check transformation files with a given status exists or not."""
    checkFileStatusFuncName = "check_%s_files" % (status.lower())
    if not (hasattr(self, checkFileStatusFuncName) and callable(getattr(self, checkFileStatusFuncName))):
      self.log.warn("Unable to process transformation files with status ", status)
      return False

    return True

  def beginExecution(self):
    """Reload the configurations before every cycle."""
    self.enabled = self.am_getOption('EnableFlag', False)
    self.transformationTypes = self.am_getOption('TransformationTypes', ["Replication"])
    self.transformationStatuses = self.am_getOption('TransformationStatuses', ["Active"])
    self.transformationFileStatuses = self.am_getOption(
        'TransformationFileStatuses', ["Assigned", "Problematic", "Processed", "Unused"])

    self.addressTo = self.am_getOption('MailTo', ["ilcdirac-admin@cern.ch"])
    self.addressFrom = self.am_getOption('MailFrom', "ilcdirac-admin@cern.ch")

    self.transformationFileStatuses = list(filter(self.checkFileStatusFuncExists, self.transformationFileStatuses))
    self.accounting.clear()

    return S_OK()

  def sendNotification(self, transID, transType=None, sourceSEs=None, targetSEs=None):
    """sends email notification about accounting information of a transformation."""
    if not(self.errors or self.accounting):
      return S_OK()

    emailBody = "Transformation ID: %s\n" % transID
    if transType:
      emailBody += "Transformation Type: %s\n" % transType

    if sourceSEs:
      emailBody += "Source SE: %s\n" % (" ".join(str(source) for source in sourceSEs))

    if targetSEs:
      emailBody += "Target SE: %s\n\n" % (" ".join(str(target) for target in targetSEs))

    rows = []
    for action, transFiles in self.accounting.items():
      emailBody += "Total number of files with action %s: %s\n" % (action, len(transFiles))
      for transFile in transFiles:
        rows.append([[transFile['LFN']], [str(transFile['AvailableOnSource'])],
                     [str(transFile['AvailableOnTarget'])], [transFile['Status']], [action]])

    if rows:
      columns = ["LFN", "Source", "Target", "Old Status", "Action"]
      emailBody += printTable(columns, rows, printOut=False, numbering=False, columnSeparator=' | ')

    if self.errors:
      emailBody += "\n\nErrors:"
      emailBody += "\n".join(self.errors)

    self.log.notice(emailBody)
    subject = "%s: %s" % (self.emailSubject, transID)
    for address in self.addressTo:
      res = self.nClient.sendMail(address, subject, emailBody, self.addressFrom, localAttempt=False)
      if not res['OK']:
        self.log.error("Failure to send Email notification to ", address)
        continue

    self.errors = []
    self.accounting.clear()
    return S_OK()

  def logError(self, errStr, varMsg=''):
    self.log.error(errStr, varMsg)
    self.errors.append(errStr + varMsg)

  def execute(self):
    """main execution loop of Agent."""

    res = self.getTransformations()
    if not res['OK']:
      self.log.error('Failure to get transformations', res['Message'])
      return S_ERROR("Failure to get transformations")

    transformations = res['Value']
    if not transformations:
      self.log.notice('No transformations found with Status %s and Type %s ' %
                      (self.transformationStatuses, self.transformationTypes))
      return S_OK()

    self.log.notice('Will treat %d transformations' % len(transformations))
    self.log.notice('Transformations: %s' % ",".join([str(transformation['TransformationID'])
                                                      for transformation in transformations]))

    for trans in transformations:
      transID = trans['TransformationID']
      if 'SourceSE' not in trans or not trans['SourceSE']:
        self.logError("SourceSE not set for transformation, skip processing, transID: ", "%s" % transID)
        self.sendNotification(transID)
        continue

      if 'TargetSE' not in trans or not trans['TargetSE']:
        self.logError("TargetSE not set for transformation, skip processing, transID: ", "%s" % transID)
        self.sendNotification(transID, sourceSEs=trans['SourceSE'])
        continue

      if 'DataTransType' not in trans:
        self.logError("Transformation Type not set for transformation, skip processing, transID: ", "%s" % transID)
        self.sendNotification(transID, sourceSEs=trans['SourceSE'], targetSEs=trans['TargetSE'])
        continue

      res = self.processTransformation(transID, trans['SourceSE'], trans['TargetSE'], trans['DataTransType'], trans)
      if not res['OK']:
        self.log.error('Failure to process transformation with ID:', transID)
        continue

    return S_OK()

  def getTransformations(self, transID=None):
    """returns transformations of a given type and status."""
    res = None
    if transID:
      res = self.tClient.getTransformations(
          condDict={'TransformationID': transID,
                    'Status': self.transformationStatuses,
                    'Type': self.transformationTypes})
    else:
      res = self.tClient.getTransformations(
          condDict={'Status': self.transformationStatuses, 'Type': self.transformationTypes})

    if not res['OK']:
      return res

    result = res['Value']
    for trans in result:
      res = self.tClient.getTransformationParameters(trans['TransformationID'], ['SourceSE', 'TargetSE'])
      if not res['OK']:
        self.log.error('Failure to get SourceSE and TargetSE parameters for Transformation ID:',
                       trans['TransformationID'])
        continue

      trans['SourceSE'] = eval(res['Value']['SourceSE'])
      trans['TargetSE'] = eval(res['Value']['TargetSE'])

      res = self.getDataTransformationType(trans['TransformationID'])
      if not res['OK']:
        self.log.error('Failure to determine Data Transformation Type', "%s: %s"
                       % (trans['TransformationID'], res['Message']))
        continue

      trans['DataTransType'] = res['Value']

    return S_OK(result)

  def getRequestStatus(self, transID, taskIDs):
    """returns request statuses for a given list of task IDs."""
    res = self.tClient.getTransformationTasks(condDict={'TransformationID': transID, 'TaskID': taskIDs})
    if not res['OK']:
      self.log.error('Failure to get Transformation Tasks for Transformation ID:', transID)
      return res

    result = res['Value']
    requestStatus = {}
    for task in result:
      requestStatus[task['TaskID']] = {'RequestStatus': task['ExternalStatus'], 'RequestID': int(task['ExternalID'])}

    return S_OK(requestStatus)

  def getDataTransformationType(self, transID):
    """returns transformation types Replication/Moving/Unknown for a given transformation."""
    res = self.tClient.getTransformationParameters(transID, 'Body')
    if not res['OK']:
      return res

    # if body is empty then we assume that it is a replication transformation
    if not res['Value']:
      return S_OK(REPLICATION_TRANS)

    replication = False
    rmReplica = False
    try:
      body = json.loads(res['Value'])
      for operation in body:
        if 'ReplicateAndRegister' in operation:
          replication = True
        if 'RemoveReplica' in operation:
          rmReplica = True
    except ValueError:
      if 'ReplicateAndRegister' in res['Value']:
        replication = True
        if 'RemoveReplica' in res['Value']:
          rmReplica = True

    if rmReplica and replication:
      return S_OK(MOVING_TRANS)

    if replication:
      return S_OK(REPLICATION_TRANS)

    return S_ERROR("Unknown Transformation Type '%r'" % res['Value'])

  def setFileStatus(self, transID, transFiles, status):
    """sets transformation file status."""

    lfns = [transFile['LFN'] for transFile in transFiles]
    lfnStatuses = {lfn: status for lfn in lfns}

    if lfnStatuses:
      if self.enabled:
        res = self.tClient.setFileStatusForTransformation(transID, newLFNsStatus=lfnStatuses, force=True)
        if not res['OK']:
          self.logError('Failed to set statuses for LFNs ', "%s" % res['Message'])
          return res

      for transFile in transFiles:
        self.accounting[status].append({'LFN': transFile['LFN'],
                                        'Status': transFile['Status'],
                                        'AvailableOnSource': transFile['AvailableOnSource'],
                                        'AvailableOnTarget': transFile['AvailableOnTarget']})
    return S_OK()

  def selectFailedRequests(self, transFile):
    """returns True if transformation file has a failed request otherwise returns False."""
    res = self.getRequestStatus(transFile['TransformationID'], transFile['TaskID'])
    if not res['OK']:
      self.log.error('Failure to get Request Status for Assigned File')
      return False
    result = res['Value']

    if result[transFile['TaskID']]['RequestStatus'] == 'Failed':
      return True

    return False

  def retryStrategyForFiles(self, transID, transFiles):
    """returns retryStrategy Reset Request if a request is found in RMS, otherwise returns set file status to unused."""
    taskIDs = [transFile['TaskID'] for transFile in transFiles]
    res = self.getRequestStatus(transID, taskIDs)
    if not res['OK']:
      return res
    result = res['Value']
    retryStrategy = defaultdict(dict)
    for taskID in taskIDs:
      if taskID is None:
        self.log.error("Task ID is None", "Transformation: %s\n Files: %r " % (transID, transFiles))
        retryStrategy[None]['Strategy'] = SET_UNUSED
        continue
      res = self.reqClient.getRequest(requestID=result[taskID]['RequestID'])
      if not res['OK']:
        self.log.notice('Request %s does not exist setting file status to unused' % result[taskID]['RequestID'])
        retryStrategy[taskID]['Strategy'] = SET_UNUSED
      else:
        retryStrategy[taskID]['Strategy'] = SET_UNUSED  # RESET_REQUEST
        retryStrategy[taskID]['RequestID'] = result[taskID]['RequestID']

    return S_OK(retryStrategy)

  def check_assigned_files(self, actions, transFiles, transType):
    """treatment for transformation files with assigned status."""
    for transFile in transFiles:
      if transFile['AvailableOnSource'] and transFile['AvailableOnTarget']:
        if transType == REPLICATION_TRANS:
          actions[SET_PROCESSED].append(transFile)
        if transType == MOVING_TRANS:
          actions[RETRY].append(transFile)

      elif transFile['AvailableOnSource'] and not transFile['AvailableOnTarget']:
        actions[RETRY].append(transFile)

      elif not transFile['AvailableOnSource'] and transFile['AvailableOnTarget']:
        actions[SET_PROCESSED].append(transFile)

      else:
        # not on src and target
        actions[SET_DELETED].append(transFile)

  def check_unused_files(self, actions, transFiles, transType):
    """treatment for transformation files with unused status."""
    for transFile in transFiles:
      if not transFile['AvailableOnSource'] and transFile['AvailableOnTarget']:
        actions[SET_PROCESSED].append(transFile)

      if not transFile['AvailableOnSource'] and not transFile['AvailableOnTarget']:
        actions[SET_DELETED].append(transFile)

  def check_processed_files(self, actions, transFiles, transType):
    """treatment for transformation files with processed status."""
    for transFile in transFiles:
      if transFile['AvailableOnSource'] and transFile['AvailableOnTarget'] and transType == MOVING_TRANS:
        actions[RETRY].append(transFile)

      if transFile['AvailableOnSource'] and not transFile['AvailableOnTarget']:
        actions[RETRY].append(transFile)

      if not transFile['AvailableOnSource'] and not transFile['AvailableOnTarget']:
        actions[SET_DELETED].append(transFile)

  def check_problematic_files(self, actions, transFiles, transType):
    """treatment for transformation files with problematic status."""
    for transFile in transFiles:
      if transFile['AvailableOnSource'] and transFile['AvailableOnTarget']:
        if transType == REPLICATION_TRANS:
          actions[SET_PROCESSED].append(transFile)
        if transType == MOVING_TRANS:
          actions[RETRY].append(transFile)

      elif transFile['AvailableOnSource'] and not transFile['AvailableOnTarget']:
        actions[RETRY].append(transFile)

      elif not transFile['AvailableOnSource'] and transFile['AvailableOnTarget']:
        actions[SET_PROCESSED].append(transFile)

      else:
        # not available on source and target
        actions[SET_DELETED].append(transFile)

  def retryFiles(self, transID, transFiles):
    """resubmits request or sets file status to unused based on the retry strategy of transformation file."""
    setFilesUnused = []
    setFilesAssigned = []
    res = self.retryStrategyForFiles(transID, transFiles)
    if not res['OK']:
      self.logError('Failure to determine retry strategy (unused / reset request) for files ', "%s" % res['Message'])
      return res

    retryStrategy = res['Value']
    for transFile in transFiles:
      if retryStrategy[transFile['TaskID']]['Strategy'] != RESET_REQUEST:
        setFilesUnused.append(transFile)
        continue

      requestID = retryStrategy[transFile['TaskID']]['RequestID']
      if self.enabled:
        res = self.reqClient.resetFailedRequest(requestID, allR=True)
        if not res['OK']:
          self.logError('Failed to reset request ', 'ReqID: %s Error: %s' % (requestID, res['Message']))
          continue

        if res['Value'] == "Not reset":
          self.logError('Failed to reset request ', 'ReqID: %s is non-recoverable' % requestID)
          continue

        setFilesAssigned.append(transFile)

        res = self.tClient.setTaskStatus(transID, transFile['TaskID'], 'Waiting')
        if not res['OK']:
          self.logError('Failure to set Waiting status for Task ID: ', "%s %s" % (transFile['TaskID'], res['Message']))
          continue

      self.accounting[RESET_REQUEST].append({'LFN': transFile['LFN'],
                                             'Status': transFile['Status'],
                                             'AvailableOnSource': transFile['AvailableOnSource'],
                                             'AvailableOnTarget': transFile['AvailableOnTarget']})

    if setFilesUnused:
      self.setFileStatus(transID, setFilesUnused, 'Unused')

    if setFilesAssigned:
      self.setFileStatus(transID, setFilesAssigned, 'Assigned')

    return S_OK()

  def applyActions(self, transID, actions):
    """sets new file statuses and resets requests."""
    for action, transFiles in actions.items():
      if action == SET_PROCESSED and transFiles:
        self.setFileStatus(transID, transFiles, 'Processed')

      if action == SET_DELETED and transFiles:
        self.setFileStatus(transID, transFiles, 'Deleted')

      if action == RETRY and transFiles:
        # if there is a request in RMS then reset request otherwise set file status unused
        self.retryFiles(transID, transFiles)

  def existsInFC(self, storageElements, lfns):
    """checks if files have replicas registered in File Catalog for all given storageElements."""
    res = {'Successful': {}, 'Failed': {}}
    self.log.info('Looking for replica information for %s files' % len(lfns))
    for index, chunk in enumerate(breakListIntoChunks(lfns, 1000)):
      chunkRes = self.fcClient.getReplicas(chunk)
      if not chunkRes['OK']:
        self.logError('Failed to get replicaInformation: ', chunkRes['Message'])
        return chunkRes
      self.log.info('Chunk %s/%s done' % (index, len(lfns) // 1000))
      res['Successful'].update(chunkRes['Value']['Successful'])
      res['Failed'].update(chunkRes['Value']['Failed'])

    result = {}
    result['Successful'] = {}
    result['Failed'] = {}
    setOfSEs = set(storageElements)

    for lfn, msg in res['Failed'].items():
      if msg == 'No such file or directory':
        result['Successful'][lfn] = False
      else:
        result['Failed'][lfn] = msg

    # check if all replicas are registered in FC
    filesFoundInFC = res['Successful']
    for lfn, replicas in filesFoundInFC.items():
      result['Successful'][lfn] = setOfSEs.issubset(set(replicas))

    return S_OK(result)

  def existsOnSE(self, storageElements, lfns, transInfoDict):
    """checks if the given files exist physically on a list of storage elements."""

    result = {}
    result['Failed'] = {}
    result['Successful'] = {}
    authorDN = transInfoDict['AuthorDN']
    authorGroup = transInfoDict['AuthorGroup']

    if not lfns:
      return S_OK(result)

    voName = lfns[0].split('/')[1]
    chunkSize = 200
    for se in storageElements:
      for index, lfnChunk in enumerate(breakListIntoChunks(lfns, chunkSize)):
        with UserProxy(proxyUserDN=authorDN, proxyUserGroup=authorGroup) as proxyResult:
          if not proxyResult['OK']:
            return S_ERROR('Failed to get a proxy: %s' % proxyResult['Message'])
          self.log.notice('Checking LFNs at', '%s: %s/%s' % (se, chunkSize * index, len(lfns)))
          res = StorageElement(se, vo=voName).exists(lfnChunk)
          if not res['OK']:
            return res
          for lfn, status in res['Value']['Successful'].items():
            if lfn not in result['Successful']:
              result['Successful'][lfn] = status
            if not status:
              result['Successful'][lfn] = False
          result['Failed'].setdefault(se, {}).update(res['Value']['Failed'])

    return S_OK(result)

  def exists(self, storageElements, lfns, transInfoDict):
    """checks if files exists on both file catalog and storage elements."""

    fcRes = self.existsInFC(storageElements, lfns)
    if not fcRes['OK']:
      self.logError('Failure to determine if files exists in File Catalog: ', fcRes['Message'])
      return fcRes

    if fcRes['Value']['Failed']:
      self.logError("Failed FileCatalog Response ", "%s" % fcRes['Value']['Failed'])

    # check if files found in file catalog also exist on SE
    checkLFNsOnStorage = [lfn for lfn in fcRes['Value']['Successful'] if fcRes['Value']['Successful'][lfn]]

    # no files were found in FC, return the result instead of verifying them on SE
    if not checkLFNsOnStorage:
      return fcRes

    seRes = self.existsOnSE(storageElements, checkLFNsOnStorage, transInfoDict)
    if not seRes['OK']:
      self.logError('Failure to determine if files exist on SE ', "%s" % seRes['Message'])
      return seRes

    for se in storageElements:
      if seRes['Value']['Failed'][se]:
        self.logError('Failed to determine if files exist on SE ', "%s %s" % (se, seRes['Value']['Failed'][se]))
        return S_ERROR()

    fcResult = fcRes['Value']['Successful']
    seResult = seRes['Value']['Successful']
    for lfn in fcResult:
      if fcResult[lfn] and not seResult[lfn]:
        fcRes['Value']['Successful'][lfn] = False

    return fcRes

  def processTransformation(self, transID, sourceSE, targetSEs, transType, transInfoDict):
    """process transformation for a given transformation ID."""

    actions = {}
    actions[SET_PROCESSED] = []
    actions[RETRY] = []
    actions[SET_DELETED] = []

    for status in self.transformationFileStatuses:
      res = self.tClient.getTransformationFiles(condDict={'TransformationID': transID, 'Status': status})
      if not res['OK']:
        errStr = 'Failure to get Transformation Files, Status: %s Transformation ID: %s Message: %s' % (status,
                                                                                                        transID,
                                                                                                        res['Message'])
        self.logError(errStr)
        continue

      transFiles = res['Value']
      if not transFiles:
        self.log.notice("No Transformation Files found with status %s for Transformation ID %d" % (status, transID))
        continue

      self.log.notice("Processing Transformation Files with status %s for TransformationID %d " % (status, transID))

      if status == 'Assigned':
        transFiles = list(filter(self.selectFailedRequests, transFiles))

      lfns = [transFile['LFN'] for transFile in transFiles]

      if not lfns:
        continue

      res = self.exists(sourceSE, lfns, transInfoDict)
      if not res['OK']:
        continue

      resultSourceSe = res['Value']['Successful']

      res = self.exists(targetSEs, lfns, transInfoDict)
      if not res['OK']:
        continue
      resultTargetSEs = res['Value']['Successful']

      for transFile in transFiles:
        lfn = transFile['LFN']
        transFile['AvailableOnSource'] = resultSourceSe[lfn]
        transFile['AvailableOnTarget'] = resultTargetSEs[lfn]

      checkFilesFuncName = "check_%s_files" % status.lower()
      checkFiles = getattr(self, checkFilesFuncName)
      checkFiles(actions, transFiles, transType)

    self.applyActions(transID, actions)
    self.sendNotification(transID, transType, sourceSE, targetSEs)

    return S_OK()
