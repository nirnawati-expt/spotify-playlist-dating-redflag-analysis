# load .env file in /env directory
import logging
import os

from dotenv import load_dotenv, find_dotenv

from vibecheck.config.base_configuration import IS_ENVIRONMENT_CLOUD
from vibecheck.config.sdk_configuration import GOOGLE_GENAI_APIKEY
from vibecheck.helper.validator import validate_url
from vibecheck.helper.writer import write_output_locally
from .helper import validator, str_utility

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


def main(playlist_link: str, ai_model_apikey: str, callback_print=None):
    def write_message(teks):
        if callback_print:  # from streamlit
            callback_print(teks)
        else:  # from local
            print(teks)

    try:
        write_message("🎵 Fetching playlist data...")

        validator.validate_args(playlist_link, ai_model_apikey)

        # Validate spotify URL
        if not validate_url(playlist_link):
            write_message("Invalid URL, can't proceed to continue process")
            return ""

        songs_collection = scrape_spotify_playlist_page(playlist_link)

        write_message("🎧 Analyzing the vibe..")
        ai_response = ai_analysis(songs_collection, playlist_link, ai_model_apikey)

        if IS_ENVIRONMENT_CLOUD:
            return ai_response
        else:
            write_message("💾 Mixing the final results... almost done!")
            write_output_locally("result", str_utility.extract_playlist_id(playlist_link), ai_response)
            print("Finished the vibe check 🪄 check the generated file on your local directory to see the result")
            return ai_response

    except Exception as e:
        write_message("Oops! The vibe got disconnected. Let's try again with a different playlist or check later.")
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(1)
    else:
        playlist_link = sys.argv[1]
        ai_model_apikey = None

        if (len(sys.argv) > 2):
            ai_model_apikey = sys.argv[2]
            print("apikey from args")
        else:
            ai_model_apikey = GOOGLE_GENAI_APIKEY;
            print("apikey from env variable")

    main(playlist_link, ai_model_apikey)
