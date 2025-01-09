import pytest
from unittest.mock import patch
from py_sp_api.generated.productPricingV0 import ProductPricingApi, SPAPIClient as PricingClient
from py_sp_api.generated.notifications import NotificationsApi, SPAPIClient as NotificationsClient
from py_sp_api import SPAPIConfig

# Mock responses
MOCK_PRICING_RESPONSE = {
    "payload": [
        {
            "ASIN": "B0DP7GSWC8",
            "status": "Success",
            "price": {
                "status": "Active",
                "listingPrice": {"amount": 29.99, "currency": "USD"},
            },
        }
    ]
}

MOCK_NOTIFICATIONS_RESPONSE = {
    "payload": {
        "destinations": [
            {
                "name": "test-destination",
                "destinationId": "test-id",
                "resource": "test-resource",
            }
        ]
    }
}


@pytest.fixture
def spapi_config():
    return SPAPIConfig(
        client_id="fake-client-id",
        client_secret="fake-client-secret",
        refresh_token="fake-refresh-token",
        region="NA",
    )


@pytest.fixture
def grantless_config():
    return SPAPIConfig(
        client_id="fake-client-id",
        client_secret="fake-client-secret",
        refresh_token="fake-refresh-token",
        region="NA",
        grant_type="client_credentials",
        scope="sellingpartnerapi::notifications",
    )


@patch.object(ProductPricingApi, "get_pricing")
def test_get_pricing(mock_get_pricing, spapi_config):
    # Setup
    mock_get_pricing.return_value = MOCK_PRICING_RESPONSE
    product_pricing = ProductPricingApi(PricingClient(spapi_config))

    # Execute
    response = product_pricing.get_pricing(marketplace_id="ATVPDKIKX0DER", item_type="Asin", asins=["B0DP7GSWC8"])

    # Verify
    assert response == MOCK_PRICING_RESPONSE
    mock_get_pricing.assert_called_once_with(marketplace_id="ATVPDKIKX0DER", item_type="Asin", asins=["B0DP7GSWC8"])


@patch.object(NotificationsApi, "get_destinations")
def test_notifications(mock_get_destinations, grantless_config):
    # Setup
    mock_get_destinations.return_value = MOCK_NOTIFICATIONS_RESPONSE
    notifications = NotificationsApi(NotificationsClient(grantless_config))

    # Execute
    response = notifications.get_destinations()

    # Verify
    assert response == MOCK_NOTIFICATIONS_RESPONSE
    mock_get_destinations.assert_called_once()
