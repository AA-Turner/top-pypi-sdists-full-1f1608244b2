# coding: utf-8

"""
    Cudo Compute service

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cudo_compute.configuration import Configuration


class UpdateDataCenterBodyDataCenter(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'region_id': 'str',
        'supplier_name': 'str',
        'renewable_energy': 'bool',
        'lng_lat': 'Point',
        'create_by': 'str',
        'one_frontend_id': 'str',
        's3_endpoint': 'str'
    }

    attribute_map = {
        'region_id': 'regionId',
        'supplier_name': 'supplierName',
        'renewable_energy': 'renewableEnergy',
        'lng_lat': 'lngLat',
        'create_by': 'createBy',
        'one_frontend_id': 'oneFrontendId',
        's3_endpoint': 's3Endpoint'
    }

    def __init__(self, region_id=None, supplier_name=None, renewable_energy=None, lng_lat=None, create_by=None, one_frontend_id=None, s3_endpoint=None, _configuration=None):  # noqa: E501
        """UpdateDataCenterBodyDataCenter - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._region_id = None
        self._supplier_name = None
        self._renewable_energy = None
        self._lng_lat = None
        self._create_by = None
        self._one_frontend_id = None
        self._s3_endpoint = None
        self.discriminator = None

        if region_id is not None:
            self.region_id = region_id
        if supplier_name is not None:
            self.supplier_name = supplier_name
        if renewable_energy is not None:
            self.renewable_energy = renewable_energy
        if lng_lat is not None:
            self.lng_lat = lng_lat
        if create_by is not None:
            self.create_by = create_by
        if one_frontend_id is not None:
            self.one_frontend_id = one_frontend_id
        if s3_endpoint is not None:
            self.s3_endpoint = s3_endpoint

    @property
    def region_id(self):
        """Gets the region_id of this UpdateDataCenterBodyDataCenter.  # noqa: E501


        :return: The region_id of this UpdateDataCenterBodyDataCenter.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this UpdateDataCenterBodyDataCenter.


        :param region_id: The region_id of this UpdateDataCenterBodyDataCenter.  # noqa: E501
        :type: str
        """

        self._region_id = region_id

    @property
    def supplier_name(self):
        """Gets the supplier_name of this UpdateDataCenterBodyDataCenter.  # noqa: E501


        :return: The supplier_name of this UpdateDataCenterBodyDataCenter.  # noqa: E501
        :rtype: str
        """
        return self._supplier_name

    @supplier_name.setter
    def supplier_name(self, supplier_name):
        """Sets the supplier_name of this UpdateDataCenterBodyDataCenter.


        :param supplier_name: The supplier_name of this UpdateDataCenterBodyDataCenter.  # noqa: E501
        :type: str
        """

        self._supplier_name = supplier_name

    @property
    def renewable_energy(self):
        """Gets the renewable_energy of this UpdateDataCenterBodyDataCenter.  # noqa: E501


        :return: The renewable_energy of this UpdateDataCenterBodyDataCenter.  # noqa: E501
        :rtype: bool
        """
        return self._renewable_energy

    @renewable_energy.setter
    def renewable_energy(self, renewable_energy):
        """Sets the renewable_energy of this UpdateDataCenterBodyDataCenter.


        :param renewable_energy: The renewable_energy of this UpdateDataCenterBodyDataCenter.  # noqa: E501
        :type: bool
        """

        self._renewable_energy = renewable_energy

    @property
    def lng_lat(self):
        """Gets the lng_lat of this UpdateDataCenterBodyDataCenter.  # noqa: E501


        :return: The lng_lat of this UpdateDataCenterBodyDataCenter.  # noqa: E501
        :rtype: Point
        """
        return self._lng_lat

    @lng_lat.setter
    def lng_lat(self, lng_lat):
        """Sets the lng_lat of this UpdateDataCenterBodyDataCenter.


        :param lng_lat: The lng_lat of this UpdateDataCenterBodyDataCenter.  # noqa: E501
        :type: Point
        """

        self._lng_lat = lng_lat

    @property
    def create_by(self):
        """Gets the create_by of this UpdateDataCenterBodyDataCenter.  # noqa: E501


        :return: The create_by of this UpdateDataCenterBodyDataCenter.  # noqa: E501
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this UpdateDataCenterBodyDataCenter.


        :param create_by: The create_by of this UpdateDataCenterBodyDataCenter.  # noqa: E501
        :type: str
        """

        self._create_by = create_by

    @property
    def one_frontend_id(self):
        """Gets the one_frontend_id of this UpdateDataCenterBodyDataCenter.  # noqa: E501


        :return: The one_frontend_id of this UpdateDataCenterBodyDataCenter.  # noqa: E501
        :rtype: str
        """
        return self._one_frontend_id

    @one_frontend_id.setter
    def one_frontend_id(self, one_frontend_id):
        """Sets the one_frontend_id of this UpdateDataCenterBodyDataCenter.


        :param one_frontend_id: The one_frontend_id of this UpdateDataCenterBodyDataCenter.  # noqa: E501
        :type: str
        """

        self._one_frontend_id = one_frontend_id

    @property
    def s3_endpoint(self):
        """Gets the s3_endpoint of this UpdateDataCenterBodyDataCenter.  # noqa: E501


        :return: The s3_endpoint of this UpdateDataCenterBodyDataCenter.  # noqa: E501
        :rtype: str
        """
        return self._s3_endpoint

    @s3_endpoint.setter
    def s3_endpoint(self, s3_endpoint):
        """Sets the s3_endpoint of this UpdateDataCenterBodyDataCenter.


        :param s3_endpoint: The s3_endpoint of this UpdateDataCenterBodyDataCenter.  # noqa: E501
        :type: str
        """

        self._s3_endpoint = s3_endpoint

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(UpdateDataCenterBodyDataCenter, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateDataCenterBodyDataCenter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateDataCenterBodyDataCenter):
            return True

        return self.to_dict() != other.to_dict()
