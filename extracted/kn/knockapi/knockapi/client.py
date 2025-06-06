import requests
from knockapi.__about__ import __version__

try:
    from requests.exceptions import JSONDecodeError
except ImportError:
    try:
        from simplejson import JSONDecodeError
    except ImportError:
        from json.decoder import JSONDecodeError


class Connection(object):
    def __init__(self, api_key, host='https://api.knock.app', timeout=None):
        self.api_key = api_key
        self.host = host
        self.client_version = __version__
        self.headers = {
            'Authorization': 'Bearer {}'.format(self.api_key),
            'User-Agent': 'Knock Python - {}'.format(self.client_version)
        }
        self.timeout = timeout

    def request(self, method, endpoint, payload=None, options={}):
        url = '{}/v1{}'.format(self.host, endpoint)

        extra_headers = {}
        if (method in ["post", "put"]) and options.get('idempotency_key') is not None:
            extra_headers['Idempotency-Key'] = options.get('idempotency_key')

        r = requests.request(
            method,
            url,
            params=payload if method == 'get' else None,
            json=payload if method != 'get' else None,
            headers={**self.headers, **extra_headers},
            timeout=self.timeout,
        )

        # If we got a successful response, check for content before attempting to deserialize as JSON
        if r.ok:
            if r.content and len(r.content) > 0:
                try:
                    return r.json()
                except JSONDecodeError:
                    return None
            return None

        return r.raise_for_status()


class Knock(Connection):
    """Client to access the Knock features."""
    @property
    def _auth(self):
        return self.api_key

    @property
    def _version(self):
        return __version__

    @property
    def users(self):
        from .resources import User
        return User(self)

    @property
    def workflows(self):
        from .resources import Workflows
        return Workflows(self)

    @property
    def preferences(self):
        from .resources import Preferences
        return Preferences(self)

    @property
    def objects(self):
        from .resources import Objects
        return Objects(self)

    @property
    def tenants(self):
        from .resources import Tenants
        return Tenants(self)

    @property
    def bulk_operations(self):
        from .resources import BulkOperations
        return BulkOperations(self)

    @property
    def messages(self):
        from .resources import Messages
        return Messages(self)

    # Defined at the top level here for convenience
    def notify(
            self,
            key,
            recipients,
            data={},
            actor=None,
            cancellation_key=None,
            tenant=None,
            options={}):
        """
        Triggers a workflow.

        Args:
            key (str): The key of the workflow to invoke.

            actor (str | dict[str, Any]): An optional reference for who/what performed the action. This can be A) a user
            id, B) an object reference, or C) a dictionary with data to identify a user or object.

            recipients (list[str | dict[str, Any]]): A list of recipients that should be notified. This can be a list of
            A) user ids, B) object references, C) dictionaries with data to identify a user or object, or D) a
            combination thereof.

            data (dict): Any data to be passed to the notify call.

            tenant (str): An optional identifier for the tenant that the notifications belong to.

            cancellation_key (str): A key used to cancel this notify.

            options (dict): An optional dictionary of options to pass to the request.
            Can include:
            - idempotency_key (str): An optional key that, if passed, will ensure that the same call is not made twice.

        Returns:
            dict: Response from Knock.
        """
        # Note: this is essentially a delegated method
        return self.workflows.trigger(
            key=key,
            recipients=recipients,
            data=data,
            actor=actor,
            cancellation_key=cancellation_key,
            tenant=tenant,
            options=options)
