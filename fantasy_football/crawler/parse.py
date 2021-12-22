import re

from bs4 import BeautifulSoup
from requests import Response


def parse_html(response: Response) -> BeautifulSoup:
    """
    Erase all comments in Response-object and parse to html object.

    Args:
        response (requests.Response):

    Returns:
        BeautifulSoup:
    """
    content = response.text
    commments = re.compile("<!--|-->")
    soup = BeautifulSoup(commments.sub("", content), "html.parser")
    return soup
