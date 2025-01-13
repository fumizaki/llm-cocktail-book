import os
from dotenv import load_dotenv
from google import generativeai as GoogleAI

load_dotenv()

GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY', '')


class GoogleAICoreClient:

    def __init__(self, api_key: str = GOOGLE_API_KEY) -> None:
        GoogleAI.configure(api_key=api_key)
        self.client = GoogleAI

