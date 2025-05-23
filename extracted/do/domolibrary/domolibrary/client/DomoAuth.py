"""Fill in a module description here"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/client/95_DomoAuth.ipynb.

# %% auto 0
__all__ = ['DomoAuth', 'test_is_full_auth', 'DomoTokenAuth', 'DomoDeveloperAuth', 'DomoJupyterAuth', 'DomoJupyterFullAuth',
           'DomoJupyterTokenAuth', 'test_is_jupyter_auth']

# %% ../../nbs/client/95_DomoAuth.ipynb 3
from domolibrary.routes.auth import (
    AuthError,
    AccountLockedError,
    InvalidAuthTypeError,
    InvalidCredentialsError,
    InvalidInstanceError,
    NoAccessTokenReturned,
)

# %% ../../nbs/client/95_DomoAuth.ipynb 4
from dataclasses import dataclass, field
from typing import Optional, Union
from urllib.parse import urlparse

from abc import abstractmethod
import httpx

import domolibrary.client.Logger as lg

import domolibrary.routes.auth as auth_routes

# %% ../../nbs/client/95_DomoAuth.ipynb 8
@dataclass
class DomoAuth:
    """abstract DomoAuth class"""

    domo_instance: str
    url_manual_login: str

    auth_header: dict = field(repr=False)
    token_name: str
    token: str = field(repr=False)

    user_id: str
    is_valid_token: bool

    def __post_init__(self):
        """Initialize url_manual_login after instance creation."""
        self.url_manual_login = self._generate_manual_login(
            domo_instance=self.domo_instance
        )

    @staticmethod
    def _generate_manual_login(domo_instance):
        return f"https://{domo_instance}.domo.com/auth/index?domoManualLogin=true"

    @classmethod
    def from_domo_instance(cls, domo_instance, token_name=None):
        """Create an instance using the provided domo_instance and optional token_name."""
        return cls(
            domo_instance=domo_instance,
            url_manual_login=cls._generate_manual_login(domo_instance),
            auth_header={},
            token_name=token_name,
            token=None,
            user_id=None,
            is_valid_token=False,
        )

    async def who_am_i(
        self,
        session: httpx.AsyncClient = None,
        debug_api: bool = False,
        debug_num_stacks_to_drop=2,
    ):
        """Perform an API call to identify the user associated with the token."""

        if not self.auth_header:
            self.generate_auth_header()

        res = await auth_routes.who_am_i(
            auth=None,
            auth_header=self.auth_header,
            domo_instance=self.domo_instance,
            parent_class=self.__class__.__name__,
            session=session,
            debug_api=debug_api,
            debug_num_stacks_to_drop=debug_num_stacks_to_drop,
        )

        self.user_id = res.response["id"]

        return res

    @abstractmethod
    async def get_auth_token(self) -> Union[str, None]:
        """placeholder method"""
        pass

    @abstractmethod
    def _generate_auth_header(self) -> Union[dict, None]:
        """returns auth header appropriate for this authentication method"""
        pass

    def generate_auth_header(self) -> Union[dict, None]:
        """Generate the authentication header using the specialized method."""
        return self._generate_auth_header()

    async def print_is_token(
        self,
        debug_api: bool = False,
        token_name=None,
        session: httpx.AsyncClient = None,
    ) -> bool:
        """Print token status and return True if token is valid, otherwise False."""
        self.token_name = token_name or self.token_name

        if not self.token:
            await self.get_auth_token(debug_api=debug_api, session=session)

        token_str = f"{self.token_name} " or ""
        if not self.token:
            print(f"🚧 failed to retrieve {token_str}token from {self.domo_instance}")
            return False

        print(f"🎉 {token_str}token retrieved from {self.domo_instance} ⚙️")
        return True

# %% ../../nbs/client/95_DomoAuth.ipynb 12
@dataclass
class DomoFullAuth(DomoAuth):
    """mix requied parameters for DomoFullAuth"""

    domo_username: str
    domo_password: str = field(repr=False)

    def __init__(
        self, domo_instance, domo_username, domo_password, token_name: str = None
    ):
        """Initialize DomoFullAuth using username and password credentials."""
        self.domo_username = domo_username
        self.domo_password = domo_password

        super().__init__(
            domo_instance=domo_instance,
            url_manual_login=super()._generate_manual_login(domo_instance),
            auth_header={},
            token_name=token_name,
            token=None,
            user_id=None,
            is_valid_token=False,
        )

    def _generate_auth_header(self) -> dict:
        """Generate the full authentication header specific to product APIs."""
        self.auth_header = {"x-domo-authentication": self.token}
        return self.auth_header

    def generate_auth_header(self) -> dict:
        """Return the generated full authentication header."""
        return self._generate_auth_header()

    async def get_auth_token(
        self,
        session: Optional[httpx.AsyncClient] = None,
        return_raw: bool = False,
        debug_api: bool = False,
        debug_num_stacks_to_drop=2,
    ) -> str:
        """Retrieve the authentication token from product APIs using the provided credentials."""

        res = await auth_routes.get_full_auth(
            auth=None,
            domo_instance=self.domo_instance,
            domo_username=self.domo_username,
            domo_password=self.domo_password,
            session=session,
            debug_api=debug_api,
            parent_class=self.__class__.__name__,
            debug_num_stacks_to_drop=debug_num_stacks_to_drop,
        )

        if return_raw:
            return res

        self.is_valid_token = True
        self.token = str(res.response.get("sessionToken"))

        self.token_name = self.token_name or "full_auth"

        self.generate_auth_header()

        return self.token

# %% ../../nbs/client/95_DomoAuth.ipynb 16
def test_is_full_auth(
    auth, function_name=None, num_stacks_to_drop=1  # pass q for route pass 2 for class
):
    """Test that the provided object is a DomoFullAuth instance."""
    tb = lg.get_traceback(num_stacks_to_drop=num_stacks_to_drop)

    function_name = function_name or tb.function_name

    if auth.__class__.__name__ != "DomoFullAuth":
        raise InvalidAuthTypeError(
            function_name=function_name,
            domo_instance=auth.domo_instance,
            required_auth_type=DomoFullAuth,
        )

# %% ../../nbs/client/95_DomoAuth.ipynb 18
@dataclass
class DomoTokenAuth(DomoAuth):
    domo_access_token: str = field(repr=False)

    """
    use for access_token authentication.
    Tokens are generated in domo > admin > access token
    Necessary in cases where direct sign on is not permitted
    """

    def __init__(
        self, domo_access_token: str, domo_instance: str, token_name: str = None
    ):
        """Initialize DomoTokenAuth with the provided access token for product APIs."""
        self.domo_access_token = domo_access_token

        super().__init__(
            domo_instance=domo_instance,
            url_manual_login=super()._generate_manual_login(domo_instance),
            auth_header={},
            token_name=token_name,
            token=None,
            user_id=None,
            is_valid_token=False,
        )

    def _generate_auth_header(self) -> dict:
        """Generate the authentication header for access token based authentication."""
        self.auth_header = {
            "x-domo-developer-token": self.token or self.domo_access_token
        }

        return self.auth_header

    def generate_auth_header(self) -> dict:
        """Return the generated access token authentication header."""
        return self._generate_auth_header()

    async def get_auth_token(
        self,
        session: Optional[httpx.AsyncClient] = None,
        debug_api: bool = False,
        debug_num_stacks_to_drop=2,
    ) -> str:
        """Retrieve the access token, updating internal attributes as necessary."""

        if not self.user_id or not self.token:
            await self.who_am_i(
                session=session,
                debug_api=debug_api,
                debug_num_stacks_to_drop=debug_num_stacks_to_drop + 1,
            )

        self.is_valid_token = True
        self.token = self.domo_access_token
        self.token_name = self.token_name or "token_auth"

        return self.token

# %% ../../nbs/client/95_DomoAuth.ipynb 24
@dataclass
class DomoDeveloperAuth(DomoAuth):
    domo_client_id: str
    domo_client_secret: str = field(repr=False)

    def __init__(
        self,
        domo_client_id,
        domo_client_secret,
        token_name: str = None,
        domo_instance: str = None,
    ):
        """Initialize DomoDeveloperAuth with client credentials for platform APIs."""
        self.domo_client_id = domo_client_id
        self.domo_client_secret = domo_client_secret

        super().__init__(
            domo_instance=domo_instance,
            url_manual_login=super()._generate_manual_login(domo_instance),
            auth_header={},
            token_name=token_name,
            token=None,
            user_id=None,
            is_valid_token=False,
        )

    def _generate_auth_header(self) -> dict:
        """Generate the authentication header for developer token authentication."""
        self.auth_header = {"Authorization": "bearer " + self.token}

        return self.auth_header

    def generate_auth_header(self) -> dict:
        """Return the generated developer token authentication header."""
        return self._generate_auth_header()

    async def get_auth_token(
        self,
        session: Optional[httpx.AsyncClient] = None,
        debug_api: bool = False,
        debug_num_stacks_to_drop=2,
    ) -> str:
        """Retrieve the developer token using client credentials and update internal attributes."""

        res = await auth_routes.get_developer_auth(
            auth=None,
            domo_client_id=self.domo_client_id,
            domo_client_secret=self.domo_client_secret,
            session=session,
            debug_api=debug_api,
            parent_class=self.__class__.__name__,
            debug_num_stacks_to_drop=debug_num_stacks_to_drop + 1,
        )

        self.is_valid_token = True

        self.token = str(res.response.get("access_token"))
        self.user_id = res.response.get("userId")
        self.domo_instance = res.response.get("domain")

        self._generate_manual_login()

        self.generate_auth_header()

        self.token_name = self.token_name or "developer_auth"

        return self.token

# %% ../../nbs/client/95_DomoAuth.ipynb 28
@dataclass
class _DomoJupyter_Optional:
    def __post_init__(self):

        self.jupyter_token = self.jupyter_token or input(
            "jupyter token: # retrieve this by monitoring domo jupyter network traffic.  it is the Authorization header"
        )
        self.service_location = self.service_location or input(
            "service_location:  # retrieve from domo jupyter env"
        )
        self.service_prefix = self.service_prefix or input(
            "service prefix: # retrieve from domo jupyter env"
        )

        self._test_prereq()
        self._generate_manual_login(domo_instance=self.domo_instance)
        
        self.generate_auth_header()


@dataclass
class _DomoJupyter_Required:
    jupyter_token: str
    service_location: str
    service_prefix: str

    def get_jupyter_token_flow(self):
        """stub"""
        print("hello world i am a jupyter_token")

    def _test_prereq(self):
        if not self.jupyter_token:
            raise Exception("DomoJupyterAuth objects must have a jupyter_token")

        if not self.service_location:
            raise Exception("DomoJupyterAuth objects must have a service_location")

        if not self.service_prefix:
            raise Exception("DomoJupyterAuth objects must have a service_prefix")

        if (
            not self.jupyter_token
            or not self.service_location
            or not self.service_prefix
        ):
            raise Exception(
                "DomoJupyterAuth objects must have jupyter_token, service_location and service_prefix"
            )

# %% ../../nbs/client/95_DomoAuth.ipynb 29
@dataclass
class DomoJupyterAuth(_DomoJupyter_Optional, _DomoJupyter_Required):
    """base class"""

# %% ../../nbs/client/95_DomoAuth.ipynb 31
@dataclass
class DomoJupyterFullAuth(_DomoJupyter_Optional, DomoFullAuth, _DomoJupyter_Required):

    @classmethod
    def convert_auth(
        cls, auth: DomoFullAuth, jupyter_token, service_location, service_prefix
    ):
        """converts DomoFullAuth to DomoJupyterFullAuth
        i.e. adds DomoJupyter specific auth fields
        eventually can add DomoJupyter specific auth flow for generating auth token
        """
        return cls(
            domo_instance=auth.domo_instance,
            domo_username=auth.domo_username,
            domo_password=auth.domo_password,
            jupyter_token=jupyter_token,
            service_location=service_location,
            service_prefix=service_prefix,
            url_manual_login=auth.url_manual_login,
            auth_header=auth.auth_header,
            token_name=auth.token_name,
            token=auth.token,
            user_id=auth.user_id,
            is_valid_token=auth.is_valid_token,
        )

    def generate_auth_header(self) -> dict:

        self._generate_auth_header()

        self.auth_header.update(
            {
                "authorization": f"Token {self.jupyter_token}",
            }
        )

        return self.auth_header

# %% ../../nbs/client/95_DomoAuth.ipynb 35
@dataclass
class DomoJupyterTokenAuth(_DomoJupyter_Optional, DomoTokenAuth, _DomoJupyter_Required):
    @classmethod
    def convert_auth(
        cls, auth: DomoTokenAuth, jupyter_token, service_location, service_prefix
    ):
        """converts DomoTokenAuth to DomoJupyterTokenAuth
        i.e. adds DomoJupyter specific auth fields
        eventually can add DomoJupyter specific auth flow for generating auth token
        """
        return cls(
            domo_instance=auth.domo_instance,
            domo_access_token=auth.domo_access_token,
            jupyter_token=jupyter_token,
            service_location=service_location,
            service_prefix=service_prefix,
            url_manual_login=auth.url_manual_login,
            auth_header=auth.auth_header,
            token_name=auth.token_name,
            token=auth.token,
            user_id=auth.user_id,
            is_valid_token=auth.is_valid_token,
        )

    def generate_auth_header(self) -> dict:
        self._generate_auth_header()

        self.auth_header.update(
            {
                "authorization": f"Token {self.jupyter_token}",
            }
        )

        return self.auth_header

# %% ../../nbs/client/95_DomoAuth.ipynb 39
def test_is_jupyter_auth(
    auth: DomoJupyterAuth,
    function_name=None,
    required_auth_type_ls=[DomoJupyterFullAuth, DomoJupyterTokenAuth],
):
    """Test that the provided object is a valid Jupyter authentication instance."""
    tb = lg.get_traceback()

    if auth.__class__.__name__ not in [
        auth_type.__name__ for auth_type in required_auth_type_ls
    ]:
        raise InvalidAuthTypeError(
            function_name=tb.function_name,
            domo_instance=auth.domo_instance,
            required_auth_type_ls=required_auth_type_ls,
        )
