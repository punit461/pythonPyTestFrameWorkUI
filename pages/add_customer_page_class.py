from locators.add_customer_locators import ACLocators
from utility.base import BaseClass


class CustomerPage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    def click_customer_menu(self):
        self.click_element(ACLocators.lnk_customers_menu)

    def click_customer_submenu(self):
        self.click_element(ACLocators.lnk_customers_menu_item)

    def click_add_new(self):
        self.click_element(ACLocators.btn_add_new)

    def set_email(self, email):
        self.send_keys(ACLocators.txt_email, email)

    def set_password(self, password):
        self.send_keys(ACLocators.txt_password, password)

    def set_fname(self, fname):
        self.send_keys(ACLocators.txt_first_name, fname)

    def set_lname(self, lname):
        self.send_keys(ACLocators.txt_last_name, lname)

    def set_gender(self, gender):
        if gender.lower() == 'male':
            self.click_element(ACLocators.rd_female_gender)
        else:
            self.click_element(ACLocators.rd_female_gender)

    def set_dob(self, dob):
        self.send_keys(ACLocators.txt_dob, dob)

    def set_company_name(self, company_name):
        self.send_keys(ACLocators.txtCompanyName, company_name)

    def set_manage_of_vendor(self, vendor):
        self.select_dropdown_by_text(ACLocators.drpmgr_of_vendor, vendor)

    def set_admin_comment(self, text):
        self.send_keys(ACLocators.txt_admin_comment, text)

    def click_save_btn(self):
        self.click_element(ACLocators.btn_save)
