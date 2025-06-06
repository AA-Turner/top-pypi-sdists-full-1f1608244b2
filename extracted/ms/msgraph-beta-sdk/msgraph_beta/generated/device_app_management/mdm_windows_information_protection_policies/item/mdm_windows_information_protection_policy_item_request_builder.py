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
    from ....models.mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
    from ....models.o_data_errors.o_data_error import ODataError
    from .assignments.assignments_request_builder import AssignmentsRequestBuilder
    from .exempt_app_locker_files.exempt_app_locker_files_request_builder import ExemptAppLockerFilesRequestBuilder
    from .protected_app_locker_files.protected_app_locker_files_request_builder import ProtectedAppLockerFilesRequestBuilder

class MdmWindowsInformationProtectionPolicyItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the mdmWindowsInformationProtectionPolicies property of the microsoft.graph.deviceAppManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MdmWindowsInformationProtectionPolicyItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/mdmWindowsInformationProtectionPolicies/{mdmWindowsInformationProtectionPolicy%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property mdmWindowsInformationProtectionPolicies for deviceAppManagement
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
    
    async def get(self,request_configuration: Optional[RequestConfiguration[MdmWindowsInformationProtectionPolicyItemRequestBuilderGetQueryParameters]] = None) -> Optional[MdmWindowsInformationProtectionPolicy]:
        """
        Windows information protection for apps running on devices which are MDM enrolled.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MdmWindowsInformationProtectionPolicy]
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
        from ....models.mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy

        return await self.request_adapter.send_async(request_info, MdmWindowsInformationProtectionPolicy, error_mapping)
    
    async def patch(self,body: MdmWindowsInformationProtectionPolicy, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[MdmWindowsInformationProtectionPolicy]:
        """
        Update the navigation property mdmWindowsInformationProtectionPolicies in deviceAppManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MdmWindowsInformationProtectionPolicy]
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
        from ....models.mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy

        return await self.request_adapter.send_async(request_info, MdmWindowsInformationProtectionPolicy, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property mdmWindowsInformationProtectionPolicies for deviceAppManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[MdmWindowsInformationProtectionPolicyItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Windows information protection for apps running on devices which are MDM enrolled.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: MdmWindowsInformationProtectionPolicy, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property mdmWindowsInformationProtectionPolicies in deviceAppManagement
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
    
    def with_url(self,raw_url: str) -> MdmWindowsInformationProtectionPolicyItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MdmWindowsInformationProtectionPolicyItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MdmWindowsInformationProtectionPolicyItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def assignments(self) -> AssignmentsRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.windowsInformationProtection entity.
        """
        from .assignments.assignments_request_builder import AssignmentsRequestBuilder

        return AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exempt_app_locker_files(self) -> ExemptAppLockerFilesRequestBuilder:
        """
        Provides operations to manage the exemptAppLockerFiles property of the microsoft.graph.windowsInformationProtection entity.
        """
        from .exempt_app_locker_files.exempt_app_locker_files_request_builder import ExemptAppLockerFilesRequestBuilder

        return ExemptAppLockerFilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def protected_app_locker_files(self) -> ProtectedAppLockerFilesRequestBuilder:
        """
        Provides operations to manage the protectedAppLockerFiles property of the microsoft.graph.windowsInformationProtection entity.
        """
        from .protected_app_locker_files.protected_app_locker_files_request_builder import ProtectedAppLockerFilesRequestBuilder

        return ProtectedAppLockerFilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class MdmWindowsInformationProtectionPolicyItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class MdmWindowsInformationProtectionPolicyItemRequestBuilderGetQueryParameters():
        """
        Windows information protection for apps running on devices which are MDM enrolled.
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
    class MdmWindowsInformationProtectionPolicyItemRequestBuilderGetRequestConfiguration(RequestConfiguration[MdmWindowsInformationProtectionPolicyItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class MdmWindowsInformationProtectionPolicyItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

