import typing

import kubernetes.client

class LogsApi:
    def __init__(self, api_client: typing.Optional[kubernetes.client.ApiClient] = ...) -> None:
        ...
    def log_file_list_handler(self) -> None:
        ...
    def log_file_handler(self, logpath: str) -> None:
        ...
