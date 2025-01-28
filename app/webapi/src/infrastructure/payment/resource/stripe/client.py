from typing import Optional
import os
from dotenv import load_dotenv
from stripe import StripeClient as StripeAPIClient

load_dotenv()

STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY', '')

class StripeClient:
    def __init__(self) -> None:
        self.client = StripeAPIClient(STRIPE_SECRET_KEY)

'''
# URLs  
# https://docs.stripe.com/
# https://docs.stripe.com/api
# https://docs.stripe.com/payments/quickstart
# https://docs.stripe.com/payments/accept-a-payment?=&ui=elements
# https://qiita.com/organizations/stripe
'''