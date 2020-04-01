import pytest

from api.client import ApiClient


@pytest.fixture(scope='function')
def create_temp_segment_with_api(config_api):
    api_client = ApiClient(config_api)
    api_client.create_new_segment('Test1')
    yield api_client
    api_client.delete_all_segments()