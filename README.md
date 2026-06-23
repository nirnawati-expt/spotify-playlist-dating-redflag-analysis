# **Project: Spotify Playlist "Dating Red Flag" Analysis**

-----

## **Summary: Integrating Data Scraping with Gen AI**

This is an end-to-end Python project that analyzes a user's Spotify playlist to generate an entertaining "dating red
flag" personality analysis.

This project represents the successful **MVP (Minimum Viable Product)** build, which was executed in seven days of
focused part-time work to quickly demonstrate core technical proficiency in Python.

The MVP's main objective was to validate a solid, production-ready data pipeline by:

- **Data Acquisition**: Grabbing songs from a public Spotify playlist using customized data scraping techniques (network
  traffic interception from Web UI).
- **GenAI Integration**: Leveraging the 3rd party API SDK to generate structured, nuanced text.
- **Prompt Engineering**: Crafting the personality analysis by designing an optimal prompt and system instructions to
  achieve the desired content goal.
- **Pipeline Engineering**: Implementing a complete data flow from unformatted scrape data to final, formatted output.

-----

## **Technology Stack**

- **Generative AI**: This demonstrates direct SDK integration and my skills in prompt engineering, using System
  Instructions, parameter configurations and specific prompt to ensure the output is structured, relevant and reliable.
- **Web Scraping (Selenium)**: This was a challenge! It showcases dynamic data acquisition by automating browser
  interaction and actively intercepting network calls, not just scraping static pages, whic is more technically
  challenging approach.
- **Python 3**: The entire data pipeline and application logic are built using modern Python 3.

-----

## Rationale: Why didn't I just use the Spotify API?

That's a great question! I know the easiest route would've been to grab the data using the official Spotify API, but I
intentionally decided against it.

This project is a first-time exploration into data acquisition. I wanted to challenge myself (and showcase my skills) by
using the Python Selenium library to perform dynamic scraping.

That means I set up the code to actively listen to and intercept network calls as the playlist web page loads.

It was a deliberate technical choice to demonstrate real-world skills in dynamic scraping and network traffic analysis
in Python, proving I can handle more than just standard API consumption.

-----

## **How It Works: The Flow**

This is the overall flow of the application:

```
Spotify Playlist ⟶ Data Scraping ⟶ Data Cleaning ⟶ AI Model ⟶ Analysis Output
```

1. The application is run with a single command-line argument: the URL of a public Spotify playlist.
2. **Selenium** takes over, automating the web browser to navigate to the URL.
3. The application listens to the network traffic and extracts a list of songs and artists from the web UI elements.
4. The extracted data, along with specific prompts and system instructions, is sent to the GenAI model.
5. The AI model, accessed via the Vertex AI API SDK, generates the personality analysis based on the provided data and
   instructions.
6. The final AI-generated response is saved as a Markdown file, with the filename automatically generated in the format
   `output_result-[spotify_playlist_id]-[yymmdd].md`.
    * **Example:** If the playlist URL is `https://open.spotify.com/playlist/7wARwuyCiPRMURGmh6xTLq`, and the analysis
      is run on December 31, 2025, the output file will be named `output_result-7wARwuyCiPRMURGmh6xTLq-251231.md`.

-----

## **Requirements**

You'll need a few things to get started:

* **Python 3** installed on your device
* **Google Vertex AI API Key and Authentication:** All required environment variables are listed in the
  `Environment Variables` section.
* **Python Modules:** All required modules are listed in the `requirements.txt` file.

-----

## **How to Run**

1. Navigate to the project directory in your terminal: `.../spotify-playlist-dating-redflag-analysis`.

2. Ensure you have gathered all of the requirements on section `Requirements`

3. **Run the Application as a Python Module**

If you have set the API key as an environment variable:

```
   python -m vibecheck.main <your_public_spotify_link>
```

If you want to pass your API key directly as an argument:

```
  python -m vibecheck.main <your_public_spotify_link> <your_google_cloud_ai_studio_api_key>
```

4. **Run Locally as a Pre-packaged Tool**
   Install the package in editable mode:

```
   pip install -e .
  ```

Once installed, run the tool using the following command:

```
  vibe-check <your_public_spotify_link> <your_google_cloud_ai_studio_api_key>
````

## **Project Structure**

* `.run/`: PyCharm run configuration files.
* `docs/`: Additional documentation. You can find samples of prompt, configurations, system instruction, and output
  files of this project.
* `vibecheck/`: The main Python package.
    * `constant/`: Modules holding constant classes and immutable variables.
    * `helper/`: Modules that support the project's core logic.
    * `model/`: Modules for data definition classes.
    * `sdk/`: Modules for implementing the 3rd party SDK and its configurations.
    * `web_scraper/`: Modules dedicated to dynamic data scraping.
* `tests/`: A package for unit tests.
    * ***Note:*** *Unit testing is planned for the future, after the Generative AI exploration is complete.*

-----

## **Configuration & Environment Variables**

This project relies on several environment variables for configuration. Here's a quick look at what they do:

```dotenv
GOOGLE_CLOUD_API_KEY=string. optional, if using 1 args on cli this is mandatory. API key, get yours from https://aistudio.google.com/app/api-keys
GOOGLE_GENAI_MODEL_TYPE=string. optional. gemini model id. if left empty, the default value is defined at noviirnawati/config/sdk_configuration.py 

GOOGLE_GENAI_SYSTEM_INSTRUCTION=string. optional. system instruction of ai model.
GOOGLE_GENAI_BASE_PROMPT=string. optional. prompt for the ai model to generate content.
GOOGLE_GENAI_TEMPERATURE=float. optional. learn from https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values . if left empty, the default value is defined at noviirnawati/config/sdk_configuration.py 
GOOGLE_GENAI_TOP_P=float. optional. learn from https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values . if left empty, the default value is defined at noviirnawati/config/sdk_configuration.py 
GOOGLE_GENAI_TOP_K=int. optional. learn from https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values . if left empty, the default value is defined at noviirnawati/config/sdk_configuration.py 

AI_ANALYSIS_SAVED_AS_MARKDOWN=bool. optional. true to save markdown of generated content into a markdown file locally. if left empty, the default value is False, defined at noviirnawati/config/base_configuration.py 
OUTPUT_FILENAME_API_DETAILS=string. optional. file name of which web data scraping result. file will be save as output_[file_name]-[spotify_playlist_id]-[yymmdd].json
OUTPUT_FILENAME_SONGS_DETAILS=string. optional. file name of which cleaned data result. file will be save as output_[file_name]-[spotify_playlist_id]-[yymmdd].json
SPOTIFY_PLAYLIST_UI_END_SCROLL_ELEMENT=string. optional. class of the element where the playlist end on the spotify web UI
```

A sample populated with example data types:

```dotenv
GOOGLE_CLOUD_API_KEY=API key, get yours from https://aistudio.google.com/app/api-keys
GOOGLE_GENAI_MODEL_TYPE=gemini-2.0-flash-001

GOOGLE_GENAI_SYSTEM_INSTRUCTION=You are a Relationship Pop Culture Analyst. Your primary function is to identify and objectively analyze potential behavioral or personality 'dating red flags' associated with a music listener, based solely on the lyrical themes, dominant mood, and artist personas present in the provided playlist data. Strict Output Rule: You MUST return your complete analysis with MARKDOWN format, with sections: Summary: A single paragraph high-level summary of the findings. Red Flags: Flag Category: e.g., Emotional Volatility, Commitment Avoidance, Materialism. Reasoning: A brief explanation of why this category was chosen, citing the lyrical themes or mood. Supporting Songs: Songs and artist to support the result
GOOGLE_GENAI_BASE_PROMPT=Perform a dating red flag analysis on the following music playlist. The playlist data is provided as a semicolon-separated list in the format (Song Title - Artist). Use the themes and moods of the songs to infer potential personality concerns. Strictly follow the MARKDOWN format defined in your instructions.
GOOGLE_GENAI_TEMPERATURE=0.7
GOOGLE_GENAI_TOP_P=0.6
GOOGLE_GENAI_TOP_K=30

AI_ANALYSIS_SAVED_AS_MARKDOWN=True
OUTPUT_FILENAME_API_DETAILS=api_details
OUTPUT_FILENAME_SONGS_DETAILS=songs_details
SPOTIFY_PLAYLIST_UI_END_SCROLL_ELEMENT=RD3ze5s5sQ4S4Tyb
```

-----

## **Future Roadmap (Post-MVP)**

The immediate roadmap focuses on transitioning the tool into a robust command-line interface (CLI) application and
expanding local data extraction capabilities using Selenium:

* **CLI Application Transformation**: Refactoring the entire script into an interactive CLI tool. Users will be able to
  pass playlist URLs and the AI model API key, and view the output directly in their terminal with clean text
  formatting.
* **Enhanced Local Data Cleaning & Processing**: enhancing the structured data cleaning and feature extraction locally
  before passing the payload to the GenAI model to keep tokens efficient.
* **Probably Trying New AI Voices**: Looking into other GenAI providers (especially those with a great free tier!) to
  see how their models analyze music and if we can get a different "vibe" for the analysis.
* **Deeper Data Scraping**: Expanding the Selenium scraping logic to capture more detailed metrics (such as Genre, BPM,
  and Mood) from the web interface's network traffic and DOM elements. More scraped data means the AI can give even
  spicier and more nuanced assessments!
* **Visualizing the Vibe**: Exploring suitable data visualization for the output file based on the collected playlist
  data.
* ```
  Spotify Playlist URL ⟶ Selenium Web Scraping ⟶ Local Data Cleaning & Feature Extraction ⟶ GenAI Model ⟶ Interactive CLI Output & Data Visualization
  ```
* Feature extraction might focus heavily on playlist-level insights, such as:
    * **Track Count**: Number of songs in a playlist.
    * **Era Preference**: Min (Oldest), Max (Latest), and Most Common Release Year.
    * **Duration Preference**: Min (Shortest), Max (Longest), and Average Song Duration.
    * **Artist Diversity**: Artist distribution and Top 3 Artists to see if the user is loyal to their favorites or
      explores
      widely.
    * **Genre Diversity**: Genre distribution and Top 3 Genres to see if the user has a comfort genre.
    * **Tempo & Energy**: BPM distribution and Top 3 BPM to see if the user prefers a faster or slower tempo.
    * **Mood Consistency**: Mood distribution and Top 3 Moods to see how consistent their musical moods are.

> [!NOTE]
> If these data points are available to scrape from Spotify's Web UI, I'll definitely try to integrate them.
> Otherwise, these ideas may become optional features should I decide to explore the Spotify API later on (which most
> likely I'll do in a separate repository).*