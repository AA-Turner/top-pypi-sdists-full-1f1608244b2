from unittest.mock import Mock

import pytest

from collate_sqllineage.core.holders import SubQueryLineageHolder
from collate_sqllineage.core.parser.sqlfluff.handlers.base import (
    ConditionalSegmentBaseHandler,
    SegmentBaseHandler,
)
from collate_sqllineage.core.parser.sqlfluff.models import SqlFluffColumn


def test_column_extract_source_columns():
    segment_mock = Mock()
    segment_mock.type = ""
    assert [] == SqlFluffColumn._extract_source_columns(segment_mock)


def test_handler_dummy():
    segment_mock = Mock()
    holder = SubQueryLineageHolder()
    c_handler = ConditionalSegmentBaseHandler("snowflake")
    with pytest.raises(NotImplementedError):
        c_handler.handle(segment_mock, holder)
    with pytest.raises(NotImplementedError):
        c_handler.indicate(segment_mock)
    s_handler = SegmentBaseHandler("snowflake")
    with pytest.raises(NotImplementedError):
        s_handler.handle(segment_mock, holder)
