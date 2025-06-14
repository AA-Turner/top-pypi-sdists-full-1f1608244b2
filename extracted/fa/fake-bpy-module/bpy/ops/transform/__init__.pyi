import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.stub_internal.rna_enums
import mathutils

def bbone_resize(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: collections.abc.Sequence[float] | mathutils.Vector | None = (1.0, 1.0, 1.0),
    orient_type: str | None = "GLOBAL",
    orient_matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix
    | None = ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
    orient_matrix_type: str | None = "GLOBAL",
    constraint_axis: collections.abc.Iterable[bool] | None = (False, False, False),
    mirror: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Scale selected bendy bones display size

    :type execution_context: int | str | None
    :type undo: bool | None
    :param value: Display Size
    :type value: collections.abc.Sequence[float] | mathutils.Vector | None
    :param orient_type: Orientation, Transformation orientation
    :type orient_type: str | None
    :param orient_matrix: Matrix
    :type orient_matrix: collections.abc.Sequence[collections.abc.Sequence[float]] | mathutils.Matrix | None
    :param orient_matrix_type: Matrix Orientation
    :type orient_matrix_type: str | None
    :param constraint_axis: Constraint Axis
    :type constraint_axis: collections.abc.Iterable[bool] | None
    :param mirror: Mirror Editing
    :type mirror: bool | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | None
    """

def bend(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: collections.abc.Iterable[float] | None = 0.0,
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    snap: bool | None = False,
    gpencil_strokes: bool | None = False,
    center_override: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Bend selected items between the 3D cursor and the mouse

    :type execution_context: int | str | None
    :type undo: bool | None
    :param value: Angle
    :type value: collections.abc.Iterable[float] | None
    :param mirror: Mirror Editing
    :type mirror: bool | None
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool | None
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems | None
    :param proportional_size: Proportional Size
    :type proportional_size: float | None
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool | None
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool | None
    :param snap: Use Snapping Options
    :type snap: bool | None
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: bool | None
    :param center_override: Center Override, Force using this center value (when set)
    :type center_override: collections.abc.Sequence[float] | mathutils.Vector | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | None
    """

def create_orientation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    use_view: bool | None = False,
    use: bool | None = False,
    overwrite: bool | None = False,
) -> None:
    """Create transformation orientation from selection

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the new custom orientation
    :type name: str
    :param use_view: Use View, Use the current view instead of the active object to create the new orientation
    :type use_view: bool | None
    :param use: Use After Creation, Select orientation after its creation
    :type use: bool | None
    :param overwrite: Overwrite Previous, Overwrite previously created orientation with same name
    :type overwrite: bool | None
    """

def delete_orientation(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Delete transformation orientation

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def edge_bevelweight(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    snap: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Change the bevel weight of edges

    :type execution_context: int | str | None
    :type undo: bool | None
    :param value: Factor
    :type value: float | None
    :param snap: Use Snapping Options
    :type snap: bool | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | None
    """

def edge_crease(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    snap: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Change the crease of edges

    :type execution_context: int | str | None
    :type undo: bool | None
    :param value: Factor
    :type value: float | None
    :param snap: Use Snapping Options
    :type snap: bool | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | None
    """

def edge_slide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    single_side: bool | None = False,
    use_even: bool | None = False,
    flipped: bool | None = False,
    use_clamp: bool | None = True,
    mirror: bool | None = False,
    snap: bool | None = False,
    snap_elements: set[bpy.stub_internal.rna_enums.SnapElementItems] | None = {
        "INCREMENT"
    },
    use_snap_project: bool | None = False,
    snap_target: bpy.stub_internal.rna_enums.SnapSourceItems | None = "CLOSEST",
    use_snap_self: bool | None = True,
    use_snap_edit: bool | None = True,
    use_snap_nonedit: bool | None = True,
    use_snap_selectable: bool | None = False,
    snap_point: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    correct_uv: bool | None = True,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Slide an edge loop along a mesh

    :type execution_context: int | str | None
    :type undo: bool | None
    :param value: Factor
    :type value: float | None
    :param single_side: Single Side
    :type single_side: bool | None
    :param use_even: Even, Make the edge loop match the shape of the adjacent edge loop
    :type use_even: bool | None
    :param flipped: Flipped, When Even mode is active, flips between the two adjacent edge loops
    :type flipped: bool | None
    :param use_clamp: Clamp, Clamp within the edge extents
    :type use_clamp: bool | None
    :param mirror: Mirror Editing
    :type mirror: bool | None
    :param snap: Use Snapping Options
    :type snap: bool | None
    :param snap_elements: Snap to Elements
    :type snap_elements: set[bpy.stub_internal.rna_enums.SnapElementItems] | None
    :param use_snap_project: Project Individual Elements
    :type use_snap_project: bool | None
    :param snap_target: Snap Base, Point on source that will snap to target
    :type snap_target: bpy.stub_internal.rna_enums.SnapSourceItems | None
    :param use_snap_self: Target: Include Active
    :type use_snap_self: bool | None
    :param use_snap_edit: Target: Include Edit
    :type use_snap_edit: bool | None
    :param use_snap_nonedit: Target: Include Non-Edited
    :type use_snap_nonedit: bool | None
    :param use_snap_selectable: Target: Exclude Non-Selectable
    :type use_snap_selectable: bool | None
    :param snap_point: Point
    :type snap_point: collections.abc.Sequence[float] | mathutils.Vector | None
    :param correct_uv: Correct UVs, Correct UV coordinates when transforming
    :type correct_uv: bool | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | None
    """

def from_gizmo(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Transform selected items by mode type

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def mirror(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    orient_type: str | None = "GLOBAL",
    orient_matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix
    | None = ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
    orient_matrix_type: str | None = "GLOBAL",
    constraint_axis: collections.abc.Iterable[bool] | None = (False, False, False),
    gpencil_strokes: bool | None = False,
    center_override: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Mirror selected items around one or more axes

    :type execution_context: int | str | None
    :type undo: bool | None
    :param orient_type: Orientation, Transformation orientation
    :type orient_type: str | None
    :param orient_matrix: Matrix
    :type orient_matrix: collections.abc.Sequence[collections.abc.Sequence[float]] | mathutils.Matrix | None
    :param orient_matrix_type: Matrix Orientation
    :type orient_matrix_type: str | None
    :param constraint_axis: Constraint Axis
    :type constraint_axis: collections.abc.Iterable[bool] | None
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: bool | None
    :param center_override: Center Override, Force using this center value (when set)
    :type center_override: collections.abc.Sequence[float] | mathutils.Vector | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | None
    """

def push_pull(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    snap: bool | None = False,
    center_override: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Push/Pull selected items

    :type execution_context: int | str | None
    :type undo: bool | None
    :param value: Distance
    :type value: float | None
    :param mirror: Mirror Editing
    :type mirror: bool | None
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool | None
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems | None
    :param proportional_size: Proportional Size
    :type proportional_size: float | None
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool | None
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool | None
    :param snap: Use Snapping Options
    :type snap: bool | None
    :param center_override: Center Override, Force using this center value (when set)
    :type center_override: collections.abc.Sequence[float] | mathutils.Vector | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | None
    """

def resize(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: collections.abc.Sequence[float] | mathutils.Vector | None = (1.0, 1.0, 1.0),
    mouse_dir_constraint: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    orient_type: str | None = "GLOBAL",
    orient_matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix
    | None = ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
    orient_matrix_type: str | None = "GLOBAL",
    constraint_axis: collections.abc.Iterable[bool] | None = (False, False, False),
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    snap: bool | None = False,
    snap_elements: set[bpy.stub_internal.rna_enums.SnapElementItems] | None = {
        "INCREMENT"
    },
    use_snap_project: bool | None = False,
    snap_target: bpy.stub_internal.rna_enums.SnapSourceItems | None = "CLOSEST",
    use_snap_self: bool | None = True,
    use_snap_edit: bool | None = True,
    use_snap_nonedit: bool | None = True,
    use_snap_selectable: bool | None = False,
    snap_point: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    gpencil_strokes: bool | None = False,
    texture_space: bool | None = False,
    remove_on_cancel: bool | None = False,
    use_duplicated_keyframes: bool | None = False,
    center_override: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Scale (resize) selected items

    :type execution_context: int | str | None
    :type undo: bool | None
    :param value: Scale
    :type value: collections.abc.Sequence[float] | mathutils.Vector | None
    :param mouse_dir_constraint: Mouse Directional Constraint
    :type mouse_dir_constraint: collections.abc.Sequence[float] | mathutils.Vector | None
    :param orient_type: Orientation, Transformation orientation
    :type orient_type: str | None
    :param orient_matrix: Matrix
    :type orient_matrix: collections.abc.Sequence[collections.abc.Sequence[float]] | mathutils.Matrix | None
    :param orient_matrix_type: Matrix Orientation
    :type orient_matrix_type: str | None
    :param constraint_axis: Constraint Axis
    :type constraint_axis: collections.abc.Iterable[bool] | None
    :param mirror: Mirror Editing
    :type mirror: bool | None
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool | None
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems | None
    :param proportional_size: Proportional Size
    :type proportional_size: float | None
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool | None
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool | None
    :param snap: Use Snapping Options
    :type snap: bool | None
    :param snap_elements: Snap to Elements
    :type snap_elements: set[bpy.stub_internal.rna_enums.SnapElementItems] | None
    :param use_snap_project: Project Individual Elements
    :type use_snap_project: bool | None
    :param snap_target: Snap Base, Point on source that will snap to target
    :type snap_target: bpy.stub_internal.rna_enums.SnapSourceItems | None
    :param use_snap_self: Target: Include Active
    :type use_snap_self: bool | None
    :param use_snap_edit: Target: Include Edit
    :type use_snap_edit: bool | None
    :param use_snap_nonedit: Target: Include Non-Edited
    :type use_snap_nonedit: bool | None
    :param use_snap_selectable: Target: Exclude Non-Selectable
    :type use_snap_selectable: bool | None
    :param snap_point: Point
    :type snap_point: collections.abc.Sequence[float] | mathutils.Vector | None
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: bool | None
    :param texture_space: Edit Texture Space, Edit object data texture space
    :type texture_space: bool | None
    :param remove_on_cancel: Remove on Cancel, Remove elements on cancel
    :type remove_on_cancel: bool | None
    :param use_duplicated_keyframes: Duplicated Keyframes, Transform duplicated keyframes
    :type use_duplicated_keyframes: bool | None
    :param center_override: Center Override, Force using this center value (when set)
    :type center_override: collections.abc.Sequence[float] | mathutils.Vector | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | None
    """

def rotate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    orient_axis: bpy.stub_internal.rna_enums.AxisXyzItems | None = "Z",
    orient_type: str | None = "GLOBAL",
    orient_matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix
    | None = ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
    orient_matrix_type: str | None = "GLOBAL",
    constraint_axis: collections.abc.Iterable[bool] | None = (False, False, False),
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    snap: bool | None = False,
    snap_elements: set[bpy.stub_internal.rna_enums.SnapElementItems] | None = {
        "INCREMENT"
    },
    use_snap_project: bool | None = False,
    snap_target: bpy.stub_internal.rna_enums.SnapSourceItems | None = "CLOSEST",
    use_snap_self: bool | None = True,
    use_snap_edit: bool | None = True,
    use_snap_nonedit: bool | None = True,
    use_snap_selectable: bool | None = False,
    snap_point: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    gpencil_strokes: bool | None = False,
    center_override: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Rotate selected items

    :type execution_context: int | str | None
    :type undo: bool | None
    :param value: Angle
    :type value: float | None
    :param orient_axis: Axis
    :type orient_axis: bpy.stub_internal.rna_enums.AxisXyzItems | None
    :param orient_type: Orientation, Transformation orientation
    :type orient_type: str | None
    :param orient_matrix: Matrix
    :type orient_matrix: collections.abc.Sequence[collections.abc.Sequence[float]] | mathutils.Matrix | None
    :param orient_matrix_type: Matrix Orientation
    :type orient_matrix_type: str | None
    :param constraint_axis: Constraint Axis
    :type constraint_axis: collections.abc.Iterable[bool] | None
    :param mirror: Mirror Editing
    :type mirror: bool | None
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool | None
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems | None
    :param proportional_size: Proportional Size
    :type proportional_size: float | None
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool | None
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool | None
    :param snap: Use Snapping Options
    :type snap: bool | None
    :param snap_elements: Snap to Elements
    :type snap_elements: set[bpy.stub_internal.rna_enums.SnapElementItems] | None
    :param use_snap_project: Project Individual Elements
    :type use_snap_project: bool | None
    :param snap_target: Snap Base, Point on source that will snap to target
    :type snap_target: bpy.stub_internal.rna_enums.SnapSourceItems | None
    :param use_snap_self: Target: Include Active
    :type use_snap_self: bool | None
    :param use_snap_edit: Target: Include Edit
    :type use_snap_edit: bool | None
    :param use_snap_nonedit: Target: Include Non-Edited
    :type use_snap_nonedit: bool | None
    :param use_snap_selectable: Target: Exclude Non-Selectable
    :type use_snap_selectable: bool | None
    :param snap_point: Point
    :type snap_point: collections.abc.Sequence[float] | mathutils.Vector | None
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: bool | None
    :param center_override: Center Override, Force using this center value (when set)
    :type center_override: collections.abc.Sequence[float] | mathutils.Vector | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | None
    """

def rotate_normal(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    orient_axis: bpy.stub_internal.rna_enums.AxisXyzItems | None = "Z",
    orient_type: str | None = "GLOBAL",
    orient_matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix
    | None = ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
    orient_matrix_type: str | None = "GLOBAL",
    constraint_axis: collections.abc.Iterable[bool] | None = (False, False, False),
    mirror: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Rotate split normal of selected items

    :type execution_context: int | str | None
    :type undo: bool | None
    :param value: Angle
    :type value: float | None
    :param orient_axis: Axis
    :type orient_axis: bpy.stub_internal.rna_enums.AxisXyzItems | None
    :param orient_type: Orientation, Transformation orientation
    :type orient_type: str | None
    :param orient_matrix: Matrix
    :type orient_matrix: collections.abc.Sequence[collections.abc.Sequence[float]] | mathutils.Matrix | None
    :param orient_matrix_type: Matrix Orientation
    :type orient_matrix_type: str | None
    :param constraint_axis: Constraint Axis
    :type constraint_axis: collections.abc.Iterable[bool] | None
    :param mirror: Mirror Editing
    :type mirror: bool | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | None
    """

def select_orientation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    orientation: str | None = "GLOBAL",
) -> None:
    """Select transformation orientation

    :type execution_context: int | str | None
    :type undo: bool | None
    :param orientation: Orientation, Transformation orientation
    :type orientation: str | None
    """

def seq_slide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
    use_restore_handle_selection: bool | None = False,
    snap: bool | None = False,
    texture_space: bool | None = False,
    remove_on_cancel: bool | None = False,
    use_duplicated_keyframes: bool | None = False,
    view2d_edge_pan: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Slide a sequence strip in time

    :type execution_context: int | str | None
    :type undo: bool | None
    :param value: Offset
    :type value: collections.abc.Sequence[float] | mathutils.Vector | None
    :param use_restore_handle_selection: Restore Handle Selection, Restore handle selection after tweaking
    :type use_restore_handle_selection: bool | None
    :param snap: Use Snapping Options
    :type snap: bool | None
    :param texture_space: Edit Texture Space, Edit object data texture space
    :type texture_space: bool | None
    :param remove_on_cancel: Remove on Cancel, Remove elements on cancel
    :type remove_on_cancel: bool | None
    :param use_duplicated_keyframes: Duplicated Keyframes, Transform duplicated keyframes
    :type use_duplicated_keyframes: bool | None
    :param view2d_edge_pan: Edge Pan, Enable edge panning in 2D view
    :type view2d_edge_pan: bool | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | None
    """

def shear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    orient_axis: bpy.stub_internal.rna_enums.AxisXyzItems | None = "Z",
    orient_axis_ortho: bpy.stub_internal.rna_enums.AxisXyzItems | None = "X",
    orient_type: str | None = "GLOBAL",
    orient_matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix
    | None = ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
    orient_matrix_type: str | None = "GLOBAL",
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    snap: bool | None = False,
    gpencil_strokes: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Shear selected items along the given axis

    :type execution_context: int | str | None
    :type undo: bool | None
    :param value: Offset
    :type value: float | None
    :param orient_axis: Axis
    :type orient_axis: bpy.stub_internal.rna_enums.AxisXyzItems | None
    :param orient_axis_ortho: Axis Ortho
    :type orient_axis_ortho: bpy.stub_internal.rna_enums.AxisXyzItems | None
    :param orient_type: Orientation, Transformation orientation
    :type orient_type: str | None
    :param orient_matrix: Matrix
    :type orient_matrix: collections.abc.Sequence[collections.abc.Sequence[float]] | mathutils.Matrix | None
    :param orient_matrix_type: Matrix Orientation
    :type orient_matrix_type: str | None
    :param mirror: Mirror Editing
    :type mirror: bool | None
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool | None
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems | None
    :param proportional_size: Proportional Size
    :type proportional_size: float | None
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool | None
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool | None
    :param snap: Use Snapping Options
    :type snap: bool | None
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: bool | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | None
    """

def shrink_fatten(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    use_even_offset: bool | None = False,
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    snap: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Shrink/fatten selected vertices along normals

    :type execution_context: int | str | None
    :type undo: bool | None
    :param value: Offset
    :type value: float | None
    :param use_even_offset: Offset Even, Scale the offset to give more even thickness
    :type use_even_offset: bool | None
    :param mirror: Mirror Editing
    :type mirror: bool | None
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool | None
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems | None
    :param proportional_size: Proportional Size
    :type proportional_size: float | None
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool | None
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool | None
    :param snap: Use Snapping Options
    :type snap: bool | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | None
    """

def skin_resize(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: collections.abc.Sequence[float] | mathutils.Vector | None = (1.0, 1.0, 1.0),
    orient_type: str | None = "GLOBAL",
    orient_matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix
    | None = ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
    orient_matrix_type: str | None = "GLOBAL",
    constraint_axis: collections.abc.Iterable[bool] | None = (False, False, False),
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    snap: bool | None = False,
    snap_elements: set[bpy.stub_internal.rna_enums.SnapElementItems] | None = {
        "INCREMENT"
    },
    use_snap_project: bool | None = False,
    snap_target: bpy.stub_internal.rna_enums.SnapSourceItems | None = "CLOSEST",
    use_snap_self: bool | None = True,
    use_snap_edit: bool | None = True,
    use_snap_nonedit: bool | None = True,
    use_snap_selectable: bool | None = False,
    snap_point: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Scale selected vertices' skin radii

    :type execution_context: int | str | None
    :type undo: bool | None
    :param value: Scale
    :type value: collections.abc.Sequence[float] | mathutils.Vector | None
    :param orient_type: Orientation, Transformation orientation
    :type orient_type: str | None
    :param orient_matrix: Matrix
    :type orient_matrix: collections.abc.Sequence[collections.abc.Sequence[float]] | mathutils.Matrix | None
    :param orient_matrix_type: Matrix Orientation
    :type orient_matrix_type: str | None
    :param constraint_axis: Constraint Axis
    :type constraint_axis: collections.abc.Iterable[bool] | None
    :param mirror: Mirror Editing
    :type mirror: bool | None
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool | None
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems | None
    :param proportional_size: Proportional Size
    :type proportional_size: float | None
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool | None
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool | None
    :param snap: Use Snapping Options
    :type snap: bool | None
    :param snap_elements: Snap to Elements
    :type snap_elements: set[bpy.stub_internal.rna_enums.SnapElementItems] | None
    :param use_snap_project: Project Individual Elements
    :type use_snap_project: bool | None
    :param snap_target: Snap Base, Point on source that will snap to target
    :type snap_target: bpy.stub_internal.rna_enums.SnapSourceItems | None
    :param use_snap_self: Target: Include Active
    :type use_snap_self: bool | None
    :param use_snap_edit: Target: Include Edit
    :type use_snap_edit: bool | None
    :param use_snap_nonedit: Target: Include Non-Edited
    :type use_snap_nonedit: bool | None
    :param use_snap_selectable: Target: Exclude Non-Selectable
    :type use_snap_selectable: bool | None
    :param snap_point: Point
    :type snap_point: collections.abc.Sequence[float] | mathutils.Vector | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | None
    """

def tilt(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    snap: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Tilt selected control vertices of 3D curve

    :type execution_context: int | str | None
    :type undo: bool | None
    :param value: Angle
    :type value: float | None
    :param mirror: Mirror Editing
    :type mirror: bool | None
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool | None
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems | None
    :param proportional_size: Proportional Size
    :type proportional_size: float | None
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool | None
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool | None
    :param snap: Use Snapping Options
    :type snap: bool | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | None
    """

def tosphere(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    snap: bool | None = False,
    gpencil_strokes: bool | None = False,
    center_override: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Move selected items outward in a spherical shape around geometric center

    :type execution_context: int | str | None
    :type undo: bool | None
    :param value: Factor
    :type value: float | None
    :param mirror: Mirror Editing
    :type mirror: bool | None
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool | None
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems | None
    :param proportional_size: Proportional Size
    :type proportional_size: float | None
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool | None
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool | None
    :param snap: Use Snapping Options
    :type snap: bool | None
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: bool | None
    :param center_override: Center Override, Force using this center value (when set)
    :type center_override: collections.abc.Sequence[float] | mathutils.Vector | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | None
    """

def trackball(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: collections.abc.Iterable[float] | None = (0.0, 0.0),
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    snap: bool | None = False,
    gpencil_strokes: bool | None = False,
    center_override: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Trackball style rotation of selected items

    :type execution_context: int | str | None
    :type undo: bool | None
    :param value: Angle
    :type value: collections.abc.Iterable[float] | None
    :param mirror: Mirror Editing
    :type mirror: bool | None
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool | None
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems | None
    :param proportional_size: Proportional Size
    :type proportional_size: float | None
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool | None
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool | None
    :param snap: Use Snapping Options
    :type snap: bool | None
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: bool | None
    :param center_override: Center Override, Force using this center value (when set)
    :type center_override: collections.abc.Sequence[float] | mathutils.Vector | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | None
    """

def transform(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: bpy.stub_internal.rna_enums.TransformModeTypeItems | None = "TRANSLATION",
    value: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
        0.0,
    ),
    orient_axis: bpy.stub_internal.rna_enums.AxisXyzItems | None = "Z",
    orient_type: bpy.stub_internal.rna_enums.TransformOrientationItems
    | None = "GLOBAL",
    orient_matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix
    | None = ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
    orient_matrix_type: bpy.stub_internal.rna_enums.TransformOrientationItems
    | None = "GLOBAL",
    constraint_axis: collections.abc.Iterable[bool] | None = (False, False, False),
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    snap: bool | None = False,
    snap_elements: set[bpy.stub_internal.rna_enums.SnapElementItems] | None = {
        "INCREMENT"
    },
    use_snap_project: bool | None = False,
    snap_target: bpy.stub_internal.rna_enums.SnapSourceItems | None = "CLOSEST",
    use_snap_self: bool | None = True,
    use_snap_edit: bool | None = True,
    use_snap_nonedit: bool | None = True,
    use_snap_selectable: bool | None = False,
    snap_point: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    snap_align: bool | None = False,
    snap_normal: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    gpencil_strokes: bool | None = False,
    texture_space: bool | None = False,
    remove_on_cancel: bool | None = False,
    use_duplicated_keyframes: bool | None = False,
    center_override: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
    use_automerge_and_split: bool | None = False,
) -> None:
    """Transform selected items by mode type

    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: bpy.stub_internal.rna_enums.TransformModeTypeItems | None
    :param value: Values
    :type value: collections.abc.Sequence[float] | mathutils.Vector | None
    :param orient_axis: Axis
    :type orient_axis: bpy.stub_internal.rna_enums.AxisXyzItems | None
    :param orient_type: Orientation, Transformation orientation
    :type orient_type: bpy.stub_internal.rna_enums.TransformOrientationItems | None
    :param orient_matrix: Matrix
    :type orient_matrix: collections.abc.Sequence[collections.abc.Sequence[float]] | mathutils.Matrix | None
    :param orient_matrix_type: Matrix Orientation
    :type orient_matrix_type: bpy.stub_internal.rna_enums.TransformOrientationItems | None
    :param constraint_axis: Constraint Axis
    :type constraint_axis: collections.abc.Iterable[bool] | None
    :param mirror: Mirror Editing
    :type mirror: bool | None
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool | None
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems | None
    :param proportional_size: Proportional Size
    :type proportional_size: float | None
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool | None
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool | None
    :param snap: Use Snapping Options
    :type snap: bool | None
    :param snap_elements: Snap to Elements
    :type snap_elements: set[bpy.stub_internal.rna_enums.SnapElementItems] | None
    :param use_snap_project: Project Individual Elements
    :type use_snap_project: bool | None
    :param snap_target: Snap Base, Point on source that will snap to target
    :type snap_target: bpy.stub_internal.rna_enums.SnapSourceItems | None
    :param use_snap_self: Target: Include Active
    :type use_snap_self: bool | None
    :param use_snap_edit: Target: Include Edit
    :type use_snap_edit: bool | None
    :param use_snap_nonedit: Target: Include Non-Edited
    :type use_snap_nonedit: bool | None
    :param use_snap_selectable: Target: Exclude Non-Selectable
    :type use_snap_selectable: bool | None
    :param snap_point: Point
    :type snap_point: collections.abc.Sequence[float] | mathutils.Vector | None
    :param snap_align: Align with Point Normal
    :type snap_align: bool | None
    :param snap_normal: Normal
    :type snap_normal: collections.abc.Sequence[float] | mathutils.Vector | None
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: bool | None
    :param texture_space: Edit Texture Space, Edit object data texture space
    :type texture_space: bool | None
    :param remove_on_cancel: Remove on Cancel, Remove elements on cancel
    :type remove_on_cancel: bool | None
    :param use_duplicated_keyframes: Duplicated Keyframes, Transform duplicated keyframes
    :type use_duplicated_keyframes: bool | None
    :param center_override: Center Override, Force using this center value (when set)
    :type center_override: collections.abc.Sequence[float] | mathutils.Vector | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | None
    :param use_automerge_and_split: Auto Merge & Split, Forces the use of Auto Merge and Split
    :type use_automerge_and_split: bool | None
    """

def translate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
    orient_type: bpy.stub_internal.rna_enums.TransformOrientationItems
    | None = "GLOBAL",
    orient_matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix
    | None = ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
    orient_matrix_type: bpy.stub_internal.rna_enums.TransformOrientationItems
    | None = "GLOBAL",
    constraint_axis: collections.abc.Iterable[bool] | None = (False, False, False),
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    snap: bool | None = False,
    snap_elements: set[bpy.stub_internal.rna_enums.SnapElementItems] | None = {
        "INCREMENT"
    },
    use_snap_project: bool | None = False,
    snap_target: bpy.stub_internal.rna_enums.SnapSourceItems | None = "CLOSEST",
    use_snap_self: bool | None = True,
    use_snap_edit: bool | None = True,
    use_snap_nonedit: bool | None = True,
    use_snap_selectable: bool | None = False,
    snap_point: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    snap_align: bool | None = False,
    snap_normal: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    gpencil_strokes: bool | None = False,
    cursor_transform: bool | None = False,
    texture_space: bool | None = False,
    remove_on_cancel: bool | None = False,
    use_duplicated_keyframes: bool | None = False,
    view2d_edge_pan: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
    use_automerge_and_split: bool | None = False,
    translate_origin: bool | None = False,
) -> None:
    """Move selected items

    :type execution_context: int | str | None
    :type undo: bool | None
    :param value: Move
    :type value: collections.abc.Sequence[float] | mathutils.Vector | None
    :param orient_type: Orientation, Transformation orientation
    :type orient_type: bpy.stub_internal.rna_enums.TransformOrientationItems | None
    :param orient_matrix: Matrix
    :type orient_matrix: collections.abc.Sequence[collections.abc.Sequence[float]] | mathutils.Matrix | None
    :param orient_matrix_type: Matrix Orientation
    :type orient_matrix_type: bpy.stub_internal.rna_enums.TransformOrientationItems | None
    :param constraint_axis: Constraint Axis
    :type constraint_axis: collections.abc.Iterable[bool] | None
    :param mirror: Mirror Editing
    :type mirror: bool | None
    :param use_proportional_edit: Proportional Editing
    :type use_proportional_edit: bool | None
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
    :type proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems | None
    :param proportional_size: Proportional Size
    :type proportional_size: float | None
    :param use_proportional_connected: Connected
    :type use_proportional_connected: bool | None
    :param use_proportional_projected: Projected (2D)
    :type use_proportional_projected: bool | None
    :param snap: Use Snapping Options
    :type snap: bool | None
    :param snap_elements: Snap to Elements
    :type snap_elements: set[bpy.stub_internal.rna_enums.SnapElementItems] | None
    :param use_snap_project: Project Individual Elements
    :type use_snap_project: bool | None
    :param snap_target: Snap Base, Point on source that will snap to target
    :type snap_target: bpy.stub_internal.rna_enums.SnapSourceItems | None
    :param use_snap_self: Target: Include Active
    :type use_snap_self: bool | None
    :param use_snap_edit: Target: Include Edit
    :type use_snap_edit: bool | None
    :param use_snap_nonedit: Target: Include Non-Edited
    :type use_snap_nonedit: bool | None
    :param use_snap_selectable: Target: Exclude Non-Selectable
    :type use_snap_selectable: bool | None
    :param snap_point: Point
    :type snap_point: collections.abc.Sequence[float] | mathutils.Vector | None
    :param snap_align: Align with Point Normal
    :type snap_align: bool | None
    :param snap_normal: Normal
    :type snap_normal: collections.abc.Sequence[float] | mathutils.Vector | None
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: bool | None
    :param cursor_transform: Transform Cursor
    :type cursor_transform: bool | None
    :param texture_space: Edit Texture Space, Edit object data texture space
    :type texture_space: bool | None
    :param remove_on_cancel: Remove on Cancel, Remove elements on cancel
    :type remove_on_cancel: bool | None
    :param use_duplicated_keyframes: Duplicated Keyframes, Transform duplicated keyframes
    :type use_duplicated_keyframes: bool | None
    :param view2d_edge_pan: Edge Pan, Enable edge panning in 2D view
    :type view2d_edge_pan: bool | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | None
    :param use_automerge_and_split: Auto Merge & Split, Forces the use of Auto Merge and Split
    :type use_automerge_and_split: bool | None
    :param translate_origin: Translate Origin, Translate origin instead of selection
    :type translate_origin: bool | None
    """

def vert_crease(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    snap: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Change the crease of vertices

    :type execution_context: int | str | None
    :type undo: bool | None
    :param value: Factor
    :type value: float | None
    :param snap: Use Snapping Options
    :type snap: bool | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | None
    """

def vert_slide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    use_even: bool | None = False,
    flipped: bool | None = False,
    use_clamp: bool | None = True,
    mirror: bool | None = False,
    snap: bool | None = False,
    snap_elements: set[bpy.stub_internal.rna_enums.SnapElementItems] | None = {
        "INCREMENT"
    },
    use_snap_project: bool | None = False,
    snap_target: bpy.stub_internal.rna_enums.SnapSourceItems | None = "CLOSEST",
    use_snap_self: bool | None = True,
    use_snap_edit: bool | None = True,
    use_snap_nonedit: bool | None = True,
    use_snap_selectable: bool | None = False,
    snap_point: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    correct_uv: bool | None = True,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Slide a vertex along a mesh

    :type execution_context: int | str | None
    :type undo: bool | None
    :param value: Factor
    :type value: float | None
    :param use_even: Even, Make the edge loop match the shape of the adjacent edge loop
    :type use_even: bool | None
    :param flipped: Flipped, When Even mode is active, flips between the two adjacent edge loops
    :type flipped: bool | None
    :param use_clamp: Clamp, Clamp within the edge extents
    :type use_clamp: bool | None
    :param mirror: Mirror Editing
    :type mirror: bool | None
    :param snap: Use Snapping Options
    :type snap: bool | None
    :param snap_elements: Snap to Elements
    :type snap_elements: set[bpy.stub_internal.rna_enums.SnapElementItems] | None
    :param use_snap_project: Project Individual Elements
    :type use_snap_project: bool | None
    :param snap_target: Snap Base, Point on source that will snap to target
    :type snap_target: bpy.stub_internal.rna_enums.SnapSourceItems | None
    :param use_snap_self: Target: Include Active
    :type use_snap_self: bool | None
    :param use_snap_edit: Target: Include Edit
    :type use_snap_edit: bool | None
    :param use_snap_nonedit: Target: Include Non-Edited
    :type use_snap_nonedit: bool | None
    :param use_snap_selectable: Target: Exclude Non-Selectable
    :type use_snap_selectable: bool | None
    :param snap_point: Point
    :type snap_point: collections.abc.Sequence[float] | mathutils.Vector | None
    :param correct_uv: Correct UVs, Correct UV coordinates when transforming
    :type correct_uv: bool | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | None
    """

def vertex_random(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    offset: float | None = 0.0,
    uniform: float | None = 0.0,
    normal: float | None = 0.0,
    seed: int | None = 0,
    wait_for_input: bool | None = True,
) -> None:
    """Randomize vertices

    :type execution_context: int | str | None
    :type undo: bool | None
    :param offset: Amount, Distance to offset
    :type offset: float | None
    :param uniform: Uniform, Increase for uniform offset distance
    :type uniform: float | None
    :param normal: Normal, Align offset direction to normals
    :type normal: float | None
    :param seed: Random Seed, Seed for the random number generator
    :type seed: int | None
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool | None
    """

def vertex_warp(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    warp_angle: float | None = 6.28319,
    offset_angle: float | None = 0.0,
    min: float | None = -1.0,
    max: float | None = 1.0,
    viewmat: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix
    | None = (
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
    ),
    center: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Warp vertices around the cursor

    :type execution_context: int | str | None
    :type undo: bool | None
    :param warp_angle: Warp Angle, Amount to warp about the cursor
    :type warp_angle: float | None
    :param offset_angle: Offset Angle, Angle to use as the basis for warping
    :type offset_angle: float | None
    :param min: Min
    :type min: float | None
    :param max: Max
    :type max: float | None
    :param viewmat: Matrix
    :type viewmat: collections.abc.Sequence[collections.abc.Sequence[float]] | mathutils.Matrix | None
    :param center: Center
    :type center: collections.abc.Sequence[float] | mathutils.Vector | None
    """
