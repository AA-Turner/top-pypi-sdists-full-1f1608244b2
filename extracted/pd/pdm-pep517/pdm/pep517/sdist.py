import io
import itertools
import os
import tarfile
from copy import copy
from posixpath import join as pjoin
from typing import Any, Iterator

from pdm.pep517._vendor import tomli, tomli_w
from pdm.pep517.base import Builder


def normalize_file_permissions(st_mode: int) -> int:
    """
    Normalizes the permission bits in the st_mode field from stat to 644/755

    Popular VCSs only track whether a file is executable or not. The exact
    permissions can vary on systems with different umasks. Normalising
    to 644 (non executable) or 755 (executable) makes builds more reproducible.
    """
    # Set 644 permissions, leaving higher bits of st_mode unchanged
    new_mode = (st_mode | 0o644) & ~0o133
    if st_mode & 0o100:
        new_mode |= 0o111  # Executable: 644 -> 755

    return new_mode


def clean_tarinfo(tar_info: tarfile.TarInfo) -> tarfile.TarInfo:
    """
    Clean metadata from a TarInfo object to make it more reproducible.

        - Set uid & gid to 0
        - Set uname and gname to ""
        - Normalise permissions to 644 or 755
        - Set mtime if not None
    """
    ti = copy(tar_info)
    ti.uid = 0
    ti.gid = 0
    ti.uname = ""
    ti.gname = ""
    ti.mode = normalize_file_permissions(ti.mode)
    if "SOURCE_DATE_EPOCH" in os.environ:
        ti.mtime = int(os.environ["SOURCE_DATE_EPOCH"])

    return ti


class SdistBuilder(Builder):
    """This build should be performed for PDM project only."""

    def _find_files_iter(self, for_sdist: bool = False) -> Iterator[str]:
        return itertools.chain(
            super()._find_files_iter(for_sdist), self.find_license_files()
        )

    def build(self, build_dir: str, **kwargs: Any) -> str:
        if not os.path.exists(build_dir):
            os.makedirs(build_dir, exist_ok=True)

        version = self.meta_version

        target = os.path.join(build_dir, f"{self.meta.project_name}-{version}.tar.gz")
        tar = tarfile.open(target, mode="w:gz", format=tarfile.PAX_FORMAT)

        try:
            tar_dir = f"{self.meta.project_name}-{version}"

            files_to_add = self.find_files_to_add(True)

            for relpath in files_to_add:
                if str(relpath) == "pyproject.toml":
                    self._add_pyproject(tar, tar_dir)
                else:
                    tarinfo = tar.gettarinfo(relpath, pjoin(tar_dir, relpath))
                    tarinfo = clean_tarinfo(tarinfo)
                    if tarinfo.isreg():
                        with open(relpath, "rb") as f:
                            tar.addfile(tarinfo, f)
                    else:
                        tar.addfile(tarinfo)
                print(f" - Adding {relpath}")

            pkg_info = self.format_pkginfo(False).encode("utf-8")
            tarinfo = clean_tarinfo(tarfile.TarInfo(pjoin(tar_dir, "PKG-INFO")))
            tarinfo.size = len(pkg_info)
            tar.addfile(tarinfo, io.BytesIO(pkg_info))
            print(" - Adding PKG-INFO")
        finally:
            tar.close()

        return target

    def _add_pyproject(self, tar: tarfile.TarFile, tar_dir: str) -> None:
        """Rewrites the pyproject.toml before adding to tarball.
        This is mainly aiming at fixing the version number in pyproject.toml
        """
        with open(self.location / "pyproject.toml", "rb") as f:
            pyproject = tomli.load(f)
        if self.meta.dynamic and "version" in self.meta.dynamic:
            self.meta.data["version"] = self.meta_version
            self.meta.data["dynamic"].remove("version")
        pyproject["project"] = self.meta.data
        name = "pyproject.toml"
        tarinfo = tar.gettarinfo(name, pjoin(tar_dir, name))
        bio = io.BytesIO()
        tomli_w.dump(pyproject, bio)
        tarinfo.size = len(bio.getvalue())
        tarinfo = clean_tarinfo(tarinfo)
        bio.seek(0)
        tar.addfile(tarinfo, bio)
