import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class Client:
    """Базовый HTTP-клиент для работы с API Insapp."""

    def __init__(self, base_url: str, timeout: int = 30, headers: dict | None = None):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.s = requests.Session()

        # Автоматические ретраи на временные ошибки
        retry = Retry(
            total=3,
            backoff_factor=0.5,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        self.s.mount("http://", HTTPAdapter(max_retries=retry))
        self.s.mount("https://", HTTPAdapter(max_retries=retry))

        self.s.headers.update({"Accept": "application/json", **(headers or {})})

    def request(self, method: str, path: str, **kw) -> requests.Response:
        url = f"{self.base_url}/{path.lstrip('/')}"
        return self.s.request(method, url, timeout=self.timeout, **kw)
