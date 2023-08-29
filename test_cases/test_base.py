import os
import sys
import tracemalloc
import pytest

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utility.config_reader import ConfigReader
from utility.driver_manager import DriverManager
from utility.custom_logger import capture_screenshot
from utility.test_data_reader import ReadData


@pytest.fixture(scope="class")
def setup(request):
    config_reader = ConfigReader()
    driver_manager = DriverManager()
    read_test_data = ReadData()
    driver = driver_manager.get_driver()
    driver.maximize_window()
    driver.get(config_reader.get_baseurl())

    # Attach the driver to the request object, so it can be accessed in test methods.
    request.cls.driver = driver
    request.cls.config_reader = config_reader

    yield driver, config_reader

    # Add teardown code here
    screenshot_mode = str(config_reader.get_ss_mode())
    current_test_name = request.node.name
    print(f"Test Case {current_test_name} Executed")

    if screenshot_mode == 'after_every_test_case':
        capture_screenshot(driver, current_test_name)
    elif screenshot_mode == 'on_failure':
        if request.node.rep_call.failed:
            capture_screenshot(driver, current_test_name)
        else:
            print("Test Case Passed")
    else:
        print("Screenshot Capture Mode turned off")

    tracemalloc.stop()
    driver.close()
    driver.quit()
