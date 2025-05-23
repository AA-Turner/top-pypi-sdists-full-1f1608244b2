from __future__ import annotations

import pytest
import binascii
import contextlib
import io
import time
from typing import List, Tuple

from qh3 import tls
from qh3._hazmat import Buffer, encode_uint_var
from qh3._compat import UINT_VAR_MAX
from qh3.quic import events
from qh3.quic.configuration import QuicConfiguration
from qh3.quic.connection import (
    STREAM_COUNT_MAX,
    MAX_PENDING_CRYPTO,
    NetworkAddress,
    QuicConnection,
    QuicConnectionError,
    QuicNetworkPath,
    QuicReceiveContext,
    MAX_LOCAL_CHALLENGES,
    check_stream_id_for_receiving,
    check_stream_id_for_sending,
)
from qh3.quic.crypto import CryptoPair
from qh3.quic.logger import QuicLogger
from qh3.quic.packet import (
    QuicErrorCode,
    QuicFrameType,
    QuicPacketType,
    QuicProtocolVersion,
    QuicTransportParameters,
    QuicVersionInformation,
    encode_quic_retry,
    encode_quic_version_negotiation,
    push_quic_transport_parameters,
)
from qh3.quic.packet_builder import QuicDeliveryState, QuicPacketBuilder
from qh3.quic.recovery import K_MAX_DATAGRAM_SIZE, K_SECOND, K_MICRO_SECOND

from .utils import (
    SERVER_CACERTFILE,
    SERVER_CERTFILE,
    SERVER_CERTFILE_WITH_CHAIN,
    SERVER_KEYFILE,
    SKIP_TESTS,
)

CLIENT_ADDR = ("1.2.3.4", 1234)
CLIENT_HANDSHAKE_DATAGRAM_SIZES = [1280]

SERVER_ADDR = ("2.3.4.5", 4433)
SERVER_INITIAL_DATAGRAM_SIZES = [1280, 1280, 890]

HANDSHAKE_COMPLETED_EVENTS = [
    events.HandshakeCompleted,
    events.ConnectionIdIssued,
    events.ConnectionIdIssued,
    events.ConnectionIdIssued,
    events.ConnectionIdIssued,
    events.ConnectionIdIssued,
    events.ConnectionIdIssued,
    events.ConnectionIdIssued,
]

TICK = 0.05  # seconds


class SessionTicketStore:
    def __init__(self):
        self.tickets = {}

    def add(self, ticket):
        self.tickets[ticket.ticket] = ticket

    def pop(self, label):
        return self.tickets.pop(label, None)


class QuicPacketPacer:
    def __init__(self) -> None:
        self.bucket_max: float = 0.0
        self.bucket_time: float = 0.0
        self.evaluation_time: float = 0.0
        self.packet_time: float | None = None

    def next_send_time(self, now: float) -> float | None:
        if self.packet_time is not None:
            self.update_bucket(now=now)
            if self.bucket_time <= 0:
                return now + self.packet_time
        return None

    def update_after_send(self, now: float) -> None:
        if self.packet_time is not None:
            self.update_bucket(now=now)
            if self.bucket_time < self.packet_time:
                self.bucket_time = 0.0
            else:
                self.bucket_time -= self.packet_time

    def update_bucket(self, now: float) -> None:
        if now > self.evaluation_time:
            self.bucket_time = min(
                self.bucket_time + (now - self.evaluation_time), self.bucket_max
            )
            self.evaluation_time = now

    def update_rate(self, congestion_window: int, smoothed_rtt: float) -> None:
        pacing_rate = congestion_window / max(smoothed_rtt, K_MICRO_SECOND)
        self.packet_time = max(
            K_MICRO_SECOND, min(K_MAX_DATAGRAM_SIZE / pacing_rate, K_SECOND)
        )

        self.bucket_max = (
            max(
                2 * K_MAX_DATAGRAM_SIZE,
                min(congestion_window // 4, 16 * K_MAX_DATAGRAM_SIZE),
            )
            / pacing_rate
        )
        if self.bucket_time > self.bucket_max:
            self.bucket_time = self.bucket_max


def client_receive_context(client, epoch=tls.Epoch.ONE_RTT):
    return QuicReceiveContext(
        epoch=epoch,
        host_cid=client.host_cid,
        network_path=client._network_paths[0],
        quic_logger_frames=[],
        time=time.time(),
        version=None,
    )


def consume_events(connection):
    while True:
        event = connection.next_event()
        if event is None:
            break


def create_standalone_client(self, **client_options):
    client = QuicConnection(
        configuration=QuicConfiguration(
            is_client=True, quic_logger=QuicLogger(), **client_options
        )
    )
    client._ack_delay = 0

    # kick-off handshake
    client.connect(SERVER_ADDR, now=time.time())
    assert drop(client) == 2

    return client


def create_standalone_server(self, original_destination_connection_id=bytes(8)):
    server_configuration = QuicConfiguration(is_client=False, quic_logger=QuicLogger())
    server_configuration.load_cert_chain(SERVER_CERTFILE, SERVER_KEYFILE)

    server = QuicConnection(
        configuration=server_configuration,
        original_destination_connection_id=original_destination_connection_id,
    )
    server._ack_delay = 0

    return server


def datagram_sizes(items: List[Tuple[bytes, NetworkAddress]]) -> List[int]:
    return [len(x[0]) for x in items]


def new_connection_id(
    *,
    sequence_number: int,
    retire_prior_to: int = 0,
    connection_id: bytes = bytes(8),
    capacity: int = 100,
):
    buf = Buffer(capacity=capacity)
    buf.push_uint_var(sequence_number)
    buf.push_uint_var(retire_prior_to)
    buf.push_uint_var(len(connection_id))
    buf.push_bytes(connection_id)
    buf.push_bytes(bytes(16))  # stateless reset token
    buf.seek(0)
    return buf


@contextlib.contextmanager
def client_and_server(
    client_kwargs={},
    client_options={},
    client_patch=lambda x: None,
    handshake=True,
    server_kwargs={},
    server_certfile=SERVER_CERTFILE,
    server_keyfile=SERVER_KEYFILE,
    server_options={},
    server_patch=lambda x: None,
):
    client_configuration = QuicConfiguration(
        is_client=True, quic_logger=QuicLogger(), **client_options
    )
    client_configuration.load_verify_locations(cafile=SERVER_CACERTFILE)

    client = QuicConnection(configuration=client_configuration, **client_kwargs)
    client._ack_delay = 0
    disable_packet_pacing(client)
    client_patch(client)

    server_configuration = QuicConfiguration(
        is_client=False, quic_logger=QuicLogger(), **server_options
    )
    server_configuration.load_cert_chain(server_certfile, server_keyfile)

    server = QuicConnection(
        configuration=server_configuration,
        original_destination_connection_id=client.original_destination_connection_id,
        **server_kwargs,
    )
    server._ack_delay = 0
    disable_packet_pacing(server)
    server_patch(server)

    # perform handshake
    if handshake:
        client.connect(SERVER_ADDR, now=time.time())
        for i in range(3):
            roundtrip(client, server)

    yield client, server

    # close
    client.close()
    server.close()


def disable_packet_pacing(connection):
    class DummyPacketPacer(QuicPacketPacer):
        def next_send_time(self, now):
            return None

    connection._loss._pacer = DummyPacketPacer()


def encode_transport_parameters(parameters: QuicTransportParameters) -> bytes:
    buf = Buffer(capacity=512)
    push_quic_transport_parameters(buf, parameters)
    return buf.data


def sequence_numbers(connection_ids):
    return list(map(lambda x: x.sequence_number, connection_ids))


def drop(sender):
    """
    Drop datagrams from `sender`.
    """
    return len(sender.datagrams_to_send(now=time.time()))


def roundtrip(sender, receiver):
    """
    Send datagrams from `sender` to `receiver` and back.
    """
    return (transfer(sender, receiver), transfer(receiver, sender))


def transfer(sender, receiver):
    """
    Send datagrams from `sender` to `receiver`.
    """
    datagrams = 0
    from_addr = CLIENT_ADDR if sender._is_client else SERVER_ADDR
    for data, addr in sender.datagrams_to_send(now=time.time()):
        datagrams += 1
        receiver.receive_datagram(data, from_addr, now=time.time())
    return datagrams


class TestQuicConnection:
    def assertEvents(self, connection: QuicConnection, expected: list):
        types = []
        while True:
            event = connection.next_event()
            if event is not None:
                types.append(type(event))
            else:
                break

        assert types == expected

    def assertPacketDropped(self, connection: QuicConnection, trigger: str):
        log = connection.configuration.quic_logger.to_dict()
        found_trigger = None
        for event in log["traces"][0]["events"]:
            if event["name"] == "transport:packet_dropped":
                found_trigger = event["data"]["trigger"]
                break
        assert found_trigger == trigger

    def assertSentPackets(self, connection: QuicConnection, expected: List[int]):
        counts = [len(space.sent_packets) for space in connection._loss.spaces]
        assert counts == expected

    def check_handshake(self, client, server, alpn_protocol=None):
        """
        Check handshake completed.
        """
        event = client.next_event()
        assert type(event) == events.ProtocolNegotiated
        assert event.alpn_protocol == alpn_protocol
        event = client.next_event()
        assert type(event) == events.HandshakeCompleted
        assert event.alpn_protocol == alpn_protocol
        assert event.early_data_accepted == False
        assert event.session_resumed == False
        for i in range(7):
            assert type(client.next_event()) == events.ConnectionIdIssued
        assert client.next_event() is None

        event = server.next_event()
        assert type(event) == events.ProtocolNegotiated
        assert event.alpn_protocol == alpn_protocol
        event = server.next_event()
        assert type(event) == events.HandshakeCompleted
        assert event.alpn_protocol == alpn_protocol
        for i in range(7):
            assert type(server.next_event()) == events.ConnectionIdIssued
        assert server.next_event() is None

    def test_connect(self):
        with client_and_server() as (client, server):
            # check handshake completed
            self.check_handshake(client=client, server=server)

            # check each endpoint has available connection IDs for the peer
            assert sequence_numbers(client._peer_cid_available) == [1, 2, 3, 4, 5, 6, 7]
            assert sequence_numbers(server._peer_cid_available) == [1, 2, 3, 4, 5, 6, 7]

            # client closes the connection
            client.close()
            assert transfer(client, server) == 1

            # check connection closes on the client side
            client.handle_timer(client.get_timer())
            event = client.next_event()
            assert type(event) == events.ConnectionTerminated
            assert event.error_code == QuicErrorCode.NO_ERROR
            assert event.frame_type == None
            assert event.reason_phrase == ""
            assert client.next_event() is None

            # check connection closes on the server side
            server.handle_timer(server.get_timer())
            event = server.next_event()
            assert type(event) == events.ConnectionTerminated
            assert event.error_code == QuicErrorCode.NO_ERROR
            assert event.frame_type == None
            assert event.reason_phrase == ""
            assert server.next_event() is None

            # check client log
            client_log = client.configuration.quic_logger.to_dict()
            assert len(client_log["traces"][0]["events"]) > 20

            # check server log
            server_log = server.configuration.quic_logger.to_dict()
            assert len(server_log["traces"][0]["events"]) > 20

    def test_connect_with_alpn(self):
        with client_and_server(
            client_options={"alpn_protocols": ["h3-25", "hq-25"]},
            server_options={"alpn_protocols": ["hq-25"]},
        ) as (client, server):
            # check handshake completed
            self.check_handshake(client=client, server=server, alpn_protocol="hq-25")

    def test_connect_with_secrets_log(self):
        client_log_file = io.StringIO()
        server_log_file = io.StringIO()
        with client_and_server(
            client_options={"secrets_log_file": client_log_file},
            server_options={"secrets_log_file": server_log_file},
        ) as (client, server):
            # check handshake completed
            self.check_handshake(client=client, server=server)

            # check secrets were logged
            client_log = client_log_file.getvalue()
            server_log = server_log_file.getvalue()
            assert client_log == server_log
            labels = []
            for line in client_log.splitlines():
                labels.append(line.split()[0])
            assert labels == \
                [
                    "SERVER_HANDSHAKE_TRAFFIC_SECRET",
                    "CLIENT_HANDSHAKE_TRAFFIC_SECRET",
                    "SERVER_TRAFFIC_SECRET_0",
                    "CLIENT_TRAFFIC_SECRET_0",
                ]

    def test_connect_with_cert_chain(self):
        with client_and_server(server_certfile=SERVER_CERTFILE_WITH_CHAIN) as (
            client,
            server,
        ):
            # check handshake completed
            self.check_handshake(client=client, server=server)

    def test_connect_with_cipher_suite_aes128(self):
        with client_and_server(
            client_options={"cipher_suites": [tls.CipherSuite.AES_128_GCM_SHA256]}
        ) as (client, server):
            # check handshake completed
            self.check_handshake(client=client, server=server)

            # check selected cipher suite
            assert client.tls.key_schedule.cipher_suite == tls.CipherSuite.AES_128_GCM_SHA256
            assert server.tls.key_schedule.cipher_suite == tls.CipherSuite.AES_128_GCM_SHA256

    def test_connect_with_cipher_suite_aes256(self):
        with client_and_server(
            client_options={"cipher_suites": [tls.CipherSuite.AES_256_GCM_SHA384]}
        ) as (client, server):
            # check handshake completed
            self.check_handshake(client=client, server=server)

            # check selected cipher suite
            assert client.tls.key_schedule.cipher_suite == tls.CipherSuite.AES_256_GCM_SHA384
            assert server.tls.key_schedule.cipher_suite == tls.CipherSuite.AES_256_GCM_SHA384

    @pytest.mark.skipif("chacha20" in SKIP_TESTS, reason="Skipping chacha20 tests")
    def test_connect_with_cipher_suite_chacha20(self):
        with client_and_server(
            client_options={"cipher_suites": [tls.CipherSuite.CHACHA20_POLY1305_SHA256]}
        ) as (client, server):
            # check handshake completed
            self.check_handshake(client=client, server=server)

            # check selected cipher suite
            assert client.tls.key_schedule.cipher_suite == \
                tls.CipherSuite.CHACHA20_POLY1305_SHA256
            assert server.tls.key_schedule.cipher_suite == \
                tls.CipherSuite.CHACHA20_POLY1305_SHA256

    def test_connect_without_loss(self):
        """
        Check connection is established in the absence of loss.
        """
        with client_and_server(handshake=False) as (client, server):
            # client sends INITIAL
            now = 0.0
            client.connect(SERVER_ADDR, now=now)
            items = client.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [1280, 1280]
            assert client.get_timer() == 0.2
            self.assertSentPackets(client, [2, 0, 0])
            self.assertEvents(client, [])

            # server receives INITIAL, sends INITIAL + HANDSHAKE
            now += TICK
            server.receive_datagram(items[0][0], CLIENT_ADDR, now=now)
            server.receive_datagram(items[1][0], CLIENT_ADDR, now=now)
            items = server.datagrams_to_send(now=now)
            assert datagram_sizes(items) == SERVER_INITIAL_DATAGRAM_SIZES
            assert server.get_timer() == pytest.approx(0.25)
            self.assertSentPackets(server, [1, 2, 0])
            self.assertEvents(server, [events.ProtocolNegotiated])

            # handshake continues normally
            now += TICK
            client.receive_datagram(items[0][0], SERVER_ADDR, now=now)
            client.receive_datagram(items[1][0], SERVER_ADDR, now=now)
            client.receive_datagram(items[2][0], SERVER_ADDR, now=now)
            items = client.datagrams_to_send(now=now)
            assert datagram_sizes(items) == CLIENT_HANDSHAKE_DATAGRAM_SIZES
            assert client.get_timer() == pytest.approx(0.425)
            self.assertSentPackets(client, [0, 1, 1])
            self.assertEvents(
                client, [events.ProtocolNegotiated] + HANDSHAKE_COMPLETED_EVENTS
            )

            now += TICK
            server.receive_datagram(items[0][0], CLIENT_ADDR, now=now)
            items = server.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [229]
            assert server.get_timer() == pytest.approx(0.425)
            self.assertSentPackets(server, [0, 0, 1])
            self.assertEvents(server, HANDSHAKE_COMPLETED_EVENTS)

            now += TICK
            client.receive_datagram(items[0][0], SERVER_ADDR, now=now)
            items = client.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [32]
            # idle timeout
            assert client.get_timer() == pytest.approx(60.2)
            self.assertSentPackets(client, [0, 0, 1])
            self.assertEvents(client, [])
    
    def test_connect_with_loss_1(self):
        """
        Check connection is established even in the client's INITIAL is lost.

        The client's PTO fires, triggering retransmission.
        """

        with client_and_server(handshake=False) as (client, server):
            # client sends INITIAL
            now = 0.0
            client.connect(SERVER_ADDR, now=now)
            items = client.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [1280, 1280]
            assert client.get_timer() == 0.2
            self.assertSentPackets(client, [2, 0, 0])
            self.assertEvents(client, [])

            # INITIAL is lost and retransmitted
            now = client.get_timer()
            client.handle_timer(now=now)
            items = client.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [1280, 1280]
            assert client.get_timer() == pytest.approx(0.6)
            self.assertSentPackets(client, [2, 0, 0])
            self.assertEvents(client, [])

            # server receives INITIAL, sends INITIAL + HANDSHAKE
            now += TICK
            server.receive_datagram(items[0][0], CLIENT_ADDR, now=now)
            server.receive_datagram(items[1][0], CLIENT_ADDR, now=now)
            items = server.datagrams_to_send(now=now)
            assert datagram_sizes(items) == SERVER_INITIAL_DATAGRAM_SIZES
            assert server.get_timer() == pytest.approx(0.45)
            self.assertSentPackets(server, [1, 2, 0])
            self.assertEvents(server, [events.ProtocolNegotiated])

            # handshake continues normally
            now += TICK
            client.receive_datagram(items[0][0], SERVER_ADDR, now=now)
            client.receive_datagram(items[1][0], SERVER_ADDR, now=now)
            client.receive_datagram(items[2][0], SERVER_ADDR, now=now)
            items = client.datagrams_to_send(now=now)
            assert datagram_sizes(items) == CLIENT_HANDSHAKE_DATAGRAM_SIZES
            assert client.get_timer() == pytest.approx(0.625)
            self.assertSentPackets(client, [0, 1, 1])
            self.assertEvents(
                client, [events.ProtocolNegotiated] + HANDSHAKE_COMPLETED_EVENTS
            )

            now += TICK
            server.receive_datagram(items[0][0], CLIENT_ADDR, now=now)
            items = server.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [229]
            assert server.get_timer() == pytest.approx(0.625)
            self.assertSentPackets(server, [0, 0, 1])
            self.assertEvents(server, HANDSHAKE_COMPLETED_EVENTS)

            now += TICK
            client.receive_datagram(items[0][0], SERVER_ADDR, now=now)
            items = client.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [32]
            # idle timeout
            assert client.get_timer() == pytest.approx(60.4)
            self.assertSentPackets(client, [0, 0, 1])
            self.assertEvents(client, [])

    def test_connect_with_loss_2(self):
        """
        Check connection is established even in the server's INITIAL is lost.

        The client receives HANDSHAKE packets before it has the corresponding keys
        and decides to retransmit its own CRYPTO to speedup handshake completion.
        """

        with client_and_server(handshake=False) as (client, server):
            # client sends INITIAL
            now = 0.0
            client.connect(SERVER_ADDR, now=now)
            items = client.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [1280, 1280]
            assert client.get_timer() == 0.2
            self.assertSentPackets(client, [2, 0, 0])
            self.assertEvents(client, [])

            # server receives INITIAL, sends INITIAL + HANDSHAKE but first datagram
            # is lost
            now += TICK
            server.receive_datagram(items[0][0], CLIENT_ADDR, now=now)
            server.receive_datagram(items[1][0], CLIENT_ADDR, now=now)
            items = server.datagrams_to_send(now=now)
            assert datagram_sizes(items) == SERVER_INITIAL_DATAGRAM_SIZES
            assert server.get_timer() == 0.25
            self.assertSentPackets(server, [1, 2, 0])
            self.assertEvents(server, [events.ProtocolNegotiated])

            # client only receives second datagram, retransmits INITIAL
            now += TICK
            client.receive_datagram(items[1][0], SERVER_ADDR, now=now)
            items = client.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [1280, 1280]
            assert client.get_timer() == pytest.approx(0.3)
            self.assertSentPackets(client, [2, 0, 0])
            self.assertEvents(client, [])

            self.assertPacketDropped(client, "key_unavailable")

            # server receives duplicate INITIAL, retransmits INITIAL + HANDSHAKE
            now += TICK
            server.receive_datagram(items[0][0], CLIENT_ADDR, now=now)
            server.receive_datagram(items[1][0], CLIENT_ADDR, now=now)
            items = server.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [1280, 1280, 890]
            # self.assertAlmostEqual(server.get_timer(), 0.35)
            self.assertSentPackets(server, [1, 2, 0])
            self.assertEvents(server, [])

            # handshake continues normally
            now += TICK
            client.receive_datagram(items[0][0], SERVER_ADDR, now=now)
            client.receive_datagram(items[1][0], SERVER_ADDR, now=now)
            client.receive_datagram(items[2][0], SERVER_ADDR, now=now)
            items = client.datagrams_to_send(now=now)
            assert datagram_sizes(items) == CLIENT_HANDSHAKE_DATAGRAM_SIZES
            # self.assertAlmostEqual(client.get_timer(), 0.525)
            self.assertSentPackets(client, [0, 1, 1])
            self.assertEvents(
                client, [events.ProtocolNegotiated] + HANDSHAKE_COMPLETED_EVENTS
            )

            now += TICK
            server.receive_datagram(items[0][0], CLIENT_ADDR, now=now)
            items = server.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [229]
            # self.assertAlmostEqual(server.get_timer(), 0.525)
            self.assertSentPackets(server, [0, 0, 1])
            self.assertEvents(server, HANDSHAKE_COMPLETED_EVENTS)

            now += TICK
            client.receive_datagram(items[0][0], SERVER_ADDR, now=now)
            items = client.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [32]
            # idle timeout
            assert client.get_timer() == pytest.approx(60.3)
            self.assertSentPackets(client, [0, 0, 1])
            self.assertEvents(client, [])

    def test_connect_with_loss_3(self):
        """
        Check connection is established even in the server's INITIAL + HANDSHAKE are
        lost.

        The server receives duplicate CRYPTO and decides to retransmit its own
        CRYPTO to speedup handshake completion.
        """

        with client_and_server(handshake=False) as (client, server):
            # client sends INITIAL
            now = 0.0
            client.connect(SERVER_ADDR, now=now)
            items = client.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [1280, 1280]
            assert client.get_timer() == 0.2
            self.assertSentPackets(client, [2, 0, 0])
            self.assertEvents(client, [])

            # server receives INITIAL, sends INITIAL + HANDSHAKE
            now += TICK
            server.receive_datagram(items[0][0], CLIENT_ADDR, now=now)
            server.receive_datagram(items[1][0], CLIENT_ADDR, now=now)
            items = server.datagrams_to_send(now=now)
            assert datagram_sizes(items) == SERVER_INITIAL_DATAGRAM_SIZES
            assert server.get_timer() == 0.25
            self.assertSentPackets(server, [1, 2, 0])
            self.assertEvents(server, [events.ProtocolNegotiated])

            # INITIAL + HANDSHAKE are lost, client retransmits INITIAL
            now = client.get_timer()
            client.handle_timer(now=now)
            items = client.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [1280, 1280]
            assert client.get_timer() == pytest.approx(0.6)
            self.assertSentPackets(client, [2, 0, 0])
            self.assertEvents(client, [])

            # server receives duplicate INITIAL, retransmits INITIAL + HANDSHAKE
            now += TICK
            server.receive_datagram(items[0][0], CLIENT_ADDR, now=now)
            server.receive_datagram(items[1][0], CLIENT_ADDR, now=now)
            items = server.datagrams_to_send(now=now)
            assert datagram_sizes(items) == SERVER_INITIAL_DATAGRAM_SIZES
            assert server.get_timer() == 0.45
            self.assertSentPackets(server, [1, 2, 0])
            self.assertEvents(server, [])

            # handshake continues normally
            now += TICK
            client.receive_datagram(items[0][0], SERVER_ADDR, now=now)
            client.receive_datagram(items[1][0], SERVER_ADDR, now=now)
            client.receive_datagram(items[2][0], SERVER_ADDR, now=now)
            items = client.datagrams_to_send(now=now)
            assert datagram_sizes(items) == CLIENT_HANDSHAKE_DATAGRAM_SIZES
            assert client.get_timer() >= 0.5
            assert client.get_timer() <= 0.63
            self.assertSentPackets(client, [0, 1, 1])
            self.assertEvents(
                client, [events.ProtocolNegotiated] + HANDSHAKE_COMPLETED_EVENTS
            )

            now += TICK
            server.receive_datagram(items[0][0], CLIENT_ADDR, now=now)
            items = server.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [229]
            assert server.get_timer() == pytest.approx(0.625)
            self.assertSentPackets(server, [0, 0, 1])
            self.assertEvents(server, HANDSHAKE_COMPLETED_EVENTS)

            now += TICK
            client.receive_datagram(items[0][0], SERVER_ADDR, now=now)
            items = client.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [32]
            # idle timeout
            assert client.get_timer() == pytest.approx(60.4)
            self.assertSentPackets(client, [0, 0, 1])
            self.assertEvents(client, [])

    def test_connect_with_loss_4(self):
        """
        Check connection is established even in the server's HANDSHAKE is lost.
        """
        with client_and_server(handshake=False) as (client, server):
            # client sends INITIAL
            now = 0.0
            client.connect(SERVER_ADDR, now=now)
            items = client.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [1280, 1280]
            assert client.get_timer() == 0.2
            self.assertSentPackets(client, [2, 0, 0])
            self.assertEvents(client, [])

            # server receives INITIAL, sends ACK + INITIAL + HANDSHAKE but third
            # datagram is lost
            now += TICK
            server.receive_datagram(items[0][0], CLIENT_ADDR, now=now)
            server.receive_datagram(items[1][0], CLIENT_ADDR, now=now)
            items = server.datagrams_to_send(now=now)
            assert datagram_sizes(items) == SERVER_INITIAL_DATAGRAM_SIZES
            assert server.get_timer() == 0.25
            self.assertSentPackets(server, [1, 2, 0])
            self.assertEvents(server, [events.ProtocolNegotiated])

            # client only receives the first datagram and sends ACKS
            now += TICK
            client.receive_datagram(items[0][0], SERVER_ADDR, now=now)
            client.receive_datagram(items[1][0], SERVER_ADDR, now=now)
            items = client.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [1280]
            assert client.get_timer() == pytest.approx(0.325)
            self.assertSentPackets(client, [0, 1, 0])
            self.assertEvents(client, [events.ProtocolNegotiated])

            # client PTO - HANDSHAKE PING
            now = client.get_timer()
            client.handle_timer(now=now)
            items = client.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [45]
            assert client.get_timer() == pytest.approx(0.975)
            self.assertSentPackets(client, [0, 2, 0])
            self.assertEvents(client, [])

            # server receives PING, discards INITIAL and sends ACK
            now += TICK
            server.receive_datagram(items[0][0], CLIENT_ADDR, now=now)
            items = server.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [48]
            assert server.get_timer() == pytest.approx(0.25)
            self.assertSentPackets(server, [0, 3, 0])
            self.assertEvents(server, [])

            # ACKs are lost, server retransmits HANDSHAKE
            now = server.get_timer()
            server.handle_timer(now=now)
            items = server.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [1280, 890]
            assert server.get_timer() == pytest.approx(0.65)
            self.assertSentPackets(server, [0, 3, 0])
            self.assertEvents(server, [])

            # handshake continues normally
            now += TICK
            client.receive_datagram(items[0][0], SERVER_ADDR, now=now)
            client.receive_datagram(items[1][0], SERVER_ADDR, now=now)
            items = client.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [313]
            assert client.get_timer() == pytest.approx(0.95)
            self.assertSentPackets(client, [0, 3, 1])
            self.assertEvents(client, HANDSHAKE_COMPLETED_EVENTS)

            now += TICK
            server.receive_datagram(items[0][0], CLIENT_ADDR, now=now)
            items = server.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [229]
            assert server.get_timer() == pytest.approx(0.675)
            self.assertSentPackets(server, [0, 0, 1])
            self.assertEvents(server, HANDSHAKE_COMPLETED_EVENTS)

            now += TICK
            client.receive_datagram(items[0][0], SERVER_ADDR, now=now)
            items = client.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [32]
            # idle timeout
            assert client.get_timer() == pytest.approx(60.4)
            self.assertSentPackets(client, [0, 0, 1])
            self.assertEvents(client, [])

    def test_connect_with_loss_5(self):
        """
        Check connection is established even in the server's HANDSHAKE_DONE is lost.
        """
        with client_and_server(handshake=False) as (client, server):
            # client sends INITIAL
            now = 0.0
            client.connect(SERVER_ADDR, now=now)
            items = client.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [1280, 1280]
            assert client.get_timer() == 0.2

            # server receives INITIAL, sends INITIAL + HANDSHAKE
            now += TICK
            server.receive_datagram(items[0][0], CLIENT_ADDR, now=now)
            server.receive_datagram(items[1][0], CLIENT_ADDR, now=now)
            items = server.datagrams_to_send(now=now)
            assert datagram_sizes(items) == SERVER_INITIAL_DATAGRAM_SIZES
            assert server.get_timer() == 0.25
            self.assertSentPackets(server, [1, 2, 0])
            self.assertEvents(server, [events.ProtocolNegotiated])

            # client receives INITIAL + HANDSHAKE
            now += TICK
            client.receive_datagram(items[0][0], SERVER_ADDR, now=now)
            client.receive_datagram(items[1][0], SERVER_ADDR, now=now)
            client.receive_datagram(items[2][0], SERVER_ADDR, now=now)
            items = client.datagrams_to_send(now=now)
            assert datagram_sizes(items) == CLIENT_HANDSHAKE_DATAGRAM_SIZES
            assert client.get_timer() == pytest.approx(0.425)
            self.assertSentPackets(client, [0, 1, 1])
            self.assertEvents(
                client, [events.ProtocolNegotiated] + HANDSHAKE_COMPLETED_EVENTS
            )

            # server completes handshake, but HANDSHAKE_DONE is lost
            now += TICK
            server.receive_datagram(items[0][0], CLIENT_ADDR, now=now)
            items = server.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [229]
            assert server.get_timer() == pytest.approx(0.425)
            self.assertSentPackets(server, [0, 0, 1])
            self.assertEvents(server, HANDSHAKE_COMPLETED_EVENTS)

            # server PTO - 1-RTT PING
            now = server.get_timer()
            server.handle_timer(now=now)
            items = server.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [29]
            assert server.get_timer() == pytest.approx(0.975)
            self.assertSentPackets(server, [0, 0, 2])
            self.assertEvents(server, [])

            # client receives PING, sends ACK
            now += TICK
            client.receive_datagram(items[0][0], SERVER_ADDR, now=now)
            items = client.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [32]
            assert client.get_timer() == pytest.approx(0.425)
            self.assertSentPackets(client, [0, 1, 2])
            self.assertEvents(client, [])

            # server receives ACK, retransmits HANDSHAKE_DONE
            now += TICK
            assert not server._handshake_done_pending
            server.receive_datagram(items[0][0], CLIENT_ADDR, now=now)
            assert server._handshake_done_pending
            items = server.datagrams_to_send(now=now)
            assert not server._handshake_done_pending
            assert datagram_sizes(items) == [224]
            assert server.get_timer() == pytest.approx(0.7625)
            self.assertSentPackets(server, [0, 0, 1])
            # FIXME: the server re-emits the ConnectionIdIssued events
            self.assertEvents(server, HANDSHAKE_COMPLETED_EVENTS[1:])

            now += TICK
            client.receive_datagram(items[0][0], SERVER_ADDR, now=now)
            items = client.datagrams_to_send(now=now)
            assert datagram_sizes(items) == [32]
            assert client.get_timer() == pytest.approx(0.425)
            self.assertSentPackets(client, [0, 0, 3])
            self.assertEvents(client, [])

            now += TICK
            server.receive_datagram(items[0][0], CLIENT_ADDR, now=now)
            items = server.datagrams_to_send(now=now)
            assert datagram_sizes(items) == []
            # idle timeout
            assert server.get_timer() == pytest.approx(60.625)
            self.assertSentPackets(server, [0, 0, 0])
            self.assertEvents(server, [])

    def test_connect_with_no_transport_parameters(self):
        real_initialize = QuicConnection._initialize

        def patched_initialize(self, peer_cid: bytes):
            real_initialize(self, peer_cid)
            if self._is_client:
                self.tls.handshake_extensions = []

        QuicConnection._initialize = patched_initialize

        try:
            with client_and_server() as (client, server):
                assert server._close_event.reason_phrase == \
                       "No QUIC transport parameters received"
        finally:
            QuicConnection._initialize = real_initialize

    def test_connect_with_compatible_version_negotiation_1(self):
        """
        The client only supports version 1.

        The server sets the Negotiated Version to version 1.
        """
        with client_and_server(
                client_options={
                    "supported_versions": [QuicProtocolVersion.VERSION_1],
                },
        ) as (client, server):
            # check handshake completed
            self.check_handshake(client=client, server=server)
            assert client._version == QuicProtocolVersion.VERSION_1
            assert server._version == QuicProtocolVersion.VERSION_1

    def test_connect_with_compatible_version_negotiation_1_to_2(self):
        """
        The client originally connects using version 1 but prefers version 2.

        The server sets the Negotiated Version to version 2.
        """
        with client_and_server(
                client_options={
                    "original_version": QuicProtocolVersion.VERSION_1,
                    "supported_versions": [
                        QuicProtocolVersion.VERSION_2,
                        QuicProtocolVersion.VERSION_1,
                    ],
                },
        ) as (client, server):
            # check handshake completed
            self.check_handshake(client=client, server=server)
            assert client._version == QuicProtocolVersion.VERSION_2
            assert server._version == QuicProtocolVersion.VERSION_2

    def test_connect_with_compatible_version_negotiation_2(self):
        """
        The client only supports version 2.

        The server sets the Negotiated Version to version 2.
        """
        with client_and_server(
                client_options={
                    "supported_versions": [QuicProtocolVersion.VERSION_2],
                },
        ) as (client, server):
            # check handshake completed
            self.check_handshake(client=client, server=server)
            assert client._version == QuicProtocolVersion.VERSION_2
            assert server._version == QuicProtocolVersion.VERSION_2

    def test_connect_with_compatible_version_negotiation_2_to_1(self):
        """
        The client originally connects using version 2 but prefers version 1.

        The server sets the Negotiated Version to version 1.
        """
        with client_and_server(
                client_options={
                    "original_version": QuicProtocolVersion.VERSION_2,
                    "supported_versions": [
                        QuicProtocolVersion.VERSION_1,
                        QuicProtocolVersion.VERSION_2,
                    ],
                },
        ) as (client, server):
            # check handshake completed
            self.check_handshake(client=client, server=server)
            assert client._version == QuicProtocolVersion.VERSION_1
            assert server._version == QuicProtocolVersion.VERSION_1

    def test_connect_with_quantum_readiness(self):
        with client_and_server(client_options={"quantum_readiness_test": True}) as (
            client,
            server,
        ):
            stream_id = client.get_next_available_stream_id()
            client.send_stream_data(stream_id, b"hello")

            assert roundtrip(client, server) == (1, 1)

            received = None
            while True:
                event = server.next_event()
                if isinstance(event, events.StreamDataReceived):
                    received = event.data
                elif event is None:
                    break

            assert received == b"hello"

    def test_connect_with_0rtt(self):
        client_ticket = None
        ticket_store = SessionTicketStore()

        def save_session_ticket(ticket):
            nonlocal client_ticket
            client_ticket = ticket

        with client_and_server(
            client_kwargs={"session_ticket_handler": save_session_ticket},
            server_kwargs={"session_ticket_handler": ticket_store.add},
        ) as (client, server):
            pass

        with client_and_server(
            client_options={"session_ticket": client_ticket},
            server_kwargs={"session_ticket_fetcher": ticket_store.pop},
            handshake=False,
        ) as (client, server):
            client.connect(SERVER_ADDR, now=time.time())
            stream_id = client.get_next_available_stream_id()
            client.send_stream_data(stream_id, b"hello")

            assert roundtrip(client, server) == (2, 2)

            event = server.next_event()
            assert type(event) == events.ProtocolNegotiated

            event = server.next_event()
            assert type(event) == events.StreamDataReceived
            assert event.data == b"hello"

    def test_connect_with_0rtt_bad_max_early_data(self):
        client_ticket = None
        ticket_store = SessionTicketStore()

        real_initialize = QuicConnection._initialize

        def patched_initialize(self, peer_cid: bytes):
            real_initialize(self, peer_cid)
            if not self._is_client:
                self.tls._max_early_data = 12345

        QuicConnection._initialize = patched_initialize

        def save_session_ticket(ticket):
            nonlocal client_ticket
            client_ticket = ticket

        try:
            with client_and_server(
                    client_kwargs={"session_ticket_handler": save_session_ticket},
                    server_kwargs={"session_ticket_handler": ticket_store.add},
            ) as (client, server):
                # check handshake failed
                event = client.next_event()
                assert event is None
        finally:
            QuicConnection._initialize = real_initialize

    def test_change_connection_id(self):
        with client_and_server() as (client, server):
            assert sequence_numbers(client._peer_cid_available) == [1, 2, 3, 4, 5, 6, 7]

            # the client changes connection ID
            client.change_connection_id()
            assert transfer(client, server) == 1
            assert sequence_numbers(client._peer_cid_available) == [2, 3, 4, 5, 6, 7]

            # the server provides a new connection ID
            assert transfer(server, client) == 1
            assert sequence_numbers(client._peer_cid_available) == [2, 3, 4, 5, 6, 7, 8]

    def test_change_connection_id_retransmit_new_connection_id(self):
        with client_and_server() as (client, server):
            assert sequence_numbers(client._peer_cid_available) == [1, 2, 3, 4, 5, 6, 7]

            # the client changes connection ID
            client.change_connection_id()
            assert transfer(client, server) == 1
            assert sequence_numbers(client._peer_cid_available) == [2, 3, 4, 5, 6, 7]

            # the server provides a new connection ID, NEW_CONNECTION_ID is lost
            assert drop(server) == 1
            assert sequence_numbers(client._peer_cid_available) == [2, 3, 4, 5, 6, 7]

            # NEW_CONNECTION_ID is retransmitted
            server._on_new_connection_id_delivery(
                QuicDeliveryState.LOST, server._host_cids[-1]
            )
            assert transfer(server, client) == 1
            assert sequence_numbers(client._peer_cid_available) == [2, 3, 4, 5, 6, 7, 8]

    def test_change_connection_id_retransmit_retire_connection_id(self):
        with client_and_server() as (client, server):
            assert sequence_numbers(client._peer_cid_available) == [1, 2, 3, 4, 5, 6, 7]

            # the client changes connection ID, RETIRE_CONNECTION_ID is lost
            client.change_connection_id()
            assert drop(client) == 1
            assert sequence_numbers(client._peer_cid_available) == [2, 3, 4, 5, 6, 7]

            # RETIRE_CONNECTION_ID is retransmitted
            client._on_retire_connection_id_delivery(QuicDeliveryState.LOST, 0)
            assert transfer(client, server) == 1

            # the server provides a new connection ID
            assert transfer(server, client) == 1
            assert sequence_numbers(client._peer_cid_available) == [2, 3, 4, 5, 6, 7, 8]

    def test_get_next_available_stream_id(self):
        with client_and_server() as (client, server):
            # client
            stream_id = client.get_next_available_stream_id()
            assert stream_id == 0
            client.send_stream_data(stream_id, b"hello")

            stream_id = client.get_next_available_stream_id()
            assert stream_id == 4
            client.send_stream_data(stream_id, b"hello")

            stream_id = client.get_next_available_stream_id(is_unidirectional=True)
            assert stream_id == 2
            client.send_stream_data(stream_id, b"hello")

            stream_id = client.get_next_available_stream_id(is_unidirectional=True)
            assert stream_id == 6
            client.send_stream_data(stream_id, b"hello")

            # server
            stream_id = server.get_next_available_stream_id()
            assert stream_id == 1
            server.send_stream_data(stream_id, b"hello")

            stream_id = server.get_next_available_stream_id()
            assert stream_id == 5
            server.send_stream_data(stream_id, b"hello")

            stream_id = server.get_next_available_stream_id(is_unidirectional=True)
            assert stream_id == 3
            server.send_stream_data(stream_id, b"hello")

            stream_id = server.get_next_available_stream_id(is_unidirectional=True)
            assert stream_id == 7
            server.send_stream_data(stream_id, b"hello")

    def test_datagram_frame(self):
        with client_and_server(
            client_options={"max_datagram_frame_size": 65536},
            server_options={"max_datagram_frame_size": 65536},
        ) as (client, server):
            # check handshake completed
            self.check_handshake(client=client, server=server, alpn_protocol=None)

            # send datagram
            client.send_datagram_frame(b"hello")
            assert transfer(client, server) == 1

            event = server.next_event()
            assert type(event) == events.DatagramFrameReceived
            assert event.data == b"hello"

    def test_datagram_frame_2(self):
        # payload which exactly fills an entire packet
        payload = b"Z" * 1250

        with client_and_server(
            client_options={"max_datagram_frame_size": 65536},
            server_options={"max_datagram_frame_size": 65536},
        ) as (client, server):
            # check handshake completed
            self.check_handshake(client=client, server=server, alpn_protocol=None)

            # queue 20 datagrams
            for i in range(20):
                client.send_datagram_frame(payload)

            # client can only 11 datagrams are sent due to congestion control
            assert transfer(client, server) == 12
            for i in range(11):
                event = server.next_event()
                assert type(event) == events.DatagramFrameReceived
                assert event.data == payload

            # server sends ACK
            assert transfer(server, client) == 1

            # client sends remaining datagrams
            assert transfer(client, server) == 8
            for i in range(9):
                event = server.next_event()
                assert type(event) == events.DatagramFrameReceived
                assert event.data == payload

    def test_decryption_error(self):
        with client_and_server() as (client, server):
            # mess with encryption key
            server._cryptos[tls.Epoch.ONE_RTT].send.setup(
                cipher_suite=tls.CipherSuite.AES_128_GCM_SHA256,
                secret=bytes(48),
                version=server._version,
            )

            # server sends close
            server.close(error_code=QuicErrorCode.NO_ERROR)
            for data, addr in server.datagrams_to_send(now=time.time()):
                client.receive_datagram(data, SERVER_ADDR, now=time.time())

    def test_tls_error(self):
        real_initialize = QuicConnection._initialize

        def patched_initialize(self, peer_cid: bytes):
            real_initialize(self, peer_cid)
            if self._is_client:
                self.tls._supported_versions = [0x0308]

        QuicConnection._initialize = patched_initialize

        # handshake fails
        try:
            with client_and_server() as (client, server):
                timer_at = server.get_timer()
                server.handle_timer(timer_at)

                event = server.next_event()
                assert type(event) == events.ConnectionTerminated
                assert event.error_code == 326
                assert event.frame_type == QuicFrameType.CRYPTO
                assert event.reason_phrase == "No supported protocol version"
        finally:
            QuicConnection._initialize = real_initialize

    def test_receive_datagram_garbage(self):
        client = create_standalone_client(self)

        datagram = binascii.unhexlify("c00000000080")
        client.receive_datagram(datagram, SERVER_ADDR, now=time.time())

    def test_receive_datagram_reserved_bits_non_zero(self):
        client = create_standalone_client(self)

        builder = QuicPacketBuilder(
            host_cid=client._peer_cid.cid,
            is_client=False,
            peer_cid=client.host_cid,
            version=client._version,
        )
        crypto = CryptoPair()
        crypto.setup_initial(
            client._peer_cid.cid, is_client=False, version=client._version
        )
        CryptoPair.encrypt_packet_real = CryptoPair.encrypt_packet

        def encrypt_packet(self, plain_header, plain_payload, packet_number):
            # mess with reserved bits
            plain_header = bytes([plain_header[0] | 0x0C]) + plain_header[1:]
            return CryptoPair.encrypt_packet_real(
                self, plain_header, plain_payload, packet_number
            )

        CryptoPair.encrypt_packet = encrypt_packet

        builder.start_packet(QuicPacketType.INITIAL, crypto)
        buf = builder.start_frame(QuicFrameType.PADDING)
        buf.push_bytes(bytes(builder.remaining_flight_space))

        for datagram in builder.flush()[0]:
            client.receive_datagram(datagram, SERVER_ADDR, now=time.time())
        assert drop(client) == 1
        assert client._close_event == \
            events.ConnectionTerminated(
                error_code=QuicErrorCode.PROTOCOL_VIOLATION,
                frame_type=QuicFrameType.PADDING,
                reason_phrase="Reserved bits must be zero",
            )

        CryptoPair.encrypt_packet = CryptoPair.encrypt_packet_real
        del CryptoPair.encrypt_packet_real

    def test_receive_datagram_wrong_version(self):
        client = create_standalone_client(self)

        builder = QuicPacketBuilder(
            host_cid=client._peer_cid.cid,
            is_client=False,
            peer_cid=client.host_cid,
            version=0xFF000011,  # DRAFT_16
        )
        crypto = CryptoPair()
        crypto.setup_initial(
            client._peer_cid.cid, is_client=False, version=client._version
        )
        builder.start_packet(QuicPacketType.INITIAL, crypto)
        buf = builder.start_frame(QuicFrameType.PADDING)
        buf.push_bytes(bytes(builder.remaining_flight_space))

        for datagram in builder.flush()[0]:
            client.receive_datagram(datagram, SERVER_ADDR, now=time.time())
        assert drop(client) == 0

        self.assertPacketDropped(client, "unsupported_version")

    def test_receive_datagram_retry(self):
        client = create_standalone_client(self)

        client.receive_datagram(
            encode_quic_retry(
                version=client._version,
                source_cid=binascii.unhexlify("85abb547bf28be97"),
                destination_cid=client.host_cid,
                original_destination_cid=client._peer_cid.cid,
                retry_token=bytes(16),
            ),
            SERVER_ADDR,
            now=time.time(),
        )
        assert drop(client) == 2

    def test_receive_datagram_retry_wrong_destination_cid(self):
        client = create_standalone_client(self)

        client.receive_datagram(
            encode_quic_retry(
                version=client._version,
                source_cid=binascii.unhexlify("85abb547bf28be97"),
                destination_cid=binascii.unhexlify("c98343fe8f5f0ff4"),
                original_destination_cid=client._peer_cid.cid,
                retry_token=bytes(16),
            ),
            SERVER_ADDR,
            now=time.time(),
        )
        assert drop(client) == 0
        self.assertPacketDropped(client, "unknown_connection_id")

    def test_receive_datagram_retry_wrong_integrity_tag(self):
        client = create_standalone_client(self)

        client.receive_datagram(
            encode_quic_retry(
                version=client._version,
                source_cid=binascii.unhexlify("85abb547bf28be97"),
                destination_cid=client.host_cid,
                original_destination_cid=client._peer_cid.cid,
                retry_token=bytes(16),
            )[0:-16]
            + bytes(16),
            SERVER_ADDR,
            now=time.time(),
        )
        assert drop(client) == 0

    def test_handle_ack_frame_ecn(self):
        client = create_standalone_client(self)

        client._handle_ack_frame(
            client_receive_context(client),
            QuicFrameType.ACK_ECN,
            Buffer(data=b"\x00\x02\x00\x00\x00\x00\x00"),
        )

    def test_handle_connection_close_frame(self):
        with client_and_server() as (client, server):
            server.close(
                error_code=QuicErrorCode.PROTOCOL_VIOLATION,
                frame_type=QuicFrameType.ACK,
                reason_phrase="illegal ACK frame",
            )
            assert roundtrip(server, client) == (1, 0)

            assert client._close_event == \
                events.ConnectionTerminated(
                    error_code=QuicErrorCode.PROTOCOL_VIOLATION,
                    frame_type=QuicFrameType.ACK,
                    reason_phrase="illegal ACK frame",
                )

    def test_handle_connection_close_frame_app(self):
        with client_and_server() as (client, server):
            server.close(error_code=QuicErrorCode.NO_ERROR, reason_phrase="goodbye")
            assert roundtrip(server, client) == (1, 0)

            assert client._close_event == \
                events.ConnectionTerminated(
                    error_code=QuicErrorCode.NO_ERROR,
                    frame_type=None,
                    reason_phrase="goodbye",
                )

    def test_handle_connection_close_frame_app_not_utf8(self):
        client = create_standalone_client(self)

        client._handle_connection_close_frame(
            client_receive_context(client),
            QuicFrameType.APPLICATION_CLOSE,
            Buffer(data=binascii.unhexlify("0008676f6f6462798200")),
        )

        assert client._close_event == \
            events.ConnectionTerminated(
                error_code=QuicErrorCode.NO_ERROR,
                frame_type=None,
                reason_phrase="",
            )

    def test_handle_crypto_frame_over_largest_offset(self):
        with client_and_server() as (client, server):
            # client receives offset + length > 2^62 - 1
            with pytest.raises(QuicConnectionError) as cm:
                client._handle_crypto_frame(
                    client_receive_context(client),
                    QuicFrameType.CRYPTO,
                    Buffer(data=encode_uint_var(UINT_VAR_MAX) + encode_uint_var(1)),
                )
            assert cm.value.error_code == QuicErrorCode.FRAME_ENCODING_ERROR
            assert cm.value.frame_type == QuicFrameType.CRYPTO
            assert cm.value.reason_phrase == "offset + length cannot exceed 2^62 - 1"

    def test_handle_data_blocked_frame(self):
        with client_and_server() as (client, server):
            # client receives DATA_BLOCKED: 12345
            client._handle_data_blocked_frame(
                client_receive_context(client),
                QuicFrameType.DATA_BLOCKED,
                Buffer(data=encode_uint_var(12345)),
            )

    def test_handle_datagram_frame(self):
        client = create_standalone_client(self, max_datagram_frame_size=6)

        client._handle_datagram_frame(
            client_receive_context(client),
            QuicFrameType.DATAGRAM,
            Buffer(data=b"hello"),
        )

        assert client.next_event() == events.DatagramFrameReceived(data=b"hello")

    def test_handle_datagram_frame_not_allowed(self):
        client = create_standalone_client(self, max_datagram_frame_size=None)

        with pytest.raises(QuicConnectionError) as cm:
            client._handle_datagram_frame(
                client_receive_context(client),
                QuicFrameType.DATAGRAM,
                Buffer(data=b"hello"),
            )
        assert cm.value.error_code == QuicErrorCode.PROTOCOL_VIOLATION
        assert cm.value.frame_type == QuicFrameType.DATAGRAM
        assert cm.value.reason_phrase == "Unexpected DATAGRAM frame"

    def test_handle_datagram_frame_too_large(self):
        client = create_standalone_client(self, max_datagram_frame_size=5)

        with pytest.raises(QuicConnectionError) as cm:
            client._handle_datagram_frame(
                client_receive_context(client),
                QuicFrameType.DATAGRAM,
                Buffer(data=b"hello"),
            )
        assert cm.value.error_code == QuicErrorCode.PROTOCOL_VIOLATION
        assert cm.value.frame_type == QuicFrameType.DATAGRAM
        assert cm.value.reason_phrase == "Unexpected DATAGRAM frame"

    def test_handle_datagram_frame_with_length(self):
        client = create_standalone_client(self, max_datagram_frame_size=7)

        client._handle_datagram_frame(
            client_receive_context(client),
            QuicFrameType.DATAGRAM_WITH_LENGTH,
            Buffer(data=b"\x05hellojunk"),
        )

        assert client.next_event() == events.DatagramFrameReceived(data=b"hello")

    def test_handle_datagram_frame_with_length_not_allowed(self):
        client = create_standalone_client(self, max_datagram_frame_size=None)

        with pytest.raises(QuicConnectionError) as cm:
            client._handle_datagram_frame(
                client_receive_context(client),
                QuicFrameType.DATAGRAM_WITH_LENGTH,
                Buffer(data=b"\x05hellojunk"),
            )
        assert cm.value.error_code == QuicErrorCode.PROTOCOL_VIOLATION
        assert cm.value.frame_type == QuicFrameType.DATAGRAM_WITH_LENGTH
        assert cm.value.reason_phrase == "Unexpected DATAGRAM frame"

    def test_handle_datagram_frame_with_length_too_large(self):
        client = create_standalone_client(self, max_datagram_frame_size=6)

        with pytest.raises(QuicConnectionError) as cm:
            client._handle_datagram_frame(
                client_receive_context(client),
                QuicFrameType.DATAGRAM_WITH_LENGTH,
                Buffer(data=b"\x05hellojunk"),
            )
        assert cm.value.error_code == QuicErrorCode.PROTOCOL_VIOLATION
        assert cm.value.frame_type == QuicFrameType.DATAGRAM_WITH_LENGTH
        assert cm.value.reason_phrase == "Unexpected DATAGRAM frame"

    def test_handle_handshake_done_not_allowed(self):
        with client_and_server() as (client, server):
            # server receives HANDSHAKE_DONE frame
            with pytest.raises(QuicConnectionError) as cm:
                server._handle_handshake_done_frame(
                    client_receive_context(server),
                    QuicFrameType.HANDSHAKE_DONE,
                    Buffer(data=b""),
                )
            assert cm.value.error_code == QuicErrorCode.PROTOCOL_VIOLATION
            assert cm.value.frame_type == QuicFrameType.HANDSHAKE_DONE
            assert cm.value.reason_phrase == \
                "Clients must not send HANDSHAKE_DONE frames"

    def test_handle_max_data_frame(self):
        with client_and_server() as (client, server):
            assert client._remote_max_data == 1048576

            # client receives MAX_DATA raising limit
            client._handle_max_data_frame(
                client_receive_context(client),
                QuicFrameType.MAX_DATA,
                Buffer(data=encode_uint_var(1048577)),
            )
            assert client._remote_max_data == 1048577

    def test_handle_max_stream_data_frame(self):
        with client_and_server() as (client, server):
            # client creates bidirectional stream 0
            stream = client._get_or_create_stream_for_send(stream_id=0)
            assert stream.max_stream_data_remote == 1048576

            # client receives MAX_STREAM_DATA raising limit
            client._handle_max_stream_data_frame(
                client_receive_context(client),
                QuicFrameType.MAX_STREAM_DATA,
                Buffer(data=b"\x00" + encode_uint_var(1048577)),
            )
            assert stream.max_stream_data_remote == 1048577

            # client receives MAX_STREAM_DATA lowering limit
            client._handle_max_stream_data_frame(
                client_receive_context(client),
                QuicFrameType.MAX_STREAM_DATA,
                Buffer(data=b"\x00" + encode_uint_var(1048575)),
            )
            assert stream.max_stream_data_remote == 1048577

    def test_handle_max_stream_data_frame_receive_only(self):
        with client_and_server() as (client, server):
            # server creates unidirectional stream 3
            server.send_stream_data(stream_id=3, data=b"hello")

            # client receives MAX_STREAM_DATA: 3, 1
            with pytest.raises(QuicConnectionError) as cm:
                client._handle_max_stream_data_frame(
                    client_receive_context(client),
                    QuicFrameType.MAX_STREAM_DATA,
                    Buffer(data=b"\x03\x01"),
                )
            assert cm.value.error_code == QuicErrorCode.STREAM_STATE_ERROR
            assert cm.value.frame_type == QuicFrameType.MAX_STREAM_DATA
            assert cm.value.reason_phrase == "Stream is receive-only"

    def test_handle_max_streams_bidi_frame(self):
        with client_and_server() as (client, server):
            assert client._remote_max_streams_bidi == 128

            # client receives MAX_STREAMS_BIDI raising limit
            client._handle_max_streams_bidi_frame(
                client_receive_context(client),
                QuicFrameType.MAX_STREAMS_BIDI,
                Buffer(data=encode_uint_var(129)),
            )
            assert client._remote_max_streams_bidi == 129

            # client receives MAX_STREAMS_BIDI lowering limit
            client._handle_max_streams_bidi_frame(
                client_receive_context(client),
                QuicFrameType.MAX_STREAMS_BIDI,
                Buffer(data=encode_uint_var(127)),
            )
            assert client._remote_max_streams_bidi == 129

            # client receives invalid MAX_STREAMS_BIDI
            with pytest.raises(QuicConnectionError) as cm:
                client._handle_max_streams_bidi_frame(
                    client_receive_context(client),
                    QuicFrameType.MAX_STREAMS_BIDI,
                    Buffer(data=encode_uint_var(STREAM_COUNT_MAX + 1)),
                )
            assert cm.value.error_code == \
                QuicErrorCode.FRAME_ENCODING_ERROR
            assert cm.value.frame_type == QuicFrameType.MAX_STREAMS_BIDI
            assert cm.value.reason_phrase == "Maximum Streams cannot exceed 2^60"

    def test_handle_max_streams_uni_frame(self):
        with client_and_server() as (client, server):
            assert client._remote_max_streams_uni == 128

            # client receives MAX_STREAMS_UNI raising limit
            client._handle_max_streams_uni_frame(
                client_receive_context(client),
                QuicFrameType.MAX_STREAMS_UNI,
                Buffer(data=encode_uint_var(129)),
            )
            assert client._remote_max_streams_uni == 129

            # client receives MAX_STREAMS_UNI raising limit
            client._handle_max_streams_uni_frame(
                client_receive_context(client),
                QuicFrameType.MAX_STREAMS_UNI,
                Buffer(data=encode_uint_var(127)),
            )
            assert client._remote_max_streams_uni == 129

            # client receives invalid MAX_STREAMS_UNI
            with pytest.raises(QuicConnectionError) as cm:
                client._handle_max_streams_uni_frame(
                    client_receive_context(client),
                    QuicFrameType.MAX_STREAMS_UNI,
                    Buffer(data=encode_uint_var(STREAM_COUNT_MAX + 1)),
                )
            assert cm.value.error_code == \
                QuicErrorCode.FRAME_ENCODING_ERROR
            assert cm.value.frame_type == QuicFrameType.MAX_STREAMS_UNI
            assert cm.value.reason_phrase == "Maximum Streams cannot exceed 2^60"

    def test_handle_new_connection_id_duplicate(self):
        with client_and_server() as (client, server):
            buf = new_connection_id(sequence_number=7)

            # client receives NEW_CONNECTION_ID
            client._handle_new_connection_id_frame(
                client_receive_context(client),
                QuicFrameType.NEW_CONNECTION_ID,
                buf,
            )

            assert client._peer_cid.sequence_number == 0
            assert sequence_numbers(client._peer_cid_available) == [1, 2, 3, 4, 5, 6, 7]

    def test_handle_new_connection_id_over_limit(self):
        with client_and_server() as (client, server):
            buf = new_connection_id(sequence_number=8)

            # client receives NEW_CONNECTION_ID
            with pytest.raises(QuicConnectionError) as cm:
                client._handle_new_connection_id_frame(
                    client_receive_context(client),
                    QuicFrameType.NEW_CONNECTION_ID,
                    buf,
                )
            assert cm.value.error_code == QuicErrorCode.CONNECTION_ID_LIMIT_ERROR
            assert cm.value.frame_type == QuicFrameType.NEW_CONNECTION_ID
            assert cm.value.reason_phrase == "Too many active connection IDs"

    def test_handle_new_connection_id_with_retire_prior_to(self):
        with client_and_server() as (client, server):
            buf = new_connection_id(sequence_number=8, retire_prior_to=2, capacity=42)

            # client receives NEW_CONNECTION_ID
            client._handle_new_connection_id_frame(
                client_receive_context(client),
                QuicFrameType.NEW_CONNECTION_ID,
                buf,
            )

            assert client._peer_cid.sequence_number == 2
            assert sequence_numbers(client._peer_cid_available) == [3, 4, 5, 6, 7, 8]

    def test_handle_new_connection_id_with_retire_prior_to_lower(self):
        with client_and_server() as (client, server):
            buf = new_connection_id(sequence_number=80, retire_prior_to=80)
            # client receives NEW_CONNECTION_ID
            client._handle_new_connection_id_frame(
                client_receive_context(client),
                QuicFrameType.NEW_CONNECTION_ID,
                buf,
            )
            assert client._peer_cid.sequence_number == 80
            assert sequence_numbers(client._peer_cid_available) == []
            buf = new_connection_id(sequence_number=30, retire_prior_to=30)
            # client receives NEW_CONNECTION_ID
            client._handle_new_connection_id_frame(
                client_receive_context(client),
                QuicFrameType.NEW_CONNECTION_ID,
                buf,
            )
            assert client._peer_cid.sequence_number == 80
            assert sequence_numbers(client._peer_cid_available) == []

    def test_handle_excessive_new_connection_id_retires(self):
        with client_and_server() as (client, server):
            for i in range(25):
                sequence_number = 8 + i
                buf = new_connection_id(
                    sequence_number=sequence_number, retire_prior_to=sequence_number
                )
                # client receives NEW_CONNECTION_ID
                client._handle_new_connection_id_frame(
                    client_receive_context(client),
                    QuicFrameType.NEW_CONNECTION_ID,
                    buf,
                )
            # So far, so good!  We should be at the (default) limit of 4*8 pending
            # retirements.
            assert len(client._retire_connection_ids) == 32
            # Now we will go one too many!
            sequence_number = 8 + 25
            buf = new_connection_id(
                sequence_number=sequence_number, retire_prior_to=sequence_number
            )
            with pytest.raises(QuicConnectionError) as cm:
                client._handle_new_connection_id_frame(
                    client_receive_context(client),
                    QuicFrameType.NEW_CONNECTION_ID,
                    buf,
                )
            assert cm.value.error_code == QuicErrorCode.CONNECTION_ID_LIMIT_ERROR
            assert cm.value.frame_type == QuicFrameType.NEW_CONNECTION_ID
            assert cm.value.reason_phrase == "Too many pending retired connection IDs"

    def test_handle_new_connection_id_with_connection_id_invalid(self):
        with client_and_server() as (client, server):
            buf = new_connection_id(
                sequence_number=8, retire_prior_to=2, connection_id=bytes(21)
            )

            # client receives NEW_CONNECTION_ID
            with pytest.raises(QuicConnectionError) as cm:
                client._handle_new_connection_id_frame(
                    client_receive_context(client),
                    QuicFrameType.NEW_CONNECTION_ID,
                    buf,
                )
            assert cm.value.error_code == \
                QuicErrorCode.FRAME_ENCODING_ERROR
            assert cm.value.frame_type == QuicFrameType.NEW_CONNECTION_ID
            assert cm.value.reason_phrase == \
                "Length must be greater than 0 and less than 20"

    def test_handle_new_connection_id_with_retire_prior_to_invalid(self):
        with client_and_server() as (client, server):
            buf = new_connection_id(sequence_number=8, retire_prior_to=9)

            # client receives NEW_CONNECTION_ID
            with pytest.raises(QuicConnectionError) as cm:
                client._handle_new_connection_id_frame(
                    client_receive_context(client),
                    QuicFrameType.NEW_CONNECTION_ID,
                    buf,
                )
            assert cm.value.error_code == \
                QuicErrorCode.PROTOCOL_VIOLATION
            assert cm.value.frame_type == QuicFrameType.NEW_CONNECTION_ID
            assert cm.value.reason_phrase == \
                "Retire Prior To is greater than Sequence Number"

    def test_handle_new_token_frame(self):
        with client_and_server() as (client, server):
            # client receives NEW_TOKEN
            client._handle_new_token_frame(
                client_receive_context(client),
                QuicFrameType.NEW_TOKEN,
                Buffer(data=binascii.unhexlify("080102030405060708")),
            )

    def test_handle_new_token_frame_from_client(self):
        with client_and_server() as (client, server):
            # server receives NEW_TOKEN
            with pytest.raises(QuicConnectionError) as cm:
                server._handle_new_token_frame(
                    client_receive_context(client),
                    QuicFrameType.NEW_TOKEN,
                    Buffer(data=binascii.unhexlify("080102030405060708")),
                )
            assert cm.value.error_code == QuicErrorCode.PROTOCOL_VIOLATION
            assert cm.value.frame_type == QuicFrameType.NEW_TOKEN
            assert cm.value.reason_phrase == "Clients must not send NEW_TOKEN frames"

    def test_handle_path_challenge_frame(self):
        with client_and_server() as (client, server):
            # client changes address and sends some data
            client.send_stream_data(0, b"01234567")
            for data, addr in client.datagrams_to_send(now=time.time()):
                server.receive_datagram(data, ("1.2.3.4", 2345), now=time.time())

            # check paths
            assert len(server._network_paths) == 2
            assert server._network_paths[0].addr == ("1.2.3.4", 2345)
            assert not server._network_paths[0].is_validated
            assert server._network_paths[1].addr == ("1.2.3.4", 1234)
            assert server._network_paths[1].is_validated

            # server sends PATH_CHALLENGE and receives PATH_RESPONSE
            for data, addr in server.datagrams_to_send(now=time.time()):
                client.receive_datagram(data, SERVER_ADDR, now=time.time())
            for data, addr in client.datagrams_to_send(now=time.time()):
                server.receive_datagram(data, ("1.2.3.4", 2345), now=time.time())

            # check paths
            assert server._network_paths[0].addr == ("1.2.3.4", 2345)
            assert server._network_paths[0].is_validated
            assert server._network_paths[1].addr == ("1.2.3.4", 1234)
            assert server._network_paths[1].is_validated

    def test_handle_path_challenge_response_on_different_path(self):
        with client_and_server() as (client, server):
            # client changes address and sends some data
            client.send_stream_data(0, b"01234567")
            for data, addr in client.datagrams_to_send(now=time.time()):
                server.receive_datagram(data, ("1.2.3.4", 2345), now=time.time())
            # check paths
            assert len(server._network_paths) == 2
            assert server._network_paths[0].addr == ("1.2.3.4", 2345)
            assert not server._network_paths[0].is_validated
            assert server._network_paths[1].addr == ("1.2.3.4", 1234)
            assert server._network_paths[1].is_validated
            # server sends PATH_CHALLENGE and receives PATH_RESPONSE on the 1234
            # path instead of the expected 2345 path.
            for data, addr in server.datagrams_to_send(now=time.time()):
                client.receive_datagram(data, SERVER_ADDR, now=time.time())
            for data, addr in client.datagrams_to_send(now=time.time()):
                server.receive_datagram(data, ("1.2.3.4", 1234), now=time.time())
            # check paths; note that the order is backwards from the prior test
            # as receiving on 1234 promotes it to first in the list
            assert server._network_paths[0].addr == ("1.2.3.4", 1234)
            assert server._network_paths[0].is_validated
            assert server._network_paths[1].addr == ("1.2.3.4", 2345)
            assert server._network_paths[1].is_validated

    def test_local_path_challenges_are_bounded(self):
        with client_and_server() as (client, server):
            for i in range(MAX_LOCAL_CHALLENGES + 2):
                server._add_local_challenge(
                    int.to_bytes(i, 8, "big"), QuicNetworkPath(f"1.2.3.{i}")
                )
            assert len(server._local_challenges) == MAX_LOCAL_CHALLENGES
            for i in range(2, MAX_LOCAL_CHALLENGES + 2):
                assert server._local_challenges[int.to_bytes(i, 8, "big")].addr == \
                    f"1.2.3.{i}"

    def test_handle_path_response_frame_bad(self):
        with client_and_server() as (client, server):
            # server receives unsolicited PATH_RESPONSE
            with pytest.raises(QuicConnectionError) as cm:
                server._handle_path_response_frame(
                    client_receive_context(client),
                    QuicFrameType.PATH_RESPONSE,
                    Buffer(data=b"\x11\x22\x33\x44\x55\x66\x77\x88"),
                )
            assert cm.value.error_code == QuicErrorCode.PROTOCOL_VIOLATION
            assert cm.value.frame_type == QuicFrameType.PATH_RESPONSE

    def test_handle_padding_frame(self):
        client = create_standalone_client(self)

        # no more padding
        buf = Buffer(data=b"")
        client._handle_padding_frame(
            client_receive_context(client), QuicFrameType.PADDING, buf
        )
        assert buf.tell() == 0

        # padding until end
        buf = Buffer(data=bytes(10))
        client._handle_padding_frame(
            client_receive_context(client), QuicFrameType.PADDING, buf
        )
        assert buf.tell() == 10

        # padding then something else
        buf = Buffer(data=bytes(10) + b"\x01")
        client._handle_padding_frame(
            client_receive_context(client), QuicFrameType.PADDING, buf
        )
        assert buf.tell() == 10

    def test_handle_reset_stream_frame(self):
        stream_id = 0
        with client_and_server() as (client, server):
            # client creates bidirectional stream
            client.send_stream_data(stream_id=stream_id, data=b"hello")
            consume_events(client)

            # client receives RESET_STREAM
            client._handle_reset_stream_frame(
                client_receive_context(client),
                QuicFrameType.RESET_STREAM,
                Buffer(
                    data=encode_uint_var(stream_id)
                    + encode_uint_var(QuicErrorCode.INTERNAL_ERROR)
                    + encode_uint_var(0)
                ),
            )

            event = client.next_event()
            assert type(event) == events.StreamReset
            assert event.error_code == QuicErrorCode.INTERNAL_ERROR
            assert event.stream_id == stream_id

    def test_handle_reset_stream_frame_final_size_error(self):
        stream_id = 0
        with client_and_server() as (client, server):
            # client creates bidirectional stream
            client.send_stream_data(stream_id=stream_id, data=b"hello")
            consume_events(client)

            # client receives RESET_STREAM at offset 8
            client._handle_reset_stream_frame(
                client_receive_context(client),
                QuicFrameType.RESET_STREAM,
                Buffer(
                    data=encode_uint_var(stream_id)
                    + encode_uint_var(QuicErrorCode.NO_ERROR)
                    + encode_uint_var(8)
                ),
            )

            event = client.next_event()
            assert type(event) == events.StreamReset
            assert event.error_code == QuicErrorCode.NO_ERROR
            assert event.stream_id == stream_id

            # client receives RESET_STREAM at offset 5
            with pytest.raises(QuicConnectionError) as cm:
                client._handle_reset_stream_frame(
                    client_receive_context(client),
                    QuicFrameType.RESET_STREAM,
                    Buffer(
                        data=encode_uint_var(stream_id)
                        + encode_uint_var(QuicErrorCode.NO_ERROR)
                        + encode_uint_var(5)
                    ),
                )
            assert cm.value.error_code == QuicErrorCode.FINAL_SIZE_ERROR
            assert cm.value.frame_type == QuicFrameType.RESET_STREAM
            assert cm.value.reason_phrase == "Cannot change final size"

    def test_handle_reset_stream_frame_over_max_data(self):
        stream_id = 0
        with client_and_server() as (client, server):
            # client creates bidirectional stream
            client.send_stream_data(stream_id=stream_id, data=b"hello")
            consume_events(client)

            # artificially raise received data counter
            client._local_max_data.used = client._local_max_data.value

            # client receives RESET_STREAM frame
            with pytest.raises(QuicConnectionError) as cm:
                client._handle_reset_stream_frame(
                    client_receive_context(client),
                    QuicFrameType.RESET_STREAM,
                    Buffer(
                        data=encode_uint_var(stream_id)
                        + encode_uint_var(QuicErrorCode.NO_ERROR)
                        + encode_uint_var(1)
                    ),
                )
            assert cm.value.error_code == QuicErrorCode.FLOW_CONTROL_ERROR
            assert cm.value.frame_type == QuicFrameType.RESET_STREAM
            assert cm.value.reason_phrase == "Over connection data limit"

    def test_handle_reset_stream_frame_over_max_stream_data(self):
        stream_id = 0
        with client_and_server() as (client, server):
            # client creates bidirectional stream
            client.send_stream_data(stream_id=stream_id, data=b"hello")
            consume_events(client)

            # client receives STREAM frame
            with pytest.raises(QuicConnectionError) as cm:
                client._handle_reset_stream_frame(
                    client_receive_context(client),
                    QuicFrameType.RESET_STREAM,
                    Buffer(
                        data=encode_uint_var(stream_id)
                        + encode_uint_var(QuicErrorCode.NO_ERROR)
                        + encode_uint_var(client._local_max_stream_data_bidi_local + 1)
                    ),
                )
            assert cm.value.error_code == QuicErrorCode.FLOW_CONTROL_ERROR
            assert cm.value.frame_type == QuicFrameType.RESET_STREAM
            assert cm.value.reason_phrase == "Over stream data limit"

    def test_handle_reset_stream_frame_send_only(self):
        with client_and_server() as (client, server):
            # client creates unidirectional stream 2
            client.send_stream_data(stream_id=2, data=b"hello")

            # client receives RESET_STREAM
            with pytest.raises(QuicConnectionError) as cm:
                client._handle_reset_stream_frame(
                    client_receive_context(client),
                    QuicFrameType.RESET_STREAM,
                    Buffer(data=binascii.unhexlify("021100")),
                )
            assert cm.value.error_code == QuicErrorCode.STREAM_STATE_ERROR
            assert cm.value.frame_type == QuicFrameType.RESET_STREAM
            assert cm.value.reason_phrase == "Stream is send-only"

    def test_handle_reset_stream_frame_twice(self):
        stream_id = 3
        reset_stream_data = (
            encode_uint_var(QuicFrameType.RESET_STREAM)
            + encode_uint_var(stream_id)
            + encode_uint_var(QuicErrorCode.INTERNAL_ERROR)
            + encode_uint_var(0)
        )
        with client_and_server() as (client, server):
            # server creates unidirectional stream
            server.send_stream_data(stream_id=stream_id, data=b"hello")
            roundtrip(server, client)
            consume_events(client)

            # client receives RESET_STREAM
            client._payload_received(client_receive_context(client), reset_stream_data)

            event = client.next_event()
            assert type(event) == events.StreamReset
            assert event.error_code == QuicErrorCode.INTERNAL_ERROR
            assert event.stream_id == stream_id

            # stream gets discarded
            assert drop(client) == 0

            # client receives RESET_STREAM again
            client._payload_received(client_receive_context(client), reset_stream_data)

            event = client.next_event()
            assert event is None

    def test_handle_retire_connection_id_frame(self):
        with client_and_server() as (client, server):
            assert sequence_numbers(client._host_cids) == [0, 1, 2, 3, 4, 5, 6, 7]

            # client receives RETIRE_CONNECTION_ID
            client._handle_retire_connection_id_frame(
                client_receive_context(client),
                QuicFrameType.RETIRE_CONNECTION_ID,
                Buffer(data=b"\x02"),
            )
            assert sequence_numbers(client._host_cids) == [0, 1, 3, 4, 5, 6, 7, 8]

    def test_handle_retire_connection_id_frame_current_cid(self):
        with client_and_server() as (client, server):
            assert sequence_numbers(client._host_cids) == [0, 1, 2, 3, 4, 5, 6, 7]

            # client receives RETIRE_CONNECTION_ID for the current CID
            with pytest.raises(QuicConnectionError) as cm:
                client._handle_retire_connection_id_frame(
                    client_receive_context(client),
                    QuicFrameType.RETIRE_CONNECTION_ID,
                    Buffer(data=b"\x00"),
                )
            assert cm.value.error_code == QuicErrorCode.PROTOCOL_VIOLATION
            assert cm.value.frame_type == QuicFrameType.RETIRE_CONNECTION_ID
            assert cm.value.reason_phrase == "Cannot retire current connection ID"
            assert sequence_numbers(client._host_cids) == [0, 1, 2, 3, 4, 5, 6, 7]

    def test_handle_retire_connection_id_frame_invalid_sequence_number(self):
        with client_and_server() as (client, server):
            assert sequence_numbers(client._host_cids) == [0, 1, 2, 3, 4, 5, 6, 7]

            # client receives RETIRE_CONNECTION_ID
            with pytest.raises(QuicConnectionError) as cm:
                client._handle_retire_connection_id_frame(
                    client_receive_context(client),
                    QuicFrameType.RETIRE_CONNECTION_ID,
                    Buffer(data=b"\x08"),
                )
            assert cm.value.error_code == QuicErrorCode.PROTOCOL_VIOLATION
            assert cm.value.frame_type == QuicFrameType.RETIRE_CONNECTION_ID
            assert cm.value.reason_phrase == "Cannot retire unknown connection ID"
            assert sequence_numbers(client._host_cids) == [0, 1, 2, 3, 4, 5, 6, 7]

    def test_handle_stop_sending_frame(self):
        with client_and_server() as (client, server):
            # client creates bidirectional stream 0
            client.send_stream_data(stream_id=0, data=b"hello")

            # client receives STOP_SENDING
            client._handle_stop_sending_frame(
                client_receive_context(client),
                QuicFrameType.STOP_SENDING,
                Buffer(data=b"\x00\x11"),
            )

            # check events
            assert type(client.next_event()) == events.ProtocolNegotiated
            assert type(client.next_event()) == events.HandshakeCompleted
            for i in range(7):
                assert type(client.next_event()) == events.ConnectionIdIssued

            event = client.next_event()
            assert type(event) == events.StopSendingReceived
            assert event.stream_id == 0
            assert event.error_code == 0x11

            assert client.next_event() is None

    def test_handle_stop_sending_frame_receive_only(self):
        with client_and_server() as (client, server):
            # server creates unidirectional stream 3
            server.send_stream_data(stream_id=3, data=b"hello")

            # client receives STOP_SENDING
            with pytest.raises(QuicConnectionError) as cm:
                client._handle_stop_sending_frame(
                    client_receive_context(client),
                    QuicFrameType.STOP_SENDING,
                    Buffer(data=b"\x03\x11"),
                )
            assert cm.value.error_code == QuicErrorCode.STREAM_STATE_ERROR
            assert cm.value.frame_type == QuicFrameType.STOP_SENDING
            assert cm.value.reason_phrase == "Stream is receive-only"

    def test_handle_stream_frame_final_size_error(self):
        with client_and_server() as (client, server):
            frame_type = QuicFrameType.STREAM_BASE | 7
            stream_id = 1

            # client receives FIN at offset 8
            client._handle_stream_frame(
                client_receive_context(client),
                frame_type,
                Buffer(
                    data=encode_uint_var(stream_id)
                    + encode_uint_var(8)
                    + encode_uint_var(0)
                ),
            )

            # client receives FIN at offset 5
            with pytest.raises(QuicConnectionError) as cm:
                client._handle_stream_frame(
                    client_receive_context(client),
                    frame_type,
                    Buffer(
                        data=encode_uint_var(stream_id)
                        + encode_uint_var(5)
                        + encode_uint_var(0)
                    ),
                )
            assert cm.value.error_code == QuicErrorCode.FINAL_SIZE_ERROR
            assert cm.value.frame_type == frame_type
            assert cm.value.reason_phrase == "Cannot change final size"

    def test_handle_stream_frame_over_largest_offset(self):
        with client_and_server() as (client, server):
            # client receives offset + length > 2^62 - 1
            frame_type = QuicFrameType.STREAM_BASE | 6
            stream_id = 1
            with pytest.raises(QuicConnectionError) as cm:
                client._handle_stream_frame(
                    client_receive_context(client),
                    frame_type,
                    Buffer(
                        data=encode_uint_var(stream_id)
                        + encode_uint_var(UINT_VAR_MAX)
                        + encode_uint_var(1)
                    ),
                )
            assert cm.value.error_code == QuicErrorCode.FRAME_ENCODING_ERROR
            assert cm.value.frame_type == frame_type
            assert cm.value.reason_phrase == "offset + length cannot exceed 2^62 - 1"

    def test_handle_stream_frame_over_max_data(self):
        with client_and_server() as (client, server):
            # artificially raise received data counter
            client._local_max_data.used = client._local_max_data.value

            # client receives STREAM frame
            frame_type = QuicFrameType.STREAM_BASE | 4
            stream_id = 1
            with pytest.raises(QuicConnectionError) as cm:
                client._handle_stream_frame(
                    client_receive_context(client),
                    frame_type,
                    Buffer(data=encode_uint_var(stream_id) + encode_uint_var(1)),
                )
            assert cm.value.error_code == QuicErrorCode.FLOW_CONTROL_ERROR
            assert cm.value.frame_type == frame_type
            assert cm.value.reason_phrase == "Over connection data limit"

    def test_handle_stream_frame_over_max_stream_data(self):
        with client_and_server() as (client, server):
            # client receives STREAM frame
            frame_type = QuicFrameType.STREAM_BASE | 4
            stream_id = 1
            with pytest.raises(QuicConnectionError) as cm:
                client._handle_stream_frame(
                    client_receive_context(client),
                    frame_type,
                    Buffer(
                        data=encode_uint_var(stream_id)
                        + encode_uint_var(client._local_max_stream_data_bidi_remote + 1)
                    ),
                )
            assert cm.value.error_code == QuicErrorCode.FLOW_CONTROL_ERROR
            assert cm.value.frame_type == frame_type
            assert cm.value.reason_phrase == "Over stream data limit"

    def test_handle_stream_frame_over_max_streams(self):
        with client_and_server() as (client, server):
            # client receives STREAM frame
            with pytest.raises(QuicConnectionError) as cm:
                client._handle_stream_frame(
                    client_receive_context(client),
                    QuicFrameType.STREAM_BASE,
                    Buffer(
                        data=encode_uint_var(client._local_max_stream_data_uni * 4 + 3)
                    ),
                )
            assert cm.value.error_code == QuicErrorCode.STREAM_LIMIT_ERROR
            assert cm.value.frame_type == QuicFrameType.STREAM_BASE
            assert cm.value.reason_phrase == "Too many streams open"

    def test_handle_stream_frame_send_only(self):
        with client_and_server() as (client, server):
            # client creates unidirectional stream 2
            client.send_stream_data(stream_id=2, data=b"hello")

            # client receives STREAM frame
            with pytest.raises(QuicConnectionError) as cm:
                client._handle_stream_frame(
                    client_receive_context(client),
                    QuicFrameType.STREAM_BASE,
                    Buffer(data=b"\x02"),
                )
            assert cm.value.error_code == QuicErrorCode.STREAM_STATE_ERROR
            assert cm.value.frame_type == QuicFrameType.STREAM_BASE
            assert cm.value.reason_phrase == "Stream is send-only"

    def test_handle_stream_frame_wrong_initiator(self):
        with client_and_server() as (client, server):
            # client receives STREAM frame
            with pytest.raises(QuicConnectionError) as cm:
                client._handle_stream_frame(
                    client_receive_context(client),
                    QuicFrameType.STREAM_BASE,
                    Buffer(data=b"\x00"),
                )
            assert cm.value.error_code == QuicErrorCode.STREAM_STATE_ERROR
            assert cm.value.frame_type == QuicFrameType.STREAM_BASE
            assert cm.value.reason_phrase == "Wrong stream initiator"

    def test_handle_stream_data_blocked_frame(self):
        with client_and_server() as (client, server):
            # client creates bidirectional stream 0
            client.send_stream_data(stream_id=0, data=b"hello")

            # client receives STREAM_DATA_BLOCKED
            client._handle_stream_data_blocked_frame(
                client_receive_context(client),
                QuicFrameType.STREAM_DATA_BLOCKED,
                Buffer(data=b"\x00\x01"),
            )

    def test_handle_stream_data_blocked_frame_send_only(self):
        with client_and_server() as (client, server):
            # client creates unidirectional stream 2
            client.send_stream_data(stream_id=2, data=b"hello")

            # client receives STREAM_DATA_BLOCKED
            with pytest.raises(QuicConnectionError) as cm:
                client._handle_stream_data_blocked_frame(
                    client_receive_context(client),
                    QuicFrameType.STREAM_DATA_BLOCKED,
                    Buffer(data=b"\x02\x01"),
                )
            assert cm.value.error_code == QuicErrorCode.STREAM_STATE_ERROR
            assert cm.value.frame_type == QuicFrameType.STREAM_DATA_BLOCKED
            assert cm.value.reason_phrase == "Stream is send-only"

    def test_handle_streams_blocked_uni_frame(self):
        with client_and_server() as (client, server):
            # client receives STREAMS_BLOCKED_UNI: 0
            client._handle_streams_blocked_frame(
                client_receive_context(client),
                QuicFrameType.STREAMS_BLOCKED_UNI,
                Buffer(data=b"\x00"),
            )

            # client receives invalid STREAMS_BLOCKED_UNI
            with pytest.raises(QuicConnectionError) as cm:
                client._handle_streams_blocked_frame(
                    client_receive_context(client),
                    QuicFrameType.STREAMS_BLOCKED_UNI,
                    Buffer(data=encode_uint_var(STREAM_COUNT_MAX + 1)),
                )
            assert cm.value.error_code == \
                QuicErrorCode.FRAME_ENCODING_ERROR
            assert cm.value.frame_type == QuicFrameType.STREAMS_BLOCKED_UNI
            assert cm.value.reason_phrase == "Maximum Streams cannot exceed 2^60"

    def test_parse_transport_parameters(self):
        client = create_standalone_client(self)

        data = encode_transport_parameters(
            QuicTransportParameters(
                original_destination_connection_id=client.original_destination_connection_id
            )
        )
        client._parse_transport_parameters(data)

    def test_parse_transport_parameters_malformed(self):
        client = create_standalone_client(self)

        with pytest.raises(QuicConnectionError) as cm:
            client._parse_transport_parameters(b"0")
        assert cm.value.error_code == QuicErrorCode.TRANSPORT_PARAMETER_ERROR
        assert cm.value.frame_type == QuicFrameType.CRYPTO
        assert cm.value.reason_phrase == "Could not parse QUIC transport parameters"

    def test_parse_transport_parameters_with_bad_ack_delay_exponent(self):
        client = create_standalone_client(self)

        data = encode_transport_parameters(
            QuicTransportParameters(
                ack_delay_exponent=21,
                original_destination_connection_id=client.original_destination_connection_id,
            )
        )
        with pytest.raises(QuicConnectionError) as cm:
            client._parse_transport_parameters(data)
        assert cm.value.error_code == QuicErrorCode.TRANSPORT_PARAMETER_ERROR
        assert cm.value.frame_type == QuicFrameType.CRYPTO
        assert cm.value.reason_phrase == "ack_delay_exponent must be <= 20"

    def test_parse_transport_parameters_with_bad_active_connection_id_limit(self):
        client = create_standalone_client(self)

        for active_connection_id_limit in [0, 1]:
            data = encode_transport_parameters(
                QuicTransportParameters(
                    active_connection_id_limit=active_connection_id_limit,
                    original_destination_connection_id=client.original_destination_connection_id,
                )
            )
            with pytest.raises(QuicConnectionError) as cm:
                client._parse_transport_parameters(data)
            assert cm.value.error_code == QuicErrorCode.TRANSPORT_PARAMETER_ERROR
            assert cm.value.frame_type == QuicFrameType.CRYPTO
            assert cm.value.reason_phrase == \
                "active_connection_id_limit must be no less than 2"

    def test_parse_transport_parameters_with_bad_max_ack_delay(self):
        client = create_standalone_client(self)

        data = encode_transport_parameters(
            QuicTransportParameters(
                max_ack_delay=2**14,
                original_destination_connection_id=client.original_destination_connection_id,
            )
        )
        with pytest.raises(QuicConnectionError) as cm:
            client._parse_transport_parameters(data)
        assert cm.value.error_code == QuicErrorCode.TRANSPORT_PARAMETER_ERROR
        assert cm.value.frame_type == QuicFrameType.CRYPTO
        assert cm.value.reason_phrase == "max_ack_delay must be < 2^14"

    def test_parse_transport_parameters_with_bad_max_udp_payload_size(self):
        client = create_standalone_client(self)

        data = encode_transport_parameters(
            QuicTransportParameters(
                max_udp_payload_size=1199,
                original_destination_connection_id=client.original_destination_connection_id,
            )
        )
        with pytest.raises(QuicConnectionError) as cm:
            client._parse_transport_parameters(data)
        assert cm.value.error_code == QuicErrorCode.TRANSPORT_PARAMETER_ERROR
        assert cm.value.frame_type == QuicFrameType.CRYPTO
        assert cm.value.reason_phrase == "max_udp_payload_size must be >= 1200"

    def test_parse_transport_parameters_with_bad_initial_source_connection_id(self):
        client = create_standalone_client(self)
        client._initial_source_connection_id = binascii.unhexlify("0011223344556677")

        data = encode_transport_parameters(
            QuicTransportParameters(
                initial_source_connection_id=binascii.unhexlify("1122334455667788"),
                original_destination_connection_id=client.original_destination_connection_id,
            )
        )
        with pytest.raises(QuicConnectionError) as cm:
            client._parse_transport_parameters(data)
        assert cm.value.error_code == QuicErrorCode.TRANSPORT_PARAMETER_ERROR
        assert cm.value.frame_type == QuicFrameType.CRYPTO
        assert cm.value.reason_phrase == "initial_source_connection_id does not match"

    def test_parse_transport_parameters_with_bad_version_information_1(self):
        server = create_standalone_server(self)
        data = encode_transport_parameters(
            QuicTransportParameters(
                version_information=QuicVersionInformation(
                    chosen_version=QuicProtocolVersion.VERSION_1,
                    available_versions=[QuicProtocolVersion.VERSION_2],
                )
            )
        )
        with pytest.raises(QuicConnectionError) as cm:
            server._parse_transport_parameters(data)
        assert cm.value.error_code == QuicErrorCode.TRANSPORT_PARAMETER_ERROR
        assert cm.value.frame_type == QuicFrameType.CRYPTO
        assert cm.value.reason_phrase == \
            "version_information's chosen_version is not included in " \
            "available_versions"

    def test_parse_transport_parameters_with_bad_version_information_2(self):
        server = create_standalone_server(self)
        data = encode_transport_parameters(
            QuicTransportParameters(
                version_information=QuicVersionInformation(
                    chosen_version=QuicProtocolVersion.VERSION_1,
                    available_versions=[
                        QuicProtocolVersion.VERSION_1,
                        QuicProtocolVersion.VERSION_2,
                    ],
                )
            )
        )
        server._crypto_packet_version = QuicProtocolVersion.VERSION_2
        with pytest.raises(QuicConnectionError) as cm:
            server._parse_transport_parameters(data)
        assert cm.value.error_code == QuicErrorCode.VERSION_NEGOTIATION_ERROR
        assert cm.value.frame_type == QuicFrameType.CRYPTO
        assert cm.value.reason_phrase == \
            "version_information's chosen_version does not match the version in use"

    def test_payload_received_empty(self):
        with client_and_server() as (client, server):
            # client receives empty payload
            with pytest.raises(QuicConnectionError) as cm:
                client._payload_received(client_receive_context(client), b"")
            assert cm.value.error_code == QuicErrorCode.PROTOCOL_VIOLATION
            assert cm.value.frame_type == QuicFrameType.PADDING
            assert cm.value.reason_phrase == "Packet contains no frames"

    def test_payload_received_padding_only(self):
        with client_and_server() as (client, server):
            # client receives padding only
            is_ack_eliciting, is_probing = client._payload_received(
                client_receive_context(client), b"\x00" * 1200
            )
            assert not is_ack_eliciting
            assert is_probing

    def test_payload_received_malformed_frame_type(self):
        with client_and_server() as (client, server):
            # client receives a malformed frame type
            with pytest.raises(QuicConnectionError) as cm:
                client._payload_received(client_receive_context(client), b"\xff")
            assert cm.value.error_code == QuicErrorCode.FRAME_ENCODING_ERROR
            assert cm.value.frame_type == None
            assert cm.value.reason_phrase == "Malformed frame type"

    def test_payload_received_unknown_frame(self):
        with client_and_server() as (client, server):
            # client receives unknown frame
            with pytest.raises(QuicConnectionError) as cm:
                client._payload_received(client_receive_context(client), b"\x1f")
            assert cm.value.error_code == QuicErrorCode.FRAME_ENCODING_ERROR
            assert cm.value.frame_type == 0x1F
            assert cm.value.reason_phrase == "Unknown frame type"

    def test_payload_received_unexpected_frame(self):
        with client_and_server() as (client, server):
            # client receives CRYPTO frame in 0-RTT
            with pytest.raises(QuicConnectionError) as cm:
                client._payload_received(
                    client_receive_context(client, epoch=tls.Epoch.ZERO_RTT), b"\x06"
                )
            assert cm.value.error_code == QuicErrorCode.PROTOCOL_VIOLATION
            assert cm.value.frame_type == QuicFrameType.CRYPTO
            assert cm.value.reason_phrase == "Unexpected frame type"

    def test_payload_received_malformed_frame(self):
        with client_and_server() as (client, server):
            # client receives malformed TRANSPORT_CLOSE frame
            with pytest.raises(QuicConnectionError) as cm:
                client._payload_received(
                    client_receive_context(client), b"\x1c\x00\x01"
                )
            assert cm.value.error_code == QuicErrorCode.FRAME_ENCODING_ERROR
            assert cm.value.frame_type == 0x1C
            assert cm.value.reason_phrase == "Failed to parse frame"

    def test_send_max_data_blocked_by_cc(self):
        with client_and_server() as (client, server):
            # check congestion control
            assert client._loss.bytes_in_flight == 0
            assert client._loss.congestion_window >= 13530
            assert client._loss.congestion_window <= 16000

            # artificially raise received data counter
            client._local_max_data_used = client._local_max_data
            assert server._remote_max_data == 1048576

            # artificially raise bytes in flight
            client._loss._cc.bytes_in_flight = client._loss.congestion_window

            # MAX_DATA is not sent due to congestion control
            assert drop(client) == 0

    def test_send_max_data_retransmit(self):
        with client_and_server() as (client, server):
            # artificially raise received data counter
            client._local_max_data.used = client._local_max_data.value
            assert client._local_max_data.sent == 1048576
            assert client._local_max_data.used == 1048576
            assert client._local_max_data.value == 1048576
            assert server._remote_max_data == 1048576

            # MAX_DATA is sent and lost
            assert drop(client) == 1
            assert client._local_max_data.sent == 2097152
            assert client._local_max_data.used == 1048576
            assert client._local_max_data.value == 2097152
            assert server._remote_max_data == 1048576

            # MAX_DATA loss is detected
            client._on_connection_limit_delivery(
                QuicDeliveryState.LOST, client._local_max_data
            )
            assert client._local_max_data.sent == 0
            assert client._local_max_data.used == 1048576
            assert client._local_max_data.value == 2097152

            # MAX_DATA is retransmitted and acked
            assert roundtrip(client, server) == (1, 1)
            assert client._local_max_data.sent == 2097152
            assert client._local_max_data.used == 1048576
            assert client._local_max_data.value == 2097152
            assert server._remote_max_data == 2097152

    def test_send_max_stream_data_retransmit(self):
        with client_and_server() as (client, server):
            # client creates bidirectional stream 0
            stream = client._get_or_create_stream_for_send(stream_id=0)
            client.send_stream_data(0, b"hello")
            assert stream.max_stream_data_local == 1048576
            assert stream.max_stream_data_local_sent == 1048576
            assert roundtrip(client, server) == (1, 1)

            # server sends data, just before raising MAX_STREAM_DATA
            server.send_stream_data(0, b"Z" * 524288)  # 1048576 // 2
            for i in range(10):
                roundtrip(server, client)
            assert stream.max_stream_data_local == 1048576
            assert stream.max_stream_data_local_sent == 1048576

            # server sends one more byte
            server.send_stream_data(0, b"Z")
            assert transfer(server, client) == 1

            # MAX_STREAM_DATA is sent and lost
            assert drop(client) == 1
            assert stream.max_stream_data_local == 2097152
            assert stream.max_stream_data_local_sent == 2097152
            client._on_max_stream_data_delivery(QuicDeliveryState.LOST, stream)
            assert stream.max_stream_data_local == 2097152
            assert stream.max_stream_data_local_sent == 0

            # MAX_DATA is retransmitted and acked
            assert roundtrip(client, server) == (1, 1)
            assert stream.max_stream_data_local == 2097152
            assert stream.max_stream_data_local_sent == 2097152

    def test_send_max_streams_retransmit(self):
        with client_and_server() as (client, server):
            # client opens 65 streams
            client.send_stream_data(4 * 64, b"Z")
            assert transfer(client, server) == 1
            assert client._remote_max_streams_bidi == 128
            assert server._local_max_streams_bidi.sent == 128
            assert server._local_max_streams_bidi.used == 65
            assert server._local_max_streams_bidi.value == 128

            # MAX_STREAMS is sent and lost
            assert drop(server) == 1
            assert client._remote_max_streams_bidi == 128
            assert server._local_max_streams_bidi.sent == 256
            assert server._local_max_streams_bidi.used == 65
            assert server._local_max_streams_bidi.value == 256

            # MAX_STREAMS loss is detected
            server._on_connection_limit_delivery(
                QuicDeliveryState.LOST, server._local_max_streams_bidi
            )
            assert client._remote_max_streams_bidi == 128
            assert server._local_max_streams_bidi.sent == 0
            assert server._local_max_streams_bidi.used == 65
            assert server._local_max_streams_bidi.value == 256

            # MAX_STREAMS is retransmitted and acked
            assert roundtrip(server, client) == (1, 1)
            assert client._remote_max_streams_bidi == 256
            assert server._local_max_streams_bidi.sent == 256
            assert server._local_max_streams_bidi.used == 65
            assert server._local_max_streams_bidi.value == 256

    def test_send_ping(self):
        with client_and_server() as (client, server):
            consume_events(client)

            # client sends ping, server ACKs it
            client.send_ping(uid=12345)
            assert roundtrip(client, server) == (1, 1)

            # check event
            event = client.next_event()
            assert type(event) == events.PingAcknowledged
            assert event.uid == 12345

    def test_send_ping_retransmit(self):
        with client_and_server() as (client, server):
            consume_events(client)

            # client sends another ping, PING is lost
            client.send_ping(uid=12345)
            assert drop(client) == 1

            # PING is retransmitted and acked
            client._on_ping_delivery(QuicDeliveryState.LOST, (12345,))
            assert roundtrip(client, server) == (1, 1)

            # check event
            event = client.next_event()
            assert type(event) == events.PingAcknowledged
            assert event.uid == 12345

    def test_send_reset_stream(self):
        with client_and_server() as (client, server):
            # client creates bidirectional stream
            client.send_stream_data(0, b"hello")
            assert roundtrip(client, server) == (1, 1)

            # client resets stream
            client.reset_stream(0, QuicErrorCode.NO_ERROR)
            assert roundtrip(client, server) == (1, 1)

    def test_send_stop_sending(self):
        with client_and_server() as (client, server):
            # check handshake completed
            self.check_handshake(client=client, server=server)

            # client creates bidirectional stream
            client.send_stream_data(0, b"hello")
            assert roundtrip(client, server) == (1, 1)

            # client sends STOP_SENDING frame
            client.stop_stream(0, QuicErrorCode.NO_ERROR)
            assert roundtrip(client, server) == (1, 1)

            # client receives STREAM_RESET frame
            event = client.next_event()
            assert type(event) == events.StreamReset
            assert event.error_code == QuicErrorCode.NO_ERROR
            assert event.stream_id == 0

    def test_send_stop_sending_uni_stream(self):
        with client_and_server() as (client, server):
            # check handshake completed
            self.check_handshake(client=client, server=server)

            # client sends STOP_SENDING frame
            with pytest.raises(ValueError) as cm:
                client.stop_stream(2, QuicErrorCode.NO_ERROR)
            assert str(cm.value) == \
                "Cannot stop receiving on a local-initiated unidirectional stream"

    def test_send_stop_sending_unknown_stream(self):
        with client_and_server() as (client, server):
            # check handshake completed
            self.check_handshake(client=client, server=server)

            # client sends STOP_SENDING frame
            with pytest.raises(ValueError) as cm:
                client.stop_stream(0, QuicErrorCode.NO_ERROR)
            assert str(cm.value) == "Cannot stop receiving on an unknown stream"

    def test_send_stream_data_over_max_streams_bidi(self):
        with client_and_server() as (client, server):
            # create streams
            for i in range(128):
                stream_id = i * 4
                client.send_stream_data(stream_id, b"")
                assert not client._streams[stream_id].is_blocked
            assert len(client._streams_blocked_bidi) == 0
            assert len(client._streams_blocked_uni) == 0
            assert roundtrip(client, server) == (0, 0)

            # create one too many -> STREAMS_BLOCKED
            stream_id = 128 * 4
            client.send_stream_data(stream_id, b"")
            assert client._streams[stream_id].is_blocked
            assert len(client._streams_blocked_bidi) == 1
            assert len(client._streams_blocked_uni) == 0
            assert roundtrip(client, server) == (1, 1)

            # peer raises max streams
            client._handle_max_streams_bidi_frame(
                client_receive_context(client),
                QuicFrameType.MAX_STREAMS_BIDI,
                Buffer(data=encode_uint_var(129)),
            )
            assert not client._streams[stream_id].is_blocked

    def test_send_stream_data_over_max_streams_uni(self):
        with client_and_server() as (client, server):
            # create streams
            for i in range(128):
                stream_id = i * 4 + 2
                client.send_stream_data(stream_id, b"")
                assert not client._streams[stream_id].is_blocked
            assert len(client._streams_blocked_bidi) == 0
            assert len(client._streams_blocked_uni) == 0
            assert roundtrip(client, server) == (0, 0)

            # create one too many -> STREAMS_BLOCKED
            stream_id = 128 * 4 + 2
            client.send_stream_data(stream_id, b"")
            assert client._streams[stream_id].is_blocked
            assert len(client._streams_blocked_bidi) == 0
            assert len(client._streams_blocked_uni) == 1
            assert roundtrip(client, server) == (1, 1)

            # peer raises max streams
            client._handle_max_streams_uni_frame(
                client_receive_context(client),
                QuicFrameType.MAX_STREAMS_UNI,
                Buffer(data=encode_uint_var(129)),
            )
            assert not client._streams[stream_id].is_blocked

    def test_send_stream_data_peer_initiated(self):
        with client_and_server() as (client, server):
            # server creates bidirectional stream
            server.send_stream_data(1, b"hello")
            assert roundtrip(server, client) == (1, 1)

            # server creates unidirectional stream
            server.send_stream_data(3, b"hello")
            assert roundtrip(server, client) == (1, 1)

            # client creates bidirectional stream
            client.send_stream_data(0, b"hello")
            assert roundtrip(client, server) == (1, 1)

            # client sends data on server-initiated bidirectional stream
            client.send_stream_data(1, b"hello")
            assert roundtrip(client, server) == (1, 1)

            # client creates unidirectional stream
            client.send_stream_data(2, b"hello")
            assert roundtrip(client, server) == (1, 1)

            # client tries to reset server-initiated unidirectional stream
            with pytest.raises(ValueError) as cm:
                client.reset_stream(3, QuicErrorCode.NO_ERROR)
            assert str(cm.value) == \
                "Cannot send data on peer-initiated unidirectional stream"

            # client tries to reset unknown server-initiated bidirectional stream
            with pytest.raises(ValueError) as cm:
                client.reset_stream(5, QuicErrorCode.NO_ERROR)
            assert str(cm.value) == "Cannot send data on unknown peer-initiated stream"

            # client tries to send data on server-initiated unidirectional stream
            with pytest.raises(ValueError) as cm:
                client.send_stream_data(3, b"hello")
            assert str(cm.value) == \
                "Cannot send data on peer-initiated unidirectional stream"

            # client tries to send data on unknown server-initiated bidirectional stream
            with pytest.raises(ValueError) as cm:
                client.send_stream_data(5, b"hello")
            assert str(cm.value) == "Cannot send data on unknown peer-initiated stream"

    def test_stream_direction(self):
        with client_and_server() as (client, server):
            for off in [0, 4, 8]:
                # Client-Initiated, Bidirectional
                assert check_stream_id_for_receiving(True, off)
                assert check_stream_id_for_sending(True, off)

                assert check_stream_id_for_receiving(False, off)
                assert check_stream_id_for_sending(False, off)

                # Server-Initiated, Bidirectional
                assert check_stream_id_for_receiving(True, off+1)
                assert check_stream_id_for_sending(True, off+1)

                assert check_stream_id_for_receiving(False, off+1)
                assert check_stream_id_for_sending(False, off+1)

                # Client-Initiated, Unidirectional
                assert not check_stream_id_for_receiving(True, off + 2)
                assert check_stream_id_for_sending(True, off + 2)

                assert check_stream_id_for_receiving(False, off + 2)
                assert not check_stream_id_for_sending(False, off + 2)

                # Server-Initiated, Unidirectional
                assert check_stream_id_for_receiving(True, off + 3)
                assert not check_stream_id_for_sending(True, off + 3)

                assert not check_stream_id_for_receiving(False, off + 3)
                assert check_stream_id_for_sending(False, off + 3)

    def test_version_negotiation_fail(self):
        client = create_standalone_client(self)

        # no common version, no retry
        client.receive_datagram(
            encode_quic_version_negotiation(
                source_cid=client._peer_cid.cid,
                destination_cid=client.host_cid,
                supported_versions=[0xFF000011],  # DRAFT_16
            ),
            SERVER_ADDR,
            now=time.time(),
        )
        assert drop(client) == 0

        event = client.next_event()
        assert type(event) == events.ConnectionTerminated
        assert event.error_code == QuicErrorCode.INTERNAL_ERROR
        assert event.frame_type == QuicFrameType.PADDING
        assert event.reason_phrase == "Could not find a common protocol version"

    def test_version_negotiation_ignore(self):
        client = create_standalone_client(self)

        # version negotiation contains the client's version
        client.receive_datagram(
            encode_quic_version_negotiation(
                source_cid=client._peer_cid.cid,
                destination_cid=client.host_cid,
                supported_versions=[client._version],
            ),
            SERVER_ADDR,
            now=time.time(),
        )
        assert drop(client) == 0

    def test_version_negotiation_ignore_server(self):
        server = create_standalone_server(self)

        # Servers do not expect version negotiation packets.
        server.receive_datagram(
            encode_quic_version_negotiation(
                source_cid=server._peer_cid.cid,
                destination_cid=server.host_cid,
                supported_versions=[QuicProtocolVersion.VERSION_1],
            ),
            CLIENT_ADDR,
            now=time.time(),
        )
        self.assertPacketDropped(server, "unexpected_packet")

    def test_version_negotiation_ok(self):
        client = create_standalone_client(self)

        # found a common version, retry
        client.receive_datagram(
            encode_quic_version_negotiation(
                source_cid=client._peer_cid.cid,
                destination_cid=client.host_cid,
                supported_versions=[QuicProtocolVersion.VERSION_1],
            ),
            SERVER_ADDR,
            now=time.time(),
        )
        assert drop(client) == 0# todo: investigate!

    def test_write_connection_close_early(self):
        client = create_standalone_client(self)

        builder = QuicPacketBuilder(
            host_cid=client.host_cid,
            is_client=True,
            peer_cid=client._peer_cid.cid,
            version=client._version,
        )
        crypto = CryptoPair()
        crypto.setup_initial(client.host_cid, is_client=True, version=client._version)
        builder.start_packet(QuicPacketType.INITIAL, crypto)
        client._write_connection_close_frame(
            builder=builder,
            epoch=tls.Epoch.INITIAL,
            error_code=123,
            frame_type=None,
            reason_phrase="some reason",
        )

        assert builder.quic_logger_frames == \
            [
                {
                    "error_code": QuicErrorCode.APPLICATION_ERROR,
                    "error_space": "transport",
                    "frame_type": "connection_close",
                    "raw_error_code": QuicErrorCode.APPLICATION_ERROR,
                    "reason": "",
                    "trigger_frame_type": QuicFrameType.PADDING,
                } \
            ]

    def test_excessive_crypto_buffering(self):
        with client_and_server() as (client, server):
            # Client receives data that causes more than 512K of buffering; note that
            # because the stream buffer is a single buffer and not a set of fragments,
            # the total buffering size depends not on how much data is received, but
            # how much buffering is needed.  We send fragments of only 100 bytes
            # at offsets 10000, 20000, 30000 etc.
            highest_good_offset = 0
            with pytest.raises(QuicConnectionError) as cm:
                # We don't start at zero as we want to force buffering, not cause
                # a TLS error.
                for offset in range(10000, 1000000, 10000):
                    client._handle_crypto_frame(
                        client_receive_context(client),
                        QuicFrameType.CRYPTO,
                        Buffer(
                            data=encode_uint_var(offset)
                            + encode_uint_var(100)
                            + b"\x00" * 100
                        ),
                    )
                    highest_good_offset = offset
            assert cm.value.error_code == QuicErrorCode.CRYPTO_BUFFER_EXCEEDED
            assert cm.value.frame_type == QuicFrameType.CRYPTO
            assert highest_good_offset == (MAX_PENDING_CRYPTO // 10000) * 10000


class TestQuicNetworkPath:
    def test_can_send(self):
        path = QuicNetworkPath(("1.2.3.4", 1234))
        assert not path.is_validated

        # initially, cannot send any data
        assert path.can_send(0)
        assert not path.can_send(1)

        # receive some data
        path.bytes_received += 1
        assert path.can_send(0)
        assert path.can_send(1)
        assert path.can_send(2)
        assert path.can_send(3)
        assert not path.can_send(4)

        # send some data
        path.bytes_sent += 3
        assert path.can_send(0)
        assert not path.can_send(1)
