from enum import Enum


class BrowserType(Enum):
    CHROMIUM = "chromium"
    FIREFOX = "firefox"
    WEBKIT = "webkit"


class Urls(Enum):
    TWITCH_HOME = "https://www.twitch.tv/"


class APIEndpoints(Enum):
    """Twitch API endpoints (example - replace with actual endpoints you're testing)."""
    SEARCH = "/api/search"
    STREAMS = "/api/streams"
    USERS = "/api/users"



