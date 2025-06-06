import warnings
from copy import deepcopy
from typing import Union, List, Tuple, Dict
from abc import ABC, abstractmethod

import numpy as np
import pandas as pd

from aequilibrae.matrix import AequilibraeMatrix
from aequilibrae.paths.graph import Graph, TransitGraph, GraphBase
from aequilibrae.paths.results import AssignmentResults, TransitAssignmentResults


class TransportClassBase(ABC):  # noqa: B024
    def __init__(self, name: str, graph: GraphBase, matrix: AequilibraeMatrix) -> None:
        """
        Instantiates the class

        :Arguments:
            **name** (:obj:`str`): UNIQUE class name.

            **graph** (:obj:`Graph`): Class/mode-specific graph

            **matrix** (:obj:`AequilibraeMatrix`): Class/mode-specific matrix. Supports multiple user classes
        """
        if not np.array_equal(matrix.index, graph.centroids):
            raise ValueError("Matrix and graph do not have compatible sets of centroids.")

        if matrix.matrix_view.dtype != graph.default_types("float"):
            raise TypeError("Matrix's computational view need to be of type np.float64")
        self._config = {}
        self.graph = graph
        self.logger = graph.logger
        self.matrix = matrix
        self._id = name

        graph_config = {
            "Mode": graph.mode,
            "Block through centroids": graph.block_centroid_flows,
            "Number of centroids": graph.num_zones,
            "Links": graph.num_links,
            "Nodes": graph.num_nodes,
        }
        self._config["Graph"] = str(graph_config)

        mat_config = {
            "Source": matrix.file_path or "",
            "Number of centroids": matrix.zones,
            "Matrix cores": matrix.view_names,
        }
        if len(matrix.view_names) == 1:
            mat_config["Matrix totals"] = {
                nm: np.sum(np.nan_to_num(matrix.matrix_view)[:, :]) for nm in matrix.view_names
            }
        else:
            mat_config["Matrix totals"] = {
                nm: np.sum(np.nan_to_num(matrix.matrix_view)[:, :, i]) for i, nm in enumerate(matrix.view_names)
            }
        self._config["Matrix"] = str(mat_config)

    @property
    def info(self) -> dict:
        config = deepcopy(self._config)
        return {self._id: config}


class TrafficClass(TransportClassBase):
    """Traffic class for equilibrium traffic assignment

    .. code-block:: python

        >>> from aequilibrae.paths import TrafficClass

        >>> project = create_example(project_path)
        >>> project.network.build_graphs()

        >>> graph = project.network.graphs['c'] # we grab the graph for cars
        >>> graph.set_graph('free_flow_time') # let's say we want to minimize time
        >>> graph.set_skimming(['free_flow_time', 'distance']) # And will skim time and distance
        >>> graph.set_blocked_centroid_flows(True)

        >>> proj_matrices = project.matrices

        >>> demand = proj_matrices.get_matrix("demand_omx")
        >>> demand.computational_view(['matrix'])

        >>> tc = TrafficClass("car", graph, demand)
        >>> tc.set_pce(1.3)
    """

    def __init__(self, name: str, graph: Graph, matrix: AequilibraeMatrix) -> None:
        """
        Instantiates the class

        :Arguments:
            **name** (:obj:`str`): UNIQUE class name.

            **graph** (:obj:`Graph`): Class/mode-specific graph

            **matrix** (:obj:`AequilibraeMatrix`): Class/mode-specific matrix. Supports multiple user classes
        """
        super().__init__(name, graph, matrix)
        self.pce = 1.0
        self.vot = 1.0
        self.mode = graph.mode
        self.class_flow: np.array  # FIXME: Is this ever access?
        self.fixed_cost = np.zeros(graph.graph.shape[0], graph.default_types("float"))
        self.fixed_cost_field = ""
        self.fc_multiplier = 1.0
        self.results = AssignmentResults()
        self._aon_results = AssignmentResults()
        self._selected_links = {}  # maps human name to link_set
        self.congested_time = np.array([])

    def set_pce(self, pce: Union[float, int]) -> None:
        """Sets Passenger Car equivalent

        :Arguments:
            **pce** (:obj:`Union[float, int]`): PCE. Defaults to 1 if not set
        """
        if not isinstance(pce, (float, int)):
            raise ValueError("PCE needs to be either integer or float ")
        self.pce = pce

    def set_fixed_cost(self, field_name: str, multiplier=1):
        """Sets value of time

        :Arguments:
             **field_name** (:obj:`str`): Name of the graph field with fixed costs for this class

             **multiplier** (:obj:`Union[float, int]`): Multiplier for the fixed cost. Defaults to 1 if not set
        """
        if field_name not in self.graph.graph.columns:
            raise ValueError("Field does not exist in the graph")

        self.fc_multiplier = float(multiplier)
        self.fixed_cost_field = field_name
        if np.any(np.isnan(self.graph.graph[field_name].values)):
            self.logger.warning(f"Cost field {field_name} has NaN values. Converted to zero")

        if self.graph.graph[field_name].min() < 0:
            msg = f"Cost field {field_name} has negative values. That is not allowed"
            self.logger.error(msg)
            raise ValueError(msg)

    def set_vot(self, value_of_time: float) -> None:
        """Sets value of time

        :Arguments:
            **value_of_time** (:obj:`Union[float, int]`): Value of time. Defaults to 1 if not set
        """

        self.vot = float(value_of_time)

    def set_select_links(self, links: Dict[str, List[Tuple[int, int]]]):
        """Set the selected links. Checks if the links and directions are valid. Translates link_id and
        direction into unique link id used in compact graph.
        Supply links=None to disable select link analysis.

        :Arguments:
            **links** (:obj:`Union[None, Dict[str, List[Tuple[int, int]]]]`): name of link set and
            Link IDs and directions to be used in select link analysis"""
        self._selected_links = {}
        for name, link_set in links.items():
            if len(name.split(" ")) != 1:
                warnings.warn("Input string name has a space in it. Replacing with _")
                name = str.join("_", name.split(" "))

            link_ids = []
            for link, dir in link_set:
                if dir == 0:
                    query = (self.graph.graph["link_id"] == link) & (
                        (self.graph.graph["direction"] == -1) | (self.graph.graph["direction"] == 1)
                    )
                else:
                    query = (self.graph.graph["link_id"] == link) & (self.graph.graph["direction"] == dir)
                if not query.any():
                    raise ValueError(f"link_id or direction {(link, dir)} is not present within graph.")
                    # Check for duplicate compressed link ids in the current link set
                for comp_id in self.graph.graph[query]["__compressed_id__"].values:
                    if comp_id in link_ids:
                        warnings.warn(
                            "Two input links map to the same compressed link in the network"
                            f", removing superfluous link {link} and direction {dir} with compressed id {comp_id}"
                        )
                    else:
                        link_ids.append(comp_id)
            self._selected_links[name] = np.array(link_ids, dtype=self.graph.default_types("int"))
        self._config["select_links"] = str(links)

    def skim_congested(self, skim_fields=None):
        """
        Skims the congested network. The user can add a list of skims to be computed, which
        will be added to the congested time and the assignment cost from the last iteration of
        the assignment.

        :Arguments:
            **skim_fields** (:obj:`Union[None, str]`): Name of the skims to use. If None, uses default only
        """
        self.graph.graph = self.graph.graph.assign(
            __assignment_cost__=self.graph.cost, __congested_time__=self.congested_time
        )
        skims = (skim_fields or []) + ["__assignment_cost__", "__congested_time__"]
        pre_fields = self.graph.skim_fields
        self.graph.set_skimming(skims)
        skimmer = self.graph.compute_skims()
        self.graph.set_skimming(pre_fields)
        return skimmer

    def __setattr__(self, key, value):
        if key not in [
            "graph",
            "logger",
            "matrix",
            "pce",
            "mode",
            "class_flow",
            "results",
            "_aon_results",
            "_id",
            "vot",
            "fixed_cost",
            "fc_multiplier",
            "fixed_cost_field",
            "_selected_links",
            "_config",
            "congested_time",
        ]:
            raise KeyError(f"Traffic Class does not have '{key}'")
        self.__dict__[key] = value


class TransitClass(TransportClassBase):
    def __init__(self, name: str, graph: TransitGraph, matrix: AequilibraeMatrix):
        super().__init__(name, graph, matrix)
        self._config["Graph"] = str(graph._config)
        self.results = TransitAssignmentResults()

        if len(matrix.view_names) == 1:
            self.matrix_core = matrix.view_names[0]
        else:
            self.matrix_core = None

    def set_demand_matrix_core(self, core: str):
        """
        Set the matrix core to use for demand.

        :Arguments:
            **core** (:obj:`str`):"""
        if core not in self.matrix.view_names:
            raise KeyError(f"'{core}' is not present in `matrix.view_names`")
        self.matrix_core = core
