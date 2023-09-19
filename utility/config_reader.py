import configparser
import os
from test_cases import project_directory


# Initialize the configparser
class ConfigReader:
    """
        A class for reading configuration from an INI file.
    """

    def __init__(self, config_path=project_directory + r'\configurations\config.ini'):
        """
               Initialize the ConfigReader.
               Args:
                   config_path (str): The path to the configuration INI file.
        """
        if config_path is None:
            config_path = os.path.join(project_directory, 'configurations', 'config.ini')

        self.config = configparser.ConfigParser()
        self.config.read(config_path)

    def get_value(self, section, key):
        return self.config.get(section, key)

    # Read data from the 'URLs' section
    def get_baseurl(self):
        base_env = self.get_value('URLs', 'base_env')
        if base_env == "test_env":
            return self.get_value('URLs', 'test_env')
        elif base_env == "dev_env":
            return self.get_value('URLs', 'dev_env')
        elif base_env == "stage_env":
            return self.get_value('URLs', 'stage_env')
        else:
            return self.get_value('URLs', 'prod_env')

    # Read data from the 'Credentials' section
    def get_username(self):
        return self.get_value('Credentials', 'username_admin')

    def get_password(self):
        return self.get_value('Credentials', 'password_admin')

    # Read the Settings value
    def get_timeout(self):
        return self.get_value('Settings', 'default_timeout')

    def get_browser(self):
        return self.get_value('Settings', 'default_browser')

    def get_browser_headless(self):
        return self.get_value('Settings', 'headless')

    # should be deprecated Since the Selenium manager only manages the driver from Selenium 4.6
    def get_browser_path(self, browser_name):
        if browser_name.lower() == 'chrome':
            return self.get_value('Paths', 'chromeD_path')
        elif browser_name.lower == 'firefox':
            return self.get_value('Paths', 'firefoxD_path')
        elif browser_name.lower == 'edge':
            return self.get_value('Paths', 'edgeD_path')
        else:
            return self.get_value('Paths', 'D_path')

    def get_ss_mode(self):
        return self.get_value('Automation', 'screenshot_mode')

    def get_log_mode(self):
        return self.get_value('Automation', 'log_mode')

    def get_ss_allure_mode(self):
        return self.get_value('Automation', 'attach_screenshot_allure_html_report')
