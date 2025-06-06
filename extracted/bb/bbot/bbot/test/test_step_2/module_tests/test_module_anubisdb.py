from .base import ModuleTestBase


class TestAnubisdb(ModuleTestBase):
    async def setup_after_prep(self, module_test):
        module_test.module.abort_if = lambda e: False
        module_test.httpx_mock.add_response(
            url="https://jldc.me/anubis/subdomains/blacklanternsecurity.com",
            json=["asdf.blacklanternsecurity.com", "zzzz.blacklanternsecurity.com"],
        )

    def check(self, module_test, events):
        assert any(e.data == "asdf.blacklanternsecurity.com" for e in events), "Failed to detect subdomain"
