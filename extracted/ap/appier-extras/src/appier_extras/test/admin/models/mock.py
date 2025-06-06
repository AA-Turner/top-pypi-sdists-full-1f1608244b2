#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Appier Framework
# Copyright (c) 2008-2024 Hive Solutions Lda.
#
# This file is part of Hive Appier Framework.
#
# Hive Appier Framework is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Appier Framework is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Appier Framework. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__copyright__ = "Copyright (c) 2008-2024 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import appier_extras

from appier.test.mock import *  # @UnusedWildImport


class AdminPerson(appier_extras.admin.Base):
    name = appier.field()

    age = appier.field(type=int)

    father = appier.field(type=appier.reference("Person", name="identifier"))

    car = appier.field(type=appier.reference("Car", name="identifier"), eager=True)

    cats = appier.field(type=appier.references("Cat", name="identifier"))

    @classmethod
    def validate(cls):
        return super(AdminPerson, cls).validate() + [
            appier.not_null("name"),
            appier.not_empty("name"),
            appier.not_duplicate("name", cls._name()),
        ]

    @classmethod
    def is_snapshot(cls):
        return True
