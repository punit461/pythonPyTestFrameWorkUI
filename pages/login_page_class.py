from locators.login_page_locators import LPLocators
from utility.base import BaseClass


class LoginPage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        self.send_keys(LPLocators.txt_username, username)

    def enter_password(self, password):
        self.send_keys(LPLocators.txt_password, password)

    def click_login_button(self):
        self.click_element(LPLocators.btn_login)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
