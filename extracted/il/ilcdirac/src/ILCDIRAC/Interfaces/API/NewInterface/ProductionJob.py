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
"""Production Job class. Used to define new productions.

Mostly similar to :mod:`~ILCDIRAC.Interfaces.API.NewInterface.UserJob`, but
cannot be (and should not be) used like the
:mod:`~ILCDIRAC.Interfaces.API.NewInterface.UserJob` class.

:author: Stephane Poss
:author: Remi Ete
:author: Ching Bon Lam
"""

from __future__ import print_function
from __future__ import absolute_import
import os
import shutil

from collections import defaultdict
from decimal import Decimal

from DIRAC import S_OK, S_ERROR, gLogger
from DIRAC.Core.Utilities.ReturnValues import returnSingleResult
from DIRAC.ConfigurationSystem.Client.Helpers.Operations import Operations
from DIRAC.ConfigurationSystem.Client.Helpers.Registry import getVOForGroup
from DIRAC.Core.Security.ProxyInfo import getProxyInfo
from DIRAC.Core.Workflow.Module import ModuleDefinition
from DIRAC.Core.Workflow.Step import StepDefinition
from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient
from DIRAC.TransformationSystem.Client.TransformationClient import TransformationClient

from ILCDIRAC.ILCTransformationSystem.Client.Transformation import Transformation
from ILCDIRAC.Interfaces.API.NewInterface.Job import Job
from ILCDIRAC.Interfaces.Utilities import JobHelpers
import six

__RCSID__ = "$Id$"

LOG = gLogger.getSubLogger(__name__)


class ProductionJob(Job):  # pylint: disable=too-many-public-methods, too-many-instance-attributes
  """Production job class.

  Suitable for CLIC studies. Need to sub class and overload for other clients.
  """

  def __init__(self, script=None):
    super(ProductionJob, self).__init__(script)
    self.prodVersion = __RCSID__
    self.dryrun = False
    self.created = False
    self.checked = False
    self.call_finalization = False
    self.finalsdict = {}
    self.transfid = 0
    self.type = 'Production'
    self.csSection = '/Production/Defaults'
    self.ops = Operations()
    self.fc = FileCatalogClient()
    self.trc = TransformationClient()
    self.defaultProdID = '12345'
    self.defaultProdJobID = '12345'
    self.jobFileGroupSize = 1
    self.nbtasks = 1
    self.slicesize = 0
    self.basename = ''
    self.basepath = self.ops.getValue('/Production/CLIC/BasePath', '/ilc/prod/clic/')
    self.evttype = ''
    self.datatype = ''
    self.energycat = ''
    self.detector = ''
    self.currtrans = None
    self.description = ''
    self.generator = None
    self.campaign = ''

    self.finalpaths = []
    self.finalMetaDict = defaultdict(dict)
    self.prodMetaDict = {}
    self.finalMetaDictNonSearch = {}
    self.metadict_external = {}
    self.specialFinalMetaData = {}
    self.outputStorage = ''

    self.proxyinfo = getProxyInfo()
    self.vo = getVOForGroup(self.proxyinfo.get('Value', {}).get('group', 'ilc_user'))

    self.inputdataquery = False
    self.inputBKSelection = {}
    self.plugin = 'Standard'
    self.prodGroup = ''

    self.prodTypes = ['MCGeneration', 'MCSimulation', 'Test', 'MCReconstruction',
                      'MCReconstruction_Overlay', 'Merge', 'Split',
                      'MCGeneration_ILD',
                      'MCSimulation_ILD',
                      'MCReconstruction_ILD',
                      'MCReconstruction_Overlay_ILD',
                      'Split_ILD'
                     ]
    self.prodparameters = {}
    self.prodparameters['NbInputFiles'] = 1
    self.prodparameters['nbevts'] = 0
    #self.prodparameters["SWPackages"] = ''
    self._addParameter(self.workflow, "IS_PROD", 'JDL', True, "This job is a production job")
    if not script:
      self.__setDefaults()

    self._recBasePaths = {}
    self.maxFCFoldersToCheck = 100000

  #############################################################################
  def __setDefaults(self):
    """Sets some default parameters."""
    self.setPlatform(self.ops.getValue('%s/Platform' % (self.csSection), 'x86_64-slc5-gcc43-opt'))
    self.setCPUTime('300000')
    self.setLogLevel('verbose')
    self.setJobGroup('@{PRODUCTION_ID}')

    # version control
    self._setParameter('productionVersion', 'string', self.prodVersion, 'ProdAPIVersion')

    # General workflow parameters
    self._setParameter('PRODUCTION_ID', 'string', self.defaultProdID.zfill(8), 'ProductionID')
    self._setParameter('JOB_ID', 'string', self.defaultProdJobID.zfill(8), 'ProductionJobID')
    self._setParameter('Priority', 'JDL', '1', 'Priority')
    self._setParameter('emailAddress', 'string', 'ilcdirac-support@cern.ch', 'CrashEmailAddress')

  def _setParameter(self, name, parameterType, parameterValue, description):
    """Set parameters checking in CS in case some defaults need to be changed."""
    if self.ops.getValue('%s/%s' % (self.csSection, name), ''):
      LOG.debug('Setting %s from CS defaults = %s' % (name, self.ops.getValue('%s/%s' % (self.csSection, name))))
      self._addParameter(self.workflow, name, parameterType, self.ops.getValue('%s/%s' % (self.csSection, name),
                                                                               'default'), description)
    else:
      LOG.debug('Setting parameter %s = %s' % (name, parameterValue))
      self._addParameter(self.workflow, name, parameterType, parameterValue, description)

  def setConfig(self, version):
    """Define the Configuration package to obtain."""
    appName = 'ILDConfig'
    self._addSoftware(appName.lower(), version)
    self.prodparameters['ILDConfigVersion'] = version
    self._addParameter(self.workflow, 'ILDConfigPackage', 'JDL', appName + version, 'ILDConfig package')
    return S_OK()

  def setConfigPackage(self, appName, version):
    """Define the config package to obtain.

    Adds Config package to workflow execution, and sets production parameter.
    See :func:`ILCDIRAC.Interfaces.API.NewInterface.Job.Job.setConfigPackage`

    :param str appName: name of the ConfigPackage, e.g. 'ClicConfig'
    :param str version: version of the ConfigPackage
    """
    super(ProductionJob, self).setConfigPackage(appName, version)
    self.prodparameters[appName + 'Version'] = version
    return S_OK()

  def setDryRun(self, run):
    """In case one wants to get all the info as if the prod was being submitted."""
    self.dryrun = run

  #############################################################################
  def setProdGroup(self, group):
    """Sets a user defined tag for the production as appears on the monitoring page."""
    self.prodGroup = group
  #############################################################################

  def setProdPlugin(self, plugin):
    """Sets the plugin to be used to creating the production jobs."""
    self.plugin = plugin

  #############################################################################
  def setJobFileGroupSize(self, files):
    """Sets the number of files to be input to each job created."""
    if self.checked:
      return self._reportError("This input is needed at the beginning of the production definition: it is \
      needed for total number of evts.")
    self.jobFileGroupSize = files
    self.prodparameters['NbInputFiles'] = files

  def setNbEvtsPerSlice(self, nbevts):
    """Define the number of events in a slice."""
    self.slicesize = nbevts

  #############################################################################
  def setProdType(self, prodType):
    """Set prod type."""
    if prodType not in self.prodTypes:
      raise TypeError('Prod must be one of %s' % (', '.join(self.prodTypes)))
    self.setType(prodType)
  #############################################################################

  def setWorkflowName(self, name):
    """Set workflow name."""
    self.workflow.setName(name)
    self.name = name

  #############################################################################
  def setWorkflowDescription(self, desc):
    """Set workflow name."""
    self.workflow.setDescription(desc)

  #############################################################################
  def createWorkflow(self):
    """Create XML for local testing."""
    name = '%s.xml' % self.name
    if os.path.exists(name):
      shutil.move(name, '%s.backup' % name)
    self.workflow.toXMLFile(name)

  #############################################################################
  def setOutputSE(self, outputse):
    """Define where the output file(s) will go."""
    self.outputStorage = outputse
    return S_OK()

  #############################################################################
  def setInputDataQuery(self, metadata):
    """Define the input data query needed."""

    retMetaKey = self._checkMetaKeys(list(metadata.keys()))
    if not retMetaKey['OK']:
      return retMetaKey
    LOG.notice('InputMetaQuery: %s' % metadata)

    if "ProdID" not in metadata:
      return self._reportError("Input metadata dictionary must contain at least a key 'ProdID' as reference")
    retDirs = self._checkFindDirectories(metadata)
    if not retDirs['OK']:
      return retDirs
    dirs = list(retDirs['Value'].values())
    for mdir in dirs[:self.maxFCFoldersToCheck]:
      LOG.notice("Directory: %s" % mdir)
      res = self.fc.getDirectoryUserMetadata(mdir)
      if not res['OK']:
        return self._reportError("Error looking up the catalog for directory metadata")
      compatmeta = res['Value']
      compatmeta.update(metadata)

    if 'EvtType' in compatmeta:
      self.evttype = JobHelpers.getValue(compatmeta['EvtType'], str, six.string_types)
    else:
      return self._reportError("EvtType is not in the metadata, it has to be!")

    if 'NumberOfEvents' in compatmeta:
      self.nbevts = JobHelpers.getValue(compatmeta['NumberOfEvents'], int, None)

    self.basename = self.evttype

    self.generator = compatmeta.get('Generator', None)

    LOG.notice("MetaData: %s" % compatmeta)
    LOG.notice("MetaData: %s" % metadata)
    if "Energy" in compatmeta:
      self.energycat = JobHelpers.getValue(compatmeta["Energy"], str, (int, int, six.string_types))

    if self.energycat.count("tev"):
      self.energy = Decimal("1000.") * Decimal(self.energycat.split("tev")[0])
    elif self.energycat.count("gev"):
      self.energy = Decimal("1.") * Decimal(self.energycat.split("gev")[0])
    else:
      self.energy = Decimal("1.") * Decimal(self.energycat)
    gendata = False
    if 'Datatype' in compatmeta:
      self.datatype = JobHelpers.getValue(compatmeta['Datatype'], str, six.string_types)
      if self.datatype == 'gen':
        gendata = True
    if "DetectorType" in compatmeta and not gendata:
      self.detector = JobHelpers.getValue(compatmeta["DetectorType"], str, six.string_types)
    self.inputBKSelection = metadata
    self.inputdataquery = True

    self.prodparameters['nbevts'] = self.nbevts
    self.prodparameters["FCInputQuery"] = self.inputBKSelection

    return S_OK()

  def setDescription(self, desc):
    """Set the production's description.

    :param str desc: Description
    """
    self.description = desc
    return S_OK()

  def getBasePath(self):
    """Return the base path.

    Updated by :any:`setInputDataQuery`.
    """
    return self.basepath

  def addFinalization(self, uploadData=False, registerData=False, uploadLog=False, sendFailover=False):
    """Add finalization step.

    :param bool uploadData: Upload or not the data to the storage
    :param bool uploadLog: Upload log file to storage (currently only available for admins, thus add them to OutputSandbox)
    :param bool sendFailover: Send Failover requests, and declare files as processed or unused in transfDB
    :param bool registerData: Register data in the file catalog
    """
    # TODO: Do the registration only once, instead of once for each job

    self.call_finalization = True
    self.finalsdict['uploadData'] = uploadData
    self.finalsdict['registerData'] = registerData
    self.finalsdict['uploadLog'] = uploadLog
    self.finalsdict['sendFailover'] = sendFailover

  def _addRealFinalization(self):
    """This is called at creation: now that the workflow is created at the last minute, we need to add this also at the last minute."""
    importLine = 'from ILCDIRAC.Workflow.Modules.<MODULE> import <MODULE>'

    dataUpload = ModuleDefinition('UploadOutputData')
    dataUpload.setDescription('Uploads the output data')
    self._addParameter(dataUpload, 'enable', 'bool', False, 'EnableFlag')
    body = importLine.replace('<MODULE>', 'UploadOutputData')
    dataUpload.setBody(body)

    failoverRequest = ModuleDefinition('FailoverRequest')
    failoverRequest.setDescription('Sends any failover requests')
    self._addParameter(failoverRequest, 'enable', 'bool', False, 'EnableFlag')
    body = importLine.replace('<MODULE>', 'FailoverRequest')
    failoverRequest.setBody(body)

    registerdata = ModuleDefinition('RegisterOutputData')
    registerdata.setDescription('Module to add in the metadata catalog the relevant info about the files')
    self._addParameter(registerdata, 'enable', 'bool', False, 'EnableFlag')
    body = importLine.replace('<MODULE>', 'RegisterOutputData')
    registerdata.setBody(body)

    logUpload = ModuleDefinition('UploadLogFile')
    logUpload.setDescription('Uploads the output log files')
    self._addParameter(logUpload, 'enable', 'bool', False, 'EnableFlag')
    body = importLine.replace('<MODULE>', 'UploadLogFile')
    logUpload.setBody(body)

    errorReport = ModuleDefinition('ReportErrors')
    errorReport.setDescription('Reports errors at the end')
    body = importLine.replace('<MODULE>', 'ReportErrors')
    errorReport.setBody(body)

    finalization = StepDefinition('Job_Finalization')
    finalization.addModule(dataUpload)
    up = finalization.createModuleInstance('UploadOutputData', 'dataUpload')
    up.setValue("enable", self.finalsdict['uploadData'])

    finalization.addModule(registerdata)
    ro = finalization.createModuleInstance('RegisterOutputData', 'RegisterOutputData')
    ro.setValue("enable", self.finalsdict['registerData'])

    finalization.addModule(logUpload)
    ul = finalization.createModuleInstance('UploadLogFile', 'logUpload')
    ul.setValue("enable", self.finalsdict['uploadLog'])

    finalization.addModule(failoverRequest)
    fr = finalization.createModuleInstance('FailoverRequest', 'failoverRequest')
    fr.setValue("enable", self.finalsdict['sendFailover'])

    finalization.addModule(errorReport)
    fr = finalization.createModuleInstance('ReportErrors', 'reportErrors')

    self.workflow.addStep(finalization)
    self.workflow.createStepInstance('Job_Finalization', 'finalization')

    return S_OK()

  def createProduction(self, name=None):
    """Create production.

    :return: S_OK with the created transformation, or S_ERROR
    """
    if not self.dryrun:
      if not self.proxyinfo['OK']:
        return S_ERROR('Not allowed to create production, you need a production proxy.')
      if 'groupProperties' not in self.proxyinfo['Value']:
        return S_ERROR('Could not determine groupProperties, you do not have the right proxy.')
      groupProperties = self.proxyinfo['Value']['groupProperties']
      if 'ProductionManagement' not in groupProperties:
        return S_ERROR('Not allowed to create production, you need a production proxy.')

    if self.created:
      return S_ERROR("Production already created.")

    # We need to add the applications to the workflow
    res = self._addToWorkflow()
    if not res['OK']:
      return res
    if self.call_finalization:
      self._addRealFinalization()

    workflowName = self.workflow.getName()
    fileName = '%s.xml' % workflowName
    LOG.verbose('Workflow XML file name is:', '%s' % fileName)
    try:
      self.createWorkflow()
    except Exception as x:
      LOG.error("Exception creating workflow", repr(x))
      return S_ERROR('Could not create workflow')
    with open(fileName, 'r') as oFile:
      workflowXML = oFile.read()
    if not name:
      name = workflowName

    res = self.trc.getTransformationStats(name)
    if res['OK']:
      return self._reportError("Transformation with name %s already exists! Cannot proceed." % name)

    # Create Tranformation
    Trans = Transformation()
    Trans.setTransformationName(name)
    Trans.setDescription(self.description)
    Trans.setLongDescription(self.description)
    Trans.setType(self.type)
    self.prodparameters['JobType'] = self.type
    Trans.setPlugin(self.plugin)
    if self.inputdataquery:
      Trans.setGroupSize(self.jobFileGroupSize)
    Trans.setTransformationGroup(self.prodGroup)
    Trans.setBody(workflowXML)
    if not self.slicesize:
      Trans.setEventsPerTask(self.jobFileGroupSize * self.nbevts)
    else:
      Trans.setEventsPerTask(self.slicesize)
    self.currtrans = Trans
    if self.inputBKSelection:
      Trans.setInputMetaQuery(self.inputBKSelection)
    if self.dryrun:
      LOG.notice('Would create prod called', name)
      self.transfid = 12345
    else:
      res = Trans.addTransformation()
      if not res['OK']:
        LOG.error(res['Message'])
        return res
      self.transfid = Trans.getTransformationID()['Value']

    if not self.dryrun:
      Trans.setAgentType("Automatic")
      Trans.setStatus("Active")

    finals = []
    for finalpaths in self.finalpaths:
      finalpaths = finalpaths.rstrip("/")
      finalpaths += "/" + str(self.transfid).zfill(8)
      finals.append(finalpaths)
      self.finalMetaDict[finalpaths].update({"ProdID": self.transfid})
      self.finalMetaDict[finalpaths].update(self.prodMetaDict)
      # if 'ILDConfigVersion' in self.prodparameters:
      #   self.finalMetaDict[finalpaths].update({"ILDConfig":self.prodparameters['ILDConfigVersion']})

      if self.nbevts:
        self.finalMetaDict[finalpaths].update({'NumberOfEvents': self.jobFileGroupSize * self.nbevts})
    self.finalpaths = finals
    self.created = True

    return S_OK(Trans)

  def setNbOfTasks(self, nbtasks):
    """Define the number of tasks you want.

    Useful for generation jobs.
    """
    if not self.currtrans:
      LOG.error("Not transformation defined earlier")
      return S_ERROR("No transformation defined")
    if self.inputBKSelection and self.plugin not in ['Limited', 'SlicedLimited']:
      LOG.error('Metadata selection activated, should not specify the number of jobs')
      return S_ERROR()
    self.nbtasks = nbtasks
    self.currtrans.setMaxNumberOfTasks(self.nbtasks)  # pylint: disable=E1101
    return S_OK()

  def addMetadataToFinalFiles(self, metadict):
    """Add additionnal non-query metadata."""
    self.metadict_external = metadict

    return S_OK()

  def finalizeProd(self, prodid=None, prodinfo=None):
    """Finalize definition: submit to Transformation service and register metadata."""
    currtrans = 0
    if self.currtrans:
      if not self.dryrun:
        currtrans = self.currtrans.getTransformationID()['Value']  # pylint: disable=E1101
      else:
        currtrans = 12345
    if prodid:
      currtrans = prodid
    if not currtrans:
      LOG.error("Not transformation defined earlier")
      return S_ERROR("No transformation defined")
    if prodinfo:
      self.prodparameters = prodinfo

    info = []
    info.append('%s Production %s has following parameters:\n' % (self.prodparameters['JobType'], currtrans))

    for key, value in self.prodparameters.items():
      if "datatype" in str(value):
        info.append('- Output %s' % key)

    if "Process" in self.prodparameters:
      info.append('- Process %s' % self.prodparameters['Process'])
    if "Energy" in self.prodparameters:
      info.append('- Energy %s GeV' % self.prodparameters["Energy"])

    if not self.slicesize:
      self.prodparameters['nbevts'] = self.jobFileGroupSize * self.nbevts
    else:
      self.prodparameters['nbevts'] = self.slicesize
    if self.prodparameters['nbevts']:
      info.append("- %s events per job" % (self.prodparameters['nbevts']))
    if self.prodparameters.get('lumi', False):
      info.append('    corresponding to a luminosity %s fb' % (self.prodparameters['lumi']
                                                               * self.prodparameters['NbInputFiles']))
    if 'FCInputQuery' in self.prodparameters:
      info.append('Using InputDataQuery :')
      for key, val in self.prodparameters['FCInputQuery'].items():
        info.append('    %s = %s' % (key, val))
    if "SWPackages" in self.prodparameters:
      info.append('- SW packages %s' % self.prodparameters["SWPackages"])
    if "SoftwareTag" in self.prodparameters:
      info.append('- SW tags %s' % self.prodparameters["SoftwareTag"])
    if "ILDConfigVersion" in self.prodparameters:
      info.append('- ILDConfig %s' % self.prodparameters['ILDConfigVersion'])

    if 'ClicConfigVersion' in self.prodparameters:
      info.append('- ClicConfig %s' % self.prodparameters['ClicConfigVersion'])

    if 'extraCLIArguments' in self.prodparameters:
      info.append('- ExtraCLIArguments %s' % self.prodparameters['extraCLIArguments'])

    # as this is the very last call all applications are registered, so all software packages are known
    # add them the the metadata registration
    for finalpath in self.finalpaths:
      if "SWPackages" in self.prodparameters:
        self.finalMetaDictNonSearch.setdefault(finalpath, {})["SWPackages"] = self.prodparameters["SWPackages"]

      if self.metadict_external:
        self.finalMetaDictNonSearch[finalpath].update(self.metadict_external)

    self.finalMetaDictNonSearch.update(self.specialFinalMetaData)

    info.append('- Registered metadata: ')
    for path, metadata in sorted(self.finalMetaDict.items()):
      info.append('    %s = %s' % (path, metadata))
    info.append('- Registered non searchable metadata: ')
    for path, metadata in sorted(self.finalMetaDictNonSearch.items()):
      info.append('    %s = %s' % (path, metadata))

    infoString = '\n'.join(info)
    self.prodparameters['DetailedInfo'] = infoString

    for name, val in self.prodparameters.items():
      result = self._setProdParameter(currtrans, name, val)
      if not result['OK']:
        LOG.error(result['Message'])

    res = self._registerMetadata()
    if not res['OK']:
      LOG.error('Could not register the following directories:', res['Message'])
      return res
    return S_OK()

  def _createDirectory(self, path, failed, mode=0o775):
    """Create the directory at path if it does not exist.

    :param str path: path to check
    :param list failed: list of failed paths
    :param int mode: mode to set for directory
    """
    exists = returnSingleResult(self.fc.isDirectory(path))
    if exists['OK'] and exists['Value']:
      LOG.verbose('Directory already exists:', path)
      return S_OK()
    result = returnSingleResult(self.fc.createDirectory(path))
    if not result['OK']:
      LOG.error('Failed to create directory:', '%s: %s' % (path, result['Message']))
      failed[path].append(result['Message'])
      return S_ERROR()
    LOG.verbose('Successfully created directory:', path)
    res = self.fc.changePathMode({path: mode}, False)
    if not res['OK']:
      LOG.error(res['Message'])
      failed[path].append(res['Message'])
      return S_ERROR()
    LOG.verbose('Successfully changed mode:', path)
    return S_OK()

  def _checkMetadata(self, path, metaCopy):
    """Get existing metadata, if it is the same do not set it again, otherwise return error."""
    existingMetadata = self.fc.getDirectoryUserMetadata(path.rstrip('/'))
    if not existingMetadata['OK']:
      return S_OK()
    failure = False
    for key, value in existingMetadata['Value'].items():
      if key in metaCopy and metaCopy[key] != value:
        LOG.error('Metadata values for folder %s disagree for key %s: Existing(%r), new(%r)' %
                  (path, key, value, metaCopy[key]))
        failure = True
      elif key in metaCopy and metaCopy[key] == value:
        LOG.verbose('Meta entry is unchanged', '%s = %s' % (key, value))
        metaCopy.pop(key, None)
    if failure:
      return S_ERROR('Error when setting new metadata, already existing metadata disagrees!')
    return S_OK()

  def _registerMetadata(self):
    """Set metadata for given folders.

    Register path and metadata before the production actually runs. This allows for the definition
    of the full chain in 1 go.
    """
    prevent_registration = self.ops.getValue('Production/PreventMetadataRegistration', False)

    if self.dryrun or prevent_registration:
      LOG.notice('Would have created and registered the following\n',
                 '\n '.join([' * %s: %s' % (fPath, val) for fPath, val in sorted(self.finalMetaDict.items())]))
      LOG.notice('Would have set this as non searchable metadata', str(self.finalMetaDictNonSearch))
      return S_OK()

    failed = defaultdict(list)
    for path, meta in sorted(self.finalMetaDict.items()):
      res = self._createDirectory(path, failed)
      if not res['OK']:
        continue
      LOG.verbose('Checking to set metadata:', meta)
      metaCopy = dict(meta)
      res = self._checkMetadata(path, metaCopy)
      if not res['OK']:
        return res
      if not metaCopy:
        LOG.verbose('No new metadata to set')
        continue

      LOG.notice('Setting metadata information: ', '%s: %s' % (path, metaCopy))
      result = self.fc.setMetadata(path.rstrip('/'), metaCopy)
      if not result['OK']:
        LOG.error('Could not preset metadata', str(metaCopy))
        LOG.error('Could not preset metadata', result['Message'])
        failed[path].append(result['Message'])

    for path, meta in sorted(self.finalMetaDictNonSearch.items()):
      res = self._createDirectory(path, failed)
      if not res['OK']:
        continue
      LOG.notice('Setting non searchable metadata information: ', '%s: %s' % (path, meta))
      result = self.fc.setMetadata(path.rstrip('/'), meta)
      if not result['OK']:
        LOG.error('Could not preset non searchable metadata', str(meta))
        LOG.error('Could not preset non searchable metadata', result['Message'])
        failed[path].append(result['Message'])

    if failed:
      return S_ERROR('Failed to register some metadata: %s' % dict(failed))
    return S_OK()

  def getMetadata(self):
    """Return the corresponding metadata of the last step."""
    metadict = {}
    for meta in self.finalMetaDict.values():
      metadict.update(meta)
    if 'NumberOfEvents' in metadict:
      del metadict['NumberOfEvents']  # As this is not supposed to be a searchable thing
    return metadict

  def _setProdParameter(self, prodID, pname, pvalue):
    """Set a production parameter."""
    if isinstance(pvalue, list):
      pvalue = '\n'.join(pvalue)

    if isinstance(pvalue, six.integer_types):
      pvalue = str(pvalue)
    if not self.dryrun:
      result = self.trc.setTransformationParameter(int(prodID), str(pname), str(pvalue))
      if not result['OK']:
        LOG.error('Problem setting parameter %s for production %s and value:\n%s' % (prodID, pname, pvalue))
    else:
      LOG.notice('Adding %s=%s to transformation' % (str(pname), str(pvalue)))
      result = S_OK()
    return result

  def _jobSpecificParams(self, application):
    """For production additional checks are needed: ask the user."""

    if self.created:
      return S_ERROR("The production was created, you cannot add new applications to the job.")

    if not application.logFile:
      logf = application.appname + "_" + application.version + "_@{STEP_ID}.log"
      res = application.setLogFile(logf)
      if not res['OK']:
        return res

      # in fact a bit more tricky as the log files have the prodID and jobID in them

    # Retrieve from the application the essential info to build the prod info.
    if not self.nbevts and not self.slicesize:
      self.nbevts = application.numberOfEvents
      if not self.nbevts:
        return S_ERROR("Number of events to process is not defined.")
    elif not application.numberOfEvents:
      if not self.slicesize:
        res = application.setNumberOfEvents(self.jobFileGroupSize * self.nbevts)
      else:
        res = application.setNumberOfEvents(self.slicesize)
      if not res['OK']:
        return res

    if application.numberOfEvents > 0 and (
        self.jobFileGroupSize
        * self.nbevts > application.numberOfEvents or self.slicesize > application.numberOfEvents):
      self.nbevts = application.numberOfEvents

    if not self.energy:
      if application.energy:
        self.energy = Decimal((("%1.3f" % float(application.energy)).rstrip('0').rstrip('.')))
      else:
        return S_ERROR("Could not find the energy defined, it is needed for the production definition.")
    elif not application.energy:
      res = application.setEnergy(float(self.energy))
      if not res['OK']:
        return res
    if self.energy:
      self._setParameter("Energy", "float", float(self.energy), "Energy used")
      self.prodparameters["Energy"] = float(self.energy)

    if not self.evttype:
      if hasattr(application, 'eventType'):
        self.evttype = application.eventType
      else:
        return S_ERROR("Event type not found nor specified, it's mandatory for the production paths.")
      self.prodparameters['Process'] = self.evttype

    if not self.outputStorage:
      return S_ERROR("You need to specify the Output storage element")

    curpackage = "%s.%s" % (application.appname, application.version)
    if "SWPackages" in self.prodparameters:
      if curpackage not in self.prodparameters["SWPackages"]:
        self.prodparameters["SWPackages"] += ";%s" % (curpackage)
    else:
      self.prodparameters["SWPackages"] = "%s" % (curpackage)

    if not application.accountInProduction:
      res = self._updateProdParameters(application)
      if not res['OK']:
        return res
      self.checked = True

      return S_OK()

    res = application.setOutputSE(self.outputStorage)
    if not res['OK']:
      return res

    energypath = self.getEnergyPath()

    if not self.basename:
      self.basename = self.evttype

    evttypepath = ''
    if not self.evttype[-1] == '/':
      evttypepath = self.evttype + '/'

    path = self.basepath

    # Need to resolve file names and paths
    if self.energy:
      self.finalMetaDict[self.basepath + energypath] = {"Energy": str(self.energy)}

    currentPathList = [self.basepath, energypath, evttypepath]
    path = os.path.join(*currentPathList)
    self.finalMetaDict[path] = {"EvtType": self.evttype}
    if self.generator:
      self.prodparameters['Generator'] = self.generator
      if self.vo != 'fcc': # for fcc we no longer include the generator inside the file path
        currentPathList.append(self.generator)
        generatorPath = os.path.join(*currentPathList)
        self.finalMetaDict[generatorPath] = {'Generator': self.generator}

    if self.vo == 'fcc':
      self.finalMetaDict[self.basepath] = {"Campaign": str(self.campaign)}
      self.configureFCCOutputPath(path, application, currentPathList)

    if self.vo == 'ilc':
      self.configureILCOutputPath(path, application, currentPathList)

    res = self._updateProdParameters(application)
    if not res['OK']:
      return res

    self.checked = True

    return S_OK()
  
  def configureFCCOutputPath(self, path, application, currentPathList):
    # comment of Lorenzo Valentini, 12-05-2023
    # In fcc we have a particular use of Gaudi. Its application is defined with the functions setOutputSimFile/setOutputRecFile.
    # However, it is sometimes used for other tasks, for which we don't want it to use the file path of the sim/rec transformations.
    # Up to now, seems like whenever we will be using sim/rec transformations we won't have to define the datatype, which we use to discriminate the two cases.

    # this is the case of a (maybe Gaudi) application used for sim/rec transformations: no datatype defined, and we check the presence of setOutputSimFile
    if hasattr(application, "setOutputSimFile") and not application.willBeCut and not application.datatype:
      detPath = os.path.join(path, application.detector)
      self.finalMetaDict[detPath] = {"DetectorType": application.detector}
      if application.keepRecFile:
        path = os.path.join(detPath, 'rec')
        self.finalMetaDict[path] = {'Datatype': 'rec'}
        fname = self.basename + '_rec.slcio'
        application.setOutputRecFile(fname, path)
        LOG.notice('Will store the files under', path)
        self.finalpaths.append(path)
      path = os.path.join(detPath, 'sim')
      self.finalMetaDict[path] = {'Datatype': 'sim'}
      fname = self.basename + '_dst.slcio'
      application.setOutputSimFile(fname, path)
      LOG.notice('Will store the files under', path)
      self.finalpaths.append(path)

    # # comment of Lorenzo Valentini, 12-05-2023
    # # this is the case of a (maybe Gaudi) application used for dst/rec transformations: no datatype defined, and we check the presence of setOutputRecFile. It would make more sense to just check for setOutputDstFile,
    # # but we wanted to keep it backward compatibile with the ilc simulations.
    # # In the case of fcc, we check for the absence of datatype.
    # elif hasattr(application, "setOutputRecFile") and not application.willBeCut and not application.datatype:
    #   detPath = os.path.join(path, application.detectortype)
    #   self.finalMetaDict[detPath] = {'DetectorType': application.detectortype}
    #   if application.keepRecFile:
    #     path = os.path.join(detPath, 'rec')
    #     self.finalMetaDict[path] = {'Datatype': 'rec'}
    #     fname = self.basename + '_rec.slcio'
    #     application.setOutputRecFile(fname, path)
    #     LOG.notice('Will store the files under', path)
    #     self.finalpaths.append(path)
    #   path = os.path.join(detPath, 'dst')
    #   self.finalMetaDict[path] = {'Datatype': 'dst'}
    #   fname = self.basename + '_dst.slcio'
    #   application.setOutputDstFile(fname, path)
    #   LOG.notice('Will store the files under', path)
    #   self.finalpaths.append(path)

    elif hasattr(application, "outputFile") and hasattr(application, 'datatype') and not application.outputFile and not application.willBeCut:
      LOG.notice('Adding output meta data for %s' % type(application))
      path = os.path.join(*currentPathList)

      if not application.datatype and self.datatype:
        application.datatype = self.datatype

      # here we are adding detector and detectortype to the path (either one or the other) if they are defined. For fcc, we usually set the detector using the attribute application.detector.
      if hasattr(application, "detectortype"):
        if application.detectortype:
          path = os.path.join(path, application.detectortype)
          self.finalMetaDict[path] = {"DetectorType": application.detectortype}
      if hasattr(application, "detector"):
        if application.detector and not application.detectortype:
          path = os.path.join(path, application.detector)
          self.finalMetaDict[path] = {"DetectorType": application.detector}
      if hasattr(application, "detectortype") or hasattr(application, "detector"):
        if self.detector and not application.detectortype and not application.detector:
          path = os.path.join(path, self.detector)
          self.finalMetaDict[path] = {"DetectorType": self.detector}

      path = os.path.join(path, application.datatype)
      self.finalMetaDict[path] = {'Datatype': application.datatype}

      LOG.notice('Will store the files under', '%s' % path)
      self.finalpaths.append(path)
      extension = getattr(application, '_extension', 'stdhep')

      fname = self.basename + "_%s" % (application.datatype.lower()) + "." + extension
      application.setOutputFile(fname, path)

    return

  def configureILCOutputPath(self, path, application, currentPathList):
    if hasattr(application, "setOutputRecFile") and not application.willBeCut:
      detPath = os.path.join(path, application.detectortype)
      self.finalMetaDict[detPath] = {'DetectorType': application.detectortype}
      if application.keepRecFile:
        path = os.path.join(detPath, 'REC')
        self.finalMetaDict[path] = {'Datatype': 'REC'}
        fname = self.basename + '_rec.slcio'
        application.setOutputRecFile(fname, path)
        LOG.notice('Will store the files under', path)
        self.finalpaths.append(path)
      path = os.path.join(detPath, 'DST')
      self.finalMetaDict[path] = {'Datatype': 'DST'}
      fname = self.basename + '_dst.slcio'
      application.setOutputDstFile(fname, path)
      LOG.notice('Will store the files under', path)
      self.finalpaths.append(path)

    elif hasattr(application, "outputFile") and hasattr(application, 'datatype') and not application.outputFile and not application.willBeCut:
      LOG.notice('Adding output meta data for %s' % type(application))
      path = os.path.join(*currentPathList)

      if not application.datatype and self.datatype:
        application.datatype = self.datatype

      if hasattr(application, "detectortype"):
        if application.detectortype:
          path = os.path.join(path, application.detectortype)
          self.finalMetaDict[path] = {"DetectorType": application.detectortype}
        elif self.detector:
          path = os.path.join(path, self.detector)
          self.finalMetaDict[path] = {"DetectorType": self.detector}
      if hasattr(application, "detector"):
        if application.detector:
          path = os.path.join(path, application.detector)
          self.finalMetaDict[path] = {"DetectorType": application.detector}
      path = os.path.join(path, application.datatype)
      self.finalMetaDict[path] = {'Datatype': application.datatype}

      LOG.notice('Will store the files under', '%s' % path)
      self.finalpaths.append(path)
      extension = getattr(application, '_extension', 'stdhep')
      if application.datatype in ['SIM', 'REC']:
        extension = 'slcio'
      fname = self.basename + "_%s" % (application.datatype.lower()) + "." + extension
      application.setOutputFile(fname, path)

    return

  def _updateProdParameters(self, application):
    """Update the prod parameters stored in the production parameters visible from the web."""
    try:
      self.prodparameters.update(application.prodparameters)
    except Exception as x:
      return S_ERROR("Exception: %r" % x)

    if hasattr(application, 'extraCLIArguments') and application.extraCLIArguments:
      self.prodparameters['extraCLIArguments'] = repr(application.extraCLIArguments)

    return S_OK()

  def _jobSpecificModules(self, application, step):
    return application._prodjobmodules(step)

  def getEnergyPath(self):
    """returns the energy path 250gev or 3tev or 1.4tev etc."""
    energy = Decimal(str(self.energy))
    tD = Decimal('1000.0')
    unit = 'gev' if energy < tD else 'tev'
    energy = energy if energy < tD else energy / tD
    energyPath = ("%1.3f" % energy).rstrip('0').rstrip('.')
    energyPath = energyPath + unit + '/'

    LOG.notice('Energy path is: ', energyPath)
    return energyPath

  def _checkMetaKeys(self, metakeys, extendFileMeta=False):
    """check if metadata keys are allowed to be metadata.

    :param list metakeys: metadata keys for production metadata
    :param bool extendFileMeta: also use FileMetaFields for checking meta keys
    :returns: S_OK, S_ERROR
    """

    res = self.fc.getMetadataFields()
    if not res['OK']:
      LOG.error("Could not contact File Catalog")
      return S_ERROR("Could not contact File Catalog")
    metaFCkeys = list(res['Value']['DirectoryMetaFields'].keys())
    if extendFileMeta:
      metaFCkeys.extend(list(res['Value']['FileMetaFields'].keys()))

    for key in metakeys:
      for meta in metaFCkeys:
        if meta != key and meta.lower() == key.lower():
          return self._reportError("Key syntax error %r, should be %r" % (key, meta), name=self.__class__.__name__)
      if key not in metaFCkeys:
        return self._reportError("Key %r not found in metadata keys, allowed are %r" % (key, metaFCkeys))

    return S_OK()

  def _checkFindDirectories(self, metadata):
    """find directories by metadata and check that there are directories found.

    :param dict metadata: metadata dictionary
    :returns: S_OK, S_ERROR
    """

    metaQuery = ' '.join('%s=%s' % (k, v) for k, v in metadata.items())
    LOG.verbose('Looking for folder with', repr(metaQuery))
    res = self.fc.findDirectoriesByMetadata(metadata)
    if not res['OK']:
      return self._reportError("Error looking up the catalog for available directories")
    elif len(res['Value']) < 1:
      return self._reportError('Could not find any directories corresponding to the query issued: %s' % metaQuery)
    for folderId, folder in res['Value'].items():
      if (folderId == 0 or folder == 'None') and not self.dryrun:
        return self._reportError('Could not find any directories corresponding to the query issued: %s' % metaQuery)
    return res

  def setReconstructionBasePaths(self, recPath, dstPath):
    """set the output Base paths for the reconstruction REC and DST files."""
    self._recBasePaths['REC'] = recPath
    self._recBasePaths['DST'] = dstPath
