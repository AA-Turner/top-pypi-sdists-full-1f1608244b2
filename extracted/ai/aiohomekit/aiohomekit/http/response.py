#
# Copyright 2019 aiohomekit team
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
#

import logging
from typing import Union

from aiohomekit.exceptions import HttpException

logger = logging.getLogger(__name__)


class HttpResponse:
    STATE_PRE_STATUS = 0
    STATE_HEADERS = 1
    STATE_BODY = 2
    STATE_DONE = 3

    def __init__(self) -> None:
        self._state = HttpResponse.STATE_PRE_STATUS
        self._raw_response = bytearray()
        self._is_ready = False
        self._is_chunked = False
        self._had_empty_chunk = False
        self._content_length = -1
        self.version = None
        self.code = None
        self.reason = None
        self.headers = []
        self.body = bytearray()

    def parse(self, part: Union[bytearray, bytes]) -> bytearray:
        self._raw_response += part
        pos = self._raw_response.find(b"\r\n")

        while pos != -1 and self._state < HttpResponse.STATE_BODY:
            line = self._raw_response[:pos]
            self._raw_response = self._raw_response[pos + 2 :]
            if self._state == HttpResponse.STATE_PRE_STATUS:
                # parse status line
                line = line.split(b" ", 2)
                if len(line) != 3:
                    raise HttpException("Malformed status line.")
                self.version = line[0].decode()
                self.code = int(line[1])
                self.reason = line[2].decode()
                self._state = HttpResponse.STATE_HEADERS

            elif self._state == HttpResponse.STATE_HEADERS and line == b"":
                # this is the empty line after the headers
                self._state = HttpResponse.STATE_BODY

            elif self._state == HttpResponse.STATE_HEADERS:
                # parse a header line
                line = line.split(b":", 1)
                name = line[0].decode().strip().title()
                value = line[1].decode().strip()
                if name == "Transfer-Encoding":
                    if value == "chunked":
                        self._is_chunked = True
                elif name == "Content-Length":
                    self._content_length = int(value)
                self.headers.append((name, value))
            else:
                raise HttpException("Unknown parser state")

            pos = self._raw_response.find(b"\r\n")

        if self._state == HttpResponse.STATE_BODY and self._is_chunked:
            pos = self._raw_response.find(b"\r\n")
            while pos > -1:
                line = self._raw_response[:pos]
                self._raw_response = self._raw_response[pos + 2 :]
                length = int(line, 16)
                if length + 2 > len(self._raw_response):
                    self._raw_response = line + b"\r\n" + self._raw_response
                    # the remaining bytes in raw response are not sufficient. bail out and wait for an other call.
                    break

                if length == 0:
                    self._had_empty_chunk = True
                    self._state = HttpResponse.STATE_DONE
                    self._raw_response = self._raw_response[length + 2 :]
                    break

                line = self._raw_response[:length]
                self.body += line
                self._raw_response = self._raw_response[length + 2 :]

                pos = self._raw_response.find(b"\r\n")

        if self._state == HttpResponse.STATE_BODY and self._content_length > 0:
            remaining = self._content_length - len(self.body)
            self.body += self._raw_response[:remaining]
            self._raw_response = self._raw_response[remaining:]

        if self.is_read_completely():
            # Whatever is left in the buffer is part of the next request
            if len(self._raw_response) > 0:
                logger.debug("Bytes left in buffer after parsing packet: %r", self._raw_response)
            return self._raw_response

        return bytearray()

    def read(self):
        """
        Returns the body of the response.

        :return: The read body or None if no body content was read yet
        """
        return self.body

    def is_read_completely(self) -> bool:
        if self._is_chunked:
            return self._had_empty_chunk

        if self._state < HttpResponse.STATE_BODY:
            return False

        if self._content_length != -1:
            return len(self.body) == self._content_length

        return True

    def get_http_name(self) -> str:
        """
        Returns the HTTP name (e.g. HTTP or EVENT).

        :return: The name or None if the status line was not yet read
        """
        if self.version is not None:
            return self.version.split("/")[0]
        return None
