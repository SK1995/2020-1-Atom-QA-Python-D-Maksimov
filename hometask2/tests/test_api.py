import pytest

from tests.base_api import BaseCase
from utils.exceptions import ResponseStatusCodeException


@pytest.mark.API
class TestApi(BaseCase):

    def test_create_new_segment(self, create_temp_segment_with_api):
        self.api_client.logout()
        self.api_client = create_temp_segment_with_api
        tmp_segment = self.api_client.segments[-1]
        self.api_client.rename_segment( 'TestTestTest', tmp_segment.id)
        assert tmp_segment.name == 'TestTestTest'

    def test_delete_segment(self, create_temp_segment_with_api):
        self.api_client.logout()
        self.api_client = create_temp_segment_with_api
        tmp_segment = self.api_client.segments[-1]
        self.api_client.delete_segment(tmp_segment.id)
        with pytest.raises(ResponseStatusCodeException):
            self.api_client.rename_segment('TestTestTest', tmp_segment.id)

    def test_delete_all_segments(self, create_temp_segment_with_api):
        self.api_client.logout()
        self.api_client = create_temp_segment_with_api
        self.api_client.create_new_segment('Test2')
        tmp_segment = self.api_client.segments[0]
        self.api_client.delete_all_segments()
        with pytest.raises(ResponseStatusCodeException):
            self.api_client.rename_segment('TestTestTest', tmp_segment.id)