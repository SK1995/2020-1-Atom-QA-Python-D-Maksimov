import pytest

from tests.base_api import BaseCase


@pytest.mark.API
class TestApi(BaseCase):

    def test_create_new_segment(self, api_client):
        segment = api_client.create_new_segment('Test1')
        assert api_client.get_segment(id=segment.id) is not None
        api_client.delete_segment(id=segment.id)

    def test_delete_segment(self, api_client):
        segment = api_client.create_new_segment('Test1')
        assert segment is not None
        api_client.delete_segment(id=segment.id)
        assert api_client.get_segment(id=segment.id) is None

    def test_delete_all_my_segments(self, api_client):
        segment1 = api_client.create_new_segment('Test1')
        segment2 = api_client.create_new_segment('Test2')
        assert all((segment1, segment2))
        api_client.delete_segments(segment_ids=[segment1.id, segment2.id])
        assert self.api_client.get_segments_list() == []
