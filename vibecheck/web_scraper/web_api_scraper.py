import os
import time

from selenium import webdriver
from selenium.common import ElementNotInteractableException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service

from .web_api_netlog_processor import process_network_logs
from ..helper import str_utility


def get_chromedriver():
    # Create the webdriver object and pass the arguments
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')  # disable this argument to show the Chrome browser UI
    options.add_argument("--ignore-certificate-errors")
    options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
    options.add_argument('--disable-gpu')  # Mematikan akselerasi grafis yang sering memicu log devtools
    options.add_argument('--log-level=3')  # 3 = INFO, WARNING, dan ERROR disembunyikan
    options.add_argument('--silent')
    options.add_argument(
        '--disable-features=OptimizationGuideModelDownloading,OptimizationHints')  # Minta Chrome untuk tidak memuat model ML internal jika memungkinkan
    options.add_argument(f"--log-path={os.devnull}")  # force chrome to sent the log to os.devnull
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # Startup the chrome webdriver
    # pass the chrome options as parameters.
    return webdriver.Chrome(service=Service(log_output=None), options=options)


def scroll_down_element_until_end(driver: webdriver.Chrome, by: str, element_name: str):
    try:
        print("Scrolling down the playlist page")
        (ActionChains(driver)
         .click(driver.find_element(by=by, value=element_name))
         .perform())
        time.sleep(1)
        # note: the scrolling is working visually but the browser won't load the desired API
        # unlike when performing scroll manually
        # next maybe we are going to try to scroll using JS driver !TODO!
        (ActionChains(driver)
         .send_keys(Keys.END)
         .perform())
        time.sleep(15)  # sleep to ensure the page loaded (we never knew when the page is loaded though)
    except ElementNotInteractableException:
        # pass through exception can't send keys
        pass
    finally:
        print("Finished scrolling down the playlist page")


def scrape_spotify_playlist_page(playlist_url: str):
        # Set up the Web Driver
        driver = get_chromedriver()

        # Load the page
        print("Loading the web page")
        driver.get(playlist_url)
        time.sleep(15)  # to ensure the page is fully loaded, esp when the internet connection is slow
        print("Finished loading the web page")

        # commented due to token optimization (to process less data) - Scroll until recommended track section show to ensure all URL is loaded
        # scroll_down_element_until_end(driver, By.CLASS_NAME, SPOTIFY_PLAYLIST_UI_END_SCROLL_ELEMENT)

        print("Extracting playlists")
        playlist_id: str = str_utility.extract_playlist_id(playlist_url)
        # Filter data from API, this approach chosen because there are no identifier in UI
        print("Extracting songs")
        song_collections = process_network_logs(driver, playlist_id)
        driver.quit()
        return song_collections
