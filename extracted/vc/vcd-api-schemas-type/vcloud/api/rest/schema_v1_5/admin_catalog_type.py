"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re
from .catalog_type import CatalogType


class AdminCatalogType(CatalogType):
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
        'catalog_storage_profiles': 'CatalogStorageProfilesType',
        'external_catalog_subscription_params': 'ExternalCatalogSubscriptionParamsType',
        'remote_uri_probe_result': 'RemoteUriProbeResultType',
        'publish_external_catalog_params': 'PublishExternalCatalogParamsType'
    }

    attribute_map = {
        'catalog_storage_profiles': 'catalogStorageProfiles',
        'external_catalog_subscription_params': 'externalCatalogSubscriptionParams',
        'remote_uri_probe_result': 'remoteUriProbeResult',
        'publish_external_catalog_params': 'publishExternalCatalogParams'
    }

    def __init__(self, catalog_storage_profiles=None,external_catalog_subscription_params=None,remote_uri_probe_result=None,publish_external_catalog_params=None):
        self._catalog_storage_profiles = None
        self._external_catalog_subscription_params = None
        self._remote_uri_probe_result = None
        self._publish_external_catalog_params = None

        if catalog_storage_profiles is not None:
            self.catalog_storage_profiles = catalog_storage_profiles
        if external_catalog_subscription_params is not None:
            self.external_catalog_subscription_params = external_catalog_subscription_params
        if remote_uri_probe_result is not None:
            self.remote_uri_probe_result = remote_uri_probe_result
        if publish_external_catalog_params is not None:
            self.publish_external_catalog_params = publish_external_catalog_params

    @property
    def catalog_storage_profiles(self):
        return self._catalog_storage_profiles
    
    @catalog_storage_profiles.setter
    def catalog_storage_profiles(self, catalog_storage_profiles):
        self._catalog_storage_profiles = catalog_storage_profiles

    @property
    def external_catalog_subscription_params(self):
        return self._external_catalog_subscription_params
    
    @external_catalog_subscription_params.setter
    def external_catalog_subscription_params(self, external_catalog_subscription_params):
        self._external_catalog_subscription_params = external_catalog_subscription_params

    @property
    def remote_uri_probe_result(self):
        return self._remote_uri_probe_result
    
    @remote_uri_probe_result.setter
    def remote_uri_probe_result(self, remote_uri_probe_result):
        self._remote_uri_probe_result = remote_uri_probe_result

    @property
    def publish_external_catalog_params(self):
        return self._publish_external_catalog_params
    
    @publish_external_catalog_params.setter
    def publish_external_catalog_params(self, publish_external_catalog_params):
        self._publish_external_catalog_params = publish_external_catalog_params


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
        """Returns the string representation of the model"""
        return pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AdminCatalogType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
