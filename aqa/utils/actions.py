from playwright.sync_api import Page

from aqa.utils.enums import Urls, WaitStates



class Actions:
    """ """
     
    def __init__(self, page: Page):
        """Initialize BasePage with a Playwright Page instance."""
        self.page = page
    
    def navigate(self, url: Urls = "www.google.com") -> None:
        """Navigate to the page URL."""
        self.page.goto(url.value)
    
    def wait_for_load_state(self, state: WaitStates = WaitStates.NETWORKIDLE) -> None:
        """Wait for the page to reach a specific load state."""
        self.page.wait_for_load_state(state.value)
    
    def take_screenshot(self, filename: str) -> None:
        """Take a screenshot of the current page."""
        self.page.screenshot(path=f"screenshots/{filename}")
