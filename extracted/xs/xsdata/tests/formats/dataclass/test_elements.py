from dataclasses import make_dataclass
from decimal import Decimal
from unittest import mock
from unittest.case import TestCase
from xml.etree.ElementTree import QName

from tests.fixtures.models import (
    ChoiceType,
    ExtendedType,
    Paragraph,
    TypeA,
    TypeB,
    TypeC,
    TypeD,
    TypeDuplicate,
    UnionType,
)
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlType, XmlVar
from xsdata.utils.testing import XmlMetaFactory, XmlVarFactory


class XmlValTests(TestCase):
    def setUp(self) -> None:
        self.context = XmlContext()

    def test_property_qname(self) -> None:
        var = XmlVarFactory.create(name="a", local_name="A", namespaces=("B",))
        self.assertEqual("{B}A", var.qname)

    def test_property_wrapper_qname(self) -> None:
        var = XmlVarFactory.create(
            name="a", local_name="A", wrapper="AA", namespaces=("B",)
        )
        self.assertEqual("{B}AA", var.wrapper_qname)

    def test_property_clazz(self) -> None:
        var = XmlVarFactory.create(name="foo")
        self.assertIsNone(var.clazz)

        var = XmlVarFactory.create(name="foo", types=(TypeA,))
        self.assertEqual(TypeA, var.clazz)

    def test_property_is_clazz_union(self) -> None:
        var = XmlVarFactory.create(name="foo", types=(TypeA,))
        self.assertFalse(var.is_clazz_union)

        var = XmlVarFactory.create(name="foo", types=(TypeA, int))
        self.assertTrue(var.is_clazz_union)

    def test_property_element_types(self) -> None:
        meta = self.context.build(ChoiceType)
        var = meta.choices[0]
        self.assertEqual(
            {TypeA, TypeB, int, float, QName, UnionType, Decimal}, var.element_types
        )

    def test_find_choice(self) -> None:
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENTS,
            name="foo",
            elements={
                "{a}a": XmlVarFactory.create(
                    xml_type=XmlType.ELEMENT, name="a", namespaces=("a",)
                ),
                "b": XmlVarFactory.create(xml_type=XmlType.ELEMENT, name="b"),
            },
        )

        self.assertIsNone(var.find_choice("a"))
        self.assertEqual("a", var.find_choice("{a}a").name)
        self.assertEqual("b", var.find_choice("b").name)

        var.elements.clear()
        var.wildcards = [
            XmlVarFactory.create(
                xml_type=XmlType.WILDCARD,
                name="target",
                namespaces=("foo",),
            ),
            XmlVarFactory.create(
                xml_type=XmlType.WILDCARD,
                name="other",
                namespaces=("!foo",),
            ),
        ]

        self.assertEqual(var.wildcards[1], var.find_choice("{a}a"))
        self.assertEqual(var.wildcards[0], var.find_choice("{foo}a"))

    def test_find_value_choice(self) -> None:
        meta = self.context.build(ChoiceType)
        var = meta.choices[0]

        self.assertEqual(var.elements["tokens"], var.find_value_choice(["1.2"], False))
        self.assertIsNone(var.find_value_choice([], False))
        self.assertEqual(var.elements["qname"], var.find_value_choice("foo", False))
        self.assertEqual(var.elements["int"], var.find_value_choice(1, False))
        self.assertEqual(var.elements["a"], var.find_value_choice(TypeA(1), True))
        der = make_dataclass("Der", fields=[], bases=(TypeA,))
        self.assertEqual(var.elements["a"], var.find_value_choice(der(1), True))

    def test_is_optional(self) -> None:
        var = XmlVarFactory.create(xml_type=XmlType.ATTRIBUTE, name="att")

        self.assertTrue(var.is_optional(None))
        self.assertFalse(var.is_optional("foo"))

        var.default = lambda: [1, 2, 3]
        self.assertTrue(var.is_optional([1, 2, 3]))

        var.required = True
        self.assertFalse(var.is_optional([1, 2, 3]))

    def test_match_namespace(self) -> None:
        var = XmlVarFactory.create(xml_type=XmlType.WILDCARD, name="foo")
        self.assertTrue(var.match_namespace("a"))

        var = XmlVarFactory.create(
            xml_type=XmlType.WILDCARD, name="foo", namespaces=("tns",)
        )
        self.assertFalse(var.match_namespace("a"))
        self.assertTrue(var.match_namespace("{tns}a"))

        var = XmlVarFactory.create(
            xml_type=XmlType.WILDCARD, name="foo", namespaces=("##any",)
        )
        self.assertTrue(var.match_namespace("a"))
        self.assertTrue(var.match_namespace("{tns}a"))

        var = XmlVarFactory.create(
            xml_type=XmlType.WILDCARD, name="foo", namespaces=("",)
        )
        self.assertTrue(var.match_namespace("a"))
        self.assertFalse(var.match_namespace("{tns}a"))

        var = XmlVarFactory.create(
            xml_type=XmlType.WILDCARD, name="foo", namespaces=("!tns",)
        )
        self.assertTrue(var.match_namespace("{foo}a"))
        self.assertFalse(var.match_namespace("{tns}a"))

        var.namespace_matches["{tns}cached"] = True
        self.assertTrue(var.match_namespace("{tns}cached"))


class XmlMetaTests(TestCase):
    def setUp(self) -> None:
        self.context = XmlContext()
        self.meta = XmlMetaFactory.create(
            clazz=TypeA,
            qname="a",
            choices=[],
            wildcards=[],
            attributes={},
            elements={},
            any_attributes=[],
        )

    def test__repr__(self) -> None:
        self.assertIn("XmlMeta(", repr(self.meta))

    def test_property_element_types(self) -> None:
        meta = self.context.build(UnionType)
        self.assertEqual({TypeA, TypeB, TypeC, TypeD}, meta.element_types)

    def test_find_attribute(self) -> None:
        a = XmlVarFactory.create(xml_type=XmlType.ATTRIBUTE, name="a")
        b = XmlVarFactory.create(xml_type=XmlType.ATTRIBUTE, name="b")

        self.meta.attributes[a.qname] = a
        self.meta.attributes[b.qname] = b

        self.assertEqual(a, self.meta.find_attribute("a"))
        self.assertEqual(b, self.meta.find_attribute("b"))

    @mock.patch.object(XmlVar, "match_namespace")
    def test_find_any_attributes(self, mock_match_namespace) -> None:
        mock_match_namespace.side_effect = [False, False, False, True]

        attributes = [
            XmlVarFactory.create(xml_type=XmlType.ATTRIBUTES, name="any"),
            XmlVarFactory.create(
                xml_type=XmlType.ATTRIBUTES, local_name="other", name="any"
            ),
        ]
        self.meta.any_attributes = attributes

        self.assertIsNone(self.meta.find_any_attributes("a"))
        self.assertEqual(attributes[1], self.meta.find_any_attributes("a"))

        mock_match_namespace.assert_has_calls([mock.call("a") for _ in range(4)])

    def test_find_wildcard(self) -> None:
        wildcards = [
            XmlVarFactory.create(xml_type=XmlType.WILDCARD, namespaces=("a",)),
            XmlVarFactory.create(xml_type=XmlType.WILDCARD, namespaces=("b",)),
            XmlVarFactory.create(
                xml_type=XmlType.WILDCARD,
                namespaces=["##any"],
                elements={
                    "{c}root": XmlVarFactory.create(
                        xml_type=XmlType.ELEMENT, name="root", namespaces=("c",)
                    ),
                },
            ),
        ]

        self.assertIsNone(self.meta.find_wildcard("a"))
        self.meta.wildcards = wildcards

        self.assertIs(wildcards[0], self.meta.find_wildcard("{a}root"))
        self.assertIs(wildcards[1], self.meta.find_wildcard("{b}root"))
        self.assertIs(
            wildcards[2].elements["{c}root"], self.meta.find_wildcard("{c}root")
        )
        self.assertIs(wildcards[2], self.meta.find_wildcard("{c}random"))

    def test_find_any_wildcard(self) -> None:
        meta = self.context.build(TypeDuplicate)
        self.assertIsNone(meta.find_any_wildcard())

        meta = self.context.build(ExtendedType)
        self.assertEqual("wildcard", meta.find_any_wildcard().qname)

    def test_find_children(self) -> None:
        meta = self.context.build(TypeDuplicate)
        self.assertIsNone(next(meta.find_children("a"), None))
        self.assertEqual(["x", "x1"], [el.name for el in meta.find_children("x")])

        meta = self.context.build(TypeB)
        self.assertEqual("x", next(meta.find_children("x")).qname)
        self.assertEqual("y", next(meta.find_children("y")).qname)

        meta = self.context.build(ChoiceType)
        self.assertIsNone(next(meta.find_children("404"), None))
        self.assertEqual("a", next(meta.find_children("a")).qname)
        self.assertEqual("b", next(meta.find_children("b")).qname)
        self.assertEqual("int", next(meta.find_children("int")).qname)

        meta = self.context.build(Paragraph)
        self.assertEqual("content", next(meta.find_children("404")).qname)
        self.assertTrue(next(meta.find_children("content")).is_wildcard)
