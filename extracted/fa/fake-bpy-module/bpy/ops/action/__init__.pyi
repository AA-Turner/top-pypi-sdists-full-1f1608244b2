import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops.transform
import bpy.stub_internal.rna_enums
import bpy.types

def bake_keys(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Add keyframes on every frame between the selected keyframes

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def clean(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    threshold: float | None = 0.001,
    channels: bool | None = False,
) -> None:
    """Simplify F-Curves by removing closely spaced keyframes

    :type execution_context: int | str | None
    :type undo: bool | None
    :param threshold: Threshold
    :type threshold: float | None
    :param channels: Channels
    :type channels: bool | None
    """

def clickselect(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    wait_to_deselect_others: bool | None = False,
    mouse_x: int | None = 0,
    mouse_y: int | None = 0,
    extend: bool | None = False,
    deselect_all: bool | None = False,
    column: bool | None = False,
    channel: bool | None = False,
) -> None:
    """Select keyframes by clicking on them

    :type execution_context: int | str | None
    :type undo: bool | None
    :param wait_to_deselect_others: Wait to Deselect Others
    :type wait_to_deselect_others: bool | None
    :param mouse_x: Mouse X
    :type mouse_x: int | None
    :param mouse_y: Mouse Y
    :type mouse_y: int | None
    :param extend: Extend Select, Toggle keyframe selection instead of leaving newly selected keyframes only
    :type extend: bool | None
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :type deselect_all: bool | None
    :param column: Column Select, Select all keyframes that occur on the same frame as the one under the mouse
    :type column: bool | None
    :param channel: Only Channel, Select all the keyframes in the channel under the mouse
    :type channel: bool | None
    """

def copy(execution_context: int | str | None = None, undo: bool | None = None) -> None:
    """Copy selected keyframes to the internal clipboard

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    confirm: bool | None = True,
) -> None:
    """Remove all selected keyframes

    :type execution_context: int | str | None
    :type undo: bool | None
    :param confirm: Confirm, Prompt for confirmation
    :type confirm: bool | None
    """

def duplicate(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Make a copy of all selected keyframes

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def duplicate_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    ACTION_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_transform: bpy.ops.transform.transform | None = None,
) -> None:
    """Make a copy of all selected keyframes and move them

    :type execution_context: int | str | None
    :type undo: bool | None
    :param ACTION_OT_duplicate: Duplicate Keyframes, Make a copy of all selected keyframes
    :type ACTION_OT_duplicate: duplicate | None
    :param TRANSFORM_OT_transform: Transform, Transform selected items by mode type
    :type TRANSFORM_OT_transform: bpy.ops.transform.transform | None
    """

def easing_type(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.BeztripleInterpolationEasingItems | None = "AUTO",
) -> None:
    """Set easing type for the F-Curve segments starting from the selected keyframes

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: bpy.stub_internal.rna_enums.BeztripleInterpolationEasingItems | None
    """

def extrapolation_type(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["CONSTANT", "LINEAR", "MAKE_CYCLIC", "CLEAR_CYCLIC"]
    | None = "CONSTANT",
) -> None:
    """Set extrapolation mode for selected F-Curves

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    CONSTANT
    Constant Extrapolation -- Values on endpoint keyframes are held.

    LINEAR
    Linear Extrapolation -- Straight-line slope of end segments are extended past the endpoint keyframes.

    MAKE_CYCLIC
    Make Cyclic (F-Modifier) -- Add Cycles F-Modifier if one doesn't exist already.

    CLEAR_CYCLIC
    Clear Cyclic (F-Modifier) -- Remove Cycles F-Modifier if not needed anymore.
        :type type: typing.Literal['CONSTANT','LINEAR','MAKE_CYCLIC','CLEAR_CYCLIC'] | None
    """

def frame_jump(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Set the current frame to the average frame value of selected keyframes

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def handle_type(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.KeyframeHandleTypeItems | None = "FREE",
) -> None:
    """Set type of handle for selected keyframes

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: bpy.stub_internal.rna_enums.KeyframeHandleTypeItems | None
    """

def interpolation_type(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.BeztripleInterpolationModeItems
    | None = "CONSTANT",
) -> None:
    """Set interpolation mode for the F-Curve segments starting from the selected keyframes

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: bpy.stub_internal.rna_enums.BeztripleInterpolationModeItems | None
    """

def keyframe_insert(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["ALL", "SEL", "GROUP"] | None = "ALL",
) -> None:
    """Insert keyframes for the specified channels

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: typing.Literal['ALL','SEL','GROUP'] | None
    """

def keyframe_type(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.BeztripleKeyframeTypeItems | None = "KEYFRAME",
) -> None:
    """Set type of keyframe for the selected keyframes

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: bpy.stub_internal.rna_enums.BeztripleKeyframeTypeItems | None
    """

def layer_next(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Switch to editing action in animation layer above the current action in the NLA Stack

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def layer_prev(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Switch to editing action in animation layer below the current action in the NLA Stack

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def markers_make_local(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Move selected scene markers to the active Action as local 'pose' markers

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def mirror(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["CFRA", "XAXIS", "MARKER"] | None = "CFRA",
) -> None:
    """Flip selected keyframes over the selected mirror line

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    CFRA
    By Times Over Current Frame -- Flip times of selected keyframes using the current frame as the mirror line.

    XAXIS
    By Values Over Zero Value -- Flip values of selected keyframes (i.e. negative values become positive, and vice versa).

    MARKER
    By Times Over First Selected Marker -- Flip times of selected keyframes using the first selected marker as the reference point.
        :type type: typing.Literal['CFRA','XAXIS','MARKER'] | None
    """

def new(execution_context: int | str | None = None, undo: bool | None = None) -> None:
    """Create new action

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def paste(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    offset: bpy.stub_internal.rna_enums.KeyframePasteOffsetItems | None = "START",
    merge: bpy.stub_internal.rna_enums.KeyframePasteMergeItems | None = "MIX",
    flipped: bool | None = False,
) -> None:
    """Paste keyframes from the internal clipboard for the selected channels, starting on the current frame

    :type execution_context: int | str | None
    :type undo: bool | None
    :param offset: Offset, Paste time offset of keys
    :type offset: bpy.stub_internal.rna_enums.KeyframePasteOffsetItems | None
    :param merge: Type, Method of merging pasted keys and existing
    :type merge: bpy.stub_internal.rna_enums.KeyframePasteMergeItems | None
    :param flipped: Flipped, Paste keyframes from mirrored bones if they exist
    :type flipped: bool | None
    """

def previewrange_set(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Set Preview Range based on extents of selected Keyframes

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def push_down(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Push action down on to the NLA stack as a new strip

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
) -> None:
    """Toggle selection of all keyframes

        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Action, Selection action to execute

    TOGGLE
    Toggle -- Toggle selection for all elements.

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.

    INVERT
    Invert -- Invert selection of all elements.
        :type action: typing.Literal['TOGGLE','SELECT','DESELECT','INVERT'] | None
    """

def select_box(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    axis_range: bool | None = False,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
    tweak: bool | None = False,
) -> None:
    """Select all keyframes within the specified region

        :type execution_context: int | str | None
        :type undo: bool | None
        :param axis_range: Axis Range
        :type axis_range: bool | None
        :param xmin: X Min
        :type xmin: int | None
        :param xmax: X Max
        :type xmax: int | None
        :param ymin: Y Min
        :type ymin: int | None
        :param ymax: Y Max
        :type ymax: int | None
        :param wait_for_input: Wait for Input
        :type wait_for_input: bool | None
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
        :type mode: typing.Literal['SET','ADD','SUB'] | None
        :param tweak: Tweak, Operator has been activated using a click-drag event
        :type tweak: bool | None
    """

def select_circle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    x: int | None = 0,
    y: int | None = 0,
    radius: int | None = 25,
    wait_for_input: bool | None = True,
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
) -> None:
    """Select keyframe points using circle selection

        :type execution_context: int | str | None
        :type undo: bool | None
        :param x: X
        :type x: int | None
        :param y: Y
        :type y: int | None
        :param radius: Radius
        :type radius: int | None
        :param wait_for_input: Wait for Input
        :type wait_for_input: bool | None
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
        :type mode: typing.Literal['SET','ADD','SUB'] | None
    """

def select_column(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["KEYS", "CFRA", "MARKERS_COLUMN", "MARKERS_BETWEEN"]
    | None = "KEYS",
) -> None:
    """Select all keyframes on the specified frame(s)

    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: typing.Literal['KEYS','CFRA','MARKERS_COLUMN','MARKERS_BETWEEN'] | None
    """

def select_lasso(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    use_smooth_stroke: bool | None = False,
    smooth_stroke_factor: float | None = 0.75,
    smooth_stroke_radius: int | None = 35,
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
) -> None:
    """Select keyframe points using lasso selection

        :type execution_context: int | str | None
        :type undo: bool | None
        :param path: Path
        :type path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None
        :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path
        :type use_smooth_stroke: bool | None
        :param smooth_stroke_factor: Smooth Stroke Factor, Higher values gives a smoother stroke
        :type smooth_stroke_factor: float | None
        :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues
        :type smooth_stroke_radius: int | None
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
        :type mode: typing.Literal['SET','ADD','SUB'] | None
    """

def select_leftright(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["CHECK", "LEFT", "RIGHT"] | None = "CHECK",
    extend: bool | None = False,
) -> None:
    """Select keyframes to the left or the right of the current frame

    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: typing.Literal['CHECK','LEFT','RIGHT'] | None
    :param extend: Extend Select
    :type extend: bool | None
    """

def select_less(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Deselect keyframes on ends of selection islands

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_linked(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Select keyframes occurring in the same F-Curves as selected ones

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_more(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Select keyframes beside already selected ones

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def snap(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["CFRA", "NEAREST_FRAME", "NEAREST_SECOND", "NEAREST_MARKER"]
    | None = "CFRA",
) -> None:
    """Snap selected keyframes to the times specified

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    CFRA
    Selection to Current Frame -- Snap selected keyframes to the current frame.

    NEAREST_FRAME
    Selection to Nearest Frame -- Snap selected keyframes to the nearest (whole) frame (use to fix accidental subframe offsets).

    NEAREST_SECOND
    Selection to Nearest Second -- Snap selected keyframes to the nearest second.

    NEAREST_MARKER
    Selection to Nearest Marker -- Snap selected keyframes to the nearest marker.
        :type type: typing.Literal['CFRA','NEAREST_FRAME','NEAREST_SECOND','NEAREST_MARKER'] | None
    """

def stash(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    create_new: bool | None = True,
) -> None:
    """Store this action in the NLA stack as a non-contributing strip for later use

    :type execution_context: int | str | None
    :type undo: bool | None
    :param create_new: Create New Action, Create a new action once the existing one has been safely stored
    :type create_new: bool | None
    """

def stash_and_create(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Store this action in the NLA stack as a non-contributing strip for later use, and create a new action

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def unlink(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    force_delete: bool | None = False,
) -> None:
    """Unlink this action from the active action slot (and/or exit Tweak Mode)

    :type execution_context: int | str | None
    :type undo: bool | None
    :param force_delete: Force Delete, Clear Fake User and remove copy stashed in this data-block's NLA stack
    :type force_delete: bool | None
    """

def view_all(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Reset viewable area to show full keyframe range

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_frame(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Move the view to the current frame

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_selected(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Reset viewable area to show selected keyframes range

    :type execution_context: int | str | None
    :type undo: bool | None
    """
