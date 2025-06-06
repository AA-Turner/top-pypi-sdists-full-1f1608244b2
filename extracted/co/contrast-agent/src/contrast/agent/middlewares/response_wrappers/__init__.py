# Copyright © 2025 Contrast Security, Inc.
# See https://www.contrastsecurity.com/enduser-terms-0317a for more details.

from contrast.agent.middlewares.response_wrappers.base_response_wrapper import (
    BaseResponseWrapper,
)


def get_otel_attributes(response: BaseResponseWrapper) -> dict:
    """
    Returns attributes following OpenTelemetry semantic conventions for HTTP responses.
    """
    return {
        "http.response.status_code": response.status_code,
    }
