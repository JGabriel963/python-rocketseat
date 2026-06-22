from typing import Dict, Optional


class HttpRequest:
    def __init__(
        self,
        headers: Optional[Dict] = None,
        body: Optional[Dict] = None,
        path_params: Optional[Dict] = None,
    ):
        self.headers = headers
        self.body = body
        self.path_params = path_params
