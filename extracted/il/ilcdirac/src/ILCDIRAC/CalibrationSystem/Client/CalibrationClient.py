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
"""The calibration client offers the interface for user and calibration worker nodes to talk to the calibration service.

The user use this interface to monitor and control calibrations.
The worker nodes use this interface to ask for new parameters, their event slices and inform the service
about the results of their reconstruction.
"""

from __future__ import absolute_import
from DIRAC.Core.Base.Client import Client
from DIRAC import S_OK, S_ERROR, gLogger
from DIRAC.ConfigurationSystem.Client.Helpers.Operations import Operations
from ILCDIRAC.CalibrationSystem.Utilities.fileutils import binaryFileToString
from ILCDIRAC.CalibrationSystem.Service.CalibrationRun import CalibrationPhase

__RCSID__ = "$Id$"
LOG = gLogger.getSubLogger(__name__)


class CalibrationClient(Client):
  """Provide an interface for user and worker nodes to talk to Calibration service.

  Contains interfaces to fetch the necessary data from the service to worker node and to report the results back.
  """

  def __init__(self, calibrationID=None, workerID=None, **kwargs):
    """Initialize the client.

    :param int workerID: ID of this worker
    :param int calibrationID: ID of the calibration run this worker belongs to
    :returns: None
    """
    super(CalibrationClient, self).__init__(**kwargs)
    self.setServer('Calibration/Calibration')
    self.calibrationID = calibrationID
    self.workerID = workerID
    self.currentStep = -1  # initial parameter request
    self.currentPhase = CalibrationPhase.ECalDigi
    self.currentStage = 1
    self.parameterSet = None
    self.log = LOG
    self.ops = Operations()
    self.maximumReportTries = self.ops.getValue('Calibration/MaximumReportTries', 10)  # TODO add this to CS

  def getInputDataDict(self, calibrationID=None, workerID=None):
    """Get input data dict. If no arguments are passed use ids which belong to the current class instance.

    :param int calibrationID: ID of the calibration
    :param int workerID: ID of this worker
    :returns: S_OK or S_ERROR
    """
    if calibrationID is None and self.calibrationID is None:
      return S_ERROR("Specify calibrationID")
    if workerID is None and self.workerID is None:
      return S_ERROR("Specify workerID")

    calibIDToUse = calibrationID if calibrationID is not None else self.calibrationID
    workerIDToUse = workerID if workerID is not None else self.workerID

    return self._getRPC().getInputDataDict(calibIDToUse, workerIDToUse)

  def requestNewParameters(self):
    """Fetch new parameter set from the service and updates the step counter in this object with the new value.

    Throws a ValueError if the calibration ended already.
    :returns: dict with 4 keys: calibrationIsFinished (bool), parameters (dict), currentPhase (int), currentStage (int)
    or None if no new parameters are available yet
    :rtype: list
    """
    res = self.getNewParameters(self.calibrationID, self.currentStep)
    if res['OK']:
      returnValue = res['Value']
      # FIXME calibrationRun state will be updated number of worker times while only one time is enough
      if returnValue is not None:
        self.currentPhase = returnValue['currentPhase']
        self.currentStage = returnValue['currentStage']
        self.currentStep = returnValue['currentStep']
    return res

  def requestNewPhotonLikelihood(self):
    """Get new photon likelihood file."""
    res = self.getNewPhotonLikelihood(self.calibrationID)
    if res['OK']:
      return res['Value']
    else:
      return None

  def reportResult(self, outFileName):
    """Send result of calibration step at the node (.root or .xml file) to the service.

    Send the root file from PfoAnalysis or PandoraLikelihoodDataPhotonTraining.xml from photon training
    back to the service procedure

    :param outFileName: Output file from one calibration iteration
    :returns: None
    """
    attempt = 0
    resultString = binaryFileToString(outFileName)

    while attempt < self.maximumReportTries:
      res = self.submitResult(self.calibrationID, self.currentStage, self.currentPhase,
                                                 self.currentStep, self.workerID, resultString)
      if res['OK']:
        return S_OK()
      self.log.warn("Failed to submit result, try", "%s: %s " % (attempt, res['Message']))
      attempt += 1

    return S_ERROR('Could not report result back to CalibrationService.')

  def createCalibration(self, inputFiles, numberOfEventsPerFile, calibSettingsDict):
    """Create calibration run (series of calibration iterations).

    :param dict inputFiles: Input files for the calibration. Dictionary.
                            Mandatory keys: 'zuds', 'kaon', 'muon', 'gamma'.
    :param dict numberOfEventsPerFile: Number of events per type of input file. Dictionary.
                                       Mandatory keys: 'zuds', 'kaon', 'muon', 'gamma'.
    :param dict calibSettingsDict: Calibration configuration settings reqired to start calibration. Dictionary.
    :returns: S_OK containing ID of the calibration, used to retrieve results etc
    :rtype: dict
    """
    res = self._getRPC().createCalibration(inputFiles, numberOfEventsPerFile, calibSettingsDict)
    if not res['OK']:
      LOG.error('Error while executing createCalibration! Error message: ', res['Message'])
    return res
