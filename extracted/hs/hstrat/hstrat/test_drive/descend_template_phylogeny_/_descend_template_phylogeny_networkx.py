import typing

from astropy.utils.decorators import deprecated_renamed_argument
from iterpop import iterpop as ip
import networkx as nx
import opytional as opyt

from ..._auxiliary_lib import HereditaryStratigraphicInstrument, unpairwise
from ._descend_template_phylogeny import descend_template_phylogeny


@deprecated_renamed_argument("seed_column", "seed_instrument", since="1.20.0")
def descend_template_phylogeny_networkx(
    tree: nx.DiGraph,
    seed_instrument: HereditaryStratigraphicInstrument,
    extant_nodes: typing.Optional[typing.Iterable[typing.Any]] = None,
    progress_wrap: typing.Callable = lambda x: x,
) -> typing.List[HereditaryStratigraphicInstrument]:
    """Generate a population of hereditary stratigraphic instruments that could
    have resulted from the template phylogeny.

    Parameters
    ----------
    tree : nx.DiGraph
        Phylogeny record as a networkx DiGraph.

        Assumes directed edges point from ancestor to descendant. Does not
        support non-unit edge length.
    seed_instrument : HereditaryStratigraphicInstrument
        Hereditary stratigraphic instrument to seed at root node of phylogeny.

        Returned hereditary stratigraphic instrument population will be
        generated as if repeatedly calling `CloneDescendant()` on
        `seed_instrument`. As such, specifies configuration (i.e., differentia
        bit width and stratum retention policy) for returned instruments. May
        already have strata deposited, which will be incorporated into generated
        extant population.
    extant_nodes : optional list of networkx nodes
        Which organisms should hereditary stratigraphic instruments be created
        for?

        Designates content and order of returned list of hereditary
        stratigraphic instrument.

        If None, hereditary stratigraphic instruments will be created for all
        phylogenetic leaves (organisms without offspring) in order of
        appearance in `tree.nodes`.
    progress_wrap : Callable, optional
        Wrapper applied around generation iterator and row generator for final
        phylogeny compilation process.

        Pass tqdm or equivalent to display progress bars.

    Returns
    -------
    list of HereditaryStratigraphicInstrument
        Population of hereditary stratigraphic instruments for extant lineage
        members (i.e., phylogeny leaf nodes).

        Instruments ordered in order of appearance of corresponding extant
        organism id.
    """

    # handle empty case
    if len(tree) == 0:
        return []

    reversed_tree = tree.reverse(copy=False)
    root_node = ip.popsingleton(
        node for node in tree.nodes if tree.in_degree(node) == 0
    )
    leaf_nodes = [node for node in tree.nodes if tree.out_degree(node) == 0]

    return descend_template_phylogeny(
        ascending_lineage_iterables=(
            unpairwise(nx.dfs_edges(reversed_tree, extant_node))
            if len(tree) > 1
            else (extant_node,)
            for extant_node in opyt.or_value(extant_nodes, leaf_nodes)
        ),
        descending_tree_iterable=(
            unpairwise(nx.dfs_edges(tree, root_node))
            if len(tree) > 1
            else (root_node,)
        ),
        get_parent=lambda node: ip.poursingleton(reversed_tree[node]),
        get_stem_length=lambda node: 1,
        seed_instrument=seed_instrument,
        demark=lambda x: x,
        progress_wrap=progress_wrap,
    )
