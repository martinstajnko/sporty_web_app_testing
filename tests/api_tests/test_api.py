import pytest
from aqa.api.client import APIClient
from aqa.enums import APIEndpoints


@pytest.fixture
def api_client():
    """Fixture to provide API client."""
    pass

class TestTwitchAPI:
    
    def test_search_api_returns_200(self, api_client: APIClient):
        pass
    
    def test_search_api_returns_json(self, api_client: APIClient):
        pass
    
    def test_api_has_required_headers(self, api_client: APIClient):
        pass
