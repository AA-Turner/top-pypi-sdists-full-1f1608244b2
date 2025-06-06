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

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__copyright__ = "Copyright (c) 2008-2024 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import netius

from . import common

FILE_WORK = 20

ERROR_ACTION = -1
OPEN_ACTION = 1
CLOSE_ACTION = 2
READ_ACTION = 3
WRITE_ACTION = 4


class FileThread(common.Thread):

    def execute(self, work):
        type = work[0]
        if not type == FILE_WORK:
            netius.NotImplemented("Cannot execute type '%d'" % type)

        try:
            self._execute(work)
        except BaseException as exception:
            self.owner.push_event((ERROR_ACTION, exception, work[-1]))

    def open(self, path, mode, data):
        file = open(path)
        self.owner.push_event((OPEN_ACTION, file, data))

    def close(self, file, data):
        file.close()
        self.owner.push_event((CLOSE_ACTION, file, data))

    def read(self, file, count, data):
        result = file.read(count)
        self.owner.push_event((READ_ACTION, result, data))

    def write(self, file, buffer, data):
        file.write(buffer)
        self.owner.push_event((WRITE_ACTION, len(buffer), data))

    def _execute(self, work):
        action = work[1]
        if action == OPEN_ACTION:
            self.open(*work[2:])
        elif action == CLOSE_ACTION:
            self.close(*work[2:])
        elif action == READ_ACTION:
            self.read(*work[2:])
        elif action == WRITE_ACTION:
            self.read(*work[2:])
        else:
            netius.NotImplemented("Undefined file action '%d'" % action)


class FilePool(common.EventPool):

    def __init__(self, base=FileThread, count=10):
        common.EventPool.__init__(self, base=base, count=count)

    def open(self, path, mode="r", data=None):
        work = (FILE_WORK, OPEN_ACTION, path, mode, data)
        self.push(work)

    def close(self, file, data=None):
        work = (FILE_WORK, CLOSE_ACTION, file, data)
        self.push(work)

    def read(self, file, count=-1, data=None):
        work = (FILE_WORK, READ_ACTION, file, count, data)
        self.push(work)

    def write(self, file, buffer, data=None):
        work = (FILE_WORK, WRITE_ACTION, file, buffer, data)
        self.push(work)
