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


class WeightedInstrumentInLineLookupIdentifiers(object):
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
        'lusid_instrument_id': 'str',
        'isin': 'str',
        'sedol': 'str',
        'cusip': 'str',
        'client_internal': 'str',
        'figi': 'str',
        'ric': 'str',
        'quote_perm_id': 'str',
        'red_code': 'str',
        'bbgid': 'str',
        'ice_code': 'str'
    }

    attribute_map = {
        'lusid_instrument_id': 'LusidInstrumentId',
        'isin': 'Isin',
        'sedol': 'Sedol',
        'cusip': 'Cusip',
        'client_internal': 'ClientInternal',
        'figi': 'Figi',
        'ric': 'RIC',
        'quote_perm_id': 'QuotePermId',
        'red_code': 'REDCode',
        'bbgid': 'BBGId',
        'ice_code': 'ICECode'
    }

    required_map = {
        'lusid_instrument_id': 'optional',
        'isin': 'optional',
        'sedol': 'optional',
        'cusip': 'optional',
        'client_internal': 'optional',
        'figi': 'optional',
        'ric': 'optional',
        'quote_perm_id': 'optional',
        'red_code': 'optional',
        'bbgid': 'optional',
        'ice_code': 'optional'
    }

    def __init__(self, lusid_instrument_id=None, isin=None, sedol=None, cusip=None, client_internal=None, figi=None, ric=None, quote_perm_id=None, red_code=None, bbgid=None, ice_code=None, local_vars_configuration=None):  # noqa: E501
        """WeightedInstrumentInLineLookupIdentifiers - a model defined in OpenAPI"
        
        :param lusid_instrument_id: 
        :type lusid_instrument_id: str
        :param isin: 
        :type isin: str
        :param sedol: 
        :type sedol: str
        :param cusip: 
        :type cusip: str
        :param client_internal: 
        :type client_internal: str
        :param figi: 
        :type figi: str
        :param ric: 
        :type ric: str
        :param quote_perm_id: 
        :type quote_perm_id: str
        :param red_code: 
        :type red_code: str
        :param bbgid: 
        :type bbgid: str
        :param ice_code: 
        :type ice_code: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._lusid_instrument_id = None
        self._isin = None
        self._sedol = None
        self._cusip = None
        self._client_internal = None
        self._figi = None
        self._ric = None
        self._quote_perm_id = None
        self._red_code = None
        self._bbgid = None
        self._ice_code = None
        self.discriminator = None

        if lusid_instrument_id is not None:
            self.lusid_instrument_id = lusid_instrument_id
        if isin is not None:
            self.isin = isin
        if sedol is not None:
            self.sedol = sedol
        if cusip is not None:
            self.cusip = cusip
        if client_internal is not None:
            self.client_internal = client_internal
        if figi is not None:
            self.figi = figi
        if ric is not None:
            self.ric = ric
        if quote_perm_id is not None:
            self.quote_perm_id = quote_perm_id
        if red_code is not None:
            self.red_code = red_code
        if bbgid is not None:
            self.bbgid = bbgid
        if ice_code is not None:
            self.ice_code = ice_code

    @property
    def lusid_instrument_id(self):
        """Gets the lusid_instrument_id of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501


        :return: The lusid_instrument_id of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501
        :rtype: str
        """
        return self._lusid_instrument_id

    @lusid_instrument_id.setter
    def lusid_instrument_id(self, lusid_instrument_id):
        """Sets the lusid_instrument_id of this WeightedInstrumentInLineLookupIdentifiers.


        :param lusid_instrument_id: The lusid_instrument_id of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501
        :type lusid_instrument_id: str
        """

        self._lusid_instrument_id = lusid_instrument_id

    @property
    def isin(self):
        """Gets the isin of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501


        :return: The isin of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501
        :rtype: str
        """
        return self._isin

    @isin.setter
    def isin(self, isin):
        """Sets the isin of this WeightedInstrumentInLineLookupIdentifiers.


        :param isin: The isin of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501
        :type isin: str
        """

        self._isin = isin

    @property
    def sedol(self):
        """Gets the sedol of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501


        :return: The sedol of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501
        :rtype: str
        """
        return self._sedol

    @sedol.setter
    def sedol(self, sedol):
        """Sets the sedol of this WeightedInstrumentInLineLookupIdentifiers.


        :param sedol: The sedol of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501
        :type sedol: str
        """

        self._sedol = sedol

    @property
    def cusip(self):
        """Gets the cusip of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501


        :return: The cusip of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501
        :rtype: str
        """
        return self._cusip

    @cusip.setter
    def cusip(self, cusip):
        """Sets the cusip of this WeightedInstrumentInLineLookupIdentifiers.


        :param cusip: The cusip of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501
        :type cusip: str
        """

        self._cusip = cusip

    @property
    def client_internal(self):
        """Gets the client_internal of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501


        :return: The client_internal of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501
        :rtype: str
        """
        return self._client_internal

    @client_internal.setter
    def client_internal(self, client_internal):
        """Sets the client_internal of this WeightedInstrumentInLineLookupIdentifiers.


        :param client_internal: The client_internal of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501
        :type client_internal: str
        """

        self._client_internal = client_internal

    @property
    def figi(self):
        """Gets the figi of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501


        :return: The figi of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501
        :rtype: str
        """
        return self._figi

    @figi.setter
    def figi(self, figi):
        """Sets the figi of this WeightedInstrumentInLineLookupIdentifiers.


        :param figi: The figi of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501
        :type figi: str
        """

        self._figi = figi

    @property
    def ric(self):
        """Gets the ric of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501


        :return: The ric of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501
        :rtype: str
        """
        return self._ric

    @ric.setter
    def ric(self, ric):
        """Sets the ric of this WeightedInstrumentInLineLookupIdentifiers.


        :param ric: The ric of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501
        :type ric: str
        """

        self._ric = ric

    @property
    def quote_perm_id(self):
        """Gets the quote_perm_id of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501


        :return: The quote_perm_id of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501
        :rtype: str
        """
        return self._quote_perm_id

    @quote_perm_id.setter
    def quote_perm_id(self, quote_perm_id):
        """Sets the quote_perm_id of this WeightedInstrumentInLineLookupIdentifiers.


        :param quote_perm_id: The quote_perm_id of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501
        :type quote_perm_id: str
        """

        self._quote_perm_id = quote_perm_id

    @property
    def red_code(self):
        """Gets the red_code of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501


        :return: The red_code of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501
        :rtype: str
        """
        return self._red_code

    @red_code.setter
    def red_code(self, red_code):
        """Sets the red_code of this WeightedInstrumentInLineLookupIdentifiers.


        :param red_code: The red_code of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501
        :type red_code: str
        """

        self._red_code = red_code

    @property
    def bbgid(self):
        """Gets the bbgid of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501


        :return: The bbgid of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501
        :rtype: str
        """
        return self._bbgid

    @bbgid.setter
    def bbgid(self, bbgid):
        """Sets the bbgid of this WeightedInstrumentInLineLookupIdentifiers.


        :param bbgid: The bbgid of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501
        :type bbgid: str
        """

        self._bbgid = bbgid

    @property
    def ice_code(self):
        """Gets the ice_code of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501


        :return: The ice_code of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501
        :rtype: str
        """
        return self._ice_code

    @ice_code.setter
    def ice_code(self, ice_code):
        """Sets the ice_code of this WeightedInstrumentInLineLookupIdentifiers.


        :param ice_code: The ice_code of this WeightedInstrumentInLineLookupIdentifiers.  # noqa: E501
        :type ice_code: str
        """

        self._ice_code = ice_code

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
        if not isinstance(other, WeightedInstrumentInLineLookupIdentifiers):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WeightedInstrumentInLineLookupIdentifiers):
            return True

        return self.to_dict() != other.to_dict()
