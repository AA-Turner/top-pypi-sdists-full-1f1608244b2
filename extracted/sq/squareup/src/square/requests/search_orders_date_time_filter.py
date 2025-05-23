# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
from .time_range import TimeRangeParams


class SearchOrdersDateTimeFilterParams(typing_extensions.TypedDict):
    """
    Filter for `Order` objects based on whether their `CREATED_AT`,
    `CLOSED_AT`, or `UPDATED_AT` timestamps fall within a specified time range.
    You can specify the time range and which timestamp to filter for. You can filter
    for only one time range at a time.

    For each time range, the start time and end time are inclusive. If the end time
    is absent, it defaults to the time of the first request for the cursor.

    __Important:__ If you use the `DateTimeFilter` in a `SearchOrders` query,
    you must set the `sort_field` in [OrdersSort](entity:SearchOrdersSort)
    to the same field you filter for. For example, if you set the `CLOSED_AT` field
    in `DateTimeFilter`, you must set the `sort_field` in `SearchOrdersSort` to
    `CLOSED_AT`. Otherwise, `SearchOrders` throws an error.
    [Learn more about filtering orders by time range.](https://developer.squareup.com/docs/orders-api/manage-orders/search-orders#important-note-about-filtering-orders-by-time-range)
    """

    created_at: typing_extensions.NotRequired[TimeRangeParams]
    """
    The time range for filtering on the `created_at` timestamp. If you use this
    value, you must set the `sort_field` in the `OrdersSearchSort` object to
    `CREATED_AT`.
    """

    updated_at: typing_extensions.NotRequired[TimeRangeParams]
    """
    The time range for filtering on the `updated_at` timestamp. If you use this
    value, you must set the `sort_field` in the `OrdersSearchSort` object to
    `UPDATED_AT`.
    """

    closed_at: typing_extensions.NotRequired[TimeRangeParams]
    """
    The time range for filtering on the `closed_at` timestamp. If you use this
    value, you must set the `sort_field` in the `OrdersSearchSort` object to
    `CLOSED_AT`.
    """
