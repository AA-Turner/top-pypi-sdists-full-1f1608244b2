# coding: utf-8

"""
    seccenter20240508

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ScanForGetRegistryImageDetailOutput(object):
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
        'compl_cnt': 'int',
        'compl_distr': 'ComplDistrForGetRegistryImageDetailOutput',
        'err_code': 'str',
        'err_msg': 'str',
        'layer_cnt': 'int',
        'pkg_cnt': 'int',
        'risk': 'int',
        'senfile_cnt': 'int',
        'senfile_distr': 'SenfileDistrForGetRegistryImageDetailOutput',
        'virus_cnt': 'int',
        'vuln_cnt': 'int',
        'vuln_distr': 'VulnDistrForGetRegistryImageDetailOutput'
    }

    attribute_map = {
        'compl_cnt': 'ComplCnt',
        'compl_distr': 'ComplDistr',
        'err_code': 'ErrCode',
        'err_msg': 'ErrMsg',
        'layer_cnt': 'LayerCnt',
        'pkg_cnt': 'PkgCnt',
        'risk': 'Risk',
        'senfile_cnt': 'SenfileCnt',
        'senfile_distr': 'SenfileDistr',
        'virus_cnt': 'VirusCnt',
        'vuln_cnt': 'VulnCnt',
        'vuln_distr': 'VulnDistr'
    }

    def __init__(self, compl_cnt=None, compl_distr=None, err_code=None, err_msg=None, layer_cnt=None, pkg_cnt=None, risk=None, senfile_cnt=None, senfile_distr=None, virus_cnt=None, vuln_cnt=None, vuln_distr=None, _configuration=None):  # noqa: E501
        """ScanForGetRegistryImageDetailOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._compl_cnt = None
        self._compl_distr = None
        self._err_code = None
        self._err_msg = None
        self._layer_cnt = None
        self._pkg_cnt = None
        self._risk = None
        self._senfile_cnt = None
        self._senfile_distr = None
        self._virus_cnt = None
        self._vuln_cnt = None
        self._vuln_distr = None
        self.discriminator = None

        if compl_cnt is not None:
            self.compl_cnt = compl_cnt
        if compl_distr is not None:
            self.compl_distr = compl_distr
        if err_code is not None:
            self.err_code = err_code
        if err_msg is not None:
            self.err_msg = err_msg
        if layer_cnt is not None:
            self.layer_cnt = layer_cnt
        if pkg_cnt is not None:
            self.pkg_cnt = pkg_cnt
        if risk is not None:
            self.risk = risk
        if senfile_cnt is not None:
            self.senfile_cnt = senfile_cnt
        if senfile_distr is not None:
            self.senfile_distr = senfile_distr
        if virus_cnt is not None:
            self.virus_cnt = virus_cnt
        if vuln_cnt is not None:
            self.vuln_cnt = vuln_cnt
        if vuln_distr is not None:
            self.vuln_distr = vuln_distr

    @property
    def compl_cnt(self):
        """Gets the compl_cnt of this ScanForGetRegistryImageDetailOutput.  # noqa: E501


        :return: The compl_cnt of this ScanForGetRegistryImageDetailOutput.  # noqa: E501
        :rtype: int
        """
        return self._compl_cnt

    @compl_cnt.setter
    def compl_cnt(self, compl_cnt):
        """Sets the compl_cnt of this ScanForGetRegistryImageDetailOutput.


        :param compl_cnt: The compl_cnt of this ScanForGetRegistryImageDetailOutput.  # noqa: E501
        :type: int
        """

        self._compl_cnt = compl_cnt

    @property
    def compl_distr(self):
        """Gets the compl_distr of this ScanForGetRegistryImageDetailOutput.  # noqa: E501


        :return: The compl_distr of this ScanForGetRegistryImageDetailOutput.  # noqa: E501
        :rtype: ComplDistrForGetRegistryImageDetailOutput
        """
        return self._compl_distr

    @compl_distr.setter
    def compl_distr(self, compl_distr):
        """Sets the compl_distr of this ScanForGetRegistryImageDetailOutput.


        :param compl_distr: The compl_distr of this ScanForGetRegistryImageDetailOutput.  # noqa: E501
        :type: ComplDistrForGetRegistryImageDetailOutput
        """

        self._compl_distr = compl_distr

    @property
    def err_code(self):
        """Gets the err_code of this ScanForGetRegistryImageDetailOutput.  # noqa: E501


        :return: The err_code of this ScanForGetRegistryImageDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._err_code

    @err_code.setter
    def err_code(self, err_code):
        """Sets the err_code of this ScanForGetRegistryImageDetailOutput.


        :param err_code: The err_code of this ScanForGetRegistryImageDetailOutput.  # noqa: E501
        :type: str
        """

        self._err_code = err_code

    @property
    def err_msg(self):
        """Gets the err_msg of this ScanForGetRegistryImageDetailOutput.  # noqa: E501


        :return: The err_msg of this ScanForGetRegistryImageDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._err_msg

    @err_msg.setter
    def err_msg(self, err_msg):
        """Sets the err_msg of this ScanForGetRegistryImageDetailOutput.


        :param err_msg: The err_msg of this ScanForGetRegistryImageDetailOutput.  # noqa: E501
        :type: str
        """

        self._err_msg = err_msg

    @property
    def layer_cnt(self):
        """Gets the layer_cnt of this ScanForGetRegistryImageDetailOutput.  # noqa: E501


        :return: The layer_cnt of this ScanForGetRegistryImageDetailOutput.  # noqa: E501
        :rtype: int
        """
        return self._layer_cnt

    @layer_cnt.setter
    def layer_cnt(self, layer_cnt):
        """Sets the layer_cnt of this ScanForGetRegistryImageDetailOutput.


        :param layer_cnt: The layer_cnt of this ScanForGetRegistryImageDetailOutput.  # noqa: E501
        :type: int
        """

        self._layer_cnt = layer_cnt

    @property
    def pkg_cnt(self):
        """Gets the pkg_cnt of this ScanForGetRegistryImageDetailOutput.  # noqa: E501


        :return: The pkg_cnt of this ScanForGetRegistryImageDetailOutput.  # noqa: E501
        :rtype: int
        """
        return self._pkg_cnt

    @pkg_cnt.setter
    def pkg_cnt(self, pkg_cnt):
        """Sets the pkg_cnt of this ScanForGetRegistryImageDetailOutput.


        :param pkg_cnt: The pkg_cnt of this ScanForGetRegistryImageDetailOutput.  # noqa: E501
        :type: int
        """

        self._pkg_cnt = pkg_cnt

    @property
    def risk(self):
        """Gets the risk of this ScanForGetRegistryImageDetailOutput.  # noqa: E501


        :return: The risk of this ScanForGetRegistryImageDetailOutput.  # noqa: E501
        :rtype: int
        """
        return self._risk

    @risk.setter
    def risk(self, risk):
        """Sets the risk of this ScanForGetRegistryImageDetailOutput.


        :param risk: The risk of this ScanForGetRegistryImageDetailOutput.  # noqa: E501
        :type: int
        """

        self._risk = risk

    @property
    def senfile_cnt(self):
        """Gets the senfile_cnt of this ScanForGetRegistryImageDetailOutput.  # noqa: E501


        :return: The senfile_cnt of this ScanForGetRegistryImageDetailOutput.  # noqa: E501
        :rtype: int
        """
        return self._senfile_cnt

    @senfile_cnt.setter
    def senfile_cnt(self, senfile_cnt):
        """Sets the senfile_cnt of this ScanForGetRegistryImageDetailOutput.


        :param senfile_cnt: The senfile_cnt of this ScanForGetRegistryImageDetailOutput.  # noqa: E501
        :type: int
        """

        self._senfile_cnt = senfile_cnt

    @property
    def senfile_distr(self):
        """Gets the senfile_distr of this ScanForGetRegistryImageDetailOutput.  # noqa: E501


        :return: The senfile_distr of this ScanForGetRegistryImageDetailOutput.  # noqa: E501
        :rtype: SenfileDistrForGetRegistryImageDetailOutput
        """
        return self._senfile_distr

    @senfile_distr.setter
    def senfile_distr(self, senfile_distr):
        """Sets the senfile_distr of this ScanForGetRegistryImageDetailOutput.


        :param senfile_distr: The senfile_distr of this ScanForGetRegistryImageDetailOutput.  # noqa: E501
        :type: SenfileDistrForGetRegistryImageDetailOutput
        """

        self._senfile_distr = senfile_distr

    @property
    def virus_cnt(self):
        """Gets the virus_cnt of this ScanForGetRegistryImageDetailOutput.  # noqa: E501


        :return: The virus_cnt of this ScanForGetRegistryImageDetailOutput.  # noqa: E501
        :rtype: int
        """
        return self._virus_cnt

    @virus_cnt.setter
    def virus_cnt(self, virus_cnt):
        """Sets the virus_cnt of this ScanForGetRegistryImageDetailOutput.


        :param virus_cnt: The virus_cnt of this ScanForGetRegistryImageDetailOutput.  # noqa: E501
        :type: int
        """

        self._virus_cnt = virus_cnt

    @property
    def vuln_cnt(self):
        """Gets the vuln_cnt of this ScanForGetRegistryImageDetailOutput.  # noqa: E501


        :return: The vuln_cnt of this ScanForGetRegistryImageDetailOutput.  # noqa: E501
        :rtype: int
        """
        return self._vuln_cnt

    @vuln_cnt.setter
    def vuln_cnt(self, vuln_cnt):
        """Sets the vuln_cnt of this ScanForGetRegistryImageDetailOutput.


        :param vuln_cnt: The vuln_cnt of this ScanForGetRegistryImageDetailOutput.  # noqa: E501
        :type: int
        """

        self._vuln_cnt = vuln_cnt

    @property
    def vuln_distr(self):
        """Gets the vuln_distr of this ScanForGetRegistryImageDetailOutput.  # noqa: E501


        :return: The vuln_distr of this ScanForGetRegistryImageDetailOutput.  # noqa: E501
        :rtype: VulnDistrForGetRegistryImageDetailOutput
        """
        return self._vuln_distr

    @vuln_distr.setter
    def vuln_distr(self, vuln_distr):
        """Sets the vuln_distr of this ScanForGetRegistryImageDetailOutput.


        :param vuln_distr: The vuln_distr of this ScanForGetRegistryImageDetailOutput.  # noqa: E501
        :type: VulnDistrForGetRegistryImageDetailOutput
        """

        self._vuln_distr = vuln_distr

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
        if issubclass(ScanForGetRegistryImageDetailOutput, dict):
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
        if not isinstance(other, ScanForGetRegistryImageDetailOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScanForGetRegistryImageDetailOutput):
            return True

        return self.to_dict() != other.to_dict()
