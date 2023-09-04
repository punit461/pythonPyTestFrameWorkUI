from locators.login_page_locators import DPLocators
from utility.base import BaseClass


class DashboardPage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    def global_search_box_click(self):
        self.click_element(DPLocators.txt_search)

    def do_click_on_search_send_value(self, value):
        self.global_search_box_click()
        self.send_keys(DPLocators.txt_search, value)
        self.click_element(DPLocators.drp_product)
