import configparser
from test_cases import project_directory


# Initialize the configparser
class ConfigReader:
    def __init__(self, config_path=project_directory + '\configurations\config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_path)

    def get_value(self, section, option):
        return self.config.get(section, option)

    # Read data from the 'URLs' section
    def get_baseurl(self):
        baseEnv = self.get_value('URLs', 'baseEnv')
        if baseEnv == "testEnv":
            return self.get_value('URLs', 'testEnv')
        elif baseEnv == "devEnv":
            return self.get_value('URLs', 'devEnv')
        elif baseEnv == "stageEnv":
            return self.get_value('URLs', 'stageEnv')
        else:
            return self.get_value('URLs', 'prodEnv')

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

    # should be depricated Since the Selenium manager only manages the driver from Selenium 4.6
    def get_browser_path(self, browserName):
        if browserName.lower() == 'chrome':
            return self.get_value('Paths', 'chromeD_path')
        elif browserName.lower == 'firefox':
            return self.get_value('Paths', 'firefoxD_path')
        elif browserName.lower == 'edge':
            return self.get_value('Paths', 'edgeD_path')
        else:
            return self.get_value('Paths', 'D_path')

    def get_ss_mode(self):
        return self.get_value('Automation', 'screenshot_mode')

    def get_log_mode(self):
        return self.get_value('Automation', 'log_mode')