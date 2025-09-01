# pyRapid

Python REST API client library for the Rapid Response Management System (RRMS) backend.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure credentials:
```bash
cp .env.example .env
# Edit .env with your Rapid API credentials
```

## Usage

```python
import os
from dotenv import load_dotenv
from pyrapid import Rapid, ContactList

load_dotenv()

# Initialize client
rapid = Rapid(
    username=os.getenv('RAPID_API_USER'),
    password=os.getenv('RAPID_API_PASSWORD')
)

# Query using dataclasses
contacts = rapid.get_endpoint(ContactList(target_site_group=123))

# Or use traditional method
devices = rapid.get('DataExport/DeviceList', {'SiteNum': 456})

# Get full response object
response = rapid.get('DataExport/SiteDetailList', full_response=True)
print(f"Status: {response.status_code}")

rapid.logout()
```

See `examples.py` for more detailed usage examples.