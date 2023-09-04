from selenium.webdriver.common.by import By


class ACLocators:
    # Add customer Page
    lnk_customers_menu = (By.XPATH, "//a[@href='#']//*[contains(text(),'Customers')]")
    lnk_customers_menu_item = (By.XPATH, "//a[@href='/Admin/Customer/List']//*[contains(text(),'Customers')]")
    btn_add_new = (By.XPATH, "//a[@href='/Admin/Customer/Create']//*[@class='fas fa-plus-square']")
    txt_email = (By.XPATH, "//input[@id='Email']")
    txt_password = (By.XPATH, "//input[@id='Password']")
    txt_first_name = (By.XPATH, "//input[@id='FirstName']")
    txt_last_name = (By.XPATH, "//input[@id='LastName']")
    rd_male_gender = (By.ID, "Gender_Male")
    rd_female_gender = (By.ID, "Gender_Female")
    txt_dob = (By.XPATH, "//input[@id='DateOfBirth']")
    txtCompanyName = (By.XPATH, "//input[@id='Company']")
    txt_customer_roles = (By.XPATH, "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]")
    lst_item_administrators = (By.XPATH, "//li[contains(text(),'Administrators')]")
    lst_item_registered = (By.XPATH, "//li[contains(text(),'Registered')]")
    lst_item_guests = (By.XPATH, "//li[contains(text(),'Guests')]")
    lst_item_vendors = (By.XPATH, "//li[contains(text(),'Vendors')]")
    drpmgr_of_vendor = (By.XPATH, "//*[@id='VendorId']")
    txt_admin_comment = (By.XPATH, "//textarea[@id='AdminComment']")
    btn_save = (By.XPATH, "//button[@name='save']")
