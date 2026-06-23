# load .env file in /env directory
import contextlib
import logging
import os

from dotenv import load_dotenv, find_dotenv

from .helper import validator

load_dotenv(dotenv_path=find_dotenv('.env', usecwd=False))

import sys
from .web_scraper.web_api_scraper import scrape_spotify_playlist_page

from .sdk.integration import ai_analysis

# LOGGING LEVEL
logging.getLogger('selenium').setLevel(logging.CRITICAL)
logging.getLogger('urllib3').setLevel(logging.CRITICAL)
logging.getLogger("google.genai").setLevel(logging.CRITICAL)

os.environ['WDM_LOG_LEVEL'] = '0'  # Untuk webdriver-manager (jika pakai)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  #


def main():
    try:
        playlist_link = sys.argv[1]
        ai_model_apikey = None

        if (len(sys.argv) > 2):
            ai_model_apikey = sys.argv[2]
        else:
            ai_model_apikey = os.getenv('GOOGLE_CLOUD_API_KEY', '')

        validator.validate_args(playlist_link, ai_model_apikey)

        songs_collection = scrape_spotify_playlist_page(playlist_link)
        ai_analysis(songs_collection, playlist_link, ai_model_apikey)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
