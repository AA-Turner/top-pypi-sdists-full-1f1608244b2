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
Whizard2: Interface to the Whizard 2 generator

.. versionadded:: v26r0p14

Usage:

>>> whiz = Whizard2()
>>> whiz.setVersion("2.3.1")
>>> whiz.setNumberOfEvents(30)
>>> whiz.setRandomSeed(15)
>>> whiz.setSinFile("__path_to__/process.sin")

"""

from __future__ import absolute_import
import os
import re

from ILCDIRAC.Interfaces.API.NewInterface.LCApplication import LCApplication
from DIRAC import S_OK, S_ERROR, gLogger
from DIRAC.Core.Workflow.Parameter import Parameter
from DIRAC.ConfigurationSystem.Client.Helpers.Operations import Operations
import six


LOG = gLogger.getSubLogger(__name__)

__RCSID__ = "$Id$"


class Whizard2(LCApplication):
  """Whizard2 Application Class."""

  def __init__(self, paramdict=None):
    self.randomSeed = -1
    self.eventType = ''
    self.whizard2SinFile = ''
    self.whizard2RawSin = False
    super(Whizard2, self).__init__(paramdict)
    # Those 5 need to come after default constructor
    self._modulename = 'Whizard2Analysis'
    self._moduledescription = 'Module to run Whizard2'
    self.appname = 'whizard2'
    self.datatype = 'GEN'
    self._paramsToExclude.extend(["outputDstPath", "outputRecPath", "OutputDstFile", "OutputRecFile"])
    self._ops = Operations()
    self._decayProc = ['decay_proc']
    self._integratedProcess = ''
    self._extension = 'stdhep'

  def setRandomSeed(self, randomSeed):
    """ Optional: Define random seed to use. Default is the jobID.

    :param int randomSeed: Seed to use during generation.
    """
    self._checkArgs({'randomSeed': int})
    self.randomSeed = randomSeed

  def setEvtType(self, evttype):
    """Define process. If the process given is not found, when calling :func:`UserJob.append() <ILCDIRAC.Interfaces.API.NewInterface.UserJob.UserJob.append>` a full list is printed.

    :param str evttype: Process to generate
    """
    self._checkArgs({'evttype': (str,)})
    if self.addedtojob:
      return self._reportError("Cannot modify this attribute once application has been added to Job")
    self.eventType = evttype
    return S_OK()

  def setProcessVariables(self, processes):
    """Set the list of processes to simulate.

    The sindarin file will be modified later on to call **simulate (proc_a, proc_b)**.
    The process variables have to be defined in the sindarin file::

      process proc_a ...
      process proc_b ...

    .. versionadded:: v28r0p6

    :param processes: which processes to call simulate on, by default 'decay_proc'
    :type processes: list, str
    """
    if isinstance(processes, six.string_types):
      self._decayProc = [proc.strip() for proc in processes.split(',')]
      return S_OK()
    elif isinstance(processes, (set, list, tuple)):
      self._decayProc = [proc.strip() for proc in processes]
      return S_OK()

    return self._reportError("Cannot handle this argument type")

  def setSinFile(self, whizard2SinFilePath, raw=False):
    """Set the Whizard2 options to be used.

    Usage:
      - Give path to the Whizard2 steering file.
      - IMPORTANT: set **seed** via iLCDirac API -> `Whizard2.setRandomSeed`
      - IMPORTANT: set **n_events** via iLCDirac API  -> `Whizard2.setNumberOfEvents`
      - IMPORTANT: set **OutputFile** via iLCDirac API -> `Whizard2.setOutputFile`
      - The variables in which processes are defined which should be simulated can be set
        via `Whizard2.setProcessVariables`

    :param str whizard2SinFilePath: Path to the whizard2 sin file.
    :param bool raw: If set to ``True`` only the **seed** will be added to the
      sindarin file. The **simulate(decay process)** , **n_events**, and **OutputFile** modifications by iLCDirac
      will be disabled. The user is responsible for consistency in this case.
    """
    self._checkArgs({'whizard2SinFilePath': (str,)})

    # Chech if file exist
    if not os.path.isfile(whizard2SinFilePath):
      return self._reportError('Whizard2 Sin file does not exist!')

    # Read file
    self.whizard2SinFile = open(whizard2SinFilePath).read()

    if raw:
      self.whizard2RawSin = True
      LOG.info("Using the raw sindarin file")
      return None

    if "n_events" in self.whizard2SinFile:
      return self._reportError('Do not set n_events in the sin file, set it via the iLCDirac API')

    if "seed" in self.whizard2SinFile:
      return self._reportError('Do not set seed in the sin file, set it via the iLCDirac API')

    if "simulate(" in self.whizard2SinFile.replace(" ", ""):
      return self._reportError('Do not call "simulate ()" in the sin file, this is done by iLCDirac')

    return None

  def setIntegratedProcess(self, integrationTarball):
    """Make whizard2 use an already integrated process.

    The ``integrationTarball`` has to be a tarball (zip, tar.gz, tgz), either an LFN, or a process defined in the
    configuration system.

    Use `getKnownProcesses` to see the list of defined processes

    >>> # processes defined in the configuration
    >>> whizard2.setIntegratedProcess('bbcbbc_3tev_negPol')

    >>> # tarball on the grid
    >>> whizard2.setIntegratedProcess('LFN:/ilc/user/u/username/bbcbbc_3tev_negPol.tar.gz')

    :param str integrationTarball: integrated process to be used for event generation

    .. warning :: It is the responsibility of the user to ensure that the sindarin file is compatible with
                  the integrated process

    .. note ::

      Whizard2 will be executed in the path where the tarball is extracted. Therefore, the tarball must contain all the
      files resulting from running Whizard2 directly and not in a subdirectory. The hidden ``.libs/`` folder must be
      included.

      To produce the tarball, change into the directory in which Whizard2 has been run and do::

        tar cvzf <name>.tar.gz * .libs

    .. note :: Tarballs stored on CVMFS need to be registered in the ConfigurationSystem.
    """
    self._checkArgs({'integrationTarball': (str,)})

    # file on the grid
    if integrationTarball.lower().startswith('lfn:'):
      LOG.info('Integrated process file is an LFN, adding it to the sandbox')
      self.inputSB.append(integrationTarball)
      # as the tarball is automatically extracted during the workflow, we do not have to do anything
      self._integratedProcess = ''
      return S_OK()

    knownProcesses = self.getKnownProcesses()
    if not knownProcesses['OK']:
      return self._reportError('Failed to get known integrated processes: %s' % knownProcesses['Message'])
    elif integrationTarball in knownProcesses['Value']:
      self._integratedProcess = integrationTarball
    else:
      return self._reportError('Unknown integrated process in %s: %s (available are: %s)' %
                               (self.appname, integrationTarball, ', '.join(list(knownProcesses['Value'].keys()))))
    return S_OK()

  def getKnownProcesses(self, version=None):
    """Return a list of known integrated processes.

    :param str version: Optional: Software version for which to print the integrated processes.
       If not given the version of the application instance is used.
    :returns: S_OK with list of integrated processes known for this software version, S_ERROR
    """
    if version is None and not self.version:
      return S_ERROR('No software version defined')
    version = self.version if version is None else version
    processes = self._ops.getOptionsDict('/AvailableTarBalls/%s/whizard2/%s/integrated_processes/processes' %
                                         ('x86_64-slc5-gcc43-opt', self.version))
    return processes

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
    """FIXME Check consistency of the Whizard2 application, this is called from the `Job` instance.

    :param job: The instance of the job
    :type job: ~ILCDIRAC.Interfaces.API.NewInterface.Job.Job
    :returns: S_OK/S_ERROR
    """
    if not self.version:
      return S_ERROR('No version found!')

    if not self.whizard2SinFile:
      return S_ERROR('No sin file set!')

    if not self.numberOfEvents:
      return S_ERROR('Number of events not set!')

    for process in self._decayProc:
      if process not in self.whizard2SinFile:
        return S_ERROR('Process "%s" not found in sindarin file, please check your inputs' % process)

    if self._jobtype != 'User':
      self._listofoutput.append({"outputFile": "@{OutputFile}", "outputPath": "@{OutputPath}",
                                 "outputDataSE": '@{OutputSE}'})

      if self.eventType != '':
        self.prodparameters['Process'] = self.eventType
      else:
        return S_ERROR('evttype not set, please set event type!')

      self.prodparameters['nbevts'] = self.numberOfEvents

      parsedString = self.whizard2SinFile.replace(" ", "").split()
      sqrtMatches = [x for x in parsedString if x.startswith('sqrts=') and x.endswith('GeV')]
      if not sqrtMatches:
        return S_ERROR('No energy set in sin file, please set "sqrts=...GeV"')
      elif len(sqrtMatches) != 1:
        return S_ERROR('Multiple instances of "sqrts=..GeV" detected, only one can be processed')

      if not self.energy:
        self.prodparameters['Energy'] = sqrtMatches[0].replace("sqrts=", "").replace("GeV", "")
        self.energy = float(self.prodparameters['Energy'])
      else:
        self.whizard2SinFile = re.sub(r"sqrts *= *[0-9.]* *GeV", "sqrts = %s GeV" %
                                      self.energy,
                                      self.whizard2SinFile)
        self.prodparameters['Energy'] = str(self.energy)

      self.prodparameters['SinFile'] = self.whizard2SinFile

      modelMatches = [x for x in parsedString if x.startswith('model=')]
      if not modelMatches:
        return S_ERROR('No model set in sin file, please set "model=..."')
      elif len(modelMatches) != 1:
        return S_ERROR('Multiple instances of "model=..." detected, only one can be processed')
      self.prodparameters['Model'] = modelMatches[0].replace("model=", "")

    return S_OK()

  def _applicationModule(self):
    md1 = self._createModuleDefinition()
    md1.addParameter(Parameter("randomSeed", 0, "int", "", "", False, False, "Random seed for the generator"))
    md1.addParameter(Parameter("debug", False, "bool", "", "", False, False, "debug mode"))
    md1.addParameter(Parameter("whizard2SinFile", '', "string", "", "", False, False, "Whizard2 steering options"))
    md1.addParameter(Parameter('whizard2RawSin', False, 'bool', '', '', False, False, 'use the raw sin file'))
    md1.addParameter(Parameter("decayProc", [], "list", "", "", False, False, "processses to simulate"))
    md1.addParameter(Parameter('integratedProcess', '', 'string', '', '', False, False, 'Integrated Process to use'))
    return md1

  def _applicationModuleValues(self, moduleinstance):
    moduleinstance.setValue("randomSeed", self.randomSeed)
    moduleinstance.setValue("debug", self.debug)
    moduleinstance.setValue("whizard2SinFile", self.whizard2SinFile)
    moduleinstance.setValue("whizard2RawSin", self.whizard2RawSin)
    moduleinstance.setValue("decayProc", self._decayProc)
    moduleinstance.setValue('integratedProcess', self._integratedProcess)

  def _checkWorkflowConsistency(self):
    return self._checkRequiredApp()
