from playwright.sync_api import Page

from aqa.utils.enums import Urls, WaitStates
from aqa.utils.actions import Actions
from aqa.pages.home_page import HomePage
from aqa.pages.profile_page import ProfilePage
from aqa.pages.result_page import ResultPage


TARGET = "starcraft ii"

def test_search_starcraftii_on_twitch(page: Page):
    """Test searching for Starcraft II on Twitch and clicking a random stream."""

    timestamp = page.evaluate("() => Date.now()")

    actions = Actions(page)
    actions.navigate(Urls.TWITCH_HOME)

    home_page = HomePage(page)
    home_page.reject_cookies()
    actions.wait_for_load_state(WaitStates.NETWORKIDLE)
    home_page.search_for(TARGET)

    result_page = ResultPage(page)
    result_page.scroll_down(times=2)
    result_page.click_random_stream()

    profile_page = ProfilePage(page)
    profile_page.wait_for_stream_page_loaded()
    actions.take_screenshot(f"twitch_stream_{timestamp}.png")
