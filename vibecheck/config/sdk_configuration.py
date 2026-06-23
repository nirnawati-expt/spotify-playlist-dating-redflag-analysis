import os

from google.genai.types import SafetySetting, HarmCategory, HarmBlockThreshold

# Gen AI Client
GOOGLE_GENAI_MODEL_TYPE: str = os.getenv('GOOGLE_GENAI_MODEL_TYPE', 'models/gemini-3-flash-preview')

# Gen AI Generate Content Parameters
GOOGLE_GENAI_BASE_PROMPT: str = os.getenv('GOOGLE_GENAI_BASE_PROMPT',
                                          'Perform a dating red flag analysis on the following music playlist.'
                                          '\nThe playlist data is provided as a semicolon-separated list in the format: Song Title - Artist. '
                                          '\nUse the themes and moods of the songs to infer potential personality concerns.'
                                          '\nStrictly follow the MARKDOWN format defined in your instructions.')
GOOGLE_GENAI_SYSTEM_INSTRUCTION: str = os.getenv('GOOGLE_GENAI_SYSTEM_INSTRUCTION',
                                                 "You are a Gen-Z Relationship Pop Culture Analyst."
                                                 "\nYour primary function is to identify and objectively analyze potential behavioral or personality 'dating red flags', associated with a music listener, based solely on the lyrical themes, dominant mood, and artist personas present in the provided playlist data."
                                                 "\nStrict Output Rule: You MUST return your complete analysis with MARKDOWN format, with sections:"
                                                 "\n- Summary (Paragraphs of of the findings, present it as if you are a content creator focus on pop culture psychology)."
                                                 "\n- List of Red Flags, which each item consist of:"
                                                 "\n  - Red Flag Name e.g., Emotional Volatility, Commitment Avoidance, Materialism, etc."
                                                 "\n  - A brief explanation of why the red flag was chosen, citing the lyrical themes or mood"
                                                 "\n  - Songs and artist to support the result."
                                                 "\nOnly list red flags if it coming from > 10% of the songs count of the playlist."
                                                 "\nAdd emojis into your response to bring the vibes of generated content."
                                                 "\nRefer some trendy pop-culture and trending phrases if suitable."
                                                 "\nYou also can emphasize your result by make the text bold or italic on the parts that you want to emphasize."
                                                 "\nMake sure you always mention that the result is just for fun and not for actual psychological screening in the end of your generated content.")
GOOGLE_GENAI_TEMPERATURE: float = os.getenv('GOOGLE_GENAI_TEMPERATURE', 1.0)
GOOGLE_GENAI_TOP_P: float = os.getenv('GOOGLE_GENAI_TOP_P', 0.8)
GOOGLE_GENAI_TOP_K: int = os.getenv('GOOGLE_GENAI_TOP_K', 30)
GOOGLE_GENAI_SAFETY_SETTINGS: list[SafetySetting] = [
    SafetySetting(
        category=HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    ),
    SafetySetting(
        category=HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    ),
    SafetySetting(
        category=HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    ),
    SafetySetting(
        category=HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    ),
]

if len(GOOGLE_GENAI_BASE_PROMPT) < 50:
    raise EnvironmentError('Environment variable GOOGLE_GENAI_BASE_PROMPT must be provided')
if len(GOOGLE_GENAI_SYSTEM_INSTRUCTION) < 50:
    raise EnvironmentError('Environment variable GOOGLE_GENAI_SYSTEM_INSTRUCTION must be provided')
