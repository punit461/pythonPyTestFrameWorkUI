import os
import sys
import random
import allure
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page_class import LoginPage
from pages.add_customer_page_class import CustomerPage
from test_cases import project_directory
from utility.custom_logger import logmethod
from test_cases.test_base import setup
from utility.test_data_reader import ReadData


@pytest.mark.usefixtures("setup")
class TestCustomerPage:

    @allure.story("Add Customer")
    @allure.title("verify Add Customer Functionality")
    @logmethod
    def test_add_customer(self, setup):
        driver, config_reader = setup
        print("Verify user should be able to create new customer")
        with allure.step("Step 1: Read the test data from json file"):
            self.read_test_data = ReadData()
            # json file name & Read the data from data file
            json_file = project_directory + r"\test_data\jsons\test_data_add_user.json"
            set_email = str(random.randint(1, 100)) + self.read_test_data.read_json(json_file, "email")
            set_password = self.read_test_data.read_json(json_file, "password")
            first_name = self.read_test_data.read_json(json_file, "first_name")
            last_name = self.read_test_data.read_json(json_file, "last_name")
            gender = self.read_test_data.read_json(json_file, "gender")
            dob = self.read_test_data.read_json(json_file, "dob")
            company_name = self.read_test_data.read_json(json_file, "company_name")
            vendor = self.read_test_data.read_json(json_file, "vendor")
            comment = self.read_test_data.read_json(json_file, "comment")
            success_msg = self.read_test_data.read_json(json_file, "success_msg")

        with allure.step("Step 2: Perform Login Functionality"):
            # perform login
            username = config_reader.get_username()
            password = config_reader.get_password()
            login_page = LoginPage(driver)
            login_page.login(username, password)

        with allure.step("Step 3: Navigating Into dashboard page & Click Customer Menu"):
            customer_page = CustomerPage(driver)
            customer_page.click_customer_menu()

        with allure.step("Step 4: Click Customer Submenu & Click Add new button"):
            customer_page.click_customer_submenu()
            customer_page.click_add_new()

        with allure.step("Step 5: Fill the Data in the Form"):
            print("WebApp Page Title after Clicking Customers Button -", driver.title)
            customer_page.set_email(set_email)
            customer_page.set_password(set_password)
            customer_page.set_fname(first_name)
            customer_page.set_lname(last_name)
            customer_page.set_gender(gender)
            customer_page.set_dob(dob)
            customer_page.set_company_name(company_name)
            customer_page.set_manage_of_vendor(vendor)
            customer_page.set_admin_comment(comment)

        with allure.step("Step 6: Click Save Button"):
            customer_page.click_save_btn()

        with allure.step("Step 7: Validate Customer Added Successfully"):
            assert (driver.page_source.__contains__(success_msg))
            print("Customer Added Successfully")
