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
"""
Marlin: Reconstructor after Mokka
"""
from __future__ import absolute_import
import os

from ILCDIRAC.Interfaces.API.NewInterface.LCApplication import LCApplication
from ILCDIRAC.Core.Utilities.CheckXMLValidity import checkXMLValidity
from ILCDIRAC.Interfaces.Utilities.DDInterfaceMixin import DDInterfaceMixin

from DIRAC import S_OK, S_ERROR, gLogger
from DIRAC.Core.Workflow.Parameter import Parameter
from DIRAC.ConfigurationSystem.Client.Helpers.Operations import Operations
import six

LOG = gLogger.getSubLogger(__name__)
__RCSID__ = "$Id$"


class Marlin(DDInterfaceMixin, LCApplication):
  """Call Marlin reconstructor (after Mokka simulator)

  Usage:

  >>> marlin = Marlin()
  >>> marlin.getInputFromApp(mo)
  >>> marlin.setSteeringfile('SteeringFile.xml')
  >>> marlin.setOutputRecFile('MyOutputRecFile.rec')
  >>> marlin.setOutputDstFile('MyOutputDstFile.dst')

  Use :func:`setExtraCLIArguments` if you want to add command line parameters
  needed for easy parameter scans and passing non-standard strings (like cuts)

  >>> marlin = Marlin()
  >>> ...
  >>> marlin.setExtraCLIArguments( "--myProcessor.myParameter=someValue" )
  >>> ...

  The output file for marlin is changed automatically if the xml
  steering file contains a processor called *MyLCIOOutputProcessor*

  >>> marlin = Marlin()
  >>> ...
  >>> marlin.setOutputFile( "output_job123.slcio" )
  >>> ...

  .. versionchanged:: v26r0p4

    The default value for the GearFile was removed. It used to be
    "GearOutput.xml" but as reconstruction based on DD4hep is not using gear
    files a default value is more dangerous than before.

  .. versionchanged:: v29r0p4

    New member flag ``keepRecFile``, defaults to ``True``, if set to
    ``False``, the REC file is not uploaded from ProductionJobs
  """

  def __init__(self, paramdict=None):

    self.outputDstPath = ''
    self.outputDstFile = ''
    self.outputRecPath = ''
    self.outputRecFile = ''
    self.keepRecFile = True
    self.gearFile = ''
    self.processorsToUse = []
    self.processorsToExclude = []
    super(Marlin, self).__init__(paramdict)
    # Those 5 need to come after default constructor
    self._modulename = 'MarlinAnalysis'
    self._moduledescription = 'Module to run MARLIN'
    self.appname = 'marlin'
    self.datatype = 'REC'
    self.detectortype = 'ILD'
    self.detectorModel = ''
    self._ops = Operations()

  def setGearFile(self, gearFile):
    """Define input gear file for Marlin.

    :param str gearFile: input gear file for Marlin reconstructor
    """
    self._checkArgs({'gearFile': (str,)})

    self.gearFile = gearFile
    if os.path.exists(gearFile) or gearFile.lower().count("lfn:"):
      self.inputSB.append(gearFile)

  def setKeepRecFile(self, val):
    """Set the ``keepRecFile`` flag.

    Only relevant for ProductionJobs

    :param bool val: If ``False`` REC file is not stored
    """
    self._checkArgs({'val': bool})
    self.keepRecFile = val

  def setOutputRecFile(self, outputRecFile, path=None):
    """Optional: Define output rec file for Marlin. Used only in production
    context. Use :func:`UserJob.setOutputData
    <ILCDIRAC.Interfaces.API.NewInterface.UserJob.UserJob.setOutputData>` if you
    want to keep the file on the grid.

    :param str outputRecFile: output rec file for Marlin
    :param str path: Path where to store the file.

    """
    self._checkArgs({'outputRecFile': (str,)})
    self.outputRecFile = outputRecFile
    self.prodparameters[self.outputRecFile] = {}
    self.prodparameters[self.outputRecFile]['datatype'] = 'REC'
    if path:
      self.outputRecPath = path

  def setOutputDstFile(self, outputDstFile, path=None):
    """Optional: Define output dst file for Marlin.  Used only in production
    context. Use :func:`UserJob.setOutputData
    <ILCDIRAC.Interfaces.API.NewInterface.UserJob.UserJob.setOutputData>` if you
    want to keep the file on the grid.

    :param str outputDstFile: output dst file for Marlin
    :param str path: Path where to store the file.

    """
    self._checkArgs({'outputDstFile': (str,)})
    self.outputDstFile = outputDstFile
    self.prodparameters[self.outputDstFile] = {}
    self.prodparameters[self.outputDstFile]['datatype'] = 'DST'
    if path:
      self.outputDstPath = path

  def setProcessorsToUse(self, processorlist):
    """Define processor list to use.

    Overwrite the default list (full reco). Useful for users willing to do dedicated analysis (TPC, Vertex digi, etc.)

    >>> ma.setProcessorsToUse(['libMarlinTPC.so','libMarlinReco.so','libOverlay.so','libMarlinTrkProcessors.so'])

    :param processorlist: list of processors to use
    :type processorlist: list
    """
    self._checkArgs({'processorlist': list})
    self.processorsToUse = processorlist

  def setProcessorsToExclude(self, processorlist):
    """Define processor list to exclude.

    Overwrite the default list (full reco). Useful for users willing to do dedicated analysis (TPC, Vertex digi, etc.)

    >>> ma.setProcessorsToExclude(['libLCFIVertex.so'])

    :param processorlist: list of processors to exclude
    :type processorlist: list
    """
    self._checkArgs({'processorlist': list})
    self.processorsToExclude = processorlist

  def _userjobmodules(self, stepdefinition):
    res1 = self._setApplicationModuleAndParameters(stepdefinition)
    res2 = self._setUserJobFinalization(stepdefinition)
    if not res1["OK"] or not res2["OK"]:
      return S_ERROR('userjobmodules failed')
    return S_OK()

  def _prodjobmodules(self, stepdefinition):

    # Here one needs to take care of listoutput
    if self.outputPath:
      self._listofoutput.append({'OutputFile': '@{OutputFile}', "outputPath": "@{OutputPath}",
                                 "outputDataSE": '@{OutputSE}'})

    res1 = self._setApplicationModuleAndParameters(stepdefinition)
    res2 = self._setOutputComputeDataList(stepdefinition)
    if not res1["OK"] or not res2["OK"]:
      return S_ERROR('prodjobmodules failed')
    return S_OK()

  def _checkConsistency(self, job=None):

    if not self.version:
      return S_ERROR('Version not set!')

    if self.steeringFile:
      # FIXME: delete dead code
      # if not os.path.exists(self.steeringFile) and not self.steeringFile.lower().count("lfn:"):
        ##res = Exists(self.SteeringFile)
        #res = S_OK()
        # if not res['OK']:
        # return res
      if os.path.exists(self.steeringFile):
        res = checkXMLValidity(self.steeringFile)
        if not res['OK']:
          return S_ERROR("Supplied steering file cannot be read with xml parser: %s" % (res['Message']))

    if not self.gearFile:
      LOG.info('GEAR file not given, will not use any gear file')
    # FIXME: delete dead code
    # if self.gearFile:
      # if not os.path.exists(self.gearFile) and not self.gearFile.lower().count("lfn:"):
      ##res = Exists(self.gearFile)
      #res = S_OK()
      # if not res['OK']:
      # return res

    if self._jobtype != 'User':
      if not self.outputFile:
        self._listofoutput.append({'outputFile': '@{outputDST}', 'outputPath': '@{outputPathDST}',
                                   'outputDataSE': '@{OutputSE}'})
        if self.keepRecFile:
          self._listofoutput.append({'outputFile': '@{outputREC}', 'outputPath': '@{outputPathREC}',
                                     'outputDataSE': '@{OutputSE}'})
      self.prodparameters['detectorType'] = self.detectortype
      self.prodparameters['marlin_gearfile'] = self.gearFile
      self.prodparameters['marlin_steeringfile'] = self.steeringFile

    return S_OK()

  def _applicationModule(self):

    md1 = self._createModuleDefinition()
    md1.addParameter(Parameter("inputGEAR", '', "string", "", "", False, False,
                               "Input GEAR file"))
    md1.addParameter(Parameter("detectorModel", '', "string", "", "", False, False,
                               "DD4hep Geomtry File"))
    md1.addParameter(Parameter("ProcessorListToUse", [], "list", "", "", False, False,
                               "List of processors to use"))
    md1.addParameter(Parameter("ProcessorListToExclude", [], "list", "", "", False, False,
                               "List of processors to exclude"))
    md1.addParameter(Parameter("debug", False, "bool", "", "", False, False,
                               "debug mode"))
    return md1

  def _applicationModuleValues(self, moduleinstance):

    moduleinstance.setValue("inputGEAR", self.gearFile)
    moduleinstance.setValue("detectorModel", self.detectorModel)
    moduleinstance.setValue('ProcessorListToUse', self.processorsToUse)
    moduleinstance.setValue('ProcessorListToExclude', self.processorsToExclude)
    moduleinstance.setValue("debug", self.debug)

  def _checkWorkflowConsistency(self):
    return self._checkRequiredApp()

  def _resolveLinkedStepParameters(self, stepinstance):
    if isinstance(self._linkedidx, six.integer_types):
      self._inputappstep = self._jobsteps[self._linkedidx]
    if self._inputappstep:
      stepinstance.setLink("InputFile", self._inputappstep.getType(), "OutputFile")
    return S_OK()
