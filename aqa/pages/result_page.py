from random import choice

from playwright.sync_api import Page


class ResultPage:
    """Page Object for Twitch Result page of the search results of a query."""

    def __init__(self, page: Page):
        self.page = page

    def scroll_down(self, times: int = 1) -> None:
        """Scroll down the page multiple times.

        Args:
            times: Number of times to scroll down
        """
        for _ in range(times):
            self.page.keyboard.press("End")
            self.page.wait_for_load_state("networkidle")

    def get_all_stream_links(self) -> list:
        """Get all available stream links on the page.

        Returns:
            List of stream link locators
        """
        streams = self.page.get_by_role("link").all()
        return streams

    def click_random_stream(self) -> None:
        """Click on a random stream from available streams."""
        streams = self.get_all_stream_links()

        if not streams:
            raise RuntimeError("No streams found on the page")

        random_stream = choice(streams)
        random_stream.click()
