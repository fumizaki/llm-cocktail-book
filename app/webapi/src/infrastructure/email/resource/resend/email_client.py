import os
from dotenv import load_dotenv
import resend
from ...email_client import EmailClient
from .email_exception import ResendEmailError
from .email_model import ResendEmailModel, ResendEmailResult

load_dotenv()

RESEND_API_KEY = os.environ.get('RESEND_API_KEY', '')
EMAIL_FROM_ADDRESS = os.environ.get('EMAIL_FROM_ADDRESS', '')


class ResendEmailClient(EmailClient):

    def __init__(self, api_key: str = RESEND_API_KEY) -> None:
        resend.api_key = api_key


    def send(self, params: ResendEmailModel) -> ResendEmailResult:
        try:
            p = {
                # "from": EMAIL_FROM_ADDRESS,
                "from": "Sending Test <onboarding@resend.dev>",
                "to": params.to,
                "subject": params.subject,
                "text": params.message,
            }

            result = resend.Emails.send(p)
            return ResendEmailResult(
                id=result.id
            )
            
        except Exception as e:
            raise ResendEmailError(f"Invalid response from Resend API: {e}")
