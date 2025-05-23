"""AMQPStorm Connection.Channel."""

import collections
import logging
import threading
import time

from pamqp import specification
from pamqp.header import ContentHeader

from amqpstorm import compatibility
from amqpstorm.base import BaseChannel
from amqpstorm.base import BaseMessage
from amqpstorm.base import IDLE_WAIT
from amqpstorm.basic import Basic
from amqpstorm.compatibility import try_utf8_decode
from amqpstorm.exception import AMQPError
from amqpstorm.exception import AMQPChannelError
from amqpstorm.exception import AMQPConnectionError
from amqpstorm.exception import AMQPInvalidArgument
from amqpstorm.exception import AMQPMessageError
from amqpstorm.exchange import Exchange
from amqpstorm.message import Message
from amqpstorm.queue import Queue
from amqpstorm.rpc import Rpc
from amqpstorm.tx import Tx

LOGGER = logging.getLogger(__name__)
CONTENT_FRAME = ['Basic.Deliver', 'ContentHeader', 'ContentBody']


class Channel(BaseChannel):
    """RabbitMQ Channel.

    e.g.
    ::

        channel = connection.channel()
    """
    __slots__ = [
        '_consumer_callbacks', 'rpc', '_basic', '_confirming_deliveries',
        '_connection', '_exchange', '_inbound', '_queue', '_tx'
    ]

    def __init__(self, channel_id, connection, rpc_timeout):
        super(Channel, self).__init__(channel_id)
        self.lock = threading.Lock()
        self.rpc = Rpc(self, timeout=rpc_timeout)
        self._consumer_callbacks = {}
        self._confirming_deliveries = False
        self._connection = connection
        self._inbound = collections.deque()
        self._basic = Basic(self, connection.max_frame_size)
        self._exchange = Exchange(self)
        self._tx = Tx(self)
        self._queue = Queue(self)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, _):
        if exception_type:
            LOGGER.warning(
                'Closing channel due to an unhandled exception: %s',
                exception_value
            )
        if not self.is_open:
            return
        self.close()

    def __int__(self):
        return self._channel_id

    @property
    def basic(self):
        """RabbitMQ Basic Operations.

            e.g.
            ::

                message = channel.basic.get(queue='hello_world')

        :rtype: amqpstorm.basic.Basic
        """
        return self._basic

    @property
    def exchange(self):
        """RabbitMQ Exchange Operations.

            e.g.
            ::

                channel.exchange.declare(exchange='hello_world')

        :rtype: amqpstorm.exchange.Exchange
        """
        return self._exchange

    @property
    def queue(self):
        """RabbitMQ Queue Operations.

            e.g.
            ::

                channel.queue.declare(queue='hello_world')

        :rtype: amqpstorm.queue.Queue
        """
        return self._queue

    @property
    def tx(self):
        """RabbitMQ Tx Operations.

            e.g.
            ::

                channel.tx.commit()

        :rtype: amqpstorm.tx.Tx
        """
        return self._tx

    def build_inbound_messages(self, break_on_empty=False, to_tuple=False,
                               auto_decode=True, message_impl=None):
        """Build messages in the inbound queue.

        :param bool break_on_empty: Should we break the loop when there are
                                    no more messages in our inbound queue.

                                    This does not guarantee that the queue
                                    is emptied before the loop is broken, as
                                    messages may be consumed faster then
                                    they are being delivered by RabbitMQ,
                                    causing the loop to be broken prematurely.
        :param bool to_tuple: Should incoming messages be converted to a
                              tuple before delivery.
        :param bool auto_decode: Auto-decode strings when possible.
        :param class message_impl: Optional message class to use, derived from
                                   BaseMessage, for created messages. Defaults
                                   to Message.
        :raises AMQPInvalidArgument: Invalid Parameters
        :raises AMQPChannelError: Raises if the channel encountered an error.
        :raises AMQPConnectionError: Raises if the connection
                                     encountered an error.

        :rtype: :py:class:`generator`
        """
        self.check_for_errors()
        if message_impl:
            if not issubclass(message_impl, BaseMessage):
                raise AMQPInvalidArgument(
                    'message_impl must derive from BaseMessage'
                )
        else:
            message_impl = Message
        while not self.is_closed:
            message = self._build_message(auto_decode=auto_decode,
                                          message_impl=message_impl)
            if not message:
                self.check_for_errors()
                time.sleep(IDLE_WAIT)
                if break_on_empty and not self._inbound:
                    break
                continue
            if to_tuple:
                yield message.to_tuple()
                continue
            yield message

    def close(self, reply_code=200, reply_text=''):
        """Close Channel.

        :param int reply_code: Close reply code (e.g. 200)
        :param str reply_text: Close reply text

        :raises AMQPInvalidArgument: Invalid Parameters
        :raises AMQPChannelError: Raises if the channel encountered an error.
        :raises AMQPConnectionError: Raises if the connection
                                     encountered an error.

        :return:
        """
        if not compatibility.is_integer(reply_code):
            raise AMQPInvalidArgument('reply_code should be an integer')
        elif not compatibility.is_string(reply_text):
            raise AMQPInvalidArgument('reply_text should be a string')
        try:
            if self._connection.is_closed or not self.is_open:
                self.stop_consuming()
                LOGGER.debug('Channel #%d forcefully Closed', self.channel_id)
                return
            self.set_state(self.CLOSING)
            LOGGER.debug('Channel #%d Closing', self.channel_id)
            try:
                self.stop_consuming()
            except AMQPChannelError:
                self.remove_consumer_tag()
            self.rpc_request(specification.Channel.Close(
                reply_code=reply_code,
                reply_text=reply_text),
                connection_adapter=self._connection
            )
        finally:
            if self._inbound:
                self._inbound.clear()
            self.set_state(self.CLOSED)
        LOGGER.debug('Channel #%d Closed', self.channel_id)

    def check_for_errors(self,):
        """Check connection and channel for errors.

        :raises AMQPChannelError: Raises if the channel encountered an error.
        :raises AMQPConnectionError: Raises if the connection
                                     encountered an error.
        :return:
        """
        try:
            self._connection.check_for_errors()
        except AMQPConnectionError:
            self.set_state(self.CLOSED)
            raise

        self.check_for_exceptions()

        if self.is_closed:
            raise AMQPChannelError('channel closed')

    def check_for_exceptions(self):
        """Check channel for exceptions.

        :raises AMQPChannelError: Raises if the channel encountered an error.

        :return:
        """
        if self.exceptions:
            exception = self.exceptions[0]
            if self.is_open:
                self.exceptions.pop(0)
            raise exception

    def confirm_deliveries(self):
        """Set the channel to confirm that each message has been
        successfully delivered.

        :raises AMQPChannelError: Raises if the channel encountered an error.
        :raises AMQPConnectionError: Raises if the connection
                                     encountered an error.

        :return:
        """
        self._confirming_deliveries = True
        confirm_frame = specification.Confirm.Select()
        return self.rpc_request(confirm_frame)

    @property
    def confirming_deliveries(self):
        """Is the channel set to confirm deliveries.

        :return:
        """
        return self._confirming_deliveries

    def on_frame(self, frame_in):
        """Handle frame sent to this specific channel.

        :param pamqp.Frame frame_in: Amqp frame.
        :return:
        """
        if self.rpc.on_frame(frame_in):
            return

        if frame_in.name in CONTENT_FRAME:
            self._inbound.append(frame_in)
        elif frame_in.name == 'Basic.Cancel':
            self._basic_cancel(frame_in)
        elif frame_in.name == 'Basic.CancelOk':
            self.remove_consumer_tag(frame_in.consumer_tag)
        elif frame_in.name == 'Basic.ConsumeOk':
            self.add_consumer_tag(frame_in['consumer_tag'])
        elif frame_in.name == 'Basic.Return':
            self._basic_return(frame_in)
        elif frame_in.name == 'Channel.Close':
            self._close_channel(frame_in)
        elif frame_in.name == 'Channel.Flow':
            self.write_frame(specification.Channel.FlowOk(frame_in.active))
        else:
            LOGGER.error(
                '[Channel%d] Unhandled Frame: %s -- %s',
                self.channel_id, frame_in.name, dict(frame_in)
            )

    def open(self):
        """Open Channel.

        :return:
        """
        self._inbound.clear()
        self._exceptions = []
        self._confirming_deliveries = False
        self.set_state(self.OPENING)
        self.rpc_request(specification.Channel.Open())
        self.set_state(self.OPEN)

    def process_data_events(self, to_tuple=False, auto_decode=True):
        """Consume inbound messages.

        :param bool to_tuple: Should incoming messages be converted to a
                              tuple before delivery.
        :param bool auto_decode: Auto-decode strings when possible.

        :raises AMQPChannelError: Raises if the channel encountered an error.
        :raises AMQPConnectionError: Raises if the connection
                                     encountered an error.

        :return:
        """
        if not self._consumer_callbacks:
            raise AMQPChannelError('no consumer callback defined')
        for message in self.build_inbound_messages(break_on_empty=True,
                                                   auto_decode=auto_decode):
            consumer_tag = message._method.get('consumer_tag')
            if to_tuple:
                # noinspection PyCallingNonCallable
                self._consumer_callbacks[consumer_tag](*message.to_tuple())
                continue
            # noinspection PyCallingNonCallable
            self._consumer_callbacks[consumer_tag](message)

    def rpc_request(self, frame_out, connection_adapter=None):
        """Perform a RPC Request.

        :param specification.Frame frame_out: Amqp frame.
        :rtype: dict
        """
        with self.rpc.lock:
            uuid = self.rpc.register_request(frame_out.valid_responses)
            self._connection.write_frame(self.channel_id, frame_out)
            return self.rpc.get_request(
                uuid, connection_adapter=connection_adapter
            )

    def start_consuming(self, to_tuple=False, auto_decode=True):
        """Start consuming messages.

        :param bool to_tuple: Should incoming messages be converted to a
                              tuple before delivery.
        :param bool auto_decode: Auto-decode strings when possible.

        :raises AMQPChannelError: Raises if the channel encountered an error.
        :raises AMQPConnectionError: Raises if the connection
                                     encountered an error.

        :return:
        """
        while not self.is_closed:
            self.process_data_events(
                to_tuple=to_tuple,
                auto_decode=auto_decode
            )
            if self.consumer_tags:
                time.sleep(IDLE_WAIT)
                continue
            break

    def stop_consuming(self):
        """Stop consuming messages.

        :raises AMQPChannelError: Raises if the channel encountered an error.
        :raises AMQPConnectionError: Raises if the connection
                                     encountered an error.

        :return:
        """
        if not self.consumer_tags:
            return
        if not self.is_closed:
            for tag in self.consumer_tags:
                self.basic.cancel(tag)
        self.remove_consumer_tag()

    def write_frame(self, frame_out):
        """Write a pamqp frame from the current channel.

        :param specification.Frame frame_out: A single pamqp frame.

        :return:
        """
        self.check_for_errors()
        self._connection.write_frame(self.channel_id, frame_out)

    def write_frames(self, frames_out):
        """Write multiple pamqp frames from the current channel.

        :param list frames_out: A list of pamqp frames.

        :return:
        """
        self.check_for_errors()
        self._connection.write_frames(self.channel_id, frames_out)

    def _basic_cancel(self, frame_in):
        """Handle a Basic Cancel frame.

        :param specification.Basic.Cancel frame_in: Amqp frame.

        :return:
        """
        LOGGER.warning(
            'Received Basic.Cancel on consumer_tag: %s',
            try_utf8_decode(frame_in.consumer_tag)
        )
        self.remove_consumer_tag(frame_in.consumer_tag)

    def _basic_return(self, frame_in):
        """Handle a Basic Return Frame and treat it as an error.

        :param specification.Basic.Return frame_in: Amqp frame.

        :return:
        """
        reply_text = try_utf8_decode(frame_in.reply_text)
        message = (
            "Message not delivered: %s (%s) to queue '%s' from exchange '%s'" %
            (
                reply_text,
                frame_in.reply_code,
                frame_in.routing_key,
                frame_in.exchange
            )
        )
        exception = AMQPMessageError(message,
                                     reply_code=frame_in.reply_code)
        self.exceptions.append(exception)

    def _build_message(self, auto_decode, message_impl):
        """Fetch and build a complete Message from the inbound queue.

        :param bool auto_decode: Auto-decode strings when possible.
        :param class message_impl: Message implementation from BaseMessage

        :rtype: Message
        """
        if len(self._inbound) < 2:
            return None
        try:
            headers = self._build_message_headers()
            if not headers:
                return None
            basic_deliver, content_header = headers
            body = self._build_message_body(content_header.body_size)
        except IndexError:
            return None

        message = message_impl(channel=self,
                               body=body,
                               method=dict(basic_deliver),
                               properties=dict(content_header.properties),
                               auto_decode=auto_decode)
        return message

    def _build_message_headers(self):
        """Fetch Message Headers (Deliver & Header Frames).

        :rtype: tuple,None
        """
        basic_deliver = self._inbound.popleft()
        content_header = self._inbound.popleft()
        if not isinstance(basic_deliver, specification.Basic.Deliver):
            LOGGER.warning(
                'Received an out-of-order frame: %s was '
                'expecting a Basic.Deliver frame',
                type(basic_deliver)
            )
            return None
        elif not isinstance(content_header, ContentHeader):
            LOGGER.warning(
                'Received an out-of-order frame: %s was '
                'expecting a ContentHeader frame',
                type(content_header)
            )
            return None

        return basic_deliver, content_header

    def _build_message_body(self, body_size):
        """Build the Message body from the inbound queue.

        :rtype: str
        """
        body = bytes()
        while len(body) < body_size:
            if not self._inbound:
                self.check_for_errors()
                time.sleep(IDLE_WAIT)
                continue
            body_piece = self._inbound.popleft()
            if not body_piece.value:
                break
            body += body_piece.value
        return body

    def _close_channel(self, frame_in):
        """Close Channel.

        :param specification.Channel.Close frame_in: Channel Close frame.
        :return:
        """
        self.set_state(self.CLOSING)
        if not self._connection.is_closed:
            try:
                self.write_frame(specification.Channel.CloseOk())
            except AMQPError:
                pass
        self.remove_consumer_tag()
        if self._inbound:
            self._inbound.clear()
        self.exceptions.append(AMQPChannelError(
            'Channel %d was closed by remote server: %s' %
            (
                self._channel_id,
                try_utf8_decode(frame_in.reply_text)
            ),
            reply_code=frame_in.reply_code
        ))
        self.set_state(self.CLOSED)
