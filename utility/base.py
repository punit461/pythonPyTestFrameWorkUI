from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import time
import os
from utility.config_reader import ConfigReader
from test_suites import project_directory


class BaseClass:

    def __init__(self, driver):
        self.driver = driver
        self.config_reader = ConfigReader()

    def locate_element(self, locator, timeout=None):
        if timeout is None:
            timeout = self.config_reader.get_timeout()

        try:
            element = WebDriverWait(self.driver, timeout).until(
                ec.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            raise Exception(f"Element {locator} not found within {timeout} seconds.")

    def click_element(self, locator, timeout=None):

        element = self.locate_element(locator, timeout)
        element.click()

    def send_keys(self, locator, text, timeout=None):

        element = self.locate_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def select_dropdown_by_text(self, locator, text, timeout=None):
        try:
            element = self.locate_element(locator, timeout)
            select = Select(element)
            select.select_by_visible_text(text)

        except Exception as e:
            raise Exception(f"An error occurred:{str(e)}")



    def take_screenshot(self, screenshot_name):
        timestamp = time.strftime('%Y%m%d%H%M%S')
        screenshot_path = f"reporting/screenshots/{screenshot_name}_{timestamp}.png"
        self.driver.save_screenshot(screenshot_path)
        return screenshot_path

    # def assertion(condition, failure_message="Assertion failed"):
    #     try:
    #         assert condition
    #         return "passed"
    #     except AssertionError as e:
    #         print(failure_message, e)
    #         raise e
    #         return "failed"
