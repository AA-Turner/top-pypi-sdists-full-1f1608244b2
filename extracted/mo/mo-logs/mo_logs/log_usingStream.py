# encoding: utf-8
#
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at https://www.mozilla.org/en-US/MPL/2.0/.
#
# Contact: Kyle Lahnakoski (kyle@lahnakoski.com)
#
from mo_future import allocate_lock, STDERR, STDOUT

from mo_logs.log_usingNothing import StructuredLogger
from mo_logs.strings import CR, expand_template


class StructuredLogger_usingStream(StructuredLogger):
    def __init__(self, stream):
        try:
            self.locker = allocate_lock()
            self.flush = stream.flush
            if stream in (STDOUT, STDERR):
                try:
                    stream = stream.buffer
                except Exception:
                    # SOMETIMES STDOUT IS REPLACED BY SOMETHING ELSE
                    pass
            self.writer = _UTF8Encoder(stream).write
        except Exception as _:
            import sys

            sys.stderr.write("can not handle")

    def write(self, template, params):
        value = expand_template(template, params)
        with self.locker:
            self.writer(value + CR)
            try:
                self.flush()
            except Exception:
                pass

    def stop(self):
        try:
            self.flush()
        except Exception:
            pass


class _UTF8Encoder:
    def __init__(self, stream):
        self.stream = stream

    def write(self, v):
        try:
            self.stream.write(v.encode("utf8"))
            self.stream.flush()
        except Exception:
            import sys

            sys.stderr.write("can not handle")
