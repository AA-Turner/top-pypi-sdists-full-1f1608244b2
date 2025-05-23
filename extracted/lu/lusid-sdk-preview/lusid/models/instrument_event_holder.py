# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.257
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid.configuration import Configuration


class InstrumentEventHolder(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'instrument_event_id': 'str',
        'corporate_action_source_id': 'ResourceId',
        'instrument_identifiers': 'dict(str, str)',
        'lusid_instrument_id': 'str',
        'instrument_scope': 'str',
        'description': 'str',
        'event_date_range': 'EventDateRange',
        'completeness': 'str',
        'instrument_event': 'InstrumentEvent',
        'properties': 'list[PerpetualProperty]',
        'sequence_number': 'int',
        'participation_type': 'str'
    }

    attribute_map = {
        'instrument_event_id': 'instrumentEventId',
        'corporate_action_source_id': 'corporateActionSourceId',
        'instrument_identifiers': 'instrumentIdentifiers',
        'lusid_instrument_id': 'lusidInstrumentId',
        'instrument_scope': 'instrumentScope',
        'description': 'description',
        'event_date_range': 'eventDateRange',
        'completeness': 'completeness',
        'instrument_event': 'instrumentEvent',
        'properties': 'properties',
        'sequence_number': 'sequenceNumber',
        'participation_type': 'participationType'
    }

    required_map = {
        'instrument_event_id': 'required',
        'corporate_action_source_id': 'optional',
        'instrument_identifiers': 'required',
        'lusid_instrument_id': 'required',
        'instrument_scope': 'required',
        'description': 'required',
        'event_date_range': 'required',
        'completeness': 'optional',
        'instrument_event': 'required',
        'properties': 'optional',
        'sequence_number': 'optional',
        'participation_type': 'optional'
    }

    def __init__(self, instrument_event_id=None, corporate_action_source_id=None, instrument_identifiers=None, lusid_instrument_id=None, instrument_scope=None, description=None, event_date_range=None, completeness=None, instrument_event=None, properties=None, sequence_number=None, participation_type='Mandatory', local_vars_configuration=None):  # noqa: E501
        """InstrumentEventHolder - a model defined in OpenAPI"
        
        :param instrument_event_id:  The unique identifier of this corporate action. (required)
        :type instrument_event_id: str
        :param corporate_action_source_id: 
        :type corporate_action_source_id: lusid.ResourceId
        :param instrument_identifiers:  The set of identifiers which determine the instrument this event relates to. (required)
        :type instrument_identifiers: dict(str, str)
        :param lusid_instrument_id:  The LUID for the instrument. (required)
        :type lusid_instrument_id: str
        :param instrument_scope:  The scope of the instrument. (required)
        :type instrument_scope: str
        :param description:  The description of the instrument event. (required)
        :type description: str
        :param event_date_range:  (required)
        :type event_date_range: lusid.EventDateRange
        :param completeness:  Is the event Economically Complete, or is it missing some DataDependent fields (Incomplete).
        :type completeness: str
        :param instrument_event:  (required)
        :type instrument_event: lusid.InstrumentEvent
        :param properties:  The properties attached to this instrument event.
        :type properties: list[lusid.PerpetualProperty]
        :param sequence_number:  The order of the instrument event relative others on the same date (0 being processed first). Must be non negative.
        :type sequence_number: int
        :param participation_type:  Is participation in this event Mandatory, MandatoryWithChoices, or Voluntary.
        :type participation_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._instrument_event_id = None
        self._corporate_action_source_id = None
        self._instrument_identifiers = None
        self._lusid_instrument_id = None
        self._instrument_scope = None
        self._description = None
        self._event_date_range = None
        self._completeness = None
        self._instrument_event = None
        self._properties = None
        self._sequence_number = None
        self._participation_type = None
        self.discriminator = None

        self.instrument_event_id = instrument_event_id
        if corporate_action_source_id is not None:
            self.corporate_action_source_id = corporate_action_source_id
        self.instrument_identifiers = instrument_identifiers
        self.lusid_instrument_id = lusid_instrument_id
        self.instrument_scope = instrument_scope
        self.description = description
        self.event_date_range = event_date_range
        self.completeness = completeness
        self.instrument_event = instrument_event
        self.properties = properties
        if sequence_number is not None:
            self.sequence_number = sequence_number
        self.participation_type = participation_type

    @property
    def instrument_event_id(self):
        """Gets the instrument_event_id of this InstrumentEventHolder.  # noqa: E501

        The unique identifier of this corporate action.  # noqa: E501

        :return: The instrument_event_id of this InstrumentEventHolder.  # noqa: E501
        :rtype: str
        """
        return self._instrument_event_id

    @instrument_event_id.setter
    def instrument_event_id(self, instrument_event_id):
        """Sets the instrument_event_id of this InstrumentEventHolder.

        The unique identifier of this corporate action.  # noqa: E501

        :param instrument_event_id: The instrument_event_id of this InstrumentEventHolder.  # noqa: E501
        :type instrument_event_id: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_event_id is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_event_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_event_id is not None and len(instrument_event_id) > 64):
            raise ValueError("Invalid value for `instrument_event_id`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_event_id is not None and len(instrument_event_id) < 1):
            raise ValueError("Invalid value for `instrument_event_id`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_event_id is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', instrument_event_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `instrument_event_id`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._instrument_event_id = instrument_event_id

    @property
    def corporate_action_source_id(self):
        """Gets the corporate_action_source_id of this InstrumentEventHolder.  # noqa: E501


        :return: The corporate_action_source_id of this InstrumentEventHolder.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._corporate_action_source_id

    @corporate_action_source_id.setter
    def corporate_action_source_id(self, corporate_action_source_id):
        """Sets the corporate_action_source_id of this InstrumentEventHolder.


        :param corporate_action_source_id: The corporate_action_source_id of this InstrumentEventHolder.  # noqa: E501
        :type corporate_action_source_id: lusid.ResourceId
        """

        self._corporate_action_source_id = corporate_action_source_id

    @property
    def instrument_identifiers(self):
        """Gets the instrument_identifiers of this InstrumentEventHolder.  # noqa: E501

        The set of identifiers which determine the instrument this event relates to.  # noqa: E501

        :return: The instrument_identifiers of this InstrumentEventHolder.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._instrument_identifiers

    @instrument_identifiers.setter
    def instrument_identifiers(self, instrument_identifiers):
        """Sets the instrument_identifiers of this InstrumentEventHolder.

        The set of identifiers which determine the instrument this event relates to.  # noqa: E501

        :param instrument_identifiers: The instrument_identifiers of this InstrumentEventHolder.  # noqa: E501
        :type instrument_identifiers: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and instrument_identifiers is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_identifiers`, must not be `None`")  # noqa: E501

        self._instrument_identifiers = instrument_identifiers

    @property
    def lusid_instrument_id(self):
        """Gets the lusid_instrument_id of this InstrumentEventHolder.  # noqa: E501

        The LUID for the instrument.  # noqa: E501

        :return: The lusid_instrument_id of this InstrumentEventHolder.  # noqa: E501
        :rtype: str
        """
        return self._lusid_instrument_id

    @lusid_instrument_id.setter
    def lusid_instrument_id(self, lusid_instrument_id):
        """Sets the lusid_instrument_id of this InstrumentEventHolder.

        The LUID for the instrument.  # noqa: E501

        :param lusid_instrument_id: The lusid_instrument_id of this InstrumentEventHolder.  # noqa: E501
        :type lusid_instrument_id: str
        """
        if self.local_vars_configuration.client_side_validation and lusid_instrument_id is None:  # noqa: E501
            raise ValueError("Invalid value for `lusid_instrument_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                lusid_instrument_id is not None and len(lusid_instrument_id) < 1):
            raise ValueError("Invalid value for `lusid_instrument_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._lusid_instrument_id = lusid_instrument_id

    @property
    def instrument_scope(self):
        """Gets the instrument_scope of this InstrumentEventHolder.  # noqa: E501

        The scope of the instrument.  # noqa: E501

        :return: The instrument_scope of this InstrumentEventHolder.  # noqa: E501
        :rtype: str
        """
        return self._instrument_scope

    @instrument_scope.setter
    def instrument_scope(self, instrument_scope):
        """Sets the instrument_scope of this InstrumentEventHolder.

        The scope of the instrument.  # noqa: E501

        :param instrument_scope: The instrument_scope of this InstrumentEventHolder.  # noqa: E501
        :type instrument_scope: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_scope is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_scope`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_scope is not None and len(instrument_scope) < 1):
            raise ValueError("Invalid value for `instrument_scope`, length must be greater than or equal to `1`")  # noqa: E501

        self._instrument_scope = instrument_scope

    @property
    def description(self):
        """Gets the description of this InstrumentEventHolder.  # noqa: E501

        The description of the instrument event.  # noqa: E501

        :return: The description of this InstrumentEventHolder.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InstrumentEventHolder.

        The description of the instrument event.  # noqa: E501

        :param description: The description of this InstrumentEventHolder.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 1024):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and not re.search(r'^[\s\S]*$', description)):  # noqa: E501
            raise ValueError(r"Invalid value for `description`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._description = description

    @property
    def event_date_range(self):
        """Gets the event_date_range of this InstrumentEventHolder.  # noqa: E501


        :return: The event_date_range of this InstrumentEventHolder.  # noqa: E501
        :rtype: lusid.EventDateRange
        """
        return self._event_date_range

    @event_date_range.setter
    def event_date_range(self, event_date_range):
        """Sets the event_date_range of this InstrumentEventHolder.


        :param event_date_range: The event_date_range of this InstrumentEventHolder.  # noqa: E501
        :type event_date_range: lusid.EventDateRange
        """
        if self.local_vars_configuration.client_side_validation and event_date_range is None:  # noqa: E501
            raise ValueError("Invalid value for `event_date_range`, must not be `None`")  # noqa: E501

        self._event_date_range = event_date_range

    @property
    def completeness(self):
        """Gets the completeness of this InstrumentEventHolder.  # noqa: E501

        Is the event Economically Complete, or is it missing some DataDependent fields (Incomplete).  # noqa: E501

        :return: The completeness of this InstrumentEventHolder.  # noqa: E501
        :rtype: str
        """
        return self._completeness

    @completeness.setter
    def completeness(self, completeness):
        """Sets the completeness of this InstrumentEventHolder.

        Is the event Economically Complete, or is it missing some DataDependent fields (Incomplete).  # noqa: E501

        :param completeness: The completeness of this InstrumentEventHolder.  # noqa: E501
        :type completeness: str
        """

        self._completeness = completeness

    @property
    def instrument_event(self):
        """Gets the instrument_event of this InstrumentEventHolder.  # noqa: E501


        :return: The instrument_event of this InstrumentEventHolder.  # noqa: E501
        :rtype: lusid.InstrumentEvent
        """
        return self._instrument_event

    @instrument_event.setter
    def instrument_event(self, instrument_event):
        """Sets the instrument_event of this InstrumentEventHolder.


        :param instrument_event: The instrument_event of this InstrumentEventHolder.  # noqa: E501
        :type instrument_event: lusid.InstrumentEvent
        """
        if self.local_vars_configuration.client_side_validation and instrument_event is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_event`, must not be `None`")  # noqa: E501

        self._instrument_event = instrument_event

    @property
    def properties(self):
        """Gets the properties of this InstrumentEventHolder.  # noqa: E501

        The properties attached to this instrument event.  # noqa: E501

        :return: The properties of this InstrumentEventHolder.  # noqa: E501
        :rtype: list[lusid.PerpetualProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this InstrumentEventHolder.

        The properties attached to this instrument event.  # noqa: E501

        :param properties: The properties of this InstrumentEventHolder.  # noqa: E501
        :type properties: list[lusid.PerpetualProperty]
        """

        self._properties = properties

    @property
    def sequence_number(self):
        """Gets the sequence_number of this InstrumentEventHolder.  # noqa: E501

        The order of the instrument event relative others on the same date (0 being processed first). Must be non negative.  # noqa: E501

        :return: The sequence_number of this InstrumentEventHolder.  # noqa: E501
        :rtype: int
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        """Sets the sequence_number of this InstrumentEventHolder.

        The order of the instrument event relative others on the same date (0 being processed first). Must be non negative.  # noqa: E501

        :param sequence_number: The sequence_number of this InstrumentEventHolder.  # noqa: E501
        :type sequence_number: int
        """

        self._sequence_number = sequence_number

    @property
    def participation_type(self):
        """Gets the participation_type of this InstrumentEventHolder.  # noqa: E501

        Is participation in this event Mandatory, MandatoryWithChoices, or Voluntary.  # noqa: E501

        :return: The participation_type of this InstrumentEventHolder.  # noqa: E501
        :rtype: str
        """
        return self._participation_type

    @participation_type.setter
    def participation_type(self, participation_type):
        """Sets the participation_type of this InstrumentEventHolder.

        Is participation in this event Mandatory, MandatoryWithChoices, or Voluntary.  # noqa: E501

        :param participation_type: The participation_type of this InstrumentEventHolder.  # noqa: E501
        :type participation_type: str
        """

        self._participation_type = participation_type

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InstrumentEventHolder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstrumentEventHolder):
            return True

        return self.to_dict() != other.to_dict()
