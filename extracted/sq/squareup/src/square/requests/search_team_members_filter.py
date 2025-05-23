# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from ..types.team_member_status import TeamMemberStatus


class SearchTeamMembersFilterParams(typing_extensions.TypedDict):
    """
    Represents a filter used in a search for `TeamMember` objects. `AND` logic is applied
    between the individual fields, and `OR` logic is applied within list-based fields.
    For example, setting this filter value:
    ```
    filter = (locations_ids = ["A", "B"], status = ACTIVE)
    ```
    returns only active team members assigned to either location "A" or "B".
    """

    location_ids: typing_extensions.NotRequired[typing.Optional[typing.Sequence[str]]]
    """
    When present, filters by team members assigned to the specified locations.
    When empty, includes team members assigned to any location.
    """

    status: typing_extensions.NotRequired[TeamMemberStatus]
    """
    When present, filters by team members who match the given status.
    When empty, includes team members of all statuses.
    See [TeamMemberStatus](#type-teammemberstatus) for possible values
    """

    is_owner: typing_extensions.NotRequired[typing.Optional[bool]]
    """
    When present and set to true, returns the team member who is the owner of the Square account.
    """
