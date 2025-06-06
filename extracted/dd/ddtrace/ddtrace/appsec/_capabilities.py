import base64
import enum
from typing import Optional

from ddtrace._trace import tracer
from ddtrace.internal import core
from ddtrace.settings._config import config
from ddtrace.settings.asm import config as asm_config


class Flags(enum.IntFlag):
    ASM_ACTIVATION = 1 << 1
    ASM_IP_BLOCKING = 1 << 2
    ASM_DD_RULES = 1 << 3
    ASM_EXCLUSIONS = 1 << 4
    ASM_REQUEST_BLOCKING = 1 << 5
    ASM_ASM_RESPONSE_BLOCKING = 1 << 6
    ASM_USER_BLOCKING = 1 << 7
    ASM_CUSTOM_RULES = 1 << 8
    ASM_CUSTOM_BLOCKING_RESPONSE = 1 << 9
    ASM_TRUSTED_IPS = 1 << 10
    ASM_EXCLUSION_DATA = 1 << 18
    ASM_RASP_SQLI = 1 << 21
    ASM_RASP_LFI = 1 << 22
    ASM_RASP_SSRF = 1 << 23
    ASM_RASP_SHI = 1 << 24
    ASM_RASP_XXE = 1 << 25
    ASM_RASP_RCE = 1 << 26
    ASM_RASP_NOSQLI = 1 << 27
    ASM_RASP_XSS = 1 << 28
    ASM_AUTO_USER = 1 << 31
    ASM_ENDPOINT_FINGERPRINT = 1 << 32
    ASM_SESSION_FINGERPRINT = 1 << 33
    ASM_NETWORK_FINGERPRINT = 1 << 34
    ASM_HEADER_FINGERPRINT = 1 << 35
    ASM_RASP_CMDI = 1 << 37
    ASM_DD_MULTICONFIG = 1 << 42
    ASM_TRACE_TAGGING_RULES = 1 << 43


_ALL_ASM_BLOCKING = (
    Flags.ASM_IP_BLOCKING
    | Flags.ASM_DD_RULES
    | Flags.ASM_EXCLUSIONS
    | Flags.ASM_REQUEST_BLOCKING
    | Flags.ASM_ASM_RESPONSE_BLOCKING
    | Flags.ASM_USER_BLOCKING
    | Flags.ASM_CUSTOM_RULES
    | Flags.ASM_CUSTOM_BLOCKING_RESPONSE
    | Flags.ASM_EXCLUSION_DATA
    | Flags.ASM_ENDPOINT_FINGERPRINT
    | Flags.ASM_SESSION_FINGERPRINT
    | Flags.ASM_NETWORK_FINGERPRINT
    | Flags.ASM_HEADER_FINGERPRINT
    | Flags.ASM_DD_MULTICONFIG
    | Flags.ASM_TRACE_TAGGING_RULES
)

_ALL_RASP = Flags.ASM_RASP_SQLI | Flags.ASM_RASP_LFI | Flags.ASM_RASP_SSRF | Flags.ASM_RASP_SHI | Flags.ASM_RASP_CMDI
_FEATURE_REQUIRED = Flags.ASM_ACTIVATION | Flags.ASM_AUTO_USER


def _asm_feature_is_required() -> bool:
    flags = _rc_capabilities()
    return (_FEATURE_REQUIRED & flags) != 0


def _rc_capabilities(test_tracer: Optional[tracer.Tracer] = None) -> Flags:
    tracer = core.tracer if test_tracer is None else test_tracer
    value = Flags(0)
    if config._remote_config_enabled:
        if asm_config._asm_can_be_enabled:
            value |= Flags.ASM_ACTIVATION
        if tracer._appsec_processor and asm_config._asm_static_rule_file is None:  # type: ignore
            value |= _ALL_ASM_BLOCKING
            if asm_config._ep_enabled:
                value |= _ALL_RASP
        if asm_config._auto_user_instrumentation_enabled:
            value |= Flags.ASM_AUTO_USER
    return value


def _appsec_rc_capabilities(test_tracer: Optional[tracer.Tracer] = None) -> str:
    r"""return the bit representation of the composed capabilities in base64
    bit 0: Reserved
    bit 1: ASM 1-click Activation
    bit 2: ASM Ip blocking

    Int Number  -> binary number    -> bytes representation -> base64 representation
    ASM Activation:
    2           -> 10               -> b'\x02'              -> "Ag=="
    ASM Ip blocking:
    4           -> 100              -> b'\x04'              -> "BA=="
    ASM Activation and ASM Ip blocking:
    6           -> 110              -> b'\x06'              -> "Bg=="
    ...
    256         -> 100000000        -> b'\x01\x00'          -> b'AQA='
    """
    value = _rc_capabilities(test_tracer=test_tracer)
    return base64.b64encode(value.to_bytes((value.bit_length() + 7) // 8, "big")).decode()
