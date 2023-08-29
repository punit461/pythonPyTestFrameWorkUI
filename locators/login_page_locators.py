from selenium.webdriver.common.by import By


# Login Page Locators
class LPLocators:
    """
    In the Beginning define what type of element it is
    for Example -> lnk - Link, btn - button, txt - textbox,
    rd - radiobutton, lst - List, drpmgr - drop down manager
    """
    txt_username = (By.ID, 'Email')
    txt_password = (By.ID, 'Password')
    btn_login = (By.XPATH, "//button[text()='Log in']")


# Dashboard Page Locators
class DPLocators:
    """ This is a demonstration for how to create multiple
    classes and store locators
    """
    txt_search = (By.XPATH, "//input[@placeholder='Search']")
    drp_product = (By.XPATH, "//div[@id='user-selection'][1]")
    btn_add_new = (By.XPATH, "//a[contains(@href, '/Admin/ProductAttribute/Create')]")

