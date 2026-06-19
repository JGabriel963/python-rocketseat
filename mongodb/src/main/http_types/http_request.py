from typing import Dict, Optional


class HttpRequest:
    def __init__(
        self,
        body: Optional[Dict] = None,
        header: Optional[Dict] = None,
    ) -> None:
        self.body = body
        self.headers = header
