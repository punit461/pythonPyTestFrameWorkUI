import os
import sys

import allure
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page_class import LoginPage
from utility.custom_logger import logmethod
from test_cases.test_base import setup
from test_cases.test_base import TestHandler


@pytest.mark.usefixtures("setup")
class TestLoginPage:
    #
    # @allure.story("Successful Login")
    # @allure.title("verify successful login")
    # @logmethod
    # def test_successful_login(self, setup):
    #     driver, config_reader = setup
    #     print("Verify Login Functionality of NopCommerce WebApp")
    #     username = config_reader.get_username()
    #     password = config_reader.get_password()
    #
    #     login_page = LoginPage(driver)
    #     with allure.step("Step 1: Login with valid credentials"):
    #         login_page.login(username, password)
    #         print("WebApp Page Title after Login -", driver.title)
    #     # Add assertions to verify successful login
    #     with allure.step("Step 2: Verify the login Credentials"):
    #         assert (driver.title == "Dashboard / nopCommerce administration")

    @allure.story("Failure Login")
    @allure.title("verify failure login")
    @logmethod
    def test_failure_login(self, setup):
        driver, config_reader = setup
        print("Verify Login Functionality of NopCommerce WebApp")
        username = config_reader.get_username()
        password = config_reader.get_password()

        login_page = LoginPage(driver)
        with allure.step("Step 1: Login with valid credentials"):
            login_page.login(username, password)
        print("WebApp Page Title after Login -", driver.title)
            # Add assertions to verify successful login
        with allure.step("Step 2: Verify the login Credentials"):
            with TestHandler():
                assert (driver.title == "Fail")
