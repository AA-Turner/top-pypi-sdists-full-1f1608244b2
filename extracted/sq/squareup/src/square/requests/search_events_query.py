# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
from .search_events_filter import SearchEventsFilterParams
from .search_events_sort import SearchEventsSortParams


class SearchEventsQueryParams(typing_extensions.TypedDict):
    """
    Contains query criteria for the search.
    """

    filter: typing_extensions.NotRequired[SearchEventsFilterParams]
    """
    Criteria to filter events by.
    """

    sort: typing_extensions.NotRequired[SearchEventsSortParams]
    """
    Criteria to sort events by.
    """
