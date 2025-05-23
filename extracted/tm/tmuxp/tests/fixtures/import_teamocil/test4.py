"""Teamocil data fixtures for import_teamocil tests, 4th test."""

from __future__ import annotations

from tests.fixtures import utils as test_utils

teamocil_yaml = test_utils.read_workspace_file("import_teamocil/test4.yaml")

teamocil_dict = {
    "windows": [
        {
            "name": "erb-example",
            "root": "<%= ENV['MY_PROJECT_ROOT'] %>",
            "panes": [{"cmd": "pwd"}],
        },
    ],
}

expected = {
    "session_name": None,
    "windows": [
        {
            "window_name": "erb-example",
            "start_directory": "<%= ENV['MY_PROJECT_ROOT'] %>",
            "panes": [{"shell_command": "pwd"}],
        },
    ],
}
