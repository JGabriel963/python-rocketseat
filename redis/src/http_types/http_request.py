from typing import Dict, Optional


class HttpRequest:
    def __init__(
        self,
        body: Optional[Dict] = None,
        params: Optional[Dict] = None,
    ) -> None:
        self.body = body
        self.params = params
