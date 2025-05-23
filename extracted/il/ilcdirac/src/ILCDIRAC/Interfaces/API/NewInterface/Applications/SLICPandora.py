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
SLICPandora : Run Pandora in the SID context
"""

from __future__ import absolute_import
import os

from DIRAC import S_OK, S_ERROR, gLogger
from DIRAC.Core.Workflow.Parameter import Parameter

from ILCDIRAC.Interfaces.API.NewInterface.LCApplication import LCApplication
from ILCDIRAC.Core.Utilities.InstalledFiles import Exists
import six

LOG = gLogger.getSubLogger(__name__)
__RCSID__ = "$Id$"


class SLICPandora(LCApplication):
  """Call SLICPandora.

  Usage:

  >>> lcsim = LCSIM()
  ...
  >>> slicpandora = SLICPandora()
  >>> slicpandora.getInputFromApp(lcsim)
  >>> slicpandora.setPandoraSettings("~/GreatPathToHeaven/MyPandoraSettings.xml")
  >>> slicpandora.setStartFrom(10)

  Use :func:`setExtraCLIArguments` if you want to add arguments to the PandoraFrontend call
  """

  def __init__(self, paramdict=None):

    self.startFrom = 0
    self.pandoraSettings = ''
    self.detectorModel = ''
    super(SLICPandora, self).__init__(paramdict)
    # Those 5 need to come after default constructor
    self._modulename = 'SLICPandoraAnalysis'
    self._moduledescription = 'Module to run SLICPANDORA'
    self.appname = 'slicpandora'
    self.datatype = 'REC'
    self.detectortype = 'SID'
    self._paramsToExclude.extend(["outputDstPath", "outputRecPath", "OutputDstFile", "OutputRecFile"])

  def setDetectorModel(self, detectorModel):
    """Define detector to use for SlicPandora simulation.

    :param str detectorModel: Detector Model to use for SlicPandora simulation.
    """
    self._checkArgs({'detectorModel': (str,)})

    self.detectorModel = detectorModel
    if os.path.exists(detectorModel) or detectorModel.lower().count("lfn:"):
      self.inputSB.append(detectorModel)

  def setStartFrom(self, startfrom):
    """ Optional: Define from where slicpandora start to read in the input file

    :param int startfrom: from how slicpandora start to read the input file
    """
    self._checkArgs({'startfrom': int})
    self.startFrom = startfrom

  def setPandoraSettings(self, pandoraSettings):
    """ Optional: Define the path where pandora settings are

    :param str pandoraSettings: path where pandora settings are
    """
    self._checkArgs({'pandoraSettings': (str,)})
    self.pandoraSettings = pandoraSettings
    if os.path.exists(pandoraSettings) or pandoraSettings.lower().count("lfn:"):
      self.inputSB.append(pandoraSettings)

  def _userjobmodules(self, stepdefinition):
    res1 = self._setApplicationModuleAndParameters(stepdefinition)
    res2 = self._setUserJobFinalization(stepdefinition)
    if not res1["OK"] or not res2["OK"]:
      return S_ERROR('userjobmodules failed')
    return S_OK()

  def _prodjobmodules(self, stepdefinition):
    res1 = self._setApplicationModuleAndParameters(stepdefinition)
    res2 = self._setOutputComputeDataList(stepdefinition)
    if not res1["OK"] or not res2["OK"]:
      return S_ERROR('prodjobmodules failed')
    return S_OK()

  def _checkConsistency(self, job=None):

    if not self.version:
      return S_ERROR('No version found')

    if self.steeringFile:
      if not os.path.exists(self.steeringFile) and not self.steeringFile.lower().count("lfn:"):
        res = Exists(self.steeringFile)
        if not res['OK']:
          return res

    if not self.pandoraSettings:
      return S_ERROR("PandoraSettings not set, you need it")

    #res = self._checkRequiredApp()
    # if not res['OK']:
    #  return res

    if not self.startFrom:
      LOG.info('No startFrom defined for SlicPandora : start from the begining')

    if self._jobtype != 'User':
      self.prodparameters['slicpandora_steeringfile'] = self.steeringFile
      self.prodparameters['slicpandora_detectorModel'] = self.detectorModel

    return S_OK()

  def _applicationModule(self):

    md1 = self._createModuleDefinition()
    md1.addParameter(Parameter("pandorasettings", "", "string", "", "", False, False,
                               "Pandora Settings"))
    md1.addParameter(Parameter("detectorxml", "", "string", "", "", False, False,
                               "Detector model for simulation"))
    md1.addParameter(Parameter("startFrom", 0, "int", "", "", False, False,
                               "From how SlicPandora start to read the input file"))
    md1.addParameter(Parameter("debug", False, "bool", "", "", False, False,
                               "debug mode"))
    return md1

  def _applicationModuleValues(self, moduleinstance):

    moduleinstance.setValue("pandorasettings", self.pandoraSettings)
    moduleinstance.setValue("detectorxml", self.detectorModel)
    moduleinstance.setValue("startFrom", self.startFrom)
    moduleinstance.setValue("debug", self.debug)

  def _checkWorkflowConsistency(self):
    return self._checkRequiredApp()

  def _resolveLinkedStepParameters(self, stepinstance):
    if isinstance(self._linkedidx, six.integer_types):
      self._inputappstep = self._jobsteps[self._linkedidx]
    if self._inputappstep:
      stepinstance.setLink("InputFile", self._inputappstep.getType(), "OutputFile")
    return S_OK()
