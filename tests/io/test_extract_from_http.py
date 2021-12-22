import requests
import pytest

from fantasy_football.io.extract_from_http import get_html_doc


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
