from dataclasses import dataclass


@dataclass(frozen=True)
class Generic:
    EMPTY_STRING: str = ""
    COMMA_STRING: str = ","
    WHITESPACE: str = " "


@dataclass(frozen=True)
class NetworkLogs:
    KEY_MESSAGE: str = 'message'
    KEY_BODY: str = 'body'
    KEY_POST_DATA: str = 'postData'
    KEY_METHOD: str = 'method'
    KEY_PARAMS: str = 'params'
    KEY_RESPONSE: str = 'response'
    KEY_REQUEST: str = 'request'
    KEY_REQUEST_ID: str = 'requestId'
    KEY_CHROME_LOG_PERFORMANCE: str = 'performance'


@dataclass(frozen=True)
class ChromeDevToolProtocol:
    NETWORK_REQUEST_WILL_BE_SENT: str = 'Network.requestWillBeSent'
    NETWORK_GET_RESPONSE_BODY: str = 'Network.getResponseBody'
    NETWORK_GET_REQUEST_POST_DATA: str = 'Network.getRequestPostData'


@dataclass(frozen=True)
class HttpMethod:
    POST: str = 'POST'


@dataclass(frozen=True)
class Spotify:
    KEY_OPERATION_NAME: str = 'operationName'
    KEY_PLAYLIST_V2: str = 'playlistV2'
    KEY_ITEM_V2: str = 'itemV2'
    KEY_NAME: str = 'name'
    KEY_ARTISTS: str = 'artists'
    KEY_CONTENT: str = 'content'
    KEY_ITEMS: str = 'items'
    KEY_DATA: str = 'data'
    KEY_PROFILE: str = 'profile'
    REQ_PARAM_FETCH_PLAYLIST_FIRST_PAGE: str = 'fetchPlaylist'
    REQ_PARAM_FETCH_PLAYLIST_NEXT_PAGE: str = 'fetchPlaylistContents'
    PLACEHOLDER_UNKNOWN_ARTIST: str = 'Unknown'


@dataclass(frozen=True)
class FileWriter:
    METHOD_TYPE_WRITE: str = 'w'
    ENCODING_UTF_8: str = 'utf-8'
