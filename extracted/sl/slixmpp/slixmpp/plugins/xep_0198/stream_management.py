
# Slixmpp: The Slick XMPP Library
# Copyright (C) 2012 Nathanael C. Fritz, Lance J.T. Stout
# This file is part of Slixmpp.
# See the file LICENSE for copying permission.
import asyncio
import logging
import collections

from slixmpp.stanza import Message, Presence, Iq, StreamFeatures
from slixmpp.xmlstream import register_stanza_plugin
from slixmpp.xmlstream.handler import Callback, Waiter
from slixmpp.xmlstream.matcher import MatchXPath, MatchMany
from slixmpp.plugins.base import BasePlugin
from slixmpp.plugins.xep_0198 import stanza


log = logging.getLogger(__name__)


MAX_SEQ = 2 ** 32


class XEP_0198(BasePlugin):

    """
    XEP-0198: Stream Management
    """

    name = 'xep_0198'
    description = 'XEP-0198: Stream Management'
    dependencies = set()
    stanza = stanza
    default_config = {
        #: The last ack number received from the server.
        'last_ack': 0,

        #: The number of stanzas to wait between sending ack requests to
        #: the server. Setting this to ``1`` will send an ack request after
        #: every sent stanza. Defaults to ``5``.
        'window': 5,

        #: The stream management ID for the stream. Knowing this value is
        #: required in order to do stream resumption.
        'sm_id': None,

        #: A counter of handled incoming stanzas, mod 2^32.
        'handled': 0,

        #: A counter of unacked outgoing stanzas, mod 2^32.
        'seq': 0,

        #: Control whether or not the ability to resume the stream will be
        #: requested when enabling stream management. Defaults to ``True``.
        'allow_resume': True,

        'order': 10100,
        'resume_order': 9000
    }

    def plugin_init(self):
        """Start the XEP-0198 plugin."""

        # Only enable stream management for non-components,
        # since components do not yet perform feature negotiation.
        if self.xmpp.is_component:
            return

        self.window_counter = self.window

        self.enabled_in = False
        self.enabled_out = False
        self.unacked_queue = collections.deque()

        register_stanza_plugin(StreamFeatures, stanza.StreamManagement)
        self.xmpp.register_stanza(stanza.Enable)
        self.xmpp.register_stanza(stanza.Enabled)
        self.xmpp.register_stanza(stanza.Resume)
        self.xmpp.register_stanza(stanza.Resumed)
        self.xmpp.register_stanza(stanza.Ack)
        self.xmpp.register_stanza(stanza.RequestAck)

        # Register the feature twice because it may be ordered two
        # different ways: enabling after binding and resumption
        # before binding.
        self.xmpp.register_feature('sm',
                self._handle_sm_feature,
                restart=True,
                order=self.order)
        self.xmpp.register_feature('sm',
                self._handle_sm_feature,
                restart=True,
                order=self.resume_order)

        self.xmpp.register_handler(
                Callback('Stream Management Enabled',
                    MatchXPath(stanza.Enabled.tag_name()),
                    self._handle_enabled,
                    instream=True))

        self.xmpp.register_handler(
                Callback('Stream Management Resumed',
                    MatchXPath(stanza.Resumed.tag_name()),
                    self._handle_resumed,
                    instream=True))

        self.xmpp.register_handler(
                Callback('Stream Management Failed',
                    MatchXPath(stanza.Failed.tag_name()),
                    self._handle_failed,
                    instream=True))

        self.xmpp.register_handler(
                Callback('Stream Management Ack',
                    MatchXPath(stanza.Ack.tag_name()),
                    self._handle_ack,
                    instream=True))

        self.xmpp.register_handler(
                Callback('Stream Management Request Ack',
                    MatchXPath(stanza.RequestAck.tag_name()),
                    self._handle_request_ack,
                    instream=True))

        self.xmpp.add_filter('in', self._handle_incoming)
        self.xmpp.add_filter('out_sync', self._handle_outgoing)

        self.xmpp.add_event_handler('disconnected', self.disconnected)
        self.xmpp.add_event_handler('session_end', self.session_end)

    def plugin_end(self):
        if self.xmpp.is_component:
            return

        self.xmpp.unregister_feature('sm', self.order)
        self.xmpp.unregister_feature('sm', self.resume_order)
        self.xmpp.del_event_handler('disconnected', self.disconnected)
        self.xmpp.del_event_handler('session_end', self.session_end)
        self.xmpp.del_filter('in', self._handle_incoming)
        self.xmpp.del_filter('out_sync', self._handle_outgoing)
        self.xmpp.remove_handler('Stream Management Enabled')
        self.xmpp.remove_handler('Stream Management Resumed')
        self.xmpp.remove_handler('Stream Management Failed')
        self.xmpp.remove_handler('Stream Management Ack')
        self.xmpp.remove_handler('Stream Management Request Ack')
        self.xmpp.remove_stanza(stanza.Enable)
        self.xmpp.remove_stanza(stanza.Enabled)
        self.xmpp.remove_stanza(stanza.Resume)
        self.xmpp.remove_stanza(stanza.Resumed)
        self.xmpp.remove_stanza(stanza.Ack)
        self.xmpp.remove_stanza(stanza.RequestAck)

    def disconnected(self, event):
        """Reset enabled state until we can resume/reenable."""
        log.debug("disconnected, disabling SM")
        self.xmpp.event('sm_disabled', event)
        self.enabled_in = False
        self.enabled_out = False

    def session_end(self, event):
        """Reset stream management state."""
        log.debug("session_end, disabling SM")
        self.xmpp.event('sm_disabled', event)
        self.enabled_in = False
        self.enabled_out = False
        self.unacked_queue.clear()
        self.sm_id = None
        self.handled = 0
        self.seq = 0
        self.last_ack = 0

    def send_ack(self):
        """Send the current ack count to the server."""
        if not self.xmpp.transport:
            log.debug('Disconnected: not sending ack')
            return
        ack = stanza.Ack(self.xmpp)
        ack['h'] = self.handled
        self.xmpp.send_raw(str(ack))

    def request_ack(self, e=None):
        """Request an ack from the server."""
        log.debug("requesting ack")
        req = stanza.RequestAck(self.xmpp)
        self.xmpp.send_raw(str(req))

    async def _handle_sm_feature(self, features):
        """
        Enable or resume stream management.

        If no SM-ID is stored, and resource binding has taken place,
        stream management will be enabled.

        If an SM-ID is known, and the server allows resumption, the
        previous stream will be resumed.
        """
        if 'stream_management' in self.xmpp.features:
            # We've already negotiated stream management,
            # so no need to do it again.
            return False
        if self.sm_id and self.allow_resume and 'bind' not in self.xmpp.features:
            resume = stanza.Resume(self.xmpp)
            resume['h'] = self.handled
            resume['previd'] = self.sm_id
            resume.send()
            log.debug("resuming SM")

            # Wait for a response before allowing stream feature processing
            # to continue. The actual result processing will be done in the
            # _handle_resumed() or _handle_failed() methods.
            waiter = Waiter('resumed_or_failed',
                    MatchMany([
                        MatchXPath(stanza.Resumed.tag_name()),
                        MatchXPath(stanza.Failed.tag_name())]))
            self.xmpp.register_handler(waiter)
            result = await waiter.wait()
            if result is not None and result.name == 'resumed':
                return True
            self.xmpp.event("session_end")
        if 'bind' in self.xmpp.features:
            enable = stanza.Enable(self.xmpp)
            enable['resume'] = self.allow_resume
            enable.send()
            log.debug("enabling SM")

            waiter = Waiter('enabled_or_failed',
                    MatchMany([
                        MatchXPath(stanza.Enabled.tag_name()),
                        MatchXPath(stanza.Failed.tag_name())]))
            self.xmpp.register_handler(waiter)
            result = await waiter.wait()
        return False

    def _handle_enabled(self, stanza):
        """Save the SM-ID, if provided.

        Raises an :term:`sm_enabled` event.
        """
        self.xmpp.features.add('stream_management')
        if stanza['id']:
            self.sm_id = stanza['id']
        self.enabled_in = True
        self.handled = 0
        self.xmpp.event('sm_enabled', stanza)
        self.xmpp.end_session_on_disconnect = False

    def _handle_resumed(self, stanza):
        """Finish resuming a stream by resending unacked stanzas.

        Raises a :term:`session_resumed` event.
        """
        self.xmpp.features.add('stream_management')
        self.enabled_in = True
        self._handle_ack(stanza)
        for id, stanza in self.unacked_queue:
            self.xmpp.send(stanza, use_filters=False)
        self.xmpp.event('session_resumed', stanza)
        self.xmpp.end_session_on_disconnect = False

    def _handle_failed(self, stanza):
        """
        Disable and reset any features used since stream management was
        requested (tracked stanzas may have been sent during the interval
        between the enable request and the enabled response).

        Raises an :term:`sm_failed` event.
        """
        self.enabled_in = False
        self.enabled_out = False
        self.unacked_queue.clear()
        self.xmpp.event('sm_failed', stanza)

    def _handle_ack(self, ack):
        """Process a server ack by freeing acked stanzas from the queue.

        Raises a :term:`stanza_acked` event for each acked stanza.
        """
        if ack['h'] == self.last_ack:
            return

        num_acked = (ack['h'] - self.last_ack) % MAX_SEQ
        num_unacked = len(self.unacked_queue)
        log.debug("Ack: %s, Last Ack: %s, " + \
                  "Unacked: %s, Num Acked: %s, " + \
                  "Remaining: %s",
            ack['h'],
            self.last_ack,
            num_unacked,
            num_acked,
            num_unacked - num_acked)
        if num_acked > len(self.unacked_queue) or num_acked < 0:
            log.error('Inconsistent sequence numbers from the server,'
                      ' ignoring and replacing ours with them.')
            num_acked = len(self.unacked_queue)
        for x in range(num_acked):
            seq, stanza = self.unacked_queue.popleft()
            self.xmpp.event('stanza_acked', stanza)
        self.last_ack = ack['h']

    def _handle_request_ack(self, req):
        """Handle an ack request by sending an ack."""
        self.send_ack()

    def _handle_incoming(self, stanza):
        """Increment the handled counter for each inbound stanza."""
        if not self.enabled_in:
            return stanza

        if isinstance(stanza, (Message, Presence, Iq)):
            # Sequence numbers are mod 2^32
            self.handled = (self.handled + 1) % MAX_SEQ
        return stanza

    def _handle_outgoing(self, stanza):
        """Store outgoing stanzas in a queue to be acked."""
        from slixmpp.plugins.xep_0198 import stanza as st
        if isinstance(stanza, (st.Enable, st.Resume)):
            self.enabled_out = True
            # do not clear the queue on resume
            if isinstance(stanza, st.Enable):
                self.unacked_queue.clear()
            log.debug("enabling outgoing SM: %s" % stanza)

        if not self.enabled_out:
            return stanza

        if isinstance(stanza, (Message, Presence, Iq)):
            seq = None
            # Sequence numbers are mod 2^32
            self.seq = (self.seq + 1) % MAX_SEQ
            seq = self.seq
            self.unacked_queue.append((seq, stanza))
            self.window_counter -= 1
            if self.window_counter == 0:
                self.window_counter = self.window
                self.request_ack()
        return stanza
