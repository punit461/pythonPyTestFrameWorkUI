import time

from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from utility.config_reader import ConfigReader


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
        if timeout is None:
            timeout = self.config_reader.get_timeout()

        try:
            element = WebDriverWait(self.driver, timeout).until(
                ec.element_to_be_clickable(locator)
            )
        except TimeoutException:
            raise Exception(f"Element {locator} not found within {timeout} seconds.")

        element.click()

    def send_keys(self, locator, text, timeout=None):

        element = self.locate_element(locator, timeout)

        if timeout is None:
            timeout = self.config_reader.get_timeout()

        try:
            # Wait for the element to be clickable
            WebDriverWait(self.driver, timeout).until(
                ec.element_to_be_clickable(locator)
            )

            # Clear the element and send keys
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            raise Exception(f"Element {locator} not clickable within {timeout} seconds.")
        except ElementNotInteractableException:
            raise Exception(f"Element {locator} not interactable.")

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
