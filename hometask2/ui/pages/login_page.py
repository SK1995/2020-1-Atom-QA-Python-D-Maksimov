from ui.locators.locators import LoginPageLocators
from ui.pages.base import BaseActions
from ui.pages.campaigns_list_page import CampaignsListPage
from utils.exceptions import InvalidLoginInfoException, NoSuchElementException


class LoginPage(BaseActions):

    locators = LoginPageLocators()

    def click_main_login_button(self):
        self.click(self.locators.MAIN_LOGIN_BUTTON)

    def paste_login_info(self, email, password):
        self.paste_some_query_into_form(self.locators.EMAIL_FIELD, email)
        self.paste_some_query_into_form(self.locators.PASSWORD_FIELD, password)

    def click_sub_login_button(self):
        self.click(self.locators.SUB_LOGIN_BUTTON)

    def login_in(self, email, password):
        self.click_main_login_button()
        self.paste_login_info(email, password)
        self.click_sub_login_button()
        try:
            if self.check_available_of_element(self.locators.INCORRECT_EMAIL_OR_TEL_NUMBER__ELEMENT):
                raise InvalidLoginInfoException(f'Invalid email/telephone number "{email}" or password "{password}"')
        except NoSuchElementException:
            try:
                if self.check_available_of_element(self.locators.INVALID_LOGIN_OR_PASSWORD_ELEMENT):
                    raise InvalidLoginInfoException(f'Invalid email/telephone number "{email}" or password "{password}"')
            except NoSuchElementException:
                return CampaignsListPage(self.driver)
