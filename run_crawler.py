import logging

from fantasy_football.io.extract_from_http import get_html_doc

URL = "https://www.pro-football-reference.com/"


def main() -> None:
    FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(format=FORMAT, level=logging.INFO)
    get_html_doc(url=URL)
    return None


if __name__ == "__main__":
    main()
