# py-sp-api

<https://developer-docs.amazon.com/sp-api/docs/tutorial-automate-your-sp-api-calls-using-python-sdk>

## Installation

`pip install py-sp-api`

## Usage

```python
import os
import dotenv

dotenv.load_dotenv()

from py_sp_api.generated.productPricingV0 import ProductPricingApi, SPAPIClient as PricingClient
from py_sp_api.generated.notifications import NotificationsApi, SPAPIClient as NotificationsClient
from py_sp_api import SPAPIConfig


def test_get_pricing(asin: str, marketplace_id="ATVPDKIKX0DER"):
    # demonstrates a grantful "refresh_token" request
    spapi_config = SPAPIConfig(
        client_id=os.getenv("SPAPI_CLIENT_ID"),
        client_secret=os.getenv("SPAPI_CLIENT_SECRET"),
        refresh_token=os.getenv("SPAPI_TOKEN"),
        region="NA",
    )
    product_pricing = ProductPricingApi(PricingClient(spapi_config))
    response = product_pricing.get_pricing(marketplace_id=marketplace_id, item_type="Asin", asins=[asin])
    print("pricing", response)


def test_notifications():
    # demomonstrates a grantless request
    grantless_config = SPAPIConfig(
        client_id=os.getenv("SPAPI_CLIENT_ID"),
        client_secret=os.getenv("SPAPI_CLIENT_SECRET"),
        refresh_token=os.getenv("SPAPI_TOKEN"),
        region="NA",
        grant_type="client_credentials",
        scope="sellingpartnerapi::notifications",
    )
    notifications = NotificationsApi(NotificationsClient(grantless_config))
    response = notifications.get_destinations()
    print("destinations", response)


test_notifications()
test_get_pricing(asin="B0DP7GSWC8")
```

## Development

- `make clean` removes the generated code
- `make generate` generates the schemas
- `make test` runs unit tests

### Structure

```text
.
├── Makefile - make scripts
├── README.md - this file
├── notebooks
│   └── api_test.ipynb - example usage
├── poetry.lock
├── pyproject.toml
├── selling-partner-api-models - git submodule from <https://github.com/amzn/selling-partner-api-models.git>
├── scripts
│   └── generate_schemas.py - script to generate api
└── src
    └── py_sp_api
        ├── auth - copied from selling-partner-api-models/clients/sellingpartner-api-aa-python/auth
        │   ├── LwaException.py - unchanged
        │   ├── LwaExceptionErrorCode.py - unchanged
        │   ├── LwaRequest.py - import paths modified
        │   └── credentials.py - tweaked to allow grantless operations
        |── base_client.py - client that gets copied into each package in generated/
        └── generated - the generated api files created when generate_schemas.py is run
```
