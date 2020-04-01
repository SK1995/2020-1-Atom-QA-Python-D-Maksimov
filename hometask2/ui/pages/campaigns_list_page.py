from ui.locators.locators import CampaignsListPageLocators
from ui.pages.base import BaseActions
from selenium.webdriver.common.action_chains import ActionChains
from ui.pages.segments_page import SegmentsPage


class CampaignsListPage(BaseActions):

    locators = CampaignsListPageLocators()

    def click_to_create_new_campaign(self):
        self.click(self.locators.FIRST_COMPANY_BUTTON)

    def click_to_goal_of_campaign(self):
        self.click(self.locators.TRAFFIC_GOAL_BUTTON)

    def paste_link_of_campaign(self, link):
        self.paste_some_query_into_form(self.locators.LINK_FIELD, link)

    def paste_budget_per_day_info(self, sum_of_money: int):
        field = self.find(self.locators.BUDGET_PER_DAY_FIELD)
        self.scroll_to_element(field)
        self.paste_some_query_into_form(self.locators.BUDGET_PER_DAY_FIELD, sum_of_money)

    def paste_budget_total_info(self, sum_of_money: int):
        field = self.find(self.locators.BUDGET_TOTAL_FIELD)
        self.scroll_to_element(field)
        self.paste_some_query_into_form(self.locators.BUDGET_TOTAL_FIELD, sum_of_money)

    def set_campaign_name(self, name):
        self.click(self.locators.CLEAR_NAME_FIELD_BUTTON)
        name_field = self.find(self.locators.CAMPAIGN_NAME_FIELD)
        self.scroll_to_element(name_field)
        self.paste_some_query_into_form(self.locators.CAMPAIGN_NAME_FIELD, name)

    def click_banner_button(self):
        self.click(self.locators.BANNER_BUTTON)

    def upload_banner_img(self, get_img_path_to_upload):
        self.upload_file(upload_locator=self.locators.IMG_DROP_FIELD, submit_locator=self.locators.SUBMIT_UPLOAD_BUTTON, file_path=get_img_path_to_upload)

    def click_to_create_campaign_button(self):
        self.click(self.locators.CREATE_CAMPAIGN_BUTTON)

    def create_new_campaign(self, name, get_img_path_to_upload):
        self.click(self.locators.NEW_CAMPAIGN_BUTTON)
        self.click_to_goal_of_campaign()
        self.paste_link_of_campaign('http://test.com')
        self.set_campaign_name(name)
        self.paste_budget_per_day_info(1000)
        self.paste_budget_total_info(1000000)
        self.click_banner_button()
        self.upload_banner_img(get_img_path_to_upload)
        self.click_to_create_campaign_button()

    def create_first_campaign(self, name, get_img_path_to_upload):
        self.click_to_create_new_campaign()
        self.click_to_goal_of_campaign()
        self.paste_link_of_campaign('http://test.com')
        self.set_campaign_name(name)
        self.paste_budget_per_day_info(1000)
        self.paste_budget_total_info(1000000)
        self.click_banner_button()
        self.upload_banner_img(get_img_path_to_upload)
        self.click_to_create_campaign_button()

    def remove_all_campaigns(self):
        self.click(self.locators.CHECKBOX_FOR_ALL_CAMPAIGNS)
        self.click(self.locators.ACTIONS_BUTTON)
        self.click(self.locators.DELETE_BUTTON)
        self.driver.refresh()

    def go_to_segments_page(self):
        self.click(self.locators.SEGMENTS_BUTTON)
        return SegmentsPage(self.driver)