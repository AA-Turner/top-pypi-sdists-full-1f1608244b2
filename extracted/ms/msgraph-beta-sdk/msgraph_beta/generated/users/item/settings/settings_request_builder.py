from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ....models.o_data_errors.o_data_error import ODataError
    from ....models.user_settings import UserSettings
    from .contact_merge_suggestions.contact_merge_suggestions_request_builder import ContactMergeSuggestionsRequestBuilder
    from .exchange.exchange_request_builder import ExchangeRequestBuilder
    from .item_insights.item_insights_request_builder import ItemInsightsRequestBuilder
    from .regional_and_language_settings.regional_and_language_settings_request_builder import RegionalAndLanguageSettingsRequestBuilder
    from .shift_preferences.shift_preferences_request_builder import ShiftPreferencesRequestBuilder
    from .storage.storage_request_builder import StorageRequestBuilder
    from .windows.windows_request_builder import WindowsRequestBuilder

class SettingsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the settings property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SettingsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/settings{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property settings for users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[SettingsRequestBuilderGetQueryParameters]] = None) -> Optional[UserSettings]:
        """
        Get settings from users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UserSettings]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.user_settings import UserSettings

        return await self.request_adapter.send_async(request_info, UserSettings, error_mapping)
    
    async def patch(self,body: UserSettings, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[UserSettings]:
        """
        Update the navigation property settings in users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UserSettings]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.user_settings import UserSettings

        return await self.request_adapter.send_async(request_info, UserSettings, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property settings for users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SettingsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get settings from users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: UserSettings, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property settings in users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> SettingsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SettingsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SettingsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def contact_merge_suggestions(self) -> ContactMergeSuggestionsRequestBuilder:
        """
        Provides operations to manage the contactMergeSuggestions property of the microsoft.graph.userSettings entity.
        """
        from .contact_merge_suggestions.contact_merge_suggestions_request_builder import ContactMergeSuggestionsRequestBuilder

        return ContactMergeSuggestionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exchange(self) -> ExchangeRequestBuilder:
        """
        Provides operations to manage the exchange property of the microsoft.graph.userSettings entity.
        """
        from .exchange.exchange_request_builder import ExchangeRequestBuilder

        return ExchangeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def item_insights(self) -> ItemInsightsRequestBuilder:
        """
        Provides operations to manage the itemInsights property of the microsoft.graph.userSettings entity.
        """
        from .item_insights.item_insights_request_builder import ItemInsightsRequestBuilder

        return ItemInsightsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def regional_and_language_settings(self) -> RegionalAndLanguageSettingsRequestBuilder:
        """
        Provides operations to manage the regionalAndLanguageSettings property of the microsoft.graph.userSettings entity.
        """
        from .regional_and_language_settings.regional_and_language_settings_request_builder import RegionalAndLanguageSettingsRequestBuilder

        return RegionalAndLanguageSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shift_preferences(self) -> ShiftPreferencesRequestBuilder:
        """
        Provides operations to manage the shiftPreferences property of the microsoft.graph.userSettings entity.
        """
        from .shift_preferences.shift_preferences_request_builder import ShiftPreferencesRequestBuilder

        return ShiftPreferencesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def storage(self) -> StorageRequestBuilder:
        """
        Provides operations to manage the storage property of the microsoft.graph.userSettings entity.
        """
        from .storage.storage_request_builder import StorageRequestBuilder

        return StorageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows(self) -> WindowsRequestBuilder:
        """
        Provides operations to manage the windows property of the microsoft.graph.userSettings entity.
        """
        from .windows.windows_request_builder import WindowsRequestBuilder

        return WindowsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SettingsRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SettingsRequestBuilderGetQueryParameters():
        """
        Get settings from users
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[list[str]] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

    
    @dataclass
    class SettingsRequestBuilderGetRequestConfiguration(RequestConfiguration[SettingsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SettingsRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

