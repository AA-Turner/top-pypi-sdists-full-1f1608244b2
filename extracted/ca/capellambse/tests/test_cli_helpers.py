# SPDX-FileCopyrightText: Copyright DB InfraGO AG
# SPDX-License-Identifier: Apache-2.0

import pytest

import capellambse

from .conftest import INSTALLED_PACKAGE, TEST_MODEL, TEST_ROOT  # type: ignore

TEST_MODEL_AIRD = TEST_ROOT / "5_0" / TEST_MODEL
TEST_MODEL_JSON = INSTALLED_PACKAGE / "known_models" / "test-5.0.json"


def test_enumerate_known_models_contains_known_test_models():
    expected = {"test-5.0.json", "test-5.2.json", "test-lib.json"}

    actual = {i.name for i in capellambse.enumerate_known_models()}

    assert actual >= expected


def test_climodel_is_idempotent(
    session_shared_model: capellambse.MelodyModel,
) -> None:
    paramtype = capellambse.ModelCLI()

    converted = paramtype.convert(session_shared_model, None, None)

    assert converted is session_shared_model


@pytest.mark.parametrize(
    "value",
    [
        pytest.param(TEST_MODEL_JSON.stem, id="str-known"),
        pytest.param(TEST_MODEL_AIRD, id="str-aird"),
        pytest.param(str(TEST_MODEL_AIRD), id="path-aird"),
        pytest.param(TEST_MODEL_JSON, id="str-jsonfile"),
        pytest.param(str(TEST_MODEL_JSON), id="path-jsonfile"),
        pytest.param(TEST_MODEL_JSON.read_text(), id="json"),
    ],
)
def test_climodel_loads_model(value):
    paramtype = capellambse.ModelCLI()

    converted = paramtype.convert(value, None, None)

    assert isinstance(converted, capellambse.MelodyModel)


@pytest.mark.parametrize(
    "value",
    [
        pytest.param(TEST_MODEL_JSON.stem, id="str-known"),
        pytest.param(TEST_MODEL_AIRD, id="str-aird"),
        pytest.param(str(TEST_MODEL_AIRD), id="path-aird"),
        pytest.param(TEST_MODEL_JSON, id="str-jsonfile"),
        pytest.param(str(TEST_MODEL_JSON), id="path-jsonfile"),
        pytest.param(TEST_MODEL_JSON.read_text(), id="json"),
    ],
)
def test_loadcli_loads_model(value):
    model = capellambse.loadcli(value)

    assert isinstance(model, capellambse.MelodyModel)
