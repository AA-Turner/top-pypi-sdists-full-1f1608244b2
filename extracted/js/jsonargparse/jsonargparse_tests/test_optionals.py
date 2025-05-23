from __future__ import annotations

import sys

import pytest

from jsonargparse import set_parsing_settings
from jsonargparse._optionals import (
    _get_config_read_mode,
    docstring_parser_support,
    fallback_final,
    fsspec_support,
    get_docstring_parse_options,
    import_docstring_parser,
    import_fsspec,
    import_jsonnet,
    import_jsonschema,
    import_requests,
    import_ruyaml,
    jsonnet_support,
    jsonschema_support,
    ruyaml_support,
    url_support,
)
from jsonargparse.typing import is_final_class
from jsonargparse_tests.conftest import (
    skip_if_docstring_parser_unavailable,
    skip_if_fsspec_unavailable,
    skip_if_requests_unavailable,
)

# jsonschema support


@pytest.mark.skipif(not jsonschema_support, reason="jsonschema package is required")
def test_jsonschema_support_true():
    import_jsonschema("test_jsonschema_support_true")


@pytest.mark.skipif(jsonschema_support, reason="jsonschema package should not be installed")
def test_jsonschema_support_false():
    with pytest.raises(ImportError) as ctx:
        import_jsonschema("test_jsonschema_support_false")
    ctx.match("test_jsonschema_support_false")


# jsonnet support


@pytest.mark.skipif(not jsonnet_support, reason="jsonnet package is required")
def test_jsonnet_support_true():
    import_jsonnet("test_jsonnet_support_true")


@pytest.mark.skipif(jsonnet_support, reason="jsonnet package should not be installed")
def test_jsonnet_support_false():
    with pytest.raises(ImportError) as ctx:
        import_jsonnet("test_jsonnet_support_false")
    ctx.match("test_jsonnet_support_false")


# requests support


@skip_if_requests_unavailable
def test_url_support_true():
    import_requests("test_url_support_true")


@pytest.mark.skipif(url_support, reason="requests package should not be installed")
def test_url_support_false():
    with pytest.raises(ImportError) as ctx:
        import_requests("test_url_support_false")
    ctx.match("test_url_support_false")


# docstring-parser support


@skip_if_docstring_parser_unavailable
def test_docstring_parser_support_true():
    import_docstring_parser("test_docstring_parser_support_true")


@pytest.mark.skipif(docstring_parser_support, reason="docstring-parser package should not be installed")
def test_docstring_parser_support_false():
    with pytest.raises(ImportError) as ctx:
        import_docstring_parser("test_docstring_parser_support_false")
    ctx.match("test_docstring_parser_support_false")


@skip_if_docstring_parser_unavailable
def test_docstring_parse_options():
    from docstring_parser import DocstringStyle

    options = get_docstring_parse_options()
    options["style"] = None
    options = get_docstring_parse_options()

    for style in [DocstringStyle.NUMPYDOC, DocstringStyle.GOOGLE]:
        set_parsing_settings(docstring_parse_style=style)
        assert options["style"] == style
    with pytest.raises(ValueError):
        set_parsing_settings(docstring_parse_style="invalid")

    assert options["attribute_docstrings"] is False
    for attribute_docstrings in [True, False]:
        set_parsing_settings(docstring_parse_attribute_docstrings=attribute_docstrings)
        assert options["attribute_docstrings"] is attribute_docstrings
    with pytest.raises(ValueError):
        set_parsing_settings(docstring_parse_attribute_docstrings="invalid")


# fsspec support


@skip_if_fsspec_unavailable
def test_fsspec_support_true():
    import_fsspec("test_fsspec_support_true")


@pytest.mark.skipif(fsspec_support, reason="fsspec package should not be installed")
def test_fsspec_support_false():
    with pytest.raises(ImportError) as ctx:
        import_fsspec("test_fsspec_support_false")
    ctx.match("test_fsspec_support_false")


# ruyaml support


@pytest.mark.skipif(not ruyaml_support, reason="ruyaml package is required")
def test_ruyaml_support_true():
    import_ruyaml("test_ruyaml_support_true")


@pytest.mark.skipif(ruyaml_support, reason="ruyaml package should not be installed")
def test_ruyaml_support_false():
    with pytest.raises(ImportError) as ctx:
        import_ruyaml("test_ruyaml_support_false")
    ctx.match("test_ruyaml_support_false")


# config read mode tests


@skip_if_requests_unavailable
def test_config_read_mode_url_support_true():
    assert "fr" == _get_config_read_mode()
    set_parsing_settings(config_read_mode_urls_enabled=True)
    assert "fur" == _get_config_read_mode()
    set_parsing_settings(config_read_mode_urls_enabled=False)
    assert "fr" == _get_config_read_mode()


@pytest.mark.skipif(url_support, reason="request package should not be installed")
def test_config_read_mode_url_support_false():
    assert "fr" == _get_config_read_mode()
    with pytest.raises(ImportError):
        set_parsing_settings(config_read_mode_urls_enabled=True)
    assert "fr" == _get_config_read_mode()
    set_parsing_settings(config_read_mode_urls_enabled=False)
    assert "fr" == _get_config_read_mode()


@skip_if_fsspec_unavailable
def test_config_read_mode_fsspec_support_true():
    assert "fr" == _get_config_read_mode()
    set_parsing_settings(config_read_mode_fsspec_enabled=True)
    assert "fsr" == _get_config_read_mode()
    set_parsing_settings(config_read_mode_fsspec_enabled=False)
    assert "fr" == _get_config_read_mode()


@pytest.mark.skipif(fsspec_support, reason="fsspec package should not be installed")
def test_config_read_mode_fsspec_support_false():
    assert "fr" == _get_config_read_mode()
    with pytest.raises(ImportError):
        set_parsing_settings(config_read_mode_fsspec_enabled=True)
    assert "fr" == _get_config_read_mode()
    set_parsing_settings(config_read_mode_fsspec_enabled=False)
    assert "fr" == _get_config_read_mode()


# final decorator tests


@fallback_final
class FinalClass:
    pass


@pytest.mark.skipif(sys.version_info < (3, 11), reason="final decorator __final__ introduced in python 3.11")
def test_final_decorator():
    assert is_final_class(FinalClass) is True
    assert is_final_class(test_final_decorator) is False
