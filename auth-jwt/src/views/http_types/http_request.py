from typing import Dict, Optional


class HttpRequest:
    def __init__(
        self,
        body: Optional[Dict] = None,
        headers: Optional[Dict] = None,
        params: Optional[Dict] = None,
        token_infos: Optional[Dict] = None,
    ) -> None:
        self.body = body
        self.headers = headers
        self.params = params
        self.token_infos = token_infos
