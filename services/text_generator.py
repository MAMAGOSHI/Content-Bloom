import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


# Load the .env file

load_dotenv()


# Get Gemini API key

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY"
)


# Create Gemini client

if GEMINI_API_KEY:

    client = genai.Client(
        api_key=GEMINI_API_KEY
    )

else:

    client = None


# Gemini model

MODEL = "gemini-3.1-flash-lite"


def generate_text(prompt):

    """
    Sends a prompt to Gemini
    and returns the generated text.
    """

    if client is None:

        raise ValueError(
            "GEMINI_API_KEY was not found."
        )


    response = client.models.generate_content(

        model=MODEL,

        contents=prompt,

        config=types.GenerateContentConfig(

            max_output_tokens=500,

            temperature=0.7

        )
    )


    return response.text