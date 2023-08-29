# from test_cases.test_base import
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page_class import LoginPage
from utility.custom_logger import logmethod
from test_cases.test_base import setup
import pytest


@pytest.mark.usefixtures("setup")
class TestLoginPage:

    @logmethod
    def test_successful_login(self, setup):
        driver, config_reader = setup
        print("Verify Login Functionality of NopCommerce WebApp")
        username = config_reader.get_username()
        password = config_reader.get_password()

        login_page = LoginPage(driver)
        login_page.login(username, password)
        print("WebApp Page Title after Login -", driver.title)
        # Add assertions to verify successful login
        assert (driver.title == "Dashboard / nopCommerce administration")

    @logmethod
    def test_failure_login(self, setup):
        driver, config_reader = setup
        print("Verify Login Functionality of NopCommerce WebApp")
        username = config_reader.get_username()
        password = config_reader.get_password()

        login_page = LoginPage(driver)
        login_page.login(username, password)
        print("WebApp Page Title after Login -", driver.title)
        # Add assertions to verify successful login
        assert (driver.title == "Fail")
