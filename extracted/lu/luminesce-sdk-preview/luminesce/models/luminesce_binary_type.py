# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.16.765
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

from luminesce.configuration import Configuration


class LuminesceBinaryType(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    COMMANDLINETOOL = "CommandLineTool"
    LOCALFILESYSTEM_PROVIDERS = "LocalFileSystem_Providers"
    EMAIL_PROVIDERS = "Email_Providers"
    PYTHON_PROVIDERS = "Python_Providers"
    AWSS3_PROVIDERS = "AwsS3_Providers"
    AZURE_PROVIDERS = "Azure_Providers"
    SQLDB_PROVIDERS_DB2LINUX = "SqlDb_Providers_Db2Linux"
    SQLDB_PROVIDERS_MYSQL = "SqlDb_Providers_MySql"
    SQLDB_PROVIDERS_ORACLE = "SqlDb_Providers_Oracle"
    SQLDB_PROVIDERS_ORACLE_SNOWFLAKE = "SqlDb_Providers_Oracle_Snowflake"
    SQLDB_PROVIDERS_POSTGRESQL = "SqlDb_Providers_Postgresql"
    SQLDB_PROVIDERS_SNOWFLAKE = "SqlDb_Providers_Snowflake"
    SQLDB_PROVIDERS_SQLSERVER = "SqlDb_Providers_SqlServer"
    SQLDB_PROVIDERS_SYBASEASE = "SqlDb_Providers_SybaseAse"
    SQLDB_PROVIDERS_SQLITE = "SqlDb_Providers_SqLite"
    SQLDB_PROVIDERS_DUCKDB = "SqlDb_Providers_DuckDb"
    SQLDB_PROVIDERS_AWSDYNAMODB = "SqlDb_Providers_AwsDynamoDb"
    SQLDB_PROVIDERS_SQLSERVER_ORACLE = "SqlDb_Providers_SqlServer_Oracle"
    JDBC_DRIVER = "Jdbc_Driver"
    POWERBI_CONNECTOR = "PowerBi_Connector"
    ODBC_WIN64_DRIVER = "Odbc_Win64_Driver"

    allowable_values = [COMMANDLINETOOL, LOCALFILESYSTEM_PROVIDERS, EMAIL_PROVIDERS, PYTHON_PROVIDERS, AWSS3_PROVIDERS, AZURE_PROVIDERS, SQLDB_PROVIDERS_DB2LINUX, SQLDB_PROVIDERS_MYSQL, SQLDB_PROVIDERS_ORACLE, SQLDB_PROVIDERS_ORACLE_SNOWFLAKE, SQLDB_PROVIDERS_POSTGRESQL, SQLDB_PROVIDERS_SNOWFLAKE, SQLDB_PROVIDERS_SQLSERVER, SQLDB_PROVIDERS_SYBASEASE, SQLDB_PROVIDERS_SQLITE, SQLDB_PROVIDERS_DUCKDB, SQLDB_PROVIDERS_AWSDYNAMODB, SQLDB_PROVIDERS_SQLSERVER_ORACLE, JDBC_DRIVER, POWERBI_CONNECTOR, ODBC_WIN64_DRIVER]  # noqa: E501

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
    }

    attribute_map = {
    }

    required_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """LuminesceBinaryType - a model defined in OpenAPI"
        

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

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
        if not isinstance(other, LuminesceBinaryType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LuminesceBinaryType):
            return True

        return self.to_dict() != other.to_dict()
