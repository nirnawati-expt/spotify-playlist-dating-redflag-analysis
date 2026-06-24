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

[see the sample result →](docs/sample-prompt-and-output-1/output_result-7wARwuyCiPRMURGmh6xTLq-250929.txt)

-----

## **Requirements**

You'll need a few things to get started:

* **Python 3** installed on your device
* **Google Vertex AI API Key and Authentication:** All required environment variables are listed in the
  `Environment Variables` section.
* **Python Modules:** All required modules are listed in the `requirements.txt` file.

-----

## 🚀 How to Run

### 1. Initial Setup

Before running the application, navigate to the project directory and ensure all prerequisites listed in the *
*Requirements** section are met.

```bash
# Navigate to the project directory
cd path/to/spotify-playlist-dating-redflag-analysis
```

### 2. Run the CLI Tool

You can execute the core CLI engine either directly as a Python Module or by installing it locally as a Pre-packaged
Tool.

#### Option A: Run as a Python Module

Use this method to run the script immediately without installing the package:

Passing the API Key Directly via Arguments:

```bash
  python -m vibecheck.main <your_public_spotify_link> <your_google_cloud_ai_studio_api_key>
```

Using Environment Variables (Ensure your API key is already set in your environment):

```bash
   python -m vibecheck.main <your_public_spotify_link>
```

#### Option B: Run Locally as a Pre-packaged Tool (Recommended)

Install the project in editable mode to register the custom terminal command:

```bash
   pip install -e .
```

Once installed, you can invoke the `vibe-check` command from any directory in your terminal:

Passing the API Key Directly via Arguments:

```bash
  vibe-check <your_public_spotify_link> <your_google_cloud_ai_studio_api_key>
```

Using Environment Variables:

```bash
  vibe-check <your_public_spotify_link>
```

### 3. Run the Streamlit Web Application
   To launch the interactive graphical user interface (GUI) wrapper in your web browser:

```bash
    streamlit run app.py
````

💡 Tip: Ensure you have configured your local .streamlit/secrets.toml file before running this command so that your API keys are automatically injected into the web UI.

[see the sample commands →](docs/sample-prompt-and-output-1/sample-command.txt)

[see the sample secrets.toml →](docs/sample-prompt-and-output-1/sample-secrets.toml.txt)

## **Project Structure**

```text
├── .streamlit/          # Streamlit configuration (local only, excluded from version control)
├── docs/                # Additional documentation (samples of prompts, commands, env variables, and outputs)
├── vibecheck/           # The core Python package (CLI Engine)
│   ├── constant/        # Configuration classes and immutable variables
│   ├── helper/          # Utility modules supporting the core business logic
│   ├── model/           # Data definition models and schemas
│   ├── sdk/             # 3rd-party SDK integrations and configurations
│   ├── web_scraper/     # Modules dedicated to dynamic web scraping
│   └── main.py          #  The central entry point for the CLI tool, responsible for parsing terminal arguments and executing the core application logic.
├── tests/               # Unit testing suite (Planned for future release)
├── app.py               # Streamlit Web Application entry point
├── packages.txt         # Linux system-level dependencies for Cloud Deployment (e.g., Streamlit Cloud)
├── pyproject.toml       # Build system configuration and package metadata
└── requirements.txt     # Python package dependencies (pip)
```

## **Configuration & Environment Variables**

This project relies on several environment variables for configuration. Here's a quick look at what they do:

```dotenv
GOOGLE_CLOUD_API_KEY=string. optional, if using 1 args on cli this is mandatory. API key, get yours from https://aistudio.google.com/app/api-keys
IS_ENVIRONMENT_CLOUD=bool. optional. default to false. set to true if you want to upload to cloud.

GOOGLE_GENAI_MODEL_TYPE=string. optional. gemini model id. if left empty, the default value is defined at noviirnawati/config/sdk_configuration.py 
GOOGLE_GENAI_SYSTEM_INSTRUCTION=string. optional. system instruction of ai model.
GOOGLE_GENAI_BASE_PROMPT=string. optional. prompt for the ai model to generate content.
GOOGLE_GENAI_TEMPERATURE=float. optional. learn from https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values . if left empty, the default value is defined at noviirnawati/config/sdk_configuration.py 
GOOGLE_GENAI_TOP_P=float. optional. learn from https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values . if left empty, the default value is defined at noviirnawati/config/sdk_configuration.py 
GOOGLE_GENAI_TOP_K=int. optional. learn from https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values . if left empty, the default value is defined at noviirnawati/config/sdk_configuration.py 

OUTPUT_FILENAME_API_DETAILS=string. optional. file name of which web data scraping result. file will be save as output_[file_name]-[spotify_playlist_id]-[yymmdd].json. fill it only for debugging in local environment
OUTPUT_FILENAME_SONGS_DETAILS=string. optional. file name of which cleaned data result. file will be save as output_[file_name]-[spotify_playlist_id]-[yymmdd].json. fill it only for debugging in local environment

SPOTIFY_PLAYLIST_UI_END_SCROLL_ELEMENT=string. optional. class of the element where the playlist end on the spotify web UI
```

A [sample](docs/sample-prompt-and-output-1/sample-.env.txt) populated with example data types:

```dotenv
GOOGLE_CLOUD_API_KEY=API key, get yours from https://aistudio.google.com/app/api-keys
IS_ENVIRONMENT_CLOUD=FALSE

GOOGLE_GENAI_MODEL_TYPE=gemini-2.0-flash-001
GOOGLE_GENAI_SYSTEM_INSTRUCTION=You are a Relationship Pop Culture Analyst. Your primary function is to identify and objectively analyze potential behavioral or personality 'dating red flags' associated with a music listener, based solely on the lyrical themes, dominant mood, and artist personas present in the provided playlist data. Strict Output Rule: You MUST return your complete analysis with MARKDOWN format, with sections: Summary: A single paragraph high-level summary of the findings. Red Flags: Flag Category: e.g., Emotional Volatility, Commitment Avoidance, Materialism. Reasoning: A brief explanation of why this category was chosen, citing the lyrical themes or mood. Supporting Songs: Songs and artist to support the result
GOOGLE_GENAI_BASE_PROMPT=Perform a dating red flag analysis on the following music playlist. The playlist data is provided as a semicolon-separated list in the format (Song Title - Artist). Use the themes and moods of the songs to infer potential personality concerns. Strictly follow the MARKDOWN format defined in your instructions.
GOOGLE_GENAI_TEMPERATURE=0.7
GOOGLE_GENAI_TOP_P=0.6
GOOGLE_GENAI_TOP_K=30

OUTPUT_FILENAME_API_DETAILS=api_details
OUTPUT_FILENAME_SONGS_DETAILS=songs_details

SPOTIFY_PLAYLIST_UI_END_SCROLL_ELEMENT=RD3ze5s5sQ4S4Tyb
```

[see the sample .env →](docs/sample-prompt-and-output-1/sample-.env.toml.txt)


-----

## **Future Roadmap (Post-MVP)**

The immediate roadmap focuses on transitioning the tool into a robust command-line interface (CLI) application and
expanding local data extraction capabilities using Selenium:

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