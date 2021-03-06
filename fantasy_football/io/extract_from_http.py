import requests
import logging


def get_html_doc(url: str) -> requests.Response:
    response = requests.get(url=url)
    logging.info(f"Status Code: {response.status_code} for {url}")
    if response.status_code != 200:
        logging.error(f"Could not connect to {url}")
        raise requests.HTTPError

    return response


if __name__ == "__main__":
    FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(format=FORMAT, level=logging.INFO)
    URL = "https://www.pro-football-reference.com/"
    get_html_doc(url=URL)
