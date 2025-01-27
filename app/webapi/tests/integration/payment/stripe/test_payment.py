import pytest
from src.infrastructure.payment.resource import StripePaymentClient, StripePaymentError, StripeCheckoutSessionModel, StripeCheckoutLineItem, StripeCheckoutSessionResult


@pytest.fixture
def sample_checkout_params():
    return StripeCheckoutSessionModel(
        currency='usd',
        line_items=[
            StripeCheckoutLineItem(
                amount=1000,
                title='Test Product',
                quantity=1
            )
        ]
    )

@pytest.fixture
def client():
    return StripePaymentClient()

def test_create_checkout_session_success(
    sample_checkout_params, 
    client
):
    # Act
    result = client.create_checkout_session(sample_checkout_params)
    print(result)
    # Assert
    assert isinstance(result, StripeCheckoutSessionResult)
    assert result.session_id == 'test_session_id'
    assert result.checkout_url == 'https://checkout.stripe.com/test'
    assert result.status == 'open'
        
        

def test_create_checkout_session_multiple_items(
    client
):
    # Arrange
    multi_item_params = StripeCheckoutSessionModel(
        currency='usd',
        line_items=[
            StripeCheckoutLineItem(amount=1000, title='Product 1', quantity=2),
            StripeCheckoutLineItem(amount=2000, title='Product 2', quantity=1)
        ]
    )
    
    # Act
    result = client.create_checkout_session(multi_item_params)
    print(result)
    # Assert
    assert result.session_id == 'test_session_id'
    