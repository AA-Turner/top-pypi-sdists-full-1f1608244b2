import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops.transform
import bpy.stub_internal.rna_enums
import mathutils

def attribute_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value_float: float | None = 0.0,
    value_float_vector_2d: collections.abc.Iterable[float] | None = (0.0, 0.0),
    value_float_vector_3d: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    value_int: int | None = 0,
    value_int_vector_2d: collections.abc.Iterable[int] | None = (0, 0),
    value_color: collections.abc.Iterable[float] | None = (1.0, 1.0, 1.0, 1.0),
    value_bool: bool | None = False,
) -> None:
    """Set values of the active attribute for selected elements

    :type execution_context: int | str | None
    :type undo: bool | None
    :param value_float: Value
    :type value_float: float | None
    :param value_float_vector_2d: Value
    :type value_float_vector_2d: collections.abc.Iterable[float] | None
    :param value_float_vector_3d: Value
    :type value_float_vector_3d: collections.abc.Iterable[float] | None
    :param value_int: Value
    :type value_int: int | None
    :param value_int_vector_2d: Value
    :type value_int_vector_2d: collections.abc.Iterable[int] | None
    :param value_color: Value
    :type value_color: collections.abc.Iterable[float] | None
    :param value_bool: Value
    :type value_bool: bool | None
    """

def average_normals(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    average_type: typing.Literal["CUSTOM_NORMAL", "FACE_AREA", "CORNER_ANGLE"]
    | None = "CUSTOM_NORMAL",
    weight: int | None = 50,
    threshold: float | None = 0.01,
) -> None:
    """Average custom normals of selected vertices

        :type execution_context: int | str | None
        :type undo: bool | None
        :param average_type: Type, Averaging method

    CUSTOM_NORMAL
    Custom Normal -- Take average of vertex normals.

    FACE_AREA
    Face Area -- Set all vertex normals by face area.

    CORNER_ANGLE
    Corner Angle -- Set all vertex normals by corner angle.
        :type average_type: typing.Literal['CUSTOM_NORMAL','FACE_AREA','CORNER_ANGLE'] | None
        :param weight: Weight, Weight applied per face
        :type weight: int | None
        :param threshold: Threshold, Threshold value for different weights to be considered equal
        :type threshold: float | None
    """

def beautify_fill(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    angle_limit: float | None = 3.14159,
) -> None:
    """Rearrange some faces to try to get less degenerated geometry

    :type execution_context: int | str | None
    :type undo: bool | None
    :param angle_limit: Max Angle, Angle limit
    :type angle_limit: float | None
    """

def bevel(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    offset_type: typing.Literal["OFFSET", "WIDTH", "DEPTH", "PERCENT", "ABSOLUTE"]
    | None = "OFFSET",
    offset: float | None = 0.0,
    profile_type: typing.Literal["SUPERELLIPSE", "CUSTOM"] | None = "SUPERELLIPSE",
    offset_pct: float | None = 0.0,
    segments: int | None = 1,
    profile: float | None = 0.5,
    affect: typing.Literal["VERTICES", "EDGES"] | None = "EDGES",
    clamp_overlap: bool | None = False,
    loop_slide: bool | None = True,
    mark_seam: bool | None = False,
    mark_sharp: bool | None = False,
    material: int | None = -1,
    harden_normals: bool | None = False,
    face_strength_mode: typing.Literal["NONE", "NEW", "AFFECTED", "ALL"]
    | None = "NONE",
    miter_outer: typing.Literal["SHARP", "PATCH", "ARC"] | None = "SHARP",
    miter_inner: typing.Literal["SHARP", "ARC"] | None = "SHARP",
    spread: float | None = 0.1,
    vmesh_method: typing.Literal["ADJ", "CUTOFF"] | None = "ADJ",
    release_confirm: bool | None = False,
) -> None:
    """Cut into selected items at an angle to create bevel or chamfer

        :type execution_context: int | str | None
        :type undo: bool | None
        :param offset_type: Width Type, The method for determining the size of the bevel

    OFFSET
    Offset -- Amount is offset of new edges from original.

    WIDTH
    Width -- Amount is width of new face.

    DEPTH
    Depth -- Amount is perpendicular distance from original edge to bevel face.

    PERCENT
    Percent -- Amount is percent of adjacent edge length.

    ABSOLUTE
    Absolute -- Amount is absolute distance along adjacent edge.
        :type offset_type: typing.Literal['OFFSET','WIDTH','DEPTH','PERCENT','ABSOLUTE'] | None
        :param offset: Width, Bevel amount
        :type offset: float | None
        :param profile_type: Profile Type, The type of shape used to rebuild a beveled section

    SUPERELLIPSE
    Superellipse -- The profile can be a concave or convex curve.

    CUSTOM
    Custom -- The profile can be any arbitrary path between its endpoints.
        :type profile_type: typing.Literal['SUPERELLIPSE','CUSTOM'] | None
        :param offset_pct: Width Percent, Bevel amount for percentage method
        :type offset_pct: float | None
        :param segments: Segments, Segments for curved edge
        :type segments: int | None
        :param profile: Profile, Controls profile shape (0.5 = round)
        :type profile: float | None
        :param affect: Affect, Affect edges or vertices

    VERTICES
    Vertices -- Affect only vertices.

    EDGES
    Edges -- Affect only edges.
        :type affect: typing.Literal['VERTICES','EDGES'] | None
        :param clamp_overlap: Clamp Overlap, Do not allow beveled edges/vertices to overlap each other
        :type clamp_overlap: bool | None
        :param loop_slide: Loop Slide, Prefer sliding along edges to even widths
        :type loop_slide: bool | None
        :param mark_seam: Mark Seams, Mark Seams along beveled edges
        :type mark_seam: bool | None
        :param mark_sharp: Mark Sharp, Mark beveled edges as sharp
        :type mark_sharp: bool | None
        :param material: Material Index, Material for bevel faces (-1 means use adjacent faces)
        :type material: int | None
        :param harden_normals: Harden Normals, Match normals of new faces to adjacent faces
        :type harden_normals: bool | None
        :param face_strength_mode: Face Strength Mode, Whether to set face strength, and which faces to set face strength on

    NONE
    None -- Do not set face strength.

    NEW
    New -- Set face strength on new faces only.

    AFFECTED
    Affected -- Set face strength on new and modified faces only.

    ALL
    All -- Set face strength on all faces.
        :type face_strength_mode: typing.Literal['NONE','NEW','AFFECTED','ALL'] | None
        :param miter_outer: Outer Miter, Pattern to use for outside of miters

    SHARP
    Sharp -- Outside of miter is sharp.

    PATCH
    Patch -- Outside of miter is squared-off patch.

    ARC
    Arc -- Outside of miter is arc.
        :type miter_outer: typing.Literal['SHARP','PATCH','ARC'] | None
        :param miter_inner: Inner Miter, Pattern to use for inside of miters

    SHARP
    Sharp -- Inside of miter is sharp.

    ARC
    Arc -- Inside of miter is arc.
        :type miter_inner: typing.Literal['SHARP','ARC'] | None
        :param spread: Spread, Amount to spread arcs for arc inner miters
        :type spread: float | None
        :param vmesh_method: Vertex Mesh Method, The method to use to create meshes at intersections

    ADJ
    Grid Fill -- Default patterned fill.

    CUTOFF
    Cutoff -- A cutoff at each profile's end before the intersection.
        :type vmesh_method: typing.Literal['ADJ','CUTOFF'] | None
        :param release_confirm: Confirm on Release
        :type release_confirm: bool | None
    """

def bisect(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    plane_co: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    plane_no: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    use_fill: bool | None = False,
    clear_inner: bool | None = False,
    clear_outer: bool | None = False,
    threshold: float | None = 0.0001,
    xstart: int | None = 0,
    xend: int | None = 0,
    ystart: int | None = 0,
    yend: int | None = 0,
    flip: bool | None = False,
    cursor: int | None = 5,
) -> None:
    """Cut geometry along a plane (click-drag to define plane)

    :type execution_context: int | str | None
    :type undo: bool | None
    :param plane_co: Plane Point, A point on the plane
    :type plane_co: collections.abc.Sequence[float] | mathutils.Vector | None
    :param plane_no: Plane Normal, The direction the plane points
    :type plane_no: collections.abc.Sequence[float] | mathutils.Vector | None
    :param use_fill: Fill, Fill in the cut
    :type use_fill: bool | None
    :param clear_inner: Clear Inner, Remove geometry behind the plane
    :type clear_inner: bool | None
    :param clear_outer: Clear Outer, Remove geometry in front of the plane
    :type clear_outer: bool | None
    :param threshold: Axis Threshold, Preserves the existing geometry along the cut plane
    :type threshold: float | None
    :param xstart: X Start
    :type xstart: int | None
    :param xend: X End
    :type xend: int | None
    :param ystart: Y Start
    :type ystart: int | None
    :param yend: Y End
    :type yend: int | None
    :param flip: Flip
    :type flip: bool | None
    :param cursor: Cursor, Mouse cursor style to use during the modal operator
    :type cursor: int | None
    """

def blend_from_shape(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    shape: str | None = "",
    blend: float | None = 1.0,
    add: bool | None = True,
) -> None:
    """Blend in shape from a shape key

    :type execution_context: int | str | None
    :type undo: bool | None
    :param shape: Shape, Shape key to use for blending
    :type shape: str | None
    :param blend: Blend, Blending factor
    :type blend: float | None
    :param add: Add, Add rather than blend between shapes
    :type add: bool | None
    """

def bridge_edge_loops(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["SINGLE", "CLOSED", "PAIRS"] | None = "SINGLE",
    use_merge: bool | None = False,
    merge_factor: float | None = 0.5,
    twist_offset: int | None = 0,
    number_cuts: int | None = 0,
    interpolation: typing.Literal["LINEAR", "PATH", "SURFACE"] | None = "PATH",
    smoothness: float | None = 1.0,
    profile_shape_factor: float | None = 0.0,
    profile_shape: bpy.stub_internal.rna_enums.ProportionalFalloffCurveOnlyItems
    | None = "SMOOTH",
) -> None:
    """Create a bridge of faces between two or more selected edge loops

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Connect Loops, Method of bridging multiple loops
    :type type: typing.Literal['SINGLE','CLOSED','PAIRS'] | None
    :param use_merge: Merge, Merge rather than creating faces
    :type use_merge: bool | None
    :param merge_factor: Merge Factor
    :type merge_factor: float | None
    :param twist_offset: Twist, Twist offset for closed loops
    :type twist_offset: int | None
    :param number_cuts: Number of Cuts
    :type number_cuts: int | None
    :param interpolation: Interpolation, Interpolation method
    :type interpolation: typing.Literal['LINEAR','PATH','SURFACE'] | None
    :param smoothness: Smoothness, Smoothness factor
    :type smoothness: float | None
    :param profile_shape_factor: Profile Factor, How much intermediary new edges are shrunk/expanded
    :type profile_shape_factor: float | None
    :param profile_shape: Profile Shape, Shape of the profile
    :type profile_shape: bpy.stub_internal.rna_enums.ProportionalFalloffCurveOnlyItems | None
    """

def colors_reverse(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Flip direction of face corner color attribute inside faces

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def colors_rotate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_ccw: bool | None = False,
) -> None:
    """Rotate face corner color attribute inside faces

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_ccw: Counter Clockwise
    :type use_ccw: bool | None
    """

def convex_hull(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    delete_unused: bool | None = True,
    use_existing_faces: bool | None = True,
    make_holes: bool | None = False,
    join_triangles: bool | None = True,
    face_threshold: float | None = 0.698132,
    shape_threshold: float | None = 0.698132,
    topology_influence: float | None = 0.0,
    uvs: bool | None = False,
    vcols: bool | None = False,
    seam: bool | None = False,
    sharp: bool | None = False,
    materials: bool | None = False,
    deselect_joined: bool | None = False,
) -> None:
    """Enclose selected vertices in a convex polyhedron

    :type execution_context: int | str | None
    :type undo: bool | None
    :param delete_unused: Delete Unused, Delete selected elements that are not used by the hull
    :type delete_unused: bool | None
    :param use_existing_faces: Use Existing Faces, Skip hull triangles that are covered by a pre-existing face
    :type use_existing_faces: bool | None
    :param make_holes: Make Holes, Delete selected faces that are used by the hull
    :type make_holes: bool | None
    :param join_triangles: Join Triangles, Merge adjacent triangles into quads
    :type join_triangles: bool | None
    :param face_threshold: Max Face Angle, Face angle limit
    :type face_threshold: float | None
    :param shape_threshold: Max Shape Angle, Shape angle limit
    :type shape_threshold: float | None
    :param topology_influence: Topology Influence, How much to prioritize regular grids of quads as well as quads that touch existing quads
    :type topology_influence: float | None
    :param uvs: Compare UVs
    :type uvs: bool | None
    :param vcols: Compare Color Attributes
    :type vcols: bool | None
    :param seam: Compare Seam
    :type seam: bool | None
    :param sharp: Compare Sharp
    :type sharp: bool | None
    :param materials: Compare Materials
    :type materials: bool | None
    :param deselect_joined: Deselect Joined, Only select remaining triangles that were not merged
    :type deselect_joined: bool | None
    """

def customdata_custom_splitnormals_add(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Add a custom split normals layer, if none exists yet

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def customdata_custom_splitnormals_clear(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Remove the custom split normals layer, if it exists

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def customdata_mask_clear(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Clear vertex sculpt masking data from the mesh

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def customdata_skin_add(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Add a vertex skin layer

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def customdata_skin_clear(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Clear vertex skin layer

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def decimate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    ratio: float | None = 1.0,
    use_vertex_group: bool | None = False,
    vertex_group_factor: float | None = 1.0,
    invert_vertex_group: bool | None = False,
    use_symmetry: bool | None = False,
    symmetry_axis: bpy.stub_internal.rna_enums.AxisXyzItems | None = "Y",
) -> None:
    """Simplify geometry by collapsing edges

    :type execution_context: int | str | None
    :type undo: bool | None
    :param ratio: Ratio
    :type ratio: float | None
    :param use_vertex_group: Vertex Group, Use active vertex group as an influence
    :type use_vertex_group: bool | None
    :param vertex_group_factor: Weight, Vertex group strength
    :type vertex_group_factor: float | None
    :param invert_vertex_group: Invert, Invert vertex group influence
    :type invert_vertex_group: bool | None
    :param use_symmetry: Symmetry, Maintain symmetry on an axis
    :type use_symmetry: bool | None
    :param symmetry_axis: Axis, Axis of symmetry
    :type symmetry_axis: bpy.stub_internal.rna_enums.AxisXyzItems | None
    """

def delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["VERT", "EDGE", "FACE", "EDGE_FACE", "ONLY_FACE"]
    | None = "VERT",
) -> None:
    """Delete selected vertices, edges or faces

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type, Method used for deleting mesh data
    :type type: typing.Literal['VERT','EDGE','FACE','EDGE_FACE','ONLY_FACE'] | None
    """

def delete_edgeloop(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_face_split: bool | None = True,
) -> None:
    """Delete an edge loop by merging the faces on each side

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry
    :type use_face_split: bool | None
    """

def delete_loose(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_verts: bool | None = True,
    use_edges: bool | None = True,
    use_faces: bool | None = False,
) -> None:
    """Delete loose vertices, edges or faces

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_verts: Vertices, Remove loose vertices
    :type use_verts: bool | None
    :param use_edges: Edges, Remove loose edges
    :type use_edges: bool | None
    :param use_faces: Faces, Remove loose faces
    :type use_faces: bool | None
    """

def dissolve_degenerate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    threshold: float | None = 0.0001,
) -> None:
    """Dissolve zero area faces and zero length edges

    :type execution_context: int | str | None
    :type undo: bool | None
    :param threshold: Merge Distance, Maximum distance between elements to merge
    :type threshold: float | None
    """

def dissolve_edges(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_verts: bool | None = True,
    angle_threshold: float | None = 0.349066,
    use_face_split: bool | None = False,
) -> None:
    """Dissolve edges, merging faces

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_verts: Dissolve Vertices, Dissolve remaining vertices which connect to only two edges
    :type use_verts: bool | None
    :param angle_threshold: Angle Threshold, Remaining vertices which separate edge pairs are preserved if their edge angle exceeds this threshold.
    :type angle_threshold: float | None
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry
    :type use_face_split: bool | None
    """

def dissolve_faces(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_verts: bool | None = False,
) -> None:
    """Dissolve faces

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_verts: Dissolve Vertices, Dissolve remaining vertices which connect to only two edges
    :type use_verts: bool | None
    """

def dissolve_limited(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    angle_limit: float | None = 0.0872665,
    use_dissolve_boundaries: bool | None = False,
    delimit: set[bpy.stub_internal.rna_enums.MeshDelimitModeItems] | None = {"NORMAL"},
) -> None:
    """Dissolve selected edges and vertices, limited by the angle of surrounding geometry

    :type execution_context: int | str | None
    :type undo: bool | None
    :param angle_limit: Max Angle, Angle limit
    :type angle_limit: float | None
    :param use_dissolve_boundaries: All Boundaries, Dissolve all vertices in between face boundaries
    :type use_dissolve_boundaries: bool | None
    :param delimit: Delimit, Delimit dissolve operation
    :type delimit: set[bpy.stub_internal.rna_enums.MeshDelimitModeItems] | None
    """

def dissolve_mode(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_verts: bool | None = False,
    angle_threshold: float | None = 0.349066,
    use_face_split: bool | None = False,
    use_boundary_tear: bool | None = False,
) -> None:
    """Dissolve geometry based on the selection mode

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_verts: Dissolve Vertices, Dissolve remaining vertices which connect to only two edges
    :type use_verts: bool | None
    :param angle_threshold: Angle Threshold, Remaining vertices which separate edge pairs are preserved if their edge angle exceeds this threshold.
    :type angle_threshold: float | None
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry
    :type use_face_split: bool | None
    :param use_boundary_tear: Tear Boundary, Split off face corners instead of merging faces
    :type use_boundary_tear: bool | None
    """

def dissolve_verts(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_face_split: bool | None = False,
    use_boundary_tear: bool | None = False,
) -> None:
    """Dissolve vertices, merge edges and faces

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry
    :type use_face_split: bool | None
    :param use_boundary_tear: Tear Boundary, Split off face corners instead of merging faces
    :type use_boundary_tear: bool | None
    """

def dupli_extrude_cursor(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    rotate_source: bool | None = True,
) -> None:
    """Duplicate and extrude selected vertices, edges or faces towards the mouse cursor

    :type execution_context: int | str | None
    :type undo: bool | None
    :param rotate_source: Rotate Source, Rotate initial selection giving better shape
    :type rotate_source: bool | None
    """

def duplicate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: int | None = 1,
) -> None:
    """Duplicate selected vertices, edges or faces

    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: int | None
    """

def duplicate_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Duplicate mesh and move

    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_duplicate: Duplicate, Duplicate selected vertices, edges or faces
    :type MESH_OT_duplicate: duplicate | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def edge_collapse(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Collapse isolated edge and face regions, merging data such as UVs and color attributes. This can collapse edge-rings as well as regions of connected faces into vertices

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def edge_face_add(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Add an edge or face to selected

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def edge_rotate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_ccw: bool | None = False,
) -> None:
    """Rotate selected edge or adjoining faces

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_ccw: Counter Clockwise
    :type use_ccw: bool | None
    """

def edge_split(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["EDGE", "VERT"] | None = "EDGE",
) -> None:
    """Split selected edges so that each neighbor face gets its own copy

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type, Method to use for splitting

    EDGE
    Faces by Edges -- Split faces along selected edges.

    VERT
    Faces & Edges by Vertices -- Split faces and edges connected to selected vertices.
        :type type: typing.Literal['EDGE','VERT'] | None
    """

def edgering_select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    deselect: bool | None = False,
    toggle: bool | None = False,
    ring: bool | None = True,
) -> None:
    """Select an edge ring

    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend the selection
    :type extend: bool | None
    :param deselect: Deselect, Remove from the selection
    :type deselect: bool | None
    :param toggle: Toggle Select, Toggle the selection
    :type toggle: bool | None
    :param ring: Select Ring, Select ring
    :type ring: bool | None
    """

def edges_select_sharp(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    sharpness: float | None = 0.523599,
) -> None:
    """Select all sharp enough edges

    :type execution_context: int | str | None
    :type undo: bool | None
    :param sharpness: Sharpness
    :type sharpness: float | None
    """

def extrude_context(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_normal_flip: bool | None = False,
    use_dissolve_ortho_edges: bool | None = False,
    mirror: bool | None = False,
) -> None:
    """Extrude selection

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_normal_flip: Flip Normals
    :type use_normal_flip: bool | None
    :param use_dissolve_ortho_edges: Dissolve Orthogonal Edges
    :type use_dissolve_ortho_edges: bool | None
    :param mirror: Mirror Editing
    :type mirror: bool | None
    """

def extrude_context_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_extrude_context: extrude_context | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Extrude region together along the average normal

    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_extrude_context: Extrude Context, Extrude selection
    :type MESH_OT_extrude_context: extrude_context | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def extrude_edges_indiv(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_normal_flip: bool | None = False,
    mirror: bool | None = False,
) -> None:
    """Extrude individual edges only

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_normal_flip: Flip Normals
    :type use_normal_flip: bool | None
    :param mirror: Mirror Editing
    :type mirror: bool | None
    """

def extrude_edges_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_extrude_edges_indiv: extrude_edges_indiv | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Extrude edges and move result

    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_extrude_edges_indiv: Extrude Only Edges, Extrude individual edges only
    :type MESH_OT_extrude_edges_indiv: extrude_edges_indiv | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def extrude_faces_indiv(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mirror: bool | None = False,
) -> None:
    """Extrude individual faces only

    :type execution_context: int | str | None
    :type undo: bool | None
    :param mirror: Mirror Editing
    :type mirror: bool | None
    """

def extrude_faces_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_extrude_faces_indiv: extrude_faces_indiv | None = None,
    TRANSFORM_OT_shrink_fatten: bpy.ops.transform.shrink_fatten | None = None,
) -> None:
    """Extrude each individual face separately along local normals

    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_extrude_faces_indiv: Extrude Individual Faces, Extrude individual faces only
    :type MESH_OT_extrude_faces_indiv: extrude_faces_indiv | None
    :param TRANSFORM_OT_shrink_fatten: Shrink/Fatten, Shrink/fatten selected vertices along normals
    :type TRANSFORM_OT_shrink_fatten: bpy.ops.transform.shrink_fatten | None
    """

def extrude_manifold(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_extrude_region: extrude_region | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Extrude, dissolves edges whose faces form a flat surface and intersect new edges

    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces
    :type MESH_OT_extrude_region: extrude_region | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def extrude_region(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_normal_flip: bool | None = False,
    use_dissolve_ortho_edges: bool | None = False,
    mirror: bool | None = False,
) -> None:
    """Extrude region of faces

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_normal_flip: Flip Normals
    :type use_normal_flip: bool | None
    :param use_dissolve_ortho_edges: Dissolve Orthogonal Edges
    :type use_dissolve_ortho_edges: bool | None
    :param mirror: Mirror Editing
    :type mirror: bool | None
    """

def extrude_region_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_extrude_region: extrude_region | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Extrude region and move result

    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces
    :type MESH_OT_extrude_region: extrude_region | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def extrude_region_shrink_fatten(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_extrude_region: extrude_region | None = None,
    TRANSFORM_OT_shrink_fatten: bpy.ops.transform.shrink_fatten | None = None,
) -> None:
    """Extrude region together along local normals

    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces
    :type MESH_OT_extrude_region: extrude_region | None
    :param TRANSFORM_OT_shrink_fatten: Shrink/Fatten, Shrink/fatten selected vertices along normals
    :type TRANSFORM_OT_shrink_fatten: bpy.ops.transform.shrink_fatten | None
    """

def extrude_repeat(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    steps: int | None = 10,
    offset: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
    scale_offset: float | None = 1.0,
) -> None:
    """Extrude selected vertices, edges or faces repeatedly

    :type execution_context: int | str | None
    :type undo: bool | None
    :param steps: Steps
    :type steps: int | None
    :param offset: Offset, Offset vector
    :type offset: collections.abc.Sequence[float] | mathutils.Vector | None
    :param scale_offset: Scale Offset
    :type scale_offset: float | None
    """

def extrude_vertices_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_extrude_verts_indiv: extrude_verts_indiv | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Extrude vertices and move result

    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_extrude_verts_indiv: Extrude Only Vertices, Extrude individual vertices only
    :type MESH_OT_extrude_verts_indiv: extrude_verts_indiv | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def extrude_verts_indiv(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mirror: bool | None = False,
) -> None:
    """Extrude individual vertices only

    :type execution_context: int | str | None
    :type undo: bool | None
    :param mirror: Mirror Editing
    :type mirror: bool | None
    """

def face_make_planar(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 1.0,
    repeat: int | None = 1,
) -> None:
    """Flatten selected faces

    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Factor
    :type factor: float | None
    :param repeat: Iterations
    :type repeat: int | None
    """

def face_split_by_edges(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Weld loose edges into faces (splitting them into new faces)

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def faces_mirror_uv(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["POSITIVE", "NEGATIVE"] | None = "POSITIVE",
    precision: int | None = 3,
) -> None:
    """Copy mirror UV coordinates on the X axis based on a mirrored mesh

    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Axis Direction
    :type direction: typing.Literal['POSITIVE','NEGATIVE'] | None
    :param precision: Precision, Tolerance for finding vertex duplicates
    :type precision: int | None
    """

def faces_select_linked_flat(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    sharpness: float | None = 0.0174533,
) -> None:
    """Select linked faces by angle

    :type execution_context: int | str | None
    :type undo: bool | None
    :param sharpness: Sharpness
    :type sharpness: float | None
    """

def faces_shade_flat(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Display faces flat

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def faces_shade_smooth(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Display faces smooth (using vertex normals)

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def fill(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_beauty: bool | None = True,
) -> None:
    """Fill a selected edge loop with faces

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_beauty: Beauty, Use best triangulation division
    :type use_beauty: bool | None
    """

def fill_grid(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    span: int | None = 1,
    offset: int | None = 0,
    use_interp_simple: bool | None = False,
) -> None:
    """Fill grid from two loops

    :type execution_context: int | str | None
    :type undo: bool | None
    :param span: Span, Number of grid columns
    :type span: int | None
    :param offset: Offset, Vertex that is the corner of the grid
    :type offset: int | None
    :param use_interp_simple: Simple Blending, Use simple interpolation of grid vertices
    :type use_interp_simple: bool | None
    """

def fill_holes(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    sides: int | None = 4,
) -> None:
    """Fill in holes (boundary edge loops)

    :type execution_context: int | str | None
    :type undo: bool | None
    :param sides: Sides, Number of sides in hole required to fill (zero fills all holes)
    :type sides: int | None
    """

def flip_normals(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    only_clnors: bool | None = False,
) -> None:
    """Flip the direction of selected faces' normals (and of their vertices)

    :type execution_context: int | str | None
    :type undo: bool | None
    :param only_clnors: Custom Normals Only, Only flip the custom loop normals of the selected elements
    :type only_clnors: bool | None
    """

def flip_quad_tessellation(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Flips the tessellation of selected quads

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def hide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    unselected: bool | None = False,
) -> None:
    """Hide (un)selected vertices, edges or faces

    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Hide unselected rather than selected
    :type unselected: bool | None
    """

def inset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_boundary: bool | None = True,
    use_even_offset: bool | None = True,
    use_relative_offset: bool | None = False,
    use_edge_rail: bool | None = False,
    thickness: float | None = 0.0,
    depth: float | None = 0.0,
    use_outset: bool | None = False,
    use_select_inset: bool | None = False,
    use_individual: bool | None = False,
    use_interpolate: bool | None = True,
    release_confirm: bool | None = False,
) -> None:
    """Inset new faces into selected faces

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_boundary: Boundary, Inset face boundaries
    :type use_boundary: bool | None
    :param use_even_offset: Offset Even, Scale the offset to give more even thickness
    :type use_even_offset: bool | None
    :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry
    :type use_relative_offset: bool | None
    :param use_edge_rail: Edge Rail, Inset the region along existing edges
    :type use_edge_rail: bool | None
    :param thickness: Thickness
    :type thickness: float | None
    :param depth: Depth
    :type depth: float | None
    :param use_outset: Outset, Outset rather than inset
    :type use_outset: bool | None
    :param use_select_inset: Select Outer, Select the new inset faces
    :type use_select_inset: bool | None
    :param use_individual: Individual, Individual face inset
    :type use_individual: bool | None
    :param use_interpolate: Interpolate, Blend face data across the inset
    :type use_interpolate: bool | None
    :param release_confirm: Confirm on Release
    :type release_confirm: bool | None
    """

def intersect(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["SELECT", "SELECT_UNSELECT"] | None = "SELECT_UNSELECT",
    separate_mode: typing.Literal["ALL", "CUT", "NONE"] | None = "CUT",
    threshold: float | None = 1e-06,
    solver: typing.Literal["FAST", "EXACT"] | None = "EXACT",
) -> None:
    """Cut an intersection into faces

        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Source

    SELECT
    Self Intersect -- Self intersect selected faces.

    SELECT_UNSELECT
    Selected/Unselected -- Intersect selected with unselected faces.
        :type mode: typing.Literal['SELECT','SELECT_UNSELECT'] | None
        :param separate_mode: Separate Mode

    ALL
    All -- Separate all geometry from intersections.

    CUT
    Cut -- Cut into geometry keeping each side separate (Selected/Unselected only).

    NONE
    Merge -- Merge all geometry from the intersection.
        :type separate_mode: typing.Literal['ALL','CUT','NONE'] | None
        :param threshold: Merge Threshold
        :type threshold: float | None
        :param solver: Solver, Which Intersect solver to use

    FAST
    Float -- Simple solver with good performance, without support for overlapping geometry.

    EXACT
    Exact -- Slower solver with the best results for coplanar faces.
        :type solver: typing.Literal['FAST','EXACT'] | None
    """

def intersect_boolean(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    operation: typing.Literal["INTERSECT", "UNION", "DIFFERENCE"] | None = "DIFFERENCE",
    use_swap: bool | None = False,
    use_self: bool | None = False,
    threshold: float | None = 1e-06,
    solver: typing.Literal["FAST", "EXACT"] | None = "EXACT",
) -> None:
    """Cut solid geometry from selected to unselected

        :type execution_context: int | str | None
        :type undo: bool | None
        :param operation: Boolean Operation, Which boolean operation to apply
        :type operation: typing.Literal['INTERSECT','UNION','DIFFERENCE'] | None
        :param use_swap: Swap, Use with difference intersection to swap which side is kept
        :type use_swap: bool | None
        :param use_self: Self Intersection, Do self-union or self-intersection
        :type use_self: bool | None
        :param threshold: Merge Threshold
        :type threshold: float | None
        :param solver: Solver, Which Boolean solver to use

    FAST
    Fast -- Faster solver, some limitations.

    EXACT
    Exact -- Exact solver, slower, handles more cases.
        :type solver: typing.Literal['FAST','EXACT'] | None
    """

def knife_project(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    cut_through: bool | None = False,
) -> None:
    """Use other objects outlines and boundaries to project knife cuts

    :type execution_context: int | str | None
    :type undo: bool | None
    :param cut_through: Cut Through, Cut through all faces, not just visible ones
    :type cut_through: bool | None
    """

def knife_tool(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_occlude_geometry: bool | None = True,
    only_selected: bool | None = False,
    xray: bool | None = True,
    visible_measurements: typing.Literal["NONE", "BOTH", "DISTANCE", "ANGLE"]
    | None = "NONE",
    angle_snapping: typing.Literal["NONE", "SCREEN", "RELATIVE"] | None = "NONE",
    angle_snapping_increment: float | None = 0.523599,
    wait_for_input: bool | None = True,
) -> None:
    """Cut new topology

        :type execution_context: int | str | None
        :type undo: bool | None
        :param use_occlude_geometry: Occlude Geometry, Only cut the front most geometry
        :type use_occlude_geometry: bool | None
        :param only_selected: Only Selected, Only cut selected geometry
        :type only_selected: bool | None
        :param xray: X-Ray, Show cuts hidden by geometry
        :type xray: bool | None
        :param visible_measurements: Measurements, Visible distance and angle measurements

    NONE
    None -- Show no measurements.

    BOTH
    Both -- Show both distances and angles.

    DISTANCE
    Distance -- Show just distance measurements.

    ANGLE
    Angle -- Show just angle measurements.
        :type visible_measurements: typing.Literal['NONE','BOTH','DISTANCE','ANGLE'] | None
        :param angle_snapping: Angle Snapping, Angle snapping mode

    NONE
    None -- No angle snapping.

    SCREEN
    Screen -- Screen space angle snapping.

    RELATIVE
    Relative -- Angle snapping relative to the previous cut edge.
        :type angle_snapping: typing.Literal['NONE','SCREEN','RELATIVE'] | None
        :param angle_snapping_increment: Angle Snap Increment, The angle snap increment used when in constrained angle mode
        :type angle_snapping_increment: float | None
        :param wait_for_input: Wait for Input
        :type wait_for_input: bool | None
    """

def loop_multi_select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    ring: bool | None = False,
) -> None:
    """Select a loop of connected edges by connection type

    :type execution_context: int | str | None
    :type undo: bool | None
    :param ring: Ring
    :type ring: bool | None
    """

def loop_select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    deselect: bool | None = False,
    toggle: bool | None = False,
    ring: bool | None = False,
) -> None:
    """Select a loop of connected edges

    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend Select, Extend the selection
    :type extend: bool | None
    :param deselect: Deselect, Remove from the selection
    :type deselect: bool | None
    :param toggle: Toggle Select, Toggle the selection
    :type toggle: bool | None
    :param ring: Select Ring, Select ring
    :type ring: bool | None
    """

def loop_to_region(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select_bigger: bool | None = False,
) -> None:
    """Select region of faces inside of a selected loop of edges

    :type execution_context: int | str | None
    :type undo: bool | None
    :param select_bigger: Select Bigger, Select bigger regions instead of smaller ones
    :type select_bigger: bool | None
    """

def loopcut(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    number_cuts: int | None = 1,
    smoothness: float | None = 0.0,
    falloff: bpy.stub_internal.rna_enums.ProportionalFalloffCurveOnlyItems
    | None = "INVERSE_SQUARE",
    object_index: int | None = -1,
    edge_index: int | None = -1,
    mesh_select_mode_init: collections.abc.Iterable[bool] | None = (
        False,
        False,
        False,
    ),
) -> None:
    """Add a new loop between existing loops

    :type execution_context: int | str | None
    :type undo: bool | None
    :param number_cuts: Number of Cuts
    :type number_cuts: int | None
    :param smoothness: Smoothness, Smoothness factor
    :type smoothness: float | None
    :param falloff: Falloff, Falloff type of the feather
    :type falloff: bpy.stub_internal.rna_enums.ProportionalFalloffCurveOnlyItems | None
    :param object_index: Object Index
    :type object_index: int | None
    :param edge_index: Edge Index
    :type edge_index: int | None
    :type mesh_select_mode_init: collections.abc.Iterable[bool] | None
    """

def loopcut_slide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_loopcut: loopcut | None = None,
    TRANSFORM_OT_edge_slide: bpy.ops.transform.edge_slide | None = None,
) -> None:
    """Cut mesh loop and slide it

    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_loopcut: Loop Cut, Add a new loop between existing loops
    :type MESH_OT_loopcut: loopcut | None
    :param TRANSFORM_OT_edge_slide: Edge Slide, Slide an edge loop along a mesh
    :type TRANSFORM_OT_edge_slide: bpy.ops.transform.edge_slide | None
    """

def mark_freestyle_edge(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    clear: bool | None = False,
) -> None:
    """(Un)mark selected edges as Freestyle feature edges

    :type execution_context: int | str | None
    :type undo: bool | None
    :param clear: Clear
    :type clear: bool | None
    """

def mark_freestyle_face(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    clear: bool | None = False,
) -> None:
    """(Un)mark selected faces for exclusion from Freestyle feature edge detection

    :type execution_context: int | str | None
    :type undo: bool | None
    :param clear: Clear
    :type clear: bool | None
    """

def mark_seam(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    clear: bool | None = False,
) -> None:
    """(Un)mark selected edges as a seam

    :type execution_context: int | str | None
    :type undo: bool | None
    :param clear: Clear
    :type clear: bool | None
    """

def mark_sharp(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    clear: bool | None = False,
    use_verts: bool | None = False,
) -> None:
    """(Un)mark selected edges as sharp

    :type execution_context: int | str | None
    :type undo: bool | None
    :param clear: Clear
    :type clear: bool | None
    :param use_verts: Vertices, Consider vertices instead of edges to select which edges to (un)tag as sharp
    :type use_verts: bool | None
    """

def merge(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["CENTER", "CURSOR", "COLLAPSE", "FIRST", "LAST"]
    | None = "CENTER",
    uvs: bool | None = False,
) -> None:
    """Merge selected vertices

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type, Merge method to use
    :type type: typing.Literal['CENTER','CURSOR','COLLAPSE','FIRST','LAST'] | None
    :param uvs: UVs, Move UVs according to merge
    :type uvs: bool | None
    """

def merge_normals(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Merge custom normals of selected vertices

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def mod_weighted_strength(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    set: bool | None = False,
    face_strength: typing.Literal["WEAK", "MEDIUM", "STRONG"] | None = "MEDIUM",
) -> None:
    """Set/Get strength of face (used in Weighted Normal modifier)

    :type execution_context: int | str | None
    :type undo: bool | None
    :param set: Set Value, Set value of faces
    :type set: bool | None
    :param face_strength: Face Strength, Strength to use for assigning or selecting face influence for weighted normal modifier
    :type face_strength: typing.Literal['WEAK','MEDIUM','STRONG'] | None
    """

def normals_make_consistent(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    inside: bool | None = False,
) -> None:
    """Make face and vertex normals point either outside or inside the mesh

    :type execution_context: int | str | None
    :type undo: bool | None
    :param inside: Inside
    :type inside: bool | None
    """

def normals_tools(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["COPY", "PASTE", "ADD", "MULTIPLY", "RESET"] | None = "COPY",
    absolute: bool | None = False,
) -> None:
    """Custom normals tools using Normal Vector of UI

        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode, Mode of tools taking input from interface

    COPY
    Copy Normal -- Copy normal to the internal clipboard.

    PASTE
    Paste Normal -- Paste normal from the internal clipboard.

    ADD
    Add Normal -- Add normal vector with selection.

    MULTIPLY
    Multiply Normal -- Multiply normal vector with selection.

    RESET
    Reset Normal -- Reset the internal clipboard and/or normal of selected element.
        :type mode: typing.Literal['COPY','PASTE','ADD','MULTIPLY','RESET'] | None
        :param absolute: Absolute Coordinates, Copy Absolute coordinates of Normal vector
        :type absolute: bool | None
    """

def offset_edge_loops(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_cap_endpoint: bool | None = False,
) -> None:
    """Create offset edge loop from the current selection

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_cap_endpoint: Cap Endpoint, Extend loop around end-points
    :type use_cap_endpoint: bool | None
    """

def offset_edge_loops_slide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_offset_edge_loops: offset_edge_loops | None = None,
    TRANSFORM_OT_edge_slide: bpy.ops.transform.edge_slide | None = None,
) -> None:
    """Offset edge loop slide

    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_offset_edge_loops: Offset Edge Loop, Create offset edge loop from the current selection
    :type MESH_OT_offset_edge_loops: offset_edge_loops | None
    :param TRANSFORM_OT_edge_slide: Edge Slide, Slide an edge loop along a mesh
    :type TRANSFORM_OT_edge_slide: bpy.ops.transform.edge_slide | None
    """

def point_normals(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["COORDINATES", "MOUSE"] | None = "COORDINATES",
    invert: bool | None = False,
    align: bool | None = False,
    target_location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    spherize: bool | None = False,
    spherize_strength: float | None = 0.1,
) -> None:
    """Point selected custom normals to specified Target

        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode, How to define coordinates to point custom normals to

    COORDINATES
    Coordinates -- Use static coordinates (defined by various means).

    MOUSE
    Mouse -- Follow mouse cursor.
        :type mode: typing.Literal['COORDINATES','MOUSE'] | None
        :param invert: Invert, Invert affected normals
        :type invert: bool | None
        :param align: Align, Make all affected normals parallel
        :type align: bool | None
        :param target_location: Target, Target location to which normals will point
        :type target_location: collections.abc.Sequence[float] | mathutils.Vector | None
        :param spherize: Spherize, Interpolate between original and new normals
        :type spherize: bool | None
        :param spherize_strength: Spherize Strength, Ratio of spherized normal to original normal
        :type spherize_strength: float | None
    """

def poke(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    offset: float | None = 0.0,
    use_relative_offset: bool | None = False,
    center_mode: typing.Literal["MEDIAN_WEIGHTED", "MEDIAN", "BOUNDS"]
    | None = "MEDIAN_WEIGHTED",
) -> None:
    """Split a face into a fan

        :type execution_context: int | str | None
        :type undo: bool | None
        :param offset: Poke Offset, Poke Offset
        :type offset: float | None
        :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry
        :type use_relative_offset: bool | None
        :param center_mode: Poke Center, Poke face center calculation

    MEDIAN_WEIGHTED
    Weighted Median -- Weighted median face center.

    MEDIAN
    Median -- Median face center.

    BOUNDS
    Bounds -- Face bounds center.
        :type center_mode: typing.Literal['MEDIAN_WEIGHTED','MEDIAN','BOUNDS'] | None
    """

def polybuild_delete_at_cursor(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
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
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | None
    """

def polybuild_dissolve_at_cursor(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def polybuild_extrude_at_cursor_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_polybuild_transform_at_cursor: polybuild_transform_at_cursor | None = None,
    MESH_OT_extrude_edges_indiv: extrude_edges_indiv | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_polybuild_transform_at_cursor: Poly Build Transform at Cursor
    :type MESH_OT_polybuild_transform_at_cursor: polybuild_transform_at_cursor | None
    :param MESH_OT_extrude_edges_indiv: Extrude Only Edges, Extrude individual edges only
    :type MESH_OT_extrude_edges_indiv: extrude_edges_indiv | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def polybuild_face_at_cursor(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    create_quads: bool | None = True,
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    :param create_quads: Create Quads, Automatically split edges in triangles to maintain quad topology
    :type create_quads: bool | None
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
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | None
    """

def polybuild_face_at_cursor_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_polybuild_face_at_cursor: polybuild_face_at_cursor | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_polybuild_face_at_cursor: Poly Build Face at Cursor
    :type MESH_OT_polybuild_face_at_cursor: polybuild_face_at_cursor | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def polybuild_split_at_cursor(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
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
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | None
    """

def polybuild_split_at_cursor_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_polybuild_split_at_cursor: polybuild_split_at_cursor | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_polybuild_split_at_cursor: Poly Build Split at Cursor
    :type MESH_OT_polybuild_split_at_cursor: polybuild_split_at_cursor | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def polybuild_transform_at_cursor(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
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
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | None
    """

def polybuild_transform_at_cursor_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_polybuild_transform_at_cursor: polybuild_transform_at_cursor | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_polybuild_transform_at_cursor: Poly Build Transform at Cursor
    :type MESH_OT_polybuild_transform_at_cursor: polybuild_transform_at_cursor | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def primitive_circle_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    vertices: int | None = 32,
    radius: float | None = 1.0,
    fill_type: typing.Literal["NOTHING", "NGON", "TRIFAN"] | None = "NOTHING",
    calc_uvs: bool | None = True,
    enter_editmode: bool | None = False,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Construct a circle mesh

        :type execution_context: int | str | None
        :type undo: bool | None
        :param vertices: Vertices
        :type vertices: int | None
        :param radius: Radius
        :type radius: float | None
        :param fill_type: Fill Type

    NOTHING
    Nothing -- Don't fill at all.

    NGON
    N-Gon -- Use n-gons.

    TRIFAN
    Triangle Fan -- Use triangle fans.
        :type fill_type: typing.Literal['NOTHING','NGON','TRIFAN'] | None
        :param calc_uvs: Generate UVs, Generate a default UV map
        :type calc_uvs: bool | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: typing.Literal['WORLD','VIEW','CURSOR'] | None
        :param location: Location, Location for the newly added object
        :type location: collections.abc.Sequence[float] | mathutils.Vector | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: collections.abc.Sequence[float] | mathutils.Euler | None
        :param scale: Scale, Scale for the newly added object
        :type scale: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def primitive_cone_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    vertices: int | None = 32,
    radius1: float | None = 1.0,
    radius2: float | None = 0.0,
    depth: float | None = 2.0,
    end_fill_type: typing.Literal["NOTHING", "NGON", "TRIFAN"] | None = "NGON",
    calc_uvs: bool | None = True,
    enter_editmode: bool | None = False,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Construct a conic mesh

        :type execution_context: int | str | None
        :type undo: bool | None
        :param vertices: Vertices
        :type vertices: int | None
        :param radius1: Radius 1
        :type radius1: float | None
        :param radius2: Radius 2
        :type radius2: float | None
        :param depth: Depth
        :type depth: float | None
        :param end_fill_type: Base Fill Type

    NOTHING
    Nothing -- Don't fill at all.

    NGON
    N-Gon -- Use n-gons.

    TRIFAN
    Triangle Fan -- Use triangle fans.
        :type end_fill_type: typing.Literal['NOTHING','NGON','TRIFAN'] | None
        :param calc_uvs: Generate UVs, Generate a default UV map
        :type calc_uvs: bool | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: typing.Literal['WORLD','VIEW','CURSOR'] | None
        :param location: Location, Location for the newly added object
        :type location: collections.abc.Sequence[float] | mathutils.Vector | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: collections.abc.Sequence[float] | mathutils.Euler | None
        :param scale: Scale, Scale for the newly added object
        :type scale: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def primitive_cube_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    size: float | None = 2.0,
    calc_uvs: bool | None = True,
    enter_editmode: bool | None = False,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Construct a cube mesh that consists of six square faces

        :type execution_context: int | str | None
        :type undo: bool | None
        :param size: Size
        :type size: float | None
        :param calc_uvs: Generate UVs, Generate a default UV map
        :type calc_uvs: bool | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: typing.Literal['WORLD','VIEW','CURSOR'] | None
        :param location: Location, Location for the newly added object
        :type location: collections.abc.Sequence[float] | mathutils.Vector | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: collections.abc.Sequence[float] | mathutils.Euler | None
        :param scale: Scale, Scale for the newly added object
        :type scale: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def primitive_cube_add_gizmo(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    calc_uvs: bool | None = True,
    enter_editmode: bool | None = False,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
    matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix
    | None = (
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
    ),
) -> None:
    """Construct a cube mesh

        :type execution_context: int | str | None
        :type undo: bool | None
        :param calc_uvs: Generate UVs, Generate a default UV map
        :type calc_uvs: bool | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: typing.Literal['WORLD','VIEW','CURSOR'] | None
        :param location: Location, Location for the newly added object
        :type location: collections.abc.Sequence[float] | mathutils.Vector | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: collections.abc.Sequence[float] | mathutils.Euler | None
        :param scale: Scale, Scale for the newly added object
        :type scale: collections.abc.Sequence[float] | mathutils.Vector | None
        :param matrix: Matrix
        :type matrix: collections.abc.Sequence[collections.abc.Sequence[float]] | mathutils.Matrix | None
    """

def primitive_cylinder_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    vertices: int | None = 32,
    radius: float | None = 1.0,
    depth: float | None = 2.0,
    end_fill_type: typing.Literal["NOTHING", "NGON", "TRIFAN"] | None = "NGON",
    calc_uvs: bool | None = True,
    enter_editmode: bool | None = False,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Construct a cylinder mesh

        :type execution_context: int | str | None
        :type undo: bool | None
        :param vertices: Vertices
        :type vertices: int | None
        :param radius: Radius
        :type radius: float | None
        :param depth: Depth
        :type depth: float | None
        :param end_fill_type: Cap Fill Type

    NOTHING
    Nothing -- Don't fill at all.

    NGON
    N-Gon -- Use n-gons.

    TRIFAN
    Triangle Fan -- Use triangle fans.
        :type end_fill_type: typing.Literal['NOTHING','NGON','TRIFAN'] | None
        :param calc_uvs: Generate UVs, Generate a default UV map
        :type calc_uvs: bool | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: typing.Literal['WORLD','VIEW','CURSOR'] | None
        :param location: Location, Location for the newly added object
        :type location: collections.abc.Sequence[float] | mathutils.Vector | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: collections.abc.Sequence[float] | mathutils.Euler | None
        :param scale: Scale, Scale for the newly added object
        :type scale: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def primitive_grid_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    x_subdivisions: int | None = 10,
    y_subdivisions: int | None = 10,
    size: float | None = 2.0,
    calc_uvs: bool | None = True,
    enter_editmode: bool | None = False,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Construct a subdivided plane mesh

        :type execution_context: int | str | None
        :type undo: bool | None
        :param x_subdivisions: X Subdivisions
        :type x_subdivisions: int | None
        :param y_subdivisions: Y Subdivisions
        :type y_subdivisions: int | None
        :param size: Size
        :type size: float | None
        :param calc_uvs: Generate UVs, Generate a default UV map
        :type calc_uvs: bool | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: typing.Literal['WORLD','VIEW','CURSOR'] | None
        :param location: Location, Location for the newly added object
        :type location: collections.abc.Sequence[float] | mathutils.Vector | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: collections.abc.Sequence[float] | mathutils.Euler | None
        :param scale: Scale, Scale for the newly added object
        :type scale: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def primitive_ico_sphere_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    subdivisions: int | None = 2,
    radius: float | None = 1.0,
    calc_uvs: bool | None = True,
    enter_editmode: bool | None = False,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Construct a spherical mesh that consists of equally sized triangles

        :type execution_context: int | str | None
        :type undo: bool | None
        :param subdivisions: Subdivisions
        :type subdivisions: int | None
        :param radius: Radius
        :type radius: float | None
        :param calc_uvs: Generate UVs, Generate a default UV map
        :type calc_uvs: bool | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: typing.Literal['WORLD','VIEW','CURSOR'] | None
        :param location: Location, Location for the newly added object
        :type location: collections.abc.Sequence[float] | mathutils.Vector | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: collections.abc.Sequence[float] | mathutils.Euler | None
        :param scale: Scale, Scale for the newly added object
        :type scale: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def primitive_monkey_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    size: float | None = 2.0,
    calc_uvs: bool | None = True,
    enter_editmode: bool | None = False,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Construct a Suzanne mesh

        :type execution_context: int | str | None
        :type undo: bool | None
        :param size: Size
        :type size: float | None
        :param calc_uvs: Generate UVs, Generate a default UV map
        :type calc_uvs: bool | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: typing.Literal['WORLD','VIEW','CURSOR'] | None
        :param location: Location, Location for the newly added object
        :type location: collections.abc.Sequence[float] | mathutils.Vector | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: collections.abc.Sequence[float] | mathutils.Euler | None
        :param scale: Scale, Scale for the newly added object
        :type scale: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def primitive_plane_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    size: float | None = 2.0,
    calc_uvs: bool | None = True,
    enter_editmode: bool | None = False,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Construct a filled planar mesh with 4 vertices

        :type execution_context: int | str | None
        :type undo: bool | None
        :param size: Size
        :type size: float | None
        :param calc_uvs: Generate UVs, Generate a default UV map
        :type calc_uvs: bool | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: typing.Literal['WORLD','VIEW','CURSOR'] | None
        :param location: Location, Location for the newly added object
        :type location: collections.abc.Sequence[float] | mathutils.Vector | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: collections.abc.Sequence[float] | mathutils.Euler | None
        :param scale: Scale, Scale for the newly added object
        :type scale: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def primitive_torus_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    major_segments: int | None = 48,
    minor_segments: int | None = 12,
    mode: typing.Literal["MAJOR_MINOR", "EXT_INT"] | None = "MAJOR_MINOR",
    major_radius: float | None = 1.0,
    minor_radius: float | None = 0.25,
    abso_major_rad: float | None = 1.25,
    abso_minor_rad: float | None = 0.75,
    generate_uvs: bool | None = True,
) -> None:
    """Construct a torus mesh

        :type execution_context: int | str | None
        :type undo: bool | None
        :param align: Align

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: typing.Literal['WORLD','VIEW','CURSOR'] | None
        :param location: Location
        :type location: collections.abc.Sequence[float] | mathutils.Vector | None
        :param rotation: Rotation
        :type rotation: collections.abc.Sequence[float] | mathutils.Euler | None
        :param major_segments: Major Segments, Number of segments for the main ring of the torus
        :type major_segments: int | None
        :param minor_segments: Minor Segments, Number of segments for the minor ring of the torus
        :type minor_segments: int | None
        :param mode: Dimensions Mode

    MAJOR_MINOR
    Major/Minor -- Use the major/minor radii for torus dimensions.

    EXT_INT
    Exterior/Interior -- Use the exterior/interior radii for torus dimensions.
        :type mode: typing.Literal['MAJOR_MINOR','EXT_INT'] | None
        :param major_radius: Major Radius, Radius from the origin to the center of the cross sections
        :type major_radius: float | None
        :param minor_radius: Minor Radius, Radius of the torus' cross section
        :type minor_radius: float | None
        :param abso_major_rad: Exterior Radius, Total Exterior Radius of the torus
        :type abso_major_rad: float | None
        :param abso_minor_rad: Interior Radius, Total Interior Radius of the torus
        :type abso_minor_rad: float | None
        :param generate_uvs: Generate UVs, Generate a default UV map
        :type generate_uvs: bool | None
    """

def primitive_uv_sphere_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    segments: int | None = 32,
    ring_count: int | None = 16,
    radius: float | None = 1.0,
    calc_uvs: bool | None = True,
    enter_editmode: bool | None = False,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Construct a spherical mesh with quad faces, except for triangle faces at the top and bottom

        :type execution_context: int | str | None
        :type undo: bool | None
        :param segments: Segments
        :type segments: int | None
        :param ring_count: Rings
        :type ring_count: int | None
        :param radius: Radius
        :type radius: float | None
        :param calc_uvs: Generate UVs, Generate a default UV map
        :type calc_uvs: bool | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: typing.Literal['WORLD','VIEW','CURSOR'] | None
        :param location: Location, Location for the newly added object
        :type location: collections.abc.Sequence[float] | mathutils.Vector | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: collections.abc.Sequence[float] | mathutils.Euler | None
        :param scale: Scale, Scale for the newly added object
        :type scale: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def quads_convert_to_tris(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    quad_method: bpy.stub_internal.rna_enums.ModifierTriangulateQuadMethodItems
    | None = "BEAUTY",
    ngon_method: bpy.stub_internal.rna_enums.ModifierTriangulateNgonMethodItems
    | None = "BEAUTY",
) -> None:
    """Triangulate selected faces

    :type execution_context: int | str | None
    :type undo: bool | None
    :param quad_method: Quad Method, Method for splitting the quads into triangles
    :type quad_method: bpy.stub_internal.rna_enums.ModifierTriangulateQuadMethodItems | None
    :param ngon_method: N-gon Method, Method for splitting the n-gons into triangles
    :type ngon_method: bpy.stub_internal.rna_enums.ModifierTriangulateNgonMethodItems | None
    """

def region_to_loop(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Select boundary edges around the selected faces

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def remove_doubles(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    threshold: float | None = 0.0001,
    use_unselected: bool | None = False,
    use_sharp_edge_from_normals: bool | None = False,
) -> None:
    """Merge vertices based on their proximity

    :type execution_context: int | str | None
    :type undo: bool | None
    :param threshold: Merge Distance, Maximum distance between elements to merge
    :type threshold: float | None
    :param use_unselected: Unselected, Merge selected to other unselected vertices
    :type use_unselected: bool | None
    :param use_sharp_edge_from_normals: Sharp Edges, Calculate sharp edges using custom normal data (when available)
    :type use_sharp_edge_from_normals: bool | None
    """

def reveal(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select: bool | None = True,
) -> None:
    """Reveal all hidden vertices, edges and faces

    :type execution_context: int | str | None
    :type undo: bool | None
    :param select: Select
    :type select: bool | None
    """

def rip(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
    use_fill: bool | None = False,
) -> None:
    """Disconnect vertex or edges from connected geometry

    :type execution_context: int | str | None
    :type undo: bool | None
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
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | None
    :param use_fill: Fill, Fill the ripped region
    :type use_fill: bool | None
    """

def rip_edge(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mirror: bool | None = False,
    use_proportional_edit: bool | None = False,
    proportional_edit_falloff: bpy.stub_internal.rna_enums.ProportionalFalloffItems
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    use_proportional_connected: bool | None = False,
    use_proportional_projected: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
) -> None:
    """Extend vertices along the edge closest to the cursor

    :type execution_context: int | str | None
    :type undo: bool | None
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
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | None
    """

def rip_edge_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_rip_edge: rip_edge | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Extend vertices and move the result

    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_rip_edge: Extend Vertices, Extend vertices along the edge closest to the cursor
    :type MESH_OT_rip_edge: rip_edge | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def rip_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_rip: rip | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Rip polygons and move the result

    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_rip: Rip, Disconnect vertex or edges from connected geometry
    :type MESH_OT_rip: rip | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def screw(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    steps: int | None = 9,
    turns: int | None = 1,
    center: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
    axis: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Extrude selected vertices in screw-shaped rotation around the cursor in indicated viewport

    :type execution_context: int | str | None
    :type undo: bool | None
    :param steps: Steps, Steps
    :type steps: int | None
    :param turns: Turns, Turns
    :type turns: int | None
    :param center: Center, Center in global view space
    :type center: collections.abc.Sequence[float] | mathutils.Vector | None
    :param axis: Axis, Axis in global view space
    :type axis: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
) -> None:
    """(De)select all vertices, edges or faces

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

def select_axis(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    orientation: bpy.stub_internal.rna_enums.TransformOrientationItems | None = "LOCAL",
    sign: typing.Literal["POS", "NEG", "ALIGN"] | None = "POS",
    axis: bpy.stub_internal.rna_enums.AxisXyzItems | None = "X",
    threshold: float | None = 0.0001,
) -> None:
    """Select all data in the mesh on a single axis

    :type execution_context: int | str | None
    :type undo: bool | None
    :param orientation: Axis Mode, Axis orientation
    :type orientation: bpy.stub_internal.rna_enums.TransformOrientationItems | None
    :param sign: Axis Sign, Side to select
    :type sign: typing.Literal['POS','NEG','ALIGN'] | None
    :param axis: Axis, Select the axis to compare each vertex on
    :type axis: bpy.stub_internal.rna_enums.AxisXyzItems | None
    :param threshold: Threshold
    :type threshold: float | None
    """

def select_by_attribute(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Select elements based on the active boolean attribute

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_by_pole_count(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    pole_count: int | None = 4,
    type: typing.Literal["LESS", "EQUAL", "GREATER", "NOTEQUAL"] | None = "NOTEQUAL",
    extend: bool | None = False,
    exclude_nonmanifold: bool | None = True,
) -> None:
    """Select vertices at poles by the number of connected edges. In edge and face mode the geometry connected to the vertices is selected

    :type execution_context: int | str | None
    :type undo: bool | None
    :param pole_count: Pole Count
    :type pole_count: int | None
    :param type: Type, Type of comparison to make
    :type type: typing.Literal['LESS','EQUAL','GREATER','NOTEQUAL'] | None
    :param extend: Extend, Extend the selection
    :type extend: bool | None
    :param exclude_nonmanifold: Exclude Non Manifold, Exclude non-manifold poles
    :type exclude_nonmanifold: bool | None
    """

def select_face_by_sides(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    number: int | None = 4,
    type: typing.Literal["LESS", "EQUAL", "GREATER", "NOTEQUAL"] | None = "EQUAL",
    extend: bool | None = True,
) -> None:
    """Select vertices or faces by the number of face sides

    :type execution_context: int | str | None
    :type undo: bool | None
    :param number: Number of Vertices
    :type number: int | None
    :param type: Type, Type of comparison to make
    :type type: typing.Literal['LESS','EQUAL','GREATER','NOTEQUAL'] | None
    :param extend: Extend, Extend the selection
    :type extend: bool | None
    """

def select_interior_faces(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Select faces where all edges have more than 2 face users

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_less(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_face_step: bool | None = True,
) -> None:
    """Deselect vertices, edges or faces at the boundary of each selection region

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_face_step: Face Step, Connected faces (instead of edges)
    :type use_face_step: bool | None
    """

def select_linked(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    delimit: set[bpy.stub_internal.rna_enums.MeshDelimitModeItems] | None = {"SEAM"},
) -> None:
    """Select all vertices connected to the current selection

    :type execution_context: int | str | None
    :type undo: bool | None
    :param delimit: Delimit, Delimit selected region
    :type delimit: set[bpy.stub_internal.rna_enums.MeshDelimitModeItems] | None
    """

def select_linked_pick(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    deselect: bool | None = False,
    delimit: set[bpy.stub_internal.rna_enums.MeshDelimitModeItems] | None = {"SEAM"},
    object_index: int | None = -1,
    index: int | None = -1,
) -> None:
    """(De)select all vertices linked to the edge under the mouse cursor

    :type execution_context: int | str | None
    :type undo: bool | None
    :param deselect: Deselect
    :type deselect: bool | None
    :param delimit: Delimit, Delimit selected region
    :type delimit: set[bpy.stub_internal.rna_enums.MeshDelimitModeItems] | None
    :type object_index: int | None
    :type index: int | None
    """

def select_loose(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
) -> None:
    """Select loose geometry based on the selection mode

    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend the selection
    :type extend: bool | None
    """

def select_mirror(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    axis: set[bpy.stub_internal.rna_enums.AxisFlagXyzItems] | None = {"X"},
    extend: bool | None = False,
) -> None:
    """Select mesh items at mirrored locations

    :type execution_context: int | str | None
    :type undo: bool | None
    :param axis: Axis
    :type axis: set[bpy.stub_internal.rna_enums.AxisFlagXyzItems] | None
    :param extend: Extend, Extend the existing selection
    :type extend: bool | None
    """

def select_mode(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_extend: bool | None = False,
    use_expand: bool | None = False,
    type: bpy.stub_internal.rna_enums.MeshSelectModeItems | None = "VERT",
    action: typing.Literal["DISABLE", "ENABLE", "TOGGLE"] | None = "TOGGLE",
) -> None:
    """Change selection mode

        :type execution_context: int | str | None
        :type undo: bool | None
        :param use_extend: Extend
        :type use_extend: bool | None
        :param use_expand: Expand
        :type use_expand: bool | None
        :param type: Type
        :type type: bpy.stub_internal.rna_enums.MeshSelectModeItems | None
        :param action: Action, Selection action to execute

    DISABLE
    Disable -- Disable selected markers.

    ENABLE
    Enable -- Enable selected markers.

    TOGGLE
    Toggle -- Toggle disabled flag for selected markers.
        :type action: typing.Literal['DISABLE','ENABLE','TOGGLE'] | None
    """

def select_more(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_face_step: bool | None = True,
) -> None:
    """Select more vertices, edges or faces connected to initial selection

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_face_step: Face Step, Connected faces (instead of edges)
    :type use_face_step: bool | None
    """

def select_next_item(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Select the next element (using selection order)

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_non_manifold(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = True,
    use_wire: bool | None = True,
    use_boundary: bool | None = True,
    use_multi_face: bool | None = True,
    use_non_contiguous: bool | None = True,
    use_verts: bool | None = True,
) -> None:
    """Select all non-manifold vertices or edges

    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend the selection
    :type extend: bool | None
    :param use_wire: Wire, Wire edges
    :type use_wire: bool | None
    :param use_boundary: Boundaries, Boundary edges
    :type use_boundary: bool | None
    :param use_multi_face: Multiple Faces, Edges shared by more than two faces
    :type use_multi_face: bool | None
    :param use_non_contiguous: Non Contiguous, Edges between faces pointing in alternate directions
    :type use_non_contiguous: bool | None
    :param use_verts: Vertices, Vertices connecting multiple face regions
    :type use_verts: bool | None
    """

def select_nth(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    skip: int | None = 1,
    nth: int | None = 1,
    offset: int | None = 0,
) -> None:
    """Deselect every Nth element starting from the active vertex, edge or face

    :type execution_context: int | str | None
    :type undo: bool | None
    :param skip: Deselected, Number of deselected elements in the repetitive sequence
    :type skip: int | None
    :param nth: Selected, Number of selected elements in the repetitive sequence
    :type nth: int | None
    :param offset: Offset, Offset from the starting point
    :type offset: int | None
    """

def select_prev_item(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Select the previous element (using selection order)

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_random(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    ratio: float | None = 0.5,
    seed: int | None = 0,
    action: typing.Literal["SELECT", "DESELECT"] | None = "SELECT",
) -> None:
    """Randomly select vertices

        :type execution_context: int | str | None
        :type undo: bool | None
        :param ratio: Ratio, Portion of items to select randomly
        :type ratio: float | None
        :param seed: Random Seed, Seed for the random number generator
        :type seed: int | None
        :param action: Action, Selection action to execute

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.
        :type action: typing.Literal['SELECT','DESELECT'] | None
    """

def select_similar(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "VERT_NORMAL",
        "VERT_FACES",
        "VERT_GROUPS",
        "VERT_EDGES",
        "VERT_CREASE",
        "EDGE_LENGTH",
        "EDGE_DIR",
        "EDGE_FACES",
        "EDGE_FACE_ANGLE",
        "EDGE_CREASE",
        "EDGE_BEVEL",
        "EDGE_SEAM",
        "EDGE_SHARP",
        "EDGE_FREESTYLE",
        "FACE_MATERIAL",
        "FACE_AREA",
        "FACE_SIDES",
        "FACE_PERIMETER",
        "FACE_NORMAL",
        "FACE_COPLANAR",
        "FACE_SMOOTH",
        "FACE_FREESTYLE",
    ]
    | None = "VERT_NORMAL",
    compare: typing.Literal["EQUAL", "GREATER", "LESS"] | None = "EQUAL",
    threshold: float | None = 0.0,
) -> None:
    """Select similar vertices, edges or faces by property types

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: typing.Literal['VERT_NORMAL','VERT_FACES','VERT_GROUPS','VERT_EDGES','VERT_CREASE','EDGE_LENGTH','EDGE_DIR','EDGE_FACES','EDGE_FACE_ANGLE','EDGE_CREASE','EDGE_BEVEL','EDGE_SEAM','EDGE_SHARP','EDGE_FREESTYLE','FACE_MATERIAL','FACE_AREA','FACE_SIDES','FACE_PERIMETER','FACE_NORMAL','FACE_COPLANAR','FACE_SMOOTH','FACE_FREESTYLE'] | None
    :param compare: Compare
    :type compare: typing.Literal['EQUAL','GREATER','LESS'] | None
    :param threshold: Threshold
    :type threshold: float | None
    """

def select_similar_region(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Select similar face regions to the current selection

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_ungrouped(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
) -> None:
    """Select vertices without a group

    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend the selection
    :type extend: bool | None
    """

def separate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["SELECTED", "MATERIAL", "LOOSE"] | None = "SELECTED",
) -> None:
    """Separate selected geometry into a new mesh

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: typing.Literal['SELECTED','MATERIAL','LOOSE'] | None
    """

def set_normals_from_faces(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    keep_sharp: bool | None = False,
) -> None:
    """Set the custom normals from the selected faces ones

    :type execution_context: int | str | None
    :type undo: bool | None
    :param keep_sharp: Keep Sharp Edges, Do not set sharp edges to face
    :type keep_sharp: bool | None
    """

def set_sharpness_by_angle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    angle: float | None = 0.523599,
    extend: bool | None = False,
) -> None:
    """Set edge sharpness based on the angle between neighboring faces

    :type execution_context: int | str | None
    :type undo: bool | None
    :param angle: Angle
    :type angle: float | None
    :param extend: Extend, Add new sharp edges without clearing existing sharp edges
    :type extend: bool | None
    """

def shape_propagate_to_all(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Apply selected vertex locations to all other shape keys

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def shortest_path_pick(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    edge_mode: typing.Literal["SELECT", "SEAM", "SHARP", "CREASE", "BEVEL", "FREESTYLE"]
    | None = "SELECT",
    use_face_step: bool | None = False,
    use_topology_distance: bool | None = False,
    use_fill: bool | None = False,
    skip: int | None = 0,
    nth: int | None = 1,
    offset: int | None = 0,
    index: int | None = -1,
) -> None:
    """Select shortest path between two selections

    :type execution_context: int | str | None
    :type undo: bool | None
    :param edge_mode: Edge Tag, The edge flag to tag when selecting the shortest path
    :type edge_mode: typing.Literal['SELECT','SEAM','SHARP','CREASE','BEVEL','FREESTYLE'] | None
    :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings)
    :type use_face_step: bool | None
    :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance
    :type use_topology_distance: bool | None
    :param use_fill: Fill Region, Select all paths between the source/destination elements
    :type use_fill: bool | None
    :param skip: Deselected, Number of deselected elements in the repetitive sequence
    :type skip: int | None
    :param nth: Selected, Number of selected elements in the repetitive sequence
    :type nth: int | None
    :param offset: Offset, Offset from the starting point
    :type offset: int | None
    :type index: int | None
    """

def shortest_path_select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    edge_mode: typing.Literal["SELECT", "SEAM", "SHARP", "CREASE", "BEVEL", "FREESTYLE"]
    | None = "SELECT",
    use_face_step: bool | None = False,
    use_topology_distance: bool | None = False,
    use_fill: bool | None = False,
    skip: int | None = 0,
    nth: int | None = 1,
    offset: int | None = 0,
) -> None:
    """Selected shortest path between two vertices/edges/faces

    :type execution_context: int | str | None
    :type undo: bool | None
    :param edge_mode: Edge Tag, The edge flag to tag when selecting the shortest path
    :type edge_mode: typing.Literal['SELECT','SEAM','SHARP','CREASE','BEVEL','FREESTYLE'] | None
    :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings)
    :type use_face_step: bool | None
    :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance
    :type use_topology_distance: bool | None
    :param use_fill: Fill Region, Select all paths between the source/destination elements
    :type use_fill: bool | None
    :param skip: Deselected, Number of deselected elements in the repetitive sequence
    :type skip: int | None
    :param nth: Selected, Number of selected elements in the repetitive sequence
    :type nth: int | None
    :param offset: Offset, Offset from the starting point
    :type offset: int | None
    """

def smooth_normals(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 0.5,
) -> None:
    """Smooth custom normals based on adjacent vertex normals

    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Factor, Specifies weight of smooth vs original normal
    :type factor: float | None
    """

def solidify(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    thickness: float | None = 0.01,
) -> None:
    """Create a solid skin by extruding, compensating for sharp angles

    :type execution_context: int | str | None
    :type undo: bool | None
    :param thickness: Thickness
    :type thickness: float | None
    """

def sort_elements(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "VIEW_ZAXIS",
        "VIEW_XAXIS",
        "CURSOR_DISTANCE",
        "MATERIAL",
        "SELECTED",
        "RANDOMIZE",
        "REVERSE",
    ]
    | None = "VIEW_ZAXIS",
    elements: set[typing.Literal["VERT", "EDGE", "FACE"]] | None = {"VERT"},
    reverse: bool | None = False,
    seed: int | None = 0,
) -> None:
    """The order of selected vertices/edges/faces is modified, based on a given method

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type, Type of reordering operation to apply

    VIEW_ZAXIS
    View Z Axis -- Sort selected elements from farthest to nearest one in current view.

    VIEW_XAXIS
    View X Axis -- Sort selected elements from left to right one in current view.

    CURSOR_DISTANCE
    Cursor Distance -- Sort selected elements from nearest to farthest from 3D cursor.

    MATERIAL
    Material -- Sort selected faces from smallest to greatest material index.

    SELECTED
    Selected -- Move all selected elements in first places, preserving their relative order.
    Warning: This will affect unselected elements' indices as well.

    RANDOMIZE
    Randomize -- Randomize order of selected elements.

    REVERSE
    Reverse -- Reverse current order of selected elements.
        :type type: typing.Literal['VIEW_ZAXIS','VIEW_XAXIS','CURSOR_DISTANCE','MATERIAL','SELECTED','RANDOMIZE','REVERSE'] | None
        :param elements: Elements, Which elements to affect (vertices, edges and/or faces)
        :type elements: set[typing.Literal['VERT','EDGE','FACE']] | None
        :param reverse: Reverse, Reverse the sorting effect
        :type reverse: bool | None
        :param seed: Seed, Seed for random-based operations
        :type seed: int | None
    """

def spin(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    steps: int | None = 12,
    dupli: bool | None = False,
    angle: float | None = 1.5708,
    use_auto_merge: bool | None = True,
    use_normal_flip: bool | None = False,
    center: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
    axis: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
) -> None:
    """Extrude selected vertices in a circle around the cursor in indicated viewport

    :type execution_context: int | str | None
    :type undo: bool | None
    :param steps: Steps, Steps
    :type steps: int | None
    :param dupli: Use Duplicates
    :type dupli: bool | None
    :param angle: Angle, Rotation for each step
    :type angle: float | None
    :param use_auto_merge: Auto Merge, Merge first/last when the angle is a full revolution
    :type use_auto_merge: bool | None
    :param use_normal_flip: Flip Normals
    :type use_normal_flip: bool | None
    :param center: Center, Center in global view space
    :type center: collections.abc.Sequence[float] | mathutils.Vector | None
    :param axis: Axis, Axis in global view space
    :type axis: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def split(execution_context: int | str | None = None, undo: bool | None = None) -> None:
    """Split off selected geometry from connected unselected geometry

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def split_normals(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Split custom normals of selected vertices

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def subdivide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    number_cuts: int | None = 1,
    smoothness: float | None = 0.0,
    ngon: bool | None = True,
    quadcorner: typing.Literal["INNERVERT", "PATH", "STRAIGHT_CUT", "FAN"]
    | None = "STRAIGHT_CUT",
    fractal: float | None = 0.0,
    fractal_along_normal: float | None = 0.0,
    seed: int | None = 0,
) -> None:
    """Subdivide selected edges

    :type execution_context: int | str | None
    :type undo: bool | None
    :param number_cuts: Number of Cuts
    :type number_cuts: int | None
    :param smoothness: Smoothness, Smoothness factor
    :type smoothness: float | None
    :param ngon: Create N-Gons, When disabled, newly created faces are limited to 3 and 4 sided faces
    :type ngon: bool | None
    :param quadcorner: Quad Corner Type, How to subdivide quad corners (anything other than Straight Cut will prevent n-gons)
    :type quadcorner: typing.Literal['INNERVERT','PATH','STRAIGHT_CUT','FAN'] | None
    :param fractal: Fractal, Fractal randomness factor
    :type fractal: float | None
    :param fractal_along_normal: Along Normal, Apply fractal displacement along normal only
    :type fractal_along_normal: float | None
    :param seed: Random Seed, Seed for the random number generator
    :type seed: int | None
    """

def subdivide_edgering(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    number_cuts: int | None = 10,
    interpolation: typing.Literal["LINEAR", "PATH", "SURFACE"] | None = "PATH",
    smoothness: float | None = 1.0,
    profile_shape_factor: float | None = 0.0,
    profile_shape: bpy.stub_internal.rna_enums.ProportionalFalloffCurveOnlyItems
    | None = "SMOOTH",
) -> None:
    """Subdivide perpendicular edges to the selected edge-ring

    :type execution_context: int | str | None
    :type undo: bool | None
    :param number_cuts: Number of Cuts
    :type number_cuts: int | None
    :param interpolation: Interpolation, Interpolation method
    :type interpolation: typing.Literal['LINEAR','PATH','SURFACE'] | None
    :param smoothness: Smoothness, Smoothness factor
    :type smoothness: float | None
    :param profile_shape_factor: Profile Factor, How much intermediary new edges are shrunk/expanded
    :type profile_shape_factor: float | None
    :param profile_shape: Profile Shape, Shape of the profile
    :type profile_shape: bpy.stub_internal.rna_enums.ProportionalFalloffCurveOnlyItems | None
    """

def symmetrize(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: bpy.stub_internal.rna_enums.SymmetrizeDirectionItems
    | None = "NEGATIVE_X",
    threshold: float | None = 0.0001,
) -> None:
    """Enforce symmetry (both form and topological) across an axis

    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Which sides to copy from and to
    :type direction: bpy.stub_internal.rna_enums.SymmetrizeDirectionItems | None
    :param threshold: Threshold, Limit for snap middle vertices to the axis center
    :type threshold: float | None
    """

def symmetry_snap(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: bpy.stub_internal.rna_enums.SymmetrizeDirectionItems
    | None = "NEGATIVE_X",
    threshold: float | None = 0.05,
    factor: float | None = 0.5,
    use_center: bool | None = True,
) -> None:
    """Snap vertex pairs to their mirrored locations

    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Which sides to copy from and to
    :type direction: bpy.stub_internal.rna_enums.SymmetrizeDirectionItems | None
    :param threshold: Threshold, Distance within which matching vertices are searched
    :type threshold: float | None
    :param factor: Factor, Mix factor of the locations of the vertices
    :type factor: float | None
    :param use_center: Center, Snap middle vertices to the axis center
    :type use_center: bool | None
    """

def tris_convert_to_quads(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    face_threshold: float | None = 0.698132,
    shape_threshold: float | None = 0.698132,
    topology_influence: float | None = 0.0,
    uvs: bool | None = False,
    vcols: bool | None = False,
    seam: bool | None = False,
    sharp: bool | None = False,
    materials: bool | None = False,
    deselect_joined: bool | None = False,
) -> None:
    """Merge triangles into four sided polygons where possible

    :type execution_context: int | str | None
    :type undo: bool | None
    :param face_threshold: Max Face Angle, Face angle limit
    :type face_threshold: float | None
    :param shape_threshold: Max Shape Angle, Shape angle limit
    :type shape_threshold: float | None
    :param topology_influence: Topology Influence, How much to prioritize regular grids of quads as well as quads that touch existing quads
    :type topology_influence: float | None
    :param uvs: Compare UVs
    :type uvs: bool | None
    :param vcols: Compare Color Attributes
    :type vcols: bool | None
    :param seam: Compare Seam
    :type seam: bool | None
    :param sharp: Compare Sharp
    :type sharp: bool | None
    :param materials: Compare Materials
    :type materials: bool | None
    :param deselect_joined: Deselect Joined, Only select remaining triangles that were not merged
    :type deselect_joined: bool | None
    """

def unsubdivide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    iterations: int | None = 2,
) -> None:
    """Un-subdivide selected edges and faces

    :type execution_context: int | str | None
    :type undo: bool | None
    :param iterations: Iterations, Number of times to un-subdivide
    :type iterations: int | None
    """

def uv_texture_add(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Add UV map

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def uv_texture_remove(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Remove UV map

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def uvs_reverse(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Flip direction of UV coordinates inside faces

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def uvs_rotate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_ccw: bool | None = False,
) -> None:
    """Rotate UV coordinates inside faces

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_ccw: Counter Clockwise
    :type use_ccw: bool | None
    """

def vert_connect(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Connect selected vertices of faces, splitting the face

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def vert_connect_concave(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Make all faces convex

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def vert_connect_nonplanar(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    angle_limit: float | None = 0.0872665,
) -> None:
    """Split non-planar faces that exceed the angle threshold

    :type execution_context: int | str | None
    :type undo: bool | None
    :param angle_limit: Max Angle, Angle limit
    :type angle_limit: float | None
    """

def vert_connect_path(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Connect vertices by their selection order, creating edges, splitting faces

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def vertices_smooth(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 0.0,
    repeat: int | None = 1,
    xaxis: bool | None = True,
    yaxis: bool | None = True,
    zaxis: bool | None = True,
    wait_for_input: bool | None = True,
) -> None:
    """Flatten angles of selected vertices

    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Smoothing, Smoothing factor
    :type factor: float | None
    :param repeat: Repeat, Number of times to smooth the mesh
    :type repeat: int | None
    :param xaxis: X-Axis, Smooth along the X axis
    :type xaxis: bool | None
    :param yaxis: Y-Axis, Smooth along the Y axis
    :type yaxis: bool | None
    :param zaxis: Z-Axis, Smooth along the Z axis
    :type zaxis: bool | None
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool | None
    """

def vertices_smooth_laplacian(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    repeat: int | None = 1,
    lambda_factor: float | None = 1.0,
    lambda_border: float | None = 5e-05,
    use_x: bool | None = True,
    use_y: bool | None = True,
    use_z: bool | None = True,
    preserve_volume: bool | None = True,
) -> None:
    """Laplacian smooth of selected vertices

    :type execution_context: int | str | None
    :type undo: bool | None
    :param repeat: Number of iterations to smooth the mesh
    :type repeat: int | None
    :param lambda_factor: Lambda factor
    :type lambda_factor: float | None
    :param lambda_border: Lambda factor in border
    :type lambda_border: float | None
    :param use_x: Smooth X Axis, Smooth object along X axis
    :type use_x: bool | None
    :param use_y: Smooth Y Axis, Smooth object along Y axis
    :type use_y: bool | None
    :param use_z: Smooth Z Axis, Smooth object along Z axis
    :type use_z: bool | None
    :param preserve_volume: Preserve Volume, Apply volume preservation after smooth
    :type preserve_volume: bool | None
    """

def wireframe(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_boundary: bool | None = True,
    use_even_offset: bool | None = True,
    use_relative_offset: bool | None = False,
    use_replace: bool | None = True,
    thickness: float | None = 0.01,
    offset: float | None = 0.01,
    use_crease: bool | None = False,
    crease_weight: float | None = 0.01,
) -> None:
    """Create a solid wireframe from faces

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_boundary: Boundary, Inset face boundaries
    :type use_boundary: bool | None
    :param use_even_offset: Offset Even, Scale the offset to give more even thickness
    :type use_even_offset: bool | None
    :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry
    :type use_relative_offset: bool | None
    :param use_replace: Replace, Remove original faces
    :type use_replace: bool | None
    :param thickness: Thickness
    :type thickness: float | None
    :param offset: Offset
    :type offset: float | None
    :param use_crease: Crease, Crease hub edges for an improved subdivision surface
    :type use_crease: bool | None
    :param crease_weight: Crease Weight
    :type crease_weight: float | None
    """
