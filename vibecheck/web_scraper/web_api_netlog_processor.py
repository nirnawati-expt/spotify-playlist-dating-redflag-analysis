import json
from json import JSONDecodeError

from selenium import webdriver
from selenium.common import WebDriverException

from ..config.base_configuration import (OUTPUT_FILENAME_SONGS_DETAILS, OUTPUT_FILENAME_API_DETAILS,
                                         DATA_SCRAPING_SAVE_API_DETAILS, DATA_SCRAPING_SAVE_SONGS_DETAILS)
from ..constant.constant import (ChromeDevToolProtocol as CDP,
                                 Generic,
                                 HttpMethod,
                                 NetworkLogs as CONSTANT,
                                 Spotify)
from ..helper.validator import str_is_empty_or_none, dct_is_empty_or_none
from ..helper.writer import write_output_to_json
from ..model.model import PlaylistItem


def get_response_body(driver: webdriver.Chrome, request_id: str):
    try:
        return driver.execute_cdp_cmd(CDP.NETWORK_GET_RESPONSE_BODY,
                                      {CONSTANT.KEY_REQUEST_ID: request_id}).get(
            CONSTANT.KEY_BODY, {})
    except WebDriverException:
        return None


def get_request_body(driver: webdriver.Chrome, request_id: str):
    try:
        return driver.execute_cdp_cmd(CDP.NETWORK_GET_REQUEST_POST_DATA,
                                      {CONSTANT.KEY_REQUEST_ID: request_id}).get(
            CONSTANT.KEY_POST_DATA, {})
    except WebDriverException:
        return None


def get_dict_from_dict_default_empty(dictionary: dict, key: str) -> dict:
    return dictionary.get(key, {})


def operation_name_is_allowed(operation_name: str) -> bool:
    return (operation_name != Spotify.REQ_PARAM_FETCH_PLAYLIST_FIRST_PAGE
            and operation_name != Spotify.REQ_PARAM_FETCH_PLAYLIST_NEXT_PAGE)


def process_artists_names(artists: list[dict]) -> str:
    if len(artists) == 0:
        return 'Unknown'

    names = ''
    for artist in artists:
        name = artist.get(Spotify.KEY_PROFILE, {}).get(Spotify.KEY_NAME, Generic.EMPTY_STRING)
        if str_is_empty_or_none(name): continue
        names += name
        names += Generic.COMMA_STRING
        names += Generic.WHITESPACE

    names = names.rstrip(Generic.COMMA_STRING + Generic.WHITESPACE)
    return names


def filter_playlist_items(filtered_network_logs: list[dict], playlist_id: str) -> list[PlaylistItem]:
    song_details = []
    for log in filtered_network_logs:
        items = (log
                 .get(CONSTANT.KEY_RESPONSE, {})
                 .get(Spotify.KEY_DATA, {})
                 .get(Spotify.KEY_PLAYLIST_V2, {})
                 .get(Spotify.KEY_CONTENT, {})
                 .get(Spotify.KEY_ITEMS, []))
        if len(items) > 0:
            for item in items:
                detail = item.get(Spotify.KEY_ITEM_V2, {}).get(Spotify.KEY_DATA, {})
                title = detail.get(Spotify.KEY_NAME, Generic.EMPTY_STRING)
                artists = detail.get(Spotify.KEY_ARTISTS, {}).get(Spotify.KEY_ITEMS, [])
                song_details.append(PlaylistItem(title, process_artists_names(artists)))

            if DATA_SCRAPING_SAVE_SONGS_DETAILS:
                write_output_to_json(OUTPUT_FILENAME_SONGS_DETAILS, playlist_id,
                                     json.dumps(song_details, default=lambda o: o.encode()))
        else:
            print("items is empty")

    return song_details


def filter_network_logs(driver: webdriver.Chrome, playlist_id: str) -> list[dict]:
    # Fets all the logs from performance in Chrome
    log_entries = driver.get_log(CONSTANT.KEY_CHROME_LOG_PERFORMANCE)

    datas = "["
    for log_entry in log_entries:
        message_data = json.loads(log_entry[CONSTANT.KEY_MESSAGE])[CONSTANT.KEY_MESSAGE]

        if message_data.get(CONSTANT.KEY_METHOD,
                            Generic.EMPTY_STRING) != CDP.NETWORK_REQUEST_WILL_BE_SENT: continue

        params = message_data.get(CONSTANT.KEY_PARAMS, {})

        request_id = params.get(CONSTANT.KEY_REQUEST_ID, Generic.EMPTY_STRING)
        if str_is_empty_or_none(request_id): continue

        http_method = params.get(CONSTANT.KEY_REQUEST, {}).get(CONSTANT.KEY_METHOD, Generic.EMPTY_STRING)
        if http_method != HttpMethod.POST: continue

        try:
            net_request_body = get_request_body(driver, request_id)
            if dct_is_empty_or_none(net_request_body): continue

            request_body = json.loads(net_request_body)

            if operation_name_is_allowed(
                    request_body.get(Spotify.KEY_OPERATION_NAME, Generic.EMPTY_STRING)): continue

            net_response_body = get_response_body(driver, request_id)
            if dct_is_empty_or_none(net_response_body): continue

            response_body = json.loads(net_response_body)

            generated_json = {CONSTANT.KEY_REQUEST: request_body, CONSTANT.KEY_RESPONSE: response_body}
            datas += (json.dumps(generated_json) + Generic.COMMA_STRING)

        except JSONDecodeError:
            continue

    datas = datas.rstrip(Generic.COMMA_STRING)
    datas += "]"

    if DATA_SCRAPING_SAVE_API_DETAILS:
        write_output_to_json(OUTPUT_FILENAME_API_DETAILS, playlist_id, datas)

    return json.loads(datas)


def process_network_logs(driver: webdriver.Chrome, playlist_id: str) -> list[PlaylistItem]:
    # Filter only relevant traffic from network logs
    filtered_logs = filter_network_logs(driver, playlist_id)

    # Filter so you only get the song and
    final_result = filter_playlist_items(filtered_logs, playlist_id)
    return final_result
