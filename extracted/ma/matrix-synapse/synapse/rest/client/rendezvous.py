#
# This file is licensed under the Affero General Public License (AGPL) version 3.
#
# Copyright 2022 The Matrix.org Foundation C.I.C.
# Copyright (C) 2023-2024 New Vector, Ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# See the GNU Affero General Public License for more details:
# <https://www.gnu.org/licenses/agpl-3.0.html>.
#
# Originally licensed under the Apache License, Version 2.0:
# <http://www.apache.org/licenses/LICENSE-2.0>.
#
# [This file includes modifications made by New Vector Limited]
#
#

import logging
from http.client import TEMPORARY_REDIRECT
from typing import TYPE_CHECKING, Optional

from synapse.http.server import HttpServer, respond_with_redirect
from synapse.http.servlet import RestServlet
from synapse.http.site import SynapseRequest
from synapse.rest.client._base import client_patterns

if TYPE_CHECKING:
    from synapse.server import HomeServer

logger = logging.getLogger(__name__)


class MSC4108DelegationRendezvousServlet(RestServlet):
    PATTERNS = client_patterns(
        "/org.matrix.msc4108/rendezvous$", releases=[], v1=False, unstable=True
    )

    def __init__(self, hs: "HomeServer"):
        super().__init__()
        redirection_target: Optional[str] = (
            hs.config.experimental.msc4108_delegation_endpoint
        )
        assert redirection_target is not None, (
            "Servlet is only registered if there is a delegation target"
        )
        self.endpoint = redirection_target.encode("utf-8")

    async def on_POST(self, request: SynapseRequest) -> None:
        respond_with_redirect(
            request, self.endpoint, statusCode=TEMPORARY_REDIRECT, cors=True
        )


class MSC4108RendezvousServlet(RestServlet):
    PATTERNS = client_patterns(
        "/org.matrix.msc4108/rendezvous$", releases=[], v1=False, unstable=True
    )

    def __init__(self, hs: "HomeServer") -> None:
        super().__init__()
        self._handler = hs.get_rendezvous_handler()

    def on_POST(self, request: SynapseRequest) -> None:
        self._handler.handle_post(request)


def register_servlets(hs: "HomeServer", http_server: HttpServer) -> None:
    if hs.config.experimental.msc4108_enabled:
        MSC4108RendezvousServlet(hs).register(http_server)

    if hs.config.experimental.msc4108_delegation_endpoint is not None:
        MSC4108DelegationRendezvousServlet(hs).register(http_server)
