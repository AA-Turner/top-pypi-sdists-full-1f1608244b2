from .input_models.graph_parameters import ICMP

ECHO_REPLY = ICMP(type=0, code=0)
NET_UNREACHABLE = ICMP(type=3, code=0)
HOST_UNREACHABLE = ICMP(type=3, code=1)
PROTOCOL_UNREACHABLE = ICMP(type=3, code=2)
PORT_UNREACHABLE = ICMP(type=3, code=3)
FRAGMENTATION_NEEDED = ICMP(type=3, code=4)
SOURCE_ROUTE_FAILED = ICMP(type=3, code=5)
DESTINATION_NETWORK_UNKNOWN = ICMP(type=3, code=6)
DESTINATION_HOST_UNKNOWN = ICMP(type=3, code=7)
SOURCE_HOST_ISOLATED = ICMP(type=3, code=8)
DESTINATION_NETWORK_ADMIN_PROHIBITED = ICMP(type=3, code=9)
DESTINATION_HOST_ADMIN_PROHIBITED = ICMP(type=3, code=10)
DESTINATION_NETWORK_UNREACHABLE_FOR_TOS = ICMP(type=3, code=11)
DESTINATION_HOST_UNREACHABLE_FOR_TOS = ICMP(type=3, code=12)
COMMUNICATION_ADMINISTRATIVELY_PROHIBITED = ICMP(type=3, code=13)
HOST_PRECEDENCE_VIOLATION = ICMP(type=3, code=14)
PRECEDENCE_CUTOFF_IN_EFFECT = ICMP(type=3, code=15)
SOURCE_QUENCH = ICMP(type=4, code=0)
REDIRECT_DATAGRAM_FOR_THE_NETWORK = ICMP(type=5, code=0)
REDIRECT_DATAGRAM_FOR_THE_HOST = ICMP(type=5, code=1)
REDIRECT_DATAGRAM_FOR_THE_TOS_AND_NETWORK = ICMP(type=5, code=2)
REDIRECT_DATAGRAM_FOR_THE_TOS_AND_HOST = ICMP(type=5, code=3)
ALTERNATE_ADDRESS_FOR_HOST = ICMP(type=6, code=0)
ECHO_REQUEST = ICMP(type=8, code=0)
NORMAL_ROUTER_ADVERTISEMENT = ICMP(type=9, code=0)
DOES_NOT_ROUTE_COMMON_TRAFFIC = ICMP(type=9, code=16)
ROUTER_SOLICITATION = ICMP(type=10, code=0)
TIME_TO_LIVE_EXCEEDED_IN_TRANSIT = ICMP(type=11, code=0)
FRAGMENT_REASSEMBLY_TIME_EXCEEDED = ICMP(type=11, code=1)
POINTER_INDICATES_THE_ERROR = ICMP(type=12, code=0)
MISSING_A_REQUIRED_OPTION = ICMP(type=12, code=1)
BAD_LENGTH = ICMP(type=12, code=2)
TIMESTAMP_REQUEST = ICMP(type=13, code=0)
TIMESTAMP_REPLY = ICMP(type=14, code=0)
INFORMATION_REQUEST = ICMP(type=15, code=0)
INFORMATION_REPLY = ICMP(type=16, code=0)
MASK_REQUEST = ICMP(type=17, code=0)
MASK_REPLY = ICMP(type=18, code=0)
BAD_SPI = ICMP(type=40, code=0)
AUTHENTICATION_FAILED = ICMP(type=40, code=1)
DECOMPRESSION_FAILED = ICMP(type=40, code=2)
DECRYPTION_FAILED = ICMP(type=40, code=3)
NEED_AUTHENTICATION = ICMP(type=40, code=4)
NEED_AUTHORIZATION = ICMP(type=40, code=5)

__all__ = [
    "ICMP",
    "ECHO_REPLY",
    "NET_UNREACHABLE",
    "HOST_UNREACHABLE",
    "PROTOCOL_UNREACHABLE",
    "PORT_UNREACHABLE",
    "FRAGMENTATION_NEEDED",
    "SOURCE_ROUTE_FAILED",
    "DESTINATION_NETWORK_UNKNOWN",
    "DESTINATION_HOST_UNKNOWN",
    "SOURCE_HOST_ISOLATED",
    "DESTINATION_NETWORK_ADMIN_PROHIBITED",
    "DESTINATION_HOST_ADMIN_PROHIBITED",
    "DESTINATION_NETWORK_UNREACHABLE_FOR_TOS",
    "DESTINATION_HOST_UNREACHABLE_FOR_TOS",
    "COMMUNICATION_ADMINISTRATIVELY_PROHIBITED",
    "HOST_PRECEDENCE_VIOLATION",
    "PRECEDENCE_CUTOFF_IN_EFFECT",
    "SOURCE_QUENCH",
    "REDIRECT_DATAGRAM_FOR_THE_NETWORK",
    "REDIRECT_DATAGRAM_FOR_THE_HOST",
    "REDIRECT_DATAGRAM_FOR_THE_TOS_AND_NETWORK",
    "REDIRECT_DATAGRAM_FOR_THE_TOS_AND_HOST",
    "ALTERNATE_ADDRESS_FOR_HOST",
    "ECHO_REQUEST",
    "NORMAL_ROUTER_ADVERTISEMENT",
    "DOES_NOT_ROUTE_COMMON_TRAFFIC",
    "ROUTER_SOLICITATION",
    "TIME_TO_LIVE_EXCEEDED_IN_TRANSIT",
    "FRAGMENT_REASSEMBLY_TIME_EXCEEDED",
    "POINTER_INDICATES_THE_ERROR",
    "MISSING_A_REQUIRED_OPTION",
    "BAD_LENGTH",
    "TIMESTAMP_REQUEST",
    "TIMESTAMP_REPLY",
    "INFORMATION_REQUEST",
    "INFORMATION_REPLY",
    "MASK_REQUEST",
    "MASK_REPLY",
    "BAD_SPI",
    "AUTHENTICATION_FAILED",
    "DECOMPRESSION_FAILED",
    "DECRYPTION_FAILED",
    "NEED_AUTHENTICATION",
    "NEED_AUTHORIZATION",
]
