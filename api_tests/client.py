import requests
import logging

logger = logging.getLogger(__name__)


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()

    def _log(self, response: requests.Response):
        logger.info(f"{response.request.method} {response.request.url} -> {response.status_code}")
        if response.request.body:
            logger.debug(f"Request body: {response.request.body}")
        if response.text:
            logger.debug(f"Response body: {response.text[:500]}")

    def get(self, path: str, **kwargs) -> requests.Response:
        response = self.session.get(f"{self.base_url}{path}", **kwargs)
        self._log(response)
        return response

    def post(self, path: str, **kwargs) -> requests.Response:
        response = self.session.post(f"{self.base_url}{path}", **kwargs)
        self._log(response)
        return response

    def put(self, path: str, **kwargs) -> requests.Response:
        response = self.session.put(f"{self.base_url}{path}", **kwargs)
        self._log(response)
        return response

    def delete(self, path: str, **kwargs) -> requests.Response:
        response = self.session.delete(f"{self.base_url}{path}", **kwargs)
        self._log(response)
        return response
