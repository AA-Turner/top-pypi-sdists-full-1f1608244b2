#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Netius System
# Copyright (c) 2008-2024 Hive Solutions Lda.
#
# This file is part of Hive Netius System.
#
# Hive Netius System is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Netius System is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Netius System. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__copyright__ = "Copyright (c) 2008-2024 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import uuid
import hashlib
import datetime

import netius.common
import netius.clients
import netius.servers


class RelaySMTPServer(netius.servers.SMTPServer):
    """
    Relay version of the SMTP server that relays messages
    that are not considered to be local to other servers.

    The servers uses the default SMTP client implementation
    to relay the messages.
    """

    def __init__(self, postmaster=None, *args, **kwargs):
        netius.servers.SMTPServer.__init__(self, *args, **kwargs)
        self.postmaster = postmaster
        self.dkim = {}

    def on_serve(self):
        netius.servers.SMTPServer.on_serve(self)
        self.postmaster = self.get_env("POSTMASTER", self.postmaster)
        self.dkim = self.get_env("DKIM", self.dkim)
        dkim_l = len(self.dkim)
        self.info("Starting Relay SMTP server with %d DKIM registers  ..." % dkim_l)
        if self.postmaster:
            self.info("Using '%s' as the Postmaster email sender ..." % self.postmaster)

    def on_header_smtp(self, connection, from_l, to_l):
        netius.servers.SMTPServer.on_header_smtp(self, connection, from_l, to_l)

        # retrieves the list or remote emails for each a relay
        # operation will have to be performed as requested by
        # the current SMTP specification (federation based)
        remotes = self._remotes(to_l)

        # updates the current connection with the list of remote
        # emails that have to be relayed and starts the buffer
        # that will hold the complete message for relay
        connection.remotes = remotes
        connection.relay = []

    def on_data_smtp(self, connection, data):
        netius.servers.SMTPServer.on_data_smtp(self, connection, data)

        # verifies if there're remote addresses in the current
        # connection's message and if there is adds the received
        # data to the current relay buffer that is used
        if not connection.remotes:
            return
        connection.relay.append(data)

    def on_message_smtp(self, connection):
        netius.servers.SMTPServer.on_message_smtp(self, connection)

        # in case there's no remotes list in the current connection
        # there's no need to proceed as no relay is required
        if not connection.remotes:
            return

        # joins the current relay buffer to create the full message
        # data and then removes the (non required) termination value
        # from it to avoid any possible problems with extra size
        data_s = b"".join(connection.relay)
        data_s = data_s[: netius.servers.TERMINATION_SIZE * -1]

        # retrieves the list of "froms" for the connection and then
        # sends the message for relay to all of the current remotes
        froms = self._emails(connection.from_l, prefix="from")
        self.relay(connection, froms, connection.remotes, data_s)

    def relay(self, connection, froms, tos, contents):
        # verifies that the current connection has an authenticated user
        # and if not raises an exception as the authentication is mandatory
        # for the relaying of message under the "default" policy
        if not hasattr(connection, "username") or not connection.username:
            raise netius.SecurityError("User is not authenticated")

        # using the auth meta information retrieves the list of allowed
        # froms for the current user and verifies that the current froms
        # are all contained in the list of allowed froms, otherwise raises
        # an exception indicating that the user is not allowed to relay
        auth_meta = getattr(connection, "auth_meta", {})
        allowed_froms = auth_meta.get("allowed_froms", [])
        allowed = not allowed_froms or all(value in allowed_froms for value in froms)
        if not allowed:
            raise netius.SecurityError("User is not allowed to relay from")

        # retrieves the current date value formatted according to
        # the SMTP based specification string value, this value
        # is going to be used for the replacement of the header
        date = self.date()

        # retrieves the first email from the froms list as this is
        # the one that is going to be used for message id generation
        # and then generates a new "temporary" message id
        first = froms[0]
        message_id = self.message_id(connection=connection, email=first)

        # the default reply to value is the first from value and it
        # should serve as a way to reply with errors in case they
        # exist - this way we can notify the sender (postmaster)
        reply_to = first

        # parses the provided contents as mime text and then appends
        # the various extra fields so that the relay operation is
        # considered valid and then re-joins the message as a string
        headers, body = netius.common.rfc822_parse(contents)
        received = connection.received_s()
        message_id = headers.pop("Message-Id", message_id)
        message_id = headers.pop("Message-ID", message_id)
        headers.set("Date", date)
        headers.set("Received", received)
        headers.set("Message-ID", message_id)
        contents = netius.common.rfc822_join(headers, body)

        # tries to sign the message using DKIM, the server is going to
        # search the current registry, trying to find a registry for the
        # domain of the sender and if it finds one signs the message using
        # the information provided by the registry
        contents = self.dkim_contents(contents, email=first)

        # creates the callback that will close the client once the message
        # is sent to all the recipients (better auto close support), note
        # that multiple SMTP session may be created for the message so that
        # all the hosts associated with the recipients are notified
        callback = lambda smtp_client: smtp_client.close()

        # creates the callback to the error as a function that sends a
        # postmaster email to the reply to address found in the message,
        # note that this is only performed in case there's a valid email
        # address defined as postmaster for this SMTP server
        callback_error = lambda smtp_client, context, exception: self.relay_postmaster(
            reply_to, context, exception
        )

        # generates a new SMTP client for the sending of the message,
        # uses the current host for identification and then triggers
        # the message event to send the message to the target host
        smtp_client = netius.clients.SMTPClient(host=self.host)
        smtp_client.message(
            froms,
            tos,
            contents,
            mark=False,
            callback=callback,
            callback_error=callback_error,
        )

    def relay_postmaster(self, reply_to, context, exception):
        # validates that the base information required for
        # postmaster processing is available, meaning that
        # a reply to address is present and the postmaster
        # email was defined for the server
        if not reply_to:
            return
        if not self.postmaster:
            return

        # tries to extract both the main message and the details
        # from the information available from the exception
        message = exception.message if hasattr(exception, "message") else str(exception)
        details = (
            exception.details
            if (
                hasattr(exception, "details")
                and isinstance(exception.details, (list, tuple))
            )
            else []
        )

        # builds the base sender and receiver information for
        # the postmaster email to be sent
        froms = (self.postmaster,)
        tos = (reply_to,)
        first = froms[0]

        # builds the contents of the message, using the extracted
        # exception information
        tos_s = ",".join(context.get("tos", []))
        contents_o = context.get("contents", [])
        subject = "Delivery Status Notification (Failure) - %s" % tos_s
        contents_l = []
        contents_l.append("Subject: %s\r\n\r\n" % subject)
        contents_l.append("%s\r\n" % subject)
        contents_l.append("Message: %s\r\n" % message)
        contents_l.append("Details: %s\r\n\r\n" % ("\n".join(details) or "-"))
        contents_l.append(
            "----- Original message -----\r\n\r\n%s" % netius.legacy.str(contents_o)
        )
        contents = "".join(contents_l)

        # builds a new SMTP client that is going to be used
        # for the postmaster operation, ensures that the
        # correct contents are set in the message (including DKIM)
        smtp_client = netius.clients.SMTPClient(host=self.host)
        contents = smtp_client.comply(
            contents, froms=froms, tos=tos, message_id=self.message_id(email=first)
        )
        contents = smtp_client.mark(contents)
        contents = netius.legacy.bytes(contents)
        contents = self.dkim_contents(contents, email=first)
        smtp_client.message(froms, tos, contents, mark=False)

    def date(self):
        date_time = datetime.datetime.utcnow()
        return date_time.strftime("%a, %d %b %Y %H:%M:%S +0000")

    def message_id(self, connection=None, email="user@localhost"):
        _user, domain = email.split("@", 1)
        domain = self.host or domain
        identifier = str(uuid.uuid4())
        identifier = netius.legacy.bytes(identifier)
        identifier = hashlib.sha1(identifier).hexdigest()
        identifier = identifier.upper()
        if connection and connection.identifier:
            identifier = connection.identifier
        return "<%s@%s>" % (identifier, domain)

    def dkim_contents(self, contents, email="user@localhost", creation=None):
        _user, domain = email.split("@", 1)
        register = self.dkim.get(domain, None)
        if not register:
            return contents

        key_path = register.get("key", None)
        key_b64 = register.get("key_b64", None)
        selector = register["selector"]
        domain = register["domain"]

        contents = contents.lstrip()

        if key_path:
            private_key = netius.common.open_private_key(key_path)
        elif key_b64:
            private_key = netius.common.open_private_key_b64(key_b64)
        else:
            raise netius.SecurityError("No private key provided")

        signature = netius.common.dkim_sign(
            contents, selector, domain, private_key, identity=email, creation=creation
        )

        return signature + contents


if __name__ == "__main__":
    import logging

    server = RelaySMTPServer(level=logging.DEBUG)
    server.serve(env=True)
else:
    __path__ = []
