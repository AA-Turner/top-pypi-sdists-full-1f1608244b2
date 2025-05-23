# Copyright 2025 Flower Labs GmbH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Flower client."""


from ..compat.client.app import start_client as start_client  # Deprecated
from ..compat.client.app import start_numpy_client as start_numpy_client  # Deprecated
from .client import Client as Client
from .client_app import ClientApp as ClientApp
from .numpy_client import NumPyClient as NumPyClient
from .typing import ClientFn as ClientFn
from .typing import ClientFnExt as ClientFnExt

__all__ = [
    "Client",
    "ClientApp",
    "ClientFn",
    "ClientFnExt",
    "NumPyClient",
    "mod",
    "start_client",
    "start_numpy_client",
]
