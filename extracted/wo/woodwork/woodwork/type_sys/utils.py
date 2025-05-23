import pandas as pd
from dateutil.parser import ParserError

import woodwork as ww


def col_is_datetime(col, datetime_format=None):
    """Determine if a dataframe column contains datetime values or not. Returns True if column
    contains datetimes, False if not. Optionally specify the datetime format string for the column.
    Will not infer numeric data as datetime."""

    if pd.api.types.is_datetime64_any_dtype(col):
        return True

    col = col.dropna()
    if len(col) == 0:
        return False

    try:
        if pd.api.types.is_numeric_dtype(pd.Series(col.values.tolist())):
            return False
    except AttributeError:
        # given our current minimum dependencies (pandas 1.3.0 and pyarrow 4.0.1)
        # if we have a string dtype series, calling `col.values.tolist()` throws an error
        # AttributeError: 'StringArray' object has no attribute 'tolist'
        # this try/except block handles that, among other potential issues for experimental dtypes
        # until we find a more appropriate solution
        pass

    col = col.astype(str)

    try:
        pd.to_datetime(
            col,
            errors="raise",
            format=datetime_format,
        )
        return True

    except (ParserError, ValueError, OverflowError, TypeError):
        return False


def _is_numeric_series(series, logical_type):
    """Determines whether a series will be considered numeric
    for the purposes of determining if it can be a time_index."""
    # If column can't be made to be numeric, don't bother checking Logical Type
    try:
        pd.to_numeric(series, errors="raise")
    except (ValueError, TypeError):
        return False

    if logical_type is not None:
        if isinstance(logical_type, str):
            logical_type = ww.type_system.str_to_logical_type(logical_type)

        # Allow numeric columns to be interpreted as Datetimes - doesn't allow strings even if they could be numeric
        if _get_ltype_class(
            logical_type,
        ) == ww.logical_types.Datetime and pd.api.types.is_numeric_dtype(series):
            return True
    else:
        logical_type = ww.type_system.infer_logical_type(series)

    return "numeric" in logical_type.standard_tags


def list_logical_types():
    """Returns a dataframe describing all of the available Logical Types.

    Args:
        None

    Returns:
        pd.DataFrame: A dataframe containing details on each LogicalType, including
        the corresponding physical type and any standard semantic tags.
    """
    ltypes_df = pd.DataFrame(
        [
            {
                "name": ltype.__name__,
                "type_string": ltype.type_string,
                "description": ltype.__doc__,
                "physical_type": ltype.primary_dtype,
                "standard_tags": ltype.standard_tags,
                "is_default_type": ltype in ww.type_system._default_inference_functions,
                "is_registered": ltype in ww.type_system.registered_types,
                "parent_type": ww.type_system._get_parent(ltype),
            }
            for ltype in ww.logical_types.LogicalType.__subclasses__()
        ],
    )
    return ltypes_df.sort_values("name").reset_index(drop=True)


def list_semantic_tags():
    """Returns a dataframe describing all of the common semantic tags.

    Args:
        None

    Returns:
        pd.DataFrame: A dataframe containing details on each Semantic Tag, including
        the corresponding logical type(s).
    """
    sem_tags = {}
    for ltype in ww.type_system.registered_types:
        for tag in ltype.standard_tags:
            if tag in sem_tags:
                sem_tags[tag].append(ltype)
            else:
                sem_tags[tag] = [ltype]
    tags_df = pd.DataFrame(
        [
            {"name": tag, "is_standard_tag": True, "valid_logical_types": sem_tags[tag]}
            for tag in sem_tags
        ],
    )
    temp_df = pd.DataFrame(
        [
            ["index", False, "Any LogicalType"],
            [
                "time_index",
                False,
                [ww.type_system.str_to_logical_type("datetime")] + sem_tags["numeric"],
            ],
            [
                "date_of_birth",
                False,
                [ww.type_system.str_to_logical_type("datetime")],
            ],
            ["ignore", False, "Any LogicalType"],
            ["passthrough", False, "Any LogicalType"],
        ],
        columns=tags_df.columns,
    )
    tags_df = pd.concat([tags_df, temp_df], ignore_index=True)
    return tags_df


def _get_ltype_class(ltype):
    if ltype in ww.type_system.registered_types:
        return ltype
    return ltype.__class__


def _get_specified_ltype_params(ltype):
    """Gets a dictionary of a LogicalType's parameters.

    Note: If the logical type has not been instantiated, no parameters have
    been specified for the LogicalType, so no parameters will be returned
    even if that LogicalType can have parameters set.

    Args:
        ltype (LogicalType): An instantiated or uninstantiated LogicalType

    Returns:
        dict: The LogicalType's specified parameters.
    """
    if ltype in ww.type_system.registered_types:
        # Do not reveal parameters for an uninstantiated LogicalType
        return {}
    return ltype.__dict__


def _is_categorical_series(series: pd.Series, threshold: float) -> bool:
    """
    Return ``True`` if the given series is "likely" to be categorical.
    Otherwise, return ``False``.  We say that a series is "likely" to be
    categorical if the percentage of unique values relative to total non-NA
    values is below a certain threshold.  In other words, if all values in the
    series are accounted for by a sufficiently small collection of unique
    values, then the series is categorical.
    """
    try:
        nunique = series.nunique()
    except TypeError as e:
        # It doesn't seem like there's a more elegant way to do this.  Pandas
        # doesn't provide an API that would give you any indication ahead of
        # time if a series with object dtype has any unhashable elements.
        if "unhashable type" in e.args[0]:
            return False
        else:
            raise  # pragma: no cover
    if nunique == 0:
        return False

    pct_unique = nunique / series.count()
    return pct_unique <= threshold
