# Sporty Home Test: Web App Testing 
## Overview
Project contains UI test, using Playwright Framework.
Main package is `aqa`, containing page objects, configuration, and utilities.
Tests are located in the `tests` directory, separated into `ui_tests` and `api_tests`.

1. UI tests are organized to allow running by device type and browser.
2. API tests utilize a base client for common HTTP methods and session management.

## Requirements
To run Sporty Home Test, ensure that you have the following:

- Python 3.11.4 or newer: Make sure you have Python installed on your system.
- Poetry: Use Poetry for packaging and dependency management. Refer to the Poetry documentation for installation instructions. 
Link -> `https://python-poetry.org/`

Clone the project: Clone the project repository and perform `poetry install` to install the required dependencies.

## Project Structure
├── tests/                   # Test cases
│   ├── test_demo.py     # Sample UI test using Playwright
├── aqa/                     # Automation framework code
│   ├── pages/               # Page Object Models
│   ├── config/              # Configuration files
│   └── utils/               # Utility functions and classes

## Running UI Tests
By default, tests run in headless mode (without browser UI). To run tests with a visible browser, set the `HEADLESS` environment variable to `false`. 

Example 
```bash
# Run all tests with browser UI
HEADLESS=false poetry run pytest tests/test_demo.py -v
```

### Run All UI Tests
```bash
# Run all tests headless (no browser UI)
poetry run pytest tests/test_demo.py -v -s 
```

### Run Test/s by Browser
```bash
# Run all tests with a specific browser
poetry run pytest tests/test_demo.py -v -s -k <browser_name>
```

### Run Test/s by Device Type
```bash
# Run all tests with a specific device type
poetry run pytest tests/test_demo.py -v -s -k <device_type>
```

### Run a specific test with all browsers
```bash
poetry run pytest tests/test_demo.py::test_search_starcraft_on_twitch -v
```