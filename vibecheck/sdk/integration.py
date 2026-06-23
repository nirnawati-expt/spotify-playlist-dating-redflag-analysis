import os.path
import sys
import traceback

from google import genai
from google.genai import Client
from google.genai.types import GenerateContentConfig, GenerateContentResponse

from ..config.base_configuration import AI_ANALYSIS_SAVED_AS_MARKDOWN
from ..config.sdk_configuration import (GOOGLE_GENAI_MODEL_TYPE,
                                        GOOGLE_GENAI_BASE_PROMPT,
                                        GOOGLE_GENAI_SYSTEM_INSTRUCTION,
                                        GOOGLE_GENAI_TEMPERATURE,
                                        GOOGLE_GENAI_TOP_K,
                                        GOOGLE_GENAI_TOP_P,
                                        GOOGLE_GENAI_SAFETY_SETTINGS)
from ..constant.constant import Generic
from ..helper import str_utility
from ..helper.validator import str_is_empty_or_none
from ..helper.writer import write_output_to_markdown
from ..model.model import PlaylistItem


def build_prompt(songs_collections: list[PlaylistItem]) -> str:
    if len(songs_collections) == 0: return Generic.EMPTY_STRING
    prompt = "Playlist Data (Semicolon-separated list: Song Title - Artist; Song Title - Artist, ...):"

    for song in songs_collections:
        prompt += Generic.WHITESPACE
        prompt += song.title
        prompt += " - "
        prompt += song.artist
        prompt += ";"

    return prompt


def construct_markdown_filename(url: str) -> str:
    return os.path.join("output_result-" + str_utility.extract_playlist_id(url))


def ai_analysis_google(prompt_context: str, apikey: str) -> str:
    print("Generate GenAI Client")
    client: Client = genai.Client(api_key=apikey)
    print("Begin generating content")
    response: GenerateContentResponse = client.models.generate_content(
        model=GOOGLE_GENAI_MODEL_TYPE,
        contents=[GOOGLE_GENAI_BASE_PROMPT, prompt_context],
        config=GenerateContentConfig(
            system_instruction=GOOGLE_GENAI_SYSTEM_INSTRUCTION,
            temperature=GOOGLE_GENAI_TEMPERATURE,
            top_p=GOOGLE_GENAI_TOP_P,
            top_k=GOOGLE_GENAI_TOP_K,
            safety_settings=GOOGLE_GENAI_SAFETY_SETTINGS
        ))
    print("Finished generating content")
    client.close()
    print("Closing GenAI Client")
    return response.text


def ai_analysis(song_collections: list, url: str, apikey: str):
    try:
        print("Preparing Prompt")
        prompt_context = build_prompt(song_collections)
        if str_is_empty_or_none(prompt_context): raise ValueError(
            "Failed to build the prompt because playlist data could not be retrieved.")

        # OPTIONAL: try multiple SDK provider besides google, create a switch case, choose the provider based on the environment variable
        response = ai_analysis_google(prompt_context, apikey)
        print(response)
        # save as markdown only if the environment variables say so
        if AI_ANALYSIS_SAVED_AS_MARKDOWN:
            print("Writing to Markdown")
            write_output_to_markdown("result", str_utility.extract_playlist_id(url), response)
            print("Finished the vibe check 🪄 check the generated files on your directory now")
        return response

    except Exception as e:
        print("No Result, please try again later or try again with a different URL")
        raise e
