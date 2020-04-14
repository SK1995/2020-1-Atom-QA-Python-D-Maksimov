import pytest

from api.client import ApiClient


@pytest.fixture(scope='session')
def api_client(config_api):
    return ApiClient(config_api)
