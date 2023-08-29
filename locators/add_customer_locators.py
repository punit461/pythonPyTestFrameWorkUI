from selenium.webdriver.common.by import By


class ACLocators:
    # Add customer Page
    lnkCustomers_menu = (By.XPATH, "//a[@href='#']//*[contains(text(),'Customers')]")
    lnkCustomers_menuitem = (By.XPATH, "//a[@href='/Admin/Customer/List']//*[contains(text(),'Customers')]")
    btnAddnew = (By.XPATH, "//a[@href='/Admin/Customer/Create']//*[@class='fas fa-plus-square']")
    txtEmail = (By.XPATH, "//input[@id='Email']")
    txtPassword = (By.XPATH, "//input[@id='Password']")
    txtFirstName = (By.XPATH, "//input[@id='FirstName']")
    txtLastName = (By.XPATH, "//input[@id='LastName']")
    rdMaleGender = (By.ID, "Gender_Male")
    rdFeMaleGender = (By.ID, "Gender_Female")
    txtDob = (By.XPATH, "//input[@id='DateOfBirth']")
    txtCompanyName = (By.XPATH, "//input[@id='Company']")
    txtcustomerRoles = (By.XPATH, "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]")
    lstitemAdministrators = (By.XPATH, "//li[contains(text(),'Administrators')]")
    lstitemRegistered = (By.XPATH, "//li[contains(text(),'Registered')]")
    lstitemGuests = (By.XPATH, "//li[contains(text(),'Guests')]")
    lstitemVendors = (By.XPATH, "//li[contains(text(),'Vendors')]")
    drpmgrOfVendor = (By.XPATH, "//*[@id='VendorId']")
    txtAdminComment = (By.XPATH, "//textarea[@id='AdminComment']")
    btnSave = (By.XPATH, "//button[@name='save']")
