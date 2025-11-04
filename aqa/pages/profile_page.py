from playwright.sync_api import Page

from aqa.utils.actions import Actions
from aqa.utils.enums import WaitStates


class ProfilePage:
    """Page Object for Twitch User Profile page."""
           
    def __init__(self, page: Page):
        """Initialize BasePage with a Playwright Page instance."""
        self.page = page

    def wait_for_stream_page_loaded(self) -> None:
        """Wait until the stream page is fully loaded."""
        Actions(self.page).wait_for_load_state(WaitStates.NETWORKIDLE)
    
        try:
            video_area = self.page.locator('video, [data-a-target="video-player"], [data-a-target="player-overlay-click-handler"]').first
            video_area.wait_for(state="visible", timeout=15000)
        except Exception:
            pass
        
        # Wait for stream info
        try:
            stream_info = self.page.locator('h1, [data-a-target="stream-title"]').first
            stream_info.wait_for(state="visible", timeout=10000)
        except Exception:
            pass

