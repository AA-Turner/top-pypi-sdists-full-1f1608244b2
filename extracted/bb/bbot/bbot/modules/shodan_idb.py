from bbot.modules.base import BaseModule
import time


class shodan_idb(BaseModule):
    """
    Query IP in Shodan InternetDB, returning open ports, discovered technologies, and findings/vulnerabilities

    InternetDB is especially nice because it doesn't require an API key

    API reference: https://internetdb.shodan.io/docs

    Example API response:

    {
        "cpes": [
            "cpe:/a:microsoft:internet_information_services",
            "cpe:/a:microsoft:outlook_web_access:15.0.1367",
        ],
        "hostnames": [
            "autodiscover.evilcorp.com",
            "mail.evilcorp.com",
        ],
        "ip": "1.2.3.4",
        "ports": [
            25,
            80,
            443,
        ],
        "tags": [
            "starttls",
            "self-signed",
            "eol-os"
        ],
        "vulns": [
            "CVE-2021-26857",
            "CVE-2021-26855"
        ]
    }
    """

    watched_events = ["IP_ADDRESS", "DNS_NAME"]
    produced_events = ["TECHNOLOGY", "VULNERABILITY", "FINDING", "OPEN_TCP_PORT", "DNS_NAME"]
    flags = ["passive", "safe", "portscan", "subdomain-enum"]
    meta = {
        "description": "Query Shodan's InternetDB for open ports, hostnames, technologies, and vulnerabilities",
        "created_date": "2023-12-22",
        "author": "@TheTechromancer",
    }
    options = {"retries": None}
    options_desc = {
        "retries": "How many times to retry API requests (e.g. after a 429 error). Overrides the global web.api_retries setting."
    }

    # we typically don't want to abort this module
    _api_failure_abort_threshold = 9999999999

    # since there are rate limits, we set a lower qsize
    # this way when our queue is full, we can give the API a break
    _qsize = 100

    base_url = "https://internetdb.shodan.io"

    async def setup(self):
        await super().setup()
        self.last_request_time = 0
        return True

    def _incoming_dedup_hash(self, event):
        return hash(self.get_ip(event))

    @property
    def api_retries(self):
        # allow the module to override global retry setting
        return self.config.get("retries", None) or super().api_retries

    async def handle_event(self, event):
        ip = self.get_ip(event)
        if ip is None:
            return
        url = f"{self.base_url}/{ip}"

        # Rate limiting: ensure at least 1 second between requests
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        if time_since_last < 1:
            await self.helpers.sleep(1 - time_since_last)

        # Update the last request time
        self.last_request_time = time.time()

        r = await self.api_request(url)
        if r is None:
            self.debug(f"No response for {event.data}")
            return
        try:
            data = r.json()
        except Exception as e:
            self.verbose(f"Error parsing JSON response from {url}: {e}")
            self.trace()
            return
        if data:
            if r.status_code == 200:
                await self._parse_response(data=data, event=event, ip=ip)
            elif r.status_code == 404:
                detail = data.get("detail", "")
                if detail:
                    self.debug(f"404 response for {url}: {detail}")
            else:
                err_data = data.get("type", "")
                err_msg = data.get("msg", "")
                self.verbose(f"Shodan error for {ip}: {err_data}: {err_msg}")

    async def _parse_response(self, data: dict, event, ip):
        """Handles emitting events from returned JSON"""
        data: dict  # has keys: cpes, hostnames, ip, ports, tags, vulns
        ip = str(ip)
        query_host = ip if event.data == ip else f"{event.data} ({ip})"
        # ip is a string, ports is a list of ports, the rest is a list of strings
        for hostname in data.get("hostnames", []):
            if hostname != event.data:
                await self.emit_event(
                    hostname,
                    "DNS_NAME",
                    parent=event,
                    context=f'{{module}} queried Shodan\'s InternetDB API for "{query_host}" and found {{event.type}}: {{event.data}}',
                )
        for cpe in data.get("cpes", []):
            await self.emit_event(
                {"technology": cpe, "host": str(event.host)},
                "TECHNOLOGY",
                parent=event,
                context=f'{{module}} queried Shodan\'s InternetDB API for "{query_host}" and found {{event.type}}: {{event.data}}',
            )
        for port in data.get("ports", []):
            await self.emit_event(
                self.helpers.make_netloc(event.data, port),
                "OPEN_TCP_PORT",
                parent=event,
                context=f'{{module}} queried Shodan\'s InternetDB API for "{query_host}" and found {{event.type}}: {{event.data}}',
            )
        vulns = data.get("vulns", [])
        if vulns:
            vulns_str = ", ".join([str(v) for v in vulns])
            await self.emit_event(
                {"description": f"Shodan reported possible vulnerabilities: {vulns_str}", "host": str(event.host)},
                "FINDING",
                parent=event,
                context=f'{{module}} queried Shodan\'s InternetDB API for "{query_host}" and found potential {{event.type}}: {vulns_str}',
            )

    def get_ip(self, event):
        """
        Get the first available IP address from an event (IP_ADDRESS or DNS_NAME)
        """
        if event.type == "IP_ADDRESS":
            return event.host
        elif event.type == "DNS_NAME":
            # always try IPv4 first
            ipv6 = []
            ips = [h for h in event.resolved_hosts if self.helpers.is_ip(h)]
            for ip in sorted([str(ip) for ip in ips]):
                if self.helpers.is_ip(ip, version=4):
                    return ip
                elif self.helpers.is_ip(ip, version=6):
                    ipv6.append(ip)
            for ip in ipv6:
                return ip
