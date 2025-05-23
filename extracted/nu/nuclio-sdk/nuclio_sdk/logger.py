# Copyright 2017 The Nuclio Authors.
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

import logging

import nuclio_sdk.json_encoder


class JSONFormatter(logging.Formatter):
    def __init__(self):
        super(JSONFormatter, self).__init__()

        self._json_encoder = nuclio_sdk.json_encoder.Encoder()

    def format(self, record):
        record_fields = self._get_formatted_record_dict(record)
        return self._json_encoder.encode(record_fields)

    def format_to_log_control_message(self, record):
        record_fields = {
            "kind": "log",
            "attributes": self._get_formatted_record_dict(record),
        }
        return self._json_encoder.encode(record_fields)

    def _get_formatted_record_dict(self, record):
        return {
            "datetime": self.formatTime(record, self.datefmt),
            "level": record.levelname.lower(),
            "message": record.getMessage(),
            "with": getattr(record, "with", {}),
        }


class HumanReadableFormatter(logging.Formatter):
    def __init__(self):
        super(HumanReadableFormatter, self).__init__()

    def format(self, record):
        record_with = getattr(record, "with", {})
        if record_with:
            more = ": {0}".format(record_with)
        else:
            more = ""

        return "Python> {0} [{1}] {2}{3}".format(
            self.formatTime(record, self.datefmt),
            record.levelname.lower(),
            record.getMessage(),
            more,
        )


class Logger(object):
    def __init__(self, level, name="nuclio_sdk"):
        self._logger = logging.getLogger(name)
        self._logger.setLevel(level)
        self._bound_variables = {}

    def set_handler(self, handler_name, file, formatter):

        # check if there's a handler by this name
        for handler in self._logger.handlers:
            if handler.name == handler_name:
                self._logger.removeHandler(handler)
                break

        # create a stream handler from the file
        stream_handler = logging.StreamHandler(file)
        stream_handler.name = handler_name

        # set the formatter
        stream_handler.setFormatter(formatter)

        # add the handler to the logger
        self._logger.addHandler(stream_handler)

    def debug(self, message, *args):
        self._update_bound_vars_and_log(logging.DEBUG, message, *args)

    def info(self, message, *args):
        self._update_bound_vars_and_log(logging.INFO, message, *args)

    def warn(self, message, *args):
        self._update_bound_vars_and_log(logging.WARNING, message, *args)

    def error(self, message, *args):
        self._update_bound_vars_and_log(logging.ERROR, message, *args)

    def debug_with(self, message, *args, **kw_args):
        self._update_bound_vars_and_log(logging.DEBUG, message, *args, **kw_args)

    def info_with(self, message, *args, **kw_args):
        self._update_bound_vars_and_log(logging.INFO, message, *args, **kw_args)

    def warn_with(self, message, *args, **kw_args):
        self._update_bound_vars_and_log(logging.WARNING, message, *args, **kw_args)

    def error_with(self, message, *args, **kw_args):
        self._update_bound_vars_and_log(logging.ERROR, message, *args, **kw_args)

    def bind(self, **kw_args):
        self._bound_variables.update(kw_args)

    def _update_bound_vars_and_log(self, level, message, *args, **kw_args):
        kw_args.update(self._bound_variables)

        if len(kw_args) != 0:
            self._logger._log(level, message, args, extra={"with": kw_args})
            return

        self._logger._log(level, message, args)
