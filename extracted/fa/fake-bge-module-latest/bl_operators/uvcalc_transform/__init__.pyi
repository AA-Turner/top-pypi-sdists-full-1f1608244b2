import typing
import collections.abc
import typing_extensions
import bpy.types

class AlignUVRotation(bpy.types.Operator):
    """Align the UV island's rotation"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def draw(self, _context):
        """

        :param _context:
        """

    def execute(self, context):
        """

        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class RandomizeUVTransform(bpy.types.Operator):
    """Randomize the UV island's location, rotation, and scale"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def execute(self, context):
        """

        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

def align_uv_rotation(context, method, axis, correct_aspect): ...
def align_uv_rotation_bmesh(bm, method, axis, aspect_y): ...
def align_uv_rotation_island(bm, uv_layer, faces, method, axis, aspect_y): ...
def find_rotation_auto(bm, uv_layer, faces, aspect_y): ...
def find_rotation_edge(bm, uv_layer, faces, aspect_y): ...
def find_rotation_geometry(bm, uv_layer, faces, method, axis, aspect_y): ...
def get_aspect_y(context): ...
def get_random_transform(transform_params, entropy): ...
def is_face_uv_selected(face, uv_layer, any_edge): ...
def is_island_uv_selected(island, uv_layer, any_edge): ...
def island_uv_bounds(island, uv_layer): ...
def island_uv_bounds_center(island, uv_layer): ...
def randomize_uv_transform(context, transform_params): ...
def randomize_uv_transform_bmesh(mesh, bm, transform_params): ...
def randomize_uv_transform_island(bm, uv_layer, faces, transform_params): ...
