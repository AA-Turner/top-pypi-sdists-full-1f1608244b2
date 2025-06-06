# -*- coding: utf-8; -*-
################################################################################
#
#  Rattail -- Retail Software Framework
#  Copyright © 2010-2023 Lance Edgar
#
#  This file is part of Rattail.
#
#  Rattail is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or (at your option) any later
#  version.
#
#  Rattail is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
#  details.
#
#  You should have received a copy of the GNU General Public License along with
#  Rattail.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
"""
(Deprecated!) Views for label batches

Please use `tailbone.views.batch.labels` instead.
"""

import warnings


def includeme(config):

    warnings.warn("The `tailbone.views.labels.batch` module is deprecated, "
                  "please use `tailbone.views.batch.labels` instead.",
                  DeprecationWarning, stacklevel=2)

    config.include('tailbone.views.batch.labels')
