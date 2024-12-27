import os
from dotenv import load_dotenv
from .model import MessageType, EmailContent


load_dotenv()

API_BASE_URL = os.environ.get('API_BASE_URL', "http://localhost:8000")


def build_signup_request_content(key: str) -> EmailContent:
    subject = f"Verify Your Account"
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