# coding: utf-8

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: support@akeyless.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from akeyless.configuration import Configuration


class TargetTypeDetailsInput(object):
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
        'artifactory_target_details': 'ArtifactoryTargetDetails',
        'aws_target_details': 'AWSTargetDetails',
        'azure_target_details': 'AzureTargetDetails',
        'chef_target_details': 'ChefTargetDetails',
        'custom_target_details': 'CustomTargetDetails',
        'db_target_details': 'DbTargetDetails',
        'dockerhub_target_details': 'DockerhubTargetDetails',
        'eks_target_details': 'EKSTargetDetails',
        'gcp_target_details': 'GcpTargetDetails',
        'github_target_details': 'GithubTargetDetails',
        'gitlab_target_details': 'GitlabTargetDetails',
        'gke_target_details': 'GKETargetDetails',
        'globalsign_atlas_target_details': 'GlobalSignAtlasTargetDetails',
        'globalsign_target_details': 'GlobalSignGCCTargetDetails',
        'godaddy_target_details': 'GodaddyTargetDetails',
        'hashi_vault_target_details': 'HashiVaultTargetDetails',
        'ldap_target_details': 'LdapTargetDetails',
        'linked_target_details': 'LinkedTargetDetails',
        'mongo_db_target_details': 'MongoDBTargetDetails',
        'native_k8s_target_details': 'NativeK8sTargetDetails',
        'ping_target_details': 'PingTargetDetails',
        'rabbit_mq_target_details': 'RabbitMQTargetDetails',
        'salesforce_target_details': 'SalesforceTargetDetails',
        'sectigo_target_details': 'SectigoTargetDetails',
        'ssh_target_details': 'SSHTargetDetails',
        'venafi_target_details': 'VenafiTargetDetails',
        'web_target_details': 'WebTargetDetails',
        'windows_target_details': 'WindowsTargetDetails',
        'zerossl_target_details': 'ZeroSSLTargetDetails'
    }

    attribute_map = {
        'artifactory_target_details': 'artifactory_target_details',
        'aws_target_details': 'aws_target_details',
        'azure_target_details': 'azure_target_details',
        'chef_target_details': 'chef_target_details',
        'custom_target_details': 'custom_target_details',
        'db_target_details': 'db_target_details',
        'dockerhub_target_details': 'dockerhub_target_details',
        'eks_target_details': 'eks_target_details',
        'gcp_target_details': 'gcp_target_details',
        'github_target_details': 'github_target_details',
        'gitlab_target_details': 'gitlab_target_details',
        'gke_target_details': 'gke_target_details',
        'globalsign_atlas_target_details': 'globalsign_atlas_target_details',
        'globalsign_target_details': 'globalsign_target_details',
        'godaddy_target_details': 'godaddy_target_details',
        'hashi_vault_target_details': 'hashi_vault_target_details',
        'ldap_target_details': 'ldap_target_details',
        'linked_target_details': 'linked_target_details',
        'mongo_db_target_details': 'mongo_db_target_details',
        'native_k8s_target_details': 'native_k8s_target_details',
        'ping_target_details': 'ping_target_details',
        'rabbit_mq_target_details': 'rabbit_mq_target_details',
        'salesforce_target_details': 'salesforce_target_details',
        'sectigo_target_details': 'sectigo_target_details',
        'ssh_target_details': 'ssh_target_details',
        'venafi_target_details': 'venafi_target_details',
        'web_target_details': 'web_target_details',
        'windows_target_details': 'windows_target_details',
        'zerossl_target_details': 'zerossl_target_details'
    }

    def __init__(self, artifactory_target_details=None, aws_target_details=None, azure_target_details=None, chef_target_details=None, custom_target_details=None, db_target_details=None, dockerhub_target_details=None, eks_target_details=None, gcp_target_details=None, github_target_details=None, gitlab_target_details=None, gke_target_details=None, globalsign_atlas_target_details=None, globalsign_target_details=None, godaddy_target_details=None, hashi_vault_target_details=None, ldap_target_details=None, linked_target_details=None, mongo_db_target_details=None, native_k8s_target_details=None, ping_target_details=None, rabbit_mq_target_details=None, salesforce_target_details=None, sectigo_target_details=None, ssh_target_details=None, venafi_target_details=None, web_target_details=None, windows_target_details=None, zerossl_target_details=None, local_vars_configuration=None):  # noqa: E501
        """TargetTypeDetailsInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._artifactory_target_details = None
        self._aws_target_details = None
        self._azure_target_details = None
        self._chef_target_details = None
        self._custom_target_details = None
        self._db_target_details = None
        self._dockerhub_target_details = None
        self._eks_target_details = None
        self._gcp_target_details = None
        self._github_target_details = None
        self._gitlab_target_details = None
        self._gke_target_details = None
        self._globalsign_atlas_target_details = None
        self._globalsign_target_details = None
        self._godaddy_target_details = None
        self._hashi_vault_target_details = None
        self._ldap_target_details = None
        self._linked_target_details = None
        self._mongo_db_target_details = None
        self._native_k8s_target_details = None
        self._ping_target_details = None
        self._rabbit_mq_target_details = None
        self._salesforce_target_details = None
        self._sectigo_target_details = None
        self._ssh_target_details = None
        self._venafi_target_details = None
        self._web_target_details = None
        self._windows_target_details = None
        self._zerossl_target_details = None
        self.discriminator = None

        if artifactory_target_details is not None:
            self.artifactory_target_details = artifactory_target_details
        if aws_target_details is not None:
            self.aws_target_details = aws_target_details
        if azure_target_details is not None:
            self.azure_target_details = azure_target_details
        if chef_target_details is not None:
            self.chef_target_details = chef_target_details
        if custom_target_details is not None:
            self.custom_target_details = custom_target_details
        if db_target_details is not None:
            self.db_target_details = db_target_details
        if dockerhub_target_details is not None:
            self.dockerhub_target_details = dockerhub_target_details
        if eks_target_details is not None:
            self.eks_target_details = eks_target_details
        if gcp_target_details is not None:
            self.gcp_target_details = gcp_target_details
        if github_target_details is not None:
            self.github_target_details = github_target_details
        if gitlab_target_details is not None:
            self.gitlab_target_details = gitlab_target_details
        if gke_target_details is not None:
            self.gke_target_details = gke_target_details
        if globalsign_atlas_target_details is not None:
            self.globalsign_atlas_target_details = globalsign_atlas_target_details
        if globalsign_target_details is not None:
            self.globalsign_target_details = globalsign_target_details
        if godaddy_target_details is not None:
            self.godaddy_target_details = godaddy_target_details
        if hashi_vault_target_details is not None:
            self.hashi_vault_target_details = hashi_vault_target_details
        if ldap_target_details is not None:
            self.ldap_target_details = ldap_target_details
        if linked_target_details is not None:
            self.linked_target_details = linked_target_details
        if mongo_db_target_details is not None:
            self.mongo_db_target_details = mongo_db_target_details
        if native_k8s_target_details is not None:
            self.native_k8s_target_details = native_k8s_target_details
        if ping_target_details is not None:
            self.ping_target_details = ping_target_details
        if rabbit_mq_target_details is not None:
            self.rabbit_mq_target_details = rabbit_mq_target_details
        if salesforce_target_details is not None:
            self.salesforce_target_details = salesforce_target_details
        if sectigo_target_details is not None:
            self.sectigo_target_details = sectigo_target_details
        if ssh_target_details is not None:
            self.ssh_target_details = ssh_target_details
        if venafi_target_details is not None:
            self.venafi_target_details = venafi_target_details
        if web_target_details is not None:
            self.web_target_details = web_target_details
        if windows_target_details is not None:
            self.windows_target_details = windows_target_details
        if zerossl_target_details is not None:
            self.zerossl_target_details = zerossl_target_details

    @property
    def artifactory_target_details(self):
        """Gets the artifactory_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The artifactory_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: ArtifactoryTargetDetails
        """
        return self._artifactory_target_details

    @artifactory_target_details.setter
    def artifactory_target_details(self, artifactory_target_details):
        """Sets the artifactory_target_details of this TargetTypeDetailsInput.


        :param artifactory_target_details: The artifactory_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: ArtifactoryTargetDetails
        """

        self._artifactory_target_details = artifactory_target_details

    @property
    def aws_target_details(self):
        """Gets the aws_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The aws_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: AWSTargetDetails
        """
        return self._aws_target_details

    @aws_target_details.setter
    def aws_target_details(self, aws_target_details):
        """Sets the aws_target_details of this TargetTypeDetailsInput.


        :param aws_target_details: The aws_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: AWSTargetDetails
        """

        self._aws_target_details = aws_target_details

    @property
    def azure_target_details(self):
        """Gets the azure_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The azure_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: AzureTargetDetails
        """
        return self._azure_target_details

    @azure_target_details.setter
    def azure_target_details(self, azure_target_details):
        """Sets the azure_target_details of this TargetTypeDetailsInput.


        :param azure_target_details: The azure_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: AzureTargetDetails
        """

        self._azure_target_details = azure_target_details

    @property
    def chef_target_details(self):
        """Gets the chef_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The chef_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: ChefTargetDetails
        """
        return self._chef_target_details

    @chef_target_details.setter
    def chef_target_details(self, chef_target_details):
        """Sets the chef_target_details of this TargetTypeDetailsInput.


        :param chef_target_details: The chef_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: ChefTargetDetails
        """

        self._chef_target_details = chef_target_details

    @property
    def custom_target_details(self):
        """Gets the custom_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The custom_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: CustomTargetDetails
        """
        return self._custom_target_details

    @custom_target_details.setter
    def custom_target_details(self, custom_target_details):
        """Sets the custom_target_details of this TargetTypeDetailsInput.


        :param custom_target_details: The custom_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: CustomTargetDetails
        """

        self._custom_target_details = custom_target_details

    @property
    def db_target_details(self):
        """Gets the db_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The db_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: DbTargetDetails
        """
        return self._db_target_details

    @db_target_details.setter
    def db_target_details(self, db_target_details):
        """Sets the db_target_details of this TargetTypeDetailsInput.


        :param db_target_details: The db_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: DbTargetDetails
        """

        self._db_target_details = db_target_details

    @property
    def dockerhub_target_details(self):
        """Gets the dockerhub_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The dockerhub_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: DockerhubTargetDetails
        """
        return self._dockerhub_target_details

    @dockerhub_target_details.setter
    def dockerhub_target_details(self, dockerhub_target_details):
        """Sets the dockerhub_target_details of this TargetTypeDetailsInput.


        :param dockerhub_target_details: The dockerhub_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: DockerhubTargetDetails
        """

        self._dockerhub_target_details = dockerhub_target_details

    @property
    def eks_target_details(self):
        """Gets the eks_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The eks_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: EKSTargetDetails
        """
        return self._eks_target_details

    @eks_target_details.setter
    def eks_target_details(self, eks_target_details):
        """Sets the eks_target_details of this TargetTypeDetailsInput.


        :param eks_target_details: The eks_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: EKSTargetDetails
        """

        self._eks_target_details = eks_target_details

    @property
    def gcp_target_details(self):
        """Gets the gcp_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The gcp_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: GcpTargetDetails
        """
        return self._gcp_target_details

    @gcp_target_details.setter
    def gcp_target_details(self, gcp_target_details):
        """Sets the gcp_target_details of this TargetTypeDetailsInput.


        :param gcp_target_details: The gcp_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: GcpTargetDetails
        """

        self._gcp_target_details = gcp_target_details

    @property
    def github_target_details(self):
        """Gets the github_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The github_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: GithubTargetDetails
        """
        return self._github_target_details

    @github_target_details.setter
    def github_target_details(self, github_target_details):
        """Sets the github_target_details of this TargetTypeDetailsInput.


        :param github_target_details: The github_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: GithubTargetDetails
        """

        self._github_target_details = github_target_details

    @property
    def gitlab_target_details(self):
        """Gets the gitlab_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The gitlab_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: GitlabTargetDetails
        """
        return self._gitlab_target_details

    @gitlab_target_details.setter
    def gitlab_target_details(self, gitlab_target_details):
        """Sets the gitlab_target_details of this TargetTypeDetailsInput.


        :param gitlab_target_details: The gitlab_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: GitlabTargetDetails
        """

        self._gitlab_target_details = gitlab_target_details

    @property
    def gke_target_details(self):
        """Gets the gke_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The gke_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: GKETargetDetails
        """
        return self._gke_target_details

    @gke_target_details.setter
    def gke_target_details(self, gke_target_details):
        """Sets the gke_target_details of this TargetTypeDetailsInput.


        :param gke_target_details: The gke_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: GKETargetDetails
        """

        self._gke_target_details = gke_target_details

    @property
    def globalsign_atlas_target_details(self):
        """Gets the globalsign_atlas_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The globalsign_atlas_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: GlobalSignAtlasTargetDetails
        """
        return self._globalsign_atlas_target_details

    @globalsign_atlas_target_details.setter
    def globalsign_atlas_target_details(self, globalsign_atlas_target_details):
        """Sets the globalsign_atlas_target_details of this TargetTypeDetailsInput.


        :param globalsign_atlas_target_details: The globalsign_atlas_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: GlobalSignAtlasTargetDetails
        """

        self._globalsign_atlas_target_details = globalsign_atlas_target_details

    @property
    def globalsign_target_details(self):
        """Gets the globalsign_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The globalsign_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: GlobalSignGCCTargetDetails
        """
        return self._globalsign_target_details

    @globalsign_target_details.setter
    def globalsign_target_details(self, globalsign_target_details):
        """Sets the globalsign_target_details of this TargetTypeDetailsInput.


        :param globalsign_target_details: The globalsign_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: GlobalSignGCCTargetDetails
        """

        self._globalsign_target_details = globalsign_target_details

    @property
    def godaddy_target_details(self):
        """Gets the godaddy_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The godaddy_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: GodaddyTargetDetails
        """
        return self._godaddy_target_details

    @godaddy_target_details.setter
    def godaddy_target_details(self, godaddy_target_details):
        """Sets the godaddy_target_details of this TargetTypeDetailsInput.


        :param godaddy_target_details: The godaddy_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: GodaddyTargetDetails
        """

        self._godaddy_target_details = godaddy_target_details

    @property
    def hashi_vault_target_details(self):
        """Gets the hashi_vault_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The hashi_vault_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: HashiVaultTargetDetails
        """
        return self._hashi_vault_target_details

    @hashi_vault_target_details.setter
    def hashi_vault_target_details(self, hashi_vault_target_details):
        """Sets the hashi_vault_target_details of this TargetTypeDetailsInput.


        :param hashi_vault_target_details: The hashi_vault_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: HashiVaultTargetDetails
        """

        self._hashi_vault_target_details = hashi_vault_target_details

    @property
    def ldap_target_details(self):
        """Gets the ldap_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The ldap_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: LdapTargetDetails
        """
        return self._ldap_target_details

    @ldap_target_details.setter
    def ldap_target_details(self, ldap_target_details):
        """Sets the ldap_target_details of this TargetTypeDetailsInput.


        :param ldap_target_details: The ldap_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: LdapTargetDetails
        """

        self._ldap_target_details = ldap_target_details

    @property
    def linked_target_details(self):
        """Gets the linked_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The linked_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: LinkedTargetDetails
        """
        return self._linked_target_details

    @linked_target_details.setter
    def linked_target_details(self, linked_target_details):
        """Sets the linked_target_details of this TargetTypeDetailsInput.


        :param linked_target_details: The linked_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: LinkedTargetDetails
        """

        self._linked_target_details = linked_target_details

    @property
    def mongo_db_target_details(self):
        """Gets the mongo_db_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The mongo_db_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: MongoDBTargetDetails
        """
        return self._mongo_db_target_details

    @mongo_db_target_details.setter
    def mongo_db_target_details(self, mongo_db_target_details):
        """Sets the mongo_db_target_details of this TargetTypeDetailsInput.


        :param mongo_db_target_details: The mongo_db_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: MongoDBTargetDetails
        """

        self._mongo_db_target_details = mongo_db_target_details

    @property
    def native_k8s_target_details(self):
        """Gets the native_k8s_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The native_k8s_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: NativeK8sTargetDetails
        """
        return self._native_k8s_target_details

    @native_k8s_target_details.setter
    def native_k8s_target_details(self, native_k8s_target_details):
        """Sets the native_k8s_target_details of this TargetTypeDetailsInput.


        :param native_k8s_target_details: The native_k8s_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: NativeK8sTargetDetails
        """

        self._native_k8s_target_details = native_k8s_target_details

    @property
    def ping_target_details(self):
        """Gets the ping_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The ping_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: PingTargetDetails
        """
        return self._ping_target_details

    @ping_target_details.setter
    def ping_target_details(self, ping_target_details):
        """Sets the ping_target_details of this TargetTypeDetailsInput.


        :param ping_target_details: The ping_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: PingTargetDetails
        """

        self._ping_target_details = ping_target_details

    @property
    def rabbit_mq_target_details(self):
        """Gets the rabbit_mq_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The rabbit_mq_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: RabbitMQTargetDetails
        """
        return self._rabbit_mq_target_details

    @rabbit_mq_target_details.setter
    def rabbit_mq_target_details(self, rabbit_mq_target_details):
        """Sets the rabbit_mq_target_details of this TargetTypeDetailsInput.


        :param rabbit_mq_target_details: The rabbit_mq_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: RabbitMQTargetDetails
        """

        self._rabbit_mq_target_details = rabbit_mq_target_details

    @property
    def salesforce_target_details(self):
        """Gets the salesforce_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The salesforce_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: SalesforceTargetDetails
        """
        return self._salesforce_target_details

    @salesforce_target_details.setter
    def salesforce_target_details(self, salesforce_target_details):
        """Sets the salesforce_target_details of this TargetTypeDetailsInput.


        :param salesforce_target_details: The salesforce_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: SalesforceTargetDetails
        """

        self._salesforce_target_details = salesforce_target_details

    @property
    def sectigo_target_details(self):
        """Gets the sectigo_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The sectigo_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: SectigoTargetDetails
        """
        return self._sectigo_target_details

    @sectigo_target_details.setter
    def sectigo_target_details(self, sectigo_target_details):
        """Sets the sectigo_target_details of this TargetTypeDetailsInput.


        :param sectigo_target_details: The sectigo_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: SectigoTargetDetails
        """

        self._sectigo_target_details = sectigo_target_details

    @property
    def ssh_target_details(self):
        """Gets the ssh_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The ssh_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: SSHTargetDetails
        """
        return self._ssh_target_details

    @ssh_target_details.setter
    def ssh_target_details(self, ssh_target_details):
        """Sets the ssh_target_details of this TargetTypeDetailsInput.


        :param ssh_target_details: The ssh_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: SSHTargetDetails
        """

        self._ssh_target_details = ssh_target_details

    @property
    def venafi_target_details(self):
        """Gets the venafi_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The venafi_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: VenafiTargetDetails
        """
        return self._venafi_target_details

    @venafi_target_details.setter
    def venafi_target_details(self, venafi_target_details):
        """Sets the venafi_target_details of this TargetTypeDetailsInput.


        :param venafi_target_details: The venafi_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: VenafiTargetDetails
        """

        self._venafi_target_details = venafi_target_details

    @property
    def web_target_details(self):
        """Gets the web_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The web_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: WebTargetDetails
        """
        return self._web_target_details

    @web_target_details.setter
    def web_target_details(self, web_target_details):
        """Sets the web_target_details of this TargetTypeDetailsInput.


        :param web_target_details: The web_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: WebTargetDetails
        """

        self._web_target_details = web_target_details

    @property
    def windows_target_details(self):
        """Gets the windows_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The windows_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: WindowsTargetDetails
        """
        return self._windows_target_details

    @windows_target_details.setter
    def windows_target_details(self, windows_target_details):
        """Sets the windows_target_details of this TargetTypeDetailsInput.


        :param windows_target_details: The windows_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: WindowsTargetDetails
        """

        self._windows_target_details = windows_target_details

    @property
    def zerossl_target_details(self):
        """Gets the zerossl_target_details of this TargetTypeDetailsInput.  # noqa: E501


        :return: The zerossl_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :rtype: ZeroSSLTargetDetails
        """
        return self._zerossl_target_details

    @zerossl_target_details.setter
    def zerossl_target_details(self, zerossl_target_details):
        """Sets the zerossl_target_details of this TargetTypeDetailsInput.


        :param zerossl_target_details: The zerossl_target_details of this TargetTypeDetailsInput.  # noqa: E501
        :type: ZeroSSLTargetDetails
        """

        self._zerossl_target_details = zerossl_target_details

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TargetTypeDetailsInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TargetTypeDetailsInput):
            return True

        return self.to_dict() != other.to_dict()
