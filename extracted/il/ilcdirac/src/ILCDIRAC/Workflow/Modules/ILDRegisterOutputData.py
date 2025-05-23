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
"""ILD specific registration of file meta data.

:since: Mar 21, 2013
:author: sposs
"""

from __future__ import absolute_import
import os

from ILCDIRAC.Workflow.Modules.ModuleBase import ModuleBase
from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient

from DIRAC import S_OK, gLogger

__RCSID__ = '$Id$'
LOG = gLogger.getSubLogger(__name__)


class ILDRegisterOutputData(ModuleBase):
  """Register output data in the FC for the ILD productions."""

  def __init__(self):
    super(ILDRegisterOutputData, self).__init__()
    self.version = "ILDRegisterOutputData v1"
    self.commandTimeOut = 10 * 60
    self.enable = True
    self.prodOutputLFNs = []
    self.nbofevents = 0
    self.filecatalog = FileCatalogClient()
    self.ildconfig = ''
    self.swpackages = []

  def applicationSpecificInputs(self):
    if 'Enable' in self.step_commons:
      self.enable = self.step_commons['Enable']
      if not isinstance(self.enable, type(True)):
        LOG.warn('Enable flag set to non-boolean value %s, setting to False' % self.enable)
        self.enable = False

    if 'ProductionOutputData' in self.workflow_commons:
      self.prodOutputLFNs = self.workflow_commons['ProductionOutputData'].split(";")
    else:
      self.prodOutputLFNs = []

    if 'SoftwarePackages' in self.workflow_commons:
      self.swpackages = self.workflow_commons['SoftwarePackages'].split(";")

    self.nbofevents = self.NumberOfEvents  # comes from ModuleBase
    if 'ILDConfigPackage' in self.workflow_commons:
      self.ildconfig = self.workflow_commons['ILDConfigPackage']
    return S_OK('Parameters resolved')

  def execute(self):
    LOG.info('Initializing %s' % self.version)
    result = self.resolveInputVariables()
    if not result['OK']:
      LOG.error("Failed to resolve input parameters:", result['Message'])
      return result

    if not self.workflowStatus['OK'] or not self.stepStatus['OK']:
      LOG.verbose('Workflow status = %s, step status = %s' % (self.workflowStatus['OK'], self.stepStatus['OK']))
      return S_OK('No registration of output data metadata attempted')

    if len(self.prodOutputLFNs) == 0:
      LOG.info('No production data found, so no metadata registration to be done')
      return S_OK("No files' metadata to be registered")

    LOG.verbose("Will try to set the metadata for the following files: \n %s" % "\n".join(self.prodOutputLFNs))

    # TODO: What meta data should be stored at file level?

    for files in self.prodOutputLFNs:
      meta = {}

      if self.nbofevents:
        nbevts = {}
        nbevts['NumberOfEvents'] = self.nbofevents
        if 'file_number_of_event_relation' in self.workflow_commons:
          if os.path.basename(files) in self.workflow_commons['file_number_of_event_relation']:
            nbevts['NumberOfEvents'] = self.workflow_commons['file_number_of_event_relation'][os.path.basename(files)]
        meta.update(nbevts)

      if 'CrossSection' in self.inputdataMeta:
        xsec = {'CrossSection': self.inputdataMeta['CrossSection']}
        meta.update(xsec)

      if 'CrossSectionError' in self.inputdataMeta:
        xsec = {'CrossSectionError': self.inputdataMeta['CrossSectionError']}
        meta.update(xsec)

      if 'GenProcessID' in self.inputdataMeta:
        fmeta = {'GenProcessID': self.inputdataMeta['GenProcessID']}
        meta.update(fmeta)

      if 'GenProcessType' in self.inputdataMeta:
        fmeta = {'GenProcessType': self.inputdataMeta['GenProcessType']}
        meta.update(fmeta)

      if 'GenProcessName' in self.inputdataMeta:
        fmeta = {'GenProcessName': self.inputdataMeta['GenProcessName']}
        meta.update(fmeta)

      if 'Luminosity' in self.inputdataMeta:
        fmeta = {'Luminosity': self.inputdataMeta['Luminosity']}
        meta.update(fmeta)

      if 'BeamParticle1' in self.inputdataMeta:
        fmeta = {'BeamParticle1': self.inputdataMeta['BeamParticle1'],
                 'BeamParticle2': self.inputdataMeta['BeamParticle2']}
        meta.update(fmeta)

      if 'PolarizationB1' in self.inputdataMeta:
        fmeta = {'PolarizationB1': self.inputdataMeta['PolarizationB1'],
                 'PolarizationB2': self.inputdataMeta['PolarizationB2']}
        meta.update(fmeta)

      if self.ildconfig:
        fmeta = {'ILDConfig': self.ildconfig}
        meta.update(fmeta)

      if self.WorkflowStartFrom:
        meta.update({"FirstEventFromInput": self.WorkflowStartFrom})

      if self.enable:
        res = self.filecatalog.setMetadata(files, meta)
        if not res['OK']:
          LOG.error('Could not register metadata:', res['Message'])
          return res
      LOG.info("Registered %s with tags %s" % (files, meta))

      # Now, set the ancestors
      if self.InputData:
        inputdata = self.InputData
        if self.enable:
          res = self.filecatalog.addFileAncestors({files: {'Ancestors': inputdata}})
          if not res['OK']:
            LOG.error('Registration of Ancestors failed for:', str(files))
            LOG.error('because of', res['Message'])
            return res

    return S_OK('Output data metadata registered in catalog')
