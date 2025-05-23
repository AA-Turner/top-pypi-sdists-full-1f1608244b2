import datetime

from pytest_httpx import HTTPXMock
import httpx

import httpx_auth
from httpx_auth.testing import BrowserMock, create_token, token_cache, browser_mock
import httpx_auth._oauth2.authorization_code_pkce


def test_basic_and_api_key_authentication_can_be_combined(httpx_mock: HTTPXMock):
    basic_auth = httpx_auth.Basic("test_user", "test_pwd")
    api_key_auth = httpx_auth.HeaderApiKey("my_provided_api_key")
    auth = basic_auth & api_key_auth

    httpx_mock.add_response(
        url="https://authorized_only",
        method="GET",
        match_headers={
            "Authorization": "Basic dGVzdF91c2VyOnRlc3RfcHdk",
            "X-API-Key": "my_provided_api_key",
        },
    )

    with httpx.Client() as client:
        client.get("https://authorized_only", auth=auth)


def test_header_api_key_and_multiple_authentication_can_be_combined(
    token_cache, httpx_mock: HTTPXMock
):
    api_key_auth = httpx_auth.HeaderApiKey("my_provided_api_key")
    api_key_auth2 = httpx_auth.HeaderApiKey(
        "my_provided_api_key2", header_name="X-Api-Key2"
    )
    api_key_auth3 = httpx_auth.HeaderApiKey(
        "my_provided_api_key3", header_name="X-Api-Key3"
    )
    auth = api_key_auth & (api_key_auth2 & api_key_auth3)

    httpx_mock.add_response(
        url="https://authorized_only",
        method="GET",
        match_headers={
            "X-API-Key": "my_provided_api_key",
            "X-Api-Key2": "my_provided_api_key2",
            "X-Api-Key3": "my_provided_api_key3",
        },
    )

    with httpx.Client() as client:
        client.get("https://authorized_only", auth=auth)


def test_multiple_auth_and_header_api_key_can_be_combined(
    token_cache, httpx_mock: HTTPXMock
):
    api_key_auth = httpx_auth.HeaderApiKey("my_provided_api_key")
    api_key_auth2 = httpx_auth.HeaderApiKey(
        "my_provided_api_key2", header_name="X-Api-Key2"
    )
    api_key_auth3 = httpx_auth.HeaderApiKey(
        "my_provided_api_key3", header_name="X-Api-Key3"
    )
    auth = (api_key_auth & api_key_auth2) & api_key_auth3

    httpx_mock.add_response(
        url="https://authorized_only",
        method="GET",
        match_headers={
            "X-API-Key": "my_provided_api_key",
            "X-Api-Key2": "my_provided_api_key2",
            "X-Api-Key3": "my_provided_api_key3",
        },
    )

    with httpx.Client() as client:
        client.get("https://authorized_only", auth=auth)


def test_multiple_auth_and_multiple_auth_can_be_combined(
    token_cache, httpx_mock: HTTPXMock
):
    api_key_auth = httpx_auth.HeaderApiKey("my_provided_api_key")
    api_key_auth2 = httpx_auth.HeaderApiKey(
        "my_provided_api_key2", header_name="X-Api-Key2"
    )
    api_key_auth3 = httpx_auth.HeaderApiKey(
        "my_provided_api_key3", header_name="X-Api-Key3"
    )
    api_key_auth4 = httpx_auth.HeaderApiKey(
        "my_provided_api_key4", header_name="X-Api-Key4"
    )
    auth = (api_key_auth & api_key_auth2) & (api_key_auth3 & api_key_auth4)

    httpx_mock.add_response(
        url="https://authorized_only",
        method="GET",
        match_headers={
            "X-API-Key": "my_provided_api_key",
            "X-Api-Key2": "my_provided_api_key2",
            "X-Api-Key3": "my_provided_api_key3",
            "X-Api-Key4": "my_provided_api_key4",
        },
    )

    with httpx.Client() as client:
        client.get("https://authorized_only", auth=auth)


def test_basic_and_multiple_authentication_can_be_combined(
    token_cache, httpx_mock: HTTPXMock
):
    basic_auth = httpx_auth.Basic("test_user", "test_pwd")
    api_key_auth2 = httpx_auth.HeaderApiKey(
        "my_provided_api_key2", header_name="X-Api-Key2"
    )
    api_key_auth3 = httpx_auth.HeaderApiKey(
        "my_provided_api_key3", header_name="X-Api-Key3"
    )
    auth = basic_auth & (api_key_auth2 & api_key_auth3)

    httpx_mock.add_response(
        url="https://authorized_only",
        method="GET",
        match_headers={
            "Authorization": "Basic dGVzdF91c2VyOnRlc3RfcHdk",
            "X-Api-Key2": "my_provided_api_key2",
            "X-Api-Key3": "my_provided_api_key3",
        },
    )

    with httpx.Client() as client:
        client.get("https://authorized_only", auth=auth)


def test_query_api_key_and_multiple_authentication_can_be_combined(
    token_cache, httpx_mock: HTTPXMock
):
    api_key_auth = httpx_auth.QueryApiKey("my_provided_api_key")
    api_key_auth2 = httpx_auth.QueryApiKey(
        "my_provided_api_key2", query_parameter_name="api_key2"
    )
    api_key_auth3 = httpx_auth.HeaderApiKey(
        "my_provided_api_key3", header_name="X-Api-Key3"
    )
    auth = api_key_auth & (api_key_auth2 & api_key_auth3)

    httpx_mock.add_response(
        url="https://authorized_only?api_key=my_provided_api_key&api_key2=my_provided_api_key2",
        method="GET",
        match_headers={
            "X-Api-Key3": "my_provided_api_key3",
        },
    )

    with httpx.Client() as client:
        client.get("https://authorized_only", auth=auth)


def test_oauth2_resource_owner_password_and_api_key_authentication_can_be_combined(
    token_cache, httpx_mock: HTTPXMock
):
    resource_owner_password_auth = httpx_auth.OAuth2ResourceOwnerPasswordCredentials(
        "https://provide_access_token", username="test_user", password="test_pwd"
    )
    api_key_auth = httpx_auth.HeaderApiKey("my_provided_api_key")
    auth = resource_owner_password_auth & api_key_auth

    httpx_mock.add_response(
        method="POST",
        url="https://provide_access_token",
        json={
            "access_token": "2YotnFZFEjr1zCsicMWpAA",
            "token_type": "example",
            "expires_in": 3600,
            "refresh_token": "tGzv3JOkF0XG5Qx2TlKWIA",
            "example_parameter": "example_value",
        },
    )

    httpx_mock.add_response(
        url="https://authorized_only",
        method="GET",
        match_headers={
            "Authorization": "Bearer 2YotnFZFEjr1zCsicMWpAA",
            "X-API-Key": "my_provided_api_key",
        },
    )

    with httpx.Client() as client:
        client.get("https://authorized_only", auth=auth)


def test_oauth2_resource_owner_password_and_multiple_authentication_can_be_combined(
    token_cache, httpx_mock: HTTPXMock
):
    resource_owner_password_auth = httpx_auth.OAuth2ResourceOwnerPasswordCredentials(
        "https://provide_access_token", username="test_user", password="test_pwd"
    )
    api_key_auth = httpx_auth.HeaderApiKey("my_provided_api_key")
    api_key_auth2 = httpx_auth.HeaderApiKey(
        "my_provided_api_key2", header_name="X-Api-Key2"
    )
    auth = resource_owner_password_auth & (api_key_auth & api_key_auth2)

    httpx_mock.add_response(
        method="POST",
        url="https://provide_access_token",
        json={
            "access_token": "2YotnFZFEjr1zCsicMWpAA",
            "token_type": "example",
            "expires_in": 3600,
            "refresh_token": "tGzv3JOkF0XG5Qx2TlKWIA",
            "example_parameter": "example_value",
        },
    )

    httpx_mock.add_response(
        url="https://authorized_only",
        method="GET",
        match_headers={
            "Authorization": "Bearer 2YotnFZFEjr1zCsicMWpAA",
            "X-API-Key": "my_provided_api_key",
            "X-Api-Key2": "my_provided_api_key2",
        },
    )

    with httpx.Client() as client:
        client.get("https://authorized_only", auth=auth)


def test_oauth2_client_credential_and_api_key_authentication_can_be_combined(
    token_cache, httpx_mock: HTTPXMock
):
    resource_owner_password_auth = httpx_auth.OAuth2ClientCredentials(
        "https://provide_access_token", client_id="test_user", client_secret="test_pwd"
    )
    api_key_auth = httpx_auth.HeaderApiKey("my_provided_api_key")
    auth = resource_owner_password_auth & api_key_auth

    httpx_mock.add_response(
        method="POST",
        url="https://provide_access_token",
        json={
            "access_token": "2YotnFZFEjr1zCsicMWpAA",
            "token_type": "example",
            "expires_in": 3600,
            "refresh_token": "tGzv3JOkF0XG5Qx2TlKWIA",
            "example_parameter": "example_value",
        },
    )

    httpx_mock.add_response(
        url="https://authorized_only",
        method="GET",
        match_headers={
            "Authorization": "Bearer 2YotnFZFEjr1zCsicMWpAA",
            "X-API-Key": "my_provided_api_key",
        },
    )

    with httpx.Client() as client:
        client.get("https://authorized_only", auth=auth)


def test_oauth2_client_credential_and_multiple_authentication_can_be_combined(
    token_cache, httpx_mock: HTTPXMock
):
    resource_owner_password_auth = httpx_auth.OAuth2ClientCredentials(
        "https://provide_access_token", client_id="test_user", client_secret="test_pwd"
    )
    api_key_auth = httpx_auth.HeaderApiKey("my_provided_api_key")
    api_key_auth2 = httpx_auth.HeaderApiKey(
        "my_provided_api_key2", header_name="X-Api-Key2"
    )
    auth = resource_owner_password_auth & (api_key_auth & api_key_auth2)

    httpx_mock.add_response(
        method="POST",
        url="https://provide_access_token",
        json={
            "access_token": "2YotnFZFEjr1zCsicMWpAA",
            "token_type": "example",
            "expires_in": 3600,
            "refresh_token": "tGzv3JOkF0XG5Qx2TlKWIA",
            "example_parameter": "example_value",
        },
    )

    httpx_mock.add_response(
        url="https://authorized_only",
        method="GET",
        match_headers={
            "Authorization": "Bearer 2YotnFZFEjr1zCsicMWpAA",
            "X-API-Key": "my_provided_api_key",
            "X-Api-Key2": "my_provided_api_key2",
        },
    )

    with httpx.Client() as client:
        client.get("https://authorized_only", auth=auth)


def test_oauth2_authorization_code_and_api_key_authentication_can_be_combined(
    token_cache, httpx_mock: HTTPXMock, browser_mock: BrowserMock, unused_tcp_port: int
):
    authorization_code_auth = httpx_auth.OAuth2AuthorizationCode(
        "https://provide_code",
        "https://provide_access_token",
        redirect_uri_port=unused_tcp_port,
    )
    api_key_auth = httpx_auth.HeaderApiKey("my_provided_api_key")
    auth = authorization_code_auth & api_key_auth

    tab = browser_mock.add_response(
        opened_url=f"https://provide_code?response_type=code&state=ce9c755b41b5e3c5b64c70598715d5de271023a53f39a67a70215d265d11d2bfb6ef6e9c701701e998e69cbdbf2cee29fd51d2a950aa05f59a20cf4a646099d5&redirect_uri=http%3A%2F%2Flocalhost%3A{unused_tcp_port}%2F",
        reply_url=f"http://localhost:{unused_tcp_port}#code=SplxlOBeZQQYbYS6WxSbIA&state=ce9c755b41b5e3c5b64c70598715d5de271023a53f39a67a70215d265d11d2bfb6ef6e9c701701e998e69cbdbf2cee29fd51d2a950aa05f59a20cf4a646099d5",
    )

    httpx_mock.add_response(
        method="POST",
        url="https://provide_access_token",
        json={
            "access_token": "2YotnFZFEjr1zCsicMWpAA",
            "token_type": "example",
            "expires_in": 3600,
            "refresh_token": "tGzv3JOkF0XG5Qx2TlKWIA",
            "example_parameter": "example_value",
        },
    )

    httpx_mock.add_response(
        url="https://authorized_only",
        method="GET",
        match_headers={
            "Authorization": "Bearer 2YotnFZFEjr1zCsicMWpAA",
            "X-API-Key": "my_provided_api_key",
        },
    )

    with httpx.Client() as client:
        client.get("https://authorized_only", auth=auth)

    tab.assert_success()


def test_oauth2_authorization_code_and_multiple_authentication_can_be_combined(
    token_cache, httpx_mock: HTTPXMock, browser_mock: BrowserMock, unused_tcp_port: int
):
    authorization_code_auth = httpx_auth.OAuth2AuthorizationCode(
        "https://provide_code",
        "https://provide_access_token",
        redirect_uri_port=unused_tcp_port,
    )
    api_key_auth = httpx_auth.HeaderApiKey("my_provided_api_key")
    api_key_auth2 = httpx_auth.HeaderApiKey(
        "my_provided_api_key2", header_name="X-Api-Key2"
    )
    auth = authorization_code_auth & (api_key_auth & api_key_auth2)

    tab = browser_mock.add_response(
        opened_url=f"https://provide_code?response_type=code&state=ce9c755b41b5e3c5b64c70598715d5de271023a53f39a67a70215d265d11d2bfb6ef6e9c701701e998e69cbdbf2cee29fd51d2a950aa05f59a20cf4a646099d5&redirect_uri=http%3A%2F%2Flocalhost%3A{unused_tcp_port}%2F",
        reply_url=f"http://localhost:{unused_tcp_port}#code=SplxlOBeZQQYbYS6WxSbIA&state=ce9c755b41b5e3c5b64c70598715d5de271023a53f39a67a70215d265d11d2bfb6ef6e9c701701e998e69cbdbf2cee29fd51d2a950aa05f59a20cf4a646099d5",
    )

    httpx_mock.add_response(
        method="POST",
        url="https://provide_access_token",
        json={
            "access_token": "2YotnFZFEjr1zCsicMWpAA",
            "token_type": "example",
            "expires_in": 3600,
            "refresh_token": "tGzv3JOkF0XG5Qx2TlKWIA",
            "example_parameter": "example_value",
        },
    )

    httpx_mock.add_response(
        url="https://authorized_only",
        method="GET",
        match_headers={
            "Authorization": "Bearer 2YotnFZFEjr1zCsicMWpAA",
            "X-API-Key": "my_provided_api_key",
            "X-Api-Key2": "my_provided_api_key2",
        },
    )

    with httpx.Client() as client:
        client.get("https://authorized_only", auth=auth)

    tab.assert_success()


def test_oauth2_pkce_and_api_key_authentication_can_be_combined(
    token_cache,
    httpx_mock: HTTPXMock,
    browser_mock: BrowserMock,
    monkeypatch,
    unused_tcp_port: int,
):
    monkeypatch.setattr(
        httpx_auth._oauth2.authorization_code_pkce.os, "urandom", lambda x: b"1" * 63
    )
    pkce_auth = httpx_auth.OAuth2AuthorizationCodePKCE(
        "https://provide_code",
        "https://provide_access_token",
        redirect_uri_port=unused_tcp_port,
    )
    api_key_auth = httpx_auth.HeaderApiKey("my_provided_api_key")
    auth = pkce_auth & api_key_auth

    tab = browser_mock.add_response(
        opened_url=f"https://provide_code?response_type=code&state=ce9c755b41b5e3c5b64c70598715d5de271023a53f39a67a70215d265d11d2bfb6ef6e9c701701e998e69cbdbf2cee29fd51d2a950aa05f59a20cf4a646099d5&redirect_uri=http%3A%2F%2Flocalhost%3A{unused_tcp_port}%2F&code_challenge=5C_ph_KZ3DstYUc965SiqmKAA-ShvKF4Ut7daKd3fjc&code_challenge_method=S256",
        reply_url=f"http://localhost:{unused_tcp_port}#code=SplxlOBeZQQYbYS6WxSbIA&state=ce9c755b41b5e3c5b64c70598715d5de271023a53f39a67a70215d265d11d2bfb6ef6e9c701701e998e69cbdbf2cee29fd51d2a950aa05f59a20cf4a646099d5",
    )

    httpx_mock.add_response(
        method="POST",
        url="https://provide_access_token",
        json={
            "access_token": "2YotnFZFEjr1zCsicMWpAA",
            "token_type": "example",
            "expires_in": 3600,
            "refresh_token": "tGzv3JOkF0XG5Qx2TlKWIA",
            "example_parameter": "example_value",
        },
    )

    httpx_mock.add_response(
        url="https://authorized_only",
        method="GET",
        match_headers={
            "Authorization": "Bearer 2YotnFZFEjr1zCsicMWpAA",
            "X-API-Key": "my_provided_api_key",
        },
    )

    with httpx.Client() as client:
        client.get("https://authorized_only", auth=auth)

    tab.assert_success()


def test_oauth2_pkce_and_multiple_authentication_can_be_combined(
    token_cache,
    httpx_mock: HTTPXMock,
    browser_mock: BrowserMock,
    monkeypatch,
    unused_tcp_port: int,
):
    monkeypatch.setattr(
        httpx_auth._oauth2.authorization_code_pkce.os, "urandom", lambda x: b"1" * 63
    )
    pkce_auth = httpx_auth.OAuth2AuthorizationCodePKCE(
        "https://provide_code",
        "https://provide_access_token",
        redirect_uri_port=unused_tcp_port,
    )
    api_key_auth = httpx_auth.HeaderApiKey("my_provided_api_key")
    api_key_auth2 = httpx_auth.HeaderApiKey(
        "my_provided_api_key2", header_name="X-Api-Key2"
    )
    auth = pkce_auth & (api_key_auth & api_key_auth2)

    tab = browser_mock.add_response(
        opened_url=f"https://provide_code?response_type=code&state=ce9c755b41b5e3c5b64c70598715d5de271023a53f39a67a70215d265d11d2bfb6ef6e9c701701e998e69cbdbf2cee29fd51d2a950aa05f59a20cf4a646099d5&redirect_uri=http%3A%2F%2Flocalhost%3A{unused_tcp_port}%2F&code_challenge=5C_ph_KZ3DstYUc965SiqmKAA-ShvKF4Ut7daKd3fjc&code_challenge_method=S256",
        reply_url=f"http://localhost:{unused_tcp_port}#code=SplxlOBeZQQYbYS6WxSbIA&state=ce9c755b41b5e3c5b64c70598715d5de271023a53f39a67a70215d265d11d2bfb6ef6e9c701701e998e69cbdbf2cee29fd51d2a950aa05f59a20cf4a646099d5",
    )

    httpx_mock.add_response(
        method="POST",
        url="https://provide_access_token",
        json={
            "access_token": "2YotnFZFEjr1zCsicMWpAA",
            "token_type": "example",
            "expires_in": 3600,
            "refresh_token": "tGzv3JOkF0XG5Qx2TlKWIA",
            "example_parameter": "example_value",
        },
    )

    httpx_mock.add_response(
        url="https://authorized_only",
        method="GET",
        match_headers={
            "Authorization": "Bearer 2YotnFZFEjr1zCsicMWpAA",
            "X-API-Key": "my_provided_api_key",
            "X-Api-Key2": "my_provided_api_key2",
        },
    )

    with httpx.Client() as client:
        client.get("https://authorized_only", auth=auth)

    tab.assert_success()


def test_oauth2_implicit_and_api_key_authentication_can_be_combined(
    token_cache, httpx_mock: HTTPXMock, browser_mock: BrowserMock, unused_tcp_port: int
):
    implicit_auth = httpx_auth.OAuth2Implicit(
        "https://provide_token",
        redirect_uri_port=unused_tcp_port,
    )
    api_key_auth = httpx_auth.HeaderApiKey("my_provided_api_key")
    auth = implicit_auth & api_key_auth

    expiry_in_1_hour = datetime.datetime.now(
        datetime.timezone.utc
    ) + datetime.timedelta(hours=1)
    token = create_token(expiry_in_1_hour)
    tab = browser_mock.add_response(
        opened_url=f"https://provide_token?response_type=token&state=bee505cb6ceb14b9f6ac3573cd700b3b3e965004078d7bb57c7b92df01e448c992a7a46b4804164fc998ea166ece3f3d5849ca2405c4a548f43b915b0677231c&redirect_uri=http%3A%2F%2Flocalhost%3A{unused_tcp_port}%2F",
        reply_url=f"http://localhost:{unused_tcp_port}",
        data=f"access_token={token}&state=bee505cb6ceb14b9f6ac3573cd700b3b3e965004078d7bb57c7b92df01e448c992a7a46b4804164fc998ea166ece3f3d5849ca2405c4a548f43b915b0677231c",
    )

    httpx_mock.add_response(
        url="https://authorized_only",
        method="GET",
        match_headers={
            "Authorization": f"Bearer {token}",
            "X-API-Key": "my_provided_api_key",
        },
    )

    with httpx.Client() as client:
        client.get("https://authorized_only", auth=auth)

    tab.assert_success()


def test_oauth2_implicit_and_multiple_authentication_can_be_combined(
    token_cache, httpx_mock: HTTPXMock, browser_mock: BrowserMock, unused_tcp_port: int
):
    implicit_auth = httpx_auth.OAuth2Implicit(
        "https://provide_token",
        redirect_uri_port=unused_tcp_port,
    )
    api_key_auth = httpx_auth.HeaderApiKey("my_provided_api_key")
    api_key_auth2 = httpx_auth.HeaderApiKey(
        "my_provided_api_key2", header_name="X-Api-Key2"
    )
    auth = implicit_auth & (api_key_auth & api_key_auth2)

    expiry_in_1_hour = datetime.datetime.now(
        datetime.timezone.utc
    ) + datetime.timedelta(hours=1)
    token = create_token(expiry_in_1_hour)
    tab = browser_mock.add_response(
        opened_url=f"https://provide_token?response_type=token&state=bee505cb6ceb14b9f6ac3573cd700b3b3e965004078d7bb57c7b92df01e448c992a7a46b4804164fc998ea166ece3f3d5849ca2405c4a548f43b915b0677231c&redirect_uri=http%3A%2F%2Flocalhost%3A{unused_tcp_port}%2F",
        reply_url=f"http://localhost:{unused_tcp_port}",
        data=f"access_token={token}&state=bee505cb6ceb14b9f6ac3573cd700b3b3e965004078d7bb57c7b92df01e448c992a7a46b4804164fc998ea166ece3f3d5849ca2405c4a548f43b915b0677231c",
    )

    httpx_mock.add_response(
        url="https://authorized_only",
        method="GET",
        match_headers={
            "Authorization": f"Bearer {token}",
            "X-API-Key": "my_provided_api_key",
            "X-Api-Key2": "my_provided_api_key2",
        },
    )

    with httpx.Client() as client:
        client.get("https://authorized_only", auth=auth)

    tab.assert_success()
