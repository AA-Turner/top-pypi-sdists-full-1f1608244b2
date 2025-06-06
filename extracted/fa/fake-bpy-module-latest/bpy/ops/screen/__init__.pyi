import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.stub_internal.rna_enums

def actionzone(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: int | None = 0,
) -> None:
    """Handle area action zones for mouse actions/gestures

    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Modifier state
    :type modifier: int | None
    """

def animation_cancel(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    restore_frame: bool | None = True,
) -> None:
    """Cancel animation, returning to the original frame

    :type execution_context: int | str | None
    :type undo: bool | None
    :param restore_frame: Restore Frame, Restore the frame when animation was initialized
    :type restore_frame: bool | None
    """

def animation_play(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    reverse: bool | None = False,
    sync: bool | None = False,
) -> None:
    """Play animation

    :type execution_context: int | str | None
    :type undo: bool | None
    :param reverse: Play in Reverse, Animation is played backwards
    :type reverse: bool | None
    :param sync: Sync, Drop frames to maintain framerate
    :type sync: bool | None
    """

def animation_step(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Step through animation by position

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def area_close(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Close selected area

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def area_dupli(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Duplicate selected area into new window

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def area_join(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    source_xy: collections.abc.Iterable[int] | None = (0, 0),
    target_xy: collections.abc.Iterable[int] | None = (0, 0),
) -> None:
    """Join selected areas into new window

    :type execution_context: int | str | None
    :type undo: bool | None
    :param source_xy: Source location
    :type source_xy: collections.abc.Iterable[int] | None
    :param target_xy: Target location
    :type target_xy: collections.abc.Iterable[int] | None
    """

def area_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    x: int | None = 0,
    y: int | None = 0,
    delta: int | None = 0,
) -> None:
    """Move selected area edges

    :type execution_context: int | str | None
    :type undo: bool | None
    :param x: X
    :type x: int | None
    :param y: Y
    :type y: int | None
    :param delta: Delta
    :type delta: int | None
    """

def area_options(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Operations for splitting and merging

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def area_split(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["HORIZONTAL", "VERTICAL"] | None = "HORIZONTAL",
    factor: float | None = 0.5,
    cursor: collections.abc.Iterable[int] | None = (0, 0),
) -> None:
    """Split selected area into new windows

    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction
    :type direction: typing.Literal['HORIZONTAL','VERTICAL'] | None
    :param factor: Factor
    :type factor: float | None
    :param cursor: Cursor
    :type cursor: collections.abc.Iterable[int] | None
    """

def area_swap(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    cursor: collections.abc.Iterable[int] | None = (0, 0),
) -> None:
    """Swap selected areas screen positions

    :type execution_context: int | str | None
    :type undo: bool | None
    :param cursor: Cursor
    :type cursor: collections.abc.Iterable[int] | None
    """

def back_to_previous(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Revert back to the original screen layout, before fullscreen area overlay

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def delete(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Delete active screen

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def drivers_editor_show(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Show drivers editor in a separate window

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def frame_jump(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    end: bool | None = False,
) -> None:
    """Jump to first/last frame in frame range

    :type execution_context: int | str | None
    :type undo: bool | None
    :param end: Last Frame, Jump to the last frame of the frame range
    :type end: bool | None
    """

def frame_offset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    delta: int | None = 0,
) -> None:
    """Move current frame forward/backward by a given number

    :type execution_context: int | str | None
    :type undo: bool | None
    :param delta: Delta
    :type delta: int | None
    """

def header_toggle_menus(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Expand or collapse the header pull-down menus

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def info_log_show(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Show info log in a separate window

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def keyframe_jump(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    next: bool | None = True,
) -> None:
    """Jump to previous/next keyframe

    :type execution_context: int | str | None
    :type undo: bool | None
    :param next: Next Keyframe
    :type next: bool | None
    """

def marker_jump(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    next: bool | None = True,
) -> None:
    """Jump to previous/next marker

    :type execution_context: int | str | None
    :type undo: bool | None
    :param next: Next Marker
    :type next: bool | None
    """

def new(execution_context: int | str | None = None, undo: bool | None = None) -> None:
    """Add a new screen

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def redo_last(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Display parameters for last action performed

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def region_blend(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Blend in and out overlapping region

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def region_context_menu(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Display region context menu

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def region_flip(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Toggle the region's alignment (left/right or top/bottom)

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def region_quadview(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Split selected area into camera, front, right, and top views

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def region_scale(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Scale selected area

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def region_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    region_type: bpy.stub_internal.rna_enums.RegionTypeItems | None = "WINDOW",
) -> None:
    """Hide or unhide the region

    :type execution_context: int | str | None
    :type undo: bool | None
    :param region_type: Region Type, Type of the region to toggle
    :type region_type: bpy.stub_internal.rna_enums.RegionTypeItems | None
    """

def repeat_history(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    index: int | None = 0,
) -> None:
    """Display menu for previous actions performed

    :type execution_context: int | str | None
    :type undo: bool | None
    :param index: Index
    :type index: int | None
    """

def repeat_last(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Repeat last action

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def screen_full_area(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_hide_panels: bool | None = False,
) -> None:
    """Toggle display selected area as fullscreen/maximized

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_hide_panels: Hide Panels, Hide all the panels
    :type use_hide_panels: bool | None
    """

def screen_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    delta: int | None = 1,
) -> None:
    """Cycle through available screens

    :type execution_context: int | str | None
    :type undo: bool | None
    :param delta: Delta
    :type delta: int | None
    """

def screenshot(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    hide_props_region: bool | None = True,
    check_existing: bool | None = True,
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = True,
    filter_movie: bool | None = False,
    filter_python: bool | None = False,
    filter_font: bool | None = False,
    filter_sound: bool | None = False,
    filter_text: bool | None = False,
    filter_archive: bool | None = False,
    filter_btx: bool | None = False,
    filter_collada: bool | None = False,
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 9,
    show_multiview: bool | None = False,
    use_multiview: bool | None = False,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
) -> None:
    """Capture a picture of the whole Blender window

        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | None
        :param filter_image: Filter image files
        :type filter_image: bool | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | None
        :param filter_python: Filter Python files
        :type filter_python: bool | None
        :param filter_font: Filter font files
        :type filter_font: bool | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | None
        :param filter_text: Filter text files
        :type filter_text: bool | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: int | None
        :param show_multiview: Enable Multi-View
        :type show_multiview: bool | None
        :param use_multiview: Use Multi-View
        :type use_multiview: bool | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: typing.Literal['DEFAULT','LIST_VERTICAL','LIST_HORIZONTAL','THUMBNAIL'] | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
    """

def screenshot_area(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    hide_props_region: bool | None = True,
    check_existing: bool | None = True,
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = True,
    filter_movie: bool | None = False,
    filter_python: bool | None = False,
    filter_font: bool | None = False,
    filter_sound: bool | None = False,
    filter_text: bool | None = False,
    filter_archive: bool | None = False,
    filter_btx: bool | None = False,
    filter_collada: bool | None = False,
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 9,
    show_multiview: bool | None = False,
    use_multiview: bool | None = False,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
) -> None:
    """Capture a picture of an editor

        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | None
        :param filter_image: Filter image files
        :type filter_image: bool | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | None
        :param filter_python: Filter Python files
        :type filter_python: bool | None
        :param filter_font: Filter font files
        :type filter_font: bool | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | None
        :param filter_text: Filter text files
        :type filter_text: bool | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: int | None
        :param show_multiview: Enable Multi-View
        :type show_multiview: bool | None
        :param use_multiview: Use Multi-View
        :type use_multiview: bool | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: typing.Literal['DEFAULT','LIST_VERTICAL','LIST_HORIZONTAL','THUMBNAIL'] | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
    """

def space_context_cycle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["PREV", "NEXT"] | None = "NEXT",
) -> None:
    """Cycle through the editor context by activating the next/previous one

    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Direction to cycle through
    :type direction: typing.Literal['PREV','NEXT'] | None
    """

def space_type_set_or_cycle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    space_type: bpy.stub_internal.rna_enums.SpaceTypeItems | None = "EMPTY",
) -> None:
    """Set the space type or cycle subtype

    :type execution_context: int | str | None
    :type undo: bool | None
    :param space_type: Type
    :type space_type: bpy.stub_internal.rna_enums.SpaceTypeItems | None
    """

def spacedata_cleanup(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Remove unused settings for invisible editors

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def userpref_show(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    section: bpy.stub_internal.rna_enums.PreferenceSectionItems | None = "INTERFACE",
) -> None:
    """Edit user preferences and system settings

    :type execution_context: int | str | None
    :type undo: bool | None
    :param section: Section to activate in the Preferences
    :type section: bpy.stub_internal.rna_enums.PreferenceSectionItems | None
    """

def workspace_cycle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["PREV", "NEXT"] | None = "NEXT",
) -> None:
    """Cycle through workspaces

    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Direction to cycle through
    :type direction: typing.Literal['PREV','NEXT'] | None
    """
