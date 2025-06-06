# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .money import MoneyParams


class ShiftWageParams(typing_extensions.TypedDict):
    """
    The hourly wage rate used to compensate an employee for this shift.

    Deprecated at Square API version 2025-05-21. See the [migration notes](https://developer.squareup.com/docs/labor-api/what-it-does#migration-notes).
    """

    title: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The name of the job performed during this shift.
    """

    hourly_rate: typing_extensions.NotRequired[MoneyParams]
    """
    Can be a custom-set hourly wage or the calculated effective hourly
    wage based on the annual wage and hours worked per week.
    """

    job_id: typing_extensions.NotRequired[str]
    """
    The id of the job performed during this shift. Square
    labor-reporting UIs might group shifts together by id.
    """

    tip_eligible: typing_extensions.NotRequired[typing.Optional[bool]]
    """
    Whether team members are eligible for tips when working this job.
    """
