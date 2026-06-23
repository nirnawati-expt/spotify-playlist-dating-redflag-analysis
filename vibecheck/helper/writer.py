import os
from datetime import date

from ..constant.constant import (FileWriter)


def write_output_to_json(filename: str, playlist_id: str, json_string: str) -> None:
    with (open(os.path.join("output_" + filename + "-" + playlist_id + "-" + date.today().strftime("%y%m%d") + ".json"),
               FileWriter.METHOD_TYPE_WRITE,
               encoding=FileWriter.ENCODING_UTF_8) as file):
        file.write(json_string)


def write_output_to_markdown(filename: str, playlist_id: str, string: str) -> None:
    with (open(os.path.join("output_" + filename + "-" + playlist_id + "-" + date.today().strftime("%y%m%d") + ".md"),
               FileWriter.METHOD_TYPE_WRITE,
               encoding=FileWriter.ENCODING_UTF_8) as file):
        file.write(string)
