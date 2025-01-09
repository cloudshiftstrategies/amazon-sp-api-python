import os
import sys
import pytest
from unittest.mock import patch

# Add the src directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


@pytest.fixture(autouse=True)
def mock_env_vars():
    """Mock environment variables for all tests"""
    with patch.dict(
        "os.environ",
        {
            "SPAPI_CLIENT_ID": "fake-client-id",
            "SPAPI_CLIENT_SECRET": "fake-client-secret",
            "SPAPI_TOKEN": "fake-refresh-token",
        },
    ):
        yield
