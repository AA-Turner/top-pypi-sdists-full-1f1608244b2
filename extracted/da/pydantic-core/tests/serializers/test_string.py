import json
from enum import Enum

import pytest

from pydantic_core import PydanticSerializationError, SchemaSerializer, core_schema


def test_str():
    v = SchemaSerializer(core_schema.str_schema())
    assert v.to_python('foobar') == 'foobar'
    assert v.to_python('emoji 💩') == 'emoji 💩'
    assert v.to_json('foobar') == b'"foobar"'
    assert v.to_json('foobar', indent=2) == b'"foobar"'
    assert v.to_json('emoji 💩') == b'"emoji \xf0\x9f\x92\xa9"'
    assert json.loads(v.to_json('emoji 💩')) == 'emoji 💩'

    assert v.to_python('foobar', mode='json') == 'foobar'

    json_emoji = v.to_json('emoji 💩')
    # note! serde_json serializes unicode characters differently to json.dumps, but it's still valid JSON
    assert json_emoji == b'"emoji \xf0\x9f\x92\xa9"'
    assert json.loads(json_emoji) == 'emoji 💩'


def test_huge_str():
    v = SchemaSerializer(core_schema.int_schema())
    msg = r"Expected `int` - serialized value may not be as expected \[input_value='123456789012345678901234...89012345678901234567890', input_type=str\]"
    with pytest.warns(UserWarning, match=msg):
        v.to_python(
            '12345678901234567890123456789012345678901234567890123456789012345678901234567890\
                           12345678901234567890123456789012345678901234567890123456789012345678901234567890\
                           12345678901234567890123456789012345678901234567890123456789012345678901234567890\
                           12345678901234567890123456789012345678901234567890123456789012345678901234567890'
        )


def test_str_fallback():
    s = SchemaSerializer(core_schema.str_schema())
    assert s.to_python(None) is None
    assert s.to_python(None, mode='json') is None
    assert s.to_json(None) == b'null'
    with pytest.warns(
        UserWarning,
        match=r'Expected `str` - serialized value may not be as expected \[input_value=123, input_type=int\]',
    ):
        assert s.to_python(123) == 123
    with pytest.warns(
        UserWarning,
        match=r'Expected `str` - serialized value may not be as expected \[input_value=123, input_type=int\]',
    ):
        assert s.to_python(123, mode='json') == 123
    with pytest.warns(
        UserWarning,
        match=r'Expected `str` - serialized value may not be as expected \[input_value=123, input_type=int\]',
    ):
        assert s.to_json(123) == b'123'
    with pytest.warns(
        UserWarning,
        match=r'Expected `str` - serialized value may not be as expected \[input_value=123, input_type=int\]',
    ):
        assert s.to_python(123, warnings='warn') == 123
    with pytest.warns(
        UserWarning,
        match=r'Expected `str` - serialized value may not be as expected \[input_value=123, input_type=int\]',
    ):
        assert s.to_python(123, mode='json', warnings='warn') == 123
    with pytest.warns(
        UserWarning,
        match=r'Expected `str` - serialized value may not be as expected \[input_value=123, input_type=int\]',
    ):
        assert s.to_json(123, warnings='warn') == b'123'
    with pytest.warns(
        UserWarning,
        match=r'Expected `str` - serialized value may not be as expected \[input_value=123, input_type=int\]',
    ):
        assert s.to_python(123, warnings=True) == 123
    with pytest.warns(
        UserWarning,
        match=r'Expected `str` - serialized value may not be as expected \[input_value=123, input_type=int\]',
    ):
        assert s.to_python(123, mode='json', warnings=True) == 123
    with pytest.warns(
        UserWarning,
        match=r'Expected `str` - serialized value may not be as expected \[input_value=123, input_type=int\]',
    ):
        assert s.to_json(123, warnings=True) == b'123'


def test_str_no_warnings():
    s = SchemaSerializer(core_schema.str_schema())
    assert s.to_python(123, warnings=False) == 123
    assert s.to_python(123, warnings='none') == 123
    assert s.to_python(123, mode='json', warnings=False) == 123
    assert s.to_python(123, mode='json', warnings='none') == 123
    assert s.to_json(123, warnings=False) == b'123'
    assert s.to_json(123, warnings='none') == b'123'


def test_str_errors():
    s = SchemaSerializer(core_schema.str_schema())
    with pytest.raises(
        PydanticSerializationError,
        match=r'Expected `str` - serialized value may not be as expected \[input_value=123, input_type=int\]',
    ):
        assert s.to_python(123, warnings='error') == 123
    with pytest.raises(
        PydanticSerializationError,
        match=r'Expected `str` - serialized value may not be as expected \[input_value=123, input_type=int\]',
    ):
        assert s.to_python(123, mode='json', warnings='error') == 123
    with pytest.raises(
        PydanticSerializationError,
        match=r'Expected `str` - serialized value may not be as expected \[input_value=123, input_type=int\]',
    ):
        assert s.to_json(123, warnings='error') == b'123'


class StrSubclass(str):
    pass


class BasicClass:
    pass


class StrMixin(str, BasicClass):
    pass


class StrEnum(str, Enum):
    foo = 'foo-value'
    bar = 'bar-value'


@pytest.mark.parametrize('schema_type', ['str', 'any'])
@pytest.mark.parametrize(
    'input_value,expected', [(StrSubclass('foo'), 'foo'), (StrMixin('foo'), 'foo'), (StrEnum.foo, 'foo-value')]
)
def test_subclass_str(schema_type, input_value, expected):
    s = SchemaSerializer({'type': schema_type})
    v = s.to_python(input_value)
    assert v == input_value
    assert type(v) == type(input_value)

    v = s.to_python(input_value, mode='json')
    assert v == expected
    assert type(v) == str

    assert s.to_json(input_value) == json.dumps(expected).encode('utf-8')
