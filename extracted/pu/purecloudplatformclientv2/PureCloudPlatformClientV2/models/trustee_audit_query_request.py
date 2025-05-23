# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from datetime import datetime
from datetime import date
from pprint import pformat
import re
import json

from ..utils import sanitize_for_serialization

# type hinting support
from typing import TYPE_CHECKING
from typing import List
from typing import Dict

if TYPE_CHECKING:
    from . import Facet
    from . import Filter

class TrusteeAuditQueryRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        TrusteeAuditQueryRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'trustee_organization_ids': 'list[str]',
            'trustee_user_ids': 'list[str]',
            'start_date': 'datetime',
            'end_date': 'datetime',
            'query_phrase': 'str',
            'facets': 'list[Facet]',
            'filters': 'list[Filter]'
        }

        self.attribute_map = {
            'trustee_organization_ids': 'trusteeOrganizationIds',
            'trustee_user_ids': 'trusteeUserIds',
            'start_date': 'startDate',
            'end_date': 'endDate',
            'query_phrase': 'queryPhrase',
            'facets': 'facets',
            'filters': 'filters'
        }

        self._trustee_organization_ids = None
        self._trustee_user_ids = None
        self._start_date = None
        self._end_date = None
        self._query_phrase = None
        self._facets = None
        self._filters = None

    @property
    def trustee_organization_ids(self) -> List[str]:
        """
        Gets the trustee_organization_ids of this TrusteeAuditQueryRequest.
        Limit returned audits to these trustee organizationIds.

        :return: The trustee_organization_ids of this TrusteeAuditQueryRequest.
        :rtype: list[str]
        """
        return self._trustee_organization_ids

    @trustee_organization_ids.setter
    def trustee_organization_ids(self, trustee_organization_ids: List[str]) -> None:
        """
        Sets the trustee_organization_ids of this TrusteeAuditQueryRequest.
        Limit returned audits to these trustee organizationIds.

        :param trustee_organization_ids: The trustee_organization_ids of this TrusteeAuditQueryRequest.
        :type: list[str]
        """
        

        self._trustee_organization_ids = trustee_organization_ids

    @property
    def trustee_user_ids(self) -> List[str]:
        """
        Gets the trustee_user_ids of this TrusteeAuditQueryRequest.
        Limit returned audits to these trustee userIds.

        :return: The trustee_user_ids of this TrusteeAuditQueryRequest.
        :rtype: list[str]
        """
        return self._trustee_user_ids

    @trustee_user_ids.setter
    def trustee_user_ids(self, trustee_user_ids: List[str]) -> None:
        """
        Sets the trustee_user_ids of this TrusteeAuditQueryRequest.
        Limit returned audits to these trustee userIds.

        :param trustee_user_ids: The trustee_user_ids of this TrusteeAuditQueryRequest.
        :type: list[str]
        """
        

        self._trustee_user_ids = trustee_user_ids

    @property
    def start_date(self) -> datetime:
        """
        Gets the start_date of this TrusteeAuditQueryRequest.
        Starting date/time for the audit search. ISO-8601 formatted date-time, UTC.

        :return: The start_date of this TrusteeAuditQueryRequest.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: datetime) -> None:
        """
        Sets the start_date of this TrusteeAuditQueryRequest.
        Starting date/time for the audit search. ISO-8601 formatted date-time, UTC.

        :param start_date: The start_date of this TrusteeAuditQueryRequest.
        :type: datetime
        """
        

        self._start_date = start_date

    @property
    def end_date(self) -> datetime:
        """
        Gets the end_date of this TrusteeAuditQueryRequest.
        Ending date/time for the audit search. ISO-8601 formatted date-time, UTC.

        :return: The end_date of this TrusteeAuditQueryRequest.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date: datetime) -> None:
        """
        Sets the end_date of this TrusteeAuditQueryRequest.
        Ending date/time for the audit search. ISO-8601 formatted date-time, UTC.

        :param end_date: The end_date of this TrusteeAuditQueryRequest.
        :type: datetime
        """
        

        self._end_date = end_date

    @property
    def query_phrase(self) -> str:
        """
        Gets the query_phrase of this TrusteeAuditQueryRequest.
        Word or phrase to look for in audit bodies.

        :return: The query_phrase of this TrusteeAuditQueryRequest.
        :rtype: str
        """
        return self._query_phrase

    @query_phrase.setter
    def query_phrase(self, query_phrase: str) -> None:
        """
        Sets the query_phrase of this TrusteeAuditQueryRequest.
        Word or phrase to look for in audit bodies.

        :param query_phrase: The query_phrase of this TrusteeAuditQueryRequest.
        :type: str
        """
        

        self._query_phrase = query_phrase

    @property
    def facets(self) -> List['Facet']:
        """
        Gets the facets of this TrusteeAuditQueryRequest.
        Facet information to be returned with the query results.

        :return: The facets of this TrusteeAuditQueryRequest.
        :rtype: list[Facet]
        """
        return self._facets

    @facets.setter
    def facets(self, facets: List['Facet']) -> None:
        """
        Sets the facets of this TrusteeAuditQueryRequest.
        Facet information to be returned with the query results.

        :param facets: The facets of this TrusteeAuditQueryRequest.
        :type: list[Facet]
        """
        

        self._facets = facets

    @property
    def filters(self) -> List['Filter']:
        """
        Gets the filters of this TrusteeAuditQueryRequest.
        Additional custom filters to be applied to the query.

        :return: The filters of this TrusteeAuditQueryRequest.
        :rtype: list[Filter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters: List['Filter']) -> None:
        """
        Sets the filters of this TrusteeAuditQueryRequest.
        Additional custom filters to be applied to the query.

        :param filters: The filters of this TrusteeAuditQueryRequest.
        :type: list[Filter]
        """
        

        self._filters = filters

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in self.swagger_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_json(self):
        """
        Returns the model as raw JSON
        """
        return json.dumps(sanitize_for_serialization(self.to_dict()))

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

