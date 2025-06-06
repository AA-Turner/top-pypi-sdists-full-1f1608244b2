# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AttackStrategy(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Strategies for attacks."""

    EASY = "easy"
    """Represents a default set of easy complexity attacks. Easy complexity attack strategies are
    defined as attacks that do not require any Large Language Model to convert or orchestrate."""
    ASCII_ART = "ascii_art"
    """Represents ASCII art, a graphic design technique that uses printable characters."""
    ASCII_SMUGGLER = "ascii_smuggler"
    """Represents ASCII smuggling, a technique for encoding or hiding data."""
    ATBASH = "atbash"
    """Represents the Atbash cipher, a substitution cipher that reverses the alphabet."""
    BASE64 = "base64"
    """Represents Base64 encoding, a method for encoding binary data as text."""
    BINARY = "binary"
    """Represents binary encoding, a representation of data in binary format."""
    CAESAR = "caesar"
    """Represents the Caesar cipher, a substitution cipher that shifts characters."""
    CHARACTER_SPACE = "character_space"
    """Represents character space manipulation, a technique involving spacing between characters."""
    JAILBREAK = "jailbreak"
    """Represents character swapping, a technique for rearranging characters in text."""


class ConnectionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The Type (or category) of the connection."""

    AZURE_OPEN_AI = "AzureOpenAI"
    """Azure OpenAI Service"""
    AZURE_BLOB_STORAGE = "AzureBlob"
    """Azure Blob Storage, with specified container"""
    AZURE_STORAGE_ACCOUNT = "AzureStorageAccount"
    """Azure Blob Storage, with container not specified (used by Assistants)"""
    AZURE_AI_SEARCH = "CognitiveSearch"
    """Azure AI Search"""
    COSMOS_DB = "CosmosDB"
    """CosmosDB"""
    API_KEY = "ApiKey"
    """Generic connection that uses API Key authentication"""
    APPLICATION_CONFIGURATION = "AppConfig"
    """Application Configuration"""
    APPLICATION_INSIGHTS = "AppInsights"
    """Application Insights"""
    CUSTOM = "CustomKeys"
    """Custom Keys"""


class CredentialType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The credential type used by the connection."""

    API_KEY = "ApiKey"
    """API Key credential"""
    ENTRA_ID = "AAD"
    """Entra ID credential (formerly known as AAD)"""
    SAS = "SAS"
    """Shared Access Signature (SAS) credential"""
    CUSTOM = "CustomKeys"
    """Custom credential"""
    NONE = "None"
    """No credential"""


class DatasetType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum to determine the type of data."""

    URI_FILE = "uri_file"
    """URI file."""
    URI_FOLDER = "uri_folder"
    """URI folder."""


class DeploymentType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of DeploymentType."""

    MODEL_DEPLOYMENT = "ModelDeployment"
    """Model deployment"""


class IndexType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of IndexType."""

    AZURE_SEARCH = "AzureSearch"
    """Azure search"""
    COSMOS_DB = "CosmosDBNoSqlVectorStore"
    """CosmosDB"""
    MANAGED_AZURE_SEARCH = "ManagedAzureSearch"
    """Managed Azure Search"""


class ListViewType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """List View Type Definition."""

    ACTIVE_ONLY = "ActiveOnly"
    """List only active items."""
    ARCHIVED_ONLY = "ArchivedOnly"
    """List only archived items."""
    ALL = "All"
    """List all items."""


class PendingUploadType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of pending upload."""

    NONE = "None"
    """No pending upload."""
    TEMPORARY_BLOB_REFERENCE = "TemporaryBlobReference"
    """Temporary Blob Reference is the only supported type."""


class ResultType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of Evaluation result."""

    BENCHMARK = "Benchmark"
    """Benchmark result"""
    EVALUATION = "Evaluation"
    """Evaluations Result"""
    REDTEAM = "Redteam"
    """Red Team Result"""
    SIMULATION = "Simulation"
    """Simulation Result"""


class RiskCategory(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Risk category for the attack objective."""

    HATE_UNFAIRNESS = "HateUnfairness"
    """Represents content related to hate or unfairness."""
    VIOLENCE = "Violence"
    """Represents content related to violence."""
    SEXUAL = "Sexual"
    """Represents content of a sexual nature."""
    SELF_HARM = "SelfHarm"
    """Represents content related to self-harm."""
    PROTECTED_MATERIAL = "ProtectedMaterial"
    """Represents content involving protected material."""
    CODE_VULNERABILITY = "CodeVulnerability"
    """Represents content related to code vulnerabilities."""
    UNGROUNDED_ATTRIBUTES = "UngroundedAttributes"
    """Represents content with ungrounded attributes."""


class SimulationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Simulation type."""

    DEFAULT = "Default"
    """Default simulation type."""
    CUSTOM_PERSONA = "CustomPersona"
    """Custom persona simulation type."""
    HARM_TURN_GENERATOR = "HarmTurnGenerator"
    """Harm turn generator simulation type."""
