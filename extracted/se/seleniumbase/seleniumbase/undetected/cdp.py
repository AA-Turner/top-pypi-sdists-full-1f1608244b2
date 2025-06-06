import fasteners
import json
import logging
import requests
from seleniumbase.fixtures import constants
from seleniumbase.fixtures import shared_utils

log = logging.getLogger(__name__)


class CDPObject(dict):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.__dict__ = self
        for k in self.__dict__:
            if isinstance(self.__dict__[k], dict):
                self.__dict__[k] = CDPObject(self.__dict__[k])
            elif isinstance(self.__dict__[k], list):
                for i in range(len(self.__dict__[k])):
                    if isinstance(self.__dict__[k][i], dict):
                        self.__dict__[k][i] = CDPObject(self)

    def __repr__(self):
        tpl = "%s(\n\t{{}}\n\t)" % self.__class__.__name__
        return tpl.format(
            "\n  ".join("%s = %s" % (k, v) for k, v in self.items())
        )


class PageElement(CDPObject):
    pass


class CDP:
    log = logging.getLogger("CDP")

    endpoints = CDPObject(
        {
            "json": "/json",
            "protocol": "/json/protocol",
            "list": "/json/list",
            "new": "/json/new?{url}",
            "activate": "/json/activate/{id}",
            "close": "/json/close/{id}",
        }
    )

    def __init__(self, options):
        self.server_addr = "http://{0}:{1}".format(
            *options.debugger_address.split(":")
        )
        self._reqid = 0
        self._session = requests.Session()
        self._last_resp = None
        self._last_json = None
        with requests.Session() as session:
            resp = session.get(
                self.server_addr + self.endpoints.json,
                headers={"Connection": "close"},
                timeout=2,
            )
            self.sessionId = resp.json()[0]["id"]
            self.wsurl = resp.json()[0]["webSocketDebuggerUrl"]

    def tab_activate(self, id=None):
        if not id:
            active_tab = self.tab_list()[0]
            id = active_tab.id
            self.wsurl = active_tab.webSocketDebuggerUrl
        with requests.Session() as session:
            resp = session.post(
                self.server_addr + self.endpoints["activate"].format(id=id),
                headers={"Connection": "close"},
                timeout=2,
            )
            return resp.json()

    def tab_list(self):
        with requests.Session() as session:
            resp = session.get(
                self.server_addr + self.endpoints["list"],
                headers={"Connection": "close"},
                timeout=2,
            )
            retval = resp.json()
            return [PageElement(o) for o in retval]

    def tab_new(self, url):
        with requests.Session() as session:
            resp = session.post(
                self.server_addr + self.endpoints["new"].format(url=url),
                headers={"Connection": "close"},
                timeout=2,
            )
            return resp.json()

    def tab_close_last_opened(self):
        sessions = self.tab_list()
        opentabs = [s for s in sessions if s["type"] == "page"]
        with requests.Session() as session:
            endp_close = self.endpoints["close"]
            resp = session.post(
                self.server_addr + endp_close.format(id=opentabs[-1]["id"]),
                headers={"Connection": "close"},
                timeout=2,
            )
            return resp.json()

    async def send(self, method, params):
        pip_find_lock = fasteners.InterProcessLock(
            constants.PipInstall.FINDLOCK
        )
        with pip_find_lock:
            try:
                import websockets
            except Exception:
                shared_utils.pip_install("websockets")
                import websockets
        self._reqid += 1
        async with websockets.connect(self.wsurl) as ws:
            await ws.send(
                json.dumps(
                    {"method": method, "params": params, "id": self._reqid}
                )
            )
            self._last_resp = await ws.recv()
            self._last_json = json.loads(self._last_resp)
            self.log.info(self._last_json)

    def get(self, uri):
        from urllib.parse import unquote

        uri = unquote(uri, errors="strict")
        with requests.Session() as session:
            resp = session.get(
                self.server_addr + uri,
                headers={"Connection": "close"},
                timeout=2,
            )
            try:
                self._last_resp = resp
                self._last_json = resp.json()
            except Exception:
                return
            else:
                return self._last_json

    def post(self, uri, data=None):
        from urllib.parse import unquote

        uri = unquote(uri, errors="strict")
        if not data:
            data = {}
        with requests.Session() as session:
            resp = session.post(
                self.server_addr + uri,
                json=data,
                headers={"Connection": "close"},
                timeout=2,
            )
            try:
                self._last_resp = resp
                self._last_json = resp.json()
            except Exception:
                return self._last_resp

    @property
    def last_json(self):
        return self._last_json
