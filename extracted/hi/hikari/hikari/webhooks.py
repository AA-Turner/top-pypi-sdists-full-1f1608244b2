# Copyright (c) 2020 Nekokatt
# Copyright (c) 2021-present davfsa
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Application and entities that are used to describe webhooks on Discord."""

from __future__ import annotations

__all__: typing.Sequence[str] = (
    "ApplicationWebhook",
    "ChannelFollowerWebhook",
    "ExecutableWebhook",
    "IncomingWebhook",
    "PartialWebhook",
    "WebhookType",
)

import abc
import typing

import attrs

from hikari import channels as channels_
from hikari import snowflakes
from hikari import undefined
from hikari import urls
from hikari.internal import attrs_extensions
from hikari.internal import deprecation
from hikari.internal import enums
from hikari.internal import routes
from hikari.internal import typing_extensions

if typing.TYPE_CHECKING:
    from hikari import embeds as embeds_
    from hikari import files
    from hikari import files as files_
    from hikari import guilds as guilds_
    from hikari import messages as messages_
    from hikari import traits
    from hikari import users as users_
    from hikari.api import special_endpoints


@typing.final
class WebhookType(int, enums.Enum):
    """Types of webhook."""

    INCOMING = 1
    """Incoming webhook."""

    CHANNEL_FOLLOWER = 2
    """Channel Follower webhook."""

    APPLICATION = 3
    """Application webhook (from the interactions flow)."""


class ExecutableWebhook(abc.ABC):
    """An abstract class with logic for executing entities as webhooks."""

    # This is a mixin, do not add slotted fields.
    __slots__: typing.Sequence[str] = ()

    @property
    @abc.abstractmethod
    def app(self) -> traits.RESTAware:
        """Client application that models may use for procedures."""

    @property
    @abc.abstractmethod
    def webhook_id(self) -> snowflakes.Snowflake:
        """ID used to execute this entity as a webhook."""

    @property
    @abc.abstractmethod
    def token(self) -> str | None:
        """Webhook's token.

        !!! note
            If this is [`None`][] then the methods provided by [`hikari.webhooks.ExecutableWebhook`][]
            will always raise a [`ValueError`][].
        """

    async def execute(
        self,
        content: undefined.UndefinedOr[typing.Any] = undefined.UNDEFINED,
        *,
        username: undefined.UndefinedOr[str] = undefined.UNDEFINED,
        avatar_url: undefined.UndefinedType | str | files.URL = undefined.UNDEFINED,
        tts: undefined.UndefinedOr[bool] = undefined.UNDEFINED,
        attachment: undefined.UndefinedOr[files_.Resourceish] = undefined.UNDEFINED,
        attachments: undefined.UndefinedOr[typing.Sequence[files_.Resourceish]] = undefined.UNDEFINED,
        component: undefined.UndefinedOr[special_endpoints.ComponentBuilder] = undefined.UNDEFINED,
        components: undefined.UndefinedOr[typing.Sequence[special_endpoints.ComponentBuilder]] = undefined.UNDEFINED,
        embed: undefined.UndefinedOr[embeds_.Embed] = undefined.UNDEFINED,
        embeds: undefined.UndefinedOr[typing.Sequence[embeds_.Embed]] = undefined.UNDEFINED,
        poll: undefined.UndefinedOr[special_endpoints.PollBuilder] = undefined.UNDEFINED,
        mentions_everyone: undefined.UndefinedOr[bool] = undefined.UNDEFINED,
        user_mentions: undefined.UndefinedOr[
            snowflakes.SnowflakeishSequence[users_.PartialUser] | bool
        ] = undefined.UNDEFINED,
        role_mentions: undefined.UndefinedOr[
            snowflakes.SnowflakeishSequence[guilds_.PartialRole] | bool
        ] = undefined.UNDEFINED,
        flags: undefined.UndefinedType | int | messages_.MessageFlag = undefined.UNDEFINED,
    ) -> messages_.Message:
        """Execute the webhook to create a message.

        !!! warning
            At the time of writing, `username` and `avatar_url` are ignored for
            interaction webhooks.

            Additionally, [`hikari.messages.MessageFlag.SUPPRESS_EMBEDS`][],
            [`hikari.messages.MessageFlag.SUPPRESS_NOTIFICATIONS`][] and
            [`hikari.messages.MessageFlag.EPHEMERAL`][] are the only flags that can
            be set, with [`hikari.messages.MessageFlag.EPHEMERAL`][] being limited to
            interaction webhooks.

        Parameters
        ----------
        content
            If provided, the message contents. If
            [`hikari.undefined.UNDEFINED`][], then nothing will be sent
            in the content. Any other value here will be cast to a
            [`str`][].

            If this is a [`hikari.embeds.Embed`][] and no `embed` and no `embeds`
            kwargs are provided, then this will instead update the embed. This
            allows for simpler syntax when sending an embed alone.

            Likewise, if this is a [`hikari.files.Resource`][], then the
            content is instead treated as an attachment if no `attachment` and
            no `attachments` kwargs are provided.
        username
            If provided, the username to override the webhook's username
            for this request.
        avatar_url
            If provided, the url of an image to override the webhook's
            avatar with for this request.
        tts
            If provided, whether the message will be sent as a TTS message.
        attachment
            If provided, the message attachment. This can be a resource,
            or string of a path on your computer or a URL.
        attachments
            If provided, the message attachments. These can be resources, or
            strings consisting of paths on your computer or URLs.
        component
            If provided, builder object of the component to include in this message.
        components
            If provided, a sequence of the component builder objects to include
            in this message.
        embed
            If provided, the message embed.
        embeds
            If provided, the message embeds.
        poll
            If provided, the poll to set on the message.
        mentions_everyone
            If provided, whether the message should parse @everyone/@here
            mentions.
        user_mentions
            If provided, and [`True`][], all mentions will be parsed.
            If provided, and [`False`][], no mentions will be parsed.
            Alternatively this may be a collection of
            [`hikari.snowflakes.Snowflake`][], or
            [`hikari.users.PartialUser`][] derivatives to enforce mentioning
            specific users.
        role_mentions
            If provided, and [`True`][], all mentions will be parsed.
            If provided, and [`False`][], no mentions will be parsed.
            Alternatively this may be a collection of
            [`hikari.snowflakes.Snowflake`][], or
            [`hikari.guilds.PartialRole`][] derivatives to enforce mentioning
            specific roles.
        flags
            The flags to set for this webhook message.

        Returns
        -------
        hikari.messages.Message
            The created message object.

        Raises
        ------
        hikari.errors.NotFoundError
            If the current webhook is not found.
        hikari.errors.BadRequestError
            This can be raised if the file is too large; if the embed exceeds
            the defined limits; if the message content is specified only and
            empty or greater than `2000` characters; if neither content, file
            or embeds are specified.
            If any invalid snowflake IDs are passed; a snowflake may be invalid
            due to it being outside of the range of a 64 bit integer.
        hikari.errors.UnauthorizedError
            If you pass a token that's invalid for the target webhook.
        ValueError
            If `token` is not available.
        TypeError
            If both `attachment` and `attachments`, `component` and `components`
            or `embed` and `embeds` are specified.
        """
        if not self.token:
            msg = "Cannot send a message using a webhook where we don't know the token"
            raise ValueError(msg)

        return await self.app.rest.execute_webhook(
            webhook=self.webhook_id,
            token=self.token,
            content=content,
            username=username,
            avatar_url=avatar_url,
            tts=tts,
            attachment=attachment,
            attachments=attachments,
            component=component,
            components=components,
            embed=embed,
            embeds=embeds,
            poll=poll,
            mentions_everyone=mentions_everyone,
            user_mentions=user_mentions,
            role_mentions=role_mentions,
            flags=flags,
        )

    async def fetch_message(self, message: snowflakes.SnowflakeishOr[messages_.Message]) -> messages_.Message:
        """Fetch an old message sent by the webhook.

        Parameters
        ----------
        message
            The message to fetch. This may be the object or the ID of an
            existing channel.

        Returns
        -------
        hikari.messages.Message
            The requested message.

        Raises
        ------
        ValueError
            If [`token`][] is not available.
        hikari.errors.UnauthorizedError
            If you are unauthorized to make the request (invalid/missing token).
        hikari.errors.NotFoundError
            If the webhook is not found or the webhook's message wasn't found.
        hikari.errors.RateLimitTooLongError
            Raised in the event that a rate limit occurs that is
            longer than `max_rate_limit` when making a request.
        hikari.errors.InternalServerError
            If an internal error occurs on Discord while handling the request.
        """
        if self.token is None:
            msg = "Cannot fetch a message using a webhook where we don't know the token"
            raise ValueError(msg)

        return await self.app.rest.fetch_webhook_message(self.webhook_id, token=self.token, message=message)

    async def edit_message(
        self,
        message: snowflakes.SnowflakeishOr[messages_.Message],
        content: undefined.UndefinedNoneOr[typing.Any] = undefined.UNDEFINED,
        *,
        attachment: undefined.UndefinedNoneOr[files.Resourceish | messages_.Attachment] = undefined.UNDEFINED,
        attachments: undefined.UndefinedNoneOr[
            typing.Sequence[files.Resourceish | messages_.Attachment]
        ] = undefined.UNDEFINED,
        component: undefined.UndefinedNoneOr[special_endpoints.ComponentBuilder] = undefined.UNDEFINED,
        components: undefined.UndefinedNoneOr[
            typing.Sequence[special_endpoints.ComponentBuilder]
        ] = undefined.UNDEFINED,
        embed: undefined.UndefinedNoneOr[embeds_.Embed] = undefined.UNDEFINED,
        embeds: undefined.UndefinedNoneOr[typing.Sequence[embeds_.Embed]] = undefined.UNDEFINED,
        mentions_everyone: undefined.UndefinedOr[bool] = undefined.UNDEFINED,
        user_mentions: undefined.UndefinedOr[
            snowflakes.SnowflakeishSequence[users_.PartialUser] | bool
        ] = undefined.UNDEFINED,
        role_mentions: undefined.UndefinedOr[
            snowflakes.SnowflakeishSequence[guilds_.PartialRole] | bool
        ] = undefined.UNDEFINED,
    ) -> messages_.Message:
        """Edit a message sent by a webhook.

        !!! note
            Mentioning everyone, roles, or users in message edits currently
            will not send a push notification showing a new mention to people
            on Discord. It will still highlight in their chat as if they
            were mentioned, however.

        !!! warning
            If you specify a text `content`, `mentions_everyone`,
            `mentions_reply`, `user_mentions`, and `role_mentions` will default
            to [`False`][] as the message will be re-parsed for mentions. This will
            also occur if only one of the four are specified

            This is a limitation of Discord's design. If in doubt, specify all
            four of them each time.

        Parameters
        ----------
        message
            The message to delete. This may be the object or the ID of
            an existing message.
        content
            If provided, the message contents. If
            [`hikari.undefined.UNDEFINED`][], then nothing will be sent
            in the content. Any other value here will be cast to a
            [`str`][].

            If this is a [`hikari.embeds.Embed`][] and no `embed` nor
            `embeds` kwarg is provided, then this will instead
            update the embed. This allows for simpler syntax when
            sending an embed alone.

            Likewise, if this is a [`hikari.files.Resource`][], then the
            content is instead treated as an attachment if no `attachment` nor
            `attachments` kwargs are provided.
        attachment
            If provided, the attachment to set on the message. If
            [`hikari.undefined.UNDEFINED`][], the previous attachment, if
            present, is not changed. If this is [`None`][], then the
            attachment is removed, if present. Otherwise, the new attachment
            that was provided will be attached.
        attachments
            If provided, the attachments to set on the message. If
            [`hikari.undefined.UNDEFINED`][], the previous attachments, if
            present, are not changed. If this is [`None`][], then the
            attachments is removed, if present. Otherwise, the new attachments
            that were provided will be attached.
        component
            If provided, builder object of the component to set for this message.
            This component will replace any previously set components and passing
            [`None`][] will remove all components.
        components
            If provided, a sequence of the component builder objects set for
            this message. These components will replace any previously set
            components and passing [`None`][] or an empty sequence will
            remove all components.
        embed
            If provided, the embed to set on the message. If
            [`hikari.undefined.UNDEFINED`][], the previous embed(s) are not changed.
            If this is [`None`][] then any present embeds are removed.
            Otherwise, the new embed that was provided will be used as the
            replacement.
        embeds
            If provided, the embeds to set on the message. If
            [`hikari.undefined.UNDEFINED`][], the previous embed(s) are not changed.
            If this is [`None`][] then any present embeds are removed.
            Otherwise, the new embeds that were provided will be used as the
            replacement.
        mentions_everyone
            If provided, sanitation for `@everyone` mentions. If
            [`hikari.undefined.UNDEFINED`][], then the previous setting is
            not changed. If [`True`][], then `@everyone`/`@here` mentions
            in the message content will show up as mentioning everyone that can
            view the chat.
        user_mentions
            If provided, and [`True`][], all user mentions will be detected.
            If provided, and [`False`][], all user mentions will be ignored
            if appearing in the message body.
            Alternatively this may be a collection of
            [`hikari.snowflakes.Snowflake`][], or
            [`hikari.users.PartialUser`][] derivatives to enforce mentioning
            specific users.
        role_mentions
            If provided, and [`True`][], all role mentions will be detected.
            If provided, and [`False`][], all role mentions will be ignored
            if appearing in the message body.
            Alternatively this may be a collection of
            [`hikari.snowflakes.Snowflake`][], or
            [`hikari.guilds.PartialRole`][] derivatives to enforce mentioning
            specific roles.

        Returns
        -------
        hikari.messages.Message
            The edited message.

        Raises
        ------
        ValueError
            If more than 100 unique objects/entities are passed for
            `role_mentions` or `user_mentions` or `token` is not available.
        TypeError
            If both `attachment` and `attachments` are specified or if both
            `embed` and `embeds` are specified.
        hikari.errors.BadRequestError
            This may be raised in several discrete situations, such as messages
            being empty with no attachments or embeds; messages with more than
            2000 characters in them, embeds that exceed one of the many embed
            limits; too many attachments; attachments that are too large;
            too many components.
        hikari.errors.UnauthorizedError
            If you are unauthorized to make the request (invalid/missing token).
        hikari.errors.NotFoundError
            If the webhook or the message are not found.
        hikari.errors.RateLimitTooLongError
            Raised in the event that a rate limit occurs that is
            longer than `max_rate_limit` when making a request.
        hikari.errors.InternalServerError
            If an internal error occurs on Discord while handling the request.
        """
        if self.token is None:
            msg = "Cannot edit a message using a webhook where we don't know the token"
            raise ValueError(msg)

        return await self.app.rest.edit_webhook_message(
            self.webhook_id,
            token=self.token,
            message=message,
            content=content,
            attachment=attachment,
            attachments=attachments,
            component=component,
            components=components,
            embed=embed,
            embeds=embeds,
            mentions_everyone=mentions_everyone,
            user_mentions=user_mentions,
            role_mentions=role_mentions,
        )

    async def delete_message(self, message: snowflakes.SnowflakeishOr[messages_.Message]) -> None:
        """Delete a given message in a given channel.

        Parameters
        ----------
        message
            The message to delete. This may be the object or the ID of
            an existing message.

        Raises
        ------
        ValueError
            If `token` is not available.
        hikari.errors.UnauthorizedError
            If you are unauthorized to make the request (invalid/missing token).
        hikari.errors.NotFoundError
            If the webhook or the message are not found.
        hikari.errors.RateLimitTooLongError
            Raised in the event that a rate limit occurs that is
            longer than `max_rate_limit` when making a request.
        hikari.errors.InternalServerError
            If an internal error occurs on Discord while handling the request.
        """
        if self.token is None:
            msg = "Cannot delete a message using a webhook where we don't know the token"
            raise ValueError(msg)

        await self.app.rest.delete_webhook_message(self.webhook_id, token=self.token, message=message)


@attrs_extensions.with_copy
@attrs.define(unsafe_hash=True, kw_only=True, weakref_slot=False)
class PartialWebhook(snowflakes.Unique):
    """Base class for all webhook implementations."""

    app: traits.RESTAware = attrs.field(
        repr=False, eq=False, hash=False, metadata={attrs_extensions.SKIP_DEEP_COPY: True}
    )
    """Client application that models may use for procedures."""

    id: snowflakes.Snowflake = attrs.field(hash=True, repr=True)
    """The ID of this entity."""

    type: WebhookType | int = attrs.field(eq=False, hash=False, repr=True)
    """The type of the webhook."""

    name: str = attrs.field(eq=False, hash=False, repr=True)
    """The name of the webhook."""

    avatar_hash: str | None = attrs.field(eq=False, hash=False, repr=False)
    """The avatar hash of the webhook."""

    application_id: snowflakes.Snowflake | None = attrs.field(eq=False, hash=False, repr=False)
    """The ID of the application that created this webhook."""

    @typing_extensions.override
    def __str__(self) -> str:
        return self.name if self.name is not None else f"Unnamed webhook ID {self.id}"

    @property
    def mention(self) -> str:
        """Return a raw mention string for the given webhook's user.

        !!! note
            This exists purely for consistency. Webhooks do not receive events
            from the gateway, and without some bot backend to support it, will
            not be able to detect mentions of their webhook.

        Examples
        --------
        ```py
        >>> some_webhook.mention
        '<@123456789123456789>'
        ```
        """
        return f"<@{self.id}>"

    @property
    @deprecation.deprecated("Use 'make_avatar_url' instead")
    def avatar_url(self) -> files_.URL | None:
        """URL for this webhook's avatar, if set.

        May be [`None`][] if no avatar is set. In this case, you should use
        `default_avatar_url` instead.
        """
        deprecation.warn_deprecated(
            "avatar_url", removal_version="2.5.0", additional_info="Use 'make_avatar_url' instead."
        )
        return self.make_avatar_url()

    @property
    def default_avatar_url(self) -> files_.URL:
        """Default avatar URL for the user."""
        return routes.CDN_DEFAULT_USER_AVATAR.compile_to_file(urls.CDN_URL, style=0, file_format="png")

    def make_avatar_url(
        self,
        *,
        file_format: undefined.UndefinedOr[
            typing.Literal["PNG", "JPEG", "JPG", "WEBP", "AWEBP", "GIF"]
        ] = undefined.UNDEFINED,
        size: int = 4096,
        lossless: bool = True,
        ext: str | None | undefined.UndefinedType = undefined.UNDEFINED,
    ) -> files.URL | None:
        """Generate the avatar URL for this webhook, if set.

        If no avatar is set, this returns [`None`][].

        Parameters
        ----------
        file_format
            The format to use for this URL.

            Supports `PNG`, `JPEG`, `JPG`, `WEBP`, `AWEBP` and `GIF`.

            If not specified, the format will be determined based on
            whether the avatar is animated or not.
        size
            The size to set for the URL. Can be any power of two between `16` and `4096`.
        lossless
            Whether to return a lossless or compressed WEBP image;
            This is ignored if `file_format` is not `WEBP` or `AWEBP`.
        ext
            The ext to use for this URL.
            Supports `png`, `jpeg`, `jpg`, `webp` and `gif` (when
            animated).

            If [`None`][], then the correct default extension is
            determined based on whether the avatar is animated or not.

            !!! deprecated 2.4.0
                This has been replaced with the `file_format` argument.

        Returns
        -------
        typing.Optional[hikari.files.URL]
            The URL, or [`None`][] if no avatar is set.

        Raises
        ------
        TypeError
            If an invalid format is passed for `file_format`;
            If an animated format is requested for a static avatar.
        ValueError
            If `size` is specified but is not a power of two or not between 16 and 4096.
        """
        if self.avatar_hash is None:
            return None

        if ext:
            deprecation.warn_deprecated(
                "ext", removal_version="2.5.0", additional_info="Use 'file_format' argument instead."
            )
            file_format = ext.upper()  # type: ignore[assignment]

        if not file_format:
            file_format = "GIF" if self.avatar_hash.startswith("a_") else "PNG"

        return routes.CDN_USER_AVATAR.compile_to_file(
            urls.CDN_URL, user_id=self.id, hash=self.avatar_hash, size=size, file_format=file_format, lossless=lossless
        )


@attrs.define(unsafe_hash=True, kw_only=True, weakref_slot=False)
class IncomingWebhook(PartialWebhook, ExecutableWebhook):
    """Represents an incoming webhook object on Discord.

    This is an endpoint that can have messages sent to it using standard
    HTTP requests, which enables external services that are not bots to
    send informational messages to specific channels.
    """

    channel_id: snowflakes.Snowflake = attrs.field(eq=False, hash=False, repr=True)
    """The channel ID this webhook is for."""

    guild_id: snowflakes.Snowflake = attrs.field(eq=False, hash=False, repr=True)
    """The guild ID of the webhook."""

    author: users_.User | None = attrs.field(eq=False, hash=False, repr=True)
    """The user that created the webhook.

    !!! note
        This will be [`None`][] when fetched with the webhook's token
        rather than bot authorization or when received within audit logs.
    """

    token: str | None = attrs.field(eq=False, hash=False, repr=False)
    """The token for the webhook.

    !!! note
        This is only available for incoming webhooks that are created in the
        channel settings.
    """

    @property
    @typing_extensions.override
    def webhook_id(self) -> snowflakes.Snowflake:
        # <<inherited docstring from ExecutableWebhook>>.
        return self.id

    async def delete(self, *, use_token: undefined.UndefinedOr[bool] = undefined.UNDEFINED) -> None:
        """Delete this webhook.

        Parameters
        ----------
        use_token
            If set to [`True`][] then the webhook's token will be used for
            this request; if set to [`False`][] then bot authorization will
            be used; if not specified then the webhook's token will be used for
            the request if it's set else bot authorization.

        Raises
        ------
        hikari.errors.NotFoundError
            If this webhook is not found.
        hikari.errors.ForbiddenError
            If you either lack the [`hikari.permissions.Permissions.MANAGE_WEBHOOKS`][] permission or
            are not a member of the guild this webhook belongs to.
        ValueError
            If `use_token` is passed as [`True`][] when [`hikari.webhooks.IncomingWebhook.token`][] is
            [`None`][].
        """
        token: undefined.UndefinedOr[str] = undefined.UNDEFINED
        if use_token:
            if self.token is None:
                msg = "This webhook's token is unknown, so cannot be used"
                raise ValueError(msg)
            token = self.token

        elif use_token is undefined.UNDEFINED and self.token:
            token = self.token

        await self.app.rest.delete_webhook(self.id, token=token)

    async def edit(
        self,
        *,
        name: undefined.UndefinedOr[str] = undefined.UNDEFINED,
        avatar: undefined.UndefinedNoneOr[files_.Resource[files_.AsyncReader]] = undefined.UNDEFINED,
        channel: undefined.UndefinedOr[snowflakes.SnowflakeishOr[channels_.WebhookChannelT]] = undefined.UNDEFINED,
        reason: undefined.UndefinedOr[str] = undefined.UNDEFINED,
        use_token: undefined.UndefinedOr[bool] = undefined.UNDEFINED,
    ) -> IncomingWebhook:
        """Edit this webhook.

        Parameters
        ----------
        name
            If provided, the new name string.
        avatar
            If provided, the new avatar image. If [`None`][], then
            it is removed. If not specified, nothing is changed.
        channel
            If provided, the object or ID of the new channel the given
            webhook should be moved to.
        reason
            If provided, the audit log reason explaining why the operation
            was performed. This field will be used when using the webhook's
            token rather than bot authorization.
        use_token
            If set to [`True`][] then the webhook's token will be used for
            this request; if set to [`False`][] then bot authorization will
            be used; if not specified then the webhook's token will be used for
            the request if it's set else bot authorization.

        Returns
        -------
        IncomingWebhook
            The updated webhook object.

        Raises
        ------
        ValueError
            If `use_token` is passed as [`True`][] when [`hikari.webhooks.IncomingWebhook.token`][] is [`None`][].
        hikari.errors.BadRequestError
            If any invalid snowflake IDs are passed; a snowflake may be invalid
            due to it being outside the range of a 64-bit integer.
        hikari.errors.NotFoundError
            If either the webhook or the channel are not found.
        hikari.errors.ForbiddenError
            If you either lack the [`hikari.permissions.Permissions.MANAGE_WEBHOOKS`][] permission or
            are not a member of the guild this webhook belongs to.
        hikari.errors.UnauthorizedError
            If you pass a token that's invalid for the target webhook.
        hikari.errors.RateLimitTooLongError
            Raised in the event that a rate limit occurs that is
            longer than `max_rate_limit` when making a request.
        hikari.errors.InternalServerError
            If an internal error occurs on Discord while handling the request.
        """
        token: undefined.UndefinedOr[str] = undefined.UNDEFINED
        if use_token:
            if self.token is None:
                msg = "This webhook's token is unknown, so cannot be used"
                raise ValueError(msg)
            token = self.token

        elif use_token is undefined.UNDEFINED and self.token:
            token = self.token

        webhook = await self.app.rest.edit_webhook(
            self.id, token=token, name=name, avatar=avatar, channel=channel, reason=reason
        )
        assert isinstance(webhook, IncomingWebhook)
        return webhook

    async def fetch_channel(self) -> channels_.WebhookChannelT:
        """Fetch the channel this webhook is for.

        Returns
        -------
        hikari.channels.WebhookChannelT
            The object of the channel this webhook targets.

        Raises
        ------
        hikari.errors.ForbiddenError
            If you don't have access to the channel this webhook belongs to.
        hikari.errors.NotFoundError
            If the channel this message was created in does not exist.
        hikari.errors.UnauthorizedError
            If you are unauthorized to make the request (invalid/missing token).
        hikari.errors.RateLimitTooLongError
            Raised in the event that a rate limit occurs that is
            longer than `max_rate_limit` when making a request.
        hikari.errors.InternalServerError
            If an internal error occurs on Discord while handling the request.
        """
        channel = await self.app.rest.fetch_channel(self.channel_id)
        assert isinstance(channel, channels_.WebhookChannelTypes)
        return channel

    async def fetch_self(self, *, use_token: undefined.UndefinedOr[bool] = undefined.UNDEFINED) -> IncomingWebhook:
        """Fetch this webhook.

        Parameters
        ----------
        use_token
            If set to [`True`][] then the webhook's token will be used for
            this request; if set to [`False`][] then bot authorization will
            be used; if not specified then the webhook's token will be used for
            the request if it's set else bot authorization.

        Returns
        -------
        IncomingWebhook
            The requested webhook object.

        Raises
        ------
        ValueError
            If `use_token` is passed as [`True`][] when [`hikari.webhooks.IncomingWebhook.token`][]
            is [`None`][].
        hikari.errors.ForbiddenError
            If you're not in the guild that owns this webhook or
            lack the [`hikari.permissions.Permissions.MANAGE_WEBHOOKS`][] permission.
        hikari.errors.NotFoundError
            If the webhook is not found.
        hikari.errors.UnauthorizedError
            If you pass a token that's invalid for the target webhook.
        hikari.errors.RateLimitTooLongError
            Raised in the event that a rate limit occurs that is
            longer than `max_rate_limit` when making a request.
        hikari.errors.InternalServerError
            If an internal error occurs on Discord while handling the request.
        """
        token: undefined.UndefinedOr[str] = undefined.UNDEFINED
        if use_token:
            if self.token is None:
                msg = "This webhook's token is unknown, so cannot be used"
                raise ValueError(msg)
            token = self.token

        elif use_token is undefined.UNDEFINED and self.token:
            token = self.token

        webhook = await self.app.rest.fetch_webhook(self.id, token=token)
        assert isinstance(webhook, IncomingWebhook)
        return webhook


@attrs.define(unsafe_hash=True, kw_only=True, weakref_slot=False)
class ChannelFollowerWebhook(PartialWebhook):
    """Represents a channel follower webhook object on Discord."""

    channel_id: snowflakes.Snowflake = attrs.field(eq=False, hash=False, repr=True)
    """The channel ID this webhook is for."""

    guild_id: snowflakes.Snowflake = attrs.field(eq=False, hash=False, repr=True)
    """The guild ID of the webhook."""

    author: users_.User | None = attrs.field(eq=False, hash=False, repr=True)
    """The user that created the webhook.

    !!! note
        This will be [`None`][] when received within an audit log.
    """

    source_channel: channels_.PartialChannel | None = attrs.field(eq=False, hash=False, repr=True)
    """The partial object of the channel this webhook is following.

    This will be [`None`][] when the user that followed the channel is no
    longer in the source guild or has lost access to the source channel.
    """

    source_guild: guilds_.PartialGuild | None = attrs.field(eq=False, hash=False, repr=True)
    """The partial object of the guild this webhook is following.

    This will be [`None`][] when the user that followed the channel is no
    longer in the source guild or has lost access to the source channel.
    """

    async def delete(self) -> None:
        """Delete this webhook.

        Raises
        ------
        hikari.errors.NotFoundError
            If this webhook is not found.
        hikari.errors.ForbiddenError
            If you either lack the [`hikari.permissions.Permissions.MANAGE_WEBHOOKS`][] permission or
            are not a member of the guild this webhook belongs to.
        """
        await self.app.rest.delete_webhook(self.id)

    async def edit(
        self,
        *,
        name: undefined.UndefinedOr[str] = undefined.UNDEFINED,
        avatar: undefined.UndefinedNoneOr[files_.Resource[files_.AsyncReader]] = undefined.UNDEFINED,
        channel: undefined.UndefinedOr[snowflakes.SnowflakeishOr[channels_.WebhookChannelT]] = undefined.UNDEFINED,
        reason: undefined.UndefinedOr[str] = undefined.UNDEFINED,
    ) -> ChannelFollowerWebhook:
        """Edit this webhook.

        Parameters
        ----------
        name
            If provided, the new name string.
        avatar
            If provided, the new avatar image. If [`None`][], then
            it is removed. If not specified, nothing is changed.
        channel
            If provided, the object or ID of the new channel the given
            webhook should be moved to.
        reason
            If provided, the audit log reason explaining why the operation
            was performed. This field will be used when using the webhook's
            token rather than bot authorization.

        Returns
        -------
        hikari.webhooks.ChannelFollowerWebhook
            The updated webhook object.

        Raises
        ------
        hikari.errors.BadRequestError
            If any invalid snowflake IDs are passed; a snowflake may be invalid
            due to it being outside of the range of a 64 bit integer.
        hikari.errors.NotFoundError
            If either the webhook or the channel are not found.
        hikari.errors.ForbiddenError
            If you either lack the [`hikari.permissions.Permissions.MANAGE_WEBHOOKS`][] permission or
            are not a member of the guild this webhook belongs to.
        hikari.errors.UnauthorizedError
            If you pass a token that's invalid for the target webhook.
        hikari.errors.RateLimitTooLongError
            Raised in the event that a rate limit occurs that is
            longer than `max_rate_limit` when making a request.
        hikari.errors.InternalServerError
            If an internal error occurs on Discord while handling the request.
        """
        webhook = await self.app.rest.edit_webhook(self.id, name=name, avatar=avatar, channel=channel, reason=reason)
        assert isinstance(webhook, ChannelFollowerWebhook)
        return webhook

    async def fetch_channel(self) -> channels_.WebhookChannelT:
        """Fetch the channel this webhook is for.

        Returns
        -------
        hikari.channels.WebhookChannelT
            The object of the channel this webhook targets.

        Raises
        ------
        hikari.errors.ForbiddenError
            If you don't have access to the channel this webhook belongs to.
        hikari.errors.NotFoundError
            If the channel this message was created in does not exist.
        hikari.errors.UnauthorizedError
            If you are unauthorized to make the request (invalid/missing token).
        hikari.errors.RateLimitTooLongError
            Raised in the event that a rate limit occurs that is
            longer than `max_rate_limit` when making a request.
        hikari.errors.InternalServerError
            If an internal error occurs on Discord while handling the request.
        """
        channel = await self.app.rest.fetch_channel(self.channel_id)
        assert isinstance(channel, channels_.WebhookChannelTypes)
        return channel

    async def fetch_self(self) -> ChannelFollowerWebhook:
        """Fetch this webhook.

        Returns
        -------
        hikari.webhooks.ChannelFollowerWebhook
            The requested webhook object.

        Raises
        ------
        hikari.errors.ForbiddenError
            If you're not in the guild that owns this webhook or
            lack the [`hikari.permissions.Permissions.MANAGE_WEBHOOKS`][] permission.
        hikari.errors.NotFoundError
            If the webhook is not found.
        hikari.errors.UnauthorizedError
            If you pass a token that's invalid for the target webhook.
        hikari.errors.RateLimitTooLongError
            Raised in the event that a rate limit occurs that is
            longer than `max_rate_limit` when making a request.
        hikari.errors.InternalServerError
            If an internal error occurs on Discord while handling the request.
        """
        webhook = await self.app.rest.fetch_webhook(self.id)
        assert isinstance(webhook, ChannelFollowerWebhook)
        return webhook


@attrs.define(unsafe_hash=True, kw_only=True, weakref_slot=False)
class ApplicationWebhook(PartialWebhook):
    """Represents an application webhook object on Discord.

    This is from the interactions flow.
    """

    application_id: snowflakes.Snowflake = attrs.field()
    # <<inherited docstring from PartialWebhook>>.
