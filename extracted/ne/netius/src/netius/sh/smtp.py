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

from . import base

import netius.clients


def send(
    path, sender, receiver, host=None, port=25, username=None, password=None, stls=True
):
    file = open(path, "rb")
    try:
        contents = file.read()
    finally:
        file.close()
    smtp_client = netius.clients.SMTPClient(auto_close=True)
    smtp_client.message(
        [sender],
        [receiver],
        contents,
        host=host,
        port=port,
        username=username,
        password=password,
        stls=stls,
    )


if __name__ == "__main__":
    base.sh_call(globals(), locals())
else:
    __path__ = []
