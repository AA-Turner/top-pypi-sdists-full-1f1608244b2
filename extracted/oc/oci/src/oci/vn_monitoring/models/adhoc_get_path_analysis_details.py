# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918

from .get_path_analysis_details import GetPathAnalysisDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AdhocGetPathAnalysisDetails(GetPathAnalysisDetails):
    """
    Defines the configuration for getting an ad-hoc path analysis.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AdhocGetPathAnalysisDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.vn_monitoring.models.AdhocGetPathAnalysisDetails.type` attribute
        of this class is ``ADHOC_QUERY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this AdhocGetPathAnalysisDetails.
            Allowed values for this property are: "PERSISTED_QUERY", "ADHOC_QUERY"
        :type type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AdhocGetPathAnalysisDetails.
        :type compartment_id: str

        :param protocol:
            The value to assign to the protocol property of this AdhocGetPathAnalysisDetails.
        :type protocol: int

        :param source_endpoint:
            The value to assign to the source_endpoint property of this AdhocGetPathAnalysisDetails.
        :type source_endpoint: oci.vn_monitoring.models.Endpoint

        :param destination_endpoint:
            The value to assign to the destination_endpoint property of this AdhocGetPathAnalysisDetails.
        :type destination_endpoint: oci.vn_monitoring.models.Endpoint

        :param protocol_parameters:
            The value to assign to the protocol_parameters property of this AdhocGetPathAnalysisDetails.
        :type protocol_parameters: oci.vn_monitoring.models.ProtocolParameters

        :param query_options:
            The value to assign to the query_options property of this AdhocGetPathAnalysisDetails.
        :type query_options: oci.vn_monitoring.models.QueryOptions

        """
        self.swagger_types = {
            'type': 'str',
            'compartment_id': 'str',
            'protocol': 'int',
            'source_endpoint': 'Endpoint',
            'destination_endpoint': 'Endpoint',
            'protocol_parameters': 'ProtocolParameters',
            'query_options': 'QueryOptions'
        }
        self.attribute_map = {
            'type': 'type',
            'compartment_id': 'compartmentId',
            'protocol': 'protocol',
            'source_endpoint': 'sourceEndpoint',
            'destination_endpoint': 'destinationEndpoint',
            'protocol_parameters': 'protocolParameters',
            'query_options': 'queryOptions'
        }
        self._type = None
        self._compartment_id = None
        self._protocol = None
        self._source_endpoint = None
        self._destination_endpoint = None
        self._protocol_parameters = None
        self._query_options = None
        self._type = 'ADHOC_QUERY'

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AdhocGetPathAnalysisDetails.
        The `OCID`__ for the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this AdhocGetPathAnalysisDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AdhocGetPathAnalysisDetails.
        The `OCID`__ for the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this AdhocGetPathAnalysisDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this AdhocGetPathAnalysisDetails.
        The IP protocol to used for the path analysis.


        :return: The protocol of this AdhocGetPathAnalysisDetails.
        :rtype: int
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this AdhocGetPathAnalysisDetails.
        The IP protocol to used for the path analysis.


        :param protocol: The protocol of this AdhocGetPathAnalysisDetails.
        :type: int
        """
        self._protocol = protocol

    @property
    def source_endpoint(self):
        """
        **[Required]** Gets the source_endpoint of this AdhocGetPathAnalysisDetails.

        :return: The source_endpoint of this AdhocGetPathAnalysisDetails.
        :rtype: oci.vn_monitoring.models.Endpoint
        """
        return self._source_endpoint

    @source_endpoint.setter
    def source_endpoint(self, source_endpoint):
        """
        Sets the source_endpoint of this AdhocGetPathAnalysisDetails.

        :param source_endpoint: The source_endpoint of this AdhocGetPathAnalysisDetails.
        :type: oci.vn_monitoring.models.Endpoint
        """
        self._source_endpoint = source_endpoint

    @property
    def destination_endpoint(self):
        """
        **[Required]** Gets the destination_endpoint of this AdhocGetPathAnalysisDetails.

        :return: The destination_endpoint of this AdhocGetPathAnalysisDetails.
        :rtype: oci.vn_monitoring.models.Endpoint
        """
        return self._destination_endpoint

    @destination_endpoint.setter
    def destination_endpoint(self, destination_endpoint):
        """
        Sets the destination_endpoint of this AdhocGetPathAnalysisDetails.

        :param destination_endpoint: The destination_endpoint of this AdhocGetPathAnalysisDetails.
        :type: oci.vn_monitoring.models.Endpoint
        """
        self._destination_endpoint = destination_endpoint

    @property
    def protocol_parameters(self):
        """
        Gets the protocol_parameters of this AdhocGetPathAnalysisDetails.

        :return: The protocol_parameters of this AdhocGetPathAnalysisDetails.
        :rtype: oci.vn_monitoring.models.ProtocolParameters
        """
        return self._protocol_parameters

    @protocol_parameters.setter
    def protocol_parameters(self, protocol_parameters):
        """
        Sets the protocol_parameters of this AdhocGetPathAnalysisDetails.

        :param protocol_parameters: The protocol_parameters of this AdhocGetPathAnalysisDetails.
        :type: oci.vn_monitoring.models.ProtocolParameters
        """
        self._protocol_parameters = protocol_parameters

    @property
    def query_options(self):
        """
        Gets the query_options of this AdhocGetPathAnalysisDetails.

        :return: The query_options of this AdhocGetPathAnalysisDetails.
        :rtype: oci.vn_monitoring.models.QueryOptions
        """
        return self._query_options

    @query_options.setter
    def query_options(self, query_options):
        """
        Sets the query_options of this AdhocGetPathAnalysisDetails.

        :param query_options: The query_options of this AdhocGetPathAnalysisDetails.
        :type: oci.vn_monitoring.models.QueryOptions
        """
        self._query_options = query_options

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
