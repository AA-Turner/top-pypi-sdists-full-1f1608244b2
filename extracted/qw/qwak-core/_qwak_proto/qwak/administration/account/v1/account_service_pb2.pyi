"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import qwak.administration.account.v1.account_pb2
import qwak.administration.account.v1.jfrog_tenant_details_pb2
import qwak.administration.account.v1.preferences_pb2
import qwak.administration.account.v1.terms_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class CreateAccountRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCOUNT_NAME_FIELD_NUMBER: builtins.int
    PREFERENCES_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    TIER_FIELD_NUMBER: builtins.int
    JFROG_TENANT_SPEC_FIELD_NUMBER: builtins.int
    account_name: builtins.str
    """Account name to be created - usually, it will be a name of the company that purchased Qwak"""
    @property
    def preferences(self) -> qwak.administration.account.v1.preferences_pb2.AccountPreferences:
        """The preferences for the account"""
    type: qwak.administration.account.v1.account_pb2.AccountType.ValueType
    """The type of the account"""
    tier: qwak.administration.account.v1.account_pb2.AccountTier.ValueType
    """The tier of the account"""
    @property
    def jfrog_tenant_spec(self) -> qwak.administration.account.v1.jfrog_tenant_details_pb2.JfrogTenantSpec:
        """The JFrog tenant spec"""
    def __init__(
        self,
        *,
        account_name: builtins.str = ...,
        preferences: qwak.administration.account.v1.preferences_pb2.AccountPreferences | None = ...,
        type: qwak.administration.account.v1.account_pb2.AccountType.ValueType = ...,
        tier: qwak.administration.account.v1.account_pb2.AccountTier.ValueType = ...,
        jfrog_tenant_spec: qwak.administration.account.v1.jfrog_tenant_details_pb2.JfrogTenantSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["jfrog_tenant_spec", b"jfrog_tenant_spec", "preferences", b"preferences"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["account_name", b"account_name", "jfrog_tenant_spec", b"jfrog_tenant_spec", "preferences", b"preferences", "tier", b"tier", "type", b"type"]) -> None: ...

global___CreateAccountRequest = CreateAccountRequest

class CreateAccountResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCOUNT_FIELD_NUMBER: builtins.int
    @property
    def account(self) -> qwak.administration.account.v1.account_pb2.Account:
        """Created account"""
    def __init__(
        self,
        *,
        account: qwak.administration.account.v1.account_pb2.Account | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["account", b"account"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["account", b"account"]) -> None: ...

global___CreateAccountResponse = CreateAccountResponse

class GetAccountRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCOUNT_ID_FIELD_NUMBER: builtins.int
    account_id: builtins.str
    """Account ID to fetch"""
    def __init__(
        self,
        *,
        account_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["account_id", b"account_id"]) -> None: ...

global___GetAccountRequest = GetAccountRequest

class GetAccountResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCOUNT_FIELD_NUMBER: builtins.int
    @property
    def account(self) -> qwak.administration.account.v1.account_pb2.Account:
        """Fetched account by the requested ID"""
    def __init__(
        self,
        *,
        account: qwak.administration.account.v1.account_pb2.Account | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["account", b"account"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["account", b"account"]) -> None: ...

global___GetAccountResponse = GetAccountResponse

class ListAccountsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILTER_FIELD_NUMBER: builtins.int
    @property
    def filter(self) -> qwak.administration.account.v1.account_pb2.ListAccountFilter:
        """Filter to filter account list"""
    def __init__(
        self,
        *,
        filter: qwak.administration.account.v1.account_pb2.ListAccountFilter | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["filter", b"filter"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter", b"filter"]) -> None: ...

global___ListAccountsRequest = ListAccountsRequest

class ListAccountsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCOUNTS_FIELD_NUMBER: builtins.int
    @property
    def accounts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[qwak.administration.account.v1.account_pb2.Account]:
        """All accounts that matched the provided filter"""
    def __init__(
        self,
        *,
        accounts: collections.abc.Iterable[qwak.administration.account.v1.account_pb2.Account] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["accounts", b"accounts"]) -> None: ...

global___ListAccountsResponse = ListAccountsResponse

class UpdateAccountRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCOUNT_ID_FIELD_NUMBER: builtins.int
    PREFERENCES_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    TIER_FIELD_NUMBER: builtins.int
    ACCEPTED_TERMS_FIELD_NUMBER: builtins.int
    JFROG_TENANT_SPEC_FIELD_NUMBER: builtins.int
    account_id: builtins.str
    """The account id to update"""
    @property
    def preferences(self) -> qwak.administration.account.v1.preferences_pb2.AccountPreferences:
        """The preferences for the account"""
    type: qwak.administration.account.v1.account_pb2.AccountType.ValueType
    """The type of the account"""
    tier: qwak.administration.account.v1.account_pb2.AccountTier.ValueType
    """The tier of the account"""
    @property
    def accepted_terms(self) -> qwak.administration.account.v1.terms_pb2.AccountAcceptedTerms:
        """The accepted terms of the account"""
    @property
    def jfrog_tenant_spec(self) -> qwak.administration.account.v1.jfrog_tenant_details_pb2.JfrogTenantSpec:
        """The JFrog tenant spec"""
    def __init__(
        self,
        *,
        account_id: builtins.str = ...,
        preferences: qwak.administration.account.v1.preferences_pb2.AccountPreferences | None = ...,
        type: qwak.administration.account.v1.account_pb2.AccountType.ValueType = ...,
        tier: qwak.administration.account.v1.account_pb2.AccountTier.ValueType = ...,
        accepted_terms: qwak.administration.account.v1.terms_pb2.AccountAcceptedTerms | None = ...,
        jfrog_tenant_spec: qwak.administration.account.v1.jfrog_tenant_details_pb2.JfrogTenantSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["accepted_terms", b"accepted_terms", "jfrog_tenant_spec", b"jfrog_tenant_spec", "preferences", b"preferences"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["accepted_terms", b"accepted_terms", "account_id", b"account_id", "jfrog_tenant_spec", b"jfrog_tenant_spec", "preferences", b"preferences", "tier", b"tier", "type", b"type"]) -> None: ...

global___UpdateAccountRequest = UpdateAccountRequest

class UpdateAccountResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___UpdateAccountResponse = UpdateAccountResponse

class UpdateAccountPreferencesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCOUNT_ID_FIELD_NUMBER: builtins.int
    PREFERENCES_FIELD_NUMBER: builtins.int
    account_id: builtins.str
    """The account id to update"""
    @property
    def preferences(self) -> qwak.administration.account.v1.preferences_pb2.AccountPreferences:
        """New account preferences"""
    def __init__(
        self,
        *,
        account_id: builtins.str = ...,
        preferences: qwak.administration.account.v1.preferences_pb2.AccountPreferences | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["preferences", b"preferences"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["account_id", b"account_id", "preferences", b"preferences"]) -> None: ...

global___UpdateAccountPreferencesRequest = UpdateAccountPreferencesRequest

class UpdateAccountPreferencesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___UpdateAccountPreferencesResponse = UpdateAccountPreferencesResponse

class UpdateAccountAcceptedTermsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCOUNT_ID_FIELD_NUMBER: builtins.int
    ACCEPTED_TERMS_FIELD_NUMBER: builtins.int
    account_id: builtins.str
    """The account id to update"""
    @property
    def accepted_terms(self) -> qwak.administration.account.v1.terms_pb2.AccountAcceptedTerms:
        """The accepted terms of the account"""
    def __init__(
        self,
        *,
        account_id: builtins.str = ...,
        accepted_terms: qwak.administration.account.v1.terms_pb2.AccountAcceptedTerms | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["accepted_terms", b"accepted_terms"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["accepted_terms", b"accepted_terms", "account_id", b"account_id"]) -> None: ...

global___UpdateAccountAcceptedTermsRequest = UpdateAccountAcceptedTermsRequest

class UpdateAccountAcceptedTermsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___UpdateAccountAcceptedTermsResponse = UpdateAccountAcceptedTermsResponse

class AddAutoBindingRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCOUNT_ID_FIELD_NUMBER: builtins.int
    AUTO_BINDING_ACCOUNT_FIELD_NUMBER: builtins.int
    account_id: builtins.str
    """Account id to bound"""
    @property
    def auto_binding_account(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[qwak.administration.account.v1.account_pb2.AutoBindingRule]:
        """Rules"""
    def __init__(
        self,
        *,
        account_id: builtins.str = ...,
        auto_binding_account: collections.abc.Iterable[qwak.administration.account.v1.account_pb2.AutoBindingRule] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["account_id", b"account_id", "auto_binding_account", b"auto_binding_account"]) -> None: ...

global___AddAutoBindingRequest = AddAutoBindingRequest

class AddAutoBindingResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUTO_BINDING_ACCOUNT_FIELD_NUMBER: builtins.int
    @property
    def auto_binding_account(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[qwak.administration.account.v1.account_pb2.AutoBindingAccount]: ...
    def __init__(
        self,
        *,
        auto_binding_account: collections.abc.Iterable[qwak.administration.account.v1.account_pb2.AutoBindingAccount] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["auto_binding_account", b"auto_binding_account"]) -> None: ...

global___AddAutoBindingResponse = AddAutoBindingResponse

class RemoveAutoBindingRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCOUNT_ID_FIELD_NUMBER: builtins.int
    AUTO_BINDING_ID_TO_REMOVE_FIELD_NUMBER: builtins.int
    account_id: builtins.str
    """Account id to remove binding for"""
    @property
    def auto_binding_id_to_remove(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Id list of auto bindings to remove"""
    def __init__(
        self,
        *,
        account_id: builtins.str = ...,
        auto_binding_id_to_remove: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["account_id", b"account_id", "auto_binding_id_to_remove", b"auto_binding_id_to_remove"]) -> None: ...

global___RemoveAutoBindingRequest = RemoveAutoBindingRequest

class RemoveAutoBindingResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___RemoveAutoBindingResponse = RemoveAutoBindingResponse

class GetAccountBriefRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCOUNT_ID_FIELD_NUMBER: builtins.int
    JFROG_TENANT_ID_FIELD_NUMBER: builtins.int
    account_id: builtins.str
    jfrog_tenant_id: builtins.str
    """The JFrog tenant id could be jpd_id for self-hosted"""
    def __init__(
        self,
        *,
        account_id: builtins.str = ...,
        jfrog_tenant_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["account_id", b"account_id", "account_identifier", b"account_identifier", "jfrog_tenant_id", b"jfrog_tenant_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["account_id", b"account_id", "account_identifier", b"account_identifier", "jfrog_tenant_id", b"jfrog_tenant_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["account_identifier", b"account_identifier"]) -> typing_extensions.Literal["account_id", "jfrog_tenant_id"] | None: ...

global___GetAccountBriefRequest = GetAccountBriefRequest

class GetAccountBriefResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCOUNT_BRIEF_FIELD_NUMBER: builtins.int
    @property
    def account_brief(self) -> qwak.administration.account.v1.account_pb2.AccountBrief: ...
    def __init__(
        self,
        *,
        account_brief: qwak.administration.account.v1.account_pb2.AccountBrief | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["account_brief", b"account_brief"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["account_brief", b"account_brief"]) -> None: ...

global___GetAccountBriefResponse = GetAccountBriefResponse
