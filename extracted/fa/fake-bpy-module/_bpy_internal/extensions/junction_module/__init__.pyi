import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class JunctionModuleHandle:
    def register_module(self):
        """Register the base module in sys.modules."""

    def register_submodule(self, submodule_name, dirpath):
        """

        :param submodule_name:
        :param dirpath:
        """

    def rename_directory(self, submodule_name, dirpath):
        """

        :param submodule_name:
        :param dirpath:
        """

    def rename_submodule(self, submodule_name_src, submodule_name_dst):
        """

        :param submodule_name_src:
        :param submodule_name_dst:
        """

    def submodule_items(self): ...
    def unregister_module(self):
        """Unregister the base module in sys.modules.
        Keep everything except the modules name (allowing re-registration).

        """

    def unregister_submodule(self, submodule_name):
        """

        :param submodule_name:
        """
