import pytest

from api.client import ApiClient
from utils.additional_structures import Segments


@pytest.fixture(scope='session')
def built_api_client(config_api):
    return ApiClient(config_api)


@pytest.fixture(scope='function')
def create_temp_segment_with_api(built_api_client):
    api_client = built_api_client
    segments = Segments()
    api_client.create_new_segment('Test1', segments)
    yield api_client, segments
    api_client.delete_all_segments(segments)
