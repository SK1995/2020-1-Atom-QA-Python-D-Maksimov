import os
import pytest

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from ui.pages.base import BaseActions
from ui.pages.campaigns_list_page import CampaignsListPage
from ui.pages.login_page import LoginPage
from utils.exceptions import UnsupportedBrowserException


@pytest.fixture(scope='function')
def base_actions(driver):
    return BaseActions(driver)


@pytest.fixture(scope='function')
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope='function')
def campaigns_list_page(driver):
    return CampaignsListPage(driver)


@pytest.fixture(scope='function')
def get_campaigns_list_page(login_page, campaigns_list_page, config):
    return login_page.login_in(email=config['user_email'], password=config['user_password'])


@pytest.fixture(scope='function')
def create_temp_campaign(get_campaigns_list_page, get_img_path_to_upload):
    camp_list_page = get_campaigns_list_page
    camp_list_page.create_first_campaign('Test1', get_img_path_to_upload)
    yield camp_list_page
    camp_list_page.remove_all_campaigns()


@pytest.fixture(scope='function')
def get_img_path_to_upload():
    return os.path.abspath('hometask2/stuff/cat.jpg')


@pytest.fixture(scope='function')
def create_temp_segment(get_campaigns_list_page):
    camp_list_page = get_campaigns_list_page
    segments_page = camp_list_page.go_to_segments_page()
    segments_page.create_first_segment('Test1')
    yield segments_page
    segments_page.delete_segment()


@pytest.fixture(scope='function')
def driver(config):
    browser = config['browser']
    version = config['version']
    url = config['url']
    download_dir = config['download_dir']
    selenoid_remote_ser = config['selenoid_remote_ser']

    if browser == 'chrome':
        if selenoid_remote_ser is None:
            options = ChromeOptions()

            prefs = {"download.default_directory": download_dir}
            options.add_experimental_option('prefs', prefs)

            manager = ChromeDriverManager(version=version)
            driver = webdriver.Chrome(executable_path=manager.install(),
                                      options=options,
                                      desired_capabilities={'acceptInsecureCerts': True}
                                      )
        else:
            options = ChromeOptions()
            prefs = {"download.default_directory": download_dir}
            options.add_experimental_option('prefs', prefs)

            capabilities = {'acceptInsecureCerts': True,
                            'browserName': browser,
                            'version': '80',
                            }

            driver = webdriver.Remote(command_executor='http://' + str(selenoid_remote_ser) + '/wd/hub/',
                                      options=options,
                                      desired_capabilities=capabilities
                                      )
    elif browser == 'firefox':
        manager = GeckoDriverManager(version=version)
        driver = webdriver.Firefox(executable_path=manager.install())

    else:
        raise UnsupportedBrowserException(f'Usupported browser: "{browser}"')

    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.close()


@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def all_drivers(config, request):
    browser = request.param
    url = config['url']

    if browser == 'chrome':
        manager = ChromeDriverManager(version='latest')
        driver = webdriver.Chrome(executable_path=manager.install())

    elif browser == 'firefox':
        manager = GeckoDriverManager(version='latest')
        driver = webdriver.Firefox(executable_path=manager.install())

    else:
        raise UnsupportedBrowserException(f'Usupported browser: "{browser}"')

    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.close()
