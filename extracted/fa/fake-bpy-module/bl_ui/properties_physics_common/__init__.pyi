import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types

class PHYSICS_PT_add(PhysicButtonsPanel, bpy.types.Panel):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def draw(self, context) -> None:
        """

        :param context:
        """

class PhysicButtonsPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

def basic_force_field_falloff_ui(self_, field) -> None: ...
def basic_force_field_settings_ui(self_, field) -> None: ...
def effector_weights_ui(self_, weights, weight_type) -> None: ...
def physics_add(layout, md, name, type, typeicon, toggles) -> None: ...
def physics_add_special(layout, data, name, addop, removeop, typeicon) -> None: ...
def point_cache_ui(self_, cache, enabled, cachetype) -> None: ...
