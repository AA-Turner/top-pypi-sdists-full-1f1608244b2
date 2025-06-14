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


class OrmKernelResourceSpecEdges(object):
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
        'kernel_cluster': 'OrmKernelCluster',
        'llm_knowledge': 'list[OrmLLMKnowledge]',
        'llm_workflow': 'list[OrmLLMWorkflow]',
        'price_overrides': 'list[OrmPriceOverride]',
        'pricing_plans': 'list[OrmPricingPlan]',
        'run_specs': 'list[OrmRunSpec]'
    }

    attribute_map = {
        'kernel_cluster': 'kernel_cluster',
        'llm_knowledge': 'llm_knowledge',
        'llm_workflow': 'llm_workflow',
        'price_overrides': 'price_overrides',
        'pricing_plans': 'pricing_plans',
        'run_specs': 'run_specs'
    }

    def __init__(self, kernel_cluster=None, llm_knowledge=None, llm_workflow=None, price_overrides=None, pricing_plans=None, run_specs=None, local_vars_configuration=None):  # noqa: E501
        """OrmKernelResourceSpecEdges - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._kernel_cluster = None
        self._llm_knowledge = None
        self._llm_workflow = None
        self._price_overrides = None
        self._pricing_plans = None
        self._run_specs = None
        self.discriminator = None

        if kernel_cluster is not None:
            self.kernel_cluster = kernel_cluster
        if llm_knowledge is not None:
            self.llm_knowledge = llm_knowledge
        if llm_workflow is not None:
            self.llm_workflow = llm_workflow
        if price_overrides is not None:
            self.price_overrides = price_overrides
        if pricing_plans is not None:
            self.pricing_plans = pricing_plans
        if run_specs is not None:
            self.run_specs = run_specs

    @property
    def kernel_cluster(self):
        """Gets the kernel_cluster of this OrmKernelResourceSpecEdges.  # noqa: E501


        :return: The kernel_cluster of this OrmKernelResourceSpecEdges.  # noqa: E501
        :rtype: OrmKernelCluster
        """
        return self._kernel_cluster

    @kernel_cluster.setter
    def kernel_cluster(self, kernel_cluster):
        """Sets the kernel_cluster of this OrmKernelResourceSpecEdges.


        :param kernel_cluster: The kernel_cluster of this OrmKernelResourceSpecEdges.  # noqa: E501
        :type kernel_cluster: OrmKernelCluster
        """

        self._kernel_cluster = kernel_cluster

    @property
    def llm_knowledge(self):
        """Gets the llm_knowledge of this OrmKernelResourceSpecEdges.  # noqa: E501


        :return: The llm_knowledge of this OrmKernelResourceSpecEdges.  # noqa: E501
        :rtype: list[OrmLLMKnowledge]
        """
        return self._llm_knowledge

    @llm_knowledge.setter
    def llm_knowledge(self, llm_knowledge):
        """Sets the llm_knowledge of this OrmKernelResourceSpecEdges.


        :param llm_knowledge: The llm_knowledge of this OrmKernelResourceSpecEdges.  # noqa: E501
        :type llm_knowledge: list[OrmLLMKnowledge]
        """

        self._llm_knowledge = llm_knowledge

    @property
    def llm_workflow(self):
        """Gets the llm_workflow of this OrmKernelResourceSpecEdges.  # noqa: E501


        :return: The llm_workflow of this OrmKernelResourceSpecEdges.  # noqa: E501
        :rtype: list[OrmLLMWorkflow]
        """
        return self._llm_workflow

    @llm_workflow.setter
    def llm_workflow(self, llm_workflow):
        """Sets the llm_workflow of this OrmKernelResourceSpecEdges.


        :param llm_workflow: The llm_workflow of this OrmKernelResourceSpecEdges.  # noqa: E501
        :type llm_workflow: list[OrmLLMWorkflow]
        """

        self._llm_workflow = llm_workflow

    @property
    def price_overrides(self):
        """Gets the price_overrides of this OrmKernelResourceSpecEdges.  # noqa: E501


        :return: The price_overrides of this OrmKernelResourceSpecEdges.  # noqa: E501
        :rtype: list[OrmPriceOverride]
        """
        return self._price_overrides

    @price_overrides.setter
    def price_overrides(self, price_overrides):
        """Sets the price_overrides of this OrmKernelResourceSpecEdges.


        :param price_overrides: The price_overrides of this OrmKernelResourceSpecEdges.  # noqa: E501
        :type price_overrides: list[OrmPriceOverride]
        """

        self._price_overrides = price_overrides

    @property
    def pricing_plans(self):
        """Gets the pricing_plans of this OrmKernelResourceSpecEdges.  # noqa: E501


        :return: The pricing_plans of this OrmKernelResourceSpecEdges.  # noqa: E501
        :rtype: list[OrmPricingPlan]
        """
        return self._pricing_plans

    @pricing_plans.setter
    def pricing_plans(self, pricing_plans):
        """Sets the pricing_plans of this OrmKernelResourceSpecEdges.


        :param pricing_plans: The pricing_plans of this OrmKernelResourceSpecEdges.  # noqa: E501
        :type pricing_plans: list[OrmPricingPlan]
        """

        self._pricing_plans = pricing_plans

    @property
    def run_specs(self):
        """Gets the run_specs of this OrmKernelResourceSpecEdges.  # noqa: E501


        :return: The run_specs of this OrmKernelResourceSpecEdges.  # noqa: E501
        :rtype: list[OrmRunSpec]
        """
        return self._run_specs

    @run_specs.setter
    def run_specs(self, run_specs):
        """Sets the run_specs of this OrmKernelResourceSpecEdges.


        :param run_specs: The run_specs of this OrmKernelResourceSpecEdges.  # noqa: E501
        :type run_specs: list[OrmRunSpec]
        """

        self._run_specs = run_specs

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
        if not isinstance(other, OrmKernelResourceSpecEdges):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmKernelResourceSpecEdges):
            return True

        return self.to_dict() != other.to_dict()
