"""
This module contains application values that remain unchanged during runtime.

bpy.app.handlers.rst
bpy.app.translations.rst
bpy.app.icons.rst
bpy.app.timers.rst

:maxdepth: 1
:caption: Submodules

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.stub_internal.rna_enums

from . import handlers as handlers
from . import icons as icons
from . import timers as timers
from . import translations as translations

def help_text(all: bool | None = False) -> None:
    """Return the help text as a string.

    :param all: Return all arguments, even those which aren't available for the current platform.
    :type all: bool | None
    """

def is_job_running(job_type: bpy.stub_internal.rna_enums.WmJobTypeItems) -> None:
    """Check whether a job of the given type is running.

    :param job_type: job type in `rna_enum_wm_job_type_items`.
    :type job_type: bpy.stub_internal.rna_enums.WmJobTypeItems
    :return: Whether a job of the given type is currently running.
    """

alembic: typing.Any
""" Constant value bpy.app.alembic(supported=True, version=(1, 8, 3), version_string=' 1,  8,  3')
"""

autoexec_fail: typing.Any
""" Undocumented, consider contributing.
"""

autoexec_fail_message: typing.Any
""" Undocumented, consider contributing.
"""

autoexec_fail_quiet: typing.Any
""" Undocumented, consider contributing.
"""

background: typing.Any
""" Boolean, True when blender is running without a user interface (started with -b)
"""

binary_path: str
""" The location of Blender's executable, useful for utilities that open new instances. Read-only unless Blender is built as a Python module - in this case the value is an empty string which script authors may point to a Blender binary.
"""

build_branch: typing.Any
""" The branch this blender instance was built from
"""

build_cflags: typing.Any
""" C compiler flags
"""

build_commit_date: typing.Any
""" The date of commit this blender instance was built
"""

build_commit_time: typing.Any
""" The time of commit this blender instance was built
"""

build_commit_timestamp: typing.Any
""" The unix timestamp of commit this blender instance was built
"""

build_cxxflags: typing.Any
""" C++ compiler flags
"""

build_date: typing.Any
""" The date this blender instance was built
"""

build_hash: typing.Any
""" The commit hash this blender instance was built with
"""

build_linkflags: typing.Any
""" Binary linking flags
"""

build_options: typing.Any
""" Constant value bpy.app.build_options(bullet=True, codec_avi=False, codec_ffmpeg=True, codec_sndfile=True, compositor_cpu=True, cycles=True, cycles_osl=True, freestyle=True, image_cineon=True, image_dds=True, image_hdr=True, image_openexr=True, image_openjpeg=True, image_tiff=True, image_webp=True, input_ndof=True, audaspace=True, international=True, openal=True, opensubdiv=True, sdl=False, coreaudio=False, jack=False, pulseaudio=False, wasapi=False, libmv=True, mod_oceansim=True, mod_remesh=True, collada=True, io_wavefront_obj=True, io_ply=True, io_stl=True, io_fbx=True, io_gpencil=True, opencolorio=True, openmp=False, openvdb=True, alembic=True, usd=True, fluid=True, xr_openxr=True, potrace=True, pugixml=True, haru=True, experimental_features=True)
"""

build_platform: typing.Any
""" The platform this blender instance was built for
"""

build_system: typing.Any
""" Build system used
"""

build_time: typing.Any
""" The time this blender instance was built
"""

build_type: typing.Any
""" The type of build (Release, Debug)
"""

debug: typing.Any
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name)
"""

debug_depsgraph: typing.Any
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name)
"""

debug_depsgraph_build: typing.Any
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name)
"""

debug_depsgraph_eval: typing.Any
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name)
"""

debug_depsgraph_pretty: typing.Any
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name)
"""

debug_depsgraph_tag: typing.Any
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name)
"""

debug_depsgraph_time: typing.Any
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name)
"""

debug_events: typing.Any
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name)
"""

debug_ffmpeg: typing.Any
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name)
"""

debug_freestyle: typing.Any
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name)
"""

debug_handlers: typing.Any
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name)
"""

debug_io: typing.Any
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name)
"""

debug_python: typing.Any
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name)
"""

debug_simdata: typing.Any
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name)
"""

debug_value: typing.Any
""" Short, number which can be set to non-zero values for testing purposes
"""

debug_wm: typing.Any
""" Boolean, for debug info (started with --debug / --debug-* matching this attribute name)
"""

driver_namespace: typing.Any
""" Dictionary for drivers namespace, editable in-place, reset on file load (read-only)
"""

factory_startup: typing.Any
""" Boolean, True when blender is running with --factory-startup)
"""

ffmpeg: typing.Any
""" Constant value bpy.app.ffmpeg(supported=True, avcodec_version=(61, 19, 101), avcodec_version_string='61, 19, 101', avdevice_version=(61, 3, 100), avdevice_version_string='61,  3, 100', avformat_version=(61, 7, 100), avformat_version_string='61,  7, 100', avutil_version=(59, 39, 100), avutil_version_string='59, 39, 100', swscale_version=(8, 3, 100), swscale_version_string=' 8,  3, 100')
"""

module: typing.Any
""" Boolean, True when running Blender as a python module
"""

ocio: typing.Any
""" Constant value bpy.app.ocio(supported=True, version=(2, 4, 1), version_string=' 2,  4,  1')
"""

oiio: typing.Any
""" Constant value bpy.app.oiio(supported=True, version=(3, 0, 6), version_string=' 3,  0,  6')
"""

online_access: typing.Any
""" Boolean, true when internet access is allowed by Blender & 3rd party scripts (read-only)
"""

online_access_override: typing.Any
""" Boolean, true when internet access preference is overridden by the command line (read-only)
"""

opensubdiv: typing.Any
""" Constant value bpy.app.opensubdiv(supported=True, version=(3, 6, 0), version_string=' 3,  6,  0')
"""

openvdb: typing.Any
""" Constant value bpy.app.openvdb(supported=True, version=(12, 0, 0), version_string='12,  0,  0')
"""

portable: typing.Any
""" Boolean, True unless blender was built to reference absolute paths (on UNIX).
"""

python_args: typing.Any
""" Leading arguments to use when calling Python directly (via sys.executable). These arguments match settings Blender uses to ensure Python runs with a compatible environment (read-only).
"""

render_icon_size: typing.Any
""" Reference size for icon/preview renders (read-only)
"""

render_preview_size: typing.Any
""" Reference size for icon/preview renders (read-only)
"""

sdl: typing.Any
""" Constant value bpy.app.sdl(supported=False, version=(0, 0, 0), version_string='Unknown')
"""

tempdir: typing.Any
""" String, the temp directory used by blender (read-only)
"""

usd: typing.Any
""" Constant value bpy.app.usd(supported=True, version=(0, 25, 2), version_string=' 0, 25,  2')
"""

use_event_simulate: typing.Any
""" Boolean, for application behavior (started with --enable-* matching this attribute name)
"""

use_userpref_skip_save_on_exit: typing.Any
""" Boolean, for application behavior (started with --enable-* matching this attribute name)
"""

version: tuple[int, int, int]
""" The Blender version as a tuple of 3 numbers (major, minor, micro). eg. (4, 3, 1)
"""

version_cycle: typing.Any
""" The release status of this build alpha/beta/rc/release
"""

version_file: typing.Any
""" The Blender File version, as a tuple of 3 numbers (major, minor, file sub-version), that will be used to save a .blend file. The last item in this tuple indicates the file sub-version, which is different from the release micro version (the last item of the bpy.app.version tuple). The file sub-version can be incremented multiple times while a Blender version is under development. This value is, and should be, used for handling compatibility changes between Blender versions
"""

version_string: typing.Any
""" The Blender version formatted as a string
"""
