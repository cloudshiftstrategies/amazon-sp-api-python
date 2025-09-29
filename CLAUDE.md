# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

This is a Poetry project. Essential commands:

- `poetry install` - Install dependencies and set up development environment
- `make clean` - Remove generated code from `src/py_sp_api/generated/`
- `make generate` - Update git submodule and regenerate API clients from Amazon's OpenAPI specs
- `make test` - Run unit tests with pytest
- `make lint` - Run flake8 linting checks
- `make fix` - Auto-fix code formatting with black and autoflake
- `make lint-fix` - Run fix then lint (recommended before commits)

## Project Architecture

This project generates Python API clients for Amazon's Selling Partner API using OpenAPI Generator. Key architectural components:

### Code Generation Flow
1. Amazon's OpenAPI specs are maintained as a git submodule in `selling-partner-api-models/`
2. `scripts/generate_schemas.py` processes these specs and generates Python clients
3. Generated code is placed in `src/py_sp_api/generated/` with separate modules for each API
4. Each generated module gets a copy of `base_client.py` for SP-API authentication

### Authentication System
- `SPAPIConfig` class handles both grantful (refresh_token) and grantless (client_credentials) authentication flows
- `SPAPIClient` extends the generated OpenAPI client with Amazon LWA token management
- Token caching is handled by `AccessTokenCache` to avoid redundant token requests
- Custom AWS auth implementation in `src/py_sp_api/auth/` (adapted from Amazon's reference implementation)

### Package Structure
- `src/py_sp_api/auth/` - Authentication components (LWA tokens, AWS signing)
- `src/py_sp_api/generated/` - Auto-generated API clients (do not manually edit)
- `src/py_sp_api/base_client.py` - Template that gets copied into each generated client
- `scripts/generate_schemas.py` - Client generation script

### Configuration Details
- Black line length: 120 characters
- Generated code and git submodule are excluded from formatting
- Python 3.9+ required
- Uses pydantic v2 for data validation and requests for HTTP client

## Important Notes

- Never manually edit files in `src/py_sp_api/generated/` - they are overwritten during generation
- Run `make generate` after updating the `selling-partner-api-models` submodule
- The project supports both marketplace-specific (grantful) and account-level (grantless) API operations
- Each API endpoint may have different authentication requirements - check Amazon's documentation