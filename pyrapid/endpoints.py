"""
Dataclasses for Rapid API endpoint parameters.
"""
from dataclasses import dataclass, field
from typing import Optional
from datetime import date


@dataclass
class BaseEndpoint:
    """Base class for all endpoint parameters with required session tokens."""
    session_num: Optional[int] = None
    session_password: Optional[str] = None
    
    def to_dict(self) -> dict:
        """Convert dataclass to dictionary, excluding None values."""
        result = {}
        for key, value in self.__dict__.items():
            if value is not None:
                # Convert snake_case to PascalCase for API
                api_key = ''.join(word.capitalize() for word in key.split('_'))
                result[api_key] = value
        return result


@dataclass
class ContactList(BaseEndpoint):
    """Parameters for DataExport/ContactList endpoint."""
    site_num: Optional[int] = None
    target_site_group: Optional[int] = None


@dataclass
class ContactPhoneList(BaseEndpoint):
    """Parameters for DataExport/ContactPhoneList endpoint."""
    site_num: Optional[int] = None


@dataclass
class DeviceList(BaseEndpoint):
    """Parameters for DataExport/DeviceList endpoint."""
    site_num: Optional[int] = None
    target_site_group: Optional[int] = None


@dataclass
class SiteDetailList(BaseEndpoint):
    """Parameters for DataExport/SiteDetailList endpoint."""
    site_num: Optional[int] = None
    target_site_group: Optional[int] = None


@dataclass
class SitePhoneList(BaseEndpoint):
    """Parameters for DataExport/SitePhoneList endpoint."""
    site_num: Optional[int] = None


@dataclass
class AgencyList(BaseEndpoint):
    """Parameters for DataExport/AgencyList endpoint."""
    site_num: Optional[int] = None


@dataclass
class SignalRuleList(BaseEndpoint):
    """Parameters for DataExport/SignalRuleList endpoint."""
    site_num: Optional[int] = None
    target_site_group: Optional[int] = None


@dataclass
class FirstSignalDatesList(BaseEndpoint):
    """Parameters for DataExport/FirstSignalDatesList endpoint."""
    site_num: Optional[int] = None
    target_site_group: Optional[int] = None
    utc_begin_date: Optional[str] = None  # Format: "YYYY-MM-DD"
    utc_end_date: Optional[str] = None    # Format: "YYYY-MM-DD"
    application_code: Optional[str] = None


@dataclass
class HistoryList(BaseEndpoint):
    """Parameters for DataExport/HistoryList endpoint."""
    site_num: Optional[int] = None
    target_site_group: Optional[int] = None
    # Add other parameters as needed based on API documentation


# Endpoint URL mapping
ENDPOINT_URLS = {
    ContactList: 'DataExport/ContactList',
    ContactPhoneList: 'DataExport/ContactPhoneList',
    DeviceList: 'DataExport/DeviceList',
    SiteDetailList: 'DataExport/SiteDetailList',
    SitePhoneList: 'DataExport/SitePhoneList',
    AgencyList: 'DataExport/AgencyList',
    SignalRuleList: 'DataExport/SignalRuleList',
    FirstSignalDatesList: 'DataExport/FirstSignalDatesList',
    HistoryList: 'DataExport/HistoryList',
}