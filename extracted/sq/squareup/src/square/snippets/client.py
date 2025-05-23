# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from .raw_client import RawSnippetsClient
from ..core.request_options import RequestOptions
from ..types.get_snippet_response import GetSnippetResponse
from ..requests.snippet import SnippetParams
from ..types.upsert_snippet_response import UpsertSnippetResponse
from ..types.delete_snippet_response import DeleteSnippetResponse
from ..core.client_wrapper import AsyncClientWrapper
from .raw_client import AsyncRawSnippetsClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SnippetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSnippetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSnippetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSnippetsClient
        """
        return self._raw_client

    def get(self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetSnippetResponse:
        """
        Retrieves your snippet from a Square Online site. A site can contain snippets from multiple snippet applications, but you can retrieve only the snippet that was added by your application.

        You can call [ListSites](api-endpoint:Sites-ListSites) to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

        Parameters
        ----------
        site_id : str
            The ID of the site that contains the snippet.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSnippetResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.snippets.get(
            site_id="site_id",
        )
        """
        response = self._raw_client.get(site_id, request_options=request_options)
        return response.data

    def upsert(
        self, site_id: str, *, snippet: SnippetParams, request_options: typing.Optional[RequestOptions] = None
    ) -> UpsertSnippetResponse:
        """
        Adds a snippet to a Square Online site or updates the existing snippet on the site.
        The snippet code is appended to the end of the `head` element on every page of the site, except checkout pages. A snippet application can add one snippet to a given site.

        You can call [ListSites](api-endpoint:Sites-ListSites) to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

        Parameters
        ----------
        site_id : str
            The ID of the site where you want to add or update the snippet.

        snippet : SnippetParams
            The snippet for the site.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpsertSnippetResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.snippets.upsert(
            site_id="site_id",
            snippet={"content": "<script>var js = 1;</script>"},
        )
        """
        response = self._raw_client.upsert(site_id, snippet=snippet, request_options=request_options)
        return response.data

    def delete(self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> DeleteSnippetResponse:
        """
        Removes your snippet from a Square Online site.

        You can call [ListSites](api-endpoint:Sites-ListSites) to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

        Parameters
        ----------
        site_id : str
            The ID of the site that contains the snippet.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteSnippetResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.snippets.delete(
            site_id="site_id",
        )
        """
        response = self._raw_client.delete(site_id, request_options=request_options)
        return response.data


class AsyncSnippetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSnippetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSnippetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSnippetsClient
        """
        return self._raw_client

    async def get(self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetSnippetResponse:
        """
        Retrieves your snippet from a Square Online site. A site can contain snippets from multiple snippet applications, but you can retrieve only the snippet that was added by your application.

        You can call [ListSites](api-endpoint:Sites-ListSites) to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

        Parameters
        ----------
        site_id : str
            The ID of the site that contains the snippet.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSnippetResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.snippets.get(
                site_id="site_id",
            )


        asyncio.run(main())
        """
        response = await self._raw_client.get(site_id, request_options=request_options)
        return response.data

    async def upsert(
        self, site_id: str, *, snippet: SnippetParams, request_options: typing.Optional[RequestOptions] = None
    ) -> UpsertSnippetResponse:
        """
        Adds a snippet to a Square Online site or updates the existing snippet on the site.
        The snippet code is appended to the end of the `head` element on every page of the site, except checkout pages. A snippet application can add one snippet to a given site.

        You can call [ListSites](api-endpoint:Sites-ListSites) to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

        Parameters
        ----------
        site_id : str
            The ID of the site where you want to add or update the snippet.

        snippet : SnippetParams
            The snippet for the site.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpsertSnippetResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.snippets.upsert(
                site_id="site_id",
                snippet={"content": "<script>var js = 1;</script>"},
            )


        asyncio.run(main())
        """
        response = await self._raw_client.upsert(site_id, snippet=snippet, request_options=request_options)
        return response.data

    async def delete(
        self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteSnippetResponse:
        """
        Removes your snippet from a Square Online site.

        You can call [ListSites](api-endpoint:Sites-ListSites) to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

        Parameters
        ----------
        site_id : str
            The ID of the site that contains the snippet.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteSnippetResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.snippets.delete(
                site_id="site_id",
            )


        asyncio.run(main())
        """
        response = await self._raw_client.delete(site_id, request_options=request_options)
        return response.data
