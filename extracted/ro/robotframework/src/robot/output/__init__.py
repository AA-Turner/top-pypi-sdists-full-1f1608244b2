#  Copyright 2008-2015 Nokia Networks
#  Copyright 2016-     Robot Framework Foundation
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

"""Package for internal logging and other output.

Not part of the public API, and also subject to change in the future when
test execution is refactored.
"""

from .logger import LOGGER as LOGGER
from .loggerhelper import LEVELS as LEVELS, Message as Message
from .loglevel import LogLevel as LogLevel
from .output import Output as Output
from .xmllogger import XmlLogger as XmlLogger
