import json


class PlaylistItem:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def to_dict(self):
        return {"title": self.title, "artist": self.artist}

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def encode(self):
        return self.__dict__
