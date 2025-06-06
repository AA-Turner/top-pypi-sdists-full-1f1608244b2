#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Copyright 2018-2023 OpenEEmeter contributors

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""
import pytest

from eeweather.warnings import EEWeatherWarning


@pytest.fixture
def generic_eeweather_warning():
    return EEWeatherWarning(
        qualified_name="qualified_name", description="description", data={}
    )


def test_str_repr(generic_eeweather_warning):
    assert str(generic_eeweather_warning) == (
        "EEWeatherWarning(qualified_name=qualified_name)"
    )


def test_json_repr(generic_eeweather_warning):
    assert generic_eeweather_warning.json() == {
        "qualified_name": "qualified_name",
        "description": "description",
        "data": {},
    }
