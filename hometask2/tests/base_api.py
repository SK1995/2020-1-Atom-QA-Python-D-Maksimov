import pytest

from api.client import ApiClient
from conftest import ApiSettings


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, config_api):
        self.config: ApiSettings = config_api
        self.api_client: ApiClient = ApiClient(config_api)
