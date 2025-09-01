from pyrapid.rapid import Rapid
from pyrapid.endpoints import ContactList, DeviceList, FirstSignalDatesList
import pytest
from unittest.mock import patch


class Request:
    def __init__(self, url):
        self.url = url


class Requests:
    def __init__(
            self,
            status_code: int,
            headers: dict = {'header': 'error'},
            content: str = 'test content',
            json: dict = {'something': 'recieved'}
    ):
        self.status_code = status_code
        self.headers = headers
        self.content = content
        self.body = content
        self.text = content  # Add text attribute for error handling
        self.json_result = json
        self.request = None

    def post(self, url: str, *args, **kwargs):
        self.request = Request(url)
        return self

    def json(self) -> dict:
        return self.json_result


def test_rapid():
    with patch('pyrapid.rapid.requests', Requests(
            status_code=200,
            json={'OutputParameter': {
                'SessionNum': 123,
                'SessionPassword': 'test'
            }}
    )):
        rapid = Rapid(username='test', password='test123')

    assert rapid.username == 'test'
    assert rapid.password == 'test123'
    assert rapid.token == {
        'SessionNum': 123,
        'SessionPassword': 'test'
    }


def test_rapid_bad_status_code():
    with patch('pyrapid.rapid.requests', Requests(status_code=500)):
        with pytest.raises(ValueError):
            Rapid(username='test', password='test123')


@pytest.fixture()
def rapid_base():
    with patch('pyrapid.rapid.requests', Requests(
            status_code=200,
            json={'OutputParameter': {
                'SessionNum': 123,
                'SessionPassword': 'test'
            }}
    )):
        rapid = Rapid(username='test', password='test123')
    return rapid


def test_rapid_get(rapid_base):
    with patch('pyrapid.rapid.requests', Requests(
            status_code=200,
            json={'results': 'here'},
    )):
        results = rapid_base.get('/Site/SiteTypeList')
        assert results == {'results': 'here'}


def test_rapid_get_with_context(rapid_base):
    with patch('pyrapid.rapid.requests', Requests(status_code=200, json={'results': 'here'})):
        results = rapid_base.get('/api/XtNewXmitPhoneList', {'KeyNum': 456, 'KeyType': 'Site'})
        assert results == {'results': 'here'}


def test_rapid_get_error(rapid_base):
    with patch('pyrapid.rapid.requests', Requests(status_code=404)):
        with pytest.raises(ValueError):
            rapid_base.get('/Site/SiteTypeList')


def test_rapid_get_full_response(rapid_base):
    mock_requests = Requests(status_code=200, json={'results': 'here'})
    with patch('pyrapid.rapid.requests', mock_requests):
        response = rapid_base.get('/Site/SiteTypeList', full_response=True)
        assert response.status_code == 200
        assert response.json() == {'results': 'here'}


def test_rapid_get_endpoint_with_dataclass(rapid_base):
    with patch('pyrapid.rapid.requests', Requests(status_code=200, json={'ContactList': []})):
        endpoint = ContactList(target_site_group=123)
        results = rapid_base.get_endpoint(endpoint)
        assert results == {'ContactList': []}


def test_rapid_get_endpoint_full_response(rapid_base):
    mock_requests = Requests(status_code=200, json={'DeviceList': []})
    with patch('pyrapid.rapid.requests', mock_requests):
        endpoint = DeviceList(site_num=456)
        response = rapid_base.get_endpoint(endpoint, full_response=True)
        assert response.status_code == 200
        assert response.json() == {'DeviceList': []}


def test_endpoint_to_dict():
    endpoint = FirstSignalDatesList(
        site_num=123,
        utc_begin_date="2024-01-01",
        utc_end_date="2024-01-31"
    )
    result = endpoint.to_dict()
    assert result == {
        'SiteNum': 123,
        'UtcBeginDate': "2024-01-01",
        'UtcEndDate': "2024-01-31"
    }
