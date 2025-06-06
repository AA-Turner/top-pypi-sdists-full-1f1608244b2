# -*- coding: utf-8; -*-
################################################################################
#
#  Rattail -- Retail Software Framework
#  Copyright © 2010-2022 Lance Edgar
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
Tailbone Web API
"""

from __future__ import unicode_literals, absolute_import

from .core import APIView, api
from .master import APIMasterView, SortColumn
# TODO: remove this
from .master2 import APIMasterView2


def includeme(config):
    config.include('tailbone.api.common')
    config.include('tailbone.api.auth')
    config.include('tailbone.api.customers')
    config.include('tailbone.api.upgrades')
    config.include('tailbone.api.users')
