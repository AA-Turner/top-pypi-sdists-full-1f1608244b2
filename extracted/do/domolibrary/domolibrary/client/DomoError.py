"""preferred base error class for Domo Exceptions"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/client/DomoError.ipynb.

# %% auto 0
__all__ = ['DomoError', 'RouteError', 'ClassError', 'AuthNotProvidedError', 'DatasetNotProvidedError']

# %% ../../nbs/client/DomoError.ipynb 2
from typing import Optional, Any
# import domolibrary.client.ResponseGetData as rgd

# %% ../../nbs/client/DomoError.ipynb 5
class DomoError(Exception):
    """base exception"""

    def __init__(
        self,
        entity_id: Optional[str] = None,
        function_name: Optional[str] = None,
        status: Optional[int] = None,  # API request status
        message: str = "error",  # <domo_instance>.domo.com
        res = None,
        domo_instance: Optional[str] = None,
        parent_class: str = None,
        is_exception_not_error: bool = False,
    ):
        function_str = ""

        if function_name:
            function_str = f"{function_name} || "

        if parent_class and function_name:
            function_str = f"{res and res.traceback_details.parent_class or parent_class}.{function_str}"
        if parent_class and not function_name:
            function_str = f"{res and res.traceback_details.parent_class or parent_class} || "
        function_str = f"function: {function_str}"

        entity_str = f"{entity_id} || " if entity_id else ""
        instance_str = f" at {res and res.auth.domo_instance or domo_instance}" if domo_instance else ""
        status_str = f"status {res and res.status or status} || " if status else ""
        prefix = "🛑 " if not is_exception_not_error else "⚠️ "

        message = f"{prefix} {self.__class__.__name__} {prefix}- {function_str}{entity_str}{status_str}{message}{instance_str}"
        super().__init__(message)

# %% ../../nbs/client/DomoError.ipynb 7
class RouteError(DomoError):
    """base exception"""

    def __init__(
        self,
        res : Any,
        entity_id: str = None,
        is_exception_not_error: bool = False,
        message=None,
    ):

        super().__init__(
            entity_id = entity_id,
            function_name = res.traceback_details.function_name,
            status =res.status,
            message =message or res.response,
            res = res,
            domo_instance = res.auth.domo_instance,
            parent_class = res.traceback_details.parent_class,
            is_exception_not_error = is_exception_not_error
        )

# %% ../../nbs/client/DomoError.ipynb 9
class ClassError(DomoError):
    """base exception"""

    def __init__(
        self,
        cls = None,
        cls_instance = None,
        cls_name_attr = None,
        entity_id: str = None,
        entity_name : str = None,
        res = None,
        auth = None,
        message :str = None
    ):
        cls = cls or cls_instance.__class__

        auth = auth or (res and res.auth)

        message_str = message or (res and res.response)

        function_str = f"{cls.__name__}"
        if res:
            if res.traceback_details.function_name:
                function_str = f"{function_str}.{res.traceback_details.function_name}"

        entity_id = entity_id or (cls_instance and cls_instance.id)
        entity_name = entity_name or (cls_instance and cls_name_attr and getattr(cls_instance, cls_name_attr)) or ""

        entity_str = entity_id

        if entity_name:
            entity_str = f"{entity_id} - {entity_name}" 
        
        instance_str = f" @ {(auth and auth.domo_instance)}" if auth else ""

        prefix = "🛑"

        message = f"{prefix} {function_str} {prefix} {entity_str} || {message_str}{instance_str}"
        super().__init__(message)

# %% ../../nbs/client/DomoError.ipynb 12
class AuthNotProvidedError(DomoError):
    def __init__(
        self,
        entity_id,
        function_name,
        message="valid Auth object not provided",
        status=None,
        domo_instance=None,
    ):

        super().__init__(
            entity_id=entity_id,
            function_name=function_name,
            status=status,
            message=message,
            domo_instance=domo_instance,
        )

# %% ../../nbs/client/DomoError.ipynb 13
class DatasetNotProvidedError(DomoError):
    def __init__(
        self,
        function_name,
        message="dataset_id not provided",
        domo_instance=None,
        entity_id=None,
        status=None,
    ):

        super().__init__(
            entity_id=entity_id,
            function_name=function_name,
            status=status,
            message=message,
            domo_instance=domo_instance,
        )
