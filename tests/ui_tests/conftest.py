import os

import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright

from aqa.enums import BrowserType


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


@pytest.fixture
def context(browser: Browser) -> BrowserContext:
    """Create a new browser context for each test."""
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def page(context: BrowserContext) -> Page:
    """Create a new page for each test."""
    page = context.new_page()
    yield page
    page.close()
