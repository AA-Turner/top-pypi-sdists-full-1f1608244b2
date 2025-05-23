"""
Options Submodule
=================

Global or contextual options for xclim, similar to xarray.set_options.
"""

from __future__ import annotations

from collections.abc import Callable
from copy import deepcopy
from inspect import signature

from boltons.funcutils import wraps

from xclim.core._exceptions import ValidationError, raise_warn_or_log
from xclim.core.locales import _valid_locales

METADATA_LOCALES = "metadata_locales"
DATA_VALIDATION = "data_validation"
CF_COMPLIANCE = "cf_compliance"
CHECK_MISSING = "check_missing"
MISSING_OPTIONS = "missing_options"
RUN_LENGTH_UFUNC = "run_length_ufunc"
KEEP_ATTRS = "keep_attrs"
AS_DATASET = "as_dataset"
MAP_BLOCKS = "resample_map_blocks"

MISSING_METHODS: dict[str, Callable] = {}

OPTIONS = {
    METADATA_LOCALES: [],
    DATA_VALIDATION: "raise",
    CF_COMPLIANCE: "warn",
    CHECK_MISSING: "any",
    MISSING_OPTIONS: {},
    RUN_LENGTH_UFUNC: "auto",
    KEEP_ATTRS: "xarray",
    AS_DATASET: False,
    MAP_BLOCKS: False,
}

_LOUDNESS_OPTIONS = frozenset(["log", "warn", "raise"])
_RUN_LENGTH_UFUNC_OPTIONS = frozenset(["auto", True, False])
_KEEP_ATTRS_OPTIONS = frozenset(["xarray", True, False])


def _valid_missing_options(mopts):
    """Check if all methods and their options in mopts are valid."""
    return all(
        # Ensure the method is registered in MISSING_METHODS
        meth in MISSING_METHODS
        # Check if all options provided for the method are valid
        and all(opt in OPTIONS[MISSING_OPTIONS][meth] for opt in opts.keys())
        # Validate the options using the method's validator; defaults to True if no validation is needed
        and MISSING_METHODS[meth].validate(**(OPTIONS[MISSING_OPTIONS][meth] | opts))
        for meth, opts in mopts.items()  # Iterate over each method and its options in mopts
    )


_VALIDATORS = {
    METADATA_LOCALES: _valid_locales,
    DATA_VALIDATION: _LOUDNESS_OPTIONS.__contains__,
    CF_COMPLIANCE: _LOUDNESS_OPTIONS.__contains__,
    CHECK_MISSING: lambda meth: meth in MISSING_METHODS or meth == "skip",
    MISSING_OPTIONS: _valid_missing_options,
    RUN_LENGTH_UFUNC: _RUN_LENGTH_UFUNC_OPTIONS.__contains__,
    KEEP_ATTRS: _KEEP_ATTRS_OPTIONS.__contains__,
    AS_DATASET: lambda opt: isinstance(opt, bool),
    MAP_BLOCKS: lambda opt: isinstance(opt, bool),
}


def _set_missing_options(mopts):
    for meth, opts in mopts.items():
        OPTIONS[MISSING_OPTIONS][meth].update(**opts)


def _set_metadata_locales(locales):
    if isinstance(locales, str):
        OPTIONS[METADATA_LOCALES] = [locales]
    else:
        OPTIONS[METADATA_LOCALES] = locales


_SETTERS = {
    MISSING_OPTIONS: _set_missing_options,
    METADATA_LOCALES: _set_metadata_locales,
}


def register_missing_method(name: str) -> Callable:
    """
    Register missing method.

    Parameters
    ----------
    name : str
        Name of missing method.

    Returns
    -------
    Callable
        Decorator function.
    """

    def _register_missing_method(cls):
        sig = signature(cls.__init__)
        opts = {
            key: param.default if param.default != param.empty else None
            for key, param in sig.parameters.items()
            if key not in ["self"]
        }

        MISSING_METHODS[name] = cls
        OPTIONS[MISSING_OPTIONS][name] = opts
        return cls

    return _register_missing_method


def run_check(func, option, *args, **kwargs):
    r"""
    Run function and customize exception handling based on option.

    Parameters
    ----------
    func : Callable
        Function to run.
    option : str
        Option to use.
    *args : tuple
        Positional arguments to pass to the function.
    **kwargs : dict
        Keyword arguments to pass to the function.

    Raises
    ------
    ValidationError
        If the function raises a ValidationError and the option is set to "raise".
    """
    try:
        func(*args, **kwargs)
    except ValidationError as err:
        raise_warn_or_log(err, OPTIONS[option], stacklevel=4)


def datacheck(func: Callable) -> Callable:
    """
    Decorate functions checking data inputs validity.

    Parameters
    ----------
    func : Callable
        Function to decorate.

    Returns
    -------
    Callable
        Decorated function.
    """

    @wraps(func)
    def _run_check(*args, **kwargs):
        return run_check(func, DATA_VALIDATION, *args, **kwargs)

    return _run_check


def cfcheck(func: Callable) -> Callable:
    """
    Decorate functions checking CF-compliance of DataArray attributes.

    Functions should raise ValidationError exceptions whenever attributes are non-conformant.

    Parameters
    ----------
    func : Callable
        Function to decorate.

    Returns
    -------
    Callable
        Decorated function.
    """

    @wraps(func)
    def _run_check(*args, **kwargs):
        return run_check(func, CF_COMPLIANCE, *args, **kwargs)

    return _run_check


class set_options:  # numpydoc ignore=PR01,PR02
    r"""
    Set options for xclim in a controlled context.

    Parameters
    ----------
    metadata_locales : list[Any]
        List of IETF language tags or tuples of language tags and a translation dict, or
        tuples of language tags and a path to a json file defining translation of attributes.
        Default: ``[]``.
    data_validation : {"log", "raise", "error"}
        Whether to "log", "raise" an error or 'warn' the user on inputs that fail the data checks in
        :py:func:`xclim.core.datachecks`. Default: ``"raise"``.
    cf_compliance : {"log", "raise", "error"}
        Whether to "log", "raise" an error or "warn" the user on inputs that fail the CF compliance checks in
        :py:func:`xclim.core.cfchecks`. Default: ``"warn"``.
    check_missing : {"any", "wmo", "pct", "at_least_n", "skip"}
        How to check for missing data and flag computed indicators.
        Available methods are "any", "wmo", "pct", "at_least_n" and "skip".
        Missing method can be registered through the `xclim.core.options.register_missing_method` decorator.
        Default: ``"any"``
    missing_options : dict
        Dictionary of options to pass to the missing method. Keys must the name of
        missing method and values must be mappings from option names to values.
    run_length_ufunc : str
        Whether to use the 1D ufunc version of run length algorithms or the dask-ready broadcasting version.
        Default is ``"auto"``, which means the latter is used for dask-backed and large arrays.
    keep_attrs : bool or str
        Controls attributes handling in indicators. If True, attributes from all inputs are merged
        using the `drop_conflicts` strategy and then updated with xclim-provided attributes.
        If ``as_dataset`` is also True and a dataset was passed to the ``ds`` argument of the Indicator,
        the dataset's attributes are copied to the indicator's output.
        If False, attributes from the inputs are ignored.
        If "xarray", xclim will use xarray's `keep_attrs` option.
        Note that xarray's "default" is equivalent to False. Default: ``"xarray"``.
    as_dataset : bool
        If True, indicators output datasets. If False, they output DataArrays. Default :``False``.
    resample_map_blocks : bool
        If True, some indicators will wrap their resampling operations with `xr.map_blocks`,
        using :py:func:`xclim.indices.helpers.resample_map`.
        This requires `flox` to be installed in order to ensure the chunking is appropriate.

    Examples
    --------
    You can use ``set_options`` either as a context manager:

    >>> import xclim
    >>> ds = xr.open_dataset(path_to_tas_file).tas
    >>> with xclim.set_options(metadata_locales=["fr"]):
    ...     out = xclim.atmos.tg_mean(ds)

    Or to set global options:

    .. code-block:: python

        import xclim

        xclim.set_options(missing_options={"pct": {"tolerance": 0.04}})
    """

    def __init__(self, **kwargs):
        self.old = {}
        for k, v in kwargs.items():
            if k not in OPTIONS:
                msg = f"Argument name {k!r} is not in the set of valid options {set(OPTIONS)!r}."
                raise ValueError(msg)
            if k in _VALIDATORS and not _VALIDATORS[k](v):
                raise ValueError(f"option {k!r} given an invalid value: {v!r}")

            self.old[k] = deepcopy(OPTIONS[k])

        self._update(kwargs)

    def __enter__(self):
        """Context management."""
        return

    @staticmethod
    def _update(kwargs):
        """Update values."""
        for k, v in kwargs.items():
            if k in _SETTERS:
                _SETTERS[k](v)
            else:
                OPTIONS[k] = v

    def __exit__(self, option_type, value, traceback):  # noqa: F841
        """Context management."""
        self._update(self.old)
