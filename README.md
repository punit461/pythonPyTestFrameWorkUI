# UI Automation Framework using Pytest

Welcome to the UI Automation Framework using Pytest! This framework is designed to simplify the automation of user interface testing using Selenium and Python's pytest framework. It follows the Page Object Model (POM) design pattern for improved maintainability and readability.
## Project Structure

The project is structured as follows:

- `Configurations`: Configuration files and settings related to the automation setup.
- `Locators`: Element locators (selectors) for the application's pages.
- `Pages`: Page Object classes encapsulating elements and methods for each page.
- `Reporting`: Handles different types of reports and logs.
  - `HtmlReports`: HTML reports generated from test runs.
  - `Logs`: Log files for debugging and tracking test execution.
  - `Screenshots`: Screenshots captured during test runs.
- `TestData`: Test data that might be used by tests.
- `TestSuites`: Test suite files that group and execute tests.
- `Utilities`: Utility modules and common functions for the framework.
- `.idea`: IDE-specific settings (created by the IDE).
- `venv`: Virtual environment directory.

### Project Tree
``` tree -O
PythonUnitTestFrameWork
│   README.md
│   __init__.py
│
│
├───configurations
│       config.ini
│
├───drivers
│       chromedriver.exe
│       geckodriver.exe
│       msedgedriver.exe
│
├───locators
│       login_page_locators.py
│       __init__.py
│   
│
├───pages
│       login_page_class.py
│       __init__.py
│
├───reporting
│   ├───html_reports
│   │       TestResults_test_cases.{test_cases_login_page.TestLoginPage_{yyyy-MM-DD_hh-mm-ss}.html
│   │
│   ├───logs
│   │       logs.log
│   │       test_{test_method_name}.log
│   │
│   └───screenshots
│       └───Test_execution_2023-08-25
│               test_{test_method_name}_{yyyy-MM-DD_hh-mm-ss}.png
│
├───test_cases
│       test_base.py
│       test_cases_login_page.py
│       __init__.py
│    
│
├───test_data
│		test_data_homepage.json
│
├───test_suites
│       test_suite_login_page.py
│       __init__.py
│   
│
└───utility
        base.py
        config_reader.py
        custom_logger.py
        driver_manager.py
        __init__.py
```

## Getting Started

1. Clone this repository to your local machine.
2. Set up a virtual environment in the `venv` directory.
3. Install required dependencies using `pip install -r requirements.txt`.
4. Update configuration files in the `Configurations` directory as needed.
5. Define page locators in the `Locators` directory.
6. Create Page Object classes in the `Pages` directory.
7. Organize test data in the `TestData` directory.
8. Create test case files in the `TestCases` directory.
9. Run tests using `pytest `.

## _Tools & Technologies Used_
_Python_, _Selenium_, _pytest_, _Allure_.

## Running Tests

To run the tests, navigate to the project root directory and execute the following command:

```bash
pytest test_cases

```
## Reporting
* HTML reports can be found in the `reports/html_reports` directory.
* Logs are stored in the `reports/logs` directory.
* Screenshots from test runs are saved in the `reports/screenshots` directory.

## Contributing
Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
