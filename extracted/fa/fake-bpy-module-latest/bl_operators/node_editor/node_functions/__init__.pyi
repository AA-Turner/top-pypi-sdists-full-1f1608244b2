import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class NodeEditorBase:
    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

def force_update(context) -> None: ...
def get_group_output_node(tree, output_node_idname="NodeGroupOutput") -> None: ...
def get_internal_socket(socket) -> None: ...
def get_output_location(tree) -> None: ...
def is_viewer_link(link, output_node) -> None: ...
def is_visible_socket(socket) -> None: ...
def node_editor_poll(cls, context) -> None: ...
def node_space_type_poll(cls, context, types) -> None: ...
