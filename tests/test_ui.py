from playwright.sync_api import Page

from aqa.utils.enums import Urls, WaitStates
from aqa.utils.actions import Actions
from aqa.pages.home_page import HomePage
from aqa.pages.result_page import ResultPage


# Failed tests for Firefox in all devices and tablet and mobile on WebKit CHECK ERRORS.
# Create locators in pages and follow POM pattern.

def test_search_starcraftii_on_twitch(page: Page):
    """Test searching for Starcraft II on Twitch and clicking a random stream."""

    TARGET = "starcraft ii"

    actions = Actions(page)
    actions.navigate(Urls.TWITCH_HOME)

    home_page = HomePage(page)    
    home_page.reject_cookies()
    actions.wait_for_load_state(WaitStates.NETWORKIDLE)  
    home_page.search_for(TARGET)
    
    result_page = ResultPage(page)
    result_page.scroll_down(times=2)
    result_page.click_random_stream()
    actions.wait_for_load_state(WaitStates.NETWORKIDLE)
    actions.take_screenshot("twitch_stream.png")
