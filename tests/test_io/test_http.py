import requests
import pytest

from fantasy_football.io.extract_from_http import get_html_doc


# def get_my_ip():
#     response = requests.get(
#         'http://ipinfo.io/json'
#     )
#     return response.json()['ip']


# def test_get_my_ip(monkeypatch):
#     my_ip = '123.123.123.123'

#     class MockResponse:

#         def __init__(self, json_body):
#             self.json_body = json_body

#         def json(self):
#             return self.json_body

#     monkeypatch.setattr(
#         requests,
#         'get',
#         lambda *args, **kwargs: MockResponse({'ip': my_ip})
#     )

#     assert get_my_ip() == my_ip


def test_get_html_doc_success(monkeypatch):

    class MockResponse:

        def __init__(self):
            self.status_code = 200


    monkeypatch.setattr(
        requests,
        'get',
        lambda *args, **kwargs: MockResponse()
    )

    assert get_html_doc(url="http://ipinfo.io/json").status_code == 200

def test_get_html_doc_exception(monkeypatch):

    class MockResponse:

        def __init__(self):
            self.status_code = 500

    monkeypatch.setattr(
        requests,
        'get',
        lambda *args, **kwargs: MockResponse()
    )

    with pytest.raises(requests.HTTPError):
        assert get_html_doc(url="http://ipinfo.io/json")