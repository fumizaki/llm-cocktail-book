import os
from dotenv import load_dotenv

load_dotenv()

ISSUER: str = os.getenv('OAUTH2_ISSUER', '')
AUDIENCE: str = os.getenv('OAUTH2_AUDIENCE', '')
ALGORITHM: str = os.getenv('OAUTH2_ALGORITHM', '')
TOKEN_SECRET: str = os.getenv('OAUTH2_TOKEN_SECRET', '')
