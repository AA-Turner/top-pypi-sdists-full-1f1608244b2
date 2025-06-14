# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 66.26.0-v202506111109-CD
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class SwapAcrossAssetsSearchV1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'is_include': 'bool',
        'root_asset_id': 'str',
        'search_type': 'str',
        'swap_item_id': 'str'
    }

    attribute_map = {
        'is_include': 'isInclude',
        'root_asset_id': 'rootAssetId',
        'search_type': 'searchType',
        'swap_item_id': 'swapItemId'
    }

    def __init__(self, is_include=None, root_asset_id=None, search_type=None, swap_item_id=None):
        """
        SwapAcrossAssetsSearchV1 - a model defined in Swagger
        """

        self._is_include = None
        self._root_asset_id = None
        self._search_type = None
        self._swap_item_id = None

        if is_include is not None:
          self.is_include = is_include
        if root_asset_id is not None:
          self.root_asset_id = root_asset_id
        if search_type is not None:
          self.search_type = search_type
        if swap_item_id is not None:
          self.swap_item_id = swap_item_id

    @property
    def is_include(self):
        """
        Gets the is_include of this SwapAcrossAssetsSearchV1.
        If true the items found by this configuration will be included in the output, if false then the results will be excluded from the output (even if found by another finder configuration)

        :return: The is_include of this SwapAcrossAssetsSearchV1.
        :rtype: bool
        """
        return self._is_include

    @is_include.setter
    def is_include(self, is_include):
        """
        Sets the is_include of this SwapAcrossAssetsSearchV1.
        If true the items found by this configuration will be included in the output, if false then the results will be excluded from the output (even if found by another finder configuration)

        :param is_include: The is_include of this SwapAcrossAssetsSearchV1.
        :type: bool
        """
        if is_include is None:
            raise ValueError("Invalid value for `is_include`, must not be `None`")

        self._is_include = is_include

    @property
    def root_asset_id(self):
        """
        Gets the root_asset_id of this SwapAcrossAssetsSearchV1.
        Used if finder type is SwapAcrossAssets, this specifies the ID of the root asset whose immediate children will be iterated.

        :return: The root_asset_id of this SwapAcrossAssetsSearchV1.
        :rtype: str
        """
        return self._root_asset_id

    @root_asset_id.setter
    def root_asset_id(self, root_asset_id):
        """
        Sets the root_asset_id of this SwapAcrossAssetsSearchV1.
        Used if finder type is SwapAcrossAssets, this specifies the ID of the root asset whose immediate children will be iterated.

        :param root_asset_id: The root_asset_id of this SwapAcrossAssetsSearchV1.
        :type: str
        """

        self._root_asset_id = root_asset_id

    @property
    def search_type(self):
        """
        Gets the search_type of this SwapAcrossAssetsSearchV1.
        The type of finder

        :return: The search_type of this SwapAcrossAssetsSearchV1.
        :rtype: str
        """
        return self._search_type

    @search_type.setter
    def search_type(self, search_type):
        """
        Sets the search_type of this SwapAcrossAssetsSearchV1.
        The type of finder

        :param search_type: The search_type of this SwapAcrossAssetsSearchV1.
        :type: str
        """
        if search_type is None:
            raise ValueError("Invalid value for `search_type`, must not be `None`")
        allowed_values = ["SWAP_ACROSS_ASSETS", "FIXED_LIST", "PROPERTY", "MATERIALIZED_TABLE_UUID_COLUMN"]
        if search_type not in allowed_values:
            raise ValueError(
                "Invalid value for `search_type` ({0}), must be one of {1}"
                .format(search_type, allowed_values)
            )

        self._search_type = search_type

    @property
    def swap_item_id(self):
        """
        Gets the swap_item_id of this SwapAcrossAssetsSearchV1.
        Used if finder type is SwapAcrossAssets, this specifies the ID of the formula item that will be swapped with each asset beneath the root. Each successful swap will be added to the list of found items

        :return: The swap_item_id of this SwapAcrossAssetsSearchV1.
        :rtype: str
        """
        return self._swap_item_id

    @swap_item_id.setter
    def swap_item_id(self, swap_item_id):
        """
        Sets the swap_item_id of this SwapAcrossAssetsSearchV1.
        Used if finder type is SwapAcrossAssets, this specifies the ID of the formula item that will be swapped with each asset beneath the root. Each successful swap will be added to the list of found items

        :param swap_item_id: The swap_item_id of this SwapAcrossAssetsSearchV1.
        :type: str
        """

        self._swap_item_id = swap_item_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        if not isinstance(other, SwapAcrossAssetsSearchV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
