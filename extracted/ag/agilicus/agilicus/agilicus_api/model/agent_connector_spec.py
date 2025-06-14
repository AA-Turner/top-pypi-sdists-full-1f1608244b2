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
    from agilicus_api.model.admin_status import AdminStatus
    from agilicus_api.model.agent_connector_cloud_routing import AgentConnectorCloudRouting
    from agilicus_api.model.agent_connector_spec_provisioning import AgentConnectorSpecProvisioning
    from agilicus_api.model.certificate_revocation_proxy import CertificateRevocationProxy
    from agilicus_api.model.connector_cloud_routing import ConnectorCloudRouting
    from agilicus_api.model.egress_gateway import EgressGateway
    from agilicus_api.model.k8s_slug import K8sSlug
    globals()['AdminStatus'] = AdminStatus
    globals()['AgentConnectorCloudRouting'] = AgentConnectorCloudRouting
    globals()['AgentConnectorSpecProvisioning'] = AgentConnectorSpecProvisioning
    globals()['CertificateRevocationProxy'] = CertificateRevocationProxy
    globals()['ConnectorCloudRouting'] = ConnectorCloudRouting
    globals()['EgressGateway'] = EgressGateway
    globals()['K8sSlug'] = K8sSlug


class AgentConnectorSpec(ModelNormal):
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
        },
        ('max_number_connections',): {
            'inclusive_maximum': 64,
            'inclusive_minimum': 0,
        },
        ('connection_uri',): {
            'max_length': 1024,
        },
        ('proxy_tunnel_termination',): {
            'max_length': 16,
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
    def org_id(self):
       return self.get("org_id")

    @org_id.setter
    def org_id(self, new_value):
       self.org_id = new_value

    @property
    def max_number_connections(self):
       return self.get("max_number_connections")

    @max_number_connections.setter
    def max_number_connections(self, new_value):
       self.max_number_connections = new_value

    @property
    def connection_uri(self):
       return self.get("connection_uri")

    @connection_uri.setter
    def connection_uri(self, new_value):
       self.connection_uri = new_value

    @property
    def service_account_required(self):
       return self.get("service_account_required")

    @service_account_required.setter
    def service_account_required(self, new_value):
       self.service_account_required = new_value

    @property
    def local_authentication_enabled(self):
       return self.get("local_authentication_enabled")

    @local_authentication_enabled.setter
    def local_authentication_enabled(self, new_value):
       self.local_authentication_enabled = new_value

    @property
    def proxy_tunnel_termination(self):
       return self.get("proxy_tunnel_termination")

    @proxy_tunnel_termination.setter
    def proxy_tunnel_termination(self, new_value):
       self.proxy_tunnel_termination = new_value

    @property
    def provisioning(self):
       return self.get("provisioning")

    @provisioning.setter
    def provisioning(self, new_value):
       self.provisioning = new_value

    @property
    def routing(self):
       return self.get("routing")

    @routing.setter
    def routing(self, new_value):
       self.routing = new_value

    @property
    def connector_cloud_routing(self):
       return self.get("connector_cloud_routing")

    @connector_cloud_routing.setter
    def connector_cloud_routing(self, new_value):
       self.connector_cloud_routing = new_value

    @property
    def admin_status(self):
       return self.get("admin_status")

    @admin_status.setter
    def admin_status(self, new_value):
       self.admin_status = new_value

    @property
    def trap_disabled(self):
       return self.get("trap_disabled")

    @trap_disabled.setter
    def trap_disabled(self, new_value):
       self.trap_disabled = new_value

    @property
    def revocation_proxy(self):
       return self.get("revocation_proxy")

    @revocation_proxy.setter
    def revocation_proxy(self, new_value):
       self.revocation_proxy = new_value

    @property
    def egress_gateway(self):
       return self.get("egress_gateway")

    @egress_gateway.setter
    def egress_gateway(self, new_value):
       self.egress_gateway = new_value

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
            'org_id': (str,),  # noqa: E501
            'name_slug': (K8sSlug,),  # noqa: E501
            'max_number_connections': (int,),  # noqa: E501
            'connection_uri': (str,),  # noqa: E501
            'service_account_required': (bool,),  # noqa: E501
            'local_authentication_enabled': (bool,),  # noqa: E501
            'proxy_tunnel_termination': (str,),  # noqa: E501
            'provisioning': (AgentConnectorSpecProvisioning,),  # noqa: E501
            'routing': (AgentConnectorCloudRouting,),  # noqa: E501
            'connector_cloud_routing': (ConnectorCloudRouting,),  # noqa: E501
            'admin_status': (AdminStatus,),  # noqa: E501
            'trap_disabled': (bool,),  # noqa: E501
            'revocation_proxy': (CertificateRevocationProxy,),  # noqa: E501
            'egress_gateway': (EgressGateway,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'name': 'name',  # noqa: E501
        'org_id': 'org_id',  # noqa: E501
        'name_slug': 'name_slug',  # noqa: E501
        'max_number_connections': 'max_number_connections',  # noqa: E501
        'connection_uri': 'connection_uri',  # noqa: E501
        'service_account_required': 'service_account_required',  # noqa: E501
        'local_authentication_enabled': 'local_authentication_enabled',  # noqa: E501
        'proxy_tunnel_termination': 'proxy_tunnel_termination',  # noqa: E501
        'provisioning': 'provisioning',  # noqa: E501
        'routing': 'routing',  # noqa: E501
        'connector_cloud_routing': 'connector_cloud_routing',  # noqa: E501
        'admin_status': 'admin_status',  # noqa: E501
        'trap_disabled': 'trap_disabled',  # noqa: E501
        'revocation_proxy': 'revocation_proxy',  # noqa: E501
        'egress_gateway': 'egress_gateway',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, name, org_id, *args, **kwargs):  # noqa: E501
        """AgentConnectorSpec - a model defined in OpenAPI

        Args:
            name (str): A descriptive name for the connector
            org_id (str): Unique identifier

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
            max_number_connections (int): The maximum number of connections to maintain to the cluster when stable. Note that this value may be exceeded during times of reconfiguration. A value of zero means that the connector is effectively unused by this Secure Agent. . [optional]  # noqa: E501
            connection_uri (str): Overrides the default URI used to connect to this connector. This can be used to point the Secure Agent somewhere other than the default. . [optional]  # noqa: E501
            service_account_required (bool): If service_account_enabled field is set to true, a service account will be created. If service_account_enabled field is set to false, the service account will be deleted. If the service_account_enabled field is not set no action on the service account is taken. . [optional]  # noqa: E501
            local_authentication_enabled (bool): Determines whether or not the agent will expose an endpoint for local authentication. [optional]  # noqa: E501
            proxy_tunnel_termination (str): How a proxy tunnel is terminated.   - tcp: terminate the tunnel at a TCP socket   - inproc: terminate the tunnel at an inprocess socket Note: if not specified, the connector will choose, likely based on its version. . [optional]  # noqa: E501
            provisioning (AgentConnectorSpecProvisioning): [optional]  # noqa: E501
            routing (AgentConnectorCloudRouting): [optional]  # noqa: E501
            connector_cloud_routing (ConnectorCloudRouting): [optional]  # noqa: E501
            admin_status (AdminStatus): [optional]  # noqa: E501
            trap_disabled (bool): Inidicates whether traps (notifications) should be disabled for this entity. A true state indicates notifications will not be sent on transition. . [optional]  # noqa: E501
            revocation_proxy (CertificateRevocationProxy): [optional]  # noqa: E501
            egress_gateway (EgressGateway): [optional]  # noqa: E501
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
        self.org_id = org_id
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
    def __init__(self, name, org_id, *args, **kwargs):  # noqa: E501
        """AgentConnectorSpec - a model defined in OpenAPI

        Args:
            name (str): A descriptive name for the connector
            org_id (str): Unique identifier

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
            max_number_connections (int): The maximum number of connections to maintain to the cluster when stable. Note that this value may be exceeded during times of reconfiguration. A value of zero means that the connector is effectively unused by this Secure Agent. . [optional]  # noqa: E501
            connection_uri (str): Overrides the default URI used to connect to this connector. This can be used to point the Secure Agent somewhere other than the default. . [optional]  # noqa: E501
            service_account_required (bool): If service_account_enabled field is set to true, a service account will be created. If service_account_enabled field is set to false, the service account will be deleted. If the service_account_enabled field is not set no action on the service account is taken. . [optional]  # noqa: E501
            local_authentication_enabled (bool): Determines whether or not the agent will expose an endpoint for local authentication. [optional]  # noqa: E501
            proxy_tunnel_termination (str): How a proxy tunnel is terminated.   - tcp: terminate the tunnel at a TCP socket   - inproc: terminate the tunnel at an inprocess socket Note: if not specified, the connector will choose, likely based on its version. . [optional]  # noqa: E501
            provisioning (AgentConnectorSpecProvisioning): [optional]  # noqa: E501
            routing (AgentConnectorCloudRouting): [optional]  # noqa: E501
            connector_cloud_routing (ConnectorCloudRouting): [optional]  # noqa: E501
            admin_status (AdminStatus): [optional]  # noqa: E501
            trap_disabled (bool): Inidicates whether traps (notifications) should be disabled for this entity. A true state indicates notifications will not be sent on transition. . [optional]  # noqa: E501
            revocation_proxy (CertificateRevocationProxy): [optional]  # noqa: E501
            egress_gateway (EgressGateway): [optional]  # noqa: E501
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
        self.org_id = org_id
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

