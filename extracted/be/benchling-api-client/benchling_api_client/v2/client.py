from typing import Dict

import attr
import httpx


@attr.s(auto_attribs=True)
class Client:
    """A class for keeping track of data related to the API."""

    base_url: str
    httpx_client: httpx.Client = attr.ib(factory=httpx.Client, kw_only=True)
    cookies: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    headers: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    timeout: float = attr.ib(5.0, kw_only=True)

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in all endpoints."""
        return {**self.headers}

    def with_headers(self, headers: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional headers."""
        return attr.evolve(self, headers={**self.headers, **headers})

    def get_cookies(self) -> Dict[str, str]:
        return {**self.cookies}

    def with_cookies(self, cookies: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional cookies."""
        return attr.evolve(self, cookies={**self.cookies, **cookies})

    def get_timeout(self) -> float:
        return self.timeout

    def with_timeout(self, timeout: float, increase_only: bool = True) -> "Client":
        """
        Get a new client matching this one with a new timeout (in seconds).

        :param timeout: The new client timeout in seconds
        :param increase_only: If True, will only use the specified timeout if it's
        higher than the existing Client timeout
        :return: A new Client with the adjusted timeout
        :rtype: Client
        """
        if (not increase_only) or timeout > self.timeout:
            return attr.evolve(self, timeout=timeout)
        return self

    def with_base_url(self, base_url: str) -> "Client":
        """Get a new client matching this one with an updated base URL."""
        return attr.evolve(self, base_url=base_url)


@attr.s(auto_attribs=True)
class AuthenticatedClient(Client):
    """A Client which has been authenticated for use on secured endpoints."""

    token: str

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in authenticated endpoints."""
        return {"Authorization": f"Bearer {self.token}", **self.headers}
