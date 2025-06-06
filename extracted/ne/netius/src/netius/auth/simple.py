#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Netius System
# Copyright (c) 2008-2024 Hive Solutions Lda.
#
# This file is part of Hive Netius System.
#
# Hive Netius System is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Netius System is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Netius System. If not, see <http://www.apache.org/licenses/>.

__copyright__ = "Copyright (c) 2008-2024 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

from . import base


class SimpleAuth(base.Auth):

    def __init__(self, username=None, password=None, *args, **kwargs):
        base.Auth.__init__(self, *args, **kwargs)
        self.username = username
        self.password = password

    @classmethod
    def auth(cls, username, password, target=None, *args, **kwargs):
        if not target:
            return False
        _username, _password = target
        if _username and not username == _username:
            return False
        if not password == _password:
            return False
        return True

    def auth_i(self, username, password, *args, **kwargs):
        return self.__class__.auth(
            username, password, target=(self.username, self.password), *args, **kwargs
        )
