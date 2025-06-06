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
"""Tests for the ResolveSE module."""
from __future__ import absolute_import
import unittest
from mock import patch, MagicMock as Mock

from DIRAC import S_OK, S_ERROR
from ILCDIRAC.Core.Utilities.ResolveSE import getDestinationSEList
from Tests.Utilities.GeneralUtils import assertDiracFailsWith, assertDiracSucceedsWith, assertDiracSucceedsWith_equals

__RCSID__ = "$Id$"

MODULE_NAME = 'ILCDIRAC.Core.Utilities.ResolveSE'


class TestGetDestinationSE(unittest.TestCase):
  """Test getDestinationSEList function."""

  def test_getdestinationse(self):
    options_dict = {'/Resources/StorageElements/myOutputSE': S_ERROR('bla')}
    values_dict = {'/Resources/Sites/pre/pre.myTestSite.country/AssociatedSEs/myOutputSE': [],
                    '/Resources/StorageElementGroups/myOutputSE': ['some_grp_member', 'GroupElement', 'StorEl', 'LocalElement']}
    conf_mock = Mock()
    conf_mock.getOptions.side_effect = lambda path: options_dict[path]
    conf_mock.getValue.side_effect = lambda path, _: values_dict[path]
    with patch('%s.getSEsForSite' % MODULE_NAME, new=Mock(return_value=S_OK(['StorEl', 'LocalElement']))), \
         patch('%s.gConfig' % MODULE_NAME, conf_mock):
      result = getDestinationSEList('myOutputSE', 'pre.myTestSite.country', 'AnyOutputmodeTest')
      assertDiracSucceedsWith_equals(result, ['StorEl', 'LocalElement', 'some_grp_member', 'GroupElement'], self)

  def test_getdestinationse_alias_found(self):
    options_dict = {'/Resources/StorageElements/myOutputSE': S_ERROR('bla')}
    values_dict = {'/Resources/Sites/pre/pre.myTestSite.country/AssociatedSEs/myOutputSE':
                    'myTest_Alias_value'}
    conf_mock = Mock()
    conf_mock.getOptions.side_effect = lambda path: options_dict[path]
    conf_mock.getValue.side_effect = lambda path, _: values_dict[path]
    with patch('%s.gConfig' % MODULE_NAME, conf_mock):
      result = getDestinationSEList('myOutputSE', 'pre.myTestSite.country', 'AnyOutputmodeTest')
      assertDiracSucceedsWith(result, 'myTest_Alias_value', self)

  def test_getdestinationse_nogroupse(self):
    options_dict = {'/Resources/StorageElements/myOutputSE': S_ERROR('bla')}
    values_dict = {'/Resources/Sites/pre/pre.myTestSite.country/AssociatedSEs/myOutputSE': [],
                    '/Resources/StorageElementGroups/myOutputSE': []}
    conf_mock = Mock()
    conf_mock.getOptions.side_effect = lambda path: options_dict[path]
    conf_mock.getValue.side_effect = lambda path, _: values_dict[path]
    #DIRAC.gConfig = conf_mock
    with patch('%s.getSEsForSite' % MODULE_NAME, new=Mock(return_value=S_OK(['myTestStorageElement1', 'otherStorageElem2']))), \
         patch('%s.gConfig' % MODULE_NAME, conf_mock):
      result = getDestinationSEList('myOutputSE', 'pre.myTestSite.country', 'AnyOutputmodeTest')
      assertDiracFailsWith(result, 'failed to resolve se myoutputse', self)

  def test_getdestinationse_localgroupse(self):
    options_dict = {'/Resources/StorageElements/myOutputSE': S_ERROR('bla')}
    values_dict = {'/Resources/Sites/pre/pre.myTestSite.country/AssociatedSEs/myOutputSE': [],
                    '/Resources/StorageElementGroups/myOutputSE': ['some_elements', 'ignore_me',
                                                                     'otherStorageElem2']}
    conf_mock = Mock()
    conf_mock.getOptions.side_effect = lambda path: options_dict[path]
    conf_mock.getValue.side_effect = lambda path, _: values_dict[path]
    with patch('%s.getSEsForSite' % MODULE_NAME, new=Mock(return_value=S_OK(['myTestStorageElement1', 'otherStorageElem2']))), \
         patch('%s.gConfig' % MODULE_NAME, conf_mock):
      result = getDestinationSEList('myOutputSE', 'pre.myTestSite.country', 'Local')
      assertDiracSucceedsWith_equals(result, ['otherStorageElem2'], self)

  def test_getdestinationse_associatedse(self):
    options_dict = {'/Resources/StorageElements/myOutputSE': S_ERROR('bla')}
    values_dict = {'/Resources/Sites/pre/pre.myTestSite.country/AssociatedSEs/myOutputSE': [],
                    '/Resources/StorageElementGroups/myOutputSE': ['some_elements', 'ignore_me'],
                    '/Resources/Countries/country/AssociatedSEs/myOutputSE': 'myassociated_se'}
    conf_mock = Mock()
    conf_mock.getOptions.side_effect = lambda path: options_dict[path]
    conf_mock.getValue.side_effect = lambda path, _: values_dict[path]
    with patch('%s.getSEsForSite' % MODULE_NAME, new=Mock(return_value=S_OK(['myTestStorageElement1', 'otherStorageElem2']))), \
         patch('%s.gConfig' % MODULE_NAME, conf_mock):
      result = getDestinationSEList('myOutputSE', 'pre.myTestSite.country', 'Local')
      assertDiracSucceedsWith_equals(result, ['myassociated_se'], self)

  def test_getdestinationse_noassoc_country(self):
    options_dict = {'/Resources/StorageElements/myOutputSE': S_ERROR('bla')}
    option_dict = {'/Resources/Countries/country/AssignedTo': S_OK('MyTestCountry.Assigned'),
                    '/Resources/Countries/MyTestCountry.Assigned/AssociatedSEs': S_OK('something')}
    values_dict = {'/Resources/Sites/pre/pre.myTestSite.country/AssociatedSEs/myOutputSE': [],
                    '/Resources/StorageElementGroups/myOutputSE': ['some_elements', 'ignore_me'],
                    '/Resources/Countries/MyTestCountry.Assigned/AssociatedSEs/myOutputSE':
                    ['myassociated_alias_se'],
                    '/Resources/Countries/country/AssociatedSEs/myOutputSE': ''}
    conf_mock = Mock()
    conf_mock.getOptions.side_effect = lambda path: options_dict[path]
    conf_mock.getOption.side_effect = lambda path: option_dict[path]
    conf_mock.getValue.side_effect = lambda path, _: values_dict[path]
    with patch('%s.getSEsForSite' % MODULE_NAME, new=Mock(return_value=S_OK(['myTestStorageElement1', 'otherStorageElem2']))), \
         patch('%s.gConfig' % MODULE_NAME, conf_mock):
      result = getDestinationSEList('myOutputSE', 'pre.myTestSite.country', 'Local')
      assertDiracSucceedsWith_equals(result, ['myassociated_alias_se'], self)

  def test_getdestinationse_no_assoc_list(self):
    options_dict = {'/Resources/StorageElements/myOutputSE': S_ERROR('bla')}
    option_dict = {'/Resources/Countries//AssignedTo': S_OK('')}
    values_dict = {'/Resources/Sites/pre/pre.myTestSite./AssociatedSEs/myOutputSE': [],
                    '/Resources/StorageElementGroups/myOutputSE': ['some_elements', 'ignore_me'],
                    '/Resources/Countries/MyTestCountry.Assigned/AssociatedSEs/myOutputSE':
                    ['myassociated_alias_se'],
                    '/Resources/Countries//AssociatedSEs/myOutputSE': ''}
    conf_mock = Mock()
    conf_mock.getOptions.side_effect = lambda path: options_dict[path]
    conf_mock.getOption.side_effect = lambda path: option_dict[path]
    conf_mock.getValue.side_effect = lambda path, _: values_dict[path]
    with patch('%s.getSEsForSite' % MODULE_NAME, new=Mock(return_value=S_OK(['myTestStorageElement1', 'otherStorageElem2']))), \
         patch('%s.gConfig' % MODULE_NAME, conf_mock):
      result = getDestinationSEList('myOutputSE', 'pre.myTestSite.', 'Local')
      assertDiracFailsWith(result, 'could not determine associated se list', self)

  def test_getdestinationse_no_assoc_alias(self):
    options_dict = {'/Resources/StorageElements/myOutputSE': S_ERROR('bla')}
    option_dict = {'/Resources/Countries/country/AssignedTo': S_OK('MyTestCountry.Assigned'),
                    '/Resources/Countries/MyTestCountry.Assigned/AssociatedSEs': S_OK('something')}
    values_dict = {'/Resources/Sites/pre/pre.myTestSite.country/AssociatedSEs/myOutputSE': [],
                    '/Resources/StorageElementGroups/myOutputSE': ['some_elements', 'ignore_me'],
                    '/Resources/Countries/MyTestCountry.Assigned/AssociatedSEs/myOutputSE': [],
                    '/Resources/Countries/country/AssociatedSEs/myOutputSE': ''}
    conf_mock = Mock()
    conf_mock.getOptions.side_effect = lambda path: options_dict[path]
    conf_mock.getOption.side_effect = lambda path: option_dict[path]
    conf_mock.getValue.side_effect = lambda path, _: values_dict[path]
    with patch('%s.getSEsForSite' % MODULE_NAME, new=Mock(return_value=S_OK(['myTestStorageElement1', 'otherStorageElem2']))), \
         patch('%s.gConfig' % MODULE_NAME, conf_mock):
      result = getDestinationSEList('myOutputSE', 'pre.myTestSite.country', 'Local')
      assertDiracFailsWith(result, 'failed to resolve se', self)
