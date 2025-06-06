import pathlib
from typing import Sequence

from pysen import (
    CommandBase,
    ComponentBase,
    Config,
    PluginBase,
    PluginConfig,
    RunOptions,
    SingleFileLintCommandBase,
    Source,
    process_utils,
)
from pysen.reporter import Reporter
from pysen.runner_options import PathContext
from pysen.types import TargetName


def golint() -> PluginBase:
    return GolintPlugin()


class GolintPlugin(PluginBase):
    def load(
        self, file_path: pathlib.Path, config: PluginConfig, root: Config
    ) -> Sequence[ComponentBase]:
        if root.lint and root.lint.source:
            source = root.lint.source
        else:
            source = Source(includes=["."])
        return [GolintComponent(source)]


class GolintComponent(ComponentBase):
    def __init__(self, source: Source) -> None:
        self._source = source

    @property
    def targets(self) -> Sequence[TargetName]:
        return ["lint"]

    def create_command(
        self, target: str, paths: PathContext, options: RunOptions
    ) -> CommandBase:
        return GolintCommand(paths.base_dir, self._source)


class GolintCommand(SingleFileLintCommandBase):
    @property
    def name(self) -> str:
        return "golint"

    @property
    def has_side_effects(self) -> bool:
        return False

    def filter(self, file_path: pathlib.Path) -> bool:
        return file_path.suffix in {".go"}

    def check(self, file_path: pathlib.Path, reporter: Reporter) -> bool:
        returncode, _, _ = process_utils.run(
            ("golint", "-set_exit_status", str(file_path)), reporter
        )
        return returncode == 0
