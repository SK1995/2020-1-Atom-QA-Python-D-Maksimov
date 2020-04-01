from ui.locators.locators import SegmentsPageLocators
from ui.pages.base import BaseActions


class SegmentsPage(BaseActions):

    locators = SegmentsPageLocators()

    def click_to_create_first_segment_button(self):
        self.click(self.locators.FIRST_SEGMENT_BUTTON)

    def click_to_audience_segments_button(self):
        self.click(self.locators.ADD_AUDIENCE_SEGMENTS_BUTTON)

    def configure_segment(self):
        self.click(self.locators.CHECKBOX1_1)
        self.click(self.locators.CHECKBOX1_2)
        self.click(self.locators.SUBMIT_CONFIGURE_SEGMENT_BUTTON)

    def set_segment_name(self, name):
        self.paste_some_query_into_form(self.locators.SEGMENT_NAME_FIELD, name)

    def click_to_submit_create_segment_button(self):
        self.click(self.locators.SUBMIT_CREATE_SEGMENT_BUTTON)

    def create_first_segment(self, name):
        self.click_to_create_first_segment_button()
        self.click_to_audience_segments_button()
        self.configure_segment()
        self.set_segment_name(name)
        self.click_to_submit_create_segment_button()

    def delete_segment(self):
        self.click(self.locators.DELETE_SEGMENT_BUTTON)
        self.click(self.locators.CONFIRM_DELETE_SEGMENT_BUTTON)

    def click_to_create_new_segment_button(self):
        self.click(self.locators.NEW_SEGMENT_BUTTON)

    def create_new_segment(self, name):
        self.click_to_create_new_segment_button()
        self.click_to_audience_segments_button()
        self.click(self.locators.CHECKBOX2_1)
        self.click(self.locators.SUBMIT_CONFIGURE_SEGMENT_BUTTON)
        self.set_segment_name(name)
        self.click_to_submit_create_segment_button()