import re
import sys
from copy import deepcopy
from decimal import Decimal
from typing import Any, Callable

import pytest
from dirty_equals import HasRepr, IsInstance

from pydantic_core import CoreConfig, SchemaError, SchemaValidator, ValidationError, core_schema


def test_model_class():
    class MyModel:
        # this is not required, but it avoids `__pydantic_fields_set__` being included in `__dict__`
        __slots__ = '__dict__', '__pydantic_fields_set__', '__pydantic_extra__', '__pydantic_private__'
        field_a: str
        field_b: int

    v = SchemaValidator(
        core_schema.model_schema(
            MyModel,
            core_schema.model_fields_schema(
                {
                    'field_a': core_schema.model_field(core_schema.str_schema()),
                    'field_b': core_schema.model_field(core_schema.int_schema()),
                }
            ),
        )
    )
    assert repr(v).startswith('SchemaValidator(title="MyModel", validator=Model(\n')
    m = v.validate_python({'field_a': 'test', 'field_b': 12})
    assert isinstance(m, MyModel)
    assert m.field_a == 'test'
    assert m.field_b == 12
    assert m.__pydantic_extra__ is None
    assert m.__pydantic_fields_set__ == {'field_a', 'field_b'}
    assert m.__dict__ == {'field_a': 'test', 'field_b': 12}

    m2 = v.validate_python({'field_a': 'test', 'field_b': 12}, strict=True)
    assert isinstance(m2, MyModel)
    assert m2.field_a == 'test'
    assert m2.field_b == 12
    assert m2.__pydantic_extra__ is None
    assert m2.__pydantic_fields_set__ == {'field_a', 'field_b'}
    assert m2.__dict__ == {'field_a': 'test', 'field_b': 12}


def test_model_class_extra():
    class MyModel:
        # this is not required, but it avoids `__pydantic_fields_set__` being included in `__dict__`
        __slots__ = '__dict__', '__pydantic_fields_set__', '__pydantic_extra__', '__pydantic_private__'
        field_a: str
        field_b: int

    v = SchemaValidator(
        core_schema.model_schema(
            MyModel,
            core_schema.model_fields_schema(
                {
                    'field_a': core_schema.model_field(core_schema.str_schema()),
                    'field_b': core_schema.model_field(core_schema.int_schema()),
                },
                extra_behavior='allow',
            ),
        )
    )
    m = v.validate_python({'field_a': 'test', 'field_b': 12, 'field_c': 'extra'})
    assert isinstance(m, MyModel)
    assert m.field_a == 'test'
    assert m.field_b == 12
    assert m.__pydantic_extra__ == {'field_c': 'extra'}
    assert m.__pydantic_fields_set__ == {'field_a', 'field_b', 'field_c'}
    assert m.__dict__ == {'field_a': 'test', 'field_b': 12}


def test_model_class_extra_forbid():
    class MyModel:
        class Meta:
            pass

        # this is not required, but it avoids `__pydantic_fields_set__` being included in `__dict__`
        __slots__ = '__dict__', '__pydantic_fields_set__', '__pydantic_extra__', '__pydantic_private__'
        field_a: str
        field_b: int

    class Wrapper:
        def __init__(self, inner):
            self._inner = inner

        def __dir__(self):
            return dir(self._inner)

        def __getattr__(self, key):
            return getattr(self._inner, key)

    v = SchemaValidator(
        core_schema.model_schema(
            MyModel,
            core_schema.model_fields_schema(
                {
                    'field_a': core_schema.model_field(core_schema.str_schema()),
                    'field_b': core_schema.model_field(core_schema.int_schema()),
                },
                extra_behavior='forbid',
            ),
        )
    )
    m = v.validate_python({'field_a': 'test', 'field_b': 12})
    assert isinstance(m, MyModel)
    assert m.field_a == 'test'
    assert m.field_b == 12

    # try revalidating from the model's attributes
    m = v.validate_python(Wrapper(m), from_attributes=True)

    with pytest.raises(ValidationError) as exc_info:
        m = v.validate_python({'field_a': 'test', 'field_b': 12, 'field_c': 'extra'})

    assert exc_info.value.errors(include_url=False) == [
        {'type': 'extra_forbidden', 'loc': ('field_c',), 'msg': 'Extra inputs are not permitted', 'input': 'extra'}
    ]


@pytest.mark.parametrize('extra_behavior', ['allow', 'ignore', 'forbid'])
def test_model_class_extra_forbid_from_attributes(extra_behavior: str):
    # iterating attributes includes much more than just __dict__, so need
    # careful interaction with __extra__

    class MyModel:
        # this is not required, but it avoids `__pydantic_fields_set__` being included in `__dict__`
        __slots__ = '__dict__', '__pydantic_fields_set__', '__pydantic_extra__', '__pydantic_private__'
        field_a: str
        field_b: int

    class Data:
        # https://github.com/pydantic/pydantic/issues/9242
        class Meta:
            pass

        def __init__(self, **values):
            self.__dict__.update(values)

    v = SchemaValidator(
        core_schema.model_schema(
            MyModel,
            core_schema.model_fields_schema(
                {
                    'field_a': core_schema.model_field(core_schema.str_schema()),
                    'field_b': core_schema.model_field(core_schema.int_schema()),
                },
                extra_behavior=extra_behavior,
                from_attributes=True,
            ),
        )
    )
    m = v.validate_python(Data(field_a='test', field_b=12))
    assert isinstance(m, MyModel)
    assert m.field_a == 'test'
    assert m.field_b == 12

    # with from_attributes, extra is basically ignored
    m = v.validate_python(Data(field_a='test', field_b=12, field_c='extra'))
    assert isinstance(m, MyModel)
    assert m.field_a == 'test'
    assert m.field_b == 12
    assert not hasattr(m, 'field_c')


def test_model_class_setattr():
    setattr_calls = []

    class MyModel:
        field_a: str

        def __setattr__(self, key, value):
            setattr_calls.append((key, value))
            # don't do anything

    m1 = MyModel()
    m1.foo = 'bar'
    assert not hasattr(m1, 'foo')
    assert setattr_calls == [('foo', 'bar')]
    setattr_calls.clear()

    v = SchemaValidator(
        core_schema.model_schema(
            cls=MyModel,
            schema=core_schema.model_fields_schema(
                fields={'field_a': core_schema.model_field(schema=core_schema.str_schema())}
            ),
        )
    )
    m = v.validate_python({'field_a': 'test'})
    assert isinstance(m, MyModel)
    assert m.field_a == 'test'
    assert m.__pydantic_fields_set__ == {'field_a'}
    assert setattr_calls == []


def test_model_class_root_validator_wrap():
    class MyModel:
        def __init__(self, **kwargs: Any) -> None:
            self.__dict__.update(kwargs)

    def f(
        input_value: dict[str, Any],
        validator: Callable[[dict[str, Any]], dict[str, Any]],
        info: core_schema.ValidationInfo,
    ):
        assert input_value['field_a'] == 123
        output = validator(input_value)
        return output

    schema = core_schema.model_schema(
        MyModel,
        core_schema.with_info_wrap_validator_function(
            f, core_schema.model_fields_schema({'field_a': core_schema.model_field(core_schema.int_schema())})
        ),
    )

    v = SchemaValidator(schema)
    m = v.validate_python({'field_a': 123})
    assert m.field_a == 123

    with pytest.raises(ValidationError) as e:
        v.validate_python({'field_a': 456})

    assert e.value.errors(include_url=False) == [
        {
            'type': 'assertion_error',
            'loc': (),
            'msg': 'Assertion failed, assert 456 == 123',
            'input': {'field_a': 456},
            'ctx': {'error': HasRepr(repr(AssertionError('assert 456 == 123')))},
        }
    ]


def test_model_class_root_validator_before():
    class MyModel:
        def __init__(self, **kwargs: Any) -> None:
            self.__dict__.update(kwargs)

    def f(input_value: dict[str, Any], info: core_schema.ValidationInfo):
        assert input_value['field_a'] == 123
        return input_value

    schema = core_schema.model_schema(
        MyModel,
        core_schema.with_info_before_validator_function(
            f, core_schema.model_fields_schema({'field_a': core_schema.model_field(core_schema.int_schema())})
        ),
    )

    v = SchemaValidator(schema)
    m = v.validate_python({'field_a': 123})
    assert m.field_a == 123

    with pytest.raises(ValidationError) as e:
        v.validate_python({'field_a': 456})

    assert e.value.errors(include_url=False) == [
        {
            'type': 'assertion_error',
            'loc': (),
            'msg': 'Assertion failed, assert 456 == 123',
            'input': {'field_a': 456},
            'ctx': {'error': HasRepr(repr(AssertionError('assert 456 == 123')))},
        }
    ]


def test_model_class_root_validator_after():
    class MyModel:
        def __init__(self, **kwargs: Any) -> None:
            self.__dict__.update(kwargs)

    def f(input_value_and_fields_set: tuple[dict[str, Any], set[str]]):
        input_value, _, _ = input_value_and_fields_set
        assert input_value['field_a'] == 123
        return input_value_and_fields_set

    schema = core_schema.model_schema(
        MyModel,
        core_schema.no_info_after_validator_function(
            f, core_schema.model_fields_schema({'field_a': core_schema.model_field(core_schema.int_schema())})
        ),
    )

    v = SchemaValidator(schema)
    m = v.validate_python({'field_a': 123})
    assert m.field_a == 123

    with pytest.raises(ValidationError) as e:
        v.validate_python({'field_a': 456})

    assert e.value.errors(include_url=False) == [
        {
            'type': 'assertion_error',
            'loc': (),
            'msg': 'Assertion failed, assert 456 == 123',
            'input': {'field_a': 456},
            'ctx': {'error': HasRepr(repr(AssertionError('assert 456 == 123')))},
        }
    ]


@pytest.mark.parametrize('mode', ['before', 'after', 'wrap'])
def test_function_ask(mode):
    class MyModel:
        __slots__ = '__dict__', '__pydantic_fields_set__', '__pydantic_extra__', '__pydantic_private__'

    def f(input_value, info):
        return input_value

    SchemaValidator(
        core_schema.model_schema(
            cls=MyModel,
            schema={
                'type': f'function-{mode}',
                'function': {'type': 'with-info', 'function': f},
                'schema': core_schema.model_fields_schema(
                    fields={'field_a': core_schema.model_field(schema=core_schema.str_schema())}
                ),
            },
        )
    )


def test_function_plain_ask():
    class MyModel:
        __slots__ = '__dict__', '__pydantic_fields_set__', '__pydantic_extra__', '__pydantic_private__'

    def f(input_value):
        return input_value, {1: 2}, {'field_a'}

    v = SchemaValidator(core_schema.model_schema(cls=MyModel, schema=core_schema.no_info_plain_validator_function(f)))
    m = v.validate_python({'field_a': 'test'})
    assert isinstance(m, MyModel)
    assert m.__dict__ == {'field_a': 'test'}
    assert m.__pydantic_extra__ == {1: 2}
    assert m.__pydantic_fields_set__ == {'field_a'}


def test_union_sub_schema():
    class MyModel:
        __slots__ = '__dict__', '__pydantic_fields_set__', '__pydantic_extra__', '__pydantic_private__'

    v = SchemaValidator(
        core_schema.model_schema(
            cls=MyModel,
            schema=core_schema.union_schema(
                choices=[
                    core_schema.model_fields_schema(
                        fields={'foo': core_schema.model_field(schema=core_schema.int_schema())}
                    ),
                    core_schema.model_fields_schema(
                        fields={'bar': core_schema.model_field(schema=core_schema.int_schema())}
                    ),
                ]
            ),
        )
    )
    m = v.validate_python({'foo': '123'})
    assert isinstance(m, MyModel)
    assert m.__dict__ == {'foo': 123}
    assert m.__pydantic_fields_set__ == {'foo'}
    m = v.validate_python({'bar': '123'})
    assert isinstance(m, MyModel)
    assert m.__dict__ == {'bar': 123}
    assert m.__pydantic_fields_set__ == {'bar'}


def test_tagged_union_sub_schema():
    class MyModel:
        pass

    v = SchemaValidator(
        core_schema.model_schema(
            cls=MyModel,
            schema=core_schema.tagged_union_schema(
                discriminator='foo',
                choices={
                    'apple': core_schema.model_fields_schema(
                        fields={
                            'foo': core_schema.model_field(schema=core_schema.str_schema()),
                            'bar': core_schema.model_field(schema=core_schema.int_schema()),
                        }
                    ),
                    'banana': core_schema.model_fields_schema(
                        fields={
                            'foo': core_schema.model_field(schema=core_schema.str_schema()),
                            'spam': core_schema.model_field(
                                schema=core_schema.list_schema(items_schema=core_schema.int_schema())
                            ),
                        }
                    ),
                },
            ),
        )
    )
    m = v.validate_python({'foo': 'apple', 'bar': '123'})
    assert isinstance(m, MyModel)
    assert m.__dict__ == {
        'foo': 'apple',
        'bar': 123,
        '__pydantic_fields_set__': {'foo', 'bar'},
        '__pydantic_extra__': None,
        '__pydantic_private__': None,
    }

    m = v.validate_python({'foo': 'banana', 'spam': [1, 2, 3]})
    assert isinstance(m, MyModel)
    # insert_assert(m.__dict__)
    assert m.__dict__ == {
        'foo': 'banana',
        'spam': [1, 2, 3],
        '__pydantic_fields_set__': {'spam', 'foo'},
        '__pydantic_extra__': None,
        '__pydantic_private__': None,
    }


def test_bad_sub_schema():
    class MyModel:
        pass

    v = SchemaValidator(core_schema.model_schema(cls=MyModel, schema=core_schema.int_schema()))
    with pytest.raises(TypeError):
        v.validate_python(123)


def test_model_class_function_after():
    class MyModel:
        __slots__ = '__dict__', '__pydantic_fields_set__', '__pydantic_extra__', '__pydantic_private__'

    def f(input_value, info):
        input_value[0]['x'] = 'y'
        return input_value

    v = SchemaValidator(
        core_schema.model_schema(
            cls=MyModel,
            schema={
                'type': 'function-after',
                'function': {'type': 'with-info', 'function': f},
                'schema': core_schema.model_fields_schema(
                    fields={'field_a': core_schema.model_field(schema=core_schema.str_schema())}
                ),
            },
        )
    )
    m = v.validate_python({'field_a': 'test'})
    assert isinstance(m, MyModel)
    assert m.__dict__ == {'field_a': 'test', 'x': 'y'}
    assert m.__pydantic_fields_set__ == {'field_a'}


def test_model_class_not_type():
    with pytest.raises(SchemaError, match=re.escape("TypeError: 'int' object cannot be converted to 'PyType'")):
        SchemaValidator(
            schema=core_schema.model_schema(
                cls=123,
                schema=core_schema.model_fields_schema(
                    fields={'field_a': core_schema.model_field(schema=core_schema.str_schema())}
                ),
            )
        )


def test_model_class_instance_direct():
    class MyModel:
        __slots__ = '__dict__', '__pydantic_fields_set__', '__pydantic_extra__', '__pydantic_private__'
        field_a: str

        def __init__(self):
            self.field_a = 'init'

    v = SchemaValidator(
        core_schema.model_schema(
            cls=MyModel,
            schema=core_schema.model_fields_schema(
                fields={'field_a': core_schema.model_field(schema=core_schema.str_schema())}
            ),
        )
    )
    m1 = v.validate_python({'field_a': 'test'})
    assert isinstance(m1, MyModel)
    assert m1.field_a == 'test'
    assert m1.__pydantic_fields_set__ == {'field_a'}

    m2 = MyModel()
    m3 = v.validate_python(m2)
    assert m2 == m3
    assert m3.field_a == 'init'


def test_model_class_instance_subclass():
    post_init_calls = []

    class MyModel:
        __slots__ = '__dict__', '__pydantic_fields_set__', '__pydantic_extra__', '__pydantic_private__'
        field_a: str

        def __init__(self):
            self.field_a = 'init_a'

        def model_post_init(self, context):
            post_init_calls.append(context)

    class MySubModel(MyModel):
        field_b: str

        def __init__(self):
            super().__init__()
            self.field_b = 'init_b'

    v = SchemaValidator(
        core_schema.model_schema(
            cls=MyModel,
            schema=core_schema.model_fields_schema(
                fields={'field_a': core_schema.model_field(schema=core_schema.str_schema())}
            ),
            post_init='model_post_init',
        )
    )

    m2 = MySubModel()
    assert m2.field_a
    m3 = v.validate_python(m2, context='call1')
    assert m2 is m3
    assert m3.field_a == 'init_a'
    assert m3.field_b == 'init_b'
    assert post_init_calls == []

    m4 = v.validate_python({'field_a': b'hello'}, context='call2')
    assert isinstance(m4, MyModel)
    assert m4.field_a == 'hello'
    assert m4.__pydantic_fields_set__ == {'field_a'}
    assert post_init_calls == ['call2']


def test_model_class_instance_subclass_revalidate():
    post_init_calls = []

    class MyModel:
        __slots__ = '__dict__', '__pydantic_fields_set__', '__pydantic_extra__', '__pydantic_private__'
        field_a: str

        def __init__(self):
            self.field_a = 'init_a'

        def model_post_init(self, context):
            post_init_calls.append(context)

    class MySubModel(MyModel):
        field_b: str
        __pydantic_fields_set__ = set()
        __pydantic_extra__ = None

        def __init__(self):
            super().__init__()
            self.field_b = 'init_b'

    v = SchemaValidator(
        core_schema.model_schema(
            cls=MyModel,
            schema=core_schema.model_fields_schema(
                fields={'field_a': core_schema.model_field(schema=core_schema.str_schema())}
            ),
            post_init='model_post_init',
            revalidate_instances='always',
        )
    )

    m2 = MySubModel()
    assert m2.field_a
    m2.__pydantic_extra__ = {}
    m2.__pydantic_fields_set__ = set()
    m3 = v.validate_python(m2, context='call1')
    assert m2 is not m3
    assert m3.field_a == 'init_a'
    assert not hasattr(m3, 'field_b')
    assert post_init_calls == ['call1']

    m4 = MySubModel()
    m4.__pydantic_extra__ = {}
    m4.__pydantic_fields_set__ = {'fruit_loop'}
    m5 = v.validate_python(m4, context='call2')
    assert m4 is not m5
    assert m5.__pydantic_fields_set__ == {'fruit_loop'}
    assert m5.field_a == 'init_a'
    assert not hasattr(m5, 'field_b')
    assert post_init_calls == ['call1', 'call2']


def test_model_class_strict():
    class MyModel:
        def __init__(self):
            self.field_a = 'init_a'
            self.field_b = 'init_b'

    v = SchemaValidator(
        core_schema.model_schema(
            strict=True,
            cls=MyModel,
            schema=core_schema.model_fields_schema(
                fields={
                    'field_a': core_schema.model_field(schema=core_schema.str_schema()),
                    'field_b': core_schema.model_field(schema=core_schema.int_schema()),
                }
            ),
        )
    )
    assert re.search(r'revalidate: \w+', repr(v)).group(0) == 'revalidate: Never'
    m = MyModel()
    m2 = v.validate_python(m)
    assert isinstance(m, MyModel)
    assert m is m2
    assert m.field_a == 'init_a'
    # note that since dict validation was not run here, there has been no check this is an int
    assert m.field_b == 'init_b'
    m3 = v.validate_python({'field_a': 'test', 'field_b': 12})
    assert isinstance(m3, MyModel)
    assert m3.field_a == 'test'
    assert m3.field_b == 12

    class MySubModel(MyModel):
        field_c: str

        def __init__(self):
            super().__init__()
            self.field_c = 'init_c'

    # instances of subclasses are allowed in strict mode
    m3 = MySubModel()
    m4 = v.validate_python(m3)
    assert m4 is m3


def test_model_class_strict_json():
    class MyModel:
        __slots__ = '__dict__', '__pydantic_fields_set__', '__pydantic_extra__', '__pydantic_private__'
        field_a: str
        field_b: int
        field_c: int

    v = SchemaValidator(
        core_schema.model_schema(
            strict=True,
            cls=MyModel,
            schema=core_schema.model_fields_schema(
                fields={
                    'field_a': core_schema.model_field(schema=core_schema.str_schema()),
                    'field_b': core_schema.model_field(schema=core_schema.int_schema()),
                    'field_c': core_schema.model_field(
                        schema=core_schema.with_default_schema(default=42, schema=core_schema.int_schema())
                    ),
                }
            ),
        )
    )
    m = v.validate_json('{"field_a": "foobar", "field_b": "123"}')
    assert isinstance(m, MyModel)
    assert m.field_a == 'foobar'
    assert m.field_b == 123
    assert m.field_c == 42
    assert m.__pydantic_fields_set__ == {'field_a', 'field_b'}


def test_internal_error():
    v = SchemaValidator(
        core_schema.model_schema(
            cls=int,
            schema=core_schema.model_fields_schema(
                fields={'f': core_schema.model_field(schema=core_schema.int_schema())}
            ),
        )
    )
    with pytest.raises(AttributeError, match=re.escape("'int' object has no attribute '__dict__'")):
        v.validate_python({'f': 123})


def test_revalidate_always():
    class MyModel:
        __slots__ = '__dict__', '__pydantic_fields_set__', '__pydantic_extra__', '__pydantic_private__'

        def __init__(self, a, b, fields_set):
            self.field_a = a
            self.field_b = b
            self.__pydantic_extra__ = {}
            if fields_set is not None:
                self.__pydantic_fields_set__ = fields_set

    v = SchemaValidator(
        core_schema.model_schema(
            cls=MyModel,
            revalidate_instances='always',
            schema=core_schema.model_fields_schema(
                fields={
                    'field_a': core_schema.model_field(schema=core_schema.str_schema()),
                    'field_b': core_schema.model_field(schema=core_schema.int_schema()),
                }
            ),
        )
    )
    assert re.search(r'revalidate: \w+', repr(v)).group(0) == 'revalidate: Always'

    m = v.validate_python({'field_a': 'test', 'field_b': 12})
    assert isinstance(m, MyModel)
    assert m.__dict__ == {'field_a': 'test', 'field_b': 12}
    assert m.__pydantic_fields_set__ == {'field_a', 'field_b'}

    m2 = MyModel('x', 42, {'field_a'})
    m3 = v.validate_python(m2)
    assert isinstance(m3, MyModel)
    assert m3 is not m2
    assert m3.__dict__ == {'field_a': 'x', 'field_b': 42}
    assert m3.__pydantic_fields_set__ == {'field_a'}

    m4 = MyModel('x', 'not int', {'field_a'})
    with pytest.raises(ValidationError) as exc_info:
        v.validate_python(m4)
    assert exc_info.value.errors(include_url=False) == [
        {
            'type': 'int_parsing',
            'loc': ('field_b',),
            'msg': 'Input should be a valid integer, unable to parse string as an integer',
            'input': 'not int',
        }
    ]

    m5 = MyModel('x', 5, None)
    with pytest.raises(AttributeError, match='__pydantic_fields_set__'):
        v.validate_python(m5)


def test_revalidate_subclass_instances():
    class MyModel:
        __slots__ = '__dict__', '__pydantic_fields_set__', '__pydantic_extra__', '__pydantic_private__'

        def __init__(self):
            self.field_a = 'init_a'
            self.field_b = 123

    class MySubModel(MyModel):
        def __init__(self):
            super().__init__()
            self.field_c = 'init_c'

    v = SchemaValidator(
        core_schema.model_schema(
            cls=MyModel,
            revalidate_instances='subclass-instances',
            schema=core_schema.model_fields_schema(
                fields={
                    'field_a': core_schema.model_field(schema=core_schema.str_schema()),
                    'field_b': core_schema.model_field(schema=core_schema.int_schema()),
                }
            ),
        )
    )

    m1 = MyModel()
    m2 = v.validate_python(m1)
    assert m2 is m1

    m3 = MySubModel()
    m3.__pydantic_extra__ = {}
    m3.__pydantic_fields_set__ = set()
    assert hasattr(m3, 'field_c')
    m4 = v.validate_python(m3)
    assert m4 is not m3
    assert type(m4) is MyModel
    assert not hasattr(m4, 'field_c')

    m5 = MySubModel()
    m5.__pydantic_extra__ = {}
    m5.__pydantic_fields_set__ = set()
    m5.field_b = 'not an int'
    with pytest.raises(ValidationError, match="type=int_parsing, input_value='not an int', input_type=str"):
        v.validate_python(m5)


def test_revalidate_extra():
    class MyModel:
        __slots__ = '__dict__', '__pydantic_fields_set__', '__pydantic_extra__', '__pydantic_private__'

        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    v = SchemaValidator(
        core_schema.model_schema(
            cls=MyModel,
            schema=core_schema.model_fields_schema(
                extra_behavior='allow',
                fields={
                    'field_a': core_schema.model_field(schema=core_schema.str_schema()),
                    'field_b': core_schema.model_field(schema=core_schema.int_schema()),
                },
            ),
            config=CoreConfig(revalidate_instances='always'),
        )
    )

    m = v.validate_python({'field_a': 'test', 'field_b': 12, 'more': (1, 2, 3)})
    assert isinstance(m, MyModel)
    assert m.__dict__ == {'field_a': 'test', 'field_b': 12}
    assert m.__pydantic_extra__ == {'more': (1, 2, 3)}
    assert m.__pydantic_fields_set__ == {'field_a', 'field_b', 'more'}

    m2 = MyModel(field_a='x', field_b=42)
    m2.__pydantic_extra__ = {'another': 42.5}
    m2.__pydantic_fields_set__ = {'field_a', 'field_b', 'another'}
    m3 = v.validate_python(m2)
    assert isinstance(m3, MyModel)
    assert m3 is not m2
    assert m3.__dict__ == {'field_a': 'x', 'field_b': 42}
    assert m3.__pydantic_extra__ == {'another': 42.5}
    assert m3.__pydantic_fields_set__ == {'field_a', 'field_b', 'another'}


def test_post_init():
    call_count = 0

    class MyModel:
        __slots__ = '__dict__', '__pydantic_fields_set__', '__pydantic_extra__', '__pydantic_private__'
        field_a: str
        field_b: int

        def call_me_maybe(self, *args):
            nonlocal call_count
            call_count += 1
            assert len(args) == 1
            context = args[0]
            assert context is None
            assert self.field_a == 'test'
            assert self.field_b == 12
            assert self.__pydantic_fields_set__ == {'field_a', 'field_b'}

    v = SchemaValidator(
        core_schema.model_schema(
            cls=MyModel,
            post_init='call_me_maybe',
            schema=core_schema.model_fields_schema(
                fields={
                    'field_a': core_schema.model_field(schema=core_schema.str_schema()),
                    'field_b': core_schema.model_field(schema=core_schema.int_schema()),
                }
            ),
        )
    )
    m = v.validate_python({'field_a': 'test', 'field_b': 12})
    assert isinstance(m, MyModel)
    assert call_count == 1


def test_revalidate_post_init():
    call_count = 0

    class MyModel:
        __slots__ = '__dict__', '__pydantic_fields_set__', '__pydantic_extra__', '__pydantic_private__'

        def call_me_maybe(self, context):
            nonlocal call_count
            call_count += 1
            assert context is None

    v = SchemaValidator(
        core_schema.model_schema(
            cls=MyModel,
            post_init='call_me_maybe',
            schema=core_schema.model_fields_schema(
                fields={
                    'field_a': core_schema.model_field(schema=core_schema.str_schema()),
                    'field_b': core_schema.model_field(schema=core_schema.int_schema()),
                }
            ),
            config=CoreConfig(revalidate_instances='always'),
        )
    )
    assert re.search(r'revalidate: \w+', repr(v)).group(0) == 'revalidate: Always'

    m = v.validate_python({'field_a': 'test', 'field_b': 12})
    assert isinstance(m, MyModel)
    assert m.__dict__ == {'field_a': 'test', 'field_b': 12}
    assert m.__pydantic_fields_set__ == {'field_a', 'field_b'}
    assert call_count == 1

    m2 = MyModel()
    m2.field_a = 'x'
    m2.field_b = 42
    m2.__pydantic_extra__ = {}
    m2.__pydantic_fields_set__ = {'field_a'}

    m3 = v.validate_python(m2)
    assert isinstance(m3, MyModel)
    assert m3 is not m2
    assert m3.__dict__ == {'field_a': 'x', 'field_b': 42}
    assert m3.__pydantic_fields_set__ == {'field_a'}
    assert call_count == 2


def test_post_init_validation_error():
    class MyModel:
        __slots__ = '__dict__', '__pydantic_fields_set__', '__pydantic_extra__', '__pydantic_private__'
        field_a: str

        def call_me_maybe(self, context, **kwargs):
            if context and 'error' in context:
                raise ValueError(f'this is broken: {self.field_a}')

    v = SchemaValidator(
        core_schema.model_schema(
            cls=MyModel,
            post_init='call_me_maybe',
            schema=core_schema.model_fields_schema(
                fields={'field_a': core_schema.model_field(schema=core_schema.str_schema())}
            ),
        )
    )
    m = v.validate_python({'field_a': 'test'})
    assert isinstance(m, MyModel)
    assert m.field_a == 'test'

    with pytest.raises(ValidationError) as exc_info:
        v.validate_python({'field_a': 'test'}, strict=None, context={'error': 1})
    assert exc_info.value.errors(include_url=False) == [
        {
            'type': 'value_error',
            'loc': (),
            'msg': 'Value error, this is broken: test',
            'input': {'field_a': 'test'},
            'ctx': {'error': HasRepr(repr(ValueError('this is broken: test')))},
        }
    ]


def test_post_init_internal_error():
    class MyModel:
        __slots__ = '__dict__', '__pydantic_fields_set__', '__pydantic_extra__', '__pydantic_private__'
        field_a: str

        def wrong_signature(self):
            pass

    v = SchemaValidator(
        core_schema.model_schema(
            cls=MyModel,
            post_init='wrong_signature',
            schema=core_schema.model_fields_schema(
                fields={'field_a': core_schema.model_field(schema=core_schema.str_schema())}
            ),
        )
    )
    with pytest.raises(TypeError, match=r'wrong_signature\(\) takes 1 positional argument but 2 were given'):
        v.validate_python({'field_a': 'test'})


def test_post_init_mutate():
    class MyModel:
        __slots__ = '__dict__', '__pydantic_fields_set__', '__pydantic_extra__', '__pydantic_private__'
        field_a: str
        field_b: int

        def call_me_maybe(self, context, **kwargs):
            self.field_a *= 2
            self.__pydantic_fields_set__ = {'field_a'}

    v = SchemaValidator(
        core_schema.model_schema(
            cls=MyModel,
            post_init='call_me_maybe',
            schema=core_schema.model_fields_schema(
                fields={
                    'field_a': core_schema.model_field(schema=core_schema.str_schema()),
                    'field_b': core_schema.model_field(schema=core_schema.int_schema()),
                }
            ),
        )
    )
    m = v.validate_python({'field_a': 'test', 'field_b': 12})
    assert isinstance(m, MyModel)
    assert m.field_a == 'testtest'
    assert m.field_b == 12
    assert m.__pydantic_fields_set__ == {'field_a'}
    assert m.__dict__ == {'field_a': 'testtest', 'field_b': 12}


def test_validate_assignment():
    class MyModel:
        # this is not required, but it avoids `__pydantic_fields_set__` being included in `__dict__`
        __slots__ = '__dict__', '__pydantic_fields_set__', '__pydantic_extra__', '__pydantic_private__'
        field_a: str
        field_b: int

        def __init__(self):
            self.__pydantic_extra__ = None

    v = SchemaValidator(
        core_schema.model_schema(
            MyModel,
            core_schema.model_fields_schema(
                {
                    'field_a': core_schema.model_field(core_schema.str_schema()),
                    'field_b': core_schema.model_field(core_schema.int_schema()),
                },
                extra_behavior='allow',
            ),
            extra_behavior='allow',
        )
    )

    m = MyModel()
    m.field_a = 'hello'
    m.field_b = 123
    m.__pydantic_fields_set__ = {'field_a'}

    v.validate_assignment(m, 'field_b', '321')

    m.field_a = 'hello'
    assert m.field_b == 321
    assert m.__pydantic_fields_set__ == {'field_a', 'field_b'}

    v.validate_assignment(m, 'field_b', '322', from_attributes=True)
    assert m.field_b == 322

    # try deleting a field
    del m.field_b
    # assignment to `field_a` should not care about `field_b` missing
    v.validate_assignment(m, 'field_a', 'hello world', from_attributes=True)
    assert m.field_a == 'hello world'


def test_validate_assignment_function():
    class MyModel:
        # this is not required, but it avoids `__pydantic_fields_set__` being included in `__dict__`
        __slots__ = '__dict__', '__pydantic_fields_set__', '__pydantic_extra__', '__pydantic_private__'
        field_a: str
        field_b: int
        field_c: int

    calls: list[Any] = []

    def func(x, info):
        calls.append(str(info))
        return x * 2

    v = SchemaValidator(
        core_schema.model_schema(
            MyModel,
            core_schema.model_fields_schema(
                {
                    'field_a': core_schema.model_field(core_schema.str_schema()),
                    'field_b': core_schema.model_field(
                        core_schema.with_info_after_validator_function(func, core_schema.int_schema())
                    ),
                    'field_c': core_schema.model_field(core_schema.int_schema()),
                }
            ),
        )
    )

    m = v.validate_python({'field_a': 'x', 'field_b': 123, 'field_c': 456})
    assert m.field_a == 'x'
    assert m.field_b == 246
    assert m.field_c == 456
    assert m.__pydantic_fields_set__ == {'field_a', 'field_b', 'field_c'}
    assert calls == ["ValidationInfo(config=None, context=None, data={'field_a': 'x'}, field_name='field_b')"]

    v.validate_assignment(m, 'field_b', '111')

    assert m.field_b == 222
    assert calls == [
        "ValidationInfo(config=None, context=None, data={'field_a': 'x'}, field_name='field_b')",
        "ValidationInfo(config=None, context=None, data={'field_a': 'x', 'field_c': 456}, field_name='field_b')",
    ]


def test_validate_assignment_no_fields_set():
    class MyModel:
        __slots__ = ('__dict__', '__pydantic_extra__')

        def __init__(self):
            self.__pydantic_extra__ = None

    v = SchemaValidator(
        core_schema.model_schema(
            cls=MyModel,
            schema=core_schema.model_fields_schema(
                fields={
                    'field_a': core_schema.model_field(schema=core_schema.str_schema()),
                    'field_b': core_schema.model_field(schema=core_schema.int_schema()),
                }
            ),
        )
    )

    m = MyModel()
    m.field_a = 'hello'
    m.field_b = 123
    assert not hasattr(m, '__pydantic_fields_set__')

    v.validate_assignment(m, 'field_a', b'different')

    m.field_a = 'different'
    assert m.field_b == 123
    assert not hasattr(m, '__pydantic_fields_set__')

    # wrong arguments
    with pytest.raises(AttributeError, match="'str' object has no attribute '__dict__'"):
        v.validate_assignment('field_a', 'field_a', b'different')


def test_frozen():
    class MyModel:
        __slots__ = {'__dict__', '__pydantic_fields_set__', '__pydantic_extra__', '__pydantic_private__'}

    v = SchemaValidator(
        core_schema.model_schema(
            MyModel,
            core_schema.model_fields_schema({'f': core_schema.model_field(core_schema.str_schema())}),
            frozen=True,
        )
    )

    m = v.validate_python({'f': 'x'})
    assert m.f == 'x'

    with pytest.raises(ValidationError) as exc_info:
        v.validate_assignment(m, 'f', 'y')

    # insert_assert(exc_info.value.errors(include_url=False))
    assert exc_info.value.errors(include_url=False) == [
        {'type': 'frozen_instance', 'loc': (), 'msg': 'Instance is frozen', 'input': 'y'}
    ]


@pytest.mark.parametrize(
    'function_schema,call1, call2',
    [
        (
            core_schema.with_info_after_validator_function,
            (({'a': 1, 'b': 2}, None, {'b'}), 'ValidationInfo(config=None, context=None, data=None, field_name=None)'),
            (({'a': 10, 'b': 2}, None, {'a'}), "ValidationInfo(config=None, context=None, data=None, field_name='a')"),
        ),
        (
            core_schema.with_info_before_validator_function,
            ({'b': 2}, 'ValidationInfo(config=None, context=None, data=None, field_name=None)'),
            ({'a': 10, 'b': 2}, "ValidationInfo(config=None, context=None, data=None, field_name='a')"),
        ),
        (
            core_schema.with_info_wrap_validator_function,
            ({'b': 2}, 'ValidationInfo(config=None, context=None, data=None, field_name=None)'),
            ({'a': 10, 'b': 2}, "ValidationInfo(config=None, context=None, data=None, field_name='a')"),
        ),
    ],
)
def test_validate_assignment_model_validator_function(function_schema: Any, call1: Any, call2: Any):
    """
    Test handling of values and fields_set for validator functions that wrap a model when using
    validate_assignment.

    Note that we are currently not exposing this functionality in conjunction with getting
    access to `fields_set` in a model validator, so the behavior of fields set.
    In particular, for function_after it is not clear if the fields set passed to
    the validator should be the fields that were assigned on this call to `validate_assignment`
    (currently always a single field) or the fields that have been assigned in the
    model since it was created.
    """

    class Model:
        __slots__ = '__dict__', '__pydantic_fields_set__', '__pydantic_extra__', '__pydantic_private__'

    calls: list[Any] = []

    def f(values_or_values_and_fields_set: Any, *args: Any) -> Any:
        if len(args) == 2:
            # wrap
            handler, info = args
            calls.append((deepcopy(values_or_values_and_fields_set), str(info)))
            return handler(values_or_values_and_fields_set)
        else:
            info = args[0]
            calls.append((deepcopy(values_or_values_and_fields_set), str(info)))
            return values_or_values_and_fields_set

    v = SchemaValidator(
        core_schema.model_schema(
            Model,
            function_schema(
                f,
                core_schema.model_fields_schema(
                    {
                        'a': core_schema.model_field(
                            core_schema.with_default_schema(core_schema.int_schema(), default=1)
                        ),
                        'b': core_schema.model_field(core_schema.int_schema()),
                    }
                ),
            ),
        )
    )

    m = v.validate_python({'b': 2})
    assert m.a == 1
    assert m.b == 2
    assert m.__pydantic_fields_set__ == {'b'}
    assert calls == [call1]

    v.validate_assignment(m, 'a', 10)
    assert m.a == 10
    assert m.b == 2
    assert m.__pydantic_fields_set__ == {'a', 'b'}
    assert calls == [call1, call2]


def test_model_error():
    class MyModel:
        # this is not required, but it avoids `__pydantic_fields_set__` being included in `__dict__`
        __slots__ = '__dict__', '__pydantic_fields_set__', '__pydantic_extra__', '__pydantic_private__'
        field_a: str
        field_b: int

    v = SchemaValidator(
        core_schema.model_schema(
            MyModel,
            core_schema.model_fields_schema(
                {
                    'field_a': core_schema.model_field(core_schema.str_schema()),
                    'field_b': core_schema.model_field(core_schema.int_schema()),
                },
                model_name='MyModel',
            ),
        )
    )
    m = v.validate_python({'field_a': 'test', 'field_b': 12})
    assert isinstance(m, MyModel)
    assert m.__dict__ == {'field_a': 'test', 'field_b': 12}

    m2 = MyModel()
    m2.field_a = '1'
    m2.field_b = 2

    m3 = v.validate_python(m2)
    assert isinstance(m3, MyModel)
    assert m3.__dict__ == {'field_a': '1', 'field_b': 2}

    m4 = v.validate_json('{"field_a": "3", "field_b": 4}')
    assert isinstance(m4, MyModel)
    assert m4.__dict__ == {'field_a': '3', 'field_b': 4}

    class OtherModel:
        pass

    with pytest.raises(ValidationError) as exc_info:
        v.validate_python(OtherModel())
    # insert_assert(exc_info.value.errors(include_url=False))
    assert exc_info.value.errors(include_url=False) == [
        {
            'type': 'model_type',
            'loc': (),
            'msg': 'Input should be a valid dictionary or instance of MyModel',
            'input': IsInstance(OtherModel),
            'ctx': {'class_name': 'MyModel'},
        }
    ]

    with pytest.raises(ValidationError) as exc_info:
        v.validate_json('123')
    # insert_assert(exc_info.value.errors(include_url=False))
    assert exc_info.value.errors(include_url=False) == [
        {
            'type': 'model_type',
            'loc': (),
            'msg': 'Input should be an object',
            'input': 123,
            'ctx': {'class_name': 'MyModel'},
        }
    ]


@pytest.mark.skipif(
    sys.version_info >= (3, 13),
    reason='Python 3.13+ enum initialization is different, see https://github.com/python/cpython/blob/ec610069637d56101896803a70d418a89afe0b4b/Lib/enum.py#L1159-L1163',
)
def test_model_with_enum_int_field_validation_should_succeed_for_any_type_equality_checks():
    # GIVEN
    from enum import Enum

    class EnumClass(Enum):
        enum_value = 1
        enum_value_2 = 2
        enum_value_3 = 3

    class IntWrappable:
        def __init__(self, value: int):
            self.value = value

        def __eq__(self, other: object) -> bool:
            return self.value == other

    class MyModel:
        __slots__ = (
            '__dict__',
            '__pydantic_fields_set__',
            '__pydantic_extra__',
            '__pydantic_private__',
        )
        enum_field: EnumClass

    # WHEN
    v = SchemaValidator(
        core_schema.model_schema(
            MyModel,
            core_schema.model_fields_schema(
                {
                    'enum_field': core_schema.model_field(
                        core_schema.enum_schema(EnumClass, list(EnumClass.__members__.values()))
                    ),
                    'enum_field_2': core_schema.model_field(
                        core_schema.enum_schema(EnumClass, list(EnumClass.__members__.values()))
                    ),
                    'enum_field_3': core_schema.model_field(
                        core_schema.enum_schema(EnumClass, list(EnumClass.__members__.values()))
                    ),
                }
            ),
        )
    )

    # THEN
    v.validate_json('{"enum_field": 1, "enum_field_2": 2, "enum_field_3": 3}')
    m = v.validate_python(
        {
            'enum_field': Decimal(1),
            'enum_field_2': Decimal(2),
            'enum_field_3': IntWrappable(3),
        }
    )
    v.validate_assignment(m, 'enum_field', Decimal(1))
    v.validate_assignment(m, 'enum_field_2', Decimal(2))
    v.validate_assignment(m, 'enum_field_3', IntWrappable(3))
