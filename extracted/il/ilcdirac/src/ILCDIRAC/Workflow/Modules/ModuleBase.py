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
"""Base class for ILC workflow modules.

Stolen by S. Poss from LHCbSystem.Workflow.Modules

:since: Feb 02, 2010
:author: S. Poss
:author: S. Paterson
"""

from __future__ import print_function
from __future__ import absolute_import
import os
import re
import shutil
import string
import sys
import six.moves.urllib.request
import six.moves.urllib.parse
import six.moves.urllib.error
from collections import defaultdict
from pprint import pformat
from random import choice

from DIRAC import S_OK, S_ERROR, gLogger
from DIRAC.Core.Security.ProxyInfo import getProxyInfoAsString
from DIRAC.Core.Utilities.Adler import fileAdler
from DIRAC.Core.Utilities.Subprocess import shellCall
from DIRAC.TransformationSystem.Client.FileReport import FileReport
from DIRAC.WorkloadManagementSystem.Client.JobReport import JobReport
from DIRAC.Core.Utilities.File import makeGuid
from DIRAC.ConfigurationSystem.Client.Helpers.Operations import Operations
from DIRAC.RequestManagementSystem.Client.Request import Request
from DIRAC.RequestManagementSystem.private.RequestValidator import RequestValidator
from DIRAC.RequestManagementSystem.Client.Operation import Operation
from DIRAC.RequestManagementSystem.Client.File import File

from ILCDIRAC.Core.Utilities.CombinedSoftwareInstallation import getSoftwareFolder, checkCVMFS
from ILCDIRAC.Core.Utilities.FindSteeringFileDir import getSteeringFileDir
from ILCDIRAC.Core.Utilities.InputFilesUtilities import getNumberOfEvents
import six
from six.moves import range

__RCSID__ = '$Id$'
LOG = gLogger.getSubLogger(__name__)


def generateRandomString(length=8, chars=string.ascii_letters + string.digits):
  """Return random string of 8 chars, used by :mod:`~ILCDIRAC.Workflow.Modules.PythiaAnalysis` and :mod:`~ILCDIRAC.Workflow.Modules.MokkaAnalysis`"""
  return ''.join([choice(chars) for _ in range(length)])


class ModuleBase(object):
  """Base class of the ILCDIRAC modules.

  Several common utilities are defined here.
  In particular, all sub classes should call the :func:`resolveInputVariables` method, and implement
  the :func:`applicationSpecificInputs`.
  """
  #############################################################################

  def __init__(self):
    """Initialization of module base."""
    super(ModuleBase, self).__init__()
    # FIXME: do we need to do this for every module?
    result = getProxyInfoAsString()
    if not result['OK']:
      LOG.error('Could not obtain proxy information in module environment with message:\n', result['Message'])
    else:
      LOG.info('Payload proxy information:\n', result['Value'])

    self.ops = Operations()

    self.platform = ''
    self.applicationLog = ''
    self.applicationVersion = ''
    self.applicationName = ''
    self.InputData = []  # Will have to become empty list
    self.SteeringFile = ''
    self.energy = 0
    self.NumberOfEvents = 0
    self.WorkflowStartFrom = 0
    self.result = S_ERROR()
    self.InputFile = []
    self.ignoremissingInput = False
    self.OutputFile = ''
    self.jobType = ''
    self.stdError = ''
    self.debug = False
    self.extraCLIarguments = ""
    self.jobID = os.environ.get("JOBID", 0)
    self.eventstring = ['']
    self.excludeAllButEventString = False
    self.ignoreapperrors = False
    self.inputdataMeta = {}
    #############
    # Set from workflow object
    self.workflow_commons = {}
    self.step_commons = {}
    self.workflowStatus = S_OK()
    self.stepStatus = S_OK()
    self.isProdJob = False
    self.productionID = 0
    self.prod_job_id = 0
    self.jobReport = None
    # Make sure this is set everywhere
    os.environ['OMP_NUM_THREADS'] = '1'

  #############################################################################
  def setApplicationStatus(self, status, sendFlag=True):
    """Wraps around setJobApplicationStatus of state update client."""
    if not self.jobID:
      return S_OK('JobID not defined')  # e.g. running locally prior to submission

    LOG.verbose('setJobApplicationStatus(%s,%s)' % (self.jobID, status))

    self.jobReport = self.workflow_commons.get('JobReport', self.jobReport)

    if not self.jobReport:
      return S_OK('No reporting tool given')
    jobStatus = self.jobReport.setApplicationStatus(status, sendFlag)
    if not jobStatus['OK']:
      LOG.warn(jobStatus['Message'])

    return jobStatus

  #############################################################################
  def sendStoredStatusInfo(self):
    """Wraps around sendStoredStatusInfo of state update client."""
    if not self.jobID:
      return S_OK('JobID not defined')  # e.g. running locally prior to submission

    self.jobReport = self.workflow_commons.get('JobReport', self.jobReport)

    if not self.jobReport:
      return S_OK('No reporting tool given')

    sendStatus = self.jobReport.sendStoredStatusInfo()
    if not sendStatus['OK']:
      LOG.error(sendStatus['Message'])

    return sendStatus

  #############################################################################
  def setJobParameter(self, name, value, sendFlag=True):
    """Wraps around setJobParameter of state update client.

    :param str name: job parameter
    :param value: value of the job parameter
    :param bool sendFlag: passed to setJobParameter
    :return: S_OK, S_ERROR
    """
    if not self.jobID:
      return S_OK('JobID not defined')  # e.g. running locally prior to submission

    LOG.verbose('setJobParameter(%s,%s,%s)' % (self.jobID, name, value))

    self.jobReport = self.workflow_commons.get('JobReport', self.jobReport)

    if not self.jobReport:
      return S_OK('No reporting tool given')
    jobParam = self.jobReport.setJobParameter(str(name), str(value), sendFlag)
    if not jobParam['OK']:
      LOG.warn(jobParam['Message'])

    return jobParam

  #############################################################################
  def sendStoredJobParameters(self):
    """Wraps around sendStoredJobParameters of state update client."""
    if not self.jobID:
      return S_OK('JobID not defined')  # e.g. running locally prior to submission

    self.jobReport = self.workflow_commons.get('JobReport', self.jobReport)

    if not self.jobReport:
      return S_OK('No reporting tool given')

    sendStatus = self.jobReport.sendStoredJobParameters()
    if not sendStatus['OK']:
      LOG.error(sendStatus['Message'])

    return sendStatus

  #############################################################################
  def setFileStatus(self, production, lfn, status):
    """Set the file status for the given production in the Production Database.

    :param int production: production ID
    :param str lfn: logical file name of the file that needs status change
    :param str status: status to set
    :return: S_OK(), S_ERROR()
    """
    LOG.verbose('setFileStatus(%s,%s,%s)' % (production, lfn, status))

    fileReport = self.workflow_commons.setdefault('FileReport', FileReport('Transformation/TransformationManager'))
    result = fileReport.setFileStatus(production, lfn, status)
    if not result['OK']:
      LOG.warn(result['Message'])

    self.workflow_commons['FileReport'] = fileReport

    return result

  def getCandidateFiles(self, outputList, outputLFNs, dummy_fileMask):
    """Returns list of candidate files to upload, check if some outputs are missing.

    :param outputList: has the following structure: [ ('outputFile':'','outputDataSE':'','outputPath':'') , (...) ]
    :param outputLFNs: list of output LFNs for the job
    :param dummy_fileMask:  UNUSED output file extensions to restrict the outputs to
    :return: S_OK with dictionary containing type, SE and LFN for files [NOT: restricted by mask]
    """
    fileInfo = {}
    for outputFile in outputList:
      if all(key in outputFile for key in ('outputFile', 'outputDataSE', 'outputPath')):
        fname = outputFile['outputFile']
        fileSE = outputFile['outputDataSE']
        filePath = outputFile['outputPath']
        fileInfo[fname] = {'path': filePath, 'workflowSE': fileSE}
      else:
        LOG.error('Ignoring malformed output data specification', str(outputFile))

    for lfn in outputLFNs:
      LOG.debug("Checking LFN: %s" % lfn)
      if os.path.basename(lfn) in fileInfo:
        fileInfo[os.path.basename(lfn)]['lfn'] = lfn
        LOG.verbose('Found LFN %s for file %s' % (lfn, os.path.basename(lfn)))
        if len(os.path.basename(lfn)) > 127:
          LOG.error('Your file name is WAAAY too long for the FileCatalog. Cannot proceed to upload. Filename:',
                    os.path.basename(lfn))
          return S_ERROR('Filename too long')
        if len(lfn) > 256 + 127:
          LOG.error('Your LFN is WAAAAY too long for the FileCatalog. Cannot proceed to upload. LFN:', lfn)
          return S_ERROR('LFN too long')

    # Check that the list of output files were produced
    for fileName, metadata in list(fileInfo.items()):
      if not os.path.exists(fileName):
        LOG.error('Output data file %s does not exist locally' % fileName)
        if not self.ignoreapperrors:
          return S_ERROR('Output Data Not Found')
        fileInfo.pop(fileName)
    # Check the list of files against the output file mask (if it exists)
    #candidateFiles = {}
    # if fileMask:
      # nothing to do yet, as FileMask is not used
      # for fileName,metadata in fileInfo.items():
      #  if metadata['type'].lower() in fileMask or fileName.split('.')[-1] in fileMask:
      #    candidateFiles[fileName]=metadata
      #  else:
      #    LOG.info('Output file %s was produced but will not be treated (outputDataFileMask is %s)' %(fileName,
      #                                                                    string.join(self.outputDataFileMask,', ')))

      # if not candidateFiles.keys():
      #  return S_OK({}) #nothing to do
    #  candidateFiles = fileInfo
    # else:
      # do not apply mask to files

    candidateFiles = fileInfo
    # Sanity check all final candidate metadata keys are present (return S_ERROR if not)
    mandatoryKeys = ['path', 'workflowSE', 'lfn']  # filedict is used for requests
    for fileName, metadata in candidateFiles.items():
      for key in mandatoryKeys:
        if key not in metadata:
          return S_ERROR('File %s has missing key %s' % (fileName, key))
    return S_OK(candidateFiles)

  #############################################################################
  def getFileMetadata(self, candidateFiles):
    """Returns the candidate file dictionary with associated metadata.

    :param dict candidateFiles: The input candidate files dictionary has the structure: {'lfn':'','path':'','workflowSE':''}
       This also assumes the files are in the current working directory.
    :return: S_OK with File Metadata, S_ERROR
    """
    # Retrieve the POOL File GUID(s) for any final output files
    LOG.info('Will search for POOL GUIDs for: %s' % (', '.join(list(candidateFiles.keys()))))
    pfnGUIDs = {}
    generated = []
    for fname in candidateFiles.keys():
      guid = makeGuid(fname)
      pfnGUIDs[fname] = guid
      generated.append(fname)
    pfnGUID = S_OK(pfnGUIDs)
    pfnGUID['generated'] = generated
    #pfnGUID = getGUID(candidateFiles.keys())
    # if not pfnGUID['OK']:
    #  LOG.error('PoolXMLFile failed to determine POOL GUID(s) for output file list, these will be generated by \
    #                   the DataManager',pfnGUID['Message'])
    #  for fileName in candidateFiles.keys():
    #    candidateFiles[fileName]['guid']=''
    # if pfnGUID['generated']:
    LOG.debug('Generated GUID(s) for the following files ', ', '.join(pfnGUID['generated']))
    # else:
    #  LOG.info('GUIDs found for all specified POOL files: %s' %(string.join(candidateFiles.keys(),', ')))

    for pfn, guid in pfnGUID['Value'].items():
      candidateFiles[pfn]['GUID'] = guid

    # Get all additional metadata about the file necessary for requests
    final = {}
    for fileName, metadata in candidateFiles.items():
      fileDict = {}
      fileDict['LFN'] = metadata['lfn']
      fileDict['Size'] = os.path.getsize(fileName)
      adlerChecksum = fileAdler(fileName)
      fileDict['Addler'] = adlerChecksum
      fileDict['ADLER32'] = adlerChecksum
      fileDict['Checksum'] = adlerChecksum
      fileDict['ChecksumType'] = "ADLER32"
      fileDict['GUID'] = metadata['GUID']
      fileDict['Status'] = "Waiting"

      final[fileName] = metadata
      final[fileName]['filedict'] = fileDict
      final[fileName]['localpath'] = '%s/%s' % (os.getcwd(), fileName)

    # Sanity check all final candidate metadata keys are present (return S_ERROR if not)
    mandatoryKeys = ['GUID', 'filedict']  # filedict is used for requests (this method adds guid and filedict)
    for fileName, metadata in final.items():
      for key in mandatoryKeys:
        if key not in metadata:
          return S_ERROR('File %s has missing %s' % (fileName, key))

    return S_OK(final)

  def _getRequestContainer(self):
    """just return the Request reporter (object)"""
    if 'Request' not in self.workflow_commons or not self.workflow_commons['Request'].RequestName:
      self.workflow_commons['Request'] = Request()
      self.workflow_commons['Request'].RequestName = 'job_%d_request.xml' % int(self.jobID)
      self.workflow_commons['Request'].JobID = int(self.jobID)
      self.workflow_commons['Request'].SourceComponent = "Job_%d" % int(self.jobID)
    return self.workflow_commons['Request']
  #############################################################################

  def _getJobReporter(self):
    """just return the job reporter (object, always defined by dirac-jobexec)"""

    if 'JobReport' not in self.workflow_commons:
      self.workflow_commons['JobReport'] = JobReport(self.jobID)
    return self.workflow_commons['JobReport']

  def resolveInputVariables(self):
    """Common utility for all sub classes, resolve the workflow parameters for the current step.

    Module parameters are resolved directly.
    """
    PLACE_HOLDER = "__PLACEHOLDER__"
    LOG.info("Calling module:", self.__class__)
    LOG.info("Workflow commons:\n", pformat(self.workflow_commons))
    LOG.info("Request:", pformat(self.workflow_commons.get('Request')))
    LOG.info("Step commons:\n", pformat(self.step_commons))

    for stepPar, stepValue in self.step_commons.items():
      stepValueOrg = stepValue
      LOG.debug('Checking %r with %r' % (stepPar, stepValue))
      if not isinstance(stepValue, str):
        continue
      stepValue = six.moves.urllib.parse.unquote(stepValue)

      if '%n' in stepValue:
        stepValue = stepValue.replace('%n', PLACE_HOLDER)
      stepValue = stepValue % self.workflow_commons
      if PLACE_HOLDER in stepValue:
        stepValue = stepValue.replace(PLACE_HOLDER, '%n')
      if stepValueOrg != stepValue:
        self.step_commons[stepPar] = stepValue
        LOG.info('Replaced in parameter %r with value %r to %r' % (stepPar, stepValueOrg, stepValue))

    self.jobReport = self._getJobReporter()

    self.prod_job_id = int(self.workflow_commons.get("JOB_ID", self.prod_job_id))
    if self.workflow_commons.get("IS_PROD", False):
      self.productionID = int(self.workflow_commons["PRODUCTION_ID"])
      self.isProdJob = True

    self.platform = self.workflow_commons.get('Platform', self.platform)

    # FIXME: Necessary for backward compatibility, can be removed eventually
    # (once all productions defined with v6r8/9 are gone)
    if 'Platform' not in self.workflow_commons and 'SystemConfig' in self.workflow_commons:
      self.platform = self.workflow_commons.get('SystemConfig')

    self.ignoreapperrors = self.workflow_commons.get('IgnoreAppError', self.ignoreapperrors)

    self.applicationName = self.step_commons.get('applicationName', self.applicationName)

    self.applicationVersion = self.step_commons.get('applicationVersion', self.applicationVersion)

    self.applicationLog = self.step_commons.get('applicationLog', self.applicationLog)

    self.extraCLIarguments = six.moves.urllib.parse.unquote(
        self.step_commons.get('ExtraCLIArguments', self.extraCLIarguments))

    self.SteeringFile = self.step_commons.get('SteeringFile', self.SteeringFile)

    self.jobType = self.workflow_commons.get('JobType', self.jobType)

    self.energy = self.workflow_commons.get('Energy', self.energy)

    if 'NbOfEvts' in self.workflow_commons and self.workflow_commons['NbOfEvts'] > 0:
      self.NumberOfEvents = self.workflow_commons['NbOfEvts']

    if 'StartFrom' in self.workflow_commons and self.workflow_commons['StartFrom'] > 0:
      self.WorkflowStartFrom = self.workflow_commons['StartFrom']

    if 'InputFile' in self.step_commons:
      # This must stay, otherwise, linking between steps is impossible: OutputFile is a string
      inputf = self.step_commons['InputFile']
      if not isinstance(inputf, list):
        if inputf:
          inputf = inputf.split(";")
        else:
          inputf = []
      self.InputFile = inputf

    self.ignoremissingInput = self.step_commons.get('ForgetInput', self.ignoremissingInput)

    if 'InputData' in self.workflow_commons:
      inputdata = self.workflow_commons['InputData']
      if not isinstance(inputdata, list):
        if inputdata:
          self.InputData = inputdata.split(";")
          self.InputData = [x.replace("LFN:", "") for x in self.InputData]
      else:
        self.InputData = [x.replace("LFN:", "") for x in inputdata]

    if 'ParametricInputData' in self.workflow_commons:
      paramdata = self.workflow_commons['ParametricInputData']
      if not isinstance(paramdata, list):
        if paramdata:
          self.InputData = [x.replace("LFN:", "") for x in paramdata.split(";")]
      else:
        # paramdata is a list, and we might need to get rid of "LFN:"
        self.InputData = [x.replace("LFN:", "") for x in paramdata]

    # only if OutputFile is not set
    if not self.OutputFile:
      self.OutputFile = self.step_commons.get("OutputFile", '')

    # Next is also a module parameter, should be already set
    self.debug = self.step_commons.get('debug', self.debug)

    if self.InputData and not self.NumberOfEvents:
      resNE = getNumberOfEvents(self.InputData)
      # NumberOfEvents == 0 does not necessarily mean things went wrong... This
      # is really almost(?)  impossible to solve, sometimes NumberOfEvents can
      # be 0 and then the correct number is already found in the steering file
      # provided to the job. Only in case of productions can we expect that we
      # always get number of events from somewhere. So we would need to check for production ID
      if not resNE['OK'] and self.NumberOfEvents == 0 and self.isProdJob:
        return S_ERROR("Failed to get NumberOfEvents from FileCatalog")
      if not resNE['OK'] and self.NumberOfEvents == 0 and not self.isProdJob:
        LOG.warn("Failed to get NumberOfEvents from FileCatalog, but this is not a production job")
      if resNE['OK']:
        eventsMeta = resNE['Value']
        self.inputdataMeta.update(eventsMeta['AdditionalMeta'])
        if eventsMeta["nbevts"]:
          if self.NumberOfEvents > eventsMeta['nbevts'] or self.NumberOfEvents == 0:
            self.NumberOfEvents = eventsMeta['nbevts']
      LOG.info("NumberOfEvents = %s" % str(self.NumberOfEvents))

    res = self.applicationSpecificInputs()
    if not res['OK']:
      return res
    return S_OK('Parameters resolved')

  def applicationSpecificInputs(self):
    """Method overwritten by sub classes.

    Called from the above.
    """
    return S_OK()

  def execute(self):
    """The execute method.

    This is called by the workflow wrapper when the module is needed
    Here we do preliminary things like resolving the application parameters and we definitely do not get a dedicated directory.
    """

    result = self.resolveInputVariables()
    if not result['OK']:
      LOG.error("Failed to resolve input variables:", result['Message'])
      return result

    # because we need to make sure this does not overwrite steering files provided  by the user
    # it must be here.
    if "SteeringFileVers" in self.step_commons:
      resSteering = self.treatSteeringFiles()
      if not resSteering['OK']:
        return resSteering

    resConf = self.treatConfigPackage()
    if not resConf['OK']:
      return resConf

    if self.SteeringFile:
      if os.path.exists(os.path.basename(self.SteeringFile)):
        LOG.verbose("Found local copy of %s" % self.SteeringFile)

    appres = self.runIt()
    if not appres["OK"]:
      LOG.error("Somehow the application did not exit properly")

    self.listDir()

    return appres

  def listDir(self):
    """List the current directories content."""
    ldir = os.listdir(os.getcwd())
    LOG.verbose("Base directory content:", "\n".join(ldir))

  def runIt(self):
    """Dummy call, needs to be overwritten by the actual applications."""
    return S_OK()

  def finalStatusReport(self, status):
    """Catch the resulting application status, and return corresponding workflow status."""
    message = '%s %s Successful' % (self.applicationName, self.applicationVersion)
    if status:
      LOG.error("==================================\n StdError:\n")
      LOG.error(self.stdError)
      message = '%s exited With Status %s' % (self.applicationName, status)
      self.setApplicationStatus(message)
      LOG.error(message)
      errorKey = "%s_%s" % (self.applicationName, self.applicationVersion)
      self.workflow_commons.setdefault('ErrorDict', defaultdict(list))[errorKey].extend([message, self.stdError])
      if not self.ignoreapperrors:
        return S_ERROR(message)
    else:
      self.setApplicationStatus('%s %s Successful' % (self.applicationName, self.applicationVersion))
    return S_OK(message)

  #############################################################################

  def generateFailoverFile(self):
    """Retrieve the accumulated reporting request, and produce a JSON file that is consumed by the JobWrapper."""
    request = self._getRequestContainer()
    LOG.notice("Request Before: %s" % pformat(request))
    reportRequest = None
    resultJR = self.jobReport.generateForwardDISET()
    if not resultJR['OK']:
      LOG.warn("Could not generate Operation for job report with result:\n%s" % (resultJR))
    else:
      reportRequest = resultJR['Value']
    if reportRequest:
      LOG.info("Populating request with job report information")
      request.addOperation(reportRequest)

    accountingReport = self.workflow_commons.get('AccountingReport', None)
    if accountingReport:
      resultAR = accountingReport.commit()
      if not resultAR['OK']:
        LOG.error("!!! Both Accounting and RequestDB are down? !!!")
        return resultAR

    if not self.workflowStatus['OK'] or not self.stepStatus['OK']:
      if 'ProductionOutputData' in self.workflow_commons:
        prodOutputLFNs = self.workflow_commons['ProductionOutputData'].split(";")
        LOG.info("There was some kind of error, cleaning up outputData: %s" % prodOutputLFNs)
        self.setApplicationStatus("Creating Removal Requests")
        self._cleanUp(prodOutputLFNs)

    if not len(request):  # pylint: disable=len-as-condition
      LOG.info("No Requests to process ")
      return S_OK()

    isValid = RequestValidator().validate(request)
    if not isValid['OK']:
      raise RuntimeError("Failover request is not valid: %s" % isValid['Message'])

    requestJSON = request.toJSON()
    if not requestJSON['OK']:
      raise RuntimeError(requestJSON['Message'])

    LOG.info("Creating failover request for deferred operations for job %d" % int(self.jobID))
    request_string = str(requestJSON['Value'])
    LOG.debug(request_string)
    # Write out the request string
    fname = '%s_%s_request.json' % (self.productionID, self.prod_job_id)
    with open(fname, 'w') as jsonFile:
      jsonFile.write(request_string)
    LOG.info("Created file containing failover request %s" % fname)
    resultDigest = request.getDigest()
    if resultDigest['OK']:
      LOG.info("Digest of the request: %s" % resultDigest['Value'])
    else:
      LOG.error("No digest? That's not sooo important, anyway: %s" % resultDigest['Message'])

    LOG.notice("Request After: %s" % pformat(request))
    return S_OK()

  def redirectLogOutput(self, fd, message):
    """Catch the output from the application print ``message`` to stdout and to the ``self.applicationLog`` file.

    * If ``self.eventstring`` is None print everything.
    * If it is an empty list, an empty string, or an empty string in a list print nothing
    * If it is a string or a list of strings print only matching strings

    :param int fd: if 1 append message to ``self.stdError``
    :param str message: message string
    :returns: None
    """
    sys.stdout.flush()
    if not message:
      return
    if fd == 1:
      self.stdError += message

    if isinstance(self.eventstring, six.string_types):
      self.eventstring = [self.eventstring]

    if self.eventstring is None:
      print(message)

    elif self.eventstring and self.eventstring[0]:
      for mystring in self.eventstring:
        if re.search(re.escape(mystring), message):
          print(message)
          break

    if not self.applicationLog:
      LOG.error("Application Log file not defined")
      return

    with open(self.applicationLog, 'at') as log:
      if self.excludeAllButEventString and isinstance(self.eventstring, list) and self.eventstring[0]:
        for mystring in self.eventstring:
          if re.search(re.escape(mystring), message):
            log.write(message + '\n')
            break
      elif not self.excludeAllButEventString:
        log.write(message + '\n')

  def addRemovalRequests(self, lfnList):
    """Create removalRequests for lfns in lfnList and add it to the common request."""
    LOG.info("Adding removal request")
    request = self._getRequestContainer()
    remove = Operation()
    remove.Type = "RemoveFile"

    for lfn in lfnList:
      rmFile = File()
      rmFile.LFN = lfn
      remove.addFile(rmFile)

    request.addOperation(remove)
    self.workflow_commons['Request'] = request

  def logWorkingDirectory(self):
    """log the content of the working directory."""
    res = shellCall(0, 'ls -laR')
    if res['OK'] and res['Value'][0] == 0:
      LOG.info('The contents of the working directory...')
      LOG.info(str(res['Value'][1]))
    else:
      LOG.error('Failed to list the working directory', str(res['Value'][2]))

    #############################################################################
  def _cleanUp(self, lfnList):
    """Clean up uploaded data for the LFNs in the list."""
    typeList = ['RegisterFile', 'ReplicateAndRegister', 'RemoveReplica']
    request = self._getRequestContainer()

    # keep all the requests which are not in typeList or whose file is not in lfnList
    request.__operations__ = [
        op for op in request for opFile in op if op.Type not in typeList or opFile.LFN not in lfnList]

    # just in case put the request object back to common request
    self.workflow_commons['Request'] = request

    # Set removal requests just in case
    self.addRemovalRequests(lfnList)

    return S_OK()

  def treatSteeringFiles(self):
    """treat steeringfiles."""
    steeringfilevers = self.step_commons["SteeringFileVers"]
    LOG.verbose("Will get all the files from the steeringfiles%s" % steeringfilevers)
    res = getSteeringFileDir(self.platform, steeringfilevers)
    if not res['OK']:
      LOG.error("Cannot find the steering file directory: %s" % steeringfilevers,
                     res['Message'])
      return S_ERROR("Failed to locate steering files %s" % steeringfilevers)
    path = res['Value']
    list_f = os.listdir(path)
    for localFile in list_f:
      if os.path.exists("./" + localFile):
        LOG.verbose("Found local file, don't overwrite")
        # Do not overwrite local files with the same name
        continue
      try:
        if os.path.isdir(os.path.join(path, localFile)):
          shutil.copytree(os.path.join(path, localFile), "./" + localFile)
        else:
          shutil.copy2(os.path.join(path, localFile), "./" + localFile)
      except EnvironmentError as why:
        LOG.error('Could not copy %s here because :' % localFile, str(why))
    return S_OK()

  def treatConfigPackage(self):
    """treat the config software package.

    If a 'ConfigPackage' is part of the workflow_dictionary check for the
    package and copy the steering files to the working directory. Existing files
    are _not_ overwritten.
    """

    # Find if there is a configPackage
    configName = None
    for key in self.workflow_commons:
      if 'ConfigPackage' in key:
        configName = key
        break
    if configName is None:
      LOG.verbose("No ConfigPackage set")
      return S_OK()

    configType = configName.split('ConfigPackage')[0]
    config_dir = self.workflow_commons[configName]
    packageName = str(configType + 'Config').lower()
    configVersion = config_dir.split('Config')[1]
    resCVMFS = checkCVMFS(self.platform, (packageName, configVersion))
    if resCVMFS['OK']:
      configPath = resCVMFS['Value'][0]
    else:
      LOG.error("Cannot find %sConfig on CVMFS" % configType, ("Version: " + config_dir, resCVMFS['Message']))
      resLoc = getSoftwareFolder(self.platform, packageName, configVersion)
      if resLoc['OK']:
        configPath = resLoc['Value']
      else:
        LOG.error("Cannot find %s" % config_dir, resLoc['Message'])
        return S_ERROR('Failed to locate %s as config dir' % config_dir)

    LOG.info("Found %sConfig here:" % configType, configPath)

    list_f = os.listdir(configPath)
    for localFile in list_f:
      if os.path.exists("./" + localFile):
        LOG.verbose("Found local file, don't overwrite:", localFile)
        # Do not overwrite local files with the same name
        continue
      try:
        if os.path.isdir(os.path.join(configPath, localFile)):
          shutil.copytree(os.path.join(configPath, localFile), "./" + localFile)
        else:
          shutil.copy2(os.path.join(configPath, localFile), "./" + localFile)
      except EnvironmentError as why:
        LOG.error('Could not copy %s here because %s!' % (localFile, str(why)))
    return S_OK()
