from collections.abc import Iterator
from unittest import TestCase

from xsdata.models.enums import Namespace
from xsdata.models.xsd import Import, Include, Override, Redefine, Schema


class SchemaTests(TestCase):
    def test_meta(self) -> None:
        schema = Schema()
        self.assertEqual("schema", schema.Meta.name)
        self.assertEqual(Namespace.XS.uri, schema.Meta.namespace)

    def test_sub_schemas(self) -> None:
        imports = [
            Import(schema_location="../foo.xsd"),
            Import(schema_location="../bar.xsd"),
        ]
        includes = [
            Include(schema_location="common.xsd"),
            Include(schema_location="uncommon.xsd"),
        ]
        redefines = [
            Redefine(schema_location="a.xsd"),
            Redefine(schema_location="b.xsd"),
        ]
        overrides = [
            Override(schema_location="a.xsd"),
            Override(schema_location="b.xsd"),
        ]
        schema = Schema(
            imports=imports, includes=includes, redefines=redefines, overrides=overrides
        )

        actual = schema.included()
        expected = imports + includes + redefines + overrides
        self.assertIsInstance(actual, Iterator)
        self.assertEqual(expected, list(actual))

        schema = Schema()
        self.assertEqual([], list(schema.included()))
