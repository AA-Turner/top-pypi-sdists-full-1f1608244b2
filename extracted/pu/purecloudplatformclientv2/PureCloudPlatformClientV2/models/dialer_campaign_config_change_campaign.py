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
    from . import DialerCampaignConfigChangeContactSort
    from . import DialerCampaignConfigChangePhoneColumn
    from . import DialerCampaignConfigChangeRestErrorDetail
    from . import DialerCampaignConfigChangeUriReference

class DialerCampaignConfigChangeCampaign(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        DialerCampaignConfigChangeCampaign - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'contact_list': 'DialerCampaignConfigChangeUriReference',
            'queue': 'DialerCampaignConfigChangeUriReference',
            'dialing_mode': 'str',
            'script': 'DialerCampaignConfigChangeUriReference',
            'edge_group': 'DialerCampaignConfigChangeUriReference',
            'site': 'DialerCampaignConfigChangeUriReference',
            'campaign_status': 'str',
            'phone_columns': 'list[DialerCampaignConfigChangePhoneColumn]',
            'abandon_rate': 'float',
            'dnc_lists': 'list[DialerCampaignConfigChangeUriReference]',
            'callable_time_set': 'DialerCampaignConfigChangeUriReference',
            'call_analysis_response_set': 'DialerCampaignConfigChangeUriReference',
            'caller_name': 'str',
            'caller_address': 'str',
            'outbound_line_count': 'int',
            'errors': 'list[DialerCampaignConfigChangeRestErrorDetail]',
            'rule_sets': 'list[DialerCampaignConfigChangeUriReference]',
            'skip_preview_disabled': 'bool',
            'preview_time_out_seconds': 'int',
            'single_number_preview': 'bool',
            'contact_sort': 'DialerCampaignConfigChangeContactSort',
            'contact_sorts': 'list[DialerCampaignConfigChangeContactSort]',
            'no_answer_timeout': 'int',
            'call_analysis_language': 'str',
            'priority': 'int',
            'contact_list_filters': 'list[DialerCampaignConfigChangeUriReference]',
            'division': 'DialerCampaignConfigChangeUriReference',
            'agent_owned_column': 'str',
            'additional_properties': 'dict(str, object)',
            'id': 'str',
            'name': 'str',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'version': 'int'
        }

        self.attribute_map = {
            'contact_list': 'contactList',
            'queue': 'queue',
            'dialing_mode': 'dialingMode',
            'script': 'script',
            'edge_group': 'edgeGroup',
            'site': 'site',
            'campaign_status': 'campaignStatus',
            'phone_columns': 'phoneColumns',
            'abandon_rate': 'abandonRate',
            'dnc_lists': 'dncLists',
            'callable_time_set': 'callableTimeSet',
            'call_analysis_response_set': 'callAnalysisResponseSet',
            'caller_name': 'callerName',
            'caller_address': 'callerAddress',
            'outbound_line_count': 'outboundLineCount',
            'errors': 'errors',
            'rule_sets': 'ruleSets',
            'skip_preview_disabled': 'skipPreviewDisabled',
            'preview_time_out_seconds': 'previewTimeOutSeconds',
            'single_number_preview': 'singleNumberPreview',
            'contact_sort': 'contactSort',
            'contact_sorts': 'contactSorts',
            'no_answer_timeout': 'noAnswerTimeout',
            'call_analysis_language': 'callAnalysisLanguage',
            'priority': 'priority',
            'contact_list_filters': 'contactListFilters',
            'division': 'division',
            'agent_owned_column': 'agentOwnedColumn',
            'additional_properties': 'additionalProperties',
            'id': 'id',
            'name': 'name',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'version': 'version'
        }

        self._contact_list = None
        self._queue = None
        self._dialing_mode = None
        self._script = None
        self._edge_group = None
        self._site = None
        self._campaign_status = None
        self._phone_columns = None
        self._abandon_rate = None
        self._dnc_lists = None
        self._callable_time_set = None
        self._call_analysis_response_set = None
        self._caller_name = None
        self._caller_address = None
        self._outbound_line_count = None
        self._errors = None
        self._rule_sets = None
        self._skip_preview_disabled = None
        self._preview_time_out_seconds = None
        self._single_number_preview = None
        self._contact_sort = None
        self._contact_sorts = None
        self._no_answer_timeout = None
        self._call_analysis_language = None
        self._priority = None
        self._contact_list_filters = None
        self._division = None
        self._agent_owned_column = None
        self._additional_properties = None
        self._id = None
        self._name = None
        self._date_created = None
        self._date_modified = None
        self._version = None

    @property
    def contact_list(self) -> 'DialerCampaignConfigChangeUriReference':
        """
        Gets the contact_list of this DialerCampaignConfigChangeCampaign.


        :return: The contact_list of this DialerCampaignConfigChangeCampaign.
        :rtype: DialerCampaignConfigChangeUriReference
        """
        return self._contact_list

    @contact_list.setter
    def contact_list(self, contact_list: 'DialerCampaignConfigChangeUriReference') -> None:
        """
        Sets the contact_list of this DialerCampaignConfigChangeCampaign.


        :param contact_list: The contact_list of this DialerCampaignConfigChangeCampaign.
        :type: DialerCampaignConfigChangeUriReference
        """
        

        self._contact_list = contact_list

    @property
    def queue(self) -> 'DialerCampaignConfigChangeUriReference':
        """
        Gets the queue of this DialerCampaignConfigChangeCampaign.
        A UriReference for a resource

        :return: The queue of this DialerCampaignConfigChangeCampaign.
        :rtype: DialerCampaignConfigChangeUriReference
        """
        return self._queue

    @queue.setter
    def queue(self, queue: 'DialerCampaignConfigChangeUriReference') -> None:
        """
        Sets the queue of this DialerCampaignConfigChangeCampaign.
        A UriReference for a resource

        :param queue: The queue of this DialerCampaignConfigChangeCampaign.
        :type: DialerCampaignConfigChangeUriReference
        """
        

        self._queue = queue

    @property
    def dialing_mode(self) -> str:
        """
        Gets the dialing_mode of this DialerCampaignConfigChangeCampaign.
        dialing mode of the campaign

        :return: The dialing_mode of this DialerCampaignConfigChangeCampaign.
        :rtype: str
        """
        return self._dialing_mode

    @dialing_mode.setter
    def dialing_mode(self, dialing_mode: str) -> None:
        """
        Sets the dialing_mode of this DialerCampaignConfigChangeCampaign.
        dialing mode of the campaign

        :param dialing_mode: The dialing_mode of this DialerCampaignConfigChangeCampaign.
        :type: str
        """
        if isinstance(dialing_mode, int):
            dialing_mode = str(dialing_mode)
        allowed_values = ["agentless", "external", "preview", "power", "predictive", "progressive"]
        if dialing_mode.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for dialing_mode -> " + dialing_mode)
            self._dialing_mode = "outdated_sdk_version"
        else:
            self._dialing_mode = dialing_mode

    @property
    def script(self) -> 'DialerCampaignConfigChangeUriReference':
        """
        Gets the script of this DialerCampaignConfigChangeCampaign.
        A UriReference for a resource

        :return: The script of this DialerCampaignConfigChangeCampaign.
        :rtype: DialerCampaignConfigChangeUriReference
        """
        return self._script

    @script.setter
    def script(self, script: 'DialerCampaignConfigChangeUriReference') -> None:
        """
        Sets the script of this DialerCampaignConfigChangeCampaign.
        A UriReference for a resource

        :param script: The script of this DialerCampaignConfigChangeCampaign.
        :type: DialerCampaignConfigChangeUriReference
        """
        

        self._script = script

    @property
    def edge_group(self) -> 'DialerCampaignConfigChangeUriReference':
        """
        Gets the edge_group of this DialerCampaignConfigChangeCampaign.
        A UriReference for a resource

        :return: The edge_group of this DialerCampaignConfigChangeCampaign.
        :rtype: DialerCampaignConfigChangeUriReference
        """
        return self._edge_group

    @edge_group.setter
    def edge_group(self, edge_group: 'DialerCampaignConfigChangeUriReference') -> None:
        """
        Sets the edge_group of this DialerCampaignConfigChangeCampaign.
        A UriReference for a resource

        :param edge_group: The edge_group of this DialerCampaignConfigChangeCampaign.
        :type: DialerCampaignConfigChangeUriReference
        """
        

        self._edge_group = edge_group

    @property
    def site(self) -> 'DialerCampaignConfigChangeUriReference':
        """
        Gets the site of this DialerCampaignConfigChangeCampaign.
        A UriReference for a resource

        :return: The site of this DialerCampaignConfigChangeCampaign.
        :rtype: DialerCampaignConfigChangeUriReference
        """
        return self._site

    @site.setter
    def site(self, site: 'DialerCampaignConfigChangeUriReference') -> None:
        """
        Sets the site of this DialerCampaignConfigChangeCampaign.
        A UriReference for a resource

        :param site: The site of this DialerCampaignConfigChangeCampaign.
        :type: DialerCampaignConfigChangeUriReference
        """
        

        self._site = site

    @property
    def campaign_status(self) -> str:
        """
        Gets the campaign_status of this DialerCampaignConfigChangeCampaign.


        :return: The campaign_status of this DialerCampaignConfigChangeCampaign.
        :rtype: str
        """
        return self._campaign_status

    @campaign_status.setter
    def campaign_status(self, campaign_status: str) -> None:
        """
        Sets the campaign_status of this DialerCampaignConfigChangeCampaign.


        :param campaign_status: The campaign_status of this DialerCampaignConfigChangeCampaign.
        :type: str
        """
        if isinstance(campaign_status, int):
            campaign_status = str(campaign_status)
        allowed_values = ["on", "off", "complete", "stopping", "invalid"]
        if campaign_status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for campaign_status -> " + campaign_status)
            self._campaign_status = "outdated_sdk_version"
        else:
            self._campaign_status = campaign_status

    @property
    def phone_columns(self) -> List['DialerCampaignConfigChangePhoneColumn']:
        """
        Gets the phone_columns of this DialerCampaignConfigChangeCampaign.
        the contact list phone columns to be called for the campaign

        :return: The phone_columns of this DialerCampaignConfigChangeCampaign.
        :rtype: list[DialerCampaignConfigChangePhoneColumn]
        """
        return self._phone_columns

    @phone_columns.setter
    def phone_columns(self, phone_columns: List['DialerCampaignConfigChangePhoneColumn']) -> None:
        """
        Sets the phone_columns of this DialerCampaignConfigChangeCampaign.
        the contact list phone columns to be called for the campaign

        :param phone_columns: The phone_columns of this DialerCampaignConfigChangeCampaign.
        :type: list[DialerCampaignConfigChangePhoneColumn]
        """
        

        self._phone_columns = phone_columns

    @property
    def abandon_rate(self) -> float:
        """
        Gets the abandon_rate of this DialerCampaignConfigChangeCampaign.
        the targeted abandon rate percentage

        :return: The abandon_rate of this DialerCampaignConfigChangeCampaign.
        :rtype: float
        """
        return self._abandon_rate

    @abandon_rate.setter
    def abandon_rate(self, abandon_rate: float) -> None:
        """
        Sets the abandon_rate of this DialerCampaignConfigChangeCampaign.
        the targeted abandon rate percentage

        :param abandon_rate: The abandon_rate of this DialerCampaignConfigChangeCampaign.
        :type: float
        """
        

        self._abandon_rate = abandon_rate

    @property
    def dnc_lists(self) -> List['DialerCampaignConfigChangeUriReference']:
        """
        Gets the dnc_lists of this DialerCampaignConfigChangeCampaign.
        identifiers of the do not call lists

        :return: The dnc_lists of this DialerCampaignConfigChangeCampaign.
        :rtype: list[DialerCampaignConfigChangeUriReference]
        """
        return self._dnc_lists

    @dnc_lists.setter
    def dnc_lists(self, dnc_lists: List['DialerCampaignConfigChangeUriReference']) -> None:
        """
        Sets the dnc_lists of this DialerCampaignConfigChangeCampaign.
        identifiers of the do not call lists

        :param dnc_lists: The dnc_lists of this DialerCampaignConfigChangeCampaign.
        :type: list[DialerCampaignConfigChangeUriReference]
        """
        

        self._dnc_lists = dnc_lists

    @property
    def callable_time_set(self) -> 'DialerCampaignConfigChangeUriReference':
        """
        Gets the callable_time_set of this DialerCampaignConfigChangeCampaign.
        A UriReference for a resource

        :return: The callable_time_set of this DialerCampaignConfigChangeCampaign.
        :rtype: DialerCampaignConfigChangeUriReference
        """
        return self._callable_time_set

    @callable_time_set.setter
    def callable_time_set(self, callable_time_set: 'DialerCampaignConfigChangeUriReference') -> None:
        """
        Sets the callable_time_set of this DialerCampaignConfigChangeCampaign.
        A UriReference for a resource

        :param callable_time_set: The callable_time_set of this DialerCampaignConfigChangeCampaign.
        :type: DialerCampaignConfigChangeUriReference
        """
        

        self._callable_time_set = callable_time_set

    @property
    def call_analysis_response_set(self) -> 'DialerCampaignConfigChangeUriReference':
        """
        Gets the call_analysis_response_set of this DialerCampaignConfigChangeCampaign.
        A UriReference for a resource

        :return: The call_analysis_response_set of this DialerCampaignConfigChangeCampaign.
        :rtype: DialerCampaignConfigChangeUriReference
        """
        return self._call_analysis_response_set

    @call_analysis_response_set.setter
    def call_analysis_response_set(self, call_analysis_response_set: 'DialerCampaignConfigChangeUriReference') -> None:
        """
        Sets the call_analysis_response_set of this DialerCampaignConfigChangeCampaign.
        A UriReference for a resource

        :param call_analysis_response_set: The call_analysis_response_set of this DialerCampaignConfigChangeCampaign.
        :type: DialerCampaignConfigChangeUriReference
        """
        

        self._call_analysis_response_set = call_analysis_response_set

    @property
    def caller_name(self) -> str:
        """
        Gets the caller_name of this DialerCampaignConfigChangeCampaign.
        caller id name to be displayed on the outbound call

        :return: The caller_name of this DialerCampaignConfigChangeCampaign.
        :rtype: str
        """
        return self._caller_name

    @caller_name.setter
    def caller_name(self, caller_name: str) -> None:
        """
        Sets the caller_name of this DialerCampaignConfigChangeCampaign.
        caller id name to be displayed on the outbound call

        :param caller_name: The caller_name of this DialerCampaignConfigChangeCampaign.
        :type: str
        """
        

        self._caller_name = caller_name

    @property
    def caller_address(self) -> str:
        """
        Gets the caller_address of this DialerCampaignConfigChangeCampaign.
        caller id phone number to be displayed on the outbound call

        :return: The caller_address of this DialerCampaignConfigChangeCampaign.
        :rtype: str
        """
        return self._caller_address

    @caller_address.setter
    def caller_address(self, caller_address: str) -> None:
        """
        Sets the caller_address of this DialerCampaignConfigChangeCampaign.
        caller id phone number to be displayed on the outbound call

        :param caller_address: The caller_address of this DialerCampaignConfigChangeCampaign.
        :type: str
        """
        

        self._caller_address = caller_address

    @property
    def outbound_line_count(self) -> int:
        """
        Gets the outbound_line_count of this DialerCampaignConfigChangeCampaign.
        for agentless campaigns, the number of outbound lines to be concurrently dialed

        :return: The outbound_line_count of this DialerCampaignConfigChangeCampaign.
        :rtype: int
        """
        return self._outbound_line_count

    @outbound_line_count.setter
    def outbound_line_count(self, outbound_line_count: int) -> None:
        """
        Sets the outbound_line_count of this DialerCampaignConfigChangeCampaign.
        for agentless campaigns, the number of outbound lines to be concurrently dialed

        :param outbound_line_count: The outbound_line_count of this DialerCampaignConfigChangeCampaign.
        :type: int
        """
        

        self._outbound_line_count = outbound_line_count

    @property
    def errors(self) -> List['DialerCampaignConfigChangeRestErrorDetail']:
        """
        Gets the errors of this DialerCampaignConfigChangeCampaign.
        a list of current error conditions associated with the campaign

        :return: The errors of this DialerCampaignConfigChangeCampaign.
        :rtype: list[DialerCampaignConfigChangeRestErrorDetail]
        """
        return self._errors

    @errors.setter
    def errors(self, errors: List['DialerCampaignConfigChangeRestErrorDetail']) -> None:
        """
        Sets the errors of this DialerCampaignConfigChangeCampaign.
        a list of current error conditions associated with the campaign

        :param errors: The errors of this DialerCampaignConfigChangeCampaign.
        :type: list[DialerCampaignConfigChangeRestErrorDetail]
        """
        

        self._errors = errors

    @property
    def rule_sets(self) -> List['DialerCampaignConfigChangeUriReference']:
        """
        Gets the rule_sets of this DialerCampaignConfigChangeCampaign.
        identifiers of the rule sets

        :return: The rule_sets of this DialerCampaignConfigChangeCampaign.
        :rtype: list[DialerCampaignConfigChangeUriReference]
        """
        return self._rule_sets

    @rule_sets.setter
    def rule_sets(self, rule_sets: List['DialerCampaignConfigChangeUriReference']) -> None:
        """
        Sets the rule_sets of this DialerCampaignConfigChangeCampaign.
        identifiers of the rule sets

        :param rule_sets: The rule_sets of this DialerCampaignConfigChangeCampaign.
        :type: list[DialerCampaignConfigChangeUriReference]
        """
        

        self._rule_sets = rule_sets

    @property
    def skip_preview_disabled(self) -> bool:
        """
        Gets the skip_preview_disabled of this DialerCampaignConfigChangeCampaign.
        for preview campaigns, indicator of whether the agent can skip a preview without placing a call

        :return: The skip_preview_disabled of this DialerCampaignConfigChangeCampaign.
        :rtype: bool
        """
        return self._skip_preview_disabled

    @skip_preview_disabled.setter
    def skip_preview_disabled(self, skip_preview_disabled: bool) -> None:
        """
        Sets the skip_preview_disabled of this DialerCampaignConfigChangeCampaign.
        for preview campaigns, indicator of whether the agent can skip a preview without placing a call

        :param skip_preview_disabled: The skip_preview_disabled of this DialerCampaignConfigChangeCampaign.
        :type: bool
        """
        

        self._skip_preview_disabled = skip_preview_disabled

    @property
    def preview_time_out_seconds(self) -> int:
        """
        Gets the preview_time_out_seconds of this DialerCampaignConfigChangeCampaign.
        for preview campaigns, number of seconds before a call will be automatically placed. A value of 0 indicates no automatic placement of calls

        :return: The preview_time_out_seconds of this DialerCampaignConfigChangeCampaign.
        :rtype: int
        """
        return self._preview_time_out_seconds

    @preview_time_out_seconds.setter
    def preview_time_out_seconds(self, preview_time_out_seconds: int) -> None:
        """
        Sets the preview_time_out_seconds of this DialerCampaignConfigChangeCampaign.
        for preview campaigns, number of seconds before a call will be automatically placed. A value of 0 indicates no automatic placement of calls

        :param preview_time_out_seconds: The preview_time_out_seconds of this DialerCampaignConfigChangeCampaign.
        :type: int
        """
        

        self._preview_time_out_seconds = preview_time_out_seconds

    @property
    def single_number_preview(self) -> bool:
        """
        Gets the single_number_preview of this DialerCampaignConfigChangeCampaign.
        for preview campaigns with multiple phone columns, indicator if one (true) or multiple (false) phone numbers will be available to call for each preview

        :return: The single_number_preview of this DialerCampaignConfigChangeCampaign.
        :rtype: bool
        """
        return self._single_number_preview

    @single_number_preview.setter
    def single_number_preview(self, single_number_preview: bool) -> None:
        """
        Sets the single_number_preview of this DialerCampaignConfigChangeCampaign.
        for preview campaigns with multiple phone columns, indicator if one (true) or multiple (false) phone numbers will be available to call for each preview

        :param single_number_preview: The single_number_preview of this DialerCampaignConfigChangeCampaign.
        :type: bool
        """
        

        self._single_number_preview = single_number_preview

    @property
    def contact_sort(self) -> 'DialerCampaignConfigChangeContactSort':
        """
        Gets the contact_sort of this DialerCampaignConfigChangeCampaign.


        :return: The contact_sort of this DialerCampaignConfigChangeCampaign.
        :rtype: DialerCampaignConfigChangeContactSort
        """
        return self._contact_sort

    @contact_sort.setter
    def contact_sort(self, contact_sort: 'DialerCampaignConfigChangeContactSort') -> None:
        """
        Sets the contact_sort of this DialerCampaignConfigChangeCampaign.


        :param contact_sort: The contact_sort of this DialerCampaignConfigChangeCampaign.
        :type: DialerCampaignConfigChangeContactSort
        """
        

        self._contact_sort = contact_sort

    @property
    def contact_sorts(self) -> List['DialerCampaignConfigChangeContactSort']:
        """
        Gets the contact_sorts of this DialerCampaignConfigChangeCampaign.
        List of contact sort objects.

        :return: The contact_sorts of this DialerCampaignConfigChangeCampaign.
        :rtype: list[DialerCampaignConfigChangeContactSort]
        """
        return self._contact_sorts

    @contact_sorts.setter
    def contact_sorts(self, contact_sorts: List['DialerCampaignConfigChangeContactSort']) -> None:
        """
        Sets the contact_sorts of this DialerCampaignConfigChangeCampaign.
        List of contact sort objects.

        :param contact_sorts: The contact_sorts of this DialerCampaignConfigChangeCampaign.
        :type: list[DialerCampaignConfigChangeContactSort]
        """
        

        self._contact_sorts = contact_sorts

    @property
    def no_answer_timeout(self) -> int:
        """
        Gets the no_answer_timeout of this DialerCampaignConfigChangeCampaign.
        for non-preview campaigns, how long to wait before dispositioning as 'no-answer', default 30 seconds

        :return: The no_answer_timeout of this DialerCampaignConfigChangeCampaign.
        :rtype: int
        """
        return self._no_answer_timeout

    @no_answer_timeout.setter
    def no_answer_timeout(self, no_answer_timeout: int) -> None:
        """
        Sets the no_answer_timeout of this DialerCampaignConfigChangeCampaign.
        for non-preview campaigns, how long to wait before dispositioning as 'no-answer', default 30 seconds

        :param no_answer_timeout: The no_answer_timeout of this DialerCampaignConfigChangeCampaign.
        :type: int
        """
        

        self._no_answer_timeout = no_answer_timeout

    @property
    def call_analysis_language(self) -> str:
        """
        Gets the call_analysis_language of this DialerCampaignConfigChangeCampaign.
        The language the edge will use to analyze the call

        :return: The call_analysis_language of this DialerCampaignConfigChangeCampaign.
        :rtype: str
        """
        return self._call_analysis_language

    @call_analysis_language.setter
    def call_analysis_language(self, call_analysis_language: str) -> None:
        """
        Sets the call_analysis_language of this DialerCampaignConfigChangeCampaign.
        The language the edge will use to analyze the call

        :param call_analysis_language: The call_analysis_language of this DialerCampaignConfigChangeCampaign.
        :type: str
        """
        

        self._call_analysis_language = call_analysis_language

    @property
    def priority(self) -> int:
        """
        Gets the priority of this DialerCampaignConfigChangeCampaign.
        The priority of this campaign relative to other campaigns

        :return: The priority of this DialerCampaignConfigChangeCampaign.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority: int) -> None:
        """
        Sets the priority of this DialerCampaignConfigChangeCampaign.
        The priority of this campaign relative to other campaigns

        :param priority: The priority of this DialerCampaignConfigChangeCampaign.
        :type: int
        """
        

        self._priority = priority

    @property
    def contact_list_filters(self) -> List['DialerCampaignConfigChangeUriReference']:
        """
        Gets the contact_list_filters of this DialerCampaignConfigChangeCampaign.
        List of contact filters

        :return: The contact_list_filters of this DialerCampaignConfigChangeCampaign.
        :rtype: list[DialerCampaignConfigChangeUriReference]
        """
        return self._contact_list_filters

    @contact_list_filters.setter
    def contact_list_filters(self, contact_list_filters: List['DialerCampaignConfigChangeUriReference']) -> None:
        """
        Sets the contact_list_filters of this DialerCampaignConfigChangeCampaign.
        List of contact filters

        :param contact_list_filters: The contact_list_filters of this DialerCampaignConfigChangeCampaign.
        :type: list[DialerCampaignConfigChangeUriReference]
        """
        

        self._contact_list_filters = contact_list_filters

    @property
    def division(self) -> 'DialerCampaignConfigChangeUriReference':
        """
        Gets the division of this DialerCampaignConfigChangeCampaign.
        A UriReference for a resource

        :return: The division of this DialerCampaignConfigChangeCampaign.
        :rtype: DialerCampaignConfigChangeUriReference
        """
        return self._division

    @division.setter
    def division(self, division: 'DialerCampaignConfigChangeUriReference') -> None:
        """
        Sets the division of this DialerCampaignConfigChangeCampaign.
        A UriReference for a resource

        :param division: The division of this DialerCampaignConfigChangeCampaign.
        :type: DialerCampaignConfigChangeUriReference
        """
        

        self._division = division

    @property
    def agent_owned_column(self) -> str:
        """
        Gets the agent_owned_column of this DialerCampaignConfigChangeCampaign.
        For Preview Campaigns. Name of the contact column in the contact list containing the userIds of agents to assign specific contact records to.

        :return: The agent_owned_column of this DialerCampaignConfigChangeCampaign.
        :rtype: str
        """
        return self._agent_owned_column

    @agent_owned_column.setter
    def agent_owned_column(self, agent_owned_column: str) -> None:
        """
        Sets the agent_owned_column of this DialerCampaignConfigChangeCampaign.
        For Preview Campaigns. Name of the contact column in the contact list containing the userIds of agents to assign specific contact records to.

        :param agent_owned_column: The agent_owned_column of this DialerCampaignConfigChangeCampaign.
        :type: str
        """
        

        self._agent_owned_column = agent_owned_column

    @property
    def additional_properties(self) -> Dict[str, object]:
        """
        Gets the additional_properties of this DialerCampaignConfigChangeCampaign.


        :return: The additional_properties of this DialerCampaignConfigChangeCampaign.
        :rtype: dict(str, object)
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties: Dict[str, object]) -> None:
        """
        Sets the additional_properties of this DialerCampaignConfigChangeCampaign.


        :param additional_properties: The additional_properties of this DialerCampaignConfigChangeCampaign.
        :type: dict(str, object)
        """
        

        self._additional_properties = additional_properties

    @property
    def id(self) -> str:
        """
        Gets the id of this DialerCampaignConfigChangeCampaign.
        The globally unique identifier for the object.

        :return: The id of this DialerCampaignConfigChangeCampaign.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this DialerCampaignConfigChangeCampaign.
        The globally unique identifier for the object.

        :param id: The id of this DialerCampaignConfigChangeCampaign.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this DialerCampaignConfigChangeCampaign.
        The UI-visible name of the object

        :return: The name of this DialerCampaignConfigChangeCampaign.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this DialerCampaignConfigChangeCampaign.
        The UI-visible name of the object

        :param name: The name of this DialerCampaignConfigChangeCampaign.
        :type: str
        """
        

        self._name = name

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this DialerCampaignConfigChangeCampaign.
        Creation time of the entity

        :return: The date_created of this DialerCampaignConfigChangeCampaign.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this DialerCampaignConfigChangeCampaign.
        Creation time of the entity

        :param date_created: The date_created of this DialerCampaignConfigChangeCampaign.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this DialerCampaignConfigChangeCampaign.
        Last modified time of the entity

        :return: The date_modified of this DialerCampaignConfigChangeCampaign.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this DialerCampaignConfigChangeCampaign.
        Last modified time of the entity

        :param date_modified: The date_modified of this DialerCampaignConfigChangeCampaign.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def version(self) -> int:
        """
        Gets the version of this DialerCampaignConfigChangeCampaign.
        Required for updates, must match the version number of the most recent update

        :return: The version of this DialerCampaignConfigChangeCampaign.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version: int) -> None:
        """
        Sets the version of this DialerCampaignConfigChangeCampaign.
        Required for updates, must match the version number of the most recent update

        :param version: The version of this DialerCampaignConfigChangeCampaign.
        :type: int
        """
        

        self._version = version

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

