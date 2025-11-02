from playwright.sync_api import Page

from aqa.enums import Urls


class BasePage:
    """Base class for all page objects."""
     
    def __init__(self, page: Page):
        """Initialize BasePage with a Playwright Page instance."""
        self.page = page
    
    def navigate(self, path: str = "") -> None:
        """Navigate to the page URL."""
        url = Urls.TWITCH_HOME.value
        self.page.goto(url)
    
    def wait_for_load_state(self, state: str = "networkidle") -> None:
        """Wait for the page to reach a specific load state."""
        self.page.wait_for_load_state(state)
    
    def take_screenshot(self, filename: str) -> None:
        """Take a screenshot of the current page."""
        self.page.screenshot(path=f"screenshots/{filename}")
