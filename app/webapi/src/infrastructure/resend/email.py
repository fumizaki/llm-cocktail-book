import os
from dotenv import load_dotenv
import resend

load_dotenv()

RESEND_API_KEY = os.environ.get('RESEND_API_KEY', '')
EMAIL_FROM_ADDRESS = os.environ.get('EMAIL_FROM_ADDRESS', '')


class ResendEmailClient:

    def __init__(self, api_key: str = RESEND_API_KEY) -> None:
        resend.api_key = api_key


    def send_mail(self, to_add: list[str], subject: str, message: str):
        params = {
            # "from": EMAIL_FROM_ADDRESS,
            "from": "Sending Test <onboarding@resend.dev>",
            "to": to_add,
            "subject": subject,
            "text": message,
        }

        result = resend.Emails.send(params)
        return