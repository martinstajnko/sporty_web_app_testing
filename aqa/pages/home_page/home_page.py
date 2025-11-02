from playwright.sync_api import Page

from aqa.enums import Urls
from aqa.pages.base_page import BasePage
from .home_page_locator import HomePageLocators


class HomePage(BasePage):
    """Page Object for Twitch Home page and search functionality."""
    
    BASE_URL = Urls.TWITCH_HOME.value
    
    def __init__(self, page: Page):
        """Initialize HomePage with a Playwright Page instance."""
        super().__init__(page)
        self.locators = HomePageLocators()
    
    def navigate(self) -> None:
        """Navigate to Twitch homepage."""
        super().navigate()
    
    def reject_cookies(self) -> None:
        """Click the reject cookies button."""
        self.page.get_by_role("button", name="Reject").click()
    
    def search_for(self, query: str) -> None:
        """Search for a query on Twitch."""
        search_box = self.page.get_by_role("searchbox", name="Search Input")
        search_box.click()
        search_box.fill(query)
        search_box.press("Enter")
    
    def navigate_to_first_suggestion(self) -> None:
        """Navigate to the first search suggestion."""
        search_box = self.page.get_by_role("searchbox", name="Search Input")
        search_box.click()
        search_box.press("ArrowDown")
        search_box.press("Enter")
