import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def activate(*, template_id=None, reload_scripts=False): ...
def import_from_id(template_id, *, ignore_not_found=False): ...
def import_from_path(path, *, ignore_not_found=False): ...
def reset(*, reload_scripts=False):
    """Sets default state."""
