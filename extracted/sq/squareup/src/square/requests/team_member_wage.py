# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .money import MoneyParams


class TeamMemberWageParams(typing_extensions.TypedDict):
    """
    Job and wage information for a [team member](entity:TeamMember).
    This convenience object provides details needed to specify the `wage`
    field for a [timecard](entity:Timecard).
    """

    id: typing_extensions.NotRequired[str]
    """
    The UUID for this object.
    """

    team_member_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The `TeamMember` that this wage is assigned to.
    """

    title: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The job title that this wage relates to.
    """

    hourly_rate: typing_extensions.NotRequired[MoneyParams]
    """
    Can be a custom-set hourly wage or the calculated effective hourly
    wage based on the annual wage and hours worked per week.
    """

    job_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    An identifier for the [job](entity:Job) that this wage relates to.
    """

    tip_eligible: typing_extensions.NotRequired[typing.Optional[bool]]
    """
    Whether team members are eligible for tips when working this job.
    """
