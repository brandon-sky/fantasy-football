import requests

from bs4 import BeautifulSoup
from fantasy_football.crawler.parse import parse_html


def test_parse_html(monkeypatch):
    class MockResponse:

        def __init__(self):
            self.status_code = 200

    monkeypatch.setattr(
        requests,
        'get',
        lambda *args, **kwargs: MockResponse()
    )
    assert type(parse_html(response=MockResponse)) == BeautifulSoup
