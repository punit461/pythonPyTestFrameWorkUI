import functools
import logging
import os
import allure
from test_cases import project_directory
from utility.config_reader import ConfigReader
from utility.generate_filename import generate_ss_folder, generate_ss_filename

config_reader = ConfigReader()


def setup_custom_logger(name):
    log_dir = os.path.join(project_directory, "reporting", "logs")
    os.makedirs(log_dir, exist_ok=True)

    # Read log_mode and generate logs based on it.
    log_mode = config_reader.get_log_mode()

    if log_mode == "each_test_case_log_file":
        log_file = os.path.join(log_dir, f'{name}.log')
    else:
        log_file = os.path.join(log_dir, 'logs.log')

    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger


def logmethod(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = setup_custom_logger(func.__name__)

        try:
            result = func(*args, **kwargs)
            logger.info(f"{func.__name__} completed successfully.")
            return result
        except Exception as e:
            logger.error(f"Test {func.__name__} FAILED")
            logger.exception(e)
            raise e
        finally:
            logger.info(f"Finished test: {func.__name__}")

    return wrapper


def allure_ss_attach(driver, name):
    allure.attach(
        driver.get_screenshot_as_png(),
        name=name,
        attachment_type=allure.attachment_type.PNG
    )


def capture_screenshot(driver, name="screenshot"):
    # read the config
    ss = str(config_reader.get_ss_mode().lower())
    allure_ss = str(config_reader.get_ss_allure_mode().lower())

    # folder and filename setup
    folder_name = generate_ss_folder()
    screenshot_dir = os.path.join(project_directory, 'reporting', 'screenshots', folder_name)
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshot_dir, f'{name}_{generate_ss_filename()}')

    # implement the logic
    if allure_ss == 'yes':
        if ss == "off":
            allure_ss_attach(driver, name)
        else:
            allure_ss_attach(driver, name)
            driver.save_screenshot(screenshot_path)
    else:
        if not ss == "off":
            driver.save_screenshot(screenshot_path)
        else:
            print("All Screenshot Capture Mode Turned Off")
