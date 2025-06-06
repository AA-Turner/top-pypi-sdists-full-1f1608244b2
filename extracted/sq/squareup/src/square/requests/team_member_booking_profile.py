# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing


class TeamMemberBookingProfileParams(typing_extensions.TypedDict):
    """
    The booking profile of a seller's team member, including the team member's ID, display name, description and whether the team member can be booked as a service provider.
    """

    team_member_id: typing_extensions.NotRequired[str]
    """
    The ID of the [TeamMember](entity:TeamMember) object for the team member associated with the booking profile.
    """

    description: typing_extensions.NotRequired[str]
    """
    The description of the team member.
    """

    display_name: typing_extensions.NotRequired[str]
    """
    The display name of the team member.
    """

    is_bookable: typing_extensions.NotRequired[typing.Optional[bool]]
    """
    Indicates whether the team member can be booked through the Bookings API or the seller's online booking channel or site (`true`) or not (`false`).
    """

    profile_image_url: typing_extensions.NotRequired[str]
    """
    The URL of the team member's image for the bookings profile.
    """
