import os

import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright

from aqa.config.device_config import DeviceConfig
from aqa.utils.enums import BrowserType, DeviceType


@pytest.fixture(scope="session")
def playwright_instance():
    """Create a Playwright instance for the test session."""
    playwright = sync_playwright().start()
    yield playwright
    playwright.stop()


@pytest.fixture(scope="session", params=[browser.value for browser in BrowserType])
def browser(request, playwright_instance) -> Browser:
    """Create a browser instance for the test session.

    Parametrized to run tests against multiple browsers from BrowserType enum.
    Run specific browser: pytest -k "chromium" or similar
    Run all: pytest

    Control headless mode with environment variable:
    - HEADLESS=true (default): Run browser in headless mode
    - HEADLESS=false: Show browser UI during test
    """
    browser_name = request.param
    headless = os.getenv("HEADLESS", "true").lower() == "true"
    browser = getattr(playwright_instance, browser_name).launch(headless=headless)
    yield browser
    browser.close()


@pytest.fixture(params=[device.value for device in DeviceType])
def device_type(request) -> DeviceType:
    """Parametrized fixture for different device types.

    Run all device types: pytest
    Run desktop only: pytest -k desktop
    Run mobile only: pytest -k mobile
    """
    return DeviceType(request.param)


@pytest.fixture
def context(browser: Browser, device_type: DeviceType) -> BrowserContext:
    """Create a new browser context for each test with device configuration.

    Automatically applies viewport and device emulation settings.
    """
    context_options = DeviceConfig.get_context_options(device_type)
    context = browser.new_context(**context_options)
    yield context
    context.close()


@pytest.fixture
def page(context: BrowserContext) -> Page:
    """Create a new page for each test."""
    page = context.new_page()
    yield page
    page.close()
