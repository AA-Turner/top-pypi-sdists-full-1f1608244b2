"""
    Agilicus API

    Agilicus is API-first. Modern software is controlled by other software, is open, is available for you to use the way you want, securely, simply.  The OpenAPI Specification in YAML format is available on [www](https://www.agilicus.com/www/api/agilicus-openapi.yaml) for importing to other tools.  A rendered, online viewable and usable version of this specification is available at [api](https://www.agilicus.com/api). You may try the API inline directly in the web page. To do so, first obtain an Authentication Token (the simplest way is to install the Python SDK, and then run `agilicus-cli --issuer https://MYISSUER get-token`). You will need an org-id for most calls (and can obtain from `agilicus-cli --issuer https://MYISSUER list-orgs`). The `MYISSUER` will typically be `auth.MYDOMAIN`, and you will see it as you sign-in to the administrative UI.  This API releases on Bearer-Token authentication. To obtain a valid bearer token you will need to Authenticate to an Issuer with OpenID Connect (a superset of OAUTH2).  Your \"issuer\" will look like https://auth.MYDOMAIN. For example, when you signed-up, if you said \"use my own domain name\" and assigned a CNAME of cloud.example.com, then your issuer would be https://auth.cloud.example.com.  If you selected \"use an Agilicus supplied domain name\", your issuer would look like https://auth.myorg.agilicus.cloud.  For test purposes you can use our [Python SDK](https://pypi.org/project/agilicus/) and run `agilicus-cli --issuer https://auth.MYDOMAIN get-token`.  This API may be used in any language runtime that supports OpenAPI 3.0, or, you may use our [Python SDK](https://pypi.org/project/agilicus/), our [Typescript SDK](https://www.npmjs.com/package/@agilicus/angular), or our [Golang SDK](https://git.agilicus.com/pub/sdk-go).  100% of the activities in our system our API-driven, from our web-admin, through our progressive web applications, to all internals: there is nothing that is not accessible.  For more information, see [developer resources](https://www.agilicus.com/developer).   # noqa: E501

    The version of the OpenAPI document: 2025.06.02
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
    from agilicus_api.model.k8s_slug import K8sSlug
    from agilicus_api.model.network_mount_rule_config import NetworkMountRuleConfig
    from agilicus_api.model.resource_config import ResourceConfig
    globals()['K8sSlug'] = K8sSlug
    globals()['NetworkMountRuleConfig'] = NetworkMountRuleConfig
    globals()['ResourceConfig'] = ResourceConfig


class FileShareServiceSpec(ModelNormal):
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
        ('name',): {
            'max_length': 100,
            'regex': {
                'pattern': r'^[a-zA-Z0-9-_.:]+$',  # noqa: E501
            },
        },
        ('share_name',): {
            'max_length': 1024,
        },
        ('local_path',): {
            'max_length': 4096,
        },
        ('share_index',): {
            'inclusive_maximum': 4294967295,
            'inclusive_minimum': 1,
        },
        ('transport_base_domain',): {
            'max_length': 240,
        },
    }

    @property
    def name(self):
       return self.get("name")

    @name.setter
    def name(self, new_value):
       self.name = new_value

    @property
    def name_slug(self):
       return self.get("name_slug")

    @name_slug.setter
    def name_slug(self, new_value):
       self.name_slug = new_value

    @property
    def share_name(self):
       return self.get("share_name")

    @share_name.setter
    def share_name(self, new_value):
       self.share_name = new_value

    @property
    def org_id(self):
       return self.get("org_id")

    @org_id.setter
    def org_id(self, new_value):
       self.org_id = new_value

    @property
    def local_path(self):
       return self.get("local_path")

    @local_path.setter
    def local_path(self, new_value):
       self.local_path = new_value

    @property
    def connector_id(self):
       return self.get("connector_id")

    @connector_id.setter
    def connector_id(self, new_value):
       self.connector_id = new_value

    @property
    def share_index(self):
       return self.get("share_index")

    @share_index.setter
    def share_index(self, new_value):
       self.share_index = new_value

    @property
    def transport_end_to_end_tls(self):
       return self.get("transport_end_to_end_tls")

    @transport_end_to_end_tls.setter
    def transport_end_to_end_tls(self, new_value):
       self.transport_end_to_end_tls = new_value

    @property
    def transport_base_domain(self):
       return self.get("transport_base_domain")

    @transport_base_domain.setter
    def transport_base_domain(self, new_value):
       self.transport_base_domain = new_value

    @property
    def file_level_access_permissions(self):
       return self.get("file_level_access_permissions")

    @file_level_access_permissions.setter
    def file_level_access_permissions(self, new_value):
       self.file_level_access_permissions = new_value

    @property
    def client_config(self):
       return self.get("client_config")

    @client_config.setter
    def client_config(self, new_value):
       self.client_config = new_value

    @property
    def resource_config(self):
       return self.get("resource_config")

    @resource_config.setter
    def resource_config(self, new_value):
       self.resource_config = new_value

    @property
    def sub_path(self):
       return self.get("sub_path")

    @sub_path.setter
    def sub_path(self, new_value):
       self.sub_path = new_value

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
            'name': (str,),  # noqa: E501
            'share_name': (str,),  # noqa: E501
            'org_id': (str,),  # noqa: E501
            'local_path': (str,),  # noqa: E501
            'connector_id': (str,),  # noqa: E501
            'name_slug': (K8sSlug,),  # noqa: E501
            'share_index': (int,),  # noqa: E501
            'transport_end_to_end_tls': (bool,),  # noqa: E501
            'transport_base_domain': (str,),  # noqa: E501
            'file_level_access_permissions': (bool,),  # noqa: E501
            'client_config': ([NetworkMountRuleConfig],),  # noqa: E501
            'resource_config': (ResourceConfig,),  # noqa: E501
            'sub_path': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'name': 'name',  # noqa: E501
        'share_name': 'share_name',  # noqa: E501
        'org_id': 'org_id',  # noqa: E501
        'local_path': 'local_path',  # noqa: E501
        'connector_id': 'connector_id',  # noqa: E501
        'name_slug': 'name_slug',  # noqa: E501
        'share_index': 'share_index',  # noqa: E501
        'transport_end_to_end_tls': 'transport_end_to_end_tls',  # noqa: E501
        'transport_base_domain': 'transport_base_domain',  # noqa: E501
        'file_level_access_permissions': 'file_level_access_permissions',  # noqa: E501
        'client_config': 'client_config',  # noqa: E501
        'resource_config': 'resource_config',  # noqa: E501
        'sub_path': 'sub_path',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, name, share_name, org_id, local_path, connector_id, *args, **kwargs):  # noqa: E501
        """FileShareServiceSpec - a model defined in OpenAPI

        Args:
            name (str): The name of the service. This uniquely identifies the service within the organisation. 
            share_name (str): The name of the share as exposed to the Internet. This will be used to build the URI used to mount the share. The share_name is unique among the file shares of the organisation. 
            org_id (str): Unique identifier
            local_path (str): The path to the directory to share on the local file system. This should point to a directory, not a file. Use a slash ('/', U+002F) to separate directories within the path. 
            connector_id (str): Unique identifier

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
            name_slug (K8sSlug): [optional]  # noqa: E501
            share_index (int): The index of the FileShareService. This is used to construct a unique URI at which to access this FileShareService. . [optional]  # noqa: E501
            transport_end_to_end_tls (bool): Whether or not the FileShareService encrypts data using the same Transport Layer Security (TLS) session as seen by the client. Setting this to true will cause the FileShareService to provision a Certificate signed by a private key only known to it. All traffic to and from the FileShareService will be encrypted using a TLS session derived from that Certificate. Setting this to false will cause the FileShareService to use a TLS session derived from a Certificate provisioned by the Agilicus Cloud. . [optional]  # noqa: E501
            transport_base_domain (str): The base domain from which to access this share. The file share endpoint will be \"https://share-$(share_index).$(base_domain)\" . [optional]  # noqa: E501
            file_level_access_permissions (bool): Enable file acl permissions on the agent's host. This option enables fine grained control of individual files based on a user's specific groups and access level . [optional] if omitted the server will use the default value of False  # noqa: E501
            client_config ([NetworkMountRuleConfig]): The configuration to determine where this share should be used automatically. Use this field to set up clients to mount a share automatically. . [optional]  # noqa: E501
            resource_config (ResourceConfig): [optional]  # noqa: E501
            sub_path (str): The subpath extending the local file system which is being shared, supporting vars expansion. [optional]  # noqa: E501
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

        self.name = name
        self.share_name = share_name
        self.org_id = org_id
        self.local_path = local_path
        self.connector_id = connector_id
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
    def __init__(self, name, share_name, org_id, local_path, connector_id, *args, **kwargs):  # noqa: E501
        """FileShareServiceSpec - a model defined in OpenAPI

        Args:
            name (str): The name of the service. This uniquely identifies the service within the organisation. 
            share_name (str): The name of the share as exposed to the Internet. This will be used to build the URI used to mount the share. The share_name is unique among the file shares of the organisation. 
            org_id (str): Unique identifier
            local_path (str): The path to the directory to share on the local file system. This should point to a directory, not a file. Use a slash ('/', U+002F) to separate directories within the path. 
            connector_id (str): Unique identifier

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
            name_slug (K8sSlug): [optional]  # noqa: E501
            share_index (int): The index of the FileShareService. This is used to construct a unique URI at which to access this FileShareService. . [optional]  # noqa: E501
            transport_end_to_end_tls (bool): Whether or not the FileShareService encrypts data using the same Transport Layer Security (TLS) session as seen by the client. Setting this to true will cause the FileShareService to provision a Certificate signed by a private key only known to it. All traffic to and from the FileShareService will be encrypted using a TLS session derived from that Certificate. Setting this to false will cause the FileShareService to use a TLS session derived from a Certificate provisioned by the Agilicus Cloud. . [optional]  # noqa: E501
            transport_base_domain (str): The base domain from which to access this share. The file share endpoint will be \"https://share-$(share_index).$(base_domain)\" . [optional]  # noqa: E501
            file_level_access_permissions (bool): Enable file acl permissions on the agent's host. This option enables fine grained control of individual files based on a user's specific groups and access level . [optional] if omitted the server will use the default value of False  # noqa: E501
            client_config ([NetworkMountRuleConfig]): The configuration to determine where this share should be used automatically. Use this field to set up clients to mount a share automatically. . [optional]  # noqa: E501
            resource_config (ResourceConfig): [optional]  # noqa: E501
            sub_path (str): The subpath extending the local file system which is being shared, supporting vars expansion. [optional]  # noqa: E501
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

        self.name = name
        self.share_name = share_name
        self.org_id = org_id
        self.local_path = local_path
        self.connector_id = connector_id
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

