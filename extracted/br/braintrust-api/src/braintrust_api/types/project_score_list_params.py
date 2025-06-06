# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ProjectScoreListParams"]


class ProjectScoreListParams(TypedDict, total=False):
    ending_before: str
    """Pagination cursor id.

    For example, if the initial item in the last page you fetched had an id of
    `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
    pass one of `starting_after` and `ending_before`
    """

    ids: Union[str, List[str]]
    """Filter search results to a particular set of object IDs.

    To specify a list of IDs, include the query param multiple times
    """

    limit: Optional[int]
    """Limit the number of objects to return"""

    org_name: str
    """Filter search results to within a particular organization"""

    project_id: str
    """Project id"""

    project_name: str
    """Name of the project to search for"""

    project_score_name: str
    """Name of the project_score to search for"""

    score_type: Union[
        Literal["slider", "categorical", "weighted", "minimum", "maximum", "online"],
        List[Literal["slider", "categorical", "weighted", "minimum", "maximum", "online"]],
    ]
    """The type of the configured score"""

    starting_after: str
    """Pagination cursor id.

    For example, if the final item in the last page you fetched had an id of `foo`,
    pass `starting_after=foo` to fetch the next page. Note: you may only pass one of
    `starting_after` and `ending_before`
    """
