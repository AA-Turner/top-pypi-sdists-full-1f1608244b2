from __future__ import annotations

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import DEFAULT_MODEL, SymbolicConstant
from .Leaf import Leaf


@abaqus_class_doc
class LeafFromNodeSets(Leaf):
    """The LeafFromNodeSets object can be used whenever a Leaf object is expected as an argument. Leaf objects
    are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which
    are then used as arguments to DisplayGroup commands. The LeafFromNodeSets object is derived from the Leaf
    object.

    .. note::
        This object can be accessed by::

            import displayGroupOdbToolset
    """

    #: A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
    #: DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.
    leafType: SymbolicConstant

    #: A sequence of Strings specifying node sets or a String specifying a single node set.
    nodeSets: tuple[str, ...] = ()

    @abaqus_method_doc
    def __init__(self, nodeSets: tuple):
        """This method creates a Leaf object from a sequence of node sets.

        .. note::
            This function can be accessed by::

                LeafFromNodeSets

        Parameters
        ----------
        nodeSets
            A sequence of Strings specifying node sets or a String specifying a single node set.

        Returns
        -------
        LeafFromNodeSets
            A LeafFromNodeSets object.
        """
        super().__init__(DEFAULT_MODEL)
