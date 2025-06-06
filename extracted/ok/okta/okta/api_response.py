import json
import xmltodict
from okta.api_client import APIClient
from okta.models import Group, GroupSchema, User, UserSchema

from okta.utils import convert_absolute_url_into_relative_url


class OktaAPIResponse():
    """
    Class for defining the wrapper of an Okta API response.
    Allows for paginated results to be retrieved easily.
    """

    def __init__(self, request_executor, req, res_details, response_body="",
                 data_type=None):
        self._url = res_details.url
        self._headers = req["headers"]
        self._resp_headers = res_details.headers
        self._self = None  # Link to first page of results
        self._body = None  # First page of results
        self._type = data_type
        self._status = res_details.status

        # Status on if there's a next page of results (based on generator)
        self._next = None

        # Request Executor for future calls
        self._request_executor = request_executor

        # Build response body based on content type
        if "application/xml" in res_details.content_type:
            self.build_xml_response(response_body)
        elif "application/json" in res_details.content_type or \
                "" == res_details.content_type:
            self.build_json_response(response_body)
        else:
            # Save response as text
            self._body = response_body

        # Get links for next if more results exist
        if self._body is not None:
            self.extract_pagination(res_details.links)
            self._current = self._body

    def get_headers(self):
        """
        Returns the response body of the Okta API Response.

        Returns:
            CIMultiDictProxy: dict-like object
        """
        return self._resp_headers

    def get_body(self):
        """
        Returns the response body of the Okta API Response.

        Returns:
            dict: Dictionary format of response
        """
        return self._body

    def get_status(self):
        """
        Returns HTTP Status Code of response

        Returns:
            int: HTTP Code
        """
        return self._status

    def get_type(self):
        """
        Returns datatype of the API response

        Returns:
            class: type of object
        """
        return self._type

    def build_json_response(self, response_body):
        """
        Converts JSON response text into Python dictionary.

        Args:
            response_body (str): Response text
        """
        self._body = json.loads(response_body)

    def build_xml_response(self, response_body):
        """
        Converts XML response text into Python dictionary.

        Args:
            response_body ([type]): [description]
        """
        self._body = xmltodict.parse(response_body, xml_attribs=True)

    def extract_pagination(self, links):
        """
        Parses the Link Headers in the Okta API Response to see if there
        are more results.

        Args:
            links (dict): Dictionary object of values in the 'Link' header
        """

        # Check for 'self' link
        if "self" in links:
            self._self = convert_absolute_url_into_relative_url(links["self"]["url"].human_repr())
        # Check for 'next' link
        if "next" in links:
            self._next = convert_absolute_url_into_relative_url(links["next"]["url"].human_repr())

    def has_next(self):
        """
        Returns if there is another page after the last response retrieved
        (Determined by generator).

        Returns:
            bool: Existence of next page of results
        """
        return self._next is not None

    async def next(self, includeResponse=False):
        """
        Generator iterating function. Retrieves the next page of results
        from the API.

        Returns:
            json: Next page of results
        """
        # if not self.has_next():
        #     return (None, None)  #This causes errors with our async testing
        MODELS_NOT_TO_CAMEL_CASE = [User, Group, UserSchema, GroupSchema]
        next_page, error, next_response = await self.get_next().__anext__()
        if error:
            return (None, error)
        if self._type is not None:
            result = []
            for item in next_page:
                result.append(self._type(item) if self._type in MODELS_NOT_TO_CAMEL_CASE
                              else self._type(APIClient.form_response_body(item)))
            if includeResponse:
                return (result, None, next_response)
            else:
                return (result, None)

        if includeResponse:
            return (next_page, error, next_response)
        else:
            return (next_page, error)

    async def get_next(self):
        """
        Async Generator function for results pagination.

        Yields:
            (json, Exception): Next page of results, Error raised
        """
        while self._next:
            # Retrieve next when next page exists

            # Create and fire request
            next_request, error = await self._request_executor.create_request(
                "GET", self._next, {}, self._headers)
            if error:
                # Return None if error and set next to none
                self._next = None
                yield (None, error, None)

            req, res_details, resp_body, error = await \
                self._request_executor.fire_request(next_request)
            if error:
                # Return None if error and set next to none
                self._next = None
                yield (None, error, None)

            if next_request:
                # create new response and update generator values
                next_response = OktaAPIResponse(
                    self._request_executor, req, res_details, resp_body, self._type)
                self._next = next_response._next
                # yield next page
                yield (next_response.get_body(), None, next_response)
