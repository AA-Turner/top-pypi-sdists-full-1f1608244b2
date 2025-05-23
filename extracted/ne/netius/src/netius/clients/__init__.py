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

from . import apn
from . import dht
from . import dns
from . import http
from . import mjpg
from . import raw
from . import smtp
from . import ssdp
from . import torrent
from . import ws

from .apn import APNProtocol, APNClient
from .dht import DHTRequest, DHTResponse, DHTClient
from .dns import DNSRequest, DNSResponse, DNSProtocol, DNSClient
from .http import HTTPProtocol, HTTPClient
from .mjpg import MJPGProtocol, MJPGClient
from .raw import RawProtocol, RawClient
from .smtp import SMTPConnection, SMTPClient
from .ssdp import SSDPProtocol, SSDPClient
from .torrent import CHOKED, UNCHOKED, TorrentConnection, TorrentClient
from .ws import WSProtocol, WSClient
