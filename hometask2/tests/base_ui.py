import pytest

from ui.pages.base import BaseActions
from ui.pages.campaigns_list_page import CampaignsListPage
from ui.pages.login_page import LoginPage


class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request):
        self.driver = driver
        self.config = config
        self.base_actions: BaseActions = request.getfixturevalue('base_actions')
        self.login_page: LoginPage = request.getfixturevalue('login_page')
        self.campaigns_list_page: CampaignsListPage = request.getfixturevalue('campaigns_list_page')
        self.user_email = config['user_email']
        self.user_password = config['user_password']
