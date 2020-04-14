import pytest

from tests.base_api import BaseCase
from utils.additional_structures import Segments
from utils.exceptions import ResponseStatusCodeException


@pytest.mark.API
class TestApi(BaseCase):

    def test_create_new_segment(self, create_temp_segment_with_api):
        self.api_client = create_temp_segment_with_api[0]
        segments: Segments = create_temp_segment_with_api[1]
        tmp_segment = segments.data[-1]
        flag = False
        for segment in self.api_client.get_segments_list():
            if segment['id'] == tmp_segment.id:
                flag = True
        assert flag
        self.api_client.delete_all_segments(segments)
        # self.api_client.rename_segment('TestTestTest', tmp_segment.id, segments)
        # assert tmp_segment.name == 'TestTestTest'

    def test_delete_segment(self, create_temp_segment_with_api):
        self.api_client = create_temp_segment_with_api[0]
        segments: Segments = create_temp_segment_with_api[1]
        tmp_segment = segments.data[-1]
        self.api_client.delete_segment(tmp_segment.id, segments)
        for segment in self.api_client.get_segments_list():
            assert not segment['id'] == tmp_segment.id
        self.api_client.delete_all_segments(segments)
        # with pytest.raises(ResponseStatusCodeException):
        #     self.api_client.rename_segment('TestTestTest', tmp_segment.id, segments)

    def test_delete_all_my_segments(self, create_temp_segment_with_api):
        self.api_client = create_temp_segment_with_api[0]
        segments: Segments = create_temp_segment_with_api[1]
        self.api_client.create_new_segment('Test2', segments)
        # tmp_segment = segments.data[0]
        self.api_client.delete_all_segments(segments)
        # with pytest.raises(ResponseStatusCodeException):
        #     self.api_client.rename_segment('TestTestTest', tmp_segment.id, segments)
        assert self.api_client.get_segments_list() == []
