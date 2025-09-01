# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

pyRapid is a Python REST API client library for interacting with the Rapid Response Management System (RRMS) backend. It provides authentication and data retrieval capabilities for the Rapid Response platform.

## Development Commands

### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest pyrapid/tests/test_rapid.py

# Run specific test function
pytest pyrapid/tests/test_rapid.py::test_rapid_get

# Run with verbose output
pytest -v

# Run with coverage
pytest --cov=pyrapid
```

### Installation
```bash
# Install in development mode
pip install -e .

# Install dependencies
pip install -r requirements.txt
```

### Example Usage
```bash
# Run the main data export script (requires environment variables)
python main.py
```

## Architecture

### Core Components

- **pyrapid/rapid.py**: Main `Rapid` class that handles:
  - Authentication (login/logout) via session tokens
  - HTTP POST requests to the RRMS API
  - Session management with automatic token injection

- **pyrapid/utils.py**: Error handling utilities for API responses

### Key Design Patterns

1. **Session Management**: The `Rapid` class automatically authenticates on initialization and maintains session tokens throughout its lifecycle.

2. **API Interaction**: All API calls use POST requests with session tokens embedded in the JSON payload. The `get()` method handles both simple token-only requests and requests with additional content.

3. **Testing Strategy**: Uses pytest with extensive mocking of the `requests` library to test API interactions without making actual HTTP calls.

## Environment Configuration

The application expects these environment variables for production use:
- `RAPID_API_USER`: API username
- `RAPID_API_PASSWORD`: API password  
- `RAPID_API_URL`: Base URL for the Rapid API (defaults to production URL if not set)

## API Endpoints

The library interacts with the Rapid Response Management System API. All endpoints use POST requests with session tokens.

### Authentication
- `/Login/UserLogin` - Initial authentication (returns SessionNum and SessionPassword)
- `/Login/Logout` - Session termination

### DataExport Endpoints
All DataExport endpoints accept optional parameters:
- `SiteNum`: Filter by specific site
- `TargetSiteGroup`: Filter by site group
- `SessionNum` & `SessionPassword`: Required authentication tokens

Available endpoints:
- `/DataExport/ContactList` - Contact information
- `/DataExport/ContactPhoneList` - Contact phone numbers
- `/DataExport/DeviceList` - Device information  
- `/DataExport/SiteDetailList` - Site details
- `/DataExport/SitePhoneList` - Site phone numbers
- `/DataExport/AgencyList` - Agency information
- `/DataExport/SignalRuleList` - Signal rule configurations
- `/DataExport/FirstSignalDatesList` - First signal dates (requires UTCBeginDate and UTCEndDate)
- `/DataExport/HistoryList` - Historical data

### API URLs
- Development: `https://eastdevapi.rrms.com/RestApiDev/api/`
- Production: `https://eastprodapi.rrms.com/RestApIProd/api/` (default)

## Error Handling

The library raises `ValueError` exceptions when API calls fail (non-200 status codes). The `utils.bad_output()` function logs detailed error information including status code, URL, response text, headers, and content before raising the exception.