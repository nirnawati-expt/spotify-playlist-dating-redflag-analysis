def extract_playlist_id(url: str) -> str:
    splitted_url = url.split("/")
    return splitted_url[len(splitted_url) - 1]
