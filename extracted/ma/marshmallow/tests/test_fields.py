import pytest

from marshmallow import (
    EXCLUDE,
    INCLUDE,
    RAISE,
    Schema,
    ValidationError,
    fields,
    missing,
)
from marshmallow.exceptions import StringNotCollectionError
from marshmallow.orderedset import OrderedSet
from tests.base import ALL_FIELDS


@pytest.mark.parametrize(
    ("alias", "field"),
    [
        (fields.Int, fields.Integer),
        (fields.Str, fields.String),
        (fields.Bool, fields.Boolean),
        (fields.URL, fields.Url),
    ],
)
def test_field_aliases(alias, field):
    assert alias is field


class TestField:
    def test_repr(self):
        default = "œ∑´"  # noqa: RUF001
        field = fields.Raw(dump_default=default, attribute=None)
        assert repr(field) == (
            f"<fields.Raw(dump_default={default!r}, attribute=None, "
            "validate=None, required=False, "
            "load_only=False, dump_only=False, "
            f"load_default={missing}, allow_none=False, "
            f"error_messages={field.error_messages})>"
        )
        int_field = fields.Integer(validate=lambda x: True)
        assert "<fields.Integer" in repr(int_field)

    def test_error_raised_if_uncallable_validator_passed(self):
        with pytest.raises(ValueError, match="must be a callable"):
            fields.Raw(validate="notcallable")  # type: ignore[arg-type]

    def test_error_raised_if_missing_is_set_on_required_field(self):
        with pytest.raises(
            ValueError, match="'load_default' must not be set for required fields"
        ):
            fields.Raw(required=True, load_default=42)

    def test_custom_field_receives_attr_and_obj(self):
        class MyField(fields.Field[str]):
            def _deserialize(self, value, attr, data, **kwargs) -> str:
                assert attr == "name"
                assert data["foo"] == 42
                return str(value)

        class MySchema(Schema):
            name = MyField()

        result = MySchema(unknown=EXCLUDE).load({"name": "Monty", "foo": 42})
        assert result == {"name": "Monty"}

    def test_custom_field_receives_data_key_if_set(self):
        class MyField(fields.Field[str]):
            def _deserialize(self, value, attr, data, **kwargs):
                assert attr == "name"
                assert data["foo"] == 42
                return str(value)

        class MySchema(Schema):
            Name = MyField(data_key="name")

        result = MySchema(unknown=EXCLUDE).load({"name": "Monty", "foo": 42})
        assert result == {"Name": "Monty"}

    def test_custom_field_follows_data_key_if_set(self):
        class MyField(fields.Field[str]):
            def _serialize(self, value, attr, obj, **kwargs) -> str:
                assert attr == "name"
                assert obj["foo"] == 42
                return str(value)

        class MySchema(Schema):
            name = MyField(data_key="_NaMe")

        result = MySchema().dump({"name": "Monty", "foo": 42})
        assert result == {"_NaMe": "Monty"}


class TestParentAndName:
    class MySchema(Schema):
        foo = fields.Raw()
        bar = fields.List(fields.Str())
        baz = fields.Tuple((fields.Str(), fields.Int()))
        bax = fields.Dict(fields.Str(), fields.Int())

    @pytest.fixture
    def schema(self):
        return self.MySchema()

    def test_simple_field_parent_and_name(self, schema):
        assert schema.fields["foo"].parent == schema
        assert schema.fields["foo"].name == "foo"
        assert schema.fields["bar"].parent == schema
        assert schema.fields["bar"].name == "bar"

    # https://github.com/marshmallow-code/marshmallow/pull/572#issuecomment-275800288
    def test_unbound_field_root_returns_none(self):
        field = fields.Str()
        assert field.root is None

        inner_field = fields.Nested(self.MySchema())
        outer_field = fields.List(inner_field)

        assert outer_field.root is None
        assert inner_field.root is None

    def test_list_field_inner_parent_and_name(self, schema):
        assert schema.fields["bar"].inner.parent == schema.fields["bar"]
        assert schema.fields["bar"].inner.name == "bar"

    def test_tuple_field_inner_parent_and_name(self, schema):
        for field in schema.fields["baz"].tuple_fields:
            assert field.parent == schema.fields["baz"]
            assert field.name == "baz"

    def test_mapping_field_inner_parent_and_name(self, schema):
        assert schema.fields["bax"].value_field.parent == schema.fields["bax"]
        assert schema.fields["bax"].value_field.name == "bax"
        assert schema.fields["bax"].key_field.parent == schema.fields["bax"]
        assert schema.fields["bax"].key_field.name == "bax"

    def test_simple_field_root(self, schema):
        assert schema.fields["foo"].root == schema
        assert schema.fields["bar"].root == schema

    def test_list_field_inner_root(self, schema):
        assert schema.fields["bar"].inner.root == schema

    def test_tuple_field_inner_root(self, schema):
        for field in schema.fields["baz"].tuple_fields:
            assert field.root == schema

    def test_list_root_inheritance(self, schema):
        class OtherSchema(TestParentAndName.MySchema):
            pass

        schema2 = OtherSchema()

        bar_field = schema.fields["bar"]
        assert isinstance(bar_field, fields.List)
        assert bar_field.inner.root == schema

        bar_field2 = schema2.fields["bar"]
        assert isinstance(bar_field2, fields.List)
        assert bar_field2.inner.root == schema2

    def test_dict_root_inheritance(self):
        class MySchema(Schema):
            foo = fields.Dict(keys=fields.Str(), values=fields.Int())

        class OtherSchema(MySchema):
            pass

        schema = MySchema()
        schema2 = OtherSchema()

        foo_field = schema.fields["foo"]
        assert isinstance(foo_field, fields.Dict)
        assert isinstance(foo_field.key_field, fields.Str)
        assert isinstance(foo_field.value_field, fields.Int)
        assert foo_field.key_field.root == schema
        assert foo_field.value_field.root == schema

        foo_field2 = schema2.fields["foo"]
        assert isinstance(foo_field2, fields.Dict)
        assert isinstance(foo_field2.key_field, fields.Str)
        assert isinstance(foo_field2.value_field, fields.Int)
        assert foo_field2.key_field.root == schema2
        assert foo_field2.value_field.root == schema2

    # Regression test for https://github.com/marshmallow-code/marshmallow/issues/1357
    def test_datetime_list_inner_format(self, schema):
        class MySchema(Schema):
            foo = fields.List(fields.DateTime())
            bar = fields.Tuple((fields.DateTime(),))
            baz = fields.List(fields.Date())
            qux = fields.Tuple((fields.Date(),))

            class Meta:
                datetimeformat = "iso8601"
                dateformat = "iso8601"

        schema = MySchema()
        for field_name in ("foo", "baz"):
            assert schema.fields[field_name].inner.format == "iso8601"
        for field_name in ("bar", "qux"):
            assert schema.fields[field_name].tuple_fields[0].format == "iso8601"

    # Regression test for https://github.com/marshmallow-code/marshmallow/issues/1808
    def test_field_named_parent_has_root(self, schema):
        class MySchema(Schema):
            parent = fields.Raw()

        schema = MySchema()
        assert schema.fields["parent"].root == schema


class TestMetadata:
    @pytest.mark.parametrize("FieldClass", ALL_FIELDS)
    def test_extra_metadata_may_be_added_to_field(self, FieldClass):
        field = FieldClass(
            required=True,
            dump_default=None,
            validate=lambda v: True,
            metadata={"description": "foo", "widget": "select"},
        )
        assert field.metadata == {"description": "foo", "widget": "select"}


class TestErrorMessages:
    class MyField(fields.Field):
        default_error_messages = {"custom": "Custom error message."}

    error_messages = (
        ("required", "Missing data for required field."),
        ("null", "Field may not be null."),
        ("custom", "Custom error message."),
        ("validator_failed", "Invalid value."),
    )

    def test_default_error_messages_get_merged_with_parent_error_messages_cstm_msg(
        self,
    ):
        field = self.MyField()
        assert field.error_messages["custom"] == "Custom error message."
        assert "required" in field.error_messages

    def test_default_error_messages_get_merged_with_parent_error_messages(self):
        field = self.MyField(error_messages={"passed": "Passed error message"})
        assert field.error_messages["passed"] == "Passed error message"

    @pytest.mark.parametrize(("key", "message"), error_messages)
    def test_make_error(self, key, message):
        field = self.MyField()

        error = field.make_error(key)
        assert error.args[0] == message

    def test_make_error_key_doesnt_exist(self):
        with pytest.raises(AssertionError) as excinfo:
            self.MyField().make_error("doesntexist")
        assert "doesntexist" in excinfo.value.args[0]
        assert "MyField" in excinfo.value.args[0]


class TestNestedField:
    @pytest.mark.parametrize("param", ("only", "exclude"))
    def test_nested_only_and_exclude_as_string(self, param):
        with pytest.raises(StringNotCollectionError):
            fields.Nested(Schema, **{param: "foo"})  # type: ignore[arg-type]

    @pytest.mark.parametrize(
        "nested_value",
        [
            {"hello": fields.String()},
            lambda: {"hello": fields.String()},
        ],
    )
    def test_nested_instantiation_from_dict(self, nested_value):
        class MySchema(Schema):
            nested = fields.Nested(nested_value)

        schema = MySchema()

        ret = schema.load({"nested": {"hello": "world"}})
        assert ret == {"nested": {"hello": "world"}}

        with pytest.raises(ValidationError):
            schema.load({"nested": {"x": 1}})

    @pytest.mark.parametrize("schema_unknown", (EXCLUDE, INCLUDE, RAISE))
    @pytest.mark.parametrize("field_unknown", (None, EXCLUDE, INCLUDE, RAISE))
    def test_nested_unknown_override(self, schema_unknown, field_unknown):
        class NestedSchema(Schema):
            class Meta:
                unknown = schema_unknown

        class MySchema(Schema):
            nested = fields.Nested(NestedSchema, unknown=field_unknown)

        if field_unknown == EXCLUDE or (
            schema_unknown == EXCLUDE and not field_unknown
        ):
            assert MySchema().load({"nested": {"x": 1}}) == {"nested": {}}
        elif field_unknown == INCLUDE or (
            schema_unknown == INCLUDE and not field_unknown
        ):
            assert MySchema().load({"nested": {"x": 1}}) == {"nested": {"x": 1}}
        elif field_unknown == RAISE or (schema_unknown == RAISE and not field_unknown):
            with pytest.raises(ValidationError):
                MySchema().load({"nested": {"x": 1}})

    @pytest.mark.parametrize(
        ("param", "fields_list"), [("only", ["foo"]), ("exclude", ["bar"])]
    )
    def test_nested_schema_only_and_exclude(self, param, fields_list):
        class NestedSchema(Schema):
            # We mean to test the use of OrderedSet to specify it explicitly
            # even if it is default
            set_class = OrderedSet
            foo = fields.String()
            bar = fields.String()

        class MySchema(Schema):
            nested = fields.Nested(NestedSchema(), **{param: fields_list})

        assert MySchema().dump({"nested": {"foo": "baz", "bar": "bax"}}) == {
            "nested": {"foo": "baz"}
        }


class TestListNested:
    @pytest.mark.parametrize("param", ("only", "exclude", "dump_only", "load_only"))
    def test_list_nested_only_exclude_dump_only_load_only_propagated_to_nested(
        self, param
    ):
        class Child(Schema):
            name = fields.String()
            age = fields.Integer()

        class Family(Schema):
            children = fields.List(fields.Nested(Child))

        schema = Family(**{param: ["children.name"]})  # type: ignore[arg-type]
        children_field = schema.fields["children"]
        assert isinstance(children_field, fields.List)
        assert isinstance(children_field.inner, fields.Nested)
        assert getattr(children_field.inner.schema, param) == {"name"}

    @pytest.mark.parametrize(
        ("param", "expected_attribute", "expected_dump"),
        (
            ("only", {"name"}, {"children": [{"name": "Lily"}]}),
            ("exclude", {"name", "surname", "age"}, {"children": [{}]}),
        ),
    )
    def test_list_nested_class_only_and_exclude_merged_with_nested(
        self, param, expected_attribute, expected_dump
    ):
        class Child(Schema):
            name = fields.String()
            surname = fields.String()
            age = fields.Integer()

        class Family(Schema):
            children = fields.List(fields.Nested(Child, **{param: ("name", "surname")}))  # type: ignore[arg-type]

        schema = Family(**{param: ["children.name", "children.age"]})  # type: ignore[arg-type]
        children_field = schema.fields["children"]
        assert isinstance(children_field, fields.List)
        assert getattr(children_field.inner, param) == expected_attribute

        family = {"children": [{"name": "Lily", "surname": "Martinez", "age": 15}]}
        assert schema.dump(family) == expected_dump

    def test_list_nested_class_multiple_dumps(self):
        class Child(Schema):
            name = fields.String()
            surname = fields.String()
            age = fields.Integer()

        class Family(Schema):
            children = fields.List(fields.Nested(Child, only=("name", "age")))

        family = {"children": [{"name": "Lily", "surname": "Martinez", "age": 15}]}
        assert Family(only=("children.age",)).dump(family) == {
            "children": [{"age": 15}]
        }
        assert Family(only=("children.name",)).dump(family) == {
            "children": [{"name": "Lily"}]
        }

    @pytest.mark.parametrize(
        ("param", "expected_attribute", "expected_dump"),
        (
            ("only", {"name"}, {"children": [{"name": "Lily"}]}),
            ("exclude", {"name", "surname", "age"}, {"children": [{}]}),
        ),
    )
    def test_list_nested_instance_only_and_exclude_merged_with_nested(
        self, param, expected_attribute, expected_dump
    ):
        class Child(Schema):
            name = fields.String()
            surname = fields.String()
            age = fields.Integer()

        class Family(Schema):
            children = fields.List(fields.Nested(Child(**{param: ("name", "surname")})))  # type: ignore[arg-type]

        schema = Family(**{param: ["children.name", "children.age"]})  # type: ignore[arg-type]
        children_field = schema.fields["children"]
        assert isinstance(children_field, fields.List)
        assert isinstance(children_field.inner, fields.Nested)
        assert getattr(children_field.inner.schema, param) == expected_attribute

        family = {"children": [{"name": "Lily", "surname": "Martinez", "age": 15}]}
        assert schema.dump(family) == expected_dump

    def test_list_nested_instance_multiple_dumps(self):
        class Child(Schema):
            name = fields.String()
            surname = fields.String()
            age = fields.Integer()

        class Family(Schema):
            children = fields.List(fields.Nested(Child(only=("name", "age"))))

        family = {"children": [{"name": "Lily", "surname": "Martinez", "age": 15}]}
        assert Family(only=("children.age",)).dump(family) == {
            "children": [{"age": 15}]
        }
        assert Family(only=("children.name",)).dump(family) == {
            "children": [{"name": "Lily"}]
        }

    @pytest.mark.parametrize(
        ("param", "expected_attribute", "expected_dump"),
        (
            ("only", {"name"}, {"children": [{"name": "Lily"}]}),
            ("exclude", {"name", "surname", "age"}, {"children": [{}]}),
        ),
    )
    def test_list_nested_lambda_only_and_exclude_merged_with_nested(
        self, param, expected_attribute, expected_dump
    ):
        class Child(Schema):
            name = fields.String()
            surname = fields.String()
            age = fields.Integer()

        class Family(Schema):
            children = fields.List(
                fields.Nested(lambda: Child(**{param: ("name", "surname")}))  # type: ignore[arg-type]
            )

        schema = Family(**{param: ["children.name", "children.age"]})  # type: ignore[arg-type]
        children_field = schema.fields["children"]
        assert isinstance(children_field, fields.List)
        assert isinstance(children_field.inner, fields.Nested)
        assert getattr(children_field.inner.schema, param) == expected_attribute

        family = {"children": [{"name": "Lily", "surname": "Martinez", "age": 15}]}
        assert schema.dump(family) == expected_dump

    def test_list_nested_partial_propagated_to_nested(self):
        class Child(Schema):
            name = fields.String(required=True)
            age = fields.Integer(required=True)

        class Family(Schema):
            children = fields.List(fields.Nested(Child))

        payload = {"children": [{"name": "Lucette"}]}

        for val in (True, ("children.age",)):
            result = Family(partial=val).load(payload)
            assert result["children"][0]["name"] == "Lucette"
            result = Family().load(payload, partial=val)
            assert result["children"][0]["name"] == "Lucette"

        for val in (False, ("children.name",)):
            with pytest.raises(ValidationError) as excinfo:
                result = Family(partial=val).load(payload)
            assert excinfo.value.args[0] == {
                "children": {0: {"age": ["Missing data for required field."]}}
            }
            with pytest.raises(ValidationError) as excinfo:
                result = Family().load(payload, partial=val)
            assert excinfo.value.args[0] == {
                "children": {0: {"age": ["Missing data for required field."]}}
            }


class TestTupleNested:
    @pytest.mark.parametrize("param", ("dump_only", "load_only"))
    def test_tuple_nested_only_exclude_dump_only_load_only_propagated_to_nested(
        self, param
    ):
        class Child(Schema):
            name = fields.String()
            age = fields.Integer()

        class Family(Schema):
            children = fields.Tuple((fields.Nested(Child), fields.Nested(Child)))

        schema = Family(**{param: ["children.name"]})  # type: ignore[arg-type]
        children_field = schema.fields["children"]
        assert isinstance(children_field, fields.Tuple)
        field1, field2 = children_field.tuple_fields
        assert isinstance(field1, fields.Nested)
        assert isinstance(field2, fields.Nested)
        assert getattr(field1.schema, param) == {"name"}
        assert getattr(field2.schema, param) == {"name"}

    def test_tuple_nested_partial_propagated_to_nested(self):
        class Child(Schema):
            name = fields.String(required=True)
            age = fields.Integer(required=True)

        class Family(Schema):
            children = fields.Tuple((fields.Nested(Child),))

        payload = {"children": [{"name": "Lucette"}]}

        for val in (True, ("children.age",)):
            result = Family(partial=val).load(payload)
            assert result["children"][0]["name"] == "Lucette"
            result = Family().load(payload, partial=val)
            assert result["children"][0]["name"] == "Lucette"

        for val in (False, ("children.name",)):
            with pytest.raises(ValidationError) as excinfo:
                result = Family(partial=val).load(payload)
            assert excinfo.value.args[0] == {
                "children": {0: {"age": ["Missing data for required field."]}}
            }
            with pytest.raises(ValidationError) as excinfo:
                result = Family().load(payload, partial=val)
            assert excinfo.value.args[0] == {
                "children": {0: {"age": ["Missing data for required field."]}}
            }


class TestDictNested:
    @pytest.mark.parametrize("param", ("only", "exclude", "dump_only", "load_only"))
    def test_dict_nested_only_exclude_dump_only_load_only_propagated_to_nested(
        self, param
    ):
        class Child(Schema):
            name = fields.String()
            age = fields.Integer()

        class Family(Schema):
            children = fields.Dict(values=fields.Nested(Child))

        schema = Family(**{param: ["children.name"]})  # type: ignore[arg-type]
        children_field = schema.fields["children"]
        assert isinstance(children_field, fields.Dict)
        assert isinstance(children_field.value_field, fields.Nested)
        assert getattr(children_field.value_field.schema, param) == {"name"}

    @pytest.mark.parametrize(
        ("param", "expected"),
        (("only", {"name"}), ("exclude", {"name", "surname", "age"})),
    )
    def test_dict_nested_only_and_exclude_merged_with_nested(self, param, expected):
        class Child(Schema):
            name = fields.String()
            surname = fields.String()
            age = fields.Integer()

        class Family(Schema):
            children = fields.Dict(
                values=fields.Nested(Child, **{param: ("name", "surname")})  # type: ignore[arg-type]
            )

        schema = Family(**{param: ["children.name", "children.age"]})  # type: ignore[arg-type]
        children_field = schema.fields["children"]
        assert isinstance(children_field, fields.Dict)
        assert getattr(children_field.value_field, param) == expected

    def test_dict_nested_partial_propagated_to_nested(self):
        class Child(Schema):
            name = fields.String(required=True)
            age = fields.Integer(required=True)

        class Family(Schema):
            children = fields.Dict(values=fields.Nested(Child))

        payload = {"children": {"daughter": {"name": "Lucette"}}}

        for val in (True, ("children.age",)):
            result = Family(partial=val).load(payload)
            assert result["children"]["daughter"]["name"] == "Lucette"
            result = Family().load(payload, partial=val)
            assert result["children"]["daughter"]["name"] == "Lucette"

        for val in (False, ("children.name",)):
            with pytest.raises(ValidationError) as excinfo:
                result = Family(partial=val).load(payload)
            assert excinfo.value.args[0] == {
                "children": {
                    "daughter": {"value": {"age": ["Missing data for required field."]}}
                }
            }
            with pytest.raises(ValidationError) as excinfo:
                result = Family().load(payload, partial=val)
            assert excinfo.value.args[0] == {
                "children": {
                    "daughter": {"value": {"age": ["Missing data for required field."]}}
                }
            }
