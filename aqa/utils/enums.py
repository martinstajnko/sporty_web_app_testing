"""Enums for various constants used in the AQA framework."""

from enum import Enum


class BrowserType(Enum):
    CHROMIUM = "chromium"
    FIREFOX = "firefox"
    WEBKIT = "webkit"


class DeviceType(Enum):
    DESKTOP = "desktop"
    MOBILE = "mobile"
    TABLET = "tablet"


class Urls(Enum):
    TWITCH_HOME = "https://www.twitch.tv/"


class WaitStates(Enum):
    LOAD = "load"  #  Wait until the page load event fires (basic HTML loaded)
    DOMCONTENTLOADED = "domcontentloaded"  # Wait until DOM is fully parsed
    NETWORKIDLE = (
        "networkidle"  # Wait until all network requests finish (images, API calls,...)
    )


class APIEndpoints(Enum):
    """Twitch API endpoints (example - replace with actual endpoints you're testing)."""

    SEARCH = "/api/search"
    STREAMS = "/api/streams"
    USERS = "/api/users"
