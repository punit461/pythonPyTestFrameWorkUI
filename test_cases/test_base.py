from datetime import datetime
from pathlib import Path

import pytest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utility.config_reader import ConfigReader
from utility.driver_manager import DriverManager
from utility.custom_logger import capture_screenshot
from utility.generate_filename import generate_report_filename
from test_cases import project_directory


@pytest.fixture(scope="function", autouse=True)
def setup(request):
    config_reader = ConfigReader()
    driver_manager = DriverManager()
    driver = driver_manager.get_driver()
    driver.maximize_window()
    driver.get(config_reader.get_baseurl())

    fail_flag_before_tc = request.session.testsfailed

    # Attach the driver to the request object, so it can be accessed in test methods.
    request.cls.driver = driver
    request.cls.config_reader = config_reader

    yield driver, config_reader

    # Add teardown code here
    screenshot_mode = str(config_reader.get_ss_mode())
    current_test_name = request.node.name
    fail_flag_after_tc = request.session.testsfailed
    print(f"Test Case {current_test_name} Executed")
    if screenshot_mode == 'after_every_test_case':
        capture_screenshot(driver, current_test_name)
    elif screenshot_mode == 'on_failure':
        # screenshot capture only when test case failed. temporary fix
        # This will be unstable if running test case in parallel
        if fail_flag_after_tc - fail_flag_before_tc == 1:
            capture_screenshot(driver, current_test_name)
    else:
        print("Screenshot Capture Mode turned off")

    driver.close()
    driver.quit()


