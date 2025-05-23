"""
Compute Functions Submodule
===========================

Here are defined the functions wrapped by map_blocks or map_groups.
The user-facing, metadata-handling functions should be defined in processing.py.
"""

from __future__ import annotations

from collections.abc import Sequence

import numpy as np
import xarray as xr

from . import nbutils as nbu
from .base import Grouper, map_groups
from .utils import ADDITIVE, apply_correction, ecdf, invert, rank


@map_groups(
    sim_ad=[Grouper.ADD_DIMS, Grouper.DIM], pth=[Grouper.PROP], dP0=[Grouper.PROP]
)
def _adapt_freq(
    ds: xr.Dataset,
    *,
    dim: Sequence[str],
    thresh: float = 0,
) -> xr.Dataset:
    r"""
    Adapt frequency of values under thresh of `sim`, in order to match ref.

    This is the compute function, see :py:func:`xclim.sdba.processing.adapt_freq` for the user-facing function.

    Parameters
    ----------
    ds : xr.Dataset
        With variables :  "ref", Target/reference data, usually observed data and "sim", Simulated data.
    dim : str, or sequence of strings
        Dimension name(s). If more than one, the probabilities and quantiles are computed within all the dimensions.
        If `window` is in the names, it is removed before the correction
        and the final timeseries is corrected along dim[0] only.
    group : Union[str, Grouper]
        Grouping information, see base.Grouper
    thresh : float
        Threshold below which values are considered zero.

    Returns
    -------
    xr.Dataset, with the following variables:

      - `sim_adj`: Simulated data with the same frequency of values under threshold than ref.
        Adjustment is made group-wise.
      - `pth` : For each group, the smallest value of sim that was not frequency-adjusted. All values smaller were
        either left as zero values or given a random value between thresh and pth.
        NaN where frequency adaptation wasn't needed.
      - `dP0` : For each group, the percentage of values that were corrected in sim.
    """
    # Compute the probability of finding a value <= thresh
    # This is the "dry-day frequency" in the precipitation case
    P0_sim = ecdf(ds.sim, thresh, dim=dim)
    P0_ref = ecdf(ds.ref, thresh, dim=dim)

    # The proportion of values <= thresh in sim that need to be corrected, compared to ref
    dP0 = (P0_sim - P0_ref) / P0_sim

    if dP0.isnull().all():
        # All NaN slice.
        pth = dP0.copy()
        sim_ad = ds.sim.copy()
    else:
        # Compute : ecdf_ref^-1( ecdf_sim( thresh ) )
        # The value in ref with the same rank as the first non-zero value in sim.
        # pth is meaningless when freq. adaptation is not needed
        pth = nbu.vecquantiles(ds.ref, P0_sim, dim).where(dP0 > 0)

        # Probabilities and quantiles computed within all dims, but correction along the first one only.
        sim = ds.sim
        # Get the percentile rank of each value in sim.
        rnk = rank(sim, dim=dim, pct=True)

        # Frequency-adapted sim
        sim_ad = sim.where(
            dP0 < 0,  # dP0 < 0 means no-adaptation.
            sim.where(
                (rnk < P0_ref) | (rnk > P0_sim),  # Preserve current values
                # Generate random numbers ~ U[T0, Pth]
                (pth.broadcast_like(sim) - thresh)
                * np.random.random_sample(size=sim.shape)
                + thresh,
            ),
        )

    # Tell group_apply that these will need reshaping (regrouping)
    # This is needed since if any variable comes out a `groupby` with the original group axis,
    # the whole output is broadcasted back to the original dims.
    pth.attrs["_group_apply_reshape"] = True
    dP0.attrs["_group_apply_reshape"] = True
    return xr.Dataset(data_vars={"pth": pth, "dP0": dP0, "sim_ad": sim_ad})


@map_groups(
    reduces=[Grouper.DIM, Grouper.PROP], data=[Grouper.DIM], norm=[Grouper.PROP]
)
def _normalize(
    ds: xr.Dataset,
    *,
    dim: Sequence[str],
    kind: str = ADDITIVE,
) -> xr.Dataset:
    """
    Normalize an array by removing its mean.

    Parameters
    ----------
    ds : xr.Dataset
        The variable `data` is normalized.
        If a `norm` variable is present, is uses this one instead of computing the norm again.
    group : Union[str, Grouper]
        Grouping information. See :py:class:`xclim.sdba.base.Grouper` for details.
    dim : sequence of strings
        Dimension name(s).
    kind : {'+', '*'}
        How to apply the adjustment, using either additive or multiplicative methods.

    Returns
    -------
    xr.Dataset
        Group-wise anomaly of x

    Notes
    -----
    Normalization is performed group-wise.
    """
    if "norm" in ds:
        norm = ds.norm
    else:
        norm = ds.data.mean(dim=dim)
    norm.attrs["_group_apply_reshape"] = True

    return xr.Dataset(
        {"data": apply_correction(ds.data, invert(norm, kind), kind), "norm": norm}
    )


@map_groups(reordered=[Grouper.DIM], main_only=False)
def _reordering(ds: xr.Dataset, *, dim: str) -> xr.Dataset:
    """
    Group-wise reordering.

    Parameters
    ----------
    ds : xr.Dataset
        With variables:
            - sim : The timeseries to reorder.
            - ref : The timeseries whose rank to use.
    dim : str
        The dimension along which to reorder.

    Returns
    -------
    xr.Dataset
        The reordered timeseries.
    """

    def _reordering_1d(data, ordr):
        return np.sort(data)[np.argsort(np.argsort(ordr))]

    def _reordering_2d(data, ordr):
        data_r = data.ravel()
        ordr_r = ordr.ravel()
        reorder = np.sort(data_r)[np.argsort(np.argsort(ordr_r))]
        return reorder.reshape(data.shape)[
            :, int(data.shape[1] / 2)
        ]  # pick the middle of the window

    if {"window", "time"} == set(dim):
        return (
            xr.apply_ufunc(
                _reordering_2d,
                ds.sim,
                ds.ref,
                input_core_dims=[["time", "window"], ["time", "window"]],
                output_core_dims=[["time"]],
                vectorize=True,
                dask="parallelized",
                output_dtypes=[ds.sim.dtype],
            )
            .rename("reordered")
            .to_dataset()
        )

    if len(dim) == 1:
        return (
            xr.apply_ufunc(
                _reordering_1d,
                ds.sim,
                ds.ref,
                input_core_dims=[dim, dim],
                output_core_dims=[dim],
                vectorize=True,
                dask="parallelized",
                output_dtypes=[ds.sim.dtype],
            )
            .rename("reordered")
            .to_dataset()
        )

    raise ValueError(
        f"Reordering can only be done along one dimension. "
        f"If there is more than one, they should be `window` and `time`. "
        f"The dimensions are {dim}."
    )
