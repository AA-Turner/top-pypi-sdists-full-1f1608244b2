"""
Functions for fetching and converting graphs and network structures.
"""

# workaround until networkx adopts types
# pyright: basic
from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, cast

import fiona
import geopandas as gpd
import networkx as nx
import numpy as np
import osmnx as ox
import pandas as pd
import requests
from osmnx._errors import InsufficientResponseError  # type: ignore
from pyproj import CRS, Transformer
from shapely import geometry
from shapely.strtree import STRtree
from tqdm import tqdm

from .. import config, rustalgos
from ..tools import graphs, util
from ..tools.util import EdgeData, ListCoordsType, NodeData, NodeKey

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


SPEED_M_S = config.SPEED_M_S


def nx_epsg_conversion(
    nx_multigraph: nx.MultiGraph, to_crs_code: int | str, from_crs_code: None = None
) -> nx.MultiGraph:
    """
    Convert a graph from the `from_crs_code` EPSG CRS to the `to_crs_code` EPSG CRS.

    The `to_crs_code` must be for a projected CRS. If edge `geom` attributes are found, the associated `LineString`
    geometries will also be converted.

    Parameters
    ----------
    nx_multigraph: nx.MultiGraph
        A `networkX` `MultiGraph` with `x` and `y` node attributes in the `from_crs_code` coordinate system. Optional
        `geom` edge attributes containing `LineString` geoms to be converted.
    to_crs_code: int | str
        A `pyproj` compatible `str` or `int` representing a valid CRS into which the graph must be projected. For
        example, [27700](https://epsg.io/27700) if converting to British National Grid.
    from_crs_code: None
        The `from_crs_code` parameter is deprecated and will be removed in a future release. If your network is
        generated via cityseer from OSM or GeoPandas then CRS handling is automatic. Otherwise, the CRS can be set
        directly in the graph if necessary at G.graph["crs"]; for example: G.graph["crs"] = 4326

    Returns
    -------
    nx.MultiGraph
        A `networkX` `MultiGraph` with `x` and `y` node attributes converted to the specified `to_crs_code` coordinate
        system. Edge `geom` attributes will also be converted if found.

    """
    if from_crs_code is not None:
        logger.warning(
            """
            The `from_crs_code` parameter is deprecated and will be removed in a future release. If your network is
            generated via cityseer from OSM or GeoPandas then CRS handling is automatic. Otherwise, the CRS can be set
            directly in the graph if necessary at G.graph["crs"]; for example: G.graph["crs"] = 4326
            """
        )
    logger.info(f"Converting networkX graph to CRS code {to_crs_code}.")
    g_multi_copy = util.validate_cityseer_networkx_graph(nx_multigraph)
    transformer = Transformer.from_crs(g_multi_copy.graph["crs"], to_crs_code, always_xy=True)
    logger.info("Processing node x, y coordinates.")
    nd_key: NodeKey
    node_data: NodeData
    for nd_key, node_data in tqdm(g_multi_copy.nodes(data=True), disable=config.QUIET_MODE):
        # be cognisant of parameter and return order, using always_xy for transformer
        easting, northing = transformer.transform(node_data["x"], node_data["y"])
        # write back to graph
        g_multi_copy.nodes[nd_key]["x"] = easting
        g_multi_copy.nodes[nd_key]["y"] = northing
    # if line geom property provided, then convert as well
    logger.info("Processing edge geom coordinates, if present.")
    start_nd_key: NodeKey
    end_nd_key: NodeKey
    edge_idx: int
    edge_data: EdgeData
    for start_nd_key, end_nd_key, edge_idx, edge_data in tqdm(  # type: ignore
        g_multi_copy.edges(data=True, keys=True),  # type: ignore
        disable=config.QUIET_MODE,  # type: ignore
    ):
        # check if geom present - optional step
        if "geom" in edge_data:
            line_geom: geometry.LineString = edge_data["geom"]
            # convert
            edge_coords: ListCoordsType = [transformer.transform(x, y) for x, y in line_geom.coords]
            # snap ends
            edge_coords = util.snap_linestring_endpoints(g_multi_copy, start_nd_key, end_nd_key, edge_coords)
            # write back to edge
            g_multi_copy[start_nd_key][end_nd_key][edge_idx]["geom"] = geometry.LineString(edge_coords)  # type: ignore

    # update CRS to new CRS
    g_multi_copy.graph["crs"] = CRS(to_crs_code)

    return g_multi_copy


def nx_wgs_to_utm(nx_multigraph: nx.MultiGraph) -> nx.MultiGraph:
    """
    Convert a graph from WGS84 geographic coordinates to UTM projected coordinates.

    Converts `x` and `y` node attributes from [WGS84](https://epsg.io/4326) `lng`, `lat` geographic coordinates to the
    local UTM projected coordinate system. If edge `geom` attributes are found, the associated `LineString` geometries
    will also be converted. The UTM zone derived from the first processed node will be used for the conversion of all
    other nodes and geometries contained in the graph. This ensures consistent behaviour in cases where a graph spans
    a UTM boundary.

    Parameters
    ----------
    nx_multigraph: nx.MultiGraph
        A `networkX` `MultiGraph` with `x` and `y` node attributes in the WGS84 coordinate system. Optional `geom` edge
        attributes containing `LineString` geoms to be converted.

    Returns
    -------
    nx.MultiGraph
        A `networkX` `MultiGraph` with `x` and `y` node attributes converted to the local UTM coordinate system. If edge
         `geom` attributes are present, these will also be converted.

    """
    # sample the first node for UTM
    nd_key = list(nx_multigraph.nodes())[0]
    to_crs_code = util.extract_utm_epsg_code(nx_multigraph.nodes[nd_key]["x"], nx_multigraph.nodes[nd_key]["y"])
    return nx_epsg_conversion(nx_multigraph, to_crs_code)


def buffered_point_poly(lng: float, lat: float, buffer: int, projected: bool = False) -> tuple[geometry.Polygon, int]:
    """
    Buffer a point and return a `shapely` Polygon.

    This function can be used to prepare a buffered point `Polygon` for passing to
    [`osm_graph_from_poly()`](#osm-graph-from-poly). Expects WGS 84 / EPSG 4326 input coordinates. If `projected` is
    `True` then a UTM converted polygon will be returned. Otherwise returned as WGS 84 polygon in geographic coords.

    Parameters
    ----------
    lng: float
        The longitudinal WGS coordinate in degrees.
    lat: float
        The latitudinal WGS coordinate in degrees.
    buffer: int
        The buffer distance in metres.
    projected: bool
        Whether to project the returned polygon to a local UTM projected coordinate reference system.

    Returns
    -------
    geometry.Polygon
        A `shapely` `Polygon` in WGS coordinates.
    int
        The UTM EPSG code.

    """
    utm_epsg_code = util.extract_utm_epsg_code(lng, lat)
    point_utm = util.project_geom(geometry.Point(lng, lat), 4326, utm_epsg_code)
    poly_utm: geometry.Polygon = point_utm.buffer(buffer)
    if projected:
        return poly_utm, utm_epsg_code
    return util.project_geom(poly_utm, utm_epsg_code, 4326), 4326


def fetch_osm_network(osm_request: str, timeout: int = 300, max_tries: int = 3) -> requests.Response | None:
    """
    Fetches an OSM response.

    :::note
    This function requires a valid OSM request. If you prepare a polygonal extents then it may be easier to use
    [`osm_graph_from_poly()`](#osm-graph-from-poly), which would call this method on your behalf and then
    builds a graph automatically.
    :::

    Parameters
    ----------
    osm_request: str
        A valid OSM request as a string. Use
        [OSM Overpass](https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL) for testing custom queries.
    timeout: int
        Timeout duration for API call in seconds.
    max_tries: int
        The number of attempts to fetch a response before raising.

    Returns
    -------
    requests.Response
        An OSM API response.

    """
    osm_response: requests.Response | None = None
    while max_tries:
        osm_response = requests.get(
            "https://overpass-api.de/api/interpreter",
            timeout=timeout,
            params={"data": osm_request},
        )
        # break if OK response
        if osm_response is not None and osm_response.status_code == 200:  # type: ignore
            break
        # otherwise try until max_tries is exhausted
        logger.warning("Unsuccessful OSM API request response, trying again...")
        max_tries -= 1
    if osm_response is None:
        raise requests.RequestException("None response. Unsuccessful OSM API request.")
    if osm_response.status_code != 200:
        osm_response.raise_for_status()

    return osm_response


def _extract_gdf(gdf):
    # extract ways and convert to polys
    # not interested in segments - which are captured separately from network query
    # but do want squares etc. described as ways - hence buffer and reverse buffer
    if "element" in gdf.index.names and "way" in gdf.index.get_level_values("element"):
        ways_gdf = gdf.xs("way", level="element", drop_level=True)
        ways_gdf = ways_gdf.explode(index_parts=False).reset_index(drop=True)
        ways_gdf = ways_gdf[ways_gdf.geometry.type == "Polygon"]
    else:
        ways_gdf = gpd.GeoDataFrame(columns=gdf.columns, crs=gdf.crs)  # type: ignore
    # extract relations
    if "element" in gdf.index.names and "relation" in gdf.index.get_level_values("element"):
        relations_gdf = gdf.xs("relation", level="element", drop_level=True)
        relations_gdf = relations_gdf.explode(index_parts=False).reset_index(drop=True)
        relations_gdf = relations_gdf[relations_gdf.geometry.type == "Polygon"]
    else:
        relations_gdf = gpd.GeoDataFrame(columns=gdf.columns, crs=gdf.crs)  # type: ignore
    # combine
    combined_gdf = pd.concat([ways_gdf, relations_gdf])
    combined_geom = combined_gdf.union_all()  # type: ignore
    # extract geoms and explode
    combined_gdf = gpd.GeoDataFrame({"geometry": [combined_geom]}, crs=combined_gdf.crs)  # type: ignore
    area_gdf = combined_gdf.explode(index_parts=False).reset_index(drop=True)
    area_gdf = area_gdf[area_gdf.geometry.type == "Polygon"]
    area_gdf = area_gdf[~area_gdf.geometry.is_empty]
    area_gdf = area_gdf[area_gdf.geometry.is_valid]
    return area_gdf


def _auto_clean_network(
    G: nx.MultiGraph,
    geom_wgs: geometry.Polygon,
    to_crs_code: int | str,
    final_clean_distances: tuple[int, ...],
    remove_disconnected: int,
    green_footways: bool = False,
    green_service_roads: bool = False,
) -> nx.MultiGraph:
    """ """
    # deduplicate by hierarchy
    G = graphs.nx_deduplicate_edges(G, dissolve_distance=20, max_ang_diff=20)
    # parks
    try:
        parks_gdf = ox.features_from_polygon(
            geom_wgs,
            tags={
                "landuse": ["cemetery", "forest"],
                "leisure": ["park", "garden", "sports_centre"],
            },
        )
        park_area_gdf = _extract_gdf(parks_gdf)
        park_area_gdf = park_area_gdf.to_crs(to_crs_code)
    except InsufficientResponseError:
        park_area_gdf = gpd.GeoDataFrame(columns=["geometry"], geometry="geometry", crs=to_crs_code)  # type: ignore
    # plazas
    try:
        plazas_gdf = ox.features_from_polygon(
            geom_wgs,
            tags={
                "highway": ["pedestrian"],
            },
        )
        plaza_area_gdf = _extract_gdf(plazas_gdf)
        plaza_area_gdf = plaza_area_gdf.to_crs(to_crs_code)
    except InsufficientResponseError:
        plaza_area_gdf = gpd.GeoDataFrame(columns=["geometry"], geometry="geometry", crs=to_crs_code)  # type: ignore
    # parking
    try:
        parking_gdf = ox.features_from_polygon(
            geom_wgs,
            tags={
                "amenity": ["parking"],
            },
        )
        parking_area_gdf = _extract_gdf(parking_gdf)
        parking_area_gdf = parking_area_gdf.to_crs(to_crs_code)
    except InsufficientResponseError:
        parking_area_gdf = gpd.GeoDataFrame(columns=["geometry"], geometry="geometry", crs=to_crs_code)  # type: ignore
    # use STR Tree for performance
    parks_buff_str_tree = STRtree(park_area_gdf.buffer(5).geometry.to_list())  # type: ignore
    plaza_str_tree = STRtree(plaza_area_gdf.geometry.to_list())  # type: ignore
    parking_str_tree = STRtree(parking_area_gdf.geometry.to_list())  # type: ignore
    # iter edges to find edges for marking
    remove_edges = []
    for start_node_key, end_node_key, edge_key, edge_data in tqdm(  # type: ignore
        G.edges(keys=True, data=True),  # type: ignore
        total=G.number_of_edges(),
        disable=config.QUIET_MODE,
    ):
        edge_geom = edge_data["geom"]
        if "footway" in edge_data["highways"]:
            # mark park footways
            itx = parks_buff_str_tree.query(edge_geom, predicate="within")
            if len(itx):
                if green_footways is False:
                    remove_edges.append((start_node_key, end_node_key, edge_key))
                else:
                    idx = G[start_node_key][end_node_key][edge_key]["highways"].index("footway")
                    G[start_node_key][end_node_key][edge_key]["highways"][idx] = "footway_green"
            # mark plaza footways
            else:
                itx = plaza_str_tree.query(edge_geom, predicate="within")
                if len(itx):
                    idx = G[start_node_key][end_node_key][edge_key]["highways"].index("footway")
                    G[start_node_key][end_node_key][edge_key]["highways"][idx] = "footway_pedestrian"
        # mark green / cemetries etc. service roads
        if "service" in edge_data["highways"]:
            itx = parks_buff_str_tree.query(edge_geom, predicate="within")
            if len(itx):
                if green_service_roads is False:
                    remove_edges.append((start_node_key, end_node_key, edge_key))
                else:
                    idx = G[start_node_key][end_node_key][edge_key]["highways"].index("service")
                    G[start_node_key][end_node_key][edge_key]["highways"][idx] = "service_green"
            # remove parking service roads
            itx = parking_str_tree.query(edge_geom, predicate="within")
            if len(itx):
                remove_edges.append((start_node_key, end_node_key, edge_key))
    G.remove_edges_from(remove_edges)
    # remove disconnected components
    G = graphs.nx_remove_dangling_nodes(G, despine=0, remove_disconnected=remove_disconnected)
    # clean by highway types - leave motorways alone
    # split only for a given type at a time
    for dist, tags, max_angle in (
        (28, ["trunk"], 45),
        (24, ["primary"], 45),
        (20, ["secondary"], 45),
        (16, ["tertiary"], 45),
    ):
        G = graphs.nx_split_opposing_geoms(
            G,
            buffer_dist=dist,
            squash_nodes=True,
            centroid_by_itx=True,
            osm_hwy_target_tags=tags,
            osm_matched_tags_only=True,
            prioritise_by_hwy_tag=True,
            simplify_by_max_angle=max_angle,
        )
    # consolidate
    for dist, tags, max_angle in (
        (28, ["trunk"], 95),
        (24, ["trunk", "primary"], 95),
        (20, ["trunk", "primary", "secondary"], 95),
        (16, ["trunk", "primary", "secondary", "tertiary"], 95),
    ):
        G = graphs.nx_consolidate_nodes(
            G,
            buffer_dist=dist,
            crawl=False,
            centroid_by_itx=True,
            osm_hwy_target_tags=tags,
            osm_matched_tags_only=True,
            prioritise_by_hwy_tag=True,
            simplify_by_max_angle=max_angle,
        )
        G = graphs.nx_remove_filler_nodes(G)
    # snap gapped endings - don't clean danglers before this
    G = graphs.nx_snap_gapped_endings(
        G,
        osm_hwy_target_tags=[
            "residential",
            "living_street",
            # "service", # intentionally omitted - e.g. parking lots
            "cycleway",
            "bridleway",
            "pedestrian",
            "steps",
            "footway",
            "footway_green",
            "footway_pedestrian",  # plazas
            "path",
        ],
        buffer_dist=20,
    )
    # snap gapped endings to roads - don't clean danglers before this
    # look for degree 1 dead-ends and link to nearby edges
    G = graphs.nx_split_opposing_geoms(
        G,
        buffer_dist=20,
        osm_hwy_target_tags=[
            # "trunk",  # intentionally omitted
            "primary",
            "primary_link",
            "secondary",
            "secondary_link",
            "tertiary",
            "tertiary_link",
            "residential",
            "living_street",
            # "service", # intentionally omitted - e.g. parking lots
            "cycleway",
            "bridleway",
            "pedestrian",
            "steps",
            "footway",
            "footway_green",
            "footway_pedestrian",  # plazas
            "path",
        ],
        min_node_degree=1,
        max_node_degree=1,
        squash_nodes=False,
    )
    # remove danglers
    G = graphs.nx_remove_dangling_nodes(G, despine=40)
    # do smaller scale cleaning
    max_angle = 120  # rue de nevers in Paris
    for dist in final_clean_distances:
        G = graphs.nx_split_opposing_geoms(
            G,
            buffer_dist=dist,
            squash_nodes=True,
            centroid_by_itx=True,
            osm_hwy_target_tags=[
                # "trunk",  # intentionally omitted
                "primary",
                "primary_link",
                "secondary",
                "secondary_link",
                "tertiary",
                "tertiary_link",
                "residential",
                "living_street",
                "service",
                "cycleway",
                "bridleway",
                "pedestrian",
                # "steps",
                "footway",
                "footway_pedestrian",  # plazas
                "path",
                "unclassified",
            ],
            prioritise_by_hwy_tag=True,
            simplify_by_max_angle=max_angle,
        )
        G = graphs.nx_consolidate_nodes(
            G,
            buffer_dist=dist,
            crawl=True,
            centroid_by_itx=True,
            osm_hwy_target_tags=[
                "trunk",
                "trunk_link",
                "primary",
                "primary_link",
                "secondary",
                "secondary_link",
                "tertiary",
                "tertiary_link",
                "residential",
                "living_street",
                "service",
                "cycleway",
                "bridleway",
                "pedestrian",
                "steps",
                "footway",
                "footway_pedestrian",  # plazas
                "path",
                "unclassified",
            ],
            prioritise_by_hwy_tag=True,
            simplify_by_max_angle=max_angle,
        )
    G = graphs.nx_remove_filler_nodes(G)
    G = graphs.nx_merge_parallel_edges(G, merge_edges_by_midline=True, contains_buffer_dist=50)
    G = graphs.nx_iron_edges(G, min_self_loop_length=100, max_foot_tunnel_length=100)
    # do this last to clean up any orphaned sub components
    G = graphs.nx_remove_dangling_nodes(G, despine=25)

    return G


def osm_graph_from_poly(
    poly_geom: geometry.Polygon,
    poly_crs_code: int | str = 4326,
    to_crs_code: int | str | None = None,
    custom_request: str | None = None,
    simplify: bool = True,
    final_clean_distances: tuple[int, ...] = (5, 10),
    remove_disconnected: int = 100,
    cycleways: bool = True,
    busways: bool = False,
    green_footways: bool = False,
    green_service_roads: bool = False,
    timeout: int = 300,
    max_tries: int = 3,
) -> nx.MultiGraph:  # noqa
    """

    Prepares a `networkX` `MultiGraph` from an OSM request for the specified shapely polygon. This function will
    retrieve the OSM response and will automatically unpack this into a `networkX` graph. Simplification will be applied
    by default, but can be disabled.

    Parameters
    ----------
    poly_geom: shapely.Polygon
        A shapely Polygon representing the extents for which to fetch the OSM network.
    poly_crs_code: int | str
        An integer representing a valid EPSG code for the provided polygon. For example, [4326](https://epsg.io/4326) if
        using WGS lng / lat, or [27700](https://epsg.io/27700) if using the British National Grid.
    to_crs_code: int | str
        An optional `pyproj` compatible `str` or `int` representing a valid CRS for the generated network returned from
        this function. If this parameter is provided, then the network will be converted to the specified CRS. If not
        provided, then the OSM network will be projected into a local UTM coordinate reference system.
    buffer_dist: int
        A distance to use for buffering and cleaning operations. 15m by default.
    custom_request: str
        An optional custom OSM request. If provided, this must include a "geom_osm" string formatting key for inserting
        the geometry passed to the OSM API query. See the discussion below.
    simplify: bool
        Whether to automatically simplify the OSM graph.
    final_clean_distances: tuple[int]
        A tuple of distances to use for the final cleaning step. These will be applied incrementally.
        (6, 12) by default.
    remove_disconnected: int
        Remove disconnected components containing fewer nodes than specified. 100 nodes by default.
    cycleways: bool
        Whether to include cycleways. True by default.
    busways: bool
        Whether to include busways. False by default.
    green_footways: bool
        Whether to include footways contained by green areas. When True, footways contained by green areas are kept
        but are labelled as `footway_green` and can be removed manually if required. False by default.
    green_service_roads: bool
        Whether to include service roads contained by green areas. When True, service roads contained by green areas are
        kept but are labelled as `service_green` and can be removed manually if required. False by default.
    timeout: int
        Timeout duration for API call in seconds.
    max_tries: int
        The number of attempts to fetch a response before raising.

    Returns
    -------
    nx.MultiGraph
        A `networkX` `MultiGraph` with `x` and `y` node attributes that have been converted to UTM. The network will be
        simplified if the `simplify` parameter is `True`.

    Examples
    --------
    If you wish to provide your own OSM request, then provide a valid OSM API request to the `custom_request` parameter.
    The string must contain a `geom_osm` f-string formatting key. This allows for the geometry parameter passed to the
    OSM API to be injected into the request. It is also recommended to not use the `skel` output option so that
    `cityseer` can use street name and highway reference information for cleaning purposes. See
    [OSM Overpass](https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL) for experimenting with custom queries.

    The following is the default query which you can adapt for your purposes. Notice the `geom_osm` f-string
    interpolation key (for injecting the geometry) and the use of `out qt;` instead of `out skel qt;`.

    ```python
    /* https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL */
    [out:json];
    (way["highway"]
        ["highway"!~"bus_guideway|busway|escape|raceway|proposed|planned|abandoned|platform|
            emergency_bay|rest_area|disused|corridor|ladder|bus_stop|elevator|services"]
        ["area"!="yes"]
        ["footway"!="sidewalk"]
        ["amenity"!~"charging_station|parking|fuel|motorcycle_parking|parking_entrance|parking_space"]
        ["indoor"!="yes"]
        ["level"!="-2"]
        ["level"!="-3"]
        ["level"!="-4"]
        ["level"!="-5"](poly:"{geom_osm}");
    );
    out body;
    >;
    out qt;
    ```

    """
    # format for OSM query
    in_transformer = Transformer.from_crs(poly_crs_code, 4326, always_xy=True)
    coords = [in_transformer.transform(lng, lat) for lng, lat in poly_geom.exterior.coords]
    geom_wgs = geometry.Polygon(shell=coords)
    geom_osm = str.join(" ", [f"{lat} {lng}" for lng, lat in coords])
    if custom_request is not None:
        if "geom_osm" not in custom_request:
            raise ValueError(
                'The provided custom_request does not contain an f-string interpolation bracket for "geom_osm". '
                "This key is required for interpolating the generated geometry into the request. See the documentation."
            )
        request = custom_request.format(geom_osm=geom_osm)
    else:
        cw = "cycleway|" if cycleways is False else ""
        bw = "busway|" if busways is False else ""
        request = f"""
        /* https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL */
        [out:json];
        (way["highway"]
            ["highway"!~"bus_guideway|{bw}{cw}escape|raceway|proposed|planned|abandoned|platform|emergency_bay|
                rest_area|disused|corridor|ladder|bus_stop|elevator|services"]
            ["area"!="yes"]
            ["footway"!="sidewalk"]
            ["amenity"!~"charging_station|parking|fuel|motorcycle_parking|parking_entrance|parking_space"]
            ["indoor"!="yes"]
            ["level"!="-2"]
            ["level"!="-3"]
            ["level"!="-4"]
            ["level"!="-5"](poly:"{geom_osm}");
        );
        out body;
        >;
        out qt;
        """
    # generate the query
    osm_response = fetch_osm_network(request, timeout=timeout, max_tries=max_tries)
    # set config to skip validation
    config.SKIP_VALIDATION = True
    # build graph
    graph_wgs = nx_from_osm(osm_json=osm_response.text)  # type: ignore
    graph_wgs = graphs.nx_simple_geoms(graph_wgs)
    # extract CRS code if necessary
    if to_crs_code is None:
        # need CRS code so do this manually
        nd_key = list(graph_wgs.nodes())[0]
        to_crs_code = util.extract_utm_epsg_code(graph_wgs.nodes[nd_key]["x"], graph_wgs.nodes[nd_key]["y"])
    # project
    graph_crs = nx_epsg_conversion(graph_wgs, to_crs_code)
    graph_crs = graphs.nx_remove_filler_nodes(graph_crs)
    if simplify:
        graph_crs = _auto_clean_network(
            graph_crs,
            geom_wgs,
            int(to_crs_code),
            final_clean_distances,
            remove_disconnected,
            green_footways,
            green_service_roads,
        )
    # reset validation flag
    config.SKIP_VALIDATION = False

    return util.validate_cityseer_networkx_graph(graph_crs)


def nx_from_osm(osm_json: str) -> nx.MultiGraph:
    """
    Generate a `NetworkX` `MultiGraph` from [Open Street Map](https://www.openstreetmap.org) data.

    Parameters
    ----------
    osm_json: str
        A `json` string response from the [OSM overpass API](https://wiki.openstreetmap.org/wiki/Overpass_API),
        consisting of `nodes` and `ways`.

    Returns
    -------
    nx.MultiGraph
        A `NetworkX` `MultiGraph` with `x` and `y` attributes in [WGS84](https://epsg.io/4326) `lng`, `lat` geographic
        coordinates.

    """
    osm_network_data = json.loads(osm_json)
    nx_multigraph = nx.MultiGraph()
    nx_multigraph.graph["crs"] = CRS(4326)
    # deduplicate nodes based on x, y matches
    xy_nd_map: dict[str, str] = {}  # from x y to original node index
    nd_merge_map: dict[str, str] = {}  # from original node index to deduplicated node index

    for elem in osm_network_data["elements"]:
        if elem["type"] == "node":
            # all nodes should be string type
            nd_idx = str(elem["id"])
            x = elem["lon"]
            y = elem["lat"]
            nd_x_y = f"{x}-{y}"
            # when deduplicating, sometimes overlapping stairways / underpasses might share an x, y space...
            if "tags" in elem and "level" in elem["tags"]:
                nd_x_y = f"{nd_x_y}-{elem['tags']['level']}"
            # only add if non-duplicate
            if nd_x_y not in xy_nd_map:
                xy_nd_map[nd_x_y] = nd_idx
            else:
                logger.warning(f"Merging node {nd_idx} into {xy_nd_map[nd_x_y]} due to identical x, y coords.")
            # ok_nd_idx will correspond to deduplicated node index
            ok_nd_idx = xy_nd_map[nd_x_y]
            # track original node idx to deduplicated idx for reference when building edges
            nd_merge_map[nd_idx] = ok_nd_idx
            nx_multigraph.add_node(ok_nd_idx, x=x, y=y)

    def get_merged_nd_keys(_idx: int) -> tuple[str, str]:
        start_nd_key = str(elem["nodes"][_idx])
        end_nd_key = str(elem["nodes"][_idx + 1])
        return nd_merge_map[start_nd_key], nd_merge_map[end_nd_key]

    for elem in osm_network_data["elements"]:
        if elem["type"] == "way":
            count = len(elem["nodes"])
            if "tags" in elem:
                tags = elem["tags"]
                name = [tags["name"].lower()] if "name" in tags else []
                ref = [tags["ref"].lower()] if "ref" in tags else []
                highway = [tags["highway"].lower()] if "highway" in tags else []
                levels = [0]
                if "level" in tags:
                    try:
                        if ":" in tags["level"]:
                            levels = tags["level"].split(":")
                        elif ";" in tags["level"]:
                            levels = tags["level"].split(";")
                        elif "," in tags["level"]:
                            levels = tags["level"].split(",")
                        else:
                            levels = [tags["level"]]
                        levels = [int(round(float(level))) for level in levels]
                    except Exception:
                        logger.warning(f"Unable to parse level info: {tags['level']}")
                is_tunnel = False
                if "tunnel" in tags:
                    # tends to be "yes" or "building_passage"
                    is_tunnel = True
                is_bridge = False
                if "bridge" in tags:
                    # tends to be "yes" or "building_passage" or things like "boardwalk"
                    is_bridge = True
                for idx in range(count - 1):
                    start_nd_key, end_nd_key = get_merged_nd_keys(idx)
                    nx_multigraph.add_edge(
                        start_nd_key,
                        end_nd_key,
                        names=name,
                        routes=ref,
                        highways=highway,
                        levels=levels,
                        is_tunnel=is_tunnel,
                        is_bridge=is_bridge,
                    )
            else:
                for idx in range(count - 1):
                    start_nd_key, end_nd_key = get_merged_nd_keys(idx)
                    nx_multigraph.add_edge(start_nd_key, end_nd_key)

    # geoms not created yet
    return util.validate_cityseer_networkx_graph(nx_multigraph, validate_edges=False)


def nx_from_osm_nx(
    nx_multidigraph: nx.MultiDiGraph,
    node_attributes: list[str] | None = None,
    edge_attributes: list[str] | None = None,
    tolerance: float = config.ATOL,
) -> nx.MultiGraph:
    """
    Copy an [`OSMnx`](https://osmnx.readthedocs.io/) directed `MultiDiGraph` to an undirected `cityseer` `MultiGraph`.

    See the [`OSMnx`](/guide#osm-and-networkx) section of the guide for a more general discussion (and example) on
    workflows combining `OSMnx` with `cityseer`.

    `x` and `y` node attributes will be copied directly and `geometry` edge attributes will be copied to a `geom` edge
    attribute. The conversion process will snap the `shapely` `LineString` endpoints to the corresponding start and end
    node coordinates.

    Note that `OSMnx` `geometry` attributes only exist for simplified edges: if a `geometry` edge attribute is not
    found, then a simple (straight) `shapely` `LineString` geometry will be inferred from the respective start and end
    nodes.

    Other attributes will be ignored to avoid potential downstream misinterpretations of the attributes as a consequence
    of subsequent steps of graph manipulation, i.e. to avoid situations where attributes may fall out of lock-step with
    the state of the graph. If particular attributes need to be copied across, and assuming cognisance of downstream
    implications, then these can be manually specified by providing a list of node attributes keys per the
    `node_attributes` parameter or edge attribute keys per the `edge_attributes` parameter.

    Parameters
    ----------
    nx_multidigraph: MultiDiGraph
        A `OSMnx` derived `networkX` `MultiDiGraph` containing `x` and `y` node attributes, with optional `geometry`
        edge attributes containing `LineString` geoms (for simplified edges).
    node_attributes: tuple[str]
        Optional node attributes to copy to the new MultiGraph. (In addition to the default `x` and `y` attributes.)
    edge_attributes: tuple[str]
        Optional edge attributes to copy to the new MultiGraph. (In addition to the optional `geometry` attribute.)
    tolerance: float
        Tolerance at which to raise errors for mismatched geometry end-points vis-a-vis corresponding node coordinates.
        Prior to conversion, this method will check edge geometry end-points for alignment with the corresponding
        end-point nodes. Where these don't align within the given tolerance an exception will be raised. Otherwise, if
        within the tolerance, the conversion function will snap the geometry end-points to the corresponding node
        coordinates so that downstream exceptions are not subsequently raised. It is preferable to minimise graph
        manipulation prior to conversion to a `cityseer` compatible `MultiGraph` otherwise particularly large tolerances
        may be required, and this may lead to some unexpected or undesirable effects due to aggressive snapping.

    Returns
    -------
    nx.MultiGraph
        A `cityseer` compatible `networkX` graph with `x` and `y` node attributes and `geom` edge attributes.

    """
    if not isinstance(nx_multidigraph, nx.MultiDiGraph):
        raise TypeError("This method requires a directed networkX MultiDiGraph as derived from `OSMnx`.")
    if node_attributes is not None and not isinstance(node_attributes, list | tuple):
        raise TypeError("Node attributes to be copied should be provided as either a list or tuple of attribute keys.")
    if edge_attributes is not None and not isinstance(edge_attributes, list | tuple):
        raise TypeError("Edge attributes to be copied should be provided as either a list or tuple of attribute keys.")
    logger.info("Converting OSMnx MultiDiGraph to cityseer MultiGraph.")
    # target MultiGraph
    g_multi = nx.MultiGraph()
    g_multi.graph["crs"] = CRS(nx_multidigraph.graph["crs"])

    def _process_node(nd_key: NodeKey) -> tuple[float, float]:
        # x
        if "x" not in nx_multidigraph.nodes[nd_key]:
            raise KeyError(f'Encountered node missing "x" coordinate attribute for node {nd_key}.')
        x: float = nx_multidigraph.nodes[nd_key]["x"]
        # y
        if "y" not in nx_multidigraph.nodes[nd_key]:
            raise KeyError(f'Encountered node missing "y" coordinate attribute for node {nd_key}.')
        y: float = nx_multidigraph.nodes[nd_key]["y"]
        # add node and attributes if necessary
        nd_key = str(nd_key)
        if nd_key not in g_multi:
            g_multi.add_node(nd_key, x=x, y=y)
            if node_attributes is not None:
                for node_att in node_attributes:
                    if node_att not in nx_multidigraph.nodes[nd_key]:
                        raise ValueError(f"Specified attribute {node_att} is not available for node {nd_key}.")
                    g_multi.nodes[nd_key][node_att] = nx_multidigraph.nodes[nd_key][node_att]

        return x, y

    # copy nodes and edges
    start_nd_key: NodeKey
    end_nd_key: NodeKey
    edge_idx: int
    edge_data: EdgeData
    for start_nd_key, end_nd_key, edge_idx, edge_data in tqdm(  # type: ignore
        nx_multidigraph.edges(data=True, keys=True),  # type: ignore
        disable=config.QUIET_MODE,  # type: ignore
    ):
        edge_data = cast(EdgeData, edge_data)  # type: ignore
        s_x, s_y = _process_node(start_nd_key)
        e_x, e_y = _process_node(end_nd_key)
        # copy edge if present
        if "geometry" in edge_data:
            line_geom: geometry.LineString = edge_data["geometry"]
        # otherwise create
        else:
            line_geom = geometry.LineString([[s_x, s_y], [e_x, e_y]])
        # check for LineString validity
        if line_geom.geom_type != "LineString":
            raise TypeError(
                f"Expecting LineString geometry but found {line_geom.geom_type} geometry for "
                f"edge {start_nd_key}-{end_nd_key}."
            )
        # orient LineString
        geom_coords = line_geom.coords
        if not np.allclose((s_x, s_y), geom_coords[0][:2], atol=tolerance, rtol=0):
            geom_coords = util.align_linestring_coords(geom_coords, (s_x, s_y))
        # check starting and ending tolerances
        if not np.allclose((s_x, s_y), geom_coords[0][:2], atol=tolerance, rtol=0):
            raise ValueError("Starting node coordinates don't match LineString geometry starting coordinates.")
        if not np.allclose((e_x, e_y), geom_coords[-1][:2], atol=tolerance, rtol=0):
            raise ValueError("Ending node coordinates don't match LineString geometry ending coordinates.")
        # snap starting and ending coords to avoid rounding error issues
        geom_coords = util.snap_linestring_startpoint(geom_coords, (s_x, s_y))
        geom_coords = util.snap_linestring_endpoint(geom_coords, (e_x, e_y))
        # convert keys to str
        start_nd_key = str(start_nd_key)
        end_nd_key = str(end_nd_key)
        # new graph expects str
        g_multi.add_edge(start_nd_key, end_nd_key, key=edge_idx, geom=geometry.LineString(geom_coords))
        if edge_attributes is not None:
            for edge_att in edge_attributes:
                if edge_att not in edge_data:
                    raise ValueError(f"Attribute {edge_att} is not available for edge {start_nd_key}-{end_nd_key}.")
                g_multi[start_nd_key][end_nd_key][edge_idx][edge_att] = edge_data[edge_att]  # type: ignore

    return util.validate_cityseer_networkx_graph(g_multi)


BboxType = tuple[int, int, int, int] | tuple[float, float, float, float]


def nx_from_open_roads(
    open_roads_path: str | Path,
    road_node_layer_key: str = "road_node",
    road_link_layer_key: str = "road_link",
    target_bbox: BboxType | None = None,
) -> nx.MultiGraph:
    """
    Generates a `networkX` `MultiGraph` from an OS Open Roads dataset.

    Parameters
    ----------
    open_roads_path: str | Path
        A valid relative filepath from which to load the OS Open Roads dataset.
    target_bbox: tuple[int]
        A tuple of integers or floats representing the `[s, w, n, e]` bounding box extents for which to load the
        dataset. Set to `None` for no bounding box.
    road_node_layer_key: str
        The `GPKG` layer key for the OS Open Roads road nodes layer. This may change from time to time.
    road_link_layer_key: str
        The `GPKG` layer key for the OS Open Roads road links layer. This may change from time to time.

    Returns
    -------
    nx.MultiGraph
        A `cityseer` compatible `networkX` graph with `x` and `y` node attributes and `geom` edge attributes.

    """
    # create a networkX multigraph
    g_multi = nx.MultiGraph()
    g_multi.graph["crs"] = CRS(27700)
    # load the nodes
    with fiona.open(open_roads_path, layer=road_node_layer_key) as nodes:
        for node_data in nodes.values(bbox=target_bbox):
            node_id: str = node_data.properties["id"]
            x: float
            y: float
            x, y = node_data.geometry["coordinates"]
            g_multi.add_node(node_id, x=x, y=y)
    # load the edges
    n_dropped = 0
    with fiona.open(open_roads_path, layer=road_link_layer_key) as edges:
        for edge_data in edges.values(bbox=target_bbox):
            # x, y = edge_data['geometry']['coordinates']
            props: dict = edge_data.properties  # type: ignore
            start_nd: str = props["start_node"]
            end_nd: str = props["end_node"]
            names: set[str] = set()
            for name_key in ["name_1", "name_2"]:
                name: str | None = props[name_key]
                if name is not None:
                    names.add(name)
            routes: set[str] = set()
            for ref_key in ["road_classification_number"]:
                ref: str | None = props[ref_key]
                if ref is not None:
                    routes.add(ref)
            highways: set[str] = set()
            for highway_key in ["road_function", "road_classification"]:  # 'formOfWay'
                highway: str | None = props[highway_key]
                if highway is not None:
                    highways.add(highway)
            if props["trunk_road"]:
                highways.add("Trunk Road")
            if props["primary_route"]:
                highways.add("Primary Road")
            # filter out unwanted highway tags
            highways.difference_update(
                {
                    "Not Classified",
                    "Unclassified",
                    "Unknown",
                    "Restricted Local Access Road",
                    "Local Road",
                    "Classified Unnumbered",
                }
            )
            # create the geometry
            geom = geometry.LineString(edge_data.geometry["coordinates"])
            geom: geometry.LineString = geom.simplify(5)  # type: ignore
            # do not add edges to clipped extents
            if start_nd not in g_multi or end_nd not in g_multi:
                n_dropped += 1
                continue
            g_multi.add_edge(
                start_nd, end_nd, names=list(names), routes=list(routes), highways=list(highways), geom=geom
            )
    logger.info(f"Nodes: {g_multi.number_of_nodes()}")
    logger.info(f"Edges: {g_multi.number_of_edges()}")
    logger.info(f"Dropped {n_dropped} edges where not both start and end nodes were present.")
    logger.info("Running basic graph cleaning")
    g_multi = graphs.nx_remove_filler_nodes(g_multi)
    g_multi = graphs.nx_merge_parallel_edges(g_multi, True, 10)

    return util.validate_cityseer_networkx_graph(g_multi)


def network_structure_from_nx(
    nx_multigraph: nx.MultiGraph,
    crs: None = None,
) -> tuple[gpd.GeoDataFrame, gpd.GeoDataFrame, rustalgos.graph.NetworkStructure]:
    """
    Transpose a `networkX` `MultiGraph` into a `gpd.GeoDataFrame` and `NetworkStructure` for use by `cityseer`.

    Calculates length and angle attributes, as well as in and out bearings, and stores this information in the returned
    data maps.

    Parameters
    ----------
    nx_multigraph: nx.MultiGraph
        A `networkX` `MultiGraph` in a projected coordinate system, containing `x` and `y` node attributes, and `geom`
        edge attributes containing `LineString` geoms.
    crs: None
        The `crs` parameter is deprecated and will be removed in a future release. If your network is
        generated via cityseer from OSM or GeoPandas then CRS handling is automatic. Otherwise, the CRS can be set
        directly in the graph if necessary at G.graph["crs"]; for example: G.graph["crs"] = 4326

    Returns
    -------
    gpd.GeoDataFrame
        A `gpd.GeoDataFrame` with `live`, `weight`, and `geometry` attributes. The original `networkX` graph's node keys
        will be used for the `GeoDataFrame` index. If `nx_multigraph` is a dual graph prepared with
        [`graphs.nx_to_dual`](/tools/graphs#nx-to-dual) then the corresponding primal edge `LineString` geometry will be
        set as the `GeoPandas` geometry for visualisation purposes using `primal_edge` for the column name. The dual
        node `Point` geometry will be saved in `WKT` format to the `dual_node` column.
    gpd.GeoDataFrame
        A `gpd.GeoDataFrame` with `ns_edge_idx`, `start_ns_node_idx`, `end_ns_node_idx`, `edge_idx`, `nx_start_node_key`
        ,`nx_end_node_key`, `imp_factor`, `total_bearing`, `geom`
        attributes.
    rustalgos.graph.NetworkStructure
        A [`rustalgos.graph.NetworkStructure`](/rustalgos/rustalgos#networkstructure) instance.

    """
    if crs is not None:
        logger.warning(
            """
            The `crs` parameter is deprecated and will be removed in a future release. If your network is
            generated via cityseer from OSM or GeoPandas then CRS handling is automatic. Otherwise, the CRS can be set
            directly in the graph if necessary at G.graph["crs"]; for example: G.graph["crs"] = 4326
            """
        )
    logger.info("Preparing node and edge arrays from networkX graph.")
    g_multi_copy = util.validate_cityseer_networkx_graph(nx_multigraph)
    # prepare the network structure
    network_structure = rustalgos.graph.NetworkStructure()
    # generate the network information
    agg_node_data: dict[str, tuple[Any, ...]] = {}
    agg_node_dual_data: dict[str, tuple[Any, Any, Any, Any]] = {}
    agg_edge_data: dict[str, tuple[Any, ...]] = {}
    agg_edge_dual_data: list[str] = []
    node_data: NodeData
    # set nodes
    for node_key, node_data in tqdm(g_multi_copy.nodes(data=True), disable=config.QUIET_MODE):
        # node_key must be string
        if not isinstance(node_key, str):
            raise TypeError(f"Node key must be of type string but encountered {type(node_key)}")
        node_x: float = node_data["x"]
        node_y: float = node_data["y"]
        is_live: bool = True
        if "live" in node_data:
            is_live = bool(node_data["live"])
        weight = 1
        if "weight" in node_data:
            weight = node_data["weight"]
        # set node
        ns_node_idx = network_structure.add_street_node(node_key, node_x, node_y, is_live, weight)
        agg_node_data[node_key] = (ns_node_idx, node_x, node_y, is_live, weight, geometry.Point(node_x, node_y))
        if "is_dual" in g_multi_copy.graph and g_multi_copy.graph["is_dual"]:  # type: ignore
            agg_node_dual_data[node_key] = (
                node_data["primal_edge"],
                node_data["primal_edge_node_a"],
                node_data["primal_edge_node_b"],
                node_data["primal_edge_idx"],
            )
    # set edges
    for start_node_key in tqdm(g_multi_copy.nodes(), disable=config.QUIET_MODE):
        # build edges
        start_ns_node_idx, start_node_x, start_node_y, _, _, _ = agg_node_data[start_node_key]
        end_node_key: str
        for end_node_key in g_multi_copy.neighbors(start_node_key):
            end_ns_node_idx, end_node_x, end_node_y, _, _, _ = agg_node_data[end_node_key]
            for edge_idx, edge_data in g_multi_copy[start_node_key][end_node_key].items():
                # align coords
                line_geom_coords = util.align_linestring_coords(edge_data["geom"].coords, (start_node_x, start_node_y))
                aligned_line_geom = geometry.LineString(line_geom_coords)
                # add edge - USE add_street_edge
                ns_edge_idx = network_structure.add_street_edge(
                    start_ns_node_idx,
                    end_ns_node_idx,
                    int(edge_idx),
                    start_node_key,
                    end_node_key,
                    aligned_line_geom.wkt,  # geom_wkt is required
                    float(edge_data.get("imp_factor", 1.0)),  # imp_factor
                )
                # add to edge data
                agg_edge_data[f"{start_node_key}-{end_node_key}"] = (
                    ns_edge_idx,
                    start_ns_node_idx,
                    end_ns_node_idx,
                    edge_idx,
                    start_node_key,
                    end_node_key,
                    edge_data.get("imp_factor", 1.0),
                    util.measure_bearing(np.array(line_geom_coords[0]), np.array(line_geom_coords[-1])),
                    aligned_line_geom,
                )
                if "is_dual" in g_multi_copy.graph and g_multi_copy.graph["is_dual"]:  # type: ignore
                    agg_edge_dual_data.append(edge_data["primal_node_id"])
    # create geopandas for node keys and data state
    nodes_gdf = gpd.GeoDataFrame.from_dict(
        agg_node_data,
        orient="index",
        columns=["ns_node_idx", "x", "y", "live", "weight", "geom"],
        geometry="geom",
        crs=g_multi_copy.graph["crs"],
    )
    # enforce float type for x, y
    nodes_gdf[["x", "y"]] = nodes_gdf[["x", "y"]].astype(float)
    edges_gdf = gpd.GeoDataFrame.from_dict(
        agg_edge_data,
        orient="index",
        columns=[
            "ns_edge_idx",
            "start_ns_node_idx",
            "end_ns_node_idx",
            "edge_idx",
            "nx_start_node_key",
            "nx_end_node_key",
            "imp_factor",
            "total_bearing",
            "geom",
        ],
        geometry="geom",
        crs=g_multi_copy.graph["crs"],
    )
    if "is_dual" in g_multi_copy.graph and g_multi_copy.graph["is_dual"]:  # type: ignore
        nodes_dual_gdf = pd.DataFrame.from_dict(
            agg_node_dual_data,
            orient="index",
            columns=[
                "primal_edge",
                "primal_edge_node_a",
                "primal_edge_node_b",
                "primal_edge_idx",
            ],
        )
        edges_gdf["primal_node_id"] = agg_edge_dual_data
        nodes_gdf: gpd.GeoDataFrame = nodes_gdf.join(nodes_dual_gdf)  # type: ignore
        nodes_gdf.set_geometry("primal_edge", inplace=True)
        nodes_gdf.set_crs(crs=g_multi_copy.graph["crs"], inplace=True)  # type: ignore
        nodes_gdf["dual_node"] = nodes_gdf["geom"].to_wkt()  # type: ignore
        nodes_gdf.drop(columns=["geom"], inplace=True)

    network_structure.validate()
    network_structure.build_edge_rtree()

    return nodes_gdf, edges_gdf, network_structure


def network_structure_from_gpd(
    nodes_gdf: gpd.GeoDataFrame,
    edges_gdf: gpd.GeoDataFrame,
) -> rustalgos.graph.NetworkStructure:
    """
    Reassembles a `NetworkStructure` from cityseer nodes and edges GeoDataFrames.

    This method is intended for use with "circular" workflows, where a `cityseer` NetworkX graph has been converted into
    `cityseer` nodes and edges GeoDataFrames using [`network_structure_from_nx`](#network_structure_from_nx). If the
    resultant GeoDataFrames are saved to disk and reloaded, then this method can be used to recreate the associated
    `NetworkStructure` which is required for optimised (`rust`) functions.

    Parameters
    ----------
    nodes_gdf: gpd.GeoDataFrame
        A cityseer created nodes `gpd.GeoDataFrame` where the originating `networkX` graph's node keys have been saved
        as the DataFrame index, and where the columns contain `x`, `y`, `live`, and `weight` attributes.
    edges_gdf: gpd.GeoDataFrame
        A cityseer created edges `gpd.GeoDataFrame` with `start_ns_node_idx`, `end_ns_node_idx`, `edge_idx`,
        `nx_start_node_key`, `nx_end_node_key`, `imp_factor` attributes.

    Returns
    -------
    rustalgos.graph.NetworkStructure
        A [`rustalgos.graph.NetworkStructure`](/rustalgos/rustalgos#networkstructure) instance.

    """
    # prepare the network structure
    network_structure = rustalgos.graph.NetworkStructure()
    # check column integrity
    nodes_cols = [
        "x",
        "y",
        "live",
        "weight",
    ]
    for col in nodes_cols:
        if col not in nodes_gdf.columns:
            raise ValueError(f"Missing expected column in nodes GDF: {col}")
    edges_cols = [
        "start_ns_node_idx",
        "end_ns_node_idx",
        "edge_idx",
        "nx_start_node_key",
        "nx_end_node_key",
        "imp_factor",
    ]
    for col in edges_cols:
        if col not in edges_gdf.columns:
            raise ValueError(f"Missing expected column in edges GDF: {col}")
    # pre-compute node index values and create mapping dictionary for faster lookups
    node_indices = nodes_gdf.index.values
    node_mapping = {}
    # process nodes and build mapping
    for nd_key, node_data in tqdm(nodes_gdf.iterrows(), total=len(nodes_gdf), disable=config.QUIET_MODE):
        ns_node_idx = network_structure.add_street_node(
            str(nd_key),
            float(node_data["x"]),
            float(node_data["y"]),
            bool(node_data["live"]),
            float(node_data["weight"]),
        )
        # store mapping in dictionary instead of writing back to GeoDataFrame
        node_mapping[nd_key] = ns_node_idx
    # process edges using the mapping dictionary
    for _edge_key, edge_data in tqdm(edges_gdf.iterrows(), total=len(edges_gdf), disable=config.QUIET_MODE):
        start_nx_nd_key = edge_data["nx_start_node_key"]
        end_nx_nd_key = edge_data["nx_end_node_key"]
        # fast lookup using dict and set membership
        if start_nx_nd_key not in node_indices or end_nx_nd_key not in node_indices:
            if start_nx_nd_key not in node_indices:
                logger.info(f"Skipping edge as start node nx key not found {start_nx_nd_key}")
            if end_nx_nd_key not in node_indices:
                logger.info(f"Skipping edge as end node nx key not found {end_nx_nd_key}")
            continue
        # get node indices from mapping dictionary - much faster than DataFrame lookups
        start_ns_nd_key = node_mapping[start_nx_nd_key]
        end_ns_nd_key = node_mapping[end_nx_nd_key]
        #
        line_geom = edge_data[edges_gdf.geometry.name]  # type: ignore
        start_nd_data = nodes_gdf.loc[start_nx_nd_key]
        line_geom_coords = util.align_linestring_coords(line_geom.coords, (start_nd_data.x, start_nd_data.y))
        aligned_line_geom = geometry.LineString(line_geom_coords)
        # add edge - USE add_street_edge
        network_structure.add_street_edge(
            start_ns_nd_key,
            end_ns_nd_key,
            int(edge_data["edge_idx"]),
            edge_data["nx_start_node_key"],
            edge_data["nx_end_node_key"],
            aligned_line_geom.wkt,  # geom_wkt is required
            float(edge_data["imp_factor"]),  # imp_factor
        )
    network_structure.validate()
    network_structure.build_edge_rtree()

    return network_structure


def add_transport_gtfs(
    gtfs_data_path: str,
    network_structure: rustalgos.graph.NetworkStructure,
    network_crs: int,
    max_netw_assign_dist: int = 400,
) -> tuple[rustalgos.graph.NetworkStructure, pd.DataFrame, pd.DataFrame]:
    """
    Add GTFS data to network structure.

    > This function is still in development and may change in future releases. Testing is ongoing.
    """
    gtfs_path = Path(gtfs_data_path)
    logger.info(f"Loading GTFS data from {gtfs_data_path}")
    if not gtfs_path.exists():
        raise FileNotFoundError(f"GTFS data not found at {gtfs_data_path}")
    if not (gtfs_path / "stops.txt").exists():
        raise FileNotFoundError(f"GTFS stops.txt not found at {gtfs_data_path}")
    if not (gtfs_path / "stop_times.txt").exists():
        raise FileNotFoundError(f"GTFS stop_times.txt not found at {gtfs_data_path}")
    # load GTFS stops data - rename stop_id to include gtfs_data_path
    stops = pd.read_csv(gtfs_path / "stops.txt")
    stops["stop_id"] = stops["stop_id"].apply(lambda sid: f"gtfs-{gtfs_data_path}-{sid}")
    # load GTFS stop times data - rename stop_id to include gtfs_data_path
    stop_times = pd.read_csv(gtfs_path / "stop_times.txt")
    stop_times["stop_id"] = stop_times["stop_id"].apply(lambda sid: f"gtfs-{gtfs_data_path}-{sid}")
    logger.info(f"Loaded {len(stops)} stops and {len(stop_times)} stop times")

    # prepare arrival time
    stop_times["arrival_time"] = pd.to_datetime(stop_times["arrival_time"], format="%H:%M:%S").dt.time
    stop_times["arrival_seconds"] = stop_times["arrival_time"].apply(lambda t: t.hour * 3600 + t.minute * 60 + t.second)
    stop_times.sort_values(by=["stop_id", "arrival_seconds"], inplace=True)
    # compute gaps between consecutive arrivals
    stop_times["wait_time"] = stop_times.groupby("stop_id")["arrival_seconds"].diff()
    # average wait time at stations
    avg_wait_time = stop_times.groupby("stop_id")["wait_time"].mean().fillna(0)
    avg_wait_time = avg_wait_time / 2
    # merge avg_wait_time into stop times data
    stops = stops.merge(avg_wait_time.rename("avg_wait_time"), on="stop_id", how="left")
    # transformer to convert lat/lon to graph crs
    transformer = Transformer.from_crs(4326, network_crs, always_xy=True)

    # Add GTFS stops as transport nodes, using add_transport_node with linking_radius and speed_m_s
    logger.info("Adding GTFS stops to network nodes (with street linking logic).")
    stop_idx_map = {}
    for _, row in tqdm(stops.iterrows(), total=len(stops), disable=config.QUIET_MODE):
        e, n = transformer.transform(row["stop_lon"], row["stop_lat"])
        ns_node_idx = network_structure.add_transport_node(
            row["stop_id"],
            float(e),
            float(n),
            linking_radius=max_netw_assign_dist,
        )
        stop_idx_map[row["stop_id"]] = ns_node_idx

    logger.info("Generating segment durations between stops.")
    stop_times["prev_stop_id"] = stop_times.groupby("trip_id")["stop_id"].shift()
    # sort stop_times for proper sequencing
    stop_times.sort_values(by=["trip_id", "stop_sequence"], inplace=True)
    # compute travel time between consecutive stops
    stop_times["segment_time"] = stop_times.groupby("trip_id")["arrival_seconds"].diff()
    # rename stop_id to next_stop_id
    stop_times.rename(columns={"stop_id": "next_stop_id"}, inplace=True)
    # average segment time between consecutive stops
    avg_stop_pairs = (
        stop_times.dropna(subset=["prev_stop_id"])  # remove rows where prev_stop_id is NaN
        .groupby(["prev_stop_id", "next_stop_id"])["segment_time"]
        .mean()
        .reset_index(name="avg_segment_time")
    )

    logger.info("Adding GTFS segments to network edges.")
    for _, row in tqdm(avg_stop_pairs.iterrows(), total=len(avg_stop_pairs), disable=config.QUIET_MODE):
        prev_stop = row["prev_stop_id"]
        next_stop = row["next_stop_id"]
        if prev_stop not in stop_idx_map or next_stop not in stop_idx_map:
            continue
        prev_stop_idx = stop_idx_map[prev_stop]
        next_stop_idx = stop_idx_map[next_stop]
        avg_seg_time = row["avg_segment_time"]
        # Add edge (forward)
        _edge_idx = network_structure.add_transport_edge(
            prev_stop_idx,
            next_stop_idx,
            0,  # edge_idx
            "na-gtfs",
            "na-gtfs",
            float(avg_seg_time),
            None,
        )
        # Add edge (reverse)
        _edge_idx = network_structure.add_transport_edge(
            next_stop_idx,
            prev_stop_idx,
            0,
            "na-gtfs",
            "na-gtfs",
            float(avg_seg_time),
            None,
        )

    network_structure.validate()
    network_structure.build_edge_rtree()

    return network_structure, stops, avg_stop_pairs


def nx_from_cityseer_geopandas(
    nodes_gdf: gpd.GeoDataFrame,
    edges_gdf: gpd.GeoDataFrame,
) -> nx.MultiGraph:
    """
    Write `cityseer` nodes and edges `GeoDataFrames` to a `networkX` `MultiGraph`.

    This method is intended for use with "circular" workflows, where a `cityseer` NetworkX graph has been converted into
    `cityseer` nodes and edges GeoDataFrames using [`network_structure_from_nx`](#network_structure_from_nx). Once
    metrics have been computed then this method can be used to convert the nodes and edges GeoDataFrames back into
    a `cityseer` compatible `networkX` graph with the computed metrics intact. This is useful when intending to
    visualise or export the metrics as a `networkX` graph.

    If importing a generic `gpd.GeoDataFrame` LineString dataset, then use the
    [nx_from_generic_geopandas](#nx_from_generic_geopandas) instead.

    Parameters
    ----------
    nodes_gdf: gpd.GeoDataFrame
        A `gpd.GeoDataFrame` with `live`, `weight`, and Point `geometry` attributes. The index will be used for the
        returned `networkX` graph's node keys.
    edges_gdf: gpd.GeoDataFrame
        An edges `gpd.GeoDataFrame` as derived from [`network_structure_from_nx`](#network-structure-from-nx).

    Returns
    -------
    nx.MultiGraph
        A `networkX` graph with geometries and attributes as copied from the input `GeoDataFrames`.

    """
    logger.info("Populating node and edge map data to a networkX graph.")
    g_multi_copy = nx.MultiGraph()
    g_multi_copy.graph["crs"] = CRS(nodes_gdf.crs)
    # after above so that errors caught first
    logger.info("Unpacking node data.")
    for nd_key, nd_data in tqdm(nodes_gdf.iterrows(), disable=config.QUIET_MODE):
        live = nd_data.live if hasattr(nd_data, "live") else True
        weight = nd_data.weight if hasattr(nd_data, "weight") else 1
        g_multi_copy.add_node(str(nd_key), x=nd_data.x, y=nd_data.y, live=live, weight=weight)
    logger.info("Unpacking edge data.")
    geom_key = edges_gdf.geometry.name
    for _, row_data in tqdm(edges_gdf.iterrows(), disable=config.QUIET_MODE):
        start_nd_key = str(row_data.nx_start_node_key)
        end_nd_key = str(row_data.nx_end_node_key)
        # explicitly only add if not yet added (vs implicit behaviour)
        if not g_multi_copy.has_edge(start_nd_key, end_nd_key, row_data.edge_idx):
            g_multi_copy.add_edge(
                start_nd_key,
                end_nd_key,
                row_data.edge_idx,
                imp_factor=row_data.imp_factor,
                total_bearing=row_data.total_bearing,
                geom=row_data[geom_key],  # type: ignore
            )
    # unpack any metrics written to the nodes
    metrics_column_labels: list[str] = [c for c in nodes_gdf.columns if c.startswith("cc_")]
    if metrics_column_labels:
        logger.info("Unpacking metrics to nodes.")
        for metrics_column_label in metrics_column_labels:
            for nd_key, node_row in tqdm(nodes_gdf.iterrows(), disable=config.QUIET_MODE):
                g_multi_copy.nodes[nd_key][metrics_column_label] = node_row[metrics_column_label]

    return util.validate_cityseer_networkx_graph(g_multi_copy)


def geopandas_from_nx(
    nx_multigraph: nx.MultiGraph,
    crs: None = None,
) -> gpd.GeoDataFrame:
    """
    Transpose a `cityseer` `networkX` `MultiGraph` into a `gpd.GeoDataFrame` representing the network edges.

    Converts the `geom` attribute attached to each edge into a GeoPandas GeoDataFrame. This is useful when
    inspecting or cleaning the network in QGIS. It can then be reimported with
    [`nx_from_generic_geopandas`](#nx-from-generic-geopandas)

    Parameters
    ----------
    nx_multigraph: nx.MultiGraph
        A `networkX` `MultiGraph` in a projected coordinate system, containing `x` and `y` node attributes, and `geom`
        edge attributes containing `LineString` geoms.
    crs: None
        The `crs` parameter is deprecated and will be removed in a future release. If your network is
        generated via cityseer from OSM or GeoPandas then CRS handling is automatic. Otherwise, the CRS can be set
        directly in the graph if necessary at G.graph["crs"]; for example: G.graph["crs"] = 4326

    Returns
    -------
    gpd.GeoDataFrame
        A `gpd.GeoDataFrame` with `edge_idx` and `geom` attributes.

    """
    if crs is not None:
        logger.warning(
            """
            The `crs` parameter is deprecated and will be removed in a future release. If your network is
            generated via cityseer from OSM or GeoPandas then CRS handling is automatic. Otherwise, the CRS can be set
            directly in the graph if necessary at G.graph["crs"]; for example: G.graph["crs"] = 4326
            """
        )
    logger.info("Preparing node and edge arrays from networkX graph.")
    g_multi_copy = util.validate_cityseer_networkx_graph(nx_multigraph)
    agg_edge_data = []
    # set edges
    for start_nd_key, end_nd_key, edge_idx, edge_data in g_multi_copy.edges(keys=True, data=True):  # type: ignore
        edge_data["start_nd_key"] = start_nd_key
        edge_data["end_nd_key"] = end_nd_key
        edge_data["edge_idx"] = edge_idx
        agg_edge_data.append(edge_data)
    edges_gdf = gpd.GeoDataFrame(agg_edge_data, crs=g_multi_copy.graph["crs"], geometry="geom")  # type: ignore

    return edges_gdf


def nx_from_generic_geopandas(
    gdf_network: gpd.GeoDataFrame,  # type: ignore
    drop_self_loops_dist: int = 50,
) -> nx.MultiGraph:
    """
    Converts a generic LineString `gpd.GeoDataFrame` to a `cityseer` compatible `networkX` `MultiGraph`.

    The `gpd.GeoDataFrame` should be provided in the "primal" form, where edges represent LineString geometries.

    Parameters
    ----------
    gdf_network: gpd.GeoDataFrame
        A LineString `gpd.GeoDataFrame`.
    drop_self_loops_dist: int
        Drop looping street segments shorter than specified distance. 20m by default.

    Returns
    -------
    nx.MultiGraph
        A `cityseer` compatible `networkX` graph with `x` and `y` node attributes and `geom` edge attributes.

    """
    gdf_network: gpd.GeoDataFrame = gdf_network.copy()  # type: ignore
    if gdf_network.crs is None:
        raise ValueError("The GeoDataframe must have a CRS set.")
    if not gdf_network.crs.is_projected:  # type: ignore
        raise ValueError("The GeoDataframe CRS must be projected, i.e. not geographic.")
    g_multi = nx.MultiGraph()
    g_multi.graph["crs"] = CRS(gdf_network.crs)

    def _node_key(node_coords):
        if len(node_coords) == 3:
            x, y, z = node_coords
            return f"x{x}-y{y}-z{z}"
        x, y = node_coords
        return f"x{x}-y{y}"

    geom_key: str = str(gdf_network.geometry.name)
    for edge_idx, edge_row in tqdm(gdf_network.iterrows(), total=len(gdf_network), disable=config.QUIET_MODE):
        # generate start and ending nodes
        edge_geom = edge_row[geom_key]
        # drop empty edges
        if edge_geom.is_empty:
            logger.warning(f"Dropping empty edge at row index {edge_idx}")
            continue
        # drop zero length edges
        if edge_geom.length == 0:
            logger.warning(f"Dropping zero length edge at row index {edge_idx}")
            continue
        # round to 1cm - assumes 1m units
        if len(edge_geom.coords[0]) == 3:
            edge_geom = geometry.LineString(
                [[round(c[0], 1), round(c[1], 1), round(c[2], 1)] for c in edge_geom.coords]
            )
        else:
            edge_geom = geometry.LineString([[round(c[0], 1), round(c[1], 1)] for c in edge_geom.coords])
        # extract node keys
        coords_a = edge_geom.coords[0]
        node_key_a = _node_key(coords_a)
        coords_b = edge_geom.coords[-1]
        node_key_b = _node_key(coords_b)
        # drop short self-loops
        if node_key_a == node_key_b and edge_geom.length < drop_self_loops_dist:
            continue
        # add nodes
        if node_key_a not in g_multi:
            g_multi.add_node(node_key_a, x=coords_a[0], y=coords_a[1])
        if node_key_b not in g_multi:
            g_multi.add_node(node_key_b, x=coords_b[0], y=coords_b[1])
        # add edge
        props = dict(edge_row)
        for k in ["geom", "geometry"]:
            if k in props:
                del props[k]
        # names, routes, highways, levels
        for k in ["names", "routes", "highways", "levels"]:
            if k not in props:
                props[k] = []  # type: ignore
            else:
                prop = props[k]
                if isinstance(prop, str):
                    prop = prop.strip("()[] ,'\"")
                    prop = prop.split(",")
                    prop = [p.strip("\" '") for p in prop]
                    prop = [p for p in prop if p not in ["", " ", None]]
                if not isinstance(prop, tuple | list):
                    raise TypeError(f"Expected key {k} to be a list type to retain compatibility with OSM workflows.")
                props[k] = prop  # type: ignore
        g_multi.add_edge(node_key_a, node_key_b, src_edge_idx=edge_idx, geom=edge_geom, **props)

    # deduplicate
    g_multi = graphs.nx_merge_parallel_edges(g_multi, merge_edges_by_midline=True, contains_buffer_dist=1)

    return util.validate_cityseer_networkx_graph(g_multi)
