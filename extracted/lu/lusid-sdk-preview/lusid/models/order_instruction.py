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


class OrderInstruction(object):
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
        'id': 'ResourceId',
        'created_date': 'datetime',
        'properties': 'dict(str, PerpetualProperty)',
        'portfolio_id': 'ResourceId',
        'instrument_identifiers': 'dict(str, str)',
        'quantity': 'float',
        'weight': 'float',
        'price': 'CurrencyAndAmount',
        'instrument_scope': 'str',
        'lusid_instrument_id': 'str',
        'version': 'Version',
        'links': 'list[Link]'
    }

    attribute_map = {
        'id': 'id',
        'created_date': 'createdDate',
        'properties': 'properties',
        'portfolio_id': 'portfolioId',
        'instrument_identifiers': 'instrumentIdentifiers',
        'quantity': 'quantity',
        'weight': 'weight',
        'price': 'price',
        'instrument_scope': 'instrumentScope',
        'lusid_instrument_id': 'lusidInstrumentId',
        'version': 'version',
        'links': 'links'
    }

    required_map = {
        'id': 'required',
        'created_date': 'required',
        'properties': 'optional',
        'portfolio_id': 'optional',
        'instrument_identifiers': 'required',
        'quantity': 'optional',
        'weight': 'optional',
        'price': 'optional',
        'instrument_scope': 'optional',
        'lusid_instrument_id': 'optional',
        'version': 'optional',
        'links': 'optional'
    }

    def __init__(self, id=None, created_date=None, properties=None, portfolio_id=None, instrument_identifiers=None, quantity=None, weight=None, price=None, instrument_scope=None, lusid_instrument_id=None, version=None, links=None, local_vars_configuration=None):  # noqa: E501
        """OrderInstruction - a model defined in OpenAPI"
        
        :param id:  (required)
        :type id: lusid.ResourceId
        :param created_date:  The active date of this order instruction. (required)
        :type created_date: datetime
        :param properties:  Client-defined properties associated with this execution.
        :type properties: dict[str, lusid.PerpetualProperty]
        :param portfolio_id: 
        :type portfolio_id: lusid.ResourceId
        :param instrument_identifiers:  The instrument ordered. (required)
        :type instrument_identifiers: dict(str, str)
        :param quantity:  The quantity of given instrument ordered.
        :type quantity: float
        :param weight:  The weight of given instrument ordered.
        :type weight: float
        :param price: 
        :type price: lusid.CurrencyAndAmount
        :param instrument_scope:  The scope in which the instrument lies
        :type instrument_scope: str
        :param lusid_instrument_id:  The LUSID instrument id for the instrument ordered.
        :type lusid_instrument_id: str
        :param version: 
        :type version: lusid.Version
        :param links: 
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_date = None
        self._properties = None
        self._portfolio_id = None
        self._instrument_identifiers = None
        self._quantity = None
        self._weight = None
        self._price = None
        self._instrument_scope = None
        self._lusid_instrument_id = None
        self._version = None
        self._links = None
        self.discriminator = None

        self.id = id
        self.created_date = created_date
        self.properties = properties
        if portfolio_id is not None:
            self.portfolio_id = portfolio_id
        self.instrument_identifiers = instrument_identifiers
        self.quantity = quantity
        self.weight = weight
        if price is not None:
            self.price = price
        self.instrument_scope = instrument_scope
        self.lusid_instrument_id = lusid_instrument_id
        if version is not None:
            self.version = version
        self.links = links

    @property
    def id(self):
        """Gets the id of this OrderInstruction.  # noqa: E501


        :return: The id of this OrderInstruction.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrderInstruction.


        :param id: The id of this OrderInstruction.  # noqa: E501
        :type id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_date(self):
        """Gets the created_date of this OrderInstruction.  # noqa: E501

        The active date of this order instruction.  # noqa: E501

        :return: The created_date of this OrderInstruction.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this OrderInstruction.

        The active date of this order instruction.  # noqa: E501

        :param created_date: The created_date of this OrderInstruction.  # noqa: E501
        :type created_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_date is None:  # noqa: E501
            raise ValueError("Invalid value for `created_date`, must not be `None`")  # noqa: E501

        self._created_date = created_date

    @property
    def properties(self):
        """Gets the properties of this OrderInstruction.  # noqa: E501

        Client-defined properties associated with this execution.  # noqa: E501

        :return: The properties of this OrderInstruction.  # noqa: E501
        :rtype: dict[str, lusid.PerpetualProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this OrderInstruction.

        Client-defined properties associated with this execution.  # noqa: E501

        :param properties: The properties of this OrderInstruction.  # noqa: E501
        :type properties: dict[str, lusid.PerpetualProperty]
        """

        self._properties = properties

    @property
    def portfolio_id(self):
        """Gets the portfolio_id of this OrderInstruction.  # noqa: E501


        :return: The portfolio_id of this OrderInstruction.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._portfolio_id

    @portfolio_id.setter
    def portfolio_id(self, portfolio_id):
        """Sets the portfolio_id of this OrderInstruction.


        :param portfolio_id: The portfolio_id of this OrderInstruction.  # noqa: E501
        :type portfolio_id: lusid.ResourceId
        """

        self._portfolio_id = portfolio_id

    @property
    def instrument_identifiers(self):
        """Gets the instrument_identifiers of this OrderInstruction.  # noqa: E501

        The instrument ordered.  # noqa: E501

        :return: The instrument_identifiers of this OrderInstruction.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._instrument_identifiers

    @instrument_identifiers.setter
    def instrument_identifiers(self, instrument_identifiers):
        """Sets the instrument_identifiers of this OrderInstruction.

        The instrument ordered.  # noqa: E501

        :param instrument_identifiers: The instrument_identifiers of this OrderInstruction.  # noqa: E501
        :type instrument_identifiers: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and instrument_identifiers is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_identifiers`, must not be `None`")  # noqa: E501

        self._instrument_identifiers = instrument_identifiers

    @property
    def quantity(self):
        """Gets the quantity of this OrderInstruction.  # noqa: E501

        The quantity of given instrument ordered.  # noqa: E501

        :return: The quantity of this OrderInstruction.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this OrderInstruction.

        The quantity of given instrument ordered.  # noqa: E501

        :param quantity: The quantity of this OrderInstruction.  # noqa: E501
        :type quantity: float
        """

        self._quantity = quantity

    @property
    def weight(self):
        """Gets the weight of this OrderInstruction.  # noqa: E501

        The weight of given instrument ordered.  # noqa: E501

        :return: The weight of this OrderInstruction.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this OrderInstruction.

        The weight of given instrument ordered.  # noqa: E501

        :param weight: The weight of this OrderInstruction.  # noqa: E501
        :type weight: float
        """

        self._weight = weight

    @property
    def price(self):
        """Gets the price of this OrderInstruction.  # noqa: E501


        :return: The price of this OrderInstruction.  # noqa: E501
        :rtype: lusid.CurrencyAndAmount
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this OrderInstruction.


        :param price: The price of this OrderInstruction.  # noqa: E501
        :type price: lusid.CurrencyAndAmount
        """

        self._price = price

    @property
    def instrument_scope(self):
        """Gets the instrument_scope of this OrderInstruction.  # noqa: E501

        The scope in which the instrument lies  # noqa: E501

        :return: The instrument_scope of this OrderInstruction.  # noqa: E501
        :rtype: str
        """
        return self._instrument_scope

    @instrument_scope.setter
    def instrument_scope(self, instrument_scope):
        """Sets the instrument_scope of this OrderInstruction.

        The scope in which the instrument lies  # noqa: E501

        :param instrument_scope: The instrument_scope of this OrderInstruction.  # noqa: E501
        :type instrument_scope: str
        """

        self._instrument_scope = instrument_scope

    @property
    def lusid_instrument_id(self):
        """Gets the lusid_instrument_id of this OrderInstruction.  # noqa: E501

        The LUSID instrument id for the instrument ordered.  # noqa: E501

        :return: The lusid_instrument_id of this OrderInstruction.  # noqa: E501
        :rtype: str
        """
        return self._lusid_instrument_id

    @lusid_instrument_id.setter
    def lusid_instrument_id(self, lusid_instrument_id):
        """Sets the lusid_instrument_id of this OrderInstruction.

        The LUSID instrument id for the instrument ordered.  # noqa: E501

        :param lusid_instrument_id: The lusid_instrument_id of this OrderInstruction.  # noqa: E501
        :type lusid_instrument_id: str
        """

        self._lusid_instrument_id = lusid_instrument_id

    @property
    def version(self):
        """Gets the version of this OrderInstruction.  # noqa: E501


        :return: The version of this OrderInstruction.  # noqa: E501
        :rtype: lusid.Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this OrderInstruction.


        :param version: The version of this OrderInstruction.  # noqa: E501
        :type version: lusid.Version
        """

        self._version = version

    @property
    def links(self):
        """Gets the links of this OrderInstruction.  # noqa: E501


        :return: The links of this OrderInstruction.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this OrderInstruction.


        :param links: The links of this OrderInstruction.  # noqa: E501
        :type links: list[lusid.Link]
        """

        self._links = links

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
        if not isinstance(other, OrderInstruction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrderInstruction):
            return True

        return self.to_dict() != other.to_dict()
