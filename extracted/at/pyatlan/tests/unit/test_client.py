# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Atlan Pte. Ltd.
from importlib.resources import read_text
from json import load, loads
from pathlib import Path
from re import escape
from unittest.mock import DEFAULT, Mock, call, patch

import pytest
from pydantic.v1 import ValidationError

from pyatlan.client.asset import (
    LOGGER,
    AssetClient,
    Batch,
    CustomMetadataHandling,
    IndexSearchResults,
)
from pyatlan.client.atlan import AtlanClient
from pyatlan.client.common import ApiCaller
from pyatlan.client.group import GroupClient
from pyatlan.client.search_log import SearchLogClient
from pyatlan.client.typedef import TypeDefClient
from pyatlan.client.user import UserClient
from pyatlan.errors import (
    ERROR_CODE_FOR_HTTP_STATUS,
    ApiError,
    AtlanError,
    ErrorCode,
    InvalidRequestError,
    NotFoundError,
)
from pyatlan.model.assets import (
    Asset,
    AtlasGlossary,
    AtlasGlossaryCategory,
    AtlasGlossaryTerm,
    Column,
    DataDomain,
    DataProduct,
    Table,
    View,
)
from pyatlan.model.core import Announcement, BulkRequest
from pyatlan.model.enums import (
    AnnouncementType,
    CertificateStatus,
    LineageDirection,
    SaveSemantic,
    SortOrder,
)
from pyatlan.model.fluent_search import CompoundQuery, FluentSearch
from pyatlan.model.group import GroupRequest
from pyatlan.model.lineage import LineageListRequest
from pyatlan.model.response import AssetMutationResponse
from pyatlan.model.search import DSL, Bool, IndexSearchRequest, Term, TermAttributes
from pyatlan.model.search_log import SearchLogRequest
from pyatlan.model.typedef import EnumDef
from pyatlan.model.user import AtlanUser, UserRequest
from tests.unit.constants import (
    TEST_ADMIN_CLIENT_METHODS,
    TEST_ASSET_CLIENT_METHODS,
    TEST_AUDIT_CLIENT_METHODS,
    TEST_GROUP_CLIENT_METHODS,
    TEST_ROLE_CLIENT_METHODS,
    TEST_SL_CLIENT_METHODS,
    TEST_TOKEN_CLIENT_METHODS,
    TEST_TYPEDEF_CLIENT_METHODS,
    TEST_USER_CLIENT_METHODS,
)
from tests.unit.model.constants import (
    CONNECTION_NAME,
    CONNECTOR_TYPE,
    DATA_DOMAIN_NAME,
    DATA_PRODUCT_NAME,
    GLOSSARY_CATEGORY_NAME,
    GLOSSARY_NAME,
    GLOSSARY_QUALIFIED_NAME,
    GLOSSARY_TERM_NAME,
    PERSONA_NAME,
    PURPOSE_NAME,
)

GLOSSARY = AtlasGlossary.create(name=GLOSSARY_NAME)
GLOSSARY_CATEGORY = AtlasGlossaryCategory.create(
    name=GLOSSARY_CATEGORY_NAME, anchor=GLOSSARY
)
GLOSSARY_TERM = AtlasGlossaryTerm.create(name=GLOSSARY_TERM_NAME, anchor=GLOSSARY)
UNIQUE_USERS = "uniqueUsers"
UNIQUE_ASSETS = "uniqueAssets"
LOG_IP_ADDRESS = "ipAddress"
LOG_USERNAME = "userName"
SEARCH_PARAMS = "searchParameters"
SEARCH_COUNT = "approximateCount"
TEST_DATA_DIR = Path(__file__).parent / "data"
SEARCH_LOG_RESPONSES_DIR = TEST_DATA_DIR / "search_log_responses"
SL_MOST_RECENT_VIEWERS_JSON = "sl_most_recent_viewers.json"
SL_MOST_VIEWED_ASSETS_JSON = "sl_most_viewed_assets.json"
SL_DETAILED_LOG_ENTRIES_JSON = "sl_detailed_log_entries.json"
CM_NAME = "testcm1.testcm2"
LINEAGE_LIST_JSON = "lineage_list.json"
LINEAGE_RESPONSES_DIR = TEST_DATA_DIR / "lineage_responses"
GROUP_LIST_JSON = "group_list.json"
GROUP_MEMBERS_JSON = "group_members.json"
GROUP_RESPONSES_DIR = TEST_DATA_DIR / "group_responses"
USER_LIST_JSON = "user_list.json"
USER_GROUPS_JSON = "user_groups.json"
USER_RESPONSES_DIR = TEST_DATA_DIR / "user_responses"
AGGREGATIONS_NULL_RESPONSES_DIR = "aggregations_null_value.json"
INDEX_SEARCH_PAGING_JSON = "index_search_paging.json"
GLOSSARY_CATEGORY_BY_NAME_JSON = "glossary_category_by_name.json"
SEARCH_RESPONSES_DIR = TEST_DATA_DIR / "search_responses"
USER_LIST_JSON = "user_list.json"
GET_BY_GUID_JSON = "get_by_guid.json"
RETRIEVE_MINIMAL_JSON = "retrieve_minimal.json"
ASSET_RESPONSES_DIR = TEST_DATA_DIR / "asset_responses"
TYPEDEF_GET_BY_NAME_JSON = "get_by_name.json"
TYPEDEF_RESPONSES_DIR = TEST_DATA_DIR / "typedef_responses"

TEST_ANNOUNCEMENT = Announcement(
    announcement_title="test-title",
    announcement_message="test-msg",
    announcement_type=AnnouncementType.INFORMATION,
)
TEST_MISSING_GLOSSARY_GUID_ERROR = "ATLAN-PYTHON-400-055 'glossary_guid' keyword argument is missing for asset type: {0}"


@pytest.fixture(autouse=True)
def set_env(monkeypatch):
    monkeypatch.setenv("ATLAN_BASE_URL", "https://test.atlan.com")
    monkeypatch.setenv("ATLAN_API_KEY", "test-api-key")


@pytest.fixture()
def client():
    return AtlanClient()


@pytest.fixture
def group_client(mock_api_caller):
    return GroupClient(client=mock_api_caller)


@pytest.fixture
def mock_atlan_client():
    return Mock(AtlanClient)


@pytest.fixture(scope="module")
def mock_api_caller():
    return Mock(spec=ApiCaller)


def load_json(respones_dir, filename):
    with (respones_dir / filename).open() as input_file:
        return load(input_file)


@pytest.fixture()
def sl_most_recent_viewers_json():
    return load_json(SEARCH_LOG_RESPONSES_DIR, SL_MOST_RECENT_VIEWERS_JSON)


@pytest.fixture()
def sl_most_viewed_assets_json():
    return load_json(SEARCH_LOG_RESPONSES_DIR, SL_MOST_VIEWED_ASSETS_JSON)


@pytest.fixture()
def sl_detailed_log_entries_json():
    return load_json(SEARCH_LOG_RESPONSES_DIR, SL_DETAILED_LOG_ENTRIES_JSON)


@pytest.fixture()
def lineage_list_json():
    return load_json(LINEAGE_RESPONSES_DIR, LINEAGE_LIST_JSON)


@pytest.fixture()
def group_list_json():
    return load_json(GROUP_RESPONSES_DIR, GROUP_LIST_JSON)


@pytest.fixture()
def group_members_json():
    return load_json(GROUP_RESPONSES_DIR, GROUP_MEMBERS_JSON)


@pytest.fixture()
def user_list_json():
    return load_json(USER_RESPONSES_DIR, USER_LIST_JSON)


@pytest.fixture()
def user_groups_json():
    return load_json(USER_RESPONSES_DIR, USER_GROUPS_JSON)


@pytest.fixture()
def aggregations_null_json():
    return load_json(SEARCH_RESPONSES_DIR, AGGREGATIONS_NULL_RESPONSES_DIR)


@pytest.fixture()
def index_search_paging_json():
    return load_json(SEARCH_RESPONSES_DIR, INDEX_SEARCH_PAGING_JSON)


@pytest.fixture()
def get_by_guid_json():
    return load_json(ASSET_RESPONSES_DIR, GET_BY_GUID_JSON)


@pytest.fixture()
def retrieve_minimal_json():
    return load_json(ASSET_RESPONSES_DIR, RETRIEVE_MINIMAL_JSON)


@pytest.fixture()
def type_def_get_by_name_json():
    return load_json(TYPEDEF_RESPONSES_DIR, TYPEDEF_GET_BY_NAME_JSON)


@pytest.fixture()
def glossary_category_by_name_json():
    return load_json(SEARCH_RESPONSES_DIR, GLOSSARY_CATEGORY_BY_NAME_JSON)


@pytest.mark.parametrize(
    "guid, qualified_name, asset_type, assigned_terms, expected_message, expected_error",
    [
        (
            None,
            None,
            Table,
            [AtlasGlossaryTerm()],
            "ATLAN-PYTHON-400-043 Either qualified_name or guid should be provided.",
            InvalidRequestError,
        ),
        (
            "123",
            "default/abc",
            Table,
            [AtlasGlossaryTerm()],
            "ATLAN-PYTHON-400-042 Only qualified_name or guid should be provided but not both.",
            InvalidRequestError,
        ),
    ],
)
def test_append_terms_invalid_parameters_raises_error(
    guid, qualified_name, asset_type, assigned_terms, expected_message, expected_error
):
    client = AtlanClient()
    with pytest.raises(expected_error, match=expected_message):
        client.append_terms(
            asset_type=asset_type,
            terms=assigned_terms,
            guid=guid,
            qualified_name=qualified_name,
        )


@pytest.mark.parametrize(
    "guid, qualified_name, asset_type, assigned_terms, mock_results, expected_message, expected_error",
    [
        (
            None,
            "nonexistent_qualified_name",
            Table,
            [AtlasGlossaryTerm()],
            [],
            "ATLAN-PYTHON-404-003 Asset with qualifiedName nonexistent_qualified_name of type Table does not exist."
            " Suggestion: Verify the qualifiedName and expected type of the asset you are trying to retrieve.",
            NotFoundError,
        ),
        (
            "nonexistent_guid",
            None,
            Table,
            [AtlasGlossaryTerm()],
            [],
            "ATLAN-PYTHON-404-001 Asset with GUID nonexistent_guid does not exist."
            " Suggestion: Verify the GUID of the asset you are trying to retrieve.",
            NotFoundError,
        ),
        (
            None,
            "default/abc",
            Table,
            [AtlasGlossaryTerm()],
            ["DifferentTypeAsset"],
            "ATLAN-PYTHON-404-014 The Table asset could not be found by name: default/abc."
            " Suggestion: Verify the requested asset type and name exist in your Atlan environment.",
            NotFoundError,
        ),
        (
            "123",
            None,
            Table,
            [AtlasGlossaryTerm()],
            ["DifferentTypeAsset"],
            "ATLAN-PYTHON-404-002 Asset with GUID 123 is not of the type requested: Table."
            " Suggestion: Verify the GUID and expected type of the asset you are trying to retrieve.",
            NotFoundError,
        ),
    ],
)
@patch("pyatlan.model.fluent_search.FluentSearch.execute")
def test_append_terms_asset_retrieval_errors(
    mock_execute,
    guid,
    qualified_name,
    asset_type,
    assigned_terms,
    mock_results,
    expected_message,
    expected_error,
):
    mock_execute.return_value.current_page = lambda: mock_results
    client = AtlanClient()
    with pytest.raises(expected_error, match=expected_message):
        client.append_terms(
            asset_type=asset_type,
            terms=assigned_terms,
            guid=guid,
            qualified_name=qualified_name,
        )


def test_append_with_valid_guid_and_no_terms_returns_asset():
    asset_type = Table
    table = Table()
    table.name = "table-test"
    table.qualified_name = "table_qn"

    terms = []

    with patch("pyatlan.model.fluent_search.FluentSearch.execute") as mock_execute:
        with patch("pyatlan.client.asset.AssetClient.save") as mock_save:
            mock_execute.return_value.current_page = lambda: [table]

            mock_save.return_value.assets_updated.return_value = [table]

            client = AtlanClient()
            guid = "123"

            asset = client.asset.append_terms(
                guid=guid, asset_type=asset_type, terms=terms
            )

            assert asset == table
            assert asset.assigned_terms is None
            mock_execute.assert_called_once()
            mock_save.assert_called_once()


def test_append_with_valid_guid_when_no_terms_present_returns_asset_with_given_terms():
    asset_type = Table
    table = Table()
    table.name = "table-test"
    table.qualified_name = "table_qn"

    terms = [AtlasGlossaryTerm(qualified_name="term1")]

    with patch("pyatlan.model.fluent_search.FluentSearch.execute") as mock_execute:
        with patch("pyatlan.client.asset.AssetClient.save") as mock_save:
            mock_execute.return_value.current_page = lambda: [table]

            def mock_save_side_effect(entity):
                entity.assigned_terms = terms
                return Mock(assets_updated=lambda asset_type: [entity])

            mock_save.side_effect = mock_save_side_effect

            client = AtlanClient()
            guid = "123"
            asset = client.asset.append_terms(
                guid=guid, asset_type=asset_type, terms=terms
            )

            assert asset.assigned_terms == terms
            mock_execute.assert_called_once()
            mock_save.assert_called_once()


def test_append_with_valid_guid_when_terms_present_returns_asset_with_combined_terms():
    asset_type = Table
    table = Table()
    table.name = "table-test"
    table.qualified_name = "table_qn"

    exisiting_term = AtlasGlossaryTerm()
    table.attributes.meanings = [exisiting_term]

    new_term = AtlasGlossaryTerm(qualified_name="new_term")
    terms = [new_term]

    with patch("pyatlan.model.fluent_search.FluentSearch.execute") as mock_execute:
        with patch("pyatlan.client.asset.AssetClient.save") as mock_save:
            mock_execute.return_value.current_page = lambda: [table]

            def mock_save_side_effect(entity):
                entity.assigned_terms = table.attributes.meanings + terms
                return Mock(assets_updated=lambda asset_type: [entity])

            mock_save.side_effect = mock_save_side_effect

            client = AtlanClient()
            guid = "123"

            asset = client.asset.append_terms(
                guid=guid, asset_type=asset_type, terms=terms
            )

            updated_terms = asset.assigned_terms
            assert updated_terms is not None
            assert len(updated_terms) == 2
            assert exisiting_term in updated_terms
            assert new_term in updated_terms
            mock_execute.assert_called_once()
            mock_save.assert_called_once()


@pytest.mark.parametrize(
    "guid, qualified_name, asset_type, assigned_terms, expected_message, expected_error",
    [
        (
            None,
            None,
            Table,
            [AtlasGlossaryTerm()],
            "ATLAN-PYTHON-400-043 Either qualified_name or guid should be provided.",
            InvalidRequestError,
        ),
        (
            "123",
            "default/abc",
            Table,
            [AtlasGlossaryTerm()],
            "ATLAN-PYTHON-400-042 Only qualified_name or guid should be provided but not both.",
            InvalidRequestError,
        ),
    ],
)
def test_replace_terms_invalid_parameters_raises_error(
    guid, qualified_name, asset_type, assigned_terms, expected_message, expected_error
):
    client = AtlanClient()
    with pytest.raises(expected_error, match=expected_message):
        client.replace_terms(
            asset_type=asset_type,
            terms=assigned_terms,
            guid=guid,
            qualified_name=qualified_name,
        )


@pytest.mark.parametrize(
    "guid, qualified_name, asset_type, assigned_terms, mock_results, expected_message, expected_error",
    [
        (
            None,
            "nonexistent_qualified_name",
            Table,
            [AtlasGlossaryTerm()],
            [],
            "ATLAN-PYTHON-404-003 Asset with qualifiedName nonexistent_qualified_name of type Table does not exist."
            " Suggestion: Verify the qualifiedName and expected type of the asset you are trying to retrieve.",
            NotFoundError,
        ),
        (
            "nonexistent_guid",
            None,
            Table,
            [AtlasGlossaryTerm()],
            [],
            "ATLAN-PYTHON-404-001 Asset with GUID nonexistent_guid does not exist."
            " Suggestion: Verify the GUID of the asset you are trying to retrieve.",
            NotFoundError,
        ),
        (
            None,
            "default/abc",
            Table,
            [AtlasGlossaryTerm()],
            ["DifferentTypeAsset"],
            "ATLAN-PYTHON-404-014 The Table asset could not be found by name: default/abc."
            " Suggestion: Verify the requested asset type and name exist in your Atlan environment.",
            NotFoundError,
        ),
        (
            "123",
            None,
            Table,
            [AtlasGlossaryTerm()],
            ["DifferentTypeAsset"],
            "ATLAN-PYTHON-404-002 Asset with GUID 123 is not of the type requested: Table."
            " Suggestion: Verify the GUID and expected type of the asset you are trying to retrieve.",
            NotFoundError,
        ),
    ],
)
@patch("pyatlan.model.fluent_search.FluentSearch.execute")
def test_replace_terms_asset_retrieval_errors(
    mock_execute,
    guid,
    qualified_name,
    asset_type,
    assigned_terms,
    mock_results,
    expected_message,
    expected_error,
):
    mock_execute.return_value.current_page = lambda: mock_results
    client = AtlanClient()
    with pytest.raises(expected_error, match=expected_message):
        client.replace_terms(
            asset_type=asset_type,
            terms=assigned_terms,
            guid=guid,
            qualified_name=qualified_name,
        )


def test_replace_terms():
    asset_type = Table
    table = Table()
    table.name = "table-test"
    table.qualified_name = "table_qn"

    exisiting_term = AtlasGlossaryTerm()
    table.attributes.meanings = [exisiting_term]

    terms = [AtlasGlossaryTerm(qualified_name="new_term")]

    with patch("pyatlan.model.fluent_search.FluentSearch.execute") as mock_execute:
        with patch("pyatlan.client.asset.AssetClient.save") as mock_save:
            mock_execute.return_value.current_page = lambda: [table]

            def mock_save_side_effect(entity):
                entity.assigned_terms = terms
                return Mock(assets_updated=lambda asset_type: [entity])

            mock_save.side_effect = mock_save_side_effect

            client = AtlanClient()
            guid = "123"

            asset = client.asset.replace_terms(
                guid=guid, asset_type=asset_type, terms=terms
            )

            assert asset.assigned_terms == terms
            mock_execute.assert_called_once()
            mock_save.assert_called_once()


@pytest.mark.parametrize(
    "guid, qualified_name, asset_type, assigned_terms, expected_message, expected_error",
    [
        (
            None,
            None,
            Table,
            [AtlasGlossaryTerm()],
            "ATLAN-PYTHON-400-043 Either qualified_name or guid should be provided.",
            InvalidRequestError,
        ),
        (
            "123",
            "default/abc",
            Table,
            [AtlasGlossaryTerm()],
            "ATLAN-PYTHON-400-042 Only qualified_name or guid should be provided but not both.",
            InvalidRequestError,
        ),
    ],
)
def test_remove_terms_invalid_parameters_raises_error(
    guid, qualified_name, asset_type, assigned_terms, expected_message, expected_error
):
    client = AtlanClient()
    with pytest.raises(expected_error, match=expected_message):
        client.remove_terms(
            asset_type=asset_type,
            terms=assigned_terms,
            guid=guid,
            qualified_name=qualified_name,
        )


@pytest.mark.parametrize(
    "guid, qualified_name, asset_type, assigned_terms, mock_results, expected_message, expected_error",
    [
        (
            None,
            "nonexistent_qualified_name",
            Table,
            [AtlasGlossaryTerm()],
            [],
            "ATLAN-PYTHON-404-003 Asset with qualifiedName nonexistent_qualified_name of type Table does not exist."
            " Suggestion: Verify the qualifiedName and expected type of the asset you are trying to retrieve.",
            NotFoundError,
        ),
        (
            "nonexistent_guid",
            None,
            Table,
            [AtlasGlossaryTerm()],
            [],
            "ATLAN-PYTHON-404-001 Asset with GUID nonexistent_guid does not exist."
            " Suggestion: Verify the GUID of the asset you are trying to retrieve.",
            NotFoundError,
        ),
        (
            None,
            "default/abc",
            Table,
            [AtlasGlossaryTerm()],
            ["DifferentTypeAsset"],
            "ATLAN-PYTHON-404-014 The Table asset could not be found by name: default/abc."
            " Suggestion: Verify the requested asset type and name exist in your Atlan environment.",
            NotFoundError,
        ),
        (
            "123",
            None,
            Table,
            [AtlasGlossaryTerm()],
            ["DifferentTypeAsset"],
            "ATLAN-PYTHON-404-002 Asset with GUID 123 is not of the type requested: Table."
            " Suggestion: Verify the GUID and expected type of the asset you are trying to retrieve.",
            NotFoundError,
        ),
    ],
)
@patch("pyatlan.model.fluent_search.FluentSearch.execute")
def test_remove_terms_asset_retrieval_errors(
    mock_execute,
    guid,
    qualified_name,
    asset_type,
    assigned_terms,
    mock_results,
    expected_message,
    expected_error,
):
    mock_execute.return_value.current_page = lambda: mock_results
    client = AtlanClient()
    with pytest.raises(expected_error, match=expected_message):
        client.remove_terms(
            asset_type=asset_type,
            terms=assigned_terms,
            guid=guid,
            qualified_name=qualified_name,
        )


def test_remove_with_valid_guid_when_terms_present_returns_asset_with_terms_removed():
    asset_type = Table
    table = Table()
    table.name = "table-test"
    table.qualified_name = "table_qn"

    existing_term = AtlasGlossaryTerm(
        qualified_name="term_to_remove", guid="b4113341-251b-4adc-81fb-2420501c30e6"
    )
    other_term = AtlasGlossaryTerm(
        qualified_name="other_term", guid="b267858d-8316-4c41-a56a-6e9b840cef4a"
    )
    table.attributes.meanings = [existing_term, other_term]

    with patch("pyatlan.model.fluent_search.FluentSearch.execute") as mock_execute:
        with patch("pyatlan.client.asset.AssetClient.save") as mock_save:
            mock_execute.return_value.current_page = lambda: [table]

            def mock_save_side_effect(entity):
                entity.assigned_terms = [
                    t for t in table.attributes.meanings if t != existing_term
                ]
                return Mock(assets_updated=lambda asset_type: [entity])

            mock_save.side_effect = mock_save_side_effect

            client = AtlanClient()
            guid = "123"

            asset = client.asset.remove_terms(
                guid=guid, asset_type=asset_type, terms=[existing_term]
            )

            updated_terms = asset.assigned_terms
            assert updated_terms is not None
            assert len(updated_terms) == 1
            assert other_term in updated_terms
            mock_execute.assert_called_once()
            mock_save.assert_called_once()


@pytest.mark.parametrize(
    "name, attributes, message",
    [
        (
            1,
            None,
            "1 validation error for FindGlossaryByName\nname\n  str type expected",
        ),
        (
            None,
            None,
            "1 validation error for FindGlossaryByName\nname\n  none is not an allowed value",
        ),
        (
            "Bob",
            1,
            "1 validation error for FindGlossaryByName\nattributes\n  value is not a valid list",
        ),
        (
            " ",
            None,
            "1 validation error for FindGlossaryByName\nname\n  ensure this value has at least 1 characters",
        ),
    ],
)
def test_find_glossary_by_name_with_bad_values_raises_value_error(
    name, attributes, message, client: AtlanClient
):
    with pytest.raises(ValueError, match=message):
        client.asset.find_glossary_by_name(name=name, attributes=attributes)


@patch.object(AssetClient, "search")
def test_find_glossary_when_none_found_raises_not_found_error(mock_search):
    mock_search.return_value.count = 0

    client = AtlanClient()
    with pytest.raises(
        NotFoundError,
        match=f"The AtlasGlossary asset could not be found by name: {GLOSSARY_NAME}.",
    ):
        client.asset.find_glossary_by_name(GLOSSARY_NAME)


@patch.object(AssetClient, "search")
def test_find_glossary_when_non_glossary_found_raises_not_found_error(mock_search):
    mock_search.return_value.count = 1
    mock_search.return_value.current_page.return_value = [Table()]

    client = AtlanClient()
    with pytest.raises(
        NotFoundError,
        match=f"The AtlasGlossary asset could not be found by name: {GLOSSARY_NAME}.",
    ):
        client.asset.find_glossary_by_name(GLOSSARY_NAME)
    mock_search.return_value.current_page.assert_called_once()


@patch.object(AssetClient, "search")
def test_find_personas_by_name_when_none_found_raises_not_found_error(mock_search):
    mock_search.return_value.count = 0

    client = AtlanClient()
    with pytest.raises(
        NotFoundError,
        match=f"The Persona asset could not be found by name: {PERSONA_NAME}.",
    ):
        client.asset.find_personas_by_name(name=PERSONA_NAME)


@patch.object(AssetClient, "search")
def test_find_purposes_by_name_when_none_found_raises_not_found_error(mock_search):
    mock_search.return_value.count = 0

    client = AtlanClient()
    with pytest.raises(
        NotFoundError,
        match=f"The Purpose asset could not be found by name: {PURPOSE_NAME}.",
    ):
        client.asset.find_purposes_by_name(name=PURPOSE_NAME)


@patch.object(AssetClient, "search")
def test_find_connections_by_name_when_none_found_raises_not_found_error(mock_search):
    mock_search.return_value.count = 0

    client = AtlanClient()
    with pytest.raises(
        NotFoundError,
        match=f"The Connection asset could not be found by name: {CONNECTION_NAME}.",
    ):
        client.asset.find_connections_by_name(
            name=CONNECTION_NAME, connector_type=CONNECTOR_TYPE
        )


@patch.object(AssetClient, "search")
def test_find_glossary(mock_search, caplog):
    request = None
    attributes = ["name"]

    def get_request(*args, **kwargs):
        nonlocal request
        request = args[0]
        mock = Mock()
        mock.count = 1
        mock.current_page.return_value = [GLOSSARY, GLOSSARY]
        return mock

    mock_search.side_effect = get_request

    client = AtlanClient()

    assert GLOSSARY == client.asset.find_glossary_by_name(
        name=GLOSSARY_NAME, attributes=attributes
    )
    assert (
        f"More than 1 AtlasGlossary found with the name '{GLOSSARY_NAME}', returning only the first."
        in caplog.text
    )
    assert request
    assert request.attributes
    assert attributes == request.attributes
    assert request.dsl
    assert request.dsl.query
    assert isinstance(request.dsl.query, Bool) is True
    assert request.dsl.query.filter
    assert 3 == len(request.dsl.query.filter)
    term1, term2, term3 = request.dsl.query.filter
    assert isinstance(term1, Term) is True
    assert term1.field == "__state"
    assert term1.value == "ACTIVE"
    assert isinstance(term2, Term) is True
    assert term2.field == "__typeName.keyword"
    assert term2.value == "AtlasGlossary"
    assert isinstance(term3, Term) is True
    assert term3.field == "name.keyword"
    assert term3.value == GLOSSARY_NAME


@pytest.mark.parametrize(
    "name, glossary_qualified_name, attributes, message",
    [
        (
            1,
            GLOSSARY_QUALIFIED_NAME,
            None,
            "1 validation error for FindCategoryFastByName\nname\n  str type expected",
        ),
        (
            None,
            GLOSSARY_QUALIFIED_NAME,
            None,
            "1 validation error for FindCategoryFastByName\nname\n  none is not an allowed value",
        ),
        (
            " ",
            GLOSSARY_QUALIFIED_NAME,
            None,
            "1 validation error for FindCategoryFastByName\nname\n  ensure this value has at least 1 characters",
        ),
        (
            GLOSSARY_CATEGORY_NAME,
            None,
            None,
            "1 validation error for FindCategoryFastByName\nglossary_qualified_name\n  none is not an allowed value",
        ),
        (
            GLOSSARY_CATEGORY_NAME,
            " ",
            None,
            "1 validation error for FindCategoryFastByName\nglossary_qualified_name\n  ensure this value has at "
            "least 1 characters",
        ),
        (
            GLOSSARY_CATEGORY_NAME,
            1,
            None,
            "1 validation error for FindCategoryFastByName\nglossary_qualified_name\n  str type expected",
        ),
        (
            GLOSSARY_NAME,
            GLOSSARY_QUALIFIED_NAME,
            1,
            "1 validation error for FindCategoryFastByName\nattributes\n  value is not a valid list",
        ),
    ],
)
def test_find_category_fast_by_name_with_bad_values_raises_value_error(
    name, glossary_qualified_name, attributes, message, client: AtlanClient
):
    with pytest.raises(ValueError, match=message):
        client.asset.find_category_fast_by_name(
            name=name,
            glossary_qualified_name=glossary_qualified_name,
            attributes=attributes,
        )


@patch.object(AssetClient, "search")
def test_find_category_fast_by_name_when_none_found_raises_not_found_error(mock_search):
    mock_search.return_value.count = 0

    client = AtlanClient()
    with pytest.raises(
        NotFoundError,
        match=f"The AtlasGlossaryCategory asset could not be found by name: {GLOSSARY_CATEGORY_NAME}.",
    ):
        client.asset.find_category_fast_by_name(
            name=GLOSSARY_CATEGORY_NAME, glossary_qualified_name=GLOSSARY_QUALIFIED_NAME
        )


@patch.object(AssetClient, "search")
def test_find_category_fast_by_name_when_non_category_found_raises_not_found_error(
    mock_search,
):
    mock_search.return_value.count = 1
    mock_search.return_value.current_page.return_value = [Table()]

    client = AtlanClient()
    with pytest.raises(
        NotFoundError,
        match=f"The AtlasGlossaryCategory asset could not be found by name: {GLOSSARY_CATEGORY_NAME}.",
    ):
        client.asset.find_category_fast_by_name(
            name=GLOSSARY_CATEGORY_NAME, glossary_qualified_name=GLOSSARY_QUALIFIED_NAME
        )
    mock_search.return_value.current_page.assert_called_once()


@patch.object(AssetClient, "search")
def test_find_category_fast_by_name(mock_search, caplog):
    request = None
    attributes = ["name"]

    def get_request(*args, **kwargs):
        nonlocal request
        request = args[0]
        mock = Mock()
        mock.count = 1
        mock.current_page.return_value = [GLOSSARY_CATEGORY, GLOSSARY_CATEGORY]
        return mock

    mock_search.side_effect = get_request

    client = AtlanClient()

    assert (
        GLOSSARY_CATEGORY
        == client.asset.find_category_fast_by_name(
            name=GLOSSARY_CATEGORY_NAME,
            glossary_qualified_name=GLOSSARY_QUALIFIED_NAME,
            attributes=attributes,
        )[0]
    )
    assert request
    assert request.attributes
    assert attributes == request.attributes
    assert request.dsl
    assert request.dsl.query
    assert isinstance(request.dsl.query, Bool) is True
    assert request.dsl.query.filter
    assert 4 == len(request.dsl.query.filter)
    term1, term2, term3, term4 = request.dsl.query.filter
    assert term1.field == "__state"
    assert term1.value == "ACTIVE"
    assert isinstance(term2, Term) is True
    assert term2.field == "__typeName.keyword"
    assert term2.value == "AtlasGlossaryCategory"
    assert isinstance(term3, Term) is True
    assert term3.field == "name.keyword"
    assert term3.value == GLOSSARY_CATEGORY_NAME
    assert isinstance(term4, Term) is True
    assert term4.field == "__glossary"
    assert term4.value == GLOSSARY_QUALIFIED_NAME


@pytest.mark.parametrize(
    "name, glossary_name, attributes, message",
    [
        (
            None,
            GLOSSARY_NAME,
            None,
            "1 validation error for FindCategoryByName\nname\n  none is not an allowed value",
        ),
        (
            " ",
            GLOSSARY_NAME,
            None,
            "1 validation error for FindCategoryByName\nname\n  ensure this value has at least 1 characters",
        ),
        (
            1,
            GLOSSARY_NAME,
            None,
            "1 validation error for FindCategoryByName\nname\n  str type expected",
        ),
        (
            GLOSSARY_CATEGORY_NAME,
            None,
            None,
            "1 validation error for FindCategoryByName\nglossary_name\n  none is not an allowed value",
        ),
        (
            GLOSSARY_CATEGORY_NAME,
            " ",
            None,
            "1 validation error for FindCategoryByName\nglossary_name\n  ensure this value has at least 1 characters",
        ),
        (
            GLOSSARY_CATEGORY_NAME,
            1,
            None,
            "1 validation error for FindCategoryByName\nglossary_name\n  str type expected",
        ),
        (
            GLOSSARY_CATEGORY_NAME,
            GLOSSARY_NAME,
            1,
            "1 validation error for FindCategoryByName\nattributes\n  value is not a valid list",
        ),
    ],
)
def test_find_category_by_name_when_bad_parameter_raises_value_error(
    name, glossary_name, attributes, message, client: AtlanClient
):
    sut = client

    with pytest.raises(ValueError, match=message):
        sut.asset.find_category_by_name(
            name=name, glossary_name=glossary_name, attributes=attributes
        )


def test_find_category_by_name():
    attributes = ["name"]
    with patch.multiple(
        AssetClient, find_glossary_by_name=DEFAULT, find_category_fast_by_name=DEFAULT
    ) as values:
        mock_find_glossary_by_name = values["find_glossary_by_name"]
        mock_find_glossary_by_name.return_value.qualified_name = GLOSSARY_QUALIFIED_NAME
        mock_find_category_fast_by_name = values["find_category_fast_by_name"]

        sut = AtlanClient()

        category = sut.asset.find_category_by_name(
            name=GLOSSARY_CATEGORY_NAME,
            glossary_name=GLOSSARY_NAME,
            attributes=attributes,
        )

        mock_find_glossary_by_name.assert_called_with(name=GLOSSARY_NAME)
        mock_find_category_fast_by_name.assert_called_with(
            name=GLOSSARY_CATEGORY_NAME,
            glossary_qualified_name=GLOSSARY_QUALIFIED_NAME,
            attributes=attributes,
        )
        assert mock_find_category_fast_by_name.return_value == category


@patch.object(AssetClient, "find_glossary_by_name")
def test_find_category_by_name_qn_guid_correctly_populated(
    mock_find_glossary_by_name, mock_api_caller, glossary_category_by_name_json
):
    client = AssetClient(mock_api_caller)
    mock_find_glossary_by_name.return_value.qualified_name = GLOSSARY_QUALIFIED_NAME
    mock_api_caller._call_api.side_effect = [glossary_category_by_name_json]

    category = client.find_category_by_name(
        name="test-cat-1-1",
        glossary_name="test-glossary",
        attributes=["terms", "anchor", "parentCategory"],
    )[0]
    category_json = glossary_category_by_name_json["entities"][0]

    assert category
    assert category_json
    assert category.guid == category_json.get("guid")
    category_json_attributes = category_json.get("attributes")
    assert category_json_attributes
    assert category.name == category_json_attributes.get("name")
    assert category.qualified_name == category_json_attributes.get("qualifiedName")

    # Glossary
    assert category.anchor.guid == category_json_attributes.get("anchor").get("guid")
    assert category.anchor.name == category_json_attributes.get("anchor").get(
        "attributes"
    ).get("name")
    assert category.anchor.qualified_name == category_json_attributes.get("anchor").get(
        "uniqueAttributes"
    ).get("qualifiedName")

    # Glossary category
    assert category.parent_category.guid == category_json_attributes.get(
        "parentCategory"
    ).get("guid")
    assert category.parent_category.name == category_json_attributes.get(
        "parentCategory"
    ).get("attributes").get("name")
    assert category.parent_category.qualified_name == category_json_attributes.get(
        "parentCategory"
    ).get("uniqueAttributes").get("qualifiedName")

    # Glossary term
    assert category.terms[0].guid == category_json_attributes.get("terms")[0].get(
        "guid"
    )
    assert category.terms[0].name == category_json_attributes.get("terms")[0].get(
        "attributes"
    ).get("name")
    assert category.terms[0].qualified_name == category_json_attributes.get("terms")[
        0
    ].get("uniqueAttributes").get("qualifiedName")
    mock_api_caller.reset_mock()


@pytest.mark.parametrize(
    "name, glossary_qualified_name, attributes, message",
    [
        (
            1,
            GLOSSARY_QUALIFIED_NAME,
            None,
            "1 validation error for FindTermFastByName\nname\n  str type expected",
        ),
        (
            None,
            GLOSSARY_QUALIFIED_NAME,
            None,
            "1 validation error for FindTermFastByName\nname\n  none is not an allowed value",
        ),
        (
            " ",
            GLOSSARY_QUALIFIED_NAME,
            None,
            "1 validation error for FindTermFastByName\nname\n  ensure this value has at least 1 characters",
        ),
        (
            GLOSSARY_TERM_NAME,
            None,
            None,
            "1 validation error for FindTermFastByName\nglossary_qualified_name\n  none is not an allowed value",
        ),
        (
            GLOSSARY_TERM_NAME,
            " ",
            None,
            "1 validation error for FindTermFastByName\nglossary_qualified_name\n  ensure this value has at "
            "least 1 characters",
        ),
        (
            GLOSSARY_TERM_NAME,
            1,
            None,
            "1 validation error for FindTermFastByName\nglossary_qualified_name\n  str type expected",
        ),
        (
            GLOSSARY_TERM_NAME,
            GLOSSARY_QUALIFIED_NAME,
            1,
            "1 validation error for FindTermFastByName\nattributes\n  value is not a valid list",
        ),
    ],
)
def test_find_term_fast_by_name_with_bad_values_raises_value_error(
    name, glossary_qualified_name, attributes, message, client: AtlanClient
):
    with pytest.raises(ValueError, match=message):
        client.asset.find_term_fast_by_name(
            name=name,
            glossary_qualified_name=glossary_qualified_name,
            attributes=attributes,
        )


@patch.object(AssetClient, "search")
def test_find_term_fast_by_name_when_none_found_raises_not_found_error(mock_search):
    mock_search.return_value.count = 0

    client = AtlanClient()
    with pytest.raises(
        NotFoundError,
        match=f"The AtlasGlossaryTerm asset could not be found by name: {GLOSSARY_TERM_NAME}.",
    ):
        client.asset.find_term_fast_by_name(
            name=GLOSSARY_TERM_NAME, glossary_qualified_name=GLOSSARY_QUALIFIED_NAME
        )


@patch.object(AssetClient, "search")
def test_find_term_fast_by_name_when_non_term_found_raises_not_found_error(
    mock_search,
):
    mock_search.return_value.count = 1
    mock_search.return_value.current_page.return_value = [Table()]

    client = AtlanClient()
    with pytest.raises(
        NotFoundError,
        match=f"The AtlasGlossaryTerm asset could not be found by name: {GLOSSARY_TERM_NAME}.",
    ):
        client.asset.find_term_fast_by_name(
            name=GLOSSARY_TERM_NAME, glossary_qualified_name=GLOSSARY_QUALIFIED_NAME
        )
    mock_search.return_value.current_page.assert_called_once()


@patch.object(AssetClient, "search")
def test_find_term_fast_by_name(mock_search, caplog):
    request = None
    attributes = ["name"]

    def get_request(*args, **kwargs):
        nonlocal request
        request = args[0]
        mock = Mock()
        mock.count = 1
        mock.current_page.return_value = [GLOSSARY_TERM, GLOSSARY_TERM]
        return mock

    mock_search.side_effect = get_request

    client = AtlanClient()

    assert GLOSSARY_TERM == client.asset.find_term_fast_by_name(
        name=GLOSSARY_TERM_NAME,
        glossary_qualified_name=GLOSSARY_QUALIFIED_NAME,
        attributes=attributes,
    )
    assert (
        f"More than 1 AtlasGlossaryTerm found with the name '{GLOSSARY_TERM_NAME}', returning only the first."
        in caplog.text
    )
    assert request
    assert request.attributes
    assert attributes == request.attributes
    assert request.dsl
    assert request.dsl.query
    assert isinstance(request.dsl.query, Bool) is True
    assert request.dsl.query.filter
    assert 4 == len(request.dsl.query.filter)
    term1, term2, term3, term4 = request.dsl.query.filter
    assert term1.field == "__state"
    assert term1.value == "ACTIVE"
    assert isinstance(term2, Term) is True
    assert term2.field == "__typeName.keyword"
    assert term2.value == "AtlasGlossaryTerm"
    assert isinstance(term3, Term) is True
    assert term3.field == "name.keyword"
    assert term3.value == GLOSSARY_TERM_NAME
    assert isinstance(term4, Term) is True
    assert term4.field == "__glossary"
    assert term4.value == GLOSSARY_QUALIFIED_NAME


@pytest.mark.parametrize(
    "name, glossary_name, attributes, message",
    [
        (
            None,
            GLOSSARY_NAME,
            None,
            "1 validation error for FindTermByName\nname\n  none is not an allowed value",
        ),
        (
            " ",
            GLOSSARY_NAME,
            None,
            "1 validation error for FindTermByName\nname\n  ensure this value has at least 1 characters",
        ),
        (
            1,
            GLOSSARY_NAME,
            None,
            "1 validation error for FindTermByName\nname\n  str type expected",
        ),
        (
            GLOSSARY_TERM_NAME,
            None,
            None,
            "1 validation error for FindTermByName\nglossary_name\n  none is not an allowed value",
        ),
        (
            GLOSSARY_TERM_NAME,
            " ",
            None,
            "1 validation error for FindTermByName\nglossary_name\n  ensure this value has at least 1 characters",
        ),
        (
            GLOSSARY_TERM_NAME,
            1,
            None,
            "1 validation error for FindTermByName\nglossary_name\n  str type expected",
        ),
        (
            GLOSSARY_TERM_NAME,
            GLOSSARY_NAME,
            1,
            "1 validation error for FindTermByName\nattributes\n  value is not a valid list",
        ),
    ],
)
def test_find_term_by_name_when_bad_parameter_raises_value_error(
    name, glossary_name, attributes, message, client: AtlanClient
):
    sut = client

    with pytest.raises(ValueError, match=message):
        sut.asset.find_term_by_name(
            name=name, glossary_name=glossary_name, attributes=attributes
        )


def test_find_term_by_name():
    attributes = ["name"]
    with patch.multiple(
        AssetClient, find_glossary_by_name=DEFAULT, find_term_fast_by_name=DEFAULT
    ) as values:
        mock_find_glossary_by_name = values["find_glossary_by_name"]
        mock_find_glossary_by_name.return_value.qualified_name = GLOSSARY_QUALIFIED_NAME
        mock_find_term_fast_by_name = values["find_term_fast_by_name"]

        sut = AtlanClient()

        term = sut.asset.find_term_by_name(
            name=GLOSSARY_TERM_NAME,
            glossary_name=GLOSSARY_NAME,
            attributes=attributes,
        )

        mock_find_glossary_by_name.assert_called_with(name=GLOSSARY_NAME)
        mock_find_term_fast_by_name.assert_called_with(
            name=GLOSSARY_TERM_NAME,
            glossary_qualified_name=GLOSSARY_QUALIFIED_NAME,
            attributes=attributes,
        )
        assert mock_find_term_fast_by_name.return_value == term


@patch.object(AssetClient, "_search_for_asset_with_name")
def test_find_domain_by_name(mock_search_for_asset_with_name):
    client = AtlanClient()
    test_domain = DataDomain()
    test_domain.name = DATA_DOMAIN_NAME
    mock_search_for_asset_with_name.return_value = [test_domain]

    domain = client.asset.find_domain_by_name(
        name=DATA_DOMAIN_NAME,
        attributes=["name"],
    )

    assert domain and domain == test_domain
    assert mock_search_for_asset_with_name.call_count == 1


@patch.object(AssetClient, "_search_for_asset_with_name")
def test_find_product_by_name(mock_search_for_asset_with_name):
    client = AtlanClient()
    test_product = DataProduct()
    test_product.name = DATA_PRODUCT_NAME
    mock_search_for_asset_with_name.return_value = [test_product]

    product = client.asset.find_product_by_name(
        name=DATA_PRODUCT_NAME,
        attributes=["name"],
    )

    assert product and product == test_product
    assert mock_search_for_asset_with_name.call_count == 1


@patch.object(SearchLogClient, "_call_search_api")
def test_search_log_most_recent_viewers(mock_sl_api_call, sl_most_recent_viewers_json):
    client = AtlanClient()
    mock_sl_api_call.return_value = sl_most_recent_viewers_json
    recent_viewers_aggs = sl_most_recent_viewers_json["aggregations"]
    recent_viewers_aggs_buckets = recent_viewers_aggs[UNIQUE_USERS]["buckets"]
    request = SearchLogRequest.most_recent_viewers(
        guid="test-guid-123", exclude_users=["testuser"]
    )
    request_dsl_json = loads(request.dsl.json(by_alias=True, exclude_none=True))
    response = client.search_log.search(request)
    viewers = response.user_views
    assert len(viewers) == 3
    assert response.asset_views is None
    assert request_dsl_json == sl_most_recent_viewers_json[SEARCH_PARAMS]["dsl"]
    assert response.count == sl_most_recent_viewers_json[SEARCH_COUNT]
    assert viewers[0].username == recent_viewers_aggs_buckets[0]["key"]
    assert viewers[0].view_count == recent_viewers_aggs_buckets[0]["doc_count"]
    assert viewers[0].most_recent_view
    assert viewers[1].username == recent_viewers_aggs_buckets[1]["key"]
    assert viewers[1].view_count == recent_viewers_aggs_buckets[1]["doc_count"]
    assert viewers[1].most_recent_view


@patch.object(SearchLogClient, "_call_search_api")
def test_search_log_most_viewed_assets(mock_sl_api_call, sl_most_viewed_assets_json):
    client = AtlanClient()
    mock_sl_api_call.return_value = sl_most_viewed_assets_json
    viewed_assets_aggs = sl_most_viewed_assets_json["aggregations"]
    viewed_assets_aggs_buckets = viewed_assets_aggs[UNIQUE_ASSETS]["buckets"][0]
    request = SearchLogRequest.most_viewed_assets(
        max_assets=10, exclude_users=["testuser"]
    )
    request_dsl_json = loads(request.dsl.json(by_alias=True, exclude_none=True))
    response = client.search_log.search(request)
    detail = response.asset_views
    assert len(detail) == 8
    assert response.user_views is None
    assert request_dsl_json == sl_most_viewed_assets_json[SEARCH_PARAMS]["dsl"]
    assert response.count == sl_most_viewed_assets_json[SEARCH_COUNT]
    assert detail[0].guid == viewed_assets_aggs_buckets["key"]
    assert detail[0].total_views == viewed_assets_aggs_buckets["doc_count"]
    assert detail[0].distinct_users == viewed_assets_aggs_buckets[UNIQUE_USERS]["value"]


@patch.object(SearchLogClient, "_call_search_api")
def test_search_log_views_by_guid(mock_sl_api_call, sl_detailed_log_entries_json):
    client = AtlanClient()
    mock_sl_api_call.return_value = sl_detailed_log_entries_json
    sl_detailed_log_entries = sl_detailed_log_entries_json["logs"]
    request = SearchLogRequest.views_by_guid(
        guid="test-guid-123", size=10, exclude_users=["testuser"]
    )
    request_dsl_json = loads(request.dsl.json(by_alias=True, exclude_none=True))
    response = client.search_log.search(request)
    log_entries = response.current_page()
    assert request_dsl_json == sl_detailed_log_entries_json[SEARCH_PARAMS]["dsl"]
    assert len(response.current_page()) == sl_detailed_log_entries_json[SEARCH_COUNT]
    assert log_entries[0].user_name == sl_detailed_log_entries[0][LOG_USERNAME]
    assert log_entries[0].ip_address == sl_detailed_log_entries[0][LOG_IP_ADDRESS]
    assert log_entries[0].host
    assert log_entries[0].user_agent
    assert log_entries[0].utm_tags
    assert log_entries[0].entity_guids_all
    assert log_entries[0].entity_guids_allowed
    assert log_entries[0].entity_qf_names_all
    assert log_entries[0].entity_qf_names_allowed
    assert log_entries[0].entity_type_names_all
    assert log_entries[0].entity_type_names_allowed
    assert log_entries[0].has_result
    assert log_entries[0].results_count
    assert log_entries[0].response_time
    assert log_entries[0].created_at
    assert log_entries[0].timestamp
    assert log_entries[0].failed is False
    assert log_entries[0].request_dsl
    assert log_entries[0].request_dsl_text
    assert log_entries[0].request_attributes is None
    assert log_entries[0].request_relation_attributes


def test_asset_get_lineage_list_response_with_custom_metadata(
    mock_api_caller, lineage_list_json
):
    asset_client = AssetClient(mock_api_caller)
    mock_api_caller._call_api.side_effect = [lineage_list_json, {}]

    lineage_request = LineageListRequest(
        guid="test-guid", depth=1, direction=LineageDirection.UPSTREAM
    )
    lineage_request.attributes = [CM_NAME]
    lineage_response = asset_client.get_lineage_list(lineage_request=lineage_request)

    for asset in lineage_response:
        assert asset
        assert asset.depth == 1
        assert asset.type_name == "View"
        assert asset.guid == "test-guid"
        assert asset.qualified_name == "test-qn"
        assert asset.attributes
        assert asset.business_attributes
        assert asset.business_attributes == {"testcm1": {"testcm2": "test-cm-value"}}

    assert mock_api_caller._call_api.call_count == 1
    mock_api_caller.reset_mock()


def test_group_get_pagination(mock_api_caller, group_list_json):
    client = GroupClient(mock_api_caller)
    last_page_response = {"totalRecord": 3, "filterRecord": 3, "records": None}
    mock_api_caller._call_api.side_effect = [group_list_json, last_page_response]
    response = client.get()

    assert response
    assert len(response.current_page()) == 2
    for group in response:
        assert group.name
        assert group.path
        assert group.personas
    assert len(response.current_page()) == 0
    assert mock_api_caller._call_api.call_count == 2
    mock_api_caller.reset_mock()


def test_group_get_members_pagination(mock_api_caller, group_members_json):
    client = GroupClient(mock_api_caller)
    last_page_response = {"totalRecord": 3, "filterRecord": 3, "records": None}
    mock_api_caller._call_api.side_effect = [group_members_json, last_page_response]
    response = client.get_members(guid="test-guid", request=UserRequest())

    assert response
    assert len(response.current_page()) == 3
    for user in response:
        assert user.username
        assert user.email
        assert user.attributes
    assert len(response.current_page()) == 0
    assert mock_api_caller._call_api.call_count == 2
    mock_api_caller.reset_mock()


def test_user_list_pagination(mock_api_caller, user_list_json):
    client = UserClient(mock_api_caller)
    last_page_response = {"totalRecord": 3, "filterRecord": 3, "records": None}
    mock_api_caller._call_api.side_effect = [user_list_json, last_page_response]
    response = client.get()

    assert response
    assert len(response.current_page()) == 3
    for user in response:
        assert user.username
        assert user.email
        assert user.attributes
        assert user.login_events
    assert len(response.current_page()) == 0
    assert mock_api_caller._call_api.call_count == 2
    mock_api_caller.reset_mock()


def test_user_groups_pagination(mock_api_caller, user_groups_json):
    client = UserClient(mock_api_caller)
    last_page_response = {"totalRecord": 2, "filterRecord": 2, "records": None}
    mock_api_caller._call_api.side_effect = [user_groups_json, last_page_response]
    response = client.get_groups(guid="test-guid", request=GroupRequest())

    assert response
    assert len(response.current_page()) == 2
    for group in response:
        assert group.name
        assert group.path
        assert group.alias
        assert group.attributes
    assert len(response.current_page()) == 0
    assert mock_api_caller._call_api.call_count == 2
    mock_api_caller.reset_mock()


def test_index_search_with_no_aggregation_results(
    mock_api_caller, aggregations_null_json
):
    client = AssetClient(mock_api_caller)
    mock_api_caller._call_api.side_effect = [aggregations_null_json]
    request = (
        FluentSearch(
            aggregations={"test1": {"test2": {"field": "__test_field"}}}
        ).where(Column.QUALIFIED_NAME.startswith("test-qn"))
    ).to_request()
    response = client.search(criteria=request)
    assert response
    assert response.count == 0
    assert response.aggregations is None
    mock_api_caller.reset_mock()


def test_type_name_in_asset_search_bool_filter(mock_api_caller):
    # When the type name is not present in the request
    request = (FluentSearch().where(CompoundQuery.active_assets())).to_request()
    client = AssetClient(mock_api_caller)
    client._ensure_type_filter_present(request)

    assert request.dsl.query and request.dsl.query.filter
    assert isinstance(request.dsl.query.filter, list)

    has_type_filter = any(
        isinstance(f, Term) and f.field == TermAttributes.SUPER_TYPE_NAMES.value
        for f in request.dsl.query.filter
    )
    assert has_type_filter is True

    # When the type name is present in the request (no need to add super type filter)
    request = (
        FluentSearch()
        .where(CompoundQuery.active_assets())
        .where(CompoundQuery.asset_type(AtlasGlossary))
    ).to_request()
    client._ensure_type_filter_present(request)

    assert request.dsl.query and request.dsl.query.filter
    assert isinstance(request.dsl.query.filter, list)

    has_type_filter = any(
        isinstance(f, Term) and f.field == TermAttributes.SUPER_TYPE_NAMES.value
        for f in request.dsl.query.filter
    )
    assert has_type_filter is False

    # When multiple type name(s) is present in the request (no need to add super type filter)
    request = (
        FluentSearch()
        .where(CompoundQuery.active_assets())
        .where(CompoundQuery.asset_types([AtlasGlossary, AtlasGlossaryTerm]))
    ).to_request()
    client._ensure_type_filter_present(request)

    assert request.dsl.query and request.dsl.query.filter
    assert isinstance(request.dsl.query.filter, list)

    has_type_filter = any(
        isinstance(f, Term) and f.field == TermAttributes.SUPER_TYPE_NAMES.value
        for f in request.dsl.query.filter
    )
    assert has_type_filter is False


def test_type_name_in_asset_search_bool_must(mock_api_caller):
    # When the type name is not present in the request
    query = Bool(must=[Term.with_state("ACTIVE")])
    request = IndexSearchRequest(dsl=DSL(query=query))

    client = AssetClient(mock_api_caller)
    client._ensure_type_filter_present(request)

    assert request.dsl.query and request.dsl.query.must
    assert isinstance(request.dsl.query.must, list)

    has_type_filter = any(
        isinstance(f, Term) and f.field == TermAttributes.SUPER_TYPE_NAMES.value
        for f in request.dsl.query.must
    )
    assert has_type_filter is True

    # When the type name is present in the request (no need to add super type filter)
    query = Bool(must=[Term.with_state("ACTIVE"), Term.with_type_name("AtlasGlossary")])
    request = IndexSearchRequest(dsl=DSL(query=query))
    client._ensure_type_filter_present(request)

    assert request.dsl.query and request.dsl.query.must
    assert isinstance(request.dsl.query.must, list)

    has_type_filter = any(
        isinstance(f, Term) and f.field == TermAttributes.SUPER_TYPE_NAMES.value
        for f in request.dsl.query.must
    )
    assert has_type_filter is False

    # When multiple type name(s) is present in the request (no need to add super type filter)
    query = Bool(
        must=[
            Term.with_state("ACTIVE"),
            Term.with_type_name("AtlasGlossary"),
            Term.with_type_name("AtlasGlossaryTerm"),
        ]
    )
    request = IndexSearchRequest(dsl=DSL(query=query))
    client._ensure_type_filter_present(request)

    assert request.dsl.query and request.dsl.query.must
    assert isinstance(request.dsl.query.must, list)

    has_type_filter = any(
        isinstance(f, Term) and f.field == TermAttributes.SUPER_TYPE_NAMES.value
        for f in request.dsl.query.must
    )
    assert has_type_filter is False


def _assert_search_results(results, response_json, sorts, bulk=False):
    for i, result in enumerate(results):
        assert result and response_json["entities"][i]
        assert result.guid == response_json["entities"][i]["guid"]

    assert results
    assert results.count == 2
    assert results._bulk == bulk
    assert results.aggregations is None
    assert results._criteria.dsl.sort == sorts


@patch.object(LOGGER, "debug")
def test_index_search_pagination(
    mock_logger, mock_api_caller, index_search_paging_json
):
    client = AssetClient(mock_api_caller)
    mock_api_caller._call_api.side_effect = [index_search_paging_json, {}]

    # Test search(): using default offset-based pagination
    # when results are less than the predefined threshold (i.e: 100,000 assets)
    request = (
        FluentSearch()
        .where(CompoundQuery.active_assets())
        .where(CompoundQuery.asset_type(AtlasGlossaryTerm))
        .page_size(2)
    ).to_request()
    results = client.search(criteria=request)
    expected_sorts = [Asset.GUID.order(SortOrder.ASCENDING)]

    _assert_search_results(results, index_search_paging_json, expected_sorts)
    assert mock_api_caller._call_api.call_count == 2
    mock_api_caller.reset_mock()

    # Test search(): with `bulk` option using timestamp-based pagination
    mock_api_caller._call_api.side_effect = [index_search_paging_json, {}]
    request = (
        FluentSearch()
        .where(CompoundQuery.active_assets())
        .where(CompoundQuery.asset_type(AtlasGlossaryTerm))
        .page_size(2)
    ).to_request()
    results = client.search(criteria=request, bulk=True)
    expected_sorts = [
        Asset.CREATE_TIME.order(SortOrder.ASCENDING),
        Asset.GUID.order(SortOrder.ASCENDING),
    ]

    _assert_search_results(results, index_search_paging_json, expected_sorts, True)
    assert mock_api_caller._call_api.call_count == 2
    assert mock_logger.call_count == 1
    assert "Bulk search option is enabled." in mock_logger.call_args_list[0][0][0]
    mock_logger.reset_mock()
    mock_api_caller.reset_mock()

    # Test search(): when the number of results exceeds the predefined threshold
    # it will automatically convert to a `bulk` search.
    TEST_THRESHOLD = 1
    with patch.object(IndexSearchResults, "_MASS_EXTRACT_THRESHOLD", TEST_THRESHOLD):
        mock_api_caller._call_api.side_effect = [
            index_search_paging_json,
            # Extra call to re-fetch the first page
            # results with updated timestamp sorting
            index_search_paging_json,
            {},
        ]
        request = (
            FluentSearch()
            .where(CompoundQuery.active_assets())
            .where(CompoundQuery.asset_type(AtlasGlossaryTerm))
            .page_size(2)
        ).to_request()
        results = client.search(criteria=request)
        expected_sorts = [
            Asset.CREATE_TIME.order(SortOrder.ASCENDING),
            Asset.GUID.order(SortOrder.ASCENDING),
        ]
        _assert_search_results(results, index_search_paging_json, expected_sorts)
        assert mock_api_caller._call_api.call_count == 3
        assert mock_logger.call_count == 1
        assert (
            "Result size (%s) exceeds threshold (%s)"
            in mock_logger.call_args_list[0][0][0]
        )
    mock_logger.reset_mock()
    mock_api_caller.reset_mock()

    # Test search(bulk=False): Raise an exception when the number of results exceeds
    # the predefined threshold and there are any user-defined sorting options present
    with patch.object(IndexSearchResults, "_MASS_EXTRACT_THRESHOLD", TEST_THRESHOLD):
        mock_api_caller._call_api.side_effect = [
            index_search_paging_json,
        ]
        request = (
            FluentSearch()
            .where(CompoundQuery.active_assets())
            .where(CompoundQuery.asset_type(AtlasGlossaryTerm))
            .page_size(2)
            # With some sort options
            .sort(Asset.NAME.order(SortOrder.ASCENDING))
        ).to_request()

        with pytest.raises(
            InvalidRequestError,
            match=(
                "ATLAN-PYTHON-400-063 Unable to execute "
                "bulk search with user-defined sorting options. "
                "Suggestion: Please ensure that no sorting options are "
                "included in your search request when performing a bulk search."
            ),
        ):
            client.search(criteria=request)
            assert mock_api_caller._call_api.call_count == 1
    mock_api_caller.reset_mock()
    mock_api_caller.reset_mock()

    # Test search(bulk=True): Raise an exception when bulk search is enabled
    # and there are any user-defined sorting options present
    request = (
        FluentSearch()
        .where(CompoundQuery.active_assets())
        .where(CompoundQuery.asset_type(AtlasGlossaryTerm))
        .page_size(2)
        .sort(Asset.NAME.order(SortOrder.ASCENDING))
    ).to_request()

    with pytest.raises(
        InvalidRequestError,
        match=(
            "ATLAN-PYTHON-400-063 Unable to execute "
            "bulk search with user-defined sorting options. "
            "Suggestion: Please ensure that no sorting options are "
            "included in your search request when performing a bulk search."
        ),
    ):
        client.search(criteria=request, bulk=True)


def test_asset_get_by_guid_without_asset_type(mock_api_caller, get_by_guid_json):
    client = AssetClient(mock_api_caller)
    mock_api_caller._call_api.side_effect = [get_by_guid_json]

    response = client.get_by_guid(
        guid="test-table-guid-123", ignore_relationships=False
    )

    assert response
    assert isinstance(response, Table)
    assert response.guid
    assert response.qualified_name
    assert response.attributes
    mock_api_caller.reset_mock()


def test_asset_retrieve_minimal_without_asset_type(
    mock_api_caller, retrieve_minimal_json
):
    client = AssetClient(mock_api_caller)
    mock_api_caller._call_api.side_effect = [retrieve_minimal_json]

    response = client.retrieve_minimal(guid="test-table-guid-123")

    assert response
    assert isinstance(response, Table)
    assert response.guid
    assert response.qualified_name
    assert response.attributes
    mock_api_caller.reset_mock()


def test_user_create(
    mock_api_caller,
    mock_role_cache,
):
    test_role_id = "role-guid-123"
    client = UserClient(mock_api_caller)
    client._client.role_cache = mock_role_cache
    mock_api_caller._call_api.side_effect = [None]
    mock_role_cache.get_id_for_name.return_value = test_role_id

    test_users = [AtlanUser.create(email="test@test.com", role_name="$member")]
    response = client.create(users=test_users)

    assert response is None
    mock_api_call_args = mock_api_caller._call_api.call_args_list
    user = mock_api_call_args[0].kwargs.get("request_obj").dict().get("users")[0]
    assert len(mock_api_call_args) == 1
    assert user.get("role_id") == test_role_id
    assert user.get("email") == test_users[0].email
    assert user.get("role_name") == test_users[0].workspace_role
    mock_api_caller.reset_mock()


def test_user_create_with_info(mock_api_caller, mock_role_cache, user_list_json):
    test_role_id = "role-guid-123"
    client = UserClient(mock_api_caller)
    mock_api_caller._call_api.side_effect = [
        None,
        {
            "totalRecord": 3,
            "filterRecord": 1,
            "records": [user_list_json["records"][0]],
        },
    ]
    mock_role_cache.get_id_for_name.return_value = test_role_id
    test_users = [AtlanUser.create(email="test@test.com", role_name="$member")]
    response = client.create(users=test_users, return_info=True)

    assert len(response.current_page()) == 1
    user = response.current_page()[0]
    assert user
    assert user.username
    assert user.email
    assert user.attributes
    assert user.login_events
    assert mock_api_caller._call_api.call_count == 2
    mock_api_caller.reset_mock()


def test_typedef_get_by_name(mock_api_caller, type_def_get_by_name_json):
    client = TypeDefClient(mock_api_caller)
    mock_api_caller._call_api.side_effect = [type_def_get_by_name_json]
    response = client.get_by_name(name="test-enum")
    assert response == EnumDef(**type_def_get_by_name_json)
    assert mock_api_caller._call_api.call_count == 1
    mock_api_caller.reset_mock()


def test_typedef_get_by_name_unsupported_category(mock_api_caller):
    client = TypeDefClient(mock_api_caller)
    mock_api_caller._call_api.side_effect = [{"category": "TEST"}]
    with pytest.raises(ApiError) as err:
        client.get_by_name(name="test-enum")

    assert "Unsupported type definition category: TEST" in str(err.value)
    mock_api_caller.reset_mock()


def test_typedef_get_by_name_invalid_response(mock_api_caller):
    client = TypeDefClient(mock_api_caller)
    mock_api_caller._call_api.side_effect = [123]
    with pytest.raises(ApiError) as err:
        client.get_by_name(name="test-enum")
    assert "Additional details: 'int' object has no attribute 'get'" in str(err.value)

    mock_api_caller._call_api.side_effect = [{"category": "ENUM", "test": "invalid"}]
    with pytest.raises(ApiError) as err:
        client.get_by_name(name="test-enum")
    assert "1 validation error for EnumDef\nelementDefs\n  field required" in str(
        err.value
    )
    mock_api_caller.reset_mock()


@pytest.mark.parametrize(
    "test_method, test_kwargs, test_asset_types",
    [
        [
            "update_certificate",
            {
                "qualified_name": "test-qn",
                "name": "test-name",
                "certificate_status": CertificateStatus.VERIFIED,
                "message": "test-message",
            },
            [AtlasGlossaryTerm, AtlasGlossaryCategory],
        ],
        [
            "remove_certificate",
            {
                "qualified_name": "test-qn",
                "name": "test-name",
            },
            [AtlasGlossaryTerm, AtlasGlossaryCategory],
        ],
        [
            "update_announcement",
            {
                "qualified_name": "test-qn",
                "name": "test-name",
                "announcement": TEST_ANNOUNCEMENT,
            },
            [AtlasGlossaryTerm, AtlasGlossaryCategory],
        ],
        [
            "remove_announcement",
            {"qualified_name": "test-qn", "name": "test-name"},
            [AtlasGlossaryTerm, AtlasGlossaryCategory],
        ],
    ],
)
def test_asset_client_missing_glossary_guid_raises_invalid_request_error(
    test_method: str,
    test_kwargs: dict,
    test_asset_types,
):
    client = AtlanClient()
    asset_client_method = getattr(client.asset, test_method)

    for asset_type in test_asset_types:
        test_error = TEST_MISSING_GLOSSARY_GUID_ERROR.format(asset_type.__name__)
        with pytest.raises(InvalidRequestError, match=test_error):
            asset_client_method(**test_kwargs, asset_type=asset_type)


@pytest.mark.parametrize("method, params", TEST_ASSET_CLIENT_METHODS.items())
def test_asset_client_methods_validation_error(client, method, params):
    client_method = getattr(client.asset, method)
    for param_values, error_msg in params:
        with pytest.raises(ValidationError) as err:
            client_method(*param_values)
        assert error_msg in str(err.value)


@pytest.mark.parametrize("method, params", TEST_ADMIN_CLIENT_METHODS.items())
def test_admin_client_methods_validation_error(client, method, params):
    client_method = getattr(client.admin, method)
    for param_values, error_msg in params:
        with pytest.raises(ValidationError) as err:
            client_method(*param_values)
        assert error_msg in str(err.value)


@pytest.mark.parametrize("method, params", TEST_AUDIT_CLIENT_METHODS.items())
def test_audit_client_methods_validation_error(client, method, params):
    client_method = getattr(client.audit, method)
    for param_values, error_msg in params:
        with pytest.raises(ValidationError) as err:
            client_method(*param_values)
        assert error_msg in str(err.value)


@pytest.mark.parametrize("method, params", TEST_GROUP_CLIENT_METHODS.items())
def test_group_client_methods_validation_error(client, method, params):
    client_method = getattr(client.group, method)
    for param_values, error_msg in params:
        with pytest.raises(ValidationError) as err:
            client_method(*param_values)
        assert error_msg in str(err.value)


@pytest.mark.parametrize("method, params", TEST_ROLE_CLIENT_METHODS.items())
def test_role_client_methods_validation_error(client, method, params):
    client_method = getattr(client.role, method)
    for param_values, error_msg in params:
        with pytest.raises(ValidationError) as err:
            client_method(*param_values)
        assert error_msg in str(err.value)


@pytest.mark.parametrize("method, params", TEST_SL_CLIENT_METHODS.items())
def test_search_log_client_methods_validation_error(client, method, params):
    client_method = getattr(client.search_log, method)
    for param_values, error_msg in params:
        with pytest.raises(ValidationError) as err:
            client_method(*param_values)
        assert error_msg in str(err.value)


@pytest.mark.parametrize("method, params", TEST_TOKEN_CLIENT_METHODS.items())
def test_token_client_methods_validation_error(client, method, params):
    client_method = getattr(client.token, method)
    for param_values, error_msg in params:
        with pytest.raises(ValidationError) as err:
            client_method(*param_values)
        assert error_msg in str(err.value)


@pytest.mark.parametrize("method, params", TEST_TYPEDEF_CLIENT_METHODS.items())
def test_typedef_client_methods_validation_error(client, method, params):
    client_method = getattr(client.typedef, method)
    for param_values, error_msg in params:
        with pytest.raises(ValidationError) as err:
            client_method(*param_values)
        assert error_msg in str(err.value)


@pytest.mark.parametrize("method, params", TEST_USER_CLIENT_METHODS.items())
def test_user_client_methods_validation_error(client, method, params):
    client_method = getattr(client.user, method)
    for param_values, error_msg in params:
        with pytest.raises(ValidationError) as err:
            client_method(*param_values)
        assert error_msg in str(err.value)


@pytest.mark.parametrize(
    "test_error_msg",
    [
        "{'error': 123}",
        "{'error': 123, 'code': 465}",
        "{'error': 123} with text",
        "Some error message...",
        "With unescape curly braces -> {'{}'}",
    ],
)
@patch.object(AtlanClient, "_session")
def test_atlan_call_api_server_error_messages(
    mock_session,
    client: AtlanClient,
    test_error_msg,
):
    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.text = test_error_msg
    mock_session.request.return_value = mock_response
    glossary = AtlasGlossary.creator(name="test-glossary")

    with pytest.raises(
        AtlanError,
        match=(
            f"ATLAN-PYTHON-500-000 {test_error_msg} "
            "Suggestion: Check the details of the "
            "server's message to correct your request."
        ),
    ):
        client.asset.save(glossary)


@pytest.mark.parametrize(
    "test_error_msg",
    [
        """
    {
        "errorCode": 1234,
        "errorMessage": "something went wrong",
        "causes": [
            {
                "errorType": "testException",
                "errorMessage": "test error message",
                "location": "Test.Class.TestException"
            }
        ],
        "errorCause": "something went wrong",
        "errorId": "95d80a45999cabc",
        "doc": "https://ask.atlan.com/hc/en-us/articles/6645223434141-Is-there-a-limit-on-the-number-of-API-requests-that-can-be-performed"
    }
    """
    ],
)
@patch.object(AtlanClient, "_session")
def test_atlan_call_api_server_error_messages_with_causes(
    mock_session,
    client: AtlanClient,
    test_error_msg,
):
    ERROR_CODE_FOR_HTTP_STATUS.update(
        {ErrorCode.ERROR_PASSTHROUGH.http_error_code: ErrorCode.ERROR_PASSTHROUGH}
    )
    STATUS_CODES = set(ERROR_CODE_FOR_HTTP_STATUS.keys())
    # For "NOT_FOUND (404)" errors, no error cause is returned by the backend,
    # so we'll exclude that from the test cases:
    STATUS_CODES.remove(ErrorCode.NOT_FOUND_PASSTHROUGH.http_error_code)

    for code in STATUS_CODES:
        error = ERROR_CODE_FOR_HTTP_STATUS.get(code)
        mock_response = Mock()
        mock_response.status_code = code
        mock_response.text = test_error_msg
        mock_session.request.return_value = mock_response
        test_error = loads(test_error_msg)
        error_code = test_error.get("errorCode")
        error_message = test_error.get("errorMessage")
        error_cause = test_error.get("errorCause")
        error_doc = test_error.get("doc")
        error_id = test_error.get("errorId")
        error_causes = test_error.get("causes")[0]
        glossary = AtlasGlossary.creator(name="test-glossary")
        error_causes = "ErrorType: testException, Message: test error message, Location: Test.Class.TestException"
        assert error and error_code and error_message and error_cause and error_causes
        error_info = error.exception_with_parameters(
            error_code,
            error_message,
            error_causes,
            error_cause=error_cause,
            backend_error_id=error_id,
            error_doc=error_doc,
        )

        with pytest.raises(
            AtlanError,
            match=escape(str(error_info)),
        ):
            client.asset.save(glossary)


class TestBatch:
    def test_init(self, mock_atlan_client):
        sut = Batch(client=mock_atlan_client, max_size=10)

        self.assert_asset_client_not_called(mock_atlan_client, sut)

    def assert_asset_client_not_called(self, mock_atlan_client, sut):
        assert 0 == len(sut.created)
        assert 0 == len(sut.updated)
        assert 0 == len(sut.failures)
        mock_atlan_client.assert_not_called()

    @pytest.mark.parametrize(
        "custom_metadata_handling",
        [
            (CustomMetadataHandling.IGNORE),
            (CustomMetadataHandling.OVERWRITE),
            (CustomMetadataHandling.MERGE),
        ],
    )
    def test_add_when_capture_failure_true(
        self, custom_metadata_handling, mock_atlan_client
    ):
        table_1 = Mock(Table(guid="t1"))
        table_2 = Mock(Table(guid="t2"))
        table_3 = Mock(Table(guid="t3"))
        table_4 = Mock(Table(guid="t4"))
        mock_response = Mock(spec=AssetMutationResponse)
        mutated_entities = Mock()
        created = [table_1]
        updated = [table_2]
        mutated_entities.CREATE = created
        mutated_entities.UPDATE = updated
        mock_response.guid_assignments = {}
        mock_response.attach_mock(mutated_entities, "mutated_entities")

        if custom_metadata_handling == CustomMetadataHandling.IGNORE:
            mock_atlan_client.asset.save.return_value = mock_response
        elif custom_metadata_handling == CustomMetadataHandling.OVERWRITE:
            mock_atlan_client.asset.save_replacing_cm.return_value = mock_response
        else:
            mock_atlan_client.asset.save_merging_cm.return_value = mock_response

        sut = Batch(
            client=mock_atlan_client,
            max_size=2,
            capture_failures=True,
            custom_metadata_handling=custom_metadata_handling,
        )
        sut.add(table_1)
        self.assert_asset_client_not_called(mock_atlan_client, sut)

        sut.add(table_2)

        assert len(created) == sut.num_created
        assert len(updated) == sut.num_updated
        for unsaved, saved in zip(created, sut.created):
            unsaved.trim_to_required.assert_called_once()
            assert unsaved.name == saved.name
        for unsaved, saved in zip(updated, sut.updated):
            unsaved.trim_to_required.assert_called_once()
            assert unsaved.name == saved.name

        exception = ErrorCode.INVALID_REQUEST_PASSTHROUGH.exception_with_parameters(
            "bad", "stuff", ""
        )
        if custom_metadata_handling == CustomMetadataHandling.IGNORE:
            mock_atlan_client.asset.save.side_effect = exception
        elif custom_metadata_handling == CustomMetadataHandling.OVERWRITE:
            mock_atlan_client.asset.save_replacing_cm.side_effect = exception
        else:
            mock_atlan_client.asset.save_merging_cm.side_effect = exception

        sut.add(table_3)

        sut.add(table_4)

        assert 1 == len(sut.failures)
        failure = sut.failures[0]
        assert [table_3, table_4] == failure.failed_assets
        assert exception == failure.failure_reason
        if custom_metadata_handling == CustomMetadataHandling.IGNORE:
            mock_atlan_client.asset.save.assert_has_calls(
                [
                    call([table_1, table_2], replace_atlan_tags=False),
                    call([table_3, table_4], replace_atlan_tags=False),
                ]
            )
        elif custom_metadata_handling == CustomMetadataHandling.OVERWRITE:
            mock_atlan_client.asset.save_replacing_cm.assert_has_calls(
                [
                    call([table_1, table_2], replace_atlan_tags=False),
                    call([table_3, table_4], replace_atlan_tags=False),
                ]
            )
        else:
            mock_atlan_client.asset.save_merging_cm.assert_has_calls(
                [
                    call([table_1, table_2], replace_atlan_tags=False),
                    call([table_3, table_4], replace_atlan_tags=False),
                ]
            )

    @pytest.mark.parametrize(
        "custom_metadata_handling",
        [
            (CustomMetadataHandling.IGNORE),
            (CustomMetadataHandling.OVERWRITE),
            (CustomMetadataHandling.MERGE),
        ],
    )
    def test_add_when_capture_failure_false_then_exception_raised(
        self, custom_metadata_handling, mock_atlan_client
    ):
        exception = ErrorCode.INVALID_REQUEST_PASSTHROUGH.exception_with_parameters(
            "bad", "stuff", ""
        )
        if custom_metadata_handling == CustomMetadataHandling.IGNORE:
            mock_atlan_client.asset.save.side_effect = exception
        elif custom_metadata_handling == CustomMetadataHandling.OVERWRITE:
            mock_atlan_client.asset.save_replacing_cm.side_effect = exception
        else:
            mock_atlan_client.asset.save_merging_cm.side_effect = exception

        sut = Batch(
            client=mock_atlan_client,
            max_size=1,
            capture_failures=False,
            custom_metadata_handling=custom_metadata_handling,
        )
        with pytest.raises(AtlanError):
            sut.add(Mock(Table))

        assert 0 == len(sut.failures)
        assert 0 == len(sut.created)
        assert 0 == len(sut.updated)

    @patch.object(AtlasGlossaryTerm, "trim_to_required")
    @patch.object(AtlasGlossaryTerm, "ref_by_guid")
    def test_term_add(self, mock_ref_by_guid, mock_trim_to_required, mock_atlan_client):
        mutated_entities = Mock()
        mock_response = Mock(spec=AssetMutationResponse)
        term_1 = AtlasGlossaryTerm(guid="test-guid1")
        term_2 = AtlasGlossaryTerm(guid="test-guid2")
        created = [term_1, term_2]
        mutated_entities.UPDATE = []
        mutated_entities.CREATE = created
        mock_response.guid_assignments = {}
        mock_response.attach_mock(mutated_entities, "mutated_entities")
        mock_atlan_client.asset.search.return_value = [term_1]
        mock_atlan_client.asset.save.return_value = mock_response
        batch = Batch(
            client=mock_atlan_client,
            max_size=2,
            track=True,
        )
        batch.add(term_1)
        # Because the batch is not yet full
        self.assert_asset_client_not_called(mock_atlan_client, batch)
        batch.add(term_2)

        assert len(created) == batch.num_created
        mock_ref_by_guid.assert_has_calls([call(term_1.guid), call(term_2.guid)])
        mock_trim_to_required.assert_not_called()


class TestBulkRequest:
    SEE_ALSO = "seeAlso"
    REMOVE = "removeRelationshipAttributes"
    APPEND = "appendRelationshipAttributes"
    PREFERRED_TO_TERMS = "preferredToTerms"

    @pytest.fixture(scope="class")
    def glossary(self):
        return GLOSSARY

    @pytest.fixture(scope="class")
    def term1(self):
        return GLOSSARY_TERM

    @pytest.fixture(scope="class")
    def term2(self):
        return AtlasGlossaryTerm(guid="term-2-guid")

    @pytest.fixture(scope="class")
    def term3(self):
        return AtlasGlossaryTerm(guid="term-3-guid")

    def to_json(self, request):
        return request.dict(by_alias=True, exclude_unset=True)["entities"][0]

    def test_process_relationship_attributes(self, glossary, term1, term2, term3):
        # Test replace (list)
        term1.attributes.see_also = [
            AtlasGlossaryTerm.ref_by_guid(guid=term2.guid),
            AtlasGlossaryTerm.ref_by_guid(
                guid=term3.guid,
            ),
        ]
        request = BulkRequest(entities=[term1])
        request_json = self.to_json(request)
        assert request_json
        assert self.SEE_ALSO in request_json["attributes"]
        replace_attributes = request_json["attributes"][self.SEE_ALSO]
        assert len(replace_attributes) == 2
        assert replace_attributes[0]["guid"] == term2.guid
        assert replace_attributes[1]["guid"] == term3.guid
        assert self.APPEND not in request_json
        assert self.REMOVE not in request_json

        # Test replace and append (list)
        term1.attributes.see_also = [
            AtlasGlossaryTerm.ref_by_guid(guid=term2.guid),
            AtlasGlossaryTerm.ref_by_guid(
                guid=term3.guid, semantic=SaveSemantic.APPEND
            ),
        ]
        request = BulkRequest(entities=[term1])
        request_json = self.to_json(request)
        assert request_json
        assert self.SEE_ALSO in request_json["attributes"]
        replace_attributes = request_json["attributes"][self.SEE_ALSO]
        assert len(replace_attributes) == 1
        assert replace_attributes[0]["guid"] == term2.guid
        assert self.APPEND in request_json
        assert self.SEE_ALSO in request_json[self.APPEND]
        append_attributes = request_json[self.APPEND][self.SEE_ALSO]
        assert len(append_attributes) == 1
        assert append_attributes[0]["guid"] == term3.guid
        assert self.REMOVE not in request_json

        # Test replace and append (list) with multiple relationships
        term1.attributes.see_also = [
            AtlasGlossaryTerm.ref_by_guid(guid=term2.guid),
            AtlasGlossaryTerm.ref_by_guid(
                guid=term3.guid, semantic=SaveSemantic.APPEND
            ),
        ]
        term1.attributes.preferred_to_terms = [
            AtlasGlossaryTerm.ref_by_guid(
                guid=term3.guid, semantic=SaveSemantic.APPEND
            ),
        ]
        request = BulkRequest(entities=[term1])
        request_json = self.to_json(request)
        assert request_json
        assert self.SEE_ALSO in request_json["attributes"]
        replace_attributes = request_json["attributes"][self.SEE_ALSO]
        assert len(replace_attributes) == 1
        assert replace_attributes[0]["guid"] == term2.guid
        assert self.APPEND in request_json
        assert self.SEE_ALSO in request_json[self.APPEND]
        append_attributes = request_json[self.APPEND][self.SEE_ALSO]
        assert len(append_attributes) == 1
        assert append_attributes[0]["guid"] == term3.guid
        append_attributes = request_json[self.APPEND][self.PREFERRED_TO_TERMS]
        assert len(append_attributes) == 1
        assert append_attributes[0]["guid"] == term3.guid
        assert self.REMOVE not in request_json

        # Test append and replace (list)
        term1.attributes.see_also = [
            AtlasGlossaryTerm.ref_by_guid(
                guid=term2.guid, semantic=SaveSemantic.APPEND
            ),
            AtlasGlossaryTerm.ref_by_guid(guid=term3.guid),
        ]
        request = BulkRequest(entities=[term1])
        request_json = self.to_json(request)
        assert request_json
        assert self.SEE_ALSO in request_json["attributes"]
        replace_attributes = request_json["attributes"][self.SEE_ALSO]
        assert len(replace_attributes) == 1
        assert replace_attributes[0]["guid"] == term3.guid
        assert self.APPEND in request_json
        assert self.SEE_ALSO in request_json[self.APPEND]
        append_attributes = request_json[self.APPEND][self.SEE_ALSO]
        assert len(append_attributes) == 1
        assert append_attributes[0]["guid"] == term2.guid
        assert self.REMOVE not in request_json

        # Test remove and append (list)
        term1.attributes.see_also = [
            AtlasGlossaryTerm.ref_by_guid(
                guid=term2.guid, semantic=SaveSemantic.REMOVE
            ),
            AtlasGlossaryTerm.ref_by_guid(
                guid=term3.guid, semantic=SaveSemantic.APPEND
            ),
        ]
        request = BulkRequest(entities=[term1])
        request_json = self.to_json(request)
        assert request_json
        assert self.APPEND in request_json
        assert self.SEE_ALSO in request_json[self.APPEND]
        append_attributes = request_json[self.APPEND][self.SEE_ALSO]
        assert len(append_attributes) == 1
        assert append_attributes[0]["guid"] == term3.guid
        assert self.REMOVE in request_json
        assert self.SEE_ALSO in request_json[self.REMOVE]
        remove_attributes = request_json[self.REMOVE][self.SEE_ALSO]
        assert len(remove_attributes) == 1
        assert remove_attributes[0]["guid"] == term2.guid
        assert self.SEE_ALSO not in request_json["attributes"]

        # Test same semantic (list)
        term1.attributes.see_also = [
            AtlasGlossaryTerm.ref_by_guid(
                guid=term2.guid, semantic=SaveSemantic.APPEND
            ),
            AtlasGlossaryTerm.ref_by_guid(
                guid=term3.guid, semantic=SaveSemantic.APPEND
            ),
        ]
        request = BulkRequest(entities=[term1])
        request_json = self.to_json(request)
        assert request_json
        assert self.APPEND in request_json
        assert self.SEE_ALSO in request_json[self.APPEND]
        append_attributes = request_json[self.APPEND][self.SEE_ALSO]
        assert len(append_attributes) == 2
        assert append_attributes[0]["guid"] == term2.guid
        assert append_attributes[1]["guid"] == term3.guid
        assert self.REMOVE not in request_json
        assert self.SEE_ALSO not in request_json["attributes"]

        # Test empty (list)
        term1.attributes.see_also = []
        term1.attributes.preferred_to_terms = []
        request = BulkRequest(entities=[term1])
        request_json = self.to_json(request)
        assert request_json
        assert self.SEE_ALSO in request_json["attributes"]
        replace_attributes = request_json["attributes"][self.SEE_ALSO]
        assert len(replace_attributes) == 0
        assert self.APPEND not in request_json
        assert self.REMOVE not in request_json

        # Test replace
        term1.attributes.anchor = AtlasGlossary.ref_by_guid(guid=glossary.guid)
        request = BulkRequest(entities=[term1])
        request_json = self.to_json(request)
        assert request_json
        assert "anchor" in request_json["attributes"]
        replace_attributes = request_json["attributes"]["anchor"]
        assert replace_attributes
        assert replace_attributes["guid"] == glossary.guid
        assert self.APPEND not in request_json
        assert self.REMOVE not in request_json

        # Test append
        term1.attributes.anchor = AtlasGlossary.ref_by_guid(
            guid=glossary.guid, semantic=SaveSemantic.APPEND
        )
        request = BulkRequest(entities=[term1])
        request_json = self.to_json(request)
        assert request_json
        assert self.APPEND in request_json
        assert "anchor" in request_json[self.APPEND]
        append_attributes = request_json[self.APPEND]["anchor"]
        assert append_attributes["guid"] == glossary.guid
        assert self.REMOVE not in request_json
        assert "anchor" not in request_json["attributes"]

        # Test remove
        term1.attributes.anchor = AtlasGlossary.ref_by_guid(
            guid=glossary.guid, semantic=SaveSemantic.REMOVE
        )
        request = BulkRequest(entities=[term1])
        request_json = self.to_json(request)
        assert request_json
        assert self.REMOVE in request_json
        assert "anchor" in request_json[self.REMOVE]
        remove_attributes = request_json[self.REMOVE]["anchor"]
        assert remove_attributes["guid"] == glossary.guid
        assert self.APPEND not in request_json
        assert "anchor" not in request_json["attributes"]

    def test_asset_attribute_none_assignment(self):
        table1 = Table.updater(name="test-table-1", qualified_name="test-qn-1")
        table1.certificate_status = None
        table1.certificate_status_message = None
        request = BulkRequest(entities=[table1])
        request_json = self.to_json(request)
        assert request_json
        assert request_json["attributes"]["certificateStatus"] is None
        assert request_json["attributes"]["certificateStatusMessage"] is None


def test_atlan_client_headers(client: AtlanClient):
    VERSION = read_text("pyatlan", "version.txt").strip()
    expected = {
        "User-Agent": f"Atlan-PythonSDK/{VERSION}",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "x-atlan-agent": "sdk",
        "x-atlan-agent-id": "python",
        "x-atlan-client-origin": "product_sdk",
    }
    assert expected == client._session.headers


def test_get_all_pagination(group_client, mock_api_caller):
    mock_page_1 = [
        {"id": "1", "alias": "Group3"},
        {"id": "2", "alias": "Group4"},
    ]
    mock_api_caller._call_api.side_effect = [
        {"records": mock_page_1},
    ]

    groups = group_client.get_all(limit=2)
    assert len(groups.current_page()) == 2
    assert groups.current_page()[0].id == "1"
    assert groups.current_page()[1].id == "2"
    assert mock_api_caller._call_api.call_count == 1
    mock_api_caller.reset_mock()


def test_get_all_empty_response_with_raw_records(group_client, mock_api_caller):
    mock_page_1 = []
    mock_api_caller._call_api.side_effect = [
        {"records": mock_page_1},
    ]

    groups = group_client.get_all()
    assert len(groups.current_page()) == 0
    mock_api_caller.reset_mock()


def test_get_all_with_columns(group_client, mock_api_caller):
    mock_page_1 = [
        {"id": "1", "alias": "Group1"},
        {"id": "2", "alias": "Group2"},
    ]
    mock_api_caller._call_api.side_effect = [
        {"records": mock_page_1},
    ]

    columns = ["alias"]
    groups = group_client.get_all(limit=10, columns=columns)

    assert len(groups.current_page()) == 2
    assert groups.current_page()[0].id == "1"
    assert groups.current_page()[0].alias == "Group1"
    mock_api_caller._call_api.assert_called_once()
    query_params = mock_api_caller._call_api.call_args.kwargs["query_params"]
    assert query_params["columns"] == columns
    mock_api_caller.reset_mock()


def test_get_all_sorting(group_client, mock_api_caller):
    mock_page_1 = [
        {"id": "1", "alias": "Group1"},
        {"id": "2", "alias": "Group2"},
    ]
    mock_api_caller._call_api.side_effect = [
        {"records": mock_page_1},
    ]

    groups = group_client.get_all(limit=10, sort="alias")

    assert len(groups.current_page()) == 2
    assert groups.current_page()[0].id == "1"
    assert groups.current_page()[0].alias == "Group1"
    mock_api_caller._call_api.assert_called_once()
    query_params = mock_api_caller._call_api.call_args.kwargs["query_params"]
    assert query_params["sort"] == "alias"
    mock_api_caller.reset_mock()


def test_get_by_guid_asset_not_found_fluent_search():
    guid = "123"
    asset_type = Table

    with patch("pyatlan.model.fluent_search.FluentSearch.execute") as mock_execute:
        mock_execute.return_value.current_page.return_value = []

        client = AssetClient(client=ApiCaller)
        with pytest.raises(
            ErrorCode.ASSET_NOT_FOUND_BY_GUID.exception_with_parameters(guid).__class__
        ):
            client.get_by_guid(
                guid=guid,
                asset_type=asset_type,
                attributes=["name"],
                related_attributes=["owner"],
            )

        mock_execute.assert_called_once()


def test_get_by_guid_type_mismatch_fluent_search(mock_api_caller):
    guid = "123"
    expected_asset_type = Table
    returned_asset_type = View

    with patch("pyatlan.model.fluent_search.FluentSearch.execute") as mock_execute:
        mock_execute.return_value.current_page.return_value = [returned_asset_type()]

        client = AssetClient(client=mock_api_caller)

        with pytest.raises(
            ErrorCode.ASSET_NOT_TYPE_REQUESTED.exception_with_parameters(
                guid, expected_asset_type.__name__
            ).__class__
        ):
            client.get_by_guid(
                guid=guid,
                asset_type=expected_asset_type,
                attributes=["name"],
                related_attributes=["owner"],
            )

        mock_execute.assert_called_once()


def test_get_by_qualified_name_type_mismatch(mock_api_caller):
    qualified_name = "example_qualified_name"
    expected_asset_type = Table
    returned_asset_type = View

    with patch("pyatlan.model.fluent_search.FluentSearch.execute") as mock_execute:
        mock_execute.return_value.current_page.return_value = [returned_asset_type()]

        client = AssetClient(client=mock_api_caller)

        with pytest.raises(
            ErrorCode.ASSET_NOT_FOUND_BY_NAME.exception_with_parameters(
                expected_asset_type.__name__, qualified_name
            ).__class__
        ):
            client.get_by_qualified_name(
                qualified_name=qualified_name,
                asset_type=expected_asset_type,
                attributes=["name"],
                related_attributes=["owner"],
            )
        mock_execute.assert_called_once()


def test_get_by_qualified_name_asset_not_found(mock_api_caller):
    qualified_name = "example_qualified_name"
    asset_type = Table

    with patch("pyatlan.model.fluent_search.FluentSearch.execute") as mock_execute:
        mock_execute.return_value.current_page.return_value = []

        client = AssetClient(client=mock_api_caller)

        with pytest.raises(
            ErrorCode.ASSET_NOT_FOUND_BY_QN.exception_with_parameters(
                qualified_name, asset_type.__name__
            ).__class__
        ):
            client.get_by_qualified_name(
                qualified_name=qualified_name,
                asset_type=asset_type,
                attributes=["name"],
                related_attributes=["owner"],
            )

        mock_execute.assert_called_once()
