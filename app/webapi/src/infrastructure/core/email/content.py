import os
from dotenv import load_dotenv
from enum import Enum
from pydantic import BaseModel

load_dotenv()

API_BASE_URL = os.environ.get('API_BASE_URL', "http://localhost:8000")

class MessageType(str, Enum):
    TEXT = 'text'
    HTML = 'html'

class EmailContent(BaseModel):
    subject: str
    message_type: str
    message: str


def build_signup_request_content(key: str) -> EmailContent:
    subject=f"Verify your account"
    message = f"""
Verify your email to sign up for App

We have received a sign-up request from you.

to complete the sign-up process; visit the link below to open the confirmination page in a new window or device:

{API_BASE_URL}/oauth/signup/verify?key={key}

please note that by completing your sign-up you are agreeing to our Terms of Service and Privacy Policy:

"""


    return EmailContent(
        subject=subject,
        message_type=MessageType.TEXT,
        message=message
    )