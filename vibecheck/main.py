# load .env file in /env directory
import logging
import os
from datetime import date
from turtle import st

from dotenv import load_dotenv, find_dotenv

from vibecheck.config.base_configuration import IS_ENVIRONMENT_CLOUD
from vibecheck.config.sdk_configuration import GOOGLE_GENAI_APIKEY
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


def main():
    try:
        playlist_link = sys.argv[1]
        ai_model_apikey = None

        if (len(sys.argv) > 2):
            ai_model_apikey = sys.argv[2]
        else:
            ai_model_apikey = GOOGLE_GENAI_APIKEY;

        validator.validate_args(playlist_link, ai_model_apikey)

        songs_collection = scrape_spotify_playlist_page(playlist_link)
        ai_response = ai_analysis(songs_collection, playlist_link, ai_model_apikey)

        filename = "output-" + str_utility.extract_playlist_id("") + "-" + date.today().strftime("%y%m%d") + ".md"

        print("Writing to responses")

        if IS_ENVIRONMENT_CLOUD:
            st.download_button(
                label="📥 Download",
                data=ai_response,
                file_name=filename,
                mime="text/txt"
            )
            print("Finished the vibe check 🪄 download the generated file to see the result")
        else:
            write_output_locally("result", str_utility.extract_playlist_id(playlist_link), ai_response)
            print("Finished the vibe check 🪄 check the generated file on your local directory to see the result")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
