import argparse
import json
import os
from urllib.parse import urlparse
import re
import logging
from datetime import datetime

def parse_arguments():
    parser = argparse.ArgumentParser(description="Crawl a website and save all pages to a Markdown file.")
    parser.add_argument("url", type=str, help="The URL of the website to crawl.",default=None)
    parser.add_argument("-g", "--get_all_pages", type=str, help="Either get all pages or get only start page", default=False)

    return parser.parse_args()

def process_urls_argument(url_arg):
    try:
        urls = json.loads(url_arg)
        if isinstance(urls, list) and all(isinstance(item, str) for item in urls):
            return urls
    except json.JSONDecodeError:
        # Not a JSON list, try splitting by comma
        return [u.strip() for u in url_arg.split(',')]

def create_filename_from_url(url):
    parsed_url = urlparse(url)
    netloc = parsed_url.netloc
    # Remove "www." if present
    if netloc.startswith("www."):
        netloc = netloc[4:]
    # Replace non-alphanumeric characters with underscore
    filename = re.sub(r'[^a-zA-Z0-9_]', '_', netloc) + ".md"
    return filename

def setup_logger(filename, LOG_DIR = "logs"):
    LOG_FILE = f"crawl_{filename}.log"
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    LOG_FILEPATH = os.path.join(LOG_DIR,LOG_FILE)
    logger = logging.getLogger(f"crawl_{filename}")
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler(LOG_FILEPATH, encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger