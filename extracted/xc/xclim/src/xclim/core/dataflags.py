"""
Data Flags
==========

Pseudo-indicators designed to analyse supplied variables for suspicious/erroneous indicator values.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence
from functools import reduce
from inspect import signature
from typing import Literal

import numpy as np
import xarray

from xclim.core._exceptions import MissingVariableError, raise_warn_or_log
from xclim.core._types import VARIABLES, Quantified
from xclim.core.calendar import climatological_mean_doy, within_bnds_doy
from xclim.core.formatting import update_xclim_history
from xclim.core.units import convert_units_to, declare_units, infer_context, str2pint
from xclim.core.utils import InputKind, infer_kind_from_parameter
from xclim.indices.generic import binary_ops
from xclim.indices.run_length import suspicious_run

_REGISTRY = {}

ALL_OPERATORS = Literal[">", "gt", "<", "lt", ">=", "ge", "<=", "le", "==", "eq", "!=", "ne"]


class DataQualityException(Exception):
    """
    Raised when any data evaluation checks are flagged as `True`.

    Parameters
    ----------
    flag_array : xarray.Dataset
        Xarray.Dataset of Data Flags.
    message : str
        Message prepended to the error messages.
    """

    flag_array: xarray.Dataset | None = None

    def __init__(
        self,
        flag_array: xarray.Dataset,
        message="Data quality flags indicate suspicious values. Flags raised are:\n  - ",
    ):
        self.message = message
        self.flags = []
        for value in flag_array.data_vars.values():
            if value.any():
                for attribute in value.attrs.keys():
                    if str(attribute) == "description":
                        self.flags.append(value.attrs[attribute])
        super().__init__(self.message)

    def __str__(self):
        """Format the errors for history."""
        nl = "\n  - "
        return f"{self.message}{nl.join(self.flags)}"


__all__ = [
    "DataQualityException",
    "data_flags",
    "ecad_compliant",
    "negative_accumulation_values",
    "outside_n_standard_deviations_of_climatology",
    "percentage_values_outside_of_bounds",
    "register_methods",
    "tas_below_tasmin",
    "tas_exceeds_tasmax",
    "tasmax_below_tasmin",
    "temperature_extremely_high",
    "temperature_extremely_low",
    "values_op_thresh_repeating_for_n_or_more_days",
    "values_repeating_for_n_or_more_days",
    "very_large_precipitation_events",
    "wind_values_outside_of_bounds",
]


def register_methods(variable_name: str | None = None) -> Callable:
    """
    Register a data flag as functional.

    Argument can be the output variable name template. The template may use any of the string-like input arguments.
    If not given, the function name is used instead, which may create variable conflicts.

    Parameters
    ----------
    variable_name : str, optional
        The output variable name template. Default is `None`.

    Returns
    -------
    callable
        The function being registered.
    """

    def _register_methods(func):
        """Summarize all methods used in dataflags checks."""
        func.__dict__["variable_name"] = variable_name or func.__name__
        _REGISTRY[func.__name__] = func
        return func

    return _register_methods


def _sanitize_attrs(da: xarray.DataArray) -> xarray.DataArray:
    to_remove = []
    for attr in da.attrs.keys():
        if str(attr) != "history":
            to_remove.append(attr)
    for attr in to_remove:
        del da.attrs[attr]
    return da


@register_methods()
@update_xclim_history
@declare_units(tasmax="[temperature]", tasmin="[temperature]")
def tasmax_below_tasmin(
    tasmax: xarray.DataArray,
    tasmin: xarray.DataArray,
) -> xarray.DataArray:
    """
    Check if tasmax values are below tasmin values for any given day.

    Parameters
    ----------
    tasmax : xarray.DataArray
        Maximum temperature.
    tasmin : xarray.DataArray
        Minimum temperature.

    Returns
    -------
    xarray.DataArray, [bool]
        Boolean array of True where tasmax is below tasmin.

    Examples
    --------
    To gain access to the flag_array:

    >>> from xclim.core.dataflags import tasmax_below_tasmin
    >>> ds = xr.open_dataset(path_to_tas_file)
    >>> flagged = tasmax_below_tasmin(ds.tasmax, ds.tasmin)
    """
    tasmax_lt_tasmin = _sanitize_attrs(tasmax < tasmin)
    description = "Maximum temperature values found below minimum temperatures."
    tasmax_lt_tasmin.attrs["description"] = description
    tasmax_lt_tasmin.attrs["units"] = ""
    return tasmax_lt_tasmin


@register_methods()
@update_xclim_history
@declare_units(tas="[temperature]", tasmax="[temperature]")
def tas_exceeds_tasmax(
    tas: xarray.DataArray,
    tasmax: xarray.DataArray,
) -> xarray.DataArray:
    """
    Check if tas values tasmax values for any given day.

    Parameters
    ----------
    tas : xarray.DataArray
        Mean temperature.
    tasmax : xarray.DataArray
        Maximum temperature.

    Returns
    -------
    xarray.DataArray, [bool]
        Boolean array of True where tas is above tasmax.

    Examples
    --------
    To gain access to the flag_array:

    >>> from xclim.core.dataflags import tas_exceeds_tasmax
    >>> ds = xr.open_dataset(path_to_tas_file)
    >>> flagged = tas_exceeds_tasmax(ds.tas, ds.tasmax)
    """
    tas_gt_tasmax = _sanitize_attrs(tas > tasmax)
    description = "Mean temperature values found above maximum temperatures."
    tas_gt_tasmax.attrs["description"] = description
    tas_gt_tasmax.attrs["units"] = ""
    return tas_gt_tasmax


@register_methods()
@update_xclim_history
@declare_units(tas="[temperature]", tasmin="[temperature]")
def tas_below_tasmin(tas: xarray.DataArray, tasmin: xarray.DataArray) -> xarray.DataArray:
    """
    Check if tas values are below tasmin values for any given day.

    Parameters
    ----------
    tas : xarray.DataArray
        Mean temperature.
    tasmin : xarray.DataArray
        Minimum temperature.

    Returns
    -------
    xarray.DataArray, [bool]
        Boolean array of True where tas is below tasmin.

    Examples
    --------
    To gain access to the flag_array:

    >>> from xclim.core.dataflags import tas_below_tasmin
    >>> ds = xr.open_dataset(path_to_tas_file)
    >>> flagged = tas_below_tasmin(ds.tas, ds.tasmin)
    """
    tas_lt_tasmin = _sanitize_attrs(tas < tasmin)
    description = "Mean temperature values found below minimum temperatures."
    tas_lt_tasmin.attrs["description"] = description
    tas_lt_tasmin.attrs["units"] = ""
    return tas_lt_tasmin


@register_methods()
@update_xclim_history
@declare_units(da="[temperature]", thresh="[temperature]")
def temperature_extremely_low(da: xarray.DataArray, *, thresh: Quantified = "-90 degC") -> xarray.DataArray:
    """
    Check if temperature values are below -90 degrees Celsius for any given day.

    Parameters
    ----------
    da : xarray.DataArray
        Temperature.
    thresh : str
        Threshold below which temperatures are considered problematic and a flag is raised.
        Default is -90 degrees Celsius.

    Returns
    -------
    xarray.DataArray, [bool]
        Boolean array of True where temperatures are below the threshold.

    Examples
    --------
    To gain access to the flag_array:

    >>> from xclim.core.dataflags import temperature_extremely_low
    >>> ds = xr.open_dataset(path_to_tas_file)
    >>> temperature = "-90 degC"
    >>> flagged = temperature_extremely_low(ds.tas, thresh=temperature)
    """
    thresh_converted = convert_units_to(thresh, da)
    extreme_low = _sanitize_attrs(da < thresh_converted)
    description = f"Temperatures found below {thresh} in {da.name}."
    extreme_low.attrs["description"] = description
    extreme_low.attrs["units"] = ""
    return extreme_low


@register_methods()
@update_xclim_history
@declare_units(da="[temperature]", thresh="[temperature]")
def temperature_extremely_high(da: xarray.DataArray, *, thresh: Quantified = "60 degC") -> xarray.DataArray:
    """
    Check if temperature values exceed 60 degrees Celsius for any given day.

    Parameters
    ----------
    da : xarray.DataArray
        Temperature.
    thresh : str
        Threshold above which temperatures are considered problematic and a flag is raised.
        Default is 60 degrees Celsius.

    Returns
    -------
    xarray.DataArray, [bool]
        Boolean array of True where temperatures are above the threshold.

    Examples
    --------
    To gain access to the flag_array:

    >>> from xclim.core.dataflags import temperature_extremely_high
    >>> ds = xr.open_dataset(path_to_tas_file)
    >>> temperature = "60 degC"
    >>> flagged = temperature_extremely_high(ds.tas, thresh=temperature)
    """
    thresh_converted = convert_units_to(thresh, da)
    extreme_high = _sanitize_attrs(da > thresh_converted)
    description = f"Temperatures found in excess of {thresh} in {da.name}."
    extreme_high.attrs["description"] = description
    extreme_high.attrs["units"] = ""
    return extreme_high


@register_methods()
@update_xclim_history
def negative_accumulation_values(
    da: xarray.DataArray,
) -> xarray.DataArray:
    """
    Check if variable values are negative for any given day.

    Parameters
    ----------
    da : xarray.DataArray
        Variable array.

    Returns
    -------
    xarray.DataArray, [bool]
        Boolean array of True where values are negative.

    Examples
    --------
    To gain access to the flag_array:

    >>> from xclim.core.dataflags import negative_accumulation_values
    >>> ds = xr.open_dataset(path_to_pr_file)
    >>> flagged = negative_accumulation_values(ds.pr)
    """
    negative_accumulations = _sanitize_attrs(da < 0)
    description = f"Negative values found for {da.name}."
    negative_accumulations.attrs["description"] = description
    negative_accumulations.attrs["units"] = ""
    return negative_accumulations


@register_methods()
@update_xclim_history
@declare_units(da="[precipitation]", thresh="[precipitation]")
def very_large_precipitation_events(da: xarray.DataArray, *, thresh: Quantified = "300 mm d-1") -> xarray.DataArray:
    """
    Check if precipitation values exceed 300 mm/day for any given day.

    Parameters
    ----------
    da : xarray.DataArray
        Precipitation.
    thresh : str
        Threshold to search an array for that will trigger flag if any day exceeds value.

    Returns
    -------
    xarray.DataArray, [bool]
        Boolean array of True where precipitation values exceed the threshold.

    Examples
    --------
    To gain access to the flag_array:

    >>> from xclim.core.dataflags import very_large_precipitation_events
    >>> ds = xr.open_dataset(path_to_pr_file)
    >>> rate = "300 mm d-1"
    >>> flagged = very_large_precipitation_events(ds.pr, thresh=rate)
    """
    thresh_converted = convert_units_to(thresh, da, context="hydro")
    very_large_events = _sanitize_attrs(da > thresh_converted)
    description = f"Precipitation events in excess of {thresh} for {da.name}."
    very_large_events.attrs["description"] = description
    very_large_events.attrs["units"] = ""
    return very_large_events


@register_methods("values_{op}_{thresh}_repeating_for_{n}_or_more_days")
@update_xclim_history
def values_op_thresh_repeating_for_n_or_more_days(
    da: xarray.DataArray, *, n: int, thresh: Quantified, op: ALL_OPERATORS = "=="
) -> xarray.DataArray:
    """
    Check if array values repeat at a given threshold for `N` or more days.

    Parameters
    ----------
    da : xarray.DataArray
        Variable array.
    n : int
        Number of repeating days needed to trigger data flag.
    thresh : str
        Repeating values to search for that will trigger data flag.
    op : {">", "gt", "<", "lt", ">=", "ge", "<=", "le", "==", "eq", "!=", "ne"}
        Operator used for comparison with thresh.

    Returns
    -------
    xarray.DataArray, [bool]
        Boolean array of True where values repeat at threshold for `N` or more days.

    Examples
    --------
    To gain access to the flag_array:

    >>> from xclim.core.dataflags import values_op_thresh_repeating_for_n_or_more_days
    >>> ds = xr.open_dataset(path_to_pr_file)
    >>> units = "5 mm d-1"
    >>> days = 5
    >>> comparison = "eq"
    >>> flagged = values_op_thresh_repeating_for_n_or_more_days(ds.pr, n=days, thresh=units, op=comparison)
    """
    thresh = convert_units_to(thresh, da, context=infer_context(standard_name=da.attrs.get("standard_name")))

    repetitions = _sanitize_attrs(suspicious_run(da, window=n, op=op, thresh=thresh))
    description = f"Repetitive values at {thresh} for at least {n} days found for {da.name}."
    repetitions.attrs["description"] = description
    repetitions.attrs["units"] = ""
    return repetitions


@register_methods()
@update_xclim_history
@declare_units(da="[speed]", lower="[speed]", upper="[speed]")
def wind_values_outside_of_bounds(
    da: xarray.DataArray,
    *,
    lower: Quantified = "0 m s-1",
    upper: Quantified = "46 m s-1",
) -> xarray.DataArray:
    """
    Check if wind speed values exceed reasonable bounds for any given day.

    Parameters
    ----------
    da : xarray.DataArray
        Wind speed.
    lower : str
        The lower limit for wind speed. Default is 0 m s-1.
    upper : str
        The upper limit for wind speed. Default is 46 m s-1.

    Returns
    -------
    xarray.DataArray, [bool]
        The boolean array of True where values exceed the bounds.

    Examples
    --------
    To gain access to the flag_array:

    >>> from xclim.core.dataflags import wind_values_outside_of_bounds
    >>> ceiling, floor = "46 m s-1", "0 m s-1"
    >>> flagged = wind_values_outside_of_bounds(sfcWind_dataset, upper=ceiling, lower=floor)
    """
    lower, upper = convert_units_to(lower, da), convert_units_to(upper, da)
    unbounded_percentages = _sanitize_attrs((da < lower) | (da > upper))
    description = f"Percentage values exceeding bounds of {lower} and {upper} found for {da.name}."
    unbounded_percentages.attrs["description"] = description
    unbounded_percentages.attrs["units"] = ""
    return unbounded_percentages


# TODO: 'Many excessive dry days' = the amount of dry days lies outside a 14·bivariate standard deviation


@register_methods("outside_{n}_standard_deviations_of_climatology")
@update_xclim_history
def outside_n_standard_deviations_of_climatology(
    da: xarray.DataArray,
    *,
    n: int,
    window: int = 5,
) -> xarray.DataArray:
    """
    Check if any daily value is outside `n` standard deviations from the day of year mean.

    Parameters
    ----------
    da : xarray.DataArray
        Variable array.
    n : int
        Number of standard deviations.
    window : int
        Moving window used in determining the climatological mean. Default: `5`.

    Returns
    -------
    xarray.DataArray, [bool]
        The boolean array of True where values exceed the bounds.

    Notes
    -----
    A moving window of five (5) days is suggested for `tas` data flag calculations according to
    ICCLIM data quality standards.

    References
    ----------
    :cite:cts:`project_team_eca&d_algorithm_2013`

    Examples
    --------
    To gain access to the flag_array:

    >>> from xclim.core.dataflags import outside_n_standard_deviations_of_climatology
    >>> ds = xr.open_dataset(path_to_tas_file)
    >>> std_devs = 5
    >>> average_over = 5
    >>> flagged = outside_n_standard_deviations_of_climatology(ds.tas, n=std_devs, window=average_over)
    """
    mu, sig = climatological_mean_doy(da, window=window)
    within_bounds = _sanitize_attrs(within_bnds_doy(da, high=(mu + n * sig), low=(mu - n * sig)))
    description = (
        f"Values outside of {n} standard deviations from climatology found for {da.name} "
        f"with moving window of {window} days."
    )
    within_bounds.attrs["description"] = description
    within_bounds.attrs["units"] = ""
    return ~within_bounds


@register_methods("values_repeating_for_{n}_or_more_days")
@update_xclim_history
def values_repeating_for_n_or_more_days(da: xarray.DataArray, *, n: int) -> xarray.DataArray:
    """
    Check if exact values are found to be repeating for at least 5 or more days.

    Parameters
    ----------
    da : xarray.DataArray
        Variable array.
    n : int
        Number of days to trigger flag.

    Returns
    -------
    xarray.DataArray, [bool]
        The boolean array of True where values repeat for `n` or more days.

    Examples
    --------
    To gain access to the flag_array:

    >>> from xclim.core.dataflags import values_repeating_for_n_or_more_days
    >>> ds = xr.open_dataset(path_to_pr_file)
    >>> flagged = values_repeating_for_n_or_more_days(ds.pr, n=5)
    """
    repetition = _sanitize_attrs(suspicious_run(da, window=n))
    description = f"Runs of repetitive values for {n} or more days found for {da.name}."
    repetition.attrs["description"] = description
    repetition.attrs["units"] = ""
    return repetition


@register_methods()
@update_xclim_history
def percentage_values_outside_of_bounds(da: xarray.DataArray) -> xarray.DataArray:
    """
    Check if variable values fall below 0% or exceed 100% for any given day.

    Parameters
    ----------
    da : xarray.DataArray
        Variable array.

    Returns
    -------
    xarray.DataArray, [bool]
        The boolean array of True where values exceed the bounds.

    Examples
    --------
    To gain access to the flag_array:

    >>> from xclim.core.dataflags import percentage_values_outside_of_bounds
    >>> flagged = percentage_values_outside_of_bounds(huss_dataset)
    """
    unbounded_percentages = _sanitize_attrs((da < 0) | (da > 100))
    description = f"Percentage values beyond bounds found for {da.name}."
    unbounded_percentages.attrs["description"] = description
    return unbounded_percentages


def data_flags(  # noqa: C901
    da: xarray.DataArray,
    ds: xarray.Dataset | None = None,
    flags: dict | None = None,
    dims: None | str | Sequence[str] = "all",
    freq: str | None = None,
    raise_flags: bool = False,
) -> xarray.Dataset:
    """
    Evaluate the supplied DataArray for a set of data flag checks.

    Test triggers depend on variable name and availability of extra variables within Dataset for comparison.
    If called with `raise_flags=True`, will raise a DataQualityException with comments for each failed quality check.

    Parameters
    ----------
    da : xarray.DataArray
        The variable to check.
        Must have a name that is a valid CMIP6 variable name and appears in :py:obj:`xclim.core.utils.VARIABLES`.
    ds : xarray.Dataset, optional
        An optional dataset with extra variables needed by some checks.
    flags : dict, optional
        A dictionary where the keys are the name of the flags to check and the values are parameter dictionaries.
        The value can be None if there are no parameters to pass (i.e. default will be used).
        The default, None, means that the data flags list will be taken from :py:obj:`xclim.core.utils.VARIABLES`.
    dims : {"all", None} or str or a sequence of strings
        Dimensions upon which the aggregation should be performed. Default: "all".
    freq : str, optional
        Resampling frequency to have data_flags aggregated over periods.
        Defaults to None, which means the "time" axis is treated as any other dimension (see `dims`).
    raise_flags : bool
        Raise exception if any of the quality assessment flags are raised. Default: False.

    Returns
    -------
    xarray.Dataset
        The Dataset of boolean flag arrays.

    Examples
    --------
    To evaluate all applicable data flags for a given variable:

    >>> from xclim.core.dataflags import data_flags
    >>> ds = xr.open_dataset(path_to_pr_file)
    >>> flagged_multi = data_flags(ds.pr, ds)
    >>> # The next example evaluates only one data flag, passing specific parameters. It also aggregates the flags
    >>> # yearly over the "time" dimension only, such that a True means there is a bad data point for that year
    >>> # at that location.
    >>> flagged_single = data_flags(
    ...     ds.pr,
    ...     ds,
    ...     flags={"very_large_precipitation_events": {"thresh": "250 mm d-1"}},
    ...     dims=None,
    ...     freq="YS",
    ... )
    """

    def _get_variable_name(function, _kwargs):
        format_args = {}
        _kwargs = _kwargs or {}
        for arg, param in signature(function).parameters.items():
            val = _kwargs.get(arg, param.default)
            kind = infer_kind_from_parameter(param)
            if arg == "op":
                format_args[arg] = val if val not in binary_ops else binary_ops[val]
            elif kind in [
                InputKind.FREQ_STR,
                InputKind.NUMBER,
                InputKind.STRING,
                InputKind.DAY_OF_YEAR,
                InputKind.DATE,
                InputKind.BOOL,
            ]:
                format_args[arg] = val
            elif kind == InputKind.QUANTIFIED:
                if isinstance(val, xarray.DataArray):
                    format_args[arg] = "array"
                else:
                    val = str2pint(val).magnitude
                    if val == int(val):
                        val = str(int(val))
                    else:
                        val = str(val).replace(".", "point")
                    val = val.replace("-", "minus")
                    format_args[arg] = str(val)
        return function.variable_name.format(**format_args)

    def _missing_vars(function, dataset: xarray.Dataset, var_provided: str):
        """Handle missing variables in passed datasets."""
        sig = signature(function)
        sig_params = sig.parameters
        extra_vars = {}
        for arg, val in sig_params.items():
            if arg in ["da", var_provided]:
                continue
            kind = infer_kind_from_parameter(val)
            if kind in [InputKind.VARIABLE]:
                if arg in dataset:
                    extra_vars[arg] = dataset[arg]
                else:
                    raise MissingVariableError()
        return extra_vars

    var = str(da.name)
    if dims == "all":
        dims = da.dims
    elif isinstance(dims, str):
        # Thus, a single dimension name, we allow this option to mirror xarray.
        dims = {dims}
    if freq is not None and dims is not None:
        dims = (set(dims) - {"time"}) or None  # Will return None if the only dimension was "time".

    if flags is None:
        try:
            flag_funcs = VARIABLES.get(var)["data_flags"]
        except (KeyError, TypeError) as err:
            raise_warn_or_log(
                err,
                mode="raise" if raise_flags else "log",
                msg=f"Data quality checks do not exist for '{var}' variable.",
                err_type=NotImplementedError,
            )
            return xarray.Dataset()
    else:
        flag_funcs = [flags]

    ds = ds or xarray.Dataset()

    flags = {}
    for flag_func in flag_funcs:
        for name, kwargs in flag_func.items():
            func = _REGISTRY[name]
            variable_name = _get_variable_name(func, kwargs)
            named_da_variable = None

            try:
                extras = _missing_vars(func, ds, str(da.name))
                # Entries in extras implies that there are two variables being compared
                # Both variables will be sent in as dict entries
                if extras:
                    named_da_variable = {da.name: da}

            except MissingVariableError:
                flags[variable_name] = None
            else:
                with xarray.set_options(keep_attrs=True):
                    if named_da_variable:
                        out = func(**named_da_variable, **extras, **(kwargs or {}))
                    else:
                        out = func(da, **extras, **(kwargs or {}))

                    # Aggregation
                    if freq is not None:
                        out = out.resample(time=freq).any()
                    if dims is not None:
                        out = out.any(dims)

                flags[variable_name] = out

    ds_flags = xarray.Dataset(data_vars=flags)

    if raise_flags:
        if np.any([ds_flags[dv] for dv in ds_flags.data_vars]):
            raise DataQualityException(ds_flags)

    return ds_flags


def ecad_compliant(
    ds: xarray.Dataset,
    dims: None | str | Sequence[str] = "all",
    raise_flags: bool = False,
    append: bool = True,
) -> xarray.DataArray | xarray.Dataset | None:
    """
    Run ECAD compliance tests.

    Assert that file adheres to ECAD-based quality assurance checks.

    Parameters
    ----------
    ds : xarray.Dataset
        Variable-containing dataset.
    dims : {"all"} or str or a sequence of strings, optional
        Dimensions upon which aggregation should be performed. Default: ``"all"``.
    raise_flags : bool
        Raise exception if any of the quality assessment flags are raised, otherwise returns None. Default: ``False``.
    append : bool
        If `True`, return the Dataset with the `ecad_qc_flag` array appended to data_vars.
        If `False`, return the DataArray of the `ecad_qc_flag` variable.

    Returns
    -------
    xarray.DataArray or xarray.Dataset or None
        Flag array or Dataset with flag array(s) appended.
    """
    flags = xarray.Dataset()
    history: list[str] = []
    for var in ds.data_vars:
        df = data_flags(ds[var], ds, dims=dims)
        for flag_name, flag_data in df.data_vars.items():
            flags = flags.assign({f"{var}_{flag_name}": flag_data})

            if "history" in flag_data.attrs.keys() and np.all(flag_data.values) is not None:
                # The extra `split("\n") should be removed when merge_attributes(missing_str=None)
                history_elems = flag_data.attrs["history"].split("\n")[-1].split(" ")
                if not history:
                    history.append(
                        " ".join(
                            [
                                " ".join(history_elems[0:2]),
                                " ".join(history_elems[-4:]),
                                "- Performed the following checks:",
                            ]
                        )
                    )
                history.append(" ".join(history_elems[3:-4]))

    if raise_flags:
        if np.any([flags[dv] for dv in flags.data_vars]):
            raise DataQualityException(flags)
        return None

    ecad_flag = xarray.DataArray(
        # TODO: Test for this change concerning data of type None in dataflag variables
        ~reduce(
            np.logical_or,
            filter(lambda x: x.dtype == bool, flags.data_vars.values()),  # noqa
        ),
        name="ecad_qc_flag",
        attrs={
            "comment": "Adheres to ECAD quality control checks.",
            "history": "\n".join(history),
        },
    )

    if append:
        return xarray.merge([ds, ecad_flag])
    return ecad_flag
