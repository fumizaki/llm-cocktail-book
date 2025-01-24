import os
from dotenv import load_dotenv
from typing import Optional
from stripe import StripeClient as StripeAPIClient

load_dotenv()

STRIPE_API_KEY = os.environ.get('STRIPE_API_KEY', '')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY', '')

class StripeClient:
    def __init__(self, api_key: Optional[str] = STRIPE_API_KEY) -> None:
        self.client = StripeAPIClient(api_key)


# URLs
# https://docs.stripe.com/
# https://docs.stripe.com/api
# https://qiita.com/organizations/stripe