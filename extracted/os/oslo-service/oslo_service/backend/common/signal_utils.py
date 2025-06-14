# Copyright (C) 2025 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import signal


def get_signal_mappings(ignore=('SIG_DFL', 'SIG_IGN')):
    signals_by_name = {
        name: getattr(signal, name)
        for name in dir(signal)
        if name.startswith('SIG') and name not in ignore
    }
    signals_to_name = {v: k for k, v in signals_by_name.items()}

    return signals_by_name, signals_to_name


class SignalExit(SystemExit):
    """Raised to indicate a signal-based exit.

    This exception is commonly raised when the process receives a termination
    signal (e.g., SIGTERM, SIGINT). The signal number is stored in `signo`.
    """

    def __init__(self, signo, exccode=1):
        super().__init__(exccode)
        self.signo = signo
