import logging
from .marmiton import MarmitonScrapper


def get_items(urls):
    for url in urls:
        if "https://www.marmiton.org/" in url:
            logging.info(f"Getting {url}")
            MarmitonScrapper.parse_url(url)
