from collections.abc import Iterator
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import mock

from xsdata.codegen.exceptions import CodegenError
from xsdata.codegen.models import Class
from xsdata.codegen.writer import CodeWriter
from xsdata.formats.dataclass.generator import DataclassGenerator
from xsdata.formats.mixins import AbstractGenerator, GeneratorResult
from xsdata.models.config import GeneratorConfig
from xsdata.utils.testing import ClassFactory, FactoryTestCase


class NoneGenerator(AbstractGenerator):
    def render(self, classes: list[Class]) -> Iterator[GeneratorResult]:
        pass


class CodeWriterTests(FactoryTestCase):
    def setUp(self) -> None:
        config = GeneratorConfig()
        generator = NoneGenerator(config)
        self.writer = CodeWriter(generator)

    @mock.patch.object(NoneGenerator, "render_header")
    @mock.patch.object(NoneGenerator, "render")
    @mock.patch.object(NoneGenerator, "normalize_packages")
    def test_write(
        self, mock_normalize_packages, mock_render, mock_render_header
    ) -> None:
        classes = ClassFactory.list(2)
        with TemporaryDirectory() as tmpdir:
            mock_render.return_value = [
                GeneratorResult(Path(f"{tmpdir}/foo/a.py"), "file", "aAa"),
                GeneratorResult(Path(f"{tmpdir}/bar/b.py"), "file", "bBb"),
                GeneratorResult(Path(f"{tmpdir}/c.py"), "file", " "),
            ]
            mock_render_header.return_value = "// Head\n"
            self.writer.write(classes)

            self.assertEqual("// Head\naAa", Path(f"{tmpdir}/foo/a.py").read_text())
            self.assertEqual("// Head\nbBb", Path(f"{tmpdir}/bar/b.py").read_text())
            self.assertFalse(Path(f"{tmpdir}/c.py").exists())
            mock_normalize_packages.assert_called_once_with(classes)

    def test_from_config(self) -> None:
        CodeWriter.unregister_generator("dataclasses")
        config = GeneratorConfig()

        with self.assertRaises(CodegenError):
            CodeWriter.from_config(config)

        CodeWriter.register_generator("dataclasses", DataclassGenerator)
        writer = CodeWriter.from_config(config)
        self.assertIsInstance(writer.generator, DataclassGenerator)
