import os
from dotenv import load_dotenv
from stripe import StripeClient as StripeAPIClient

load_dotenv()

STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY', '')
STRIPE_ENDPOINT_SECRET = os.environ.get("STRIPE_ENDPOINT_SECRET", '')

class StripeClient:
    def __init__(self) -> None:
        self.client = StripeAPIClient(STRIPE_SECRET_KEY)
        self.endpoint_secret = STRIPE_ENDPOINT_SECRET

'''
# URLs  
# https://docs.stripe.com/
# https://docs.stripe.com/api
# https://qiita.com/organizations/stripe
'''