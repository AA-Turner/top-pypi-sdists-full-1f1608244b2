import pathlib
from typing import Optional, Sequence

from pysen.command import CommandBase
from pysen.component import LintComponentBase
from pysen.isort import IsortCommand
from pysen.runner_options import PathContext, RunOptions
from pysen.source import Source


class Isort(LintComponentBase):
    def __init__(
        self,
        name: str = "isort",
        source: Optional[Source] = None,
        settings_dir: Optional[pathlib.Path] = None,
    ) -> None:
        super().__init__(name, source)
        self._settings_dir = settings_dir or pathlib.Path(".")

    @property
    def targets(self) -> Sequence[str]:
        return ["lint", "format"]

    def create_command(
        self, target: str, paths: PathContext, options: RunOptions
    ) -> CommandBase:
        paths = PathContext(base_dir=paths.base_dir, settings_dir=self._settings_dir)
        if target == "lint":
            return IsortCommand(self.name, paths, self.source, False)
        elif target == "format":
            return IsortCommand(self.name, paths, self.source, True)

        raise AssertionError(f"unknown {target}")
