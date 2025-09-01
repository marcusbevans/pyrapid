"""
Example usage of pyrapid with the new dataclass endpoints and response options.
"""
import os
from dotenv import load_dotenv
from pyrapid import Rapid
from pyrapid.endpoints import (
    ContactList, 
    DeviceList, 
    SiteDetailList,
    FirstSignalDatesList,
    AgencyList
)

# Load environment variables from .env file
# Copy .env.example to .env and fill in your credentials
load_dotenv()


def example_basic_usage():
    """Basic usage with the original get() method."""
    rapid = Rapid(
        username=os.getenv('RAPID_API_USER'),
        password=os.getenv('RAPID_API_PASSWORD'),
        url=os.getenv('RAPID_API_URL', 'https://eastprodapi.rrms.com/RestApIProd/api/')
    )
    
    # Get JSON response (default)
    contacts = rapid.get('DataExport/ContactList', {'TargetSiteGroup': 123})
    print(f"Found {len(contacts.get('ContactList', []))} contacts")
    
    # Get full response object
    response = rapid.get('DataExport/DeviceList', {'SiteNum': 456}, full_response=True)
    print(f"Status Code: {response.status_code}")
    print(f"Headers: {response.headers}")
    devices = response.json()
    
    rapid.logout()


def example_dataclass_usage():
    """Using the new dataclass endpoints for cleaner code."""
    rapid = Rapid(
        username=os.getenv('RAPID_API_USER'),
        password=os.getenv('RAPID_API_PASSWORD')
    )
    
    # Create endpoint objects with parameters
    contact_query = ContactList(target_site_group=123)
    device_query = DeviceList(site_num=456, target_site_group=789)
    
    # Get JSON responses
    contacts = rapid.get_endpoint(contact_query)
    devices = rapid.get_endpoint(device_query)
    
    print(f"Contacts: {len(contacts.get('ContactList', []))}")
    print(f"Devices: {len(devices.get('DeviceList', []))}")
    
    rapid.logout()


def example_date_range_query():
    """Example with date range parameters."""
    rapid = Rapid(
        username=os.getenv('RAPID_API_USER'),
        password=os.getenv('RAPID_API_PASSWORD')
    )
    
    # Query first signal dates for January 2024
    signal_query = FirstSignalDatesList(
        utc_begin_date="2024-01-01",
        utc_end_date="2024-01-31",
        target_site_group=123
    )
    
    # Get full response to check headers and status
    response = rapid.get_endpoint(signal_query, full_response=True)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Found {len(data.get('FirstSignalDatesList', []))} signals")
    else:
        print(f"Error: {response.status_code}")
    
    rapid.logout()


def example_multiple_endpoints():
    """Query multiple endpoints and combine results."""
    rapid = Rapid(
        username=os.getenv('RAPID_API_USER'),
        password=os.getenv('RAPID_API_PASSWORD')
    )
    
    site_group = 123
    
    # Define all queries
    queries = {
        'sites': SiteDetailList(target_site_group=site_group),
        'contacts': ContactList(target_site_group=site_group),
        'devices': DeviceList(target_site_group=site_group),
        'agencies': AgencyList(site_num=456)
    }
    
    # Execute all queries
    results = {}
    for name, query in queries.items():
        try:
            results[name] = rapid.get_endpoint(query)
            print(f"✓ {name}: Success")
        except ValueError as e:
            print(f"✗ {name}: Failed - {e}")
            results[name] = None
    
    # Process results
    for name, data in results.items():
        if data:
            # The response structure varies by endpoint
            # You'll need to check the actual API response format
            print(f"{name}: Retrieved data successfully")
    
    rapid.logout()


def example_error_handling():
    """Example with proper error handling."""
    try:
        rapid = Rapid(
            username=os.getenv('RAPID_API_USER'),
            password=os.getenv('RAPID_API_PASSWORD')
        )
        
        # This will fail if the site doesn't exist
        query = DeviceList(site_num=999999)
        
        try:
            devices = rapid.get_endpoint(query)
            print(f"Found {len(devices.get('DeviceList', []))} devices")
        except ValueError as e:
            print(f"Query failed: {e}")
            # Try with full response to get more details
            response = rapid.get_endpoint(query, full_response=True)
            print(f"Response details: {response.text}")
        
    except ValueError as e:
        print(f"Login failed: {e}")
    finally:
        if 'rapid' in locals():
            rapid.logout()


if __name__ == '__main__':
    print("=" * 50)
    print("Basic Usage Example")
    print("=" * 50)
    example_basic_usage()
    
    print("\n" + "=" * 50)
    print("Dataclass Usage Example")
    print("=" * 50)
    example_dataclass_usage()
    
    print("\n" + "=" * 50)
    print("Date Range Query Example")
    print("=" * 50)
    example_date_range_query()
    
    print("\n" + "=" * 50)
    print("Multiple Endpoints Example")
    print("=" * 50)
    example_multiple_endpoints()