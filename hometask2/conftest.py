import pytest

from dataclasses import dataclass
from ui.fixtures import *
from api.fixtures import *


def pytest_addoption(parser):
    parser.addoption('--url', default='https://target.my.com/')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='80.0.3987.106')
    parser.addoption('--download_dir', default='/home/qunity/Загрузки/temp')
    parser.addoption('--user_email', default='test_target_my@mail.ru')
    parser.addoption('--user_password', default='Testtargetmy2020')
    parser.addoption('--selenoid', default=None)
    parser.addoption('--api_url', default='https://target.my.com/')


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')
    download_dir = request.config.getoption('--download_dir')
    user_email = request.config.getoption('--user_email')
    user_password = request.config.getoption('--user_password')
    selenoid_remote_ser = request.config.getoption('--selenoid')

    return {'browser': browser, 'version': version, 'url': url, 'download_dir': download_dir, 'user_email': user_email, 'user_password': user_password, 'selenoid_remote_ser': selenoid_remote_ser}


@dataclass
class ApiSettings:
    url: str = None
    user_email: str = None
    user_password: str = None


@pytest.fixture(scope='session')
def config_api(request) -> ApiSettings:
    settings = ApiSettings(url=request.config.getoption('--api_url'), user_email=request.config.getoption('--user_email'), user_password=request.config.getoption('--user_password'))
    return settings
