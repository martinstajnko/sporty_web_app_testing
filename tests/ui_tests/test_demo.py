import re
from playwright.sync_api import Page, expect
from aqa.pages.home_page import HomePage

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()



def test_search_starcraft_on_twitch(page: Page):
    """Test searching for Starcraft II on Twitch and navigating to a live stream."""
    # Initialize the page object
    home_page = HomePage(page)
    
    # Navigate to Twitch
    home_page.navigate()
    
    # Reject cookies
    home_page.reject_cookies()
    
    # Search for "Starcraft II"
    home_page.search_for("startcraft ii")
    
    # Navigate through search suggestions
    home_page.navigate_to_first_suggestion()
    
    # Click on the specific stream
    page.get_by_role("link", name="Clan War - Platinum Heroes vs. pheeniX Viking - 90s delay - esarel LIVE 8").click()
    
    # Wait for the stream page to load
    home_page.wait_for_load_state("networkidle")
    
    # Take a final screenshot
    home_page.take_screenshot("twitch_stream.png")
