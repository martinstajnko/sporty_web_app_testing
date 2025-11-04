from playwright.sync_api import Page


class HomePage:
    """Page Object for Twitch Home page and search functionality."""
           
    def __init__(self, page: Page):
        """Initialize BasePage with a Playwright Page instance."""
        self.page = page
        
    def reject_cookies(self) -> None:
        """Click the reject cookies button."""
        self.page.get_by_role("button", name="Reject").click()

    def accept_cookies(self) -> None:
        """Click the accept cookies button."""
        self.page.get_by_role("button", name="Accept").click()
    
    def search_for(self, query: str) -> None:
        """Search for a query on Twitch."""
        search_box = self.page.get_by_role("searchbox", name="Search Input")
        search_box.click()
        search_box.fill(query)
        self.page.wait_for_timeout(500)
        search_box.press('ArrowDown')
        search_box.press("Enter")

