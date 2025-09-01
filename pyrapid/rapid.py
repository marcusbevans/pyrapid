from dataclasses import dataclass, field
from typing import Union
import logging

import requests


@dataclass
class Rapid:
    username: str
    password: str
    token: dict = field(default_factory=dict)
    url: str = 'https://eastprodapi.rrms.com/RestApIProd/api/'

    def __post_init__(self):
        self.token = self.login()

    def login(self):
        body = {
            'username': self.username,
            'password': self.password,
        }

        result = requests.post(self.url + 'Login/UserLogin', json=body)

        if result.status_code == 200:
            r_json = result.json()
            session = {
                'SessionNum': r_json.get('OutputParameter', {}).get('SessionNum'),
                'SessionPassword': r_json.get('OutputParameter', {}).get('SessionPassword'),
            }
            return session
        else:
            self._bad_output(result)

    def logout(self):
        result = requests.post(self.url + 'Login/Logout', json=self.token)
        
        if result.status_code != 200:
            self._bad_output(result)

    def get(self, url: str, content: dict = None, full_response: bool = False) -> Union[dict, requests.Response]:
        """
        Make a GET request to the API endpoint.

        Args:
            url: The endpoint URL path (e.g., 'DataExport/ContactList')
            content: Optional dictionary of additional parameters to send
            full_response: If True, return the full Response object; if False, return just the JSON

        Returns:
            Either the JSON response (dict) or the full Response object
        """
        if content:
            payload = {**self.token, **content}
        else:
            payload = self.token

        result = requests.post(self.url + url, json=payload)

        if result.status_code != 200:
            self._bad_output(result)

        return result if full_response else result.json()

    def get_endpoint(self, endpoint, full_response: bool = False) -> Union[dict, requests.Response]:
        """
        Make a request using an endpoint dataclass.

        Args:
            endpoint: An endpoint dataclass instance from pyrapid.endpoints
            full_response: If True, return the full Response object; if False, return just the JSON

        Returns:
            Either the JSON response (dict) or the full Response object
        """
        from pyrapid.endpoints import ENDPOINT_URLS, BaseEndpoint

        if not isinstance(endpoint, BaseEndpoint):
            raise ValueError(
                "Endpoint must be an instance of a pyrapid.endpoints dataclass")

        # Get the URL for this endpoint type
        endpoint_type = type(endpoint)
        if endpoint_type not in ENDPOINT_URLS:
            raise ValueError(
                f"Unknown endpoint type: {endpoint_type.__name__}")

        url = ENDPOINT_URLS[endpoint_type]

        # Set session tokens if not already set
        if endpoint.session_num is None:
            endpoint.session_num = self.token.get('SessionNum')
        if endpoint.session_password is None:
            endpoint.session_password = self.token.get('SessionPassword')

        # Convert to dictionary and make request
        content = endpoint.to_dict()
        return self.get(url, content, full_response)

    def _bad_output(self, result: requests.Response):
        logging.error(f'{result.status_code}: {result.request.url}')
        logging.error(f'{result.text}')
        logging.error(f'{result.headers}')
        logging.error(f'{result.content}')
        raise ValueError(
            f"API request failed with status {result.status_code}")
