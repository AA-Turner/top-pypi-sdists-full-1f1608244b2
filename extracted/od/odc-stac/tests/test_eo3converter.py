# pylint: disable=unused-argument,unused-variable,missing-module-docstring,wrong-import-position,import-error
# pylint: disable=redefined-outer-name,protected-access,import-outside-toplevel

import pytest

_ = pytest.importorskip("datacube")

import uuid
from typing import Any

import pystac
import pystac.asset
import pystac.collection
import pystac.item
from common import NO_WARN_CFG, STAC_CFG, mk_stac_item
from datacube.testutils.io import native_geobox
from datacube.utils.geometry import Geometry
from pystac.extensions.eo import EOExtension
from pystac.extensions.item_assets import ItemAssetsExtension
from pystac.extensions.projection import ProjectionExtension
from toolz import dicttoolz

from odc.stac._mdtools import RasterCollectionMetadata, has_proj_ext, has_raster_ext
from odc.stac.eo3 import infer_dc_product, stac2ds
from odc.stac.eo3._eo3converter import _compute_uuid, _item_to_ds


def test_infer_product_collection(
    sentinel_stac_collection: pystac.collection.Collection,
    sentinel_stac_ms_with_raster_ext: pystac.item.Item,
) -> None:
    assert has_raster_ext(sentinel_stac_collection) is True
    product = infer_dc_product(sentinel_stac_collection)
    assert product.measurements["SCL"].dtype == "uint8"
    assert product.measurements["SCL"].get("band") is None
    # check aliases from eo extension
    assert product.canonical_measurement("red") == "B04"
    assert product.canonical_measurement("green") == "B03"
    assert product.canonical_measurement("blue") == "B02"

    # check band2grid
    md: RasterCollectionMetadata = product._md  # type: ignore
    b2g = md.band2grid
    assert b2g["B02"] == "default"
    assert b2g["B01"] == "g60"
    assert set(b2g.values()) == set("default g20 g60".split(" "))

    # Check that we can use product derived this way on an Item
    item = sentinel_stac_ms_with_raster_ext.clone()

    ds = _item_to_ds(item, product)
    geobox = native_geobox(ds, basis="B02")
    assert geobox.shape == (10980, 10980)
    assert geobox.crs == "EPSG:32606"
    assert native_geobox(ds, basis="B01").shape == (1830, 1830)

    # Check unhappy path
    collection = sentinel_stac_collection.clone()
    item_assets = getattr(collection, "item_assets", None)
    if item_assets is not None:
        # newer pystac
        item_assets.clear()
    else:
        collection.stac_extensions.remove(ItemAssetsExtension.get_schema_uri())

    with pytest.raises(ValueError):
        infer_dc_product(collection)

    # Test bad overload
    with pytest.raises(TypeError):
        infer_dc_product([])


def test_infer_product_item(sentinel_stac_ms: pystac.item.Item) -> None:
    item = sentinel_stac_ms

    assert item.collection_id in STAC_CFG

    product = infer_dc_product(item, STAC_CFG)

    assert product.measurements["SCL"].dtype == "uint8"
    assert product.measurements["visual"].dtype == "uint8"
    # check aliases from eo extension
    assert product.canonical_measurement("red") == "B04"
    assert product.canonical_measurement("green") == "B03"
    assert product.canonical_measurement("blue") == "B02"
    # check aliases from config
    assert product.canonical_measurement("rededge1") == "B05"
    assert product.canonical_measurement("rededge2") == "B06"
    assert product.canonical_measurement("rededge3") == "B07"

    assert set(product._md.band2grid) == set(product.measurements)  # type: ignore

    _stac = dicttoolz.dissoc(sentinel_stac_ms.to_dict(), "collection")
    item_no_collection = pystac.item.Item.from_dict(_stac)
    assert item_no_collection.collection_id is None

    product = infer_dc_product(item_no_collection)


def test_infer_product_raster_ext(
    sentinel_stac_ms_with_raster_ext: pystac.item.Item,
) -> None:
    item = sentinel_stac_ms_with_raster_ext.clone()
    assert has_raster_ext(item) is True
    product = infer_dc_product(item)

    assert product.measurements["SCL"].dtype == "uint8"
    assert product.measurements["visual"].dtype == "uint8"
    assert product.measurements["visual_2"].dtype == "uint8"
    assert product.measurements["visual_2"].band == 2
    assert product.measurements["visual_3"].band == 3

    # check aliases from eo extension
    assert product.canonical_measurement("red") == "B04"
    assert product.canonical_measurement("green") == "B03"
    assert product.canonical_measurement("blue") == "B02"
    assert set(product._md.band2grid) | set(["visual_2", "visual_3"]) == set(  # type: ignore
        product.measurements
    )


def test_item_to_ds(sentinel_stac_ms: pystac.item.Item) -> None:
    item0 = sentinel_stac_ms
    item = item0.clone()

    assert item.collection_id in STAC_CFG

    product = infer_dc_product(item, STAC_CFG)
    ds = _item_to_ds(item, product)

    assert set(ds.measurements) == set(product.measurements)
    assert ds.crs is not None
    assert ds.metadata.lat is not None
    assert ds.metadata.lon is not None
    assert ds.center_time is not None

    # this checks property remap, without changing
    # key names .platform would be None
    assert ds.metadata.platform == "Sentinel-2B"

    dss = list(stac2ds(iter([item, item, item]), STAC_CFG))
    assert len(dss) == 3
    assert len({id(ds.product) for ds in dss}) == 1

    # Test missing band case
    item = item0.clone()
    item.assets.pop("B01")
    ds = _item_to_ds(item, product, STAC_CFG)

    # Test no eo extension case
    item = item0.clone()
    item.stac_extensions.remove(EOExtension.get_schema_uri())
    product = infer_dc_product(item, STAC_CFG)
    with pytest.raises(ValueError):
        product.canonical_measurement("green")

    # Test multiple CRS path
    item = item0.clone()
    ProjectionExtension.ext(item.assets["B01"]).epsg = 3857
    assert ProjectionExtension.ext(item.assets["B01"]).crs_string == "EPSG:3857"
    infer_dc_product(item, NO_WARN_CFG)


def test_item_to_ds_no_proj(sentinel_stac_ms: pystac.item.Item) -> None:
    item0 = sentinel_stac_ms
    item = item0.clone()
    item.stac_extensions.remove(ProjectionExtension.get_schema_uri())
    assert has_proj_ext(item) is False

    product = infer_dc_product(item, STAC_CFG)

    assert item.geometry is not None
    geom = Geometry(item.geometry, "EPSG:4326")
    ds = _item_to_ds(item, product, STAC_CFG)
    assert ds.crs == "EPSG:4326"
    assert ds.extent is not None
    assert ds.extent.contains(geom)
    assert native_geobox(ds).shape == (1, 1)


def test_item_uuid() -> None:
    item1 = mk_stac_item("id1", custom_property=1)
    item2 = mk_stac_item("id2")

    # Check determinism
    assert _compute_uuid(item1) == _compute_uuid(item1)
    assert _compute_uuid(item2) == _compute_uuid(item2)
    assert _compute_uuid(item1) != _compute_uuid(item2)

    # Check random case
    assert _compute_uuid(item1, "random").version == 4
    assert _compute_uuid(item1, "random") != _compute_uuid(item1, "random")

    # Check "native" mode
    _id = uuid.uuid4()
    assert _compute_uuid(mk_stac_item(str(_id)), "native") == _id
    assert _compute_uuid(mk_stac_item(str(_id)), "auto") == _id

    # Check that extras are used
    id1 = _compute_uuid(item1, extras=["custom_property", "missing_property"])
    id2 = _compute_uuid(item1)

    assert id1.version == 5
    assert id2.version == 5
    assert id1 != id2


def test_issue_n6(usgs_landsat_stac_v1: pystac.Item) -> None:
    expected_bands = {
        "blue",
        "coastal",
        "green",
        "nir08",
        "red",
        "swir16",
        "swir22",
        "qa_aerosol",
        "qa_pixel",
        "qa_radsat",
    }
    p = infer_dc_product(usgs_landsat_stac_v1)
    assert set(p.measurements) == expected_bands


def test_partial_proj(partial_proj_stac: pystac.Item) -> None:
    (ds,) = list(stac2ds([partial_proj_stac]))
    assert ds.metadata_doc["grids"]["default"]["shape"] == (1, 1)


def test_noassets_case(no_bands_stac: Any) -> None:
    (ds,) = stac2ds([no_bands_stac])
    assert len(ds.measurements) == 0


def test_old_imports() -> None:
    import odc.stac

    assert "stac2ds" in dir(odc.stac)
    assert "infer_dc_product" in dir(odc.stac)

    assert odc.stac.stac2ds is stac2ds
    assert odc.stac.infer_dc_product is infer_dc_product

    with pytest.raises(AttributeError):
        _ = odc.stac.no_such_thing


def test_product_cache(sentinel_stac_ms: pystac.item.Item) -> None:
    item = sentinel_stac_ms
    # simulate a product that was not created via infer_dc_product
    # (and therefore did not have the _md attr set)
    product = infer_dc_product(item, STAC_CFG)
    delattr(product, "_md")
    # make sure it doesn't error when product_cache is provided
    (ds,) = stac2ds([item], STAC_CFG, {product.name: product})
    assert ds.id
