"""
Copyright  (c)  2018-2025 Open Text  or  one  of its
affiliates.  Licensed  under  the   Apache  License,
Version 2.0 (the  "License"); You  may  not use this
file except in compliance with the License.

You may obtain a copy of the License at:
http://www.apache.org/licenses/LICENSE-2.0

Unless  required  by applicable  law or  agreed to in
writing, software  distributed  under the  License is
distributed on an  "AS IS" BASIS,  WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.
See the  License for the specific  language governing
permissions and limitations under the License.
"""
from typing import Optional, Union

from vertica_python.errors import QueryError

from verticapy._utils._sql._collect import save_verticapy_logs
from verticapy._utils._sql._format import format_type, quote_ident
from verticapy._utils._sql._sys import _executeSQL
from verticapy.connection import current_cursor


from verticapy.core.string_sql.base import StringSQL


@save_verticapy_logs
def compute_flextable_keys(
    flex_name: str, usecols: Optional[list] = None
) -> list[tuple]:
    """
    Computes the flex table keys and returns the
    predicted data types.

    Parameters
    ----------
    flex_name: str
        Flex table name.
    usecols: list, optional
        List of columns to consider.

    Returns
    -------
    List of tuples
        List  of virtual column names and  their
        respective data types.

    Examples
    --------
    Create a JSON file:

    .. ipython:: python

        import json

        data = {
            "column1": {
                "subcolumn1A": "value1A",
                "subcolumn1B": "value1B",
            },
            "column2": {
                "subcolumn2A": "value2A",
                "subcolumn2B": "value2B",
            }
        }

        json_string = json.dumps(data, indent=4)

        with open("nested_columns.json", "w") as json_file:
            json_file.write(str(json_string))

    We import :py:mod:`verticapy`:

    .. ipython:: python

        import verticapy as vp

    .. hint::

        By assigning an alias to :py:mod:`verticapy`,
        we mitigate the risk of code collisions with
        other libraries. This precaution is necessary
        because verticapy uses commonly known function
        names like "average" and "median", which can
        potentially lead to naming conflicts. The use
        of an alias ensures that the functions from
        :py:mod:`verticapy` are used as intended
        without interfering with functions from other
        libraries.

    We create a temporary schema:

    .. ipython:: python
        :okwarning:

        vp.drop("temp", method = "schema")
        vp.create_schema("temp")

    We injest the JSON file:

    .. ipython:: python
        :okwarning:

        vdf = vp.read_json(
            "nested_columns.json",
            schema = "temp",
            table_name = "test",
            flatten_maps = False,
            materialize = False
        )

    Then compute the flex table keys:

    .. ipython:: python
        :okwarning:

        from verticapy.sql import compute_flextable_keys

        compute_flextable_keys(flex_name = "temp.test")

    We drop the temporary table.

    .. ipython:: python

        vp.drop("temp.test")

    .. hint::

        Flex tables can be used to identify all the data types
        needed to ingest the file and can also be employed to
        flatten a nested JSON file. Explore all the flex functions
        to understand the possibilities.

    .. seealso::
        | :py:func:`~verticapy.sql.compute_vmap_keys` : Computes the vmap most frequent keys.
        | :py:func:`~verticapy.sql.isflextable` : Checks if the input relation is a flextable.
        | :py:func:`~verticapy.sql.isvmap` : Checks if the input column is a VMap.
    """
    usecols = format_type(usecols, dtype=list)
    _executeSQL(
        query=f"""
            SELECT 
                /*+LABEL('compute_flex_table_keys')*/
                compute_flextable_keys('{flex_name}');""",
        title="Guessing flex tables keys.",
    )
    usecols_str = [
        "'" + str(column).lower().replace("'", "''") + "'" for column in usecols
    ]
    usecols_str = ", ".join(usecols_str)
    where = f" WHERE LOWER(key_name) IN ({usecols_str})" if (usecols) else ""
    return _executeSQL(
        query=f"""
            SELECT 
                /*+LABEL('compute_flex_table_keys')*/
                key_name,
                data_type_guess 
            FROM {flex_name}_keys{where}""",
        title="Guessing the data types.",
        method="fetchall",
    )


@save_verticapy_logs
def compute_vmap_keys(
    expr: Union[str, StringSQL],
    vmap_col: str,
    limit: int = 100,
) -> list[tuple]:
    """
    Computes the most frequent keys in the input VMap.

    Parameters
    ----------
    expr: SQLRelation
        Input  expression.   You  can  also  specify  a
        vDataFrame  or a customized  relation, but  you
        must  enclose it  with an  alias.  For example,
        ``(SELECT 1) x`` is allowed, whereas ``(SELECT 1)``
        and "SELECT 1" are not.
    vmap_col: str
        VMap column.
    limit: int, optional
        Maximum number of keys to consider.

    Returns
    -------
    List of tuples
        List of virtual column names and their respective
        frequencies.

    Examples
    --------
    Create a JSON file:

    .. ipython:: python
        :okwarning:

        import json

        data = {
            "column1": {
                "subcolumn1A": "value1A",
                "subcolumn1B": "value1B",
            },
            "column2": {
                "subcolumn2A": "value2A",
                "subcolumn2B": "value2B",
            }
        }

        json_string = json.dumps(data, indent=4)

        with open("nested_columns.json", "w") as json_file:
            json_file.write(str(json_string))

    We import :py:mod:`verticapy`:

    .. ipython:: python

        import verticapy as vp

    .. hint::

        By assigning an alias to :py:mod:`verticapy`,
        we mitigate the risk of code collisions with
        other libraries. This precaution is necessary
        because verticapy uses commonly known function
        names like "average" and "median", which can
        potentially lead to naming conflicts. The use
        of an alias ensures that the functions from
        :py:mod:`verticapy` are used as intended
        without interfering with functions from other
        libraries.

    We create a temporary schema:

    .. ipython:: python
        :okwarning:

        vp.create_schema("temp")

    We injest the JSON file:

    .. ipython:: python
        :okwarning:

        vdf = vp.read_json(
            "nested_columns.json",
            schema = "temp",
            table_name = "test",
            flatten_maps = False,
        )

    Then compute the most frequent keys in the
    input VMap's ``column1``:

    .. ipython:: python
        :okwarning:

        from verticapy.sql import compute_vmap_keys

        compute_vmap_keys(expr = "temp.test", vmap_col = "column1")

    We drop the temporary table.

    .. ipython:: python
        :okwarning:

        vp.drop("temp.test")

    .. hint::

        Flex tables can be used to identify all the data types
        needed to ingest the file and can also be employed to
        flatten a nested JSON file. Explore all the flex functions
        to understand the possibilities.

    .. seealso::
        | :py:func:`~verticapy.sql.compute_flextable_keys` : Computes the flex table keys.
        | :py:func:`~verticapy.sql.isflextable` : Checks if the input relation is a flextable.
        | :py:func:`~verticapy.sql.isvmap` : Checks if the input column is a VMap.
    """
    vmap = quote_ident(vmap_col)
    if hasattr(expr, "object_type") and (expr.object_type == "vDataFrame"):
        if not expr[vmap_col].isvmap():
            raise ValueError(f"Virtual column {vmap_col} is not a VMAP.")
        expr = expr.current_relation()
    return _executeSQL(
        query=f"""
            SELECT 
                /*+LABEL('compute_vmap_keys')*/ 
                keys, 
                COUNT(*) 
            FROM 
                (SELECT 
                    MAPKEYS({vmap}) OVER (PARTITION BEST) 
                FROM {expr}) VERTICAPY_SUBTABLE 
            GROUP BY 1 
            ORDER BY 2 DESC 
            LIMIT {limit};""",
        title="Getting vmap most occurent keys.",
        method="fetchall",
    )


def isflextable(table_name: str, schema: str) -> bool:
    """
    Checks if the input relation is a flextable.

    Parameters
    ----------
    table_name: str
        Name of the table to check.
    schema: str
        Table schema.

    Returns
    -------
    bool
        True if the relation is a flex table.

    Examples
    --------
    Create a JSON file:

    .. ipython:: python

        import json

        data = {
            "column1": {
                "subcolumn1A": "value1A",
                "subcolumn1B": "value1B",
            },
            "column2": {
                "subcolumn2A": "value2A",
                "subcolumn2B": "value2B",
            }
        }

        json_string = json.dumps(data, indent=4)

        with open("nested_columns.json", "w") as json_file:
            json_file.write(str(json_string))

    We import :py:mod:`verticapy`:

    .. ipython:: python

        import verticapy as vp

    .. hint::

        By assigning an alias to :py:mod:`verticapy`,
        we mitigate the risk of code collisions with
        other libraries. This precaution is necessary
        because verticapy uses commonly known function
        names like "average" and "median", which can
        potentially lead to naming conflicts. The use
        of an alias ensures that the functions from
        :py:mod:`verticapy` are used as intended
        without interfering with functions from other
        libraries.

    We create a temporary schema:

    .. ipython:: python
        :okwarning:

        vp.create_schema("temp")

    We injest the JSON file:

    .. ipython:: python
        :okwarning:

        vdf = vp.read_json(
            "nested_columns.json",
            schema = "temp",
            table_name = "test",
            flatten_maps = False,
        )

    Then check if the table is a flex table:

    .. ipython:: python
        :okwarning:

        from verticapy.sql import isflextable

        isflextable(table_name = "test", schema = "temp")

    We drop the temporary table.

    .. ipython:: python

        vp.drop("temp.test")

    .. hint::

        Flex tables can be used to identify all the data types
        needed to ingest the file and can also be employed to
        flatten a nested JSON file. Explore all the flex functions
        to understand the possibilities.

    .. seealso::
        | :py:func:`~verticapy.sql.compute_flextable_keys` : : Computes the flex table keys.
        | :py:func:`~verticapy.sql.compute_vmap_keys` : Computes the vmap most frequent keys.
        | :py:func:`~verticapy.sql.isvmap` : Checks if the input column is a VMap.
    """
    table_name = quote_ident(table_name)[1:-1]
    schema = quote_ident(schema)[1:-1]
    res = _executeSQL(
        query=f"""
            SELECT 
                is_flextable 
            FROM v_catalog.tables 
            WHERE table_name = '{table_name}' 
              AND table_schema = '{schema}' 
              AND is_flextable 
            LIMIT 1;""",
        title="Checking if the table is a flextable.",
        method="fetchall",
    )
    return bool(res)


def isvmap(
    expr: Union[str, StringSQL],
    column: str,
) -> bool:
    """
    Checks if the input column is a VMap.

    Parameters
    ----------
    expr: SQLRelation
        Any relation or expression. If you enter
        an  expression,  you must enclose it  in
        parentheses and provide an alias.
    column: str
        Name of the column to check.

    Returns
    -------
    bool
        True if the column is a VMap.

    Examples
    --------
    Create a JSON file:

    .. ipython:: python
        :okwarning:

        import json

        data = {
            "column1": {
                "subcolumn1A": "value1A",
                "subcolumn1B": "value1B",
            },
            "column2": {
                "subcolumn2A": "value2A",
                "subcolumn2B": "value2B",
            }
        }

        json_string = json.dumps(data, indent=4)

        with open("nested_columns.json", "w") as json_file:
            json_file.write(str(json_string))

    We import :py:mod:`verticapy`:

    .. ipython:: python

        import verticapy as vp

    .. hint::

        By assigning an alias to :py:mod:`verticapy`,
        we mitigate the risk of code collisions with
        other libraries. This precaution is necessary
        because verticapy uses commonly known function
        names like "average" and "median", which can
        potentially lead to naming conflicts. The use
        of an alias ensures that the functions from
        :py:mod:`verticapy` are used as intended
        without interfering with functions from other
        libraries.

    We create a temporary schema:

    .. ipython:: python
        :okwarning:

        vp.create_schema("temp")

    We injest the JSON file:

    .. ipython:: python
        :okwarning:

        vdf = vp.read_json(
            "nested_columns.json",
            schema = "temp",
            table_name = "test",
            flatten_maps = False,
        )

    Checking if ``column1`` is a vmap:

    .. ipython:: python
        :okwarning:

        from verticapy.sql import isvmap

        isvmap("temp.test", "column1")

    We drop the temporary table.

    .. ipython:: python

        vp.drop("temp.test")

    .. hint::

        Flex tables can be used to identify all the data types
        needed to ingest the file and can also be employed to
        flatten a nested JSON file. Explore all the flex functions
        to understand the possibilities.

    .. seealso::
        | :py:func:`~verticapy.sql.compute_flextable_keys` : Computes the flex table keys.
        | :py:func:`~verticapy.sql.compute_vmap_keys` : : Computes the vmap most frequent keys.
        | :py:func:`~verticapy.sql.isflextable` : Checks if the input relation is a flextable.
    """
    column = quote_ident(column)
    if hasattr(expr, "object_type") and (expr.object_type == "vDataFrame"):
        expr = expr.current_relation()
    try:
        res = _executeSQL(
            query=f"""
                SELECT 
                    MAPVERSION({column}) AS isvmap, 
                    {column} 
                FROM {expr} 
                WHERE {column} IS NOT NULL 
                LIMIT 1;""",
            title="Checking if the column is a vmap.",
            method="fetchall",
        )
        dtype = current_cursor().description[1][1]
        if dtype not in (
            115,
            116,
        ):  # 116 is for long varbinary and 115 is for long varchar
            return False
    except UnicodeDecodeError:
        res = _executeSQL(
            query=f"""
                SELECT 
                    MAPVERSION({column}) AS isvmap 
                FROM {expr} 
                WHERE {column} IS NOT NULL 
                LIMIT 1;""",
            title="Checking if the column is a vmap.",
            method="fetchall",
        )
    except QueryError:
        return False
    return len(res) != 0 and (res[0][0] != -1)
