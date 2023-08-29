from locators.add_customer_locators import ACLocators
from locators.login_page_locators import LPLocators
from utility.base import BaseClass


class CustomerPage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    def click_customer_menu(self):
        self.click_element(ACLocators.lnkCustomers_menu)

    def click_customer_submenu(self):
        self.click_element(ACLocators.lnkCustomers_menuitem)

    def click_add_new(self):
        self.click_element(ACLocators.btnAddnew)

    def set_email(self, email):
        self.send_keys(ACLocators.txtEmail, email)

    def set_password(self, password):
        self.send_keys(ACLocators.txtPassword, password)

    def set_fname(self, fname):
        self.send_keys(ACLocators.txtFirstName, fname)

    def set_lname(self, lname):
        self.send_keys(ACLocators.txtLastName, lname)

    def set_gender(self, gender):
        if gender.lower() == 'male':
            self.click_element(ACLocators.rdFeMaleGender)
        else:
            self.click_element(ACLocators.rdFeMaleGender)

    def set_dob(self, dob):
        self.send_keys(ACLocators.txtDob, dob)

    def set_company_name(self, companyName):
        self.send_keys(ACLocators.txtCompanyName, companyName)

    def set_manage_of_vendor(self, vendor):
        self.select_dropdown_by_text(ACLocators.drpmgrOfVendor, vendor)

    def set_admin_comment(self, text):
        self.send_keys(ACLocators.txtAdminComment, text)

    def click_save_btn(self):
        self.click_element(ACLocators.btnSave)