"""Base class for all API endpoints."""
from typing import Any, Dict, Optional

import requests


class APIClient:
    """Base client for API testing."""
    
    def __init__(self, base_url: str):
        """Initialize API client with base URL."""
        self.base_url = base_url
        self.session = requests.Session()
    
    def get(self, endpoint: str, **kwargs) -> requests.Response:
        """Perform GET request."""
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url, **kwargs)
    
    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None, **kwargs) -> requests.Response:
        """Perform POST request."""
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=data, **kwargs)
    
    def put(self, endpoint: str, data: Optional[Dict[str, Any]] = None, **kwargs) -> requests.Response:
        """Perform PUT request."""
        url = f"{self.base_url}{endpoint}"
        return self.session.put(url, json=data, **kwargs)
    
    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        """Perform DELETE request."""
        url = f"{self.base_url}{endpoint}"
        return self.session.delete(url, **kwargs)
    
    def set_header(self, key: str, value: str) -> None:
        """Set a custom header."""
        self.session.headers.update({key: value})
    
    def close(self) -> None:
        """Close the session."""
        self.session.close()
