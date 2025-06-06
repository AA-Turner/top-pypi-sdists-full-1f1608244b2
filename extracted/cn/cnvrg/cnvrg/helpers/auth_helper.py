import yaml
import re
import os
import requests
import json
import cnvrg.modules.errors as errors
from tinynetrc import Netrc
from cnvrg.helpers.url_builder_helper import url_join
NETRC_HOST = "cnvrg.io"
CONFIG_FILE_PATH = os.path.join(os.path.expanduser("~"), ".cnvrg", "config.yml")
netrc_filename = "_netrc" if os.name == "nt" else ".netrc"
NETRC_FILE_PATH = os.path.join(os.path.expanduser("~"), netrc_filename)


class SSO_VERSION:
    AUTH_TOKEN = "v1"
    CAPI = "v2"
    SSOV3 = "v3"

DEFAULT_API_URL = "https://app.cnvrg.io/api"

class CnvrgCredentials():
    def __init__(self):
        self.token = None
        self.api_url = self.set_api_url(DEFAULT_API_URL)
        self.owner = None
        self.username = None
        self.sso_version = None
        self.logged_in = self._load_yaml() or self._load_environ()

        if self.sso_version is None and self.api_url != DEFAULT_API_URL:
            self.sso_version = self._fetch_sso_version()

    def set_api_url(self, api_url):
        api_url = re.sub(r'(\/api\/?)?(v1.*)?', '', api_url)
        self.api_url = url_join(api_url, 'api')
        return self.api_url

    def _fetch_sso_version(self):
        try:
            resp = requests.get(url_join(self.api_url, 'v2', 'version'))
            return resp.json().get("sso_version")
        except Exception:
            return SSO_VERSION.CAPI

    def login(self, email, password, api_url=None, owner=None):
        api_url = self.set_api_url(api_url or self.api_url)
        if self.sso_version is None:
            self.sso_version = self._fetch_sso_version()
        resp = requests.post(url_join(api_url, 'v1', 'users', 'sign_in'), headers={"EMAIL": email, "PASSWORD": password},verify=False)
        if resp.status_code != 200:
            error_message = json.loads(resp.content).get("message")
            raise errors.CnvrgError("Can't Authenticate {email}, message: {message}".format(email=email, message=error_message))
        res = resp.json().get("result")
        if not res:
            raise errors.CnvrgError("Can't Authenticate {email}".format(email=email))
        token = res.get("token")
        username = res.get("username")
        owner = owner or res.get("owners")[0]
        api_url = api_url or res.get("urls")[0]

        self.__set_credentials(token=token, owner=owner, username=username, email=email, api_url=api_url)
        self.logged_in = True

    def token_login(self, email, token, api_url=None, owner=None):
        api_url = self.set_api_url(api_url or self.api_url)
        if self.sso_version is None:
            self.sso_version = self._fetch_sso_version()
        self.token = token
        auth_header = self.get_auth_header()
        resp = requests.post(url_join(api_url, 'v1', 'users', 'sign_in'),
                             headers={"EMAIL": email, "PASSWORD": "", "Authorization": auth_header}, verify=False)

        if resp.status_code != 200:
            error_message = json.loads(resp.content).get("message")
            raise errors.CnvrgError(
                "Can't Authenticate {email}, message: {message}".format(email=email, message=error_message))
        res = resp.json().get("result")
        if not res:
            raise errors.CnvrgError("Can't Authenticate {email}".format(email=email))
        username = res.get("username")
        owner = owner or res.get("owners")[0]
        api_url = api_url or res.get("urls")[0]

        self.__set_credentials(token=token, owner=owner, username=username, email=email, api_url=api_url)
        self.logged_in = True

    def logout(self):
        if not self.logged_in: return
        netrc = Netrc(file=NETRC_FILE_PATH)
        del netrc[NETRC_HOST]
        netrc.save()
        os.remove(CONFIG_FILE_PATH)
        return True

    def __set_credentials(self, token=None, owner=None, username=None, email=None, api_url=None):
        self.token = token
        self.owner = owner
        self.username = username
        self.email = email
        self.api_url = api_url

    def _load_environ(self):
        token = os.environ.get("CNVRG_AUTH_TOKEN")
        api_url = os.environ.get("CNVRG_API")
        owner = os.environ.get("CNVRG_OWNER")
        if not api_url: return None
        self.set_api_url(api_url)
        if not token: return None
        if not owner: return None
        self.token = token
        self.owner = owner
        self.sso_version = os.environ.get("CNVRG_SSO_VERSION", SSO_VERSION.CAPI)
        return True

    def _load_yaml(self):
        if not os.path.exists(NETRC_FILE_PATH): return None
        if not os.path.exists(CONFIG_FILE_PATH): return None
        netrc = Netrc(file=NETRC_FILE_PATH)
        token = netrc[NETRC_HOST]["password"]
        config = yaml.safe_load(open(CONFIG_FILE_PATH, "r"))
        api_url = config.get(":api") or config.get("api")
        owner = config.get(":owner") or config.get("owner")
        if not api_url: return None
        self.set_api_url(api_url)
        if not token: return None
        if not owner: return None
        self.token = token
        self.owner = owner
        return True

    def get_auth_header(self):
        if self.sso_version == SSO_VERSION.SSOV3:
            return "Bearer {}".format(self.token)
        return "CAPI {}".format(self.token)

    def web_url(self):
        return self.api_url.replace("/api", "")