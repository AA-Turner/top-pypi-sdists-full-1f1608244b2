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

########################################################################
# File :   InputDataResolution.py
# Author : S Poss, based on S Paterson
########################################################################

"""The input data resolution module is a VO-specific plugin that allows to define VO input data policy in a simple way using existing utilities in DIRAC or extension code supplied by the VO.

The arguments dictionary from the Job Wrapper includes the file catalogue
result and in principle has all necessary information to resolve input data
for applications.
"""

from __future__ import absolute_import
__RCSID__ = "$Id$"

from DIRAC.Core.Utilities.ModuleFactory import ModuleFactory
from DIRAC.ConfigurationSystem.Client.Helpers.Operations import Operations

from DIRAC import S_OK, S_ERROR, gLogger
import DIRAC


LOG = gLogger.getSubLogger(__name__)
COMPONENT_NAME = 'ILCInputDataResolution'


class InputDataResolution(object):
  """ILC specific input data resolution, imported from DIRAC."""
  #############################################################################

  def __init__(self, argumentsDict):
    """Standard constructor."""
    self.arguments = argumentsDict
    self.name = COMPONENT_NAME
    self.ops = Operations()
  #############################################################################

  def execute(self):
    """Given the arguments from the Job Wrapper, this function calls existing utilities in DIRAC to resolve input data according to LHCb VO policy."""
    result = self.__resolveInputData()
    if not result['OK']:
      LOG.error('InputData resolution failed with result:\n%s' % (result))
      LOG.error('on no, double error')

    # For local running of this module we can expose an option to ignore missing files
    ignoreMissing = False
    if 'IgnoreMissing' in self.arguments:
      ignoreMissing = self.arguments['IgnoreMissing']

    # For LHCb original policy was as long as one TURL exists, this can be conveyed to the application
    # this breaks due to the stripping so the policy has been changed.
    if 'Failed' in result:
      failedReplicas = result['Failed']
      if failedReplicas and not ignoreMissing:
        LOG.error('Failed to obtain access to the following files:\n%s' % ('\n'.join(failedReplicas)))
        return S_ERROR('Failed to access all of requested input data')

    if 'Successful' not in result:
      return result

    if not result['Successful']:
      return S_ERROR('Could not access any requested input data')

    return result

  #############################################################################
  def __resolveInputData(self):
    """This method controls the execution of the DIRAC input data modules according to the ILC VO policy defined in the configuration service."""
    if 'SiteName' in self.arguments['Configuration']:
      site = self.arguments['Configuration']['SiteName']
    else:
      site = DIRAC.siteName()

    policy = []
    if 'Job' not in self.arguments:
      self.arguments['Job'] = {}

    if 'InputDataPolicy' in self.arguments['Job']:
      policy = self.arguments['Job']['InputDataPolicy']
      # In principle this can be a list of modules with the first taking precedence
      if type(policy) in (str,):
        policy = [policy]
      LOG.info('Job has a specific policy setting: %s' % (', '.join(policy)))
    else:
      LOG.verbose('Attempting to resolve input data policy for site %s' % site)
      inputDataPolicy = self.ops.getOptionsDict('/InputDataPolicy')
      if not inputDataPolicy:
        return S_ERROR('Could not resolve InputDataPolicy from /InputDataPolicy')

      options = inputDataPolicy['Value']
      if site in options:
        policy = options[site]
        policy = [x.strip() for x in policy.split(',')]
        LOG.info('Found specific input data policy for site %s:\n%s' % (site, ',\n'.join(policy)))
      elif 'Default' in options:
        policy = options['Default']
        policy = [x.strip() for x in policy.split(',')]
        LOG.info('Applying default input data policy for site %s:\n%s' % (site, ',\n'.join(policy)))

    dataToResolve = None  # if none, all supplied input data is resolved
    allDataResolved = False
    successful = {}
    failedReplicas = []
    for modulePath in policy:
      if not allDataResolved:
        result = self.__runModule(modulePath, dataToResolve)
        if not result['OK']:
          LOG.warn('Problem during %s execution' % modulePath)
          return result

        if 'Failed' in result:
          failedReplicas = result['Failed']

        if failedReplicas:
          LOG.info('%s failed for the following files:\n%s' % (modulePath, '\n'.join(failedReplicas)))
          dataToResolve = failedReplicas
        else:
          LOG.info('All replicas resolved after %s execution' % (modulePath))
          allDataResolved = True

        successful.update(result['Successful'])
        LOG.verbose(successful)

    result = S_OK()
    result['Successful'] = successful
    result['Failed'] = failedReplicas
    return result

  #############################################################################
  def __runModule(self, modulePath, remainingReplicas):
    """This method provides a way to run the modules specified by the VO that govern the input data access policy for the current site.

    For LHCb the
    standard WMS modules are applied in a different order depending on the site.
    """
    LOG.info('Attempting to run %s' % (modulePath))
    moduleFactory = ModuleFactory()
    moduleInstance = moduleFactory.getModule(modulePath, self.arguments)
    if not moduleInstance['OK']:
      return moduleInstance

    module = moduleInstance['Value']
    result = module.execute(remainingReplicas)
    return result

#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#
