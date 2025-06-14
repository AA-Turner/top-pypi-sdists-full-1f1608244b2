"""
    Agilicus API

    Agilicus is API-first. Modern software is controlled by other software, is open, is available for you to use the way you want, securely, simply.  The OpenAPI Specification in YAML format is available on [www](https://www.agilicus.com/www/api/agilicus-openapi.yaml) for importing to other tools.  A rendered, online viewable and usable version of this specification is available at [api](https://www.agilicus.com/api). You may try the API inline directly in the web page. To do so, first obtain an Authentication Token (the simplest way is to install the Python SDK, and then run `agilicus-cli --issuer https://MYISSUER get-token`). You will need an org-id for most calls (and can obtain from `agilicus-cli --issuer https://MYISSUER list-orgs`). The `MYISSUER` will typically be `auth.MYDOMAIN`, and you will see it as you sign-in to the administrative UI.  This API releases on Bearer-Token authentication. To obtain a valid bearer token you will need to Authenticate to an Issuer with OpenID Connect (a superset of OAUTH2).  Your \"issuer\" will look like https://auth.MYDOMAIN. For example, when you signed-up, if you said \"use my own domain name\" and assigned a CNAME of cloud.example.com, then your issuer would be https://auth.cloud.example.com.  If you selected \"use an Agilicus supplied domain name\", your issuer would look like https://auth.myorg.agilicus.cloud.  For test purposes you can use our [Python SDK](https://pypi.org/project/agilicus/) and run `agilicus-cli --issuer https://auth.MYDOMAIN get-token`.  This API may be used in any language runtime that supports OpenAPI 3.0, or, you may use our [Python SDK](https://pypi.org/project/agilicus/), our [Typescript SDK](https://www.npmjs.com/package/@agilicus/angular), or our [Golang SDK](https://git.agilicus.com/pub/sdk-go).  100% of the activities in our system our API-driven, from our web-admin, through our progressive web applications, to all internals: there is nothing that is not accessible.  For more information, see [developer resources](https://www.agilicus.com/developer).   # noqa: E501

    The version of the OpenAPI document: 2025.06.11
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from agilicus_api.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from agilicus_api.exceptions import ApiAttributeError


def lazy_import():
    from agilicus_api.model.domain import Domain
    globals()['Domain'] = Domain


class PointOfPresenceRouting(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @property
    def domains(self):
       return self.get("domains")

    @domains.setter
    def domains(self, new_value):
       self.domains = new_value

    @property
    def org_domains(self):
       return self.get("org_domains")

    @org_domains.setter
    def org_domains(self, new_value):
       self.org_domains = new_value

    @property
    def requests_enabled(self):
       return self.get("requests_enabled")

    @requests_enabled.setter
    def requests_enabled(self, new_value):
       self.requests_enabled = new_value

    @property
    def public(self):
       return self.get("public")

    @public.setter
    def public(self, new_value):
       self.public = new_value

    @property
    def restrict_by_user_id(self):
       return self.get("restrict_by_user_id")

    @restrict_by_user_id.setter
    def restrict_by_user_id(self, new_value):
       self.restrict_by_user_id = new_value

    @property
    def permitted_user_ids(self):
       return self.get("permitted_user_ids")

    @permitted_user_ids.setter
    def permitted_user_ids(self, new_value):
       self.permitted_user_ids = new_value

    @property
    def ces(self):
       return self.get("ces")

    @ces.setter
    def ces(self, new_value):
       self.ces = new_value

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'domains': ([Domain],),  # noqa: E501
            'org_domains': ([Domain],),  # noqa: E501
            'requests_enabled': (bool,),  # noqa: E501
            'public': (bool,),  # noqa: E501
            'restrict_by_user_id': (bool,),  # noqa: E501
            'permitted_user_ids': ([str],),  # noqa: E501
            'ces': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'domains': 'domains',  # noqa: E501
        'org_domains': 'org_domains',  # noqa: E501
        'requests_enabled': 'requests_enabled',  # noqa: E501
        'public': 'public',  # noqa: E501
        'restrict_by_user_id': 'restrict_by_user_id',  # noqa: E501
        'permitted_user_ids': 'permitted_user_ids',  # noqa: E501
        'ces': 'ces',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, domains, *args, **kwargs):  # noqa: E501
        """PointOfPresenceRouting - a model defined in OpenAPI

        Args:
            domains ([Domain]): The domains that address this point of presence. Use these when configuring external systems such as a DNS CNAME or a firewall. 

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            org_domains ([Domain]): Organisation subdomains supported by this region. [optional]  # noqa: E501
            requests_enabled (bool): If true, allow this PointOfPresence to serve RoutingRequests.. [optional]  # noqa: E501
            public (bool): If true, this region is public and is visible to external systems.. [optional]  # noqa: E501
            restrict_by_user_id (bool): If true, routing is restricted by user_id (see permitted_user_ids). [optional]  # noqa: E501
            permitted_user_ids ([str]): A list of user_ids that are permitted for using this region on a routing request. The omission of this property (not set) allows any user_id. . [optional]  # noqa: E501
            ces (str): A Common Expression Library (CES) used to evaluate if a routing request should utilize this Region  The following objects are available to the ces program:      geoip:       iso_code:       city:       country:       currency:     token_info:       email:       sub:       org:  Example ces that evaluates to true if subscriber ip address is found in USA:      geoip.iso_code == 'US' . [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.domains = domains
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    def __python_set(val):
        return set(val)
 
    required_properties = __python_set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, domains, *args, **kwargs):  # noqa: E501
        """PointOfPresenceRouting - a model defined in OpenAPI

        Args:
            domains ([Domain]): The domains that address this point of presence. Use these when configuring external systems such as a DNS CNAME or a firewall. 

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            org_domains ([Domain]): Organisation subdomains supported by this region. [optional]  # noqa: E501
            requests_enabled (bool): If true, allow this PointOfPresence to serve RoutingRequests.. [optional]  # noqa: E501
            public (bool): If true, this region is public and is visible to external systems.. [optional]  # noqa: E501
            restrict_by_user_id (bool): If true, routing is restricted by user_id (see permitted_user_ids). [optional]  # noqa: E501
            permitted_user_ids ([str]): A list of user_ids that are permitted for using this region on a routing request. The omission of this property (not set) allows any user_id. . [optional]  # noqa: E501
            ces (str): A Common Expression Library (CES) used to evaluate if a routing request should utilize this Region  The following objects are available to the ces program:      geoip:       iso_code:       city:       country:       currency:     token_info:       email:       sub:       org:  Example ces that evaluates to true if subscriber ip address is found in USA:      geoip.iso_code == 'US' . [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.domains = domains
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

