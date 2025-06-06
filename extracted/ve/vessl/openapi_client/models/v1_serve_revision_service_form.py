# coding: utf-8

"""
    Aron API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from openapi_client.configuration import Configuration


class V1ServeRevisionServiceForm(object):
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
    """
    openapi_types = {
        'autoscaling': 'V1Autoscaling',
        'auxiliary': 'V1AuxiliaryForm',
        'expose': 'str',
        'healthcheck': 'V1HealthcheckForm',
        'monitoring': 'list[V1PortPath]',
        'openapi': 'V1OpenAPIForm',
        'serverless': 'V1ServerlessOptionsForm'
    }

    attribute_map = {
        'autoscaling': 'autoscaling',
        'auxiliary': 'auxiliary',
        'expose': 'expose',
        'healthcheck': 'healthcheck',
        'monitoring': 'monitoring',
        'openapi': 'openapi',
        'serverless': 'serverless'
    }

    def __init__(self, autoscaling=None, auxiliary=None, expose=None, healthcheck=None, monitoring=None, openapi=None, serverless=None, local_vars_configuration=None):  # noqa: E501
        """V1ServeRevisionServiceForm - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._autoscaling = None
        self._auxiliary = None
        self._expose = None
        self._healthcheck = None
        self._monitoring = None
        self._openapi = None
        self._serverless = None
        self.discriminator = None

        if autoscaling is not None:
            self.autoscaling = autoscaling
        if auxiliary is not None:
            self.auxiliary = auxiliary
        self.expose = expose
        if healthcheck is not None:
            self.healthcheck = healthcheck
        if monitoring is not None:
            self.monitoring = monitoring
        if openapi is not None:
            self.openapi = openapi
        if serverless is not None:
            self.serverless = serverless

    @property
    def autoscaling(self):
        """Gets the autoscaling of this V1ServeRevisionServiceForm.  # noqa: E501


        :return: The autoscaling of this V1ServeRevisionServiceForm.  # noqa: E501
        :rtype: V1Autoscaling
        """
        return self._autoscaling

    @autoscaling.setter
    def autoscaling(self, autoscaling):
        """Sets the autoscaling of this V1ServeRevisionServiceForm.


        :param autoscaling: The autoscaling of this V1ServeRevisionServiceForm.  # noqa: E501
        :type autoscaling: V1Autoscaling
        """

        self._autoscaling = autoscaling

    @property
    def auxiliary(self):
        """Gets the auxiliary of this V1ServeRevisionServiceForm.  # noqa: E501


        :return: The auxiliary of this V1ServeRevisionServiceForm.  # noqa: E501
        :rtype: V1AuxiliaryForm
        """
        return self._auxiliary

    @auxiliary.setter
    def auxiliary(self, auxiliary):
        """Sets the auxiliary of this V1ServeRevisionServiceForm.


        :param auxiliary: The auxiliary of this V1ServeRevisionServiceForm.  # noqa: E501
        :type auxiliary: V1AuxiliaryForm
        """

        self._auxiliary = auxiliary

    @property
    def expose(self):
        """Gets the expose of this V1ServeRevisionServiceForm.  # noqa: E501


        :return: The expose of this V1ServeRevisionServiceForm.  # noqa: E501
        :rtype: str
        """
        return self._expose

    @expose.setter
    def expose(self, expose):
        """Sets the expose of this V1ServeRevisionServiceForm.


        :param expose: The expose of this V1ServeRevisionServiceForm.  # noqa: E501
        :type expose: str
        """
        if self.local_vars_configuration.client_side_validation and expose is None:  # noqa: E501
            raise ValueError("Invalid value for `expose`, must not be `None`")  # noqa: E501

        self._expose = expose

    @property
    def healthcheck(self):
        """Gets the healthcheck of this V1ServeRevisionServiceForm.  # noqa: E501


        :return: The healthcheck of this V1ServeRevisionServiceForm.  # noqa: E501
        :rtype: V1HealthcheckForm
        """
        return self._healthcheck

    @healthcheck.setter
    def healthcheck(self, healthcheck):
        """Sets the healthcheck of this V1ServeRevisionServiceForm.


        :param healthcheck: The healthcheck of this V1ServeRevisionServiceForm.  # noqa: E501
        :type healthcheck: V1HealthcheckForm
        """

        self._healthcheck = healthcheck

    @property
    def monitoring(self):
        """Gets the monitoring of this V1ServeRevisionServiceForm.  # noqa: E501


        :return: The monitoring of this V1ServeRevisionServiceForm.  # noqa: E501
        :rtype: list[V1PortPath]
        """
        return self._monitoring

    @monitoring.setter
    def monitoring(self, monitoring):
        """Sets the monitoring of this V1ServeRevisionServiceForm.


        :param monitoring: The monitoring of this V1ServeRevisionServiceForm.  # noqa: E501
        :type monitoring: list[V1PortPath]
        """

        self._monitoring = monitoring

    @property
    def openapi(self):
        """Gets the openapi of this V1ServeRevisionServiceForm.  # noqa: E501


        :return: The openapi of this V1ServeRevisionServiceForm.  # noqa: E501
        :rtype: V1OpenAPIForm
        """
        return self._openapi

    @openapi.setter
    def openapi(self, openapi):
        """Sets the openapi of this V1ServeRevisionServiceForm.


        :param openapi: The openapi of this V1ServeRevisionServiceForm.  # noqa: E501
        :type openapi: V1OpenAPIForm
        """

        self._openapi = openapi

    @property
    def serverless(self):
        """Gets the serverless of this V1ServeRevisionServiceForm.  # noqa: E501


        :return: The serverless of this V1ServeRevisionServiceForm.  # noqa: E501
        :rtype: V1ServerlessOptionsForm
        """
        return self._serverless

    @serverless.setter
    def serverless(self, serverless):
        """Sets the serverless of this V1ServeRevisionServiceForm.


        :param serverless: The serverless of this V1ServeRevisionServiceForm.  # noqa: E501
        :type serverless: V1ServerlessOptionsForm
        """

        self._serverless = serverless

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
        if not isinstance(other, V1ServeRevisionServiceForm):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ServeRevisionServiceForm):
            return True

        return self.to_dict() != other.to_dict()
