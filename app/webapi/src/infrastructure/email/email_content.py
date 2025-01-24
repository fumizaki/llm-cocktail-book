import os
from dotenv import load_dotenv
from enum import Enum
from pydantic import BaseModel

class MessageType(str, Enum):
    TEXT = 'text'
    HTML = 'html'

class EmailContent(BaseModel):
    subject: str
    message_type: str
    message: str

load_dotenv()

VIEW_BASE_URL = os.environ.get('VIEW_BASE_URL', "http://localhost:3000")


def build_signup_request_content(key: str) -> EmailContent:
    subject = f"Verify Your Account"
    message = f"""
Verify your email to sign up for App

We have received a sign-up request from you.

to complete the sign-up process; visit the link below to open the confirmination page in a new window or device:

{VIEW_BASE_URL}/auth/signup/verify?key={key}

please note that by completing your sign-up you are agreeing to our Terms of Service and Privacy Policy:

"""


    return EmailContent(
        subject=subject,
        message_type=MessageType.TEXT,
        message=message
    )


def build_update_password_content() -> EmailContent:
    subject = f"Notice of Password Change"
    message = f"""
Notice of password change 
"""

    return EmailContent(
        subject=subject,
        message_type=MessageType.TEXT,
        message=message
    )