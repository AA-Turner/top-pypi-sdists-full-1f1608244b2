# !/usr/bin/env python
# encoding: utf-8
import json
import requests
from email.feedparser import FeedParser
from .json_object import *
from ..core import is_third

def get_prepared_request_details(request):
    if request is None:
        return "The request is None."
    
    try:
        method = request.method or "Unknown Method"
        url = request.url or "Unknown URL"
        headers = dict(request.headers) if request.headers else {}
        details = [
            f"Method: {method}",
            f"URL: {url}",
            f"Headers: {headers}"
        ]
        return "\n".join(details)
    except Exception as e:
        return f"Error generating request details: {str(e)}"


class ApiResponse:
    def __init__(self, request=None, response=None):
        self._request = request
        self._response = response

    def ok(self):
        return self._response.ok

    def raw(self):
        return self._response.raw

    def body(self):
        return self._response.content

    def text(self):
        return self._response.text

    def json_dict(self):
        if not self._is_content_type('application/json'):
            raise Exception('Response is not JSON')

        return self._response.json()

    def json(self):
        return unfold(self._response.json())

    def multipart(self):
        if not self._is_content_type('multipart/mixed'):
            raise Exception('Response is not Batch (Multipart)')

        parts = self._break_into_parts()

        if len(parts) < 1:
            raise Exception("Malformed Batch Response (not enough parts)")  # sic! not specific extension

        statuses = json.loads(parts[0].get_payload())

        if len(statuses["response"]) != len(parts) - 1:
            raise Exception("Malformed Batch Response (not-consistent number of parts)")

        responses = []

        for response, payload in zip(statuses["response"], parts[1:]):
            res = create_response(payload, response['status'])

            responses.append(ApiResponse(response=res))

        return responses

    def error(self):

        if self._response is None or self.ok():
            return None

        message = 'HTTP ' + str(self._response.status_code) + ' ' + self._response.text

        if self._request is not None:
            message = message + ' (request details: ' + get_prepared_request_details(self._request) + ')'

        # try:
        #     data = self.json_dict()

        #     if 'message' in data:
        #         message = data['message']
        #     elif 'error_description' in data:
        #         message = data['error_description']
        #     elif 'description' in data:
        #         message = data['description']

        # except Exception as e:
        #     message = message + ' (and additional error happened during JSON parse: ' + e.message + ')'

        return message

    def request(self):
        return self._request

    def response(self):
        return self._response

    def _is_content_type(self, content_type):
        return self._get_content_type().lower().find(content_type) >= 0

    def _get_content_type(self):
        return self._response.headers.get('Content-Type') or ''

    def _break_into_parts(self):
        p = FeedParser()

        for h in self._response.headers:
            p.feed(h + ':' + self._response.headers[h] + "\r\n")

        p.feed("\r\n")
        p.feed(self.text())

        msg = p.close()

        parts = msg.get_payload()

        return parts


def create_response(payload, status):
    res = requests.Response()
    res.headers = dict(payload)
    if is_third():
        res._content = bytes(payload.get_payload(), 'utf8')
        res.encoding = 'utf8'
    else:
        res._content = str(payload.get_payload())
    res.status_code = status
    return res
