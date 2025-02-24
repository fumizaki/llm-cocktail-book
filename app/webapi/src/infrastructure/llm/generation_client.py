import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')
ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY', '')
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY', '')

class GenerationClient:
    
    def __init__(self) -> None:
        self._openai_api_key = OPENAI_API_KEY
        self._anthropic_api_key = ANTHROPIC_API_KEY
        self._google_api_key = GOOGLE_API_KEY

