import pytest

from tests.base_ui import BaseCase
from utils.exceptions import InvalidLoginInfoException, NoSuchElementException


@pytest.mark.UI
class TestUi(BaseCase):

    def test_login_in(self, get_campaigns_list_page):
        camp_list_page = get_campaigns_list_page
        assert camp_list_page.check_available_of_element(camp_list_page.locators.PROFILE_ELEMENT)

    @pytest.mark.parametrize('user_email', ['qweqweqweqwe@mail.ru', 'qweqweqwe'])
    def test_login_in_failed(self, user_email):
        with pytest.raises(InvalidLoginInfoException):
            self.login_page.login_in(email=user_email, password='qweqweqweqwe')

    def test_create_first_campaign(self, create_temp_campaign):
        camp_list_page = create_temp_campaign
        assert camp_list_page.find(camp_list_page.locators.CAMPAIGN_NAME_ELEM).text == 'Test1'

    def test_create_new_campaign(self, create_temp_campaign, upload_image_path):
        camp_list_page = create_temp_campaign
        camp_list_page.create_new_campaign('Test2', upload_image_path)
        assert camp_list_page.find(camp_list_page.locators.CAMPAIGN_NAME_ELEM).text == 'Test2'

    def test_remove_all_campaigns(self, get_campaigns_list_page, upload_image_path):
        camp_list_page = get_campaigns_list_page
        camp_list_page.create_first_campaign('Test1', upload_image_path)
        camp_list_page.remove_all_campaigns()
        with pytest.raises(NoSuchElementException):
            camp_list_page.find(camp_list_page.locators.CAMPAIGN_NAME_ELEM)

    def test_create_first_segment(self, create_temp_segment):
        segments_page = create_temp_segment
        assert segments_page.find(segments_page.locators.SEGMENT_NAME_ELEM).text == 'Test1'

    def test_delete_segment(self, get_campaigns_list_page):
        camp_list_page = get_campaigns_list_page
        segments_page = camp_list_page.go_to_segments_page()
        segments_page.create_first_segment('Test1')
        segments_page.delete_segment()
        self.driver.refresh()
        with pytest.raises(NoSuchElementException):
            segments_page.find(segments_page.locators.SEGMENT_NAME_ELEM)
